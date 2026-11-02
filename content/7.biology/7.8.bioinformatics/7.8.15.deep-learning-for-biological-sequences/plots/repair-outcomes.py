# Predicting the deletions produced by microhomology-mediated end joining at a Cas9 cut (invented target
# sequence). The 20-nt protospacer AGTTCGGCATCCAGTGGCAG is followed by the PAM TGG; SpCas9 cuts 3 bp
# upstream of the PAM. Every pair of identical k-mers (k >= 2) on the two sides of the cut defines a
# deletion that keeps one copy; its pattern score (Bae and colleagues 2014) is
# 100 exp(-D/20) (2 n_GC + n_AT), with D the deletion length and n_GC, n_AT the composition of the
# microhomology. A: the target and the four highest-scoring deletions (the microhomology that is kept is
# boxed). B: the share of the total score of the 12 highest-scoring deletions, colored by frame; the
# out-of-frame score is the share of deletions whose length is not a multiple of 3.
import math
from matplotlib.patches import Rectangle
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FT = bio.core.FONT
left = "ATGCTGGACAAGTTCGGCATCCAGTGG"
right = "CAGTGGTGACCAACAAGCGGTACGTCA"


def mh_deletions(left, right, kmin=2):
    Ll = len(left)
    out = {}
    for k in range(min(len(left), len(right)), kmin - 1, -1):
        for i in range(Ll - k + 1):
            for j in range(len(right) - k + 1):
                if left[i:i + k] != right[j:j + k]:
                    continue
                D = (Ll - i) + j
                prod = left[:i] + right[j:]
                if D <= 0 or prod in out:
                    continue
                mh = left[i:i + k]
                gc = sum(ch in "GC" for ch in mh)
                out[prod] = (D, mh, i, j, 100 * math.exp(-D / 20) * (2 * gc + k - gc))
    return sorted(out.values(), key=lambda t: -t[4])


res = mh_deletions(left, right)
tot = sum(r[4] for r in res)
oof = sum(r[4] for r in res if r[0] % 3) / tot

fig, ax = bio.canvas(30.0, 11.0)
cw = 0.36
x0 = 1.4
y = 10.0
MONO = "DejaVu Sans Mono"


def seqrow(y, s, offset=0, colors=None):
    for k, ch in enumerate(s):
        col = (colors or {}).get(k, P.ink())
        ax.text(x0 + (offset + k + 0.5) * cw, y, ch, ha="center", va="center", fontsize=FT["small"],
                family=MONO, color=col)


full = left + right
cut = len(left)
seqrow(y, full, colors={k: C.line("rna") for k in range(cut + 3, cut + 6)})
ax.plot([x0 + cut * cw] * 2, [y - 0.35, y + 0.35], color=C.line("negative"), lw=1.6)
ax.plot([x0 + (cut - 17) * cw, x0 + (cut + 3) * cw], [y + 0.45] * 2, color=C.line("dna"), lw=1.2)
bio.label(ax, (x0 + (cut - 7) * cw, y + 0.8), "protospacer", size="tiny", color=C.line("dna"))
bio.label(ax, (x0 + (cut + 4.5) * cw, y + 0.8), "PAM", size="tiny", color=C.line("rna"))
bio.label(ax, (x0 + cut * cw, y - 0.75), "cut", size="tiny", color=C.line("negative"))
for r_, (D, mh, i, j, sc) in enumerate(res[:4]):
    yy = y - 1.7 - r_ * 1.05
    kept = left[:i]
    seqrow(yy, kept)
    seqrow(yy, right[j:], offset=cut + j)
    ax.plot([x0 + i * cw, x0 + (cut + j) * cw], [yy, yy], color=P.muted(), lw=0.8, ls=(0, (2, 2)))
    k = len(mh)
    ax.add_patch(Rectangle((x0 + (cut + j) * cw, yy - 0.28), k * cw, 0.56, fill=False,
                           edgecolor=C.line("positive"), lw=1.0))
    ax.text(x0 + len(full) * cw + 0.4, yy, f"Δ{D} ({mh}), {sc / tot:.1%}", va="center",
            fontsize=FT["tiny"], color=C.line("negative") if D % 3 else C.line("dna"))
bio.panel(ax, "A", (0.2, 10.6))
b = C.axes_at(ax, (2.0, 0.9, 26.5, 3.0))
top = res[:12]
cols = [C.line("negative") if r[0] % 3 else C.line("dna") for r in top]
b.bar(range(len(top)), [r[4] / tot for r in top], color=cols, width=0.7)
b.set_xticks(range(len(top)))
b.set_xticklabels([f"Δ{r[0]}\n{r[1]}" for r in top], fontsize=FT["tiny"])
C.style_axes(b, None, "share of total score")
b.text(len(top) - 0.6, 0.15, f"in frame (blue) / out of frame (red); out-of-frame score {oof:.0%}", ha="right",
       fontsize=FT["tiny"], color=P.ink())
bio.panel(ax, "B", (0.2, 4.4))
