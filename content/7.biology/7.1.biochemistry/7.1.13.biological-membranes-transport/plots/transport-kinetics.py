"""Kinetics of passive transport by a carrier (GLUT1).

A: initial rate of uptake into erythrocytes, V0/Vmax = [S]out/(Kt + [S]out), for four hexoses with the
Kt values of GLUT1 (D-glucose 6 mM, D-mannose 20 mM, D-galactose 30 mM, L-glucose 3000 mM;
Lehninger 8e). The dashed line marks the blood glucose concentration (5 mM).
B: net flux of a symmetric carrier (binding at equilibrium on both sides, the same rate of
reorientation for the empty and the loaded carrier) at [S]out = 5 mM and Kt = 6 mM, against the
internal concentration: J = Jmax Kt([S]out - [S]in)/((Kt + [S]out)(Kt + [S]in)). Flux falls to zero
when the concentrations are equal and reverses beyond it; simple diffusion through the bilayer
(J proportional to [S]out - [S]in, drawn 1000-fold enlarged) is linear and far slower.
"""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(20.0, 7.6)

bio.panel(ax, "A", (0.1, 7.5))
pa = charts.axes_at(ax, (1.6, 1.4, 7.6, 5.4))
s = np.logspace(-1, 4.3, 400)
for name, kt, tok in (("D-glucose, Kt = 6 mM", 6, "carbohydrate"), ("D-mannose, 20 mM", 20, "enzyme"),
                      ("D-galactose, 30 mM", 30, "lipid_head"), ("L-glucose, 3000 mM", 3000, "negative")):
    pa.semilogx(s, s / (kt + s), color=charts.line(tok), lw=1.8, label=name)
pa.axvline(5, color=P.muted(), lw=0.8, ls=(0, (4, 3)))
pa.text(5.6, 0.03, "blood glucose 5 mM", fontsize=bio.core.FONT["tiny"], color=P.muted())
pa.set_xlim(0.1, 2e4)
pa.set_ylim(0, 1.05)
pa.legend(frameon=True, framealpha=1, facecolor=P.surface(), edgecolor="none", fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(pa, r"[S]$_\mathrm{out}$ / mM", r"$V_0 / V_{\max}$")
charts.title(pa, "Stereospecificity of GLUT1")

bio.panel(ax, "B", (10.3, 7.5))
pb = charts.axes_at(ax, (11.9, 1.4, 7.4, 5.4))
so, kt = 5.0, 6.0
si = np.linspace(0, 30, 300)
J = kt * (so - si) / ((kt + so) * (kt + si))
pb.plot(si, J, color=charts.line("carbohydrate"), lw=1.8, label="carrier (GLUT1)")
pb.plot(si, 1000 * 2e-5 * (so - si), color=charts.line("neutral"), lw=1.4, ls=(0, (4, 2.4)), label="bilayer diffusion (×1000)")
pb.axhline(0, color=P.muted(), lw=0.6)
pb.axvline(so, color=P.muted(), lw=0.8, ls=(0, (1, 2)))
pb.text(so + 0.4, 0.4, r"[S]$_\mathrm{in}$ = [S]$_\mathrm{out}$", fontsize=bio.core.FONT["tiny"], color=P.muted())
pb.text(10, 0.12, "J > 0: inward", fontsize=bio.core.FONT["tiny"], color=P.muted())
pb.text(10, -0.52, "J < 0: outward", fontsize=bio.core.FONT["tiny"], color=P.muted())
pb.set_xlim(0, 30)
pb.set_ylim(-0.6, 0.5)
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(pb, r"[S]$_\mathrm{in}$ / mM", r"net influx $J / J_{\max}$")
charts.title(pb, r"Equilibrating carrier, [S]$_\mathrm{out}$ = 5 mM")
