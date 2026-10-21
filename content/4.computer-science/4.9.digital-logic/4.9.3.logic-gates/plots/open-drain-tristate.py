"""Sharing one wire. Left: open-drain outputs with a pull-up resistor; any output
that turns its transistor on pulls the line low (wired-AND). Right: tri-state
buffers on a bus; at most one enable may be active, the others are high impedance."""

import numpy as np
import matplotlib.pyplot as plt

FG = plt.rcParams["text.color"]


def line(ax, *pts):
    xs, ys = zip(*pts)
    ax.plot(xs, ys, color=FG, lw=1.3, solid_capstyle="round")


def dot(ax, p):
    ax.plot(*p, "o", color=FG, ms=4)


def text(ax, p, s, **kw):
    kw.setdefault("ha", "center")
    kw.setdefault("va", "center")
    kw.setdefault("fontsize", 10)
    ax.text(p[0], p[1], s, color=FG, **kw)


def nmos(ax, x, y):
    line(ax, (x, y - 0.3), (x, y + 0.3))
    line(ax, (x, y + 0.22), (x + 0.3, y + 0.22), (x + 0.3, y + 0.5))
    line(ax, (x, y - 0.22), (x + 0.3, y - 0.22), (x + 0.3, y - 0.5))
    line(ax, (x - 0.1, y - 0.25), (x - 0.1, y + 0.25))
    line(ax, (x - 0.6, y), (x - 0.1, y))
    return (x + 0.3, y + 0.5), (x + 0.3, y - 0.5), (x - 0.6, y)


def resistor(ax, x, y0, y1):
    ys = np.linspace(y0, y1, 14)
    xs = [x] + [x + (0.12 if k % 2 else -0.12) for k in range(1, 13)] + [x]
    line(ax, *zip(xs, ys))


def ground(ax, p):
    x, y = p
    for k, w in enumerate((0.2, 0.13, 0.06)):
        line(ax, (x - w, y - 0.08 * k), (x + w, y - 0.08 * k))


fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))

ax = axes[0]
bus_y = 0.9
for k, x in enumerate((-1.0, 0.6)):
    top, bot, gate = nmos(ax, x, 0.0)
    line(ax, top, (top[0], bus_y))
    dot(ax, (top[0], bus_y))
    ground(ax, bot)
    text(ax, (gate[0] - 0.25, gate[1]), r"$\overline{a_%d}$" % (k + 1))
line(ax, (-1.4, bus_y), (2.2, bus_y))
resistor(ax, 1.7, bus_y, 2.0)
dot(ax, (1.7, bus_y))
line(ax, (1.45, 2.0), (1.95, 2.0))
text(ax, (1.7, 2.2), "VDD")
text(ax, (2.05, 1.45), "R pull-up", ha="left", fontsize=9)
text(ax, (2.3, bus_y), "Y", ha="left")
text(ax, (0.4, -1.15), r"$Y = a_1 a_2$  (low if any transistor is on)", fontsize=9)
ax.set_title("open-drain outputs: wired-AND", fontsize=10)
ax.set_xlim(-2.0, 3.0)
ax.set_ylim(-1.4, 2.5)

ax = axes[1]
bus_y = 1.6
for k, x in enumerate((-0.8, 1.2)):
    y = 0.3
    tri = [(x, y - 0.35), (x, y + 0.35), (x + 0.6, y), (x, y - 0.35)]
    line(ax, *tri)
    line(ax, (x - 0.5, y), (x, y))
    text(ax, (x - 0.75, y), f"D{k + 1}")
    line(ax, (x + 0.6, y), (x + 0.9, y), (x + 0.9, bus_y))
    dot(ax, (x + 0.9, bus_y))
    line(ax, (x + 0.3, y - 0.18), (x + 0.3, y - 0.8))
    text(ax, (x + 0.3, y - 1.0), f"EN{k + 1}")
line(ax, (-1.2, bus_y), (2.8, bus_y))
text(ax, (2.9, bus_y), "bus", ha="left")
text(ax, (0.8, -1.15), "EN1 = 1, EN2 = 0: D1 drives the bus", fontsize=9)
ax.set_title("tri-state buffers on a shared bus", fontsize=10)
ax.set_xlim(-1.8, 3.6)
ax.set_ylim(-1.4, 2.5)

for ax in axes:
    ax.set_aspect("equal")
    ax.axis("off")
fig.tight_layout()
