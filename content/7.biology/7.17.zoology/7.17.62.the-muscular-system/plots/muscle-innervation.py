# Head and neck muscles of a shark and of a mammal, coloured by their motor nerve (and so by pharyngeal arch
# for branchiomeric muscles; arch colours from vertskel). Lateral views, anterior to the left. Schematic.
import numpy as np
import wikibio as bio
import vertskel as vs

P = bio.P

NERVE = {  # nerve -> (fill, edge)
    "V": (vs.color("meckel"), vs.edge("meckel")),
    "VII": (vs.color("hyomandibula"), vs.edge("hyomandibula")),
    "IX": (vs.color("arch_3"), vs.edge("arch_3")),
    "X": (vs.color("arch_4"), vs.edge("arch_4")),
    "XI": (vs.color("arch_6"), vs.edge("arch_6")),
}


def muscle(ax, verts, nerve=None, token=None, z=6):
    v = np.asarray(verts, float)
    if nerve:
        f, e = NERVE[nerve]
        ax.fill(v[:, 0], v[:, 1], facecolor=f, edgecolor=e, lw=0.9, zorder=z, joinstyle="round")
    else:
        bio.shape(ax, v, token=token, zorder=z, lw=0.9)
    return v.mean(axis=0)


def oval(c, rx, ry, a=0):
    return vs.oval(c, rx, ry, a)


fig, ax = bio.canvas(28.2, 11.4)

# ---------------------------------------------------------------- A: shark
bio.panel(ax, "A", (0.3, 10.6))
bio.label(ax, (0.9, 10.6), "Shark", size="title", ha="left")
ox, oy = 0.6, 3.3
top = [(0, 3.0), (0.8, 3.9), (2.5, 4.6), (5, 5.0), (8, 5.3), (11.8, 5.2)]
bot = [(11.8, 1.2), (8, 1.0), (5, 1.1), (3.0, 1.5), (1.2, 2.2), (0.2, 2.7)]
body = vs.smooth([(x + ox, y + oy) for x, y in top + bot])
bio.shape(ax, body, token="animal", zorder=2)
X = lambda x: x + ox  # noqa: E731
Y = lambda y: y + oy  # noqa: E731
# eye
bio.shape(ax, oval((X(2.3), Y(4.0)), 0.32, 0.24), token="nucleus", zorder=9)
# myomeres: epaxial above, hypaxial below the horizontal septum
sept = 3.2
muscle(ax, [(X(8.3), Y(sept)), (X(8.3), Y(5.2)), (X(11.8), Y(5.15)), (X(11.8), Y(sept))], token="muscle", z=4)
muscle(ax, [(X(7.9), Y(sept)), (X(11.8), Y(sept)), (X(11.8), Y(1.25)), (X(8.0), Y(1.05))], token="enzyme", z=4)
for k in range(6):
    x = X(8.6 + 0.6 * k)
    w = np.array([(x, Y(5.15)), (x - 0.25, Y(4.4)), (x + 0.15, Y(3.2)), (x - 0.25, Y(2.0)), (x, Y(1.15))])
    ax.plot(w[:, 0], w[:, 1], color=P.on_fill(), lw=0.8, zorder=5)
ax.plot([X(7.9), X(11.8)], [Y(sept), Y(sept)], color=P.ink(), lw=1.0, zorder=5)
# mandibular arch: adductor mandibulae, levator palatoquadrati, intermandibularis
muscle(ax, oval((X(3.5), Y(2.65)), 0.75, 0.45, 20), "V")
muscle(ax, oval((X(3.1), Y(3.55)), 0.45, 0.22, -25), "V")
muscle(ax, [(X(1.4), Y(2.1)), (X(3.2), Y(1.55)), (X(3.4), Y(1.75)), (X(1.6), Y(2.35))], "V")
# hyoid arch constrictor and levator hyomandibulae
muscle(ax, [(X(4.35), Y(1.4)), (X(4.75), Y(1.35)), (X(4.85), Y(4.55)), (X(4.45), Y(4.5))], "VII")
# branchial constrictors between five gill slits
slits = [5.3, 5.85, 6.4, 6.95, 7.5]
for i, sx in enumerate(slits):
    nerve = "IX" if i == 0 else "X"
    muscle(ax, [(X(sx - 0.42), Y(1.35)), (X(sx - 0.08), Y(1.3)), (X(sx - 0.08), Y(4.0)), (X(sx - 0.42), Y(4.05))], nerve)
    ax.plot([X(sx), X(sx)], [Y(1.8), Y(3.7)], color=P.ink(), lw=1.6, zorder=8, solid_capstyle="round")
