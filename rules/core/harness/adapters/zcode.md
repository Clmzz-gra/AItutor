# Harness 适配：ZCode

> 适配方式：**原生注入**（ZCode 原生读取项目根 `AGENTS.md`，无需额外指针文件，单一来源 M5）。

## 加载入口
- 项目指令：项目根 `AGENTS.md`（ZCode 作为 workspace 指令自动注入，即唯一权威，非指针复制）
- 全量规则/本职：`AGENTS.md`（唯一权威）+ `rules/` + `.dsh/skills/`

## 指针注入内容
- 无需 `CLAUDE.md` 式额外指针文件：ZCode 直接注入 `AGENTS.md` 全文
- 不复制任何规则正文，规则变更只改唯一来源

## 状态读写
- 通过文件系统工具读写 `_checkpoints/` 与文章目录
- git / shell 可用，TOPIC OPEN/CLOSE 生命周期照常执行

## 能力声明
- 支持文件系统工具、git、shell、子代理调度、MCP
- 无 Obsidian 强依赖（图谱查看仍建议 Obsidian）

## 每轮注入
- ✅ `AGENTS.md` 每轮自动注入（2026-08-29 实测：P0/P1 新规则会话内可加载并执行）

## 已知注意（免费模型）
- **免费/弱模型（如 GLM-4.5-Flash）可能不严格遵循注入的 `AGENTS.md`**，而倾向去读根目录最显眼的 `README.md`。
- 缓解：`README.md` 顶部已加「给 AI 的提示」指针，引导模型先读 `AGENTS.md`；若仍不生效，请在 ZCode 里确认「项目指令 / workspace instructions / AGENTS.md」注入开关已开启。
