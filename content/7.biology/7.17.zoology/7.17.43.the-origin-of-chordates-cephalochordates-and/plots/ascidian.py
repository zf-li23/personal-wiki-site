# Solitary ascidian, schematic: (A) tadpole larva, (B) settlement and retrogressive metamorphosis,
# (C) adult in sagittal section. Colours as in the lancelet figure (notochord orange, nerve tissue yellow,
# pharynx and gut yellow, tunic neutral).
import numpy as np
import wikibio as bio
from matplotlib.patches import Polygon, Ellipse

P = bio.P
fig, ax = bio.canvas(31.0, 12.0)
NOTO, NERVE, GUT, MUSC, GONAD = "drug", "neuron", "endoderm", "muscle", "nucleolus"


def poly(pts, face, edge, z=5, lw=0.9):
    ax.add_patch(Polygon(np.asarray(pts), closed=True, facecolor=face, edgecolor=edge, lw=lw, zorder=z,
                         joinstyle="round"))


def ell(c, w, h, tok, z=6, lw=0.8, light=False, angle=0.0):
    ax.add_patch(Ellipse(c, w, h, angle=angle, facecolor=P.light(tok) if light else P.fill(tok),
                         edgecolor=P.edge(tok), lw=lw, zorder=z))


TUNIC = dict(face=P.fill("extracellular"), edge=P.edge("neutral"))


def larva(x0, y0, s=1.0, tail=1.0, label=False):
    """Tadpole larva, anterior to the left; ``tail`` (0..1) is the fraction of the tail not yet resorbed."""
    def T(x, y):
        return (x0 + s * x, y0 + s * y)
    L = 7.0 * tail
    # tail fin (larval tunic) and tail
    if tail > 0.05:
        xs = np.linspace(2.6, 2.6 + L, 60)
        fin = 0.75 * np.sin(np.pi * np.clip((xs - 2.6) / L, 0, 1)) ** 0.5 + 0.05
        poly([T(x, y) for x, y in np.vstack([np.c_[xs, fin], np.c_[xs[::-1], -fin[::-1]]])], z=3, lw=0.7, **TUNIC)
        tw = 0.38 * (1 - 0.7 * (xs - 2.6) / L)
        poly([T(x, y) for x, y in np.vstack([np.c_[xs, tw], np.c_[xs[::-1], -tw[::-1]]])],
             face=P.light(MUSC), edge=P.edge(MUSC), z=4, lw=0.7)
        # notochord: a single row of cells
        nx = np.linspace(2.7, 2.6 + 0.95 * L, 22)
        for a, b in zip(nx[:-1], nx[1:]):
            h = 0.17 * (1 - 0.6 * (a - 2.6) / L)
            poly([T(a, -h), T(b, -h), T(b, h), T(a, h)], face=P.fill(NOTO), edge=P.edge(NOTO), z=5, lw=0.5)
        # dorsal nerve cord above the notochord
        ax.plot(*zip(*[T(x, 0.26 * (1 - 0.6 * (x - 2.6) / L)) for x in np.linspace(2.0, 2.6 + 0.9 * L, 40)]),
                color=P.edge(NERVE), lw=2.2 * s, zorder=5.5, solid_capstyle="round")
    # trunk
    trunk = bio.smooth_closed([(0.0, 0.1), (0.3, 0.9), (1.4, 1.25), (2.5, 0.9), (2.9, 0.2), (2.8, -0.6),
                               (1.6, -1.05), (0.4, -0.75)])
    poly([T(x, y) for x, y in trunk], z=4, lw=0.8, **TUNIC)
    inner = bio.smooth_closed([(0.35, 0.1), (0.6, 0.75), (1.4, 1.0), (2.3, 0.75), (2.6, 0.15), (2.5, -0.45),
                               (1.6, -0.82), (0.6, -0.55)])
    poly([T(x, y) for x, y in inner], face=P.light("ectoderm"), edge=P.edge("ectoderm"), z=4.2, lw=0.6)
    # pharynx and endostyle rudiments
    ell(T(1.25, -0.1), 1.3 * s, 0.85 * s, GUT, z=4.6, light=True)
    ax.plot(*zip(T(0.75, -0.48), T(1.75, -0.48)), color=P.edge(GUT), lw=2.0 * s, zorder=4.7)
    # sensory vesicle with ocellus and otolith; visceral ganglion
    ell(T(1.6, 0.6), 0.9 * s, 0.5 * s, NERVE, z=5, light=True)
    ax.add_patch(Ellipse(T(1.35, 0.6), 0.16 * s, 0.16 * s, facecolor=P.ink(), edgecolor=P.ink(), zorder=5.6))
    ax.add_patch(Ellipse(T(1.85, 0.68), 0.18 * s, 0.13 * s, facecolor=P.ink(), edgecolor=P.ink(), zorder=5.6))
    ell(T(2.4, 0.35), 0.35 * s, 0.3 * s, NERVE, z=5.2)
    # adhesive papillae
    for yy in (0.55, 0.05, -0.45):
        poly([T(0.02, yy - 0.12), T(-0.3, yy), T(0.02, yy + 0.12)], face=P.fill("positive"),
             edge=P.edge("positive"), z=5, lw=0.6)
    return T


