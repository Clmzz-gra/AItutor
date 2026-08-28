# 架构设计：通用核心 + 学科拓展（DeepSeek harness 治理）

> 定位：AItutor 是一套**通用学习系统**，通过"学科拓展包"适配不同学科。
> 核心稳定、拓展可插拔——换学科只换拓展，不动核心。
> 治理：采用 **DeepSeek harness（EAC）规范治理模式**管理 skill 与学习模式。
> 版本：0.2.1 ｜ 日期：2026-08-27

---

## 1. 设计原则

1. **核心稳定**：流程、约束、模板框架学科无关，任何学科都复用同一套。
2. **拓展可插拔**：学科内容、工具、专属规则以"学科包"形式挂载，互不干扰。
3. **换学科只换拓展**：新增学科 = 新增一个学科包，不改核心规则。
4. **核心给"怎么学"，拓展给"学什么"**：核心管方法，拓展管内容。
5. **规则与资产分离**：规则（方法/指令/规范）与资产（产出/数据/内容）彻底分开。
6. **核心和拓展都属于规则类**：核心规则 + 学科规则都在规则层。
7. **基于教材初始化**：人人可基于教材自建学科，现成图谱作为可选 seed。
8. **补充定位**：工具是正常教学的补充（addition），不替代课程进度与作业。

---

## 2. 治理模式（DeepSeek harness 规范）

- **Skill 目录**：项目级 skill 放 `.dsh/skills/<kebab-name>/SKILL.md`
- **frontmatter**：`name`（必须 kebab-case）+ `description`
- **学习模式**：作为核心 skill 纳入同一治理（`.dsh/skills/ai-study-method/`）
- **多 harness**：规则通过 interface + adapters 跑在各种 harness 上

### 当前 skill 清单

| skill | 路径 | 职责 |
|-------|------|------|
| `ai-study-method` | `.dsh/skills/ai-study-method/` | 核心学习模式（图管理 + 大管线） |
| `tutor` | `.dsh/skills/tutor/` | 通用讲解 |
| `visualization-interaction-builder` | `.dsh/skills/visualization-interaction-builder/` | 可视化交互生成 |

---

## 3. 分层架构

```
┌──────────────────────────────────────────────────────┐
│  应用层：学生 / 教授 / 助教（角色入口）                  │
├──────────────────────────────────────────────────────┤
│  规则层（方法 · 指令 · 规范）                          │
│  ├─ 核心规则（学科无关 · 通用）                        │
│  │  ├─ 大管线（初始化→创建文章→维护文章）                 │
│  │  ├─ 三条铁律 + 讲解质量约束 + 文章对象               │
│  │  ├─ 初始化规范（基于教材，人人可自建）               │
│  │  ├─ 输出模板框架（overview / section-note / explain-pack）│
│  │  ├─ 生命周期（TOPIC OPEN/CLOSE，git log）           │
│  │  ├─ 学习画像规则（通用行为追踪）                    │
│  │  ├─ harness 抽象（interface + adapters）            │
│  │  └─ 通用 skill（tutor / 可视化交互生成）     │
│  └─ 学科规则（拓展 · 每学科一个子目录）                 │
│     └─ {subject}/：config（学习依赖+思考方式）/ case / capabilities / demo-spec │
├──────────────────────────────────────────────────────┤
│  资产层（产出 · 数据 · 内容）                          │
│  └─ {subject}/：seed（现成图谱/教材初始化）+ personal（notes/knowledge/homework/demos/profiles）│
└──────────────────────────────────────────────────────┘
```

---

## 4. 规则层

### 4.1 核心规则（学科无关 · 通用）

