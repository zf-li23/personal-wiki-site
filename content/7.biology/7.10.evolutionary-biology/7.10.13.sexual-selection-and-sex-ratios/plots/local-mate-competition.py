"""Hamilton's unbeatable sex ratio under local mate competition (Theorem 13.3.2).

Diploid outbred: x* = (n - 1) / (2n). Haplodiploid with sib-mating: x* = (n - 1)(2n - 1) / (n (4n - 1)).
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(16.0, 10.0)
p = C.axes_at(ax, (2.4, 1.6, 12.6, 7.4))
n = np.arange(1, 21)
nc = np.linspace(1, 20, 400)
dip = (nc - 1) / (2 * nc)
hap = (nc - 1) * (2 * nc - 1) / (nc * (4 * nc - 1))
p.plot(nc, dip, color=C.line("dna"), lw=1.8, label="diploid: (n − 1)/2n")
p.plot(nc, hap, color=C.line("rna"), lw=1.8, label="haplodiploid: (n − 1)(2n − 1)/[n(4n − 1)]")
p.plot(n, (n - 1) / (2 * n), "o", ms=3.5, color=C.line("dna"))
p.plot(n, (n - 1) * (2 * n - 1) / (n * (4 * n - 1)), "s", ms=3.5, color=C.line("rna"))
p.axhline(0.5, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
p.text(19.8, 0.51, "Fisher: 1/2", color=P.muted(), fontsize=FS["tiny"], ha="right", va="bottom")
p.set_xlim(0.5, 20.5)
p.set_ylim(0, 0.56)
p.set_xticks([1, 2, 4, 6, 8, 10, 15, 20])
C.style_axes(p, "number of mothers laying eggs in a patch, n", "ESS proportion of sons x*")
p.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower right")
