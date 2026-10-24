# Central carbon metabolism: glycolysis in the cytosol (ten steps; from glyceraldehyde 3-phosphate on, every
# step runs twice per glucose), pyruvate import by the mitochondrial pyruvate carrier, oxidative
# decarboxylation by the pyruvate dehydrogenase complex and the citric acid cycle in the matrix.
# Irreversible steps have one head, near-equilibrium steps two; enzymes are written on the inner side,
# co-substrates on arcs on the outer side (first joins, second leaves).
from matplotlib.patches import FancyBboxPatch

import wikibio as bio
from wikibio import metabolism as M

fig, ax = bio.canvas(21.2, 27.2, scale=0.4)
P = bio.P

# --- mitochondrion: outer and inner membrane around the matrix -------------------------------------
mx0, my0, mx1, my1 = 7.2, 0.3, 20.9, 13.0
ax.add_patch(FancyBboxPatch((mx0, my0), mx1 - mx0, my1 - my0, boxstyle="round,pad=0,rounding_size=1.0",
                            facecolor=P.fill("mitochondrion"), edgecolor=P.edge("mitochondrion"), lw=1.4, zorder=1))
ax.add_patch(FancyBboxPatch((mx0 + 0.22, my0 + 0.22), mx1 - mx0 - 0.44, my1 - my0 - 0.44,
                            boxstyle="round,pad=0,rounding_size=0.85", facecolor=P.fill("matrix"),
                            edgecolor=P.edge("mitochondrion"), lw=1.1, zorder=1.1))
bio.label(ax, (mx0 + 0.6, my0 + 0.75), "Mitochondrial matrix", size="small", bold=True, ha="left", color=P.edge("mitochondrion"))
bio.label(ax, (0.4, 26.8), "Cytosol", size="small", bold=True, ha="left", color=P.muted())

pw = M.Pathway(ax, size="small")
X = 3.6
names = [("glc", "Glucose"), ("g6p", "Glucose 6-phosphate"), ("f6p", "Fructose 6-phosphate"),
         ("fbp", "Fructose 1,6-bisphosphate"), ("gap", "Glyceraldehyde 3-phosphate"), ("bpg", "1,3-Bisphosphoglycerate"),
         ("pg3", "3-Phosphoglycerate"), ("pg2", "2-Phosphoglycerate"), ("pep", "Phosphoenolpyruvate"), ("pyr", "Pyruvate")]
Y0, DY = 26.1, 1.62
for k, (id, text) in enumerate(names):
    pw.node(id, (X, Y0 - k * DY), text, bold=id in ("glc", "pyr"))
pw.node("dhap", (10.9, Y0 - 4 * DY), "Dihydroxyacetone\nphosphate", h=0.62)

steps = [
    ("glc", "g6p", "Hexokinase", ("ATP", "ADP"), False),
    ("g6p", "f6p", "Phosphoglucose\nisomerase", None, True),
    ("f6p", "fbp", "PFK-1", ("ATP", "ADP"), False),
    ("fbp", "gap", "Aldolase", None, True),
    ("gap", "bpg", "GAPDH", ("NAD⁺ + Pᵢ", "NADH + H⁺"), True),
    ("bpg", "pg3", "Phosphoglycerate\nkinase", ("ADP", "ATP"), True),
    ("pg3", "pg2", "Phosphoglycerate\nmutase", None, True),
    ("pg2", "pep", "Enolase", (None, "H₂O"), True),
    ("pep", "pyr", "Pyruvate kinase", ("ADP", "ATP"), False),
]
for a, b, enz, side, rev in steps:
    pw.step(a, b, enzyme=enz, side=side, reversible=rev, side_span=0.6)
pw.step("fbp", "dhap", bend=-0.08)
pw.step("dhap", "gap", enzyme="Triose phosphate\nisomerase", reversible=True, enzyme_flip=True, enzyme_offset=0.3)

