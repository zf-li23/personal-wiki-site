"""The stages of M phase in an animal cell (schematic; three chromosome pairs shown, a diploid cell has more).

1 Prophase: chromosomes condense inside the intact nucleus; the duplicated centrosomes nucleate asters and
move apart along the nuclear envelope. 2 Prometaphase: the nuclear envelope breaks down (fragments remain
as ER); microtubules from both poles capture kinetochores, at first laterally; chromosomes move.
3 Metaphase: every chromosome is bi-oriented, its sister kinetochores attached to opposite poles, and the
chromosomes are aligned on the metaphase plate. 4 Anaphase: cohesin is cleaved; sister chromatids move to
the poles (anaphase A) and the poles move apart (anaphase B). 5 Telophase: nuclear envelopes re-form around
the decondensing chromosomes; the contractile ring begins to constrict the cell between the two nuclei over
the spindle midzone. 6 Cytokinesis: the furrow has ingressed to a narrow bridge containing the midbody,
which is cut by abscission; each daughter has one nucleus and one centrosome.
"""

import math

import numpy as np
from matplotlib.patches import Arc, Circle, Ellipse, PathPatch
from matplotlib.path import Path

import wikibio as bio
from wikibio import cytoskel as C
from wikibio.core import smooth_closed

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(4)

fig, ax = bio.canvas(27.0, 13.6)
W, H = 4.0, 2.9  # half-axes of a cell


def cell(c, rx=W, ry=H, waist=0.0):
    th = np.linspace(0, 2 * np.pi, 80, endpoint=False)
    x = rx * np.cos(th)
    y = ry * np.sin(th) * (1 - waist * np.exp(-(x / (0.35 * rx)) ** 2))
    pts = smooth_closed(np.c_[x + c[0], y + c[1]], n=300)
    ax.add_patch(PathPatch(Path(pts, closed=True), facecolor=P.fill("cytoplasm"), edgecolor=P.edge("membrane"),
                           lw=1.4, zorder=2))


def condensing(c, n=3, spread=0.75, thin=False):
    for k in range(n):
        x0 = c[0] + rng.uniform(-spread, spread)
        y0 = c[1] + rng.uniform(-spread * 0.8, spread * 0.8)
        t = np.linspace(-0.45, 0.45, 30)
        th = rng.uniform(0, np.pi)
        u = np.array([math.cos(th), math.sin(th)])
        nrm = np.array([-u[1], u[0]])
        for o in (-0.06, 0.06):
            pts = np.array([x0, y0]) + t[:, None] * u + (o + 0.05 * np.sin(14 * t))[:, None] * nrm
            ax.plot(pts[:, 0], pts[:, 1], color=P.edge("chromatin"), lw=1.0 if thin else 2.2, solid_capstyle="round",
                    zorder=6)


def nucleus(c, r=1.25, dashed=False):
    if dashed:
        for a0 in range(0, 360, 45):
            ax.add_patch(Arc(c, 2 * r, 2 * r, theta1=a0, theta2=a0 + 25, color=P.edge("nucleus"), lw=1.6, zorder=5))
    else:
        ax.add_patch(Circle(c, r, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=1.3, zorder=4))


def caption(c, num, name):
    bio.label(ax, (c[0] - W + 0.1, c[1] + H + 0.35), f"{num}  {name}", size="small", bold=True, ha="left")


cols = [4.4, 13.5, 22.6]
rows = [10.0, 3.4]

# 1 prophase
c = (cols[0], rows[0])
cell(c)
nucleus(c, 1.35)
condensing(c, n=4, spread=0.7)
for dx, ang in ((-1.75, (95, 265)), (1.75, (-85, 85))):
    C.centrosome(ax, (c[0] + dx, c[1] + 0.9), size=0.32, microtubules=9, length=1.3, angles=ang, lw=1.0)
caption(c, 1, "Prophase")
bio.label(ax, (c[0], c[1] - 2.2), "condensation; asters separate", size="tiny", color=P.muted())

# 2 prometaphase
c = (cols[1], rows[0])
cell(c)
nucleus(c, 1.6, dashed=True)
poles = [np.array([c[0] - 2.4, c[1]]), np.array([c[0] + 2.4, c[1]])]
chroms = [(-0.95, 0.75, 30), (0.75, -0.75, 120), (0.15, 0.45, 75)]
for (dx, dy, ang) in chroms:
    q = (c[0] + dx, c[1] + dy)
    cp = C.chromatid_pair(ax, q, length=0.6, width=0.12, angle=ang, facing=ang - 90, zorder=11)
for k, (dx, dy, ang) in enumerate(chroms):
    q = np.array([c[0] + dx, c[1] + dy])
    pole = poles[0] if k != 1 else poles[1]
    C.mt_line(ax, pole, q + (0.25 if k != 1 else -0.25) * np.array([-1, 0]), lw=1.0, zorder=8)
