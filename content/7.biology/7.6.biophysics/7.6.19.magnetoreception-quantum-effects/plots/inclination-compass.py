# The inclination compass.
# A: field lines of a dipole (the geomagnetic field, magnetic axis vertical, field pointing from the southern
#    to the northern geographic hemisphere outside the Earth) with local field vectors at the surface. The
#    inclination I (angle of the field below the horizontal) satisfies tan I = 2 tan(latitude); the field
#    points down in the northern hemisphere, up in the southern, horizontal at the magnetic equator.
# B: what a bird senses at 50 degrees north: an inclination compass reads only the axis of the field lines
#    (no polarity). "Poleward" is the direction along the axis in which the field and the gravity vector
#    make the smaller angle. Reversing only the vertical component (dashed) makes the same axis read
#    "equatorward", which is the classic test of Wiltschko and Wiltschko (1972).
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 2, figsize=(11.6, 5.0), gridspec_kw=dict(width_ratios=[1.2, 1]))
ax = axs[0]
ax.add_patch(Circle((0, 0), 1.0, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.0, alpha=0.35))
# dipole field lines r = L cos^2(lat), drawn outside the Earth
for Lv in (1.3, 1.8, 2.6, 4.0):
    lat = np.linspace(-np.arccos(np.sqrt(1 / Lv)), np.arccos(np.sqrt(1 / Lv)), 300)
    r = Lv * np.cos(lat) ** 2
    for s in (1, -1):
        ax.plot(s * r * np.cos(lat), r * np.sin(lat), color=charts.line("dna"), lw=0.9)
# local field vectors on the surface (dipole moment pointing to geographic south, so B points north and,
# in the north, downward)
for latd in (-60, -30, 0, 30, 60):
    for s in (1, -1):
        lat = np.radians(latd)
        x, y = s * np.cos(lat), np.sin(lat)
        Br = -2 * np.sin(lat)        # radial component (negative = into the Earth) for B pointing north
        Bt = np.cos(lat)             # northward component
        er = np.array([np.cos(lat) * s, np.sin(lat)])
        en = np.array([-np.sin(lat) * s, np.cos(lat)])
        v = Br * er + Bt * en
        v = 0.32 * v / np.linalg.norm(v)
        ax.annotate("", xy=(x + v[0], y + v[1]), xytext=(x, y),
                    arrowprops=dict(arrowstyle="-|>", color=charts.line("rna"), lw=1.3))
ax.text(0, 1.06, "N", ha="center", va="bottom", fontsize=9, color=P.ink(), weight="bold")
ax.text(0, -1.06, "S", ha="center", va="top", fontsize=9, color=P.ink(), weight="bold")
ax.text(1.05, 0.05, "magnetic equator:\nhorizontal field", fontsize=7, color=P.ink())
ax.set_xlim(-2.4, 2.4)
ax.set_ylim(-1.9, 1.9)
ax.set_aspect("equal")
ax.axis("off")
charts.title(ax, "A   Field lines and inclination (tan I = 2 tan latitude)")

ax = axs[1]
I = np.degrees(np.arctan(2 * np.tan(np.radians(50))))
ax.plot([-1.3, 1.3], [0, 0], color=P.muted(), lw=1.0)
ax.text(1.3, -0.08, "horizontal", fontsize=7, ha="right", va="top", color=P.muted())
d = np.array([np.cos(np.radians(I)), -np.sin(np.radians(I))])
ax.annotate("", xy=tuple(d * 1.1), xytext=tuple(-d * 1.1), arrowprops=dict(arrowstyle="-|>", color=charts.line("rna"), lw=1.8))
d2 = np.array([np.cos(np.radians(I)), np.sin(np.radians(I))])
ax.annotate("", xy=tuple(d2 * 1.1), xytext=tuple(-d2 * 1.1),
            arrowprops=dict(arrowstyle="-|>", color=charts.line("rna"), lw=1.2, ls="--"))
ax.annotate("", xy=(0, -1.2), xytext=(0, 0.0), arrowprops=dict(arrowstyle="-|>", color=P.ink(), lw=1.2))
ax.text(0.04, -1.18, "g", fontsize=9, color=P.ink())
ax.text(d[0] * 1.15, d[1] * 1.15 - 0.05, f"B, I = {I:.0f}°\n(north is this way)", fontsize=7, color=charts.line("rna"))
ax.text(d2[0] * 1.15, d2[1] * 1.15, "vertical component reversed:\nthis side now reads equatorward", fontsize=7, color=charts.line("rna"))
ax.text(-1.3, 1.25, "poleward = along the field axis\ntowards the side where it dips down", fontsize=7.5, color=P.ink())
ax.set_xlim(-1.4, 2.0)
ax.set_ylim(-1.4, 1.5)
ax.set_aspect("equal")
ax.axis("off")
charts.title(ax, "B   What the bird reads at 50° N")
fig.tight_layout()
