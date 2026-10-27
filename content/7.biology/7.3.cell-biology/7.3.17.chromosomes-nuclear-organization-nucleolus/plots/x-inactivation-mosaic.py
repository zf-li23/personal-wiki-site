"""X-inactivation mosaics (simulation) and chance skewing (Proposition 17.1.1).
(A-C) An 8 x 8 sheet of founder cells, each inactivating the paternal or the maternal X with probability 1/2, grows
by four rounds of doubling in each dimension (each cell becomes a 2 x 2 block). After every round, a number of
random swaps between neighboring cells (0, 0.3 and 3 per cell) mimics cell mixing.
(D) Distribution of the fraction F of cells with an active maternal X in a tissue derived from n precursors,
nF ~ Bin(n, 1/2), for n = 8, 16, 64; shaded: the tails beyond 80:20."""

import numpy as np
from matplotlib.colors import ListedColormap
from scipy.stats import binom

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
founders = rng.integers(0, 2, (8, 8))


def grow(mix):
    g = founders.copy()
    for _ in range(4):
        g = np.kron(g, np.ones((2, 2), int))
        n = g.shape[0]
        swaps = int(mix * g.size)
        for _ in range(swaps):
            i, j = rng.integers(0, n, 2)
            if rng.random() < 0.5:
                i2, j2 = (i + 1) % n, j
            else:
                i2, j2 = i, (j + 1) % n
            g[i, j], g[i2, j2] = g[i2, j2], g[i, j]
    return g


cmap = ListedColormap([P.fill("lipid_head"), P.edge("neutral")])
fig, ax = bio.canvas(22.0, 7.6)
for k, (mix, title) in enumerate(((0, "coherent clonal growth"), (0.3, "moderate mixing"), (3, "extensive mixing"))):
    x0 = 0.4 + k * 4.75
    bio.panel(ax, "ABC"[k], (x0 - 0.3, 7.5))
    a = charts.axes_at(ax, (x0, 1.4, 4.3, 4.3 * 7.6 / 7.6 * 1.0))
    a.imshow(grow(mix), cmap=cmap, interpolation="nearest", vmin=0, vmax=1)
    a.set_axis_off()
    bio.label(ax, (x0 + 2.15, 6.15), title, size="small")
bio.box(ax, (1.0, 0.65), 0.35, 0.35, token="lipid_head")
bio.label(ax, (1.35, 0.65), "maternal X active", size="small", ha="left")
ax.add_patch(__import__("matplotlib.patches", fromlist=["Rectangle"]).Rectangle((4.45, 0.475), 0.35, 0.35, facecolor=P.edge("neutral"),
                                                                                  edgecolor=P.edge("neutral")))
bio.label(ax, (5.0, 0.65), "paternal X active", size="small", ha="left")

bio.panel(ax, "D", (14.9, 7.5))
d = charts.axes_at(ax, (16.4, 1.4, 5.2, 5.6))
for n, tok in ((8, "negative"), (16, "positive"), (64, "channel")):
    k = np.arange(n + 1)
    pk = binom.pmf(k, n, 0.5)
    f = k / n
    d.plot(f, pk * n, color=charts.line(tok), lw=1.6, marker="o", ms=3, label=f"n = {n}")
    tail = (f >= 0.8) | (f <= 0.2)
    d.vlines(f[tail], 0, pk[tail] * n, color=charts.line(tok), lw=4, alpha=0.5)
for xv in (0.2, 0.8):
    d.axvline(xv, color=P.muted(), ls=":", lw=0.9)
d.set_xlim(0, 1)
d.set_ylim(0, 7)
d.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(d, "fraction F of cells with maternal X active", "probability density")
