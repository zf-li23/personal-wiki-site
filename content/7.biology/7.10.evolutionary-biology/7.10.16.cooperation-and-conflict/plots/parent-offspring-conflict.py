"""Parent-offspring conflict (Trivers 1974), schematic model.

Benefit/cost ratio of continued investment B/C(t) = 4 exp(-t / 4) during the period of care. The parent
favors care while B/C > 1; an offspring while B/C > r (1/2 full sibs, 1/4 half sibs).
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(18.0, 10.0)
p = C.axes_at(ax, (2.6, 1.6, 14.4, 7.4))
t = np.linspace(0, 12, 400)
bc = 4 * np.exp(-t / 4)
p.plot(t, bc, color=P.ink(), lw=2.0, label="B/C of further investment")
tp = 4 * np.log(4)
for r, tok, lab in ((1.0, "dna", "parent stops (B/C = 1)"), (0.5, "rna", "offspring with full siblings (B/C = 1/2)"),
                    (0.25, "negative", "offspring with half siblings (B/C = 1/4)")):
    tt = 4 * np.log(4 / r)
    p.axhline(r, color=C.line(tok), lw=0.9, ls=(0, (3, 2)))
    p.plot([tt], [r], "o", ms=5, color=C.line(tok), label=lab)
p.axvspan(tp, 4 * np.log(8), color=C.line("rna"), alpha=0.15, lw=0)
p.axvspan(4 * np.log(8), 4 * np.log(16), color=C.line("negative"), alpha=0.10, lw=0)
p.text((tp + 4 * np.log(8)) / 2, 3.0, "conflict", ha="center", color=P.ink(), fontsize=FS["small"])
p.set_xlim(0, 12)
p.set_ylim(0, 4.2)
C.style_axes(p, "age of offspring (time since birth)", "benefit to offspring / cost to parent, B/C")
p.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
