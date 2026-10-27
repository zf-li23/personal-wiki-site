"""Why cells need transport proteins.

A: permeability coefficients of a protein-free phospholipid bilayer (order-of-magnitude values in
cm/s, compiled from measurements on synthetic bilayers): small nonpolar and small uncharged polar
molecules cross readily, sugars slowly, ions about a billion times more slowly than water.
B: initial rate of uptake against external concentration: simple diffusion through the bilayer is
linear, J = P A c; transport by a carrier saturates, J = Jmax c / (K_t + c) (Michaelis-Menten form;
here K_t = 1.5 mM, the K_t of GLUT1 for glucose).
"""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(22.0, 8.0)

bio.panel(ax, "A", (0.1, 7.8))
pa = charts.axes_at(ax, (3.4, 1.3, 6.6, 5.8))
data = [("O₂, CO₂", 1e1, "positive"), ("H₂O", 3e-3, "channel"), ("ethanol", 1e-3, "channel"), ("urea", 4e-6, "channel"),
        ("glycerol", 5e-6, "channel"), ("tryptophan", 1e-7, "metabolite"), ("glucose", 4e-8, "metabolite"),
        ("Cl⁻", 1e-11, "cl"), ("K⁺", 5e-12, "k"), ("Na⁺", 1e-12, "na")]
y = np.arange(len(data))[::-1]
for yi, (name, p, tok) in zip(y, data):
    pa.barh(yi, np.log10(p) + 13, left=-13, height=0.62, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.8)
pa.set_yticks(y)
pa.set_yticklabels([d[0] for d in data])
pa.set_xlim(-13, 2)
pa.set_xticks([-12, -9, -6, -3, 0])
pa.set_xticklabels(["10⁻¹²", "10⁻⁹", "10⁻⁶", "10⁻³", "1"])
charts.style_axes(pa, "permeability coefficient / (cm s⁻¹)", None)
charts.title(pa, "A pure lipid bilayer")

bio.panel(ax, "B", (11.3, 7.8))
pb = charts.axes_at(ax, (12.9, 1.3, 7.6, 5.8))
c = np.linspace(0, 20, 300)
Kt, Jmax = 1.5, 1.0
pb.plot(c, Jmax * c / (Kt + c), color=charts.line("enzyme"), lw=2.0, label="carrier-mediated")
pb.plot(c, 0.045 * c, color=charts.line("neutral"), lw=2.0, ls=(0, (4, 2)), label="simple diffusion")
pb.axhline(Jmax, color=P.muted(), lw=0.6, ls=(0, (1, 2)))
pb.axvline(Kt, color=P.muted(), lw=0.6, ls=(0, (1, 2)))
pb.text(19.5, Jmax + 0.03, "J_max".replace("J_max", "Jmax"), fontsize=bio.core.FONT["tiny"], color=P.muted(), ha="right")
pb.text(Kt + 0.3, 0.05, "Kₜ", fontsize=bio.core.FONT["tiny"], color=P.muted(), ha="left")
pb.set_xlim(0, 20)
pb.set_ylim(0, 1.15)
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(pb, "external concentration / mM", "rate of uptake (relative)")
charts.title(pb, "Diffusion versus a carrier")
