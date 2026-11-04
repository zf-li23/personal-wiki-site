# From lipid A to inflammation: LBP, CD14, TLR4-MD-2, NF-kB and the cytokines; potency set by acylation.
import numpy as np
from matplotlib.patches import Rectangle

import wikibio as bio
from wikibio import microbio as M

P = bio.P
fig, ax = bio.canvas(19.0, 9.0)
bio.label(ax, (0.3, 8.75), "Recognition of lipid A and the inflammatory response", size="title",
          bold=True, ha="left")

# ---------------------------------------------------------------- left: the bacterial surface
ax.add_patch(Rectangle((0.3, 0.4), 4.4, 7.9, facecolor=P.fill("extracellular"), edgecolor="none", zorder=0))
env = M.envelope(ax, 0.6, 4.4, y=1.9, kind="gram-", top=4.6)
bio.label(ax, (2.5, 0.7), "Gram-negative outer membrane", size="small", bold=True)
bio.callout(ax, (1.6, env["om_hi"] + 0.55), (2.6, 6.0),
            "lipopolysaccharide:\nO-antigen, core, lipid A")
bio.label(ax, (2.5, 7.4), "released when cells divide,\nlyse, or are killed by an antibiotic\nor by complement",
          size="tiny", color=P.muted())
bio.arrow(ax, (4.3, 5.3), (5.6, 5.0), kind="process")

# ---------------------------------------------------------------- middle: the host cell
X = 5.9
ax.add_patch(Rectangle((X, 0.4), 7.0, 7.9, facecolor=P.fill("cytoplasm"), edgecolor="none", zorder=0))
bio.bilayer(ax, [(X, 5.6), (X + 7.0, 5.6)], zorder=4)
bio.label(ax, (X + 0.15, 7.4), "macrophage, monocyte, endothelial cell", size="tiny", ha="left", color=P.muted())

bio.molecule(ax, (X + 0.9, 6.5), token="lipid", text="LBP", r=0.33, size="tiny")
bio.molecule(ax, (X + 2.1, 6.3), token="receptor", text="CD14", r=0.36, size="tiny")
bio.arrow(ax, (X + 1.3, 6.4), (X + 1.7, 6.35), kind="process")
bio.arrow(ax, (X + 2.5, 6.15), (X + 3.2, 5.95), kind="process")
bio.receptor(ax, X + 3.6, 5.6, kind="rtk", token="channel", text=None)
bio.receptor(ax, X + 4.4, 5.6, kind="rtk", token="channel", text=None)
bio.label(ax, (X + 4.3, 6.9), "TLR4–MD-2 dimer", size="small", bold=True)
bio.label(ax, (X + 4.3, 6.5), "MD-2 holds the acyl chains", size="tiny", color=P.muted())

bio.box(ax, (X + 4.0, 4.5), 3.0, 0.7, token="protein", radius=0.15)
bio.label(ax, (X + 4.0, 4.5), "MyD88 and TRIF", size="tiny", color=P.on_fill())
bio.arrow(ax, (X + 4.0, 5.2), (X + 4.0, 4.9), kind="process")
bio.box(ax, (X + 4.0, 3.4), 3.0, 0.7, token="dna2", radius=0.15)
bio.label(ax, (X + 4.0, 3.4), "NF-κB, IRF3", size="tiny", color=P.on_fill())
bio.arrow(ax, (X + 4.0, 4.1), (X + 4.0, 3.8), kind="process")

bio.box(ax, (X + 4.0, 2.1), 3.4, 1.0, token="nucleus", radius=0.2)
bio.label(ax, (X + 4.0, 2.35), "nucleus", size="tiny", bold=True, color=P.on_fill())
bio.label(ax, (X + 4.0, 1.95), "TNF-α, IL-1β, IL-6,\ntype I interferons", size="tiny", color=P.on_fill())
bio.arrow(ax, (X + 4.0, 3.0), (X + 4.0, 2.65), kind="process")

# the cytosolic route
bio.box(ax, (X + 1.3, 3.4), 2.1, 0.7, token="enzyme", radius=0.15)
bio.label(ax, (X + 1.3, 3.4), "caspase-4/5", size="tiny", color=P.on_fill())
bio.label(ax, (X + 1.3, 4.1), "cytosolic LPS", size="tiny", color=P.muted())
bio.arrow(ax, (X + 1.3, 5.2), (X + 1.3, 3.8), kind="process", dashed=True)
bio.arrow(ax, (X + 1.3, 3.0), (X + 1.3, 2.6), kind="process")
bio.label(ax, (X + 1.3, 2.35), "pyroptosis", size="tiny")

# ---------------------------------------------------------------- right: local and systemic outcome
X2 = 13.2
bio.arrow(ax, (12.7, 4.3), (13.3, 4.3), kind="process")
bio.box(ax, (X2 + 2.6, 6.1), 5.0, 2.0, token="positive", radius=0.2)
bio.label(ax, (X2 + 2.6, 6.75), "Local: a useful response", size="small", bold=True, color=P.on_fill())
bio.label(ax, (X2 + 2.6, 6.0), "vasodilation, leaky venules,\nneutrophils recruited, fever;\nthe infection is contained",
          size="tiny", color=P.on_fill())
bio.box(ax, (X2 + 2.6, 3.4), 5.0, 2.2, token="negative", radius=0.2)
bio.label(ax, (X2 + 2.6, 4.2), "Systemic: the disease", size="small", bold=True, color=P.on_fill())
bio.label(ax, (X2 + 2.6, 3.3), "widespread vasodilation and\ncapillary leak, coagulation,\nfalling blood pressure:\nseptic shock",
          size="tiny", color=P.on_fill())
bio.label(ax, (X2 + 2.6, 1.6), "Potency is set by lipid A", size="small", bold=True)
bio.label(ax, (X2 + 2.6, 0.95), "six acyl chains ($\\it{Escherichia\\ coli}$): strong agonist\n"
                                "four chains ($\\it{Yersinia\\ pestis}$ at 37 °C): nearly silent\n"
                                "aminoarabinose added: weak, and resists cationic peptides",
          size="tiny", color=P.muted())
