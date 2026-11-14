"""Rock-paper-scissors dynamics of the three male morphs of the side-blotched lizard (Uta stansburiana).

Orange (O) beats blue (B), blue beats yellow (Y), yellow beats orange. The winner of a pairing gains a, the
loser loses b, payoff matrix A = [[0, a, -b], [-b, 0, a], [a, -b, 0]] in the order (O, B, Y), replicator dynamics
dx_i/dt = x_i [(A x)_i - x^T A x]. A: a = b (zero-sum): the product x_O x_B x_Y is conserved and the population
cycles on closed orbits around (1/3, 1/3, 1/3). B: a = 0.8, b = 1: losing costs more than winning gains, and the
population spirals out towards the boundary, each morph in turn becoming nearly fixed. C: morph frequencies
over time for B.
"""

import numpy as np
from matplotlib.patches import Polygon

import wikibio as bio
from wikibio import charts as Ch
from wikibio import quant

P = bio.P
FS = bio.core.FONT
NAMES = ["orange", "blue", "yellow"]
TOK = ["rna", "dna", "atp"]


def matrix(a, b):
    return np.array([[0, a, -b], [-b, 0, a], [a, -b, 0]], float)


def flow(A, x0, t):
    def rhs(_, x):
        f = A @ x
        return x * (f - x @ f)
    return quant.odeint_rk4(rhs, np.array(x0, float), t)


fig, ax = bio.canvas(33.0, 11.0)


def simplex(cx, letter, title):
    w = 8.8
    v = [np.array([cx - w / 2, 1.6]), np.array([cx + w / 2, 1.6]), np.array([cx, 1.6 + w * np.sqrt(3) / 2])]
    ax.add_patch(Polygon(v, closed=True, facecolor=P.mix(P.fill("neutral"), P.surface(), 0.75),
                         edgecolor=P.muted(), lw=0.9, zorder=2))
    for k, (dx, dy, ha) in enumerate(((0, -0.5, "center"), (0, -0.5, "center"), (0, 0.35, "center"))):
        bio.label(ax, (v[k][0] + dx, v[k][1] + dy), NAMES[k], size="small", bold=True,
                  color=quant.line_color(TOK[k]), ha=ha)
    bio.panel(ax, letter, (cx - w / 2 - 0.9, 10.8))
    bio.label(ax, (cx, 10.55), title, size="small", bold=True)
    return lambda x: np.atleast_2d(x) @ np.array(v)


to = simplex(5.6, "A", "a = b: neutral cycles")
for r in (0.05, 0.12, 0.2, 0.27):
    x = flow(matrix(1, 1), [1 / 3 + r, 1 / 3 - r / 2, 1 / 3 - r / 2], np.linspace(0, 12, 3000))
    xy = to(x)
    ax.plot(xy[:, 0], xy[:, 1], color=quant.line_color("ink"), lw=1.0, zorder=5)
    k = 400
    bio.arrow(ax, xy[k - 4], xy[k + 4], kind="process", color=quant.line_color("ink"), lw=0, head=0.25, zorder=6)
c = to([1 / 3, 1 / 3, 1 / 3])[0]
ax.plot(*c, "o", color=P.ink(), ms=3, zorder=7)

to2 = simplex(16.6, "B", "a < b: spiral towards the boundary")
t = np.linspace(0, 120, 24000)
x = flow(matrix(0.8, 1.0), [0.36, 0.33, 0.31], t)
xy = to2(x)
ax.plot(xy[:, 0], xy[:, 1], color=quant.line_color("ink"), lw=0.9, zorder=5)
for k in (2000, 9000, 16000):
    bio.arrow(ax, xy[k - 6], xy[k + 6], kind="process", color=quant.line_color("ink"), lw=0, head=0.25, zorder=6)

pc = Ch.axes_at(ax, (24.6, 2.2, 7.6, 7.4))
for i in range(3):
    pc.plot(t, x[:, i], color=Ch.line(TOK[i]), lw=1.4, label=NAMES[i])
pc.set_xlim(0, 120)
pc.set_ylim(0, 1)
Ch.style_axes(pc, "time (arbitrary units)", "morph frequency")
leg = pc.legend(fontsize=FS["tiny"], frameon=False, loc="upper left", ncol=3)
for txt in leg.get_texts():
    txt.set_color(P.ink())
bio.panel(ax, "C", (23.0, 10.8))
