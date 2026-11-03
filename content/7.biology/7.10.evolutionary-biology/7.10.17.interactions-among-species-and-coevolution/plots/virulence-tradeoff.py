"""The trade-off hypothesis of virulence (Theorem 17.2.1).

beta(alpha) = c sqrt(alpha) with c = 1; R0 = beta / (alpha + d), d = mu + gamma (S = 1). A: beta(alpha) and
the tangent from (-d, 0) for d = 1; the optimum alpha* = d. B: R0(alpha) for d = 0.5, 1, 2.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 10.0)
a = np.linspace(0, 6, 400)
pa = C.axes_at(ax, (2.2, 1.6, 11.5, 6.8))
pa.plot(a, np.sqrt(a), color=C.line("virus"), lw=1.9, label="transmission rate β(α)")
d = 1.0
pa.plot([-d, 6], [0, (6 + d) * np.sqrt(d) / (2 * d)], color=C.line("negative"), lw=1.2, label="tangent from (−(μ + γ), 0)")
pa.plot([d], [np.sqrt(d)], "o", ms=5, color=C.line("negative"))
pa.axvline(0, color=P.muted(), lw=0.8)
pa.text(d + 0.1, np.sqrt(d) - 0.25, "α* = μ + γ", fontsize=FS["small"], color=P.ink())
pa.set_xlim(-1.2, 6)
pa.set_ylim(0, 3.2)
C.style_axes(pa, "virulence α", "transmission rate β")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "A", (0.2, 9.8))
bio.label(ax, (2.2, 9.4), "The tangent construction", size="small", bold=True, ha="left")
pb = C.axes_at(ax, (17.5, 1.6, 11.0, 6.8))
for dd, tok in ((0.5, "protein"), (1.0, "enzyme"), (2.0, "negative")):
    pb.plot(a, np.sqrt(a) / (a + dd), color=C.line(tok), lw=1.9, label=f"μ + γ = {dd:g}")
    pb.plot([dd], [np.sqrt(dd) / (2 * dd)], "o", ms=4, color=C.line(tok))
pb.set_xlim(0, 6)
pb.set_ylim(0, 0.8)
C.style_axes(pb, "virulence α", "basic reproduction number R₀")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "B", (15.7, 9.8))
bio.label(ax, (17.5, 9.4), "Higher background mortality favors higher virulence", size="small", bold=True, ha="left")
