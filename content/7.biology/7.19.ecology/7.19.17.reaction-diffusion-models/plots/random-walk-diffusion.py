"""From random walks to diffusion.

A: 4000 walkers on a line start at x = 0 and take steps of +-h every tau (h = 0.1, tau = 0.005,
so D = h^2 / (2 tau) = 1); histograms at t = 0.1, 0.5 and 2 and the Gaussian heat kernel
N(0, 2Dt). B: tracks of five two-dimensional walkers (Gaussian steps of variance 2 D dt per
coordinate, D = 1, dt = 0.01, 400 steps). C: mean squared displacement of 2000 such walkers
against time (points) and the line 4Dt: the slope estimates D.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(0)
fig, ax = bio.canvas(30.0, 10.0)

h, tau = 0.1, 0.005
D = h**2 / (2 * tau)
pa = C.axes_at(ax, (2.0, 1.6, 7.2, 6.8))
xs = np.linspace(-5, 5, 400)
for t, tok in [(0.1, "dna"), (0.5, "enzyme"), (2.0, "protein")]:
    n = int(round(t / tau))
    pos = h * (2 * rng.binomial(n, 0.5, size=4000) - n)
    pa.hist(pos, bins=np.arange(-5, 5.01, 0.2), density=True, color=Q.line_color(tok), alpha=0.35)
    pa.plot(xs, np.exp(-xs**2 / (4 * D * t)) / np.sqrt(4 * np.pi * D * t), color=Q.line_color(tok), lw=1.6,
            label=f"t = {t}")
pa.set_xlim(-5, 5)
C.style_axes(pa, "position x", "density")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink())
bio.panel(ax, "A", (0.3, 9.6))
bio.label(ax, (2.0, 9.2), "Random walk and heat kernel", size="small", bold=True, ha="left")

dt, nstep = 0.01, 400
pb = C.axes_at(ax, (12.0, 1.6, 6.8, 6.8))
for k, tok in enumerate(["dna", "enzyme", "protein", "negative", "positive"]):
    steps = rng.normal(0, np.sqrt(2 * D * dt), size=(nstep, 2))
    path = np.vstack([[0, 0], np.cumsum(steps, axis=0)])
    pb.plot(path[:, 0], path[:, 1], color=Q.line_color(tok), lw=0.8)
    pb.plot(path[-1, 0], path[-1, 1], "o", ms=3.5, color=Q.line_color(tok))
pb.plot(0, 0, "s", ms=4, color=P.ink())
pb.set_xlim(-6, 6)
pb.set_ylim(-6, 6)
pb.set_aspect("equal")
C.style_axes(pb, "x", "y")
bio.panel(ax, "B", (10.6, 9.6))
bio.label(ax, (12.0, 9.2), "Tracks in two dimensions", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (22.5, 1.6, 7.0, 6.8))
steps = rng.normal(0, np.sqrt(2 * D * dt), size=(nstep, 2000, 2))
paths = np.cumsum(steps, axis=0)
msd = (paths**2).sum(axis=2).mean(axis=1)
tt = dt * np.arange(1, nstep + 1)
pc.plot(tt[::20], msd[::20], "o", ms=3.5, color=Q.line_color("dna"), label="simulated")
pc.plot(tt, 4 * D * tt, color=Q.line_color("enzyme"), lw=1.5, label="4Dt")
slope = np.polyfit(tt, msd, 1)[0]
pc.text(0.3, 14.5, f"fitted slope / 4 = {slope / 4:.2f}", fontsize=FS["tiny"], color=P.ink())
pc.set_xlim(0, 4)
pc.set_ylim(0, 17)
C.style_axes(pc, "time t", "mean squared displacement")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower right")
bio.panel(ax, "C", (21.0, 9.6))
bio.label(ax, (22.5, 9.2), "Estimating D", size="small", bold=True, ha="left")
