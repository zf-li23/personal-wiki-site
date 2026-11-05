"""From spores to the ovule: five schematic steps in the evolution of the seed (after the fossil series of
Devonian and Early Carboniferous seed plants). A homosporous sporangium with many equal spores; a
heterosporous megasporangium with a tetrad of large megaspores; a single functional megaspore retained in
the megasporangium (nucellus), forming an endosporic female gametophyte with archegonia; free
integumentary lobes around the nucellus, the nucellus apex modified into a pollen-receiving chamber, the
whole overtopped by a cupule (preovule, as in Elkinsia); the lobes fused into an integument with only a
micropyle open, a pollination drop catching pollen (ovule). Bottom: unit of dispersal at each step."""
import numpy as np
from matplotlib.patches import Circle, Ellipse, PathPatch, Polygon
from matplotlib.path import Path

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30, 11.5)
XS = [3.0, 9.0, 15.0, 21.0, 27.0]
Y0 = 4.2  # base of each structure


def poly(pts, token, lw=1.0, z=6, light=False):
    fc = P.light(token) if light else P.fill(token)
    ax.add_patch(Polygon(np.asarray(pts), closed=True, facecolor=fc, edgecolor=P.edge(token), lw=lw, joinstyle="round",
                         zorder=z))


def sac(cx, w, h, token="ovule", z=6):
    """A sporangium-like sac: rounded base on Y0, tapering apex."""
    t = np.linspace(0, 2 * np.pi, 120)
    x = cx + 0.5 * w * np.sin(t) * (1 - 0.18 * (np.cos(t) > 0) * np.cos(t))
    y = Y0 + 0.5 * h + 0.5 * h * np.cos(t)
    poly(np.c_[x, y], token, lw=1.1, z=z)


def stalk(cx):
    ax.plot([cx, cx], [Y0 - 0.9, Y0 + 0.05], color=P.edge("plant"), lw=3.0, solid_capstyle="round", zorder=5)


# A: homospory
cx = XS[0]
stalk(cx)
sac(cx, 2.4, 3.2, token="animal")
rng = np.random.default_rng(3)
for k in range(46):
    p = (cx + rng.uniform(-0.85, 0.85), Y0 + rng.uniform(0.35, 2.85))
    if ((p[0] - cx) / 1.05) ** 2 + ((p[1] - Y0 - 1.6) / 1.45) ** 2 < 1:
        ax.add_patch(Circle(p, 0.11, facecolor=P.fill("lipid"), edgecolor=P.edge("lipid"), lw=0.5, zorder=8))

# B: heterospory, megasporangium with one tetrad
cx = XS[1]
stalk(cx)
sac(cx, 2.4, 3.2, token="ovule")
for k, (dx, dy) in enumerate(((-0.42, 0.42), (0.42, 0.42), (-0.42, -0.42), (0.42, -0.42))):
    ax.add_patch(Circle((cx + dx, Y0 + 1.6 + dy), 0.4, facecolor=P.fill("lipid"), edgecolor=P.edge("lipid"), lw=0.9, zorder=8))

# C: one functional megaspore, endosporic female gametophyte
cx = XS[2]
stalk(cx)
sac(cx, 2.4, 3.2, token="ovule")
ax.add_patch(Ellipse((cx, Y0 + 1.35), 1.5, 1.95, facecolor=P.fill("lipid"), edgecolor=P.edge("lipid"), lw=1.3, zorder=8))
for k in range(3):
    ax.add_patch(Circle((cx - 0.25 + 0.25 * k, Y0 + 2.55 + 0.05 * (k == 1)), 0.1, facecolor=P.light("lipid"),
                        edgecolor=P.edge("lipid"), lw=0.5, zorder=8))
for gx in np.linspace(cx - 0.55, cx + 0.55, 5):
    ax.plot([gx, gx], [Y0 + 0.55, Y0 + 2.15], color=P.edge("lipid"), lw=0.35, zorder=9)
for gy in np.linspace(Y0 + 0.65, Y0 + 2.05, 5):
    ax.plot([cx - 0.62, cx + 0.62], [gy, gy], color=P.edge("lipid"), lw=0.35, zorder=9)
for dx in (-0.3, 0.3):
    ax.add_patch(Ellipse((cx + dx, Y0 + 2.05), 0.28, 0.42, facecolor=P.fill("receptor"), edgecolor=P.edge("receptor"), lw=0.7,
                         zorder=10))

# D: preovule: free integumentary lobes, cupule, pollen chamber
cx = XS[3]
stalk(cx)
for sgn in (-1, 1):  # cupule lobes (sterile, dichotomous)
    poly([(cx + sgn * 0.6, Y0 - 0.1), (cx + sgn * 1.95, Y0 + 3.2), (cx + sgn * 1.75, Y0 + 3.4), (cx + sgn * 1.45, Y0 + 2.6),
          (cx + sgn * 1.35, Y0 + 3.6), (cx + sgn * 1.15, Y0 + 3.55), (cx + sgn * 1.25, Y0 + 2.2), (cx + sgn * 0.4, Y0)],
         "plant", lw=0.8, z=5, light=True)
