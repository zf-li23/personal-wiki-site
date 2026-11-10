# Serial killing by cytotoxic T lymphocytes as saturable enzyme-like kinetics (illustrative parameters).
# Each CTL spends t_kill = 20 min per target (conjugate formation, granule delivery, detachment) and finds a
# new target at rate k_c * T, with T the number of targets per unit volume (relative units).
# Per-CTL killing rate: v(T) = T / (T * t_kill + 1 / k_c) = V_max * T / (K + T),
#   V_max = 1 / t_kill = 3 targets per hour, K = 1 / (k_c * t_kill).
# A: killing rate per CTL versus target density: it saturates at V_max.
# B: fraction of targets remaining over time for different effector : target ratios (E:T), solving
#    dT/dt = - E * v(T) with T(0) = 1 (relative to the initial number of targets), k_c = 1 per hour per unit T.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
T_KILL = 1 / 3.0        # hours per kill
KC = 1.0                # search rate constant: finding a target takes 1 / (KC * T) hours
VMAX = 1 / T_KILL
K_HALF = 1 / (KC * T_KILL)


def v(T):
    return T / (T * T_KILL + 1 / KC)


fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.5))
Tg = np.logspace(-2, 1.3, 200)
axs[0].plot(Tg, v(Tg), color=charts.line("negative"), lw=1.6)
axs[0].axhline(VMAX, color=P.muted(), lw=0.8, ls="--")
axs[0].axvline(K_HALF, color=P.muted(), lw=0.8, ls=":")
axs[0].text(0.012, VMAX * 1.03, "V_max = 3 kills per hour", fontsize=7, color=P.muted(), va="bottom")
axs[0].text(K_HALF * 1.08, 0.2, "K = 3", fontsize=7, color=P.muted())
axs[0].set_xscale("log")
axs[0].set_ylim(0, 3.6)
charts.style_axes(axs[0], "target density T (relative units)", "kills per CTL per hour")
charts.title(axs[0], "A")

t = np.linspace(0, 12, 1201)
dt = t[1] - t[0]
for ratio, tok in ((0.03, "neutral"), (0.1, "enzyme"), (0.3, "protein"), (1.0, "negative")):
    T = np.empty_like(t)
    T[0] = 1.0
    for i in range(1, len(t)):
        T[i] = max(T[i - 1] - dt * ratio * v(T[i - 1]), 0.0)
    axs[1].plot(t, T, color=charts.line(tok), lw=1.5, label=f"E:T = {ratio:g}")
axs[1].set_yscale("log")
axs[1].set_ylim(1e-3, 1.2)
axs[1].legend(frameon=False, fontsize=7, labelcolor=P.ink(), loc="lower left")
charts.style_axes(axs[1], "time / h", "fraction of targets remaining")
charts.title(axs[1], "B")
fig.tight_layout()
