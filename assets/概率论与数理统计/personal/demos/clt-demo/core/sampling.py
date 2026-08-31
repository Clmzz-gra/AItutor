"""CLT 核心：抽样 → 样本均值分布。纯逻辑，零界面依赖。"""
import numpy as np

def sample_means(dist, n, trials, seed=None):
    """从 dist 抽样 trials 组，每组 n 个，返回每组样本均值。"""
    rng = np.random.default_rng(seed)
    return np.array([dist(rng, n) for _ in range(trials)])

def uniform(rng, n):
    return rng.uniform(0, 1, n).mean()

def exponential(rng, n):
    return rng.exponential(1.0, n).mean()

def binomial(rng, n):
    return rng.binomial(10, 0.3, n).mean()

DISTS = {"均匀": uniform, "指数": exponential, "二项": binomial}
