"""Why data-driven discovery needs a null model. A: the correlation coefficients between a random
phenotype and 20000 random, independent 'genes', each measured in n = 8 samples (histogram), with the
exact null density f(r) proportional to (1 - r^2)^((n-4)/2) (line); correlations beyond |r| = 0.8
(shaded) arise by chance alone. B: the largest |r| among p independent genes as a function of p, for
n = 8, 20 and 100 samples: simulation (points, mean of 200 repeats) and the exact expectation
computed from the null distribution (lines)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats, integrate
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
fig, (a, b) = plt.subplots(1, 2, figsize=(9.6, 3.6))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.16, top=0.9, wspace=0.28)


def null_cdf(r, n):
    # under independence, t = r sqrt(n-2)/sqrt(1-r^2) has a t distribution with n-2 df
    r = np.clip(r, -0.999999, 0.999999)
    return stats.t.cdf(r * np.sqrt(n - 2) / np.sqrt(1 - r ** 2), n - 2)


n, p = 8, 20000
y = rng.standard_normal(n)
X = rng.standard_normal((p, n))
yc = (y - y.mean()) / np.linalg.norm(y - y.mean())
Xc = X - X.mean(1, keepdims=True)
r = Xc @ yc / np.linalg.norm(Xc, axis=1)
a.hist(r, bins=60, range=(-1, 1), density=True, color=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.4)
g = np.linspace(-0.999, 0.999, 400)
dens = (1 - g ** 2) ** ((n - 4) / 2)
dens /= integrate.trapezoid(dens, g)
a.plot(g, dens, color=charts.line("dna"), lw=1.6)
a.axvspan(0.8, 1, color=P.fill("negative"), alpha=0.35, lw=0)
a.axvspan(-1, -0.8, color=P.fill("negative"), alpha=0.35, lw=0)
frac = np.mean(np.abs(r) > 0.8)
a.text(0.0, 0.93, f"|r| > 0.8: {int(np.sum(np.abs(r) > 0.8))} of {p} genes ({100 * frac:.1f}%)",
       transform=a.transAxes, fontsize=8, color=P.ink())
a.set_ylim(0, 1.15)
charts.style_axes(a, "correlation with phenotype, r", "density")
charts.title(a, "A  n = 8 samples, 20000 null genes")

ps = np.unique(np.logspace(0, 4.3, 14).astype(int))
for n, tok in [(8, "negative"), (20, "highlight"), (100, "dna")]:
    sims = []
    for q in ps:
        m = []
        for _ in range(200):
            # |r| under the null: draw t and transform, avoiding p x n matrices
            t = stats.t.rvs(n - 2, size=q, random_state=rng)
            m.append(np.max(np.abs(t / np.sqrt(n - 2 + t ** 2))))
        sims.append(np.mean(m))
    # exact E[max |r|] = integral of 1 - F_|r|(u)^p over (0, 1)
    u = np.linspace(0, 1, 4001)
    Fa = 2 * null_cdf(u, n) - 1
    qq = np.logspace(0, 4.3, 80)
    ex = [integrate.trapezoid(1 - Fa ** k, u) for k in qq]
    b.plot(qq, ex, color=charts.line(tok), lw=1.5, label=f"n = {n}")
    b.plot(ps, sims, "o", ms=3.5, color=charts.line(tok))
b.set_xscale("log")
b.set_ylim(0, 1.02)
b.legend(frameon=False, fontsize=8, loc="lower right")
charts.style_axes(b, "number of genes tested, p", "largest |r| expected by chance")
charts.title(b, "B  The best correlation among p null genes")
