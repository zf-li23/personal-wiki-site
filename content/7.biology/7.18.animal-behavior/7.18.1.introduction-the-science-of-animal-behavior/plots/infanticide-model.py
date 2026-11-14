"""Sexually selected infanticide: a minimal timing model with illustrative langur-like parameters.

Interbirth interval I = 24 months, gestation g = 6.5 months, so without infanticide a mother whose infant
is a months old at takeover conceives after I - g - a months. With infanticide she conceives after d = 4 months.
Male tenure is exponential with mean T; P(still resident at conception) = exp(-t/T), averaged over a ~ U(0, I - g).
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
I, g, d = 24.0, 6.5, 4.0
fig, ax = bio.canvas(26.0, 10.0)

a = np.linspace(0, I - g, 200)
pa = C.axes_at(ax, (2.2, 1.6, 9.6, 6.8))
pa.plot(a, I - a, color=C.line("neutral"), lw=1.9)
pa.plot(a, np.full_like(a, d + g), color=C.line("negative"), lw=1.9)
pa.fill_between(a, d + g, I - a, where=(I - a) > d + g, color=C.line("negative"), alpha=0.22, lw=0)
pa.text(1.0, I - 1.0 + 0.8, "no infanticide", color=C.line("neutral"), fontsize=FS["tiny"], va="bottom")
pa.text(1.0, d + g - 0.6, "infanticide", color=C.line("negative"), fontsize=FS["tiny"], va="top")
pa.text(4.5, 15.0, "time saved", color=P.muted(), fontsize=FS["tiny"])
pa.set_xlim(0, I - g)
pa.set_ylim(0, 26)
C.style_axes(pa, "age of infant at takeover / months", "time to male's first infant / months")
bio.panel(ax, "A", (0.3, 9.7))

T = np.linspace(1, 60, 300)
L = I - g
p_no = (T / L) * (1 - np.exp(-L / T))
p_kill = np.exp(-d / T)
pb = C.axes_at(ax, (15.4, 1.6, 9.6, 6.8))
pb.plot(T, p_no, color=C.line("neutral"), lw=1.9)
pb.plot(T, p_kill, color=C.line("negative"), lw=1.9)
pb.plot(T, p_kill - p_no, color=C.line("positive"), lw=1.4, ls=(0, (4, 2)))
pb.text(40, p_kill[200] + 0.03, "infanticide", color=C.line("negative"), fontsize=FS["tiny"], va="bottom")
pb.text(40, p_no[200] - 0.04, "no infanticide", color=C.line("neutral"), fontsize=FS["tiny"], va="top")
pb.text(30, 0.2, "difference", color=C.line("positive"), fontsize=FS["tiny"])
pb.set_xlim(0, 60)
pb.set_ylim(0, 1)
C.style_axes(pb, "mean male tenure T / months", "P(male resident at conception)")
bio.panel(ax, "B", (13.5, 9.7))
