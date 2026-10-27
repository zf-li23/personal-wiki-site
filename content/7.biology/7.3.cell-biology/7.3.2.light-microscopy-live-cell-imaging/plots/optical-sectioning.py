# Three geometries of optical sectioning, drawn as light paths through a thick fluorescent specimen.
# A, widefield epifluorescence: the whole depth is excited and all emitted light reaches the camera.
# B, confocal: a focused laser spot excites a double cone; a pinhole in a plane conjugate to the focus passes
#    light from the focal spot (solid) and blocks light from above and below it (dashed).
# C, light sheet: a thin sheet of excitation enters from the side, so only the observed plane is excited
#    (less photobleaching and phototoxicity); detection is at right angles.
# D, TIRF: totally internally reflected light at the glass-water interface creates an evanescent field that
#    decays as exp(-z/delta) with delta ~ 100 nm, exciting only fluorophores at the basal membrane.
import numpy as np
from matplotlib.patches import Polygon, Rectangle

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26, 9.5)


def specimen(x0, w, y0, h):
    ax.add_patch(Rectangle((x0, y0), w, h, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("cytoplasm"), lw=1.0, zorder=2))


def lens(cx, cy, w):
    t = np.linspace(-1, 1, 50)
    pts = np.c_[np.r_[cx + w / 2 * t, cx - w / 2 * t], np.r_[cy + 0.18 * np.sqrt(1 - t**2), cy - 0.18 * np.sqrt(1 - t**2)]]
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill("channel"), edgecolor=P.edge("channel"), lw=1.0, zorder=5))


exc, emi = P.edge("positive"), P.edge("negative")

# A widefield
specimen(0.8, 4.4, 1.2, 1.6)
ax.add_patch(Rectangle((0.8, 1.2), 4.4, 1.6, facecolor=P.fill("positive"), alpha=0.45, edgecolor="none", zorder=3))
lens(3.0, 4.2, 3.0)
for xx in np.linspace(1.4, 4.6, 5):
    ax.plot([xx, xx], [2.9, 4.0], color=emi, lw=1.0, zorder=4)
    ax.plot([xx, 3.0 + (xx - 3.0) * 0.3], [4.4, 7.0], color=emi, lw=1.0, zorder=4)
ax.add_patch(Rectangle((1.9, 7.0), 2.2, 0.4, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), zorder=5))
bio.label(ax, (3.0, 7.75), "camera", size="small")
bio.label(ax, (3.0, 0.5), "A  widefield: whole depth excited", size="small")

# B confocal
specimen(7.0, 4.4, 1.2, 1.6)
fy = 2.0
lens(9.2, 4.2, 3.0)
ax.add_patch(Polygon([(7.9, 4.0), (10.5, 4.0), (9.2, fy)], closed=True, facecolor=P.fill("positive"), alpha=0.45, edgecolor="none", zorder=3))
ax.add_patch(Polygon([(9.2, fy), (8.6, 1.2), (9.8, 1.2)], closed=True, facecolor=P.fill("positive"), alpha=0.45, edgecolor="none", zorder=3))
ax.plot([9.2], [fy], "o", color=exc, ms=4, zorder=6)
ax.plot([7.9, 9.2, 10.5], [4.0, fy, 4.0], color=emi, lw=1.1, zorder=4)
ax.plot([9.2, 8.2, 9.2], [7.0, 4.4, 7.0], color=emi, lw=1.1, zorder=4)
ax.plot([9.2, 10.2], [7.0, 4.4], color=emi, lw=1.1, zorder=4)
ax.plot([8.3, 9.55, 10.4], [4.0, 2.5, 4.0], color=emi, lw=0.9, ls=(0, (3, 2)), zorder=4)
ax.plot([8.4, 9.57], [4.4, 7.0], color=emi, lw=0.9, ls=(0, (3, 2)), zorder=4)
ax.plot([7.6, 9.05], [7.0, 7.0], color=P.ink(), lw=3, zorder=6)
ax.plot([9.35, 10.8], [7.0, 7.0], color=P.ink(), lw=3, zorder=6)
ax.add_patch(Rectangle((8.6, 7.9), 1.2, 0.5, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), zorder=5))
bio.label(ax, (9.2, 8.75), "detector", size="small")
bio.callout(ax, (10.6, 7.0), (11.6, 7.6), "pinhole")
bio.callout(ax, (9.2, fy), (11.8, 2.0), "focus")
bio.label(ax, (9.2, 0.5), "B  confocal: pinhole rejects\nout-of-focus light", size="small")

# C light sheet
specimen(13.4, 4.4, 1.2, 2.6)
ax.add_patch(Polygon([(12.6, 2.3), (12.6, 2.7), (17.8, 2.56), (17.8, 2.44)], closed=True, facecolor=P.fill("positive"),
                     edgecolor=exc, lw=0.8, alpha=0.6, zorder=3))
bio.arrow(ax, (12.0, 2.5), (12.9, 2.5), kind="process", color=exc)
lens(15.6, 4.6, 2.6)
for xx in np.linspace(14.2, 17.0, 4):
    ax.plot([xx, xx], [2.6, 4.4], color=emi, lw=1.0, zorder=4)
    ax.plot([xx, 15.6 + (xx - 15.6) * 0.3], [4.8, 7.0], color=emi, lw=1.0, zorder=4)
ax.add_patch(Rectangle((14.5, 7.0), 2.2, 0.4, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), zorder=5))
bio.label(ax, (15.6, 7.75), "camera", size="small")
bio.label(ax, (12.4, 3.1), "sheet", size="small")
bio.label(ax, (15.6, 0.5), "C  light sheet: only the\nobserved plane is excited", size="small")

# D TIRF
ax.add_patch(Rectangle((19.4, 1.4), 6.0, 0.9, facecolor=P.fill("channel"), edgecolor=P.edge("channel"), lw=1.0, zorder=3))
bio.label(ax, (20.3, 1.85), "glass", size="small")
o = bio.blob((22.6, 3.4), 2.0, 1.0, wobble=0.04, seed=3)
o[:, 1] = np.maximum(o[:, 1], 2.32)
ax.add_patch(Polygon(o, closed=True, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("cytoplasm"), lw=1.0, zorder=4))
z = np.linspace(0, 1, 30)
for k in range(30):
    ax.add_patch(Rectangle((20.4, 2.3 + z[k] * 0.9), 4.6, 0.03, facecolor=P.fill("positive"), edgecolor="none",
                           alpha=float(0.7 * np.exp(-z[k] * 4)), zorder=5))
ax.plot([19.6, 22.6, 25.6], [0.5 + 0.0, 2.3, 0.5], color=exc, lw=1.4, zorder=6)
bio.arrow(ax, (25.0, 0.9), (25.6, 0.5), kind="process", color=exc)
bio.callout(ax, (24.6, 2.45), (25.6, 4.9), "evanescent field\n~100 nm")
bio.label(ax, (22.6, 5.8), "D  TIRF: only the basal\n~100 nm is excited", size="small")
