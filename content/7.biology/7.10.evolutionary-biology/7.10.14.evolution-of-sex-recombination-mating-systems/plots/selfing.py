"""Mating systems of hermaphrodites.

A: transmission of a complete selfer relative to an outcrosser, (2 (1 - delta) + 1 - d) / 2, where delta is
inbreeding depression and d the fraction of outcross pollen lost (pollen discounting); d = 0 and 0.5.
B: equilibrium inbreeding coefficient F = S / (2 - S) under partial selfing at rate S.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 10.0)
pa = C.axes_at(ax, (2.2, 1.6, 11.5, 6.8))
dl = np.linspace(0, 1, 200)
for d, tok in ((0.0, "protein"), (0.5, "negative")):
    pa.plot(dl, (2 * (1 - dl) + 1 - d) / 2, color=C.line(tok), lw=1.9, label=f"pollen discounting d = {d:g}")
pa.axhline(1, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pa.axvline(0.5, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pa.text(0.02, 1.53, "3 : 2", color=C.line("protein"), fontsize=FS["small"], va="bottom")
pa.text(0.03, 0.62, "selfing spreads above the dashed line", color=P.muted(), fontsize=FS["tiny"])
pa.set_xlim(0, 1)
pa.set_ylim(0.4, 1.65)
C.style_axes(pa, "inbreeding depression δ", "relative transmission of a selfer")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "A", (0.2, 9.8))
bio.label(ax, (2.2, 9.4), "Fisher's automatic advantage", size="small", bold=True, ha="left")
pb = C.axes_at(ax, (17.5, 1.6, 11.0, 6.8))
S = np.linspace(0, 1, 200)
pb.plot(S, S / (2 - S), color=C.line("dna"), lw=1.9)
pb.plot(S, S, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pb.set_xlim(0, 1)
pb.set_ylim(0, 1)
C.style_axes(pb, "selfing rate S", "equilibrium inbreeding coefficient F")
pb.text(0.55, 0.25, "F = S / (2 − S)", color=C.line("dna"), fontsize=FS["small"])
bio.panel(ax, "B", (15.7, 9.8))
bio.label(ax, (17.5, 9.4), "Inbreeding under partial selfing", size="small", bold=True, ha="left")
