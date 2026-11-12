# The quasi-steady test ("bumblebee paradox"). For each insect in hovering, the mean lift coefficient
# required to support the weight, from blade-element quasi-steady theory with a sinusoidal stroke:
# C_L = 4 m g / (rho S r2^2 R^2 pi^2 Phi^2 f^2), where S is the area of both wings, r2 = 0.55 the
# non-dimensional radius of the second moment of wing area, Phi the stroke amplitude and f the wingbeat
# frequency (same representative morphology as the scaling figure). Dashed lines: the maximum steady lift
# coefficient of insect wings at their Reynolds numbers (about 0.8-1.2 in wind tunnels) and the mean value
# measured on a dynamically scaled flapping wing with a leading-edge vortex (about 1.8, Dickinson et al.
# 1999 and later). Requirements above the steady value need unsteady mechanisms.
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
rho, g, r2 = 1.2, 9.81, 0.55
D = [("Drosophila", 1.0e-6, 2.5e-3, 0.30, 2.6, 220), ("Culex", 1.4e-6, 2.8e-3, 0.25, 0.68, 717),
     ("Apis", 1.0e-4, 9.5e-3, 0.28, 1.6, 230), ("Bombus", 1.75e-4, 13e-3, 0.30, 2.0, 155),
     ("Manduca", 1.6e-3, 48e-3, 0.39, 2.0, 25)]
fig, ax = bio.canvas(20, 9.5)
pax = charts.axes_at(ax, (2.0, 1.6, 11.0, 7.2))
names, CL, Re = [], [], []
for name, m, R, k, Phi, f in D:
    S = 2 * k * R * R
    c = 4 * m * g / (rho * S * r2 ** 2 * R ** 2 * np.pi ** 2 * Phi ** 2 * f ** 2)
    U = 2 * Phi * f * R * r2  # mean speed at r2
    chord = S / (2 * R)
    names.append(name); CL.append(c); Re.append(U * chord / 1.5e-5)
x = np.arange(len(names))
pax.bar(x, CL, color=P.fill("enzyme"), edgecolor=P.edge("enzyme"), width=0.62)
for xi, c, r in zip(x, CL, Re):
    pax.text(xi, c + 0.05, "%.2f\nRe %.0f" % (c, r), ha="center", fontsize=7, color=P.ink())
pax.axhspan(0.8, 1.2, color=P.fill("neutral"), alpha=0.5, lw=0)
pax.axhline(1.8, color=charts.line("negative"), ls=(0, (4, 3)), lw=1.2)
pax.text(-0.3, 1.86, "flapping wing with LEV", fontsize=7, ha="left", color=charts.line("negative"))
pax.text(4.45, 0.83, "steady wing, max", fontsize=7, ha="right", color=P.ink())
pax.set_xticks(x); pax.set_xticklabels(names, fontsize=8, style="italic")
pax.set_ylim(0, 2.6)
charts.style_axes(pax, None, "Required mean lift coefficient")
txt = ("C_L = 4mg / (rho S r2^2 R^2 pi^2 Phi^2 f^2)\n\n"
       "rho = 1.2 kg/m^3, r2 = 0.55\nS: area of both wings\nPhi: stroke amplitude (rad)\nf: wingbeat frequency")
bio.label(ax, (13.8, 8.0), txt, size="small", ha="left", va="top")
