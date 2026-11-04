"""The price of autotrophy: ATP equivalents needed to make one pyruvate from CO2 in the six classical pathways.

Values after Berg (2011), counting ATP equivalents (an ATP hydrolysed to AMP counts as two) and not counting
the electrons: Calvin-Benson-Bassham cycle 7, reverse citric acid cycle 2, Wood-Ljungdahl pathway about 1,
3-hydroxypropionate bicycle 7, 3-hydroxypropionate/4-hydroxybutyrate cycle 9, dicarboxylate/4-hydroxybutyrate
cycle 5. Bar colour: oxygen tolerance of the enzymes (the three cheap pathways use oxygen-sensitive
ferredoxin-dependent or metal-cluster enzymes and occur in anaerobes or microaerobes).
"""
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(20.0, 10.8)
rows = [
    ("Calvin cycle", 7, "positive", "cyanobacteria,\nplants, most\nchemolithotrophs"),
    ("Reverse citric\nacid cycle", 2, "negative", "green sulfur\nbacteria,\nAquificota"),
    ("Wood–Ljungdahl", 1, "negative", "acetogens,\nmethanogens,\nanammox, SRB"),
    ("3-Hydroxypropionate\nbicycle", 7, "positive", "Chloroflexus"),
    ("3HP/4HB cycle", 9, "positive", "Sulfolobales,\nammonia-oxidizing\narchaea"),
    ("DC/4HB cycle", 5, "negative", "Desulfurococcales,\nThermoproteales"),
]
n = len(rows)
p = quant.Plot(ax, (2.4, 3.6, 16.6, 5.8), xlim=(0, n), ylim=(0, 10), ylabel="ATP per pyruvate",
               yticks=[0, 2, 4, 6, 8, 10], grid=True)
for i, (name, atp, tok, where) in enumerate(rows):
    p.bars([i + 0.18, i + 0.82], [atp], token=tok)
    p.text(i + 0.5, atp + 0.25, f"{atp}", size="small", token=tok, va="bottom")
    bio.label(ax, (p.X(i + 0.5), 3.2), name, size="tiny", va="top", bold=True)
    bio.label(ax, (p.X(i + 0.5), 2.0), where, size="tiny", va="top", color=P.muted(), italic=(where == "Chloroflexus"))
p.legend([("oxygen-tolerant enzymes", "positive", "-"), ("oxygen-sensitive enzymes", "negative", "-")], at=(3.0, 10.5))
