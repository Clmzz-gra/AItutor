#Requires -Version 5.1
<#
.SYNOPSIS
  AItutor 一键环境安装（Windows，无需任何前置，系统自带 PowerShell 即可运行）
.DESCRIPTION
  默认【国内加速模式】：Git 走 npmmirror 二进制镜像、Python 走华为云镜像，
  全程不翻墙、高速稳定；加 -Global 切换国际官方源。
  Claude Code / Codex（npm）改为按需安装：脚本只给命令，不自动装。
  Obsidian 官方无国内镜像（安装包托管在 GitHub），脚本走 winget 官方渠道，
  极慢时给出手动兜底建议。
  Obsidian CLI 开启需在 Obsidian 界面操作一次，脚本会给出精确步骤。
  安装方法唯一来源：tools/setup/README.md
.EXAMPLE
  powershell -ExecutionPolicy Bypass -File tools\setup\bootstrap.ps1 -CheckOnly   # 只体检，不安装
  powershell -ExecutionPolicy Bypass -File tools\setup\bootstrap.ps1              # 国内加速，安装缺失项
  powershell -ExecutionPolicy Bypass -File tools\setup\bootstrap.ps1 -Global      # 国际官方源
#>
param(
    [switch]$CheckOnly,
    [switch]$Global
)

$ErrorActionPreference = "Continue"
$ProgressPreference = "SilentlyContinue"   # PS5.1 不关进度条时下载慢数倍
try { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 } catch {}
try { [Net.ServicePointManager]::SecurityProtocol = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12 } catch {}

$China = (-not $Global)
$Script:PyVer   = "3.13.7"        # 国内镜像直链固定版本（华为云），失败回退 winget

function Write-Step($msg) { Write-Host "`n== $msg ==" -ForegroundColor Cyan }
function Write-Ok($msg)   { Write-Host "  [OK] $msg" -ForegroundColor Green }
function Write-Miss($msg) { Write-Host "  [缺] $msg" -ForegroundColor Yellow }
function Write-Tip($msg)  { Write-Host "  [提示] $msg" -ForegroundColor Gray }
function Have($cmd)       { return [bool](Get-Command $cmd -ErrorAction SilentlyContinue) }
function Open-Url($url) {
    try { Start-Process $url } catch { Write-Tip "请手动打开：$url" }
}

function Download-File($url, $out) {
    try {
        Invoke-WebRequest -Uri $url -OutFile $out -UseBasicParsing -TimeoutSec 600
        return $true
    } catch {
        Write-Tip "下载失败：$url"
        return $false
    }
}

function Install-GitChina {
    # npmmirror（阿里巴巴维护）的 git-for-windows 二进制镜像，国内高速稳定
    try {
        $api = "https://registry.npmmirror.com/-/binary/git-for-windows/"
        $dirs = @(Invoke-RestMethod -Uri $api -TimeoutSec 30 | Where-Object { $_.name -match '^v\d+(\.\d+)*\.windows\.\d+/?$' })
        if ($dirs.Count -eq 0) { throw "镜像目录列表为空" }
        $latest = ($dirs | ForEach-Object { $_.name.Trim('/') } |
            Sort-Object { [version](($_ -replace '^v','') -replace '\.windows\.','.') } -Descending |
            Select-Object -First 1)
        $files = @(Invoke-RestMethod -Uri "$api/$latest/")
        $exe = ($files | Where-Object { $_.name -match '^Git-.*-64-bit\.exe$' } | Select-Object -First 1).name
        if (-not $exe) { throw "未找到安装包" }
        $url = "$api/$latest/$exe"
        Write-Host "  国内镜像下载（npmmirror）：$url"
        $tmp = Join-Path $env:TEMP $exe
        if (-not (Download-File $url $tmp)) { throw "下载失败" }
        Write-Host "  静默安装中（约 1-3 分钟）…"
        Start-Process -FilePath $tmp -ArgumentList "/VERYSILENT /NORESTART /NORUN" -Wait
        Write-Ok "Git 安装完成（重开终端后生效）"
        return $true
    } catch {
        Write-Tip "国内镜像通道失败（$($_.Exception.Message)），改用 winget…"
        return $false
    }
}

