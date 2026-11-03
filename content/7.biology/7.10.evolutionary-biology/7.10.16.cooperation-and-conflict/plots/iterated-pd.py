"""Tit for tat (TFT) versus always defect (ALLD) in the iterated donation game (Theorem 16.2.1).

b = 3, c = 1; probability of another round w. Payoffs per game: TFT-TFT (b - c)/(1 - w), TFT-ALLD -c,
ALLD-TFT b, ALLD-ALLD 0. A: expected payoffs against the TFT frequency x for w = 0.8.
B: the unstable threshold x* = c / ((b - c)/(1 - w) + c - b) against w.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
b, c = 3.0, 1.0
fig, ax = bio.canvas(30.0, 10.0)
w = 0.8
x = np.linspace(0, 1, 200)
WT = x * (b - c) / (1 - w) - (1 - x) * c
WD = x * b
xs = c / ((b - c) / (1 - w) + c - b)
pa = C.axes_at(ax, (2.2, 1.6, 11.5, 6.8))
pa.plot(x, WT, color=C.line("protein"), lw=1.9, label="tit for tat")
pa.plot(x, WD, color=C.line("negative"), lw=1.9, label="always defect")
pa.axvline(xs, color=P.muted(), lw=0.9, ls=(0, (3, 2)))
pa.text(xs + 0.02, 8.5, f"x* = {xs:.2f}", color=P.ink(), fontsize=FS["small"])
pa.set_xlim(0, 1)
C.style_axes(pa, "frequency of tit for tat x", "expected payoff per game")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "A", (0.2, 9.8))
bio.label(ax, (2.2, 9.4), "Payoffs for w = 0.8 (b = 3, c = 1)", size="small", bold=True, ha="left")
pb = C.axes_at(ax, (17.5, 1.6, 11.0, 6.8))
ws = np.linspace(c / b + 1e-3, 0.99, 400)
th = c / ((b - c) / (1 - ws) + c - b)
pb.plot(ws, th, color=C.line("protein"), lw=1.9)
pb.fill_between(ws, th, 1, color=C.line("protein"), alpha=0.15, lw=0)
pb.axvline(c / b, color=P.muted(), lw=0.9, ls=(0, (3, 2)))
pb.text(c / b + 0.01, 0.9, "w = c/b", color=P.muted(), fontsize=FS["tiny"])
pb.text(0.7, 0.55, "TFT spreads", color=C.line("protein"), fontsize=FS["small"])
pb.text(0.45, 0.05, "ALLD spreads", color=C.line("negative"), fontsize=FS["small"])
pb.set_xlim(0, 1)
pb.set_ylim(0, 1)
C.style_axes(pb, "probability of another round w", "threshold frequency of TFT x*")
bio.panel(ax, "B", (15.7, 9.8))
bio.label(ax, (17.5, 9.4), "Repeated interaction lowers the barrier", size="small", bold=True, ha="left")
