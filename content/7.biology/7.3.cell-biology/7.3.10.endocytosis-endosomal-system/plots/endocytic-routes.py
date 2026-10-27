"""Routes into an animal cell and the endosomal system (schematic, not to scale).
Top: five routes of internalization at the plasma membrane - phagocytosis of a bacterium by a cup of
pseudopods, macropinocytosis by a collapsing ruffle, clathrin-mediated endocytosis from a coated pit,
caveolae, and clathrin-independent tubular carriers (CLIC/GEEC). Below: the early endosome (vacuolar body
with tubules) sorts cargo back to the surface (directly or through the recycling endosome) or keeps it as
it matures into a late endosome / multivesicular body, which fuses with lysosomes. The trans-Golgi network
supplies acid hydrolases and V-ATPases to maturing endosomes and receives retrieved receptors. Typical
lumenal pH values are given for each compartment."""

import numpy as np

import wikibio as bio

P = bio.P
FT = bio.core.FONT
W, H = 22.0, 13.0
fig, ax = bio.canvas(W, H, scale=0.42)
Y0 = 10.0  # plasma membrane
TH = 0.13  # membrane thickness


def bez(p0, p1, p2, p3, n=40):
    t = np.linspace(0, 1, n)[:, None]
    p0, p1, p2, p3 = map(np.asarray, (p0, p1, p2, p3))
    return (1 - t) ** 3 * p0 + 3 * (1 - t) ** 2 * t * p1 + 3 * (1 - t) * t ** 2 * p2 + t ** 3 * p3


def arc(c, r, a0, a1, n=50):
    a = np.radians(np.linspace(a0, a1, n))
    return np.c_[c[0] + r * np.cos(a), c[1] + r * np.sin(a)]


def band(pts, token="membrane", zorder=6, closed=False):
    q, nrm, _ = bio.core.polyline(pts, n=1600 if not closed else 300, closed=closed)
    o, i = q + nrm * TH / 2, q - nrm * TH / 2
    poly = np.vstack([o, i[::-1]])
    bio.shape(ax, poly, token, lw=0, zorder=zorder)
    for ln in (o, i):
        ax.plot(ln[:, 0], ln[:, 1], color=P.edge(token), lw=0.8, zorder=zorder + 1, solid_joinstyle="round")
    return q, nrm


def compartment(c, r, token, cargo=None, zorder=8):
    bio.vesicle(ax, c, r, token=token, cargo=cargo, zorder=zorder)


def coat(pts, token="positive", every=1, r=0.055, zorder=9):
    for p in pts[::every]:
        ax.add_patch(bio.core.Circle(p, r, color=P.edge(token), lw=0, zorder=zorder))