function Install-PythonChina {
    # 华为云镜像直链（python.org 官方安装包的国内镜像）
    $url = "https://mirrors.huaweicloud.com/python/$Script:PyVer/python-$Script:PyVer-amd64.exe"
    Write-Host "  国内镜像下载（华为云）：$url"
    $tmp = Join-Path $env:TEMP "python-$Script:PyVer-amd64.exe"
    if (-not (Download-File $url $tmp)) { return $false }
    Write-Host "  静默安装中（约 1-2 分钟）…"
    Start-Process -FilePath $tmp -ArgumentList "/quiet InstallAllUsers=0 PrependPath=1 Include_test=0" -Wait
    Write-Ok "Python 安装完成（重开终端后生效）"
    return $true
}

$obsidianExe = Join-Path $env:LOCALAPPDATA "Obsidian\Obsidian.exe"
$obsidianInstalled = (Test-Path $obsidianExe) -or (Have "obsidian")

Write-Step "网络模式"
if ($China) { Write-Ok "国内加速（默认，不翻墙）：Git=npmmirror｜Python=华为云（Claude/Codex 按需手动装 npm）" }
else        { Write-Ok "国际官方源（-Global）" }

# ---- 0. winget 可用性（作为回退渠道） ----
Write-Step "检查 winget（回退安装渠道）"
$haveWinget = Have "winget"
if ($haveWinget) { Write-Ok "winget 可用" }
else { Write-Miss "未检测到 winget"; Write-Tip "镜像直链仍可用；如需 winget 可安装 App Installer：https://aka.ms/getwinget" }

# ---- 1. Git ----
Write-Step "检查 Git（话题生命周期 / 防丢失依赖）"
if (Have "git") {
    Write-Ok "已安装（$((git --version) 2>$null)）"
} elseif ($CheckOnly) {
    Write-Miss "未安装"; Write-Tip "国内：脚本自动走 npmmirror 镜像；或手动 https://git-scm.com/download/win"
} else {
    $done = $false
    if ($China) { $done = Install-GitChina }
    if (-not $done -and $haveWinget) {
        Write-Host "  正在通过 winget 安装：Git.Git …"
        winget install --id Git.Git -e --silent --accept-source-agreements --accept-package-agreements
        if ($LASTEXITCODE -eq 0) { Write-Ok "安装完成（重开终端后生效）" } else { Write-Miss "安装失败，手动安装：https://git-scm.com/download/win" }
    } elseif (-not $done) {
        Write-Miss "未安装"; Write-Tip "手动安装：https://git-scm.com/download/win"
    }
}

# ---- 2. Python ----
Write-Step "检查 Python 3（学习画像 / 辅助脚本）"
if ((Have "python") -or (Have "py")) {
    Write-Ok "已安装"
} elseif ($CheckOnly) {
    Write-Miss "未安装"; Write-Tip "国内：脚本自动走华为云镜像；或手动 https://www.python.org/downloads/"
} else {
    $done = $false
    if ($China) { $done = Install-PythonChina }
    if (-not $done -and $haveWinget) {
        Write-Host "  正在通过 winget 安装：Python.Python.3.13 …"
        winget install --id Python.Python.3.13 -e --silent --accept-source-agreements --accept-package-agreements
        if ($LASTEXITCODE -eq 0) { Write-Ok "安装完成（重开终端后生效）" } else { Write-Miss "安装失败，手动安装：https://www.python.org/downloads/" }
    } elseif (-not $done) {
        Write-Miss "未安装"; Write-Tip "手动安装：https://www.python.org/downloads/"
    }
}

# ---- 2.5 MinerU CLI（教材 OCR / PDF → Markdown，可选） ----
Write-Step "检查 MinerU CLI（教材 OCR 用，可选）"
$py = $null
if (Have "python") { $py = "python" } elseif (Have "py") { $py = "py" }
$mineruOk = (Have "mineru-open-api") -or (Have "mineru")
if ($mineruOk) {
    Write-Ok "MinerU CLI 已安装"
} elseif ($CheckOnly) {
    Write-Miss "未安装"; Write-Tip "安装命令：pip install mineru-open-api（详见 https://mineru.net/ecosystem?tab=cli）"
} elseif ($py) {
    Write-Host "  正在安装 MinerU CLI（pip install mineru-open-api）…"
    & $py -m pip install --quiet mineru-open-api
    if ($LASTEXITCODE -eq 0) { Write-Ok "MinerU CLI 安装完成" }
    else { Write-Miss "安装失败，可手动：pip install mineru-open-api" }
} else {
    Write-Miss "未检测到 Python，无法安装 MinerU CLI"
}

