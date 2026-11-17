"""Finite differences for u_t = D u_xx + f(u).

A: the space-time grid (x_i = i dx, t_n = n dt) with the stencils of the explicit scheme (forward in
time, centred in space: u_i^{n+1} from u_{i-1}^n, u_i^n, u_{i+1}^n) and the implicit scheme
(u_{i-1}^{n+1}, u_i^{n+1}, u_{i+1}^{n+1} coupled to u_i^n).
B: von Neumann amplification factors of one step for the Fourier mode exp(i k x), against k dx, with
lambda = D dt / dx^2: explicit G = 1 - 4 lambda sin^2(k dx / 2) for lambda = 0.25, 0.5 and 0.6, implicit
G = 1 / (1 + 4 lambda sin^2) and Crank-Nicolson G = (1 - 2 lambda s) / (1 + 2 lambda s) for lambda = 2.
The explicit scheme is stable when |G| <= 1 for all modes, i.e. lambda <= 1/2.
C: the explicit scheme applied to the heat equation (D = 1, dx = 0.05, zero-flux ends) from a step plus
1 % random noise, after 60 steps: lambda = 0.48 gives a smooth profile, lambda = 0.52 lets the shortest
mode (k dx = pi) grow by |G| = 1.08 per step.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(0)
fig, ax = bio.canvas(30.0, 10.0)

x0, y0, s = 1.2, 1.8, 1.05
for i in range(7):
    ax.plot([x0 + i * s, x0 + i * s], [y0, y0 + 5 * s], color=P.muted(), lw=0.6)
for n in range(6):
    ax.plot([x0, x0 + 6 * s], [y0 + n * s, y0 + n * s], color=P.muted(), lw=0.6)
for i in range(7):
    for n in range(6):
        ax.plot(x0 + i * s, y0 + n * s, "o", ms=2.2, color=P.muted())


def stencil(points, target, tok):
    col = Q.line_color(tok)
    for (i, n) in points:
        ax.plot(x0 + i * s, y0 + n * s, "o", ms=6, color=col)
        ax.plot([x0 + i * s, x0 + target[0] * s], [y0 + n * s, y0 + target[1] * s], color=col, lw=1.4)
    ax.plot(x0 + target[0] * s, y0 + target[1] * s, "s", ms=7, color=col)


stencil([(1, 1), (2, 1), (3, 1)], (2, 2), "dna")
stencil([(3, 4), (5, 4), (4, 3)], (4, 4), "negative")
ax.text(x0 + 2 * s, y0 + 2 * s + 0.35, "explicit", fontsize=FS["tiny"], color=Q.line_color("dna"), ha="center")
ax.text(x0 + 4 * s, y0 + 4 * s + 0.35, "implicit", fontsize=FS["tiny"], color=Q.line_color("negative"),
        ha="center")
ax.annotate("", xy=(x0 + 6.6 * s, y0 - 0.5), xytext=(x0 - 0.2, y0 - 0.5),
            arrowprops=dict(arrowstyle="->", color=P.ink(), lw=0.9))
ax.text(x0 + 6.7 * s, y0 - 0.5, "x_i", fontsize=FS["small"], color=P.ink(), va="center")
ax.annotate("", xy=(x0 - 0.5, y0 + 5.6 * s), xytext=(x0 - 0.5, y0 - 0.2),
            arrowprops=dict(arrowstyle="->", color=P.ink(), lw=0.9))
ax.text(x0 - 0.5, y0 + 5.8 * s, "t_n", fontsize=FS["small"], color=P.ink(), ha="center")
bio.panel(ax, "A", (0.3, 9.6))
bio.label(ax, (1.2, 9.2), "Grid and stencils", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (12.0, 1.6, 7.0, 6.8))
th = np.linspace(0, np.pi, 300)
sn = np.sin(th / 2) ** 2
for lam, tok in [(0.25, "dna"), (0.5, "enzyme"), (0.6, "negative")]:
    pb.plot(th, 1 - 4 * lam * sn, color=Q.line_color(tok), lw=1.6, label=f"explicit, lambda = {lam}")
pb.plot(th, 1 / (1 + 8 * sn), color=Q.line_color("protein"), lw=1.4, ls=(0, (4, 2)), label="implicit, lambda = 2")
pb.plot(th, (1 - 4 * sn) / (1 + 4 * sn), color=Q.line_color("positive"), lw=1.4, ls=(0, (1, 1.5)),
        label="Crank-Nicolson, lambda = 2")
pb.axhspan(-1, 1, color=P.fill("highlight"), alpha=0.25, lw=0)
pb.axhline(-1, color=P.muted(), lw=0.7)
pb.set_xlim(0, np.pi)
pb.set_ylim(-1.5, 1.1)
pb.set_xticks([0, np.pi / 2, np.pi])
pb.set_xticklabels(["0", "pi/2", "pi"])
C.style_axes(pb, "k dx", "amplification factor G")
pb.legend(frameon=False, fontsize=FS["tiny"] - 1, labelcolor=P.ink(), loc="lower left")
bio.panel(ax, "B", (10.5, 9.6))
bio.label(ax, (12.0, 9.2), "Von Neumann analysis", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (22.5, 1.6, 7.0, 6.8))
dx = 0.05
x = np.arange(0, 5 + dx / 2, dx)
u0 = np.where(x < 2.5, 1.0, 0.0) + 0.01 * rng.standard_normal(x.size)
for lam, tok in [(0.48, "dna"), (0.52, "negative")]:
    u = u0.copy()
    for _ in range(60):
        up = np.concatenate([[u[1]], u, [u[-2]]])
        u = u + lam * (up[2:] - 2 * u + up[:-2])
    pc.plot(x, u, color=Q.line_color(tok), lw=1.2, label=f"lambda = {lam}")
pc.set_xlim(0, 5)
pc.set_ylim(-0.6, 1.6)
C.style_axes(pc, "x", "u after 60 steps")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left")
bio.panel(ax, "C", (21.0, 9.6))
bio.label(ax, (22.5, 9.2), "Stability in practice", size="small", bold=True, ha="left")
