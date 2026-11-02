# How much evidence a match must carry to stand out in a large search. A search over N candidates
# expects N * 2^(-b) chance matches at b bits per candidate, so a significant match needs about log2(N) bits
# (one chance match, solid line) plus log2(1/E) for a smaller expected number E (dashed line: E = 0.01).
# Points are the cases of the course, with the numbers of the chapters:
#   BLAST: query of 300 residues against Swiss-Prot (N = mn = 6.3e10), 42.5 bits at E = 0.01 (7.8.4);
#          query of 821 residues against 1e11 residues (nr scale): 52.9 bits at E = 0.01;
#   seed: an exact s-mer carries 2s bits; in 6.2e9 positions (both strands) s = 16 gives 1.4 chance hits,
#          s = 20 gives 0.0056 (7.8.10);
#   CRISPR guide: 20 nt + NGG carry 44 bits; allowing d mismatches removes log2 N20(d) bits, giving
#          3.5e-4, 0.62 and 11.5 chance sites at d = 0, 2, 3 (7.8.10);
#   PWM: the CTCF matrix at p = 1e-6 per window carries 19.9 bits, giving 6200 chance sites (7.8.8);
#   GWAS: 5e-8 is 0.05 / 1e6 independent tests, 24.3 bits.
import numpy as np
import wikibio as bio
from math import comb, log2
from wikibio import charts as C

P = bio.P
FT = bio.core.FONT
G2 = 2 * 3.1e9

fig, ax = bio.canvas(19.0, 11.5)
a = C.axes_at(ax, (2.2, 1.5, 15.8, 9.2))
x = np.linspace(4, 16, 100)
a.plot(x, x * np.log2(10), color=P.ink(), lw=1.3, label="one chance match (E = 1)")
a.plot(x, x * np.log2(10) + log2(100), color=P.ink(), lw=1.0, ls=(0, (4, 3)), label="E = 0.01")

def point(n, bits, text, tok, dx=0.15, dy=0.0, ha="left"):
    xx = np.log10(n)
    a.scatter([xx], [bits], s=26, color=C.line(tok), zorder=5)
    a.plot([xx, xx], [bits, xx * np.log2(10)], color=C.line(tok), lw=0.7, ls=(0, (1, 1.5)))
    a.text(xx + dx, bits + dy, text, fontsize=FT["tiny"], color=C.line(tok), ha=ha, va="center")

point(300 * 2.1e8, log2(300 * 2.1e8 / 0.01), "BLAST, 300 aa vs Swiss-Prot:\n42.5 bits at E = 0.01", "protein", dx=0.15, dy=-2.2)
point(821 * 1e11, log2(821 * 1e11 / 0.01), "BLAST, 821 aa vs 1e11 residues: 52.9 bits", "protein", dx=-0.15, ha="right")
xg = np.log10(G2)
point(G2, 32, "16-mer seed: 1.4 chance hits", "dna")
point(G2, 40, "20-mer seed: 0.006 chance hits", "dna", dx=-0.15, ha="right")
n20 = [sum(comb(20, j) * 3 ** j for j in range(d + 1)) for d in range(5)]
for d, dy in ((0, 0.0), (2, 0.0), (3, -0.4)):
    bits = 44 - log2(n20[d])
    chance = G2 / 16 * n20[d] / 4 ** 20
    point(G2, bits, f"guide + NGG, {d} mismatches: {chance:.2g} sites", "rna", dy=dy)
point(G2, -log2(1e-6), "CTCF PWM at p = 1e-6: 6200 sites", "enzyme")
point(1e6, -log2(5e-8), "GWAS: 5e-8 = 0.05 / 1e6 tests", "highlight", dx=0.15, dy=1.4)
a.set_xlim(4, 16)
a.set_ylim(10, 60)
C.style_axes(a, "number of candidates searched, log10 N", "evidence carried by a match (bits)")
a.legend(fontsize=FT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper left")
