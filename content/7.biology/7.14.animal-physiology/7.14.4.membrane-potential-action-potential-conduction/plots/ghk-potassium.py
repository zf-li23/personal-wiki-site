# Resting potential of a mammalian skeletal muscle fibre against extracellular K+ (37 C).
# GHK voltage equation with Cl- ignored (P_Cl ~ 0) and alpha = P_Na / P_K:
#   Vm = 61.5 mV * log10( ([K]o + alpha [Na]o) / ([K]i + alpha [Na]i) ),
# [K]i = 155, [Na]i = 12 mM; [K]o is replaced by Na+ so that [K]o + [Na]o = 149.5 mM throughout.
# alpha = 0 gives the Nernst line for K+ (slope 61.5 mV per tenfold change); a small Na+ permeability
# bends the curve away from it at low [K]o, shifting Vm towards E_Na. Marker: the normal [K]o = 4.5 mM.
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(14.0, 9.4)
pa = charts.axes_at(ax, (2.3, 1.5, 11.0, 7.0))
Ko = np.logspace(0, np.log10(149.5), 300)
Nao = 149.5 - Ko
for a, tok in ((0.0, "positive"), (0.01, "dna"), (0.03, "protein"), (0.1, "rna")):
    V = 61.5 * np.log10((Ko + a * Nao) / (155 + a * 12))
    lab = "α = 0 (Nernst for K⁺)" if a == 0 else f"α = {a}"
    pa.semilogx(Ko, V, color=charts.line(tok), lw=1.8, label=lab)
pa.axvline(4.5, color=P.muted(), lw=0.7, ls="--")
pa.text(4.8, -128, "normal [K⁺]ₒ", fontsize=7.5, color=P.muted())
pa.axhline(0, color=P.muted(), lw=0.6)
leg = pa.legend(loc="upper left", fontsize=7.5, frameon=False)
for txt in leg.get_texts():
    txt.set_color(P.ink())
pa.set_xlim(1, 150)
pa.set_ylim(-135, 10)
charts.style_axes(pa, "[K⁺]ₒ / mM (log scale)", "resting potential Vm / mV")
charts.title(pa, "GHK equation, α = P_Na / P_K")
