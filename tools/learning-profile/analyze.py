#!/usr/bin/env python3
"""学习画像分析：先输出原始图谱（图结构 + frontmatter），再基于图做画像判别。

设计原则：
- **原始输出 = 图本身**（节点 + 边 + frontmatter），画像判别是从图推导的视图。
- **seed 与增量分开算**：画像基于学生增量图谱（personal），seed 单独统计。
- 学习类型阈值未经验证，输出标注"待校准"。

用法:
    python analyze.py --personal <个人图谱目录> [--seed <seed目录>]
                      [--checkpoints <_checkpoints目录>]
"""
import argparse
import re
import subprocess
import sys
from collections import deque
from datetime import datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
LINE = "─" * 60

def parse_wikilinks(text):
    return [m.strip() for m in WIKILINK.findall(text)]

def parse_frontmatter(text):
    """解析文章开头的 YAML frontmatter，返回 dict；解析失败/不存在时返回空 dict。"""
    m = FRONTMATTER.match(text)
    if not m:
        return {}
    data = {}
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line or ":" not in line:
            continue
        key, val = line.split(":", 1)
        key = key.strip().lower()
        val = val.strip()
        if not val:
            data[key] = ""
            continue
        # 去掉成对引号
        if len(val) >= 2 and val[0] == val[-1] and val[0] in ("'", '"'):
            val = val[1:-1]
        # 行内列表 [a, b, c]
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            data[key] = [x.strip().strip("'\"") for x in inner.split(",") if x.strip()]
        else:
            data[key] = val
    return data

def scan_graph(root: Path):
    nodes = {}
    if not root.is_dir():
        return nodes
    for f in root.rglob("*.md"):
        name = f.stem
        text = f.read_text(encoding="utf-8", errors="ignore")
        out = set(parse_wikilinks(text))
        fm = parse_frontmatter(text)
        nodes[name] = {"file": f, "out": out, "in": set(), "fm": fm}
    for name, node in nodes.items():
        for t in node["out"]:
            if t in nodes:
                nodes[t]["in"].add(name)
    return nodes

def frontmatter_stats(nodes):
    """统计 frontmatter 覆盖情况：type / formal 分布、缺失必填字段。"""
    if not nodes:
        return None
    total = len(nodes)
    with_fm = [n for n, v in nodes.items() if v.get("fm")]
    types = {}
    formal_true = 0
    formal_false = 0
    missing = []
    for name, node in nodes.items():
        fm = node.get("fm", {})
        if not fm:
            missing.append(f"{name}（无 frontmatter）")
            continue
        typ = str(fm.get("type", "")).strip()
        if typ:
            types[typ] = types.get(typ, 0) + 1
        else:
            missing.append(f"{name}（缺 type）")
        formal = fm.get("formal")
        if formal == "true":
            formal_true += 1
        elif formal == "false":
            formal_false += 1
        else:
            missing.append(f"{name}（缺/错 formal）")
    return {
        "total": total,
        "with_fm": len(with_fm),
        "types": dict(sorted(types.items())),
        "formal_true": formal_true,
        "formal_false": formal_false,
        "missing": missing,
    }

def raw_graph_text(nodes):
    names = sorted(nodes.keys())
    lines = [f"  节点({len(names)}): {', '.join(names)}"]
    lines.append("  出链/入链（每节点）:")
    for name in names:
        out = sorted(t for t in nodes[name]["out"] if t in nodes)
        inn = sorted(t for t in nodes[name]["in"] if t in nodes)
        out_s = ", ".join(out) if out else "—"
        inn_s = ", ".join(inn) if inn else "—"
        lines.append(f"    {name}: 出→[{out_s}]  入←[{inn_s}]")
    dbl = []
    for a in names:
        for b in nodes[a]["out"]:
            if b in nodes and b > a and a in nodes[b]["out"]:
                dbl.append(f"{a}↔{b}")
    lines.append(f"  双链({len(dbl)}): {', '.join(dbl) if dbl else '（无）'}")
    return "\n".join(lines)

def longest_chain(nodes):
    memo = {}
    def depth(name, visiting):
        if name in memo:
            return memo[name]
        if name in visiting:
            return 0
        visiting.add(name)
        d = 0
        for t in nodes[name]["out"]:
            if t in nodes:
                d = max(d, 1 + depth(t, visiting))
        visiting.discard(name)
        memo[name] = d
        return d
    return max((depth(n, set()) for n in nodes), default=0)

