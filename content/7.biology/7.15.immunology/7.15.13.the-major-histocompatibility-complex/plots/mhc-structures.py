# MHC class I and class II molecules and the peptide motif of one class I allele.
# A: domain diagrams on a cell membrane. Class I = heavy chain (alpha1, alpha2, alpha3) + beta2-microglobulin,
#    groove closed at both ends (8-10 residue peptides). Class II = alpha (alpha1, alpha2) + beta (beta1, beta2),
#    groove open at both ends (13-25 residue peptides).
# B: an illustrative probability logo of 9-mer peptides eluted from HLA-A*02:01. Only the two dominant anchors
#    are modelled (P2: L > M > I, V; PΩ = P9: V > L > I); the other positions are drawn nearly uniform with
#    weak hydrophobic preferences. The matrix is a schematic of the published motif, not data.
import numpy as np

import wikibio as bio
from wikibio import immuno, sequence

P = bio.P
fig, ax = bio.canvas(23, 8.6)

# ---- A: structures ---------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 8.5))
ym = 1.5
bio.bilayer(ax, [(0.4, ym), (10.6, ym)])
bio.label(ax, (10.5, ym - 0.6), "Cytoplasm", size="tiny", ha="right", color=P.muted())
bio.label(ax, (10.5, ym + 0.6), "Outside", size="tiny", ha="right", color=P.muted())

h = 1.0
m1 = immuno.mhc_i(ax, 2.2, ym + 0.42, h=h)
bio.label(ax, (2.9, 6.6), "MHC class I", size="small", bold=True)
bio.callout(ax, (m1["top"][0], m1["top"][1] + 0.08), (2.6, 5.7), "peptide 8–10 aa,\nends buried", size="tiny")
bio.callout(ax, (3.85, ym + 1.1), (5.0, 3.3), "β2-microglobulin\n(chromosome 15)", size="tiny")
bio.callout(ax, (1.7, ym + 1.1), (0.6, 3.6), "α3 (CD8\nbinding)", size="tiny")

m2 = immuno.mhc_ii(ax, 8.0, ym + 0.42, h=h)
bio.label(ax, (8.0, 6.6), "MHC class II", size="small", bold=True)
bio.callout(ax, (m2["top"][0] + 1.3, m2["top"][1] + 0.05), (9.9, 5.7), "peptide 13–25 aa,\nends overhang", size="tiny")
bio.callout(ax, (8.95, ym + 1.1), (10.0, 3.5), "β2 (CD4\nbinding)", size="tiny")
bio.label(ax, (5.3, 7.7), "Peptide-binding groove: α1/α2 (class I) or α1/β1 (class II)", size="tiny", color=P.muted())

# ---- B: HLA-A*02:01 motif (schematic) ----------------------------------------------------------------
bio.panel(ax, "B", (12.0, 8.5))
AA = "ACDEFGHIKLMNPQRSTVWY"
L = 9
base = np.ones((L, 20))
hyd = {c: 1.6 for c in "LIVMFYW"}
for i in (0, 2, 4, 5, 6):  # weak hydrophobic tendency in the middle positions
    for c, w in hyd.items():
        base[i, AA.index(c)] = w
mat = base / base.sum(1, keepdims=True)
p2 = {"L": 0.62, "M": 0.2, "I": 0.08, "V": 0.05, "A": 0.02, "T": 0.03}
p9 = {"V": 0.48, "L": 0.32, "I": 0.14, "A": 0.04, "M": 0.02}
for pos, d in ((1, p2), (8, p9)):
    mat[pos] = 0
    for c, v in d.items():
        mat[pos, AA.index(c)] = v
lg = sequence.logo(ax, mat, at=(13.6, 1.5), col_width=0.95, height=5.0, alphabet=AA, kind="probs", ic=True)
bio.label(ax, (13.6 + 4.5 * 0.95, 7.6), "HLA-A*02:01 9-mer motif (schematic)", size="small", bold=True)
for pos, txt in ((1, "anchor P2"), (8, "anchor P9")):
    bio.label(ax, (lg["x"](pos), 1.5 - 0.65), txt, size="tiny", color=P.edge("highlight"), va="top")
bio.label(ax, (13.6 + 4.5 * 0.95, 0.25), "peptide position", size="small")
