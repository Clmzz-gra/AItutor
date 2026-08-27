#!/usr/bin/env python3
"""自动配置 Obsidian 图谱颜色分组（初始化时运行一次即可）。

用法:
    python tools/graph-style/configure.py

效果:
    写入 .obsidian/graph.json 的 colorGroups（file: 检索式，任意学科通用）:
      file:学科概览  学科全景（主色）
      file:Ch        章
      file:Sec       节
      file:概念      概念/其余
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GRAPH = ROOT / ".obsidian" / "graph.json"

# 配色（新一组：玫红 / 深蓝 / 深绿 / 蓝灰）
PALETTE = [
    ("file:学科概览", "#C2185B"),   # 学科全景
    ("file:Ch",       "#1565C0"),   # 章
    ("file:Sec",      "#2E7D32"),   # 节
    ("file:概念",      "#78909C"),   # 概念/其余
]

def rgb(hexstr: str) -> int:
    h = hexstr.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return (r << 16) | (g << 8) | b

def main() -> int:
    if not GRAPH.exists():
        print(f"错误：找不到 {GRAPH}", file=sys.stderr)
        return 1
    data = json.loads(GRAPH.read_text(encoding="utf-8"))
    data["colorGroups"] = [
        {"query": q, "color": {"a": 1, "rgb": rgb(c)}} for q, c in PALETTE
    ]
    data["collapse-color-groups"] = False
    GRAPH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print("已写入配色分组：")
    for q, c in PALETTE:
        print(f"  {q}  {c}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
