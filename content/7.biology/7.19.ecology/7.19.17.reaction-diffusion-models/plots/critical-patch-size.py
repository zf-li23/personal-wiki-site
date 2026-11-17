"""Critical patch size (the KISS model).

Scaled units: D = r = 1, so lengths are in units of sqrt(D/r) and L_c = pi.
A: steady states of u_t = u_xx + u(1 - u) on (0, L) with u = 0 at both ends (lethal surroundings),
for L = 4, 6, 10 and 20, found by running an implicit finite-difference scheme to t = 200 (dx = 0.02).
For L < pi the solution decays to zero.
B: the growth rate r - D pi^2 / L^2 of the slowest-decaying mode (line, left axis) and the mean density
of the steady state (points, right axis) against L: both become positive at L_c = pi.
C: critical length with a partially hostile matrix in which individuals die at rate mu (same D):
L_c = 2 sqrt(D/r) arctan(sqrt(mu/r)); it approaches pi sqrt(D/r) as mu grows and vanishes as mu -> 0.
"""

import numpy as np
from scipy.linalg import solve_banded

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 10.0)


def steady(L, dx=0.02, dt=0.2, T=200.0):
    m = int(round(L / dx)) - 1
    x = dx * np.arange(1, m + 1)
    u = 0.5 * np.sin(np.pi * x / L)
    lam = dt / dx**2
    ab = np.zeros((3, m))
    ab[0, 1:] = -lam
    ab[1, :] = 1 + 2 * lam
    ab[2, :-1] = -lam
    for _ in range(int(T / dt)):
        u = solve_banded((1, 1), ab, u + dt * u * (1 - u))
    return np.concatenate([[0], x, [L]]), np.concatenate([[0], u, [0]])


pa = C.axes_at(ax, (2.0, 1.6, 7.0, 6.8))
for L, tok in [(4, "negative"), (6, "protein"), (10, "enzyme"), (20, "dna")]:
    xx, uu = steady(L)
    pa.plot(xx, uu, color=Q.line_color(tok), lw=1.6, label=f"L = {L}")
pa.set_xlim(0, 20)
pa.set_ylim(0, 1.05)
C.style_axes(pa, "position x (units of sqrt(D/r))", "steady density u / K")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower center", ncol=4)
bio.panel(ax, "A", (0.3, 9.6))
bio.label(ax, (2.0, 9.2), "Steady states in a patch", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (12.0, 1.6, 7.0, 6.8))
Ls = np.linspace(1.2, 20, 300)
pb.plot(Ls, 1 - np.pi**2 / Ls**2, color=Q.line_color("dna"), lw=1.6)
pb.axhline(0, color=P.muted(), lw=0.7)
pb.axvline(np.pi, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pb.set_ylim(-1.0, 1.05)
pb.set_xlim(0, 20)
C.style_axes(pb, "patch length L", "growth rate of first mode")
pb.text(np.pi + 0.3, -0.85, "L_c = pi", fontsize=FS["tiny"], color=P.ink())
pb2 = pb.twinx()
Lp = [2.5, 3.0, 3.3, 3.6, 4, 5, 6, 8, 10, 14, 20]
mean = []
for L in Lp:
    xx, uu = steady(L, dx=0.05, dt=0.5, T=400.0)
    mean.append(np.trapezoid(uu, xx) / L)
pb2.plot(Lp, mean, "o", ms=4, color=Q.line_color("enzyme"))
pb2.set_ylim(-1.0, 1.05)
C.style_axes(pb2, None, "mean density of steady state", box=True)
pb2.spines["left"].set_visible(False)
bio.panel(ax, "B", (10.5, 9.6))
bio.label(ax, (12.0, 9.2), "Persistence threshold", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (22.5, 1.6, 7.0, 6.8))
mu = np.logspace(-2, 3, 300)
pc.semilogx(mu, 2 * np.arctan(np.sqrt(mu)), color=Q.line_color("protein"), lw=1.6)
pc.axhline(np.pi, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pc.text(0.012, np.pi + 0.08, "lethal matrix: pi sqrt(D/r)", fontsize=FS["tiny"], color=P.ink())
pc.set_ylim(0, 3.5)
pc.set_xlim(1e-2, 1e3)
C.style_axes(pc, "matrix mortality mu / r", "critical length L_c / sqrt(D/r)")
bio.panel(ax, "C", (21.0, 9.6))
bio.label(ax, (22.5, 9.2), "A partially hostile matrix", size="small", bold=True, ha="left")
