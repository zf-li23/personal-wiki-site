"""Feedback control of cellular cholesterol by SREBP-2 (SBGN activity flow; open arrows activate, bars inhibit).

ER: when ER cholesterol is high, cholesterol binds SCAP and oxysterols (25-hydroxycholesterol) bind Insig;
Insig holds the SCAP-SREBP complex in the ER. When sterols fall, SCAP escorts SREBP in COPII vesicles to the
Golgi, where site-1 and site-2 proteases release the N-terminal bHLH-Zip domain (nuclear SREBP), which
enters the nucleus and activates genes with sterol regulatory elements: HMG-CoA reductase, the LDL receptor,
other enzymes of cholesterol synthesis, and PCSK9. HMG-CoA reductase makes cholesterol; the LDL receptor
imports it from LDL. Sterols (lanosterol, 25-hydroxycholesterol) also make Insig trigger ubiquitination and
ER-associated degradation of HMG-CoA reductase. AMPK (low energy) phosphorylates and inactivates the
reductase; statins inhibit it competitively; PCSK9 sends the LDL receptor to lysosomes.
"""

from matplotlib.patches import FancyBboxPatch

import wikibio as bio
from wikibio import network
from wikibio import photosynthesis as ps

P = bio.P
fig, ax = bio.canvas(28.0, 13.2, scale=0.42)
for (x0, y0, x1, y1), tok, txt in (((0.3, 0.3, 12.0, 12.9), "er", "Endoplasmic reticulum"),
                                   ((12.4, 6.6, 17.2, 12.9), "golgi", "Golgi"),
                                   ((17.6, 4.4, 27.7, 12.9), "nucleus", "Nucleus"),
                                   ((12.4, 0.3, 27.7, 4.0), "extracellular", "Plasma membrane and endosomes")):
    ax.add_patch(FancyBboxPatch((x0, y0), x1 - x0, y1 - y0, boxstyle="round,pad=0,rounding_size=0.5",
                                facecolor=ps.tint(tok, 0.55, 0.82), edgecolor=P.edge(tok), lw=1.4, zorder=1))
    bio.label(ax, (x0 + 0.3, y1 - 0.35), txt, size="small", bold=True, ha="left", color=P.edge(tok))

d = network.Diagram(ax, size="small")
d.simple_chemical("chol", (2.8, 9.0), "cholesterol", r=0.95, token="lipid")
d.simple_chemical("oxy", (2.8, 5.2), "oxysterols,\nlanosterol", r=1.05, token="lipid")
d.activity("insig", (6.6, 7.2), "Insig", token="protein", w=2.0)
d.activity("scap", (9.2, 10.6), "SCAP–SREBP-2\nexport (COPII)", token="receptor", w=4.0, h=1.3)
d.connect("chol", "scap", "negative", text="binds SCAP", text_offset=(0.0, 0.1))
d.connect("oxy", "insig", "positive")
d.connect("insig", "scap", "negative", text="retains", text_offset=(0.5, -0.2))

d.activity("cleave", (14.8, 10.6), "S1P, S2P\ncleavage", token="enzyme", w=3.2, h=1.3)
d.connect("scap", "cleave", "positive")
d.activity("nsrebp", (20.4, 10.6), "nuclear SREBP-2\n(bHLH-Zip)", token="dna", w=4.0, h=1.3)
d.connect("cleave", "nsrebp", "positive")
d.nucleic_acid("genes", (22.6, 7.2), "SRE: HMGCR, LDLR, PCSK9,\nother sterol genes", token="dna", w=7.4, h=1.4)
d.connect("nsrebp", "genes", "positive")

d.activity("hmgcr", (9.0, 3.6), "HMG-CoA reductase", token="enzyme", w=4.4)
d.connect("genes", "hmgcr", "positive", via=[(17.0, 5.8), (9.0, 5.8)])
d.connect("hmgcr", "chol", "positive", bend=-0.12, text="synthesis", text_at=0.5, text_offset=(0.3, 0.2))
d.activity("erad", (5.4, 1.3), "Insig-dependent\nubiquitination, ERAD", token="negative", w=4.6, h=1.3)
d.connect("oxy", "erad", "positive")
d.connect("erad", "hmgcr", "negative")
d.perturbation("statin", (14.2, 5.0), "statins", token="drug", w=2.6, h=1.0)
d.connect("statin", "hmgcr", "negative")
d.activity("ampk", (11.0, 1.3), "AMPK", token="positive", w=2.2)
d.connect("ampk", "hmgcr", "negative", text="P", text_offset=(0.25, 0.0))

d.activity("ldlr", (18.6, 2.0), "LDL receptor", token="receptor", w=3.4)
d.activity("pcsk9", (24.6, 2.0), "PCSK9", token="drug", w=2.4)
d.connect("genes", "ldlr", "positive")
d.connect("genes", "pcsk9", "positive")
d.connect("pcsk9", "ldlr", "negative", text="lysosomal\ndegradation", text_offset=(0.0, 0.25))
d.connect("ldlr", "chol", "positive", via=[(12.2, 2.0), (12.2, 12.15), (2.8, 12.15)], text="LDL uptake",
          text_at=0.25, text_offset=(0.0, 0.0))
