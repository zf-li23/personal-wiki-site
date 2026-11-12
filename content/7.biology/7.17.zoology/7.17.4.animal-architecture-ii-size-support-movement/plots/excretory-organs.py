"""Three types of invertebrate excretory organ (schematic, not to scale).

A: protonephridium of a flatworm. Blind tubules end in flame cells (terminal cells), whose tuft of beating
cilia drives fluid down the tubule; body fluid is filtered through a weir of fine slits in the wall of the
terminal cell, modified in the tubule and released through a nephridiopore. B: metanephridium of an
annelid. A ciliated funnel (nephrostome) opens into the coelom of one segment, the tubule passes through
the septum and leaves through a nephridiopore in the next segment; the primary urine is coelomic fluid
filtered across the walls of blood vessels into the coelom. C: Malpighian tubules of an insect. Blind
tubules bathed in hemolymph secrete ions actively and water follows; the fluid flows into the gut at the
junction of midgut and hindgut, and the rectum reabsorbs water and ions before excretion.
"""

import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(27.0, 9.4)
TUBE, FLUID = "rrna", "vacuole"


def tube(pts, w=0.22, token=TUBE, z=6):
    pts = np.asarray(pts, float)
    ax.plot(pts[:, 0], pts[:, 1], color=P.edge(token), lw=w * 40, solid_capstyle="round", zorder=z)
    ax.plot(pts[:, 0], pts[:, 1], color=P.fill(token), lw=w * 28, solid_capstyle="round", zorder=z + 1)


# ---- A: protonephridium
bio.panel(ax, "A", (0.4, 8.9))
bio.label(ax, (4.3, 8.9), "Protonephridium (flatworm)", size="small", bold=True)
main = [(1.2, 2.0), (2.5, 3.5), (3.8, 4.4), (5.2, 5.0), (6.6, 6.2)]
tube(main)
for base, tip in (((2.5, 3.5), (1.4, 5.6)), ((3.8, 4.4), (3.2, 7.0)), ((5.2, 5.0), (6.0, 7.6)), ((6.6, 6.2), (7.4, 7.9))):
    tube([base, tip])
    c = bio.box(ax, tip, 0.55, 0.55, token="protein", radius=0.25)
    for k in range(4):
        ax.plot([tip[0] - 0.12 + 0.08 * k, tip[0] - 0.12 + 0.08 * k - 0.05], [tip[1] - 0.15, tip[1] - 0.75],
                color=P.ink(), lw=0.8, zorder=15)
bio.callout(ax, (6.0, 7.6), (7.3, 8.5), "Flame cell", size="tiny")
bio.callout(ax, (3.2, 6.6), (1.2, 8.1), "Ciliary tuft", size="tiny")
bio.callout(ax, (4.5, 4.7), (6.6, 3.4), "Tubule", size="tiny")
bio.callout(ax, (1.2, 2.0), (2.6, 1.1), "Nephridiopore", size="tiny")
bio.arrow(ax, (2.2, 3.0), (1.5, 2.3), kind="process", color=P.muted())

# ---- B: metanephridium
bio.panel(ax, "B", (9.4, 8.9))
bio.label(ax, (13.3, 8.9), "Metanephridium (annelid)", size="small", bold=True)
for x0 in (9.8, 13.5):
    bio.box(ax, (x0 + 1.8, 5.0), 3.6, 5.4, token=FLUID, radius=0.2, text=None, zorder=2)
ax.plot([13.4, 13.4], [2.3, 7.7], color=P.edge("muscle"), lw=3.0, zorder=8)
bio.label(ax, (13.4, 8.0), "Septum", size="tiny")
bio.label(ax, (11.6, 7.3), "Coelom of segment n", size="tiny", color=P.muted())
bio.label(ax, (15.3, 7.3), "segment n + 1", size="tiny", color=P.muted())
funnel = np.array([(12.3, 5.6), (12.8, 5.2), (13.6, 4.9), (14.4, 5.6), (15.0, 4.7), (14.2, 4.0), (15.2, 3.4), (14.6, 2.6)])
tube(funnel)
ax.add_patch(__import__("matplotlib.patches", fromlist=["Polygon"]).Polygon([(11.8, 6.1), (12.0, 5.1), (12.5, 5.5)],
             closed=True, facecolor=P.fill(TUBE), edgecolor=P.edge(TUBE), lw=1.0, zorder=9))
bio.callout(ax, (11.95, 5.7), (10.4, 6.4), "Nephrostome\n(ciliated funnel)", size="tiny")
bio.callout(ax, (14.6, 2.6), (12.2, 2.0), "Nephridiopore", size="tiny")
bio.callout(ax, (15.0, 4.7), (16.6, 5.8), "Coiled tubule\n(reabsorption)", size="tiny")
bio.arrow(ax, (10.6, 5.3), (11.6, 5.6), kind="process", color=P.muted())

# ---- C: Malpighian tubules
bio.panel(ax, "C", (18.4, 8.9))
bio.label(ax, (22.6, 8.9), "Malpighian tubules (insect)", size="small", bold=True)
bio.box(ax, (22.6, 5.0), 8.0, 6.0, token="extracellular", radius=0.3, zorder=2)
bio.label(ax, (19.6, 7.6), "Hemolymph", size="tiny", color=P.muted())
tube([(19.0, 4.0), (22.2, 4.0)], w=0.5, token="carbohydrate")
tube([(22.4, 4.0), (24.6, 4.0), (25.8, 3.5)], w=0.35, token="lipid")
bio.label(ax, (20.6, 3.2), "Midgut", size="tiny")
bio.label(ax, (24.2, 3.2), "Hindgut", size="tiny")
bio.label(ax, (25.9, 2.9), "Rectum", size="tiny")
for k, (dx, dy) in enumerate(((-1.6, 3.0), (-0.6, 3.4), (0.6, 3.3), (1.6, 2.8))):
    pts = [(22.3, 4.2), (22.3 + dx * 0.5, 4.2 + dy * 0.5 + 0.2 * np.sin(k)), (22.3 + dx, 4.2 + dy)]
    tube(pts, w=0.13, token="atp")
bio.callout(ax, (23.3, 6.9), (25.2, 7.6), "Blind tubules", size="tiny")
bio.label(ax, (18.9, 5.6), "K$^+$, Cl$^-$, water,\nuric acid in", size="tiny", ha="left")
bio.arrow(ax, (20.4, 6.0), (21.1, 6.5), kind="process", color=P.muted())
bio.callout(ax, (25.6, 3.6), (25.6, 1.6), "Water and ions reabsorbed", size="tiny")
