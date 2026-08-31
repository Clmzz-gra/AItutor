#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AItutor 环境与仓库体检脚本（doctor）。

用法:
    python tools/doctor.py             # 完整体检
    python tools/doctor.py --repo-only # 只查仓库/图谱健康
    python tools/doctor.py --env-only  # 只查本机环境

设计原则:
- 学生无需记很多命令：运行一次即可得到“缺什么 / 怎么修 / 下一步做什么”。
- 默认推荐免费模型 GLM-4-Flash，输出中会给出免费配置入口。
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

# 让输出统一 UTF-8（配合 bat 里的 chcp 65001，避免中文乱码）
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]

# 项目默认免费模型（与 guide/免费模型配置.md 保持一致）
DEFAULT_FREE_MODEL = "glm-4.5-flash"
DEFAULT_FREE_BASE_URL = "https://open.bigmodel.cn/api/paas/v4/"
FREE_MODEL_GUIDE = "guide/免费模型配置.md"

# 不参与知识图谱/文章体检的目录
EXCLUDE_DIRS = {
    ".git", ".obsidian", "_archive", "_session", "_demo-vault",
    "_references", "maintenance", "node_modules", "__pycache__",
}
# 在资产区中额外排除教材源材料
EXCLUDE_TEXTBOOK = {"textbook"}

# 文章类型（单一来源：rules/core/asset-spec.md §一）
KNOWN_TYPES = {
    "学科全景", "章", "节", "概念", "论文", "思考",
    "提问", "习题", "作业", "问题",
}


def parse_frontmatter(text: str) -> dict:
    """极简 frontmatter 解析（不引入 PyYAML）。"""
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    data = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip().strip("'\"")
        if key:
            data[key] = value
    return data


def is_md_article(path: Path) -> bool:
    return path.suffix.lower() == ".md" and path.name.lower() != "readme.md"


def iter_article_files() -> list[Path]:
    """遍历资产区文章 md；跳过 textbook、README 和临时目录。"""
    files: list[Path] = []
    assets = ROOT / "assets"
    if assets.is_dir():
        for path in assets.rglob("*.md"):
            parts = set(path.relative_to(ROOT).parts)
            if parts & EXCLUDE_DIRS or parts & EXCLUDE_TEXTBOOK:
                continue
            if is_md_article(path):
                files.append(path)
    return files


def normalize_wikilink(target: str) -> str:
    target = target.strip()
    if "|" in target:
        target = target.split("|", 1)[0]
    if "#" in target:
        target = target.split("#", 1)[0]
    if "^" in target:
        target = target.split("^", 1)[0]
    target = target.strip("/\\").replace("\\", "/")
    if target.lower().endswith(".md"):
        target = target[:-3]
    return target.strip()


def load_path_index(files: list[Path]) -> dict[str, Path]:
    index: dict[str, Path] = {}
    for path in files:
        rel = path.relative_to(ROOT).with_suffix("")
        index.setdefault(rel.as_posix().lower(), path)
        index.setdefault(path.stem.lower(), path)
        if "assets" in rel.parts:
            idx = rel.parts.index("assets")
            index.setdefault(Path(*rel.parts[idx + 1:]).as_posix().lower(), path)
    return index


def find_wikilinks(text: str) -> list[str]:
    return [normalize_wikilink(m) for m in re.findall(r"\[\[([^\]]+)\]\]", text)]


def candidates_of(target: str) -> list[str]:
    cands = [target.lower()]
    if "/" in target:
        cands.append(target.split("/")[-1].lower())
    return cands


def resolve(target: str, index: dict[str, Path]) -> Path | None:
    for c in candidates_of(target):
        if c in index:
            return index[c]
    return None


def check_wikilinks(files: list[Path], index: dict[str, Path]):
    unresolved = []
    for path in files:
        text = path.read_text(encoding="utf-8", errors="replace")
        for target in find_wikilinks(text):
            if target and resolve(target, index) is None:
                unresolved.append((path, target))
    return unresolved


def check_orphans(files: list[Path], index: dict[str, Path]):
    outbound = set()
    inbound = {p: set() for p in files}
    for path in files:
        text = path.read_text(encoding="utf-8", errors="replace")
        targets = find_wikilinks(text)
        if targets:
            outbound.add(path)
        for target in targets:
            resolved = resolve(target, index)
            if resolved is not None:
                inbound[resolved].add(target)
    return [p for p in files if p not in outbound and not inbound[p]]


def check_frontmatter(files: list[Path]):
    required = ("type", "formal", "subject", "created", "updated")
    issues = []
    for path in files:
        text = path.read_text(encoding="utf-8", errors="replace")
        data = parse_frontmatter(text)
        for field in required:
            if not data.get(field):
                issues.append((path, f"缺少 frontmatter 字段: {field}"))
        typ = data.get("type", "").strip()
        if typ and typ not in KNOWN_TYPES:
            issues.append((path, f"未知 type: {typ}"))
    return issues


