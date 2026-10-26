# Accuracy of copying and specificity of recognition, from the numbers of course 7.2.
# A: expected number of errors in one product, lambda = epsilon * L (ranges from the ranges of epsilon):
#    E. coli chromosome per replication (L = 4.6e6 bp, epsilon = 1e-10..1e-9; 7.2.7), human diploid genome per
#    S phase (6e9 bp, same epsilon), an mRNA of 2 kb (epsilon = 1e-6..1e-5; 7.2.10, 7.2.22), a protein of 400
#    residues (epsilon = 1e-4..1e-3; 7.2.19), a 1 kb PCR product after 30 duplications (epsilon = 1e-6..2e-5
#    per duplication, Example 5.6.2) and a 150-nt sequencing read at Q30..Q20 (Definition 6.7.5).
#    The lengths of the mRNA, protein and read are illustrative round values.
# B: expected number of chance matches of a fully specified site of l base pairs in a random genome of G bp,
#    counted on both strands, 2G / 4^l (Formula 5.1.1, Example 9.3.1), for E. coli (G = 4.64e6) and the human
#    genome (G = 3.1e9). A site is unique below the dotted line. Recognition systems of the course are placed at
#    their specified length: on the E. coli curve the EcoRI site and the Shine-Dalgarno sequence (6), Chi (8);
#    on the human curve the TATA box (TATAWAWR, 13 bits = 6.5 bp of information), the Zif268 site (9), the
#    two RSS signals (heptamer + nonamer, 16), the Cas9 protospacer with the GG of its PAM (22), a ZFN pair with
#    four fingers per arm (24) and a TALEN pair with 18 repeats per arm (36).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 2, figsize=(11.4, 4.4), gridspec_kw={"width_ratios": [1.0, 1.05]})
fig.subplots_adjust(left=0.22, right=0.98, bottom=0.14, top=0.88, wspace=0.42)

ax = axs[0]
rows = [
    ("$\\mathit{E.\\ coli}$ chromosome, one replication", 4.6e6 * 1e-10, 4.6e6 * 1e-9, "dna"),
    ("human diploid genome, one S phase", 6e9 * 1e-10, 6e9 * 1e-9, "dna"),
    ("mRNA, 2 kb", 2e3 * 1e-6, 2e3 * 1e-5, "mrna"),
    ("protein, 400 residues", 400 * 1e-4, 400 * 1e-3, "protein"),
    ("PCR product, 1 kb, 30 duplications", 1e3 * 30 * 1e-6, 1e3 * 30 * 2e-5, "enzyme"),
    ("sequencing read, 150 nt, Q30–Q20", 150 * 1e-3, 150 * 1e-2, "enzyme"),
]
n = len(rows)
for k, (name, lo, hi, tok) in enumerate(rows):
    y = n - 1 - k
    ax.barh(y, hi - lo, left=lo, height=0.55, color=P.fill(tok), edgecolor=charts.line(tok), lw=0.9, zorder=3)
ax.axvline(1, color=P.muted(), lw=0.8, ls=":", zorder=1)
ax.text(1.15, n - 0.45, "one error\nper product", fontsize=7, color=P.muted(), va="top")
ax.set_xscale("log")
ax.set_xlim(1e-4, 30)
ax.set_xticks([1e-4, 1e-3, 1e-2, 1e-1, 1, 10], ["10⁻⁴", "10⁻³", "10⁻²", "0.1", "1", "10"])
ax.minorticks_off()
ax.set_yticks(range(n), [r[0] for r in rows][::-1])
ax.set_ylim(-0.6, n - 0.4)
charts.style_axes(ax, "expected errors per product, εL", None)
ax.tick_params(axis="y", length=0)
ax.set_title("A   Errors per copy", loc="left", fontsize=9, color=P.ink())

ax = axs[1]
l = np.linspace(0, 40, 200)
for G, tok, name in ((4.64e6, "bacterium", "$\\mathit{E.\\ coli}$"), (3.1e9, "dna", "human")):
    ax.plot(l, 2 * G / 4.0**l, color=charts.line(tok), lw=1.6)
    ax.text(1.0, 2 * G / 4.0 * 3, name, fontsize=7.5, color=charts.line(tok))
ax.axhline(1, color=P.muted(), lw=0.8, ls=":")
ax.text(39.5, 1.6, "unique", fontsize=7, color=P.muted(), ha="right", va="bottom")
marks = [
    (6.5, 3.1e9, "dna", "TATA box (6.5)", (0.7, 1.5)),
    (9, 3.1e9, "dna", "Zif268 site (9)", (0.7, 1.2)),
    (16, 3.1e9, "dna", "RSS heptamer + nonamer (16)", (0.7, 1.0)),
    (22, 3.1e9, "dna", "Cas9: 20 nt + GG (22)", (0.7, 1.0)),
    (24, 3.1e9, "dna", "ZFN pair (24)", (0.7, 1.0)),
    (36, 3.1e9, "dna", "TALEN pair (36)", (-0.7, 1.0)),
]
for x, G, tok, text, (dx, dl) in marks:
    y = 2 * G / 4.0**x
    ax.plot([x], [y], "o", color=charts.line(tok), ms=4.5, zorder=4)
    ax.text(x + dx, y * 10**dl, text, fontsize=6.8, color=P.ink(), ha="left" if dx > 0 else "right", va="bottom")
for x, text, at in ((6, "EcoRI site, SD (6)", (0.6, 1e-4)), (8, "Chi (8): 142 expected,\n1009 found", (0.6, 1e-8))):
    y = 2 * 4.64e6 / 4.0**x
    ax.plot([x], [y], "o", color=charts.line("bacterium"), ms=4.5, zorder=4)
    ax.annotate(text, (x, y), at, fontsize=6.8, color=P.ink(), ha="left", va="center",
                arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.6, shrinkB=3))
ax.set_yscale("log")
ax.set_xlim(0, 40)
ax.set_ylim(1e-14, 1e12)
ax.set_yticks([1e-12, 1e-8, 1e-4, 1, 1e4, 1e8, 1e12], ["10⁻¹²", "10⁻⁸", "10⁻⁴", "1", "10⁴", "10⁸", "10¹²"])
ax.minorticks_off()
charts.style_axes(ax, "specified length l / bp", "chance matches, 2G / 4ˡ")
ax.set_title("B   How long must a signal be?", loc="left", fontsize=9, color=P.ink())
