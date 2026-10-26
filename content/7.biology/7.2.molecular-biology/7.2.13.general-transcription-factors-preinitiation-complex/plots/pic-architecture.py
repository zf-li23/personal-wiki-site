# Architecture of the class II preinitiation complex (schematic, not to scale; after the cryo-EM structures).
# The DNA centerline is parameterized by promoter position p (bp): TBP bends it by about 80 degrees at the TATA box
# (p about -28), each arm leaving the apex 40 degrees below horizontal; downstream DNA turns back to horizontal and
# runs through Pol II. Strands separate between -9 and +2 (open complex). TFIIA and TFIIB flank TBP; TFIIB reaches
# into Pol II; TFIIF on the polymerase; TFIIE and TFIIH downstream, XPB gripping DNA about 20-30 bp downstream.
# Bars at the bottom: DNase I footprints of the DAB and DABPolF complexes on a linear position scale.
import math

import numpy as np
import wikibio as bio
from wikibio import molbio as M

P = bio.P
fig, ax = bio.canvas(20.0, 10.0)

SC = 0.14  # canvas units per bp
apex = np.array([5.6, 7.4])


def theta(p):
    """Direction of the DNA centerline (radians) at position p, going downstream."""
    if p < -28:
        return math.radians(40)          # upstream arm rises toward the apex
    if p < -16:
        return math.radians(-40)
    if p < -6:
        return math.radians(-40 + 40 * (p + 16) / 10)
    return 0.0


def centerline(p0, p1, n=400):
    ps = np.linspace(p0, p1, n)
    pts = np.zeros((n, 2))
    # integrate from the apex in both directions
    i0 = int(np.argmin(abs(ps + 28)))
    pts[i0] = apex
    for i in range(i0 + 1, n):
        t = theta(0.5 * (ps[i] + ps[i - 1]))
        pts[i] = pts[i - 1] + SC * (ps[i] - ps[i - 1]) * np.array([math.cos(t), math.sin(t)])
    for i in range(i0 - 1, -1, -1):
        t = theta(0.5 * (ps[i] + ps[i + 1]))
        pts[i] = pts[i + 1] - SC * (ps[i + 1] - ps[i]) * np.array([math.cos(t), math.sin(t)])
    return ps, pts


ps, c = centerline(-62, 62)
d = np.gradient(c, axis=0)
nrm = np.c_[-d[:, 1], d[:, 0]] / np.hypot(d[:, 0], d[:, 1])[:, None]
half = 0.11 + M.bubble_profile(ps, -9, 2, 0.42, ramp=2.5)
top = c + nrm * half[:, None]
bot = c - nrm * half[:, None]


def at(p):
    return c[int(np.argmin(abs(ps - p)))]


# proteins behind the DNA
pol = at(2) + np.array([0.6, 0.15])
bio.protein(ax, tuple(pol), 5.2, 3.6, "enzyme", None, zorder=3)
bio.label(ax, (pol[0] + 0.9, pol[1] - 1.15), "Pol II", size="normal", color=P.on_fill(), zorder=21)
tfiih = at(26) + np.array([1.3, 1.25])
bio.protein(ax, tuple(tfiih), 3.4, 2.4, "carbohydrate", None, zorder=2)
bio.label(ax, (tfiih[0] + 0.6, tfiih[1] + 0.55), "TFIIH", size="small", color=P.on_fill(), zorder=21)
xpb = at(25) + np.array([0.0, 0.42])
bio.protein(ax, tuple(xpb), 1.2, 0.7, "positive", "XPB", size="tiny", zorder=13)
cak = tfiih + np.array([1.35, 1.05])
bio.protein(ax, tuple(cak), 1.5, 0.8, "drug", "CDK7", size="tiny", zorder=4)
tfiie = at(12) + np.array([1.35, 2.0])
bio.protein(ax, tuple(tfiie), 1.5, 0.9, "metabolite", "TFIIE", size="tiny", zorder=6)
tfiif = pol + np.array([-0.15, 1.95])
bio.protein(ax, tuple(tfiif), 1.6, 0.85, "channel", "TFIIF", size="tiny", zorder=6)

