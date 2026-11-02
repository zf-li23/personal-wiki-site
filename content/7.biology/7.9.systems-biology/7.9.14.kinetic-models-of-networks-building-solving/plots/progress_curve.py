"""Identifiability of K_M and V_max from enzyme progress curves (simulation: K_M = 10, V_max = 1,
15 measurements of the product with Gaussian error of standard deviation 2 % of S0; the model is the
integrated Michaelis-Menten equation, Formula 14.6.2). Low design: S0 = 2 (0.2 K_M), times 2 to 60;
high design: S0 = 50 (5 K_M), times 6 to 90. A: data and fitted curves. B: profile likelihood of
K_M, 2[l_max - l_p(K_M)], with the 95 % threshold 3.84; the profile of the low design stays below the
threshold for all large K_M, so K_M has no upper confidence limit, while the high design gives a
closed interval. C: estimates from 300 parametric bootstrap data sets of each design (logarithmic
axes); for the low design they spread along the line V_max/K_M = constant, the only combination the
data determine."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import lambertw
from scipy.optimize import least_squares, minimize_scalar
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
KM, Vm = 10.0, 1.0


def product(t, km, vm, S0):
    return S0 - km * np.real(lambertw(S0 / km * np.exp((S0 - vm * t) / km)))


designs = [("low", 2.0, np.linspace(2, 60, 15), "highlight"), ("high", 50.0, np.linspace(6, 90, 15), "enzyme")]
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(11, 3.5))
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.17, top=0.86, wspace=0.36)
out = {}
for name, S0, t, tok in designs:
    sig = 0.02 * S0
    y = product(t, KM, Vm, S0) + rng.normal(0, sig, t.size)

    def res(th, y=y):
        return (product(t, np.exp(th[0]), np.exp(th[1]), S0) - y) / sig

    fit = least_squares(res, [np.log(5), np.log(0.5)], method="lm")
    chi2 = 2 * fit.cost
    grid = np.linspace(np.log(0.5), np.log(500), 200)
    prof = np.array([minimize_scalar(lambda lv: np.sum(res([g, lv]) ** 2), bounds=(-8, 8),
                                     method="bounded").fun for g in grid]) - chi2
    boot = []
    for _ in range(300):
        yb = product(t, *np.exp(fit.x), S0) + rng.normal(0, sig, t.size)
        boot.append(least_squares(lambda th: res(th, yb), fit.x, method="lm").x)
    boot = np.exp(np.array(boot))
    out[name] = dict(fit=np.exp(fit.x), chi2=chi2, grid=np.exp(grid), prof=prof, boot=boot)
    col = charts.line(tok)
    tt = np.linspace(0, t[-1], 200)
    ax1.plot(t, y / S0, "o", ms=3.5, color=col)
    ax1.plot(tt, product(tt, *np.exp(fit.x), S0) / S0, color=col, lw=1.5, label=f"S0 = {S0:g} ({name})")
    ax2.semilogx(np.exp(grid), prof, color=col, lw=1.8, label=f"S0 = {S0:g}")
    ax3.loglog(boot[:, 0], boot[:, 1], "o", ms=2.2, color=col, alpha=0.6, label=f"S0 = {S0:g}")
ax1.legend(fontsize=7, frameon=False, loc="lower right")
charts.style_axes(ax1, "t", "P / S0")
charts.title(ax1, "A  Progress curves")
ax2.axhline(3.84, color=P.muted(), ls="--", lw=1)
ax2.text(0.6, 4.4, "95 % threshold", fontsize=7, color=P.muted())
ax2.axvline(KM, color=P.ink(), ls=":", lw=0.8)
ax2.set_ylim(0, 20)
ax2.legend(fontsize=7, frameon=False, loc="upper right")
charts.style_axes(ax2, "K_M", "2 [l_max - l_p(K_M)]")
charts.title(ax2, "B  Profile likelihood of K_M")
km = np.logspace(-0.5, 3.5, 10)
ax3.loglog(km, 0.1 * km, color=P.muted(), ls="--", lw=1)
ax3.text(25, 20, "V/K = 0.1", fontsize=7, color=P.muted(), ha="right")
ax3.plot(KM, Vm, "*", color=P.ink(), ms=9)
ax3.set_xlim(1, 3e3)
ax3.set_ylim(0.1, 300)
ax3.legend(fontsize=7, frameon=False, loc="upper left")
charts.style_axes(ax3, "K_M estimate", "V_max estimate")
charts.title(ax3, "C  Parametric bootstrap")
