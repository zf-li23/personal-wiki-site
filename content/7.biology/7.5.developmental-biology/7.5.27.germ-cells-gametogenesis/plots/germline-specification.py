"""Two ways of setting aside the germ line. A: preformation in Drosophila, pole cells form at the posterior pole
around the pole plasm. B: C. elegans, P granules segregate to the P lineage at each division and P4 founds the
germ line. C: zebrafish, germ plasm collects at the distal ends of the first cleavage furrows and ends up in four
cells. D: induction in the mouse, BMP4 from the extraembryonic ectoderm (and BMP2 from the visceral endoderm)
induces Blimp1-positive PGC precursors in the proximal posterior epiblast at E6.25."""
import numpy as np
from matplotlib.patches import Circle
import wikibio as bio
from wikibio import development as dev, bodyaxes as BA

P = bio.P
fig, ax = bio.canvas(26, 8.0)
ax.set_ylim(1.5, 9.5)
G = "protein"

# A: Drosophila
bio.panel(ax, "A", (0.2, 9.3))
fly = dev.FlyEmbryo(ax, (3.4, 6.0), length=5.6, height=2.2)
fly.domain(0.9, 1.0, "highlight", soft=0.04)
for k, a in enumerate(np.linspace(-1.1, 1.1, 7)):
    c = (fly.x(1.0) + 0.32 * np.cos(a) + 0.1, 6.0 + 0.32 * np.sin(a) * 2.2)
    ax.add_patch(Circle(c, 0.17, facecolor=P.fill(G), edgecolor=P.edge(G), lw=0.7, zorder=14))
bio.callout(ax, (fly.x(1.0) + 0.35, 6.3), (5.8, 8.6), "Pole cells")
bio.callout(ax, (fly.x(0.95), 5.6), (4.4, 3.9), "Pole plasm")
bio.label(ax, (3.4, 3.2), r"$\it{Drosophila}$: pole plasm ($\it{oskar}$)", size="small")

# B: C. elegans P lineage
bio.panel(ax, "B", (7.0, 9.3))
nodes = {"P0": (9.6, 8.4), "AB": (8.4, 7.3), "P1": (10.8, 7.3), "EMS": (9.9, 6.2), "P2": (11.7, 6.2),
         "C": (10.9, 5.1), "P3": (12.5, 5.1), "D": (11.8, 4.0), "P4": (13.2, 4.0)}
edges = [("P0", "AB"), ("P0", "P1"), ("P1", "EMS"), ("P1", "P2"), ("P2", "C"), ("P2", "P3"), ("P3", "D"), ("P3", "P4")]
for a, b in edges:
    ax.plot(*zip(nodes[a], nodes[b]), color=P.muted(), lw=1.0, zorder=3)
for k, (x, y) in nodes.items():
    germ = k.startswith("P")
    bio.box(ax, (x, y), 0.95, 0.55, G if germ else "neutral", k, size="small")
bio.label(ax, (10.6, 3.2), r"$\it{C.\ elegans}$: P granules, PIE-1", size="small")

# C: zebrafish 4-cell stage seen from the animal pole
bio.panel(ax, "C", (14.2, 9.3))
c0 = np.array([16.6, 6.1])
ax.add_patch(Circle(c0, 1.6, facecolor=P.light("animal"), edgecolor=P.edge("animal"), lw=1.2, zorder=4))
for a in (0, 90):
    t = np.radians(a)
    d = np.array([np.cos(t), np.sin(t)])
    ax.plot(*np.array([c0 - 1.6 * d, c0 + 1.6 * d]).T, color=P.edge("animal"), lw=1.0, zorder=5)
    for s in (1, -1):
        ax.add_patch(Circle(tuple(c0 + s * 1.38 * d), 0.15, facecolor=P.fill(G), edgecolor=P.edge(G), lw=0.6, zorder=6))
bio.callout(ax, tuple(c0 + [0, 1.38]), (18.4, 8.6), "Germ plasm at furrow ends")
bio.label(ax, (16.6, 3.2), "Zebrafish: 4 germ-plasm aggregates", size="small")

# D: mouse egg cylinder E6.25
bio.panel(ax, "D", (19.8, 9.3))
m = BA.egg_cylinder(ax, (22.6, 6.0), 1.1, 4.0, streak=False, node=False)
cx, cy = 22.6, 6.0
for k, (dx, dy) in enumerate(((0.82, -0.05), (0.78, -0.32), (0.62, -0.18), (0.66, 0.08))):
    ax.add_patch(Circle((cx + dx, cy + dy), 0.12, facecolor=P.fill(G), edgecolor=P.edge(G), lw=0.6, zorder=12))
bio.arrow(ax, (cx - 0.1, cy + 1.3), (cx + 0.45, cy + 0.15), kind="activation", color=P.ink())
bio.label(ax, (cx - 1.6, cy + 1.6), "BMP4 (ExE)", size="small")
bio.callout(ax, (cx + 0.8, cy - 0.2), (25.6, 4.4), "Blimp1+ PGC\nprecursors")
bio.label(ax, (22.6, 3.2), "Mouse: induction (BMP4, Wnt3)", size="small")
bio.label(ax, (cx - 1.8, cy - 2.2), "anterior", size="tiny", color=P.muted())
bio.label(ax, (cx + 1.8, cy - 2.2), "posterior", size="tiny", color=P.muted())

bio.label(ax, (7.2, 2.2), "Preformation: inherited germ plasm (fly, worm, fish, frog, bird)", size="normal")
bio.label(ax, (22.6, 2.2), "Epigenesis: induction (mammals, axolotl)", size="normal")
