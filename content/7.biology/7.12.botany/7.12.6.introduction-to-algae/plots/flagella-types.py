"""Flagellar types of algae. A: tinsel flagellum (two rows of stiff hairs, mastigonemes) and whiplash
flagellum (smooth), with the 9 + 2 axoneme in cross-section. B-I: motile cells of the algal groups,
showing number, relative length, insertion and type of the flagella (hairs drawn as short ticks)."""
import numpy as np
from matplotlib.patches import Circle, Ellipse
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(34, 13.2)
FL = P.edge("flagellum") if "flagellum" else P.ink()


def flag(p0, ang, L, hairs=0, amp=0.12, waves=2.2, lw=1.4, hair_len=0.16, ribbon=False):
    """A flagellum from p0 in direction ang (deg), length L; hairs = 0, 1 (one row) or 2 (two rows)."""
    t = np.linspace(0, 1, 160)
    a = np.radians(ang)
    u = np.array([np.cos(a), np.sin(a)])
    n = np.array([-u[1], u[0]])
    env = np.minimum(1, t * 4)
    off = amp * env * np.sin(2 * np.pi * waves * t)
    pts = p0 + np.outer(t * L, u) + np.outer(off, n)
    ax.plot(pts[:, 0], pts[:, 1], color=P.ink(), lw=lw * (1.8 if ribbon else 1), solid_capstyle="round", zorder=8)
    if hairs:
        d = np.gradient(pts, axis=0)
        d /= np.linalg.norm(d, axis=1)[:, None]
        nn = np.c_[-d[:, 1], d[:, 0]]
        for k in range(12, 160, 9):
            for sgn in ((1, -1) if hairs == 2 else (1,)):
                q = pts[k] + sgn * nn[k] * hair_len
                ax.plot([pts[k, 0], q[0]], [pts[k, 1], q[1]], color=P.muted(), lw=0.7, zorder=7)
    return pts


def body(c, rx, ry, ang=0, tok="chloroplast"):
    ax.add_patch(Ellipse(c, 2 * rx, 2 * ry, angle=ang, facecolor=P.light(tok), edgecolor=P.edge(tok), lw=1.3, zorder=5))


def title(x, y, letter, t, sub):
    bio.panel(ax, letter, (x, y))
    bio.label(ax, (x + 0.55, y - 0.18), t, size="small", bold=True, ha="left", va="top")
    bio.label(ax, (x + 0.55, y - 0.78), sub, size="tiny", ha="left", va="top", color=P.muted())


# A: tinsel vs whiplash, axoneme
title(0.2, 13.0, "A", "Flagellar types", "")
flag(np.array([0.8, 10.2]), 0, 6.0, hairs=2, amp=0.25, waves=2.0, hair_len=0.35)
bio.label(ax, (7.2, 10.2), "tinsel\n(hairy)", size="tiny", ha="left")
flag(np.array([0.8, 8.4]), 0, 6.0, hairs=0, amp=0.25, waves=2.0)
bio.label(ax, (7.2, 8.4), "whiplash\n(smooth)", size="tiny", ha="left")
c = np.array([3.8, 4.6])
ax.add_patch(Circle(c, 1.7, facecolor=P.light("membrane"), edgecolor=P.edge("membrane"), lw=1.3, zorder=4))
for k in range(9):
    a = np.radians(90 - 40 * k)
    q = c + 1.2 * np.array([np.cos(a), np.sin(a)])
    for dd in (-0.13, 0.13):
        r = q + dd * np.array([np.sin(a), -np.cos(a)])
        ax.add_patch(Circle(r, 0.13, facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.8, zorder=6))
for dd in (-0.2, 0.2):
    ax.add_patch(Circle(c + np.array([dd, 0]), 0.14, facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.8, zorder=6))
bio.label(ax, (3.8, 2.4), "axoneme 9 + 2", size="tiny")
bio.label(ax, (3.8, 1.9), "(diatom sperm: 9 + 0)", size="tiny", color=P.muted())

# cells: x positions on two rows
cells = [
    ("B", "Green algae", "2 equal, apical, smooth"),
    ("C", "Stephanokont", "crown of many flagella"),
    ("D", "Euglenids", "1 emergent, 1 short in reservoir"),
    ("E", "Cryptophytes", "2 subapical, both hairy"),
    ("F", "Haptophytes", "2 smooth + haptonema"),
    ("G", "Dinoflagellates", "transverse + longitudinal"),
    ("H", "Heterokonts", "hairy forward, smooth backward"),
    ("I", "Centric diatom sperm", "1 hairy, apical"),
]
pos = [(9.6, 13.0), (15.6, 13.0), (21.6, 13.0), (27.6, 13.0), (9.6, 6.5), (15.6, 6.5), (21.6, 6.5), (27.6, 6.5)]
for (L, t, s), (x, y) in zip(cells, pos):
    title(x, y, L, t, s)

