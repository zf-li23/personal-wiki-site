"""Opposing pathways of glycolysis and gluconeogenesis in the liver.

The seven near-equilibrium steps are shared (double heads, centre column). At the three
irreversible steps glycolysis (left arcs) and gluconeogenesis (right arcs) use different enzymes:
hexokinase / glucose 6-phosphatase (in the ER lumen), PFK-1 / FBPase-1, and pyruvate kinase /
the pyruvate carboxylase + PEP carboxykinase bypass, which passes through the mitochondrial matrix
(pyruvate -> oxaloacetate -> malate, exported, reoxidized to oxaloacetate in the cytosol).
The dashed branch is the second route, used when lactate is the precursor: mitochondrial PEPCK.
Entry points of lactate, alanine and glycerol are shown on the left.
"""

from matplotlib.patches import FancyBboxPatch

import wikibio as bio
from wikibio import metabolism as M

P = bio.P
fig, ax = bio.canvas(21.0, 23.6, scale=0.42)

GLY = P.edge("drug")      # glycolysis-specific enzymes
GNG = P.edge("channel")   # gluconeogenesis-specific enzymes

# --- compartments ----------------------------------------------------------------------------------
bio.label(ax, (0.4, 23.15), "Cytosol", size="small", bold=True, ha="left", color=P.muted())
# ER lumen around the glucose 6-phosphatase arc
ax.add_patch(FancyBboxPatch((8.45, 20.85), 6.3, 1.0, boxstyle="round,pad=0,rounding_size=0.5",
                            fill=False, edgecolor=P.edge("er"), lw=1.1, ls=(0, (3, 2)), zorder=1))
bio.label(ax, (14.55, 21.05), "ER lumen", size="tiny", bold=True, ha="right", color=P.edge("er"))
# mitochondrion at the bottom
mx0, my0, mx1, my1 = 4.6, 0.3, 20.7, 5.0
ax.add_patch(FancyBboxPatch((mx0, my0), mx1 - mx0, my1 - my0, boxstyle="round,pad=0,rounding_size=0.8",
                            facecolor=P.fill("mitochondrion"), edgecolor=P.edge("mitochondrion"), lw=1.3, zorder=1))
ax.add_patch(FancyBboxPatch((mx0 + 0.2, my0 + 0.2), mx1 - mx0 - 0.4, my1 - my0 - 0.4,
                            boxstyle="round,pad=0,rounding_size=0.65", facecolor=P.fill("matrix"),
                            edgecolor=P.edge("mitochondrion"), lw=1.0, zorder=1.1))
bio.label(ax, (mx1 - 0.5, my0 + 0.65), "Mitochondrial matrix", size="small", bold=True, ha="right",
          color=P.edge("mitochondrion"))

pw = M.Pathway(ax, size="small")
X, Y0, DY = 7.6, 22.2, 1.72
names = [("glc", "Glucose"), ("g6p", "Glucose 6-phosphate"), ("f6p", "Fructose 6-phosphate"),
         ("fbp", "Fructose 1,6-bisphosphate"), ("gap", "Glyceraldehyde 3-phosphate"),
         ("bpg", "1,3-Bisphosphoglycerate"), ("pg3", "3-Phosphoglycerate"), ("pg2", "2-Phosphoglycerate"),
         ("pep", "Phosphoenolpyruvate"), ("pyr", "Pyruvate")]
for k, (id, text) in enumerate(names):
    pw.node(id, (X, Y0 - k * DY), text, bold=id in ("glc", "pyr"))
pw.node("dhap", (X - 5.2, Y0 - 3.5 * DY), "Dihydroxyacetone\nphosphate", h=0.62)

# shared near-equilibrium steps (from step 6 on, twice per glucose)
for a, b, side, flip in [("g6p", "f6p", None, False), ("fbp", "gap", None, False),
                         ("gap", "bpg", ("NAD⁺ + Pᵢ", "NADH + H⁺"), False),
                         ("bpg", "pg3", ("ADP", "ATP"), False), ("pg3", "pg2", None, False),
                         ("pg2", "pep", (None, "H₂O"), False)]:
    pw.step(a, b, side=side, reversible=True, side_span=0.55, flip=flip)
pw.step("fbp", "dhap", bend=0.08, reversible=True)
pw.step("dhap", "gap", reversible=True)

# bypass pairs: glycolysis on the left, gluconeogenesis on the right (bulge of about 1 unit)
BEND = -1.15


def bypass(a, b, name, cosub, color, right):
    mid = (pw.nodes[a][0] + pw.nodes[b][0]) / 2
    sgn, ha = (1, "left") if right else (-1, "right")
    if right:
        pw.step(b, a, bend=BEND, color=color)
    else:
        pw.step(a, b, bend=BEND, color=color)
    bio.label(ax, (mid[0] + sgn * 1.25, mid[1] + 0.2), name, size="tiny", bold=True, color=color, ha=ha)
    bio.label(ax, (mid[0] + sgn * 1.25, mid[1] - 0.22), cosub, size="tiny", ha=ha)


