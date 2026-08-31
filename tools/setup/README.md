# AItutor 一键环境安装（tools/setup）

> 目标：让学生**少操作设置**，跑一条命令装好 Git / Python / Obsidian / Obsidian CLI / 可选 AI harness，
> 再按默认免费模型配置好 token 即可开始学习。
>
> **单一来源**：安装命令以本目录脚本为准；免费模型配置以 `guide/免费模型配置.md` 为准；环境自检以 `tools/doctor.py` 为准。

## 快速开始（学生版：只会解压和打开文件）

### Windows
1. 下载本项目为 **ZIP** 并**解压**。
2. **双击解压后项目根目录的 `一键安装.bat`**（就在根目录，很好找）。
3. 什么都不用输入，等它自动装完（脚本会自动装 Git / Python / Obsidian / Obsidian CLI）。
4. 装完后按窗口提示操作即可。

> 说明：脚本**不做任何 harness 检测**，只列出各 harness 官方网址；Claude Code / Codex 按需手动安装（默认不装）。
> 一键安装结束会自动运行体检（doctor）；也可以随时双击根目录的 `体检.bat`。
> 进阶：管理员/助教也可在命令行运行 `tools\setup\install.bat -CheckOnly`（只体检）或 `-Global`（国际源）。
> `tools\setup\一键安装.bat` 是同一个入口的备份位置。

### macOS / Linux / Git Bash
```bash
# 1. 只体检，不安装（可选）
bash tools/setup/bootstrap.sh --check

# 2. 一键安装缺失项（默认国内加速）
bash tools/setup/bootstrap.sh
```

> 需要走国际官方源时：PowerShell 加 `-Global`，bash 加 `--global`。

## 脚本会自动检查 / 安装什么
1. **Git** —— 话题生命周期 / 防丢失
2. **Python 3** —— `tools/doctor.py`、学习画像、演示工具
3. **MinerU CLI** —— 教材 OCR / PDF → Markdown（`pip install mineru-open-api`）
4. **Obsidian** —— 笔记与知识图谱（桌面端）
5. **Obsidian CLI** —— AI 管理 vault 的通道（需在 Obsidian 界面开启一次：Settings → About → Command line interface）
6. **AI harness（默认推荐 ZCode，不检测）** —— 脚本只列出各 harness 官方网址（ZCode / Claude Code / Codex / dsh / Trae）；Claude Code / Codex 按需手动安装。

## 安装后（学生只需 3 步；默认推荐 ZCode）
0. **装 AI harness（默认 ZCode，最简）**：用 ZCode 官方渠道安装（官网 https://zcode.z.ai/，脚本不做任何检测、只给链接）；Claude Code / Codex 按需手动安装（脚本只给命令，不再自动装）。
1. **打开本仓库为 Obsidian vault**：Obsidian → Open folder as vault → 选项目根目录
2. **确认 CLI**：`obsidian help` 能正常输出
3. **配默认免费模型**：申请一个智谱 GLM-4.5-Flash Key（免费档中能力最强、永久免费），把 Base URL / Key / 模型名填进你的 harness，详见 `guide/免费模型配置.md`

### 自检
```bash
python tools/doctor.py          # 完整体检（环境 + 图谱 + 未闭合 TOPIC + 临时残留）
python tools/doctor.py --env-only   # 只看本机环境
python tools/doctor.py --repo-only  # 只看图谱/仓库健康
```
> doctor 会告诉你“缺什么、怎么修、下一步做什么”，学生不用记一堆命令。

## 参数说明
| 脚本 | 参数 | 作用 |
|------|------|------|
| `一键安装.bat` | （无） | 学生入口：双击即可自动安装（推荐） |
| `install.bat` | `-CheckOnly` | 只体检，不安装（Windows 命令行） |
| `install.bat` | `-Global` | 切国际官方源（Windows） |
| `bootstrap.ps1` | `-CheckOnly` | 只体检，不安装 |
| `bootstrap.ps1` | `-Global` | 切国际官方源（默认国内加速） |
| `bootstrap.sh` | `--check` | 只体检，不安装 |
| `bootstrap.sh` | `--global` | 切国际官方源 |

## 与相关文件的关系
- 免费模型默认配置（GLM-4.5-Flash，免费档中能力最强）：`guide/免费模型配置.md`
- 免费模型环境变量模板：`tools/setup/glm4flash.env.example`
- 环境/仓库自检：`tools/doctor.py`
- Obsidian CLI 用法：`tools/obsidian-cli.md`
