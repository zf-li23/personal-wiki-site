# The work an exhaustive method would do against the work of the method used, for problems of the course
# at a realistic size (operation counts, log scale). Values follow from the formulas of the chapters:
#   multiple alignment of k = 15 sequences of n = 800: exact DP 2^k k^2 n^k against progressive k n^2 (7.8.5);
#   tree search for 15 taxa: (2n - 5)!! unrooted binary trees against neighbor joining n^3 (7.8.6);
#   counting a 20-mer in both strands of a human genome: scanning 6.2e9 positions against 20 steps of
#     backward search in an FM-index (7.8.10);
#   Smith-Waterman of all 6.2e8 reads of a 30x genome against the genome: 150 x 3.1e9 cells per read;
#     a seeded aligner must be about 1e5 times faster to finish in hours (7.8.10);
#   Li-Stephens imputation with m = 1e6 SNPs and K = 1e4 haplotypes: naive forward m K^2 against m K (7.8.13);
#   RNA folding of n = 76 (tRNA): interior loops of any size n^4 against capped loops n^3 (7.8.16).
import numpy as np
import wikibio as bio
from math import log10
from wikibio import charts as C

P = bio.P
FT = bio.core.FONT

def dfact(k):
    r = 1
    while k > 1:
        r *= k
        k -= 2
    return r

rows = [
    ("multiple alignment, 15 x 800 aa", 2 ** 15 * 15 ** 2 * 800 ** 15, 15 * 800 ** 2, "exact DP", "progressive"),
    ("tree topologies, 15 taxa", dfact(25), 15 ** 3, "all trees", "neighbor joining"),
    ("count a 20-mer in a genome", 6.2e9, 20, "scan", "FM-index"),
    ("map a 30x genome", 150 * 3.1e9 * 6.2e8, 150 * 3.1e9 * 6.2e8 / 1e5, "Smith-Waterman", "seed and extend"),
    ("imputation, 1e6 SNPs, 1e4 haplotypes", 1e6 * 1e4 ** 2, 1e6 * 1e4, "naive HMM", "Li-Stephens"),
    ("fold a tRNA, 76 nt", 76 ** 4, 76 ** 3, "all loops", "loops capped"),
]

fig, ax = bio.canvas(20.0, 10.5)
a = C.axes_at(ax, (7.6, 1.4, 11.8, 8.6))
for k, (name, ex, used, lex, lus) in enumerate(rows):
    y = len(rows) - 1 - k
    a.barh(y + 0.18, log10(ex), height=0.34, color=P.fill("negative"), edgecolor=P.edge("negative"), lw=0.6)
    a.barh(y - 0.18, log10(used), height=0.34, color=P.fill("positive"), edgecolor=P.edge("positive"), lw=0.6)
    a.text(log10(ex) + 0.5, y + 0.18, f"{lex}: 1e{log10(ex):.1f}", va="center", fontsize=FT["tiny"],
           color=P.ink())
    a.text(log10(used) + 0.5, y - 0.18, f"{lus}: 1e{log10(used):.1f}", va="center", fontsize=FT["tiny"],
           color=P.ink())
a.set_yticks(range(len(rows)))
a.set_yticklabels([r[0] for r in rows[::-1]])
a.set_xlim(0, 62)
a.axvline(log10(1e11 * 3600), color=P.muted(), lw=0.8, ls=(0, (3, 2)))
a.text(30, 3.0, "dashed line: one hour at 1e11\noperations per second", fontsize=FT["tiny"],
       color=P.muted(), va="center")
C.style_axes(a, "operations, log10", None)
