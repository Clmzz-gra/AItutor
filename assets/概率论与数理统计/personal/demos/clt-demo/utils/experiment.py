"""实验：不同样本量 n / 不同 seed 下样本均值分布与理论正态的偏差，支持导出 CSV。"""
from __future__ import annotations

import csv
from typing import List

from core.model import DISTS
from core.step import DemoState


def run_experiment(dist_name: str, ns: List[int], trials: int = 2000,
                   seeds: List[int] | None = None, out_csv: str | None = None) -> List[dict]:
    """对给定分布，在样本量序列 ns × 多个 seed 上跑样本均值，返回逐 n 统计。

    可复现：固定 seed 两次运行结果一致。
    """
    if seeds is None:
        seeds = [42]
    rows = []
    for n in ns:
        mean_errs, std_errs = [], []
        for seed in seeds:
            s = DemoState(dist_name, n, trials, seed)
            mean_errs.append(abs(s.sample_mean - s.theo_mean))
            std_errs.append(abs(s.sample_std - s.theo_std))
        rows.append(
            {
                "n": n,
                "mean_err_mean": round(sum(mean_errs) / len(mean_errs), 6),
                "std_err_mean": round(sum(std_errs) / len(std_errs), 6),
                "theo_std": round(DemoState(dist_name, n, trials, 42).theo_std, 6),
            }
        )
    if out_csv:
        with open(out_csv, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
    return rows


def run_all(ns: List[int], trials: int = 2000, seeds: List[int] | None = None,
            out_csv: str | None = None) -> dict:
    """对全部分布跑实验，返回 {分布名: rows}。"""
    result = {}
    for name in DISTS:
        result[name] = run_experiment(name, ns, trials, seeds)
    if out_csv:
        with open(out_csv, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["distribution", "n", "mean_err_mean", "std_err_mean", "theo_std"])
            for name, rows in result.items():
                for r in rows:
                    w.writerow([name, r["n"], r["mean_err_mean"], r["std_err_mean"], r["theo_std"]])
    return result


if __name__ == "__main__":
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ns = [1, 5, 10, 30, 50, 100, 200]
    for name, rows in run_all(ns, seeds=[42, 7, 2024]).items():
        last = rows[-1]
        print(
            f"{name:16s} n={last['n']:3d}  均值偏差={last['mean_err_mean']:.4f}"
            f"  标准差偏差={last['std_err_mean']:.4f}  理论σ/√n={last['theo_std']:.4f}"
        )
