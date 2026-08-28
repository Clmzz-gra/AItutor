# 初始化规范（init-spec）

> 基于教材生成一个学科的 seed（共享地基），人人可对任意教材执行。
> **全量生成、每个学科只初始化一次、无生命周期**（不走 TOPIC OPEN/CLOSE）。
> 核心规则 · 学科无关。

## 通用依赖（初始化必需）

| 依赖 | 用途 |
|------|------|
| **MinerU** | 教材 OCR（PDF → Markdown） |
| **LaTeX** | 数学公式渲染/符号规范 |
| **Python** | 脚本处理、工具生成 |
| **Obsidian** | 图谱展示与治理（桌面端） |
| **Obsidian CLI**（官方） | Command-line control of Obsidian: https://obsidian.md/cli；requires 1.12.7+ installer; enable **Settings → About → Command line interface** and register |

> 这些是**通用依赖**，任何学科初始化都需要。
>
> **关于 Obsidian 自动化**：官方提供 CLI（https://obsidian.md/cli）。
> 使用前需要：
> 1. 安装 **Obsidian 桌面端**；
> 2. 在 Obsidian 设置中开启 **「允许命令行与 Obsidian 交互」**；
> 3. 得到可调用的 CLI 命令（命令以官方页面为准，本文档记录时未联网逐条验证）。
>
> 初始化自动化应**优先使用官方 CLI**；同时保留已验证的本地方式：直接读写 `.obsidian/*.json` 配置 + 文件系统（如 `tools/graph-style/configure.py`）、`obsidian://` URI。
> **不引入第三方非官方 CLI / REST API 作为硬依赖**。

## 初始化流程

```
输入：教材（任意学科，PDF/扫描件）
  │
  ▼
① OCR 教材        MinerU → Markdown（`assets/{subject}/seed/textbook/`，不参与图谱）
  ▼
② 生成学科全景    `学科概览.md`（历史/脉络/当代应用/学科关系）
  ▼
③ 生成全量章骨架  `Ch{N} {章名}.md`（全量章节，不做阶段推进）
  ▼
④ 生成能力覆盖矩阵  7 维度 × 章节（每章标注用哪些 AI 能力，见 capabilities）
  ▼
⑤ 生成初始图谱    seed/ 核心概念/节骨架（wikilink 相连）
  ▼
⑥ 自动配置图谱样式  `python tools/graph-style/configure.py`（配色分组 path + file 检索式）
  ▼
输出：seed 目录（可分发，人人可在此基础上搭建）
```

> 不生成 `_index.md`；不生成进度表；不做“分层/不讲”标记（旧五阶段残留）。

## 两种 seed 来源（产出同一套结构）

| 来源 | 说明 | 适用 |
|------|------|------|
| 教材初始化（本规范） | 任何人跑一遍生成（全量） | 通用、人人可做 |
| 现成知识图谱 | 已有现成图谱作为 seed | 试点（质量更高） |

## 验收标准
- 教材 OCR 完成（`seed/textbook/` 有 Markdown）
- `学科概览.md` 四要素齐全
- 全量 `Ch{N} {章名}.md` 骨架已生成（每学科一次）
- 能力覆盖矩阵（7 维度 × 章节）已生成
- seed 节点间 wikilink 相连，无坏链

## 中间文件清理 / 忽略规则（初始化后强制）

> 目的：确保 Obsidian 图谱中**只出现文章节点**（学科全景 / 章 / 节 / 概念），
> 不出现说明文件、教材源材料、初始化输入、临时文件等中间文件。

### 中间文件清单（发现即补充）

