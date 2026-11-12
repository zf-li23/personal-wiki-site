# Schematic cross-section through the edge of a placozoan (Trichoplax): lower epithelium of tall
# monociliate cells with lipophil and gland cells, thin upper epithelium with shiny spheres, fibre cells
# between the layers, crystal cells near the rim; a temporary feeding pocket over algae.
import numpy as np
import wikibio as bio
from matplotlib.patches import Ellipse, FancyBboxPatch

P = bio.P
fig, ax = bio.canvas(27, 9.4)


def cell(x, y, w, h, token, z=6, r=0.12):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}", facecolor=P.fill(token),
                                edgecolor=P.edge(token), lw=0.8, zorder=z))


def nucleus(x, y, r=0.13, z=7):
    ax.add_patch(Ellipse((x, y), 2 * r, 1.6 * r, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.6, zorder=z))


def cilium(x, y, up=True, ln=0.55, z=5):
    s = 1 if up else -1
    t = np.linspace(0, 1, 20)
    ax.plot(x + 0.12 * np.sin(t * 6), y + s * ln * t, color=P.muted(), lw=0.8, zorder=z)


# substrate
ax.add_patch(FancyBboxPatch((0.5, 0.4), 25.0, 0.6, boxstyle="round,pad=0,rounding_size=0.05",
                            facecolor=P.mix(P.fill("neutral"), P.surface(), 0.6), edgecolor=P.edge("neutral"), lw=0.6, zorder=2))
bio.label(ax, (2.5, 0.7), "Substrate", size="tiny", color=P.muted())
# algae in a feeding pocket under the right part of the body
for i, x in enumerate(np.linspace(15.3, 19.8, 6)):
    ax.add_patch(Ellipse((x, 1.35 + 0.1 * (i % 2)), 0.55, 0.42, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=0.6, zorder=4))

lipo, gland = {3, 9, 16}, {6, 13, 19}
x0, y_low, y_up = 2.2, 1.9, 5.7
for i in range(22):
    x = x0 + i * 1.0
    lift = 0.6 if 14 <= i <= 19 else 0.0  # the body lifts over the pocket
    yb = y_low + lift
    if i in lipo:
        cell(x, yb, 0.92, 2.0, "lysosome")
        for g in range(3):
            ax.add_patch(Ellipse((x + 0.46, yb + 0.5 + 0.45 * g), 0.34, 0.3, facecolor=P.edge("lysosome"), edgecolor="none", zorder=7))
    elif i in gland:
        cell(x, yb, 0.92, 2.0, "vesicle")
        nucleus(x + 0.46, yb + 0.6)
        for g in range(4):
            ax.add_patch(Ellipse((x + 0.3 + 0.3 * (g % 2), yb + 1.25 + 0.25 * (g // 2)), 0.2, 0.2, facecolor=P.edge("vesicle"), edgecolor="none", zorder=7))
    else:
        cell(x, yb, 0.92, 2.0, "protein")
        nucleus(x + 0.46, yb + 1.3)
        cilium(x + 0.46, yb, up=False, ln=0.45 if lift == 0 else 0.4)
    # upper epithelium: flat cells
    yu = y_up + lift * 0.3
    cell(x, yu, 0.92, 0.55, "membrane", r=0.08)
    cilium(x + 0.46, yu + 0.55)
    if i % 3 == 1:
        ax.add_patch(Ellipse((x + 0.5, yu + 0.28), 0.36, 0.3, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.6, zorder=8))

# fibre cells in the middle layer
rng = np.random.default_rng(2)
for xc in (4.5, 9.0, 13.2, 17.6, 21.5):
    yc = 4.6 + (0.3 if 16 <= xc <= 20 else 0)
    ax.add_patch(Ellipse((xc, yc), 0.9, 0.55, facecolor=P.fill("muscle"), edgecolor=P.edge("muscle"), lw=0.8, zorder=6))
    for a in rng.uniform(0, 2 * np.pi, 5):
        ax.plot([xc, xc + 1.3 * np.cos(a)], [yc, yc + 0.45 * np.sin(a)], color=P.edge("muscle"), lw=1.0, zorder=5)
# crystal cell near the rim (left edge)
cell(0.9, 3.9, 1.1, 1.0, "bone")
ax.add_patch(plt_poly := __import__("matplotlib.patches", fromlist=["RegularPolygon"]).RegularPolygon(
    (1.45, 4.4), 4, radius=0.32, facecolor=P.edge("bone"), edgecolor="none", zorder=8))

bio.callout(ax, (3.66, 2.4), (3.0, 8.6), "Ventral epithelial cell (ciliated)", size="small")
bio.callout(ax, (5.66, 3.1), (9.6, 8.6), "Lipophil cell (digestive enzymes)", size="small")
bio.callout(ax, (9.0, 4.6), (14.4, 8.6), "Fibre cell", size="small")
bio.callout(ax, (15.66, 3.4), (18.6, 8.6), "Gland cell (mucus, peptides)", size="small")
bio.callout(ax, (21.7, 6.16), (23.0, 7.6), "Dorsal epithelium, shiny sphere", size="small")
bio.callout(ax, (1.45, 4.4), (0.9, 7.0), "Crystal cell", size="small")
bio.label(ax, (17.6, 0.7), "Algae in the feeding pocket (external digestion)", size="tiny", color=P.ink())
bio.label(ax, (26.2, 5.0), "Upper side", size="tiny", color=P.muted(), ha="left", rotation=90)
