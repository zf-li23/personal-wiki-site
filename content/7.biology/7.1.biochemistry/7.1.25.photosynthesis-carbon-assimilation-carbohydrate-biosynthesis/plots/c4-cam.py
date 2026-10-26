"""CO2-concentrating pathways: C4 photosynthesis separates CO2 capture and rubisco in space, CAM in time.

A: C4, NADP-malic enzyme type (maize, sugarcane, sorghum). In the mesophyll cell, carbonic anhydrase gives
HCO3-, which PEP carboxylase adds to phosphoenolpyruvate (PEP); oxaloacetate is reduced to malate
(NADP-malate dehydrogenase in the chloroplast). Malate diffuses through plasmodesmata into the bundle-sheath
cell, where NADP-malic enzyme releases CO2 next to rubisco and the Calvin cycle; pyruvate returns and
pyruvate phosphate dikinase (PPDK) regenerates PEP at the cost of ATP -> AMP + PPi (two phosphoanhydride
bonds). B: crassulacean acid metabolism. At night the stomata are open, PEP from starch breakdown is
carboxylated and malic acid accumulates in the vacuole; in the day the stomata close, malate is
decarboxylated and the CO2 is fixed by rubisco behind closed stomata, and the three-carbon remainder is
made back into starch. C: schematic time course over a day for a CAM leaf: stomatal conductance and
vacuolar malic acid (arbitrary units).
"""

import numpy as np
from matplotlib.patches import FancyBboxPatch

import wikibio as bio
from wikibio import charts
from wikibio import metabolism as M
from wikibio import photosynthesis as ps

P = bio.P
fig, ax = bio.canvas(28.0, 21.2, scale=0.4)
ax.set_ylim(-6.2, 15.0)


def cell(x0, y0, x1, y1, txt, tok="cytoplasm"):
    ax.add_patch(FancyBboxPatch((x0, y0), x1 - x0, y1 - y0, boxstyle="round,pad=0,rounding_size=0.6",
                                facecolor=ps.tint(tok, 0.5, 0.82), edgecolor=P.edge("cell_wall"), lw=2.2, zorder=1))
    bio.label(ax, (x0 + 0.35, y1 - 0.4), txt, size="small", bold=True, ha="left", color=P.edge("cell_wall"))


# --- A: C4 ---------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.2, 14.8))
bio.label(ax, (0.9, 14.75), "C4 (NADP-malic enzyme type): separation in space", size="title", ha="left", va="top")
cell(0.4, 0.5, 7.4, 13.4, "Mesophyll cell")
cell(8.0, 0.5, 13.9, 13.4, "Bundle-sheath cell", tok="chloroplast")
for y in (2.6, 6.6, 10.9):
    ax.add_patch(FancyBboxPatch((7.35, y - 0.12), 0.7, 0.24, boxstyle="round,pad=0,rounding_size=0.1",
                                facecolor=P.fill("cell_wall"), edgecolor=P.edge("cell_wall"), lw=0.8, zorder=2))
bio.label(ax, (7.7, 0.95), "plasmodesmata", size="tiny", color=P.muted())

pw = M.Pathway(ax, size="small")
pw.node("co2a", (1.8, 12.3), "CO₂ (air)", token="neutral")
pw.node("hco3", (1.8, 10.2), "HCO₃⁻")
pw.node("pep", (1.8, 6.2), "PEP")
pw.node("oaa", (4.7, 8.2), "Oxaloacetate")
pw.node("mal", (4.7, 10.9), "Malate", bold=True)
pw.node("pyr_m", (4.7, 2.6), "Pyruvate")
pw.step("co2a", "hco3", enzyme="carbonic\nanhydrase", enzyme_offset=0.15, enzyme_flip=True)
pw.step("hco3", "oaa")
pw.step("pep", "oaa")
bio.label(ax, (2.0, 8.2), "PEP\ncarboxylase", size="tiny", bold=True, color=P.edge("enzyme"))
pw.step("oaa", "mal")
bio.label(ax, (6.3, 9.55), "NADP-MDH\n(NADPH)", size="tiny", bold=True, color=P.edge("enzyme"))
pw.step("pyr_m", "pep", enzyme="PPDK", side=("ATP + Pᵢ", "AMP + PPᵢ"), enzyme_offset=0.15, flip=True)

