"""Number of distinct oligomers of n residues (log scale) for nucleic acids (4 nucleotides, 4^n),
peptides (20 amino acids, 20^n) and oligosaccharides built from m = 20 monosaccharides.
Counting model for glycans: every glycosidic bond has 2 anomeric configurations and joins C-1 of the
added residue to one of k = 4 free hydroxyls (C-2, C-3, C-4, C-6) of its acceptor. Linear chains:
m^n (2k)^(n-1). Branched chains (any acceptor may carry up to k residues at distinct positions):
coefficients of the tree generating function T(x) = m x (1 + 2T(x))^k, computed exactly with integers.
Counts ignore ring size and the configuration of the reducing end; including ring size (pyranose or
furanose) multiplies them by 2^n. The dashed line marks hexamers."""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
N, M, K = 8, 20, 4


def poly_mul(a, b):
    c = [0] * (N + 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b[: N + 1 - i]):
                c[i + j] += x * y
    return c


T = [0] * (N + 1)
for _ in range(N):  # fixed-point iteration: each pass fixes one more coefficient
    base = [1] + [2 * t for t in T[1:]]
    p = [1] + [0] * N
    for _ in range(K):
        p = poly_mul(p, base)
    T = [0] + [M * p[i - 1] for i in range(1, N + 1)]

n = np.arange(1, N + 1)
series = [
    ("nucleic acid, 4ⁿ", [4 ** k for k in n], "dna"),
    ("peptide, 20ⁿ", [20 ** k for k in n], "protein"),
    ("linear glycan", [M ** k * (2 * K) ** (k - 1) for k in n], "carbohydrate"),
    ("branched glycan", T[1:], "positive"),
]

fig, ax = bio.canvas(12.5, 7.6)
pa = charts.axes_at(ax, (1.6, 1.3, 7.0, 5.8))
for name, vals, tok in series:
    lv = np.log10(np.array(vals, dtype=float))
    pa.plot(n, lv, "-o", color=charts.line(tok), mfc=P.fill(tok), mec=charts.line(tok), ms=4.5, lw=1.6)
    pa.text(N + 0.15, lv[-1], name, color=charts.line(tok), fontsize=bio.core.FONT["small"], va="center")
    e = int(np.floor(lv[5]))
    pa.text(5.9 if tok != "carbohydrate" else 6.1, lv[5] + (0.45 if tok != "carbohydrate" else -0.5), f"${vals[5] / 10 ** e:.2g}\\times 10^{{{e}}}$",
            fontsize=bio.core.FONT["tiny"], color=P.ink(), ha="right" if tok != "carbohydrate" else "left")
pa.axvline(6, color=P.muted(), lw=0.8, ls=(0, (4, 3)))
pa.set_xlim(0.7, N + 0.3)
pa.set_ylim(0, 19)
pa.set_xticks(n)
charts.style_axes(pa, "number of residues n", "lg(number of distinct structures)")