| 模块 | 说明 | 现有载体 |
|------|------|---------|
| **大管线** | 初始化→创建文章→维护文章 | `.dsh/skills/ai-study-method/SKILL.md`（唯一来源） |
| **三条铁律** | AI 是导游不是答案机 / 问题设置>追问 / 允许不全懂继续走 | 同上 |
| **讲解质量约束** | 先定义再使用、每步有"因为"、多视角、核心收束、防跳跃、反例强制 | `.dsh/skills/tutor/SKILL.md`（唯一来源） |
| **文章对象与类型** | 10 类文章/节点，一切活动落成文章 | `rules/core/asset-spec.md`（唯一来源） |
| **决策规则** | 成文/归属/文章操作/链接/TOPIC/恢复/学习类型 | `rules/core/decision-trees.md`（唯一来源） |
| **初始化规范** | 基于教材生成 seed（含能力覆盖矩阵） | `rules/core/init-spec.md`（已建） |
| **输出模板框架** | 带占位符的通用模板 | `templates/*-template.md` |
| **文章生成方式** | 10 类文章的生成依赖与规范 | `rules/core/article-generation.md`（新增） |
| **生命周期（TOPIC）** | 新话题建 checkpoint（OPEN，按文章名）；升级/归档/删除 = CLOSE；新对话先查 git log | `_checkpoints/` + `rules/core/decision-trees.md` §5·5 |
| **学习画像规则** | 扫 wikilink + frontmatter；兴趣焦点看图结构 | `rules/core/profile.md` + `tools/learning-profile/analyze.py`（已建） |
| **harness 抽象** | interface + adapters，跑在各种 harness | `rules/core/harness/`（已建） |
| **通用讲解** | 知识脉络教学法 | `.dsh/skills/tutor/` |
| **可视化交互生成** | 演示工具生成规范 | `.dsh/skills/visualization-interaction-builder/` |

**核心判定标准**：换一门学科（概率论→有机化学→历史）**不需要改**的模块，就是核心。

### 4.2 学科规则（拓展 · 每学科一个子目录）

| 模块 | 说明 | 概率论实例 |
|------|------|-----------|
| **学科配置 config** | 学习依赖 + 思考方式（非课程对应） | `rules/subjects/概率论与数理统计/config.md` |
| **学科案例 case** | 教材、课程结构、应用计划 | `rules/subjects/概率论与数理统计/case.md` |
| **学科能力地图 capabilities** | 通用 AI 维度 + 该学科实例 | `rules/subjects/概率论与数理统计/capabilities.md` |
| **演示工具规范 demo-spec** | 该学科要做哪些演示工具（清单） | `rules/subjects/{subject}/demo-spec.md`（通用生成规范见 `.dsh/skills/visualization-interaction-builder/SKILL.md`） |

**学科配置聚焦**（不是课程对应）：
- **学习依赖**：前置知识链、符号系统（如 LaTeX）、工具依赖、表达规范
- **思考方式**：该学科特有的认知模式（如数学的"定义-定理-证明"式思维）
- **教学约定**：由思考方式派生的讲解/检验偏好

**拓展判定标准**：换一门学科**需要替换/新增**的模块，就是拓展。

---

## 5. 资产层

> 资产 = 实际产出/数据/内容。规则与资产分离。

```
assets/{subject}/
├── seed/                    # 共享地基（现成图谱 或 教材初始化产物）
│   ├── 学科概览.md
│   └── Ch1~ChN 章文章
├── personal/                # 学生个人搭建（在此地基上生长）
│   ├── papers/              # 论文/文献（源材料）
│   ├── notes/               # 章/节/概念/思考/提问/习题/作业/问题
│   ├── knowledge/           # 补充定理 / 习题
│   ├── homework/            # 作业 / 练习册 / 试卷
│   ├── demos/               # 演示工具实现
│   └── profiles/            # 学习画像数据
```

### 关键点
- **seed = 共享只读**：所有学生拿到同一份（现成图谱或教材初始化），作为地基
- **personal = 个人可写**：学生在此地基上搭建
- **Obsidian 图谱**：seed + personal 通过 wikilink 连成**同一个图谱**（子目录不影响图谱）
- **AI 检索**：子目录 + 命名 + frontmatter + wikilink + 搜索，保证检索高效（无索引文件）
- **同步/隐私**：已有 seed 分发；学生个人部分可选提交

---

## 6. 初始化机制（基于教材）

**初始化 = 从教材生成一个学科的 seed**，人人可对任意教材执行。
> 完整流程见 **`rules/core/init-spec.md`**（唯一来源，此处不重复）。

**两种 seed 来源**（产出同一套结构）：
| 来源 | 说明 | 适用 |
|------|------|------|
| 教材初始化（通用） | 任何人跑初始化规范自建 | 通用、人人可做 |
| 现成知识图谱（试点） | 已有现成图谱作为 seed | 本次试点（质量更高） |

---

## 7. 拓展机制：如何新增一个学科

