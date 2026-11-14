"""Division of labor by response thresholds (after Bonabeau, Theraulaz and Deneubourg 1996).

A colony of 100 workers performs one task, for example feeding larvae. The task stimulus s increases by delta = 1 per
time step and decreases by 4 times the fraction of the colony's workers performing the task, so that about a quarter
of the workers must be active to keep it constant. An inactive worker with threshold theta starts the task with probability
s^2 / (s^2 + theta^2) per step; an active worker stops with probability 0.2. Half the workers have a low threshold
(theta = 5, like the minor workers of Pheidole) and half a high threshold (theta = 30, majors).
At step 400 all the low-threshold workers are removed: the stimulus rises until the high-threshold workers take
over the task, as majors do when minors are removed (Wilson 1984).
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(0)
N = 100
theta = np.array([5.0] * 50 + [30.0] * 50)
present = np.ones(N, bool)
active = np.zeros(N, bool)
s, delta, alpha = 0.0, 1.0, 4.0
steps = 900
S, A_lo, A_hi = [], [], []
for t in range(steps):
    if t == 400:
        present[:50] = False
        active[:50] = False
    p_start = s ** 2 / (s ** 2 + theta ** 2)
    start = (~active) & present & (rng.random(N) < p_start)
    stop = active & (rng.random(N) < 0.2)
    active = (active | start) & ~stop
    s = max(0.0, s + delta - alpha * active.sum() / N)
    S.append(s)
    A_lo.append(active[:50].sum())
    A_hi.append(active[50:].sum())

fig, ax = bio.canvas(30.0, 10.0)
pa = Ch.axes_at(ax, (2.6, 1.8, 11.0, 7.2))
pa.plot(S, color=P.ink(), lw=1.3)
pa.axvline(400, color=Ch.line("rna"), lw=0.9, ls=(0, (4, 2)))
pa.text(410, max(S) * 0.55, "low-threshold\nworkers removed", fontsize=FS["tiny"], color=Ch.line("rna"), va="top")
pa.set_xlim(0, steps)
Ch.style_axes(pa, "time step", "task stimulus s")
bio.panel(ax, "A", (0.3, 9.8))

pb = Ch.axes_at(ax, (18.2, 1.8, 10.8, 7.2))
pb.plot(A_lo, color=Ch.line("dna"), lw=1.2)
pb.plot(A_hi, color=Ch.line("protein"), lw=1.2)
pb.axvline(400, color=Ch.line("rna"), lw=0.9, ls=(0, (4, 2)))
pb.text(30, max(A_lo) + 1, "low threshold (θ = 5)", fontsize=FS["tiny"], color=Ch.line("dna"))
pb.text(480, max(A_hi[400:]) + 1, "high threshold (θ = 30)", fontsize=FS["tiny"], color=Ch.line("protein"))
pb.set_xlim(0, steps)
pb.set_ylim(0, max(max(A_lo), max(A_hi)) * 1.25)
Ch.style_axes(pb, "time step", "workers performing the task")
bio.panel(ax, "B", (15.8, 9.8))
