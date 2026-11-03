"""The infinite-sites plot (simulation of the infinite-sites theory). Five nodes on a tree evolving
under a strict clock have true ages 5, 10, 20, 40 and 80 Myr; the 20 Myr node carries a fossil
calibration, a uniform prior on (16, 26) Myr. Sequence data on n sites give, for each node, the
number of substitutions from the node to the present, Poisson with mean n r t (r = 10^-9 per site per
year); with vague priors the posterior of the distances r t_k is gamma, the posterior of the
calibrated age equals its prior, and every age follows as t_k = (r t_k) t_c / (r t_c) (Monte Carlo,
20 000 draws). A: width of the 95 % credible interval of each node age against its posterior mean, for
increasing n; with infinitely many sites the points fall on a line through the origin whose slope is
set by the calibration alone. B: the credible-interval width of the oldest node against n
approaches its infinite-data limit (dashed); beyond about 10^5 sites more sequence hardly helps."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(4)
T = np.array([5.0, 10.0, 20.0, 40.0, 80.0])
c = 2
r = 1e-3  # substitutions per site per Myr
draws = 20000


def posterior(n):
    x = rng.poisson(n * r * T)
    u = rng.gamma(x[None, :] + 1, 1 / n, size=(draws, len(T)))
    tc = rng.uniform(16, 26, draws)
    ages = u * (tc / u[:, c])[:, None]
    lo, hi = np.percentile(ages, [2.5, 97.5], axis=0)
    return ages.mean(0), hi - lo


fig, (a, b) = plt.subplots(1, 2, figsize=(10.0, 3.8))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.9, wspace=0.28)
toks = ["rna", "protein", "dna"]
for n, tok in zip([10 ** 4, 10 ** 5, 10 ** 7], toks):
    m, w = posterior(n)
    slope = (m @ w) / (m @ m)
    R2 = np.corrcoef(m, w)[0, 1] ** 2
    a.scatter(m, w, s=18, color=charts.line(tok), zorder=4,
              label=f"$n = 10^{{{int(np.log10(n))}}}$: $w = {slope:.3f}\\,t$, $R^2 = {R2:.3f}$")
    xx = np.linspace(0, 90, 10)
    a.plot(xx, slope * xx, color=charts.line(tok), lw=0.8)
a.set_xlim(0, 90)
a.set_ylim(0)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(a, "posterior mean age $t$ (Myr)", "95 % CI width $w$ (Myr)")
charts.title(a, "A  Infinite-sites plot")
ns = np.logspace(3, 7, 13)
wid = [posterior(int(n))[1][-1] for n in ns]
lim = T[-1] / T[c] * (np.percentile(rng.uniform(16, 26, 200000), 97.5) - np.percentile(rng.uniform(16, 26, 200000), 2.5))
b.semilogx(ns, wid, "o-", color=charts.line("dna"), lw=1.5, ms=3.5)
b.axhline(lim, color=P.muted(), lw=0.9, ls="--")
b.text(1.5e3, lim + 1.5, "infinite-data limit", fontsize=FT["tiny"], color=P.ink())
charts.style_axes(b, "number of sites $n$", "CI width of the 80 Myr node (Myr)")
charts.title(b, "B  Uncertainty that more data cannot remove")
