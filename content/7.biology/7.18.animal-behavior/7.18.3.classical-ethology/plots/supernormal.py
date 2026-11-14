"""Supernormal stimuli: a monotonic receiver response and a natural stimulus held at a moderate value by costs."""

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
s = np.linspace(0, 4, 400)
resp = 1 / (1 + np.exp(-2.2 * (s - 1.3)))
nat = np.exp(-0.5 * ((s - 1.0) / 0.12) ** 2)
fig, ax = bio.canvas(18.0, 10.0)
pa = C.axes_at(ax, (2.6, 1.8, 14.0, 7.2))
pa.fill_between(s, 0, 0.35 * nat, color=C.line("plant"), alpha=0.35, lw=0)
pa.plot(s, resp, color=C.line("negative"), lw=2.0)
pa.axvspan(2.0, 4.0, color=P.muted(), alpha=0.08, lw=0)
pa.text(1.0, 0.38, "natural eggs", color=C.line("plant"), fontsize=FS["tiny"], ha="center", va="bottom")
pa.text(3.0, 0.55, "supernormal range:\nnever occurs in nature", color=P.muted(), fontsize=FS["tiny"], ha="center")
pa.text(1.42, 0.62, "receiver's response", color=C.line("negative"), fontsize=FS["tiny"], ha="right")
pa.plot([1.0], [1 / (1 + np.exp(-2.2 * (1.0 - 1.3)))], "o", color=P.ink(), ms=5)
pa.plot([3.0], [1 / (1 + np.exp(-2.2 * (3.0 - 1.3)))], "o", color=P.ink(), ms=5)
pa.text(1.08, 0.30, "natural\nstimulus", color=P.ink(), fontsize=FS["tiny"], va="top")
pa.text(3.05, 0.93, "giant\negg", color=P.ink(), fontsize=FS["tiny"], va="top")
pa.set_xlim(0, 4)
pa.set_ylim(0, 1.05)
pa.set_xticks([0, 1, 2, 3, 4])
C.style_axes(pa, "egg size relative to the natural mean", "response (probability of incubation)")
