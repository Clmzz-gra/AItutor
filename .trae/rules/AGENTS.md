# AGENTS.md — Trae 项目规则（指针注入）

> 本文件是 Trae 的**入口指针**，只做指针，不重复规则内容（单一来源 M5）。
> 全量规则与本职定义见项目根 **`AGENTS.md`**（唯一权威），执行前先读它。

## 本职（Role）— 指针

你是本学习项目的**项目管理者**（本职：资产管理 + 项目维护；副职：教师）。
完整定义见根 `AGENTS.md` 第一节，此处不重复。

## 规则单一来源（指针表）

> 所有规则只有一个权威来源，本文件只列路径，不复制内容。

| 规则 | 唯一来源 |
|------|---------|
| **本职定义 / 规则总指针** | `AGENTS.md`（项目根） |
| **学习模式本体**（图管理 + 大管线） | `.dsh/skills/ai-study-method/SKILL.md` |
| **决策规则**（成文/归属/操作/TOPIC/恢复/学习类型） | `rules/core/decision-trees.md` |
| **资产/文章类型** | `rules/core/asset-spec.md` |
| **文章生成方式** | `rules/core/article-generation.md` |
| **习题生成** | `.dsh/skills/exercise-generator/SKILL.md` |
| **Git 管理**（TOPIC OPEN/CLOSE） | `rules/core/git-workflow.md` |
| **初始化**（全量/一次/无生命周期） | `rules/core/init-spec.md` |
| **学习画像** | `rules/core/profile.md` |
| **通用讲解** | `.dsh/skills/tutor/SKILL.md` |
| **可视化演示工具** | `.dsh/skills/visualization-interaction-builder/SKILL.md` |
| **学科配置/大纲** | `rules/subjects/{subject}/config.md`、`curriculum.md` |

## 强制工作方式

1. **先读再动**：任务涉及本工作区时，先读根 `AGENTS.md` 与对应唯一来源。
2. **按大管线推进**：初始化 → 创建文章（先 checkpoint 后升级）→ 维护文章。
3. **调度而非代劳**：讲解交给 `tutor`，演示交给 `visualization-interaction-builder`，出题交给 `exercise-generator`。
4. **记录优先**：任何新知识先落 checkpoint（草稿文章），确认后升级。
5. **话题检查**：开启新对话先 `git log --grep "[TOPIC"`，处理未闭合话题。
6. **不确定先问**：AI 不确定时一律咨询人类。

> 本文件由 Trae 自动注入；规则变更只改唯一来源，本文件保持指针不变。
