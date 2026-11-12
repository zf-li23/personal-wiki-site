# Discharge of a stenotele nematocyst (Hydra), schematic, in three stages, with the time course on a
# log scale. Stylet phase about 700 ns (Nuechter et al. 2006); eversion and muscle twitch: order of magnitude.
import numpy as np
import wikibio as bio
from wikibio import quant
from matplotlib.patches import Ellipse, FancyBboxPatch, Polygon

P = bio.P
fig, ax = bio.canvas(24, 13.0)
CAP = "drug"


def prey(x, y, w=5.0):
    ax.add_patch(FancyBboxPatch((x - w / 2, y), w, 0.7, boxstyle="round,pad=0,rounding_size=0.1",
                                facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=0.8, zorder=3))


def cnidocyte(x, y):
    ax.add_patch(FancyBboxPatch((x - 1.5, y - 2.4), 3.0, 4.6, boxstyle="round,pad=0,rounding_size=0.8",
                                facecolor=P.fill("cytoplasm"), edgecolor=P.edge("cytoplasm"), lw=0.9, zorder=4))
    ax.add_patch(Ellipse((x + 0.6, y - 1.8), 0.7, 0.5, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.7, zorder=6))


def capsule(x, y, coiled=True, open_=False):
    ax.add_patch(Ellipse((x, y), 1.8, 3.0, facecolor=P.fill(CAP), edgecolor=P.edge(CAP), lw=1.2, zorder=6))
    if coiled:
        t = np.linspace(0, 7 * np.pi, 400)
        ax.plot(x + 0.55 * np.sin(t), y + 1.0 - 2.1 * t / t[-1] + 0.12 * np.cos(t), color=P.edge(CAP), lw=1.0, zorder=7)
    if not open_:
        ax.plot([x - 0.35, x + 0.35], [y + 1.5, y + 1.5], color=P.edge(CAP), lw=2.2, zorder=8)  # operculum


xs, yc, ytop = [3.6, 11.2, 18.8], 6.6, 9.9
for i, x in enumerate(xs):
    prey(x, ytop)
    cnidocyte(x, yc)
    bio.label(ax, (x, 12.4), ["1  At rest", "2  Stylet ejection", "3  Tubule eversion"][i], size="normal", bold=True)
# 1: at rest, cnidocil
capsule(xs[0], yc)
ax.plot([xs[0] + 0.9, xs[0] + 1.0], [yc + 2.2, yc + 3.0], color=P.muted(), lw=1.4, zorder=8)
bio.callout(ax, (xs[0] + 1.0, yc + 2.9), (xs[0] + 2.6, yc + 2.0), "Cnidocil", size="small")
bio.callout(ax, (xs[0] - 0.6, yc + 0.9), (xs[0] - 2.8, yc + 2.4), "Capsule\n(~15 MPa)", size="small")
bio.callout(ax, (xs[0] + 0.5, yc - 0.3), (xs[0] - 2.8, yc - 2.9), "Coiled tubule", size="small")
bio.label(ax, (xs[0], ytop + 1.05), "Prey cuticle", size="tiny", color=P.muted())
# 2: capsule open, stylet shot into the prey
capsule(xs[1], yc, open_=True)
x = xs[1]
ax.add_patch(Polygon([(x - 0.35, yc + 1.5), (x + 0.35, yc + 1.5), (x, ytop + 0.55)], closed=True,
                     facecolor=P.edge(CAP), edgecolor=P.edge(CAP), lw=0.8, zorder=9))
bio.callout(ax, (x + 0.15, ytop - 0.6), (x + 2.6, ytop - 1.4), "Stylet", size="small")
bio.label(ax, (x, yc - 3.1), "~700 ns, up to 5.4 million g", size="tiny", color=P.muted())
# 3: tubule everted through the prey
capsule(xs[2], yc, coiled=False, open_=True)
x = xs[2]
t = np.linspace(0, 1, 200)
tx = x + 0.25 * np.sin(t * 10)
ty = yc + 1.5 + t * (ytop + 2.0 - yc - 1.5)
ax.plot(tx, ty, color=P.edge(CAP), lw=2.0, zorder=9)
for k in range(0, 200, 25):
    ax.plot([tx[k] - 0.15, tx[k] + 0.15], [ty[k] - 0.1, ty[k] + 0.1], color=P.edge(CAP), lw=1.0, zorder=9)
bio.callout(ax, (tx[150], ty[150]), (x + 2.6, ytop + 1.6), "Everted tubule\n(venom)", size="small")
bio.label(ax, (x, yc - 3.1), "microseconds to milliseconds", size="tiny", color=P.muted())

# time course
pl = quant.Plot(ax, (3.0, 0.9, 18.0, 0.01), (1e-8, 1), (0, 1), xlog=True, frame=None)
y = 0.9
ax.plot([pl.X(1e-8), pl.X(1)], [y, y], color=P.muted(), lw=0.8)
for e in range(-8, 1):
    xx = pl.X(10.0 ** e)
    ax.plot([xx, xx], [y, y - 0.12], color=P.muted(), lw=0.8)
    bio.label(ax, (xx, y - 0.35), f"$10^{{{e}}}$", size="tiny", color=P.muted())
bio.label(ax, (pl.X(1) + 0.3, y), "s", size="small", color=P.muted(), ha="left")
for (a, b, tok, txt, dy) in [(1e-8, 7e-7, CAP, "Stylet ejection (0.7 µs)", 0.55), (1e-6, 3e-3, "dna", "Tubule eversion", 0.55),
                              (1e-2, 1e-1, "muscle", "Fast muscle twitch", 1.3)]:
    bio.box(ax, ((pl.X(a) + pl.X(b)) / 2, y + dy), pl.X(b) - pl.X(a), 0.42, token=tok, radius=0.08, zorder=8)
    bio.label(ax, ((pl.X(a) + pl.X(b)) / 2, y + dy + 0.45), txt, size="tiny")
