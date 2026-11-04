"""Asexual (top row) and sexual (bottom row) spores of fungi, schematic and not to a common scale. Asexual:
sporangiospores formed inside a sporangium on a sporangiophore (Rhizopus, Mucor); conidia budded off in
chains from phialides on the swollen vesicle of a conidiophore (Aspergillus); arthroconidia from the
fragmentation of a hypha (Geotrichum); a thick-walled chlamydospore (Candida albicans, many molds). Sexual:
a zygospore between two suspensors after the fusion of two gametangia (Mucoromycota); eight ascospores in an
ascus (Neurospora); four basidiospores on the sterigmata of a basidium (mushrooms); and, for comparison,
blastoconidia budding from a yeast cell (asexual)."""
import numpy as np
from matplotlib.patches import Circle, Ellipse, Rectangle, FancyBboxPatch
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(28, 15)
W, SP = "cell_wall", "na"


def hypha(x0, y0, x1, y1, w=0.28, z=4):
    ax.plot([x0, x1], [y0, y1], color=P.edge(W), lw=w * 22, solid_capstyle="round", zorder=z)
    ax.plot([x0, x1], [y0, y1], color=P.fill("cytoplasm"), lw=w * 15, solid_capstyle="round", zorder=z + 0.1)


def spore(x, y, r, tok=SP, z=8, thick=False):
    ax.add_patch(Circle((x, y), r, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=2.2 if thick else 0.8, zorder=z))


titles = [("sporangiospores", "Rhizopus"), ("conidia", "Aspergillus"), ("arthroconidia", "Geotrichum"),
          ("chlamydospore", "Candida albicans"), ("zygospore", "Rhizopus"), ("ascospores", "Neurospora"),
          ("basidiospores", "Agaricus"), ("blastoconidia", "Saccharomyces")]
for i, (t, g) in enumerate(titles):
    cx = 3.5 + 7.0 * (i % 4); top = 14.4 if i < 4 else 7.0
    bio.label(ax, (cx, top), t, size="small", bold=True)
    bio.label(ax, (cx, top - 0.55), g, size="tiny", italic=True, color=P.muted())
bio.label(ax, (0.3, 11.0), "asexual", size="small", rotation=90, color=P.muted())
bio.label(ax, (0.3, 3.6), "sexual", size="small", rotation=90, color=P.muted())

# 1 sporangium
cx = 3.5
hypha(cx, 8.6, cx, 11.4)
ax.add_patch(Circle((cx, 12.2), 1.15, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=1.2, zorder=6))
rng = np.random.default_rng(1)
for _ in range(40):
    a, r = rng.uniform(0, 2 * np.pi), rng.uniform(0.55, 1.0)
    spore(cx + r * np.cos(a), 12.2 + r * np.sin(a), 0.09)
ax.add_patch(Ellipse((cx, 11.85), 0.9, 1.0, facecolor=P.fill("cytoplasm"), edgecolor=P.edge(W), lw=1.0, zorder=7))
bio.callout(ax, (cx + 0.2, 11.8), (cx + 2.2, 10.0), "columella")
bio.callout(ax, (cx - 0.1, 9.5), (cx - 2.2, 9.2), "sporangiophore")

# 2 conidiophore (Aspergillus)
cx = 10.5
hypha(cx, 8.6, cx, 11.2)
ax.add_patch(Circle((cx, 11.6), 0.55, facecolor=P.fill("cytoplasm"), edgecolor=P.edge(W), lw=1.2, zorder=6))
for a in np.linspace(15, 165, 9):
    ar = np.radians(a)
    bx, by = cx + 0.55 * np.cos(ar), 11.6 + 0.55 * np.sin(ar)
    ax.plot([bx, bx + 0.35 * np.cos(ar)], [by, by + 0.35 * np.sin(ar)], color=P.edge(W), lw=3, zorder=6)
    for j in range(4):
        spore(bx + (0.5 + 0.28 * j) * np.cos(ar), by + (0.5 + 0.28 * j) * np.sin(ar), 0.13, "plant")
bio.callout(ax, (cx + 0.3, 11.5), (cx + 2.4, 9.8), "vesicle, phialides")

