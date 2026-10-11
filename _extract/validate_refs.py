# -*- coding: utf-8 -*-
"""校验所有读书笔记 md 中的图片引用：路径必须存在；并汇总每文件引用数。"""
import os, re, glob

ROOT = "/home/ericli/workspace/tradeMd"
pat = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")

bad = []
used = set()
for md in sorted(glob.glob(os.path.join(ROOT, "*.md"))):
    with open(md, encoding="utf-8") as f:
        text = f.read()
    refs = pat.findall(text)
    if refs:
        print(f"{os.path.basename(md)}: {len(refs)} 张")
    for r in refs:
        p = os.path.normpath(os.path.join(ROOT, r.split()[0]))
        used.add(os.path.basename(p))
        if not os.path.isfile(p):
            bad.append((os.path.basename(md), r))

print()
if bad:
    print("!! 失效引用：")
    for m, r in bad:
        print(" ", m, "->", r)
else:
    print("所有引用均存在。")

imgs = set(os.listdir(os.path.join(ROOT, "images")))
unused = sorted(imgs - used)
print(f"\nimages/ 共 {len(imgs)} 个文件，被引用 {len(used)} 个，未使用 {len(unused)} 个。")
if unused:
    for u in unused:
        print("  未使用:", u)
