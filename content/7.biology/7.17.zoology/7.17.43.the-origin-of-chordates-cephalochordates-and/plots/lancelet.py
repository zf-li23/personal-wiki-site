# Lancelet (Branchiostoma), schematic: (A) lateral view with the main organ systems, anterior to the left;
# (B) cross-section through the pharynx, dorsal up. Drawn natively (germ-layer colours as in 7.17.41).
import numpy as np
import wikibio as bio
from matplotlib.patches import Polygon, Ellipse

P = bio.P
fig, ax = bio.canvas(30.0, 12.5)


def poly(pts, face, edge, z=5, lw=0.9):
    ax.add_patch(Polygon(np.asarray(pts), closed=True, facecolor=face, edgecolor=edge, lw=lw, zorder=z,
                         joinstyle="round"))


def ell(c, w, h, tok, z=6, lw=0.8, light=False, angle=0.0):
    ax.add_patch(Ellipse(c, w, h, angle=angle, facecolor=P.light(tok) if light else P.fill(tok),
                         edgecolor=P.edge(tok), lw=lw, zorder=z))


NOTO, NERVE, GUT, BLOOD, GONAD, MUSC = "drug", "neuron", "endoderm", "blood", "nucleolus", "muscle"

# ================= (A) lateral view =================
Y = 6.4
SY = 1.5  # vertical exaggeration of panel A (organs legible)


def T(p):
    return (p[0], Y + SY * (p[1] - Y))


n_before = len(ax.patches) + len(ax.lines)
X0, X1 = 1.0, 21.6
xs = np.linspace(X0, X1, 220)
t = (xs - X0) / (X1 - X0)
up = 1.25 * np.sin(np.pi * t ** 0.8) ** 0.9          # dorsal profile
lo = 1.35 * np.sin(np.pi * t ** 0.75) ** 0.85        # ventral profile (deeper pharyngeal region)
body = np.vstack([np.c_[xs, Y + up], np.c_[xs[::-1], Y - lo[::-1]]])
# median fins: low dorsal fin, caudal fin around the tail, preanal fin from atriopore to anus
taper = np.clip((X1 + 0.5 - xs) / 2.2, 0, 1) ** 0.7
caud = np.sin(np.pi * np.clip((xs - 17.6) / (X1 + 0.5 - 17.6), 0, 1))
fin_up = np.where(xs > 2.5, 0.16 * taper + 0.42 * caud, 0.0)
fin_lo = np.where(xs > 13.5, 0.14 * taper + 0.36 * caud, 0.0)
fin = np.vstack([np.c_[xs, Y + up + fin_up], np.c_[xs[::-1], Y - lo[::-1] - fin_lo[::-1]]])
poly(fin, face=P.mix(P.light("ectoderm"), P.surface(), 0.4), edge=P.edge("ectoderm"), z=2, lw=0.7)
poly(body, face=P.light("ectoderm"), edge=P.edge("ectoderm"), z=3, lw=1.0)
# fin-ray boxes in the dorsal fin
for x in np.arange(3.0, 17.5, 0.35):
    k = np.searchsorted(xs, x)
    ax.plot([x, x], [Y + up[k] + 0.03, Y + up[k] + fin_up[k] - 0.03], color=P.edge("ectoderm"), lw=0.4, zorder=2.5)

# myomeres: chevrons pointing forward (faint, in the body wall)
for x in np.arange(2.6, 20.8, 0.33):
    k = np.searchsorted(xs, x)
    a, b = up[k] * 0.92, lo[k] * 0.92
    ax.plot([x + 0.35, x, x + 0.35], [Y + a, Y + 0.15, Y - b], color=P.mix(P.edge(MUSC), P.surface(), 0.55),
            lw=0.5, zorder=3.2)

