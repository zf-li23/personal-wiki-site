"""Replicates against sequencing depth. Negative binomial counts with mean mu = f x depth and
dispersion phi = 0.05 (biological coefficient of variation about 22%); the log fold change of a
twofold changed gene is estimated from the group means, with variance about (1/mu + 1/(2 mu) + 2 phi)/n, and
tested at a two-sided level of 0.001 (lines: normal approximation; points: 4000 simulated
experiments each). A: a fixed budget of 120 million reads divided among 2n libraries, for a weakly
(f = 1e-6 of the reads) and a moderately expressed gene (f = 1e-5). B: power as a function of depth
per library for n = 3 and n = 6 replicates per group (f = 1e-6): depth stops helping once
1/mu is small against phi, replicates do not."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
phi, fc, level = 0.05, 2.0, 0.001
zc = stats.norm.isf(level / 2)
d = np.log(fc)


def power(mu, n):
    se = np.sqrt((1 / mu + 1 / (fc * mu) + 2 * phi) / n)
    return stats.norm.sf(zc - d / se) + stats.norm.cdf(-zc - d / se)


def simulate(mu, n, reps=4000):
    # NB with mean mu and variance mu + phi mu^2: gamma-Poisson mixture
    def draw(m):
        lam = rng.gamma(1 / phi, m * phi, size=(reps, n))
        return rng.poisson(lam)
    a, b = draw(mu), draw(mu * fc)
    ma, mb = a.mean(1) + 0.5 / n, b.mean(1) + 0.5 / n
    se = np.sqrt((1 / ma + phi) / n + (1 / mb + phi) / n)
    return np.mean(np.abs(np.log(mb / ma)) / se > zc)


fig, (a, b) = plt.subplots(1, 2, figsize=(9.6, 3.6))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.16, top=0.88, wspace=0.28)
budget = 120e6
ns = np.arange(2, 21)
for f, tok, lab in [(1e-6, "rna", "weak gene, f = 1e-6"), (1e-5, "dna", "moderate gene, f = 1e-5")]:
    mu = f * budget / (2 * ns)
    a.plot(ns, power(mu, ns), color=charts.line(tok), lw=1.6, label=lab)
    sel = ns[::3]
    a.plot(sel, [simulate(f * budget / (2 * k), k) for k in sel], "o", ms=4, color=charts.line(tok))
a.legend(frameon=False, fontsize=7.5, loc="lower right")
a.set_ylim(0, 1)
charts.style_axes(a, "replicates per group n (120 M reads in total)", "power")
charts.title(a, "A  Fixed budget")

depth = np.logspace(6, 8.5, 60)
for n, tok in [(3, "rna"), (6, "dna")]:
    mu = 1e-6 * depth
    b.plot(depth / 1e6, power(mu, n), color=charts.line(tok), lw=1.6, label=f"n = {n}")
    sel = depth[::12]
    b.plot(sel / 1e6, [simulate(1e-6 * x, n) for x in sel], "o", ms=4, color=charts.line(tok))
    b.axhline(power(np.inf, n), color=charts.line(tok), lw=0.8, ls=":")
b.set_xscale("log")
b.set_ylim(0, 1)
b.legend(frameon=False, fontsize=7.5, loc="upper left")
charts.style_axes(b, "reads per library (millions)", "power")
charts.title(b, "B  Depth saturates (dotted: infinite depth)")
