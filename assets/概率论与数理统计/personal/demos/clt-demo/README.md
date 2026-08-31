# clt-demo — 中心极限定理演示（招牌）

> 教学演示：任意分布抽样 → 样本均值分布逼近正态钟形。
> 规范：`.dsh/skills/visualization-interaction-builder/SKILL.md`（拓展 B：概率论）

## 结构

```
clt-demo/
├── main.py            # Streamlit 入口
├── core/              # 领域核心（纯逻辑，零界面）
│   ├── model.py       # 总体分布库 + 抽样 → 样本均值 + 理论正态近似
│   └── step.py        # DemoState：单步推进接口
├── ui/                # 界面层（展示/交互）
│   ├── visualization.py  # 画布：直方图 + 理论正态曲线叠加
│   ├── sidebar.py       # 控制面板
│   ├── analysis.py      # 结果对比 + CLT 判定
│   └── help_content.py  # 帮助面板
└── utils/             # 实验/批处理
    └── experiment.py  # 多 seed 实验 + CSV 导出
```

## 运行

```bash
cd assets/概率论与数理统计/personal/demos/clt-demo
streamlit run main.py
```

依赖：`streamlit`、`numpy`、`plotly`、`pandas`。

## 演示内容

| 总体分布 | 均值 μ | 方差 σ² | 教学点 |
|----------|--------|---------|--------|
| 均匀 U(0,1) | 0.5 | 1/12 | 对称分布，n 小也较快接近正态 |
| 指数 Exp(1) | 1 | 1 | 强偏态，n 需较大才逼近钟形 |
| 二项 B(10,0.3) | 3 | 2.1 | 离散分布，n 增大后连续化 |

## 核心逻辑

- **样本均值**：从总体抽 trials 组、每组 n 个，算每组均值 → 样本均值分布。
- **理论正态**：CLT 给出 X̄ ≈ N(μ, σ²/n)，作为解析真值叠加对照。
- **判定语义一致**：直方图与理论曲线都对应**当前 n**，语义一致。

## 无界面验证

```bash
python -m core.step        # 每个分布推进若干步打印样本均值/方差 vs 理论真值
python -m utils.experiment # 多 seed 收敛实验
```

## 状态

- [x] 核心逻辑（core 可无界面运行）
- [x] 界面（Streamlit 直方图 + 理论曲线 + 结果面板 + 帮助）
- [x] 实验（utils/experiment.py 多 seed + CSV）
