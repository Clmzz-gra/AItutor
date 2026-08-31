"""控制面板：参数控件（分布选择 + 样本量 n + 抽样组数 + 随机种子 + 自动演示）。"""
from __future__ import annotations

import streamlit as st

from core.model import DISTS


def render():
    """渲染侧栏控件，返回 (dist_name, n, trials, seed, run, auto)。"""
    dist_name = st.sidebar.selectbox("总体分布", list(DISTS))
    n = st.sidebar.slider("样本量 n（每组抽样个数）", 1, 200, 30)
    trials = st.sidebar.slider("抽样组数（样本均值个数）", 100, 5000, 1000, step=100)
    seed = st.sidebar.number_input("随机种子", 0, 9999, 42)
    run = st.sidebar.button("▶ 运行")
    auto = st.sidebar.button("⏩ 自动演示（n 从 1 递增逼近钟形）")
    st.sidebar.caption("拖动 n 观察样本均值分布如何逼近正态钟形。")
    return dist_name, n, trials, seed, run, auto