# ---------------- (A) tadpole larva ----------------
T = larva(1.2, 8.6, 1.4)
bio.panel(ax, "A", (0.4, 11.5))
C = bio.callout
C(ax, T(-0.25, 0.55), (0.8, 10.9), "Adhesive papillae")
C(ax, T(1.35, 0.6), (2.6, 11.5), "Ocellus")
C(ax, T(1.85, 0.68), (4.6, 11.5), "Otolith")
C(ax, T(1.6, 0.85), (5.6, 10.9), "Sensory vesicle")
C(ax, T(2.4, 0.35), (7.8, 11.5), "Visceral ganglion")
C(ax, T(4.5, 0.23), (10.0, 10.9), "Dorsal nerve cord")
C(ax, T(8.5, 0.35), (13.4, 11.5), "Larval tunic (fin)")
C(ax, T(1.25, -0.25), (0.8, 6.2), "Pharynx rudiment")
C(ax, T(1.6, -0.48), (4.4, 5.6), "Endostyle rudiment")
C(ax, T(5.0, -0.25), (8.8, 6.2), "Tail muscle (unsegmented)")
C(ax, T(6.0, 0.0), (12.4, 5.6), "Notochord (40 cells)")

# ---------------- (B) metamorphosis ----------------
bio.panel(ax, "B", (0.4, 5.3))
ground = 0.6
ax.plot([0.6, 15.5], [ground, ground], color=P.muted(), lw=1.2, zorder=2)
for x in np.arange(0.8, 15.5, 0.4):
    ax.plot([x, x - 0.25], [ground, ground - 0.25], color=P.muted(), lw=0.6, zorder=2)


