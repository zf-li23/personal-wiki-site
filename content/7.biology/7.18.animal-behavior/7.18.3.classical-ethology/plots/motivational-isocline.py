"""Dual quantification: isoclines S M = c, and an accumulation model producing vacuum activity."""

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(28.0, 10.0)
pa = C.axes_at(ax, (2.4, 1.6, 9.6, 7.2))
m = np.linspace(0.05, 1, 300)
for c, lab in [(0.1, "weak"), (0.25, "moderate"), (0.5, "full display")]:
    pa.plot(m, c / m, color=C.line("negative"), lw=1.6)
    pa.text(1.0, c / 1.0 - 0.03, lab, color=C.line("negative"), fontsize=FS["tiny"], ha="right", va="top")
pa.plot([0.9], [0.5 / 0.9], "o", color=P.ink(), ms=5)
pa.text(0.9, 0.5 / 0.9 + 0.04, "1", color=P.ink(), fontsize=FS["tiny"], ha="right")
pa.plot([0.55], [0.5 / 0.55 if 0.5 / 0.55 < 1 else 0.95], "o", color=P.ink(), ms=5)
pa.text(0.53, 0.95, "2", color=P.ink(), fontsize=FS["tiny"], ha="right", va="bottom")
pa.set_xlim(0, 1)
pa.set_ylim(0, 1.05)
C.style_axes(pa, "internal motivation M", "stimulus strength S")
bio.panel(ax, "A", (0.4, 9.7))

# B: accumulation model. M rises at rate a; released when S*(1+M) ... use S_eff = S + s0, response if (S + 0.05) * M > theta
a, theta, dt = 0.02, 0.5, 0.05
t = np.arange(0, 140, dt)
M = np.zeros_like(t)
events = []
stim_times = np.arange(5, 60, 8.0)
mm = 0.0
for i, ti in enumerate(t):
    S = 0.05
    if any(abs(ti - st) < 0.5 for st in stim_times):
        S = 1.0
    if S * mm > theta:
        events.append((ti, mm, S > 0.5))
        mm = 0.0
    mm += a * dt * 10
    M[i] = mm
pb = C.axes_at(ax, (15.6, 1.6, 11.8, 7.2))
pb.plot(t, M, color=C.line("dna"), lw=1.6)
for st in stim_times:
    pb.axvspan(st - 0.5, st + 0.5, color=C.line("rna"), alpha=0.35, lw=0)
for ti, mv, withstim in events:
    pb.plot([ti], [mv], "v", color=P.ink() if not withstim else C.line("rna"), ms=7)
pb.axvline(60, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pb.text(61, 9.6, "no stimuli", color=P.muted(), fontsize=FS["tiny"], va="top")
pb.text(2, 9.6, "stimulus presented", color=C.line("rna"), fontsize=FS["tiny"], va="top")
vac = [e for e in events if not e[2]]
if vac:
    pb.text(vac[0][0] - 1, vac[0][1] + 0.3, "vacuum activity", color=P.ink(), fontsize=FS["tiny"], ha="right", va="bottom")
pb.set_xlim(0, 140)
pb.set_ylim(0, 10.5)
C.style_axes(pb, "time", "motivation M")
bio.panel(ax, "B", (13.8, 9.7))
