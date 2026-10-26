"""Partitioning of triose phosphate between starch (chloroplast) and sucrose (cytosol).

The Pi-triose phosphate translocator (TPT) of the inner envelope exchanges stromal triose phosphate for
cytosolic Pi. Cytosol: aldolase and FBPase-1 give fructose 6-phosphate, which phosphohexose isomerase and
phosphoglucomutase convert to glucose 1-phosphate and UDP-glucose; sucrose 6-phosphate synthase (SPS)
joins UDP-glucose and fructose 6-phosphate, and sucrose 6-phosphate phosphatase (SPP) releases sucrose.
Regulation: fructose 2,6-bisphosphate (F2,6BP) inhibits cytosolic FBPase-1; its synthesis by PFK-2 is
inhibited by triose phosphate and 3-phosphoglycerate (abundant in light) and stimulated by Pi and
fructose 6-phosphate. SPS is activated by glucose 6-phosphate and inhibited by Pi. Chloroplast: ADP-glucose
pyrophosphorylase (AGPase), the regulated step of starch synthesis, is activated by 3-phosphoglycerate and
inhibited by Pi, so starch is made when sucrose synthesis lags and stromal 3-PGA rises while Pi falls.
"""

from matplotlib.patches import FancyBboxPatch

import wikibio as bio
from wikibio import metabolism as M
from wikibio import photosynthesis as ps

P = bio.P
fig, ax = bio.canvas(27.0, 14.2, scale=0.42)
for (x0, x1), tok, txt in (((0.3, 10.4), "chloroplast", "Chloroplast stroma"), ((11.6, 26.7), "cytoplasm", "Cytosol")):
    ax.add_patch(FancyBboxPatch((x0, 0.3), x1 - x0, 13.6, boxstyle="round,pad=0,rounding_size=0.7",
                                facecolor=ps.tint(tok, 0.5, 0.82), edgecolor=P.edge(tok), lw=1.3, zorder=1))
    bio.label(ax, (x0 + 0.4, 13.45), txt, size="small", bold=True, ha="left", color=P.edge(tok))
bio.box(ax, (11.0, 9.4), 1.0, 2.0, "channel")
bio.label(ax, (11.0, 8.05), "TPT", size="tiny", bold=True, va="top")

pw = M.Pathway(ax, size="small")
# chloroplast
pw.node("cal", (5.0, 12.2), "Calvin cycle", token="carbohydrate", bold=True)
pw.node("tp", (7.6, 9.4), "Triose phosphate")
pw.node("pga", (2.4, 9.4), "3-Phosphoglycerate")
pw.node("f6p_c", (7.6, 6.6), "Fructose 6-P → glucose 6-P")
pw.node("g1p_c", (7.6, 4.6), "Glucose 1-P")
pw.node("adpg", (4.2, 4.6), "ADP-glucose")
pw.node("starch", (4.2, 1.6), "Starch", token="carbohydrate", bold=True)
pw.step("cal", "tp")
pw.step("cal", "pga")
pw.step("tp", "f6p_c", enzyme="aldolase,\nFBPase", enzyme_offset=0.2)
pw.step("f6p_c", "g1p_c", enzyme="PGM", enzyme_offset=0.2, reversible=True)
pw.step("g1p_c", "adpg", enzyme="AGPase", side=("ATP", "PPᵢ → 2 Pᵢ"), enzyme_offset=0.2)
pw.step("adpg", "starch", enzyme="starch synthase", side=(None, "ADP"), enzyme_offset=0.2)
# cytosol
pw.node("tp_y", (14.0, 9.4), "Triose phosphate")
pw.node("pi_y", (14.0, 12.2), "Pᵢ")
pw.node("fbp", (17.8, 9.4), "Fructose 1,6-BP")
pw.node("f6p", (17.8, 6.6), "Fructose 6-P")
pw.node("g6p", (13.9, 6.6), "Glucose 6-P")
pw.node("udpg", (13.9, 4.0), "UDP-glucose")
pw.node("s6p", (17.8, 4.0), "Sucrose 6-P")
pw.node("suc", (17.8, 1.6), "Sucrose → phloem", token="carbohydrate", bold=True)
pw.step("tp", "tp_y", reversible=True, color=P.muted())
pw.step(None, "pi_y", start=(11.3, 10.5), end=pw.anchor("pi_y", "l") + (-0.1, 0), color=P.muted(), bend=0.25)
bio.label(ax, (11.0, 12.5), "Pᵢ in, triose-P out", size="tiny", color=P.muted())
pw.step("tp_y", "fbp", enzyme="aldolase", enzyme_offset=0.2)
pw.step("fbp", "f6p", enzyme="FBPase-1", side=("H₂O", "Pᵢ"), enzyme_offset=0.2, flip=True)
pw.step("f6p", "g6p", reversible=True, enzyme="isomerase", enzyme_offset=0.2)
pw.step("g6p", "udpg", enzyme="PGM, UGPase", side=("UTP", "PPᵢ"), enzyme_offset=0.2)
pw.step("udpg", "s6p", enzyme="SPS", side=("UDP", None), enzyme_offset=0.2, flip=True)
pw.step(None, "s6p", start=pw.anchor("f6p", "b") + (0.4, 0), end=pw.anchor("s6p", "t") + (0.4, 0))
pw.step("s6p", "suc", enzyme="SPP", side=("H₂O", "Pᵢ"), enzyme_offset=0.2)

# fructose 2,6-bisphosphate loop and allosteric control
pw.node("f26", (23.4, 8.0), "F2,6BP", token="drug", bold=True)
bio.arrow(ax, (21.7, 7.6), (19.4, 8.05), kind="inhibition", color=P.edge("negative"))
bio.label(ax, (21.6, 6.75), "PFK-2", size="tiny", bold=True, color=P.edge("enzyme"))
bio.arrow(ax, (20.0, 6.8), (22.6, 7.6), kind="process", color=P.muted())
bio.label(ax, (24.6, 11.6), "triose-P, 3-PGA ⊣ PFK-2\n(light: F2,6BP falls)", size="tiny", color=P.edge("negative"))
bio.label(ax, (24.6, 4.6), "Pᵢ, F6P → PFK-2\n(dark: F2,6BP rises)", size="tiny", color=P.edge("positive"))
bio.arrow(ax, (23.4, 10.95), (23.4, 8.6), kind="inhibition", color=P.edge("negative"))
bio.arrow(ax, (23.4, 5.25), (23.4, 7.4), kind="activation", color=P.edge("positive"), bg=ps.tint("cytoplasm", 0.5, 0.82))
bio.label(ax, (21.6, 2.9), "SPS: + glucose 6-P, − Pᵢ\n(also inactivated by phosphorylation)", size="tiny",
          color=P.muted())
# AGPase control in the stroma
bio.label(ax, (2.0, 6.0), "3-PGA activates,\nPᵢ inhibits\nAGPase", size="tiny", color=P.edge("positive"))
bio.arrow(ax, (2.6, 8.95), (5.7, 5.0), kind="activation", color=P.edge("positive"), bg=ps.tint("chloroplast", 0.5, 0.82))
