# Upper-jaw protrusion in a spiny-finned teleost, schematic lateral views (anterior to the left).
# (A) Mouth closed. (B) Mouth open: the lower jaw (dentary, articular) rotates down about the quadrate; a
# ligament from the lower jaw swings the maxilla forward, and the maxilla pushes the premaxilla, whose
# ascending process slides forward along the snout, so the upper jaw protrudes and the gape becomes a
# tube. Colours follow the course-wide homology scheme. Not to scale.
import numpy as np
import wikibio as bio
import vertskel as vs

P = bio.P
fig, ax, boxes = vs.panels(2, 10.0, 6.4, titles=["A  Mouth closed", "B  Mouth open, upper jaw protruded"],
                           ncols=2, legend_rows=1)


def rot(pts, c, deg):
    a = np.radians(deg)
    R = np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])
    return (np.asarray(pts) - c) @ R.T + c


skull = vs.smooth([(3.0, 4.1), (4.5, 5.4), (7.5, 5.8), (9.6, 5.2), (9.6, 3.2), (7.0, 2.9), (4.5, 3.4)])
quad_c = np.array([6.6, 2.4])
quadrate = vs.poly([(6.2, 3.3), (7.0, 3.3), (6.9, 2.3), (6.3, 2.2)])
lower = [(2.2, 2.2), (4.5, 2.4), (6.6, 2.5), (6.8, 2.1), (4.5, 1.6), (2.2, 1.9)]
artic = [(5.6, 2.45), (6.8, 2.5), (6.8, 2.05), (5.6, 1.85)]
pmx_closed = [(2.0, 2.9), (2.3, 3.2), (3.2, 4.3), (3.5, 4.1), (2.7, 2.95), (3.6, 2.7), (3.5, 2.5), (2.1, 2.6)]
mx_closed = [(2.6, 3.0), (3.0, 3.4), (4.8, 2.9), (4.7, 2.6)]

for k, (x, y, w, h) in enumerate(boxes):
    if k == 0:
        lo, ar, pmx, mx = lower, artic, pmx_closed, mx_closed
    else:
        lo = rot(lower, quad_c, 32)
        ar = rot(artic, quad_c, 32)
        pmx = np.asarray(pmx_closed) + np.array([-1.0, -0.55])
        mx = rot(np.asarray(mx_closed) + np.array([-0.7, -0.35]), np.array([4.3, 2.6]), 25)
    parts = [("chondrocranium", skull, {"state": "context"}),
             ("quadrate", quadrate),
             ("dentary", vs.smooth(lo)),
             ("articular", vs.poly(ar)),
             ("maxilla", vs.poly(mx)),
             ("premaxilla", vs.poly(pmx))]
    a = vs.draw(ax, parts, at=(x, y))
    vs.callout(ax, a["premaxilla"], (x + 0.6, y + 5.6), "premaxilla")
    vs.callout(ax, a["maxilla"], (x + 3.4, y + 0.5) if k else (x + 4.6, y + 4.2), "maxilla")
    vs.callout(ax, a["dentary"], (x + 1.0, y + 0.4) if k == 0 else (x + 6.5, y + 0.4), "dentary")
    vs.callout(ax, a["quadrate"], (x + 8.6, y + 1.6), "quadrate")
    if k == 1:
        bio.arrow(ax, (x + 2.9, y + 4.9), (x + 1.9, y + 4.35), kind="process")
        bio.label(ax, (x + 3.0, y + 5.15), "protrusion", size="tiny", ha="left")
vs.legend(ax, ["premaxilla", "maxilla", "dentary", ("articular", "articular"), ("quadrate", "quadrate")],
          at=(0.5, 1.0), width=20.0, ncols=5)