# atrium (ectoderm-lined cavity around the pharynx, to the atriopore)
atr = bio.smooth_closed([(3.4, Y + 0.05), (4.5, Y + 0.42), (8.0, Y + 0.45), (11.5, Y + 0.35), (13.4, Y - 0.2),
                         (13.6, Y - 1.05), (11.0, Y - 1.15), (7.0, Y - 1.15), (4.2, Y - 0.85)])
poly(atr, face=P.mix(P.light("ectoderm"), P.surface(), 0.55), edge=P.edge("ectoderm"), z=3.5, lw=0.6)

# pharynx with oblique gill slits
ph = bio.smooth_closed([(3.2, Y + 0.05), (3.6, Y + 0.3), (6.0, Y + 0.34), (10.4, Y + 0.3), (10.8, Y + 0.05),
                        (10.4, Y - 0.6), (6.0, Y - 0.75), (3.6, Y - 0.5)])
poly(ph, face=P.light(GUT), edge=P.edge(GUT), z=4, lw=0.8)
for x in np.arange(3.9, 10.3, 0.22):
    ax.plot([x + 0.16, x - 0.12], [Y + 0.24, Y - 0.6], color=P.edge("blood"), lw=0.9, zorder=4.5)
# endostyle (ventral) and epibranchial groove (dorsal)
ax.plot(np.linspace(3.7, 10.3, 30), Y - 0.66 + 0.0 * np.linspace(0, 1, 30), color=P.edge(GUT), lw=2.2, zorder=4.6)
ax.plot(np.linspace(3.7, 10.5, 30), np.full(30, Y + 0.28), color=P.edge(GUT), lw=1.4, zorder=4.6)

# gut behind the pharynx: midgut, ileocolic ring, hindgut, anus (ventral, before the caudal fin)
gx = np.linspace(10.5, 18.3, 80)
gy = Y - 0.1 - 0.5 * np.clip((gx - 15.5) / 2.8, 0, 1) ** 1.5
gh = np.interp(gx, [10.5, 12.5, 14.5, 15.0, 15.5, 18.3], [0.38, 0.34, 0.3, 0.36, 0.25, 0.14])
poly(np.vstack([np.c_[gx, gy + gh], np.c_[gx[::-1], (gy - gh)[::-1]]]), face=P.fill(GUT), edge=P.edge(GUT), z=5)
anus = (18.35, Y - 0.68)
ax.plot([18.25, anus[0] + 0.05], [Y - 0.6, Y - lo[np.searchsorted(xs, 18.4)] + 0.02], color=P.edge(GUT), lw=1.6,
        zorder=5)
# hepatic caecum: blind sac from the midgut forward beside (to the right of) the pharynx
cae = bio.smooth_closed([(10.9, Y - 0.15), (9.8, Y - 0.05), (8.0, Y - 0.12), (7.3, Y - 0.32), (8.0, Y - 0.52),
                         (9.8, Y - 0.5), (10.9, Y - 0.45)])
poly(cae, face=P.fill(GUT), edge=P.edge(GUT), z=5.2)

# gonads: serial pouches in the atrial wall
for x in np.arange(4.6, 12.6, 0.62):
    ell((x, Y - 0.95), 0.48, 0.32, GONAD, z=4.8, lw=0.6)

# notochord (snout tip to tail tip, beneath the nerve cord) and nerve cord with cerebral vesicle and eye spot
nx = np.linspace(1.1, 21.4, 120)
nt = (nx - X0) / (X1 - X0)
ntop = Y + 0.82 * np.sin(np.pi * nt ** 0.8) ** 0.9
poly(np.vstack([np.c_[nx, ntop - 0.1], np.c_[nx[::-1], (ntop - 0.36 * np.minimum(1, 8 * nt * (1 - nt) + 0.3))[::-1]]]),
     face=P.fill(NOTO), edge=P.edge(NOTO), z=6, lw=0.7)
cx = np.linspace(2.0, 21.0, 110)
ct = (cx - X0) / (X1 - X0)
ctop = Y + 1.02 * np.sin(np.pi * ct ** 0.8) ** 0.9
poly(np.vstack([np.c_[cx, ctop], np.c_[cx[::-1], (ctop - 0.17)[::-1]]]), face=P.fill(NERVE), edge=P.edge(NERVE),
     z=6.2, lw=0.6)
