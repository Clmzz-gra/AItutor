# 演示工具族（demo-tools）— 跨学科索引

> "知识可视化·可交互·可实验"维度的工程落地，**跨学科**。
> 生成规范见 `.dsh/skills/visualization-interaction-builder/SKILL.md`。
> **实现位置**：各演示工具放在**对应学科的 `personal/demos/`** 下（单一来源，本目录不存放实现）。
> 本目录仅保留工具脚本与跨项目工具指南（如 `learning-profile/analyze.py`、`graph-style/configure.py`、`obsidian-cli.md`）。

## 工具索引（指向各学科 personal/demos/）

| 工具 | 学科 | 演示 | 状态 |
|------|------|------|------|
| `lebesgue-riemann-demo` | 实变函数与泛函分析 | 勒贝格 vs 黎曼积分对比 | ✅ 已建 |
| `cantor-set-demo` | 实变函数与泛函分析 | 康托尔集构造 | ✅ 已建 |
| `clt-demo` | 概率论与数理统计 | 中心极限定理（招牌） | ✅ 已建 |
| `lln-demo` | 概率论与数理统计 | 大数定律 | 待建 |
| `dist-explorer` | 概率论与数理统计 | 分布探索器 | 待建 |
| `ht-demo` | 概率论与数理统计 | 假设检验 | 待建 |
| `ci-demo` | 概率论与数理统计 | 置信区间 | 待建 |
| `mc-demo` | 概率论与数理统计 | 蒙特卡洛 | 待建 |

## 工具脚本索引

| 脚本/指南 | 用途 | 入口/用法 |
|-----------|------|-----------|
| `graph-style/configure.py` | Obsidian 图谱配色分组自动配置（path + file 检索式，seed/personal × 层级/类型） | `python tools/graph-style/configure.py` |
| `obsidian-cli.md` | Obsidian CLI 使用指南（vault 读写/搜索/坏链体检、AI 建笔记标准回路、Python 调用模板；实测 1.13.7） | `tools/obsidian-cli.md` |
| `doctor.py` | 环境 + 图谱/仓库体检（坏链、孤立节点、frontmatter、未闭合 TOPIC、临时残留；默认免费模型提示） | `python tools/doctor.py` |
| `setup/` | 一键环境安装（Windows / macOS / Linux），少操作设置 | `tools/setup/README.md` |

## 技术栈

- Streamlit（交互界面）+ Plotly/Matplotlib（实时绘图）+ NumPy/SciPy（计算）
- 参考实现：`_temp/edudemo-skill-pack/edudemo/`（ACO/GA/PSO/SA 四件套）
