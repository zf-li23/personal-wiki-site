"""Persistence in a river: u_t = D u_xx - v u_x + r u (1 - u), scaled so that D = r = 1.

A: region of the (v, L) plane in which a population persists in a river reach of length L with
lethal ends (shaded): v < 2 sqrt(rD) and L > L_c = 2 pi D / sqrt(4 r D - v^2); the dashed line is the
critical length pi sqrt(D/r) of the KISS model, recovered at v = 0.
B: an introduction at x = 0 in an unbounded river (flow to the right), profiles at t = 0, 10, 20, 30, 40
for v = 1 (blue: spreads both ways) and v = 2.5 (red: the whole population is washed downstream).
C: position of the upstream edge (where u = 0.1) against time for v = 0, 1, 1.5, 2.5 (points) and the
predicted upstream speed 2 sqrt(rD) - v (lines).
Numerics: dx = 0.25, dt = 0.05, implicit diffusion, explicit upwind advection and reaction.
"""

import numpy as np
from scipy.linalg import solve_banded

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 10.0)

pa = C.axes_at(ax, (2.0, 1.6, 7.0, 6.8))
v = np.linspace(0, 1.999, 400)
Lc = 2 * np.pi / np.sqrt(4 - v**2)
pa.fill_between(v, Lc, 30, color=P.fill("positive"), alpha=0.45, lw=0)
pa.plot(v, Lc, color=Q.line_color("positive"), lw=1.6)
pa.axvline(2, color=Q.line_color("negative"), lw=1.2)
pa.axhline(np.pi, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pa.text(0.8, 18, "persistence", fontsize=FS["small"], color=P.ink(), ha="center")
pa.text(2.25, 18, "washout", fontsize=FS["small"], color=P.ink(), ha="center")
pa.set_xlim(0, 2.6)
pa.set_ylim(0, 30)
C.style_axes(pa, "flow speed v / sqrt(rD)", "reach length L / sqrt(D/r)")
bio.panel(ax, "A", (0.3, 9.6))
bio.label(ax, (2.0, 9.2), "Critical length in a river", size="small", bold=True, ha="left")


def run(vel, T=40.0, dx=0.25, dt=0.05, L=200.0):
    x = np.arange(-L, L + dx / 2, dx)
    n = x.size
    u = np.where(np.abs(x) < 2, 0.5, 0.0)
    lam = dt / dx**2
    ab = np.zeros((3, n))
    ab[0, 1:] = -lam
    ab[1, :] = 1 + 2 * lam
    ab[2, :-1] = -lam
    ab[1, 0] = ab[1, -1] = 1 + lam
    snaps, ts, up = [], [], []
    for k in range(int(round(T / dt)) + 1):
        if k % 200 == 0:
            snaps.append(u.copy())
        if k % 20 == 0:
            occ = x[u >= 0.1]
            ts.append(k * dt)
            up.append(occ.min() if occ.size else np.nan)
        adv = np.zeros_like(u)
        adv[1:] = -vel * (u[1:] - u[:-1]) / dx
        u = solve_banded((1, 1), ab, u + dt * (adv + u * (1 - u)))
    return x, snaps, np.array(ts), np.array(up)


pb = C.axes_at(ax, (12.0, 1.6, 7.0, 6.8))
for vel, tok in [(1.0, "dna"), (2.5, "negative")]:
    x, snaps, _, _ = run(vel)
    for i, s in enumerate(snaps):
        pb.plot(x, s, color=Q.line_color(tok), lw=1.1, alpha=0.3 + 0.7 * i / (len(snaps) - 1),
                label=f"v = {vel}" if i == len(snaps) - 1 else None)
pb.annotate("", xy=(60, 1.1), xytext=(20, 1.1), arrowprops=dict(arrowstyle="->", color=P.ink(), lw=1))
pb.text(40, 1.13, "flow", fontsize=FS["tiny"], color=P.ink(), ha="center")
pb.set_xlim(-60, 160)
pb.set_ylim(0, 1.22)
C.style_axes(pb, "distance downstream x", "density u / K")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "B", (10.5, 9.6))
bio.label(ax, (12.0, 9.2), "Spread against the current", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (22.5, 1.6, 7.0, 6.8))
for vel, tok in [(0.0, "dna"), (1.0, "enzyme"), (1.5, "protein"), (2.5, "negative")]:
    _, _, ts, up = run(vel)
    pc.plot(ts[::5], -up[::5], "o", ms=3, color=Q.line_color(tok), label=f"v = {vel}")
    ok = ~np.isnan(up)
    t_end = ts[ok][-1]
    tt = np.linspace(10, t_end, 50)
    pc.plot(tt, -up[ok][-1] + (2 - vel) * (tt - t_end), color=Q.line_color(tok), lw=1.0, ls=(0, (4, 2)))
pc.axhline(0, color=P.muted(), lw=0.7)
pc.set_xlim(0, 40)
pc.set_ylim(-20, 85)
C.style_axes(pc, "time t", "upstream advance of the edge")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "C", (21.0, 9.6))
bio.label(ax, (22.5, 9.2), "Upstream speed 2 sqrt(rD) - v", size="small", bold=True, ha="left")
