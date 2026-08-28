# Changelog

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