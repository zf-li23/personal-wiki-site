"""Dynamics at low resolution: Boolean versions of continuous models.

A: predator-prey (Lotka-Volterra) dynamics reduced to two Boolean variables (a predator, h prey).
Left, with the epsilon-modification of text (variant 1): a' = h, h' = not a, a single 4-cycle
00 -> 01 -> 11 -> 10 -> 00 (the discrete counterpart of the closed orbits). Right (variant 2):
a' = h, h' = a xor h: the state 00 becomes a fixed point and the other three form a 3-cycle.
B: "diffusion" as a cellular automaton on a line, from the rule that a_n follows the sign of
a_{n+1} - 2 a_n + a_{n-1} (unchanged when it is zero): a'_n = a_{n-1} a_n a_{n+1} + not(a_n) (a_{n-1}
or a_{n+1}); 41 sites, initial block of 4 occupied sites, 18 steps (time downwards): the front
spreads at one site per step while the coarse-grained density falls.
C: a Lindenmayer-type growing automaton: each new row is the previous one with each cell replaced by
(cell xor left neighbour) and one cell added at the right, starting from a single 1: the
Sierpinski pattern of Pascal's triangle mod 2.
"""

import numpy as np

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(32.0, 11.0)
bio.panel(ax, "A", (0.1, 10.9))


def graph(cx, mapping, title):
    pos = {"00": (cx - 1.6, 7.8), "01": (cx + 1.6, 7.8), "11": (cx + 1.6, 4.4), "10": (cx - 1.6, 4.4)}
    for s, xy in pos.items():
        fixed = mapping[s] == s
        bio.box(ax, xy, 1.3, 0.8, "positive" if fixed else "neutral", text=s, size="small")
    for s, xy in pos.items():
        t = mapping[s]
        if t == s:
            ax.annotate("", xy=(xy[0] + 0.45, xy[1] + 0.42), xytext=(xy[0] - 0.45, xy[1] + 0.42),
                        arrowprops=dict(arrowstyle="->", color=P.ink(), lw=1.0, connectionstyle="arc3,rad=-1.2"))
        else:
            bio.arrow(ax, xy, pos[t], kind="process", shrink=0.7)
    bio.label(ax, (cx, 2.9), title, size="tiny")


graph(2.6, {"00": "01", "01": "11", "11": "10", "10": "00"}, "a′ = h,  h′ = not a")
graph(8.4, {"00": "00", "01": "11", "11": "10", "10": "01"}, "a′ = h,  h′ = a xor h")
bio.label(ax, (5.5, 9.9), "states (a h): predator, prey", size="tiny", color=P.muted())

from matplotlib.colors import to_rgba

bio.panel(ax, "B", (12.2, 10.9))
N, steps = 41, 18
a = np.zeros(N, int)
a[18:22] = 1
rows = [a.copy()]
for _ in range(steps):
    l = np.r_[0, a[:-1]]
    r = np.r_[a[1:], 0]
    a = ((l & a & r) | ((1 - a) & (l | r))).astype(int)
    rows.append(a.copy())
img = np.zeros((steps + 1, N, 4))
img[np.array(rows) == 1] = to_rgba(P.fill("ectoderm"))
ax.imshow(img, extent=(13.0, 21.2, 1.4, 9.6), origin="upper", interpolation="nearest", zorder=2)
bio.label(ax, (17.1, 0.8), "position →   (time runs downwards)", size="tiny")

bio.panel(ax, "C", (22.4, 10.9))
M = 32
rows = []
row = [1]
for k in range(M):
    rows.append(row + [0] * (M - len(row)))
    new = [row[0]] + [row[i] ^ row[i - 1] for i in range(1, len(row))] + [row[-1]]
    row = new
img = np.zeros((M, M, 4))
img[np.array(rows) == 1] = to_rgba(P.fill("plant"))
ax.imshow(img, extent=(23.2, 31.4, 1.4, 9.6), origin="upper", interpolation="nearest", zorder=2)
bio.label(ax, (27.3, 0.8), "growing row, apex at the left", size="tiny")
