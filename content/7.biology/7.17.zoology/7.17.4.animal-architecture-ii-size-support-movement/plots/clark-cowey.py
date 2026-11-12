"""The Clark-Cowey model of a worm whose body wall is reinforced by a lattice of inextensible helical fibres.

Take one turn of fibre of fixed length D wound around a cylinder at angle theta to the long axis. The turn
covers a length l = D cos(theta) of the body and a circumference 2 pi r = D sin(theta), so the volume it
encloses is V = D^3 sin^2(theta) cos(theta) / (4 pi), maximal at tan(theta) = sqrt(2), theta = 54 deg 44 min
(Clark & Cowey 1958, J. Exp. Biol. 35: 731). The aspect ratio of the cylinder is l / 2r = pi cot(theta).
A worm of fixed volume V < V_max (horizontal line; illustrative value 0.4 V_max) can keep a circular cross
section only between the two fibre angles where the curve crosses the line: elongating beyond the smaller
angle is impossible, and contracting beyond the larger one forces the body to flatten (its section becomes
elliptical, enclosing less than the cylinder). Nemerteans work close to the curve over a wide range of
angles; flatworms, far below it, are flat at all lengths. Glyphs: cylinders drawn to the aspect ratio of
three fibre angles.
"""

import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(22.0, 10.0)
p = quant.Plot(ax, (2.0, 1.5, 10.0, 7.4), xlim=(0, 90), ylim=(0, 1.1), xlabel="fibre angle θ / degrees",
               ylabel="volume enclosed / V$_{max}$", xticks=[0, 30, 54.7, 90], yticks=[0, 0.5, 1.0])
th = np.radians(np.linspace(0.5, 89.5, 300))
v = np.sin(th) ** 2 * np.cos(th)
vmax = v.max()
p.line(np.degrees(th), v / vmax, "dna")
p.vline(54.74, text="54°44′", top=True)
level = 0.4
p.hline(level, text="worm volume", side="right")
cross = np.degrees(th)[np.where(np.diff(np.sign(v / vmax - level)))[0]]
p.span(0, cross[0], "neutral")
p.span(cross[0], cross[1], "positive")
p.text(cross[0] / 2, 0.75, "cannot\nelongate\nfurther", size="tiny")
p.text(54.7, 0.2, "circular section possible", size="tiny")
p.span(cross[1], 90, "negative")
p.text((cross[1] + 90) / 2, 0.75, "flattens", size="tiny")

# glyphs: cylinders with crossing helical fibres drawn at the corresponding aspect ratio
from matplotlib.patches import FancyBboxPatch


def worm(cx, cy, theta_deg, area=1.6):
    t = np.radians(theta_deg)
    aspect = np.pi / np.tan(t)
    h = np.sqrt(area / aspect)
    w = h * aspect
    r = min(h, w) * 0.3
    body = FancyBboxPatch((cx - w / 2, cy - h / 2), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                          facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=1.2, zorder=10)
    ax.add_patch(body)
    dx = h / np.tan(t)  # horizontal run of a fibre that crosses the visible face once
    step = max(w, dx) / 7
    for s in (1, -1):
        for x0 in np.arange(cx - w / 2 - dx - step, cx + w / 2 + dx + step, step):
            ln, = ax.plot([x0, x0 + s * dx], [cy - h / 2, cy + h / 2], color=P.edge("animal"), lw=0.6, zorder=11)
            ln.set_clip_path(body)
    bio.label(ax, (cx, cy - h / 2 - 0.35), f"θ = {theta_deg}°", size="tiny")


worm(17.0, 8.0, 25)
worm(17.0, 5.0, 54.7)
worm(17.0, 2.3, 80)
bio.label(ax, (17.0, 9.5), "Body shape at three fibre angles", size="small", bold=True)