| 文件 / 目录 | 性质 | 处理 |
|-------------|------|------|
| `assets/{学科}/seed/README.md` | 目录说明 | **忽略**（`**/README.md`），或移出 vault |
| `assets/{学科}/seed/textbook/**` | 教材 OCR 源材料 | **忽略**（`**/textbook/**`、`assets/*/seed/textbook/**`） |
| `assets/{学科}/seed/*.xlsx` 等图谱源文件 | 初始化输入（可能含版权） | **导入完成后立即删除**；如暂不删除则至少忽略（`**/*.xlsx`），且不得提交 |
| `_index.md`（任意层级） | 旧索引 | **忽略** + **禁止生成**（`**_index.md`、`**/_index.md`） |
| `theorems.md` / `problems.md` | 旧固定库文件 | **删除** / **禁止生成**（新架构不用固定合集） |
| `_checkpoints/` | 学生临时快照 | **忽略**（`_checkpoints/`、`**/_checkpoints/**`），不入图谱 |
| `_session/`、`_archive/`、`_demo-vault/` | 会话 / 归档 / 演示 | **忽略**（已配置） |
| `未命名.base` 等运行时文件 | 本地运行时 | **忽略**（`**/*.base`） |
| `.obsidian/*.json` | Obsidian 配置 | **忽略**（非 md，天然不入图谱） |

### 强制规则

1. 初始化产物**只允许文章节点**（`.md`：学科全景 / 章 / 节 / 概念）
2. 非文章 `.md`（说明 / README）必须被 `userIgnoreFilters` 忽略，或移出 vault
3. 初始化完成后做“图谱卫生检查”：
   - Obsidian 图视图只出现文章节点
   - 脚本检查无孤立文章节点（孤立节点只能是已被忽略的非文章文件）
4. 忽略规则统一维护在 `.obsidian/app.json` 的 `userIgnoreFilters`
5. 后续初始化遇到新的中间文件类型 → **加入本表 + app.json**，不遗漏


---

## 初始化经验记录（实测 2026-08-27，写入规则）

> 来源：概率论与数理统计 seed 初始化（某现成知识图谱 xlsx）。以下经验应作为后续任意学科初始化的默认做法。

### 1. 来源模式（三选一）

| 模式 | 输入 | 做法 |
|------|------|------|
| A 现成图谱 | 现成图谱（xlsx / md 图谱） | 导入并校验，AI 不擅自增删内容；**导入完成并生成 seed 后删除源文件**（版权内容不保留） |
| B 教材初始化 | 教材 OCR | 全量生成 学科概览 + Ch 骨架（见上文流程） |
| C 空 seed | 无教材、无图谱 | 允许 seed 为空，学习从 personal 直接生长 |

### 2. 现成图谱导入（Excel 模板经验）

- 模板列 A-H 表示层级：**每个节点只填一列**，列位置=深度（B=章，C=节，D 起=更细分类/知识点）
- 类型：`分类` 与 `知识点` 两种；分类是容器，知识点是叶子
- 映射到本项目文章类型：
  - 深度 1 分类 → `Ch{N} {名}.md`（章）
  - 深度 2 分类 → `Sec{N.M} {名}.md`（节）
  - 深度 ≥3 分类 & 知识点 → `概念-{名}.md`（概念）
- 表内 I/J/K 列 = 前置 / 后置 / 关联 → **全部转成 wikilink**（多节点用 `;` 分隔）
- **重名消歧**：同章节优先；仍重名则加 父级名 或 `（Ch{N}）` 后缀
- **疑似错别字不擅自改**：如现成图谱第 5 章「大数定量」，应保留原文并记录/询问，不静默修正

### 3. 图谱链接层级（决定节点大小）

- **章只链直接下级（节）**，节只链直接下级（概念）
- 后代保留为**纯文本清单**（不写 `[[…]]`），避免章出现几十上百条出链
- 效果：学科概览（只连 8 章）= 最大枢纽；否则章会因全量子节点链接而异常放大
- 初始化后校验：0 坏链、无孤立文章节点（README 等中间文件除外）

### 4. 图谱样式配置

- Obsidian 原生**节点大小由链接数决定**，不支持按类型设大小；通过 3 的层级链接让概览自然最大
- **颜色分组用检索式配置**（`.obsidian/graph.json` → `colorGroups`）
- **配色规则（强制区分 seed / personal + 层级/类型）**：
  - **seed 类**：低饱和 / 沉稳色，表示共享只读地基；按层级区分色相
  - **personal 类**：高饱和 / 鲜艳色，表示个人增量；按文章类型区分色相
