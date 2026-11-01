# Scanning the lactase-persistence enhancer with a PWM. The 101 bp of GRCh38 chr2:135,851,026-135,851,126
# around rs4988235 (forward-strand G>A at the centre; -13910C>T on the strand of LCT and MCM6) scanned with
# the JASPAR POU2F1 (Oct-1) matrix MA0785.1 (pseudocount 0.8, human background). A: the PWM score of each
# 12-bp window, maximum over the two strands, for the ancestral (G) and derived (A) sequences; the variant
# changes only the windows that contain it (shaded). B: the best window covering the variant, read on the
# minus strand, under the logo of the matrix: at position 10, where the matrix prefers A, the derived T is
# less disfavoured than C and raises the score by 1.6 bits, but both alleles score far below the strongest site of the region
# (ATTATACAAATG, 46 bp away, 9.4 bits; matrix maximum 16.0 bits).
import numpy as np
import wikibio as bio
from wikibio import charts as C, sequence as S

P = bio.P
SEQ = ("AAACATTATACAAATGCAACCTAAGGAGGAGAGTTCCTTTGAGGCCAGGGGCTACATTATCTTATCTGTATTGCCAGCGCAGAGGCC"
       "TACTAGTACATTGT")
POU = np.array([[5076, 1938, 1494, 2075], [5351, 1046, 2142, 5231], [756, 1347, 474, 10582], [10582, 12, 29, 43],
                [153, 501, 213, 10582], [186, 82, 10582, 1326], [300, 10582, 1351, 3375], [6932, 33, 46, 3651],
                [10582, 108, 879, 787], [10582, 37, 51, 158], [1422, 457, 755, 10582], [1976, 1840, 2504, 4262]], float)
q = np.array([0.295, 0.205, 0.205, 0.295])
Wm = np.log2((POU + 0.8 * q) / (POU.sum(1, keepdims=True) + 0.8) / q)
L = len(Wm)
IDX = {c: i for i, c in enumerate("ACGT")}
COMP = str.maketrans("ACGT", "TGCA")


def scores(s):
    rc = s.translate(COMP)[::-1]
    n = len(s) - L + 1
    fw = np.array([sum(Wm[j, IDX[s[k + j]]] for j in range(L)) for k in range(n)])
    rv = np.array([sum(Wm[j, IDX[rc[len(s) - L - k + j]]] for j in range(L)) for k in range(n)])
    return np.maximum(fw, rv)


ref = SEQ
alt = SEQ[:50] + "A" + SEQ[51:]
sr, sa = scores(ref), scores(alt)
fig, ax = bio.canvas(26.0, 12.5)
a = C.axes_at(ax, (2.0, 6.8, 22.5, 4.6))
x = np.arange(1, len(sr) + 1)
a.axvspan(50 - L + 1.5, 51.5, color=P.light("highlight"), lw=0)
a.plot(x, sr, "o-", ms=2.5, lw=1.0, color=C.line("neutral"), label="ancestral (G / -13910C)")
a.plot(x, sa, "o-", ms=2.5, lw=1.0, color=C.line("dna"), label="derived (A / -13910T)")
a.axhline(0, color=P.muted(), lw=0.6)
a.set_xlim(0, len(sr) + 1)
C.style_axes(a, "window start (position in the 101-bp sequence)", "POU2F1 PWM score (bits)")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper right")
a.annotate("ATTATACAAATG", (5, sr[4]), (12, 8.0), fontsize=bio.core.FONT["tiny"], color=P.ink(),
           arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
cw = 0.8
x0 = 8.0
S.logo(ax, POU, at=(x0, 2.2), col_width=cw, height=2.6, numbers=False, title="POU2F1 (MA0785.1)")
win_ref = ref.translate(COMP)[::-1][41:41 + L]
win_alt = alt.translate(COMP)[::-1][41:41 + L]
for row, (w, nm, sc) in enumerate([(win_ref, "-13910C", sr), (win_alt, "-13910T", sa)]):
    y = 1.35 - row * 0.65
    val = sum(Wm[j, IDX[w[j]]] for j in range(L))
    bio.label(ax, (x0 - 0.4, y), nm, size="small", ha="right")
    for j, ch in enumerate(w):
        col = S.residue_colour(ch, "nucleotide")
        bold = j == 9
        bio.label(ax, (x0 + (j + 0.5) * cw, y), ch, size="normal", bold=bold, color=col)
    bio.label(ax, (x0 + L * cw + 0.5, y), f"{val:.2f} bits", size="small", ha="left")
bio.panel(ax, "A", (0.3, 12.1))
bio.panel(ax, "B", (0.3, 5.4))
