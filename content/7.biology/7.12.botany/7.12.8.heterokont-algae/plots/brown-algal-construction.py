"""Evolutionary series of thallus construction in brown algae (schematic). A: heterotrichous uniseriate
filament (Ectocarpus type), prostrate part on the substrate and branched erect part; band-shaped plastids. B:
pseudoparenchyma: branched filaments pressed together, colourless medullary filaments in the centre and
assimilatory laterals at the surface. C: parenchymatous thallus with holdfast, stipe and blade (kelp type);
the meristem lies at the junction of stipe and blade (intercalary growth). D: cross-section of a kelp blade:
mucilage layer, epidermis (meristoderm) with plastids, cortex of large cells with mucilage ducts, and medulla
of filaments and trumpet hyphae; inset: two trumpet-hypha ends joined at a sieve plate."""
import numpy as np
from matplotlib.patches import Rectangle, Ellipse, Circle, FancyBboxPatch
import wikibio as bio

P = bio.P
rng = np.random.default_rng(4)
fig, ax = bio.canvas(34, 13)
B = "highlight"


def rc(x, y, w, h, tok=B, fc=None, z=5, lw=0.8):
    ax.add_patch(Rectangle((x, y), w, h, facecolor=fc or P.light(tok), edgecolor=P.edge(tok), lw=lw, zorder=z))


def head(x, L, t):
    bio.panel(ax, L, (x, 12.8))
    bio.label(ax, (x + 0.6, 12.55), t, size="small", bold=True, ha="left")


# A heterotrichous
head(0.2, "A", "Heterotrichous filament")
for k in range(10):
    rc(0.6 + 0.6 * k, 1.5, 0.6, 0.4)
for x0, n, br in ((1.2, 14, 6), (3.0, 18, 9), (4.8, 12, 5)):
    for k in range(n):
        w = 0.36 * (1 - 0.4 * k / n)
        rc(x0 + 0.18 - w / 2, 1.9 + 0.5 * k, w, 0.5)
        ax.plot([x0 + 0.18, x0 + 0.18], [2.0 + 0.5 * k, 2.3 + 0.5 * k], color=P.edge(B), lw=1.6, zorder=6)
    for k in range(4):
        rc(x0 + 0.36 + 0.4 * k, 1.9 + 0.5 * br + 0.22 * k, 0.4, 0.28)
bio.label(ax, (3.3, 0.9), "prostrate part on substrate", size="tiny", color=P.muted())

# B pseudoparenchyma
head(8.2, "B", "Pseudoparenchyma")
for xa in np.linspace(10.6, 12.4, 5):
    for k in range(10):
        rc(xa - 0.15, 1.4 + 0.9 * k, 0.3, 0.88, fc=P.fill("cytoplasm"))
for sgn in (-1, 1):
    for k in range(10):
        y = 1.6 + 0.9 * k
        xs = 12.4 + 0.35 if sgn > 0 else 10.6 - 0.35
        for j in range(4):
            xx = xs + sgn * 0.38 * j
            rc(xx - 0.17, y + 0.1 * j, 0.34, 0.34, fc=P.fill(B) if j == 3 else None)
bio.label(ax, (11.5, 0.8), "medullary filaments; laterals at surface", size="tiny", color=P.muted())

# C kelp
head(16.2, "C", "Parenchymatous thallus")
kx, ky = 19.0, 1.8
for a in (-65, -40, -20, 20, 40, 65):
    r = np.radians(a - 90)
    ax.plot([kx, kx + 1.1 * np.cos(r)], [ky, ky + 0.7 * np.sin(r)], color=P.edge(B), lw=2.4, solid_capstyle="round")
ax.add_patch(Rectangle((kx - 0.15, ky), 0.3, 2.0, facecolor=P.fill(B), edgecolor=P.edge(B), lw=1.0))
t = np.linspace(0, 1, 80)
w = 1.0 * np.sin(np.pi * t) ** 0.45
ax.fill(np.r_[kx + w, (kx - w)[::-1]], np.r_[ky + 2.0 + 7.6 * t, (ky + 2.0 + 7.6 * t)[::-1]],
        facecolor=P.light(B), edgecolor=P.edge(B), lw=1.2)
