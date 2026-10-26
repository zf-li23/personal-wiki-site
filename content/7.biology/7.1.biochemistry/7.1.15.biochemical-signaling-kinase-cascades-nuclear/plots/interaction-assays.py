"""Three assays for protein-protein interactions in living cells.

A: yeast two-hybrid. The bait X is fused to the DNA-binding domain (DBD) of Gal4, which binds the
Gal4 upstream activating sequence (UAS) in front of reporter genes; the prey Y (one protein or a cDNA
library) is fused to a transcription activation domain (AD). Only if X binds Y is the AD brought to the
promoter, where it recruits the transcription machinery: the reporter genes (for example HIS3, ADE2 or
URA3, selected by growth without histidine, adenine or uracil; lacZ, giving blue colonies on X-gal) are
expressed. Plasmids carrying bait and prey are maintained by selection for TRP1 and LEU2.
B: bimolecular fluorescence complementation (BiFC). Proteins A and B are fused to the N- and C-terminal
halves of YFP (YN, YC), neither of which fluoresces; if A binds B, the halves fold into a fluorescent
YFP (an essentially irreversible event), revealing where in the cell the interaction occurs.
C: luciferase complementation imaging (LCI). A and B are fused to the N- and C-terminal halves of
firefly luciferase (NLuc, CLuc); interaction reconstitutes the enzyme, which oxidizes luciferin with
ATP and O2 and emits light. Complementation is reversible, so the signal follows the interaction
quantitatively.
"""

import wikibio as bio
from wikibio import genetics as G

P = bio.P
fig, ax = bio.canvas(26.0, 8.4)

# --- A: yeast two-hybrid -------------------------------------------------------------
bio.panel(ax, "A", (0.1, 8.3))
bio.label(ax, (5.2, 8.0), "Yeast two-hybrid", size="normal", bold=True)
gl = G.construct(ax, 1.0, 2.2, [("operator", "UAS", "neutral"), ("promoter", None), {"kind": "cds", "text": "HIS3, lacZ", "token": "positive", "width": 3.2, "italic": True},
                                ("terminator", None)], unit=0.55)
uas = gl[0]
bio.protein(ax, (uas["centre"], 2.85), 1.2, 0.8, "receptor", text="DBD", size="tiny")
x0 = uas["centre"]
bio.protein(ax, (x0 + 0.2, 3.95), 1.1, 0.85, "drug", text="X", size="small")
bio.protein(ax, (x0 + 1.4, 4.3), 1.1, 0.85, "metabolite", text="Y", size="small")
bio.protein(ax, (x0 + 2.6, 3.95), 1.2, 0.8, "enzyme", text="AD", size="tiny")
bio.protein(ax, (x0 + 4.3, 3.1), 1.9, 1.0, "neutral", text="RNA pol II", size="tiny")
bio.arrow(ax, (x0 + 3.2, 3.7), (x0 + 3.55, 3.45), kind="activation")
bio.label(ax, (x0 + 0.2, 4.75), "bait", size="tiny", color=P.muted())
bio.label(ax, (x0 + 1.4, 5.1), "prey", size="tiny", color=P.muted())
bio.label(ax, (3.6, 1.55), "reporter genes", size="tiny", color=P.muted())
bio.label(ax, (5.2, 1.0), "growth on −His (−Ade, −Ura) medium; blue colonies on X-gal", size="tiny")
bio.label(ax, (5.2, 0.5), "only when X binds Y", size="tiny", bold=True)

# --- B: BiFC -------------------------------------------------------------------------
bio.panel(ax, "B", (10.4, 8.3))
bio.label(ax, (14.2, 8.0), "BiFC", size="normal", bold=True)
bio.protein(ax, (12.0, 6.0), 1.0, 0.8, "drug", text="A", size="small")
bio.protein(ax, (12.0, 5.05), 0.9, 0.6, "neutral", text="YN", size="tiny")
bio.protein(ax, (13.6, 6.0), 1.0, 0.8, "metabolite", text="B", size="small")
bio.protein(ax, (13.6, 5.05), 0.9, 0.6, "neutral", text="YC", size="tiny")
bio.label(ax, (12.8, 4.3), "no fluorescence", size="tiny", color=P.muted())
bio.arrow(ax, (14.5, 5.5), (15.5, 5.5), kind="process")
bio.protein(ax, (16.4, 6.0), 1.0, 0.8, "drug", text="A", size="small")
bio.protein(ax, (17.3, 6.0), 1.0, 0.8, "metabolite", text="B", size="small")
bio.protein(ax, (16.85, 4.95), 1.6, 0.8, "positive", text="YFP", size="small")
bio.arrow(ax, (17.75, 4.6), (18.4, 4.0), kind="process", color=P.edge("positive"), head=0.16)
bio.label(ax, (18.0, 3.65), "yellow fluorescence", size="tiny", color=P.edge("positive"), ha="left")
bio.label(ax, (14.6, 2.6), "halves fold together when A and B interact;", size="tiny")
bio.label(ax, (14.6, 2.1), "reports location in the cell (irreversible)", size="tiny")

# --- C: luciferase complementation ---------------------------------------------------
bio.panel(ax, "C", (19.6, 8.3))
bio.label(ax, (22.8, 8.0), "Luciferase complementation", size="normal", bold=True)
bio.protein(ax, (21.2, 6.0), 1.0, 0.8, "drug", text="A", size="small")
bio.protein(ax, (21.2, 5.05), 1.0, 0.6, "highlight", text="NLuc", size="tiny")
bio.protein(ax, (22.5, 6.0), 1.0, 0.8, "metabolite", text="B", size="small")
bio.protein(ax, (22.5, 5.05), 1.0, 0.6, "highlight", text="CLuc", size="tiny")
bio.arrow(ax, (23.1, 5.5), (23.9, 5.5), kind="process")
bio.protein(ax, (24.6, 6.05), 0.9, 0.75, "drug", text="A", size="tiny")
bio.protein(ax, (25.4, 6.05), 0.9, 0.75, "metabolite", text="B", size="tiny")
bio.protein(ax, (25.0, 5.05), 1.5, 0.75, "highlight", text="luciferase", size="tiny")
bio.label(ax, (23.0, 3.6), "luciferin + ATP + O₂ → light (560 nm)", size="tiny")
bio.label(ax, (23.0, 2.6), "reversible: signal follows the", size="tiny")
bio.label(ax, (23.0, 2.1), "interaction (e.g. in tobacco leaves)", size="tiny")
