# 文章生成方式（article-generation）

> 每一类文章必须明确：**生成依赖**（哪个 skill / 哪些用户信息）+ **生成规范**（命名 / frontmatter / 结构 / 链接 / 校验）。
> 核心规则 · 学科无关。
> 10 类文章结构规范与模板已落地；习题生成走 `exercise-generator`。

## 10 类文章生成方式

| 文章类型 | 生成依赖（skill / 用户信息） | 生成规范落点 |
|---------|---------------------------|-------------|
| 学科全景 | 初始化（`init-spec`）+ 用户学科材料 / 现成 seed | `templates/overview-template.md` + `asset-spec.md` §四.1 |
| 章 | `tutor`（知识脉络教学法）+ 教材 + 节文章 | `templates/chapter-template.md` + `asset-spec.md` §四.2 |
| 节 | `tutor`（知识脉络教学法）+ 教材 | `templates/section-note-template.md` + `asset-spec.md` §四.3 |
| 概念 | `tutor`（定义→正反例→边界）+ 教材 / 用户提问 | `templates/concept-template.md` + `asset-spec.md` §四.4 |
| 论文 | 用户提供论文 + `tutor`（复杂对象可用讲解包模式） | `templates/paper-template.md` + `asset-spec.md` §四.5 |
| 思考 | 用户讨论 / 反思 + `decision-trees.md` §1 成文判定 | `templates/thinking-template.md` + `asset-spec.md` §四.6 |
| 提问 | 用户提问 + `decision-trees.md` §1 成文判定 | `templates/question-template.md` + `asset-spec.md` §四.7 |
| 习题 | `exercise-generator`（出题 + 答案折叠，不做检验） | `templates/exercise-template.md` + `asset-spec.md` §四.8 |
| 作业 | 用户提供作业 / 任务 + 入链挂知识点 | `templates/homework-template.md` + `asset-spec.md` §四.9 |
| 问题 | 用户待解问题 + `decision-trees.md` §1 成文判定 | `templates/problem-template.md` + `asset-spec.md` §四.10 |

## 讲解包（多文件展开，属于 note）

- 触发：复杂对象（论文 / 跨章节主题 / 方法链 / 交付他人）
- 生成依赖：`tutor` 讲解包模式（Explain-Pack Mode）
- 规范：`{主题} — 讲解包/00 整体认知.md` + 01/02/… 编号分篇；spilt 篇互链，无孤立分篇

## 生成通用校验（每篇文章）

1. 命名符合 10 类规范
2. frontmatter 必填（type / formal / subject / created / updated）
3. 至少 1 个 wikilink（无孤立文章）
4. 无坏链（链接目标存在）
5. 类型不变（无转化关系）
6. AI 不确定 → 咨询人类

## 待办

- [x] 10 类文章结构规范细化（结构模板逐类完善）
- [x] 习题生成 skill 设计（出题流程 + 答案折叠，不做检验）
- [x] 各类型校验规则补全（如学科概览四要素、节的三段结构）
