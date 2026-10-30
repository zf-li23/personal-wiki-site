"""Human growth and allometry (Section 34.6).

A: height and height velocity of a boy according to the Preece-Baines model 1,
h(t) = h1 - 2 (h1 - h_theta) / (exp(s0 (t - theta)) + exp(s1 (t - theta))), with typical parameters h1 = 176 cm,
h_theta = 162 cm, s0 = 0.10 / y, s1 = 1.2 / y, theta = 14.5 y (the model applies from about 2 years); the velocity
falls through childhood and peaks at about 9.5 cm per year in the pubertal spurt. B: allometry of head length against
body length during human growth, from the classical proportions (head one half of the body at 2 fetal months, one
quarter at birth, one eighth in the adult); the log-log slope b < 1 (negative allometry); dashed lines: isometry
(b = 1) and two other exponents for comparison.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
fig, ax = bio.canvas(26.0, 9.5)
h1, ht, s0, s1, th = 176.0, 162.0, 0.10, 1.2, 14.5
t = np.linspace(2, 20, 400)
h = h1 - 2 * (h1 - ht) / (np.exp(s0 * (t - th)) + np.exp(s1 * (t - th)))
v = np.gradient(h, t)
pa = C.axes_at(ax, (1.8, 1.5, 9.0, 6.6))
pa.plot(t, h, color=Q.line_color("channel"), lw=1.8)
pa.set_xlim(2, 20)
pa.set_ylim(60, 190)
C.style_axes(pa, "age / years", "height / cm")
pa2 = pa.twinx()
pa2.plot(t, v, color=Q.line_color("drug"), lw=1.6, ls=(0, (5, 2)))
pa2.set_ylim(0, 12)
C.style_axes(pa2, None, "velocity / (cm per year)")
pa2.spines["right"].set_visible(True)
pa2.spines["right"].set_color(P.muted())
pa.text(3, 172, "height (solid)", fontsize=bio.core.FONT["tiny"], color=Q.line_color("channel"))
pa.text(3, 162, "velocity (dashed)", fontsize=bio.core.FONT["tiny"], color=Q.line_color("drug"))
bio.panel(ax, "A", (0.3, 9.3))
bio.label(ax, (1.8, 9.1), "Preece–Baines growth curve", size="small", bold=True, ha="left", va="top")

L = np.array([3.0, 50.0, 87.0, 115.0, 150.0, 175.0])      # body length / cm: 2 fetal months, birth, 2, 6, 12 y, adult
frac = np.array([1 / 2, 1 / 4, 1 / 5, 1 / 6, 1 / 7, 1 / 8])
H = L * frac
b, la = np.polyfit(np.log(L), np.log(H), 1)
pb = C.axes_at(ax, (15.0, 1.5, 9.0, 6.6))
xx = np.logspace(np.log10(2), np.log10(250), 50)
pb.loglog(L, H, "o", ms=5, color=Q.line_color("protein"))
pb.loglog(xx, np.exp(la) * xx**b, color=Q.line_color("protein"), lw=1.5, label=f"fit: b = {b:.2f}")
for bb, tk in ((1.0, "neutral"), (1.5, "highlight")):
    pb.loglog(xx, H[1] * (xx / L[1]) ** bb, color=Q.line_color(tk), lw=1.0, ls=(0, (4, 2)), label=f"b = {bb:g}")
for x_, y_, lab in zip(L, H, ["2 fetal mo", "birth", "2 y", "6 y", "12 y", "adult"]):
    pb.text(x_ * 1.08, y_ * 0.86, lab, fontsize=bio.core.FONT["tiny"], color=P.ink())
pb.set_xlim(2, 250)
pb.set_ylim(1, 60)
C.style_axes(pb, "body length / cm", "head length / cm")
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "B", (13.5, 9.3))
bio.label(ax, (15.0, 9.1), "Allometry y = a xᵇ", size="small", bold=True, ha="left", va="top")
