# Harness 适配：Claude Code

> 适配方式：**指针注入**（入口只放指针，引向全量文件，单一来源 M5）。

## 加载入口
- 项目指令：`CLAUDE.md`（Claude Code 自动注入）
- 全量规则/本职：项目根 `AGENTS.md`（唯一权威）+ `rules/` + `.dsh/skills/`

## 指针注入内容
- `CLAUDE.md` 只含：本职指针 + 规则单一来源指针表 + 强制工作方式
- 不复制任何规则正文，规则变更只改唯一来源

## 状态读写
- 通过文件系统工具读写 `_checkpoints/` 与文章目录

## 能力声明
- 支持 skill 目录、CLAUDE.md、MCP、文件系统工具

## 每轮注入
- ✅ `CLAUDE.md` 为项目指令，Claude Code 自动注入（基线）
- 如需每轮动态注入，可用自定义 hook 增强（可选）