# DNA strands (nontemplate on top, template below) over Pol II
M.backbone(ax, top, "dna2", lw=2.6, zorder=10)
M.backbone(ax, bot, "dna", lw=2.6, zorder=10)
for k in range(0, len(ps), 6):
    if half[k] < 0.15:
        ax.plot([top[k, 0], bot[k, 0]], [top[k, 1], bot[k, 1]], color=P.muted(), lw=0.6, zorder=9)

# TBP saddle astride the bend, TFIIA and TFIIB on either side
t = np.linspace(math.radians(25), math.radians(155), 60)
r_in, r_out = 0.42, 1.2
cen = apex + np.array([0, -0.28])
saddle = np.r_[np.c_[cen[0] + r_out * np.cos(t), cen[1] + r_out * np.sin(t)],
               np.c_[cen[0] + r_in * np.cos(t[::-1]), cen[1] + r_in * np.sin(t[::-1])]]
bio.core.shape(ax, saddle, "protein", zorder=12)
bio.label(ax, (apex[0], apex[1] + 1.25), "TBP", size="small", bold=True)
bio.protein(ax, (apex[0] - 2.2, apex[1] + 0.55), 1.6, 0.9, "antibody", "TFIIA", size="tiny", zorder=11)
tfiib = apex + np.array([1.9, 0.35])
bio.protein(ax, tuple(tfiib), 1.5, 0.9, "receptor", "TFIIB", size="tiny", zorder=11)
tail = np.array([tfiib + [0.6, -0.3], tfiib + [1.6, -0.9], at(0) + [0.2, 0.6]])
ax.plot(tail[:, 0], tail[:, 1], color=P.edge("receptor"), lw=3.0, solid_capstyle="round", zorder=11)
bio.label(ax, tuple(tail[-1] + [0.25, -0.05]), "B-reader", size="tiny", color=P.on_fill(), ha="left")

# labels on the DNA
bio.callout(ax, tuple(at(-28) + [0, -0.12]), (apex[0] + 0.05, apex[1] - 3.3), "TATA, bent ~80°", size="tiny")
bio.callout(ax, tuple(at(-4) + [0, -0.5]), (at(-4)[0] - 0.3, at(-4)[1] - 2.75), "open DNA: −9 to +2", size="tiny")
bio.label(ax, tuple(at(-60) + [-0.1, -0.45]), "upstream", size="tiny", color=P.muted())
bio.label(ax, tuple(at(60) + [0.0, -0.5]), "downstream", size="tiny", color=P.muted())
bio.label(ax, tuple(at(62) + [0.35, 0.55]), "nontemplate", size="tiny", color=P.edge("dna2"), ha="left")
bio.label(ax, tuple(at(62) + [0.35, -0.4]), "template", size="tiny", color=P.edge("dna"), ha="left")
bio.arrow(ax, (pol[0] + 2.2, pol[1] - 2.0), (pol[0] + 3.4, pol[1] - 2.0), kind="process")
bio.label(ax, (pol[0] + 2.8, pol[1] - 2.35), "transcription", size="tiny", color=P.muted())

# footprints on a linear scale
y0, x0 = 1.35, 4.0
XS = 0.13


def X(p):
    return x0 + (p + 50) * XS


ax.plot([X(-50), X(40)], [y0, y0], color=P.ink(), lw=1.2)
for tk in [-40, -20, 1, 20, 40]:
    ax.plot([X(tk), X(tk)], [y0 - 0.06, y0 - 0.18], color=P.muted(), lw=0.8)
    bio.label(ax, (X(tk), y0 - 0.4), ("+1" if tk == 1 else f"{tk:+d}".replace("-", "−")), size="tiny", color=P.muted())
for (a, b, name, yy, tok) in [(-42, -17, "DAB", y0 + 0.45, "receptor"), (-42, 17, "DABPolF", y0 + 0.95, "enzyme")]:
    bio.box(ax, ((X(a) + X(b)) / 2, yy), X(b) - X(a), 0.26, tok, None, radius=0.05)
    bio.label(ax, (X(b) + 0.2, yy), name, size="tiny", ha="left")
bio.label(ax, (x0 - 0.3, y0 + 0.7), "DNase I\nfootprints", size="tiny", ha="right", color=P.muted())