k = np.searchsorted(cx, 2.15)
ell((2.25, ctop[k] - 0.08), 0.45, 0.3, NERVE, z=6.3)               # cerebral vesicle
ax.add_patch(Ellipse((2.03, ctop[k] - 0.1), 0.12, 0.12, facecolor=P.ink(), edgecolor=P.ink(), zorder=6.5))
for x in np.arange(3.2, 20.0, 0.9):                                 # dorsal ocelli (pigment cups)
    kk = np.searchsorted(cx, x)
    ax.add_patch(Ellipse((x, ctop[kk] - 0.09), 0.06, 0.06, facecolor=P.ink(), edgecolor=P.ink(), zorder=6.5))

# oral hood with cirri, wheel organ, velum
for j, ang in enumerate(np.linspace(-150, -60, 9)):
    a = np.radians(ang)
    ax.plot([2.5 + 0.35 * np.cos(a), 2.5 + 0.95 * np.cos(a)], [Y - 0.35 + 0.35 * np.sin(a), Y - 0.35 + 0.95 * np.sin(a)],
            color=P.edge("ectoderm"), lw=0.9, zorder=3.6, solid_capstyle="round")
ax.plot([3.15, 3.15], [Y - 0.45, Y + 0.25], color=P.edge(GUT), lw=1.6, zorder=4.7)  # velum with mouth
for yy in (Y + 0.05, Y - 0.25):
    ax.plot([3.15, 3.5], [yy, yy - 0.05], color=P.edge(GUT), lw=0.6, zorder=4.7)  # velar tentacles

# blood vessels: ventral aorta (forward), dorsal aorta (backward), subintestinal vein to the hepatic caecum
bl = P.edge(BLOOD)
ax.plot([4.0, 10.6], [Y - 0.82, Y - 0.82], color=bl, lw=1.4, zorder=4.9)
ax.plot([4.0, 11.0, 20.0], [Y + 0.38, Y + 0.38, Y + 0.12], color=bl, lw=1.4, zorder=4.9)
ax.plot([17.5, 12.0, 10.9], [Y - 0.55, Y - 0.5, Y - 0.32], color=bl, lw=1.1, zorder=5.3, dashes=(3, 1.2))
bio.arrow(ax, (9.0, Y - 0.82), (7.4, Y - 0.82), kind="process", color=bl, lw=1.0, head=0.16, zorder=7)
bio.arrow(ax, (14.0, Y + 0.33), (15.8, Y + 0.28), kind="process", color=bl, lw=1.0, head=0.16, zorder=7)
# water current: mouth -> slits -> atrium -> atriopore
wc = P.edge("channel")
bio.arrow(ax, (0.6, Y - 1.4), (2.2, Y - 0.7), kind="process", color=wc, lw=1.3, head=0.2, bend=0.2, zorder=7)
atp = (13.45, Y - lo[np.searchsorted(xs, 13.45)] + 0.03)
bio.arrow(ax, (atp[0], atp[1] + 0.25), (atp[0] + 0.5, atp[1] - 0.8), kind="process", color=wc, lw=1.3, head=0.2,
          zorder=7)

from matplotlib.transforms import Affine2D
TR = Affine2D().translate(0, -Y).scale(1, SY).translate(0, Y) + ax.transData
for art in (list(ax.patches) + list(ax.lines))[n_before:]:
    art.set_transform(TR)

bio.panel(ax, "A", (0.3, 11.9))


def C(ax, p, q, text):
    bio.callout(ax, T(p), q, text)


