"""Stem-cell-based embryo models and the stages they mimic (schematic, not to scale).

Top: the developmental time line of the mouse (E, embryonic day) and human (days after fertilization), with the
14-day limit on culturing human embryos. Below: A, blastoid: ES cells (green) and trophoblast stem cells (pink)
aggregated in microwells form a blastocyst-like cyst with an inner cluster. B, gastruloid: about 300 ES cells
aggregated and given a pulse of the Wnt agonist CHIR99021 break symmetry, elongate, express Brachyury at one end
(red: mesoderm) and form somite-like blocks and a gut-like tube (yellow) along an axis with colinear Hox
expression, but no brain, no extraembryonic tissue. C, ETX/SEM: ES, trophoblast stem and extraembryonic
endoderm cells (or ES cells with induced Gata4 and Cdx2) assemble into an egg-cylinder-like structure that
gastrulates and reaches the stage of neural folds and a beating heart tube. D, 2D micropatterned colony of human
ES cells given BMP4: rings of ectoderm (blue, center), mesoderm (red), endoderm (yellow) and an outer
trophectoderm-like ring (pink), set by the colony edge.
"""

from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Polygon
import numpy as np
import wikibio as bio

P = bio.P
LW = bio.core.LINE
G = {"ecto": "channel", "meso": "muscle", "endo": "highlight", "epi": "positive", "tro": "receptor", "pre": "lipid"}
fig, ax = bio.canvas(32.0, 15.0)

# time line
y = 13.2
ax.plot([1.0, 31.0], [y, y], color=P.ink(), lw=1.0)
marks = ((2.0, "E3.5 / d5", "blastocyst"), (8.0, "E6.5 / d14", "gastrulation"), (16.0, "E8.5 / d21", "neurulation, heart tube"),
         (26.0, "E9.5 / d28", "organogenesis"))
for xx, t1, t2 in marks:
    ax.plot([xx, xx], [y - 0.2, y + 0.2], color=P.ink(), lw=1.0)
    bio.label(ax, (xx, y + 0.65), t1, size="tiny")
    bio.label(ax, (xx, y - 0.6), t2, size="tiny", color=P.muted())
ax.plot([8.0, 8.0], [y - 1.0, y + 1.3], color=P.edge("negative"), lw=1.2, ls=(0, (3, 2)))
bio.label(ax, (8.2, y + 1.4), "14-day limit (human embryos)", size="tiny", ha="left", color=P.edge("negative"))


def cell(c, r, tok, z=6):
    ax.add_patch(Circle(c, r, fc=P.fill(tok), ec=P.edge(tok), lw=LW * 0.6, zorder=z))


# A blastoid
bio.panel(ax, "A", (0.3, 10.6))
bio.label(ax, (1.5, 10.3), "Blastoid", size="small", bold=True, ha="left")
c = (4.0, 6.6)
ax.add_patch(Circle(c, 2.0, fc=P.light("vacuole"), ec="none", zorder=4))
for k in range(18):
    a = 2 * np.pi * k / 18
    cell((c[0] + 1.85 * np.cos(a), c[1] + 1.85 * np.sin(a)), 0.36, G["tro"])
for dx, dy in ((0, 1.1), (-0.45, 1.0), (0.45, 1.0), (-0.22, 0.65), (0.22, 0.65)):
    cell((c[0] + dx, c[1] + dy), 0.3, G["epi"], z=7)
bio.label(ax, (4.0, 3.9), "ESC + TSC (or naive human PSC)", size="tiny")
bio.label(ax, (4.0, 3.3), "mimics: blastocyst; implants, no further development", size="tiny", color=P.muted())