新增学科 = 新建一个"学科包"，**不改核心**：

```
1. 建学科规则      rules/subjects/{subject}/config.md（学习依赖 + 思考方式）
2. 写学科案例      rules/subjects/{subject}/case.md
3. 建学科能力地图  rules/subjects/{subject}/capabilities.md
4. 建演示工具规范  rules/subjects/{subject}/demo-spec.md（可选）
5. 初始化 seed     assets/{subject}/seed/（基于教材 或 现成图谱）
6. 初始化学科 seed（**全量、每学科一次、无生命周期**）
7. 学生搭建        assets/{subject}/personal/
```

**核心层零改动**：新增学科时，`.dsh/skills/`、`templates/` 都不需要改。
### 7·5 如何扩展文章类型（二次开发）

- 内置 10 类文章类型，支持二次开发按“扩展通道”新增类型
- 唯一权威：`rules/core/asset-spec.md §一·五`
- 扩展点：类型定义 / frontmatter / 模板 / 生成方式 / 图谱配色 / 校验 / 生命周期
- 原则：核心流程不变，新增类型必须补齐全部扩展点，不能只改一个文件

---

## 8. 当前项目映射

| 文件/目录 | 归属 | 说明 |
|-----------|------|------|
| `.dsh/skills/ai-study-method/` | 🟦 核心规则 | 核心学习模式（图管理 + 大管线） |
| `.dsh/skills/tutor/` | 🟦 核心规则 | 通用讲解 |
| `.dsh/skills/exercise-generator/` | 🟦 核心规则 | 习题生成（出题 + 答案折叠，不做检验） |
| `.dsh/skills/visualization-interaction-builder/` | 🟦 核心规则 | 可视化交互生成 |
| `templates/` | 🟦 核心规则 | 通用模板框架 |
| `rules/core/capabilities.md` | 🟦 核心规则 | 通用 AI 能力维度框架 |
| `rules/subjects/概率论与数理统计/capabilities.md` | 🟨 学科规则 | 概率论能力地图 |
| `rules/subjects/概率论与数理统计/case.md` | 🟨 学科规则 | 概率论案例 |
| `tools/` | 🟨 资产 | 工具脚本（学习画像等）；演示工具在各学科 `personal/demos/` |
| `guide/` | 🟦 核心规则 | 学生/助教引导（通用） |
| `maintenance/` | — | 维护规范（规则 + 自检 + 登记表） |
| `_archive/` | — | 归档 |

> 🟦 = 核心规则 ｜ 🟨 = 学科规则/资产

---

## 9. 待办（架构落地）

- [x] 拆分 `method/ai-capabilities.md` → `rules/core/capabilities.md` + `rules/subjects/概率论与数理统计/capabilities.md`
- [x] 拆分 `method/demo-builder.md` → 归档，演示规范收敛到 `.dsh/skills/visualization-interaction-builder/`
- [x] 归位 `cases/概率论与数理统计.md` → `rules/subjects/概率论与数理统计/case.md`
- [x] 收敛合并文档 → 归档 PROFESSOR-PACK/TECHNICAL/CHANGELOG，README 重写为单一入口
- [x] 建立 `init-spec` 初始化规范（基于教材，含 MinerU/LaTeX/Python 通用依赖）
- [x] 建立 `index-format`（`_index.md`）→ 已归档（不设索引，2026-08-27）
- [x] 建立 `subject-config` 学科配置规范（学习依赖 + 思考方式）
- [x] 建立 harness 抽象层（interface + dsh/trae/claude-code/codex adapters）
- [x] 建立 `assets/` 资产层结构（seed + personal）
- [x] 建立 `curriculum` 课程大纲模板（老师开课前写）
- [x] 概率论 seed 初始化（现成知识图谱导入，含能力覆盖矩阵）
- [x] 演示工具（clt-demo 结构 + 核心采样逻辑）
- [x] 学生/助教引导完善（guide/学生使用指南 + 助教手册）
- [x] 管线状态机规范（rules/core/state-machine.md）→ 已归档（五阶段残留）
- [x] 管线状态机实现（tools/state-machine/pipeline.py）→ 已归档（五阶段残留）
- [x] 学习画像系统（rules/core/profile.md + tools/learning-profile/analyze.py：原始图谱/学习类型/兴趣焦点/生长形态/双链/节奏）
