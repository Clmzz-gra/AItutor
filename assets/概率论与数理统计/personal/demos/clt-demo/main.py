"""中心极限定理演示 — 入口（Streamlit）。

运行：在本目录下执行
    streamlit run main.py
"""
from __future__ import annotations

import time

import streamlit as st

from core.model import DISTS
from core.step import DemoState
from ui import analysis, help_content, sidebar, visualization

st.set_page_config(page_title="中心极限定理演示", layout="wide")
st.title("中心极限定理（CLT）— 样本均值逼近正态")

dist_name, n, trials, seed, run, auto = sidebar.render()

# 显示当前总体分布表达式（UI 必须把对象写出来）
# st.latex 会自动用 $$...$$ 包裹，故去掉 formula 自带的 $ 定界符，避免三重美元渲染失败
st.latex(DISTS[dist_name].formula.strip("$"))

# 切换分布/参数时重置状态
key = (dist_name, trials, seed)
if "state" not in st.session_state or st.session_state.get("key") != key:
    st.session_state.state = DemoState(dist_name, n, trials, seed)
    st.session_state.key = key
state: DemoState = st.session_state.state

if auto:
    # 自动演示：n 从 1 递增到 200，逐帧逼近钟形
    placeholder = st.empty()
    for k in range(1, 201, 5):
        state.set_n(k)
        placeholder.plotly_chart(visualization.render(state), use_container_width=True)
        time.sleep(0.05)
else:
    state.set_n(n)
    st.plotly_chart(visualization.render(state), use_container_width=True)

analysis.render(state)

with st.expander("帮助 / 概念说明"):
    help_content.render()
