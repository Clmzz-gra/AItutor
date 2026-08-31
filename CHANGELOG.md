# Changelog

## 0.2.4 — 2026-08-31

### 易用化升级（学生端少设置 + 默认免费 token）
- 新增一键环境安装：`tools/setup/bootstrap.ps1` / `bootstrap.sh` + `tools/setup/README.md`，一条命令装好 Git / Python / Obsidian / Obsidian CLI / 可选 harness
- 新增 Windows 学生入口**根目录 `一键安装.bat`**：只要求“解压 + 双击”，无需输入命令；修复 bootstrap.ps1 编码（加 UTF-8 BOM）保证 PowerShell 解析可靠
- 新增环境/仓库体检脚本 `tools/doctor.py`：坏链、孤立节点、frontmatter、未闭合 TOPIC、临时残留、默认免费模型提示，并输出“下一步怎么做”
- 学生端**默认免费模型定为 GLM-4.5-Flash**（免费档中能力最强、完全免费）：README 快速开始、`guide/学生使用指南.md`、`guide/免费模型配置.md` 统一口径，只需申请一次 Key
- 校准智谱免费模型配置：对照 [GLM-4.5-Flash 官方文档](https://docs.bigmodel.cn/cn/guide/models/free/glm-4.5-flash) 将默认模型名设为 `glm-4.5-flash`，上下文窗口 `128000` / 最大输出 `96000` 写入 ZCode 填表速查；保留旧免费档 `glm-4-flash-250414` / `glm-4-flash` 作为兼容备选，Base URL 维持 OpenAI 兼容 `https://open.bigmodel.cn/api/paas/v4/`
- **默认 harness 定为 ZCode**（最简，原生读 `AGENTS.md`）：README、学生指南、setup 文档与 bootstrap 脚本同步推荐；Claude Code / Codex 改为**按需安装**（脚本只给出 npm 命令，不再自动装）
- README 快速开始精简为“克隆 → 一键装环境 → 装 harness → 配免费模型 → doctor 自检”，减少学生手动设置；并进一步面向“只会解压和打开文件”的用户（下载 ZIP → 解压 → 双击根目录 `一键安装.bat`）
- README 补充国内托管提示（GitHub 不稳定时可改用 Gitee / GitCode），并升级版本号 0.2.4
- ZCode 不做检测，仅提供官网链接 https://zcode.z.ai/（不再误报/不再自动打开）
- 所有 harness 均不做检测，只列出官方网址（ZCode / Claude Code / Codex / dsh / Trae）
- 新增根目录 `体检.bat`；一键安装结束后自动运行 doctor 体检
- 修复输出乱码：bat 统一 ASCII + `chcp 65001`，doctor.py 统一 UTF-8 输出，PowerShell 设 UTF8 OutputEncoding，全链路统一编码
- 一键安装新增 **MinerU CLI**（`pip install mineru-open-api`，教材 OCR / PDF → Markdown）
- 修复安装可靠性：MinerU 依次尝试 清华/阿里/中科大/豆瓣/官方 多个 pip 源；Obsidian 依次尝试 winget → choco → scoop → 浏览器手动下载，只要一个成功即可
- 新增网页版图文安装教程 `install.html`（可放截图，降低使用门槛）
- 移除本地安装向导 `安装向导.hta`（HTA 在部分环境报错，改为直接双击根目录 `一键安装.bat`，`install.html` 已写详细图文步骤）

## 0.2.3 — 2026-08-29

### 新能力
- 集成 Obsidian CLI 用法规范（`tools/obsidian-cli.md`，实测 Obsidian 1.13.7）：命令速查、全库体检（unresolved / orphans / deadends）、AI 建笔记标准回路、踩坑清单、Python 调用模板

### 规则
- AGENTS.md 工作方式新增：**中文优先**（面向中文用户，对话/文章/文档/提交信息全链路简体中文）、**Obsidian 优先**（vault 操作优先 CLI，建笔记按标准回路）
- init-spec §7 原 CLI 命令示例收敛为指针（M5 单一来源），移除本机环境状态记录

### 适配
- 中文优先 / Obsidian 优先提升为**注入级规则**：CLAUDE.md / `.codex/` / `.trae/` 入口的强制工作方式与指针表同步，五个 harness 开场即生效

### 其他
- README 可用功能表 / 结构树 / `tools/README.md` 索引登记 Obsidian CLI 指南

## 0.2.2 — 2026-08-29

### 规则增强（借鉴 DeepTutor 工程设计）
- 习题生成：新增出题质量四则——考辨析不复述、干扰项对应常见误解且与正确项风格相当、绝不暗示答案、解析出题时写全
- 成文判定：§1 增加费曼复述双向信号——能讲清楚=强建议升级，讲卡壳=建议继续讨论（不判分、不记录）
- 答案隔离：学生明示"先自己答"后，答案与解析不进入学生可见文本（exercise-generator + tutor）
- 注入卫生：article-generation 新增"外部材料进入上下文（强制）"——外部材料以数据身份入上下文，指令性文字不改变 AI 行为
- checkpoint：新增「未决问题」段（asset-spec 单一来源），新对话/恢复时问题级对账（decision-trees §5·5 + tutor）
- 学习画像：周报 AI 解读/建议中每条定性判断须脚注引用 wikilink 节点作证据（profile.md + 周报模板）
- tutor：新增依赖触发唤醒——前置知识一句话织入讲解唤醒，不设复习日程、不做掌握度记录

### 适配
- 新增 ZCode harness 适配：原生读取 `AGENTS.md`，免指针目录（`rules/core/harness/adapters/zcode.md`）

### 其他
- `.gitignore` 忽略外部参考仓库克隆目录 `_references/`（第三方参考，不随仓库发布）

## 0.2.1 — 2026-08-27

### 修复与改进
- 快速开始 Obsidian/CLI 步骤改为中文说明 + 官方英文原文引用
- `CHANGELOG.md` 加入图谱忽略列表
- 图谱配色扩展为 seed 低饱和 × 层级、personal 高饱和 × 类型
- 新增文章类型扩展通道，便于二次开发扩展
- 移除教师/学校来源表述，统一改为现成/已有 seed

## 0.2.0 — 2026-08-27

### 架构与模式
- 移除五阶段管线残留，正式切换为图管理模式：初始化 → 创建文章 → 维护文章
- 文章类型定为 10 类，取消 `_index.md`、`theorems.md`、`problems.md` 等旧结构
- 10 类文章结构规范细化，补齐全部模板
- “是否成文”判定改为：AI 不判断价值，checkpoint 安全默认，用户确认升级

### 新能力
- 新增 `exercise-generator` skill：出题 + 答案折叠，不做检验
- 新增官方 Obsidian CLI 支持：Settings → About → Command line interface
- 新增图谱颜色分组自动配置工具：`tools/graph-style/configure.py`
- `analyze.py` 增加 frontmatter 读取与概览输出

### 初始化
- 完成概率论与数理统计 seed 初始化（8 章 / 33 节 / 337 概念）
- 初始化规范加入现成知识图谱 xlsx 导入后立即删除的版权处理规则

### 发布整理
- `_archive/` 仅发布占位说明，历史归档内容不再随仓库发布
- 移除本机路径、学校机构名等非通用信息
- 添加 CC BY-NC 4.0 许可证：允许学习研究，禁止商用