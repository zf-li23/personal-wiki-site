# Target-cell-limited model of HIV infection (standard teaching model, illustrative parameters).
#   dT/dt = lambda - d T - beta T V,   dI/dt = beta T V - delta I,   dV/dt = p I - c V
# T: uninfected CD4 T cells per microlitre, I: productively infected cells, V: free virions per microlitre.
# Basic reproduction number R0 = beta p T0 / (delta c), T0 = lambda / d; the infected steady state has T* = T0 / R0.
# Panel A: acute phase with R0 = 2.5 (viral peak, target-cell depletion, damped approach to a set point).
# Panel B: ten years, with R0 rising slowly (viral adaptation, loss of CTL control) as a phenomenological assumption:
#   R0(t) = 2.5 (1 + t / 3650 d), so that the quasi-steady CD4 count T*(t) = T0 / R0(t) falls from 400 to 200 per ul.
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts

P = bio.P
T0, D, DELTA, C, PROD = 1000.0, 0.01, 1.0, 23.0, 500.0
LAM = D * T0


def run(r0, tmax, n=3000):
    def f(t, y):
        T, I, V = y
        beta = r0(t) * DELTA * C / (PROD * T0)
        return [LAM - D * T - beta * T * V, beta * T * V - DELTA * I, PROD * I - C * V]

    ts = np.linspace(0, tmax, n)
    sol = solve_ivp(f, (0, tmax), [T0, 0.0, 1e-3], t_eval=ts, method="LSODA", rtol=1e-9, atol=1e-12)
    return ts, sol.y


fig, axs = plt.subplots(1, 2, figsize=(10, 3.6))
ta, ya = run(lambda t: 2.5, 200)
ax = axs[0]
ax.plot(ta, ya[2], color=charts.line("virus"), lw=1.6, label="free virus V")
ax.set_yscale("log")
ax.set_ylim(1e-3, 3e4)
charts.style_axes(ax, "time after infection / days", "virions per $\\mu$l (log scale)")
ax2 = ax.twinx()
ax2.plot(ta, ya[0], color=charts.line("protein"), lw=1.6, label="CD4$^+$ T cells T")
ax2.set_ylim(0, 1100)
charts.style_axes(ax2, None, "CD4$^+$ T cells per $\\mu$l")
ax2.spines["right"].set_visible(True)
h1, l1 = ax.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax.legend(h1 + h2, l1 + l2, frameon=False, fontsize=7, labelcolor=P.ink(), loc="lower right")
charts.title(ax, "A")

tb, yb = run(lambda t: 2.5 * (1 + t / 3650.0), 3650 * 1.15, 6000)
ax = axs[1]
yrs = tb / 365.0
ax.plot(yrs, yb[0], color=charts.line("protein"), lw=1.6, label="CD4$^+$ T cells (model)")
ax.axhline(200, color=P.edge("negative"), lw=0.9, ls="--")
ax.text(4.0, 212, "200 per $\\mu$l (AIDS threshold)", fontsize=7, color=P.edge("negative"))
ax.axhline(1000, color=P.muted(), lw=0.7, ls=":")
ax.text(11.4, 1010, "uninfected", fontsize=7, color=P.muted(), ha="right", va="bottom")
ax.set_ylim(0, 1150)
ax.set_xlim(0, 11.5)
charts.style_axes(ax, "time after infection / years", "CD4$^+$ T cells per $\\mu$l")
bx = ax.twinx()
bx.plot(yrs, yb[2] * 1e3, color=charts.line("virus"), lw=1.2, label="viral load (copies/ml)")
bx.set_yscale("log")
bx.set_ylim(1e3, 1e8)
charts.style_axes(bx, None, "virions per ml (log scale)")
bx.spines["right"].set_visible(True)
h1, l1 = ax.get_legend_handles_labels()
h2, l2 = bx.get_legend_handles_labels()
ax.legend(h1 + h2, l1 + l2, frameon=False, fontsize=7, labelcolor=P.ink(), loc="center right")
charts.title(ax, "B")
fig.tight_layout()
