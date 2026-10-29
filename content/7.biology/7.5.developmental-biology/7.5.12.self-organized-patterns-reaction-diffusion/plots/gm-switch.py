"""The switch point of the Gierer-Meinhardt model in the limit of a non-diffusing activator.

Model (scaled): f(a, h) = a^2 / (h (1 + a^2)) - a/2 + mu, g(a, h) = a^2 - lambda h, here mu = 0 and lambda = 1.
A: the activator null-cline f = 0 has three branches for h < 1: A0 = 0 and A1,2 = 1/h -+ sqrt(1/h^2 - 1); the
middle branch (dashed) is unstable. B: at the switch point h_s the activator jumps from A0 to A2 through an
inner layer of width sqrt(eps); this requires the signed area of f(a, h_s) between A0 and A2 to vanish
(equal-area rule). Solving tan^-1 a_s = a_s (1 + a_s^2 / 2) / (1 + a_s^2) gives a_s = 1.515, h_s = 2 a_s / (1 + a_s^2)
= 0.920. C: along the switched path the inhibitor equation nu h'' + g = 0 has the potential V(h) = int g dh, which has
a kink at h_s: slope g0 = -lambda h_s < 0 on the low branch and g1 = A2(h_s)^2 - lambda h_s > 0 on the high branch.
"""

import numpy as np
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
lam = 1.0
a_s = brentq(lambda a: np.arctan(a) - a * (1 + a * a / 2) / (1 + a * a), 0.5, 5)
h_s = 2 * a_s / (1 + a_s**2)

fig, ax = bio.canvas(30.0, 9.2)
h = np.linspace(0.3, 1.0, 400)
A1 = 1 / h - np.sqrt(1 / h**2 - 1)
A2 = 1 / h + np.sqrt(1 / h**2 - 1)
pa = C.axes_at(ax, (1.6, 1.4, 7.4, 6.4))
pa.plot(h, 0 * h, color=Q.line_color("protein"), lw=1.8)
pa.plot(h, A2, color=Q.line_color("protein"), lw=1.8)
pa.plot(h, A1, color=Q.line_color("protein"), lw=1.4, ls=(0, (3, 2)))
pa.plot([h_s, h_s], [0, a_s], color=Q.line_color("negative"), lw=1.6)
pa.text(h_s - 0.02, a_s + 0.35, "switch\nat $h_s$", color=Q.line_color("negative"), fontsize=FS["tiny"], ha="right")
pa.set_xlim(0.3, 1.05)
pa.set_ylim(-0.2, 6)
C.style_axes(pa, "inhibitor h", "activator a on f = 0")
for txt, xy in (("$A_0$", (0.35, 0.15)), ("$A_1$ (unstable)", (0.45, 0.75)), ("$A_2$", (0.45, 4.3))):
    pa.text(*xy, txt, color=P.ink(), fontsize=FS["tiny"])
bio.panel(ax, "A", (0.3, 8.6))
bio.label(ax, (1.6, 8.6), "Three branches of the activator", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (11.6, 1.4, 7.4, 6.4))
a = np.linspace(0, 1.8, 400)
f = a * a / (h_s * (1 + a * a)) - a / 2
pb.plot(a, f, color=Q.line_color("protein"), lw=1.8)
pb.fill_between(a, 0, f, where=(f < 0) & (a < a_s), color=P.fill("na"), alpha=0.45, lw=0)
pb.fill_between(a, 0, f, where=(f > 0) & (a < a_s), color=P.fill("negative"), alpha=0.45, lw=0)
pb.axhline(0, color=P.muted(), lw=0.8)
pb.text(0.15, -0.035, "area −", color=P.ink(), fontsize=FS["tiny"])
pb.text(1.0, 0.012, "area +", color=P.ink(), fontsize=FS["tiny"])
pb.set_xlim(0, 1.8)
C.style_axes(pb, "activator a", f"f(a, $h_s$),  $h_s$ = {h_s:.3f}")
bio.panel(ax, "B", (10.3, 8.6))
bio.label(ax, (11.6, 8.6), f"Equal-area rule: $a_s$ = {a_s:.3f}", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (21.6, 1.4, 7.4, 6.4))
hh = np.linspace(0.6, 1.0, 400)
A2h = 1 / hh + np.sqrt(np.maximum(1 / hh**2 - 1, 0))
g = np.where(hh < h_s, -lam * hh, A2h**2 - lam * hh)
V = np.concatenate([[0], np.cumsum(0.5 * (g[1:] + g[:-1]) * np.diff(hh))])
V -= np.interp(h_s, hh, V)
pc.plot(hh, V, color=Q.line_color("protein"), lw=1.8)
pc.axvline(h_s, color=Q.line_color("negative"), lw=0.9, ls=(0, (2, 2)))
pc.set_xlim(0.6, 1.0)
C.style_axes(pc, "inhibitor h", "V(h) = ∫ g dh")
pc.text(0.63, 0.15, "low branch:\nslope −λh", color=P.ink(), fontsize=FS["tiny"])
pc.text(h_s - 0.075, 0.2, "high branch\n(right of $h_s$):\nslope $A_2^2 - λh$", color=P.ink(), fontsize=FS["tiny"])
bio.panel(ax, "C", (20.3, 8.6))
bio.label(ax, (21.6, 8.6), "A kinked potential: relative regulation", size="small", bold=True, ha="left")
