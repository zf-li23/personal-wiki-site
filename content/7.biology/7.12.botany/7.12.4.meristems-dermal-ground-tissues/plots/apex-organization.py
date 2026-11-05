"""Organization of the apical meristems (schematic, longitudinal sections). A: shoot apex of an
angiosperm, tunica-corpus view: two tunica layers (L1, L2) divide only anticlinally and stay single
layers; the corpus (L3) divides in all planes. Dashed lines: the cytohistological zones that cut across the
layers: the central zone of slowly dividing stem cells at the summit, the peripheral zone on the flanks,
where leaf primordia arise, and the rib zone below, which makes the pith in vertical files. B: the
WUSCHEL-CLAVATA3 feedback loop: cells of the organizing centre below the stem cells express WUS, whose
protein moves up and keeps the stem cells and their CLV3 expression; the CLV3 peptide, sensed by CLV1 and
related receptors, represses WUS. C: root apex, histogen view: plerome (future stele), periblem (cortex)
and dermatogen (epidermis) arise from separate tiers of initials; a calyptrogen forms the root cap.
"""

import math

import numpy as np
from matplotlib.patches import Polygon

import wikibio as bio
from wikibio import botany as B

P = bio.P
fig, ax = bio.canvas(29.0, 12.4)

# ---------- A: shoot apex built from cells
bio.panel(ax, "A", (0.1, 12.3))
C = np.array([6.0, 0.4])
R = 7.2
s = 0.6
sec = B.Section(seed=7)
arc = (math.radians(30), math.radians(150))
sec.ring(C, R - 0.5 * s, s, "epidermis", spacing=s * 0.9, arc=arc)
sec.ring(C, R - 1.5 * s, s, "cambium", spacing=s * 0.9, arc=arc)
YB = 1.0


def corpus(pts):
    d = np.hypot(*(pts - C).T)
    ok = (d < R - 2.05 * s) & (pts[:, 1] > YB)
    return [("ground" if o else None) for o in ok], np.full(len(pts), s * 0.95)


sec.fill((-1.5, YB, 13.5, 8.0), corpus, s * 0.9)
sec.mirror_circle(C, R)
sec.box_ghosts((-1.6, YB - 0.2, 13.6, 8.2), s)
dome = np.r_[[[C[0] + R * math.cos(t), C[1] + R * math.sin(t)] for t in np.linspace(arc[0], arc[1], 80)],
             [[C[0] + R * math.cos(arc[1]), YB], [C[0] + R * math.cos(arc[0]), YB]]]
clip = Polygon(dome, closed=True, transform=ax.transData)
sec.draw(ax, clip=clip)
ax.plot(dome[:80, 0], dome[:80, 1], color=P.edge("cell_wall"), lw=1.2, zorder=8)
ax.set_xlim(0, 29)
ax.set_ylim(0, 12.4)
# leaf primordia: bulges on the flanks
for sgn in (-1, 1):
    a0 = math.radians(90 + sgn * 50)
    p = C + (R - 0.25) * np.array([math.cos(a0), math.sin(a0)])
    n = np.array([math.cos(a0), math.sin(a0)])
    tg = np.array([-n[1], n[0]])
    t = np.linspace(0, math.pi, 30)
    bump = np.array([p + tg * 1.0 * math.cos(u) + n * 1.1 * math.sin(u) for u in t])
    ax.add_patch(Polygon(bump, closed=True, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.2, zorder=8))
