"""Entry of long-chain fatty acids into mitochondria: activation and the carnitine shuttle.

Cytosolic face of the outer membrane: long-chain acyl-CoA synthetase forms fatty acyl-CoA (fatty acid + CoA
+ ATP -> acyl-CoA + AMP + PPi; PPi hydrolysed). Carnitine palmitoyltransferase 1 (CPT1, outer membrane)
transfers the acyl group to carnitine; malonyl-CoA inhibits it. The carnitine/acylcarnitine translocase of
the inner membrane exchanges acylcarnitine (in) for carnitine (out). CPT2 on the matrix face of the inner
membrane transfers the acyl group to mitochondrial CoA. Cytosolic and mitochondrial CoA pools stay separate.
"""

import wikibio as bio
from wikibio import cellbio

P = bio.P
fig, ax = bio.canvas(22.0, 13.0, scale=0.42)
from matplotlib.patches import Rectangle

ax.add_patch(Rectangle((0, 0), 22, 4.0,
             facecolor=P.fill("matrix"), edgecolor="none", zorder=0))
bio.bilayer(ax, [(0, 8.4), (22, 8.4)])
bio.bilayer(ax, [(0, 4.2), (22, 4.2)])
bio.label(ax, (0.3, 12.5), "Cytosol", size="small", bold=True, ha="left", color=P.muted())
bio.label(ax, (0.3, 9.3), "Outer membrane", size="tiny", ha="left", color=P.muted())
bio.label(ax, (0.3, 6.3), "Intermembrane space", size="small", bold=True, ha="left", color=P.muted())
bio.label(ax, (0.3, 5.1), "Inner membrane", size="tiny", ha="left", color=P.muted())
bio.label(ax, (0.3, 0.5), "Mitochondrial matrix", size="small", bold=True, ha="left", color=P.edge("mitochondrion"))

# activation
bio.protein(ax, (4.0, 9.55), 2.6, 1.2, "enzyme", text="acyl-CoA\nsynthetase", size="tiny")
bio.label(ax, (1.4, 11.9), "fatty acid\n+ CoA + ATP", size="small", ha="left")
bio.arrow(ax, (2.6, 11.3), (3.4, 10.3), kind="process")
bio.label(ax, (6.2, 11.9), "fatty acyl-CoA", size="small", bold=True, ha="left")
bio.arrow(ax, (4.8, 10.3), (6.6, 11.4), kind="process")
bio.label(ax, (4.6, 11.0), "AMP + 2 Pᵢ", size="tiny", ha="left", color=P.muted())

# CPT1 in the outer membrane
bio.protein(ax, (10.5, 8.4), 2.0, 2.0, "receptor", text="CPT1")
bio.arrow(ax, (8.4, 11.6), (10.0, 9.55), kind="process", bend=0.15)
bio.label(ax, (11.9, 12.2), "CoA (cytosolic)", size="tiny", ha="left")
bio.arrow(ax, (10.9, 9.5), (11.8, 11.9), kind="process", bend=-0.1)
bio.label(ax, (8.3, 10.8), "carnitine", size="tiny", ha="right")
bio.label(ax, (10.5, 6.8), "acylcarnitine", size="small", bold=True)
bio.arrow(ax, (10.6, 7.35), (10.6, 7.05), kind="process")
bio.label(ax, (14.4, 11.3), "malonyl-CoA", size="small", bold=True, color=P.edge("negative"))
bio.arrow(ax, (13.9, 11.0), (11.6, 9.0), kind="inhibition", color=P.edge("negative"))
bio.label(ax, (14.4, 10.6), "(fatty acid synthesis, 7.1.26)", size="tiny", color=P.muted())

# translocase
cellbio.carrier(ax, 13.6, 4.2, open="out", token="channel")
bio.label(ax, (16.6, 3.3), "carnitine/acylcarnitine\ntranslocase (antiporter)", size="tiny", color=P.edge("channel"), bold=True, ha="left")
bio.arrow(ax, (11.6, 6.6), (13.2, 4.9), kind="process", bend=0.2)
bio.arrow(ax, (13.4, 3.5), (13.0, 2.3), kind="process")
bio.arrow(ax, (14.7, 2.5), (14.1, 3.5), kind="process", color=P.muted())
bio.arrow(ax, (14.1, 4.9), (16.0, 6.6), kind="process", bend=0.2, color=P.muted())
bio.label(ax, (16.2, 6.8), "carnitine", size="tiny", ha="left", color=P.muted())

# CPT2 on the matrix face
bio.protein(ax, (12.0, 1.6), 2.0, 1.4, "receptor", text="CPT2")
bio.label(ax, (8.0, 2.7), "CoA (mitochondrial)", size="tiny", ha="right")
bio.arrow(ax, (8.1, 2.5), (11.0, 1.9), kind="process")
bio.label(ax, (14.9, 2.2), "carnitine", size="tiny", ha="left", color=P.muted())
bio.label(ax, (18.4, 1.3), "fatty acyl-CoA → β oxidation", size="small", bold=True)
bio.arrow(ax, (13.1, 1.3), (15.4, 1.3), kind="process")
