"""Proportion regulation in the slug: a reaction-diffusion reading, and the time to regulate after truncation.

A: in the activator-inhibitor interpretation the activated (prestalk) tissue is a fixed fraction alpha of the slug
plus a transition layer of constant thickness, which is also prestalk. With the transition volume a fraction
1 / (beta V^(1/3)) of the slug volume V, prespore / prestalk = ((1 - alpha) / alpha) (beta V^(1/3) - 1) /
(beta V^(1/3) - 1 + 1 / alpha); here alpha = 0.15 and beta = 1 (volume in units of the cube of the layer
thickness). The ratio rises with V and is close to a power law K V^0.2 (dashed) over a range of volumes, as
measured; it saturates at (1 - alpha) / alpha for large slugs. B: after the front of a slug is cut off, the
change of inhibitor caused by the new boundary spreads by diffusion: the exact solution
-sqrt(nu) h0'(l) [2 sqrt(t / pi) exp(-z^2) - d / sqrt(nu) erfc(z)], z = d / (2 sqrt(nu t)), at distances d = 1, 2, 3
(units with nu = 1), normalized by its value at t = 10. The time at which it reaches 1 % grows as d^2 / nu.
"""

import numpy as np
from scipy.special import erfc
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(24.0, 9.2)
alpha, beta = 0.15, 1.0
V = np.logspace(1.0, 6.0, 300)
u = beta * V ** (1 / 3) - 1
R = (1 - alpha) / alpha * u / (u + 1 / alpha)
lnR = np.log(R)
slope = np.gradient(lnR, np.log(V))
i0 = np.argmin(np.abs(slope - 0.2))
K = R[i0] / V[i0] ** 0.2
pa = C.axes_at(ax, (1.8, 1.4, 8.8, 6.4))
pa.loglog(V, R, color=Q.line_color("protein"), lw=1.8, label="model")
pa.loglog(V, K * V**0.2, color=P.muted(), lw=1.2, ls=(0, (4, 2)), label="K V^0.2")
pa.axhline((1 - alpha) / alpha, color=P.edge("highlight"), lw=0.9, ls=(0, (2, 2)))
pa.text(20, (1 - alpha) / alpha * 1.1, "(1 − α)/α", color=P.edge("highlight"), fontsize=FS["tiny"])
C.style_axes(pa, "slug volume V (log scale)", "prespore / prestalk (log scale)")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower right")
bio.panel(ax, "A", (0.3, 8.6))
bio.label(ax, (1.8, 8.6), "Allometric proportion of cell types", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (14.2, 1.4, 8.8, 6.4))
t = np.linspace(1e-3, 10, 600)
for d, tk in ((1.0, "protein"), (2.0, "na"), (3.0, "negative")):
    z = d / (2 * np.sqrt(t))
    dh = 2 * np.sqrt(t / np.pi) * np.exp(-z * z) - d * erfc(z)
    dh /= dh[-1]
    pb.plot(t, dh, color=Q.line_color(tk), lw=1.8, label=f"d = {d:g}")
    t1 = t[np.argmax(dh > 0.01)]
    pb.plot([t1], [0.01], "o", color=Q.line_color(tk), ms=4)
pb.set_xlim(0, 10)
pb.set_ylim(0, 1.02)
C.style_axes(pb, "time after truncation (units of 1/ν)", "inhibitor change (normalized)")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "B", (12.7, 8.6))
bio.label(ax, (14.2, 8.6), "The signal of a cut arrives after ~ d²/ν", size="small", bold=True, ha="left")
