# Water potential along the soil-plant-atmosphere continuum as a series-resistance (Ohm's law) model,
# Psi_leaf = Psi_soil - E * R_plant - rho g h, with leaf-area based fluxes (illustrative values for a 10 m tree).
# Moist soil: Psi_soil = -0.1 MPa, whole-path conductance K = 6 mmol m-2 s-1 MPa-1, peak E = 5 mmol m-2 s-1.
# Dry soil: Psi_soil = -0.8 MPa; soil hydraulic conductivity has fallen so K = 3, and partial stomatal closure
# limits the peak E to 2.5 mmol m-2 s-1.
# A: diurnal course of transpiration (top) and leaf water potential (bottom); before dawn E = 0 and the
#    leaf comes to equilibrium with the soil (minus the gravitational term).
# B: profiles along the path at predawn and midday; the fractions of the resistance in soil, root, stem
#    and leaf differ between moist (10/35/25/30 %) and dry soil (50/25/12/13 %).
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(26.0, 10.4)
RHOGH = 0.1  # MPa for 10 m
cases = {
    "moist": dict(psoil=-0.1, K=6.0, Emax=5.0, frac=(0.10, 0.35, 0.25, 0.30), tok="dna"),
    "dry": dict(psoil=-0.8, K=3.0, Emax=2.5, frac=(0.50, 0.25, 0.12, 0.13), tok="rna"),
}
t = np.linspace(0, 24, 481)


def transp(c):
    return c["Emax"] * np.clip(np.sin(np.pi * (t - 6) / 12), 0, None)


# ---- A: diurnal --------------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.2, 10.3))
pe = charts.axes_at(ax, (2.3, 6.4, 9.6, 2.9))
pl = charts.axes_at(ax, (2.3, 1.4, 9.6, 4.2))
for name, c in cases.items():
    E = transp(c)
    col = charts.line(c["tok"])
    pe.plot(t, E, color=col, lw=1.8, label=f"{name} soil")
    pl.plot(t, c["psoil"] - RHOGH - E / c["K"], color=col, lw=1.8)
    pl.axhline(c["psoil"], color=col, lw=0.8, ls=":")
pl.text(19.5, -0.085, "Ψsoil (moist)", fontsize=7.5, color=charts.line("dna"), va="bottom")
pl.text(19.5, -0.785, "Ψsoil (dry)", fontsize=7.5, color=charts.line("rna"), va="bottom")
pl.text(12, -1.34, "midday minimum", fontsize=7.5, color=P.muted(), ha="center")
for a in (pe, pl):
    a.set_xlim(0, 24)
    a.set_xticks([0, 6, 12, 18, 24])
pe.set_xticklabels([])
pe.set_ylim(0, 5.6)
pl.set_ylim(-1.95, 0.05)
leg = pe.legend(loc="upper left", frameon=False, fontsize=7.5)
for tt in leg.get_texts():
    tt.set_color(P.ink())
charts.style_axes(pe, None, "E / (mmol m⁻² s⁻¹)")
charts.style_axes(pl, "time of day / h", "Ψleaf / MPa")
charts.title(pe, "Diurnal course")

# ---- B: profiles -------------------------------------------------------------------------------------------
bio.panel(ax, "B", (13.6, 10.3))
pp = charts.axes_at(ax, (15.6, 1.4, 9.8, 7.9))
xs = np.arange(5)
names = ["soil", "root\nsurface", "root\nxylem", "leaf\nxylem", "leaf\ncells"]
for name, c in cases.items():
    col = charts.line(c["tok"])
    drop = c["Emax"] / c["K"]
    f = c["frac"]
    grav = np.array([0, 0, 0, RHOGH, RHOGH])
    mid = c["psoil"] - np.concatenate([[0], np.cumsum(f)]) * drop - grav
    pre = c["psoil"] - grav
    pp.plot(xs, mid, "-o", color=col, lw=1.8, ms=4, label=f"{name} soil, midday")
    pp.plot(xs, pre, "--", color=col, lw=1.1, label=f"{name} soil, predawn")
pp.set_xticks(xs)
pp.set_xticklabels(names)
pp.set_ylim(-1.95, 0.05)
leg = pp.legend(loc="lower left", frameon=False, fontsize=7.5)
for tt in leg.get_texts():
    tt.set_color(P.ink())
charts.style_axes(pp, None, "Ψ / MPa")
charts.title(pp, "Profiles along the path")
