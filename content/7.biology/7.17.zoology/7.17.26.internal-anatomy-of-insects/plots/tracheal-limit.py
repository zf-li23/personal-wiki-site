# How far can tracheae supply tissue by diffusion alone? A column of tissue of length L, supplied from one
# end by tracheae occupying a fraction phi of its cross-section, consumes O2 uniformly at rate M; steady
# diffusion through the gas-filled tracheae gives a drop dC = M L^2 / (2 phi D), so the longest column that
# can be kept above a minimum tissue partial pressure P_min is L_max = sqrt(2 phi D (P_O2 - P_min) / (M R T)).
# Parameters (schematic): D = 2e-5 m^2/s (O2 in air), phi = 0.1, P_min = 2 kPa, T = 298 K; M = 1.5 mol/(m^3 s)
# for active flight muscle and 0.015 for resting tissue. L_max grows with the square root of the
# atmospheric O2 level: from 21% today to about 30% (late Carboniferous-early Permian estimate, Berner's
# GEOCARBSULF model) it increases by about 20%.
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
D, phi, Pmin, R, T = 2e-5, 0.1, 2.0e3, 8.314, 298.0
fO2 = np.linspace(0.10, 0.35, 200)
PO2 = fO2 * 101.3e3
fig, ax = bio.canvas(20, 9.5)
pax = charts.axes_at(ax, (2.2, 1.6, 10.5, 7.4))
for M, tok, name in ((1.5, "negative", "flight muscle, M = 1.5"), (0.15, "enzyme", "M = 0.15"), (0.015, "channel", "resting, M = 0.015")):
    L = np.sqrt(2 * phi * D * (PO2 - Pmin) / (M * R * T)) * 1e3
    pax.plot(fO2 * 100, L, color=charts.line(tok), lw=1.6)
    pax.text(35.3, L[-1], name, fontsize=7, color=charts.line(tok), va="center")
pax.set_yscale("log")
for x, txt in ((21, "today"), (30, "c. 300 Ma")):
    pax.axvline(x, color=P.muted(), lw=0.9, ls=(0, (4, 3)))
    pax.text(x + 0.3, 0.9, txt, fontsize=7, color=P.muted())
pax.set_xlim(10, 35)
pax.set_ylim(0.8, 200)
charts.style_axes(pax, "Atmospheric O2 / %", "Maximum diffusion length L_max / mm")
r = np.sqrt((0.30 * 101.3e3 - Pmin) / (0.21 * 101.3e3 - Pmin))
bio.label(ax, (14.5, 3.0), "L_max(30%%) / L_max(21%%) = %.2f" % r, size="small", ha="left")
bio.label(ax, (14.5, 2.2), "M in mol O2 per m^3 tissue per s", size="tiny", ha="left", color=P.muted())
