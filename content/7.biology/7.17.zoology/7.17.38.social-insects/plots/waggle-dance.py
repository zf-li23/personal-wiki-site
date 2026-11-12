# Waggle dance encoding (schematic). Left: field view from above; food at angle alpha to the right of the
# sun's azimuth. Right: vertical comb; waggle runs at alpha to the right of upward vertical, return loops
# alternately left and right. Bottom: waggle duration vs distance, roughly 1 s per km (schematic).
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(20, 14)
ink, mut = P.ink(), P.muted()
alpha = np.radians(50)
# field panel
hive = np.array([4.5, 8.0])
bio.label(ax, (4.5, 13.3), "Field (seen from above)", size="normal", bold=True)
sun = hive + 4.0 * np.array([0, 1])
ax.plot(*sun, marker="o", ms=16, color=P.fill("atp"), mec=P.edge("atp"), zorder=6)
bio.label(ax, (sun[0] + 1.0, sun[1]), "sun azimuth", size="small", color=mut, ha="left")
food = hive + 4.0 * np.array([np.sin(alpha), np.cos(alpha)])
ax.plot(*food, marker="*", ms=16, color=P.fill("plant"), mec=P.edge("plant"), zorder=6)
bio.label(ax, (food[0] + 0.4, food[1] - 0.5), "food", size="small", color=P.edge("plant"), ha="left")
bio.box(ax, hive, 1.2, 0.8, token="atp", text="hive", size="small")
bio.arrow(ax, hive + [0, 0.5], sun - [0, 0.5], kind="process", color=mut, dashed=True)
bio.arrow(ax, hive + [0.3, 0.4], food - 0.4 * np.array([np.sin(alpha), np.cos(alpha)]), kind="process", color=P.edge("plant"))
t = np.linspace(np.pi / 2, np.pi / 2 - alpha, 30)
ax.plot(hive[0] + 1.8 * np.cos(t), hive[1] + 1.8 * np.sin(t), color=ink, lw=1)
bio.label(ax, (hive[0] + 1.15, hive[1] + 2.05), "α", size="normal")
# comb panel
c = np.array([14.5, 9.0])
bio.label(ax, (14.5, 13.3), "Vertical comb (inside the hive)", size="normal", bold=True)
ax.add_patch(__import__("matplotlib").patches.FancyBboxPatch((10.8, 5.6), 7.4, 7.0, boxstyle="round,pad=0.1",
             facecolor=P.light("atp"), edgecolor=P.edge("atp"), lw=0.8, zorder=1))
bio.arrow(ax, (11.6, 6.4), (11.6, 9.4), kind="process", color=mut)
bio.label(ax, (11.6, 9.8), "up", size="small", color=mut)
u = np.array([np.sin(alpha), np.cos(alpha)])
n = np.array([u[1], -u[0]])
p0, p1 = c - 1.6 * u, c + 1.6 * u
xs = np.linspace(0, 1, 120)
wig = 0.15 * np.sin(xs * 2 * np.pi * 7)
pts = p0[None, :] + xs[:, None] * (p1 - p0)[None, :] + wig[:, None] * n[None, :]
ax.plot(pts[:, 0], pts[:, 1], color=P.edge("negative"), lw=1.6, zorder=6)
for side in (1, -1):
    th = np.linspace(0, np.pi, 60)
    mid = c + side * 1.1 * n
    loop = mid[None, :] + 1.6 * np.cos(th)[:, None] * u[None, :] + side * 1.1 * np.sin(th)[:, None] * n[None, :]
    ax.plot(loop[:, 0], loop[:, 1], color=mut, lw=1, ls="--", zorder=5)
ax.plot([c[0], c[0]], [c[1], c[1] + 2.6], color=ink, lw=0.8, ls=":")
t2 = np.linspace(np.pi / 2, np.pi / 2 - alpha, 30)
ax.plot(c[0] + 1.2 * np.cos(t2), c[1] + 1.2 * np.sin(t2), color=ink, lw=1)
bio.label(ax, (c[0] + 0.75, c[1] + 1.45), "α", size="normal")
bio.label(ax, (p1[0] + 0.6, p1[1] + 0.2), "waggle run", size="small", color=P.edge("negative"), ha="left")
bio.label(ax, (c[0] + 1.6, c[1] - 3.0), "return loops", size="small", color=mut)
# calibration
b = charts.axes_at(ax, (3.0, 0.9, 15.0, 3.4))
d = np.linspace(0, 5, 50)
b.plot(d, 1.0 * d + 0.1, color=P.edge("negative"), lw=1.8)
b.set_xlabel("Distance to food (km)", fontsize=7)
b.set_ylabel("Waggle run (s)", fontsize=7)
b.tick_params(labelsize=6)
b.text(0.1, 4.2, "schematic: about 1 s per km; slope varies among subspecies", fontsize=6, color=mut)
