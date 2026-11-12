# Growth and polymorphism of an encrusting bryozoan colony (model and schematic). A: a colony grown from a
# single ancestrula by budding on a square grid of zooid sites: at each budding round every zooid on the
# margin buds into each empty neighbouring site with probability p = 0.5 (an Eden-type model); zooids are
# coloured by the round in which they were budded. B: number of zooids against budding rounds; because only
# marginal zooids bud, the colony area grows as the square of time (dashed: c t^2), far slower than the
# doubling that would follow if every zooid budded (dotted). C: polymorphic zooids of a cheilostome
# (schematic): feeding autozooids, an avicularium with a mandible, a vibraculum with a long seta, and an
# ovicell (brood chamber) above a zooid.
import numpy as np
from matplotlib.patches import Circle, Rectangle
import wikibio as bio
from wikibio import quant

P = bio.P
rng = np.random.default_rng(0)
G, ROUNDS, PB = 41, 18, 0.5
age = -np.ones((G, G), int)
age[G // 2, G // 2] = 0
counts = [1]
for r in range(1, ROUNDS + 1):
    occ = age >= 0
    new = np.zeros_like(occ)
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nb = np.roll(occ, (dx, dy), axis=(0, 1))
        new |= nb & ~occ & (rng.random(occ.shape) < PB)
    age[new] = r
    counts.append(int((age >= 0).sum()))
counts = np.array(counts)

fig, ax = bio.canvas(30, 11.0)
# ---------------- A ----------------
bio.panel(ax, "A", (0.2, 10.8))
bio.label(ax, (5.2, 10.5), "Encrusting colony grown by marginal budding", size="small", bold=True)
cell = 9.0 / G
x0, y0 = 0.8, 0.6
young, old = P.fill("dna"), P.fill("bone")
for i in range(G):
    for j in range(G):
        if age[i, j] >= 0:
            t = age[i, j] / ROUNDS
            col = P.mix(old, young, t)
            ax.add_patch(Rectangle(
                (x0 + i * cell, y0 + j * cell), cell * 0.92, cell * 0.92, facecolor=col, edgecolor=P.edge("neutral"),
                lw=0.3, zorder=5))
bio.callout(ax, (x0 + (G // 2 + 0.45) * cell, y0 + (G // 2 + 0.45) * cell), (8.6, 8.8), "Ancestrula")
bio.label(ax, (10.0, 2.0), "old", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (10.0, 1.4), "young (margin)", size="tiny", color=P.muted(), ha="left")
ax.add_patch(Rectangle((9.6, 1.85), 0.3, 0.3, facecolor=old, lw=0.3,
                                                                   edgecolor=P.edge("neutral")))
ax.add_patch(Rectangle((9.6, 1.25), 0.3, 0.3, facecolor=young, lw=0.3,
                                                                   edgecolor=P.edge("neutral")))

# ---------------- B ----------------
bio.panel(ax, "B", (12.6, 10.8))
pb = quant.Plot(ax, (14.2, 1.6, 5.6, 7.8), (0, ROUNDS), (1, 1e4), ylog=True, xlabel="Budding rounds  t",
                ylabel="Number of zooids  N", xticks=[0, 6, 12, 18], yticks=[(1, "1"), (10, "10"), (100, "10$^2$"),
                                                                                   (1000, "10$^3$"), (1e4, "10$^4$")])
t = np.arange(ROUNDS + 1)
pb.points(t, counts, token="dna", r=0.08)
c = np.sum(counts[6:] * t[6:] ** 2) / np.sum(t[6:] ** 4)
tt = np.linspace(1, ROUNDS, 100)
pb.line(tt, c * tt ** 2, token="dna", dashed=True, )
pb.text(14.5, 160, f"N = {c:.1f} t$^2$", size="tiny", color=quant.line_color("dna"))
te = np.linspace(0, 13.2, 100)
pb.line(te, 2 ** te, token="negative", dotted=True, )
pb.text(9.6, 3000, "every zooid buds: 2$^t$", size="tiny", ha="left", color=quant.line_color("negative"))

# ---------------- C ----------------
bio.panel(ax, "C", (21.2, 10.8))
bio.label(ax, (25.6, 10.5), "Polymorphic zooids (cheilostome)", size="small", bold=True)


def zooid(cx, cy, w=1.5, h=2.4):
    bio.shape(ax, [[cx - w / 2, cy - h / 2], [cx + w / 2, cy - h / 2], [cx + w / 2, cy + h / 2], [cx - w / 2, cy + h / 2]],
              token="bone", lw=0.8, zorder=5)
    t = np.linspace(0, 2 * np.pi, 40)
    ax.fill(cx + 0.35 * np.cos(t), cy + h / 2 - 0.45 + 0.25 * np.sin(t), facecolor=P.surface(), edgecolor=P.edge("bone"),
            lw=0.6, zorder=6)


for k, cx in enumerate((22.6, 24.4, 26.2, 28.0)):
    zooid(cx, 4.0)
for k, cx in enumerate((22.6, 26.2)):        # extended lophophores on two autozooids
    for a in np.linspace(np.pi * 0.25, np.pi * 0.75, 7):
        ax.plot([cx, cx + 1.2 * np.cos(a)], [5.0, 5.0 + 1.2 * np.sin(a)], color=P.edge("mesoderm"), lw=1.4, zorder=8)
# ovicell above zooid 2
t = np.linspace(0, np.pi, 40)
ax.fill(24.4 + 0.7 * np.cos(t), 5.25 + 0.6 * np.sin(t), facecolor=P.fill("bone"), edgecolor=P.edge("bone"), lw=0.8, zorder=7)
ax.add_patch(Circle((24.4, 5.5), 0.22, facecolor=P.fill("highlight"),
                                                                edgecolor=P.edge("highlight"), lw=0.6, zorder=8))
# avicularium between zooids 3 and 4 (small beak-like zooid)
bio.shape(ax, [[27.0, 6.0], [27.8, 6.0], [27.8, 6.8], [27.0, 6.8]], token="bone", lw=0.8, zorder=7)
ax.plot([27.1, 27.75, 27.3], [6.8, 6.8, 7.5], color=P.ink(), lw=1.6, zorder=9)
# vibraculum next to zooid 1 (long seta)
bio.shape(ax, [[21.4, 2.0], [21.8, 2.0], [21.8, 2.5], [21.4, 2.5]], token="bone", lw=0.8, zorder=7)
ax.plot([21.6, 21.0, 20.9], [2.5, 4.5, 6.8], color=P.ink(), lw=1.2, zorder=9)
bio.callout(ax, (22.6, 6.0), (22.2, 8.6), "Autozooid (feeding)")
bio.callout(ax, (24.4, 5.7), (24.6, 9.4), "Ovicell with embryo")
bio.callout(ax, (27.6, 7.3), (28.6, 8.6), "Avicularium")
bio.callout(ax, (20.95, 6.0), (20.4, 8.0), "Vibraculum")
bio.callout(ax, (24.4, 4.75), (24.0, 1.2), "Orifice (operculum)")
bio.callout(ax, (28.7, 3.0), (28.6, 1.6), "Zooecium")
