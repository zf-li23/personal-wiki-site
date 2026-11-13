# The pelvic girdle of dinosaurs and birds, left lateral view, anterior to the left (schematic, after Pough
# et al. 2023, Kardong 2019 and Benton 2015). Saurischian (e.g. a theropod): triradiate pelvis with the pubis
# pointing forward and down (propubic). Ornithischian (e.g. an ornithopod): the pubis is rotated backward
# beside the ischium (opisthopubic) and has a forward prepubic process. Bird: the pubis is also rotated
# backward, convergently with ornithischians, and the long ilium is fused with the synsacrum. All have a
# perforate (open) acetabulum, a dinosaur synapomorphy. Bones in the course-wide homology colours.
import numpy as np
import wikibio as bio
import vertskel as vs

P = bio.P
fig, ax, boxes = vs.panels(3, 8.4, 6.4, titles=["Saurischian", "Ornithischian", "Bird"],
                           subtitles=["propubic (Tyrannosaurus, sauropods)", "opisthopubic, prepubic process",
                                      "opisthopubic, fused to synsacrum"], legend_rows=1, gap=0.8)


def hole(c, r):
    pts = np.array(vs.oval(c, r, r * 0.9))
    ax.fill(pts[:, 0], pts[:, 1], color=P.surface(), zorder=9, lw=0)
    ax.plot(np.r_[pts[:, 0], pts[0, 0]], np.r_[pts[:, 1], pts[0, 1]], color=P.ink(), lw=0.9, zorder=9.5)


def vertebrae(x0, x1, y, n):
    for k in range(n):
        cx = x0 + (k + 0.5) * (x1 - x0) / n
        vs.bone(ax, "centrum", vs.oval((cx, y), (x1 - x0) / n * 0.46, 0.32), state="context")


# saurischian
x, y, w, h = boxes[0]
c = (x + 4.0, y + 4.0)
vertebrae(x + 0.6, x + 7.6, y + 5.9, 6)
a = vs.draw(ax, [
    ("ilium", vs.poly([(-3.2, 1.0), (-2.6, 1.7), (3.0, 1.8), (3.6, 1.0), (1.0, 0.45), (-1.0, 0.45)])),
    ("pubis", vs.rod((-0.6, 0.0), (-2.0, -3.4), 0.6, 0.45)),
    ("pubis", vs.oval((-1.6, -3.55), 0.9, 0.3)),
    ("ischium", vs.rod((0.8, 0.0), (2.6, -2.9), 0.5, 0.3))], at=c)
hole((c[0], c[1] + 0.05), 0.55)
vs.callout(ax, (c[0] - 2.2, c[1] - 3.55), (x + 0.2, y + 0.3), "pubic boot")
vs.callout(ax, (c[0], c[1] + 0.05), (x + 0.3, y + 2.6), "perforate acetabulum")

# ornithischian
x, y, w, h = boxes[1]
c = (x + 4.0, y + 4.0)
vertebrae(x + 0.6, x + 7.6, y + 5.9, 6)
vs.draw(ax, [
    ("ilium", vs.poly([(-3.6, 1.0), (-3.0, 1.5), (3.0, 1.75), (3.6, 1.0), (1.0, 0.45), (-1.0, 0.45)])),
    ("pubis", vs.rod((-0.5, 0.0), (-3.2, -0.9), 0.45, 0.3)),
    ("pubis", vs.rod((-0.3, -0.2), (2.4, -3.2), 0.28, 0.2)),
    ("ischium", vs.rod((0.8, 0.0), (3.0, -2.8), 0.45, 0.3))], at=c)
hole((c[0], c[1] + 0.05), 0.55)
vs.callout(ax, (c[0] - 2.6, c[1] - 0.75), (x + 0.2, y + 1.6), "prepubic process")
vs.callout(ax, (c[0] + 1.6, c[1] - 2.3), (x + 1.8, y + 0.3), "postpubic rod")

# bird
x, y, w, h = boxes[2]
c = (x + 3.6, y + 4.0)
vertebrae(x + 0.4, x + 8.2, y + 5.4, 9)
vs.draw(ax, [
    ("ilium", vs.poly([(-3.0, 0.9), (-2.8, 1.5), (4.3, 1.5), (4.5, 0.4), (1.0, 0.2), (-1.0, 0.5)])),
    ("ischium", vs.poly([(0.6, 0.0), (4.4, 0.35), (4.2, -0.9), (1.2, -0.6)])),
    ("pubis", vs.rod((-0.2, -0.35), (4.6, -1.8), 0.22, 0.16))], at=c)
hole((c[0], c[1] + 0.05), 0.45)
vs.callout(ax, (x + 6.0, y + 5.4), (x + 6.5, y + 6.6), "synsacrum (fused vertebrae)")
vs.legend(ax, ["ilium", "ischium", "pubis", ("centrum", "vertebrae", "context")], at=(0.4, 0.55 + 0.25),
          width=24.0, ncols=4)