C(ax, (1.4, Y + 0.05), (0.9, 10.2), "Rostrum (notochord tip)")
C(ax, (2.03, ctop[k] - 0.1), (2.6, 11.0), "Frontal eye")
C(ax, (2.4, ctop[k]), (4.6, 10.2), "Cerebral vesicle")
C(ax, (8.0, ctop[np.searchsorted(cx, 8.0)] - 0.08), (9.6, 10.2), "Dorsal nerve cord")
C(ax, (11.5, Y + 0.38), (12.0, 11.0), "Dorsal aorta")
C(ax, (13.0, ntop[np.searchsorted(nx, 13.0)] - 0.22), (13.8, 10.2), "Notochord")
C(ax, (15.0, Y + 0.95), (15.8, 11.0), "Myomeres")
C(ax, (17.0, Y + up[np.searchsorted(xs, 17.0)] + 0.15), (18.6, 10.2), "Dorsal fin")
C(ax, (20.8, Y + 0.3), (21.2, 11.0), "Caudal fin")
C(ax, (6.5, Y + 0.28), (7.4, 11.0), "Epibranchial groove")
C(ax, (2.0, Y - 1.2), (0.9, 2.0), "Oral cirri")
C(ax, (3.15, Y - 0.1), (2.6, 1.0), "Velum (mouth)")
C(ax, (5.0, Y + 0.1), (4.4, 2.0), "Gill slits")
C(ax, (5.6, Y - 0.66), (6.0, 1.0), "Endostyle")
C(ax, (7.5, Y - 0.82), (7.6, 2.0), "Ventral aorta")
C(ax, (8.5, Y - 0.32), (9.2, 1.0), "Hepatic caecum")
C(ax, (10.2, Y - 0.95), (10.6, 2.0), "Gonads")
C(ax, (12.2, Y + 0.3), (12.4, 1.0), "Atrium")
C(ax, atp, (13.8, 2.0), "Atriopore")
C(ax, (14.8, Y - 0.12), (15.4, 1.0), "Midgut")
C(ax, (16.8, Y - 0.2), (17.2, 2.0), "Hindgut")
C(ax, anus, (18.6, 1.0), "Anus")
C(ax, (16.2, Y - lo[np.searchsorted(xs, 16.2)] - 0.15), (20.0, 2.0), "Preanal fin")

# ================= (B) cross-section through the pharynx =================
cx0, cy0 = 26.3, 6.0
out = bio.smooth_closed([(cx0, cy0 + 4.1), (cx0 + 1.2, cy0 + 2.6), (cx0 + 1.9, cy0 + 0.6), (cx0 + 2.1, cy0 - 1.8),
                         (cx0 + 2.6, cy0 - 3.2), (cx0 + 1.6, cy0 - 3.4), (cx0 + 0.6, cy0 - 3.0), (cx0, cy0 - 3.1),
                         (cx0 - 0.6, cy0 - 3.0), (cx0 - 1.6, cy0 - 3.4), (cx0 - 2.6, cy0 - 3.2), (cx0 - 2.1, cy0 - 1.8),
                         (cx0 - 1.9, cy0 + 0.6), (cx0 - 1.2, cy0 + 2.6)])
poly(out, face=P.light("ectoderm"), edge=P.edge("ectoderm"), z=3, lw=1.0)
# myomeres (upper body wall, both sides)
for s in (1, -1):
    poly(bio.smooth_closed([(cx0 + s * 0.35, cy0 + 3.2), (cx0 + s * 1.15, cy0 + 2.2), (cx0 + s * 1.6, cy0 + 0.4),
                            (cx0 + s * 1.75, cy0 - 1.2), (cx0 + s * 1.45, cy0 - 1.0), (cx0 + s * 1.3, cy0 + 0.4),
                            (cx0 + s * 0.6, cy0 + 1.2), (cx0 + s * 0.45, cy0 + 2.6)]),
         face=P.light(MUSC), edge=P.edge(MUSC), z=4, lw=0.6)
