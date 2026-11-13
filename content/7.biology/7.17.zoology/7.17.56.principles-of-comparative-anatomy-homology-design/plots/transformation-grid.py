# A transformation grid in the manner of D'Arcy Thompson (1917), schematic. Left: a generalized laterally
# compressed fish outline on a square Cartesian grid. Right: the same outline and grid after one smooth
# coordinate transformation, a shear x' = x + 0.35 y combined with a dorsoventral stretch that grows toward
# the tail, y' = y (1 + 0.25 x / 6). Every grid line and every point of the outline is carried by the same
# mapping, which is Thompson's point: related shapes can differ by a global deformation rather than by
# independent changes of parts.
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24, 9)

t = np.linspace(0, 2 * np.pi, 400)
# fish body: head at x=0, tail at x=6; centreline y=0
xb = 3 + 3 * np.cos(t)
yb = 1.5 * np.sin(t) * (1 - 0.35 * (xb / 6)) * np.sqrt(np.clip(1 - ((xb - 3) / 3.05) ** 6, 0, 1)) ** 0.2
tail_x = np.array([5.6, 7.2, 6.7, 7.2, 5.6])
tail_y = np.array([0.25, 1.3, 0.0, -1.3, -0.25])
eye = (0.8, 0.35)


def T(x, y):
    return x + 0.35 * y, y * (1 + 0.25 * x / 6)


def draw(x0, y0, f):
    for gx in np.arange(-0.5, 8.01, 0.5):
        yy = np.linspace(-2.2, 2.2, 60)
        X, Y = f(np.full_like(yy, gx), yy)
        ax.plot(x0 + X, y0 + Y, color=P.muted(), lw=0.5, zorder=2)
    for gy in np.arange(-2.0, 2.01, 0.5):
        xx = np.linspace(-0.5, 8.0, 80)
        X, Y = f(xx, np.full_like(xx, gy))
        ax.plot(x0 + X, y0 + Y, color=P.muted(), lw=0.5, zorder=2)
    X, Y = f(xb, yb)
    ax.fill(x0 + X, y0 + Y, color=P.fill("animal"), zorder=4, lw=0)
    ax.plot(x0 + X, y0 + Y, color=P.edge("animal"), lw=1.4, zorder=5)
    X, Y = f(tail_x, tail_y)
    ax.fill(x0 + X, y0 + Y, color=P.fill("animal"), zorder=4, lw=0)
    ax.plot(x0 + X, y0 + Y, color=P.edge("animal"), lw=1.4, zorder=5)
    ex, ey = f(np.array([eye[0]]), np.array([eye[1]]))
    ax.plot(x0 + ex, y0 + ey, "o", color=P.ink(), ms=4, zorder=6)


draw(2.0, 4.5, lambda x, y: (x, y))
draw(14.0, 4.5, T)
bio.label(ax, (5.75, 8.3), "Original outline", size="small", bold=True)
bio.label(ax, (18.6, 8.3), "After one coordinate transformation", size="small", bold=True)
bio.arrow(ax, (10.6, 4.5), (12.6, 4.5), kind="process")
bio.label(ax, (11.6, 5.1), "x' = x + ky", size="tiny")
bio.label(ax, (11.6, 3.9), "y' = y(1 + cx)", size="tiny")
