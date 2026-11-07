# Strigolactones in the rhizosphere: one signal, two readers (schematic). A host root exudes strigolactones (SL),
# more under phosphate deficiency. Arbuscular mycorrhizal (AM) fungi respond with spore germination and hyphal
# branching (Akiyama et al. 2005) and colonise the root (arbuscules). Seeds of the root parasite Striga, which can
# survive many years in the soil, germinate only when SL perceived by the expanded KAI2d/HTL receptor family
# reaches them (Conn et al. 2015); the radicle grows to the host root, host quinones (DMBQ) induce a haustorium
# that connects to the host xylem. Control: SL-deficient host lines (sorghum lgs1) and "suicidal germination"
# with SL analogues applied in the absence of a host.
import matplotlib.patches as mp
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24.0, 9.4)
ax.add_patch(mp.Rectangle((0.2, 0.2), 23.6, 9.0, facecolor=P.fill("cytoplasm"), edgecolor="none", zorder=0))
bio.label(ax, (0.5, 8.85), "Soil", size="small", bold=True, ha="left", color=P.muted())
# host root
ax.add_patch(mp.FancyBboxPatch((1.0, 4.4), 22.0, 1.1, boxstyle="round,pad=0,rounding_size=0.5",
                               facecolor=P.fill("bone"), edgecolor=P.edge("bone"), lw=1.3, zorder=3))
ax.plot([1.3, 22.7], [4.95, 4.95], color=P.edge("xylem"), lw=2.5, zorder=4)
bio.label(ax, (2.0, 5.75), "host root", size="small", ha="left")
bio.label(ax, (12.0, 5.75), "low phosphate → more SL exudation", size="tiny", color=P.muted())
rng = np.random.default_rng(0)
for k in range(110):
    x = rng.uniform(2.0, 22.0)
    y = 4.95 + rng.choice([-1, 1]) * (0.7 + rng.exponential(0.55))
    if abs(y - 4.95) > 3.3 or (x > 17.8 and y < 4.4) or (8.5 < x < 15.5 and y > 5.5 and y < 6.0):
        continue
    ax.add_patch(mp.Circle((x, y), 0.07, facecolor=P.fill("drug"), edgecolor="none", zorder=2))
bio.label(ax, (12.0, 8.2), "strigolactone gradient around the root", size="small", color=P.edge("drug"))

# AM fungus (left, above root)
ax.add_patch(mp.Circle((3.6, 8.0), 0.45, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=1.1, zorder=5))
hy = [(3.9, 7.7), (4.6, 7.2), (5.2, 6.6), (5.6, 5.6)]
ax.plot(*zip(*hy), color=P.edge("highlight"), lw=1.6, zorder=5)
for (x, y) in [(4.6, 7.2), (5.2, 6.6)]:
    for d in (-1, 1):
        ax.plot([x, x + 0.5 * d], [y, y - 0.4], color=P.edge("highlight"), lw=1.2, zorder=5)
for k in range(3):
    ax.add_patch(mp.Circle((5.9 + 0.35 * k, 5.0), 0.16, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.8, zorder=6))
bio.label(ax, (2.3, 7.0), "AM fungus:", size="small", bold=True, ha="left")
bio.label(ax, (0.6, 6.55), "spore germination,", size="tiny", ha="left")
bio.label(ax, (0.6, 6.15), "hyphal branching", size="tiny", ha="left")
bio.label(ax, (6.9, 4.1), "arbuscules", size="tiny", ha="left")

# Striga (right, below root)
sx = [16.0, 18.2, 20.4]
bio.label(ax, (13.4, 0.95), "Striga", size="small", ha="left", italic=True)
bio.label(ax, (14.25, 0.95), "seeds survive for years in the soil", size="small", ha="left")
# dormant seed far away
ax.add_patch(mp.Ellipse((14.6, 1.7), 0.42, 0.3, facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=1, zorder=5))
bio.label(ax, (14.6, 2.15), "far from root: stays dormant", size="tiny")
# germinated seed with radicle toward root
ax.add_patch(mp.Ellipse((18.2, 2.0), 0.42, 0.3, facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=1, zorder=5))
ax.plot([18.25, 18.5, 18.7], [2.15, 2.9, 3.55], color=P.edge("plant"), lw=1.8, zorder=5)
bio.label(ax, (19.0, 2.6), "germination", size="tiny", ha="left")
bio.label(ax, (19.0, 2.2), "(KAI2d/HTL)", size="tiny", ha="left")
# attached haustorium
ax.add_patch(mp.Ellipse((21.7, 2.2), 0.42, 0.3, facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=1, zorder=5))
ax.plot([21.7, 21.7], [2.35, 3.7], color=P.edge("plant"), lw=2.0, zorder=5)
ax.add_patch(mp.Polygon([(21.3, 3.7), (22.1, 3.7), (21.75, 4.85)], closed=True, facecolor=P.fill("plant"),
                        edgecolor=P.edge("plant"), lw=1.1, zorder=6))
bio.label(ax, (22.2, 3.15), "haustorium", size="tiny", ha="left")
bio.label(ax, (22.2, 2.75), "(DMBQ)", size="tiny", ha="left")
bio.label(ax, (21.0, 0.45), "taps host xylem → water, nutrients, sugars", size="tiny", color=P.muted())
