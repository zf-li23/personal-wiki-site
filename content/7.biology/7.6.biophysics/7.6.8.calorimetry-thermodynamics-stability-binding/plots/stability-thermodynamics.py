"""Thermodynamic decomposition of protein stability (Formula 8.3.1, Example 8.3.1).

A: Delta H_U, T Delta S_U and Delta G_U against temperature for a protein with T_m = 60 C,
Delta H_m = 350 kJ/mol and Delta C_p = 6 kJ/(mol K): enthalpy and entropy are large and nearly
cancel; Delta H_U = 0 at T_H, Delta S_U = 0 at T_S (maximum stability), Delta G_U = 0 at T_m and T_c.
B: the same protein and a point mutant destabilized by Delta Delta G = 5 kJ/mol at all temperatures
(enthalpy lowered, entropy and Delta C_p unchanged); the shift of T_m is close to
Delta Delta G T_m / Delta H_m (Formula 8.3.2).
"""

import numpy as np
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
Tm, dHm, dCp = 333.15, 350.0, 6.0


def dH(T, Tm=Tm, dHm=dHm):
    return dHm + dCp * (T - Tm)


def dS(T, Tm=Tm, dHm=dHm):
    return dHm / Tm + dCp * np.log(T / Tm)


def dG(T, Tm=Tm, dHm=dHm):
    return dH(T, Tm, dHm) - T * dS(T, Tm, dHm)


T = np.linspace(200, 380, 800)
t = T - 273.15
TH = Tm - dHm / dCp
TS = Tm * np.exp(-dHm / (Tm * dCp))
Tc = brentq(dG, 180, TS)

fig, ax = bio.canvas(20.0, 8.2)
bio.panel(ax, "A", (0.1, 8.1))
pa = charts.axes_at(ax, (1.6, 1.3, 8.0, 5.8))
pa.plot(t, dH(T), color=charts.line("receptor"), lw=1.6, label=r"$\Delta_\mathrm{U}H$")
pa.plot(t, T * dS(T), color=charts.line("channel"), lw=1.6, label=r"$T\Delta_\mathrm{U}S$")
pa.plot(t, dG(T), color=P.ink(), lw=2.0, label=r"$\Delta_\mathrm{U}G$")
pa.axhline(0, color=P.muted(), lw=0.6)
for x, name, yoff in ((TH, "$T_H$", -60), (TS, "$T_S$", 75), (Tm, "$T_m$", 40), (Tc, "$T_c$", 40)):
    pa.axvline(x - 273.15, color=P.muted(), lw=0.6, ls=":")
    pa.text(x - 273.15 + 1.5, yoff, name, fontsize=FT["tiny"], color=P.ink())
pa.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
pa.set_xlim(t[0], t[-1])
pa.set_ylim(-450, 450)
charts.style_axes(pa, "t / °C", "kJ/mol")
charts.title(pa, "Enthalpy and entropy nearly cancel")

# B: point mutant
bio.panel(ax, "B", (10.4, 8.1))
pb = charts.axes_at(ax, (11.9, 1.3, 7.6, 5.8))
ddG = 5.0
# mutant: Delta H lowered by ddG at all temperatures, Delta S and Delta C_p unchanged
dGmut = lambda TT: dG(TT) - ddG
Tm2 = brentq(dGmut, 300, 400)
Tc2 = brentq(dGmut, 180, 290)
TT = np.linspace(230, 360, 500)
pb.plot(TT - 273.15, dG(TT), color=P.ink(), lw=1.8, label="wild type")
pb.plot(TT - 273.15, dGmut(TT), color=charts.line("negative"), lw=1.8, label=f"mutant (ΔΔG = {ddG:.0f} kJ/mol)")
pb.axhline(0, color=P.muted(), lw=0.6)
pb.plot([Tm - 273.15, Tm2 - 273.15], [0, 0], "o", ms=4, mfc=P.surface(), mec=P.ink())
pred = ddG * Tm / dHm
pb.annotate(f"ΔT$_m$ = {Tm2 - Tm:.1f} K\n(estimate ΔΔG·T$_m$/ΔH$_m$ = {-pred:.1f} K)", xy=(Tm2 - 273.15, 0),
            xytext=(-12, 7), fontsize=FT["tiny"], color=P.ink(), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.6))
pb.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
pb.set_xlim(-40, 85)
pb.set_ylim(-12, 34)
charts.style_axes(pb, "t / °C", r"$\Delta_\mathrm{U}G$ / (kJ/mol)")
charts.title(pb, "A small change in stability moves both T$_m$ and T$_c$")