# ---- plasma membrane with its invaginations ------------------------------------------------------------
bact = (2.55, 11.25)
pm = [np.array([[0.0, Y0], [0.9, Y0]])]
pm.append(bez((0.9, Y0), (1.25, Y0), (1.05, 11.6), (1.35, 12.15)))          # left pseudopod, outer side
pm.append(arc((1.5, 12.15), 0.15, 180, 0, 12))                               # its tip
pm.append(bez((1.65, 12.15), (1.75, 11.6), (1.55, 11.0), (1.75, 10.65)))      # inner side down to the cup
pm.append(arc(bact, 1.05, 220, 320, 40))                                      # cup around the bacterium
pm.append(bez((3.35, 10.57), (3.55, 11.0), (3.35, 11.6), (3.45, 12.15)))     # right pseudopod, inner side
pm.append(arc((3.6, 12.15), 0.15, 180, 0, 12))
pm.append(bez((3.75, 12.15), (3.95, 11.6), (3.85, Y0), (4.3, Y0)))
# macropinocytic ruffle: a sheet that rises and folds back over the surface
pm.append(np.array([[4.3, Y0], [5.4, Y0]]))
pm.append(bez((5.4, Y0), (5.8, Y0), (5.6, 11.8), (6.4, 12.2)))
pm.append(bez((6.4, 12.2), (7.2, 12.5), (7.7, 11.9), (7.5, 11.4)))
pm.append(arc((7.38, 11.4), 0.12, 0, -180, 10))
pm.append(bez((7.26, 11.4), (7.3, 11.9), (6.4, 12.0), (6.15, 11.4)))
pm.append(bez((6.15, 11.4), (5.95, 10.9), (6.1, Y0), (6.4, Y0)))
# clathrin-coated pit
pm.append(np.array([[6.4, Y0], [9.0, Y0]]))
pit_c = (9.7, 9.55)
pm.append(bez((9.0, Y0), (9.25, Y0), (9.2, 9.85), (9.25, 9.65)))
pit = arc(pit_c, 0.47, 165, 375, 50)
pm.append(pit)
pm.append(bez((10.15, 9.65), (10.2, 9.85), (10.15, Y0), (10.4, Y0)))
# caveola: flask with a narrow neck
pm.append(np.array([[10.4, Y0], [12.3, Y0]]))
cav_c = (12.6, 9.35)
pm.append(bez((12.3, Y0), (12.45, Y0), (12.48, 9.9), (12.42, 9.66)))
cav = arc(cav_c, 0.34, 122, 418, 50)
pm.append(cav)
pm.append(bez((12.78, 9.66), (12.72, 9.9), (12.75, Y0), (12.9, Y0)))
# CLIC/GEEC tubular invagination
pm.append(np.array([[12.9, Y0], [15.25, Y0]]))
pm.append(bez((15.25, Y0), (15.42, Y0), (15.42, 9.6), (15.4, 8.95)))
pm.append(arc((15.55, 8.95), 0.15, 180, 360, 14))
pm.append(bez((15.7, 8.95), (15.68, 9.6), (15.68, Y0), (15.85, Y0)))
pm.append(np.array([[15.85, Y0], [W, Y0]]))
pts = np.vstack(pm)
# extracellular region above the membrane, cytosol below
bio.shape(ax, np.vstack([pts, [[W, H], [0, H]]]), "extracellular", lw=0, zorder=1)
bio.shape(ax, np.vstack([pts, [[W, 0], [0, 0]]]), "cytoplasm", lw=0, zorder=1)
q, nrm = band(pts)
# the bacterium sits in the cup
cap = np.vstack([arc((0.26, 0), 0.36, -90, 90, 20), arc((-0.26, 0), 0.36, 90, 270, 20)])
bio.shape(ax, cap + (bact[0], 10.72), "bacterium", lw=1.1, zorder=9)
# clathrin and caveolin coats on the cytosolic face
coat(arc(pit_c, 0.62, 175, 365, 18), "positive")
coat(arc(cav_c, 0.48, 130, 410, 16), "lipid", r=0.05)

# ---- carriers just below the membrane ------------------------------------------------------------------
phago = (2.6, 8.0)
compartment(phago, 0.95, "vesicle")
bio.shape(ax, cap * 0.85 + phago, "bacterium", lw=1.0, zorder=10)
bio.arrow(ax, (2.6, 9.95), (2.6, 9.1), kind="process", head=0.18)
mp = (6.6, 8.3)
compartment(mp, 0.62, "vesicle", cargo="extracellular")
bio.arrow(ax, (6.4, 9.85), (6.55, 9.0), kind="process", head=0.18)
ccv = (9.75, 7.95)
compartment(ccv, 0.36, "vesicle", cargo="highlight")
coat(arc(ccv, 0.47, 0, 360, 16), "positive")
bio.arrow(ax, (9.72, 8.95), (9.74, 8.5), kind="process", head=0.16)
bio.label(ax, (8.95, 7.95), "dynamin", size="tiny", ha="right", color=P.muted())
cv = (12.6, 8.15)
compartment(cv, 0.3, "vesicle")
coat(arc(cv, 0.41, 0, 360, 14), "lipid", r=0.045)
bio.arrow(ax, (12.6, 8.92), (12.6, 8.55), kind="process", head=0.15)

# ---- endosomes ------------------------------------------------------------------------------------------
ee = np.array([11.2, 5.4])
for ang, ln in ((25, 1.5), (-15, 1.3), (160, 1.1)):
    a = np.radians(ang)
    tip = ee + (0.7 + ln) * np.array([np.cos(a), np.sin(a)])
    band(np.array([ee + 0.6 * np.array([np.cos(a), np.sin(a)]), tip]), "vesicle", zorder=7)
compartment(ee, 0.85, "vesicle", cargo="highlight")
bio.label(ax, ee + (1.3, -1.0), "Early endosome", size="small", bold=True, ha="left")
bio.label(ax, ee + (1.3, -1.4), "Rab5, PI(3)P · pH 6.0–6.5", size="tiny", color=P.muted(), ha="left")

rec = np.array([17.2, 6.5])
for k, dy in enumerate((-0.35, 0.0, 0.35)):
    band(np.array([rec + (-0.9, dy), rec + (0.9, dy + 0.12 * (k - 1))]), "vesicle", zorder=7)
