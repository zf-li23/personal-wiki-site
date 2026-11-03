"""Sexual selection against natural selection (Example 13.2.1).

A: survival S(z) = exp(-(z - theta)^2 / (2 omega^2)) with theta = 0, omega = 1; mating success
M(z) = exp(alpha z) with alpha = 0.8, scaled to its value at z = 2; lifetime fitness W = S M scaled to its
maximum, which lies at z* = theta + alpha omega^2. B: z* as a function of alpha for omega = 0.5 and 1.5.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 10.0)

z = np.linspace(-2.5, 3.0, 500)
theta, omega, alpha = 0.0, 1.0, 0.8
S = np.exp(-(z - theta) ** 2 / (2 * omega ** 2))
M = np.exp(alpha * z) / np.exp(alpha * 2.0)
W = S * np.exp(alpha * z)
W = W / W.max()
zs = theta + alpha * omega ** 2

pa = C.axes_at(ax, (2.2, 1.6, 11.5, 6.8))
pa.plot(z, S, color=C.line("dna"), lw=1.8, label="survival S(z)")
pa.plot(z, M, color=C.line("rna"), lw=1.8, label="mating success M(z)")
pa.plot(z, W, color=P.ink(), lw=2.2, label="lifetime fitness W = SM")
pa.axvline(theta, color=C.line("dna"), lw=0.9, ls=(0, (3, 2)))
pa.axvline(zs, color=P.ink(), lw=0.9, ls=(0, (3, 2)))
pa.text(theta - 0.08, 1.04, "θ", color=C.line("dna"), fontsize=FS["small"], ha="right")
pa.text(zs + 0.08, 1.04, "z* = θ + αω²", color=P.ink(), fontsize=FS["small"], ha="left")
pa.set_xlim(-2.5, 3.0)
pa.set_ylim(0, 1.12)
C.style_axes(pa, "male trait z", "relative value")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "A", (0.2, 9.8))
bio.label(ax, (2.2, 9.4), "Fitness is a compromise", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (17.5, 1.6, 11.0, 6.8))
a = np.linspace(-1.0, 1.0, 200)
for om, tok in ((0.5, "protein"), (1.5, "negative")):
    pb.plot(a, theta + a * om ** 2, color=C.line(tok), lw=1.8, label=f"ω = {om:g}")
pb.axhline(0, color=P.muted(), lw=0.8)
pb.axvline(0, color=P.muted(), lw=0.8)
pb.set_xlim(-1, 1)
C.style_axes(pb, "strength of female preference α", "equilibrium trait z* − θ")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "B", (15.7, 9.8))
bio.label(ax, (17.5, 9.4), "Weak natural selection, larger exaggeration", size="small", bold=True, ha="left")
