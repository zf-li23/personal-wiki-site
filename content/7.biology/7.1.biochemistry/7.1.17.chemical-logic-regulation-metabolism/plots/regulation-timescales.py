"""Time scales of metabolic regulation (orders of magnitude, logarithmic axis): from single enzyme
turnovers to changes of enzyme amount by gene expression and protein degradation."""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(20.0, 8.0)
a = charts.axes_at(ax, (7.2, 1.3, 12.2, 6.2))
rows = [("Turnover of one enzyme molecule", 1e-6, 1e-1, "enzyme"),
        ("Change of substrate concentration", 1e-3, 1e1, "metabolite"),
        ("Allosteric effectors", 1e-3, 1e0, "enzyme"),
        ("Second messengers (cAMP, Ca²⁺)", 1e-1, 6e1, "receptor"),
        ("Covalent modification (kinases, phosphatases)", 1e0, 6e2, "protein"),
        ("Transport into compartments", 1e0, 3e2, "channel"),
        ("Transcription, translation", 6e2, 3.6e4, "dna"),
        ("Protein degradation (half-lives)", 3.6e3, 1.7e6, "drug")]
for k, (name, t0, t1, tok) in enumerate(rows):
    yy = len(rows) - 1 - k
    a.barh(yy, np.log10(t1) - np.log10(t0), left=np.log10(t0), height=0.6, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.8)
a.set_yticks(range(len(rows)))
a.set_yticklabels([r[0] for r in rows][::-1])
ticks = [(-6, "1 µs"), (-3, "1 ms"), (0, "1 s"), (np.log10(60), "1 min"), (np.log10(3600), "1 h"),
         (np.log10(86400), "1 d"), (np.log10(864000), "10 d")]
a.set_xticks([t for t, _ in ticks])
a.set_xticklabels([s for _, s in ticks])
a.set_xlim(-6.3, 6.4)
for t, _ in ticks:
    a.axvline(t, color=P.muted(), lw=0.4, ls=":")
charts.style_axes(a, "response time (logarithmic)")
charts.title(a, "Fast: activity of existing enzymes;  slow: amount of enzyme")
