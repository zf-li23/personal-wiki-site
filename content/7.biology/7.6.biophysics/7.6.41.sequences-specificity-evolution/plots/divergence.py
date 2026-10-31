# Sequence divergence and the molecular clock. A: the fraction p of sites that differ between two
# sequences against the number of substitutions per site d that separate them, under the Jukes-Cantor
# model p = (3/4)(1 - exp(-4d/3)) (line), with sequences of 1000 sites simulated under the model
# (circles); the Jukes-Cantor distance d = -(3/4) ln(1 - 4p/3) recovers d (squares) until p approaches
# 3/4, where the estimate becomes noisy and finally undefined. B: dating an origin by root-to-tip
# regression, with simulated sequences: 60 sequences of 2500 sites sampled between 1983 and 1997, each
# separated from a common ancestor existing in 1930 by Poisson-distributed substitutions at
# 2.4e-3 per site per year plus a lineage-specific scatter, and one sequence sampled in 1959; the
# regression of distance on sampling year, extrapolated to zero distance, estimates the date of the
# ancestor (bootstrap 95 % interval shaded).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.0))
ax = axs[0]
d = np.linspace(0, 3, 300)
ax.plot(d, 0.75 * (1 - np.exp(-4 * d / 3)), color=charts.line("dna"), lw=2.0, label="Jukes–Cantor $p(d)$")
ax.plot(d, d, color=P.muted(), lw=0.8, ls=":", label="$p = d$ (no multiple hits)")
L = 1000
ds = np.linspace(0.05, 2.5, 16)
ps, dhat = [], []
for dd in ds:
    # number of substitutions per site Poisson(dd); each substitution picks one of the 3 other bases
    seqA = rng.integers(0, 4, L)
    seqB = seqA.copy()
    nsub = rng.poisson(dd, L)
    for i in np.where(nsub > 0)[0]:
        for _ in range(nsub[i]):
            seqB[i] = (seqB[i] + rng.integers(1, 4)) % 4
    p = np.mean(seqA != seqB)
    ps.append(p)
    dhat.append(-0.75 * np.log(1 - 4 * p / 3) if p < 0.75 else np.nan)
ax.plot(ds, ps, "o", ms=5, color=charts.line("dna"), label="simulated $p$")
ax.plot(ds, dhat, "s", ms=4.5, color=charts.line("negative"), mfc="none", label="Jukes–Cantor estimate of $d$")
ax.axhline(0.75, color=P.muted(), lw=0.6, ls="--")
ax.text(2.0, 0.78, "saturation 3/4", fontsize=7.5, color=P.ink())
ax.set_ylim(0, 2.8)
ax.legend(fontsize=7.5, frameon=False, loc="upper left")
charts.style_axes(ax, "true substitutions per site $d$", "observed difference / estimated $d$")
charts.title(ax, "A   Multiple hits hide divergence")

ax = axs[1]
L = 2500
rate = 2.4e-3
years = np.sort(rng.uniform(1983, 1997, 60))
t0 = 1930


def dist(y):
    lam = rate * (y - t0) * np.exp(rng.normal(0, 0.12, np.size(y)))
    return rng.poisson(lam * L) / L


dist_s = dist(years)
old = dist(np.array([1959.0]))
sl, ic = np.polyfit(years, dist_s, 1)
boots = []
for _ in range(400):
    i = rng.integers(0, years.size, years.size)
    s, c = np.polyfit(years[i], dist_s[i], 1)
    boots.append(-c / s)
lo, hi = np.percentile(boots, [2.5, 97.5])
yy = np.linspace(1915, 2000, 100)
ax.plot(years, dist_s, "o", ms=4, color=charts.line("virus"), label="sampled sequences (simulated)")
ax.plot([1959], old, "D", ms=7, color=charts.line("atp"), label="early sample, 1959")
ax.plot(yy, sl * yy + ic, color=P.ink(), lw=1.0, ls="--", label=f"regression: origin {-ic / sl:.0f}")
ax.axvspan(lo, hi, color=P.fill("highlight"), alpha=0.35, lw=0)
ax.axhline(0, color=P.muted(), lw=0.6)
ax.set_xlim(1915, 2000)
ax.legend(fontsize=7.5, frameon=False, loc="upper left")
charts.style_axes(ax, "year of sampling", "distance to ancestor (subst. per site)")
charts.title(ax, "B   Dating an origin with a molecular clock")
fig.tight_layout()
