# Water vascular system of a sea star: (A) oral-view schematic with Loven's ray labels,
# (B) the hydraulics of one tube foot, (C) arm cross-section template with the system highlighted.
import numpy as np
import wikibio as bio
from matplotlib.patches import Polygon, Circle, Ellipse

P = bio.P
fig, ax = bio.canvas(28.0, 10.6)
W = "channel"  # water vascular system
we, wf = P.edge(W), P.fill(W)

# ---------------------------------------------------------------- A: oral view
bio.panel(ax, "A", (0.2, 10.3))
c = np.array([5.0, 4.9])
ang = {"A": 270, "B": 198, "C": 126, "D": 54, "E": 342}
th = np.linspace(0, 2 * np.pi, 600)
r = 1.75 + 2.75 * (0.5 + 0.5 * np.cos(5 * (th - np.radians(270)))) ** 2.2
ax.add_patch(Polygon(np.c_[c[0] + r * np.cos(th), c[1] + r * np.sin(th)], closed=True,
                     facecolor=P.light("animal"), edgecolor=P.edge("animal"), lw=1.0, zorder=2))
ax.add_patch(Circle(c, 0.42, facecolor=P.surface(), edgecolor=P.edge("animal"), lw=0.9, zorder=6))  # mouth
ax.add_patch(Circle(c, 0.8, facecolor="none", edgecolor=we, lw=3.0, zorder=7))  # ring canal
for name, a in ang.items():
    u = np.array([np.cos(np.radians(a)), np.sin(np.radians(a))])
    n = np.array([-u[1], u[0]])
    p0, p1 = c + u * 0.8, c + u * 4.15
    ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=we, lw=2.2, zorder=7)
    for k, s in enumerate(np.linspace(1.25, 3.85, 9)):
        side = 1 if k % 2 == 0 else -1
        q = c + u * s
        f = q + n * side * 0.32
        ax.plot([q[0], f[0]], [q[1], f[1]], color=we, lw=1.0, zorder=7)
        ax.add_patch(Circle(f, 0.11, facecolor=wf, edgecolor=we, lw=0.7, zorder=8))
    tip = c + u * 4.3
    ax.add_patch(Circle(tip, 0.13, facecolor=P.fill("negative"), edgecolor=P.edge("negative"), lw=0.7, zorder=8))
    bio.label(ax, c + u * 4.85, name, size="small", bold=True)
for a in (162, 234, 306, 18):  # Polian vesicles in four interradii
    u = np.array([np.cos(np.radians(a)), np.sin(np.radians(a))])
    q = c + u * 0.8
    ax.add_patch(Ellipse(q + u * 0.32, 0.55, 0.22, angle=a, facecolor=P.light(W), edgecolor=we, lw=0.8, zorder=8))
for a in (18, 90, 162, 234, 306):  # paired Tiedemann's bodies
    for d in (-11, 11):
        u = np.array([np.cos(np.radians(a + d)), np.sin(np.radians(a + d))])
        ax.add_patch(Circle(c + u * 0.8, 0.09, facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.6, zorder=9))
mad = c + np.array([0, 1.75])
ax.plot([c[0], mad[0]], [c[1] + 0.8, mad[1] - 0.25], color=we, lw=2.0, zorder=7, dashes=(2.5, 1.2))
ax.add_patch(Circle(mad, 0.27, facecolor=P.surface(), edgecolor=we, lw=1.1, ls="--", zorder=8))
C = bio.callout
C(ax, mad + (0.25, 0.1), (8.6, 9.9), "Madreporite (aboral)")
C(ax, c + (0.1, 1.25), (8.9, 9.1), "Stone canal")
C(ax, c + (0.75, -0.3), (9.5, 2.3), "Ring canal")
C(ax, c + np.array([np.cos(np.radians(306)), np.sin(np.radians(306))]) * 1.12, (9.6, 1.4), "Polian vesicle")
C(ax, c + np.array([np.cos(np.radians(29)), np.sin(np.radians(29))]) * 0.8, (9.6, 6.8), "Tiedemann's body")
C(ax, c + np.array([np.cos(np.radians(198)), np.sin(np.radians(198))]) * 2.6, (0.4, 2.0), "Radial canal")
tf = c + np.array([np.cos(np.radians(342)), np.sin(np.radians(342))]) * 3.2
C(ax, tf + np.array([np.cos(np.radians(72)), np.sin(np.radians(72))]) * 0.32, (9.6, 5.6), "Tube foot")
C(ax, c + np.array([np.cos(np.radians(126)), np.sin(np.radians(126))]) * 4.3, (0.4, 9.9), "Terminal tentacle")

