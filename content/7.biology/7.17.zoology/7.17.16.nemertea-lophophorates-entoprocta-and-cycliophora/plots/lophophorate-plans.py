# U-shaped guts and tentacle crowns (schematic sagittal views, not to scale; mouth and tentacle crown up).
# A-C: the three lophophorate phyla, in which the anus opens OUTSIDE the ring of tentacles (lophophore,
# hollow tentacles containing a coelomic canal). D: an entoproct, whose solid tentacles surround both mouth
# and anus (hence "inner anus"); its tentacle crown is not a lophophore. Body wall grey, coelom green wash,
# gut yellow, tentacles red, shell or zooecium beige.
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(32, 12.0)


def gut(points, w=2.6):
    p = np.asarray(points, float)
    t = np.linspace(0, 1, 200)
    # Catmull-Rom through control points
    out = []
    m = len(p)
    for i in range(m - 1):
        p0, p1, p2, p3 = p[max(i - 1, 0)], p[i], p[i + 1], p[min(i + 2, m - 1)]
        for s in np.linspace(0, 1, 40, endpoint=False):
            out.append(0.5 * ((2 * p1) + (-p0 + p2) * s + (2 * p0 - 5 * p1 + 4 * p2 - p3) * s * s
                              + (-p0 + 3 * p1 - 3 * p2 + p3) * s ** 3))
    out.append(p[-1])
    out = np.array(out)
    ax.plot(out[:, 0], out[:, 1], color=P.edge("endoderm"), lw=w + 1.6, zorder=20, solid_capstyle="round")
    ax.plot(out[:, 0], out[:, 1], color=P.fill("endoderm"), lw=w, zorder=21, solid_capstyle="round")
    return out


def tentacles(base_pts, length, angles, hollow=True, z=24):
    for (x, y), a in zip(base_pts, angles):
        x2, y2 = x + length * np.cos(a), y + length * np.sin(a)
        ax.plot([x, x2], [y, y2], color=P.edge("mesoderm"), lw=3.2, zorder=z, solid_capstyle="round")
        ax.plot([x, x2], [y, y2], color=P.fill("coelom") if hollow else P.fill("mesoderm"), lw=1.4 if hollow else 2.2,
                zorder=z + 1, solid_capstyle="round")


def title(x, letter, name, sub):
    bio.panel(ax, letter, (x - 3.4, 11.7))
    bio.label(ax, (x, 11.4), name, size="normal", bold=True)
    bio.label(ax, (x, 10.8), sub, size="small", color=P.muted())


# ---------------- A: phoronid ----------------
x = 4.0
title(x, "A", "Phoronida", "horseshoe worm in its tube")
bio.shape(ax, [[x - 1.0, 0.8], [x + 1.0, 0.8], [x + 1.0, 7.4], [x - 1.0, 7.4]], token="bone", lw=0.8, zorder=4)
bio.shape(ax, bio.smooth_closed([[x - 0.6, 1.3], [x + 0.6, 1.3], [x + 0.7, 4.0], [x + 0.55, 7.8], [x - 0.55, 7.8],
                                  [x - 0.7, 4.0]]), token="neutral", zorder=6)
bio.shape(ax, bio.smooth_closed([[x - 0.42, 1.6], [x + 0.42, 1.6], [x + 0.5, 4.0], [x + 0.4, 7.4], [x - 0.4, 7.4],
                                  [x - 0.5, 4.0]]), token="coelom", zorder=7, lw=0.5)
gut([[x - 0.15, 7.75], [x - 0.2, 5.0], [x - 0.15, 2.4], [x, 1.9], [x + 0.18, 2.4], [x + 0.22, 5.0], [x + 0.35, 7.9]])
base = [(x - 0.5 + 1.0 * k / 7, 7.9) for k in range(8)]
tentacles(base, 2.0, np.linspace(np.pi * 0.72, np.pi * 0.28, 8))
bio.callout(ax, (x - 0.15, 7.75), (x - 2.6, 9.6), "Mouth")
bio.callout(ax, (x + 0.35, 7.92), (x + 2.6, 8.4), "Anus (outside crown)")
bio.callout(ax, (x - 0.9, 9.4), (x - 2.6, 10.2), "Lophophore")
bio.callout(ax, (x - 0.2, 4.8), (x - 2.8, 4.8), "U-shaped gut")
bio.callout(ax, (x + 0.35, 3.4), (x + 2.6, 3.4), "Trunk coelom")
bio.callout(ax, (x + 0.95, 1.6), (x + 2.6, 1.0), "Chitinous tube")

# ---------------- B: bryozoan zooid ----------------
x = 11.4
title(x, "B", "Bryozoa", "one feeding zooid (polypide extended)")
bio.shape(ax, [[x - 1.7, 0.8], [x + 1.7, 0.8], [x + 1.7, 5.6], [x + 0.7, 5.6], [x + 0.7, 5.3], [x - 0.7, 5.3],
               [x - 0.7, 5.6], [x - 1.7, 5.6]], token="bone", lw=0.9, zorder=4)
bio.shape(ax, [[x - 1.5, 1.0], [x + 1.5, 1.0], [x + 1.5, 5.1], [x - 1.5, 5.1]], token="coelom", lw=0.5, zorder=5)
bio.shape(ax, [[x - 0.35, 5.1], [x + 0.35, 5.1], [x + 0.3, 7.5], [x - 0.3, 7.5]], token="neutral", zorder=6)
gut([[x - 0.05, 7.5], [x - 0.1, 5.5], [x - 0.5, 3.4], [x - 0.3, 2.2], [x + 0.3, 2.2], [x + 0.5, 3.0],
     [x + 0.35, 4.6], [x + 0.25, 6.2]])