def graph_metrics(nodes):
    n = len(nodes)
    links = sum(len(v["out"]) for v in nodes.values())
    density = links / (n * (n - 1)) if n > 1 else 0
    depth = longest_chain(nodes)
    hubs = sorted(nodes.items(), key=lambda kv: len(kv[1]["in"]), reverse=True)[:5]
    dbl = 0
    for a in nodes:
        for b in nodes[a]["out"]:
            if b in nodes and a in nodes[b]["out"]:
                dbl += 1
    dbl //= 2
    return {
        "nodes": n, "links": links, "density": round(density, 3), "depth": depth,
        "hubs": [h[0] for h in hubs if len(h[1]["in"]) > 0],
        "double_links": dbl,
    }

def interest_focus(nodes):
    if not nodes:
        return None
    memo = {}
    def descendants(name, visiting):
        if name in memo:
            return memo[name]
        if name in visiting:
            return set()
        visiting.add(name)
        d = set()
        for t in nodes[name]["out"]:
            if t in nodes:
                d.add(t)
                d |= descendants(t, visiting)
        visiting.discard(name)
        memo[name] = d
        return d
    best = None
    for name in nodes:
        ds = descendants(name, set())
        if best is None or len(ds) > len(best[1]) or (
            len(ds) == len(best[1]) and len(nodes[name]["in"]) > len(nodes[best[0]]["in"])
        ):
            best = (name, ds)
    name, ds = best
    total = len(nodes)
    return {"focus": name, "covered": len(ds), "total": total,
            "ratio": round(len(ds) / total, 3) if total else 0}

def growth_shape(nodes, focus):
    if not focus or focus not in nodes:
        return None
    visited = {focus}
    q = deque([focus])
    width = 1
    depth = 0
    while q:
        level_size = len(q)
        width = max(width, level_size)
        depth += 1
        for _ in range(level_size):
            n = q.popleft()
            for t in nodes[n]["out"]:
                if t in nodes and t not in visited:
                    visited.add(t)
                    q.append(t)
    if width <= 2 and depth >= 4:
        shape = "链式深挖（单链深入）"
    elif width >= 4:
        shape = "扇形展开（多分支）"
    else:
        shape = "均衡生长"
    return {"width": width, "depth": depth, "shape": shape}

def classify(metrics):
    """学习类型：非互斥，符合条件的都算。"""
    n, depth, density = metrics["nodes"], metrics["depth"], metrics["density"]
    if n == 0:
        return ["无增量数据"], "学生尚未新增节点，画像待积累"
    matched = []
    reasons = []
    if depth >= 4 and density >= 0.5:
        matched.append("深挖型"); reasons.append(f"深度{depth}≥4 且 密度{density}≥0.5")
    if n >= 20 and depth <= 2:
        matched.append("广撒网型"); reasons.append(f"节点{n}≥20 且 深度{depth}≤2")
    if density >= 0.6:
        matched.append("关联型"); reasons.append(f"密度{density}≥0.6")
    if depth >= 3:
        matched.append("纵深型"); reasons.append(f"深度{depth}≥3")
    if not matched:
        matched.append("均衡型"); reasons.append("未达特殊阈值")
    return matched, "; ".join(reasons)

def git_pace(checkpoints_dir: Path):
    if not checkpoints_dir.is_dir():
        return None
    try:
        out = subprocess.run(
            ["git", "log", "--format=%ct", "--", str(checkpoints_dir)],
            capture_output=True, text=True, cwd=checkpoints_dir.parent, timeout=10,
        )
    except Exception:
        return None
    stamps = [int(x) for x in out.stdout.split() if x.strip()]
    if not stamps:
        return None
    stamps.sort()
    days = (stamps[-1] - stamps[0]) / 86400
    gaps = [stamps[i+1] - stamps[i] for i in range(len(stamps)-1)]
    avg_gap = sum(gaps) / len(gaps) / 3600 if gaps else 0
    return {
        "checkpoints": len(stamps), "span_days": round(days, 1),
        "avg_gap_h": round(avg_gap, 1),
        "first": datetime.fromtimestamp(stamps[0]).strftime("%Y-%m-%d"),
        "last": datetime.fromtimestamp(stamps[-1]).strftime("%Y-%m-%d"),
    }

