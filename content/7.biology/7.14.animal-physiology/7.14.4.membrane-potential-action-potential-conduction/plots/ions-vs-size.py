# How large a fraction of a cell's ions does an electrical signal move?
# Sphere of radius r: charging the membrane (C_m = 1 uF/cm^2) to |V| = 70 mV moves Q = C_m 4 pi r^2 V,
# i.e. N = Q / e monovalent ions; the cell contains [K+]i (4/3) pi r^3 N_A potassium ions (140 mM).
# Fraction = 3 C_m V / (e N_A [K]i r).
# Cylinder (axon) of radius a: one action potential needs at least C_m * 2 pi a * 100 mV of Na+ entry per
# unit length, against pi a^2 [Na]i N_A sodium ions (12 mM) per unit length: fraction = 2 C_m dV / (e N_A [Na]i a).
# Real spikes move 1.3-4 times this minimum because Na+ and K+ currents overlap.
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(14.0, 9.4)
pa = charts.axes_at(ax, (2.3, 1.5, 11.0, 7.0))
Cm, e, NA = 1e-2, 1.602e-19, 6.022e23
dia = np.logspace(-1, 2, 200)  # diameter in um
r = dia / 2 * 1e-6
frac_rest = 3 * Cm * 0.070 / (e * NA * 140 * r)
frac_ap = 2 * Cm * 0.100 / (e * NA * 12 * r)
pa.loglog(dia, 100 * frac_rest, color=charts.line("k"), lw=1.8, label="K⁺ moved to set −70 mV (sphere)")
pa.loglog(dia, 100 * frac_ap, color=charts.line("na"), lw=1.8, label="Na⁺ entering per spike, minimum (axon)")
for x, lab in ((10, "10 µm cell"), (0.2, "thin axon"), (500, "")):
    if lab:
        pa.axvline(x, color=P.muted(), lw=0.6, ls=":")
        pa.text(x * 1.08, 3e-5, lab, fontsize=7, color=P.muted(), rotation=90, va="bottom")
pa.axhline(1, color=P.muted(), lw=0.6, ls=":")
pa.text(60, 1.15, "1 %", fontsize=7.5, color=P.muted())
leg = pa.legend(loc="upper right", fontsize=7.5, frameon=False)
for txt in leg.get_texts():
    txt.set_color(P.ink())
pa.set_xlim(0.1, 100)
pa.set_ylim(1e-5, 10)
charts.style_axes(pa, "cell or axon diameter / µm", "fraction of the cell's ions / %")
charts.title(pa, "Electrical signals move few ions — except in thin processes")
