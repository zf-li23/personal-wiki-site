"""Overall map of mammalian energy metabolism (a liver-like cell), condensed from 7.1.18-7.1.28.

Cytosol on the left and top, mitochondrial matrix in the box on the right. Black arrows are
degradative (catabolic) steps, blue arrows biosynthetic (anabolic) steps, including the
gluconeogenic bypasses. Gold pills: the three hubs (glucose 6-phosphate, pyruvate, acetyl-CoA).
Small arcs: the currencies made or used (ATP, NADH, FADH2, NADPH, CO2).
"""

from matplotlib.patches import FancyBboxPatch

import wikibio as bio
from wikibio import metabolism as M

P = bio.P
fig, ax = bio.canvas(31.0, 21.0, scale=0.42)
ANA = P.edge("channel")
CAT = P.ink()

# --- compartments ---------------------------------------------------------------------------------
bio.label(ax, (0.3, 20.6), "Cytosol", size="normal", bold=True, ha="left", color=P.muted())
mx0, my0, mx1, my1 = 14.9, 0.3, 30.8, 13.6
ax.add_patch(FancyBboxPatch((mx0, my0), mx1 - mx0, my1 - my0, boxstyle="round,pad=0,rounding_size=0.9",
                            facecolor=P.fill("mitochondrion"), edgecolor=P.edge("mitochondrion"), lw=1.4, zorder=1))
ax.add_patch(FancyBboxPatch((mx0 + 0.22, my0 + 0.22), mx1 - mx0 - 0.44, my1 - my0 - 0.44,
                            boxstyle="round,pad=0,rounding_size=0.75", facecolor=P.fill("matrix"),
                            edgecolor=P.edge("mitochondrion"), lw=1.0, zorder=1.1))
bio.label(ax, (mx1 - 0.6, my1 - 0.75), "Mitochondrial matrix", size="normal", bold=True, ha="right",
          color=P.edge("mitochondrion"))

pw = M.Pathway(ax, size="small")
HUB = dict(token="highlight", bold=True)

# --- carbohydrate column ----------------------------------------------------------------------------
pw.node("glc", (8.0, 19.4), "Glucose (blood)")
pw.node("glycogen", (2.6, 17.0), "Glycogen")
pw.node("g6p", (8.0, 17.0), "Glucose 6-phosphate", **HUB)
pw.node("tp", (8.0, 14.0), "Triose phosphates")
pw.node("pep", (8.0, 11.5), "Phosphoenolpyruvate")
pw.node("pyr", (8.0, 9.0), "Pyruvate", **HUB)
pw.node("lac", (2.6, 11.2), "Lactate")
pw.node("r5p", (14.0, 17.0), "Ribose 5-phosphate")
pw.node("nuc", (21.0, 17.0), "Nucleotides, DNA, RNA")

B = 0.16
pw.step("glc", "g6p", bend=B, enzyme="hexokinase (ATP)", enzyme_flip=True)
pw.step("g6p", "glc", bend=B, color=ANA, enzyme="glucose 6-phosphatase", enzyme_flip=True)
pw.step("glycogen", "g6p", bend=B, enzyme="phosphorylase (Pᵢ)", enzyme_flip=True)
pw.step("g6p", "glycogen", bend=B, color=ANA, enzyme="glycogen synthase (UTP)", enzyme_flip=True)
pw.step("g6p", "tp", bend=B, enzyme="PFK-1 (ATP)", enzyme_flip=True)
pw.step("tp", "g6p", bend=B, color=ANA, enzyme="FBPase-1", enzyme_flip=True)
pw.step("tp", "pep", bend=B, side=("NAD⁺", "NADH, ATP"))
pw.step("pep", "tp", bend=B, color=ANA)
pw.step("pep", "pyr", side=("ADP", "ATP"), enzyme="pyruvate kinase")
pw.step("pyr", "lac", reversible=True, enzyme="LDH (NADH)", enzyme_flip=True)
pw.step("g6p", "r5p", side=("NADP⁺", "NADPH"), enzyme="oxidative PPP")
pw.step("r5p", "nuc", color=ANA, side=("Gln, Gly, Asp, THF", None), enzyme="PRPP; purines, pyrimidines")

