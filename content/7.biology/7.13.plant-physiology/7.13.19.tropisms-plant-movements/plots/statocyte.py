# Gravity sensing in a root columella cell (schematic, after Taiz et al. 6e, Fig. 18.18; Kleine-Vehn et al.
# 2010). (A) Vertical root: amyloplasts (statoliths) rest on the ER at the bottom of the cell; PIN3 is
# distributed around the plasma membrane and auxin leaves the columella symmetrically. (B) About 10 min
# after the root is turned 90 degrees: the amyloplasts have sedimented onto the new lower side; within
# minutes the cytosol alkalinizes (pH 7.2 -> 7.6) and the apoplast acidifies, Ca2+ signals arise, and PIN3
# is relocated to the new lower membrane, so that more auxin flows to the lower flank of the root, where
# it inhibits elongation and the root bends down.
import numpy as np
import wikibio as bio
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch

P = bio.P
fig, ax = bio.canvas(16, 8.4)
red = P.edge("negative")


def cell(c, w, h, rotated):
    x, y = c
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0,rounding_size=0.35",
                                facecolor=P.fill("cytoplasm"), edgecolor=P.edge("cell_wall"), lw=2.6, zorder=2))
    bio.nucleus(ax, (x, y + (0.35 if not rotated else 0.0) * h / 2 + (0 if not rotated else 0)), 0.55, pores=6, zorder=4)
    # ER sheets along the (current) lower side
    if not rotated:
        bio.er(ax, (x, y - h / 2 + 0.45), w * 0.6, 0.35, sheets=2, zorder=3)
    else:
        bio.er(ax, (x, y - h / 2 + 0.45), w * 0.6, 0.35, sheets=2, zorder=3)
    rng = np.random.default_rng(2)
    for k in range(7):
        px = x + (k - 3) * 0.42 + rng.uniform(-0.05, 0.05)
        py = y - h / 2 + 0.95 + (k % 2) * 0.32
        ax.add_patch(Ellipse((px, py), 0.5, 0.42, facecolor=P.fill("carbohydrate"), edgecolor=P.edge("carbohydrate"),
                             lw=0.9, zorder=6))
    # PIN3 marks on the membrane
    if not rotated:
        sides = [(x - w / 2 + 0.06, yy) for yy in np.linspace(y - h / 2 + 0.6, y + h / 2 - 0.6, 4)]
        sides += [(x + w / 2 - 0.06, yy) for yy in np.linspace(y - h / 2 + 0.6, y + h / 2 - 0.6, 4)]
        sides += [(xx, y - h / 2 + 0.06) for xx in np.linspace(x - w / 2 + 0.6, x + w / 2 - 0.6, 3)]
        sides += [(xx, y + h / 2 - 0.06) for xx in np.linspace(x - w / 2 + 0.6, x + w / 2 - 0.6, 3)]
    else:
        sides = [(xx, y - h / 2 + 0.06) for xx in np.linspace(x - w / 2 + 0.45, x + w / 2 - 0.45, 8)]
        sides += [(x - w / 2 + 0.06, y - h / 2 + 0.6), (x + w / 2 - 0.06, y - h / 2 + 0.6)]
    for p in sides:
        ax.add_patch(Circle(p, 0.11, facecolor=P.fill("channel"), edgecolor=P.edge("channel"), lw=0.7, zorder=7))


# panel A: vertical root, gravity down; auxin leaves both sides equally
bio.panel(ax, "A", (0.1, 8.3))
bio.label(ax, (3.6, 8.0), "Vertical root", size="small", bold=True)
cell((3.6, 4.4), 3.4, 4.6, False)
for s in (-1, 1):
    bio.arrow(ax, (3.6 + s * 1.85, 4.4), (3.6 + s * 3.0, 4.4), kind="process", color=red, lw=2.0)
bio.label(ax, (3.6, 1.45), "Auxin out on both sides", size="small", color=red)
# panel B: rotated 90 degrees: new lower side
bio.panel(ax, "B", (8.2, 8.3))
bio.label(ax, (11.9, 8.0), "Root turned 90°: about 10 min later", size="small", bold=True)
cell((11.9, 4.4), 4.6, 3.4, True)
bio.arrow(ax, (11.9, 2.55), (11.9, 1.4), kind="process", color=red, lw=3.0)
bio.arrow(ax, (14.35, 4.4), (14.9, 4.4), kind="process", color=red, lw=0.9)
bio.arrow(ax, (9.45, 4.4), (8.9, 4.4), kind="process", color=red, lw=0.9)
bio.label(ax, (11.9, 0.9), "More auxin to the lower flank", size="small", color=red)
# gravity arrows
for gx in (6.6, 15.6):
    bio.arrow(ax, (gx, 6.5), (gx, 5.2), kind="process", lw=1.6)
    bio.label(ax, (gx + 0.2, 5.85), "g", size="small", italic=True, ha="left")
bio.callout(ax, (3.6 - 0.4, 2.95), (0.3, 1.0), "Amyloplasts (statoliths) on the ER", size="tiny")
bio.callout(ax, (3.6 + 1.64, 5.4), (6.0, 7.4), "PIN3 (uniform)", size="tiny")
bio.callout(ax, (13.0, 2.76), (14.6, 1.6), "PIN3 relocated\nto the lower side", size="tiny")
bio.label(ax, (11.9, 6.7), "cytosol pH 7.2 → 7.6, wall acidifies, Ca²⁺", size="tiny", color=P.muted())
