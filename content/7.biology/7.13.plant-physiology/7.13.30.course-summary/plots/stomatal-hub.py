# The stoma as the hub that couples water and carbon (a C3 leaf).
# For each stomatal conductance g_s the operating point is where the Farquhar demand curve
# (Eqs. 9.3-9.6, Bernacchi 2001 constants, Vcmax = 80, J = 150, Rd = 1 umol m^-2 s^-1) meets the diffusive
# supply line A = (g_s / 1.6)(c_a - c_i) (Eq. 9.7, mesophyll conductance ignored, c_a = 420 umol/mol).
# Transpiration E = g_tw * dw with 1/g_tw = 1/g_s + 1/g_b (Eq. 3.5), boundary-layer conductance g_b = 3 mol m^-2 s^-1.
# A: A and E against g_s at D = 1.5 kPa.  B: c_i / c_a.  C: water-use efficiency A/E for three leaf-to-air
# vapour pressure differences: A saturates while E keeps rising, so WUE falls as the stomata open wider and
# as the air dries.
import numpy as np

import wikibio as bio
from wikibio import charts
from wikibio import photosynthesis as ps

P = bio.P
ca, p_atm, gb = 420.0, 101.3, 3.0
gs = np.linspace(0.005, 0.8, 300)


def operating_point(g):
    gc = g / 1.6
    lo, hi = ps.GAMMA_STAR, ca
    for _ in range(60):
        ci = 0.5 * (lo + hi)
        demand = float(ps.farquhar(ci, vcmax=80.0, j=150.0, rd=1.0)[0])
        supply = gc * (ca - ci)
        if demand > supply:
            hi = ci
        else:
            lo = ci
    ci = 0.5 * (lo + hi)
    return gc * (ca - ci), ci


A = np.empty_like(gs)
Ci = np.empty_like(gs)
for k, g in enumerate(gs):
    A[k], Ci[k] = operating_point(g)


def transpiration(D):
    dw = D / p_atm  # mol/mol
    return dw / (1 / gs + 1 / gb) * 1000.0  # mmol m^-2 s^-1


fig, ax = bio.canvas(30.0, 9.6)
w, h = 7.2, 6.6
a1 = charts.axes_at(ax, (1.6, 1.6, w, h))
a2 = charts.axes_at(ax, (11.6, 1.6, w, h))
a3 = charts.axes_at(ax, (21.6, 1.6, w, h))

cA, cE = charts.line("chloroplast"), charts.line("dna")
a1.plot(gs, A, color=cA, lw=2.2, label="A (net CO₂ uptake)")
a1.set_ylim(0, 30)
a1b = a1.twinx()
a1b.plot(gs, transpiration(1.5), color=cE, lw=2.2, ls="--", label="E (transpiration)")
a1b.set_ylim(0, 12)
charts.style_axes(a1, r"$g_{\mathrm{s}}$ / (mol m⁻² s⁻¹)", "A / (µmol m⁻² s⁻¹)")
charts.style_axes(a1b, None, "E / (mmol m⁻² s⁻¹)", box=True)
a1b.spines["top"].set_visible(False)
a1b.spines["left"].set_visible(False)
a1b.spines["bottom"].set_visible(False)
h1, l1 = a1.get_legend_handles_labels()
h2, l2 = a1b.get_legend_handles_labels()
a1.legend(h1 + h2, l1 + l2, frameon=False, fontsize=8, loc="lower right", labelcolor=P.ink())
charts.title(a1, "A   Carbon gain saturates, water loss does not")

a2.plot(gs, Ci / ca, color=charts.line("enzyme"), lw=2.2)
a2.axhline(0.7, color=P.muted(), lw=0.8, ls=":")
a2.text(0.79, 0.715, "typical C3 leaf ≈ 0.7", fontsize=7.5, color=P.muted(), ha="right", va="bottom")
a2.set_ylim(0, 1)
charts.style_axes(a2, r"$g_{\mathrm{s}}$ / (mol m⁻² s⁻¹)", r"$c_{\mathrm{i}}/c_{\mathrm{a}}$")
charts.title(a2, "B   Intercellular CO₂ rises with stomatal opening")

for D, tok in ((0.8, "chloroplast"), (1.5, "dna"), (3.0, "negative")):
    a3.plot(gs, A / transpiration(D), color=charts.line(tok), lw=2.2, label=f"D = {D:g} kPa")
a3.set_ylim(0, 16)
a3.legend(frameon=False, fontsize=8, loc="upper right", labelcolor=P.ink())
charts.style_axes(a3, r"$g_{\mathrm{s}}$ / (mol m⁻² s⁻¹)", "A/E / (µmol CO₂ per mmol H₂O)")
charts.title(a3, "C   Water-use efficiency falls")
