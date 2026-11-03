"""Cole's paradox and the Smith-Fretwell model.

A: extra offspring an annual needs to match a perennial, p / c, against adult survival p for c = 1, 0.5, 0.1.
B: offspring fitness f(s) = 1 / (1 + exp(-(s - 3) / 0.5)) - f(0) (sigmoid, offspring size s); the optimal size
s* maximizes f(s) / s, where the line from the origin is tangent to f.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 10.0)
pa = C.axes_at(ax, (2.2, 1.6, 11.5, 6.8))
p = np.linspace(0, 1, 200)
for c, tok in ((1.0, "protein"), (0.5, "enzyme"), (0.1, "negative")):
    pa.plot(p, p / c, color=C.line(tok), lw=1.9, label=f"juvenile survival c = {c:g}")
pa.set_xlim(0, 1)
pa.set_ylim(0, 10)
C.style_axes(pa, "adult survival p", "extra offspring needed  B_a − B_p")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "A", (0.2, 9.8))
bio.label(ax, (2.2, 9.4), "Cole's paradox resolved", size="small", bold=True, ha="left")
pb = C.axes_at(ax, (17.5, 1.6, 11.0, 6.8))
s = np.linspace(0.001, 8, 2000)
f0 = 1 / (1 + np.exp(3 / 0.5))
f = np.clip(1 / (1 + np.exp(-(s - 3) / 0.5)) - f0, 0, None) / (1 - f0)
i = int(np.argmax(f / s))
pb.plot(s, f, color=C.line("dna"), lw=1.9, label="offspring survival f(s)")
pb.plot([0, 8], [0, 8 * f[i] / s[i]], color=C.line("rna"), lw=1.2, label="tangent from the origin")
pb.axvline(s[i], color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pb.plot([s[i]], [f[i]], "o", ms=4, color=C.line("rna"))
pb.text(s[i] + 0.1, 0.05, f"s* = {s[i]:.2f}", color=P.ink(), fontsize=FS["small"])
pb.set_xlim(0, 8)
pb.set_ylim(0, 1.1)
C.style_axes(pb, "resources per offspring s", "offspring survival")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower right")
bio.panel(ax, "B", (15.7, 9.8))
bio.label(ax, (17.5, 9.4), "Smith–Fretwell optimal offspring size", size="small", bold=True, ha="left")
