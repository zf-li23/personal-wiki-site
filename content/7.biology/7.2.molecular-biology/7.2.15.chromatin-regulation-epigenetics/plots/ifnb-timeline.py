# Ordered events at the IFN-beta promoter after Sendai virus infection (schematic timeline; approximate times from
# Agalioti et al. 2000, 2002 as summarized by Weaver). Bars: interval in which a factor is bound or a histone mark is
# present at the promoter by ChIP. Right: dependencies tested by immunodepletion and alanine-substituted histones.
import wikibio as bio
from wikibio import charts as C

P = bio.P
fig, ax = bio.canvas(22.0, 9.8)
rows = [
    ("enhanceosome", 2, 24, "rna"),
    ("GCN5/PCAF", 3, 8, "enzyme"),
    ("H4 K8ac", 3, 8, "positive"),
    ("H3 K9ac", 3, 19, "positive"),
    ("H3 S10ph", 3, 8, "highlight"),
    ("H3 K14ac", 6, 19, "positive"),
    ("CBP–Pol II", 5, 12, "receptor"),
    ("SWI/SNF (BRG1)", 6, 12, "drug"),
    ("TFIID (TBP)", 6, 19, "channel"),
    ("IFN-β mRNA", 6, 24, "mrna"),
]
a = C.axes_at(ax, (3.2, 1.3, 10.6, 7.6))
for k, (name, t0, t1, tok) in enumerate(rows):
    y = len(rows) - 1 - k
    a.barh(y, t1 - t0, left=t0, height=0.62, color=P.fill(tok), edgecolor=C.line(tok), lw=0.8)
a.set_yticks(range(len(rows)), [r[0] for r in rows[::-1]])
a.set_xlim(0, 24)
a.set_ylim(-0.6, len(rows) + 0.5)
a.set_xticks([0, 2, 4, 6, 8, 12, 19, 24])
C.style_axes(a, "time after virus infection / h", None)
a.axvline(6, color=P.muted(), lw=0.7, ls=(0, (2, 2)))
a.text(6.2, len(rows) + 0.35, "nucleosome slides 36 bp,\ntranscription begins", fontsize=bio.core.FONT["tiny"],
       color=P.muted(), va="top")

# dependency diagram
x, y0 = 17.6, 8.6
nodes = [("enhanceosome", 8.6), ("GCN5 (HAT)", 7.3), ("H4K8ac, H3K9ac;\nS10ph → K14ac", 5.9), ("SWI/SNF", 4.4),
         ("TFIID", 3.0), ("transcription", 1.6)]
for name, y in nodes:
    bio.box(ax, (x, y), 3.6, 0.85, "neutral", name, size="tiny", radius=0.12)
for (_, ya), (_, yb) in zip(nodes[:-1], nodes[1:]):
    bio.arrow(ax, (x, ya - 0.45), (x, yb + 0.45), kind="activation")
bio.arrow(ax, (x + 1.85, 5.9), (x + 1.85, 3.0), kind="activation", bend=0.7)
bio.label(ax, (x + 3.0, 4.45), "K9ac,\nK14ac", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (x - 1.95, 5.05), "H4K8ac", size="tiny", color=P.muted(), ha="right")
bio.label(ax, (x, 9.45), "dependencies", size="small", bold=True)
