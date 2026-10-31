"""Linked equilibria seen by calorimetry (Formulas 8.4.4 and 8.3.3).

A: apparent binding enthalpy measured by ITC in buffers of different ionization enthalpy
(Delta H_ion at 25 C: acetate -0.4, phosphate 3.6, PIPES 11.2, HEPES 20.4, MOPS 21.1, imidazole 36.6,
Tris 47.5 kJ/mol). Delta H_app = Delta H_b + n_H Delta H_ion; two simulated complexes with
Delta H_b = -60 kJ/mol and n_H = 0.73 or 0.02 (noise 0.8 kJ/mol, seed 0), fitted by straight lines.
B, C: thermal shift: a ligand that binds only the native state raises T_m; the new T_m solves
Delta G_U(T) + R T ln(1 + [L]/K_d) = 0 (protein of Fig. 8.3.1, K_d independent of temperature).
B: fraction unfolded for [L]/K_d = 0, 1, 10, 100, 1000. C: T_m against [L]/K_d, exact and the
small-shift approximation Delta T_m = (R T_m^2 / Delta H_m) ln(1 + [L]/K_d).
"""

import numpy as np
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
R = 8.314e-3
BUF = [("acetate", -0.41), ("phosphate", 3.6), ("PIPES", 11.2), ("HEPES", 20.4), ("MOPS", 21.1),
       ("imidazole", 36.6), ("Tris", 47.45)]

fig, ax = bio.canvas(25.0, 8.2)
bio.panel(ax, "A", (0.1, 8.1))
pa = charts.axes_at(ax, (1.5, 1.3, 6.6, 5.8))
rng = np.random.default_rng(0)
x = np.array([b[1] for b in BUF])
for nH, tok in ((0.73, "protein"), (0.02, "enzyme")):
    y = -60.0 + nH * x + rng.normal(0, 0.8, x.size)
    slope, icpt = np.polyfit(x, y, 1)
    xx = np.linspace(-5, 52, 10)
    pa.plot(x, y, "o", ms=4.5, mfc=charts.line(tok), mec="none")
    pa.plot(xx, icpt + slope * xx, color=charts.line(tok), lw=1.2,
            label=f"fit: n$_{{H^+}}$ = {slope:.2f}, ΔH$_b$ = {icpt:.1f} kJ/mol")
for name, v in BUF:
    dx = {"HEPES": -1.3, "MOPS": 1.3}.get(name, 0.0)
    pa.text(v + dx, -64.5, name, rotation=90, fontsize=FT["tiny"], color=P.muted(), ha="center", va="top")
pa.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
pa.set_xlim(-5, 52)
pa.set_ylim(-82, -16)
charts.style_axes(pa, r"$\Delta H_\mathrm{ion}$ of buffer / (kJ/mol)", r"$\Delta H_\mathrm{app}$ / (kJ/mol)")
charts.title(pa, "Protons taken up on binding")

Tm, dHm, dCp = 333.15, 350.0, 6.0


def dG(T):
    return dHm * (1 - T / Tm) + dCp * (T - Tm - T * np.log(T / Tm))


bio.panel(ax, "B", (8.9, 8.1))
pb = charts.axes_at(ax, (10.3, 1.3, 6.4, 5.8))
T = np.linspace(273.15 + 30, 273.15 + 100, 600)
toks = ["neutral", "channel", "protein", "receptor", "enzyme"]
for r, tok in zip([0, 1, 10, 100, 1000], toks):
    K = np.exp(-dG(T) / (R * T)) / (1 + r)
    pb.plot(T - 273.15, K / (1 + K), color=charts.line(tok), lw=1.5, label=f"[L]/K$_d$ = {r}")
pb.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
pb.set_xlim(30, 100)
charts.style_axes(pb, "t / °C", "fraction unfolded")
charts.title(pb, "Ligand binding to N stabilizes")

bio.panel(ax, "C", (17.5, 8.1))
pc = charts.axes_at(ax, (18.9, 1.3, 5.8, 5.8))
rr = np.logspace(-1, 4, 60)
exact = [brentq(lambda TT: dG(TT) + R * TT * np.log(1 + r), Tm - 1, Tm + 80) for r in rr]
approx = Tm + R * Tm ** 2 / dHm * np.log(1 + rr)
pc.semilogx(rr, np.array(exact) - Tm, color=P.ink(), lw=1.6, label="exact")
pc.semilogx(rr, approx - Tm, color=P.muted(), lw=1.2, ls="--", label=r"$(RT_m^2/\Delta H_m)\ln(1+[L]/K_d)$")
pc.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(pc, "[L]/K$_d$", r"$\Delta T_m$ / K", box=True)
charts.title(pc, "Shift of the melting temperature")
