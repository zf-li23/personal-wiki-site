# Splice-site signals of human introns. Counts at the 1883 introns of the longest RefSeq (NM) transcript of
# each of the 228 curated protein-coding genes on chromosome 21 (GRCh38), read from the genome on the
# strand of the gene. A: 5' splice site (donor), exon positions -3 to -1 and intron positions +1 to +6;
# the intron starts with GT in 98.9 % of introns (GC in 0.8 %). B: 3' splice site (acceptor), intron
# positions -20 to -1 and exon positions +1 to +3: the invariant AG is preceded by a pyrimidine-rich
# tract. The boundary is marked by a vertical line. Stack heights are information contents in bits.
import numpy as np
import wikibio as bio
from wikibio import sequence as S

P = bio.P
DON = [[652, 700, 343, 188], [1234, 205, 189, 255], [172, 62, 1532, 117], [4, 0, 1879, 0], [0, 16, 0, 1867],
       [1143, 57, 634, 49], [1304, 145, 224, 210], [133, 108, 1500, 142], [272, 310, 350, 951]]
ACC = [[364, 452, 319, 748], [320, 466, 319, 778], [297, 482, 300, 804], [265, 485, 279, 854],
       [213, 496, 304, 870], [210, 489, 259, 925], [217, 475, 263, 928], [182, 508, 233, 960],
       [183, 477, 211, 1012], [127, 471, 203, 1082], [169, 513, 215, 986], [191, 553, 239, 900],
       [226, 600, 203, 854], [204, 622, 179, 878], [164, 536, 141, 1042], [166, 522, 124, 1071],
       [427, 471, 433, 552], [145, 1214, 3, 521], [1883, 0, 0, 0], [0, 4, 1879, 0], [502, 259, 925, 197],
       [480, 300, 388, 715], [502, 449, 439, 493]]
fig, ax = bio.canvas(30.0, 6.4)
cw = 0.72
x0 = 1.8
S.logo(ax, DON, at=(x0, 1.3), col_width=cw, height=3.6, numbers=False, title="A   5' splice site (donor)")
labs = ["-3", "-2", "-1", "+1", "+2", "+3", "+4", "+5", "+6"]
for i, t in enumerate(labs):
    bio.label(ax, (x0 + (i + 0.5) * cw, 1.05), t, size="tiny", color=P.muted())
xb = x0 + 3 * cw
ax.plot([xb, xb], [1.2, 5.0], color=P.muted(), lw=0.9, ls=(0, (3, 2)))
bio.label(ax, (xb - 0.9, 0.45), "exon", size="small", color=P.muted())
bio.label(ax, (xb + 1.6, 0.45), "intron", size="small", color=P.muted())
x1 = 11.0
S.logo(ax, ACC, at=(x1, 1.3), col_width=cw, height=3.6, numbers=False, title="B   3' splice site (acceptor)")
for i in range(23):
    t = f"-{20 - i}" if i < 20 else f"+{i - 19}"
    if i % 2 == 0 or i >= 17:
        bio.label(ax, (x1 + (i + 0.5) * cw, 1.05), t, size="tiny", color=P.muted())
xb = x1 + 20 * cw
ax.plot([xb, xb], [1.2, 5.0], color=P.muted(), lw=0.9, ls=(0, (3, 2)))
bio.label(ax, (xb - 3.0, 0.45), "intron (polypyrimidine tract)", size="small", color=P.muted())
bio.label(ax, (xb + 1.1, 0.45), "exon", size="small", color=P.muted())
