# 演示工具族（demo-tools）— 跨学科索引

> "知识可视化·可交互·可实验"维度的工程落地，**跨学科**。
> 生成规范见 `.dsh/skills/visualization-interaction-builder/SKILL.md`。
> **实现位置**：各演示工具放在**对应学科的 `personal/demos/`** 下（单一来源，本目录不存放实现）。
> 本目录仅保留工具脚本与跨项目工具指南（如 `learning-profile/analyze.py`、`graph-style/configure.py`、`obsidian-cli.md`）。

## 工具索引（指向各学科 personal/demos/）

| 工具 | 学科 | 演示 | 状态 |
|------|------|------|------|
| `ielts-vocab-map` | 雅思 | 同义替换/场景词图谱 | 待建 |
| `writing-structure-builder` | 雅思 | 写作结构生成器（小作文/大作文） | 待建 |
| `speaking-practice-timer` | 雅思 | 口语限时练习 / Part 2 计时 | 待建 |
| `listening-dictation-tool` | 雅思 | 听力精听 / 听写工具 | 待建 |

| `graph-style/configure.py` | Obsidian 图谱配色分组自动配置（path + file 检索式，seed/personal × 层级/类型） | `tools/graph-style/configure.py` |
| `obsidian-cli.md` | Obsidian CLI 使用指南（vault 读写/搜索/坏链体检、AI 建笔记标准回路、Python 调用模板；实测 1.13.7） | `tools/obsidian-cli.md` |

## 技术栈

- Streamlit（交互界面）+ Plotly/Matplotlib（实时绘图）+ NumPy/SciPy（计算）
- 参考实现：`_temp/edudemo-skill-pack/edudemo/`（ACO/GA/PSO/SA 四件套）
