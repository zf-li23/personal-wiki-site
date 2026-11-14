"""Non-independence of species: independent Brownian motion of two traits on a 16-tip tree with two clades.

Raw species correlation versus Felsenstein's (1985) independent contrasts, 2000 simulations.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(1)

# balanced tree, depth 4; branch lengths by level (root's children first)
BL = [6.0, 0.6, 0.6, 0.6]


def build(level=0):
    if level == 4:
        return None
    return [(build(level + 1), BL[level]), (build(level + 1), BL[level])]


TREE = build()


def simulate(node, x, rng, out):
    if node is None:
        out.append(x)
        return
    for child, bl in node:
        simulate(child, x + rng.normal(0, np.sqrt(bl), 2), rng, out)


def contrasts(node, vals, it, out):
    """Return (value, extra branch length) of node; append standardized contrasts to out."""
    if node is None:
        return next(it), 0.0
    res = []
    for child, bl in node:
        v, extra = contrasts(child, vals, it, out)
        res.append((v, bl + extra))
    (v1, l1), (v2, l2) = res
    out.append((v1 - v2) / np.sqrt(l1 + l2))
    return (v1 / l1 + v2 / l2) / (1 / l1 + 1 / l2), l1 * l2 / (l1 + l2)


def one(rng):
    tips = []
    simulate(TREE, np.zeros(2), rng, tips)
    tips = np.array(tips)
    cs = []
    contrasts(TREE, tips, iter(tips), cs)
    cs = np.array(cs)
    r_raw = np.corrcoef(tips[:, 0], tips[:, 1])[0, 1]
    r_pic = np.sum(cs[:, 0] * cs[:, 1]) / np.sqrt(np.sum(cs[:, 0] ** 2) * np.sum(cs[:, 1] ** 2))
    return tips, r_raw, r_pic


# pick an illustrative replicate with a clear spurious correlation
for _ in range(200):
    tips, r_raw, r_pic = one(rng)
    if abs(r_raw) > 0.75 and abs(r_pic) < 0.3:
        break
fig, ax = bio.canvas(28.0, 10.5)
pa = C.axes_at(ax, (2.4, 1.6, 9.0, 7.2))
sgn = 1 if r_raw > 0 else -1
tips[:, 1] *= sgn
pa.plot(tips[:8, 0], tips[:8, 1], "o", color=C.line("dna"), ms=6)
pa.plot(tips[8:, 0], tips[8:, 1], "s", color=C.line("rna"), ms=6)
pa.text(0.03, 0.95, f"species: r = {abs(r_raw):.2f}", transform=pa.transAxes, fontsize=FS["tiny"], color=P.ink(), va="top")
pa.text(0.03, 0.87, f"contrasts: r = {sgn * r_pic:.2f}", transform=pa.transAxes, fontsize=FS["tiny"], color=P.ink(), va="top")
pa.text(0.97, 0.10, "clade 1 (circles), clade 2 (squares)", transform=pa.transAxes, fontsize=FS["tiny"], color=P.muted(), ha="right")
C.style_axes(pa, "trait X", "trait Y")
pa.set_xticks([])
pa.set_yticks([])
bio.panel(ax, "A", (0.4, 10.2))

raws, pics = [], []
for _ in range(2000):
    _, a, b = one(rng)
    raws.append(a)
    pics.append(b)
raws, pics = np.array(raws), np.array(pics)
# critical |r| at 5% for n = 16 (df 14) and 15 contrasts through the origin (df 14): t = 2.145
tcrit = 2.145
rc = tcrit / np.sqrt(14 + tcrit ** 2)
pb = C.axes_at(ax, (15.4, 1.6, 11.6, 7.2))
bins = np.linspace(-1, 1, 41)
pb.hist(raws, bins=bins, color=C.line("negative"), alpha=0.45, lw=0)
pb.hist(pics, bins=bins, histtype="step", color=C.line("dna"), lw=1.8)
for v in (-rc, rc):
    pb.axvline(v, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pb.text(-0.98, pb.get_ylim()[1] * 0.92, f"species values: {np.mean(abs(raws) > rc):.0%} significant",
        color=C.line("negative"), fontsize=FS["tiny"])
pb.text(-0.98, pb.get_ylim()[1] * 0.82, f"independent contrasts: {np.mean(abs(pics) > rc):.0%} significant",
        color=C.line("dna"), fontsize=FS["tiny"])
pb.set_xlim(-1, 1)
C.style_axes(pb, "correlation coefficient r", "number of simulations")
bio.panel(ax, "B", (13.6, 10.2))
