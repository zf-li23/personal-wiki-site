# Why the bicarbonate buffer of blood plasma works although pH 7.4 is 1.3 units above its pKa' = 6.1.
# A: buffer capacity beta = d[base]/dpH of a closed CO2/HCO3- system (total 25.2 mM) and of the open system,
# in which the lungs hold p(CO2) at 5.3 kPa ([CO2(d)] = 0.23 mM/kPa x p(CO2) = 1.2 mM) so that
# beta_open = 2.303 [HCO3-]. B: plasma pH after adding a strong acid (mM): closed system, open system at
# constant p(CO2), and open system with respiratory compensation: hyperventilation lowers p(CO2) by about
# 0.2 kPa per mM fall in [HCO3-] (Winter's relation, 1.5 mmHg per mM).
import numpy as np
import wikibio as bio
from wikibio import charts as C

pKa, s, pco2 = 6.1, 0.23, 5.3
co2 = s * pco2                     # mM
hco3 = co2 * 10 ** (7.4 - pKa)      # mM at pH 7.4
Ct = co2 + hco3
fig, ax = bio.canvas(19, 8.4)

a = C.axes_at(ax, (1.8, 1.5, 7.0, 6.2))
pH = np.linspace(5.0, 8.2, 400)
h = 10 ** (-pH)
Ka = 10 ** (-pKa)
beta_closed = 2.303 * Ct * Ka * h / (Ka + h) ** 2
beta_open = 2.303 * co2 * 10 ** (pH - pKa)
a.plot(pH, beta_closed, color=C.line("dna"), lw=2.0)
a.plot(pH, beta_open, color=C.line("negative"), lw=2.0)
a.axvline(7.4, color=bio.P.muted(), lw=0.8, ls=(0, (3, 3)))
a.axvline(pKa, color=bio.P.muted(), lw=0.8, ls=(0, (1, 2)))
F = bio.core.FONT["tiny"]
a.text(7.35, 75, "plasma\npH 7.4", fontsize=F, color=bio.P.muted(), va="top", ha="right")
a.text(6.15, 75, "pK$_a'$ = 6.1", fontsize=F, color=bio.P.muted(), va="top")
a.text(5.15, 20, "closed\n(constant total CO$_2$)", fontsize=F, color=C.line("dna"))
a.text(6.55, 48, "open\n(constant p$_{CO_2}$)", fontsize=F, color=C.line("negative"))
a.set_xlim(5.0, 8.2)
a.set_ylim(0, 80)
C.style_axes(a, "pH", r"buffer capacity $\beta$ / (mM per pH unit)")
bio.panel(ax, "A", (0.15, 8.1))

b = C.axes_at(ax, (11.3, 1.5, 7.2, 6.2))
acid = np.linspace(0, 20, 300)
pH_closed = pKa + np.log10((hco3 - acid) / (co2 + acid))
pH_open = pKa + np.log10((hco3 - acid) / co2)
pH_comp = pKa + np.log10((hco3 - acid) / (s * (pco2 - 0.2 * acid)))
b.plot(acid, pH_closed, color=C.line("dna"), lw=2.0)
b.plot(acid, pH_open, color=C.line("negative"), lw=2.0)
b.plot(acid, pH_comp, color=C.line("positive"), lw=2.0, ls=(0, (5, 3)))
b.axhspan(7.35, 7.45, color=bio.P.mix(bio.P.surface(), bio.P.muted(), 0.25), lw=0)
b.text(19.6, 7.47, "normal range", ha="right", fontsize=F, color=bio.P.muted())
b.text(12.5, 6.35, "closed", fontsize=F, color=C.line("dna"))
b.text(6.0, 7.06, "open, p$_{CO_2}$ = 5.3 kPa", fontsize=F, color=C.line("negative"))
b.text(3.0, 7.62, "open + respiratory compensation", fontsize=F, color=C.line("positive"))
b.set_xlim(0, 20)
b.set_ylim(5.8, 7.9)
C.style_axes(b, "strong acid added / mM", "pH")
bio.panel(ax, "B", (9.7, 8.1))