# "x 2" bracket from GAP to pyruvate
yb0, yb1 = Y0 - 4 * DY - 0.85, Y0 - 9 * DY + 0.45
bx = 6.6
ax.plot([bx - 0.12, bx, bx, bx - 0.12], [yb0, yb0, yb1, yb1], color=P.muted(), lw=0.9)
bio.label(ax, (bx + 0.15, (yb0 + yb1) / 2), "×2 per\nglucose", size="small", color=P.muted(), ha="left")

# --- pyruvate import and pyruvate dehydrogenase ------------------------------------------------------
Yp = Y0 - 9 * DY
pw.node("pyr_m", (8.75, Yp), "Pyruvate", bold=True)
pw.step("pyr", "pyr_m")
bio.label(ax, (mx0 + 0.1, Yp + 0.32), "MPC", size="tiny", color=P.edge("mitochondrion"), bold=True)
pw.node("acoa", (14.3 - 4.25 * 0.3827, Yp), "Acetyl-CoA", bold=True, token="highlight")
pw.step("pyr_m", "acoa", enzyme="Pyruvate\ndehydrogenase", side=("NAD⁺ + CoA", "NADH + CO₂"), side_reach=0.5,
        enzyme_offset=0.22)

# --- citric acid cycle ---------------------------------------------------------------------------------
c, r = (14.3, 5.85), 4.25
cyc = [("cit", "Citrate"), ("icit", "Isocitrate"), ("akg", "α-Ketoglutarate"), ("scoa", "Succinyl-CoA"),
       ("suc", "Succinate"), ("fum", "Fumarate"), ("mal", "Malate"), ("oaa", "Oxaloacetate")]
pos = M.ring(c, r, 8, start=90, clockwise=True)
for (id, text), p in zip(cyc, pos):
    pw.node(id, p, text)
tca = [
    ("oaa", "cit", "Citrate\nsynthase", (None, "CoA"), False),
    ("cit", "icit", "Aconitase", None, True),
    ("icit", "akg", "Isocitrate\nDH", ("NAD⁺", "NADH + CO₂"), False),
    ("akg", "scoa", "α-KG DH", ("NAD⁺ + CoA", "NADH + CO₂"), False),
    ("scoa", "suc", "Succinyl-CoA\nsynthetase", ("GDP + Pᵢ", "GTP + CoA"), True),
    ("suc", "fum", "Succinate\nDH", ("FAD", "FADH₂"), True),
    ("fum", "mal", "Fumarase", ("H₂O", None), True),
    ("mal", "oaa", "Malate\nDH", ("NAD⁺", "NADH + H⁺"), True),
]
for a, b, enz, side, rev in tca:
    mid, tan, left = pw.step(a, b, enzyme=enz, side=side, reversible=rev, side_reach=0.6 if a == "oaa" else 0.5,
                             side_span=1.1 if a == "oaa" else 0.7, enzyme_offset=0.85 if a == "scoa" else 0.6,
                             bend=M.cycle_bend(pw.nodes[a][0], pw.nodes[b][0], c, clockwise=True))
    if a == "oaa":
        bio.arrow(ax, pw.anchor("acoa", "b") + (0, -0.08), mid + (0, 0.04), kind="link", color=P.ink())
bio.label(ax, c, "Citric acid\ncycle", size="normal", bold=True, color=P.edge("mitochondrion"))

# --- yield ----------------------------------------------------------------------------------------------
bio.label(ax, (0.4, 6.9), "Per glucose", size="small", bold=True, ha="left")
rows = ["Glycolysis: 2 ATP (net), 2 NADH", "PDH (×2): 2 NADH, 2 CO₂", "Cycle (×2): 6 NADH, 2 FADH₂,",
        "    2 GTP, 4 CO₂"]
for k, t in enumerate(rows):
    bio.label(ax, (0.4, 6.35 - k * 0.5), t, size="small", ha="left")
