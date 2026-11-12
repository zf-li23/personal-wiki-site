# Polyp and medusa in longitudinal section, germ layers coloured (epidermis = ectoderm, gastrodermis =
# endoderm, mesoglea). Drawn natively: each layer is a band between two offsets of a smooth centre line.
import numpy as np
import wikibio as bio
from wikibio import zoology as zoo
from matplotlib.patches import Polygon

P = bio.P
fig, ax = bio.canvas(25.5, 11.6)
ECT, END, MES = "ectoderm", "endoderm", "mesoglea"
CAV = P.mix(P.fill("neutral"), P.surface(), 0.55)


def spline(pts, n=300):
    pts = np.asarray(pts, float)
    d = np.r_[0, np.cumsum(np.hypot(*np.diff(pts, axis=0).T))]
    t = np.linspace(0, d[-1], n)
    # Catmull-Rom style smoothing by repeated averaging of a dense linear interpolation
    xy = np.c_[np.interp(t, d, pts[:, 0]), np.interp(t, d, pts[:, 1])]
    for _ in range(220):
        xy[1:-1] = 0.25 * xy[:-2] + 0.5 * xy[1:-1] + 0.25 * xy[2:]
    return xy


def normals(xy):
    g = np.gradient(xy, axis=0)
    g /= np.linalg.norm(g, axis=1)[:, None]
    return np.c_[-g[:, 1], g[:, 0]]


def band(ax, xy, a, b, token=None, face=None, z=5, lw=0.7):
    nrm = normals(xy)
    p, q = xy + nrm * a, xy + nrm * b
    poly = np.vstack([p, q[::-1]])
    fc = face if face is not None else P.fill(token)
    ec = "none" if face is not None else P.edge(token)
    ax.add_patch(Polygon(poly, closed=True, facecolor=fc, edgecolor=ec, lw=lw, zorder=z))


def tube(ax, xy, r_out, z=4):
    """A hollow tube (tentacle, manubrium, canal): epidermis, mesoglea, gastrodermis, lumen."""
    band(ax, xy, -r_out, r_out, ECT, z=z)
    band(ax, xy, -0.55 * r_out, 0.55 * r_out, MES, z=z + 0.1, lw=0.4)
    band(ax, xy, -0.45 * r_out, 0.45 * r_out, END, z=z + 0.2)
    band(ax, xy, -0.15 * r_out, 0.15 * r_out, face=CAV, z=z + 0.3)


# ---------------------------------------------------------------- A: polyp
bio.panel(ax, "A", (0.2, 11.4))
cx = 5.5
wall = spline([(cx + 0.35, 9.0), (cx + 0.9, 8.5), (cx + 1.5, 7.8), (cx + 1.5, 4.0), (cx + 1.5, 1.6), (cx + 0.9, 1.0),
               (cx - 0.9, 1.0), (cx - 1.5, 1.6), (cx - 1.5, 4.0), (cx - 1.5, 7.8), (cx - 0.9, 8.5), (cx - 0.35, 9.0)])
# outward normal: the centre line runs clockwise (right side down), so the left normal points inward
for sgn, x0 in ((1, cx + 1.25), (-1, cx - 1.25)):
    t = spline([(x0, 8.1), (x0 + sgn * 0.9, 9.0), (x0 + sgn * 1.9, 9.9), (x0 + sgn * 3.0, 10.4)])
    tube(ax, t, 0.24, z=3)
inner = wall - normals(wall) * 0.33
ax.add_patch(Polygon(inner, closed=True, facecolor=CAV, edgecolor="none", zorder=4))
band(ax, wall, 0.04, 0.36, ECT)
band(ax, wall, -0.04, 0.04, MES, lw=0.4)
band(ax, wall, -0.36, -0.04, END)
bio.callout(ax, (cx, 9.05), (cx + 3.3, 11.0), "Mouth (hypostome)", size="small")
bio.callout(ax, (cx + 3.0, 10.35), (cx + 4.0, 9.6), "Tentacle", size="small")
bio.callout(ax, (cx - 1.8, 5.5), (0.6, 6.6), "Epidermis", size="small")
bio.callout(ax, (cx - 1.5, 4.6), (0.6, 5.2), "Mesoglea", size="small")
bio.callout(ax, (cx - 1.2, 3.8), (0.6, 3.8), "Gastrodermis", size="small")
bio.callout(ax, (cx + 0.2, 5.0), (cx + 3.4, 5.6), "Gastrovascular\ncavity", size="small")
bio.callout(ax, (cx, 0.7), (cx + 3.4, 1.2), "Pedal disc", size="small")
bio.label(ax, (cx, 0.15), "Polyp", size="title", bold=True)

