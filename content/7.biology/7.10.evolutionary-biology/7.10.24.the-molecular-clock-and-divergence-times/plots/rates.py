"""Relaxed clocks: rates drawn on a tree of 12 species (a pure-birth tree simulated with a fixed seed,
root age 100 Myr). Top row: autocorrelated rates (geometric Brownian motion, Eq. (24.4), with
nu = 0.006 per Myr and root rate 1, rate taken at the midpoint of each branch); bottom row: independent
log-normal rates (Eq. (24.5), sigma^2 = 0.3, mean 1). Left: the chronogram (branch lengths in time),
branches colored by rate. Right: the resulting phylogram (branch lengths = rate x time, the expected
numbers of substitutions), which is what sequences estimate. With autocorrelated rates, related
lineages share fast or slow rates and whole clades are stretched or compressed; with independent
rates, neighbouring branches vary independently."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import LogNorm
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(5)


def yule(n, root_age):
    # backward construction: random coalescence of n lineages with Yule-like times
    nodes = [dict(id=i, kids=[], age=0.0) for i in range(n)]
    active = list(range(n))
    ages = np.sort(rng.uniform(0, 1, n - 2))
    ages = np.concatenate([ages ** 1.6 * root_age * 0.95, [root_age]])
    for a in ages:
        i, j = rng.choice(len(active), 2, replace=False)
        new = dict(id=len(nodes), kids=[active[i], active[j]], age=a)
        nodes.append(new)
        active = [x for k, x in enumerate(active) if k not in (i, j)] + [new["id"]]
    return nodes


nodes = yule(12, 100.0)
root = len(nodes) - 1
parent = {}
for nd in nodes:
    for k in nd["kids"]:
        parent[k] = nd["id"]


def order(i):
    nd = nodes[i]
    return [i] if not nd["kids"] else order(nd["kids"][0]) + order(nd["kids"][1])


tips = order(root)
ypos = {t: k for k, t in enumerate(tips)}


def sety(i):
    nd = nodes[i]
    if nd["kids"]:
        for k in nd["kids"]:
            sety(k)
        ypos[i] = np.mean([ypos[k] for k in nd["kids"]])


sety(root)


def autocorrelated(nu):
    r = {root: 1.0}

    def go(i):
        for k in nodes[i]["kids"]:
            dt = nodes[i]["age"] - nodes[k]["age"]
            v = nu * dt
            r[k] = r[i] * np.exp(rng.normal(-v / 2, np.sqrt(v)))
            go(k)
    go(root)
    # midpoint rate approximated by geometric mean of the ends
    return {k: np.sqrt(r[k] * r[parent[k]]) for k in parent}


def independent(s2):
    return {k: np.exp(rng.normal(-s2 / 2, np.sqrt(s2))) for k in parent}


def draw(ax, rate, scaled):
    x = {}
    if scaled:
        def go(i, x0):
            x[i] = x0
            for k in nodes[i]["kids"]:
                go(k, x0 + rate[k] * (nodes[i]["age"] - nodes[k]["age"]))
        go(root, 0.0)
    else:
        for nd in nodes:
            x[nd["id"]] = 100.0 - nd["age"]
    segs, cols = [], []
    for k, pa in parent.items():
        segs.append([(x[pa], ypos[k]), (x[k], ypos[k])])
        cols.append(rate[k])
        ax.plot([x[pa], x[pa]], [ypos[k], ypos[pa]], color=P.muted(), lw=0.8)
    lc = LineCollection(segs, cmap="coolwarm", norm=LogNorm(0.3, 3.0), linewidths=2.6)
    lc.set_array(np.array(cols))
    ax.add_collection(lc)
    ax.set_xlim(-2, max(x.values()) * 1.05)
    ax.set_ylim(-0.8, len(tips) - 0.2)
    ax.set_yticks([])
    for sp in ("left", "top", "right"):
        ax.spines[sp].set_visible(False)
    return lc


fig, axs = plt.subplots(2, 2, figsize=(10.0, 6.4))
fig.subplots_adjust(left=0.04, right=0.88, bottom=0.09, top=0.94, wspace=0.12, hspace=0.42)
ra = autocorrelated(0.006)
ri = independent(0.3)
for row, (rate, name) in enumerate([(ra, "autocorrelated rates"), (ri, "independent rates")]):
    lc = draw(axs[row, 0], rate, False)
    charts.style_axes(axs[row, 0], "time from root (Myr)")
    charts.title(axs[row, 0], f"{'AC'[row]}  Chronogram, {name}")
    draw(axs[row, 1], rate, True)
    charts.style_axes(axs[row, 1], "substitutions (rate x time, relative units)")
    charts.title(axs[row, 1], f"{'BD'[row]}  Phylogram, {name}")
cax = fig.add_axes([0.91, 0.25, 0.015, 0.5])
cb = fig.colorbar(lc, cax=cax)
cb.set_ticks([0.3, 0.5, 1, 2, 3])
cb.set_ticklabels(["0.3", "0.5", "1", "2", "3"])
cb.minorticks_off()
cb.set_label("relative rate", fontsize=FT["small"], color=P.ink())
cb.ax.tick_params(labelsize=FT["tiny"], colors=P.muted(), labelcolor=P.ink())
cb.outline.set_edgecolor(P.muted())
