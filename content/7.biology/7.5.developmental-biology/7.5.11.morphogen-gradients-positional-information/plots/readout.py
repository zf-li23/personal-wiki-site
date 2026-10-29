"""Reading a gradient: sharpness, internal contours and opposing gradients.

A: a target gene activated by cooperative binding of a morphogen with an exponential profile C = C0 exp(-x / lambda)
responds as a Hill function C^n / (C^n + K^n), which along the axis is the logistic function
1 / (1 + exp(n (x - x_T) / lambda)): the boundary width is about 4 lambda / n (n = 1, 2, 5 shown; n = 5 is close to
the value estimated for Bicoid and hunchback). B: contour control by stepwise binding P + S <-> PS, PS + S <-> PSS
with K1 = 10, K2 = 0.1: the fraction of the singly bound state [PS] peaks at S* = (K1 K2)^(-1/2) = 1, so a monotone
morphogen profile S(x) marks an internal stripe where S is near S*. C: boundary position, as a fraction of tissue
length L, for a single gradient (threshold at C / C0 = 0.2, lambda = 0.2) and for a ratio of two opposing gradients
of the same decay length (boundary where C1 / C2 = 2): the ratio boundary x* = L / 2 - (lambda / 2) ln 2 stays near
the middle of the tissue as L changes threefold; the single-gradient boundary does not.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 9.6)

pa = C.axes_at(ax, (1.6, 1.4, 7.4, 6.4))
x = np.linspace(0, 4, 400)
for n, tk in ((1, "neutral"), (2, "na"), (5, "protein")):
    pa.plot(x, 1 / (1 + np.exp(n * (x - 2.0))), color=Q.line_color(tk), lw=1.8, label=f"n = {n}")
pa.set_xlim(0, 4)
pa.set_ylim(0, 1.05)
C.style_axes(pa, "x / λ", "target activity")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "A", (0.3, 9.0))
bio.label(ax, (1.6, 9.0), "Cooperativity sharpens the boundary", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (11.6, 1.4, 7.4, 6.4))
S = np.logspace(-2, 2, 400)
K1, K2 = 10.0, 0.1
Z = 1 + K1 * S + K1 * K2 * S**2
for y, name, tk in ((1 / Z, "[P]", "neutral"), (K1 * S / Z, "[PS]", "highlight"), (K1 * K2 * S**2 / Z, "[PSS]", "protein")):
    pb.semilogx(S, y, color=Q.line_color(tk), lw=1.8, label=name)
pb.axvline(1.0, color=P.muted(), lw=0.8, ls=(0, (2, 2)))
pb.set_ylim(0, 1.05)
C.style_axes(pb, "morphogen S (log scale)", "fraction of P")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="center left")
bio.panel(ax, "B", (10.3, 9.0))
bio.label(ax, (11.6, 9.0), "Contour control: a stripe at S ≈ S*", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (21.6, 1.4, 7.6, 6.4))
lam = 0.2
L = np.linspace(0.6, 1.8, 200)
single = np.minimum(lam * np.log(1 / 0.2), L) / L
ratio = (L / 2 - lam / 2 * np.log(2)) / L
pc.plot(L, single, color=Q.line_color("negative"), lw=1.8, label="single gradient")
pc.plot(L, ratio, color=Q.line_color("protein"), lw=1.8, label="ratio of opposing gradients")
pc.set_xlim(0.6, 1.8)
pc.set_ylim(0, 0.7)
C.style_axes(pc, "tissue length L / L₀", "boundary position x* / L")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "C", (20.3, 9.0))
bio.label(ax, (21.6, 9.0), "Opposing gradients improve scaling", size="small", bold=True, ha="left")
