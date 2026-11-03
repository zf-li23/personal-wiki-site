"""Fisher's runaway in a simplified Lande (1981) model (Theorem 13.2.1).

Male trait mean zbar, female preference mean ybar. beta = (ybar - zbar)/nu^2 - (zbar - theta)/omega^2,
dz = G beta / 2, dy = B beta / 2. theta = 0, nu^2 = 1, omega^2 = 2: the line of equilibria
ybar = 1.5 zbar. A: B/G = 0.8 (approach to the line). B: B/G = 2.5 (runaway). G = 0.1.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
theta, nu2, om2, G = 0.0, 1.0, 2.0, 0.1
slope = 1 + nu2 / om2


def run(z, y, ratio, steps=3000, lim=6.0):
    B = ratio * G
    zs, ys = [z], [y]
    for _ in range(steps):
        beta = (y - z) / nu2 - (z - theta) / om2
        z, y = z + G * beta / 2, y + B * beta / 2
        zs.append(z)
        ys.append(y)
        if abs(z) > lim or abs(y) > lim:
            break
    return np.array(zs), np.array(ys)


fig, ax = bio.canvas(30.0, 12.0)
starts_a = [(-3.0, -1.0), (-2.0, -3.0), (2.0, 0.0), (3.0, 3.0), (0.0, -1.0), (-1.0, 1.0), (-3.5, -2.5)]
starts_b = [(-2.0, 1.0), (-1.0, 2.0), (0.5, 3.0), (2.0, 1.0), (1.0, -1.5), (-0.5, -2.5), (2.5, 2.0), (-2.5, -1.5)]
for k, (ratio, title, x0) in enumerate(((0.8, "B/G = 0.8: a line of equilibria", 2.4),
                                         (2.5, "B/G = 2.5: runaway", 17.4))):
    p = C.axes_at(ax, (x0, 1.6, 10.6, 8.8))
    zz = np.linspace(-4, 4, 10)
    p.plot(zz, theta + slope * (zz - theta), color=P.muted(), lw=2.6, alpha=0.6)
    for (z0, y0) in (starts_a if ratio < slope else starts_b):
        zs, ys = run(z0, y0, ratio)
        p.plot(zs, ys, color=C.line("rna"), lw=1.4)
        p.plot([z0], [y0], "o", ms=3.5, color=C.line("rna"))
        if len(zs) > 3:
            i = min(len(zs) - 2, max(1, len(zs) // 3))
            p.annotate("", xy=(zs[i + 1], ys[i + 1]), xytext=(zs[i], ys[i]),
                       arrowprops=dict(arrowstyle="-|>", color=C.line("rna"), lw=1.2, mutation_scale=10))
        p.plot([zs[-1]], [ys[-1]], "s" if ratio < slope else "", ms=3.5, color=P.ink())
    p.set_xlim(-4, 4)
    p.set_ylim(-4, 4)
    C.style_axes(p, "mean male trait z̄", "mean female preference ȳ", box=True)
    p.text(2.0, 3.6, "line of\nequilibria", color=P.muted(), fontsize=FS["tiny"], ha="left", va="top")
    bio.panel(ax, "AB"[k], (x0 - 2.2, 11.6))
    bio.label(ax, (x0, 11.2), title, size="small", bold=True, ha="left")
