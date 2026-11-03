"""Composition of the human genome (percent; data from Futuyma and Kirkpatrick 2017, Fig. 14.14):
transposable elements (LINEs, SINEs, LTR retrotransposons, DNA transposons) together almost half, introns
26 percent, protein-coding exons 2 percent."""
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
DATA = [("Coding exons", 2, "protein"), ("Introns", 26, "rna"), ("LINEs", 20, "dna"), ("SINEs (Alu)", 13, "dna"),
        ("LTR retrotransposons", 8, "dna"), ("DNA transposons", 3, "dna"), ("Segmental duplications", 5, "highlight"),
        ("Simple sequence repeats", 3, "highlight"), ("Heterochromatin", 8, "neutral"),
        ("Other unique sequence", 12, "neutral")]
fig, ax = bio.canvas(16, 8.4)
pax = charts.axes_at(ax, (5.6, 0.9, 9.6, 6.9))
ys = list(range(len(DATA)))[::-1]
for y, (name, v, tok) in zip(ys, DATA):
    pax.barh(y, v, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, height=0.7)
    pax.text(v + 0.5, y, f"{v} %", va="center", fontsize=FT["tiny"], color=P.ink())
pax.set_yticks(ys)
pax.set_yticklabels([d[0] for d in DATA])
pax.set_xlim(0, 30)
charts.style_axes(pax, "percent of the genome")
pax.tick_params(axis="y", labelsize=FT["small"], length=0)
# bracket for transposable elements
x0 = -12.2
yt, yb = ys[2] + 0.35, ys[5] - 0.35
pax.plot([x0, x0], [yb, yt], color=charts.line("dna"), lw=1.4, clip_on=False)
pax.text(x0 - 0.4, (yt + yb) / 2, "transposable\nelements, 44 %", ha="right", va="center", fontsize=FT["tiny"],
         color=charts.line("dna"))
