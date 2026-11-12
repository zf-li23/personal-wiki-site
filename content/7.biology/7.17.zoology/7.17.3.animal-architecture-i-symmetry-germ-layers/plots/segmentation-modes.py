"""Three ways of making segments (schematic; anterior to the left, not to scale).

(A) Annelid: segments added one by one in a growth zone in front of the pygidium; teloblasts bud off the
mesodermal and ectodermal bands; prostomium and pygidium are not segments; youngest segment at the rear.
(B) Arthropod: short-germ (anterior segments first, the rest added from a posterior growth zone with cyclic
gene expression) versus long-germ (all segments specified at once in the blastoderm, ending in fourteen
engrailed stripes at the parasegment boundaries).
(C) Vertebrate: only the paraxial mesoderm is segmented; somites bud from the presomitic mesoderm where
the travelling wave of the segmentation clock meets a wavefront of falling FGF signalling.
"""

import numpy as np
from matplotlib.patches import Circle
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24.0, 17.0)


def half_disc(cx, cy, r, side, token, ry=None):
    """A semicircular cap facing left (side=-1) or right (side=+1)."""
    ry = ry or r
    t = np.linspace(-np.pi / 2, np.pi / 2, 60)
    pts = np.c_[cx + side * r * np.cos(t), cy + ry * np.sin(t)]
    bio.shape(ax, pts, token, lw=0.9, zorder=6)


# ---------------- (A) annelid ----------------
bio.panel(ax, "A", (0.4, 16.4))
bio.label(ax, (1.2, 16.4), "Annelid: sequential addition from a growth zone", size="normal", bold=True, ha="left")
yA, h = 14.3, 1.5
x = 2.6
half_disc(x, yA, 1.0, -1, "ectoderm", ry=h / 2)
bio.label(ax, (1.2, yA - 1.35), "prostomium", size="tiny", color=P.muted())
widths = [1.35, 1.3, 1.25, 1.2, 1.12, 1.04, 0.95, 0.85, 0.74, 0.62, 0.5]
for k, w in enumerate(widths):
    bio.box(ax, (x + w / 2, yA), w - 0.06, h * (1.0 - 0.025 * k), "mesoderm", radius=0.12, lw=0.8)
    x += w
gz0 = x
bio.box(ax, (x + 0.6, yA), 1.2, h * 0.7, "highlight", radius=0.12, lw=0.8)
for dy in (-0.25, 0.25):
    ax.add_patch(Circle((x + 0.85, yA + dy), 0.13, facecolor=P.fill("ectoderm"), edgecolor=P.edge("ectoderm"), lw=0.6, zorder=12))
x += 1.2
half_disc(x, yA, 0.8, 1, "ectoderm", ry=h * 0.36)
bio.label(ax, (x + 0.9, yA - 1.0), "pygidium", size="tiny", color=P.muted())
bio.callout(ax, (gz0 + 0.85, yA + 0.25), (gz0 + 2.8, yA + 1.4), "teloblasts", size="tiny")
bio.label(ax, (gz0 + 0.6, yA - 1.2), "growth zone", size="tiny", color=P.muted())
bio.arrow(ax, (3.2, yA - 1.35), (gz0 - 0.3, yA - 1.35), kind="process", color=P.muted())
bio.label(ax, ((3.2 + gz0) / 2, yA - 1.75), "segment age: oldest  →  youngest", size="tiny", color=P.muted())
bio.label(ax, (17.3, yA + 0.5), "segmented: ectoderm and mesoderm", size="small", ha="left")
bio.label(ax, (17.3, yA - 0.1), "(chaetae, ganglia, muscles,", size="tiny", ha="left", color=P.muted())
bio.label(ax, (17.3, yA - 0.55), "coelomic sacs, nephridia)", size="tiny", ha="left", color=P.muted())

# ---------------- (B) arthropod ----------------
bio.panel(ax, "B", (0.4, 11.6))
bio.label(ax, (1.2, 11.6), "Arthropod: growth zone (short germ) or subdivision of the blastoderm (long germ)", size="normal",
          bold=True, ha="left")
yB = 9.9
bio.label(ax, (1.2, yB + 1.05), "short germ", size="small", ha="left")
x = 2.6
half_disc(x, yB, 1.1, -1, "ectoderm", ry=0.8)
bio.label(ax, (2.0, yB - 1.0), "head lobes", size="tiny", color=P.muted())
for k in range(6):
    bio.box(ax, (x + 0.55, yB), 1.0, 1.2, "ectoderm", radius=0.1, lw=0.8)
    ax.plot([x + 0.98, x + 0.98], [yB - 0.6, yB + 0.6], color=P.edge("negative"), lw=2.0, zorder=12)
    x += 1.1
# growth zone with cyclic expression (stripes of varying strength)
gz = x
bio.box(ax, (gz + 1.5, yB), 3.0, 1.1, "highlight", radius=0.3, lw=0.8)
for k, a in enumerate((0.85, 0.5, 0.2)):
    bio.box(ax, (gz + 0.45 + 0.75 * k, yB), 0.3, 0.9, "negative", radius=0.05, lw=0.0, zorder=11)
