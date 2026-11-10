# Interferon and CTL control of an acute viral infection (conceptual model, illustrative parameters).
#   dT/dt = -b T V / (1 + f F)                      target cells (T0 = 1e6), infection rate reduced by interferon F
#   dI/dt =  b T V / (1 + f F) - delta I - k E I    infected cells: lost by virus-induced death and by CTL killing
#   dV/dt =  p I - c V                              virus
#   dF/dt =  s I - a F                              type I interferon, made by infected cells (fast, no lag)
#   dE/dt =  rho E I / (I + h) - mu E               CTL: antigen-driven expansion from E0 = 1, hence a lag of days
# Four scenarios: no response, interferon only (k = 0), CTL only (f = 0), both.
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts

P = bio.P
T0, DELTA, C, PROD, R0 = 1e6, 0.5, 5.0, 40.0, 8.0
B0 = R0 * DELTA * C / (PROD * T0)
RHO, H, MU, S, A = 1.6, 1e3, 0.05, 1e-3, 1.5
FIFN, KCTL = 0.1, 2e-6


def run(f, k, tmax=30.0):
    def rhs(t, y):
        T, I, V, F, E = y
        b = B0 / (1 + f * F)
        return [-b * T * V, b * T * V - DELTA * I - k * E * I, PROD * I - C * V, S * I - A * F,
                RHO * E * I / (I + H) - MU * E]

    ts = np.linspace(0, tmax, 3000)
    e0 = 1.0 if k > 0 else 0.0
    sol = solve_ivp(rhs, (0, tmax), [T0, 0.0, 1e3, 0.0, e0], t_eval=ts, method="LSODA", rtol=1e-9, atol=1e-9)
    return ts, sol.y


fig, axs = plt.subplots(1, 2, figsize=(10, 3.6))
ax = axs[0]
cases = [("no response", 0.0, 0.0, "neutral"), ("interferon only", FIFN, 0.0, "enzyme"),
         ("CTL only", 0.0, KCTL, "receptor"), ("interferon + CTL", FIFN, KCTL, "protein")]
for name, f, k, tok in cases:
    t, y = run(f, k)
    lost = 1 - y[0][-1] / T0
    ax.plot(t, np.maximum(y[2], 1e-2), color=charts.line(tok), lw=1.6, label=f"{name} ({100 * lost:.0f}% of target cells lost)")
ax.set_yscale("log")
ax.set_ylim(1e-2, 2e7)
ax.legend(frameon=False, fontsize=7, labelcolor=P.ink(), loc="lower left")
charts.style_axes(ax, "time after infection / days", "free virus V (log scale)")
charts.title(ax, "A")

t, y = run(FIFN, KCTL)
ax = axs[1]
ax.plot(t, y[3] / y[3].max(), color=charts.line("enzyme"), lw=1.6, label="interferon F (relative to its peak)")
ax.set_ylim(0, 1.15)
charts.style_axes(ax, "time after infection / days", "interferon (relative)")
bx = ax.twinx()
bx.plot(t, np.maximum(y[4], 1.0), color=charts.line("protein"), lw=1.6, label="CTL E (log scale)")
bx.set_yscale("log")
bx.set_ylim(1, 1e8)
charts.style_axes(bx, None, "CTL (log scale)")
bx.spines["right"].set_visible(True)
h1, l1 = ax.get_legend_handles_labels()
h2, l2 = bx.get_legend_handles_labels()
ax.legend(h1 + h2, l1 + l2, frameon=False, fontsize=7, labelcolor=P.ink(), loc="upper right")
charts.title(ax, "B")
fig.tight_layout()
