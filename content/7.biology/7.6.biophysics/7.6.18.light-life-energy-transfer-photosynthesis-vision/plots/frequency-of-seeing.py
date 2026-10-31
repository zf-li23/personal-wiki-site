# The Hecht-Shlaer-Pirenne analysis of the absolute threshold of vision.
# A flash delivers a Poisson number of photons to the cornea with mean n; a fraction alpha is absorbed by
# rhodopsin, so the number absorbed is Poisson with mean alpha n. If a flash is seen when at least K photons
# are absorbed, P_see(n) = 1 - sum_{k<K} exp(-alpha n) (alpha n)^k / k!.
# A: frequency-of-seeing curves for K = 1..10 on a logarithmic intensity axis (alpha = 1): alpha only shifts
#    a curve sideways, while its steepness depends on K alone.
# B: a simulated observer (alpha = 0.06, K = 6; 7 intensities, 50 flashes each, seed 0) and the maximum-
#    likelihood fit of alpha for K = 2, 6 and 10; the log-likelihood picks K.
# C: dark noise. Thermal isomerizations in the summation pool of rods give a Poisson number of false events
#    with mean d = 0.6 per integration time (500 rods x 0.006 per s x 0.2 s). With a signal of 6 absorbed
#    photons on average, the hit rate P(N_dark + N_signal >= K) and the false-alarm rate P(N_dark >= K)
#    both fall as the criterion K rises: a criterion of 5-7 events keeps false alarms below 1 %.
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize_scalar
from scipy.stats import poisson

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
fig, axs = plt.subplots(1, 3, figsize=(13.4, 4.0))

ax = axs[0]
x = np.logspace(-1, 2, 400)
cmap = plt.get_cmap("viridis")
for K in range(1, 11):
    ax.plot(np.log10(x), poisson.sf(K - 1, x), color=cmap((K - 1) / 9), lw=1.4)
    if K in (1, 2, 3, 5, 10):
        xm = x[np.argmin(abs(poisson.sf(K - 1, x) - 0.5))]
        ax.text(np.log10(xm) - 0.04, 0.5, str(K), fontsize=7, ha="right", color=P.ink())
ax.text(-0.95, 0.92, "K = threshold\n(photons absorbed)", fontsize=7, color=P.ink())
charts.style_axes(ax, "log₁₀ mean number absorbed αn", "probability of seeing")
charts.title(ax, "A   Steepness reveals K")

ax = axs[1]
alpha_true, K_true = 0.06, 6
n = np.array([40, 60, 80, 100, 140, 200, 300])
trials = 50
seen = rng.binomial(trials, poisson.sf(K_true - 1, alpha_true * n))
ax.plot(np.log10(n), seen / trials, "o", ms=5, color=charts.line("rna"), label="simulated observer", zorder=5)
xx = np.logspace(1.3, 2.7, 300)
for K, tok in ((2, "dna"), (6, "enzyme"), (10, "protein")):
    nll = lambda la: -np.sum(seen * poisson.logsf(K - 1, np.exp(la) * n)
                             + (trials - seen) * poisson.logcdf(K - 1, np.exp(la) * n))
    res = minimize_scalar(nll, bounds=(np.log(1e-3), np.log(1.0)), method="bounded")
    a = np.exp(res.x)
    ax.plot(np.log10(xx), poisson.sf(K - 1, a * xx), color=charts.line(tok), lw=1.5,
            label=f"K = {K}: α = {a:.3f}, −log L = {res.fun:.1f}")
ax.legend(fontsize=6.8, frameon=False, loc="upper left")
ax.set_ylim(-0.03, 1.15)
charts.style_axes(ax, "log₁₀ mean photons at the cornea n", "fraction of flashes seen")
charts.title(ax, "B   Fitting a frequency-of-seeing curve")

ax = axs[2]
d, s = 0.6, 6.0
Ks = np.arange(1, 13)
hit = poisson.sf(Ks - 1, d + s)
fa = poisson.sf(Ks - 1, d)
ax.semilogy(Ks, hit, "o-", ms=4, color=charts.line("enzyme"), lw=1.5, label="hit (flash of 6 absorbed photons)")
ax.semilogy(Ks, fa, "s-", ms=4, color=charts.line("rna"), lw=1.5, label="false alarm (darkness)")
ax.axvspan(5, 7, color=P.fill("enzyme"), alpha=0.18, lw=0)
ax.set_ylim(1e-8, 2)
ax.legend(fontsize=7, frameon=False, loc="lower left")
charts.style_axes(ax, "criterion K (events in the pool)", "probability")
charts.title(ax, "C   Why the threshold is several photons")
fig.tight_layout()
