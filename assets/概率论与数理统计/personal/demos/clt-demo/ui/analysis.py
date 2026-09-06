"""结果分析：样本均值/标准差 vs 理论真值 + CLT 判定。"""
from __future__ import annotations

import streamlit as st


def render(state) -> None:
    st.subheader("结果对比（当前 n）")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("样本均值 X̄", f"{state.sample_mean:.4f}")
    c2.metric("理论均值 μ", f"{state.theo_mean:.4f}")
    c3.metric("样本标准差", f"{state.sample_std:.4f}")
    c4.metric("理论标准差 σ/√n", f"{state.theo_std:.4f}")

    # 判定语义与当前状态一致：这里"当前状态"就是当前 n 的样本均值分布，
    # 理论正态 N(μ, σ²/n) 也是当前 n 的，二者语义一致。
    mean_err = abs(state.sample_mean - state.theo_mean)
    std_err = abs(state.sample_std - state.theo_std)
    st.write(
        f"**CLT 近似**：样本均值分布 ≈ N(μ, σ²/n)。"
        f"当前 n={state.n}，样本均值偏差 {mean_err:.4f}、标准差偏差 {std_err:.4f}。"
    )
    if state.n < 10:
        st.info(
            f"**n={state.n} 较小时**，样本均值分布还明显偏离正态（尤其偏态分布如指数/二项）。"
            "增大 n 观察逼近钟形。"
        )
    else:
        st.success(
            f"**n={state.n} 时**，样本均值分布已接近正态钟形——这正是中心极限定理："
            "无论总体分布如何，样本均值（标准化后）随 n 增大趋于正态。"
        )
