"""中心极限定理演示 — 领域核心（纯逻辑，零界面依赖）。

本模块只定义：总体分布库、抽样 → 样本均值、以及理论正态近似。
不 import 任何 UI 模块；界面层调用本模块，本模块不反向依赖界面。
"""
from __future__ import annotations

import numpy as np


class Distribution:
    """一个可演示的总体分布及其 CLT 理论参数。

    mean / var 为总体真值（解析值），用于对照样本均值/方差（数值真值）。
    """

    def __init__(self, name, formula, sampler, mean, var):
        self.name = name
        self.formula = formula          # LaTeX 表达式（UI 展示用，不带 $ 定界符）
        self.sampler = sampler          # sampler(rng, n) -> 长度为 n 的样本
        self.mean = float(mean)         # 总体均值 μ（解析真值）
        self.var = float(var)           # 总体方差 σ²（解析真值）

    @property
    def std(self) -> float:
        return float(np.sqrt(self.var))


def _uniform(rng, n):
    return rng.uniform(0.0, 1.0, n)


def _exponential(rng, n):
    return rng.exponential(1.0, n)


def _binomial(rng, n):
    return rng.binomial(10, 0.3, n)


DISTS = {
    "均匀分布 U(0,1)": Distribution(
        "均匀分布 U(0,1)",
        r"X\sim U(0,1),\ \mu=\tfrac12,\ \sigma^2=\tfrac1{12}",
        _uniform,
        mean=0.5,
        var=1.0 / 12.0,
    ),
    "指数分布 Exp(1)": Distribution(
        "指数分布 Exp(1)",
        r"X\sim \mathrm{Exp}(1),\ \mu=1,\ \sigma^2=1",
        _exponential,
        mean=1.0,
        var=1.0,
    ),
    "二项分布 B(10,0.3)": Distribution(
        "二项分布 B(10,0.3)",
        r"X\sim B(10,0.3),\ \mu=3,\ \sigma^2=2.1",
        _binomial,
        mean=3.0,
        var=10.0 * 0.3 * 0.7,
    ),
}


def sample_means(dist: Distribution, n: int, trials: int, seed: int | None = None) -> np.ndarray:
    """从 dist 抽样 trials 组，每组 n 个，返回每组样本均值（长度 trials）。

    可复现：固定 seed 两次运行结果一致。
    """
    rng = np.random.default_rng(seed)
    return np.array([dist.sampler(rng, n).mean() for _ in range(trials)])


def theoretical_normal(dist: Distribution, n: int, xs: np.ndarray) -> np.ndarray:
    """CLT 理论近似：X̄ ≈ N(μ, σ²/n) 的密度值（解析真值，用于对照）。"""
    mu = dist.mean
    sigma = dist.std / np.sqrt(n)
    if sigma < 1e-12:
        return np.zeros_like(xs, dtype=float)
    return np.exp(-0.5 * ((xs - mu) / sigma) ** 2) / (sigma * np.sqrt(2.0 * np.pi))
