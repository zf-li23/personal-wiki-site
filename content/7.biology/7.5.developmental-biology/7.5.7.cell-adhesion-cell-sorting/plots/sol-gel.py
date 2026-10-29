"""Sol-gel transition of a matrix network of bivalent A and trivalent B molecules.

A: a tree grown from an A molecule: A (rods with two binding ends) bind only B (Y-shaped, three
binding sites) and vice versa; each free A end binds a B with probability p', each free B site binds
an A with probability p (here sketched, not simulated).
B: mean number of A molecules in the tree rooted at an A, <n_A> = 1 + 4 p p' / (1 - 2 p p'), for
p = p' (diverging at the gel point 2 p p' = 1, p = 1/sqrt(2)); dots: Monte Carlo trees (4000 per
point). Right axis: gel fraction, the probability that an A molecule belongs to an infinite network,
1 - f_A^2 with f_A = q' + p' f_B, f_B = (q + p f_A)^2 (smallest root), q = 1 - p, q' = 1 - p'.
"""

import numpy as np

import wikibio as bio
from wikibio import charts, quant

P = bio.P
rng = np.random.default_rng(2)

fig, ax = bio.canvas(28.0, 10.6)
bio.panel(ax, "A", (0.1, 10.5))

# sketch of a branched tree: a radial layout, fixed pattern of occupied sites
C0 = np.array([6.0, 6.0])
nodes, links, free = [], [], []
present = iter([1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0])


def place(kind, ang, lo, hi, rad, parent, depth):
    xy = C0 + rad * np.array([np.cos(ang), np.sin(ang)])
    nodes.append((xy, kind))
    me = len(nodes) - 1
    if parent is not None:
        links.append((parent, me))
    if depth == 0:
        return
    nchild = 2 if kind == "B" else 1
    w = (hi - lo) / nchild
    for c in range(nchild):
        a0, a1 = lo + c * w, lo + (c + 1) * w
        if next(present, 0):
            place("A" if kind == "B" else "B", (a0 + a1) / 2, a0, a1, rad + 1.15, me, depth - 1)
        else:
            free.append((xy, (a0 + a1) / 2))


nodes.append((C0, "A"))
for side, (lo, hi) in enumerate(((-np.pi / 2, np.pi / 2), (np.pi / 2, 3 * np.pi / 2))):
    place("B", (lo + hi) / 2, lo, hi, 1.25, 0, 3)
for i, j in links:
    ax.plot([nodes[i][0][0], nodes[j][0][0]], [nodes[i][0][1], nodes[j][0][1]], color=P.ink(), lw=1.2, zorder=3)
for xy, a in free:
    ax.plot([xy[0], xy[0] + 0.5 * np.cos(a)], [xy[1], xy[1] + 0.5 * np.sin(a)], color=P.muted(), lw=1.0,
            ls=(0, (2, 1.5)), zorder=3)
for xy, t in nodes:
    if t == "A":
        bio.box(ax, tuple(xy), 0.55, 0.32, "protein", radius=0.12, zorder=6)
    else:
        bio.box(ax, tuple(xy), 0.42, 0.42, "enzyme", radius=0.21, zorder=6)
bio.box(ax, (1.2, 0.5), 0.55, 0.32, "protein", radius=0.12)
bio.label(ax, (1.7, 0.5), "A: bivalent", size="tiny", ha="left")
bio.box(ax, (5.0, 0.5), 0.42, 0.42, "enzyme", radius=0.21)
bio.label(ax, (5.4, 0.5), "B: trivalent", size="tiny", ha="left")
ax.plot([8.2, 8.7], [0.5, 0.5], color=P.muted(), lw=1.0, ls=(0, (2, 1.5)))
bio.label(ax, (8.9, 0.5), "free site", size="tiny", ha="left")
bio.label(ax, (6.0, 9.9), "A tree in the sol (no loops)", size="small")

bio.panel(ax, "B", (13.6, 10.5))
pb = charts.axes_at(ax, (15.6, 1.8, 11.0, 7.6))
p = np.linspace(0, 0.7, 300)
pb.plot(p, 1 + 4 * p * p / (1 - 2 * p * p), color=quant.line_color("protein"), lw=2.2, label="<n_A> (exact)")


def mc(p, n=4000):
    tot = 0
    for _ in range(n):
        na, front = 1, [("A", 2)]
        while front and na < 5000:
            t, k = front.pop()
            for _ in range(k):
                if t == "A":
                    if rng.random() < p:
                        front.append(("B", 2))
                elif rng.random() < p:
                    na += 1
                    front.append(("A", 1))
        tot += na
    return tot / n


ps = [0.2, 0.35, 0.5, 0.6]
pb.plot(ps, [mc(x) for x in ps], "o", color=quant.line_color("protein"), ms=4.5, label="Monte Carlo")
pc = 1 / np.sqrt(2)
pb.axvline(pc, color=P.muted(), lw=0.8)
pb.text(pc + 0.01, 15, "gel point", fontsize=bio.core.FONT["tiny"], color=P.muted(), ha="left")
pb.set_xlim(0, 1)
pb.set_ylim(0, 30)
charts.style_axes(pb, "binding probability p = p′", "mean A molecules per tree")
pr = pb.twinx()
pp = np.linspace(0, 1, 300)
gel = []
for x in pp:
    fA = 0.0
    for _ in range(4000):
        fB = (1 - x + x * fA) ** 2
        fA = 1 - x + x * fB
    gel.append(1 - fA ** 2)
pr.plot(pp, gel, color=quant.line_color("mesoderm"), lw=2.2, label="gel fraction")
pr.set_ylim(0, 1.0)
charts.style_axes(pr, None, "gel fraction", box=True)
pr.spines["left"].set_visible(False)
h1, l1 = pb.get_legend_handles_labels()
h2, l2 = pr.get_legend_handles_labels()
leg = pb.legend(h1 + h2, l1 + l2, frameon=False, fontsize=bio.core.FONT["tiny"], loc="upper left")
for t in leg.get_texts():
    t.set_color(P.ink())
charts.title(pb, "Mean size diverges where the gel appears")
