# -*- coding: utf-8 -*-
import io, re, sys

def transform(path):
    raw = open(path, 'rb').read()
    crlf = b'\r\n' in raw
    s = raw.decode('utf-8').replace('\r\n', '\n')
    marker = '## 📖 全文讲解'
    if marker not in s:
        print("NO 讲解 marker:", path); return
    before, after = s.split(marker, 1)
    after = marker + after

    # ---- parse before: 本段表达 callout blocks (character offsets) ----
    callout_re = re.compile(r'> \[!note\]- 本段表达\n((?:> - .*\n?)+)')
    callouts = []
    for m in callout_re.finditer(before):
        bullets = m.group(1).rstrip('\n').split('\n')
        callouts.append((m.start(), m.end(), bullets))

    # ---- parse after: 二、逐段精讲 section ----
    m2 = re.search(r'### 二、逐段精讲.*?\n', after)
    m3 = re.search(r'### 三、', after)
    if not m2 or not m3:
        print("NO 二/三 section:", path); return
    sec2 = after[m2.start():m3.start()]
    segs = re.split(r'#### 段\s*[A-Za-z0-9]+', sec2)
    para_info = []
    for seg in segs[1:]:
        fm = re.search(r'——\s*功能[：:]\s*(.+)', seg)
        func = fm.group(1).strip() if fm else ''
        im = re.search(r'\*\*信息要点\*\*[：:]\s*(.+)', seg)
        info = im.group(1).strip() if im else ''
        para_info.append((func, info))

    # ---- rebuild before ----
    new_before = before
    repls = []
    for idx, (st, end, bullets) in enumerate(callouts):
        func, info = para_info[idx] if idx < len(para_info) else ('', '')
        block = '> [!note]- 本段精讲\n'
        block += '> **功能**：' + func + '\n'
        block += '> **信息要点**：' + info + '\n'
        block += '> **表达**：\n'
        for b in bullets:
            block += b + '\n'
        block = block.rstrip('\n')
        repls.append((st, end, block))
    for st, end, block in reversed(repls):
        new_before = new_before[:st] + block + new_before[end:]

    # ---- rebuild after: remove 二 section ----
    new_after = after[:m2.start()] + after[m3.start():]

    out = new_before + new_after
    if crlf:
        out = out.replace('\n', '\r\n')
    open(path, 'wb').write(out.encode('utf-8'))
    print("OK:", path, "| callouts:", len(callouts), "| para_info:", len(para_info))

if __name__ == '__main__':
    for p in sys.argv[1:]:
        transform(p)
