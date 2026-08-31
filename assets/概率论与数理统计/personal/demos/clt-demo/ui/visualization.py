"""画布：样本均值直方图 + 理论正态曲线叠加（逐帧逼近钟形）。"""
from __future__ import annotations

import plotly.graph_objects as go


def render(state) -> go.Figure:
    """根据当前 DemoState 绘制直方图 + 理论正态曲线，返回 plotly Figure。"""
    fig = go.Figure()

    # 样本均值直方图（密度）
    fig.add_trace(
        go.Bar(
            x=state.bin_centers,
            y=state.hist,
            width=state.bin_edges[1] - state.bin_edges[0],
            name="样本均值分布",
            marker_color="rgba(66,133,244,0.55)",
            hovertemplate="均值区间 %{x:.3f}<br>密度 %{y:.3f}<extra></extra>",
        )
    )

    # 理论正态曲线（解析真值）
    fig.add_trace(
        go.Scatter(
            x=state.norm_x,
            y=state.norm_y,
            mode="lines",
            name=f"理论正态 N(μ, σ²/n)",
            line=dict(color="crimson", width=3),
            hovertemplate="x=%{x:.3f}<br>密度 %{y:.3f}<extra></extra>",
        )
    )

    fig.update_layout(
        title=(
            f"{state.dist.name}  —  样本均值分布（n={state.n}，{state.trials} 组）"
        ),
        xaxis_title="样本均值 X̄",
        yaxis_title="密度",
        barmode="overlay",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        template="plotly_white",
        height=480,
    )
    return fig