- **初始化自动执行**（无需手动）：`python tools/graph-style/configure.py`
  - 默认配色：
    - seed：学科全景 `#B0717A`／章 `#5C7A99`／节 `#6B8E6B`／概念 `#78909C`
    - personal：学科全景 `#FF1744`／章 `#2979FF`／节 `#00C853`／概念 `#FF9100`／论文 `#D500F9`／思考 `#FF6D00`／提问 `#651FFF`／习题 `#00E5FF`／作业 `#76FF03`／问题 `#F50057`
  - 脚本用 `path:seed` / `path:personal` 结合 `file:` 检索式，按目录 + 文件名区分，任意学科通用
- 也可在 **Obsidian 图视图 → 设置 → 颜色分组** 手动增改（UI 会写回 `graph.json`，格式为 `{"query":"...","color":{"a":1,"rgb":N}}`）

### 5. 中间文件清理/忽略（重要教训）

- Obsidian `userIgnoreFilters` 的 **`**` 通配不可靠**（README/part1 仍入图）
- 必须用**显式路径**：根文件写文件名，目录写 `folder/`，例如：
  - `README.md`、`CHANGELOG.md`、`CLAUDE.md`、`AGENTS.md`、`ARCHITECTURE.md`
  - `.claude/` `.codex/` `.trae/` `rules/` `templates/` `guide/` `tools/` `maintenance/` `_archive/` `_session/` `_checkpoints/` `_demo-vault/`
  - `assets/README.md`、`assets/{学科}/seed/README.md`、`assets/{学科}/seed/textbook/`
  - `未命名.canvas`、`未命名.base`
- 图谱中只应出现文章节点（Ch/Sec/概念/学科概览）；README、CHANGELOG、textbook、json、base、canvas 全部忽略；xlsx 等版权源文件导入后删除
- 每次初始化后做“图谱卫生检查”，新中间文件类型 → 加入本文件清单 + `.obsidian/app.json`

### 6. 初始化验收（含本次新增）

- [ ] 学科概览四要素齐全（占位也需有章节导航）
- [ ] 全量 Ch 骨架生成（每学科一次，无生命周期）
- [ ] 图谱层级：学科概览 → Ch → Sec → 概念，边只在相邻层
- [ ] 现成图谱关系（前置/后置/关联）全部转为 wikilink
- [ ] 0 坏链，无孤立文章节点
- [ ] 中间文件已忽略（README/textbook/xlsx/base/canvas）
- [ ] 配色分组已自动配置（`python tools/graph-style/configure.py`，path + file 检索式）


> **实测结论（2026-08-27）**：直接改 `.obsidian/graph.json` 可能被运行中的 Obsidian 覆盖/不生效；
> 用 **`obsidian eval` + `app.vault.adapter`** 让 Obsidian 自己读写 `graph.json` 可**实时生效且不被覆盖**（已验证 `ok:4`）。
> 初始化配色建议：`tools/graph-style/configure.py` 写文件 + `obsidian eval` 触发重载（或直接用 eval 写回）。

### 7. Obsidian CLI（用法唯一来源：`tools/obsidian-cli.md`）

> CLI 用法细节已收敛到 **`tools/obsidian-cli.md`**（实测 2026-08-29，Obsidian 1.13.7）：启用与验证、核心概念（多 vault / `path=` 优先 / 转义）、命令速查、全库体检（`unresolved` / `orphans` / `deadends`）、AI 建笔记标准回路、踩坑清单与 Python 调用模板。本节原先的命令示例停止维护（M5 单一来源）。

- 初始化批量操作要点：多 vault 环境所有命令必须显式 `vault=<名称>`，写库前先 `obsidian vaults verbose` 确认目标库
- 图谱样式实时生效做法见上文「实测结论」（`obsidian eval` + `app.vault.adapter`）