# cucullaris above the gills
muscle(ax, [(X(5.0), Y(4.55)), (X(7.9), Y(4.9)), (X(8.0), Y(4.3)), (X(5.1), Y(4.1))], "XI")
# hypobranchial muscles below the gills (somatic, spinal nerves)
muscle(ax, [(X(2.6), Y(1.45)), (X(7.8), Y(1.05)), (X(7.8), Y(1.3)), (X(2.8), Y(1.7))], token="positive", z=7)
lab = [((X(3.6), Y(2.7)), (X(1.0), Y(0.0)), "adductor mandibulae"),
       ((X(3.1), Y(3.6)), (X(0.4), Y(5.9)), "levator palatoquadrati"),
       ((X(2.0), Y(2.1)), (X(-0.2), Y(1.0)), "intermandibularis"),
       ((X(4.6), Y(4.3)), (X(3.4), Y(6.9)), "levator hyomandibulae / hyoid constrictor"),
       ((X(5.1), Y(3.0)), (X(6.0), Y(6.9)), "constrictor of arch 3"),
       ((X(6.6), Y(2.6)), (X(7.0), Y(-0.45)), "constrictors of arches 4-7"),
       ((X(6.5), Y(4.6)), (X(8.3), Y(6.4)), "cucullaris"),
       ((X(5.5), Y(1.35)), (X(4.2), Y(-0.45)), "hypobranchial muscles"),
       ((X(10.2), Y(4.6)), (X(10.6), Y(6.2)), "epaxial myomeres"),
       ((X(10.2), Y(2.0)), (X(11.0), Y(0.0)), "hypaxial myomeres"),
       ((X(11.5), Y(sept)), (X(12.4), Y(4.1)), "horizontal septum")]
for p, q, s in lab:
    bio.callout(ax, p, q, s, size="tiny")

# ---------------------------------------------------------------- B: mammal
bio.panel(ax, "B", (13.6, 10.6))
bio.label(ax, (14.2, 10.6), "Mammal", size="title", ha="left")
mx, my = 13.9, 3.1
M = lambda x, y: (x + mx, y + my)  # noqa: E731
head = vs.smooth([M(*p) for p in [(0.1, 2.6), (0.4, 3.6), (1.6, 4.4), (3.2, 5.6), (4.6, 5.8), (5.6, 5.2), (6.6, 5.6),
                                    (9.5, 5.6), (11.8, 5.4), (11.8, 0.6), (8.0, 0.4), (6.2, 0.9), (4.8, 1.3),
                                    (3.0, 1.5), (1.2, 1.8), (0.3, 2.1)]])
bio.shape(ax, head, token="animal", zorder=2)
bio.shape(ax, oval(M(2.7, 4.2), 0.3, 0.22), token="nucleus", zorder=9)
# eye ring (orbicularis oculi) and mouth ring (orbicularis oris), facial muscles
th = np.linspace(0, 2 * np.pi, 60)
for c, r1, r2 in ((M(2.7, 4.2), 0.55, 0.36), (M(1.05, 2.45), 0.7, 0.45)):
    ring = np.vstack([np.column_stack([c[0] + r1 * np.cos(th), c[1] + r1 * 0.75 * np.sin(th)]),
                      np.column_stack([c[0] + r2 * np.cos(th[::-1]), c[1] + r2 * 0.75 * np.sin(th[::-1])])])
    muscle(ax, ring, "VII", z=8)