for pole, s in zip(poles, (-1, 1)):
    for a in np.linspace(-70, 70, 6):
        th = math.radians(a)
        d = np.array([-s * math.cos(th), math.sin(th)])
        C.mt_line(ax, pole, pole + 1.6 * d, lw=0.9, plus=True, zorder=7)
    for a in np.linspace(-60, 60, 4):
        th = math.radians(a)
        d = np.array([s * math.cos(th), math.sin(th)])
        C.mt_line(ax, pole, pole + 0.9 * d, lw=0.9, zorder=7)
    C.centrosome(ax, pole, size=0.3, microtubules=0, length=0.1, lw=1.0)
caption(c, 2, "Prometaphase")
bio.label(ax, (c[0], c[1] - 2.2), "envelope breaks down; capture", size="tiny", color=P.muted())

# 3 metaphase
c = (cols[2], rows[0])
cell(c)
C.spindle(ax, c, half_length=2.5, height=2.7, chromosomes=3, astral=5, interpolar=2, kmts=2, chrom_length=0.55, lw=1.0)
caption(c, 3, "Metaphase")
bio.label(ax, (c[0], c[1] - 2.2), "bi-orientation; metaphase plate", size="tiny", color=P.muted())

# 4 anaphase
c = (cols[0], rows[1])
cell(c, rx=W * 1.05, ry=H * 0.95)
C.spindle(ax, c, half_length=2.6, height=2.4, chromosomes=3, astral=3, interpolar=3, kmts=2, chrom_length=0.55, lw=1.0,
          stage="anaphase")
caption(c, 4, "Anaphase")
bio.label(ax, (c[0], c[1] - 2.2), "sisters separate (A); poles part (B)", size="tiny", color=P.muted())

# 5 telophase
c = (cols[1], rows[1])
cell(c, rx=W * 1.05, ry=H * 0.95, waist=0.3)
for s in (-1, 1):
    q = (c[0] + s * 2.4, c[1])
    nucleus(q, 0.85)
    condensing(q, n=3, spread=0.4, thin=True)
    C.centrosome(ax, (q[0] + s * 0.95, q[1] + 0.6), size=0.28, microtubules=0, length=0.1, lw=1.0)
for y in (-0.35, -0.12, 0.12, 0.35):
    C.mt_line(ax, (c[0] - 1.4, c[1] + y), (c[0] + 0.15, c[1] + y * 0.6), lw=0.9, zorder=7)
    C.mt_line(ax, (c[0] + 1.4, c[1] + y), (c[0] - 0.15, c[1] + y * 0.6), lw=0.9, zorder=7)
for s in (-1, 1):
    ax.plot([c[0] - 0.12, c[0] + 0.12], [c[1] + s * H * 0.66, c[1] + s * H * 0.66], color=P.edge("muscle"), lw=4.5,
            solid_capstyle="round", zorder=9)
caption(c, 5, "Telophase")
bio.label(ax, (c[0], c[1] - 1.6), "nuclei re-form; furrow starts", size="tiny", color=P.muted())

# 6 cytokinesis
c = (cols[2], rows[1])
for s in (-1, 1):
    q = (c[0] + s * 2.05, c[1])
    ax.add_patch(Ellipse(q, 3.9, 4.0, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("membrane"), lw=1.4, zorder=2))
    nucleus((q[0] + s * 0.3, q[1]), 0.8)
    condensing((q[0] + s * 0.3, q[1]), n=3, spread=0.35, thin=True)
    C.centrosome(ax, (q[0] + s * 1.1, q[1] + 0.7), size=0.26, microtubules=6, length=0.8, lw=0.9)
ax.add_patch(PathPatch(Path(np.array([[c[0] - 0.3, c[1] - 0.12], [c[0] + 0.3, c[1] - 0.12], [c[0] + 0.3, c[1] + 0.12],
                                      [c[0] - 0.3, c[1] + 0.12], [c[0] - 0.3, c[1] - 0.12]]), closed=True),
                       facecolor=P.fill("cytoplasm"), edgecolor="none", zorder=3))
for s_ in (-1, 1):
    ax.plot([c[0] - 0.32, c[0] + 0.32], [c[1] + s_ * 0.12, c[1] + s_ * 0.12], color=P.edge("membrane"), lw=1.4, zorder=4)
ax.add_patch(Ellipse(c, 0.36, 0.26, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.8, zorder=6))
bio.callout(ax, (c[0], c[1] + 0.12), (c[0] + 0.6, c[1] + 2.5), "midbody", size="tiny")
caption(c, 6, "Cytokinesis")
bio.label(ax, (c[0], c[1] - 2.35), "abscission of the bridge", size="tiny", color=P.muted())

# arrows between panels
for (x0, y0), (x1, y1) in (((8.5, 10.0), (9.3, 10.0)), ((17.6, 10.0), (18.4, 10.0)), ((8.7, 3.4), (9.2, 3.4)),
                           ((17.85, 3.4), (18.35, 3.4))):
    bio.arrow(ax, (x0, y0), (x1, y1), kind="process", color=P.muted())
