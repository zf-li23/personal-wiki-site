# FRAP and FLIP, simulated and fitted.
# A: FRAP of a uniform circular bleach spot of radius w in a membrane (2D diffusion). Soumpasis (1983): the
#    normalized recovery of the mobile pool is f(t) = exp(-2 tau_D / t) [I0(2 tau_D / t) + I1(2 tau_D / t)],
#    tau_D = w^2 / (4 D); the measured curve is F(t) = F0 + M (1 - F0) f(t) for prebleach intensity 1, with
#    mobile fraction M. Two simulated proteins (w = 1 um): D = 1 um^2/s, M = 0.9, and D = 0.1 um^2/s,
#    M = 0.6, with 2% noise; least-squares fits return D and M (printed in the legend).
# B: FLIP: a spot is bleached repeatedly (every 2 s, 90% loss per pulse). A two-compartment model: the
#    region connected to the spot exchanges with it at rate k = 0.2 s^-1 and loses fluorescence step by
#    step; a region not connected (k = 0) keeps its fluorescence. Only connected pools are depleted.
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.special import i0e, i1e

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
w = 1.0


def soumpasis(t, tau):
    x = 2 * tau / np.maximum(t, 1e-9)
    return i0e(x) + i1e(x)  # exp(-x) I0(x) + exp(-x) I1(x)


def model(t, D, M, F0):
    return F0 + M * (1 - F0) * soumpasis(t, w**2 / (4 * D))


fig, axs = plt.subplots(1, 2, figsize=(11.0, 3.9))
ax = axs[0]
t = np.linspace(0.05, 30, 300)
for D, M, tok in ((1.0, 0.9, "positive"), (0.1, 0.6, "negative")):
    F0 = 0.15
    data = model(t, D, M, F0) + rng.normal(0, 0.02, t.size)
    (Df, Mf, F0f), _ = curve_fit(model, t, data, p0=(0.5, 0.7, 0.1), bounds=([1e-3, 0, 0], [10, 1, 1]))
    ax.plot(np.r_[-3, -0.01, t], np.r_[1, 1, data], ".", ms=2.2, color=charts.line(tok), alpha=0.6)
    ax.plot(t, model(t, Df, Mf, F0f), color=charts.line(tok), lw=1.8,
            label=f"fit: D = {Df:.2f} µm²/s, M = {Mf:.2f}")
    ax.axhline(F0f + Mf * (1 - F0f), color=charts.line(tok), lw=0.6, ls=":")
ax.axvline(0, color=P.muted(), lw=0.7, ls=":")
ax.text(0.4, 1.06, "bleach", fontsize=7, color=P.muted())
ax.annotate("", xy=(27, 0.15), xytext=(27, 0.69), arrowprops=dict(arrowstyle="<->", color=P.muted(), lw=0.8))
ax.text(26.5, 0.42, "mobile", fontsize=7, color=P.muted(), ha="right")
ax.annotate("", xy=(27, 0.69), xytext=(27, 1.0), arrowprops=dict(arrowstyle="<->", color=P.muted(), lw=0.8))
ax.text(26.5, 0.84, "immobile", fontsize=7, color=P.muted(), ha="right")
ax.set_xlim(-3, 30)
ax.set_ylim(0, 1.12)
ax.legend(fontsize=7, frameon=False, loc="lower right", bbox_to_anchor=(0.88, 0.02))
charts.style_axes(ax, "t / s", "spot fluorescence (prebleach = 1)")
ax.set_title("A   FRAP: recovery rate gives D, plateau gives M", loc="left", fontsize=9, color=P.ink())

ax = axs[1]
dt, h = 0.02, 2.0
T = np.arange(0, 60, dt)
for k, txt, tok in ((0.2, "connected region", "positive"), (0.0, "unconnected region", "dna")):
    s, r, frac = 1.0, 1.0, 0.1  # spot and rest; spot holds 10% of the connected volume
    S, R = [], []
    for i, ti in enumerate(T):
        if i % int(h / dt) == 0:
            s *= 0.1
        flux = k * (r - s)
        s += dt * flux / frac * (1 - frac)
        r -= dt * flux
        S.append(s)
        R.append(r)
    ax.plot(T, R, color=charts.line(tok), lw=1.8, label=txt)
    if k > 0:
        ax.plot(T, S, color=charts.line(tok), lw=0.8, ls=":", label="bleached spot")
ax.set_xlim(0, 60)
ax.set_ylim(0, 1.08)
ax.legend(fontsize=7, frameon=False, loc="center right")
charts.style_axes(ax, "t / s (bleach pulse every 2 s)", "fluorescence (initial = 1)")
ax.set_title("B   FLIP: repeated bleaching drains connected pools", loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
