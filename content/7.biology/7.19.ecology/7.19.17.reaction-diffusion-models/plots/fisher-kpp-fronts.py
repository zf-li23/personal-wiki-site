"""Invasion fronts of the Fisher-KPP equation u_t = D u_xx + r u (1 - u).

Numerical method: finite differences, dx = 0.25, IMEX time stepping (implicit diffusion with a banded
solver, explicit logistic reaction), dt = 0.05, zero-flux boundaries.
A: an introduction u = 0.5 on |x| < 2 (D = r = 1) spreads as two fronts; profiles every 10 time units.
B: front position (where u = 0.1) against time for three (r, D) pairs (points) and lines of slope
2 sqrt(rD) through the last point; the fronts approach the minimal speed slowly from below.
C: measured asymptotic speeds (slope over the last 20 time units) against 2 sqrt(rD) for nine pairs.
D: phase plane of the traveling-wave equation U'' + c U' + U(1 - U) = 0 (scaled), V = U'. For c = 2.5
the orbit leaving the saddle (1, 0) enters the node (0, 0) inside the triangle 0 <= U <= 1,
-cU/2 <= V <= 0 (shaded); for c = 1 the origin is a spiral and the orbit makes U negative.
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import solve_banded

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(40.0, 10.0)


def run(r, D, L=260.0, dx=0.25, dt=0.05, T=60.0, every=10.0):
    x = np.arange(-L, L + dx / 2, dx)
    n = x.size
    u = np.where(np.abs(x) < 2, 0.5, 0.0)
    lam = D * dt / dx**2
    ab = np.zeros((3, n))
    ab[0, 1:] = -lam
    ab[1, :] = 1 + 2 * lam
    ab[2, :-1] = -lam
    ab[1, 0] = ab[1, -1] = 1 + lam
    snaps, ts, fronts = [], [], []
    steps = int(round(T / dt))
    k_every = int(round(every / dt))
    for k in range(steps + 1):
        if k % k_every == 0:
            snaps.append(u.copy())
        if k % 10 == 0:
            right = x[(x > 0) & (u >= 0.1)]
            ts.append(k * dt)
            fronts.append(right.max() if right.size else 0.0)
        u = solve_banded((1, 1), ab, u + dt * r * u * (1 - u))
    return x, snaps, np.array(ts), np.array(fronts)


x, snaps, ts, fr = run(1.0, 1.0)
pa = C.axes_at(ax, (2.0, 1.6, 7.5, 6.8))
for i, s in enumerate(snaps):
    pa.plot(x, s, color=Q.line_color("dna"), lw=1.2, alpha=0.35 + 0.65 * i / (len(snaps) - 1))
pa.set_xlim(-140, 140)
pa.set_ylim(0, 1.08)
C.style_axes(pa, "distance x", "density u / K")
pa.text(0, 1.02, "t = 0, 10, ..., 60", fontsize=FS["tiny"], color=P.ink(), ha="center")
bio.panel(ax, "A", (0.3, 9.6))
bio.label(ax, (2.0, 9.2), "Spread from an introduction", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (12.0, 1.6, 7.0, 6.8))
for (r, D), tok in [((1.0, 1.0), "dna"), ((0.5, 1.0), "enzyme"), ((1.0, 2.0), "protein")]:
    _, _, ts, fr = run(r, D)
    c = 2 * np.sqrt(r * D)
    pb.plot(ts[::6], fr[::6], "o", ms=3, color=Q.line_color(tok), label=f"r = {r}, D = {D}")
    pb.plot(ts, fr[-1] + c * (ts - ts[-1]), color=Q.line_color(tok), lw=1.0, ls=(0, (4, 2)))
pb.set_xlim(0, 60)
pb.set_ylim(0, 175)
C.style_axes(pb, "time t", "front position (u = 0.1)")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "B", (10.5, 9.6))
bio.label(ax, (12.0, 9.2), "Fronts move at constant speed", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (22.0, 1.6, 6.8, 6.8))
pred, meas = [], []
for r in (0.25, 0.5, 1.0):
    for D in (0.5, 1.0, 2.0):
        _, _, ts, fr = run(r, D, T=80.0)
        sel = ts >= 60
        meas.append(np.polyfit(ts[sel], fr[sel], 1)[0])
        pred.append(2 * np.sqrt(r * D))
pc.plot([0, 3.2], [0, 3.2], color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pc.plot(pred, meas, "o", ms=4.5, color=Q.line_color("negative"))
pc.set_xlim(0, 3.2)
pc.set_ylim(0, 3.2)
C.style_axes(pc, "2 sqrt(rD)", "measured speed")
bio.panel(ax, "C", (20.5, 9.6))
bio.label(ax, (22.0, 9.2), "Speed = 2 sqrt(rD)", size="small", bold=True, ha="left")

pd = C.axes_at(ax, (32.0, 1.6, 7.0, 6.8))
cc = 2.5
U = np.linspace(0, 1, 50)
pd.fill_between(U, -cc / 2 * U, 0, color=P.fill("highlight"), alpha=0.35, lw=0)
for c, tok in [(2.5, "dna"), (1.0, "negative")]:
    lp = (-c + np.sqrt(c * c + 4)) / 2
    eps = 1e-4
    sol = solve_ivp(lambda t, y: [y[1], -c * y[1] - y[0] * (1 - y[0])], [0, 60],
                    [1 - eps, -lp * eps], max_step=0.05, rtol=1e-9, atol=1e-12)
    pd.plot(sol.y[0], sol.y[1], color=Q.line_color(tok), lw=1.6, label=f"c = {c}")
pd.plot([0, 1], [0, 0], "o", ms=4.5, color=P.ink())
pd.axhline(0, color=P.muted(), lw=0.7)
pd.axvline(0, color=P.muted(), lw=0.7)
pd.set_xlim(-0.12, 1.05)
pd.set_ylim(-0.45, 0.12)
C.style_axes(pd, "U", "V = dU/dz")
pd.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left")
bio.panel(ax, "D", (30.5, 9.6))
bio.label(ax, (32.0, 9.2), "Phase plane of the wave", size="small", bold=True, ha="left")