# B green: Chlamydomonas
x, y = 12.6, 8.6
body((x, y), 1.0, 1.3)
flag(np.array([x - 0.15, y + 1.25]), 115, 1.9, amp=0.12)
flag(np.array([x + 0.15, y + 1.25]), 65, 1.9, amp=0.12)
ax.add_patch(Circle((x - 0.75, y + 0.4), 0.13, color=P.edge("negative"), zorder=7))
# C Oedogonium zoospore
x, y = 18.6, 8.6
body((x, y), 1.1, 1.2, tok="chloroplast")
for k, a in enumerate(np.linspace(30, 150, 9)):
    r = np.radians(a)
    p0 = np.array([x + 0.5 * np.cos(r), y + 1.05 + 0.15 * np.sin(r)])
    flag(p0, a, 1.6, amp=0.06, lw=1.0)
# D euglenid
x, y = 24.4, 7.9
body((x, y), 0.8, 1.7, tok="chloroplast")
ax.add_patch(Ellipse((x, y + 1.15), 0.5, 0.6, facecolor=P.fill("vacuole"), edgecolor=P.edge("vacuole"), lw=1, zorder=6))
flag(np.array([x, y + 1.0]), 90, 2.5, hairs=1, amp=0.15, hair_len=0.12)
ax.plot([x, x + 0.15], [y + 1.0, y + 1.25], color=P.ink(), lw=1.3, zorder=8)
ax.add_patch(Circle((x - 0.32, y + 1.25), 0.11, color=P.edge("negative"), zorder=8))
bio.label(ax, (x + 1.0, y + 1.0), "reservoir", size="tiny", ha="left")
# E cryptophyte
x, y = 30.6, 8.5
body((x, y), 0.9, 1.4, ang=-15, tok="highlight")
flag(np.array([x + 0.35, y + 1.25]), 75, 2.3, hairs=2, amp=0.1, hair_len=0.12)
flag(np.array([x + 0.4, y + 1.2]), 40, 2.0, hairs=1, amp=0.1, hair_len=0.12)
# F haptophyte
x, y = 12.6, 2.4
body((x, y), 1.1, 1.1, tok="highlight")
flag(np.array([x - 0.3, y + 1.05]), 120, 2.4, amp=0.14)
flag(np.array([x + 0.3, y + 1.05]), 60, 2.4, amp=0.14)
ax.plot([x, x], [y + 1.1, y + 2.5], color=P.edge("rna"), lw=2.2, zorder=8, solid_capstyle="round")
bio.label(ax, (x - 0.15, y + 2.75), "haptonema", size="tiny", ha="center")
# G dinoflagellate (ventral view)
x, y = 18.6, 2.5
body((x, y), 1.2, 1.5, tok="highlight")
ax.plot([x - 1.2, x + 1.2], [y, y], color=P.edge("highlight"), lw=4, zorder=6, alpha=0.6)
flag(np.array([x - 1.15, y]), 0, 2.3, amp=0.12, waves=4, ribbon=True)
ax.plot([x + 0.05, x + 0.05], [y, y - 1.4], color=P.edge("highlight"), lw=3, zorder=6, alpha=0.6)
flag(np.array([x + 0.05, y - 0.05]), -90, 2.6, amp=0.1)
bio.label(ax, (x + 1.35, y + 0.3), "transverse\nflagellum (girdle)", size="tiny", ha="left")
bio.label(ax, (x + 0.3, y - 2.0), "longitudinal\nflagellum", size="tiny", ha="left")
# H heterokont zoospore (lateral insertion, brown alga)
x, y = 24.6, 2.4
body((x, y), 1.4, 0.9, tok="highlight")
flag(np.array([x - 0.2, y + 0.85]), 135, 2.8, hairs=2, amp=0.12, hair_len=0.14)
flag(np.array([x + 0.1, y + 0.85]), -20, 2.8, amp=0.1)
ax.add_patch(Circle((x + 0.6, y + 0.4), 0.12, color=P.edge("negative"), zorder=7))
bio.label(ax, (x - 2.6, y + 2.7), "forward", size="tiny")
# I diatom sperm
x, y = 30.4, 2.2
body((x, y), 0.6, 0.6, tok="highlight")
flag(np.array([x, y + 0.6]), 90, 2.6, hairs=2, amp=0.12, hair_len=0.12)

bio.label(ax, (33.6, 0.4), "red dot: eyespot (stigma)", size="tiny", color=P.muted(), ha="right")