ax.plot([x - 0.3, x - 1.3], [2.2, 1.0], color=P.edge("mesoderm"), lw=1.2, zorder=19)   # funiculus
ax.plot([x + 0.2, x + 1.2], [6.0, 1.1], color=P.edge("muscle"), lw=1.6, zorder=19)     # retractor
base = [(x - 0.3 + 0.6 * k / 7, 7.55) for k in range(8)]
tentacles(base, 2.4, np.linspace(np.pi * 0.8, np.pi * 0.2, 8))
bio.callout(ax, (x - 0.05, 7.5), (x - 2.6, 9.0), "Mouth")
bio.callout(ax, (x + 0.27, 6.1), (x + 2.4, 8.6), "Anus (outside crown)")
bio.callout(ax, (x + 0.9, 3.1), (x + 2.6, 4.6), "Retractor muscle")
bio.callout(ax, (x - 0.9, 1.55), (x - 2.4, 0.4), "Funiculus")
bio.callout(ax, (x - 1.6, 4.0), (x - 2.6, 4.6), "Zooecium (body wall)")
bio.callout(ax, (x + 0.3, 6.8), (x + 2.6, 6.6), "Tentacle sheath")

# ---------------- C: brachiopod ----------------
x = 19.0
title(x, "C", "Brachiopoda", "lamp shell, sagittal section")
th = np.linspace(0, np.pi, 80)
dors = np.c_[x + 2.1 * np.cos(th), 4.6 + 1.4 * np.sin(th)]
vent = np.c_[x + 2.3 * np.cos(th), 4.4 - 1.7 * np.sin(th)]
ax.plot(dors[:, 0], dors[:, 1], color=P.edge("bone"), lw=5, zorder=8, solid_capstyle="round")
ax.plot(vent[:, 0], vent[:, 1], color=P.edge("bone"), lw=5, zorder=8, solid_capstyle="round")
bio.shape(ax, bio.smooth_closed([[x + 1.9, 4.4], [x + 1.2, 5.4], [x + 0.4, 5.0], [x + 0.5, 3.8], [x + 1.3, 3.4]]),
          token="coelom", zorder=9, lw=0.6)
gut([[x - 0.2, 4.5], [x + 0.6, 4.8], [x + 1.2, 4.8], [x + 1.4, 4.2], [x + 1.0, 3.8]])
for k in range(4):                         # lophophore arms seen in section: coils with tentacles
    cxx = x - 0.4 - 0.45 * k
    t2 = np.linspace(0, 2 * np.pi, 40)
    ax.plot(cxx + 0.25 * np.cos(t2), 4.5 + 0.25 * np.sin(t2), color=P.edge("mesoderm"), lw=1.2, zorder=12)
    tentacles([(cxx, 4.75), (cxx, 4.25)], 0.55, [np.pi / 2 + 0.3, -np.pi / 2 - 0.3], z=13)
ax.plot([x + 2.3, x + 3.4], [4.4, 4.0], color=P.edge("neutral"), lw=4.5, zorder=7, solid_capstyle="round")
bio.callout(ax, (x, 6.0), (x - 1.2, 9.6), "Dorsal (brachial) valve")
bio.callout(ax, (x, 2.7), (x - 1.0, 1.0), "Ventral (pedicle) valve")
bio.callout(ax, (x - 1.15, 4.05), (x - 2.6, 2.0), "Lophophore arms")
bio.callout(ax, (x + 1.25, 3.95), (x + 3.4, 1.0), "Gut (blind in articulates)")
bio.callout(ax, (x + 3.2, 4.06), (x + 3.0, 2.4), "Pedicle")
bio.callout(ax, (x - 0.2, 4.5), (x - 3.2, 3.4), "Mouth")

# ---------------- D: entoproct ----------------
x = 26.4
title(x, "D", "Entoprocta (contrast)", "anus inside the tentacle ring")
ax.plot([x, x], [0.8, 4.3], color=P.edge("neutral"), lw=5, zorder=6, solid_capstyle="round")
cup = bio.smooth_closed([[x - 1.5, 7.3], [x - 0.9, 5.2], [x, 4.3], [x + 0.9, 5.2], [x + 1.5, 7.3], [x, 7.0]])
bio.shape(ax, cup, token="neutral", zorder=7)
bio.shape(ax, bio.smooth_closed([[x - 1.1, 6.9], [x - 0.6, 5.4], [x, 4.8], [x + 0.6, 5.4], [x + 1.1, 6.9], [x, 6.7]]),
          token="pseudocoel", zorder=8, lw=0.5)
gut([[x - 0.7, 7.05], [x - 0.6, 5.8], [x, 5.2], [x + 0.6, 5.6], [x + 0.5, 6.6], [x + 0.45, 7.0]], w=2.2)
base = [(x - 1.5 + 3.0 * k / 9, 7.25 + 0.15 * np.sin(np.pi * k / 9)) for k in range(10)]
tentacles(base, 1.6, np.linspace(np.pi * 0.85, np.pi * 0.15, 10), hollow=False)
bio.callout(ax, (x - 0.7, 7.05), (x - 2.6, 9.6), "Mouth")
bio.callout(ax, (x + 0.45, 7.0), (x + 2.6, 9.6), "Anus (inside crown)")
bio.callout(ax, (x + 0.2, 5.6), (x + 1.9, 4.4), "Body cavity (not a coelom)")
bio.callout(ax, (x, 2.5), (x + 1.6, 2.2), "Stalk")
bio.callout(ax, (x + 1.3, 8.0), (x + 2.6, 8.6), "Solid tentacles")