# ---------------------------------------------------------------- B: one tube foot, two phases
bio.panel(ax, "B", (11.9, 10.3))
for k, (x, amp_h, pod_l, title) in enumerate(((13.8, 0.45, 3.2, "Ampulla contracts:\npodium extends"),
                                              (16.9, 1.15, 1.4, "Podium shortens:\nfluid returns"))):
    yb = 6.2  # ambulacral plate level
    ax.add_patch(Polygon([(x - 1.2, yb), (x + 1.2, yb), (x + 1.2, yb - 0.3), (x - 1.2, yb - 0.3)], closed=True,
                         facecolor=P.light("bone"), edgecolor=P.edge("bone"), lw=0.8, zorder=4))
    ax.add_patch(Ellipse((x, yb + 0.25 + amp_h), 0.95 if k else 0.6, 2 * amp_h, facecolor=P.light(W), edgecolor=we,
                         lw=1.0, zorder=5))
    ax.plot([x - 1.3, x - 0.25], [yb + 0.55, yb + 0.55], color=we, lw=1.6, zorder=5)  # lateral canal
    ax.plot([x - 0.45, x - 0.45], [yb + 0.42, yb + 0.68], color=P.ink(), lw=1.6, zorder=6)  # valve
    pod = np.array([(x - 0.25, yb + 0.25), (x - 0.22, yb - pod_l), (x + 0.22, yb - pod_l), (x + 0.25, yb + 0.25)])
    ax.add_patch(Polygon(pod, closed=True, facecolor=wf, edgecolor=we, lw=1.0, zorder=5))
    ax.add_patch(Ellipse((x, yb - pod_l - 0.05), 0.75, 0.18, facecolor=P.fill("protein"), edgecolor=P.edge("protein"),
                         lw=0.8, zorder=6))
    ax.plot([x - 1.3, x + 1.3], [yb - pod_l - 0.16] * 2, color=P.muted(), lw=1.2, zorder=3)
    if k == 0:
        bio.arrow(ax, (x + 0.55, yb + 0.9), (x + 0.55, yb - 1.6), kind="process", color=we, lw=1.2)
    else:
        bio.arrow(ax, (x + 0.85, yb - 1.0), (x + 0.85, yb + 1.0), kind="process", color=we, lw=1.2)
    bio.label(ax, (x, 9.6), title, size="small")
C(ax, (13.8, 6.9), (12.3, 8.4), "Ampulla")
C(ax, (13.35, 6.55), (12.3, 7.4), "Valve")
C(ax, (17.1, 5.3), (18.2, 4.2), "Podium")
C(ax, (17.2, 4.75), (18.2, 3.3), "Adhesive disc")
C(ax, (17.9, 6.05), (18.2, 5.6), "Ambulacral plate")

# ---------------------------------------------------------------- C: arm cross-section
bio.panel(ax, "C", (20.4, 10.3))
ID = "wikimedia/sea-star-arm"
kw = dict(at=(23.9, 5.4), height=2.6, rotate=0)
bio.icon(ax, "wikimedia/sea-star-arm", parts={"water-vascular": "channel"}, mute="neutral", **kw)
pt = lambda part: bio.icon_part(ID, part, **kw)
C(ax, pt("water-vascular"), (24.4, 1.6), "Water vascular system")
C(ax, pt("digestive"), (21.8, 8.6), "Pyloric caeca")
C(ax, pt("radial-nerve"), (21.0, 2.6), "Radial nerve")
C(ax, pt("body-wall"), (24.6, 9.4), "Body wall with ossicles")
