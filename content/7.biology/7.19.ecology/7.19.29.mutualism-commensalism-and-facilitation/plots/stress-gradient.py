"""A minimal model of the stress-gradient hypothesis.

A target plant alone performs W0(s) = 1 - s at stress level s (0 = benign, 1 = lethal). A neighbour
(a nurse plant) ameliorates stress, so that the target experiences s (1 - phi), but takes a constant
fraction c of its resources: W1(s) = (1 - s (1 - phi)) (1 - c). Here phi = 0.6 and c = 0.25.
A: performance with and without the neighbour; the curves cross at s* = c / (phi + c - phi c) = 0.36.
B: the relative interaction index RII = (W1 - W0) / (W1 + W0), negative (competition) in benign and
positive (facilitation) in stressful conditions; dashed: a stronger amelioration, phi = 0.8, moves the
switch to lower stress (s* = 0.29). The model is illustrative, not fitted to data.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(24.0, 10.5)
s = np.linspace(0, 0.98, 300)
c = 0.25


def w1(phi):
    return (1 - s * (1 - phi)) * (1 - c)


w0 = 1 - s
pa = C.axes_at(ax, (2.0, 1.7, 8.5, 7.2))
pa.plot(s, w0, color=Q.line_color("neutral"), lw=1.8, label="alone, W0")
pa.plot(s, w1(0.6), color=Q.line_color("plant"), lw=1.8, label="with nurse plant, W1")
ss = c / (0.6 + c - 0.6 * c)
pa.axvline(ss, color=P.muted(), lw=0.8, ls=":")
pa.text(ss + 0.02, 0.92, "s* = 0.36", fontsize=FS["tiny"], color=P.ink())
pa.set_xlim(0, 1)
pa.set_ylim(0, 1.05)
C.style_axes(pa, "environmental stress, s", "performance of target")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left")
bio.panel(ax, "A", (0.3, 10.2))
bio.label(ax, (2.0, 9.6), "Benefit of amelioration vs. cost of competition", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (14.0, 1.7, 8.5, 7.2))
for phi, ls in ((0.6, "-"), (0.8, (0, (4, 2)))):
    rii = (w1(phi) - w0) / (w1(phi) + w0)
    pb.plot(s, rii, color=Q.line_color("plant"), lw=1.8, ls=ls, label=f"phi = {phi}")
pb.axhline(0, color=P.ink(), lw=0.8)
pb.fill_between(s, 0, 1, color=P.mix(P.fill("positive"), P.surface(), 0.75), lw=0, zorder=0)
pb.fill_between(s, -0.4, 0, color=P.mix(P.fill("negative"), P.surface(), 0.75), lw=0, zorder=0)
pb.text(0.05, 0.75, "facilitation", fontsize=FS["small"], color=P.ink())
pb.text(0.55, -0.3, "competition", fontsize=FS["small"], color=P.ink())
pb.set_xlim(0, 1)
pb.set_ylim(-0.4, 1)
C.style_axes(pb, "environmental stress, s", "relative interaction index, RII")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper center")
bio.panel(ax, "B", (12.3, 10.2))
bio.label(ax, (14.0, 9.6), "Net interaction along the gradient", size="small", bold=True, ha="left")
