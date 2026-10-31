"""Sedimentation equilibrium (Formulas 8.9.1 and 8.9.2).

Column from 6.90 to 7.20 cm at 12 000 rpm and 20 C; partial specific volume 0.73 mL/g, solvent
density 1.0 g/mL. Concentration profiles c(r) = c0 exp(sigma xi), xi = (r^2 - r0^2)/2, with the
reduced molar mass sigma = M (1 - vbar rho) w^2 / R T, for: a 50 kDa monomer; a 100 kDa dimer; a
reversible monomer-dimer equilibrium c = c1 + K c1^2 (c1 = c_10 exp(sigma_1 xi), K = 2 L/g);
and a nonideal 50 kDa monomer (second virial coefficient, apparent M = M/(1 + 2 B M c)).
All are normalized to the same loading concentration (1 g/L). A: c(r). B: ln c against xi; a single
ideal species gives a straight line whose slope is sigma. C: apparent weight-average molar mass
M_w,app = (d ln c / d xi) / [(1 - vbar rho) w^2 / R T] as a function of the local concentration.
"""

import numpy as np
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
R, T = 8.314, 293.15
vbar, rho = 0.73e-3, 1000.0              # m^3/kg, kg/m^3
w = 2 * np.pi * 12000 / 60
r0, rb = 6.90, 7.20
r = np.linspace(r0, rb, 400)
xi = (r ** 2 - r0 ** 2) / 2 * 1e-4       # m^2
buoy = (1 - vbar * rho) * w ** 2 / (R * T)   # per (kg/mol) per m^2


def sigma(M):
    return M * buoy


def normalize(c):
    """Scale to a loading concentration of 1 g/L (mass conservation in a sector cell: int c r dr)."""
    return c / (np.trapezoid(c * r, r) / np.trapezoid(r, r))


ideal1 = normalize(np.exp(sigma(50.0) * xi))
ideal2 = normalize(np.exp(sigma(100.0) * xi))
K = 2.0                                  # L/g, so that c2 = K c1^2 in g/L


def md_profile(c10):
    c1 = c10 * np.exp(sigma(50.0) * xi)
    return c1 + K * c1 ** 2


c10 = brentq(lambda a: np.trapezoid(md_profile(a) * r, r) / np.trapezoid(r, r) - 1.0, 1e-6, 10)
md = md_profile(c10)
# nonideal monomer: d ln c / d xi = sigma / (1 + 2 B M c), B M = 0.05 L/g (B in mol L/g^2)
BM = 0.05


def nonideal(c0):
    out = [c0]
    for i in range(1, r.size):
        c = out[-1]
        out.append(c * np.exp(sigma(50.0) / (1 + 2 * BM * c) * (xi[i] - xi[i - 1])))
    return np.array(out)


a = brentq(lambda c0: np.trapezoid(nonideal(c0) * r, r) / np.trapezoid(r, r) - 1.0, 1e-4, 5)
ni = nonideal(a)
CASES = [("monomer 50 kDa", ideal1, "protein"), ("dimer 100 kDa", ideal2, "receptor"),
         ("monomer–dimer", md, "enzyme"), ("nonideal monomer", ni, "neutral")]

fig, ax = bio.canvas(24.0, 8.0)
bio.panel(ax, "A", (0.1, 7.9))
pa = charts.axes_at(ax, (1.5, 1.3, 6.0, 5.8))
for name, c, tok in CASES:
    pa.plot(r, c, color=charts.line(tok), lw=1.6, label=name)
pa.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(pa, "radius r / cm", "c / (g/L)")
charts.title(pa, "Equilibrium profiles (12 000 rpm)")

bio.panel(ax, "B", (8.3, 7.9))
pb = charts.axes_at(ax, (9.7, 1.3, 6.0, 5.8))
for name, c, tok in CASES:
    pb.plot(xi * 1e4, np.log(c), color=charts.line(tok), lw=1.6)
pb.text(0.75, -2.2, "slope = σ = M(1 − v̄ρ)ω²/RT", fontsize=FT["tiny"], color=P.ink())
charts.style_axes(pb, r"$\xi = (r^2 - r_0^2)/2$ / cm$^2$", "ln c")
charts.title(pb, "Straight only for one ideal species")

bio.panel(ax, "C", (16.5, 7.9))
pc = charts.axes_at(ax, (17.9, 1.3, 6.0, 5.8))
for name, c, tok in CASES:
    Mw = np.gradient(np.log(c), xi, edge_order=2) / buoy
    if name.endswith("kDa"):                   # ideal single species: exactly constant
        Mw = np.full_like(c, 50.0 if name.startswith("monomer") else 100.0)
    pc.plot(c, Mw, color=charts.line(tok), lw=1.6)
pc.set_xscale("log")
pc.set_ylim(30, 110)
charts.style_axes(pc, "local concentration c / (g/L)", r"$M_{w,\mathrm{app}}$ / kDa", box=True)
charts.title(pc, "Apparent molar mass along the cell")
