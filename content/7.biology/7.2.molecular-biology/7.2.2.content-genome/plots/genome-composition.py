# Composition of the human genome (about 3.1 Gb, complete T2T-CHM13 assembly), as approximate percentages.
# Top bar, by gene structure: protein-coding exons (coding sequence and untranslated regions), introns of
# protein-coding genes, and everything outside them (intergenic DNA, noncoding-RNA genes, regulatory DNA).
# Bottom bar, by sequence class (the two bars classify the same DNA in two ways and overlap: most
# transposon-derived DNA lies in introns and intergenic regions): LINEs, SINEs, LTR retrotransposons and
# DNA transposons (together about 46 %), satellites and other tandem/simple repeats, and non-repetitive DNA.
import wikibio as bio
from matplotlib.patches import Rectangle

P = bio.P
fig, ax = bio.canvas(19, 6.6)
x0, w = 3.2, 15.0


def bar(y, parts, title):
    bio.label(ax, (x0 - 0.2, y), title, size="small", ha="right")
    x = x0
    for frac, tok, text, inside in parts:
        dw = w * frac / 100
        ax.add_patch(Rectangle((x, y - 0.42), dw, 0.84, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8,
                               zorder=5))
        if inside:
            bio.label(ax, (x + dw / 2, y), f"{text}\n{frac:g} %", size="tiny", color=P.on_fill(), zorder=6)
        x += dw
    return x


y1, y2 = 4.6, 2.0
bar(y1, [(1.2, "highlight", "CDS", False), (1.0, "mrna", "UTR", False),
         (36, "dna", "Introns", True), (61.8, "neutral", "Outside protein-coding genes", True)], "Gene structure")
bio.callout(ax, (x0 + w * 0.006, y1 + 0.42), (x0 + 0.2, y1 + 1.25), "Coding exons (CDS) 1.2 %", size="tiny")
bio.callout(ax, (x0 + w * 0.017, y1 - 0.42), (x0 + 1.6, y1 - 1.0), "UTR exons ≈1 %", size="tiny")
bar(y2, [(20.7, "dna", "LINE", True), (13.0, "mrna", "SINE", True), (8.9, "protein", "LTR", True),
         (3.6, "receptor", "DNA", False), (7.8, "highlight", "Tandem", True),
         (46.0, "neutral", "Non-repetitive", True)], "Sequence class")
bio.callout(ax, (x0 + w * (0.427 + 0.018), y2 - 0.42), (x0 + w * 0.445, y2 - 1.15), "DNA transposons 3.6 %", size="tiny")
bio.label(ax, (x0 + w * 0.23, y2 + 0.75), "transposon-derived ≈ 46 %", size="tiny", color=P.muted())
ax.plot([x0, x0 + w * 0.462], [y2 + 0.55, y2 + 0.55], color=P.muted(), lw=0.8)