bypass("glc", "g6p", "Hexokinase", "ATP → ADP", GLY, False)
bypass("glc", "g6p", "Glucose 6-phosphatase", "H₂O → Pᵢ", GNG, True)
bypass("f6p", "fbp", "PFK-1", "ATP → ADP", GLY, False)
bypass("f6p", "fbp", "FBPase-1", "H₂O → Pᵢ", GNG, True)
bypass("pep", "pyr", "Pyruvate kinase", "ADP → ATP", GLY, False)

# --- the pyruvate -> PEP bypass through the mitochondrion -------------------------------------------
gn = M.Pathway(ax, size="small", enzyme_color=GNG)
gn.nodes = pw.nodes
Ym = 3.35
pw.node("pyr_m", (X, Ym), "Pyruvate")
pw.node("oaa_m", (12.3, Ym), "Oxaloacetate")
pw.node("mal_m", (17.4, Ym), "Malate")
pw.node("mal_c", (17.4, Y0 - 8.5 * DY), "Malate")
pw.node("oaa_c", (17.4, Y0 - 8 * DY + 0.95), "Oxaloacetate")
gn.step("pyr", "pyr_m", color=GNG)
bio.label(ax, (X + 0.35, my1 + 0.25), "MPC", size="tiny", bold=True, ha="left", color=P.edge("mitochondrion"))
gn.step("pyr_m", "oaa_m", enzyme="Pyruvate\ncarboxylase", side=("ATP + HCO₃⁻", "ADP + Pᵢ"), color=GNG,
        side_span=0.8, enzyme_offset=0.2)
gn.step("oaa_m", "mal_m", enzyme="Malate DH", side=("NADH + H⁺", "NAD⁺"), color=GNG, reversible=True,
        side_span=0.7, enzyme_offset=0.2)
gn.step("mal_m", "mal_c", color=GNG, flip=True)
bio.label(ax, (17.75, my1 + 0.25), "malate–α-KG\ncarrier", size="tiny", ha="left", color=P.edge("mitochondrion"))
gn.step("mal_c", "oaa_c", enzyme="Malate DH", side=("NAD⁺", "NADH + H⁺"), color=GNG, reversible=True,
        flip=True, side_span=0.5, side_reach=0.5, enzyme_offset=0.2)
gn.step("oaa_c", "pep", enzyme="PEP carboxykinase", side=("GTP", "GDP + CO₂"), color=GNG, flip=True,
        side_span=0.8, enzyme_offset=0.18)

# second route (lactate as precursor): mitochondrial PEPCK, PEP exported
pw.node("pep_m", (12.3, 1.35), "PEP")
gn.step("oaa_m", "pep_m", enzyme="PEPCK (mitochondrial)", color=GNG, dashed=True, enzyme_flip=True,
        enzyme_offset=0.35)
pw.step(None, None, start=(13.0, 1.35), end=(19.9, 1.35), color=GNG, dashed=True)
pw.step(None, None, start=(19.9, 1.35), end=(19.9, Y0 - 8 * DY + 0.95), color=GNG, dashed=True)
pw.step(None, None, start=(19.9, Y0 - 8 * DY + 0.95), end=(18.85, Y0 - 8 * DY + 0.95), color=GNG, dashed=True)
bio.label(ax, (20.15, 7.5), "lactate route", size="tiny", rotation=90, color=GNG)

# --- precursors entering on the left -----------------------------------------------------------------
pw.node("lac", (2.6, Y0 - 9 * DY - 2.0), "Lactate")
pw.step("lac", "pyr", enzyme="LDH\n(NAD⁺ → NADH)", reversible=True, enzyme_offset=0.12, enzyme_flip=True)
pw.node("ala", (2.6, Y0 - 9 * DY - 0.25), "Alanine")
pw.step("ala", "pyr", enzyme="ALT", reversible=True, enzyme_offset=0.12, enzyme_flip=True)
pw.node("glyc", (2.4, Y0 - 5.2 * DY), "Glycerol")
pw.step("glyc", "dhap", enzyme="glycerol kinase,\nG3P DH", enzyme_offset=0.12)

# legend
bio.label(ax, (0.4, 22.3), "glycolysis only", size="tiny", bold=True, ha="left", color=GLY)
bio.label(ax, (0.4, 21.8), "gluconeogenesis only", size="tiny", bold=True, ha="left", color=GNG)
bio.label(ax, (0.4, 21.3), "shared (near equilibrium)", size="tiny", bold=True, ha="left", color=P.ink())
