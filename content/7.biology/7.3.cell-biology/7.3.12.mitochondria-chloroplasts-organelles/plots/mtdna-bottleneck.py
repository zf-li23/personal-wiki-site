"""Segregation of mtDNA heteroplasmy through the germline bottleneck (neutral sampling model).
In each maternal generation the mtDNA of the germline passes through N effective segregating units, sampled
binomially from the mother's heteroplasmy h, and is then amplified to the 10^5 copies of the oocyte without
further change of the mutant fraction.
(A) Heteroplasmy in ten maternal lineages over eight generations starting from h0 = 0.3, for N = 10 and N = 100.
(B) Distribution of heteroplasmy among the offspring of a mother with h0 = 0.3 (one sampling step) for
N = 10, 30 and 200; the dashed line marks a biochemical threshold of 0.7.
(C) Probability that a child exceeds the threshold, P(Bin(N, h0)/N >= 0.7), as a function of N for mothers with
h0 = 0.2, 0.3 and 0.5; the normalized variance of offspring heteroplasmy is V = Var/(h0(1 - h0)) = 1/N."""

import numpy as np
from scipy.stats import binom

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
theta = 0.7


def lineages(N, h0=0.3, gens=8, reps=10):
    h = np.full(reps, h0)
    out = [h.copy()]
    for _ in range(gens):
        h = rng.binomial(N, h) / N
        out.append(h.copy())
    return np.array(out)


fig, ax = bio.canvas(22.0, 7.6)
bio.panel(ax, "A", (0.1, 7.5))
a = charts.axes_at(ax, (1.7, 1.3, 5.4, 5.6))
g = np.arange(9)
for N, tok, ls in ((10, "negative", "-"), (100, "channel", "-")):
    tr = lineages(N)
    for k in range(tr.shape[1]):
        a.plot(g, tr[:, k], color=charts.line(tok), lw=1.0, alpha=0.85, label=f"N = {N}" if k == 0 else None)
a.axhline(theta, color=P.muted(), ls="--", lw=0.9)
a.text(8, theta + 0.02, "threshold", fontsize=FT["tiny"], color=P.muted(), ha="right", va="bottom")
a.set_xlim(0, 8)
a.set_ylim(-0.02, 1.02)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(a, "maternal generation", "heteroplasmy h")

bio.panel(ax, "B", (7.9, 7.5))
b = charts.axes_at(ax, (9.5, 1.3, 5.2, 5.6))
for N, tok in ((10, "negative"), (30, "positive"), (200, "channel")):
    k = np.arange(N + 1)
    pk = binom.pmf(k, N, 0.3)
    # plot as a density over h so that the three distributions are comparable
    b.plot(k / N, pk * N, color=charts.line(tok), lw=1.6, marker="o" if N <= 30 else None, ms=3, label=f"N = {N}")
b.axvline(theta, color=P.muted(), ls="--", lw=0.9)
b.axvline(0.3, color=P.muted(), ls=":", lw=0.9)
b.set_xlim(0, 1)
b.set_ylim(0, 13)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(b, "offspring heteroplasmy h", "probability density")

bio.panel(ax, "C", (15.3, 7.5))
c = charts.axes_at(ax, (16.9, 1.3, 4.8, 5.6))
Ns = np.unique(np.round(np.logspace(0, 3, 120)).astype(int))
for h0, tok in ((0.2, "channel"), (0.3, "positive"), (0.5, "negative")):
    pr = [1 - binom.cdf(np.ceil(theta * N - 1e-9) - 1, N, h0) for N in Ns]
    c.plot(Ns, pr, color=charts.line(tok), lw=1.7, label=f"h₀ = {h0}")
c.set_xscale("log")
c.set_yscale("log")
c.set_ylim(1e-6, 1)
c.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(c, "segregating units N", "P(child above threshold)")