def mini(xc, stage):
    """Stage 1: attached larva; 2: tail resorbing; 3: rotating juvenile; 4: young adult with siphons."""
    g = ground
    if stage in (1, 2):
        Lt = 3.2 if stage == 1 else 1.1
        trunk = bio.smooth_closed([(xc - 0.55, g + 0.15), (xc + 0.55, g + 0.15), (xc + 0.7, g + 0.9),
                                   (xc + 0.3, g + 1.5), (xc - 0.3, g + 1.5), (xc - 0.7, g + 0.9)])
        poly(trunk, z=4, lw=0.8, **TUNIC)
        ell((xc, g + 0.95), 0.75, 0.6, GUT, z=4.5, light=True)
        for dx in (-0.3, 0, 0.3):
            poly([(xc + dx - 0.1, g + 0.18), (xc + dx, g), (xc + dx + 0.1, g + 0.18)], face=P.fill("positive"),
                 edge=P.edge("positive"), z=5, lw=0.5)
        ys = np.linspace(g + 1.45, g + 1.45 + Lt, 30)
        poly(np.vstack([np.c_[xc - 0.17 + 0.0 * ys, ys], np.c_[(xc + 0.17) + 0.0 * ys, ys][::-1]]),
             face=P.light(MUSC), edge=P.edge(MUSC), z=4.4, lw=0.6)
        ax.plot([xc, xc], [g + 1.45, g + 1.4 + Lt], color=P.edge(NOTO), lw=2.2, zorder=4.6)
    elif stage == 3:
        body = bio.smooth_closed([(xc - 0.9, g + 0.1), (xc + 0.9, g + 0.1), (xc + 1.0, g + 0.9), (xc + 0.5, g + 1.6),
                                  (xc - 0.6, g + 1.5), (xc - 1.0, g + 0.8)])
        poly(body, z=4, lw=0.8, **TUNIC)
        ell((xc, g + 0.9), 1.2, 0.95, GUT, z=4.5, light=True)
        ell((xc - 0.5, g + 0.35), 0.35, 0.3, NOTO, z=4.8)          # resorbed tail remnant
        bio.arrow(ax, (xc + 1.15, g + 0.6), (xc + 0.65, g + 1.75), kind="process", bend=-0.35, lw=1.0, head=0.16,
                  color=P.muted())
    else:
        body = bio.smooth_closed([(xc - 0.8, g + 0.1), (xc + 0.8, g + 0.1), (xc + 0.95, g + 1.5), (xc + 0.8, g + 2.5),
                                  (xc + 0.15, g + 2.7), (xc - 0.15, g + 2.6), (xc - 0.7, g + 2.4), (xc - 0.95, g + 1.4)])
        poly(body, z=4, lw=0.8, **TUNIC)
        ell((xc - 0.05, g + 1.55), 1.2, 1.5, GUT, z=4.5, light=True)
        for sx, top in ((-0.45, 3.1), (0.55, 2.95)):
            poly([(xc + sx - 0.18, g + 2.3), (xc + sx - 0.12, g + top), (xc + sx + 0.12, g + top),
                  (xc + sx + 0.18, g + 2.3)], z=4.1, lw=0.7, **TUNIC)


for k, xc in enumerate((2.2, 5.8, 9.4, 13.2)):
    mini(xc, k + 1)
for a, b in ((3.0, 4.8), (6.7, 8.2), (10.6, 12.1)):
    bio.arrow(ax, (a, 2.2), (b, 2.2), kind="process", lw=1.1, head=0.2)
bio.label(ax, (2.2, 0.15), "Attachment", size="small")
bio.label(ax, (5.8, 0.15), "Tail resorbing", size="small")
bio.label(ax, (9.4, 0.15), "Body rotates", size="small")
bio.label(ax, (13.2, 0.15), "Juvenile", size="small")
C(ax, (2.2, ground + 3.0), (3.6, 4.7), "Tail with notochord")
C(ax, (13.2 - 0.45, ground + 3.05), (11.2, 4.7), "Oral siphon")
C(ax, (13.2 + 0.55, ground + 2.9), (15.3, 4.7), "Atrial siphon")

# ---------------- (C) adult, sagittal section ----------------
bio.panel(ax, "C", (17.3, 11.5))
ox, oy = 23.0, 0.8
ax.plot([18.5, 30.5], [oy, oy], color=P.muted(), lw=1.2, zorder=2)
for x in np.arange(18.7, 30.5, 0.4):
    ax.plot([x, x - 0.25], [oy, oy - 0.25], color=P.muted(), lw=0.6, zorder=2)
tunic = bio.smooth_closed([(ox - 2.6, oy + 0.05), (ox + 2.8, oy + 0.05), (ox + 3.4, oy + 3.5), (ox + 3.1, oy + 7.2),
                           (ox + 2.2, oy + 9.0), (ox + 0.6, oy + 8.6), (ox - 0.8, oy + 9.6), (ox - 2.4, oy + 8.6),
                           (ox - 3.2, oy + 5.5), (ox - 3.1, oy + 2.0)])
