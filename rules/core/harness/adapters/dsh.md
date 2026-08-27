# Harness 适配：dsh（DeepSeek harness）

> 适配方式：**指针注入**（入口只放指针，引向全量文件，单一来源 M5）。

## 加载入口
- 项目指令：`AGENTS.md`（根，host 自动注入，基线 + 变更时）
- 项目级 skill：`.dsh/skills/<kebab-name>/SKILL.md`
- 全量规则：`rules/` + `.dsh/skills/`

## 指针注入内容
- 根 `AGENTS.md` 只含：本职定义 + 规则单一来源指针表 + 管线引用 + 工作方式
- 不复制规则正文，规则变更只改唯一来源

## 状态读写
- 通过文件系统工具读写 `_checkpoints/` 与文章目录

## 能力声明
- 支持 skill 目录、AGENTS.md、MCP
- 支持系统提示 section（可做每轮注入）

## 每轮注入
- ✅ 支持（自定义插件注册 systemPrompt section）
