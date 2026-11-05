"""Reproduction of Fucus (gametic meiosis). A: thallus with dichotomous branches, midrib, air bladders and
swollen receptacles at the branch tips; dots are conceptacle openings. B: a conceptacle in section (monoecious
example): the ostiole is lined with periphyses; oogonia (each with 8 eggs after meiosis and one mitosis) sit on
the wall, antheridia (64 sperm) on branched filaments, among sterile paraphyses. C: the cycle: the thallus is
diploid; meiosis in oogonia and antheridia gives eggs and sperm directly; the zygote grows into a new thallus."""
import numpy as np
from matplotlib.patches import Circle, Ellipse, Wedge
import wikibio as bio

P = bio.P
rng = np.random.default_rng(5)
fig, ax = bio.canvas(32, 13)
B = "highlight"

# A thallus
bio.panel(ax, "A", (0.2, 12.8))
def branch(p, ang, L, depth):
    a = np.radians(ang)
    q = p + L * np.array([np.cos(a), np.sin(a)])
    ax.plot([p[0], q[0]], [p[1], q[1]], color=P.edge(B), lw=7 - depth * 1.2, solid_capstyle="round", zorder=4)
    ax.plot([p[0], q[0]], [p[1], q[1]], color=P.light(B), lw=4.5 - depth * 1.0, solid_capstyle="round", zorder=5)
    if depth == 1:
        m = (p + q) / 2
        ax.add_patch(Ellipse(m, 0.45, 0.6, angle=ang, facecolor=P.fill("cytoplasm"), edgecolor=P.edge(B), lw=1.0, zorder=6))
    if depth < 3:
        branch(q, ang + 24, L * 0.8, depth + 1)
        branch(q, ang - 24, L * 0.8, depth + 1)
    else:
        r = q + 0.55 * np.array([np.cos(a), np.sin(a)])
        ax.add_patch(Ellipse(r, 0.7, 1.3, angle=ang - 90, facecolor=P.fill(B), edgecolor=P.edge(B), lw=1.0, zorder=6))
        for k in range(4):
            ax.add_patch(Circle(r + rng.normal(0, 0.15, 2), 0.05, color=P.edge(B), zorder=7))
branch(np.array([5.0, 0.8]), 90, 3.0, 0)
ax.plot([4.4, 5.6], [0.7, 0.7], color=P.edge(B), lw=3)
bio.callout(ax, (6.9, 9.8), (8.4, 11.8), "receptacle", size="tiny")
bio.callout(ax, (5.6, 4.95), (8.0, 5.6), "air bladder", size="tiny")
bio.callout(ax, (5.0, 1.0), (7.6, 1.0), "holdfast", size="tiny")

# B conceptacle
bio.panel(ax, "B", (10.4, 12.8))
cx, cy, R = 16.0, 5.8, 4.2
ax.add_patch(Circle((cx, cy), R + 1.0, facecolor=P.light(B), edgecolor=P.edge(B), lw=1.2, zorder=2))
ax.add_patch(Circle((cx, cy), R, facecolor=P.fill("extracellular"), edgecolor=P.edge(B), lw=1.0, zorder=3))
ax.add_patch(Wedge((cx, cy), R + 1.05, 82, 98, width=1.15, facecolor=P.fill("extracellular"), edgecolor="none", zorder=4))
for x in (cx - 0.35, cx + 0.35):
    for k in range(4):
        ax.plot([x, x + np.sign(x - cx) * -0.2], [cy + R - 0.3 + 0.25 * k, cy + R + 0.3 + 0.25 * k], color=P.edge(B), lw=0.8, zorder=5)
bio.label(ax, (cx, cy + R + 1.4), "ostiole with periphyses", size="tiny")
for a in np.linspace(200, 340, 9):
    r = np.radians(a)
    base = np.array([cx, cy]) + R * np.array([np.cos(r), np.sin(r)])
    inward = -np.array([np.cos(r), np.sin(r)])
    for k in range(5):
        p0 = base + inward * (0.4 + 0.45 * k)
        ax.plot(*np.c_[base, p0 + inward * 0.2].T if False else ([base[0], p0[0]], [base[1], p0[1]]), color=P.muted(), lw=0.7, zorder=4)
# oogonia
for a in (215, 265, 320):
    r = np.radians(a)
    p = np.array([cx, cy]) + (R - 0.9) * np.array([np.cos(r), np.sin(r)])
    ax.add_patch(Circle(p, 0.75, facecolor=P.fill("ovule"), edgecolor=P.edge(B), lw=1.0, zorder=6))
    for k in range(8):
        ax.add_patch(Circle(p + 0.42 * np.array([np.cos(k * np.pi / 4), np.sin(k * np.pi / 4)]), 0.16, facecolor=P.fill("positive"), edgecolor=P.edge("positive"), lw=0.5, zorder=7))
# antheridia
for a in (160, 20, 240, 295):
    r = np.radians(a)
    base = np.array([cx, cy]) + R * np.array([np.cos(r), np.sin(r)])
    inward = -np.array([np.cos(r), np.sin(r)])
    stem = base + inward * 1.3
    ax.plot([base[0], stem[0]], [base[1], stem[1]], color=P.edge("rna"), lw=1.0, zorder=5)
    for side in (-0.5, 0.5):
        q = stem + 0.5 * np.array([inward[1] * side, -inward[0] * side])
        ax.plot([stem[0], q[0]], [stem[1], q[1]], color=P.edge("rna"), lw=0.9, zorder=5)
        ax.add_patch(Ellipse(q, 0.32, 0.5, angle=np.degrees(r), facecolor=P.fill("rna"), edgecolor=P.edge("rna"), lw=0.7, zorder=6))
bio.callout(ax, (cx + (R - 0.9) * np.cos(np.radians(320)), cy + (R - 0.9) * np.sin(np.radians(320))), (22.0, 1.0), "oogonium (8 eggs)", size="tiny")
bio.callout(ax, (cx + (R - 1.5) * np.cos(np.radians(20)), cy + (R - 1.5) * np.sin(np.radians(20))), (22.0, 8.0), "antheridia (64 sperm each)", size="tiny")
bio.callout(ax, (15.08, 3.3), (10.8, 1.2), "paraphyses", size="tiny")

# C cycle
bio.panel(ax, "C", (24.4, 12.8))
items = [((28.0, 10.6), "Thallus (2n)"), ((30.2, 6.6), "Oogonia and\nantheridia"), ((28.0, 2.6), "Eggs and sperm (n)"), ((25.8, 6.6), "Zygote (2n)")]
for (xy, t) in items:
    bio.box(ax, xy, 2.8, 1.2, token="neutral", text=t, size="tiny")
bio.arrow(ax, (29.0, 10.0), (30.0, 7.3), kind="process", head=0.16)
bio.arrow(ax, (30.0, 5.9), (29.0, 3.2), kind="process", head=0.16)
bio.label(ax, (30.6, 4.2), "Meiosis", size="small", bold=True, color=P.edge("rna"))
bio.arrow(ax, (27.0, 3.2), (26.0, 5.9), kind="process", head=0.16)
bio.label(ax, (25.0, 4.4), "Fertilization", size="small", bold=True, color=P.edge("dna"))
bio.arrow(ax, (26.0, 7.3), (27.0, 10.0), kind="process", head=0.16)
