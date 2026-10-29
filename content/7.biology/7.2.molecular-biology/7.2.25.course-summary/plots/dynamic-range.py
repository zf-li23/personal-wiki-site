"""How much each factor of the expression product can change, on one logarithmic axis.

Top group, single mechanisms with the numbers of the course: gene dosage between origin and
terminus of E. coli at a 20 min doubling time with C = 40 min (2^(C/tau) = 4, Proposition 7.7.1);
lac repression by O1 alone (18-fold) and with all three operators (1300-fold, Example 11.2.2);
activation by CAP at lac (50-fold, 11.6); four activators that each stabilize the machinery
4-fold (4^4 = 256, Formula 14.4.1); trp repression with attenuation (700-fold, 25.2); the iron
response elements of ferritin and transferrin-receptor mRNAs (about 20-fold, Example 18.4.1).
Bottom group, the genome-wide spread in mammalian cells: transcription rates span about two orders
of magnitude and mRNA half-lives about 100-fold (Schwanhausser et al. 2011; 18.1.1); for 95 % of the
genes, translation rates span 219-fold as estimated from the model of Schwanhausser et al. but only
5.8-fold as measured by ribosome profiling (Li, Bickel and Biggin 2014)."""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FONT = bio.core.FONT
fig, ax = bio.canvas(16.0, 11.0)
a = charts.axes_at(ax, (6.4, 1.2, 9.0, 9.0))

single = [
    (r"gene dosage, ori/ter ($\it{E.\ coli}$)", 4, "dna"),
    (r"$\it{lac}$ repression, O$_1$ alone", 18, "negative"),
    (r"$\it{lac}$ repression, three operators", 1300, "negative"),
    (r"CAP activation at $\it{lac}$", 50, "positive"),
    ("synergy of four activators", 256, "positive"),
    (r"$\it{trp}$, repressor + attenuation", 700, "negative"),
    ("IRE translational control", 20, "protein"),
]
spread = [
    ("transcription rate", 100, "rna"),
    ("mRNA half-life", 100, "rna"),
    ("translation rate, model estimate", 219, "protein"),
    ("translation rate, ribosome profiling", 5.8, "protein"),
]
rows = single + [None] + spread
labels = []
for i, row in enumerate(rows):
    y = len(rows) - 1 - i
    if row is None:
        labels.append("")
        continue
    name, fold, tok = row
    a.barh(y, fold - 1, left=1, height=0.62, color=P.fill(tok), edgecolor=P.edge(tok), lw=1.0)
    a.text(fold * 1.15, y, f"{fold:g}×", va="center", fontsize=FONT["small"], color=P.ink())
    labels.append(name)
a.set_xscale("log")
a.set_xlim(1, 1e4)
a.set_yticks(range(len(rows)))
a.set_yticklabels(labels[::-1], fontsize=FONT["small"])
a.set_ylim(-0.6, len(rows) - 0.4)
charts.style_axes(a, "fold change")
a.text(1.1, len(rows) - 0.25, "single mechanisms (examples)", fontsize=FONT["small"], color=P.muted(), va="bottom")
a.text(1.1, len(spread) - 0.6, "genome-wide spread, mammalian cells", fontsize=FONT["small"],
       color=P.muted(), va="bottom")
a.axhline(len(spread), color=P.muted(), lw=0.6, ls=":")
