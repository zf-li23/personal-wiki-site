"""A graph model of the mitochondrial network (after Sukhorukov and colleagues, 2012).
Mitochondria are edges of a graph whose nodes are free tips (degree 1), tip-to-tip fusion sites (degree 2) and
three-way junctions (degree 3). Tip-to-tip fusion X1 + X1 <-> X2 and tip-to-side fusion X1 + X2 <-> X3 are
balanced by fission; with the same fusion/fission ratio kappa for both reactions, mass action gives
x2 = kappa x1^2 and x3 = kappa^2 x1^3, where x_k is the number of nodes of degree k per edge end and
x1 + 2 x2 + 3 x3 = 1 (edge ends are conserved).
(A) The three node types and the two fusion-fission reactions.
(B) Fractions of edge ends at tips, degree-2 nodes and junctions as functions of kappa.
(C) Fraction of the mitochondrial mass in the largest connected cluster: random-graph theory for a graph with
this degree distribution (solid) and simulations of random networks with 4000 edge ends (dots). A giant
network appears at the Molloy-Reed threshold 3 x3 = x1, kappa = 2/sqrt(3) + 2/3 = 1.82 (dashed)."""

import numpy as np
from scipy.optimize import brentq

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT


def fractions(kappa):
    x1 = brentq(lambda x: x + 2 * kappa * x ** 2 + 3 * kappa ** 2 * x ** 3 - 1, 0, 1)
    return x1, kappa * x1 ** 2, kappa ** 2 * x1 ** 3


def giant(kappa):
    x1, x2, x3 = fractions(kappa)
    p = np.array([x1, x2, x3])
    p = p / p.sum()
    k = np.array([1, 2, 3])
    mean = (k * p).sum()

    def g1(u):
        return (p[0] + 2 * p[1] * u + 3 * p[2] * u ** 2) / mean

    if 3 * x3 <= x1:
        return 0.0
    u = brentq(lambda u: g1(u) - u, 0, 1 - 1e-12)
    return 1 - u ** 2


def simulate(kappa, ends=4000, rng=None):
    x1, x2, x3 = fractions(kappa)
    n = np.round(np.array([x1, x2, x3]) * ends).astype(int)
    deg = np.repeat([1, 2, 3], n)
    stubs = np.repeat(np.arange(len(deg)), deg)
    if len(stubs) % 2:
        stubs = stubs[:-1]
    rng.shuffle(stubs)
    parent = np.arange(len(deg))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    pairs = stubs.reshape(-1, 2)
    for a, b in pairs:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
    roots = np.array([find(a) for a, b in pairs])
    _, counts = np.unique(roots, return_counts=True)
    return counts.max() / len(pairs)


fig, ax = bio.canvas(22.0, 7.6)

# ---- A: schematic ------------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 7.5))


def tube(a, b, w=0.28):
    a, b = np.asarray(a, float), np.asarray(b, float)
    d = (b - a) / np.linalg.norm(b - a)
    n = np.array([-d[1], d[0]]) * w / 2
    bio.shape(ax, [a + n, b + n, b - n, a - n], "mitochondrion", lw=0.9, zorder=6)


def node(c, k):
    ax.add_patch(bio.core.Circle(c, 0.13, facecolor=P.fill("highlight") if k == 3 else P.fill("neutral"),
                                 edgecolor=P.ink(), lw=0.7, zorder=9))


y1 = 5.6
tube((0.6, y1), (1.6, y1))
node((1.6, y1), 1)
tube((2.1, y1), (3.1, y1))
node((2.1, y1), 1)
bio.label(ax, (3.6, y1), "⇌", size="title")
tube((4.0, y1), (5.0, y1))
tube((5.0, y1), (6.0, y1))
node((5.0, y1), 2)
bio.label(ax, (3.3, y1 + 0.75), "tip + tip ⇌ degree-2 node (fusion a₁, fission b₁)", size="tiny")
y2 = 2.9
tube((0.6, y2), (1.6, y2))
node((1.6, y2), 1)
tube((1.7, y2 - 0.6), (3.1, y2 - 0.6))
node((2.4, y2 - 0.6), 2)
bio.label(ax, (3.6, y2 - 0.3), "⇌", size="title")
tube((4.0, y2 - 0.6), (5.0, y2 - 0.6))
tube((5.0, y2 - 0.6), (6.0, y2 - 0.6))
tube((5.0, y2 - 0.6), (5.0, y2 + 0.4))
node((5.0, y2 - 0.6), 3)
bio.label(ax, (3.3, y2 + 1.0), "tip + side ⇌ three-way junction (a₂, b₂)", size="tiny")
bio.label(ax, (3.3, 0.9), "κ = a/b: fusion relative to fission", size="tiny", color=P.muted())

# ---- B: node fractions ---------------------------------------------------------------------------------------
bio.panel(ax, "B", (7.3, 7.5))
b = charts.axes_at(ax, (8.9, 1.3, 5.2, 5.6))
ks = np.logspace(-1.5, 2, 200)
fr = np.array([fractions(k) for k in ks])
for i, (name, tok) in enumerate((("tips (x₁)", "neutral"), ("degree 2 (2x₂)", "channel"), ("junctions (3x₃)", "highlight"))):
    b.plot(ks, fr[:, i] * (i + 1), color=charts.line(tok), lw=1.8, label=name)
kc = 2 / np.sqrt(3) + 2 / 3
b.axvline(kc, color=P.muted(), ls="--", lw=0.9)
b.set_xscale("log")
b.set_ylim(0, 1.02)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center left")
charts.style_axes(b, "fusion/fission ratio κ", "fraction of edge ends")

# ---- C: giant cluster ----------------------------------------------------------------------------------------
bio.panel(ax, "C", (14.8, 7.5))
c = charts.axes_at(ax, (16.4, 1.3, 5.3, 5.6))
c.plot(ks, [giant(k) for k in ks], color=charts.line("mitochondrion"), lw=1.9, label="random-graph theory")
rng = np.random.default_rng(0)
ksim = np.logspace(-1, 1.8, 16)
c.plot(ksim, [np.mean([simulate(k, rng=rng) for _ in range(3)]) for k in ksim], "o", color=charts.line("enzyme"),
       ms=4.5, label="simulation (4000 ends)")
c.axvline(kc, color=P.muted(), ls="--", lw=0.9)
c.text(kc * 1.15, 0.35, "threshold\n3x₃ = x₁", fontsize=FT["tiny"], color=P.ink(), va="top")
c.set_xscale("log")
c.set_ylim(0, 1.02)
c.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(c, "fusion/fission ratio κ", "mass in largest cluster")