pw.node("mal_b", (10.9, 10.9), "Malate", bold=True)
pw.node("co2b", (9.9, 7.8), "CO₂ (≈ 10× air)", token="highlight", bold=True)
pw.node("cal", (10.2, 5.0), "Calvin cycle", token="carbohydrate")
pw.node("pyr_b", (12.0, 2.6), "Pyruvate")
pw.step("mal", "mal_b", color=P.muted(), dashed=True)
pw.step("pyr_b", "pyr_m", color=P.muted(), dashed=True)
pw.step("mal_b", "co2b", side=("NADP⁺", "NADPH"), flip=True)
bio.label(ax, (12.95, 8.6), "NADP-ME", size="tiny", bold=True, color=P.edge("enzyme"))
pw.step(None, "pyr_b", start=pw.anchor("mal_b", "b") + (0.55, 0.05), end=pw.anchor("pyr_b", "t") + (0.55, 0.05))
pw.step("co2b", "cal", enzyme="rubisco", enzyme_offset=0.15)
# --- B: CAM --------------------------------------------------------------------------------------
bio.panel(ax, "B", (14.6, 14.8))
bio.label(ax, (15.3, 14.75), "CAM: separation in time", size="title", ha="left", va="top")
cell(14.8, 7.4, 27.6, 13.4, "Night: stomata open", tok="cytoplasm")
cell(14.8, 0.5, 27.6, 6.9, "Day: stomata closed", tok="chloroplast")
pn = M.Pathway(ax, size="small")
pn.node("st", (16.8, 9.0), "Starch")
pn.node("pepn", (19.6, 9.0), "PEP")
pn.node("co2n", (19.6, 11.8), "CO₂ → HCO₃⁻", token="neutral")
pn.node("oaan", (22.6, 9.0), "Oxaloacetate")
pn.node("maln", (25.6, 9.0), "Malate", bold=True)
pn.step("st", "pepn", enzyme="glycolysis", enzyme_offset=0.15)
pn.step("pepn", "oaan", enzyme="PEP carboxylase", enzyme_offset=0.15)
pn.step(None, "oaan", start=pn.anchor("co2n", "r") + (0.05, -0.1), bend=-0.15)
pn.step("oaan", "maln", enzyme="MDH", side=("NADH", "NAD⁺"), enzyme_offset=0.15, flip=True)
ax.add_patch(FancyBboxPatch((24.3, 10.6), 2.7, 1.5, boxstyle="round,pad=0,rounding_size=0.5",
                            facecolor=P.fill("vacuole"), edgecolor=P.edge("vacuole"), lw=1.0, zorder=5))
bio.label(ax, (25.65, 11.35), "vacuole:\nmalic acid", size="tiny", bold=True, zorder=12)
bio.arrow(ax, (25.6, 9.45), (25.6, 10.55), kind="process")

pd = M.Pathway(ax, size="small")
pd.node("mald", (25.6, 5.3), "Malate", bold=True)
pd.node("co2d", (21.2, 5.3), "CO₂", token="highlight", bold=True)
pd.node("cald", (17.4, 5.3), "Calvin cycle → sugars", token="carbohydrate")
pd.node("pyrd", (21.2, 2.2), "Pyruvate")
pd.node("std", (17.4, 2.2), "Starch")
pd.step("mald", "co2d", enzyme="NADP-malic enzyme", enzyme_offset=0.15)
pd.step("co2d", "cald", enzyme="rubisco", enzyme_offset=0.15)
pd.step(None, "pyrd", start=pd.anchor("mald", "b") + (-0.3, 0), bend=-0.15)
pd.step("pyrd", "std", enzyme="gluconeogenesis", enzyme_offset=0.15)
bio.arrow(ax, (25.6, 10.55), (25.6, 5.8), kind="process", dashed=True, color=P.muted())
bio.label(ax, (26.4, 7.15), "next day", size="tiny", color=P.muted(), rotation=90)

# --- C: schematic CAM day -----------------------------------------------------------------------
c = charts.axes_at(ax, (2.0, -5.0, 24.5, 3.6))
t = np.linspace(0, 24, 241)
night = ((t < 6) | (t > 18)).astype(float)
gs = 0.15 + 0.85 * np.clip(np.cos((t - 0) / 24 * 2 * np.pi), 0, None) ** 0.6
mal = np.interp(t, [0, 6, 7, 12, 17, 18, 24], [0.55, 1.0, 1.0, 0.35, 0.1, 0.1, 0.55])
c.fill_between(t, 0, 1.1, where=night > 0, color=P.mix(P.muted(), P.surface(), 0.75), lw=0, step="mid")
c.plot(t, gs, color=charts.line("dna"), lw=2.0, label="stomatal conductance")
c.plot(t, mal, color=charts.line("lipid"), lw=2.0, label="vacuolar malic acid")
c.set_xlim(0, 24)
c.set_ylim(0, 1.1)
c.set_xticks([0, 6, 12, 18, 24])
charts.style_axes(c, "time of day / h", "relative value")
c.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper center", ncol=2)
bio.panel(ax, "C", (0.2, -0.5))