# ---- 3. Obsidian 本体（官方无国内镜像，如实说明） ----
Write-Step "检查 Obsidian（笔记与知识图谱）"
if ($obsidianInstalled) {
    Write-Ok "Obsidian 已安装"
} elseif ($CheckOnly) {
    Write-Miss "未安装"; Write-Tip "winget install --id Obsidian.Obsidian -e 或 https://obsidian.md/download"
} elseif ($haveWinget) {
    Write-Host "  正在通过 winget 安装：Obsidian.Obsidian（官方无国内镜像，安装包在 GitHub，若极慢见下方兜底）…"
    winget install --id Obsidian.Obsidian -e --silent --accept-source-agreements --accept-package-agreements
    if ($LASTEXITCODE -eq 0) { Write-Ok "安装完成" } else { Write-Miss "安装失败/超时" }
} else {
    Write-Miss "未安装"
}
if (-not $obsidianInstalled -and -not $CheckOnly) {
    Write-Tip "兜底：用浏览器打开 https://obsidian.md/download 下载安装包（浏览器下载可断点续传）；"
    Write-Tip "      或复制下载链接到多线程下载工具（IDM/迅雷等）加速；装好后重跑本脚本确认"
}

# ---- 4. Obsidian CLI（不能全自动，给出精确步骤） ----
Write-Step "检查 Obsidian CLI（AI 管理 vault 的通道）"
if (Have "obsidian") {
    Write-Ok "Obsidian CLI 可用"
} elseif ($obsidianInstalled) {
    Write-Miss "Obsidian 已装但 CLI 未开启（需在界面操作一次）"
    Write-Tip "打开 Obsidian → Settings → About → Command line interface → 按提示注册 → 重启终端"
    Write-Tip "验证命令：obsidian help ；详见 tools/obsidian-cli.md 第 1 节"
} else {
    Write-Miss "Obsidian 未安装，装好后按上述步骤开启 CLI"
}

# ---- 5. AI harness（不做检测，直接给官网） ----
Write-Step "AI harness（不做检测，已装哪个你自己最清楚）"
Write-Tip "ZCode（默认推荐）：https://zcode.z.ai/"
Write-Tip "Claude Code：https://docs.anthropic.com/en/docs/claude-code/"
Write-Tip "Codex CLI：https://github.com/openai/codex"
Write-Tip "dsh（DeepSeek harness）：按你的获取渠道安装（平台 https://platform.deepseek.com/）"
Write-Tip "Trae：https://www.trae.ai"

if (-not $CheckOnly) {
    Write-Tip "Claude Code / Codex CLI 如需安装，按需手动执行（国内自动用 npmmirror 源）："
    if ($China -and (Have "npm")) {
        Write-Tip "  Claude Code: npm install -g @anthropic-ai/claude-code --registry=https://registry.npmmirror.com"
        Write-Tip "  Codex CLI:   npm install -g @openai/codex --registry=https://registry.npmmirror.com"
    } else {
        Write-Tip "  Claude Code: npm install -g @anthropic-ai/claude-code"
        Write-Tip "  Codex CLI:   npm install -g @openai/codex"
    }
    Write-Tip "需要 Node.js/npm 前置；默认推荐 ZCode，一般无需安装 Claude Code / Codex。"
}

# ---- 6. 下一步 ----
Write-Step "下一步"
Write-Tip "1) 用 Obsidian 打开本仓库根目录（作为 vault）"
Write-Tip "2) 确认 obsidian help 可正常输出（CLI 已开启）"
if ((Have "python") -or (Have "py")) {
    Write-Tip "3) 运行体检：python tools\doctor.py（或 py tools\doctor.py）"
} else {
    Write-Tip "3) 重开终端后运行体检：python tools\doctor.py"
}
Write-Tip "4) 对 AI 说『开始学习〈学科名〉』即可进入学习模式"
