# Zones of aquatic ecosystems (schematic, not to scale).
# A: a stratified lake; B: the ocean (horizontal and vertical zones).
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import wikibio as bio

P = bio.P
fig, (a, b) = plt.subplots(1, 2, figsize=(11.6, 4.9), gridspec_kw=dict(width_ratios=[1, 1.25]))

# ---- A: lake ----
x = np.linspace(0, 10, 300)
bottom = -9 * np.sin(np.pi * x / 10) ** 0.8  # lake basin
a.fill_between(x, bottom, 0, color=P.mix(P.surface(), P.fill("channel"), 0.25), lw=0)
a.fill_between(x, np.maximum(bottom, -2.2), 0, color=P.mix(P.surface(), P.fill("channel"), 0.45), lw=0)
a.fill_between(x, np.maximum(bottom, -3.6), np.maximum(bottom, -2.2), color=P.mix(P.surface(), P.fill("atp"), 0.35), lw=0)
a.plot(x, bottom, color=P.edge("animal"), lw=1.6)
a.fill_between(x, bottom, -10, color=P.mix(P.surface(), P.fill("animal"), 0.5), lw=0)
a.axhline(0, color=P.edge("dna"), lw=1.2)
comp = -4.0  # compensation depth
xl = np.interp(comp, bottom[:150][::-1], x[:150][::-1])
xr = 10 - xl
a.plot([xl, xr], [comp, comp], color=P.ink(), lw=1.0, ls="--")
a.text(5, comp - 0.25, "compensation depth", ha="center", va="top", fontsize=7.5, color=P.ink())
a.text(5, -1.1, "limnetic zone", ha="center", fontsize=8.5, color=P.ink(), weight="bold")
a.text(5, -6.3, "profundal zone", ha="center", fontsize=8.5, color=P.ink(), weight="bold")
a.text(1.0, -1.0, "littoral\nzone", ha="center", fontsize=8, color=P.ink(), weight="bold")
a.text(9.0, -1.0, "littoral\nzone", ha="center", fontsize=8, color=P.ink(), weight="bold")
a.text(5, -9.6, "benthic zone (bottom)", ha="center", fontsize=7.5, color=P.ink())
# rooted plants in the littoral
for xp in np.linspace(0.3, xl - 0.2, 6):
    yb = np.interp(xp, x, bottom)
    a.plot([xp, xp + 0.05], [yb, min(0.4, yb + 2.6)], color=P.edge("plant"), lw=1.3)
    a.plot([10 - xp, 10 - xp - 0.05], [yb, min(0.4, yb + 2.6)], color=P.edge("plant"), lw=1.3)
for y, t in ((-1.1, "epilimnion"), (-2.9, "thermocline"), (-5.0, "hypolimnion")):
    a.text(10.15, y, t, fontsize=7.5, ha="left", va="center", color=P.muted())
a.set_xlim(-0.2, 12.4)
a.set_ylim(-10, 1)
a.axis("off")
a.set_title("A  Lake", loc="left", fontweight="bold")

# ---- B: ocean ----
# depth in km, distance in arbitrary units; shelf to 0.2 km, slope, abyssal plain at 4-6 km, trench
d = np.array([0, 1.2, 2.0, 2.4, 3.4, 6.0, 7.0, 7.6, 8.2, 10])
z = np.array([0.0, -0.1, -0.2, -0.6, -4.0, -4.6, -5.2, -10.5, -5.4, -5.0])
xx = np.linspace(0, 10, 400)
zz = np.interp(xx, d, z)
layers = [(0, -0.2, "epipelagic (0-200 m)", 0.55), (-0.2, -1.0, "mesopelagic (200-1000 m)", 0.4),
          (-1.0, -4.0, "bathypelagic (1-4 km)", 0.28), (-4.0, -6.0, "abyssopelagic (4-6 km)", 0.18),
          (-6.0, -11, "hadal (> 6 km)", 0.1)]
for top, bot, name, t in layers:
    lo = np.maximum(zz, bot)
    b.fill_between(xx, lo, np.minimum(top, 0), where=zz < top, color=P.mix(P.surface(), P.fill("dna"), t), lw=0)
b.fill_between(xx, zz, -11, color=P.mix(P.surface(), P.fill("animal"), 0.5), lw=0)
b.plot(xx, zz, color=P.edge("animal"), lw=1.6)
for top, bot, name, t in layers:
    yc = (top + max(bot, -10.5)) / 2 if bot > -6.5 else -8.3
    b.text(10.15, yc, name, fontsize=7.5, va="center", ha="left", color=P.ink())
b.text(1.0, 0.25, "intertidal", fontsize=7, ha="center", va="bottom", color=P.muted())
b.text(1.6, 0.85, "neritic zone", fontsize=8, ha="center", va="bottom", color=P.ink(), weight="bold")
b.text(6.5, 0.85, "oceanic zone", fontsize=8, ha="center", va="bottom", color=P.ink(), weight="bold")
b.plot([2.4, 2.4], [0.1, 0.8], color=P.muted(), lw=0.8)
b.text(1.1, -0.55, "shelf", fontsize=7, ha="center", color=P.ink())
b.text(2.55, -2.4, "slope", fontsize=7, ha="left", color=P.ink())
b.text(4.8, -5.0, "abyssal plain", fontsize=7, ha="center", color=P.ink())
b.text(7.6, -10.9, "trench", fontsize=7, ha="center", va="top", color=P.ink())
# light zones (right margin bar)
for top, bot, t, tok in ((0, -0.2, "euphotic", "atp"), (-0.2, -1.0, "dysphotic", "lipid"), (-1.0, -10.5, "aphotic", "neutral")):
    b.add_patch(Polygon([(-0.75, top), (-0.45, top), (-0.45, bot), (-0.75, bot)], closed=True,
                        facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.6))
    b.text(-0.85, (top + bot) / 2 if bot > -2 else -3.0, t, fontsize=7, ha="right", va="center", color=P.ink(),
           rotation=0)
b.axhline(0, color=P.edge("dna"), lw=1.2, xmin=0.08, xmax=0.8)
b.set_xlim(-2.3, 13.6)
b.set_ylim(-11.3, 1.4)
b.set_yticks([])
b.axis("off")
b.set_title("B  Ocean (depth exaggerated near the surface: not to scale)", loc="left", fontweight="bold")
fig.tight_layout()
