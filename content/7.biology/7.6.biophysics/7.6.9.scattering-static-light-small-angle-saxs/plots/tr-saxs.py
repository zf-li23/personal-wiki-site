# Time-resolved SAXS of RNA folding: fitting a multistage collapse (simulated data).
# After a stopped-flow jump of Mg2+ concentration at t = 0 (dead time about 1 ms), the radius of gyration of
# a ribozyme of about 200 nt is followed from Guinier fits of successive frames. The model, with
# illustrative parameters (not fitted to a published data set), has a fast nonspecific collapse and a slower
# search for the native tertiary structure:
#   Rg(t) = Rg_inf + A1 exp(-t / tau1) + A2 exp(-t / tau2),
#   Rg_inf = 42 A, A1 = 16 A, tau1 = 4 ms, A2 = 12 A, tau2 = 150 ms,
# observed at 45 times from 1 ms to 5 s (logarithmic spacing) with Gaussian errors of 0.6 A.
# A: data with least-squares fits of one and of two exponentials (scipy.optimize.curve_fit), against log t.
# B: normalized residuals; the single exponential leaves systematic deviations, the double one does not.
#    The Bayesian information criterion BIC = chi^2 + k ln n (k parameters, n points) is printed.
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(6)
t = np.logspace(-3, np.log10(5.0), 45)
true = (42.0, 16.0, 0.004, 12.0, 0.150)


def one(t, a, b, tau):
    return a + b * np.exp(-t / tau)


def two(t, a, b1, tau1, b2, tau2):
    return a + b1 * np.exp(-t / tau1) + b2 * np.exp(-t / tau2)


sig = 0.6
y = two(t, *true) + sig * rng.normal(size=t.size)
p1, _ = curve_fit(one, t, y, p0=(42, 25, 0.03))
p2, c2 = curve_fit(two, t, y, p0=(40, 15, 0.002, 10, 0.3))
r1 = (y - one(t, *p1)) / sig
r2 = (y - two(t, *p2)) / sig
n = t.size
bic1 = (r1**2).sum() + 3 * np.log(n)
bic2 = (r2**2).sum() + 5 * np.log(n)

fig, axs = plt.subplots(2, 1, figsize=(7.4, 5.6), sharex=True, gridspec_kw={"height_ratios": [2.2, 1.0]})
ax = axs[0]
ax.errorbar(t * 1e3, y, yerr=sig, fmt="o", ms=3, color=P.muted(), elinewidth=0.6, label="Rg from Guinier fits")
tt = np.logspace(-3, np.log10(5.0), 400)
ax.plot(tt * 1e3, one(tt, *p1), color=charts.line("negative"), lw=1.5,
        label=f"one exponential: τ = {p1[2] * 1e3:.0f} ms")
ax.plot(tt * 1e3, two(tt, *p2), color=charts.line("dna"), lw=1.8,
        label=f"two exponentials: τ₁ = {p2[2] * 1e3:.1f} ms, τ₂ = {p2[4] * 1e3:.0f} ms")
ax.axvspan(0.5, 1.0, color=P.light("neutral"), lw=0)
ax.text(0.72, 46, "dead\ntime", fontsize=7, color=P.muted(), ha="center")
ax.set_xscale("log")
ax.set_xlim(0.5, 6000)
ax.legend(fontsize=7.5, frameon=False, loc="upper right")
charts.style_axes(ax, None, "Rg / Å")
charts.title(ax, "A   Collapse of a ribozyme after adding Mg²⁺")
ax = axs[1]
ax.plot(t * 1e3, r1, "o-", ms=2.5, lw=0.8, color=charts.line("negative"), label=f"one exp.: BIC = {bic1:.0f}")
ax.plot(t * 1e3, r2, "o-", ms=2.5, lw=0.8, color=charts.line("dna"), label=f"two exp.: BIC = {bic2:.0f}")
ax.axhline(0, color=P.muted(), lw=0.6)
ax.set_ylim(-11, 11)
ax.legend(fontsize=7.5, frameon=False, loc="lower right", ncol=2)
charts.style_axes(ax, "time after mixing / ms", "residual / σ")
charts.title(ax, "B   Residuals")
fig.tight_layout()
