"""Population history and the genealogy. Coalescent with time-varying size N(t) (time back in units of
2N0 generations, N0 the present size), simulated by rescaling the waiting times of the standard coalescent:
with k lineages, the waiting time W ~ Exp(k(k - 1)/2) on the intensity scale is mapped to real time by
solving integral_t^(t + dt) N0 / N(s) ds = W. Histories: constant size; exponential growth, N(t) = N0 exp(-10 t)
backward (floored at 0.001 N0); bottleneck to 0.05 N0 between 0.2 and 0.25. Top: one genealogy of n = 20 for
each. Bottom: shape of the mean site frequency spectrum over 2000 samples with theta = 10 (infinite sites):
the proportion of segregating sites in each class divided by the neutral proportion (1/i) / a_n."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
n, theta = 20, 10.0
grid = np.linspace(0, 20, 200001)
dt = grid[1] - grid[0]


def make(rel):
    inten = np.concatenate([[0], np.cumsum(1 / rel(grid[:-1]) * dt)])
    return lambda w: np.interp(w, inten, grid)


hist = {
    "constant": lambda t: np.ones_like(t),
    "growth": lambda t: np.maximum(np.exp(-10 * t), 1e-3),
    "bottleneck": lambda t: np.where((t > 0.2) & (t < 0.25), 0.05, 1.0),
}
tmap = {k: make(f) for k, f in hist.items()}


def genealogy(name, rng):
    sizes, members = [1] * n, [[i] for i in range(n)]
    nodes = []            # (time, child_a_members, child_b_members)
    w = 0.0
    tprev = 0.0
    xi = np.zeros(n)
    starts = [0.0] * n
    ids = list(range(n))
    heights = {i: 0.0 for i in range(n)}
    children = {}
    nid = n
    while len(ids) > 1:
        k = len(ids)
        w += rng.exponential(2 / (k * (k - 1)))
        t = float(tmap[name](w))
        for s in sizes:
            xi[s] += rng.poisson(theta * (t - tprev) / 2)
        tprev = t
        i, j = sorted(rng.choice(k, 2, replace=False))
        children[nid] = (ids[i], ids[j])
        heights[nid] = t
        sizes[i] += sizes[j]
        sizes.pop(j)
        ids[i] = nid
        ids.pop(j)
        nid += 1
    return children, heights, nid - 1, xi[1:n]


def draw(ax, children, heights, root, color):
    pos, order = {}, []

    def leaves(v):
        if v not in children:
            order.append(v)
        else:
            for c in children[v]:
                leaves(c)
    leaves(root)
    for k, v in enumerate(order):
        pos[v] = k

    def place(v):
        if v not in pos:
            a, b = children[v]
            pos[v] = (place(a) + place(b)) / 2
        return pos[v]
    place(root)
    for v, (a, b) in children.items():
        for c in (a, b):
            ax.plot([pos[c], pos[c]], [heights[c], heights[v]], color=color, lw=1.0)
        ax.plot([pos[a], pos[b]], [heights[v], heights[v]], color=color, lw=1.0)


fig, axs = plt.subplots(2, 3, figsize=(11.5, 6.0), gridspec_kw={"height_ratios": [1.2, 1]})
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.09, top=0.93, wspace=0.25, hspace=0.42)
rng = np.random.default_rng(12)
titles = {"constant": "constant size", "growth": "exponential growth", "bottleneck": "bottleneck"}
for c, (name, tok) in enumerate((("constant", "dna"), ("growth", "rna"), ("bottleneck", "enzyme"))):
    ch, h, root, _ = genealogy(name, rng)
    ax = axs[0, c]
    draw(ax, ch, h, root, charts.line(tok))
    if name == "bottleneck":
        ax.axhspan(0.2, 0.25, color=P.mix(P.surface(), P.muted(), 0.25), lw=0)
    ax.set_ylim(0, 3.2)
    ax.set_xticks([])
    ax.spines["bottom"].set_visible(False)
    charts.style_axes(ax, None, "time back ($2N_0$ generations)" if c == 0 else None)
    charts.title(ax, f"{'ABC'[c]}  {titles[name]}")
    X = np.mean([genealogy(name, rng)[3] for _ in range(2000)], axis=0)
    b = axs[1, c]
    i = np.arange(1, n)
    an = np.sum(1 / i)
    b.bar(i, (X / X.sum()) / ((1 / i) / an), color=P.fill(tok), edgecolor=P.edge(tok), lw=0.5)
    b.axhline(1, color=P.ink(), lw=0.9, ls=":")
    b.set_xlim(0.3, n - 0.3)
    charts.style_axes(b, "derived allele count $i$", "shape relative to neutral" if c == 0 else None)
