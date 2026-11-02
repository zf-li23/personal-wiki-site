"""When the Michaelis-Menten rate law replaces the mass-action scheme E + S <-> ES -> E + P
(k1 = 1, k-1 = 9, k2 = 1, so K_M = 10; S0 = 50; concentrations and time in model units).
A: low enzyme, E_T = 0.1 (E_T/(S0 + K_M) = 0.0017). The complex reaches its quasi-steady state within
about 0.1 time units (dashed, right axis: C/E_T), after which the product curve of the full model
(solid) and of the Michaelis-Menten equation (dots) coincide; the time axis is logarithmic.
B: high enzyme, E_T = 20 (ratio 0.33). The standard quasi-steady-state approximation (dotted) runs
ahead of the full model, because a third of the substrate is sequestered in the complex; the total
quasi-steady-state approximation (dashed), written for the total substrate S + C, follows it."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import wikibio as bio
from wikibio import charts

P = bio.P
k1, km1, k2 = 1.0, 9.0, 1.0
KM, S0 = (km1 + k2) / k1, 50.0


def full(t, z, ET):
    S, C = z
    E = ET - C
    return [-k1 * E * S + km1 * C, k1 * E * S - (km1 + k2) * C]


def sqssa(t, z, ET):
    return [-k2 * ET * z[0] / (KM + z[0])]


def tqssa(t, z, ET):
    St = z[0]
    s = ET + KM + St
    C = (s - np.sqrt(s * s - 4 * ET * St)) / 2
    return [-k2 * C]


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 3.5))
fig.subplots_adjust(left=0.08, right=0.92, bottom=0.17, top=0.86, wspace=0.45)

ET = 0.1
t = np.logspace(-3, np.log10(1500), 400)[:-1]
a = solve_ivp(full, (0, 1500), [S0, 0], args=(ET,), method="LSODA", rtol=1e-9, atol=1e-12, t_eval=t)
b = solve_ivp(sqssa, (0, 1500), [S0], args=(ET,), rtol=1e-9, atol=1e-12, t_eval=t)
Pfull = S0 - a.y[0] - a.y[1]
ax1.semilogx(t, Pfull / S0, color=charts.line("enzyme"), lw=1.8, label="full model: P/S0")
ax1.semilogx(t[::12], (S0 - b.y[0][::12]) / S0, "o", ms=3, color=P.ink(), label="Michaelis-Menten")
axr = ax1.twinx()
axr.semilogx(t, a.y[1] / ET, "--", color=charts.line("highlight"), lw=1.2)
axr.set_ylim(0, 1.05)
charts.style_axes(axr, None, "C / E_T (dashed)", box=True)
ax1.legend(fontsize=7, frameon=False, loc="center", bbox_to_anchor=(0.42, 0.35))
charts.style_axes(ax1, "t (log scale)", "P / S0")
charts.title(ax1, "A  E_T = 0.1: approximation valid")

ET = 20.0
t = np.linspace(0, 15, 300)
a = solve_ivp(full, (0, 15), [S0, 0], args=(ET,), method="LSODA", rtol=1e-9, atol=1e-12, t_eval=t)
b = solve_ivp(sqssa, (0, 15), [S0], args=(ET,), rtol=1e-9, atol=1e-12, t_eval=t)
c = solve_ivp(tqssa, (0, 15), [S0], args=(ET,), rtol=1e-9, atol=1e-12, t_eval=t)
ax2.plot(t, (S0 - a.y[0] - a.y[1]) / S0, color=charts.line("enzyme"), lw=1.8, label="full model")
ax2.plot(t, (S0 - b.y[0]) / S0, ":", color=charts.line("negative"), lw=1.8, label="standard QSSA")
ax2.plot(t, (S0 - c.y[0]) / S0, "--", color=P.ink(), lw=1.2, label="total QSSA")
ax2.legend(fontsize=7, frameon=False, loc="lower right")
charts.style_axes(ax2, "t", "P / S0")
charts.title(ax2, "B  E_T = 20: standard QSSA fails")
