"""Birth-death trees and lineage-through-time plots (Section 31.5.1). A: one simulated clade with
speciation rate 0.5 and extinction rate 0.25 per lineage per Myr over 12 Myr; lineages that went
extinct are grey, and the reconstructed tree of the living species (what a molecular phylogeny can
show) is dark. B: mean log number of lineages in the reconstructed trees of 300 clades (conditioned on
survival to the present, starting from one lineage) for three models with the same net rate early on:
a pure-birth (Yule) process with rate 0.25; a birth-death process with rates 0.5 and 0.25, whose LTT
curve steepens toward the present (the pull of the present, because recently born lineages have not
yet had time to go extinct); and diversity-dependent speciation, rate 0.5 (1 - N/12) with extinction
0.05, whose LTT curve levels off."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
T = 12.0


def simulate(rng, lam_fn, mu, cap=4000):
    """Forward simulation. Nodes: [start, end, parent, children(list), extinct(bool)]."""
    nodes = [[0.0, None, -1, [], False]]
    active = [0]
    t = 0.0
    while active:
        n = len(active)
        lam = lam_fn(n)
        rate = n * (lam + mu)
        t += rng.exponential(1 / rate) if rate > 0 else np.inf
        if t >= T:
            break
        i = active.pop(rng.integers(n))
        if rng.random() < lam / (lam + mu):
            nodes[i][1] = t
            for _ in range(2):
                nodes.append([t, None, i, [], False])
                nodes[i][3].append(len(nodes) - 1)
                active.append(len(nodes) - 1)
        else:
            nodes[i][1] = t
            nodes[i][4] = True
        if len(nodes) > cap:
            return None
    for i in active:
        nodes[i][1] = T
    return nodes


def has_living(nodes, i, memo):
    if i in memo:
        return memo[i]
    nd = nodes[i]
    r = (not nd[4]) if not nd[3] else any(has_living(nodes, c, memo) for c in nd[3])
    memo[i] = r
    return r


def ltt(nodes, grid):
    memo = {}
    keep = [i for i in range(len(nodes)) if has_living(nodes, i, memo)]
    s = np.array([nodes[i][0] for i in keep])
    e = np.array([nodes[i][1] for i in keep])
    return np.array([np.sum((s <= g) & (e >= g)) for g in grid])


rng = np.random.default_rng(5)
fig, (a, b) = plt.subplots(1, 2, figsize=(10.4, 4.0), gridspec_kw={"width_ratios": [1.05, 1]})
fig.subplots_adjust(left=0.03, right=0.98, bottom=0.14, top=0.9, wspace=0.18)

# panel A: draw one tree with between 12 and 30 living tips
while True:
    nodes = simulate(rng, lambda n: 0.5, 0.25)
    if nodes is None:
        continue
    memo = {}
    tips = [i for i, nd in enumerate(nodes) if not nd[3]]
    living = sum(1 for i in tips if not nodes[i][4])
    if 12 <= living <= 30 and len(tips) < 70:
        break
ys = {}
counter = [0]


def place(i):
    nd = nodes[i]
    if not nd[3]:
        ys[i] = counter[0]
        counter[0] += 1
    else:
        for c in nd[3]:
            place(c)
        ys[i] = np.mean([ys[c] for c in nd[3]])


place(0)
memo = {}
for i, nd in enumerate(nodes):
    alive = has_living(nodes, i, memo)
    col = P.ink() if alive else P.mix(P.muted(), P.surface(), 0.35)
    lw = 1.5 if alive else 0.9
    a.plot([nd[0], nd[1]], [ys[i], ys[i]], color=col, lw=lw, solid_capstyle="butt")
    if nd[3]:
        a.plot([nd[1], nd[1]], [ys[nd[3][0]], ys[nd[3][1]]], color=col, lw=lw)
    elif nd[4]:
        a.plot([nd[1]], [ys[i]], "x", ms=3.5, color=col, mew=0.9)
a.plot([-0.4, 0], [ys[0], ys[0]], color=P.ink(), lw=1.5)
a.set_xlim(-0.6, T + 0.3)
a.set_yticks([])
a.set_xticks([0, 3, 6, 9, 12])
a.set_xticklabels(["12", "9", "6", "3", "0"])
charts.style_axes(a, "time (Myr ago)")
a.spines["left"].set_visible(False)
charts.title(a, "A  Complete and reconstructed tree")

grid = np.linspace(0.05, T, 120)
models = [("pure birth (Yule)", lambda n: 0.25, 0.0, "dna"),
          ("birth-death", lambda n: 0.5, 0.25, "rna"),
          ("diversity-dependent", lambda n: max(0.5 * (1 - n / 12), 0.0), 0.05, "plant")]
for lab, fn, mu, tok in models:
    curves = []
    while len(curves) < 300:
        nd = simulate(rng, fn, mu)
        if nd is None:
            continue
        L = ltt(nd, grid)
        if L[-1] >= 2:
            curves.append(np.log(np.maximum(L, 1)))
    b.plot(grid, np.mean(curves, axis=0), color=charts.line(tok), lw=2, label=lab)
b.set_xticks([0, 3, 6, 9, 12])
b.set_xticklabels(["12", "9", "6", "3", "0"])
charts.style_axes(b, "time (Myr ago)", "mean ln(lineages)")
charts.title(b, "B  Lineage-through-time plots")
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
