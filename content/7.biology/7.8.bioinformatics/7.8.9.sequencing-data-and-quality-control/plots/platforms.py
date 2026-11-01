# A: read length against per-base accuracy (as a Phred score) for the main sequencing platforms, as representative
# ranges for current chemistries (2025; they vary with instrument, kit and base-calling model). Hollow markers are
# historical modes. B: why repeated passes help single-molecule reads: if each pass over a circular template has an
# independent error probability e = 0.1 at a base, a majority vote of n passes errs with probability
# P(Bin(n, e) >= (n+1)/2); 5 passes give about Q21, 9 passes about Q31. Real HiFi consensus is computed from a
# probabilistic model of all passes and handles insertions and deletions, which a column vote does not.
import numpy as np
from scipy import stats
import wikibio as bio
from wikibio import charts as C

P = bio.P
fig, ax = bio.canvas(26.0, 9.4)
a = C.axes_at(ax, (1.8, 1.4, 12.0, 7.0))
plat = [  # name, (len lo, hi), (Q lo, hi), centre (len, Q), token, filled
    ("Illumina / DNBSEQ\n(short read, 2x150)", (50, 300), (25, 36), (150, 31), "dna", True),
    ("Element AVITI", (150, 300), (33, 44), (200, 39), "enzyme", True),
    ("Sanger", (500, 1000), (35, 45), (800, 40), "neutral", True),
    ("PacBio HiFi", (1e4, 2.5e4), (20, 40), (1.6e4, 30), "rna", True),
    ("ONT simplex (R10.4.1)", (5e3, 1e5), (15, 25), (2e4, 20), "protein", True),
    ("ONT duplex", (1e4, 6e4), (25, 33), (2.5e4, 29), "protein", False),
    ("PacBio CLR (historical)", (1e4, 5e4), (8, 12), (2e4, 10), "rna", False),
]
LAB = {"Illumina / DNBSEQ\n(short read, 2x150)": (60, 20.5, "left"), "PacBio HiFi": (9e3, 41, "right"),
       "ONT duplex": (6.5e4, 28.5, "left"), "Element AVITI": (180, 45, "right")}
for name, (l0, l1), (q0, q1), (lc, qc), tok, filled in plat:
    a.errorbar([lc], [qc], xerr=[[lc - l0], [l1 - lc]], yerr=[[qc - q0], [q1 - qc]], fmt="o", ms=7,
               color=C.line(tok), mfc=P.fill(tok) if filled else "none", mec=C.line(tok), elinewidth=1.0, capsize=2)
    lx, ly, ha = LAB.get(name, (lc * 1.35, qc + 1.0, "left"))
    a.text(lx, ly, name, fontsize=bio.core.FONT["tiny"], color=P.ink(), va="bottom", ha=ha)
a.set_xscale("log")
a.set_xlim(30, 4e5)
a.set_ylim(0, 50)
yt = [10, 20, 30, 40]
a.set_yticks(yt)
a.set_yticklabels(["Q10\n90%", "Q20\n99%", "Q30\n99.9%", "Q40\n99.99%"])
C.style_axes(a, "read length (nt)", "per-base accuracy")
bio.panel(ax, "A", (0.1, 9.3))

b = C.axes_at(ax, (17.6, 1.4, 7.6, 7.0))
ns = np.arange(1, 22, 2)
pe = np.array([stats.binom.sf((n - 1) // 2, n, 0.1) for n in ns])
b.plot(ns, -10 * np.log10(pe), "o-", color=C.line("rna"), ms=4, lw=1.6)
b.axhline(20, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
b.text(21, 20.8, "HiFi threshold Q20", ha="right", fontsize=bio.core.FONT["tiny"], color=P.muted())
b.set_xlim(0, 22)
b.set_xticks([1, 5, 9, 13, 17, 21])
b.set_ylim(0, 65)
C.style_axes(b, "passes n over the template", "consensus quality (Phred)")
bio.panel(ax, "B", (15.9, 9.3))
bio.label(ax, (18.2, 8.6), "majority vote, e = 0.1 per pass", size="small", ha="left")