poly(tunic, z=3, lw=1.0, **TUNIC)
# siphons (tunic tubes)
poly([(ox - 1.7, oy + 8.6), (ox - 1.5, oy + 10.4), (ox - 0.3, oy + 10.4), (ox - 0.1, oy + 8.9)], z=3, lw=1.0, **TUNIC)
poly([(ox + 1.3, oy + 8.3), (ox + 1.4, oy + 9.7), (ox + 2.5, oy + 9.7), (ox + 2.7, oy + 8.2)], z=3, lw=1.0, **TUNIC)
# mantle / atrium (ectoderm-lined cavity)
mant = bio.smooth_closed([(ox - 2.2, oy + 1.0), (ox + 2.3, oy + 1.0), (ox + 2.8, oy + 4.0), (ox + 2.4, oy + 7.6),
                          (ox + 1.6, oy + 8.4), (ox + 0.4, oy + 7.9), (ox - 0.6, oy + 8.6), (ox - 1.9, oy + 8.0),
                          (ox - 2.6, oy + 5.0)])
poly(mant, face=P.mix(P.light("ectoderm"), P.surface(), 0.45), edge=P.edge("ectoderm"), z=3.5, lw=0.8)
ax.plot([ox - 1.4, ox - 1.3, ox - 0.5, ox - 0.4], [oy + 8.3, oy + 10.3, oy + 10.3, oy + 8.5],
        color=P.edge("ectoderm"), lw=0.8, zorder=3.6)
ax.plot([ox + 1.5, ox + 1.6, ox + 2.3, ox + 2.4], [oy + 8.1, oy + 9.6, oy + 9.6, oy + 8.0],
        color=P.edge("ectoderm"), lw=0.8, zorder=3.6)
# branchial basket with rows of stigmata
bb = bio.smooth_closed([(ox - 2.0, oy + 2.8), (ox + 0.5, oy + 2.6), (ox + 1.0, oy + 4.5), (ox + 0.6, oy + 7.2),
                        (ox - 0.4, oy + 8.1), (ox - 1.6, oy + 7.6), (ox - 2.3, oy + 5.2)])
poly(bb, face=P.light(GUT), edge=P.edge(GUT), z=4, lw=0.9)
for yy in np.arange(oy + 3.2, oy + 7.6, 0.42):
    for xx in np.arange(ox - 1.8, ox + 0.6, 0.32):
        if np.hypot((xx - (ox - 0.6)) / 1.55, (yy - (oy + 5.3)) / 2.45) < 0.95:
            ax.add_patch(Ellipse((xx, yy), 0.2, 0.08, facecolor=P.surface(), edgecolor=P.edge(GUT), lw=0.5, zorder=4.2))
# endostyle (ventral = left side here) and dorsal lamina (right, facing the atrial siphon)
ax.plot(*bio.smooth_closed([(ox - 2.15, oy + 3.3), (ox - 2.3, oy + 5.2), (ox - 1.65, oy + 7.4)], n=40)[:30].T,
        color=P.edge(GUT), lw=3.0, zorder=4.4)
ax.plot([ox + 0.8, ox + 0.95, ox + 0.65], [oy + 6.9, oy + 4.8, oy + 3.0], color=P.edge(GUT), lw=1.6, zorder=4.4,
        dashes=(2.5, 1.2))
# oral tentacles at the base of the oral siphon
for dx in (-1.25, -0.95, -0.65):
    ax.plot([ox + dx, ox + dx + 0.12], [oy + 8.3, oy + 7.95], color=P.edge(GUT), lw=1.0, zorder=4.5)