# 3 arthroconidia
cx = 17.5
for j in range(6):
    x = cx - 2.4 + 0.85 * j + (0.08 * j)
    ax.add_patch(FancyBboxPatch((x, 11.1), 0.72, 0.5, boxstyle="round,pad=0,rounding_size=0.12",
                                facecolor=P.fill(SP if j > 1 else "cytoplasm"), edgecolor=P.edge(W), lw=1.0, zorder=6))
bio.label(ax, (cx, 10.0), "hypha breaks at its septa", size="tiny", color=P.muted())

# 4 chlamydospore
cx = 24.5
hypha(cx - 2.6, 11.0, cx + 0.2, 11.0)
spore(cx + 0.7, 11.0, 0.6, SP, thick=True)
bio.label(ax, (cx, 10.0), "thick wall, resting", size="tiny", color=P.muted())

# 5 zygospore
cx = 3.5
hypha(cx - 2.6, 3.4, cx - 0.75, 3.4); hypha(cx + 0.75, 3.4, cx + 2.6, 3.4)
spore(cx, 3.4, 0.75, "dna", thick=True)
for dx in np.linspace(-0.45, 0.45, 5):
    ax.plot([cx + dx - 0.08, cx + dx + 0.08], [3.4 + 0.5, 3.4 + 0.62], color=P.edge("dna"), lw=1.2, zorder=9)
bio.callout(ax, (cx - 1.3, 3.5), (cx - 1.6, 1.8), "suspensors")
bio.label(ax, (cx, 5.0), "+ and − gametangia fuse", size="tiny", color=P.muted())

# 6 ascus
cx = 10.5
ax.add_patch(FancyBboxPatch((cx - 0.45, 1.2), 0.9, 4.4, boxstyle="round,pad=0,rounding_size=0.4",
                            facecolor=P.fill("cytoplasm"), edgecolor=P.edge(W), lw=1.2, zorder=6))
for j in range(8):
    ax.add_patch(Ellipse((cx, 1.6 + 0.5 * j), 0.5, 0.42, facecolor=P.fill("rna" if j < 4 else "dna"),
                         edgecolor=P.edge("rna" if j < 4 else "dna"), lw=0.8, zorder=8))
bio.callout(ax, (cx + 0.45, 4.6), (cx + 2.0, 5.4), "ascus")
bio.label(ax, (cx + 2.2, 2.6), "4 + 4 spores:\nan ordered\noctad", size="tiny", color=P.muted())

# 7 basidium
cx = 17.5
ax.add_patch(FancyBboxPatch((cx - 0.5, 1.0), 1.0, 2.8, boxstyle="round,pad=0,rounding_size=0.45",
                            facecolor=P.fill("cytoplasm"), edgecolor=P.edge(W), lw=1.2, zorder=6))
for dx in (-0.4, -0.13, 0.13, 0.4):
    ax.plot([cx + dx * 0.8, cx + dx * 1.8], [3.7, 4.4], color=P.edge(W), lw=1.4, zorder=6)
    ax.add_patch(Ellipse((cx + dx * 1.9, 4.75), 0.32, 0.5, angle=-dx * 40, facecolor=P.fill("rna"), edgecolor=P.edge("rna"), lw=0.8, zorder=8))
bio.callout(ax, (cx + 0.4, 4.2), (cx + 2.2, 5.0), "sterigmata")
bio.callout(ax, (cx + 0.5, 2.0), (cx + 2.2, 1.6), "basidium")

# 8 blastoconidia
cx = 24.5
ax.add_patch(Ellipse((cx, 3.2), 1.6, 1.9, facecolor=P.fill("cytoplasm"), edgecolor=P.edge(W), lw=1.2, zorder=6))
ax.add_patch(Ellipse((cx + 0.95, 4.2), 0.8, 0.85, facecolor=P.fill("cytoplasm"), edgecolor=P.edge(W), lw=1.2, zorder=6))
for (x, y) in ((cx - 0.5, 2.5), (cx - 0.65, 3.4), (cx + 0.3, 2.3)):
    ax.add_patch(Circle((x, y), 0.12, facecolor="none", edgecolor=P.edge(W), lw=1.6, zorder=7))
bio.callout(ax, (cx - 0.65, 3.4), (cx - 2.2, 4.6), "bud scars")
bio.label(ax, (cx, 1.4), "(asexual, for comparison)", size="tiny", color=P.muted())