top = C + R * np.array([0, 1])
# zones: central zone (stem cells), organizing centre below it, rib zone
t = np.linspace(0, 2 * math.pi, 80)
czc = (6.0, top[1] - 1.35)
ax.plot(czc[0] + 1.45 * np.cos(t), czc[1] + 1.25 * np.sin(t), color=P.edge("negative"), lw=1.4, ls=(0, (3, 2)), zorder=9)
occ = (6.0, top[1] - 3.25)
ax.plot(occ[0] + 0.85 * np.cos(t), occ[1] + 0.55 * np.sin(t), color=P.edge("dna"), lw=1.4, zorder=9)
ax.plot([5.0, 5.0, 7.0, 7.0], [YB, top[1] - 4.0, top[1] - 4.0, YB], color=P.muted(), lw=1.2, ls=(0, (3, 2)), zorder=9)
bio.label(ax, (7.75, czc[1] + 0.2), "CZ", size="small", color=P.edge("negative"), bold=True)
bio.label(ax, (7.35, occ[1]), "OC", size="tiny", color=P.edge("dna"), bold=True)
bio.label(ax, (6.0, 1.9), "RZ", size="small", color=P.muted(), bold=True)
bio.label(ax, (2.2, 4.1), "PZ", size="small", color=P.muted(), bold=True)
bio.label(ax, (9.8, 4.1), "PZ", size="small", color=P.muted(), bold=True)
bio.callout(ax, (6.3, top[1] - 0.3), (13.2, 9.6), "L1  tunica (anticlinal only)", size="tiny")
bio.callout(ax, (6.9, top[1] - 0.9), (13.2, 8.9), "L2  tunica", size="tiny")
bio.callout(ax, (8.4, 4.6), (13.2, 8.2), "L3  corpus (all planes)", size="tiny")
bio.callout(ax, (1.0, 6.5), (0.4, 9.9), "Leaf primordium", size="tiny")
bio.label(ax, (13.3, 7.2), "CZ  central zone (stem cells)", size="tiny", ha="left")
bio.label(ax, (13.3, 6.6), "OC  organizing centre", size="tiny", ha="left")
bio.label(ax, (13.3, 6.0), "PZ  peripheral zone (leaf primordia)", size="tiny", ha="left")
bio.label(ax, (13.3, 5.4), "RZ  rib zone (pith files)", size="tiny", ha="left")

# ---------- B: WUS-CLV3 loop
bio.panel(ax, "B", (12.4, 4.2))
bio.box(ax, (14.6, 2.4), 2.6, 1.1, token="negative", text="stem cells\n(CLV3)", size="tiny")
bio.box(ax, (18.6, 2.4), 2.6, 1.1, token="dna", text="organizing\ncentre (WUS)", size="tiny")
bio.arrow(ax, (17.25, 2.75), (15.95, 2.75), kind="activation", bend=-0.25)
bio.arrow(ax, (15.95, 2.05), (17.25, 2.05), kind="inhibition", bend=-0.25)
bio.label(ax, (16.6, 3.55), "WUS protein moves up", size="tiny", color=P.muted())
bio.label(ax, (16.6, 1.2), "CLV3 peptide via CLV1", size="tiny", color=P.muted())

# ---------- C: root apex, histogens
bio.panel(ax, "C", (21.0, 12.3))
x0 = 25.0
yb = 2.0


def profile(w, y_tip):
    """Left-right outline of a rounded tier: half-width w, tip at y_tip, up to y = 11.8."""
    t = np.linspace(-math.pi / 2, math.pi / 2, 40)
    tip = np.c_[x0 + w * np.sin(t), y_tip + w * (1 - np.cos(t)) * 1.0]
    return np.r_[[[x0 - w, 11.8]], tip, [[x0 + w, 11.8]]]


tiers = [(2.4, 0.7, "bract", "Root cap"), (1.9, 2.3, "cell_wall", "Dermatogen (epidermis)"),
         (1.65, 2.6, "cytoplasm", "Periblem (cortex)"), (0.8, 3.1, "pericycle", "Plerome (stele)")]
for w, y_tip, tk, name in tiers:
    o = profile(w, y_tip)
    if tk == "bract":
        o = np.r_[o[:1], o[1:-1], o[-1:]]
        o[0, 1] = o[-1, 1] = 5.2
    ax.add_patch(Polygon(o, closed=True, facecolor=P.fill(tk), edgecolor=P.edge(tk), lw=1.0, zorder=3 + w * -0.1 + 1))
# initials
for y, tk in ((2.45, "negative"), (2.72, "negative"), (3.25, "negative")):
    ax.plot([x0 - 0.35, x0 + 0.35], [y, y], color=P.edge(tk), lw=2.2, zorder=8)
bio.callout(ax, (x0 + 1.5, 1.4), (27.2, 0.7), "Root cap (calyptrogen)", size="tiny")
bio.callout(ax, (x0 + 1.78, 7.0), (27.5, 8.0), "Dermatogen", size="tiny")
bio.callout(ax, (x0 + 1.2, 6.0), (27.5, 6.6), "Periblem", size="tiny")
bio.callout(ax, (x0 + 0.3, 7.6), (27.5, 9.4), "Plerome", size="tiny")
bio.callout(ax, (x0 - 0.3, 2.72), (21.6, 3.6), "Initials", size="tiny")
bio.label(ax, (27.5, 7.6), "(epidermis)", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (27.5, 6.2), "(cortex)", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (27.5, 9.0), "(stele)", size="tiny", color=P.muted(), ha="left")
