**如果该项目对你有用，请为我点个star⭐**

# AItutor

关于笔记，你可能时常遇到如下问题：
   1. 写笔记效率太低
   2. 写完的笔记从不再看
   3. 笔记的维护耗费精力
   4. 不够直观，复习困难

关于图谱，你通常可能通常认为它：
   1. 徒有其表，不堪大用
   2. 静态且死板
   3. 无趣，信息量低

**在该项目中，这些问题将不再是阻碍**

**AItutor**是依赖**开源笔记软件obsidian**的一个**通用AI学习辅助项目**，同时也是一套**AI时代的学习方法论**，只要你有**学科材料**，便能轻松通过**初始化"学科拓展包"适配不同学科**。

AItutor将知识图谱设计为**动态的可拓展对象**。你只需要通过正常与AI对话，无需花费精力管理。你的每一个想法，每一次提问都将成为图谱的一部分。图谱将会为你生长，长成最适合你学习模式的样子。
**你可以通过知识图谱直观地通过图谱了解你学习的“形状”，进而更高效地学习，发掘自己的潜力。**

该项目同时服务于自学的**学生**，希望使用该项目提高教学效果的**教师**，以及想要对该项目二次开发的创作者。

> 版本：0.2.1
**该项目当前处于测试阶段，在获取试点反馈后将进行蜕变式更新。**

架构与设计说明见 [ARCHITECTURE.md](./ARCHITECTURE.md)

---

## 项目特色

**通用核心 + 学科拓展**
一套系统适配所有学科：核心管"怎么学"，拓展管"学什么"。不同学科只需要初始化一个学科包。

**规则与资产分离**
规则与资产彻底分开。规则可复用、可维护；资产是使用者个人增量，互不污染。

**三条铁律**
三条铁律贯穿：AI 是导游不是答案机、问题设置大于追问、允许不全懂继续走。

**seed 与 personal 分离**
seed 是只读的教材初始化资料，personal 是学生个人增量。避免污染，便于查询和管理。

**业务栈提交防丢失**
每个实质学习话题先建 checkpoint 快照，学完沉淀升级为资产。新对话先查 git 记录确认快照情况，防止进度丢失。

**多 harness 适配**
同一套规则通过 interface + adapters 跑在 DeepSeek / Claude Code / Codex / Trae 上，入口只放指针引向全量文件。

**学习画像程序化**
基于学生增量图谱程序化分析学习类型、兴趣焦点、生长形态，不依赖 AI 主观统计。

**可视化演示工具**
按统一规范生成可交互教学演示，把抽象概念变成可看、可拖、可实验的 GUI。

---

## 可用功能

| 功能 | 说明 | 载体 |
|------|------|------|
| 学习流程 | 大管线三步：初始化 → 创建文章 → 维护文章；讲解/讨论/习题都落为文章 | `.dsh/skills/ai-study-method/` + `rules/core/asset-spec.md` |
| 通用讲解 | 知识脉络教学法，学科无关的讲解模式 | `.dsh/skills/tutor/` |
| 习题生成 | 按常见练习形式出题（单选/判断/填空/读表/计算/综合），答案折叠，不做检验 | `.dsh/skills/exercise-generator/` |
| 可视化演示工具 | 教学演示工具生成规范（core/ui/utils 三层 + 自检流程） | `.dsh/skills/visualization-interaction-builder/` |
| 学习画像 | 程序化分析学习类型/兴趣焦点/生长形态 | `tools/learning-profile/analyze.py` |
| 多 harness 适配 | 同一套规则跑在 dsh / Claude Code / Codex / Trae | `.dsh/` `.claude/` `.codex/` `.trae/` |
| 模板框架 | 10 类文章模板 + 周报 | `templates/` |
| 学科规则 | 每学科一个子目录（学习依赖、思考方式、能力地图、课程大纲） | `rules/subjects/` |

> 提供了中心极限定律的可视化演示，实例在`assets\概率论与数理统计\personal\demos\clt-demo`

---

## 快速开始

### 学生

**准备环境**

1. 安装 **Obsidian**（1.12.7+），将项目根目录作为 vault 打开——图谱、文章和笔记都会在这里可视化；启用 **Obsidian CLI**（官方原文）：
   > Enable **Obsidian CLI** under **Settings → About → Command line interface**, follow the registration prompt, restart your terminal, then verify with `obsidian help`.
   按提示注册后重启终端，验证 `obsidian help` 可正常输出。
2. 安装任一支持的 harness（DeepSeek / Claude Code / Codex / Trae）。
3. 克隆本项目到自己的电脑。