sac(cx, 1.5, 2.6, token="ovule", z=7)
ax.add_patch(Ellipse((cx, Y0 + 1.1), 0.95, 1.4, facecolor=P.fill("lipid"), edgecolor=P.edge("lipid"), lw=1.0, zorder=8))
poly([(cx - 0.3, Y0 + 2.45), (cx - 0.22, Y0 + 2.95), (cx + 0.22, Y0 + 2.95), (cx + 0.3, Y0 + 2.45)], "ovule", lw=0.8, z=8)
for k, dx in enumerate((-0.95, -0.55, 0.55, 0.95)):  # free integumentary lobes, tips curving inward
    tip = cx + dx * 0.55
    poly([(cx + dx - 0.12, Y0), (cx + dx * 1.05 - 0.1, Y0 + 2.4), (tip, Y0 + 3.05), (cx + dx * 1.05 + 0.08, Y0 + 2.4),
          (cx + dx + 0.12, Y0)], "bract", lw=0.8, z=9)

# E: ovule with fused integument, micropyle and pollination drop
cx = XS[4]
stalk(cx)
t = np.linspace(-np.pi * 0.86, np.pi * 0.86, 100)
outer = np.c_[cx + 1.15 * np.sin(t), Y0 + 1.6 - 1.6 * np.cos(t)]
inner = np.c_[cx + 0.8 * np.sin(t[::-1]), Y0 + 1.75 - 1.4 * np.cos(t[::-1])]
poly(np.vstack([outer, inner]), "bract", lw=1.0, z=7)
sac(cx, 1.45, 2.65, token="ovule", z=6)
ax.add_patch(Ellipse((cx, Y0 + 1.15), 0.95, 1.45, facecolor=P.fill("lipid"), edgecolor=P.edge("lipid"), lw=1.0, zorder=8))
for dx in (-0.22, 0.22):
    ax.add_patch(Ellipse((cx + dx, Y0 + 1.7), 0.2, 0.32, facecolor=P.fill("receptor"), edgecolor=P.edge("receptor"), lw=0.6, zorder=9))
ax.add_patch(Circle((cx, Y0 + 3.55), 0.42, facecolor=P.light("vacuole"), edgecolor=P.edge("vacuole"), lw=0.9, zorder=9))
for dx, dy in ((-0.15, 0.08), (0.17, -0.05), (0.0, 0.25)):
    ax.add_patch(Circle((cx + dx, Y0 + 3.55 + dy), 0.09, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=0.5, zorder=10))

# arrows and labels
for a, b in zip(XS[:-1], XS[1:]):
    bio.arrow(ax, (a + 1.55, Y0 + 1.6), (b - 1.55, Y0 + 1.6), kind="process")
heads = ["1 Homospory", "2 Heterospory", "3 One megaspore retained", "4 Preovule", "5 Ovule"]
subs = ["many equal spores\nin one sporangium", "few large megaspores,\nmany small microspores",
        "endosporic female\ngametophyte, archegonia", "free integumentary lobes,\ncupule, pollen chamber",
        "fused integument,\nmicropyle, pollination drop"]
for x, h, s in zip(XS, heads, subs):
    bio.label(ax, (x, 10.9), h, size="normal", bold=True)
    bio.label(ax, (x, 9.85), s, size="small", color=P.muted())
bio.callout(ax, (XS[2] + 0.62, Y0 + 2.15), (XS[2] + 1.9, Y0 + 3.75), "archegonium")
bio.callout(ax, (XS[2] - 0.7, Y0 + 2.9), (XS[2] - 1.9, Y0 + 3.75), "nucellus")
bio.callout(ax, (XS[3] + 1.2, Y0 + 1.5), (XS[3] + 2.3, Y0 + 0.2), "cupule")
bio.callout(ax, (XS[3] - 0.55, Y0 + 1.9), (XS[3] - 2.4, Y0 + 4.6), "integumentary lobe")
bio.callout(ax, (XS[4] + 1.05, Y0 + 2.4), (XS[4] + 1.9, Y0 + 4.4), "integument")
bio.callout(ax, (XS[4] - 0.35, Y0 + 3.65), (XS[4] - 1.6, Y0 + 4.6), "pollination drop")
bio.callout(ax, (XS[4] + 0.45, Y0 + 0.9), (XS[4] + 1.9, Y0 - 0.4), "female gametophyte")

# unit of dispersal
units = ["spore", "megaspore / microspore", "megasporangium\nwith megaspore", "preovule (seed)", "seed"]
ax.plot([XS[0] - 2.5, XS[-1] + 2.5], [1.95, 1.95], color=P.muted(), lw=0.6)
bio.label(ax, (XS[0] - 2.5, 2.35), "Unit of dispersal:", size="small", bold=True, ha="left")
for x, u in zip(XS, units):
    bio.label(ax, (x, 1.35), u, size="small", italic=False)
bio.label(ax, (XS[0], 0.55), "Rhyniophytes, ferns", size="tiny", color=P.muted())
bio.label(ax, (XS[1], 0.55), r"$\it{Selaginella}$, $\it{Archaeopteris}$", size="tiny", color=P.muted())
bio.label(ax, (XS[2], 0.55), "heterosporous lineages", size="tiny", color=P.muted())
bio.label(ax, (XS[3], 0.55), r"$\it{Runcaria}$ (c. 385 Ma), $\it{Elkinsia}$ (c. 365 Ma)", size="tiny", color=P.muted())
bio.label(ax, (XS[4], 0.55), "Carboniferous seed ferns onward", size="tiny", color=P.muted())
