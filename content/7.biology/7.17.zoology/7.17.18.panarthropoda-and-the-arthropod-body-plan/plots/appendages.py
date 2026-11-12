# Arthropod limbs (schematic). A generalized limb has a basal protopod (coxa and basis) and a distal
# telopod; the protopod bears medial endites (e.g. gnathobases for chewing) and lateral exites (e.g. gills,
# epipods). A: a biramous limb (crustaceans, trilobites): the basis carries two rami, an inner endopod and
# an outer exopod. B: a uniramous limb (an insect leg): a single series of podomeres, coxa, trochanter,
# femur, tibia, tarsus and pretarsus, without an exopod (the trochanter is often homologized with the basis). Colours mark the protopod (grey-blue), endopod
# (teal) and exopod (orange); joints are arthrodial membranes.
import numpy as np
from matplotlib.patches import FancyBboxPatch
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24, 11)


def seg(a, b, w, tok, z=6):
    a, b = np.asarray(a, float), np.asarray(b, float)
    d = b - a
    L = np.linalg.norm(d)
    ang = np.degrees(np.arctan2(d[1], d[0]))
    p = FancyBboxPatch((0, -w / 2), L, w, boxstyle="round,pad=0,rounding_size=%.3f" % (w * 0.45),
                       facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.9, zorder=z)
    import matplotlib.transforms as mt
    p.set_transform(mt.Affine2D().rotate_deg(ang).translate(*a) + ax.transData)
    ax.add_patch(p)


def chain(start, dirs, lens, widths, tok, gap=0.07):
    pts = [np.asarray(start, float)]
    for dg, L in zip(dirs, lens):
        r = np.radians(dg)
        pts.append(pts[-1] + L * np.array([np.cos(r), np.sin(r)]))
    for i in range(len(lens)):
        u = pts[i + 1] - pts[i]
        u = u / np.linalg.norm(u)
        seg(pts[i] + u * gap, pts[i + 1] - u * gap, widths[i], tok)
    return pts


# body wall
for x0 in (0.8, 13.0):
    ax.add_patch(FancyBboxPatch((x0, 9.0), 9.6, 1.3, boxstyle="round,pad=0,rounding_size=0.3",
                                facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=0.9, zorder=4))
    bio.label(ax, (x0 + 4.8, 9.65), "Body (sternite)", size="small")

# A: biramous
c = chain((5.0, 9.0), [-90, -90], [1.3, 1.2], [1.2, 1.05], "neutral")          # coxa, basis
endo = chain(c[-1], [-100, -110, -100, -95, -90], [1.0, 1.0, 0.9, 0.8, 0.6], [0.7, 0.62, 0.55, 0.48, 0.38], "enzyme")
exo = chain(c[-1] + np.array([0.3, 0.1]), [-35, -45, -55], [1.3, 1.2, 1.0], [0.55, 0.45, 0.35], "rna")
for k, tip in enumerate(np.linspace(0, 1, 7)):  # setae on exopod
    p = exo[1] + (exo[3] - exo[1]) * tip
    ax.plot([p[0], p[0] + 0.5], [p[1], p[1] + 0.25], color=P.edge("rna"), lw=0.6, zorder=7)
# exite (epipod gill) on the coxa
seg((5.6, 8.4), (7.4, 8.0), 0.55, "chloroplast")
# endite (gnathobase) on the coxa
seg((4.4, 8.3), (3.2, 8.1), 0.45, "neutral")
bio.panel(ax, "A", (0.3, 10.9))
bio.label(ax, (5.6, 0.5), "Biramous limb (crustacean)", size="normal", bold=True)
bio.callout(ax, (5.0, 8.4), (1.0, 8.9), "Coxa", size="small")
bio.callout(ax, (5.0, 7.1), (1.0, 6.5), "Basis", size="small")
bio.callout(ax, (3.4, 8.1), (1.0, 7.6), "Endite", size="small")
bio.callout(ax, (7.2, 8.05), (9.6, 8.4), "Exite (epipod)", size="small")
bio.callout(ax, exo[2], (9.6, 6.0), "Exopod", size="small")
bio.callout(ax, endo[3], (1.0, 3.6), "Endopod", size="small")
ax.plot([0.6, 0.6], [6.0, 9.0], color=P.muted(), lw=0.9)

# B: uniramous insect leg
names = ["Coxa", "Trochanter", "Femur", "Tibia", "Tarsus"]
toks = ["neutral", "neutral", "enzyme", "enzyme", "enzyme"]
pts = [np.array([17.5, 9.0])]
spec = [(-80, 1.2, 1.1), (-60, 0.7, 0.85), (-20, 3.2, 0.8), (-80, 3.0, 0.55), (-60, 1.6, 0.4)]
for dg, L, w in spec:
    r = np.radians(dg)
    pts.append(pts[-1] + L * np.array([np.cos(r), np.sin(r)]))
for i, (dg, L, w) in enumerate(spec):
    u = (pts[i + 1] - pts[i]) / L
    seg(pts[i] + u * 0.07, pts[i + 1] - u * 0.07, w, toks[i])
tip = pts[-1]
ax.plot([tip[0], tip[0] + 0.35], [tip[1], tip[1] - 0.25], color=P.ink(), lw=1.4, zorder=8)
ax.plot([tip[0], tip[0] + 0.1], [tip[1], tip[1] - 0.4], color=P.ink(), lw=1.4, zorder=8)
offs = [(-3.0, 0.2), (-3.2, -0.4), (0.6, 1.2), (1.3, 0.2), (1.1, 0.0)]
for i, nm in enumerate(names):
    mid = (pts[i] + pts[i + 1]) / 2
    bio.callout(ax, mid, mid + np.array(offs[i]), nm, size="small")
bio.callout(ax, tip + np.array([0.2, -0.3]), tip + np.array([1.4, -0.6]), "Pretarsus (claws)", size="small")
bio.panel(ax, "B", (12.5, 10.9))
bio.label(ax, (17.8, 0.5), "Uniramous limb (insect leg)", size="normal", bold=True)
# legend
for i, (tok, txt) in enumerate((("neutral", "Protopod"), ("enzyme", "Endopod / telopod"), ("rna", "Exopod"), ("chloroplast", "Exite"))):
    bio.box(ax, (13.4, 4.2 - i * 0.6), 0.45, 0.32, tok)
    bio.label(ax, (13.8, 4.2 - i * 0.6), txt, size="small", ha="left")
