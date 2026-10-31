"""Temperature gating of a two-state channel. A: open probability against temperature for a
heat-activated channel with half-activation at 42 C and gating enthalpy 420, 630 or 840 kJ/mol
(TRPV1-like), and for a cold-activated channel with dH = -420 kJ/mol and half-activation at 25 C
(TRPM8-like); dashed: a process with the temperature dependence of a typical enzyme (activation
energy 50 kJ/mol, Q10 about 1.9), normalised to 1 at 55 C. B: van 't Hoff plot of the equilibrium
constant K = p_o/(1 - p_o): straight lines of slope -dH/R. C: the temperature coefficient Q10 of
K at 37 C grows exponentially with the enthalpy of the transition."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
R = 8.314e-3  # kJ/(mol K)
T0 = 273.15


def po(T, dH, Th):
    return 1 / (1 + np.exp(dH / R * (1 / T - 1 / Th)))


fig, axs = plt.subplots(1, 3, figsize=(10.5, 3.3))
fig.subplots_adjust(wspace=0.42, left=0.07, right=0.98, bottom=0.17, top=0.88)
Tc = np.linspace(5, 55, 500)
T = Tc + T0
cases = ((420, 42, "negative"), (630, 42, "drug"), (840, 42, "blood"), (-420, 25, "na"))

ax = axs[0]
for dH, th, tok in cases:
    lab = rf"$\Delta H = {dH}$ kJ/mol" if dH > 0 else rf"cold: $\Delta H = {dH}$"
    ax.plot(Tc, po(T, dH, th + T0), color=charts.line(tok), lw=1.7, label=lab)
ea = 50.0
ax.plot(Tc, np.exp(-ea / R * (1 / T - 1 / (55 + T0))), color=P.muted(), lw=1.2, ls="--", label=r"enzyme rate, $E_\mathrm{a} = 50$")
ax.set_ylim(-0.02, 1.05)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"] - 0.6, labelcolor=P.ink(), loc="center left")
charts.style_axes(ax, r"temperature / $^\circ$C", r"$p_\mathrm{o}$")
charts.title(ax, "A  Thermal gating")

ax = axs[1]
for dH, th, tok in cases:
    lnK = dH / R * (1 / (th + T0) - 1 / T)
    m = np.abs(lnK) < 12
    ax.plot(1000 / T[m], lnK[m], color=charts.line(tok), lw=1.7)
ax.axhline(0, color=P.muted(), lw=0.5)
charts.style_axes(ax, r"$1000/T$ / K$^{-1}$", r"$\ln K$")
charts.title(ax, "B  van 't Hoff plot")

ax = axs[2]
dH = np.logspace(1, 2.95, 200)
Tm = 37 + T0
q10 = np.exp(dH / R * (1 / Tm - 1 / (Tm + 10)))
ax.plot(dH, q10, color=charts.line("blood"), lw=1.8)
for x, txt, at in ((50, "typical enzyme\n($Q_{10} \\approx 2$)", (12, 12)), (420, "TRPV1-like\n($Q_{10} > 100$)", (40, 2000))):
    y = np.exp(x / R * (1 / Tm - 1 / (Tm + 10)))
    ax.plot([x], [y], "o", color=charts.line("blood"), ms=4)
    ax.annotate(txt, (x, y), at, fontsize=bio.core.FONT["tiny"], color=P.ink(),
                arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.6))
ax.set_xscale("log")
ax.set_yscale("log")
charts.style_axes(ax, r"$|\Delta H|$ / (kJ mol$^{-1}$)", r"$Q_{10}$ of $K$ at 37 $^\circ$C")
charts.title(ax, "C  Steepness needs enthalpy")