# temporalis fan and masseter
muscle(ax, [M(3.3, 4.5), M(4.0, 5.5), M(5.2, 5.3), M(5.3, 4.4), M(4.2, 3.6)], "V")
muscle(ax, oval(M(3.6, 2.6), 0.85, 0.55, 30), "V")
# platysma sheet over the neck (thin) and posterior digastric
muscle(ax, [M(4.4, 1.5), M(7.8, 1.0), M(8.4, 2.2), M(5.4, 2.6)], "VII", z=5)
# stylopharyngeus (IX), pharynx and larynx (X)
muscle(ax, oval(M(5.1, 3.25), 0.4, 0.15, -40), "IX", z=7)
muscle(ax, oval(M(6.1, 2.75), 0.55, 0.3), "X", z=7)
# sternocleidomastoid and trapezius (XI)
muscle(ax, [M(5.4, 4.2), M(5.9, 4.5), M(9.0, 1.5), M(8.6, 1.1)], "XI", z=7)
muscle(ax, [M(6.4, 5.4), M(11.8, 5.35), M(11.8, 4.2), M(8.2, 4.4)], "XI", z=6)
# epaxial neck muscles (somatic), infrahyoid and tongue (somatic: XII, cervical)
muscle(ax, [M(6.0, 4.4), M(11.8, 4.15), M(11.8, 3.2), M(6.5, 3.6)], token="muscle", z=5)
muscle(ax, [M(6.8, 2.1), M(11.6, 0.8), M(11.7, 1.25), M(7.0, 2.45)], token="positive", z=6)
muscle(ax, oval(M(1.9, 2.35), 0.8, 0.18, -5), token="positive", z=9)
labm = [((M(1.0, 1.95)[0], M(1.0, 1.95)[1]), M(0.8, -0.6), "orbicularis oris"),
        (M(2.3, 4.55), M(1.0, 6.3), "orbicularis oculi"),
        (M(4.4, 4.9), M(3.4, 6.9), "temporalis"),
        (M(3.7, 2.4), M(2.6, -0.3), "masseter"),
        (M(2.3, 2.35), M(-0.2, 1.1), "tongue (XII)"),
        (M(5.1, 3.25), M(5.6, 6.9), "stylopharyngeus"),
        (M(6.2, 2.7), M(6.4, -0.45), "pharynx, larynx"),
        (M(6.2, 1.6), M(4.6, -0.45), "platysma"),
        (M(7.4, 2.8), M(8.0, 7.4), "sternocleidomastoid"),
        (M(10.0, 4.9), M(11.9, 6.95), "trapezius"),
        (M(10.0, 3.7), M(12.6, 6.2), "epaxial"),
        (M(9.6, 1.25), M(10.6, -0.3), "infrahyoid")]
for p, q, s in labm:
    bio.callout(ax, p, q, s, size="tiny")

# ---------------------------------------------------------------- legend
items = [("V", "trigeminal V (arch 1)"), ("VII", "facial VII (arch 2)"), ("IX", "glossopharyngeal IX (arch 3)"),
         ("X", "vagus X (arches 4-7)"), ("XI", "accessory XI / cucullaris group")]
x = 1.0
for key, text in items:
    f, e = NERVE[key]
    ax.fill([x, x + 0.45, x + 0.45, x], [0.95, 0.95, 1.27, 1.27], facecolor=f, edgecolor=e, lw=0.8)
    bio.label(ax, (x + 0.6, 1.11), text, size="tiny", ha="left")
    x += 5.0
x = 1.0
for tok, text in (("muscle", "epaxial (dorsal rami)"), ("enzyme", "hypaxial (ventral rami)"),
                  ("positive", "hypobranchial, infrahyoid, tongue (spinal nerves, XII)")):
    bio.shape(ax, np.array([(x, 0.25), (x + 0.45, 0.25), (x + 0.45, 0.57), (x, 0.57)]), token=tok, lw=0.8, zorder=6)
    bio.label(ax, (x + 0.6, 0.41), text, size="tiny", ha="left")
    x += 6.5