**放入教材**

4. 在 `assets/{学科}/seed/textbook/` 放入教材（Markdown/OCR 文本，勿放 PDF，遵守版权）。
5. 若已有现成 seed 图谱（学科概览/章文章），一并放入 `assets/{学科}/seed/`；否则让 AI 基于教材初始化。

**开始学习**

6. 正常对话提问即可，例如"开始学习概率论"。AI 会自动：
   - 建 checkpoint 快照（防丢失）
   - 把讲解/讨论/习题写成文章（节点）
   - 按 初始化→创建文章→维护文章 驱动学习
   - 沉淀升级为正式资产（章/节/概念/思考/提问/习题）

**查看图谱与画像**

7. 用 Obsidian 看知识图谱（节点大小 = 链接度），节点即文章。
8. 用 Obsidian 看知识图谱与目录结构，掌握当前学习形状。
9. 跑 `python tools/learning-profile/analyze.py --personal assets/{学科}/personal/notes --seed assets/{学科}/seed` 看学习画像。

### 教授

**开课前**

1. 在 `rules/subjects/{学科}/curriculum.md` 填写课程大纲（章节、重点、进度、考核）。
2. 提供教材/知识图谱，初始化 `seed/`（学科概览、章文章、能力地图），见 `ARCHITECTURE.md` 初始化机制。（初始化规范名明确，提供教材即可利用AI进行）

**教学中**

3. 学生按大管线（初始化→创建文章→维护文章）自主学习，AI 负责讲解、演示、画像、文章与图谱维护。
4. 教授负责正常课程进度、作业、考核——本工具是补充，不替代。

**跟进**

5. 收集学生的 `personal/` 增量与学习画像，定位薄弱点，调整教学。

### 二次开发

**了解架构**

1. 读 `ARCHITECTURE.md`（规则/资产分层、核心/拓展、harness、初始化）。
2. 读 `AGENTS.md`（智能体角色与规则单一来源）。

**新增学科**

3. 在 `rules/subjects/` 建子目录：`config.md`（学习依赖/思考方式）、`case.md`（教材/课程）、`capabilities.md`（能力地图）、`curriculum.md`（大纲）。
4. 基于教材初始化 `assets/{学科}/seed/`。

**新增文章类型**

5. 按 `asset-spec.md §一·五` 扩展通道补齐：类型定义、模板、生成方式、配色、校验，并登记。

**新增演示工具**

6. 按 `visualization-interaction-builder` 规范生成，放 `assets/{学科}/personal/demos/`，跑自检审查流程。

**扩展 harness**

7. 在 `rules/core/harness/adapters/` 加适配文件，建对应入口指针文件（如 `CLAUDE.md`、`.codex/AGENTS.md`）。

---

## 项目结构

```
AItutor/
├── AGENTS.md                    # 智能体角色 + 规则单一来源指针
├── ARCHITECTURE.md              # 架构设计（规则/资产 + 核心/拓展 + harness）
├── .dsh/skills/                 # 核心 skill（DeepSeek harness 治理）
│   ├── ai-study-method/         #   学习模式（图管理 + 大管线）
│   ├── tutor/                   #   通用讲解
│   ├── exercise-generator/       #   习题生成（出题 + 答案折叠）
│   └── visualization-interaction-builder/  # 可视化演示工具生成
├── rules/                       # 规则层
│   ├── core/                    #   核心规则（学科无关）
│   └── subjects/                #   学科规则（每学科一个子目录）
├── templates/                   # 通用模板框架
├── guide/                       # 学生/助教引导
├── tools/                       # 工具脚本（学习画像等）
├── assets/                      # 学科资产层（seed 只读地基 + personal 学生增量；仅占位结构，实际内容本地）
│   └── {学科}/                  #   每学科一个子目录（seed/textbook + personal/notes...）
└── .claude/ .codex/ .trae/      # 各 harness 指针注入入口
```

---

## License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International License** (CC BY-NC 4.0).

You are free to use, share, and adapt it for **learning and research purposes**, but **not for commercial use**.

See [LICENSE](./LICENSE) for details.

---

## 文档导航

- `ARCHITECTURE.md` — 架构设计（分层、核心/拓展、harness、初始化、待办）
- `AGENTS.md` — 智能体角色、规则单一来源、流程引用
- `CHANGELOG.md` — 版本更新记录
- `rules/core/` — 核心规则（决策树、资产规范、Git 管理、学习画像等）
- `guide/` — 学生/助教使用引导
