# The parts of a vertebra and the types of centra, schematic (vertskel homology colours). A: tetrapod trunk
# vertebra in anterior and left lateral views with a two-headed rib; fish caudal vertebra in anterior view.
# B: median sagittal sections of three successive centra (anterior to the left) for the five centrum types.
# After Kardong (2019) and Romer & Parsons. Not to scale.
import numpy as np
import wikibio as bio
import vertskel as vs

P = bio.P
fig, ax = bio.canvas(30, 15)

# A1: anterior view of a tetrapod vertebra
o = (1.0, 8.0)
a = vs.draw(ax, [("centrum", vs.oval((2.5, 1.2), 1.0, 0.9)),
                 ("neural_arch", vs.poly([(1.6, 1.9), (2.0, 3.3), (3.0, 3.3), (3.4, 1.9), (3.0, 2.2), (2.0, 2.2)])),
                 ("neural_spine", vs.rod((2.5, 3.2), (2.5, 5.0), 0.4)),
                 ("transverse_process", vs.rod((1.8, 2.4), (0.3, 2.6), 0.35)),
                 ("transverse_process", vs.rod((3.2, 2.4), (4.7, 2.6), 0.35)),
                 ("zygapophysis", vs.oval((1.9, 3.2), 0.3, 0.18)), ("zygapophysis", vs.oval((3.1, 3.2), 0.3, 0.18)),
                 ("rib", vs.smooth([(4.6, 2.6), (5.8, 2.2), (6.4, 0.2), (6.1, -1.6), (5.8, -1.6), (6.0, 0.2), (5.4, 1.9), (4.0, 1.4)]))],
            at=o)
c = np.array(vs.oval((o[0] + 2.5, o[1] + 2.7), 0.38, 0.33))
ax.fill(c[:, 0], c[:, 1], color=P.surface(), zorder=20)
bio.label(ax, (o[0] + 2.5, o[1] + 2.7), "cord", size="tiny", color=P.muted())
for k, (tx, ty) in (("centrum", (o[0] - 0.6, o[1] - 0.6)), ("neural_spine", (o[0] + 4.2, o[1] + 5.2)),
                    ("transverse_process", (o[0] - 0.8, o[1] + 3.6)), ("zygapophysis", (o[0] + 0.2, o[1] + 4.6)),
                    ("rib", (o[0] + 7.4, o[1] + 0.8))):
    vs.callout(ax, a[k], (tx, ty), k)
vs.callout(ax, (o[0] + 4.3, o[1] + 1.5), (o[0] + 4.6, o[1] - 1.4), "capitulum")
vs.callout(ax, (o[0] + 5.0, o[1] + 2.5), (o[0] + 7.4, o[1] + 3.2), "tuberculum")
bio.label(ax, (o[0] + 3.0, 14.3), "Tetrapod trunk vertebra, anterior", size="small", bold=True)

# A2: fish caudal vertebra, anterior view
o = (11.5, 8.0)
a = vs.draw(ax, [("centrum", vs.oval((2.0, 2.4), 0.9, 0.85)),
                 ("neural_arch", vs.poly([(1.3, 3.0), (1.7, 4.2), (2.3, 4.2), (2.7, 3.0)])),
                 ("neural_spine", vs.rod((2.0, 4.1), (2.2, 5.6), 0.3)),
                 ("haemal_arch", vs.poly([(1.3, 1.8), (1.7, 0.6), (2.3, 0.6), (2.7, 1.8)])),
                 ("haemal_spine", vs.rod((2.0, 0.7), (2.2, -0.8), 0.3))], at=o)
for yy, t in ((3.65, "cord"), (1.15, "vessels")):
    c = np.array(vs.oval((o[0] + 2.0, o[1] + yy), 0.28, 0.25))
    ax.fill(c[:, 0], c[:, 1], color=P.surface(), zorder=20)
vs.callout(ax, a["haemal_arch"], (o[0] + 3.8, o[1] + 0.4), "haemal_arch")
vs.callout(ax, a["neural_arch"], (o[0] + 3.8, o[1] + 4.6), "neural_arch")
bio.label(ax, (o[0] + 2.0, 14.3), "Fish caudal vertebra", size="small", bold=True)

# A3: lateral view of three tetrapod vertebrae
o = (18.5, 9.0)
for k in range(3):
    x = k * 3.2
    vs.draw(ax, [("centrum", vs.poly([(x, 0.0), (x + 2.6, 0.0), (x + 2.6, 1.6), (x, 1.6)])),
                 ("neural_arch", vs.poly([(x + 0.3, 1.6), (x + 2.3, 1.6), (x + 2.1, 2.6), (x + 0.5, 2.6)])),
                 ("neural_spine", vs.poly([(x + 0.8, 2.6), (x + 2.0, 2.6), (x + 2.2, 4.4), (x + 1.0, 4.4)])),
                 ("zygapophysis", vs.oval((x + 0.25, 2.5), 0.35, 0.18)),
                 ("zygapophysis", vs.oval((x + 2.55, 2.4), 0.35, 0.18))], at=o)
vs.callout(ax, (o[0] + 3.45, o[1] + 2.45), (o[0] + 8.6, o[1] + 4.0), "zygapophyses overlap")
bio.label(ax, (o[0] + 4.7, 14.3), "Lateral view, anterior left", size="small", bold=True)
bio.panel(ax, "A", (0.3, 14.8))

# B: centrum types, sagittal sections
types = ["amphicoelous", "procoelous", "opisthocoelous", "heterocoelous", "acoelous"]
bio.panel(ax, "B", (0.3, 6.4))
for t_i, t in enumerate(types):
    ox = 0.8 + t_i * 5.9
    oy = 2.2
    bio.label(ax, (ox + 2.4, 6.0), t, size="small", bold=True)
    for k in range(3):
        x0 = ox + k * 1.65
        x1 = x0 + 1.45
        n = 30
        ys = np.linspace(0, 2.4, n)
        d = 0.35 * np.sin(np.pi * ys / 2.4)
        if t == "amphicoelous":
            left, right = x0 + d, x1 - d
        elif t == "procoelous":
            left, right = x0 + d, x1 + d
        elif t == "opisthocoelous":
            left, right = x0 - d, x1 - d
        elif t == "heterocoelous":
            left, right = x0 + 0.6 * d, x1 + 0.6 * d
        else:
            left, right = np.full(n, x0), np.full(n, x1)
        pts = list(zip(left, ys)) + list(zip(right[::-1], ys[::-1]))
        vs.bone(ax, "centrum", vs.poly([(x, y + oy) for x, y in pts]))
        if t in ("amphicoelous",) and k < 2:
            vs.bone(ax, "notochord", vs.oval((x1 + 0.1, oy + 1.2), 0.32, 0.9))
        if t == "acoelous" and k < 2:
            vs.bone(ax, "notochord", vs.poly([(x1 + 0.03, oy + 0.1), (x1 + 0.17, oy + 0.1), (x1 + 0.17, oy + 2.3), (x1 + 0.03, oy + 2.3)]),
                    state="cartilage")
    if t == "heterocoelous":
        bio.label(ax, (ox + 2.4, 1.6), "saddle-shaped faces: concave in one plane,\nconvex in the other", size="tiny", color=P.muted())
    if t == "acoelous":
        bio.label(ax, (ox + 2.4, 1.6), "flat faces; discs with nucleus pulposus", size="tiny", color=P.muted())
    if t == "amphicoelous":
        bio.label(ax, (ox + 2.4, 1.6), "notochord remnants between centra", size="tiny", color=P.muted())
