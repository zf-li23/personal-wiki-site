"""Fatty acid synthesis is not beta oxidation in reverse: the two cycles side by side, in the same layout.

Left, beta oxidation (mitochondrial matrix; CoA thioesters; L-3-hydroxy intermediate; FAD and NAD+): acyl-CoA
dehydrogenase, enoyl-CoA hydratase, L-3-hydroxyacyl-CoA dehydrogenase and thiolase remove two carbons as
acetyl-CoA per turn. Right, fatty acid synthesis (cytosol in animals, plastid stroma in plants; acyl
carrier protein, ACP; D-3-hydroxy intermediate; NADPH): beta-ketoacyl-ACP synthase (KS) condenses the acyl
group with malonyl-ACP, releasing CO2; beta-ketoacyl-ACP reductase (KR), beta-hydroxyacyl-ACP dehydratase
(DH) and enoyl-ACP reductase (ER) reduce the keto group to CH2. The positions of the four intermediates are
the same in both cycles; the arrows run in opposite directions.
"""

from matplotlib.patches import FancyBboxPatch

import wikibio as bio
from wikibio import metabolism as M
from wikibio import photosynthesis as ps

P = bio.P
fig, ax = bio.canvas(33.4, 15.4, scale=0.4)
for (x0, x1), tok, txt in (((0.3, 16.4), "mitochondrion", "β oxidation: mitochondrial matrix"),
                           ((17.0, 33.1), "cytoplasm", "Fatty acid synthesis: cytosol (plants: plastid)")):
    ax.add_patch(FancyBboxPatch((x0, 0.3), x1 - x0, 14.8, boxstyle="round,pad=0,rounding_size=0.7",
                                facecolor=ps.tint(tok, 0.5, 0.82), edgecolor=P.edge(tok), lw=1.3, zorder=1))
    bio.label(ax, (x0 + 0.4, 14.65), txt, size="small", bold=True, ha="left", color=P.edge(tok))

r = 4.3
# --- beta oxidation (clockwise) --------------------------------------------------------------
c = (8.35, 7.4)
pw = M.Pathway(ax, size="small")
pos = M.ring(c, r, 4, start=90, clockwise=True)
for id, t, p in zip(("a", "e", "h", "k"),
                    ("Acyl-CoA (Cₙ)\nR–CH₂–CH₂–CO–SCoA", "trans-Δ²-Enoyl-CoA\nR–CH=CH–CO–SCoA",
                     "L-3-Hydroxyacyl-CoA\nR–CH(OH)–CH₂–CO–SCoA", "3-Ketoacyl-CoA\nR–CO–CH₂–CO–SCoA"), pos):
    pw.node(id, p, t, h=1.0, token="lipid" if id == "a" else "metabolite")
for a, b, e, side, rev in (("a", "e", "acyl-CoA DH", ("FAD", "FADH₂"), False),
                           ("e", "h", "hydratase", ("H₂O", None), True),
                           ("h", "k", "L-3-hydroxyacyl-\nCoA DH", ("NAD⁺", "NADH"), True),
                           ("k", "a", "thiolase", ("CoA", "acetyl-CoA"), True)):
    pw.step(a, b, enzyme=e, side=side, reversible=rev, enzyme_offset=0.55, side_reach=0.75, side_span=0.9,
            bend=M.cycle_bend(pw.nodes[a][0], pw.nodes[b][0], c, clockwise=True))
bio.label(ax, (c[0], c[1] + 0.45), "− C₂\nper turn", size="small", bold=True, color=P.edge("mitochondrion"))
bio.label(ax, (c[0], c[1] - 0.55), "oxidation", size="small", color=P.muted())

# --- fatty acid synthesis (counterclockwise: same positions, opposite direction) -------------
c2 = (25.05, 7.4)
pf = M.Pathway(ax, size="small")
pos2 = M.ring(c2, r, 4, start=90, clockwise=True)
for id, t, p in zip(("a", "e", "h", "k"),
                    ("Acyl-ACP (Cₙ₊₂)\nR–CH₂–CH₂–CO–S-ACP", "trans-Δ²-Enoyl-ACP\nR–CH=CH–CO–S-ACP",
                     "D-3-Hydroxyacyl-ACP\nR–CH(OH)–CH₂–CO–S-ACP", "3-Ketoacyl-ACP\nR–CO–CH₂–CO–S-ACP"), pos2):
    pf.node(id, p, t, h=1.0, token="lipid" if id == "a" else "metabolite")
for a, b, e, side in (("k", "h", "KR", ("NADPH", "NADP⁺")),
                      ("h", "e", "DH", (None, "H₂O")),
                      ("e", "a", "ER", ("NADPH", "NADP⁺"))):
    pf.step(a, b, enzyme=e, side=side, enzyme_offset=0.55, side_reach=0.75, side_span=0.9, flip=True,
            bend=M.cycle_bend(pf.nodes[a][0], pf.nodes[b][0], c2, clockwise=False))
pf.step("a", "k", enzyme="KS", side=("malonyl-ACP", "CO₂ + ACP"), enzyme_offset=0.55, side_reach=0.75,
        side_span=0.9, flip=True, bend=M.cycle_bend(pf.nodes["a"][0], pf.nodes["k"][0], c2, clockwise=False))
bio.label(ax, (c2[0], c2[1] + 0.45), "+ C₂\nper turn", size="small", bold=True, color=P.edge("cytoplasm"))
bio.label(ax, (c2[0], c2[1] - 0.55), "reduction", size="small", color=P.muted())
bio.label(ax, (25.05, 0.9), "acyl group moves from ACP to the KS cysteine before each condensation",
          size="tiny", color=P.muted())