def check_temp_residue():
    residue = []
    for name in ("_temp", "_scratch"):
        d = ROOT / name
        if d.exists():
            residue.append(d)
    for pattern in ("*.tmp", "未命名.*"):
        for p in ROOT.glob(pattern):
            if p.is_file():
                residue.append(p)
    return residue


def check_unclosed_topics():
    if not (ROOT / ".git").is_dir():
        return None, None
    try:
        out = subprocess.run(
            ["git", "log", "--grep", r"\[TOPIC", "--format=%s"],
            cwd=str(ROOT), capture_output=True, text=True,
            encoding="utf-8", errors="replace", timeout=20,
        )
    except (OSError, subprocess.SubprocessError):
        return None, None
    if out.returncode != 0:
        return None, out.stderr.strip()
    topic_re = re.compile(r"\[TOPIC\s+(.+?)\]\[(OPEN|CLOSE)\]")
    opened: dict[str, str] = {}
    for line in out.stdout.splitlines():
        m = topic_re.search(line)
        if not m:
            continue
        name, event = m.group(1).strip(), m.group(2)
        if event == "OPEN":
            opened.setdefault(name, line)
        elif event == "CLOSE":
            opened.pop(name, None)
    return list(opened.values()), None


def check_graph_style():
    """检查 Obsidian 图谱配色分组（colorGroups）是否完好。

    背景：`obsidian reload` 会重写 .obsidian/graph.json 的视图状态，
    可能把 colorGroups 清空（见 tools/obsidian-cli.md §5 踩坑）。
    这里做一道防护，丢了就提示用 tools/graph-style/configure.py 一键恢复。
    """
    graph = ROOT / ".obsidian" / "graph.json"
    if not graph.exists():
        return ("图谱配色", False, "未找到 .obsidian/graph.json",
                "运行 python tools/graph-style/configure.py 生成配色分组，再重启 Obsidian 生效")
    try:
        data = json.loads(graph.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        return ("图谱配色", False, f"graph.json 解析失败: {e}",
                "运行 python tools/graph-style/configure.py 重建，再重启 Obsidian 生效")
    groups = data.get("colorGroups") or []
    if not groups:
        return ("图谱配色", False, "colorGroups 为空（可能被 obsidian reload 清空）",
                "运行 python tools/graph-style/configure.py 一键恢复配色分组，再重启 Obsidian（obsidian restart）使其生效")
    return ("图谱配色", True, f"colorGroups {len(groups)} 组完好",
            "若需调整配色，运行 python tools/graph-style/configure.py 后重启 Obsidian 生效")


def check_environment():
    checks = []
    py_cmd = next((c for c in ("python", "python3") if shutil.which(c)), None)
    checks.append(("Python 3", py_cmd is not None,
                   py_cmd or "未检测到",
                   "安装 Python 3 或运行 tools/setup/bootstrap"))
    git_cmd = shutil.which("git")
    checks.append(("Git", git_cmd is not None,
                   git_cmd or "未检测到",
                   "安装 Git 或运行 tools/setup/bootstrap"))
    obs = shutil.which("obsidian")
    checks.append(("Obsidian CLI", obs is not None,
                   obs or "未检测到",
                   "Obsidian → Settings → About → Command line interface → 注册；详见 tools/obsidian-cli.md"))
    model = os.environ.get("ANTHROPIC_MODEL", "").strip()
    base = os.environ.get("ANTHROPIC_BASE_URL", "").strip()
    free_models = {DEFAULT_FREE_MODEL, "glm-4-flash", "glm-4-flash-250414"}  # 最强免费档 + 兼容旧免费档
    if model and model.lower() not in free_models:
        checks.append(("默认免费模型", False,
                       f"当前 ANTHROPIC_MODEL={model}",
                       f"学生默认推荐 {DEFAULT_FREE_MODEL}（免费），见 {FREE_MODEL_GUIDE}"))
    elif base and "bigmodel.cn" not in base:
        checks.append(("默认免费模型", False,
                       f"当前 ANTHROPIC_BASE_URL={base}",
                       f"学生默认推荐智谱 {DEFAULT_FREE_MODEL}，见 {FREE_MODEL_GUIDE}"))
    else:
        checks.append(("默认免费模型", True,
                       f"{DEFAULT_FREE_MODEL}（默认免费）或未覆盖为付费模型",
                       f"若尚未配置模型，按 {FREE_MODEL_GUIDE} 填入一个免费 Key 即可"))
    checks.append(check_graph_style())
    return checks


def print_report(checks, unresolved, orphans, frontmatter, residues,
                 topics, topic_error, files, repo_checked=True):
    print("== AItutor 体检报告 ==")
    if checks:
        print("\n[环境]")
        for label, ok, msg, fix in checks:
            flag = "[OK]  " if ok else "[需处理]"
            print(f"{flag} {label}: {msg}")
            if not ok:
                print(f"        → {fix}")
    if not repo_checked:
        print("\n[仓库/图谱] 已使用 --env-only 跳过仓库与图谱检查")
        print("\n[下一步]")
        print("  1) 若上面有 [需处理]，先按提示修复（多数可由 AI 对话直接处理）。")
        print("  2) 若环境未配好：Windows 运行 tools\\setup\\bootstrap.ps1；macOS/Linux 运行 tools/setup/bootstrap.sh。")
        print(f"  3) 配置默认免费模型 {DEFAULT_FREE_MODEL}：见 {FREE_MODEL_GUIDE}（只需申请一次 Key）。")
        print("  4) 一切就绪后，对 AI 说：开始学习〈学科名〉。")
        return
    print("\n[文章节点]")
    if files:
        print(f"[OK]   扫描文章节点: {len(files)} 个")
    else:
        print("[提示] 未扫描到文章节点（assets/ 中可能还没有内容）")
    print("\n[图谱健康]")
    if unresolved:
        print(f"[需处理] 未解析 wikilink {len(unresolved)} 个:")
        for path, target in unresolved[:20]:
            print(f"        - {path.relative_to(ROOT)} → [[{target}]]")
        if len(unresolved) > 20:
            print(f"        … 等共 {len(unresolved)} 个")
        print("        → 修复：创建目标文章，或改链到已有文章；详见 tools/obsidian-cli.md")
    else:
        print("[OK]   未发现未解析 wikilink")
    if orphans:
        print(f"[需处理] 孤立文章 {len(orphans)} 个（无出链也无入链）:")
        for p in orphans[:20]:
            print(f"        - {p.relative_to(ROOT)}")
        if len(orphans) > 20:
            print(f"        … 等共 {len(orphans)} 个")
        print("        → 修复：每篇至少补 1 条 wikilink（见 rules/core/asset-spec.md §三.2）")
    else:
        print("[OK]   未发现孤立文章节点")
    print("\n[frontmatter]")
    if frontmatter:
        print(f"[需处理] frontmatter 不一致 {len(frontmatter)} 处:")
        for path, msg in frontmatter[:20]:
            print(f"        - {path.relative_to(ROOT)}: {msg}")
        if len(frontmatter) > 20:
            print(f"        … 等共 {len(frontmatter)} 处")
        print("        → 修复：按 rules/core/asset-spec.md §三.1 补齐")
    else:
        print("[OK]   文章 frontmatter 基本一致")
    print("\n[Git 话题]")
    if topic_error:
        print(f"[提示] 无法读取 git 话题: {topic_error}")
    elif topics is None:
        print("[提示] 当前目录不是 git 仓库，跳过未闭合 TOPIC 检查")
    elif topics:
        print(f"[需处理] 未闭合 TOPIC {len(topics)} 个:")
        for line in topics[:20]:
            print(f"        - {line}")
        if len(topics) > 20:
            print(f"        … 等共 {len(topics)} 个")
        print("        → 修复：继续后提交 [TOPIC <文章名>][CLOSE] 闭合")
    else:
        print("[OK]   没有未闭合 TOPIC")
    print("\n[临时残留]")
    if residues:
        print(f"[需处理] 发现临时残留 {len(residues)} 个:")
        for p in residues:
            print(f"        - {p.relative_to(ROOT)}")
        print("        → 修复：删除 _temp/、_scratch/、*.tmp、未命名.*")
    else:
        print("[OK]   无临时残留")
    print("\n[下一步]")
    print("  1) 若上面有 [需处理]，先按提示修复（多数可由 AI 对话直接处理）。")
    print("  2) 若环境未配好：Windows 运行 tools\\setup\\bootstrap.ps1；macOS/Linux 运行 tools/setup/bootstrap.sh。")
    print(f"  3) 配置默认免费模型 {DEFAULT_FREE_MODEL}：见 {FREE_MODEL_GUIDE}（只需申请一次 Key）。")
    print("  4) 一切就绪后，对 AI 说：开始学习〈学科名〉。")


def main():
    parser = argparse.ArgumentParser(description="AItutor 环境与仓库体检")
    parser.add_argument("--repo-only", action="store_true", help="只检查仓库/图谱健康")
    parser.add_argument("--env-only", action="store_true", help="只检查本机环境")
    args = parser.parse_args()

    issues = 0
    files: list[Path] = []
    unresolved, orphans, frontmatter, residues = [], [], [], []
    topics, topic_error = None, None

    if not args.env_only:
        files = iter_article_files()
        index = load_path_index(files)
        unresolved = check_wikilinks(files, index)
        orphans = check_orphans(files, index)
        frontmatter = check_frontmatter(files)
        residues = check_temp_residue()
        topics, topic_error = check_unclosed_topics()
        issues += len(unresolved) + len(orphans) + len(frontmatter) + len(residues)
        if topics:
            issues += len(topics)

    checks = []
    if not args.repo_only:
        checks = check_environment()
        issues += sum(1 for _, ok, _, _ in checks if not ok)

    print_report(checks, unresolved, orphans, frontmatter, residues,
                 topics, topic_error, files, repo_checked=not args.env_only)
    sys.exit(1 if issues else 0)


if __name__ == "__main__":
    main()
