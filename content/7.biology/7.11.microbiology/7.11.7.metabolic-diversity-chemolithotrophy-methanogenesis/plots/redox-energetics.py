"""Energy available from inorganic electron donors and from the alternative electron acceptors.

A: standard transformed Gibbs energy (pH 7) per two electrons transferred for chemolithotrophic reactions.
Aerobic reactions after Madigan et al. (2019): H2 -237.2; HS- to S0 -209.4; S0 to sulfate -195.7;
ammonium to nitrite -91.6; nitrite to nitrate -74.1; Fe2+ to Fe3+ at pH 2 -65.8 kJ per 2 e-. Anaerobic
H2 oxidation: with sulfate (4 H2 + SO4^2- + H+ -> HS- + 4 H2O, -152 kJ) -38; with CO2 to methane
(4 H2 + HCO3- + H+ -> CH4 + 3 H2O, -135.6 kJ) -34; with CO2 to acetate (4 H2 + 2 HCO3- + H+ -> acetate +
4 H2O, -104.6 kJ) -26 kJ per 2 e-. Dashed line: about -20 kJ, the smallest free-energy change per
reaction that cells are commonly estimated to be able to couple to ATP synthesis (one ion pumped).
B: the electron-acceptor ladder: Delta G'° for the complete oxidation of acetate (8 e-, E'° of CO2/acetate
-0.29 V) with each acceptor, from Delta G'° = -zF Delta E'°. E'° (V): O2/H2O +0.82; NO3-/N2 +0.75;
MnO2/Mn2+ about +0.40 (1 M Mn2+); Fe(III) oxide/Fe2+ about -0.1 to +0.2 depending on the mineral (range bar);
SO4^2-/HS- -0.22; CO2/CH4 -0.24 (acetate cleavage to methane plus CO2).
"""
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(26.0, 11.6)
F = 96.485

# A ------------------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.3, 11.4))
bio.label(ax, (6.9, 11.0), "Chemolithotrophy: energy per 2 e⁻", size="small", bold=True)
A = [("H₂ + O₂", -237.2, "dna"), ("HS⁻ → S⁰ (O₂)", -209.4, "atp"), ("S⁰ → SO₄²⁻ (O₂)", -195.7, "atp"),
     ("NH₄⁺ → NO₂⁻ (O₂)", -91.6, "enzyme"), ("NO₂⁻ → NO₃⁻ (O₂)", -74.1, "enzyme"), ("Fe²⁺ → Fe³⁺ (O₂, pH 2)", -65.8, "rna"),
     ("H₂ + SO₄²⁻", -152.0 / 4, "neutral"), ("H₂ + CO₂ → CH₄", -135.6 / 4, "neutral"), ("H₂ + CO₂ → acetate", -104.6 / 4, "neutral")]
n = len(A)
pa = quant.Plot(ax, (4.8, 1.2, 7.8, 9.0), xlim=(-260, 0), ylim=(0, n), xlabel="ΔG'° / (kJ per 2 e⁻)",
                xticks=[-250, -200, -150, -100, -50, 0], frame="l", grid=True)
for i, (name, g, tok) in enumerate(A):
    y = n - 1 - i
    pa.band(np.array([g, 0]), np.array([y + 0.18, y + 0.18]), np.array([y + 0.82, y + 0.82]), token=tok, alpha=0.9)
    pa.text(g - 4, y + 0.5, f"{g:.0f}".replace("-", "−"), size="tiny", ha="right")
    bio.label(ax, (4.6, float(pa.Y(y + 0.5))), name, size="tiny", ha="right")
pa.vline(-20, text="≈ −20 kJ", top=True)

# B ------------------------------------------------------------------------------------------------
bio.panel(ax, "B", (13.6, 11.4))
bio.label(ax, (19.6, 11.0), "Anaerobic respiration: acceptor ladder (acetate as donor)", size="small", bold=True)
Ed = -0.29
B = [("O₂ / H₂O", 0.82, None, "dna"), ("NO₃⁻ / N₂", 0.75, None, "enzyme"), ("MnO₂ / Mn²⁺", 0.40, (0.30, 0.50), "protein"),
     ("Fe(III) oxide / Fe²⁺", 0.05, (-0.10, 0.20), "rna"), ("SO₄²⁻ / HS⁻", -0.22, None, "atp"), ("CO₂ / CH₄", -0.24, None, "neutral")]
m = len(B)
pb = quant.Plot(ax, (17.6, 1.2, 7.8, 9.0), xlim=(-900, 0), ylim=(0, m), xlabel="ΔG'° / (kJ per acetate)",
                xticks=[-800, -600, -400, -200, 0], frame="l", grid=True)
for i, (name, E, rng, tok) in enumerate(B):
    y = m - 1 - i
    g = -8 * F * (E - Ed)
    pb.band(np.array([g, 0]), np.array([y + 0.2, y + 0.2]), np.array([y + 0.8, y + 0.8]), token=tok, alpha=0.9)
    if rng:
        g0, g1 = (-8 * F * (e - Ed) for e in rng)
        pb.line([g0, g1], [y + 0.5, y + 0.5], "ink", lw=1.0)
        for gg in (g0, g1):
            pb.line([gg, gg], [y + 0.38, y + 0.62], "ink", lw=1.0)
    lab = f"{g:.0f}".replace("-", "−")
    if g < -150:
        pb.text(g + 12, y + 0.5 if not rng else y + 0.72, lab, size="tiny", ha="left", color=P.on_fill())
    else:
        pb.text(g - 12, y + 0.5, lab, size="tiny", ha="right")
    bio.label(ax, (17.4, float(pb.Y(y + 0.62))), name, size="tiny", ha="right")
    bio.label(ax, (17.4, float(pb.Y(y + 0.3))), f"E'° ≈ {E:+.2f} V".replace("-", "−"), size="tiny", ha="right", color=P.muted())
bio.label(ax, (21.5, 0.15), "order of use in sediments: from top to bottom", size="tiny", color=P.muted())