# atrium around the pharynx (floored by the metapleural folds)
poly(bio.smooth_closed([(cx0, cy0 + 1.05), (cx0 + 1.2, cy0 + 0.5), (cx0 + 1.4, cy0 - 1.2), (cx0 + 1.1, cy0 - 2.55),
                        (cx0, cy0 - 2.7), (cx0 - 1.1, cy0 - 2.55), (cx0 - 1.4, cy0 - 1.2), (cx0 - 1.2, cy0 + 0.5)]),
     face=P.mix(P.light("ectoderm"), P.surface(), 0.55), edge=P.edge("ectoderm"), z=4.2, lw=0.6)
# gonads in the lateral atrial wall
for s in (1, -1):
    ell((cx0 + s * 1.5, cy0 - 1.7), 0.55, 0.95, GONAD, z=4.4)
# pharynx: ring of gill bars and slits
th = np.linspace(0, 2 * np.pi, 33)[:-1]
for a in th:
    if abs(np.sin(a) - 1) < 0.05 or abs(np.sin(a) + 1) < 0.05:
        continue
    p = (cx0 + 0.85 * np.cos(a), cy0 - 0.85 + 1.25 * np.sin(a))
    ell(p, 0.13, 0.22, GUT, z=5, lw=0.5, angle=np.degrees(a) + 90)
ell((cx0, cy0 - 0.85), 1.45, 2.25, GUT, z=4.8, lw=0.0, light=True)
# epibranchial groove (top) and endostyle (bottom)
ell((cx0, cy0 + 0.35), 0.45, 0.22, GUT, z=5.5)
ell((cx0, cy0 - 2.05), 0.6, 0.3, GUT, z=5.5)
# coelomic canals beside the epibranchial groove and beneath the endostyle
for s in (1, -1):
    ell((cx0 + s * 0.42, cy0 + 0.62), 0.28, 0.2, "coelom", z=5.4, light=True)
ell((cx0, cy0 - 2.37), 0.5, 0.16, "coelom", z=5.4, light=True)
# vessels
for s in (1, -1):
    ell((cx0 + s * 0.22, cy0 + 0.85), 0.2, 0.2, BLOOD, z=5.6)       # paired dorsal aortae
ell((cx0, cy0 - 2.55), 0.22, 0.14, BLOOD, z=5.6)                   # ventral aorta
# notochord and nerve cord
ell((cx0, cy0 + 1.55), 0.85, 0.85, NOTO, z=6)
ell((cx0, cy0 + 2.55), 0.5, 0.5, NERVE, z=6)
ell((cx0, cy0 + 2.55), 0.08, 0.08, "extracellular", z=6.2, lw=0.4)  # central canal
bio.panel(ax, "B", (23.3, 11.9))
C = bio.callout
C(ax, (cx0, cy0 + 2.75), (24.0, 9.9), "Nerve cord")
C(ax, (cx0 + 0.25, cy0 + 1.7), (28.9, 9.9), "Notochord")
C(ax, (cx0 - 1.0, cy0 + 1.6), (23.6, 8.6), "Myomere")
C(ax, (cx0 + 0.22, cy0 + 0.85), (29.3, 8.6), "Dorsal aortae")
C(ax, (cx0 + 0.42, cy0 + 0.62), (29.3, 7.6), "Coelom")
C(ax, (cx0 - 0.2, cy0 + 0.35), (29.4, 6.9), "Epibranchial groove")
C(ax, (cx0 - 0.85, cy0 - 0.85), (23.2, 6.2), "Gill bars")
C(ax, (cx0 + 0.3, cy0 - 0.9), (29.4, 5.8), "Pharynx")
C(ax, (cx0 - 1.25, cy0 - 0.3), (23.2, 5.0), "Atrium")
C(ax, (cx0 + 1.5, cy0 - 1.7), (29.6, 4.0), "Gonad")
C(ax, (cx0 - 0.2, cy0 - 2.05), (23.4, 2.2), "Endostyle")
C(ax, (cx0 + 0.1, cy0 - 2.55), (28.4, 1.2), "Ventral aorta")
C(ax, (cx0 - 2.2, cy0 - 3.1), (23.6, 1.0), "Metapleural fold")
