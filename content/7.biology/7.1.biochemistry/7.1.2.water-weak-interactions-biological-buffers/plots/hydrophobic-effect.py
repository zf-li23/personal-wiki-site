# Thermodynamics of the hydrophobic effect: transfer of benzene from liquid benzene into water, modelled with a
# constant heat capacity change dCp = +225 J/(mol K) and the convergence temperatures T_H = 295 K (dH = 0) and
# T_S = 386 K (dS = 0) observed for liquid hydrocarbons. dH(T) = dCp (T - T_H), dS(T) = dCp ln(T / T_S).
# Near room temperature the unfavourable dG comes almost entirely from -T dS (ordering of water);
# at high temperature it becomes enthalpic. dG(25 C) = +18 kJ/mol, close to the value from the solubility.
import numpy as np
import wikibio as bio
from wikibio import charts as C

dCp, TH, TS = 0.225, 295.0, 386.0  # kJ/(mol K), K, K
T = np.linspace(273.15, 393.15, 300)
dH = dCp * (T - TH)
TdS = T * dCp * np.log(T / TS)
dG = dH - TdS

fig, ax = bio.canvas(13, 8.4)
a = C.axes_at(ax, (1.9, 1.5, 10.4, 6.4))
t = T - 273.15
a.axhline(0, color=bio.P.muted(), lw=0.8)
a.plot(t, dG, color=C.line("negative"), lw=2.2)
a.plot(t, dH, color=C.line("dna"), lw=1.8)
a.plot(t, -TdS, color=C.line("lipid_tail"), lw=1.8, ls=(0, (5, 3)))
F = bio.core.FONT["small"]
a.text(102, dG[-60] + 1.2, r"$\Delta G$", color=C.line("negative"), fontsize=F)
a.text(100, dH[-75] + 1.2, r"$\Delta H$", color=C.line("dna"), fontsize=F)
a.text(100, -TdS[-75] + 1.4, r"$-T\Delta S$", color=C.line("lipid_tail"), fontsize=F)
a.axvline(25, color=bio.P.muted(), lw=0.7, ls=(0, (3, 3)))
a.text(26, 24.5, "25 °C", fontsize=bio.core.FONT["tiny"], color=bio.P.muted())
a.set_xlim(0, 120)
a.set_ylim(-12, 27)
C.style_axes(a, "temperature / °C", "transfer of benzene into water / kJ mol$^{-1}$")
