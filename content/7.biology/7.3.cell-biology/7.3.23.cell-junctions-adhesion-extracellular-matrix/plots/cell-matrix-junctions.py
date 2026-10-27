"""Cell-matrix junctions and the basal lamina (schematic, not to scale).

A: a focal adhesion of a fibroblast on fibronectin. Activated (extended, open) integrins bind fibronectin
fibrils outside; inside, talin binds the beta-integrin tail with its head and actin with its long rod,
kindlin binds the tail next to it, vinculin reinforces the talin-actin link, and focal adhesion kinase (FAK)
and paxillin signal; the actin filaments of a stress fiber end on the plaque. B: a hemidesmosome of a basal
keratinocyte: alpha6beta4 integrin and type XVII collagen (BP180) bind laminin-332 in the basal lamina; the
long cytoplasmic tail of beta4 binds plectin and BP230 in the plaque, into which keratin filaments loop.
C: the basal lamina in more detail: a polymer of laminin (cross-shaped heterotrimers, linked to cell-surface
receptors through their LG domains), a network of type IV collagen beneath, nidogen bridging the two, and the
heparan sulfate proteoglycan perlecan.
"""

import wikibio as bio
from wikibio import junctions as J

P = bio.P
fig, ax = bio.canvas(29.0, 11.4)

bio.panel(ax, "A", (0.1, 11.3))
f = J.focal_adhesion(ax, 0.8, 8.4, 5.4, integrins=5)
bio.callout(ax, f["talin"], (2.0, 9.6), "Talin")
bio.callout(ax, f["vinculin"], (4.4, 9.9), "Vinculin")
bio.callout(ax, f["fak"], (0.6, 8.1), "FAK, paxillin")
bio.callout(ax, f["kindlin"], (6.6, 9.0), "Kindlin")
bio.callout(ax, f["actin"], (10.6, 9.4), "Stress fiber (actin)")
bio.callout(ax, f["integrin"], (9.6, 4.4), "Integrin (αβ)")
bio.callout(ax, f["fibronectin"], (1.4, 2.6), "Fibronectin fibril")
bio.label(ax, (8.6, 6.0), "Cytoplasm", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (8.6, 3.7), "Extracellular", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (5.0, 1.6), "Focal adhesion", size="small", bold=True)

bio.panel(ax, "B", (13.2, 11.3))
h = J.hemidesmosome(ax, 14.0, 20.6, 5.0)
bio.callout(ax, h["plaque"], (21.4, 6.3), "Plectin, BP230")
bio.callout(ax, h["integrin"], (21.4, 4.3), "α6β4 integrin")
bio.callout(ax, h["col17"], (13.3, 4.0), "Type XVII collagen")
bio.callout(ax, h["if"], (21.4, 8.7), "Keratin filaments")
bio.callout(ax, h["lamina"], (13.3, 2.7), "Basal lamina (laminin-332)")
bio.label(ax, (17.3, 1.6), "Hemidesmosome", size="small", bold=True)

bio.panel(ax, "C", (23.0, 11.3))
b = J.basal_lamina(ax, 23.4, 28.8, 8.8, depth=2.6)
bio.callout(ax, b["laminin"], (23.8, 10.5), "Laminin")
bio.callout(ax, b["nidogen"], (27.4, 10.5), "Nidogen")
bio.callout(ax, b["collagen_iv"], (23.6, 5.2), "Type IV collagen")
bio.callout(ax, b["perlecan"], (28.6, 5.2), "Perlecan")
bio.label(ax, (26.1, 4.3), "Basal lamina", size="small", bold=True)
bio.label(ax, (26.1, 9.6), "Cells above", size="tiny", color=P.muted())