bio.label(ax, rec + (0, -0.85), "Recycling endosome", size="small", bold=True)
bio.label(ax, rec + (0, -1.25), "Rab11 · pH ≈ 6.5", size="tiny", color=P.muted())

mvb = np.array([7.2, 3.2])
compartment(mvb, 0.95, "vesicle")
rng = np.random.default_rng(3)
for k in range(9):
    a, d = rng.uniform(0, 2 * np.pi), 0.6 * np.sqrt(rng.uniform(0.05, 1))
    compartment(mvb + d * np.array([np.cos(a), np.sin(a)]), 0.15, "vesicle", zorder=9)
bio.label(ax, mvb + (0, -1.35), "Late endosome / MVB", size="small", bold=True)
bio.label(ax, mvb + (0, -1.75), "Rab7, PI(3,5)P₂ · pH 5.0–6.0", size="tiny", color=P.muted())

lyso = np.array([12.3, 1.9])
bio.lysosome(ax, lyso, 0.8)
bio.label(ax, lyso + (1.05, 0.2), "Lysosome", size="small", bold=True, ha="left")
bio.label(ax, lyso + (1.05, -0.2), "pH 4.5–5.0", size="tiny", color=P.muted(), ha="left")

bio.golgi(ax, (2.4, 3.6), 2.8, cisternae=4, curve=0.3)
bio.label(ax, (2.4, 2.2), "trans-Golgi network", size="small", bold=True)

# ---- traffic ----------------------------------------------------------------------------------------------
A = dict(kind="process", head=0.2)
bio.arrow(ax, (10.0, 7.6), (10.75, 6.25), **A)                             # CCV -> EE
bio.arrow(ax, (12.45, 7.85), (11.75, 6.2), dashed=True, **A)               # caveolar carrier -> EE
bio.arrow(ax, (15.5, 8.75), (12.3, 5.95), bend=-0.12, **A)                 # CLIC -> EE
bio.label(ax, (14.75, 7.25), "GEEC", size="tiny", color=P.muted())
bio.arrow(ax, (12.85, 6.35), (13.7, 9.85), bend=-0.15, **A)                # fast recycling
bio.label(ax, (13.75, 8.7), "fast\nrecycling", size="tiny", color=P.muted(), ha="left")
bio.arrow(ax, (12.95, 5.1), (16.2, 6.2), bend=0.1, **A)                    # EE -> REC
bio.arrow(ax, (17.6, 7.0), (18.3, 9.85), bend=-0.1, **A)                   # REC -> PM
bio.label(ax, (18.35, 8.3), "slow recycling,\ntranscytosis", size="tiny", color=P.muted(), ha="left")
bio.arrow(ax, (10.45, 4.75), (8.3, 3.75), bend=0.1, **A)                   # maturation
bio.label(ax, (8.4, 3.15), "maturation\n(microtubules)", size="tiny", color=P.muted(), ha="left")
bio.arrow(ax, (8.1, 2.65), (11.45, 1.95), bend=0.1, **A)                   # LE -> lysosome
bio.arrow(ax, (6.65, 7.75), (7.15, 4.25), **A)                             # macropinosome -> LE
bio.arrow(ax, (3.3, 7.4), (11.5, 2.5), bend=0.07, **A)                  # phagosome -> lysosome
bio.label(ax, (5.6, 7.45), "phagosome–lysosome\nfusion", size="tiny", color=P.muted())
bio.arrow(ax, (3.6, 4.0), (6.2, 3.5), color=P.edge("lysosome"), **A)        # TGN -> LE (hydrolases)
bio.arrow(ax, (3.7, 4.55), (10.3, 5.3), color=P.edge("lysosome"), bend=-0.08, **A)
bio.arrow(ax, (6.25, 2.65), (3.6, 3.1), color=P.muted(), dashed=True, **A)   # receptor retrieval
bio.label(ax, (2.4, 1.15), "hydrolases out,\nM6P receptors back", size="tiny", color=P.edge("lysosome"))

# ---- route names ------------------------------------------------------------------------------------------
for x, s in ((2.55, "Phagocytosis"), (6.6, "Macropinocytosis"), (9.7, "Clathrin-mediated"), (12.6, "Caveolae"),
             (15.55, "CLIC/GEEC")):
    bio.label(ax, (x, 12.65), s, size="small", bold=True)
bio.label(ax, (20.9, 12.0), "Extracellular\nspace", size="small", color=P.muted(), ha="right")
bio.label(ax, (20.9, 3.0), "Cytosol", size="small", color=P.muted(), ha="right", bold=True)
