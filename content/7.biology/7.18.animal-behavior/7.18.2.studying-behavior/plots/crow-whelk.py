"""Whelk dropping by crows: drops needed N(h) = 1 + k / (h - h0) and total upward flight h N(h)."""

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
h0, k = 1.2, 12.0
h = np.linspace(1.6, 15, 400)
N = 1 + k / (h - h0)
H = h * N
hs = h0 + np.sqrt(k * h0)
fig, ax = bio.canvas(24.0, 10.0)
pa = C.axes_at(ax, (2.4, 1.6, 8.6, 6.8))
pa.plot(h, N, color=C.line("neutral"), lw=1.9)
pa.set_ylim(0, 20)
pa.set_xlim(0, 15)
C.style_axes(pa, "drop height h / m", "drops needed N(h)")
bio.panel(ax, "A", (0.4, 9.7))
pb = C.axes_at(ax, (14.6, 1.6, 8.6, 6.8))
pb.plot(h, H, color=C.line("negative"), lw=1.9)
pb.plot([hs], [hs * (1 + k / (hs - h0))], "o", color=P.ink(), ms=5)
pb.axvline(5.2, color=P.muted(), lw=0.9, ls=(0, (3, 2)))
pb.text(5.5, 52, "observed mean\n5.2 m", color=P.muted(), fontsize=FS["tiny"], va="top")
pb.text(hs - 0.4, hs * (1 + k / (hs - h0)) - 2.5, f"h* = {hs:.1f} m", color=P.ink(), fontsize=FS["tiny"], ha="right", va="top")
pb.set_ylim(0, 55)
pb.set_xlim(0, 15)
C.style_axes(pb, "drop height h / m", "total upward flight h N(h) / m")
bio.panel(ax, "B", (12.6, 9.7))
