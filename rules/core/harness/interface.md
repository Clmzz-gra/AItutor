# Harness 抽象接口（interface）

> 定义"一套规则如何被任意 harness 加载和执行"的通用接口。
> 核心规则 · 学科无关。

## 接口维度

| 维度 | 说明 |
|------|------|
| **加载入口** | 规则/skill 如何被 harness 发现并加载 |
| **状态读写** | 文章定位 / checkpoint 如何读写 |
| **文件访问** | 资产/教材/图谱如何访问 |
| **能力声明** | 该 harness 支持哪些能力（OCR/执行/可视化…） |
| **每轮注入** | 是否支持每轮注入（如系统提示 section） |

## 适配清单

> 适配方式统一为**指针注入**：各 harness 入口文件只放指针，引向全量文件（根 `AGENTS.md` + `rules/` + `.dsh/skills/`），不复制规则正文（单一来源 M5）。

| harness | 入口文件（指针注入） | 适配文件 | 状态 |
|---------|---------------------|---------|------|
| dsh | `AGENTS.md`（根） | `adapters/dsh.md` | ✅ 已适配 |
| claude code | `CLAUDE.md` | `adapters/claude-code.md` | ✅ 已适配 |
| codex | `.codex/AGENTS.md` | `adapters/codex.md` | ✅ 已适配 |
| trae | `.trae/rules/AGENTS.md` | `adapters/trae.md` | ✅ 已适配 |
