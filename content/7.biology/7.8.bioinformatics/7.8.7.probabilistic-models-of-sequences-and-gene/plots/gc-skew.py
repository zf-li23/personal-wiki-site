# GC skew of the Escherichia coli K-12 MG1655 genome (RefSeq NC_000913.3, 4 641 652 bp). A: the skew
# (G - C)/(G + C) of the forward strand in 10-kb windows. B: its cumulative sum. The cumulative skew has
# its minimum at 3.925 Mb, the replication origin oriC, and its maximum near 1.55 Mb, in the terminus
# region: the sign of the skew changes where the forward strand switches from lagging to leading
# strand template (gcskew.csv, computed from the genome sequence).
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
d = np.genfromtxt("gcskew.csv", delimiter=",", names=True)
fig, ax = bio.canvas(24.0, 10.0)
a = C.axes_at(ax, (2.0, 6.0, 20.5, 3.3))
b = C.axes_at(ax, (2.0, 1.3, 20.5, 3.3))
x = d["pos_mb"]
a.bar(x, d["skew"], width=0.0095, color=np.where(d["skew"] > 0, C.line("positive"), C.line("negative")), lw=0)
a.axhline(0, color=P.muted(), lw=0.6)
a.set_xlim(0, 4.65)
C.style_axes(a, None, "GC skew")
b.plot(x, d["cum"], color=C.line("dna"), lw=1.4)
i0, i1 = np.argmin(d["cum"]), np.argmax(d["cum"])
for i, lab in [(i0, "minimum: oriC (3.93 Mb)"), (i1, "maximum: terminus region (1.55 Mb)")]:
    b.plot(x[i], d["cum"][i], "o", color=C.line("negative"), ms=5)
    b.annotate(lab, (x[i], d["cum"][i]), (x[i] - 1.3 if i == i0 else x[i] + 0.25, d["cum"][i] + (0.6 if i == i0 else 0.9)),
               fontsize=bio.core.FONT["tiny"], color=P.ink(), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
b.set_xlim(0, 4.65)
b.set_ylim(-3.6, 6.6)
C.style_axes(b, "genome position (Mb)", "cumulative skew")
bio.panel(ax, "A", (0.3, 9.7))
bio.panel(ax, "B", (0.3, 4.9))
