"""Clonal evolution of a tumor: successive driver mutations and selective sweeps (simulation).

A tumor starts from one cell carrying a first driver mutation and grows logistically towards a carrying
capacity of 1e9 cells (growth rate 0.05 per generation, as if limited by space and blood supply). Each
generation the cells reproduce in proportion to their fitness (1 + s)^d, where d is the number of driver
mutations of the clone and s = 0.1, and each new cell acquires a further driver mutation with probability
u = 2e-9 (multinomial Wright-Fisher sampling with a growing population). Each new mutant founds a subclone
that inherits its parent's drivers.
(A) Muller plot: the fraction of the tumor occupied by each clone over time; every subclone is drawn inside
its parent, colored by its number of drivers (lighter to darker). New clones arise only when the population
is large, expand, and are overtaken by their own descendants; several subclones coexist at any time
(intratumor heterogeneity), and the lineage of the final dominant clone is a chain of sweeps.
(B) Tumor size (log scale) and the mean number of drivers per cell (dashed): growth stops at the carrying
capacity, but evolution continues; drivers arise once the population is large and sweep one after another,
each sweep taking about ln(N)/s, roughly 200 generations.
"""

import numpy as np
from matplotlib.patches import Rectangle

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(3)
K, r, s, u, G = 1e9, 0.05, 0.1, 2e-9, 1100

sizes = {0: 1}
drivers = {0: 1}
parent = {0: None}
hist = []
total = []
N = 1.0
nxt = 1
for g in range(G):
    N = N + r * N * (1 - N / K)
    ids = list(sizes)
    n = np.array([sizes[i] for i in ids], float)
    w = n * (1 + s) ** np.array([drivers[i] for i in ids])
    Nn = max(int(round(N)), 1)
    new = rng.multinomial(Nn, w / w.sum())
    sizes = {i: int(c) for i, c in zip(ids, new) if c > 0}
    for i in list(sizes):
        m = rng.binomial(sizes[i], u)
        for _ in range(min(m, 3)):
            sizes[i] -= 1
            sizes[nxt] = 1
            drivers[nxt] = drivers[i] + 1
            parent[nxt] = i
            nxt += 1
    hist.append(dict(sizes))
    total.append(sum(sizes.values()))
total = np.array(total, float)

# clones worth drawing: reach 1 % of the tumor at some time
peak = {}
for h, T in zip(hist, total):
    for i, c in h.items():
        peak[i] = max(peak.get(i, 0), c / T)
keep = {i for i, f in peak.items() if f >= 0.01}
keep.add(0)


def anc_kept(i):
    while i not in keep:
        i = parent[i]
    return i


children = {i: [] for i in keep}
for i in keep:
    if i != 0:
        children[anc_kept(parent[i])].append(i)
for v in children.values():
    v.sort()

tg = np.arange(G)
own = {i: np.zeros(G) for i in keep}
for k, (h, T) in enumerate(zip(hist, total)):
    for i, c in h.items():
        own[anc_kept(i)][k] += c / T


def subtotal(i):
    tot = own[i].copy()
    for c in children[i]:
        tot += subtotal(c)
    return tot


TOT = {i: subtotal(i) for i in keep}
lo = {i: np.zeros(G) for i in keep}
hi = {i: np.zeros(G) for i in keep}


def layout(i, a):
    lo[i] = a.copy()
    hi[i] = a + TOT[i]
    y = a + own[i] / 2
    for c in children[i]:
        layout(c, y)
        y = y + TOT[c]


layout(0, np.zeros(G))
TOK = ["neutral", "positive", "channel", "drug", "enzyme", "negative", "highlight", "dna"]

fig, ax = bio.canvas(27.0, 9.0)
bio.panel(ax, "A", (0.2, 8.8))
A = charts.axes_at(ax, (1.8, 1.5, 14.0, 6.6))


def draw(i):
    tok = TOK[(drivers[i] - 1) % len(TOK)]
    m = TOT[i] > 1e-4
    if m.any():
        A.fill_between(tg, lo[i], hi[i], where=m, color=P.fill(tok), ec=P.edge(tok), lw=0.5)
    for c in children[i]:
        draw(c)


draw(0)
A.set_xlim(0, G - 1)
A.set_ylim(0, 1)
charts.style_axes(A, "time / cell generations", "fraction of tumor cells")
for d_ in range(1, 7):
    tok = TOK[(d_ - 1) % len(TOK)]
    A.add_patch(Rectangle((20 + (d_ - 1) * 135, 1.03), 18, 0.04, color=P.fill(tok),
                                                           ec=P.edge(tok), lw=0.5, clip_on=False))
    A.text(43 + (d_ - 1) * 135, 1.05, f"{d_} driver{'s' if d_ > 1 else ''}", fontsize=FT["tiny"], color=P.ink(),
           va="center")

bio.panel(ax, "B", (17.4, 8.8))
B = charts.axes_at(ax, (19.2, 1.5, 6.0, 6.6))
B.semilogy(tg, total, color=charts.line("negative"), lw=1.8)
B.set_ylim(1, 3e9)
B.axhline(1e9, color=P.muted(), ls="--", lw=0.8)
B.text(10, 1.6e9, "about 1 cm³: clinically detectable", fontsize=FT["tiny"], color=P.muted())
charts.style_axes(B, "time / cell generations", "tumor cells")
B2 = B.twinx()
B2.set_facecolor("none")
md = [sum(drivers[i] * c for i, c in h.items()) / T for h, T in zip(hist, total)]
B2.plot(tg, md, color=charts.line("channel"), lw=1.5, ls="--")
B2.set_ylabel("mean drivers per cell (dashed)", fontsize=FT["small"], color=P.ink())
B2.tick_params(colors=P.muted(), labelcolor=P.ink(), labelsize=FT["tiny"])
for sp in B2.spines.values():
    sp.set_visible(False)