# --- lipids and nitrogen in the cytosol ---------------------------------------------------------------
pw.node("aa", (2.6, 7.6), "Amino acids")
pw.node("urea", (2.6, 5.0), "Urea")
pw.node("acoac", (12.4, 1.2), "Acetyl-CoA")
pw.node("mal", (8.2, 1.2), "Malonyl-CoA")
pw.node("fa", (4.0, 1.2), "Palmitate")
pw.node("tag", (4.0, 3.2), "Triacylglycerols")
pw.node("chol", (9.0, 4.2), "Cholesterol")
pw.node("fab", (11.6, 12.6), "Fatty acids (blood)")
pw.step("acoac", "mal", color=ANA, side=("ATP, CO₂", None), enzyme="ACC")
pw.step("mal", "fa", color=ANA, side=("NADPH", None), enzyme="FAS")
pw.step("fa", "tag", color=ANA, side=("glycerol 3-P", None), flip=True)
pw.step("acoac", "chol", color=ANA, enzyme="HMG-CoA reductase (NADPH)")
pw.step("aa", "urea", side=("NH₄⁺, HCO₃⁻", "3 ATP"), enzyme="urea cycle")
pw.step("aa", "pyr", dashed=True, enzyme="carbon skeletons")

# --- mitochondrial matrix ------------------------------------------------------------------------------
c, r = (21.8, 5.6), 2.6
cyc = [("oaa", "Oxaloacetate"), ("cit", "Citrate"), ("akg", "α-Ketoglutarate"), ("scoa", "Succinyl-CoA"),
       ("fum", "Fumarate")]
pos = M.ring(c, r, 5, start=90, clockwise=False)
for (id, t), p in zip(cyc, pos):
    pw.node(id, p, t)
sides = {("cit", "akg"): (None, "NADH, CO₂"), ("akg", "scoa"): (None, "NADH, CO₂"),
         ("scoa", "fum"): (None, "GTP, FADH₂"), ("fum", "oaa"): (None, "NADH")}
for k in range(5):
    a, b = cyc[k][0], cyc[(k + 1) % 5][0]
    pw.step(a, b, bend=M.cycle_bend(pw.nodes[a][0], pw.nodes[b][0], c, clockwise=False),
            side=sides.get((a, b)), flip=True, side_reach=0.45)
bio.label(ax, (c[0], c[1]), "Citric acid\ncycle", size="small", bold=True, color=P.muted())

pw.node("acoam", (18.6, 10.2), "Acetyl-CoA", **HUB)
pw.node("facoa", (18.6, 12.4), "Fatty acyl-CoA")
pw.node("kb", (25.6, 11.6), "Ketone bodies")
pw.step("pyr", "acoam", side=("NAD⁺", "NADH, CO₂"))
bio.label(ax, (10.9, 9.85), "PDH complex", size="tiny", bold=True, color=P.edge("enzyme"))
pw.step("fab", "facoa", enzyme="carnitine shuttle")
pw.step("facoa", "acoam", side=(None, "FADH₂, NADH"), enzyme="β oxidation", enzyme_flip=True)
pw.step("acoam", "kb", enzyme="ketogenesis (liver)")
pw.step("acoam", "cit", bend=-0.15)
# gluconeogenic route through oxaloacetate
pw.step("pyr", "oaa", color=ANA, bend=-0.07, enzyme="pyruvate carboxylase (ATP, CO₂)", enzyme_flip=True)
pw.step("oaa", "pep", color=ANA, bend=0.06, )
bio.label(ax, (17.4, 8.85), "PEPCK (GTP)", size="tiny", bold=True, color=P.edge("enzyme"))
# citrate shuttle to the cytosol
pw.step("cit", "acoac", color=ANA, bend=0.05, enzyme="citrate shuttle")

# respiratory chain and ATP synthase
bx, by, bw, bh = 28.4, 6.6, 3.6, 6.0
bio.box(ax, (bx, by), bw, bh, token="enzyme", text="Respiratory\nchain\n+\nATP synthase", size="small")
pw.node("atp", (bx, 1.6), "ATP", token="atp", bold=True)
bio.arrow(ax, (24.9, 6.4), (bx - bw / 2 - 0.1, 7.6), kind="process")
bio.label(ax, (25.4, 7.9), "NADH,\nFADH₂", size="tiny", bold=True)
bio.arrow(ax, (bx, by - bh / 2 - 0.05), (bx, 2.05), kind="process")
bio.label(ax, (bx + 0.25, by + bh / 2 + 0.45), "O₂ → H₂O", size="tiny", ha="center")

# legend
bio.arrow(ax, (16.0, 19.9), (17.6, 19.9), kind="process", color=CAT)
bio.label(ax, (17.9, 19.9), "catabolic", size="small", ha="left")
bio.arrow(ax, (20.4, 19.9), (22.0, 19.9), kind="process", color=ANA)
bio.label(ax, (22.3, 19.9), "anabolic, gluconeogenic", size="small", ha="left")