# ---------------------------------------------------------------- B: medusa
bio.panel(ax, "B", (11.4, 11.4))
mx, yb = 17.6, 6.0  # bell centre and margin height
ang = np.linspace(np.pi, 0, 240)
ex = np.c_[mx + 4.6 * np.cos(ang), yb + 3.6 * np.sin(ang)]   # exumbrella, left to right
sub = np.c_[mx + 4.2 * np.cos(ang), yb + 1.5 * np.sin(ang)]  # subumbrella
bell = np.vstack([ex, sub[::-1]])
ax.add_patch(Polygon(bell, closed=True, facecolor=P.fill(MES), edgecolor=P.edge(MES), lw=0.7, zorder=3))
band(ax, ex, 0.0, 0.16, ECT, z=4)
band(ax, sub, 0.0, 0.14, ECT, z=4)
# tentacles and velum at the margin
for sgn in (1, -1):
    x0 = mx + sgn * 4.42
    t = spline([(x0, yb + 0.05), (x0 + sgn * 0.12, yb - 1.4), (x0 - sgn * 0.08, yb - 2.8), (x0 + sgn * 0.1, yb - 4.2)])
    band(ax, t, -0.09, 0.09, ECT, z=4)
    v = spline([(mx + sgn * 4.3, yb + 0.02), (mx + sgn * 3.3, yb - 0.1)])
    band(ax, v, -0.08, 0.08, ECT, z=5)
# radial canals: run in the mesoglea just above the subumbrella, from the stomach to the ring canal
for sl in (slice(20, 95), slice(145, 220)):
    c = sub[sl]
    band(ax, c, 0.3, 0.55, END, z=5)
    band(ax, c, 0.39, 0.46, face=CAV, z=5.2)
for sgn in (1, -1):
    ax.add_patch(Polygon(np.c_[mx + sgn * 4.0 + 0.17 * np.cos(np.linspace(0, 2 * np.pi, 40)),
                               yb + 0.45 + 0.17 * np.sin(np.linspace(0, 2 * np.pi, 40))],
                         closed=True, facecolor=CAV, edgecolor=P.edge(END), lw=2.2, zorder=5.3))
# stomach above the subumbrella apex
th = np.linspace(0, 2 * np.pi, 120)
ax.add_patch(Polygon(np.c_[mx + 1.3 * np.cos(th), yb + 2.15 + 0.42 * np.sin(th)], closed=True, facecolor=CAV,
                     edgecolor=P.edge(END), lw=2.6, zorder=5.4))
# manubrium hanging from the subumbrella
man = spline([(mx, yb + 1.9), (mx, yb + 0.5), (mx, yb - 1.2)])
tube(ax, man, 0.34, z=6)
bio.callout(ax, (mx, yb - 1.25), (mx + 1.6, yb - 2.4), "Mouth (manubrium)", size="small")
bio.callout(ax, (mx - 0.8, yb + 2.2), (12.0, yb + 3.4), "Stomach", size="small")
bio.callout(ax, (mx + 2.6, yb + 1.6), (mx + 3.6, yb + 4.6), "Radial canal", size="small")
bio.callout(ax, (mx - 4.0, yb + 0.45), (12.0, yb + 1.2), "Ring canal", size="small")
bio.callout(ax, (mx + 1.2, yb + 3.0), (mx + 4.6, yb + 4.0), "Mesoglea", size="small")
bio.callout(ax, (mx + 3.75, yb + 2.15), (mx + 4.9, yb + 2.9), "Exumbrella epidermis", size="small")
bio.callout(ax, (mx - 3.5, yb - 0.08), (12.0, yb - 0.6), "Velum", size="small")
bio.callout(ax, (mx - 1.6, yb + 1.4), (12.0, yb + 2.3), "Subumbrella", size="small")
bio.callout(ax, (mx + 4.55, yb - 2.4), (mx + 5.2, yb - 1.4), "Tentacle", size="small")
bio.label(ax, (mx, 0.15), "Medusa", size="title", bold=True)
zoo.germ_layer_legend(ax, (12.6, 0.9), items=("ectoderm", "endoderm", "mesoglea"))
