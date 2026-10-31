"""FRAP in one dimension, solved by a Fourier cosine series. A compartment of length 2L = 10 um
with reflecting ends is uniformly fluorescent (c0 = 1); at t = 0 the strip |x| < a = 1 um is
bleached. A: profiles c(x, t) for D = 5 um^2/s at t = 0, 0.02, 0.1, 0.5 and 2 s (series with
400 terms). B: fluorescence in the bleached strip relative to its prebleach value for D = 1, 5 and
25 um^2/s; it recovers to 1 - a/L = 0.8, not 1, because the bleached molecules stay in the
compartment, and the time axis scales as 1/D. C: synthetic data (D = 5 um^2/s, 3 % noise) fitted
with the series: the fit recovers D."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import wikibio as bio
from wikibio import charts

P = bio.P
L, a = 5.0, 1.0
n = np.arange(1, 401)


def profile(x, t, D):
    A = -2 / (n * np.pi) * np.sin(n * np.pi * a / L)
    return (1 - a / L) + (A[:, None] * np.cos(np.outer(n, x) * np.pi / L) * np.exp(-D * (n[:, None] * np.pi / L) ** 2 * t)).sum(0)


def recovery(t, D):
    """Fluorescence in |x| < a divided by its prebleach value 2a c0."""
    t = np.atleast_1d(t)
    term = (4 * L / (n * np.pi) ** 2 * np.sin(n * np.pi * a / L) ** 2)[:, None] * np.exp(-D * np.outer((n * np.pi / L) ** 2, t))
    return (2 * a * (1 - a / L) - term.sum(0)) / (2 * a)


fig, axs = plt.subplots(1, 3, figsize=(10.5, 3.3))
fig.subplots_adjust(wspace=0.38, left=0.06, right=0.98, bottom=0.17, top=0.88)

ax = axs[0]
x = np.linspace(-L, L, 600)
for t, tok in ((0.0, "neutral"), (0.02, "blood"), (0.1, "drug"), (0.5, "enzyme"), (2.0, "dna")):
    c = profile(x, t, 5.0) if t > 0 else np.where(np.abs(x) < a, 0.0, 1.0)
    ax.plot(x, c, color=charts.line(tok), lw=1.5, label=f"t = {t:g} s")
ax.axvspan(-a, a, color=P.mix(P.fill("highlight"), P.surface(), 0.7), lw=0, zorder=0)
ax.set_ylim(-0.03, 1.1)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, r"$x$ / $\mu$m", r"$c/c_0$")
charts.title(ax, r"A  Profiles, $D = 5\,\mu\mathrm{m^2\,s^{-1}}$")

ax = axs[1]
t = np.logspace(-3, 1.3, 300)
for D, tok in ((1.0, "protein"), (5.0, "enzyme"), (25.0, "dna")):
    ax.plot(t, recovery(t, D), color=charts.line(tok), lw=1.7, label=rf"$D = {D:g}\,\mu\mathrm{{m^2\,s^{{-1}}}}$")
ax.axhline(1 - a / L, color=P.muted(), lw=0.6, ls=":")
ax.text(1.2e-3, 0.83, r"plateau $1 - a/L$", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.set_xscale("log")
ax.set_ylim(0, 1)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="center left")
charts.style_axes(ax, "time after bleach / s", r"$F(t)/F_{\mathrm{pre}}$")
charts.title(ax, "B  Recovery scales with 1/D")

ax = axs[2]
rng = np.random.default_rng(4)
td = np.linspace(0.01, 3, 60)
yd = recovery(td, 5.0) + rng.normal(0, 0.03, td.size)
popt, pcov = curve_fit(lambda tt, D: recovery(tt, D), td, yd, p0=[1.0])
tt = np.linspace(0, 3, 300)
ax.plot(td, yd, "o", color=charts.line("neutral"), ms=3, label="data (noise 3 %)")
ax.plot(tt, recovery(tt, popt[0]), color=charts.line("enzyme"), lw=1.7,
        label=rf"fit: $D = {popt[0]:.2f} \pm {np.sqrt(pcov[0, 0]):.2f}\,\mu\mathrm{{m^2\,s^{{-1}}}}$")
ax.set_ylim(0, 1)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, "time after bleach / s", r"$F(t)/F_{\mathrm{pre}}$")
charts.title(ax, "C  Fitting the series")
