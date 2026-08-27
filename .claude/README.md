# Harness 适配说明

本项目采用 **DeepSeek harness（EAC）规范治理模式**管理 skill 与学习模式。

## Skill 目录（DeepSeek harness 规范）

项目级 skill 统一放在 `.dsh/skills/<kebab-name>/SKILL.md`：

- `.dsh/skills/ai-study-method/SKILL.md` — 学习模式（图管理 + 大管线）
- `.dsh/skills/tutor/SKILL.md` — 通用讲解
- `.dsh/skills/exercise-generator/SKILL.md` — 习题生成（出题 + 答案折叠）
- `.dsh/skills/visualization-interaction-builder/SKILL.md` — 可视化交互生成

frontmatter 要求：`name`（kebab-case）+ `description`。

## 激活方式

在 DeepSeek harness 中，skill 自动从 `.dsh/skills/` 加载：
- `.dsh/skills/ai-study-method/SKILL.md`（主入口）
- `rules/core/`（规则单一来源）
- `templates/`（产出模板）

## 使用

学习模式（`ai-study-method`）是**核心 skill，自动注入**（作为基线），不依赖特定触发词：
- 通过入口文件（`AGENTS.md` / `CLAUDE.md` / `.codex/AGENTS.md` / `.trae/rules/AGENTS.md`）自动加载。
- 任何学习对话默认按 **大管线（初始化 → 创建文章 → 维护文章）** 推进。
- `tutor`（讲解）、`exercise-generator`（出题）、`visualization-interaction-builder`（演示）按需调度。

## 分发

学生复制 `.dsh/skills/` + `rules/core/` + `templates/` 到自己的 harness skills 目录即可使用。
