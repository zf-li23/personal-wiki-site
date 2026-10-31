"""The membrane as a circuit and as a cable. A: steady passive spread of a voltage clamped at x = 0
along a long cable, V(x) = V0 exp(-x/lambda), for a mammalian dendrite (radius 1 um, R_m = 2 Ohm m2,
R_i = 1 Ohm m, lambda = 1 mm) and the squid giant axon (radius 250 um, R_m = 0.1 Ohm m2,
R_i = 0.3 Ohm m, lambda = 6.5 mm). B: spread of a brief, local charge injection in a passive cable,
V(x, t) = exp(-t/tau) exp(-x^2 tau/(4 lambda^2 t)) / sqrt(4 pi t/tau): the heat kernel multiplied by
membrane leakage, at t = 0.1, 0.5 and 2 tau. C: a patch with a constant K+ conductance and a
voltage-gated Na+ conductance g_Na(V) (two-state gating, effective charge 0.5/mV in units of 1/k_BT,
midpoint -50 mV) is bistable: dV/dt against V has stable fixed points near E_K and near E_Na (filled)
separated by an unstable threshold (open), the phase line of a switch."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.2))
fig.subplots_adjust(wspace=0.38, left=0.07, right=0.98, bottom=0.17, top=0.87)

ax = axs[0]
x = np.linspace(0, 15, 300)
for lam, tok, lab in [(1.0, "neuron", r"dendrite, $\lambda = 1$ mm"), (6.5, "blood", r"squid axon, $\lambda = 6.5$ mm")]:
    ax.plot(x, np.exp(-x / lam), color=charts.line(tok), lw=1.7, label=lab)
ax.axhline(np.exp(-1), color=P.muted(), lw=0.6, ls=":")
ax.text(12, np.exp(-1) + 0.03, "1/e", fontsize=FT["tiny"], color=P.ink())
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "distance $x$ / mm", r"$V(x)/V_0$")
charts.title(ax, "A  Steady electrotonic spread")

ax = axs[1]
X = np.linspace(-4, 4, 400)
for T, tok in [(0.1, "dna"), (0.5, "bacterium"), (2.0, "blood")]:
    v = np.exp(-T) * np.exp(-X ** 2 / (4 * T)) / np.sqrt(4 * np.pi * T)
    ax.plot(X, v, color=charts.line(tok), lw=1.6, label=rf"$t = {T:g}\,\tau$")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, r"$x/\lambda$", r"$V$ (per unit charge)")
charts.title(ax, "B  Transient spread")

ax = axs[2]
EK, ENa, gK = -90.0, 60.0, 5.0
V = np.linspace(-100, 70, 600)
gNa = 100 / (1 + np.exp(0.5 * (-50 - V))) + 0.2
dV = -(gK * (V - EK) + gNa * (V - ENa))
ax.plot(V, dV / 100, color=charts.line("na"), lw=1.7)
ax.axhline(0, color=P.muted(), lw=0.7)
s = np.sign(dV)
for i in np.where(np.diff(s) != 0)[0]:
    stable = dV[i] > 0 > dV[i + 1]
    ax.plot([V[i]], [0], "o", ms=6, mfc=charts.line("na") if stable else "none", mec=charts.line("na"), mew=1.3)
for xa, xb, yy in [(-75, -88, 0), (-45, -25, 0)]:
    ax.annotate("", (xb, yy + 0.4), (xa, yy + 0.4), arrowprops=dict(arrowstyle="->", color=P.ink(), lw=0.9))
ax.set_ylim(-20, 20)
charts.style_axes(ax, "V / mV", r"$C\,\mathrm{d}V/\mathrm{d}t$ (a.u.)")
charts.title(ax, "C  A bistable patch")
