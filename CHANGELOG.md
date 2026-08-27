# Changelog

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