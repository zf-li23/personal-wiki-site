# Finding CpG islands with a hidden Markov model in 200 kb of human chromosome 2 around LCT and MCM6
# (GRCh38 chr2:135.70-135.90 Mb). The two hidden states (island, background) emit bases by first-order
# Markov chains whose transition probabilities were estimated from chromosome 21 (inside and outside the
# 446 UCSC CpG islands); the switching probabilities are 1/780 out of an island and 1/90 000
# into one. A: genes (RefSeq; UBXN4 on the plus strand, LCT and MCM6 on the minus strand) and the UCSC
# CpG islands (boxes). B: CpG observed/expected ratio in 500-bp windows. C: posterior probability of the
# island state from the forward-backward algorithm (sampled every 100 bp). The two annotated islands, at
# the promoters of UBXN4 and MCM6, have posterior close to 1 over their whole length; LCT, a
# tissue-specific gene, has no promoter island. The other 45 segments with posterior above 0.5 are mostly
# shorter than 200 bp; two segments of about 0.7 kb inside LCT are GC-rich (62 %) but have CpG obs/exp of
# only 0.28-0.39: the first-order emission models reward GC content as well as CpG.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
post = np.genfromtxt("lct_post.csv", delimiter=",", names=True)
win = np.genfromtxt("lct_win.csv", delimiter=",", names=True)
GENES = [("UBXN4", 135.741854, 135.785056, "+"), ("LCT", 135.787849, 135.837184, "-"),
         ("MCM6", 135.839625, 135.876443, "-")]
ISL = [(135.741575, 135.742574), (135.875793, 135.876659)]
fig, ax = bio.canvas(24.0, 12.0)
g = C.axes_at(ax, (2.0, 9.4, 20.5, 1.6))
for name, s, e, st in GENES:
    g.plot([s, e], [0.6, 0.6], color=C.line("dna"), lw=4, solid_capstyle="butt")
    tip = e if st == "+" else s
    g.annotate("", (tip + (0.002 if st == "+" else -0.002), 0.6), (tip, 0.6),
               arrowprops=dict(arrowstyle="-|>", color=C.line("dna"), lw=1.2))
    g.text((s + e) / 2, 0.95, f"{name} ({st})", ha="center", fontsize=bio.core.FONT["tiny"], color=P.ink(),
           style="italic")
for s, e in ISL:
    g.add_patch(__import__("matplotlib.patches", fromlist=["Rectangle"]).Rectangle(
        (s, 0.0), e - s, 0.3, color=C.line("highlight"), lw=0))
g.text(135.70, 0.05, "CpG islands", fontsize=bio.core.FONT["tiny"], color=P.muted())
g.set_xlim(135.70, 135.90)
g.set_ylim(-0.1, 1.3)
g.axis("off")
b = C.axes_at(ax, (2.0, 5.4, 20.5, 3.2))
b.plot(win["pos_mb"], win["cpg_oe"], color=C.line("neutral"), lw=0.9)
b.axhline(0.6, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
b.set_xlim(135.70, 135.90)
C.style_axes(b, None, "CpG obs/exp")
c = C.axes_at(ax, (2.0, 1.3, 20.5, 3.2))
c.fill_between(post["pos_mb"], post["post"], color=P.light("dna"), lw=0)
c.plot(post["pos_mb"], post["post"], color=C.line("dna"), lw=0.8)
c.set_xlim(135.70, 135.90)
c.set_ylim(0, 1.05)
C.style_axes(c, "chr2 position (Mb, GRCh38)", "P(island | sequence)")
bio.panel(ax, "A", (0.3, 11.6))
bio.panel(ax, "B", (0.3, 9.0))
bio.panel(ax, "C", (0.3, 5.0))
