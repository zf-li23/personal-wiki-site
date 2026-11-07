# How far can a Na+-coupled transporter concentrate its substrate?
# At equilibrium of a cotransporter carrying n Na+ with one neutral glucose,
#   [G]i / [G]o = ([Na]o / [Na]i)^n * exp(-n F Vm / RT).
# Curves at 37 C with [Na]o / [Na]i = 145 / 12: n = 1 (SGLT2) and n = 2 (SGLT1), against membrane
# potential. At -60 mV with the round numbers of the text ([Na]o/[Na]i = 10, 60 mV per decade) the
# ratios are 100 and 10^4.
# Right axis: the Na+/Ca2+ exchanger (3 Na+ in, 1 Ca2+ out) sets the lowest cytosolic [Ca2+] it can
# reach, [Ca]i,eq = [Ca]o / (([Na]o/[Na]i)^3 exp(-F Vm / RT)), with [Ca]o = 1.2 mM. When the cytosolic
# [Ca2+] is above this value the exchanger extrudes Ca2+; below it (e.g. during the cardiac plateau at
# positive potentials) it runs in reverse.
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(24.0, 9.4)
F, R, T = 96485.0, 8.314, 310.15
f = F / (R * T)
V = np.linspace(-0.12, 0.04, 400)
r = 145 / 12

bio.panel(ax, "A", (0.2, 9.3))
pa = charts.axes_at(ax, (2.2, 1.5, 8.8, 6.7))
for n, tok, lab in ((1, "dna", "1 Na⁺ : 1 glucose (SGLT2)"), (2, "rna", "2 Na⁺ : 1 glucose (SGLT1)")):
    pa.semilogy(V * 1e3, r**n * np.exp(-n * f * V), color=charts.line(tok), lw=1.8, label=lab)
pa.axvline(-60, color=P.muted(), lw=0.7, ls="--")
pa.text(-58, 2, "−60 mV", fontsize=7.5, color=P.muted())
leg = pa.legend(loc="upper right", fontsize=7.5, frameon=False)
for txt in leg.get_texts():
    txt.set_color(P.ink())
pa.set_xlim(-120, 40)
pa.set_ylim(1, 1e7)
charts.style_axes(pa, "membrane potential Vm / mV", "maximal [glucose]ᵢ / [glucose]ₒ")
charts.title(pa, "Na⁺–glucose cotransport")

bio.panel(ax, "B", (12.6, 9.3))
pb = charts.axes_at(ax, (14.6, 1.5, 8.8, 6.7))
ca_eq = 1.2e-3 / (r**3 * np.exp(-f * V)) * 1e9  # nM
pb.semilogy(V * 1e3, ca_eq, color=charts.line("ca"), lw=1.8, label="[Ca²⁺]ᵢ at which NCX is at equilibrium")
pb.axhline(100, color=P.muted(), lw=0.8, ls="--")
pb.text(-118, 115, "resting cytosolic [Ca²⁺] ≈ 100 nM", fontsize=7.5, color=P.muted(), va="bottom")
pb.fill_between(V * 1e3, ca_eq, 1e5, color=P.mix(charts.line("positive"), P.surface(), 0.85), lw=0)
pb.fill_between(V * 1e3, 1, ca_eq, color=P.mix(charts.line("negative"), P.surface(), 0.85), lw=0)
pb.text(-110, 3000, "forward mode:\nCa²⁺ out, 3 Na⁺ in", fontsize=7.5, color=P.ink())
pb.text(0, 3, "reverse mode:\nCa²⁺ in", fontsize=7.5, color=P.ink())
pb.set_xlim(-120, 40)
pb.set_ylim(1, 1e5)
charts.style_axes(pb, "membrane potential Vm / mV", "cytosolic [Ca²⁺] / nM")
charts.title(pb, "Na⁺/Ca²⁺ exchanger (3 : 1)")
