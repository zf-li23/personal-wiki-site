"""Free energy of transport across a membrane, dG_t = RT ln(c2/c1) + zF dphi, at 37 deg C.

A: dG_t against the concentration ratio c2/c1 (destination/origin) for an uncharged solute and for
cations moved across a plasma membrane with a membrane potential of -50 mV (inside negative): a
monovalent cation moved inward gains -4.8 kJ/mol from the field, one moved outward pays +4.8, a
divalent cation moved outward pays +9.6. Points: export of Ca2+ from the cytosol (0.1 uM) to the
extracellular fluid (1 mM), +33 kJ/mol; entry of Na+ (145 mM outside, 12 mM inside), -11.2 kJ/mol.
The shaded band is the free energy available from ATP hydrolysis in cells (about 50-60 kJ/mol).
B: the largest glucose accumulation ratio [glucose]in/[glucose]out a Na+-glucose symporter can reach
with perfect coupling, against the membrane potential, for 1 and 2 Na+ per glucose
([Na+]out = 145 mM, [Na+]in = 12 mM). Points mark -50 mV (the value used by Lehninger) and -70 mV.
"""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
R, T, F = 8.314, 310.0, 96485.0
RT = R * T / 1000  # kJ/mol
dphi = -0.050  # V, inside relative to outside

fig, ax = bio.canvas(20.0, 7.8)
bio.panel(ax, "A", (0.1, 7.7))
pa = charts.axes_at(ax, (1.7, 1.4, 7.6, 5.6))
r = np.logspace(-3, 5, 300)
lines = [("uncharged solute", 0.0, "neutral", "-"), ("cation (z = +1) inward", +F * dphi / 1000, "na", "-"),
         ("cation (z = +1) outward", -F * dphi / 1000, "k", "--"), ("cation (z = +2) outward", -2 * F * dphi / 1000, "ca", "--")]
for name, el, tok, ls in lines:
    pa.semilogx(r, RT * np.log(r) + el, color=charts.line(tok), lw=1.8, ls=ls if ls == "-" else (0, (4, 2.4)), label=name)
pa.axhspan(50, 60, color=P.fill("atp"), alpha=0.35, lw=0)
pa.text(1.5e-3, 53.5, "−ΔG of ATP hydrolysis in cells", fontsize=bio.core.FONT["tiny"], color=P.ink())
pa.axhline(0, color=P.muted(), lw=0.6)
ca = RT * np.log(1e-3 / 1e-7) + 2 * F * 0.050 / 1000
na = RT * np.log(12 / 145) + F * dphi / 1000
pa.plot([1e4], [ca], "o", ms=6, mfc=P.fill("ca"), mec=charts.line("ca"))
pa.text(4e2, ca + 3.5, f"Ca²⁺ export +{ca:.0f} kJ mol⁻¹", fontsize=bio.core.FONT["tiny"], color=P.ink())
pa.plot([12 / 145], [na], "o", ms=6, mfc=P.fill("na"), mec=charts.line("na"))
pa.text(0.11, na - 6.5, f"Na⁺ entry −{-na:.1f}", fontsize=bio.core.FONT["tiny"], color=P.ink())
pa.set_xlim(1e-3, 1e5)
pa.set_ylim(-30, 62)
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(pa, "concentration ratio c₂/c₁ (destination / origin)", r"$\Delta G_\mathrm{t}$ / (kJ mol$^{-1}$)")
charts.title(pa, "Cost of transport, membrane potential −50 mV")

bio.panel(ax, "B", (10.6, 7.7))
pb = charts.axes_at(ax, (12.3, 1.4, 7.0, 5.6))
v = np.linspace(-0.12, 0.0, 200)
per_na = RT * np.log(145 / 12) - F * v / 1000  # kJ released per Na+ entering
for n, tok in ((1, "carbohydrate"), (2, "enzyme")):
    pb.semilogy(v * 1000, np.exp(n * per_na / RT), color=charts.line(tok), lw=1.8, label=f"{n} Na⁺ per glucose")
    for vv in (-0.050, -0.070):
        val = np.exp(n * (RT * np.log(145 / 12) - F * vv / 1000) / RT)
        pb.plot([vv * 1000], [val], "o", ms=5, mfc=P.fill(tok), mec=charts.line(tok))
        if n == 2:
            pb.text(vv * 1000 + 2, val * 1.5, f"{val:,.0f}".replace(",", " "), fontsize=bio.core.FONT["tiny"], color=P.ink())
pb.set_xlim(-120, 0)
pb.set_ylim(1, 1e6)
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(pb, r"membrane potential $\varphi_\mathrm{in} - \varphi_\mathrm{out}$ / mV", r"maximal [glucose]$_\mathrm{in}$ / [glucose]$_\mathrm{out}$")
charts.title(pb, "Na⁺-driven glucose accumulation")
