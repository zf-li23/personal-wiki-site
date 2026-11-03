"""Brownian motion on a phylogeny. A: a trait evolving by Brownian motion (sigma^2 = 1 per unit time,
starting at 0) along a dated tree of eight species, drawn as a traitgram (trait value against time);
the paths of a lineage and its sister are identical up to their split and independent afterwards.
B: the phylogenetic covariance matrix C of the eight tips, C_ij = length of the path shared from the
root to the common ancestor of i and j (diagonal: root-to-tip length 1); under Brownian motion the tip
values are multivariate normal with covariance sigma^2 C. C: over 5000 simulations, the empirical
covariance of the tip values (dots) against the shared path length, with the prediction
Cov = sigma^2 x shared length (line)."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(12)
# tree: node -> (parent, time of node); tips at time 1
nodes = {"r": (None, 0.0), "a": ("r", 0.25), "b": ("r", 0.55), "c": ("a", 0.6), "d": ("a", 0.8),
         "e": ("b", 0.85)}
tips = {"1": "c", "2": "c", "3": "d", "4": "d", "5": "a", "6": "e", "7": "e", "8": "b"}


def path(tip):
    p, out = tips[tip], []
    while p is not None:
        out.append(p)
        p = nodes[p][0]
    return out


names = list(tips)
C = np.array([[max(nodes[x][1] for x in set(path(i)) & set(path(j))) if i != j else 1.0
               for j in names] for i in names])
fig = plt.figure(figsize=(10.0, 3.6))
a = fig.add_axes([0.06, 0.15, 0.36, 0.75])
b = fig.add_axes([0.48, 0.15, 0.22, 0.75])
c = fig.add_axes([0.78, 0.15, 0.2, 0.75])
dt = 0.005
val = {"r": 0.0}
order = ["r", "a", "b", "c", "d", "e"]

def bm_segment(x0, t0, t1):
    n = max(int(round((t1 - t0) / dt)), 1)
    steps = rng.normal(0, np.sqrt((t1 - t0) / n), n)
    return np.linspace(t0, t1, n + 1), x0 + np.concatenate([[0], np.cumsum(steps)])


segs = {}
for nd in order[1:]:
    pa, t1 = nodes[nd]
    ts, xs = bm_segment(val[pa], nodes[pa][1], t1)
    val[nd] = xs[-1]
    segs[nd] = (ts, xs)
for nd, (ts, xs) in segs.items():
    a.plot(ts, xs, color=P.muted(), lw=1.0)
for k, tip in enumerate(names):
    pa = tips[tip]
    ts, xs = bm_segment(val[pa], nodes[pa][1], 1.0)
    a.plot(ts, xs, color=charts.line("dna"), lw=1.0)
    a.text(1.01, xs[-1], tip, fontsize=FT["tiny"], color=P.ink(), va="center")
a.set_xlim(0, 1.06)
charts.style_axes(a, "time", "trait value")
charts.title(a, "A  Traitgram")
from matplotlib.patches import Rectangle
for i in range(8):
    for j in range(8):
        b.add_patch(Rectangle((j - 0.5, i - 0.5), 1, 1, facecolor=P.fill("dna"), alpha=0.08 + 0.8 * C[i, j], lw=0))
        b.text(j, i, f"{C[i, j]:.2f}".rstrip("0").rstrip("."), ha="center", va="center", fontsize=5.5,
               color=P.ink())
b.set_xlim(-0.5, 7.5)
b.set_ylim(7.5, -0.5)
b.set_aspect("equal")
b.set_xticks(range(8))
b.set_yticks(range(8))
b.set_xticklabels(names)
b.set_yticklabels(names)
charts.style_axes(b, box=True)
charts.title(b, "B  Covariance matrix $C$")
L = np.linalg.cholesky(C)
X = rng.normal(size=(5000, 8)) @ L.T
S = np.cov(X.T)
iu = np.triu_indices(8)
c.scatter(C[iu], S[iu], s=12, color=charts.line("dna"), zorder=4)
c.plot([0, 1], [0, 1], color=P.ink(), lw=1)
charts.style_axes(c, "shared path length", "empirical covariance")
charts.title(c, "C  Cov $= \\sigma^2 C_{ij}$")
