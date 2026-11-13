"""Characteristic taxa of Wallace's six zoogeographic realms, and a clustering of the realms by them.

Left: presence of living native members of 32 characteristic taxa in each realm (0 absent, 1 present,
2 endemic or nearly endemic, or the clear centre of diversity), scored from standard distribution data
(mammals, birds, reptiles, amphibians, fishes, insects). The selection of taxa is deliberately the set
used in the text, so the matrix illustrates the method rather than a full faunal analysis.
Right: Jaccard similarity of the realms (presence = score >= 1) and the UPGMA dendrogram.
"""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FONT = bio.core.FONT

REALMS = ["Palearctic", "Nearctic", "Neotropical", "Afrotropical", "Oriental", "Australian"]
# group, taxon, scores for the six realms in the order above
ROWS = [
    ("Mammals", "Monotremata", [0, 0, 0, 0, 0, 2]),
    ("Mammals", "Marsupialia", [0, 1, 1, 0, 0, 2]),
    ("Mammals", "Xenarthra", [0, 1, 2, 0, 0, 0]),
    ("Mammals", "Afrotheria (land)", [1, 0, 0, 2, 1, 0]),
    ("Mammals", "Platyrrhini", [0, 0, 2, 0, 0, 0]),
    ("Mammals", "Lemurs", [0, 0, 0, 2, 0, 0]),
    ("Mammals", "Gibbons", [0, 0, 0, 0, 2, 0]),
    ("Mammals", "Tarsiers", [0, 0, 0, 0, 2, 0]),
    ("Mammals", "Giraffes, hippos", [0, 0, 0, 2, 0, 0]),
    ("Mammals", "Pikas", [2, 1, 0, 0, 0, 0]),
    ("Mammals", "Beavers", [1, 1, 0, 0, 0, 0]),
    ("Mammals", "Pronghorn", [0, 2, 0, 0, 0, 0]),
    ("Mammals", "Deer", [1, 1, 1, 0, 1, 0]),
    ("Mammals", "Bears", [1, 1, 1, 0, 1, 0]),
    ("Birds", "Ratites", [0, 0, 1, 1, 0, 1]),
    ("Birds", "Hummingbirds", [0, 1, 2, 0, 0, 0]),
    ("Birds", "Lyrebirds, birds-of-paradise", [0, 0, 0, 0, 0, 2]),
    ("Birds", "Pheasants", [1, 0, 0, 1, 2, 0]),
    ("Birds", "Hornbills", [0, 0, 0, 1, 1, 1]),
    ("Reptiles", "Rhynchocephalia", [0, 0, 0, 0, 0, 2]),
    ("Reptiles", "Chameleons", [1, 0, 0, 2, 1, 0]),
    ("Reptiles", "Alligatoridae", [0, 1, 1, 0, 1, 0]),
    ("Amphibians", "Caudata", [1, 2, 1, 0, 1, 0]),
    ("Amphibians", "Gymnophiona", [0, 0, 1, 1, 1, 0]),
    ("Amphibians", "Pipidae", [0, 0, 1, 1, 0, 0]),
    ("Fishes", "Dipnoi", [0, 0, 1, 1, 0, 1]),
    ("Fishes", "Polypteridae", [0, 0, 0, 2, 0, 0]),
    ("Fishes", "Gars", [0, 2, 1, 0, 0, 0]),
    ("Insects", "Grylloblattodea", [1, 1, 0, 0, 0, 0]),
    ("Insects", "Mantophasmatodea", [0, 0, 0, 2, 0, 0]),
    ("Insects", "Moss bugs (Peloridiidae)", [0, 0, 1, 0, 0, 1]),
    ("Insects", "Birdwing butterflies", [0, 0, 0, 0, 1, 1]),
]
M = np.array([r[2] for r in ROWS])
n, k = M.shape

fig, ax = bio.canvas(24, 19)

# heat map
a = charts.axes_at(ax, (7.2, 1.2, 6.0, 15.6))
levels = [P.surface(), P.fill("dna2"), P.edge("dna")]
for i in range(n):
    for j in range(k):
        y = n - 1 - i
        a.add_patch(__import__("matplotlib").patches.Rectangle((j, y), 1, 1, facecolor=levels[M[i, j]],
                                                                 edgecolor=P.muted(), lw=0.4))
