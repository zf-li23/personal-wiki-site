"""Pre-steady-state burst in the hydrolysis of p-nitrophenyl acetate by chymotrypsin.

Mechanism: E + S <=> ES (k1, k-1), ES -> E-acyl + P1 (k2, p-nitrophenol released), E-acyl -> E + P2
(k3, acetate released). Acylation is fast and deacylation slow (k2 >> k3), so the first turnover
produces about one P1 per active site quickly, after which P1 appears at the steady-state rate
k_cat [E]0 with k_cat = k2 k3 / (k2 + k3). Illustrative rate constants; integrated with solve_ivp.
A: P1 against time for three enzyme concentrations, with the steady-state lines extrapolated to
t = 0. B: the burst amplitude (intercept) is proportional to [E]0, with slope close to 1, so it
titrates the active sites."""

import numpy as np
from scipy.integrate import solve_ivp
import wikibio as bio
from wikibio import charts

P = bio.P
k1, km1, k2, k3 = 1.0e3, 100.0, 0.1, 0.004  # mM^-1 s^-1, s^-1, s^-1, s^-1
S0 = 2.0  # mM, far above K_S = km1/k1 = 0.1 mM


def run(E0, t):
    def f(_, y):
        E, S, ES, EA, P1 = y
        v1 = k1 * E * S - km1 * ES
        v2 = k2 * ES
        v3 = k3 * EA
        return [-v1 + v3, -v1, v1 - v2, v2 - v3, v2]

    sol = solve_ivp(f, (t[0], t[-1]), [E0, S0, 0, 0, 0], t_eval=t, method="LSODA", rtol=1e-9, atol=1e-12)
    return sol.y[4]


fig, ax = bio.canvas(20.0, 8.2)
t = np.linspace(0, 200, 2000)
kcat = k2 * k3 / (k2 + k3)

bio.panel(ax, "A", (0.1, 8.1))
a = charts.axes_at(ax, (1.4, 1.0, 9.0, 6.2))
amps = []
E0s = np.array([0.005, 0.010, 0.020])  # mM
for E0, tok in zip(E0s, ("channel", "enzyme", "protein")):
    p1 = run(E0, t) * 1e3  # uM
    tail = t > 120
    slope, icpt = np.polyfit(t[tail], p1[tail], 1)
    amps.append(icpt)
    a.plot(t, p1, color=charts.line(tok), lw=2.0, label=f"[E]$_0$ = {E0 * 1e3:.0f} µM")
    a.plot([0, 200], [icpt, icpt + slope * 200], color=charts.line(tok), lw=0.9, ls="--")
    a.plot([0], [icpt], "o", ms=4, color=charts.line(tok))
a.text(95, 3, "dashed: steady state,\nslope $k_{\\mathrm{cat}}[\\mathrm{E}]_0$, extrapolated to $t = 0$",
       fontsize=bio.core.FONT["tiny"], color=P.ink())
a.set_xlim(0, 200)
a.set_ylim(0, None)
a.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(a, "$t$ / s", "p-nitrophenol / µM")
charts.title(a, "Fast acylation, slow deacylation")

bio.panel(ax, "B", (11.6, 8.1))
b = charts.axes_at(ax, (12.9, 1.0, 6.6, 6.2))
e = np.linspace(0, 25, 50)
b.plot(e, e, color=P.muted(), lw=0.9, ls=":", label="one P$_1$ per active site")
b.plot(E0s * 1e3, amps, "o", ms=6, mfc=P.fill("enzyme"), mec=charts.line("enzyme"), label="burst amplitude")
pred = (k2 * S0 / (S0 + km1 / k1)) / (k2 * S0 / (S0 + km1 / k1) + k3)
b.plot(e, pred**2 * e, color=charts.line("enzyme"), lw=1.4, label=f"theory, slope {pred**2:.2f}")
b.set_xlim(0, 25)
b.set_ylim(0, 25)
b.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(b, "[E]$_0$ / µM", "burst amplitude / µM")
charts.title(b, "Active-site titration")
