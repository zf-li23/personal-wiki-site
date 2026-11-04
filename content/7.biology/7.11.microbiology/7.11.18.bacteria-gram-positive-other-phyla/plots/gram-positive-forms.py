"""Cell forms of Bacillota and Actinomycetota (schematic, not to a common scale; approximate sizes in the
labels). Top: chains of cocci (Streptococcus), grape-like clusters (Staphylococcus), a rod with a central
endospore (Bacillus), a rod with a terminal, swollen endospore ("drumstick", Clostridium tetani), and the
flask-shaped, wall-less cell of Mycoplasma pneumoniae with its attachment organelle. Bottom: club-shaped
cells in V and palisade arrangements after snapping division (Corynebacterium), slender rods in cords
(Mycobacterium), branching substrate hyphae with an aerial hypha that ends in a chain of spores
(Streptomyces), and a giant cell of Epulopiscium with two internal daughter cells."""
import numpy as np
from matplotlib.patches import Circle, Ellipse

import wikibio as bio
from wikibio import microbio as M

P = bio.P
fig, ax = bio.canvas(25, 12)


def name(x, y, genus, size):
    bio.label(ax, (x, y), genus, size="normal", italic=True)
    bio.label(ax, (x, y - 0.5), size, size="tiny", color=P.muted())


def spore(c, r=0.22):
    ax.add_patch(Ellipse(c, 2.2 * r, 1.6 * r, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"),
                         lw=1.0, zorder=12))


M.chain(ax, (0.9, 9.0), 6, 0.3, angle=0.1, gram="+", seed=2)
name(2.4, 7.0, "Streptococcus", "cocci 0.8 µm, chains")
M.cluster(ax, (6.6, 9.0), 0.32, n=10, gram="+")
name(6.6, 7.0, "Staphylococcus", "cocci 1 µm, clusters")
M.bacillus(ax, (11.0, 9.0), 2.6, 0.85, gram="+")
spore((11.0, 9.0))
name(11.0, 7.0, "Bacillus", "1 x 3 µm, central spore")
M.bacillus(ax, (15.2, 9.0), 2.6, 0.5, gram="+")
ax.add_patch(Circle((16.6, 9.0), 0.42, facecolor=P.fill("gram_pos"), edgecolor=P.edge("gram_pos"), lw=1.1, zorder=9))
spore((16.6, 9.0), 0.3)
name(15.5, 7.0, "Clostridium tetani", "terminal spore")
# Mycoplasma pneumoniae: flask shape, no wall (drawn in membrane colour)
pts = [(20.1, 9.0), (20.4, 9.5), (21.1, 9.58), (21.7, 9.25), (22.35, 9.1), (22.5, 9.0), (22.35, 8.9),
       (21.7, 8.75), (21.1, 8.42), (20.4, 8.5)]
bio.shape(ax, bio.smooth_closed(pts), token="membrane", lw=1.1, zorder=8)
bio.callout(ax, (22.4, 9.0), (22.9, 9.9), "attachment organelle", size="tiny")
name(21.3, 7.0, "Mycoplasma pneumoniae", "0.3 x 1-2 µm, no wall")

# bottom row
for (x, y, a) in [(1.4, 3.8, 70), (1.95, 3.8, 110), (2.9, 4.0, 90), (3.35, 4.0, 90), (3.8, 4.0, 90), (2.4, 2.9, 20)]:
    M.bacillus(ax, (x, y), 1.4, 0.42, angle=a, gram="+")
name(2.6, 1.6, "Corynebacterium", "0.5 x 2 µm, V and palisades")
rng = np.random.default_rng(3)
for k in range(9):
    M.bacillus(ax, (6.3 + 0.18 * k, 3.4 + 0.12 * np.sin(k)), 1.6, 0.26, angle=78 + rng.uniform(-6, 6), gram="+",
               token="neutral")
bio.label(ax, (7.1, 4.75), "cord", size="tiny", color=P.muted())
name(7.1, 1.6, "Mycobacterium", "0.4 x 3 µm, acid-fast")
# Streptomyces mycelium
seg = [((10.0, 2.6), (13.8, 2.8)), ((11.0, 2.65), (10.6, 3.6)), ((12.2, 2.7), (12.9, 3.5)), ((13.0, 2.75), (13.6, 2.1)),
       ((10.6, 3.6), (10.0, 4.0))]
for a, b in seg:
    ax.plot([a[0], b[0]], [a[1], b[1]], color=P.edge("gram_pos"), lw=3.2, solid_capstyle="round", zorder=7)
ax.plot([12.2, 12.4, 12.3, 12.5], [2.7, 3.6, 4.2, 4.6], color=P.edge("gram_pos"), lw=3.2, solid_capstyle="round",
        zorder=7)
for k in range(7):
    ang = k * 0.55
    ax.add_patch(Circle((12.5 + 0.33 * np.sin(ang) + 0.05 * k, 4.75 + 0.23 * k), 0.15, facecolor=P.fill("highlight"),
                        edgecolor=P.edge("highlight"), lw=0.8, zorder=9))
bio.callout(ax, (12.9, 5.6), (13.9, 5.8), "spore chain", size="tiny")
bio.callout(ax, (11.4, 2.68), (11.0, 1.95 + 0.5), "substrate hyphae", size="tiny")
name(12.0, 1.0 + 0.6, "Streptomyces", "hyphae 0.5-1 µm wide")
# Epulopiscium
ax.add_patch(Ellipse((19.6, 3.4), 6.0, 1.6, facecolor=P.fill("gram_pos"), edgecolor=P.edge("gram_pos"), lw=1.2, zorder=6))
for cx in (18.3, 20.9):
    ax.add_patch(Ellipse((cx, 3.4), 2.0, 0.8, facecolor=P.light("gram_pos"), edgecolor=P.edge("gram_pos"), lw=0.9,
                         zorder=7))
bio.callout(ax, (20.9, 3.6), (22.9, 4.8), "daughter cells", size="tiny")
name(19.6, 1.6, "Epulopiscium", "up to 80 x 600 µm")
