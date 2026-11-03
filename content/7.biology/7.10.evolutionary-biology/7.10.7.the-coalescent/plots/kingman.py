"""Kingman's coalescent. A: three independent genealogies of n = 20 gene copies (time in units of 2N_e
generations, present at the bottom), drawn on the same scale; tips are ordered so that branches do not cross.
B: histograms over 20 000 simulated genealogies of the time to the most recent common ancestor (TMRCA) and of
T2, the time during which the last two lineages persist; vertical lines: their expectations 2(1 - 1/n) = 1.9
and 1; dashed: the exponential density of T2."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT


def coalescent(n, rng):
    """Return (children, heights) of a Kingman tree; nodes 0..n-1 are tips."""
    active = list(range(n))
    heights = [0.0] * n
    children = [None] * n
    t = 0.0
    while len(active) > 1:
        k = len(active)
        t += rng.exponential(2 / (k * (k - 1)))
        i, j = rng.choice(k, 2, replace=False)
        a, b = active[i], active[j]
        children.append((a, b))
        heights.append(t)
        active = [x for idx, x in enumerate(active) if idx not in (i, j)] + [len(heights) - 1]
    return children, heights


def draw(ax, children, heights, x0, color, lw=1.0):
    pos = {}
    order = []

    def leaves(v):
        if children[v] is None:
            order.append(v)
            return
        for c in children[v]:
            leaves(c)
    root = len(heights) - 1
    leaves(root)
    for k, v in enumerate(order):
        pos[v] = x0 + k

    def place(v):
        if v in pos:
            return pos[v]
        a, b = children[v]
        pos[v] = (place(a) + place(b)) / 2
        return pos[v]
    place(root)
    for v, ch in enumerate(children):
        if ch is None:
            continue
        for c in ch:
            ax.plot([pos[c], pos[c]], [heights[c], heights[v]], color=color, lw=lw)
        ax.plot([pos[ch[0]], pos[ch[1]]], [heights[v], heights[v]], color=color, lw=lw)
    return heights[root]


fig, (a, b) = plt.subplots(1, 2, figsize=(11.0, 4.0), gridspec_kw={"width_ratios": [1.6, 1]})
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.14, top=0.9, wspace=0.22)
rng = np.random.default_rng(8)
for k, tok in enumerate(("dna", "enzyme", "rna")):
    ch, h = coalescent(20, rng)
    H = draw(a, ch, h, k * 23, charts.line(tok))
    a.text(k * 23 + 9.5, -0.18, f"TMRCA = {H:.2f}", ha="center", fontsize=FT["tiny"], color=P.ink())
a.set_xlim(-1, 3 * 23 - 2)
a.set_ylim(-0.3, None)
a.set_xticks([])
charts.style_axes(a, None, "time back (units of $2N_{\\mathrm{e}}$ generations)")
a.spines["bottom"].set_visible(False)
charts.title(a, "A  Three genealogies of $n = 20$")

n = 20
k = np.arange(2, n + 1)
Tk = rng.exponential(2 / (k * (k - 1)), size=(20000, n - 1))
tm = Tk.sum(1)
t2 = Tk[:, 0]
bins = np.linspace(0, 6, 61)
b.hist(t2, bins=bins, density=True, color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.4, alpha=0.8, label="$T_2$")
b.hist(tm, bins=bins, density=True, histtype="step", color=charts.line("rna"), lw=1.5, label="TMRCA")
x = np.linspace(0, 6, 200)
b.plot(x, np.exp(-x), color=P.ink(), lw=1, ls="--", label="$\\mathrm{e}^{-t}$")
b.axvline(1, color=charts.line("dna"), lw=0.9, ls=":")
b.axvline(2 * (1 - 1 / n), color=charts.line("rna"), lw=0.9, ls=":")
b.set_xlim(0, 6)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(b, "time (units of $2N_{\\mathrm{e}}$ generations)", "density")
charts.title(b, "B  TMRCA and the last two lineages")
