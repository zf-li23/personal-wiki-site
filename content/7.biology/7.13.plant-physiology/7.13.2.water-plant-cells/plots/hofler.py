# Hofler diagram of a vacuolated plant cell, from a two-parameter model.
# Relative volume v = V / V_ip, where V_ip is the protoplast volume at incipient plasmolysis.
# Solute potential follows Boyle-van 't Hoff (solutes conserved): Psi_s = Psi_s0 / v.
# Pressure potential with a constant volumetric elastic modulus: Psi_p = eps * (v - 1) for v >= 1;
# below incipient plasmolysis (cell in a solution) the protoplast leaves the wall and Psi_p = 0.
# A: the three components for Psi_s0 = -1.0 MPa, eps = 7 MPa (full turgor where Psi_w = 0).
# B: cell water potential for three wall stiffnesses (eps = 3, 7, 20 MPa): a stiff wall gives a
#    large change of Psi_w for a small change of volume.
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(24.0, 9.6)

PS0, EPS = -1.0, 7.0


def components(v, eps=EPS, ps0=PS0):
    ps = ps0 / v
    pp = np.where(v >= 1.0, eps * (v - 1.0), 0.0)
    return ps, pp, ps + pp


def full_turgor(eps, ps0=PS0):
    # eps (v - 1) = -ps0 / v  ->  eps v^2 - eps v + ps0 = 0
    return (eps + np.sqrt(eps**2 - 4 * eps * ps0)) / (2 * eps)


# ---- A ----------------------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.2, 9.5))
pa = charts.axes_at(ax, (2.2, 1.5, 8.6, 6.9))
vft = full_turgor(EPS)
v = np.linspace(0.85, vft, 400)
ps, pp, pw = components(v)
pa.axvspan(0.85, 1.0, color=P.mix(P.muted(), P.surface(), 0.82), lw=0)
pa.axhline(0, color=P.muted(), lw=0.7)
pa.plot(v, ps, color=charts.line("metabolite"), lw=1.6)
pa.plot(v, pw, color=charts.line("dna"), lw=2.0, zorder=5)
pa.plot(v, pp, color=charts.line("cell_wall"), lw=1.6)
pa.plot([1.0], [PS0], "o", ms=5, color=charts.line("dna"))
pa.plot([vft], [0.0], "o", ms=5, color=charts.line("dna"))
pa.text(vft - 0.004, 0.62, "Ψp", color=charts.line("cell_wall"), fontsize=9, ha="right")
pa.text(0.93, -1.24, "Ψs = Ψw", color=charts.line("metabolite"), fontsize=9)
pa.text(1.065, -0.66, "Ψw = Ψs + Ψp", color=charts.line("dna"), fontsize=9)
pa.annotate("incipient\nplasmolysis\n(Ψp = 0, Ψw = Ψs)", (1.0, PS0), (1.03, -1.45), fontsize=7.5, color=P.ink(),
            arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
pa.annotate("full turgor\n(Ψw = 0, Ψp = −Ψs)", (vft, 0.0), (0.995, 0.66), fontsize=7.5, color=P.ink(),
            arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
pa.text(0.857, 0.78, "plasmolysed\n(in solution)", fontsize=7.5, color=P.muted())
pa.set_xlim(0.85, vft + 0.01)
pa.set_ylim(-1.3 / 0.85 * 0.97, 1.0)
charts.style_axes(pa, "relative protoplast volume V / V_ip", "Ψ / MPa")
charts.title(pa, "Components of cell water potential")

# ---- B ----------------------------------------------------------------------------------------------------
bio.panel(ax, "B", (12.6, 9.5))
pb = charts.axes_at(ax, (14.6, 1.5, 8.6, 6.9))
for eps, tok, txt in ((3.0, "plant", "ε = 3 MPa (elastic)"), (7.0, "dna", "ε = 7 MPa"), (20.0, "rna", "ε = 20 MPa (stiff)")):
    vf = full_turgor(eps)
    vv = np.linspace(1.0, vf, 200)
    _, _, w = components(vv, eps)
    pb.plot(vv, w, color=charts.line(tok), lw=1.8)
    pb.plot([], [], color=charts.line(tok), lw=1.8, label=txt)
leg = pb.legend(loc="lower right", frameon=False, fontsize=8)
for t in leg.get_texts():
    t.set_color(P.ink())
pb.axhline(0, color=P.muted(), lw=0.7)
pb.set_xlim(0.99, 1.33)
pb.set_ylim(-1.05, 0.1)
charts.style_axes(pb, "relative protoplast volume V / V_ip", "Ψw / MPa")
charts.title(pb, "Wall stiffness sets the volume change")
