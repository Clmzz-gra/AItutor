#!/usr/bin/env python3
"""自动配置 Obsidian 图谱颜色分组（初始化时运行一次即可）。

用法:
    python tools/graph-style/configure.py

效果:
    写入 .obsidian/graph.json 的 colorGroups（path: + file: 检索式，任意学科通用）:
      seed 类：低饱和色，按层级区分（学科全景 / 章 / 节 / 概念）
      personal 类：高饱和色，按文章类型区分
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GRAPH = ROOT / ".obsidian" / "graph.json"

# 配色规则：
# - seed 类：低饱和 / 沉稳，表示共享只读地基；同一色系内按层级用不同色相区分
# - personal 类：高饱和 / 鲜艳，表示个人增量；同一高饱和体系内按文章类型用不同色相区分
# 二次开发新增文章类型时，在此 PALETTE 追加对应 query 即可（见 asset-spec §一·五）。
PALETTE = [
    # seed：低饱和，按层级区分
    ("path:seed file:学科概览", "#B0717A"),  # 学科全景：低饱和玫瑰
    ("path:seed file:Ch",       "#5C7A99"),  # 章：低饱和蓝
    ("path:seed file:Sec",      "#6B8E6B"),  # 节：低饱和绿
    ("path:seed file:概念",      "#78909C"),  # 概念：低饱和蓝灰
    # personal：高饱和，按文章类型区分
    ("path:personal file:学科概览", "#FF1744"),  # 学科全景：高饱和红
    ("path:personal file:Ch",       "#2979FF"),  # 章：高饱和蓝
    ("path:personal file:Sec",      "#00C853"),  # 节：高饱和绿
    ("path:personal file:概念",      "#FF9100"),  # 概念：高饱和橙
    ("path:personal file:论文",      "#D500F9"),  # 论文：高饱和紫
    ("path:personal file:思考",      "#FF6D00"),  # 思考：高饱和深橙
    ("path:personal file:提问",      "#651FFF"),  # 提问：高饱和靛蓝
    ("path:personal file:习题",      "#00E5FF"),  # 习题：高饱和青
    ("path:personal file:作业",      "#76FF03"),  # 作业：高饱和黄绿
    ("path:personal file:问题",      "#F50057"),  # 问题：高饱和粉红
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
