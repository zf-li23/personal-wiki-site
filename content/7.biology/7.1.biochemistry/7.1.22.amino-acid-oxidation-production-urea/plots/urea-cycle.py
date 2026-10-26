"""The urea cycle in a hepatocyte and its link to the citric acid cycle (the "Krebs bicycle").
Matrix: carbamoyl phosphate synthetase I (CPS I) condenses NH4+ and bicarbonate with 2 ATP (activator
N-acetylglutamate); ornithine transcarbamoylase (OTC) forms citrulline, which is exported in exchange for
ornithine. Cytosol: argininosuccinate synthetase (ASS) joins citrulline and aspartate (the second nitrogen)
through citrullyl-AMP (ATP -> AMP + PPi); argininosuccinate lyase (ASL) releases fumarate and arginine;
arginase hydrolyzes arginine to urea and ornithine. Fumarate is hydrated to malate and oxidized to
oxaloacetate (NADH), which is transaminated back to aspartate: the aspartate-argininosuccinate shunt."""

from matplotlib.patches import FancyBboxPatch

import wikibio as bio
from wikibio import metabolism as M

P = bio.P
fig, ax = bio.canvas(20.6, 13.6)
mx0, my0, mx1, my1 = 0.3, 0.4, 7.3, 13.0
ax.add_patch(FancyBboxPatch((mx0, my0), mx1 - mx0, my1 - my0, boxstyle="round,pad=0,rounding_size=0.8",
                            facecolor=P.fill("mitochondrion"), edgecolor=P.edge("mitochondrion"), lw=1.4, zorder=1))
ax.add_patch(FancyBboxPatch((mx0 + 0.22, my0 + 0.22), mx1 - mx0 - 0.44, my1 - my0 - 0.44,
                            boxstyle="round,pad=0,rounding_size=0.65", facecolor=P.fill("matrix"),
                            edgecolor=P.edge("mitochondrion"), lw=1.1, zorder=1.1))
bio.label(ax, (mx0 + 0.6, my0 + 0.7), "Mitochondrial matrix", size="small", bold=True, ha="left", color=P.edge("mitochondrion"))
bio.label(ax, (8.2, 13.1), "Cytosol", size="small", bold=True, ha="left", color=P.muted())

pw = M.Pathway(ax, size="small")
# matrix
pw.node("nh4", (2.6, 11.6), "NH₄⁺ + HCO₃⁻")
pw.node("cp", (2.6, 8.3), "Carbamoyl phosphate", bold=True)
pw.node("orn_m", (5.4, 4.6), "Ornithine")
pw.node("cit_m", (5.4, 10.3), "Citrulline")
pw.node("nag", (5.1, 12.1), "N-Acetylglutamate", token="highlight", size="tiny")
mid, tan, left = pw.step("nh4", "cp", enzyme="CPS I", side=("2 ATP", "2 ADP + Pᵢ"), side_reach=0.55, enzyme_flip=True)
bio.arrow(ax, pw.anchor("nag", "b"), (mid[0] + 0.12, mid[1] + 0.35), kind="activation", color=P.edge("positive"),
          bg=P.fill("matrix"), bend=-0.25, shrink=0.05)
m2, _, _ = pw.step("orn_m", "cit_m", enzyme="OTC", side=(None, "Pᵢ"), side_reach=0.55)
bio.arrow(ax, pw.anchor("cp", "r"), (m2[0] - 0.05, m2[1]), kind="link", color=P.ink(), bend=0.15)

# cytosol: the rest of the cycle
pw.node("cit_c", (9.8, 10.3), "Citrulline")
pw.node("as", (14.2, 10.3), "Argininosuccinate", bold=True)
pw.node("arg", (14.2, 4.6), "Arginine")
pw.node("orn_c", (9.8, 4.6), "Ornithine")
pw.step("cit_m", "cit_c", enzyme="ORNT1", enzyme_size="tiny")
pw.step("orn_c", "orn_m")
m3, _, _ = pw.step("cit_c", "as", enzyme="ASS", side=("ATP", "AMP + PPᵢ"), side_reach=0.55, flip=True)
pw.step("as", "arg", enzyme="ASL", reversible=True, enzyme_flip=True)
m4, _, _ = pw.step("arg", "orn_c", enzyme="arginase", side=("H₂O", None), side_reach=0.55, flip=True)
pw.node("urea", (12.0, 2.7), "Urea", bold=True, token="positive")
bio.arrow(ax, (m4[0], m4[1] - 0.15), pw.anchor("urea", "t"), kind="process", color=P.ink(), shrink=0.05)
bio.label(ax, (12.0, 7.5), "Urea\ncycle", size="normal", bold=True, color=P.muted())

# aspartate-argininosuccinate shunt
X = 18.4
pw.node("fum", (X, 4.6), "Fumarate")
pw.node("mal", (X, 6.9), "Malate")
pw.node("oaa", (X, 9.2), "Oxaloacetate")
pw.node("asp", (X, 11.6), "Aspartate", bold=True)
bio.arrow(ax, (14.2, 7.45), pw.anchor("fum", "l"), kind="process", color=P.ink(), bend=0.12, shrink=0.05)
pw.step("fum", "mal", enzyme="fumarase", side=("H₂O", None), reversible=True, side_reach=0.45)
pw.step("mal", "oaa", enzyme="MDH", side=("NAD⁺", "NADH"), reversible=True, side_reach=0.45)
pw.step("oaa", "asp", enzyme="AAT", side=("Glu", "α-KG"), reversible=True, side_reach=0.45)
bio.arrow(ax, pw.anchor("asp", "l"), (m3[0] + 0.5, m3[1] + 0.1), kind="process", color=P.ink(), bend=-0.2, shrink=0.05)
bio.label(ax, (X, 3.9), "aspartate–argininosuccinate\nshunt (malate also enters\nthe citric acid cycle)", size="tiny",
          color=P.muted(), va="top")
bio.label(ax, (15.4, 1.3), "net: 2 NH₄⁺ (one via Asp) + HCO₃⁻ + 3 ATP\n→ urea + 2 ADP + AMP + 4 Pᵢ\n(4 high-energy phosphates)",
          size="tiny", color=P.ink())
