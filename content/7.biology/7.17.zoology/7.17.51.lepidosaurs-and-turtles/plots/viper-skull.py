# Cranial kinesis in a viper (left lateral view, anterior to the left; schematic after Kardong 1974, Cundall
# and Irish 2008 and Pough et al. 2023). Mouth closed (A) and open with the fang erected (B). The quadrate
# hangs from the supratemporal and swings forward when the mouth opens; it pushes the pterygoid forward,
# which pushes the ectopterygoid against the short maxilla; the maxilla rotates on the prefrontal and the
# hollow fang swings from its folded position to point forward. The lower jaw (dentary and compound bone)
# drops at the quadrate joint; the two halves of the lower jaw are joined only by soft tissue at the chin.
# Bones in the course-wide homology colours; joints are open circles. Not to scale.
import numpy as np
import wikibio as bio
import vertskel as vs

P = bio.P
fig, ax, boxes = vs.panels(2, 11.5, 6.4, titles=["Mouth closed", "Mouth open, fang erected"], legend_rows=3,
                           gap=1.0)


def rot(pts, c, deg):
    a = np.radians(deg)
    R = np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])
    return (np.asarray(pts) - c) @ R.T + c


BRAINCASE = [
    ("premaxilla", vs.poly([(0.0, 1.6), (0.6, 2.2), (0.8, 1.9), (0.4, 1.4)])),
    ("nasal", vs.poly([(0.6, 2.2), (2.0, 2.45), (2.0, 2.05), (0.8, 1.9)])),
    ("frontal", vs.poly([(2.0, 2.45), (3.7, 2.65), (3.7, 1.75), (2.2, 1.85)])),
    ("parietal", vs.poly([(3.7, 2.65), (7.9, 2.85), (8.4, 2.3), (7.8, 1.65), (3.7, 1.75)])),
    ("otic_capsule", vs.poly([(7.0, 1.75), (8.4, 2.3), (8.9, 1.6), (7.3, 1.35)])),
    ("prefrontal", vs.poly([(1.7, 1.95), (2.35, 2.05), (2.3, 1.35), (1.8, 1.3)])),
    ("postorbital", vs.poly([(3.55, 2.3), (3.85, 2.3), (3.75, 1.55), (3.5, 1.65)])),
    ("supratemporal", vs.rod((7.4, 2.75), (9.4, 2.45), 0.28)),
]


def skull(x, y, open_):
    q_top = np.array([9.25, 2.45])
    q_bot = np.array([9.0, 0.25]) if open_ else np.array([9.65, 0.55])
    shift = 0.55 if open_ else 0.0
    mx = np.array([1.85, 1.05])
    if open_:
        fang = vs.rod(mx + (0.0, -0.1), mx + (0.25, -1.45), 0.16, 0.05)
        maxi = vs.oval(tuple(mx), 0.42, 0.3, angle=-60)
    else:
        fang = vs.rod(mx + (0.1, -0.15), mx + (1.25, -0.45), 0.16, 0.05)
        maxi = vs.oval(tuple(mx), 0.42, 0.3, angle=0)
    jaw = [("dentary", vs.rod((1.2, 0.2), (5.6, 0.3), 0.4, 0.3)),
           ("articular", vs.rod((5.0, 0.3), (9.75, 0.45), 0.36), {"text": ""})]
    if open_:
        jaw = [(k, (np.asarray(v) + (q_bot - np.array([9.75, 0.45]))).tolist(), *o) for (k, v, *o) in jaw]
        jaw = [(k, rot(v, q_bot, 22).tolist(), *o) for (k, v, *o) in jaw]
    parts = BRAINCASE + [
        ("quadrate", vs.rod(tuple(q_top), tuple(q_bot), 0.36)),
        ("pterygoid", vs.rod((3.5 - shift, 1.05), tuple(q_bot + (-0.25, 0.25)), 0.22)),
        ("ectopterygoid", vs.rod(tuple(mx + (0.25, -0.05)), (3.8 - shift, 0.95), 0.2)),
        ("palatine", vs.rod((2.3 - shift * 0.6, 1.3), (3.6 - shift, 1.2), 0.2)),
        ("maxilla", maxi),
        ("dentine_fang", fang, {"state": "highlight"}),
    ] + jaw
    parts = [p if p[0] != "dentine_fang" else ("maxilla", p[1], p[2]) for p in parts]
    a = vs.draw(ax, parts, at=(x, y))
    for j in (q_top, q_bot, mx + (0.0, 0.25)):
        ax.scatter([x + j[0]], [y + j[1]], s=28, facecolors=P.surface(), edgecolors=P.ink(), linewidths=0.9, zorder=30)
    return a, q_bot, mx


x, y, w, h = boxes[0]
a, qb, mx = skull(x + 0.6, y + 2.6, False)
vs.callout(ax, (x + 0.6 + 2.7, y + 2.6 + 0.6), (x + 1.5, y + 0.3), "fang folded back")
vs.callout(ax, (x + 0.6 + 9.3, y + 2.6 + 1.5), (x + 11.6, y + 5.8), "quadrate")
vs.callout(ax, (x + 0.6 + 8.4, y + 2.6 + 2.65), (x + 7.0, y + 6.2), "supratemporal")
vs.callout(ax, (x + 0.6 + 6.5, y + 2.6 + 0.72), (x + 11.6, y + 1.4), "pterygoid")
vs.callout(ax, (x + 0.6 + 7.5, y + 2.6 + 0.4), (x + 8.5, y + 0.2), "compound bone")

x, y, w, h = boxes[1]
a, qb, mx = skull(x + 0.4, y + 3.2, True)
for (p0, p1) in (((9.8, 1.6), (9.25, 1.4)), ((6.8, 0.45), (6.0, 0.58)), ((3.2, 0.5), (2.8, 0.7))):
    bio.arrow(ax, (x + 0.4 + p0[0], y + 3.2 + p0[1]), (x + 0.4 + p1[0], y + 3.2 + p1[1]), kind="process", head=0.16)
vs.callout(ax, (x + 0.4 + 2.0, y + 3.2 - 0.6), (x + 0.3, y + 0.6), "fang erected")
vs.callout(ax, (x + 0.4 + 1.85, y + 3.2 + 1.3), (x + 1.0, y + 6.2), "maxilla rotates on prefrontal")
vs.callout(ax, (x + 0.4 + 6.0, y + 3.2 - 1.2), (x + 9.5, y + 0.3), "lower jaw drops")
vs.legend(ax, ["premaxilla", "maxilla", "nasal", "frontal", "parietal", "prefrontal", "postorbital",
               "supratemporal", ("otic_capsule", "braincase (otic region)"), "palatine", "pterygoid", "ectopterygoid",
               ("quadrate", "quadrate"), "dentary", ("articular", "compound bone (articular)")],
          at=(0.4, 3 * 0.55 + 0.25), width=24.0, ncols=6)
