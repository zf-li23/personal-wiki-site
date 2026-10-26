"""The citric acid cycle in the mitochondrial matrix, with the pyruvate dehydrogenase complex feeding acetyl-CoA.

Eight steps clockwise from oxaloacetate. Irreversible steps in the cell (citrate synthase, isocitrate
dehydrogenase, alpha-ketoglutarate dehydrogenase) have one head, near-equilibrium steps two. Enzymes are
written inside the ring, co-substrates on arcs outside (the first joins, the second leaves).
"""

from matplotlib.patches import FancyBboxPatch

import wikibio as bio
from wikibio import metabolism as M

P = bio.P
fig, ax = bio.canvas(19.0, 19.6, scale=0.42)
ax.add_patch(FancyBboxPatch((0.3, 0.3), 18.4, 15.6, boxstyle="round,pad=0,rounding_size=1.0",
                            facecolor=P.fill("mitochondrion"), edgecolor=P.edge("mitochondrion"), lw=1.4, zorder=1))
ax.add_patch(FancyBboxPatch((0.52, 0.52), 17.96, 15.16, boxstyle="round,pad=0,rounding_size=0.85",
                            facecolor=P.fill("matrix"), edgecolor=P.edge("mitochondrion"), lw=1.1, zorder=1.1))
bio.label(ax, (0.9, 1.05), "Mitochondrial matrix", size="small", bold=True, ha="left", color=P.edge("mitochondrion"))
bio.label(ax, (0.5, 19.2), "Cytosol", size="small", bold=True, ha="left", color=P.muted())

pw = M.Pathway(ax, size="small")
c, r = (9.5, 7.0), 4.9
pw.node("pyr_c", (9.5, 18.6), "Pyruvate", bold=True)
pw.node("pyr", (9.5, 15.0), "Pyruvate")
pw.step("pyr_c", "pyr")
bio.label(ax, (9.85, 16.15), "MPC", size="tiny", bold=True, ha="left", color=P.edge("mitochondrion"))
pw.node("acoa", (9.5, 13.25), "Acetyl-CoA", bold=True, token="highlight")
pw.step("pyr", "acoa", enzyme="Pyruvate dehydrogenase\ncomplex", side=("NAD⁺ + CoA", "NADH + CO₂"), side_reach=0.5,
        enzyme_offset=0.25, side_span=0.9)

cyc = [("cit", "Citrate"), ("icit", "Isocitrate"), ("akg", "α-Ketoglutarate"), ("scoa", "Succinyl-CoA"),
       ("suc", "Succinate"), ("fum", "Fumarate"), ("mal", "L-Malate"), ("oaa", "Oxaloacetate")]
pos = M.ring(c, r, 8, start=67.5, clockwise=True)
for (id, text), p in zip(cyc, pos):
    pw.node(id, p, text)
tca = [
    ("oaa", "cit", "1 Citrate\nsynthase", ("H₂O", "CoA"), False, "C–C bond\n(Claisen/aldol)"),
    ("cit", "icit", "2 Aconitase", None, True, "isomerization\n(via cis-aconitate)"),
    ("icit", "akg", "3 Isocitrate\nDH", ("NAD⁺", "NADH + CO₂"), False, "oxidative\ndecarboxylation"),
    ("akg", "scoa", "4 α-KG DH\ncomplex", ("NAD⁺ + CoA", "NADH + CO₂"), False, "oxidative\ndecarboxylation"),
    ("scoa", "suc", "5 Succinyl-CoA\nsynthetase", ("GDP + Pᵢ", "GTP + CoA"), True, "substrate-level\nphosphorylation"),
    ("suc", "fum", "6 Succinate\nDH", ("FAD", "FADH₂"), True, "oxidation"),
    ("fum", "mal", "7 Fumarase", ("H₂O", None), True, "hydration"),
    ("mal", "oaa", "8 Malate\nDH", ("NAD⁺", "NADH + H⁺"), True, "oxidation"),
]
import numpy as np

for a, b, enz, side, rev, cls in tca:
    mid, tan, left = pw.step(a, b, enzyme=enz, side=side, reversible=rev, side_reach=0.55, side_span=0.75,
                             enzyme_offset=0.55, bend=M.cycle_bend(pw.nodes[a][0], pw.nodes[b][0], c, clockwise=True))
    if a == "oaa":
        bio.arrow(ax, pw.anchor("acoa", "b") + (0, -0.08), mid + (0, 0.04), kind="link", color=P.ink())
bio.label(ax, c, "Citric acid\ncycle", size="normal", bold=True, color=P.edge("mitochondrion"))
bio.label(ax, (c[0], c[1] - 1.1), "per acetyl-CoA:\n3 NADH, 1 FADH₂ (as QH₂),\n1 GTP, 2 CO₂", size="tiny", color=P.ink())