# B gastruloid
bio.panel(ax, "B", (8.3, 10.6))
bio.label(ax, (9.5, 10.3), "Gastruloid", size="small", bold=True, ha="left")
t = np.linspace(0, 1, 60)
xs = 9.6 + 5.6 * t
w = 0.75 + 0.35 * np.sin(np.pi * t) - 0.25 * t
top = np.column_stack([xs, 6.6 + w])
bot = np.column_stack([xs[::-1], 6.6 - w[::-1]])
ax.add_patch(Polygon(np.vstack([top, bot]), closed=True, fc=P.fill(G["ecto"]), ec=P.edge(G["ecto"]), lw=LW, zorder=4))
for k in range(5):
    for s in (1, -1):
        ax.add_patch(FancyBboxPatch((10.3 + 0.75 * k, 6.6 + s * 0.42 - 0.22), 0.6, 0.44,
                                    boxstyle="round,pad=0,rounding_size=0.12", fc=P.fill(G["meso"]),
                                    ec=P.edge(G["meso"]), lw=LW * 0.6, zorder=6))
ax.plot([10.0, 14.2], [6.6, 6.6], color=P.edge(G["endo"]), lw=3.0, zorder=5)
ax.add_patch(Ellipse((14.6, 6.6), 0.9, 1.0, fc=P.fill(G["meso"]), ec=P.edge(G["meso"]), lw=LW * 0.7, zorder=6))
bio.label(ax, (14.6, 8.0), r"$\it{Bra}$+ tail", size="tiny")
bio.label(ax, (10.6, 8.0), "anterior", size="tiny", color=P.muted())
bio.label(ax, (12.4, 3.9), "~300 ESC + CHIR pulse", size="tiny")
bio.label(ax, (12.4, 3.3), "mimics: trunk axis, somites, Hox colinearity; no brain", size="tiny", color=P.muted())

# C ETX / SEM
bio.panel(ax, "C", (16.3, 10.6))
bio.label(ax, (17.5, 10.3), "ETX / SEM embryo", size="small", bold=True, ha="left")
c = (20.6, 6.6)
ax.add_patch(Ellipse(c, 3.2, 5.2, fc=P.fill(G["pre"]), ec=P.edge(G["pre"]), lw=LW, zorder=4))
ax.add_patch(Ellipse((c[0], c[1] + 1.4), 2.6, 1.8, fc=P.fill(G["tro"]), ec=P.edge(G["tro"]), lw=LW * 0.8, zorder=5))
ax.add_patch(Ellipse((c[0], c[1] - 0.8), 2.4, 2.8, fc=P.fill(G["ecto"]), ec=P.edge(G["ecto"]), lw=LW * 0.8, zorder=5))
ax.add_patch(Ellipse((c[0] + 0.55, c[1] - 1.1), 0.8, 1.6, fc=P.fill(G["meso"]), ec=P.edge(G["meso"]), lw=LW * 0.7, zorder=6))
bio.label(ax, (c[0] + 2.4, c[1] + 1.6), "extraembryonic\nectoderm", size="tiny", ha="left")
bio.label(ax, (c[0] + 2.4, c[1] - 1.6), "visceral\nendoderm", size="tiny", ha="left")
bio.label(ax, (20.6, 3.3), "ESC + TSC + XEN: to neural folds, heart tube", size="tiny", color=P.muted())

# D micropattern
bio.panel(ax, "D", (24.6, 10.6))
bio.label(ax, (25.8, 10.3), "2D micropattern + BMP4", size="small", bold=True, ha="left")
c = (28.5, 6.6)
for r, tok in ((2.2, G["tro"]), (1.75, G["endo"]), (1.3, G["meso"]), (0.85, G["ecto"])):
    ax.add_patch(Circle(c, r, fc=P.fill(tok), ec=P.edge(tok), lw=LW * 0.7, zorder=5))
bio.label(ax, (28.5, 3.9), "human ESC colony, 500 µm", size="tiny")
bio.label(ax, (28.5, 3.3), "rings: ecto, meso, endo, TE-like", size="tiny", color=P.muted())
bio.label(ax, (16.0, 1.4), "Embryo models are not embryos: they lack parts, are inefficient (often < 1-5 % form correctly)"
          " and cannot develop to term", size="tiny", color=P.muted())
