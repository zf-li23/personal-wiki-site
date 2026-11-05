"""The five modes of plasmogamy in fungi and fungus-like organisms (after Alexopoulos et al. 1996),
schematic. Orange and blue nuclei: the two mating types (or sexes)."""
import numpy as np
from matplotlib.patches import Circle, Ellipse, Polygon

import wikibio as bio
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(32, 9)


def nuc(xy, tok, r=0.14):
    ax.add_patch(Circle(xy, r, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.6, zorder=14))


def cellb(xy, w, h, tok="lipid_tail", angle=0, z=8):
    ax.add_patch(Ellipse(xy, w, h, angle=angle, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.9, zorder=z))


def flag(x, y, ang, L=0.9):
    t = np.linspace(0, 1, 30); a = np.radians(ang)
    u, n = np.array([np.cos(a), np.sin(a)]), np.array([-np.sin(a), np.cos(a)])
    pts = np.array([[x, y]]) + np.outer(t * L, u) + np.outer(0.07 * np.sin(t * 12), n)
    ax.plot(pts[:, 0], pts[:, 1], color=P.edge("lipid_tail"), lw=0.9, zorder=9)


def title(x, letter, t):
    bio.panel(ax, letter, (x - 0.1, 8.8))
    bio.label(ax, (x + 2.9, 8.3), t, size="small", bold=True)


# A planogametic copulation (anisogamy)
title(0.3, "A", "Planogametic copulation")
cellb((1.6, 5.6), 1.0, 1.0); nuc((1.6, 5.6), "rna"); flag(1.6, 5.1, -90, 1.1)
cellb((4.0, 5.9), 0.55, 0.55); nuc((4.0, 5.9), "dna", 0.1); flag(4.0, 5.62, -90, 0.9)
bio.arrow(ax, (2.6, 4.0), (3.6, 3.0), kind="process")
cellb((3.2, 2.0), 1.15, 1.15); nuc((3.05, 2.0), "rna"); nuc((3.35, 2.0), "dna", 0.1)
bio.label(ax, (1.6, 7.0), "female gamete", size="tiny"); bio.label(ax, (4.0, 7.0), "male gamete", size="tiny")
bio.label(ax, (3.1, 0.6), "Allomyces", size="small", italic=True)

# B gametangial contact
title(6.8, "B", "Gametangial contact")
plant.hypha(ax, np.array([[7.0, 3.0], [9.2, 3.0]]), width=0.3, septa=None, nuclei=0, tip=False)
ax.add_patch(Circle((9.8, 4.4), 1.3, facecolor=P.fill("lipid_tail"), edgecolor=P.edge("lipid_tail"), lw=1.0, zorder=8))
plant.hypha(ax, np.array([[9.4, 3.0], [9.6, 3.2]]), width=0.3, septa=None, nuclei=0, tip=False)
for xy in [(9.4, 4.8), (10.2, 4.9), (9.6, 4.0), (10.3, 4.0)]:
    ax.add_patch(Circle(xy, 0.34, facecolor=P.light("rna"), edgecolor=P.edge("rna"), lw=0.7, zorder=9)); nuc(xy, "rna", 0.1)
ax.add_patch(Ellipse((11.9, 5.6), 1.4, 0.7, angle=-25, facecolor=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.9, zorder=10))
plant.hypha(ax, np.array([[12.6, 5.3], [12.9, 3.0]]), width=0.22, septa=None, nuclei=0, tip=False)
ax.plot([11.4, 10.4], [5.4, 4.9], color=P.edge("dna"), lw=1.6, zorder=11)
nuc((10.55, 4.95), "dna", 0.08)
bio.callout(ax, (9.0, 3.6), (7.3, 6.6), "Oogonium with eggs")
bio.callout(ax, (12.2, 5.9), (11.2, 7.6), "Antheridium")
bio.callout(ax, (10.9, 5.15), (10.6, 1.6), "Fertilization tube")
bio.label(ax, (9.8, 0.6), "Oomycetes", size="small")

# C gametangial copulation
title(13.6, "C", "Gametangial copulation")
plant.hypha(ax, np.array([[14.0, 1.6], [14.6, 3.2], [15.6, 4.0]]), width=0.34, septa=None, nuclei=0, tip=False)
plant.hypha(ax, np.array([[19.2, 1.6], [18.6, 3.2], [17.6, 4.0]]), width=0.34, septa=None, nuclei=0, tip=False, token="ovule")
ax.add_patch(Ellipse((16.6, 4.3), 1.7, 1.3, facecolor=P.fill("chromatin"), edgecolor=P.edge("chromatin"), lw=1.0, zorder=9))
rng = np.random.default_rng(2)
for k in range(10):
    a = rng.uniform(0, 2 * np.pi); r = rng.uniform(0.1, 0.5)
    p = np.array([16.6 + 1.2 * r * np.cos(a), 4.3 + 0.8 * r * np.sin(a)])
    nuc(p - [0.07, 0], "rna", 0.07); nuc(p + [0.07, 0], "dna", 0.07)
bio.callout(ax, (15.2, 3.7), (15.0, 6.3), "Suspensor (+)")
bio.callout(ax, (18.0, 3.7), (18.2, 6.3), "Suspensor (−)")
bio.callout(ax, (16.6, 4.95), (16.6, 7.4), "Young zygosporangium")
bio.label(ax, (16.6, 0.6), "Rhizopus", size="small", italic=True)

# D spermatization
title(20.3, "D", "Spermatization")
plant.hypha(ax, np.array([[21.0, 1.6], [21.4, 4.0], [22.6, 5.6]]), width=0.22, septa=0.9, nuclei=1, token="ovule")
for xy in [(23.3, 6.2), (24.1, 6.5), (23.8, 7.1)]:
    cellb(xy, 0.42, 0.3, tok="dna", z=10); nuc(xy, "dna", 0.07)
bio.arrow(ax, (25.2, 7.5), (24.4, 6.9), kind="process")
bio.label(ax, (25.3, 7.8), "by insects", size="tiny", ha="left")
bio.callout(ax, (22.0, 4.9), (24.6, 4.0), "Receptive hypha\n(trichogyne)")
bio.callout(ax, (24.1, 6.5), (25.6, 5.5), "Spermatia")
bio.label(ax, (22.9, 0.6), "Rust fungi", size="small")

# E somatogamy
title(27.0, "E", "Somatogamy")
t = np.linspace(0, 1, 20)
plant.hypha(ax, np.c_[27.4 + 4.0 * t, 6.4 + 0.1 * t], width=0.26, septa=1.0, nuclei=1, token="lipid_tail")
plant.hypha(ax, np.c_[27.4 + 4.0 * t, 5.0 - 0.1 * t], width=0.26, septa=1.0, nuclei=1, token="ovule")
ax.plot([29.4, 29.4], [5.0, 6.4], color=P.edge("lipid_tail"), lw=5, zorder=5, solid_capstyle="butt")
bio.arrow(ax, (29.4, 4.4), (29.4, 3.4), kind="process")
plant.hypha(ax, np.c_[27.4 + 4.0 * t, 2.4 + 0 * t], width=0.32, septa=1.2, nuclei=2, clamps=True)
bio.label(ax, (29.4, 7.2), "two monokaryotic hyphae", size="tiny")
bio.label(ax, (29.4, 1.5), "dikaryon with clamp connections", size="tiny")
bio.label(ax, (29.4, 0.6), "Mushroom-forming basidiomycetes", size="small")
