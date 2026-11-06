# The syconium of the fig and the life cycle of its pollinating wasp (schematic). Left: longitudinal
# section of the syconium: the ostiole at the top closed by bracts; male flowers on the upper inner wall,
# long-styled female flowers and short-styled gall flowers lower down. Right: the cycle: a pollen-bearing
# female wasp enters, pollinates the female flowers and lays eggs in the gall flowers, larvae develop in
# the galls, wingless males mate with the females and chew exit tunnels, and females load pollen from the
# now-mature male flowers and fly to a receptive syconium on another tree.
import math

import numpy as np
import wikibio as bio
from matplotlib.patches import Circle, Ellipse, Polygon

P = bio.P
fig, ax = bio.canvas(34, 14)
cx, cy = 7.0, 6.6
t = np.linspace(math.pi / 2 + 0.22, 5 * math.pi / 2 - 0.22, 160)
R = 5.0
outer = [(cx + R * 0.95 * math.cos(a), cy + R * math.sin(a) * (1.05 if math.sin(a) > 0 else 1.0)) for a in t]
inner = [(cx + (R - 1.0) * 0.95 * math.cos(a), cy + (R - 1.0) * math.sin(a)) for a in t[::-1]]
ax.add_patch(Polygon(outer + inner, closed=True, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.2, zorder=3))
ax.add_patch(Polygon(inner, closed=True, facecolor=P.light("plant"), edgecolor="none", zorder=2))
for s in (-1, 1):
    for k in range(3):
        ax.add_patch(Ellipse((cx + s * (0.35 + 0.25 * k), cy + R + 0.1 - 0.35 * k), 0.9, 0.3, angle=-s * 30,
                             facecolor=P.fill("bract"), edgecolor=P.edge("bract"), lw=0.8, zorder=4))
ax.plot([cx, cx], [cy - R, cy - R - 1.2], color=P.edge("plant"), lw=2.4, zorder=2)
rng = np.random.default_rng(0)
for a in np.linspace(math.pi / 2 + 0.4, 5 * math.pi / 2 - 0.4, 30):
    base = np.array([cx + (R - 1.0) * 0.95 * math.cos(a), cy + (R - 1.0) * math.sin(a)])
    inward = np.array([cx, cy]) - base
    inward /= np.linalg.norm(inward)
    if math.sin(a) > 0.55:
        tip = base + inward * 0.6
        ax.plot(*zip(base, tip), color=P.edge("anther"), lw=0.8, zorder=5)
        ax.add_patch(Ellipse(tuple(tip), 0.35, 0.25, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=0.6, zorder=6))
    else:
        long = (int(a * 10) % 2 == 0)
        ov = base + inward * 0.35
        ax.add_patch(Circle(tuple(ov), 0.22, facecolor=P.fill("ovary") if long else P.fill("highlight"),
                            edgecolor=P.edge("ovary") if long else P.edge("highlight"), lw=0.6, zorder=6))
        st = ov + inward * (1.1 if long else 0.45)
        ax.plot(*zip(ov, st), color=P.edge("ovary"), lw=0.8, zorder=5)
bio.callout(ax, (cx, cy + R + 0.2), (cx + 4.0, 13.4), "Ostiole closed by bracts", size="small")
bio.callout(ax, (cx - 2.4, cy + 2.9), (0.3, 12.0), "Male flowers (near ostiole)", size="small")
bio.callout(ax, (cx - 3.6, cy - 0.8), (0.3, 2.0), "Long-styled female flower (seed)", size="small")
bio.callout(ax, (cx + 3.4, cy - 1.6), (9.8, 0.4), "Short-styled gall flower (wasp larva)", size="small")

# cycle
ox, oy, rr = 25.5, 7.0, 5.2
steps = ["1  Pollen-bearing female\nenters through ostiole",
         "2  Pollinates female flowers;\nlays eggs in gall flowers",
         "3  Larvae develop\nin the galls",
         "4  Wingless males mate,\nchew exit tunnels",
         "5  Females collect pollen\nand fly to another fig"]
pts = []
for k, s in enumerate(steps):
    a = math.radians(90 - 72 * k)
    p = (ox + rr * math.cos(a), oy + rr * math.sin(a))
    pts.append(p)
    bio.box(ax, p, 5.0, 1.5, token="neutral", text=s, size="small")
for k in range(5):
    a0, a1 = math.radians(90 - 72 * k - 17), math.radians(90 - 72 * (k + 1) + 17)
    bio.arrow(ax, (ox + rr * 0.78 * math.cos(a0), oy + rr * 0.78 * math.sin(a0)),
              (ox + rr * 0.78 * math.cos(a1), oy + rr * 0.78 * math.sin(a1)), kind="process", bend=0.15)
bio.label(ax, (ox, oy), "Fig wasp\n(Agaonidae)", size="small")
