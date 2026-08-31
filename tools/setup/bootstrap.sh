#!/usr/bin/env bash
# AItutor 一键环境安装（macOS / Linux / Git Bash）
# 用法：bash tools/setup/bootstrap.sh [--check] [--global]
#   --check   只体检，不安装
#   --global  切国际官方源（默认【国内加速】：不翻墙；Claude/Codex npm 按需手动装）
# 安装方法唯一来源：tools/setup/README.md
set -u

CHECK_ONLY=0
CHINA=1
for a in "$@"; do
  case "$a" in
    --check)  CHECK_ONLY=1 ;;
    --global) CHINA=0 ;;
  esac
done

ok()   { printf '  \033[32m[OK]\033[0m %s\n' "$1"; }
miss() { printf '  \033[33m[缺]\033[0m %s\n' "$1"; }
tip()  { printf '  \033[90m[提示]\033[0m %s\n' "$1"; }
step() { printf '\n== %s ==\n' "$1"; }
have() { command -v "$1" >/dev/null 2>&1; }

case "$(uname -s)" in
  MINGW*|MSYS*|CYGWIN*) OS=windows ;;
  Darwin)               OS=mac ;;
  *)                    OS=linux ;;
esac

# ---- 0. 选择安装渠道 ----
step "选择安装渠道（$OS）"
PKG=none
case "$OS" in
  mac)
    if have brew; then PKG=brew; ok "brew 可用"
    else PKG=none; miss "未检测到 Homebrew"; tip "可先装 brew：https://brew.sh （或按下方手动地址安装）"; fi
    if [ "$CHINA" = 1 ]; then
      tip "brew 国内加速（可选，写入 ~/.zshrc 后重开终端）："
      tip '  export HOMEBREW_API_DOMAIN="https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles/api"'
      tip '  export HOMEBREW_BOTTLE_DOMAIN="https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles"'
    fi ;;
  windows)
    if have winget; then PKG=winget; ok "winget 可用（Git Bash 内调用）"
    else PKG=none; miss "未检测到 winget"; tip "也可改用 PowerShell 运行 tools/setup/bootstrap.ps1（国内镜像直链）"; fi ;;
  linux)
    if have apt-get; then PKG=apt; ok "apt 可用（国内可换阿里云/清华源加速）"
    else PKG=none; miss "未检测到 apt-get"; tip "请用你的发行版包管理器手动安装"; fi ;;
esac

winget_install() { # $1 = 包 id
  winget install --id "$1" -e --silent --accept-source-agreements --accept-package-agreements
}

# ---- 1. Git ----
step "检查 Git（话题生命周期 / 防丢失依赖）"
if have git; then
  ok "已安装（$(git --version 2>/dev/null)）"
else
  miss "未安装"
  if [ "$CHECK_ONLY" = 0 ]; then
    case "$PKG" in
      brew)   brew install git && ok "安装完成" ;;
      apt)    sudo apt-get update && sudo apt-get install -y git && ok "安装完成" ;;
      winget) winget_install "Git.Git" && ok "安装完成（重开终端后生效）" ;;
      *)      tip "手动安装：https://git-scm.com/downloads" ;;
    esac
  else
    tip "brew: brew install git ｜ apt: sudo apt install git ｜ win: winget Git.Git"
  fi
fi

# ---- 2. Python ----
step "检查 Python 3（学习画像 / 辅助脚本）"
if have python3 || have python; then
  ok "已安装（$(python3 --version 2>/dev/null || python --version 2>/dev/null)）"
else
  miss "未安装"
  if [ "$CHECK_ONLY" = 0 ]; then
    case "$PKG" in
      brew)   brew install python3 && ok "安装完成" ;;
      apt)    sudo apt-get update && sudo apt-get install -y python3 && ok "安装完成" ;;
      winget) winget_install "Python.Python.3.13" && ok "安装完成（重开终端后生效）" ;;
      *)      tip "手动安装：https://www.python.org/downloads/" ;;
    esac
  else
    tip "brew: brew install python3 ｜ apt: sudo apt install python3 ｜ win: winget Python.Python.3.13"
  fi
fi

# ---- 2.5 MinerU CLI（教材 OCR / PDF → Markdown，可选） ----
step "检查 MinerU CLI（教材 OCR 用，可选）"
PY_CMD=""
if have python3; then PY_CMD=python3; elif have python; then PY_CMD=python; fi
if have mineru-open-api || have mineru; then
  ok "MinerU CLI 已安装"
