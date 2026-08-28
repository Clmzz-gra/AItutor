# Changelog

## 本地调整 — 2026-08-28

### 学科调整
- 清空预设学科：移除 `rules/subjects/实变函数与泛函分析/`、`rules/subjects/概率论与数理统计/` 及对应 `assets/` 占位
- 新增雅思学科包：`rules/subjects/雅思/`（config / case / capabilities / curriculum / studyhelper-method）+ `assets/雅思/` 目录结构；seed 含占位 `学科概览.md`
- 雅思学科拓展参考 `E:\StudyHelper\skills\ielts\SKILL.md` 方法论撰写
- 雅思长期仅保留：听读回抄法、串词成文、引导精读/扫盲式阅读；其他 StudyHelper 方法静默，不追踪进度
- 新增扩展文章类型：`每日外刊`、`阅读真题`（基础结构为原文 + Expression Library）
- 接入文章类型扩展通道：核心规范、模板、图谱配色、生成方式已补齐
- 同步更新 README、ARCHITECTURE、guide、tools 索引与 Obsidian 忽略规则

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