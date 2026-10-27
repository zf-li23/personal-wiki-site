"""Translocation of a polypeptide by a Brownian ratchet (Simon, Peskin and Oster 1992).

The chain diffuses back and forth in the translocation channel with coefficient D. Each time a new
segment of length delta has emerged on the trans side, a chaperone (BiP in the ER, mtHsp70 in
mitochondria) binds it and prevents backward sliding past that point (a perfect ratchet). A load force
f opposing import adds a drift -f D / kT. Units: delta = 1, D = 1, kT = 1 (time unit delta^2/D).
A: one trajectory with the ratchet and one of free diffusion (no binding), same random numbers.
B: mean velocity from 200 simulated chains (points) and the analytic result
v = (2D/delta) * (w^2/2) / (exp(w) - 1 - w), w = f delta / kT (line); without load v = 2D/delta.
"""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
fig, ax = bio.canvas(22.0, 8.0)
dt = 5e-4
sig = np.sqrt(2 * dt)

# ---- A: trajectories
bio.panel(ax, "A", (0.1, 7.8))
pa = charts.axes_at(ax, (1.7, 1.3, 8.2, 5.8))
n = int(20 / dt)
steps = rng.standard_normal(n) * sig
free = np.concatenate([[0], np.cumsum(steps)])
rat = np.zeros(n + 1)
bar = 0.0
for i in range(n):
    x = rat[i] + steps[i]
    x = 2 * bar - x if x < bar else x
    bar = max(bar, np.floor(x))
    rat[i + 1] = x
t = np.arange(n + 1) * dt
pa.plot(t, rat, color=charts.line("positive"), lw=1.3, label="with ratchet (chaperone binding)")
pa.plot(t, free, color=charts.line("neutral"), lw=1.1, label="free diffusion")
pa.plot(t, 2 * t, color=charts.line("positive"), lw=0.8, ls=(0, (3, 2)))
pa.text(18.5, 2 * 18.5 - 5, "v = 2D/δ", fontsize=bio.core.FONT["tiny"], color=P.muted(), ha="right")
pa.set_xlim(0, 20)
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(pa, "time / (δ²/D)", "chain imported / δ")
charts.title(pa, "Rectified diffusion")

# ---- B: force-velocity
bio.panel(ax, "B", (11.3, 7.8))
pb = charts.axes_at(ax, (12.9, 1.3, 7.6, 5.8))
W = np.linspace(0.01, 6, 200)
v_th = 2 * (W**2 / 2) / (np.exp(W) - 1 - W)
pb.plot(W, v_th, color=charts.line("protein"), lw=2.0, label="theory (perfect ratchet)")
nw, T = 200, 30.0
for w in (0.0, 0.5, 1.0, 2.0, 3.0, 4.0, 5.0):
    x = np.zeros(nw)
    b = np.zeros(nw)
    for _ in range(int(T / dt)):
        x = x - w * dt + rng.standard_normal(nw) * sig
        x = np.where(x < b, 2 * b - x, x)  # reflecting wall at the last bound site
        b = np.maximum(b, np.floor(x))
    pb.plot([w], [x.mean() / T], "o", color=charts.line("negative"), ms=5, zorder=5)
pb.plot([], [], "o", color=charts.line("negative"), ms=5, label="simulation")
pb.set_xlim(0, 6)
pb.set_ylim(0, 2.2)
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(pb, "load  fδ / kT", "velocity / (D/δ)")
charts.title(pb, "Force–velocity relation")
