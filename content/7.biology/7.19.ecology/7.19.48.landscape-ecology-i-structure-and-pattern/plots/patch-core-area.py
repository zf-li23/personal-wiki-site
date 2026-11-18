# Edge and core of habitat patches. Edge effects are assumed to penetrate a depth d = 100 m.
# A: four patches of equal area (20 ha) - circle, square, 4:1 rectangle and a lobed shape - with
#    their core areas (dark) computed on a 2 m raster by the distance transform.
# B: core area as a fraction of patch area against patch area for circles, squares and rectangles
#    with aspect ratios 4 and 16; the circle attains the Brunn-Minkowski bound (sqrt(A) - d sqrt(pi))^2.
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
import wikibio as bio

P = bio.P
d, A = 100.0, 20e4                   # m, m^2
res = 2.0
L = 940
xx, yy = np.meshgrid(np.arange(-L / 2, L / 2, res), np.arange(-L / 2, L / 2, res))
R = np.sqrt(A / np.pi)
s = np.sqrt(A)
a4, b4 = np.sqrt(4 * A), np.sqrt(A / 4)
th = np.arctan2(yy, xx)
rlob = 1.0 + 0.35 * np.cos(5 * th)
scale = np.sqrt(A / (np.pi * np.mean(rlob ** 2)))
shapes = [("circle", np.hypot(xx, yy) <= R), ("square", (np.abs(xx) <= s / 2) & (np.abs(yy) <= s / 2)),
          ("4:1 rectangle", (np.abs(xx) <= a4 / 2) & (np.abs(yy) <= b4 / 2)),
          ("lobed", np.hypot(xx, yy) <= scale * rlob)]

fig = plt.figure(figsize=(12.4, 4.6))
gs = fig.add_gridspec(2, 4, width_ratios=[1, 1, 1.3, 1.3], wspace=0.15, hspace=0.25)
for k, (name, m) in enumerate(shapes):
    ax = fig.add_subplot(gs[k // 2, k % 2])
    core = ndimage.distance_transform_edt(m) * res > d
    img = np.where(core, 2, np.where(m, 1, 0))
    ax.contourf(xx, yy, img, levels=[0.5, 1.5, 2.5], colors=[P.fill("highlight"), P.fill("plant")])
    ax.contour(xx, yy, m.astype(float), levels=[0.5], colors=[P.edge("plant")], linewidths=1)
    frac = core.sum() / m.sum()
    ax.set_title(f"{name}: core {100 * frac:.0f}%", fontsize=8.5)
    ax.set_aspect("equal")
    ax.set_xlim(-L / 2, L / 2)
    ax.set_ylim(-L / 2, L / 2)
    ax.axis("off")
fig.text(0.04, 0.95, "A  Patches of 20 ha, edge depth 100 m", fontsize=11, fontweight="bold")

ax = fig.add_subplot(gs[:, 2:])
area = np.logspace(np.log10(3e4), np.log10(1e8), 300)       # m^2
circ = np.clip(np.sqrt(area) - d * np.sqrt(np.pi), 0, None) ** 2 / area
def rect(k):
    b = np.sqrt(area / k)
    a = k * b
    return np.clip(a - 2 * d, 0, None) * np.clip(b - 2 * d, 0, None) / area
ax.plot(area / 1e4, circ, color=P.ink(), lw=2, label="circle (upper bound)")
for k, tok, lab in ((1, "dna", "square"), (4, "highlight", "4:1 rectangle"), (16, "negative", "16:1 rectangle")):
    col = P.edge(tok) if tok == "highlight" else P.fill(tok)
    ax.plot(area / 1e4, rect(k), color=col, lw=1.8, label=lab)
ax.axvline(20, color=P.muted(), lw=0.8, ls=":")
ax.set_xscale("log")
ax.set_xlim(3, 1e4)
ax.set_ylim(0, 1)
ax.set_xlabel("Patch area / ha")
ax.set_ylabel("Core area / patch area")
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.set_title("B  Core fraction and patch area", loc="left", fontweight="bold")
for sp in ("top", "right"):
    ax.spines[sp].set_visible(False)
