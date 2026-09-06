"""单步推进接口：每次推进一个演示单元（样本量 n 递增）。

DemoState 保存当前演示的全部状态，供界面逐帧读取绘图。
core 层零界面依赖，可在无界面环境单独运行（见文件末尾 __main__）。
"""
from __future__ import annotations

import numpy as np

from .model import DISTS, Distribution, sample_means, theoretical_normal

# 直方图分箱数（固定，便于不同 n 之间对比形状）
N_BINS = 40


class DemoState:
    """一次演示的全部状态：总体分布 + 样本量 n + 抽样组数 trials + 样本均值分布。"""

    def __init__(self, dist_name: str, n: int = 1, trials: int = 1000, seed: int = 42):
        self.dist_name = dist_name
        self.dist: Distribution = DISTS[dist_name]
        self.n = max(1, int(n))
        self.trials = max(10, int(trials))
        self.seed = int(seed)
        self._recompute()

    # -- 单步推进 ----------------------------------------------------------
    def step(self, delta: int = 1) -> "DemoState":
        """推进 delta 个样本量单元，返回自身（便于链式调用）。"""
        self.n = max(1, self.n + delta)
        self._recompute()
        return self

    def set_n(self, n: int) -> "DemoState":
        self.n = max(1, int(n))
        self._recompute()
        return self

    # -- 计算 --------------------------------------------------------------
    def _recompute(self) -> None:
        self.means = sample_means(self.dist, self.n, self.trials, self.seed)
        self.sample_mean = float(self.means.mean())
        self.sample_std = float(self.means.std(ddof=1)) if self.trials > 1 else 0.0
        # 理论真值（解析）：X̄ ≈ N(μ, σ²/n)
        self.theo_mean = self.dist.mean
        self.theo_std = self.dist.std / np.sqrt(self.n)
        # 直方图范围（以理论均值 ± 4 倍理论标准差为界，稳定画布）
        lo = self.theo_mean - 4.0 * self.theo_std
        hi = self.theo_mean + 4.0 * self.theo_std
        if hi - lo < 1e-12:
            lo, hi = self.sample_mean - 1.0, self.sample_mean + 1.0
        self.bin_edges = np.linspace(lo, hi, N_BINS + 1)
        self.hist, _ = np.histogram(self.means, bins=self.bin_edges, density=True)
        self.bin_centers = (self.bin_edges[:-1] + self.bin_edges[1:]) / 2.0
        # 理论正态密度曲线（解析真值，用于对照）
        self.norm_x = np.linspace(lo, hi, 200)
        self.norm_y = theoretical_normal(self.dist, self.n, self.norm_x)


if __name__ == "__main__":
    # 无界面环境验证：每个分布推进若干步，打印样本均值/方差 vs 理论真值。
    # 运行方式（从工具根目录）：python -m core.step
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    for name in DISTS:
        s = DemoState(name, 1, 2000, 42)
        for _ in range(5):
            s.step(10)
        print(
            f"{name:16s} n={s.n:3d}  样本均值={s.sample_mean:.4f}(理论{s.theo_mean:.4f})"
            f"  样本标准差={s.sample_std:.4f}(理论{s.theo_std:.4f})"
        )
