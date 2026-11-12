# Acorn worm (Enteropneusta) in schematic sagittal section: three body regions with their coeloms,
# stomochord, heart-glomerulus complex, gill slits, nerve cords and the two main blood vessels.
import numpy as np
import wikibio as bio
from matplotlib.patches import Polygon

P = bio.P
fig, ax = bio.canvas(24.0, 9.4)


def poly(pts, face, edge, z=5, lw=0.9):
    ax.add_patch(Polygon(np.asarray(pts), closed=True, facecolor=face, edgecolor=edge, lw=lw, zorder=z,
                         joinstyle="round"))


def tok(t, z=5, lw=0.9):
    return dict(face=P.fill(t), edge=P.edge(t), z=z, lw=lw)


def light(t, z=5, lw=0.9):
    return dict(face=P.light(t), edge=P.edge(t), z=z, lw=lw)


Y = 4.6  # body axis
# ---- body outline (epidermis), three regions
prob = bio.smooth_closed([(0.6, Y + 0.1), (1.2, Y + 1.2), (2.6, Y + 1.5), (4.0, Y + 1.0), (4.6, Y + 0.35),
                          (4.6, Y - 0.25), (3.9, Y - 0.9), (2.5, Y - 1.2), (1.1, Y - 0.9)])
poly(prob, **light("ectoderm", z=3))
poly([(4.4, Y + 0.32), (5.1, Y + 0.32), (5.1, Y - 0.12), (4.4, Y - 0.12)], **light("ectoderm", z=2.9))  # stalk
collar = bio.smooth_closed([(4.95, Y + 0.9), (5.6, Y + 1.25), (7.0, Y + 1.2), (7.4, Y + 1.05), (7.4, Y - 1.05),
                            (7.0, Y - 1.2), (5.6, Y - 1.25), (4.95, Y - 0.75), (4.85, Y + 0.05)])
poly(collar, **light("ectoderm", z=3))
xs = np.linspace(7.3, 22.6, 60)
half = 1.05 - 0.55 * (xs - 7.3) / (22.6 - 7.3)
top = np.c_[xs, Y + half]
bot = np.c_[xs[::-1], Y - half[::-1]]
trunk = np.vstack([top, [(22.9, Y)], bot])
poly(trunk, **light("ectoderm", z=3))

# ---- coeloms
proto = bio.smooth_closed([(1.0, Y + 0.1), (1.5, Y + 1.0), (2.6, Y + 1.25), (3.8, Y + 0.85), (4.2, Y + 0.3),
                           (3.8, Y - 0.6), (2.5, Y - 0.95), (1.3, Y - 0.7)])
poly(proto, **tok("coelom", z=4))
for sgn in (1, -1):  # paired mesocoels (dorsal and ventral halves of the section)
    meso = bio.smooth_closed([(5.25, Y + sgn * 0.45), (5.7, Y + sgn * 1.05), (7.0, Y + sgn * 1.0),
                              (7.2, Y + sgn * 0.55), (6.4, Y + sgn * 0.4)])
    poly(meso, **light("coelom", z=4))
mt_top = np.c_[xs[1:-2], Y + half[1:-2] - 0.12]
mt_bot = np.c_[xs[1:-2][::-1], Y + 0.62 * half[1:-2][::-1]]
poly(np.vstack([mt_top, mt_bot]), **dict(face=P.mix(P.light("coelom"), P.surface(), 0.35), edge=P.edge("coelom"),
                                         z=4, lw=0.6))
mb_top = np.c_[xs[1:-2], Y - 0.62 * half[1:-2]]
mb_bot = np.c_[xs[1:-2][::-1], Y - half[1:-2][::-1] + 0.12]
poly(np.vstack([mb_top, mb_bot]), **dict(face=P.mix(P.light("coelom"), P.surface(), 0.35), edge=P.edge("coelom"),
                                         z=4, lw=0.6))

# ---- gut: buccal cavity, pharynx, oesophagus, hepatic region, intestine, anus
gx = np.linspace(4.9, 22.75, 80)
gh = np.where(gx < 7.4, 0.32, np.interp(gx, [7.4, 12.0, 12.6, 15.5, 22.75], [0.55, 0.55, 0.3, 0.32, 0.12]))
gut = np.vstack([np.c_[gx, Y + gh], np.c_[gx[::-1], Y - gh[::-1]]])
poly(gut, **tok("endoderm", z=6))
poly([(4.75, Y - 0.05), (5.05, Y + 0.22), (5.05, Y - 0.42)], face=P.surface(), edge=P.edge("endoderm"), z=6.5)  # mouth
# hepatic sacculations (dorsal outpocketings of the intestine)
for x in np.arange(13.0, 16.6, 0.6):
    poly(bio.smooth_closed([(x - 0.22, Y + 0.3), (x - 0.1, Y + 0.68), (x + 0.12, Y + 0.68), (x + 0.22, Y + 0.3)]),
         **tok("endoderm", z=6))
