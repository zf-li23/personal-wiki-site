"""Life insurance: assured fitness returns in social wasps (after Queller 1989 and Gadagkar 1991).

A brood needs T = 62 days of care from egg to adult (Ropalidia marginata). A foundress survives each day with constant
probability, chosen so that she survives the whole period with probability 0.12. A solitary foundress's brood is
completed only if she survives; in a group of n females in which any surviving female completes the care, it is
completed with probability 1 - (1 - 0.12)^n (deaths assumed independent).
A: assured fitness returns: if a female dies on day t, the share of a brood's worth of care she has given (t/T) is
lost when she nests alone, but is still realized in a group if at least one of the other n - 1 females survives to
complete the brood.
B: probability of completing a brood against the number of females caring for it.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
T, s_total = 62.0, 0.12
fig, ax = bio.canvas(30.0, 10.0)

pa = Ch.axes_at(ax, (2.6, 1.8, 11.0, 7.2))
t = np.linspace(0, T, 200)
for n, tok in ((2, "protein"), (5, "positive")):
    others = 1 - (1 - s_total) ** (n - 1)
    pa.plot(t, t / T * others, color=Ch.line(tok), lw=1.7)
    pa.text(T - 1, others + 0.02, f"group of {n}", fontsize=FS["tiny"], color=Ch.line(tok), ha="right", va="bottom")
pa.plot(t, np.zeros_like(t), color=Ch.line("rna"), lw=1.7)
pa.plot([T], [1], "o", ms=5, color=Ch.line("rna"))
pa.text(60, 0.95, "solitary: credit only if she\nsurvives all 62 days", fontsize=FS["tiny"], color=Ch.line("rna"), ha="right", va="top")
pa.set_xlim(0, T + 1)
pa.set_ylim(0, 1.05)
Ch.style_axes(pa, "day on which the female dies", "fraction of a brood credited to her")
bio.panel(ax, "A", (0.3, 9.8))

pb = Ch.axes_at(ax, (18.2, 1.8, 10.8, 7.2))
n = np.arange(1, 11)
comp = 1 - (1 - s_total) ** n
pb.plot(n, comp, "o-", ms=3.5, color=Ch.line("positive"), lw=1.6)
pb.axhline(s_total, color=Ch.line("rna"), lw=1.0, ls=(0, (3, 2)))
pb.text(10, s_total + 0.03, "solitary 0.12", fontsize=FS["tiny"], color=Ch.line("rna"), ha="right")
pb.set_xlim(0.5, 10.5)
pb.set_ylim(0, 1.0)
Ch.style_axes(pb, "number of females caring for the brood, n", "probability the brood is completed")
bio.panel(ax, "B", (15.8, 9.8))