ax.add_patch(Ellipse((kx, ky + 2.15), 0.9, 0.35, facecolor=P.fill("positive"), edgecolor=P.edge("positive"), lw=0.8, zorder=6))
bio.callout(ax, (kx + 0.6, ky + 6.0), (21.4, 9.6), "blade", size="tiny")
bio.callout(ax, (kx + 0.45, ky + 2.15), (21.4, 4.9), "meristem (intercalary)", size="tiny")
bio.callout(ax, (kx + 0.15, ky + 1.0), (21.4, 3.0), "stipe", size="tiny")
bio.callout(ax, (kx + 0.9, ky - 0.5), (21.4, 1.2), "holdfast", size="tiny")

# D cross-section
head(24.6, "D", "Kelp blade, cross-section")
X0, X1, Y0 = 25.0, 33.6, 1.6
H = 9.6
mid = Y0 + H / 2
ax.add_patch(Rectangle((X0, Y0), X1 - X0, H, facecolor=P.fill("extracellular"), edgecolor=P.muted(), lw=0.8, zorder=2))
for side in (1, -1):
    ys = mid + side * (H / 2 - 0.35)
    for x in np.arange(X0 + 0.1, X1 - 0.3, 0.4):
        ax.add_patch(Rectangle((x, ys - 0.25 if side > 0 else ys - 0.15), 0.38, 0.4, facecolor=P.fill(B), edgecolor=P.edge(B), lw=0.6, zorder=5))
    for row in range(2):
        yy = mid + side * (H / 2 - 1.3 - 1.05 * row)
        for x in np.arange(X0 + 0.15, X1 - 0.8, 0.95):
            ax.add_patch(Ellipse((x + 0.45, yy), 0.9, 0.95, facecolor=P.light(B), edgecolor=P.edge(B), lw=0.6, zorder=4))
    ax.add_patch(Ellipse((X0 + 5.4, mid + side * (H / 2 - 1.8)), 0.6, 0.6, facecolor=P.fill("vacuole"), edgecolor=P.edge("vacuole"), lw=0.8, zorder=6))
for k in range(14):
    yy = mid + rng.uniform(-1.3, 1.3)
    x0_ = X0 + rng.uniform(0, 4)
    ax.plot([x0_, x0_ + rng.uniform(3, 5)], [yy, yy + rng.uniform(-0.3, 0.3)], color=P.edge(B), lw=0.9, zorder=3)
bio.label(ax, (X0 + 0.2, Y0 + H + 0.25), "mucilage layer", size="tiny", ha="left", color=P.muted())
bio.callout(ax, (X1 - 1.0, mid + H / 2 - 0.35), (X1 + 0.15, mid + H / 2 - 0.35), "epidermis", size="tiny")
bio.callout(ax, (X1 - 1.2, mid + H / 2 - 2.35), (X1 + 0.15, mid + 2.4), "cortex", size="tiny")
bio.callout(ax, (X0 + 5.4, mid + H / 2 - 1.8), (X0 + 7.0, mid + 3.0), "mucilage duct", size="tiny")
bio.callout(ax, (X1 - 3.4, mid), (X1 + 0.15, mid), "medulla", size="tiny")
# trumpet hyphae joined at a sieve plate
hx, hy = X0 + 2.6, mid - 1.6
t = np.linspace(0, 1, 40)
for sg in (-1, 1):
    xs = hx + sg * (0.15 + 1.6 * t)
    half = 0.08 + 0.32 * (1 - t) ** 3
    ax.fill(np.r_[xs, xs[::-1]], np.r_[hy + half, (hy - half)[::-1]], facecolor=P.fill("cytoplasm"), edgecolor=P.edge(B), lw=1.0, zorder=7)
ax.plot([hx, hx], [hy - 0.42, hy + 0.42], color=P.edge(B), lw=2.2, zorder=8)
for yy in (-0.25, 0.0, 0.25):
    ax.add_patch(Circle((hx, hy + yy), 0.05, color=P.fill("extracellular"), zorder=9))
bio.callout(ax, (hx - 0.6, hy + 0.2), (X0 - 0.1, mid + 0.4), "trumpet hyphae,\nsieve plate", size="tiny")
