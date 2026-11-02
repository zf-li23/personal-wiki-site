"""The coherent type-1 feed-forward loop (C1-FFL) with logic input functions.

dY/dt = theta(Sx) - Y,  dZ/dt = G(theta(Sx), theta(Y > K)) - Z, with all production and removal
rates equal to 1 (time in units of the removal time 1/alpha) and K = 0.5 Y_st.
A: AND gate. Sx is switched on at t = 0 and off at t = 5. Z starts only when Y crosses K, after
T_ON = ln(1/(1 - K/Y_st)) = ln 2, but stops at once when Sx is removed. Simple regulation
(X -> Z only) is shown for comparison.
B: AND gate, pulses of Sx of duration D: the peak of Z. Pulses shorter than T_ON give no output.
C: OR gate, same steps: no delay at the ON step, a delay T_OFF = ln(Y_st/K) = ln 2 at the OFF step.
"""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
K = 0.5
dt = 1e-3


def run(t_on, t_off, gate, t_end):
    t = np.arange(0.0, t_end, dt)
    Y = np.zeros_like(t)
    Z = np.zeros_like(t)
    Zs = np.zeros_like(t)
    for i in range(1, len(t)):
        sx = 1.0 if t_on <= t[i - 1] < t_off else 0.0
        y = Y[i - 1]
        if gate == "AND":
            pz = sx * (y > K)
        else:
            pz = float(sx > 0 or y > K)
        Y[i] = y + dt * (sx - y)
        Z[i] = Z[i - 1] + dt * (pz - Z[i - 1])
        Zs[i] = Zs[i - 1] + dt * (sx - Zs[i - 1])
    return t, Y, Z, Zs


fig, axes = plt.subplots(1, 3, figsize=(11, 3.4))
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.17, top=0.86, wspace=0.32)
col_y, col_z, col_s = charts.line("protein"), charts.line("positive"), P.muted()

ax = axes[0]
t, Y, Z, Zs = run(0.0, 5.0, "AND", 9.0)
ax.axvspan(0, 5, ymax=1.08 / 1.5, color=P.muted(), alpha=0.15, lw=0)
ax.plot(t, Zs, color=col_s, lw=1.2, ls="--", label="Z, simple (= Y)")
ax.plot(t, Y, color=col_y, lw=1.4, label="Y")
ax.plot(t, Z, color=col_z, lw=1.8, label="Z, C1-FFL (AND)")
ax.axhline(K, color=P.muted(), lw=0.7, ls=":")
ax.text(8.9, K + 0.03, "K_YZ", fontsize=7, color=P.ink(), ha="right")
ax.annotate("", xy=(np.log(2), 0.08), xytext=(0, 0.08), arrowprops=dict(arrowstyle="<->", color=P.ink(), lw=0.8))
ax.text(np.log(2) / 2 + 0.15, 0.13, "T_ON", fontsize=7, color=P.ink(), ha="center")
ax.set_ylim(0, 1.5)
ax.set_xlim(-0.5, 9)
ax.legend(fontsize=7, frameon=False, loc="upper right", ncol=1)
charts.style_axes(ax, "time (1/alpha)", "level (units of steady state)")
charts.title(ax, "A  AND gate: delay at ON, none at OFF")

ax = axes[1]
Ds = np.linspace(0.05, 3.0, 60)
peak_ffl, peak_simple = [], []
for D in Ds:
    t, Y, Z, Zs = run(0.0, D, "AND", D + 3.0)
    peak_ffl.append(Z.max())
    peak_simple.append(Zs.max())
ax.plot(Ds, peak_simple, color=col_s, lw=1.2, ls="--", label="simple regulation")
ax.plot(Ds, peak_ffl, color=col_z, lw=1.8, label="C1-FFL (AND)")
ax.axvline(np.log(2), color=P.muted(), lw=0.7, ls=":")
ax.text(np.log(2) + 0.05, 0.85, "D = T_ON = ln 2", fontsize=7, color=P.ink())
ax.set_ylim(0, 1.0)
ax.legend(fontsize=7, frameon=False, loc="upper left", bbox_to_anchor=(0.25, 0.75))
charts.style_axes(ax, "pulse duration D (1/alpha)", "peak of Z")
charts.title(ax, "B  AND gate filters short pulses")

ax = axes[2]
t, Y, Z, Zs = run(0.0, 5.0, "OR", 9.0)
ax.axvspan(0, 5, ymax=1.08 / 1.5, color=P.muted(), alpha=0.15, lw=0)
ax.plot(t, Zs, color=col_s, lw=1.2, ls="--", label="Z, simple (= Y)")
ax.plot(t, Y, color=col_y, lw=1.4, label="Y")
ax.plot(t, Z, color=col_z, lw=1.8, label="Z, C1-FFL (OR)")
ax.axhline(K, color=P.muted(), lw=0.7, ls=":")
ax.annotate("", xy=(5 + np.log(2), 0.08), xytext=(5, 0.08), arrowprops=dict(arrowstyle="<->", color=P.ink(), lw=0.8))
ax.text(5 + np.log(2) / 2, 0.12, "T_OFF", fontsize=7, color=P.ink(), ha="center")
ax.set_ylim(0, 1.5)
ax.set_xlim(-0.5, 9)
ax.legend(fontsize=7, frameon=False, loc="upper right", ncol=1)
charts.style_axes(ax, "time (1/alpha)", "level (units of steady state)")
charts.title(ax, "C  OR gate: delay at OFF, none at ON")