# stomochord: blind rod from the roof of the buccal cavity into the proboscis base
poly(bio.smooth_closed([(5.2, Y + 0.18), (4.3, Y + 0.2), (3.6, Y + 0.12), (3.45, Y), (3.6, Y - 0.1),
                        (4.3, Y - 0.06), (5.2, Y - 0.02)]), face=P.edge("endoderm"), edge=P.edge("endoderm"), z=7)
# heart vesicle above the central sinus; glomerulus in front
poly(bio.blob((3.95, Y + 0.48), 0.42, 0.2, seed=2), **tok("muscle", z=7))
poly(bio.blob((3.0, Y + 0.25), 0.42, 0.32, wobble=0.25, seed=5, k=11), **tok("blood", z=7))
# gill slits: U-shaped openings in the dorsal pharynx wall leading to gill pores
for k, x in enumerate(np.arange(7.9, 12.0, 0.5)):
    ax.plot([x - 0.12, x - 0.12, x + 0.12, x + 0.12], [Y + 0.55, Y + 0.15, Y + 0.15, Y + 0.55],
            color=P.edge("endoderm"), lw=1.1, zorder=8, solid_capstyle="round")
    ax.plot([x, x], [Y + 0.55, Y + 0.95], color=P.edge("ectoderm"), lw=1.0, zorder=8)
    ax.add_patch(Polygon(bio.blob((x, Y + 1.0), 0.07, 0.05, wobble=0, seed=1), closed=True,
                         facecolor=P.surface(), edgecolor=P.edge("ectoderm"), lw=0.7, zorder=9))
# proboscis pore (dorsal, at the proboscis stalk)
ax.add_patch(Polygon(bio.blob((4.55, Y + 0.36), 0.07, 0.06, wobble=0, seed=1), closed=True,
                     facecolor=P.surface(), edgecolor=P.edge("coelom"), lw=0.8, zorder=9))

# ---- blood vessels: dorsal (forward flow) and ventral (backward flow)
bl = P.edge("blood")
ax.plot([4.0, 7.4, 22.0], [Y + 0.68, Y + 0.72, Y + 0.48], color=bl, lw=1.6, zorder=6.8)
ax.plot([3.3, 7.4, 22.0], [Y - 0.45, Y - 0.72, Y - 0.38], color=bl, lw=1.6, zorder=6.8)
bio.arrow(ax, (19.2, Y + 0.56), (17.4, Y + 0.6), kind="process", color=bl, lw=1.2, head=0.18)
bio.arrow(ax, (17.4, Y - 0.5), (19.2, Y - 0.46), kind="process", color=bl, lw=1.2, head=0.18)

# ---- nervous system: collar cord (internalized), dorsal and ventral trunk cords
ne = P.edge("neuron")
poly([(5.1, Y + 0.98), (7.35, Y + 0.95), (7.35, Y + 0.8), (5.1, Y + 0.85)], **tok("neuron", z=8, lw=0.6))
ax.plot(xs, Y + half - 0.05, color=ne, lw=1.0, zorder=8, dashes=(3, 1.5))
ax.plot(xs, Y - half + 0.05, color=ne, lw=1.0, zorder=8, dashes=(3, 1.5))

# ---- region brackets
for x0, x1, name in ((0.6, 4.7, "Proboscis (prosome)"), (4.85, 7.4, "Collar (mesosome)"),
                     (7.4, 22.9, "Trunk (metasome)")):
    yb = Y + 2.15
    ax.plot([x0, x0, x1, x1], [yb - 0.15, yb, yb, yb - 0.15], color=P.muted(), lw=0.9, zorder=9)
    bio.label(ax, ((x0 + x1) / 2, yb + 0.35), name, size="small")
bio.label(ax, (9.95, Y + 1.75), "Pharynx with gill slits", size="small")
bio.label(ax, (14.8, Y + 1.75), "Hepatic region", size="small")

# ---- callouts
C = bio.callout
C(ax, (1.7, Y + 0.6), (0.9, 8.4), "Protocoel")
C(ax, (3.0, Y + 0.25), (0.9, 1.6), "Glomerulus")
C(ax, (3.95, Y + 0.55), (3.5, 8.4), "Heart vesicle")
C(ax, (3.7, Y + 0.05), (3.0, 1.2), "Stomochord")
C(ax, (4.55, Y + 0.4), (5.3, 8.4), "Proboscis pore")
C(ax, (4.85, Y - 0.15), (5.0, 1.2), "Mouth")
C(ax, (6.6, Y + 0.9), (8.2, 8.4), "Collar cord")
C(ax, (6.4, Y - 0.8), (7.0, 1.2), "Mesocoel")
C(ax, (11.4, Y + 1.0), (11.4, 8.4), "Gill pore")
C(ax, (12.5, Y - 0.75), (9.6, 1.2), "Metacoel")
C(ax, (16.6, Y + 0.6), (16.6, 8.4), "Dorsal vessel")
C(ax, (17.6, Y - 0.49), (13.2, 1.2), "Ventral vessel")
C(ax, (20.0, Y - 0.58), (17.4, 1.2), "Ventral nerve cord")
C(ax, (20.0, Y + 0.55), (20.2, 8.4), "Dorsal nerve cord")
C(ax, (22.8, Y), (22.0, 1.2), "Anus")
