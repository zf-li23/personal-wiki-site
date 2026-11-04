"""Shapes and arrangements of prokaryotic cells. Top: cocci and arrangements with division planes.
Bottom: rods, vibrio, spirillum, spirochete, stalked, budding, filament, square archaeon."""
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch

import wikibio as bio
from wikibio import microbio as M

P = bio.P
fig, ax = bio.canvas(28, 10)
T = "bacterium"


def name(x, y, kind, genus):
    bio.label(ax, (x, y), kind, size="tiny")
    bio.label(ax, (x, y - 0.4), genus, size="tiny", italic=True, color=P.muted())


def plane(a, b):
    ax.plot([a[0], b[0]], [a[1], b[1]], color=P.edge("highlight"), lw=0.9, ls="--", zorder=12)


bio.label(ax, (0.3, 9.6), "Cocci: arrangements follow the planes of division", size="normal", bold=True, ha="left")
y = 7.6
r = 0.38
M.coccus(ax, (1.6, y), r, token=T)
name(1.6, 6.4, "single coccus", "")
M.diplococcus(ax, (4.4, y), r, token=T)
plane((4.4, y - 0.7), (4.4, y + 0.7))
name(4.4, 6.4, "diplococci", "Neisseria")
M.chain(ax, (6.6, y), 6, 0.3, angle=0.0, token=T, wiggle=0.08)
name(8.1, 6.4, "chain: one plane", "Streptococcus")
for dx in (-0.34, 0.34):
    for dy in (-0.34, 0.34):
        M.coccus(ax, (12.4 + dx, y + dy), 0.32, token=T)
plane((12.4, y - 0.9), (12.4, y + 0.9))
plane((11.5, y), (13.3, y))
name(12.4, 6.4, "tetrad: two planes", "Micrococcus")
# packet of eight: 2x2 front, offset back layer
for dx in (-0.32, 0.32):
    for dy in (-0.32, 0.32):
        M.coccus(ax, (16.2 + dx + 0.28, y + dy + 0.28), 0.3, token=T, zorder=6)
for dx in (-0.32, 0.32):
    for dy in (-0.32, 0.32):
        M.coccus(ax, (16.2 + dx, y + dy), 0.3, token=T, zorder=9)
name(16.4, 6.4, "packet: three planes", "Sarcina")
M.cluster(ax, (20.6, y + 0.25), 0.26, n=11, token=T)
name(20.6, 6.4, "cluster: random planes", "Staphylococcus")
# square archaeon
for k in range(2):
    ax.add_patch(FancyBboxPatch((23.6 + 1.45 * k, y - 0.6), 1.2, 1.2, boxstyle="round,pad=0.0,rounding_size=0.08",
                                facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=1.2, zorder=8))
name(25.0, 6.4, "square archaeon", "Haloquadratum")

bio.label(ax, (0.3, 4.6), "Rods, curved and helical cells, appendaged and filamentous forms", size="normal", bold=True,
          ha="left")
y = 2.5
M.bacillus(ax, (1.6, y), 1.6, 0.55, token=T)
name(1.6, 1.2, "rod", "Escherichia")
for k in range(3):
    M.bacillus(ax, (3.5 + 1.15 * k, y), 1.1, 0.45, token=T)
name(4.65, 1.2, "chain of rods", "Bacillus")
M.vibrio(ax, (8.2, y), 1.3, 0.45, token=T, flagella=None)
name(8.2, 1.2, "vibrio", "Vibrio")
M.spirillum(ax, (9.8, y), (12.2, y), width=0.26, turns=2.0, amplitude=0.3, token=T, flagella=None)
name(11.0, 1.2, "spirillum", "Spirillum")
M.spirochete(ax, (13.0, y), (15.6, y), width=0.11, turns=7, amplitude=0.13, token=T)
name(14.3, 1.2, "spirochete", "Treponema")
# stalked Caulobacter: crescent body + stalk + holdfast
M.vibrio(ax, (17.4, y + 0.3), 1.2, 0.42, token=T, flagella=None, angle=0)
ax.plot([16.85, 16.6, 16.5], [y + 0.25, y - 0.4, y - 0.9], color=P.edge(T), lw=1.6, zorder=7)
ax.add_patch(Circle((16.5, y - 0.95), 0.08, color=P.edge("carbohydrate"), zorder=8))
name(17.3, 1.2, "stalked", "Caulobacter")
# budding Hyphomicrobium
M.bacillus(ax, (19.4, y + 0.1), 0.9, 0.6, token=T)
ax.plot([19.85, 20.6], [y + 0.1, y + 0.1], color=P.edge(T), lw=1.6, zorder=7)
M.coccus(ax, (20.85, y + 0.1), 0.28, token=T)
name(20.1, 1.2, "budding", "Hyphomicrobium")
# filament of cells
for k in range(7):
    ax.add_patch(FancyBboxPatch((22.1 + 0.62 * k, y - 0.28), 0.58, 0.56, boxstyle="round,pad=0,rounding_size=0.12",
                                facecolor=P.fill("chloroplast"), edgecolor=P.edge("chloroplast"), lw=1.0, zorder=8))
name(24.3, 1.2, "filament", "Oscillatoria")
