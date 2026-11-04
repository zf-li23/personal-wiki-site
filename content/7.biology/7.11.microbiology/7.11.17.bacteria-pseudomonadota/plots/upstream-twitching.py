"""Upstream twitching of Pseudomonas aeruginosa on a surface in flow (after the mechanism proposed by Shen
et al. 2012). A: type IV pili extend from the leading pole, attach to the surface and retract, pulling the
cell forward; the attached leading pole acts as a pivot, and the drag of the flow on the rest of the body
turns the trailing pole downstream, like a weathervane, so that the leading pole comes to point upstream.
B: a minimal model of this mechanism: each cell moves at speed v along its axis and its axis relaxes toward
the upstream direction at rate omega with rotational noise (Formula 17.5.1; v = 0.3 um/s, omega = 0.02 per s,
D_r = 0.005 per s; 25 cells, 15 min, starting at the origin with random orientations)."""
import numpy as np

import wikibio as bio
from wikibio import charts
from wikibio import microbio as M

P = bio.P
fig, ax = bio.canvas(24, 9)
bio.panel(ax, "A", (0.2, 8.8))
bio.panel(ax, "B", (12.8, 8.8))

# A: surface, flow, cell with pili at the upstream (left) pole
ax.fill_between([0.6, 11.6], 1.2, 1.9, color=P.light("neutral"), zorder=1, lw=0)
bio.label(ax, (6.1, 0.8), "surface", size="small", color=P.muted())
for y in (5.6, 6.6, 7.6):
    L = 1.2 + 0.6 * (y - 5.0)
    bio.arrow(ax, (2.0, y), (2.0 + L, y), kind="process", color=P.muted())
bio.label(ax, (1.0, 6.6), "flow", size="small", ha="left", color=P.muted())
M.bacillus(ax, (6.6, 2.55), 3.2, 1.0, gram="-")
for xe, ye, bend in [(3.3, 1.9, 0.35), (3.9, 1.9, 0.25), (4.4, 1.9, 0.15)]:
    tt = np.linspace(0, 1, 30)
    xs = 5.05 + (xe - 5.05) * tt
    ys = 2.55 + (ye - 2.55) * tt + bend * np.sin(np.pi * tt)
    ax.plot(xs, ys, color=P.edge("flagellum"), lw=1.0, zorder=7)
bio.callout(ax, (3.3, 1.92), (2.4, 3.8), "type IV pili attach and retract", size="tiny")
bio.arrow(ax, (5.6, 3.6), (3.8, 3.6), kind="process", color=P.edge("positive"))
bio.label(ax, (4.7, 4.05), "movement", size="tiny", color=P.edge("positive"))
bio.arrow(ax, (8.3, 3.4), (9.3, 2.7), kind="process", bend=-0.3, color=P.edge("negative"))
bio.label(ax, (9.6, 3.6), "drag turns the trailing pole", size="tiny", ha="left", color=P.edge("negative"))
bio.label(ax, (9.6, 3.2), "downstream", size="tiny", ha="left", color=P.edge("negative"))

# B: model trajectories
rng = np.random.default_rng(4)
v, omega, Dr, dt, T = 0.3, 0.02, 0.005, 1.0, 900
pax = charts.axes_at(ax, (14.4, 1.5, 8.8, 6.6))
ends = []
for i in range(25):
    phi = rng.uniform(-np.pi, np.pi)  # angle of the leading pole; pi = upstream (-x)
    x = y = 0.0
    xs, ys = [x], [y]
    for _ in range(int(T / dt)):
        phi += -omega * np.sin(phi - np.pi) * dt + np.sqrt(2 * Dr * dt) * rng.normal()
        x += v * np.cos(phi) * dt
        y += v * np.sin(phi) * dt
        xs.append(x)
        ys.append(y)
    pax.plot(xs, ys, color=charts.line("enzyme"), lw=0.8, alpha=0.75)
    pax.plot(xs[-1], ys[-1], "o", ms=2.5, color=charts.line("enzyme"))
    ends.append(xs[-1])
pax.plot(0, 0, "o", ms=4, color=P.ink())
pax.annotate("", xy=(120, -110), xytext=(40, -110), arrowprops=dict(arrowstyle="->", color=P.muted()))
pax.text(80, -100, "flow", fontsize=6.8, ha="center", color=P.muted())
pax.set_xlim(-270, 130)
pax.set_ylim(-150, 150)
pax.set_aspect("equal")
charts.style_axes(pax, "x / µm (flow to the right)", "y / µm")
pax.text(-260, 128, f"{np.mean(np.array(ends) < 0) * 100:.0f} % of cells end upstream", fontsize=6.8, color=P.ink())