def main():
    ap = argparse.ArgumentParser(description="学习画像分析")
    ap.add_argument("--personal", required=True, help="个人增量图谱目录")
    ap.add_argument("--seed", help="seed 基础图谱目录")
    ap.add_argument("--checkpoints", help="_checkpoints 目录（git 节奏）")
    args = ap.parse_args()

    personal = scan_graph(Path(args.personal))
    seed = scan_graph(Path(args.seed)) if args.seed else {}
    inc = graph_metrics(personal)
    seed_m = graph_metrics(seed) if seed else None
    focus = interest_focus(personal)
    shape = growth_shape(personal, focus["focus"]) if focus and focus["covered"] > 0 else None

    print(LINE)
    print("📊 学习画像分析")
    print(LINE)
    print(f"分析时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"个人图谱: {args.personal}")
    if args.seed:
        print(f"seed 图谱: {args.seed}")
    print()

    print("【0】原始图谱（图结构，画像的源头）")
    print(raw_graph_text(personal))
    print()

    print("【0·5】frontmatter 概览（文章属性）")
    fm = frontmatter_stats(personal)
    if fm:
        print(f"  文章节点: {fm['total']}")
        print(f"  有 frontmatter: {fm['with_fm']}/{fm['total']}")
        if fm["types"]:
            print("  按 type 分布:")
            for typ, cnt in fm["types"].items():
                print(f"    {typ}: {cnt}")
        else:
            print("  按 type 分布: （无）")
        print(f"  正式 (formal:true): {fm['formal_true']}")
        print(f"  checkpoint (formal:false): {fm['formal_false']}")
        if fm["missing"]:
            print("  缺失/异常:")
            for m in fm["missing"]:
                print(f"    - {m}")
        else:
            print("  缺失/异常: （无）")
    else:
        print("  （无 personal 数据）")
    print()

    print("【1】增量图谱指标（从原始图推导）")
    print(f"  新增节点: {inc['nodes']}")
    print(f"  新增链接: {inc['links']}")
    print(f"  链接密度: {inc['density']}")
    print(f"  最长依赖链(深度): {inc['depth']}")
    print(f"  双链(互链): {inc['double_links']} 条"
          + ("（图谱更像网，学生对已有知识深入研究）" if inc['double_links'] >= 2 else ""))
    print(f"  核心枢纽(入链最多): {inc['hubs'] if inc['hubs'] else '（暂无）'}")
    print()

    if seed_m:
        print("【2】seed 基础图谱（共享地基，不计入画像）")
        print(f"  seed 节点: {seed_m['nodes']}")
        print(f"  seed 链接: {seed_m['links']}")
        print(f"  增量占比: {inc['nodes']}/{seed_m['nodes']} 节点 "
              f"({round(inc['nodes']/seed_m['nodes']*100,1) if seed_m['nodes'] else 0}%)")
        print()

    pace = git_pace(Path(args.checkpoints)) if args.checkpoints else None
    print("【3】学习节奏（git checkpoint）")
    if pace:
        print(f"  checkpoint 数: {pace['checkpoints']}")
        print(f"  学习跨度: {pace['span_days']} 天（{pace['first']} → {pace['last']}）")
        print(f"  平均间隔: {pace['avg_gap_h']} 小时")
    else:
        print("  （无 checkpoint 数据）")
    print()

    print("【5】兴趣焦点（生长中心）")
    if focus and focus["covered"] > 0:
        print(f"  焦点节点: {focus['focus']}")
        print(f"  覆盖增量: {focus['covered']}/{focus['total']} 节点 ({focus['ratio']*100:.0f}%)")
        print("  解读: 学生兴趣高度集中于此节点（兴趣焦点明显）" if focus["ratio"] >= 0.5
              else "  解读: 兴趣较分散")
    else:
        print("  （增量不足，暂无法判断兴趣焦点）")
    print()

    print("【5b】生长形态（宽度/分支）")
    if shape:
        print(f"  形态: {shape['shape']}")
        print(f"  宽度(每层最大节点): {shape['width']}  深度: {shape['depth']}")
    else:
        print("  （增量不足，暂无法判断）")
    print()

    print("【6】学习类型（⚠ 阈值待校准，仅供参考）")
    if inc["nodes"] == 0:
        print("  学生尚未新增节点，画像待积累（学期初正常）")
    else:
        typs, reason = classify(inc)
        print(f"  判定: {' + '.join(typs)}")
        print(f"  依据: {reason}")
        print("  说明: 阈值未经验证，需实测后校准")
    print(LINE)


if __name__ == "__main__":
    main()
