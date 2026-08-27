#!/usr/bin/env python3
"""自动配置 Obsidian 图谱颜色分组（初始化时运行一次即可）。

用法:
    python tools/graph-style/configure.py

效果:
    写入 .obsidian/graph.json 的 colorGroups（path: 检索式，任意学科通用）:
      path:seed      seed 类（低饱和蓝灰，共享只读地基）
      path:personal  personal 类（高饱和橙红，个人增量）
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GRAPH = ROOT / ".obsidian" / "graph.json"

# 配色规则：
# - seed 类：低饱和 / 沉稳，表示共享只读地基
# - personal 类：高饱和 / 鲜艳，表示个人增量，与 seed 形成明显视觉区分
PALETTE = [
    ("path:seed",      "#78909C"),  # seed：低饱和蓝灰
    ("path:personal",  "#FF3D00"),  # personal：高饱和橙红
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
