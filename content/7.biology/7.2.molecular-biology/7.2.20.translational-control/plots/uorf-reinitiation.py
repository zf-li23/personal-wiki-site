# Delayed reinitiation on the mRNA of ATF4 (mammals; GCN4 in yeast works the same way with four uORFs).
# A: the 5' leader of ATF4 mRNA contains a short uORF1 (3 codons) and an inhibitory uORF2 whose stop codon lies
#    beyond, and out of frame with, the ATF4 start codon. After translating uORF1, most 40S subunits stay on the
#    mRNA and resume scanning, but must rebind a ternary complex (eIF2-GTP-Met-tRNAi) before they can recognize
#    another AUG. With abundant ternary complex (unstressed cells), they reacquire it before uORF2, translate
#    uORF2 and miss ATF4; when eIF2alpha is phosphorylated, many scan past uORF2 before rebinding and
#    reinitiate at ATF4.
# B: a model: rebinding is a Poisson process along the leader with rate a proportional to the ternary-complex
#    concentration (per nucleotide scanned); the probability of rebinding within a distance d is
#    1 - exp(-a d). Fraction initiating at uORF2 = 1 - exp(-a d2); at ATF4 = exp(-a d2)(1 - exp(-a D)), with
#    d2 = 90 nt (uORF1 to uORF2) and D = 180 nt (uORF2 start to ATF4 start), illustrative values;
#    a = 0.03 nt^-1 at the normal TC level. Bulk (cap-dependent) translation is taken proportional to the TC
#    level. ATF4 translation rises while bulk translation falls, and falls again at very low TC.
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
import wikibio as bio
from wikibio import charts

P = bio.P
fig = plt.figure(figsize=(12.6, 4.4))
gs = fig.add_gridspec(1, 2, width_ratios=[1.3, 1])
ax = fig.add_subplot(gs[0])
ax.set_xlim(0, 14)
ax.set_ylim(0, 7)
ax.axis("off")
ax.set_title("A   Delayed reinitiation on ATF4 mRNA", loc="left", fontsize=9, color=P.ink())


def mrna(y):
    ax.plot([0.6, 13.4], [y, y], color=P.edge("mrna"), lw=1.6)
    ax.add_patch(bio.core.Circle((0.6, y), 0.13, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), zorder=5))
    ax.add_patch(Rectangle((1.6, y - 0.16), 0.5, 0.32, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral")))
    ax.add_patch(Rectangle((3.8, y + 0.02), 4.6, 0.28, facecolor=P.fill("negative"), edgecolor=P.edge("negative")))
    ax.add_patch(Rectangle((6.6, y - 0.3), 6.6, 0.28, facecolor=P.fill("positive"), edgecolor=P.edge("positive")))
    bio.label(ax, (1.85, y + 0.42), "uORF1", size="tiny")
    bio.label(ax, (6.1, y + 0.55), "uORF2 (inhibitory)", size="tiny", color=P.edge("negative"))
    bio.label(ax, (10.0, y - 0.6), "ATF4 coding sequence", size="tiny", color=P.edge("positive"))


y1, y2 = 4.9, 1.9
mrna(y1)
mrna(y2)
bio.label(ax, (0.2, y1 + 1.25), "No stress: ternary complex abundant", size="small", ha="left", bold=True)
bio.label(ax, (0.2, y2 + 1.25), "Stress: eIF2α-P, ternary complex scarce", size="small", ha="left", bold=True)
# scanning arrows
bio.arrow(ax, (2.2, y1 + 0.75), (3.75, y1 + 0.75), kind="process")
bio.label(ax, (3.0, y1 + 1.0), "TC rebound", size="tiny", color=P.muted())
bio.arrow(ax, (3.85, y1 + 0.75), (8.4, y1 + 0.75), kind="process", color=P.edge("negative"))
bio.label(ax, (9.6, y1 + 0.75), "ATF4 skipped", size="tiny", color=P.edge("negative"))
bio.arrow(ax, (2.2, y2 + 0.75), (6.5, y2 + 0.75), kind="process", dashed=True)
bio.label(ax, (4.8, y2 + 1.0), "40S without TC scans past uORF2", size="tiny", color=P.muted())
bio.arrow(ax, (6.65, y2 + 0.75), (13.2, y2 + 0.75), kind="process", color=P.edge("positive"))
bio.label(ax, (10.0, y2 + 1.0), "ATF4 translated", size="tiny", color=P.edge("positive"))

ax = fig.add_subplot(gs[1])
tc = np.logspace(-2, 0.5, 300)
a0, d2, D = 0.03, 90.0, 180.0
a = a0 * tc
u2 = 1 - np.exp(-a * d2)
atf4 = np.exp(-a * d2) * (1 - np.exp(-a * D))
ax.semilogx(tc, atf4 / atf4[np.argmin(abs(tc - 1))], color=charts.line("positive"), lw=1.8, label="ATF4 (relative to normal)")
ax.semilogx(tc, tc, color=charts.line("neutral"), lw=1.4, ls="--", label="bulk translation ∝ TC")
ax.axvline(1, color=P.muted(), lw=0.7, ls=":")
ax.text(1.05, 0.2, "normal TC", fontsize=7, color=P.muted(), rotation=90)
ax.set_ylim(0, 8)
ax.set_xlim(1e-2, 10 ** 0.5)
ax.legend(fontsize=7, frameon=False, loc="upper right")
charts.style_axes(ax, "ternary complex level (relative)", "translation (relative)")
ax.set_title("B   Less ternary complex, more ATF4", loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
