"""The interphase nucleus (schematic).
(A) Chromosome territories (two highlighted) inside the envelope and lamina, a nucleolus, and nuclear bodies in the
interchromatin space: Cajal bodies, speckles and PML bodies. (B) One territory against the lamina: LADs (dark,
B compartment) at the periphery, A-compartment chromatin (light) towards the interior, an active gene looping out
towards a speckle. (C) A simulated contact map of a 10-Mb region: contact probability ~ s^-1 along the diagonal,
modulated by alternating A/B compartments (checkerboard), TAD blocks and one CTCF loop (corner peak)."""

import numpy as np
from matplotlib.patches import Circle, PathPatch
from matplotlib.path import Path

import wikibio as bio
from wikibio import charts
from wikibio import nuclear as N

P = bio.P
rng = np.random.default_rng(0)
fig, ax = bio.canvas(23.0, 8.2)

# A: territories and bodies
bio.panel(ax, "A", (0.1, 8.1))
nl = (4.3, 3.6, 0.85)
t = N.territories(ax, (3.9, 4.1), 3.4, 3.0, n=14, seed=5, highlight={3: "dna", 10: "receptor"}, nucleoli=[nl])
N.nucleolus(ax, nl[:2], nl[2], units=3)
cent = np.array([tt["center"] for tt in t["territories"]])
# nuclear bodies at midpoints between neighboring territories (interchromatin space)
mids = []
for i in range(len(cent)):
    d = np.hypot(*(cent - cent[i]).T)
    for j in np.argsort(d)[1:3]:
        m = (cent[i] + cent[j]) / 2
        if np.hypot(m[0] - nl[0], m[1] - nl[1]) > nl[2] + 0.4 and all(np.hypot(*(m - q)) > 0.6 for q in mids):
            mids.append(m)
mids = mids[:9]
for k, m in enumerate(mids):
    if k < 4:  # speckles
        v = bio.blob(tuple(m), 0.22, 0.15, wobble=0.25, seed=k, k=7, angle=k)
        ax.add_patch(PathPatch(Path(v, closed=True), facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.7, zorder=12))
    elif k < 6:  # Cajal bodies
        ax.add_patch(Circle(tuple(m), 0.13, facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=0.8, zorder=12))
    else:  # PML bodies
        ax.add_patch(Circle(tuple(m), 0.09, facecolor=P.fill("negative"), edgecolor=P.edge("negative"), lw=0.8, zorder=12))
bio.callout(ax, tuple(mids[0]), (8.0, 7.6), "Nuclear speckle")
bio.callout(ax, tuple(mids[4]), (8.0, 7.0), "Cajal body")
bio.callout(ax, tuple(mids[6]), (8.0, 6.4), "PML body")
bio.callout(ax, (4.3, 3.6), (8.0, 1.3), "Nucleolus")
bio.callout(ax, t["territories"][3]["center"], (8.0, 5.6), "Chromosome territory")
bio.callout(ax, (2.0, 1.75), (0.5, 0.5), "Lamina and envelope")

# B: one territory at the periphery
bio.panel(ax, "B", (10.2, 8.1))
x0, x1, yl = 10.6, 15.6, 1.3
N.lamina(ax, x0, x1, yl + 0.4, depth=0.3)
ax.plot([x0, x1], [yl] * 2, color=P.edge("nucleus"), lw=2.2)
ax.plot([x0, x1], [yl + 0.07] * 2, color=P.edge("nucleus"), lw=1.0)
bio.label(ax, (x1, yl - 0.25), "envelope and lamina", size="tiny", ha="right", color=P.muted())
terr = bio.blob((13.1, 3.9), 2.2, 2.3, wobble=0.08, seed=3, k=10)
ax.add_patch(PathPatch(Path(terr, closed=True), facecolor=P.light("dna"), edgecolor=P.edge("dna"), lw=1.0, zorder=5))
for k in range(7):  # LADs near the lamina
    xc = 11.4 + k * 0.55
    v = bio.blob((xc, 2.05 + 0.15 * rng.random()), 0.26, 0.2, wobble=0.2, seed=20 + k, k=7)
    ax.add_patch(PathPatch(Path(v, closed=True), facecolor=P.edge("dna"), edgecolor=P.edge("dna"), lw=0.6, zorder=6))
for k in range(6):  # A-compartment chromatin towards the interior
    v = bio.blob((12.0 + (k % 3) * 1.0, 4.4 + (k // 3) * 0.9), 0.34, 0.26, wobble=0.2, seed=40 + k, k=7)
    ax.add_patch(PathPatch(Path(v, closed=True), facecolor=P.fill("dna2"), edgecolor=P.edge("dna2"), lw=0.6, zorder=6))
loop = np.array([[14.5, 5.0], [15.4, 5.6], [16.4, 6.2], [16.6, 6.9], [16.0, 7.0], [15.2, 6.3], [14.6, 5.3]])
q = bio.smooth_closed(loop, n=120)
ax.plot(q[:, 0], q[:, 1], color=P.edge("dna"), lw=1.6, zorder=7)
v = bio.blob((17.0, 7.3), 0.42, 0.3, wobble=0.25, seed=2, k=7)
ax.add_patch(PathPatch(Path(v, closed=True), facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.8, zorder=6))
bio.callout(ax, (12.0, 2.1), (11.0, 0.6), "LADs (B compartment)")
bio.callout(ax, (13.15, 4.4), (14.9, 3.6), "A compartment")
bio.callout(ax, (15.7, 6.55), (15.4, 7.7), "active gene loops out")
bio.label(ax, (17.0, 7.85), "speckle", size="tiny")

# C: contact map
bio.panel(ax, "C", (17.6, 8.1))
n = 200
i, j = np.meshgrid(np.arange(n), np.arange(n), indexing="ij")
s = np.abs(i - j) + 1.0
comp = np.where((np.arange(n) // 25) % 2 == 0, 1, -1)
M = s ** -1.0 * (1 + 0.22 * np.outer(comp, comp))
tads = [0, 18, 40, 65, 90, 110, 140, 160, 185, 200]
for a, b in zip(tads[:-1], tads[1:]):
    M[a:b, a:b] *= 2.6
M[60:64, 86:90] *= 12
M[86:90, 60:64] *= 12
M *= np.exp(rng.normal(0, 0.08, M.shape))
c = charts.axes_at(ax, (18.6, 1.6, 4.1, 4.1 * 1.0))
c.imshow(np.log10(M), cmap="magma_r" if not P.is_dark() else "magma", interpolation="nearest")
c.set_xticks([0, 100, 199])
c.set_xticklabels(["0", "5", "10"])
c.set_yticks([0, 100, 199])
c.set_yticklabels(["0", "5", "10"])
charts.style_axes(c, "position / Mb", "position / Mb")
bio.label(ax, (20.65, 6.3), "contact map (simulated)", size="small")