a.set_xlim(0, k)
a.set_ylim(0, n)
a.set_xticks(np.arange(k) + 0.5)
a.set_xticklabels(REALMS, rotation=50, ha="left", fontsize=FONT["tiny"])
a.xaxis.tick_top()
a.set_yticks(np.arange(n) + 0.5)
a.set_yticklabels([r[1] for r in ROWS][::-1], fontsize=FONT["tiny"])
charts.style_axes(a, box=True)
a.tick_params(length=0)
# group separators and labels
prev = None
for i, r in enumerate(ROWS):
    if r[0] != prev:
        y = n - i
        if prev is not None:
            a.axhline(y, color=P.ink(), lw=1.0)
        prev = r[0]
        cnt = sum(1 for q in ROWS if q[0] == r[0])
        yc = 1.2 + 15.6 * (y - cnt / 2) / n
        bio.label(ax, (0.3, yc), r[0], size="small", bold=True, ha="left")

# legend
for t, (txt, c) in enumerate([("absent", levels[0]), ("present", levels[1]), ("endemic / centre", levels[2])]):
    yy = 0.35
    xx = 7.2 + t * 2.2
    ax.add_patch(__import__("matplotlib").patches.Rectangle((xx, yy - 0.18), 0.36, 0.36, facecolor=c,
                                                             edgecolor=P.muted(), lw=0.5))
    bio.label(ax, (xx + 0.5, yy), txt, size="tiny", ha="left")

# Jaccard similarity and UPGMA
B = M >= 1
S = np.zeros((k, k))
for p in range(k):
    for q in range(k):
        S[p, q] = (B[:, p] & B[:, q]).sum() / max((B[:, p] | B[:, q]).sum(), 1)
D = 1 - S

clusters = {j: [j] for j in range(k)}
height = {j: 0.0 for j in range(k)}
pos = {}
dist = {(p, q): D[p, q] for p in range(k) for q in range(k) if p < q}
merges = []
nid = k
active = list(range(k))
while len(active) > 1:
    p, q = min(((p, q) for ii, p in enumerate(active) for q in active[ii + 1:]),
               key=lambda pq: np.mean([D[x, y] for x in clusters[pq[0]] for y in clusters[pq[1]]]))
    h = np.mean([D[x, y] for x in clusters[p] for y in clusters[q]])
    clusters[nid] = clusters[p] + clusters[q]
    height[nid] = h
    merges.append((p, q, nid, h))
    active = [c for c in active if c not in (p, q)] + [nid]
    nid += 1

order = clusters[active[0]]
d = charts.axes_at(ax, (16.0, 9.5, 6.5, 6.0))
ypos = {leaf: i for i, leaf in enumerate(order)}
xpos = {leaf: 0.0 for leaf in order}
for p, q, c, h in merges:
    for child in (p, q):
        d.plot([xpos[child], h], [ypos[child], ypos[child]], color=P.ink(), lw=1.2)
    d.plot([h, h], [ypos[p], ypos[q]], color=P.ink(), lw=1.2)
    ypos[c] = (ypos[p] + ypos[q]) / 2
    xpos[c] = h
d.set_yticks(range(k))
d.set_yticklabels([REALMS[j] for j in order], fontsize=FONT["tiny"])
d.yaxis.tick_right()
d.set_xlim(max(height.values()) * 1.08, 0)
d.set_ylim(-0.6, k - 0.4)
charts.style_axes(d, "Jaccard distance (UPGMA)")
d.spines["left"].set_visible(False)
d.spines["right"].set_visible(True)
charts.title(d, "Similarity of realms")

# similarity matrix
s = charts.axes_at(ax, (16.0, 1.6, 5.2, 5.2))
s.imshow(S[np.ix_(order, order)], cmap=__import__("matplotlib").colors.LinearSegmentedColormap.from_list(
    "sim", [P.surface(), P.edge("dna")]), vmin=0, vmax=1, extent=(0, k, k, 0))
for p in range(k):
    for q in range(k):
        v = S[order[p], order[q]]
        s.text(q + 0.5, p + 0.5, f"{v:.2f}", ha="center", va="center", fontsize=FONT["tiny"] * 0.8,
               color=P.on_fill() if v > 0.55 else P.ink())
s.set_xticks(np.arange(k) + 0.5)
s.set_xticklabels([REALMS[j][:4] for j in order], fontsize=FONT["tiny"])
s.set_yticks(np.arange(k) + 0.5)
s.set_yticklabels([REALMS[j][:4] for j in order], fontsize=FONT["tiny"])
charts.style_axes(s, box=True)
charts.title(s, "Jaccard similarity")