elif [ "$CHECK_ONLY" = 0 ] && [ -n "$PY_CMD" ]; then
  tip "正在安装 MinerU CLI（pip install mineru-open-api）..."
  "$PY_CMD" -m pip install --quiet mineru-open-api && ok "MinerU CLI 安装完成" || miss "安装失败，可手动：pip install mineru-open-api"
elif [ -n "$PY_CMD" ]; then
  miss "MinerU CLI 未安装"; tip "安装命令：pip install mineru-open-api（详见 https://mineru.net/ecosystem?tab=cli）"
else
  miss "未检测到 Python，无法安装 MinerU CLI"; tip "先安装 Python"
fi

# ---- 3. Obsidian 本体（官方无国内镜像，安装包在 GitHub） ----
step "检查 Obsidian（笔记与知识图谱）"
obsidian_installed=0
if [ "$OS" = mac ] && [ -d "/Applications/Obsidian.app" ]; then obsidian_installed=1; fi
if [ "$OS" = windows ] && [ -n "${LOCALAPPDATA:-}" ] && [ -e "$LOCALAPPDATA/Obsidian/Obsidian.exe" ]; then obsidian_installed=1; fi
if have obsidian; then obsidian_installed=1; fi

if [ "$obsidian_installed" = 1 ]; then
  ok "Obsidian 已安装"
else
  miss "未安装（官方无国内镜像，下载走 GitHub，极慢时用浏览器/多线程下载器兜底）"
  if [ "$CHECK_ONLY" = 0 ]; then
    case "$PKG" in
      brew)   brew install --cask obsidian && ok "安装完成" ;;
      winget) winget_install "Obsidian.Obsidian" && ok "安装完成" ;;
      *)      tip "手动下载：https://obsidian.md/download（Linux 提供 .deb/AppImage）" ;;
    esac
  else
    tip "mac: brew install --cask obsidian ｜ win: winget Obsidian.Obsidian ｜ 手动：https://obsidian.md/download"
  fi
fi

# ---- 4. Obsidian CLI（不能全自动，给出精确步骤） ----
step "检查 Obsidian CLI（AI 管理 vault 的通道）"
if have obsidian; then
  ok "Obsidian CLI 可用"
elif [ "$obsidian_installed" = 1 ]; then
  miss "Obsidian 已装但 CLI 未开启（需在界面操作一次）"
  tip "打开 Obsidian → Settings → About → Command line interface → 按提示注册 → 重启终端"
  tip "验证命令：obsidian help ；详见 tools/obsidian-cli.md 第 1 节"
else
  miss "Obsidian 未安装，装好后按上述步骤开启 CLI"
fi

# ---- 5. AI harness（不做检测，直接给官网） ----
step "AI harness（不做检测，已装哪个你自己最清楚）"
tip "ZCode（默认推荐）：https://zcode.z.ai/"
tip "Claude Code：https://docs.anthropic.com/en/docs/claude-code/"
tip "Codex CLI：https://github.com/openai/codex"
tip "dsh（DeepSeek harness）：按你的获取渠道安装（平台 https://platform.deepseek.com/）"
tip "Trae：https://www.trae.ai"

if [ "$CHECK_ONLY" = 0 ]; then
  tip "Claude Code / Codex CLI 如需安装，按需手动执行（国内自动用 npmmirror 源）："
  if [ "$CHINA" = 1 ]; then
    tip "  Claude Code: npm install -g @anthropic-ai/claude-code --registry=https://registry.npmmirror.com"
    tip "  Codex CLI:   npm install -g @openai/codex --registry=https://registry.npmmirror.com"
  else
    tip "  Claude Code: npm install -g @anthropic-ai/claude-code"
    tip "  Codex CLI:   npm install -g @openai/codex"
  fi
  tip "需要 Node.js/npm 前置；默认推荐 ZCode，一般无需安装 Claude Code / Codex。"
fi

# ---- 6. 下一步 ----
step "下一步"
tip "1) 用 Obsidian 打开本仓库根目录（作为 vault）"
tip "2) 确认 obsidian help 可正常输出（CLI 已开启）"
tip "3) 运行体检：python3 tools/doctor.py"
tip "4) 对 AI 说『开始学习〈学科名〉』即可进入学习模式"