bio.label(ax, (gz + 1.5, yB - 1.05), "growth zone: cyclic pair-rule / Notch", size="tiny", color=P.muted())
bio.label(ax, (gz + 3.7, yB + 0.1), "→ new segments", size="tiny", ha="left", color=P.muted())
bio.label(ax, (17.3, yB + 0.3), "engrailed stripe at the", size="small", ha="left")
bio.label(ax, (17.3, yB - 0.25), "rear of each segment", size="small", ha="left")
ax.plot([16.6, 17.1], [yB + 0.0, yB + 0.0], color=P.edge("negative"), lw=2.0)

yL = 7.1
bio.label(ax, (1.2, yL + 1.3), "long germ ($\\it{Drosophila}$)", size="small", ha="left")
t = np.linspace(0, 2 * np.pi, 120)
cx, rx, ry = 8.6, 6.0, 0.95
bio.shape(ax, np.c_[cx + rx * np.cos(t), yL + ry * np.sin(t)], "ectoderm", lw=0.9, zorder=5)
for k in range(14):
    xs = cx - rx + 1.4 + k * (2 * rx - 2.4) / 13
    half = ry * np.sqrt(max(0.0, 1 - ((xs - cx) / rx) ** 2))
    ax.plot([xs, xs], [yL - half * 0.92, yL + half * 0.92], color=P.edge("negative"), lw=2.0, zorder=12)
bio.label(ax, (cx, yL - 1.35), "14 stripes specified at once: gap → pair-rule → segment-polarity genes", size="tiny",
          color=P.muted())
bio.label(ax, (17.3, yL + 0.25), "segmented: ectoderm first,", size="small", ha="left")
bio.label(ax, (17.3, yL - 0.3), "mesoderm patterned partly by it", size="small", ha="left")

# ---------------- (C) vertebrate ----------------
bio.panel(ax, "C", (0.4, 4.8))
bio.label(ax, (1.2, 4.8), "Vertebrate: somites from a clock and a wavefront", size="normal", bold=True, ha="left")
yC = 2.6
bio.box(ax, (8.4, yC + 1.05), 13.6, 0.45, "ectoderm", text=None, radius=0.2, lw=0.8)
bio.label(ax, (1.0, yC + 1.05), "neural tube", size="tiny", ha="right", color=P.muted())
bio.box(ax, (8.4, yC + 0.45), 13.6, 0.3, "bone", radius=0.15, lw=0.7)
bio.label(ax, (1.0, yC + 0.45), "notochord", size="tiny", ha="right", color=P.muted())
x = 1.8
sizes = [0.95] * 8
for k, w in enumerate(sizes):
    bio.box(ax, (x + w / 2, yC - 0.35), w - 0.12, 0.9, "mesoderm", radius=0.15, lw=0.8)
    x += w
psm0 = x
# presomitic mesoderm with clock stripes and an FGF gradient underneath
bio.box(ax, (psm0 + 2.6, yC - 0.35), 5.2, 0.9, "mesoderm", radius=0.3, lw=0.8)
for k, xs in enumerate((psm0 + 0.6, psm0 + 2.2, psm0 + 3.6, psm0 + 4.7)):
    bio.box(ax, (xs, yC - 0.35), 0.35 + 0.15 * k, 0.75, "highlight", radius=0.08, lw=0.0, zorder=11)
bio.label(ax, (psm0 + 3.2, yC - 1.2), "presomitic mesoderm: clock waves (Hes/Her)", size="tiny", color=P.muted())
n = 30
for i in range(n):
    f = i / (n - 1)
    bio.box(ax, (psm0 + 0.1 + f * 5.0, yC - 1.75), 5.0 / n + 0.02, 0.28, "positive", radius=0.0, lw=0.0, zorder=6)
    ax.patches[-1].set_alpha(0.12 + 0.8 * f)
bio.label(ax, (psm0 - 0.2, yC - 1.75), "FGF", size="tiny", ha="right", color=P.muted())
ax.plot([psm0 + 0.1, psm0 + 0.1], [yC - 2.05, yC + 0.3], color=P.ink(), lw=1.0, ls="--", zorder=13)
bio.label(ax, (psm0 - 0.6, yC - 2.35), "wavefront: next boundary", size="tiny", color=P.muted())
bio.label(ax, (psm0 - 3.8, yC - 1.2), "somites (oldest at the front)", size="tiny", color=P.muted())
bio.label(ax, (17.3, yC + 0.3), "segmented: paraxial mesoderm only", size="small", ha="left")
bio.label(ax, (17.3, yC - 0.25), "(myotomes, vertebrae, ribs; spinal", size="tiny", ha="left", color=P.muted())
bio.label(ax, (17.3, yC - 0.7), "nerves follow the somites)", size="tiny", ha="left", color=P.muted())
