"""Gradual and punctuated change on a phylogeny (Section 32.4.3). A, B: a character evolving on the same
tree either gradually, in proportion to time along every branch (phyletic gradualism), or only in
bursts at speciation events followed by stasis (punctuated equilibrium). C: a test with molecular or
morphological path lengths, the total change from the root to each living species. In 40 simulated
Yule trees of 30 species and equal depth, path length is unrelated to the number of nodes on the path
under gradualism (blue) and increases with it if change is concentrated at speciation (orange), the
pattern found by Pagel and colleagues in many phylogenies."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(6)


def yule(n, rng):
    """Yule tree grown to n tips; returns list of tips with (node count on path) and depth 1."""
    tips = [[0]]  # per tip: list of node times
    t = 0.0
    while len(tips) < n:
        t += rng.exponential(1 / len(tips))
        i = rng.integers(len(tips))
        new = tips[i] + [t]
        tips[i] = new
        tips.append(list(new))
    return t, [len(x) - 1 for x in tips]


fig, axes = plt.subplots(1, 3, figsize=(10.8, 3.4), gridspec_kw={"width_ratios": [1, 1, 1.25]})
fig.subplots_adjust(left=0.05, right=0.98, bottom=0.17, top=0.87, wspace=0.3)
# A, B: schematic trees in trait-time space
for ax, mode, title in ((axes[0], "g", "A  Phyletic gradualism"), (axes[1], "p", "B  Punctuated equilibrium")):
    # nodes: (time, trait)
    root = (0.0, 0.0)
    n1 = (0.35, 0.0)
    n2 = (0.65, 0.6)
    tips = {"a": (1.0, -0.9), "b": (1.0, 0.25), "c": (1.0, 1.1)}
    segs = [(root, n1), (n1, n2)]

    def draw(p, q, tok="dna"):
        if mode == "g":
            ax.plot([p[1], q[1]], [p[0], q[0]], color=charts.line(tok), lw=2)
        else:
            ax.plot([p[1], q[1]], [p[0], p[0] + 0.02], color=charts.line(tok), lw=2)
            ax.plot([q[1], q[1]], [p[0] + 0.02, q[0]], color=charts.line(tok), lw=2)
    tok = "dna" if mode == "g" else "rna"
    draw(root, n1, tok)
    draw(n1, tips["a"], tok)
    draw(n1, n2 if mode == "g" else (n2[0], n2[1]), tok)
    draw(n2, tips["b"], tok)
    draw(n2, tips["c"], tok)
    ax.set_xlim(-1.4, 1.5)
    ax.set_ylim(-0.05, 1.08)
    ax.set_xticks([])
    ax.set_yticks([])
    charts.style_axes(ax, "character value", "time" if ax is axes[0] else None)
    charts.title(ax, title)
c = axes[2]
for mode, tok, lab in (("g", "dna", "gradual"), ("p", "rna", "punctuated")):
    xs, ys = [], []
    for _ in range(40):
        depth, nodes = yule(30, rng)
        for k in nodes:
            if mode == "g":
                L = rng.poisson(40)  # substitutions in proportion to (equal) time
            else:
                L = rng.poisson(8 + 6 * k)
            xs.append(k + rng.uniform(-0.18, 0.18))
            ys.append(L)
    xs, ys = np.array(xs), np.array(ys)
    c.plot(xs, ys, "o", ms=2.2, alpha=0.35, color=charts.line(tok))
    kk = np.unique(np.round(xs))
    c.plot(kk, [ys[np.round(xs) == k].mean() for k in kk], "-", lw=2, color=charts.line(tok), label=lab)
charts.style_axes(c, "nodes between root and tip", "path length (changes)")
charts.title(c, "C  Path length and speciation")
c.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
