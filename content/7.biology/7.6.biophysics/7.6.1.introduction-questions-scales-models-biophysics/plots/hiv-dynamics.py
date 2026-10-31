# Viral dynamics of HIV-1 under potent antiretroviral therapy (model in the spirit of Perelson et al. 1996, 1997).
# Before therapy the infection is at steady state with plasma virus V0 = 1e5 copies/mL. At t = 0 therapy blocks
# all new infections. Cells already infected but still in the eclipse phase (E, leaving at rate k = 1 per day)
# become productive; short-lived productive cells T1 die at delta1 = 0.5 per day and make 99 % of the virus,
# long-lived infected cells T2 die at delta2 = 0.04 per day and make 1 %; free virions are cleared at
# c = 3 per day (half-life 5.5 h):
#   dE/dt = -k E,  dT1/dt = k E - delta1 T1,  dT2/dt = -delta2 T2,  dV/dt = p1 T1 + p2 T2 - c V.
# A: log10 V(t): a shoulder of about a day, a first phase of slope -delta1/ln 10, a second phase of slope
#    -delta2/ln 10 (dotted guide lines), and, dashed, the decay at rate c that would follow if virion
#    production stopped at once.
# B: the expected number of new virions per day that carry one particular single, double or triple point
#    mutation, N mu^k with N = 1e10 virions per day and mu = 3e-5 per base per replication cycle; the dotted
#    line marks one per day.
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts

P = bio.P
V0, c, k, d1, d2 = 1e5, 3.0, 1.0, 0.5, 0.04
f1 = 0.99
# steady state before therapy (units: virus-equivalents per mL); choose p1 = p2 = 1 by scaling the cells
T1, T2 = f1 * c * V0, (1 - f1) * c * V0
E = d1 * T1 / k


def rhs(t, y):
    e, t1, t2, v = y
    return [-k * e, k * e - d1 * t1, -d2 * t2, t1 + t2 - c * v]


t = np.linspace(0, 60, 1201)
sol = solve_ivp(rhs, (0, 60), [E, T1, T2, V0], t_eval=t, rtol=1e-9, atol=1e-6)
V = sol.y[3]

fig, axs = plt.subplots(1, 2, figsize=(11.5, 3.9), gridspec_kw={"width_ratios": [1.5, 1.0]})
ax = axs[0]
ax.plot(t, np.log10(V), color=charts.line("virus"), lw=2.0, label="model")
tt = np.linspace(0, 3, 50)
ax.plot(tt, np.log10(V0 * np.exp(-c * tt)), color=charts.line("neutral"), lw=1.3, ls=(0, (4, 2.5)),
        label="production stopped at once")
# guide lines for the two phases
ta = np.linspace(1, 16, 20)
ax.plot(ta, np.log10(V[np.searchsorted(t, 4)]) - d1 * (ta - 4) / np.log(10) + 0.12, color=P.muted(), lw=0.9, ls=":")
tb = np.linspace(20, 60, 20)
ax.plot(tb, np.log10(V[np.searchsorted(t, 40)]) - d2 * (tb - 40) / np.log(10) + 0.12, color=P.muted(), lw=0.9, ls=":")
ax.text(10.5, 3.6, "first phase\nslope −δ₁/ln 10\n(t½ ≈ 1.4 d)", fontsize=7, color=P.ink())
ax.text(30, 3.05, "second phase\nslope −δ₂/ln 10 (t½ ≈ 17 d)", fontsize=7, color=P.ink())
ax.text(0.6, 5.08, "shoulder", fontsize=7, color=P.ink())
ax.set_xlim(0, 60)
ax.set_ylim(0, 5.4)
ax.set_yticks(range(0, 6))
ax.set_yticklabels(["1", "10", "10²", "10³", "10⁴", "10⁵"])
ax.legend(fontsize=7, frameon=False, loc="lower left")
charts.style_axes(ax, "days after the start of therapy", "plasma virus / (copies mL⁻¹)")
ax.set_title("A   Decay of plasma virus", loc="left", fontsize=9, color=P.ink())

ax = axs[1]
N, mu = 1e10, 3e-5
ks = np.array([1, 2, 3])
vals = N * mu ** ks
ax.bar(ks, np.log10(vals) + 5, bottom=-5, color=[P.fill("virus"), P.fill("highlight"), P.fill("positive")],
       edgecolor=[P.edge("virus"), P.edge("highlight"), P.edge("positive")], width=0.6)
for kk, v, lbl in zip(ks, vals, ("3 × 10⁵", "9", "2.7 × 10⁻⁴")):
    ax.text(kk, np.log10(v) + 0.25, lbl, ha="center", fontsize=7.5, color=P.ink())
ax.axhline(0, color=P.muted(), lw=0.8, ls=":")
ax.set_xticks(ks)
ax.set_xticklabels(["single", "double", "triple"])
ax.set_ylim(-5, 7)
ax.set_yticks([-4, -2, 0, 2, 4, 6])
ax.set_yticklabels(["10⁻⁴", "10⁻²", "1", "10²", "10⁴", "10⁶"])
charts.style_axes(ax, "specific point mutant", "new virions per day")
ax.set_title("B   Why monotherapy fails", loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
