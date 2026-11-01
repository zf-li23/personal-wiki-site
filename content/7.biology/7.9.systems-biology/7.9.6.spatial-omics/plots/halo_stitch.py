"""Segmenting a large image in tiles. A: a synthetic image of 90 cells (radius 6-11 px) divided
into 3 x 3 tiles of 120 px (solid lines); each tile is processed together with a halo of 24 px
(dashed: the window of the centre tile). B: without a halo, cells crossing tile boundaries are
cut into fragments that are counted as separate cells (red outlines). C: with the halo, objects
touching an inner window edge are discarded (they are complete in a neighbouring window, because
the halo exceeds the largest cell diameter), and the duplicates found in overlapping windows are
merged when their intersection over union is at least 0.5, using a union-find structure.
D: the extra pixels processed because of the halo, (1 + 2h/L)^d - 1, for tiles of side L in two
and three dimensions."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from scipy import ndimage as ndi
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
S, L, h, ncell = 360, 120, 24, 90
yy, xx = np.mgrid[0:S, 0:S]
cs, rs = [], []
while len(cs) < ncell:
    c, r = rng.uniform(8, S - 8, 2), rng.uniform(6, 11)
    if all(np.hypot(*(c - c2)) > r + r2 + 2 for c2, r2 in zip(cs, rs)):
        cs.append(c)
        rs.append(r)
mask = np.zeros((S, S), bool)
for c, r in zip(cs, rs):
    mask |= np.hypot(yy - c[0], xx - c[1]) < r


def segment(window):
    """Stand-in for a segmentation model: connected components of the window."""
    lab, n = ndi.label(window)
    return lab, n


def tiles(halo):
    out = []
    for i in range(S // L):
        for j in range(S // L):
            y0, x0 = max(i * L - halo, 0), max(j * L - halo, 0)
            y1, x1 = min((i + 1) * L + halo, S), min((j + 1) * L + halo, S)
            out.append((y0, y1, x0, x1))
    return out


# B: no halo
naive = []
for y0, y1, x0, x1 in tiles(0):
    lab, n = segment(mask[y0:y1, x0:x1])
    for k in range(1, n + 1):
        m = np.zeros((S, S), bool)
        m[y0:y1, x0:x1] = lab == k
        naive.append(m)

# C: halo, drop objects touching inner window edges, merge duplicates by IoU with union-find
objs = []
for y0, y1, x0, x1 in tiles(h):
    lab, n = segment(mask[y0:y1, x0:x1])
    for k in range(1, n + 1):
        sub = lab == k
        edge = ((y0 > 0 and sub[0].any()) or (y1 < S and sub[-1].any())
                or (x0 > 0 and sub[:, 0].any()) or (x1 < S and sub[:, -1].any()))
        if not edge:
            m = np.zeros((S, S), bool)
            m[y0:y1, x0:x1] = sub
            objs.append(m)
parent = list(range(len(objs)))


def find(a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a


for a in range(len(objs)):
    for b in range(a + 1, len(objs)):
        inter = (objs[a] & objs[b]).sum()
        if inter and inter / (objs[a] | objs[b]).sum() >= 0.5:
            parent[find(a)] = find(b)
roots = sorted({find(a) for a in range(len(objs))})
true_n = ndi.label(mask)[1]
RESULT = {"true": true_n, "naive": len(naive), "kept_before_merge": len(objs), "stitched": len(roots)}

fig, axs = plt.subplots(1, 4, figsize=(12.4, 3.4), gridspec_kw={"width_ratios": [1, 1, 1, 1.05]})
fig.subplots_adjust(left=0.01, right=0.98, bottom=0.15, top=0.86, wspace=0.12)
cell_rgba = np.zeros((S, S, 4))
cell_rgba[mask] = list(plt.matplotlib.colors.to_rgba(P.fill("chromatin")))
for a in axs[:3]:
    a.imshow(cell_rgba, interpolation="nearest")
    for t in range(1, S // L):
        a.axhline(t * L - 0.5, color=P.edge("dna"), lw=1.0)
        a.axvline(t * L - 0.5, color=P.edge("dna"), lw=1.0)
    a.set_xticks([])
    a.set_yticks([])
    for sp in a.spines.values():
        sp.set_color(P.muted())
axs[0].add_patch(Rectangle((L - h - 0.5, L - h - 0.5), L + 2 * h, L + 2 * h, fill=False,
                           ec=P.edge("rna"), ls="--", lw=1.3))
charts.title(axs[0], f"A  {S // L}x{S // L} tiles, halo {h} px")
# outline fragments from naive tiling
cut = np.zeros((S, S), bool)
for m in naive:
    full = ndi.label(mask)[0][m][0]
    if m.sum() < (ndi.label(mask)[0] == full).sum():
        cut |= m
axs[1].contour(cut, levels=[0.5], colors=[P.edge("negative")], linewidths=1.2)
charts.title(axs[1], f"B  No halo: {len(naive)} objects")
stitched = np.zeros((S, S), int)
for i, r in enumerate(roots, 1):
    stitched[objs[r]] = i
axs[2].contour(stitched > 0, levels=[0.5], colors=[P.edge("positive")], linewidths=0.9)
charts.title(axs[2], f"C  Halo + stitching: {len(roots)} objects")
ratio = np.linspace(0, 0.25, 100)
for d, tok in [(2, "dna"), (3, "rna")]:
    axs[3].plot(ratio, 100 * ((1 + 2 * ratio) ** d - 1), color=charts.line(tok), lw=1.6, label=f"{d}D")
axs[3].plot([h / L], [100 * ((1 + 2 * h / L) ** 2 - 1)], "o", color=charts.line("dna"), ms=4)
axs[3].legend(frameon=False, fontsize=7.5, labelcolor=P.ink())
charts.style_axes(axs[3], "halo / tile side, h/L", "extra pixels processed / %")
charts.title(axs[3], "D  Cost of the halo")
