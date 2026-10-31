"""Robust perfect adaptation in the Barkai-Leibler model (Theorem 35.6.1). The receptor cluster is in
fast equilibrium (MWC activity of Fig. 35.4, N = 6, K_I = 18 uM, K_A = 3 mM, alpha = 1.7 kT); the
methylation level m changes slowly, dm/dt = V_R - V_B a/(a + K_B), with CheR saturated (V_R) and CheB
acting only on active receptors (V_B = 0.1 per second, K_B = 0.5). A: activity after steps of the
attractant from 0 to 0.1 mM, to 1 mM and back to 0.1 mM, for cells with half, normal, twice and
three times the normal CheR level (V_R = 0.02 per second at normal level): each response returns
exactly to its own prestimulus level. B: adaptation precision (activity 290 s after the step to 1 mM
divided by the prestimulus activity) against the CheR level, for the Barkai-Leibler model and for a
model in which CheR is not saturated (rate proportional to (M - m)/(K_R + M - m), M = 4, K_R = 0.5):
then the methylation rate depends on m itself and precision is lost. C: the adapted activity a* = K_B V_R/(V_B - V_R) (left axis) and the time to recover
half of the response to the step to 1 mM (right axis) both change with the CheR level, as measured by
Alon and colleagues (1999): precision is robust, the adapted level and the adaptation time are not."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
N, KI, KA, alpha, m0 = 6, 18e-3, 3.0, 1.7, 1.0
VB, KB, VR0 = 0.1, 0.5, 0.02
M, KR = 4.0, 0.5


def act(m, c):
    return 1 / (1 + np.exp(N * (alpha * (m0 - m) + np.log((1 + c / KI) / (1 + c / KA)))))


def conc(t):
    return np.where(t < 100, 0.0, np.where(t < 400, 0.1, np.where(t < 700, 1.0, 0.1)))


def rate(m, a, VR, sat):
    met = VR if sat else VR * (1 + KR / M) * (M - m) / (KR + M - m)
    return met - VB * a / (a + KB)


def run(folds, sat=True, dt=0.1, T=1000):
    t = np.arange(0, T, dt)
    VR = VR0 * np.asarray(folds, float)
    m = np.full(VR.size, 1.0)
    for _ in range(3000):        # equilibrate at c = 0
        a = act(m, 0.0)
        m += 1.0 * rate(m, a, VR, sat)
    out = np.empty((t.size, VR.size))
    for i, ti in enumerate(t):
        a = act(m, conc(ti))
        out[i] = a
        m += dt * rate(m, a, VR, sat)
    return t, out


fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.3))
fig.subplots_adjust(wspace=0.5, left=0.06, right=0.94, bottom=0.17, top=0.88)

folds = [0.5, 1.0, 2.0, 3.0]
t, A = run(folds)
ax = axs[0]
for j, (f, tok) in enumerate(zip(folds, ["neutral", "receptor", "enzyme", "positive"])):
    ax.plot(t, A[:, j], color=charts.line(tok), lw=1.2, label=f"CheR x{f:g}")
for x0 in (100, 400, 700):
    ax.axvline(x0, color=P.muted(), lw=0.5, ls=":")
for x0, lab in ((250, "0.1 mM"), (550, "1 mM"), (850, "0.1 mM")):
    ax.text(x0, 1.02, lab, fontsize=6.5, color=P.muted(), ha="center")
ax.set_ylim(0, 1.08)
ax.legend(frameon=False, fontsize=6.5, loc="center right")
charts.style_axes(ax, "time / s", "receptor activity a")
charts.title(ax, "A  step responses", loc="left")

fg = np.linspace(0.4, 3.1, 14)
ax = axs[1]
for sat, tok, lab in ((True, "receptor", "CheR saturated"), (False, "enzyme", "CheR not saturated")):
    t, A = run(fg, sat=sat)
    pre = A[np.searchsorted(t, 390)]
    post = A[np.searchsorted(t, 690)]
    ax.plot(fg, post / pre, "o-", color=charts.line(tok), ms=3, lw=1.0, label=lab)
ax.axhline(1, color=P.muted(), lw=0.6, ls="--")
ax.set_ylim(0, 1.6)
ax.legend(frameon=False, fontsize=7, loc="lower right")
charts.style_axes(ax, "CheR level (fold of normal)", "adaptation precision")
charts.title(ax, "B  precision")

ax = axs[2]
t, A = run(fg)
astar = KB * VR0 * fg / (VB - VR0 * fg)
ax.plot(fg, astar, color=charts.line("receptor"), lw=1.4)
ax.plot(fg, A[np.searchsorted(t, 390)], "o", color=charts.line("receptor"), ms=3)
charts.style_axes(ax, "CheR level (fold of normal)", r"adapted activity $a^*$")
ax2 = ax.twinx()
i0 = np.searchsorted(t, 400)
tau = []
for j in range(fg.size):
    seg = A[i0:np.searchsorted(t, 700), j]
    base = A[i0 - 5, j]
    half = base - 0.5 * (base - seg.min())
    k = np.argmin(seg) + np.argmax(seg[np.argmin(seg):] >= half)
    tau.append(t[i0 + k] - 400)
ax2.plot(fg, tau, "s--", color=charts.line("enzyme"), ms=3, lw=1.0)
charts.style_axes(ax2, None, "half-recovery time / s", box=True)
ax2.spines["top"].set_visible(False)
charts.title(ax, "C  what is not robust")