# U-shaped gut: oesophagus -> stomach -> intestine -> anus near the atrial siphon
gpath = [(ox - 0.2, oy + 2.7), (ox - 0.1, oy + 1.9), (ox + 0.8, oy + 1.5), (ox + 1.8, oy + 2.0), (ox + 2.1, oy + 3.6),
         (ox + 1.9, oy + 5.8), (ox + 1.7, oy + 7.0)]
gp = np.asarray(gpath, float)
for _ in range(4):  # Chaikin smoothing of the open gut path
    q = 0.75 * gp[:-1] + 0.25 * gp[1:]
    r = 0.25 * gp[:-1] + 0.75 * gp[1:]
    gp = np.vstack([gp[:1], np.c_[q, r].reshape(-1, 2), gp[-1:]])
ax.plot(gp[:, 0], gp[:, 1], color=P.edge(GUT), lw=7.0, zorder=4.6, solid_capstyle="round")
ax.plot(gp[:, 0], gp[:, 1], color=P.fill(GUT), lw=5.4, zorder=4.7, solid_capstyle="round")
ell((ox + 0.8, oy + 1.65), 1.4, 0.8, GUT, z=4.8)                    # stomach
# heart in pericardium, gonads in the gut loop, neural complex between the siphons
ell((ox - 1.0, oy + 1.65), 1.0, 0.5, "blood", z=4.8, light=True)
ax.plot([ox - 1.4, ox - 0.6], [oy + 1.65, oy + 1.65], color=P.edge("blood"), lw=2.0, zorder=4.9)
ell((ox + 1.25, oy + 3.0), 0.7, 1.3, GONAD, z=4.7)
ell((ox + 0.35, oy + 8.35), 0.55, 0.3, NERVE, z=5)
ell((ox + 0.35, oy + 8.05), 0.35, 0.2, NERVE, z=5, light=True)
# water current
wc = P.edge("channel")
bio.arrow(ax, (ox - 0.9, oy + 10.9), (ox - 0.9, oy + 9.3), kind="process", color=wc, lw=1.3, head=0.2, zorder=7)
bio.arrow(ax, (ox + 0.1, oy + 5.2), (ox + 1.6, oy + 5.4), kind="process", color=wc, lw=1.1, head=0.18, zorder=7)
bio.arrow(ax, (ox + 1.95, oy + 9.0), (ox + 2.1, oy + 10.9), kind="process", color=wc, lw=1.3, head=0.2, zorder=7)
C(ax, (ox - 0.9, oy + 10.0), (19.6, 11.2), "Oral siphon")
C(ax, (ox + 2.0, oy + 9.5), (28.4, 11.2), "Atrial siphon")
C(ax, (ox + 0.35, oy + 8.4), (27.7, 10.2), "Cerebral ganglion")
C(ax, (ox + 0.35, oy + 8.0), (28.6, 9.4), "Neural gland")
C(ax, (ox - 1.0, oy + 8.1), (19.0, 10.0), "Oral tentacles")
C(ax, (ox - 2.27, oy + 5.0), (18.6, 6.0), "Endostyle")
C(ax, (ox - 0.95, oy + 5.3), (18.6, 7.6), "Branchial basket (stigmata)")
C(ax, (ox + 0.9, oy + 5.5), (29.0, 7.8), "Dorsal lamina")
C(ax, (ox + 2.5, oy + 6.0), (29.2, 6.8), "Atrium")
C(ax, (ox + 1.95, oy + 4.6), (29.2, 5.6), "Intestine")
C(ax, (ox + 1.25, oy + 3.0), (29.2, 4.2), "Gonads")
C(ax, (ox + 1.7, oy + 7.0), (29.2, 8.8), "Anus")
C(ax, (ox + 0.8, oy + 1.65), (27.8, 0.3), "Stomach")
C(ax, (ox - 1.0, oy + 1.65), (19.2, 0.3), "Heart in pericardium")
C(ax, (ox - 3.1, oy + 3.0), (18.6, 3.2), "Tunic")
C(ax, (ox - 2.4, oy + 2.2), (18.6, 4.4), "Mantle")
