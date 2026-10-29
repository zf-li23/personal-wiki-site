"""Contact inhibition of locomotion makes a group of cells invade free space (self-propelled particle model,
Formula 20.5.1). Cells start packed in a band at the left of a channel (x < 0) and move at constant speed in the
direction of their polarity, which turns at random (rotational diffusion) and, with CIL, is repolarized away from
every cell they touch; soft repulsion prevents overlap and a weak co-attraction (as by C3a) keeps the group
together. (A) Positions after the same time with CIL (green) and without it (grey, random polarity only). (B) The
leading edge (95th percentile of x) moves steadily with CIL and only diffusively without: contact gives the cells
at the edge, whose free side faces open space, a net outward polarity, so the group spreads as a collective."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT


def simulate(cil, seed=0, n=160, steps=1600, dt=0.05):
    rng = np.random.default_rng(seed)
    W = 8.0
    x = np.c_[rng.uniform(-6, 0, n), rng.uniform(0, W, n)]
    th = rng.uniform(0, 2 * np.pi, n)
    v0, Dr, R, kcil, krep, katt = 1.0, 0.6, 1.0, 4.0, 8.0, 0.05
    front, ts = [], []
    for k in range(steps):
        d = x[:, None, :] - x[None, :, :]
        r = np.hypot(d[..., 0], d[..., 1]) + np.eye(n) * 1e9
        touch = r < R
        u = d / r[..., None]
        rep = (krep * np.clip(R - r, 0, None))[..., None] * u
        fx = rep.sum(1)
        near = (r < 3 * R) & ~touch
        fx -= katt * (u * near[..., None]).sum(1)
        if cil:
            away = (u * touch[..., None]).sum(1)
            has = touch.any(1)
            target = np.arctan2(away[:, 1], away[:, 0])
            dth = np.angle(np.exp(1j * (target - th)))
            th = th + dt * kcil * dth * has
        th = th + np.sqrt(2 * Dr * dt) * rng.standard_normal(n)
        vel = v0 * np.c_[np.cos(th), np.sin(th)] + fx
        x = x + dt * vel
        x[:, 0] = np.maximum(x[:, 0], -6.0)
        x[:, 1] = np.clip(x[:, 1], 0, W)
        if k % 20 == 0:
            front.append(np.percentile(x[:, 0], 95))
            ts.append(k * dt)
    return x, np.array(ts), np.array(front)


xc, t, fc = simulate(True)
xn, _, fn = simulate(False)
fig, (a, b) = plt.subplots(1, 2, figsize=(10.4, 3.6), gridspec_kw={"width_ratios": [1.6, 1]})
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.17, top=0.88, wspace=0.25)
a.scatter(xn[:, 0], xn[:, 1] + 9.5, s=14, color=P_.fill("neutral"), edgecolor=P_.edge("neutral"), lw=0.4)
a.scatter(xc[:, 0], xc[:, 1], s=14, color=P_.fill("cl"), edgecolor=P_.edge("cl"), lw=0.4)
a.axvline(0, color=P_.muted(), lw=0.7, ls=":")
a.text(24, -1.6, "with CIL", fontsize=FT["small"], color=P_.ink())
a.text(24, 13.5, "without CIL", fontsize=FT["small"], color=P_.ink())
a.set_aspect("equal")
a.set_ylim(-2.6, 18.2)
a.set_yticks([])
charts.style_axes(a, "x (start: band at x < 0)", None)
charts.title(a, "A  Positions at t = 80")
b.plot(t, fc, color=charts.line("cl"), lw=1.6, label="with CIL")
b.plot(t, fn, color=charts.line("neutral"), lw=1.6, label="without CIL")
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="upper left")
charts.style_axes(b, "time", "leading edge (95th percentile of x)")
charts.title(b, "B  Invasion of free space")
