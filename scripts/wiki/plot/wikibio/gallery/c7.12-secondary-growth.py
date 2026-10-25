# Secondary growth of a woody eudicot stem. (A) Transverse section of a five-year-old stem: pith and
# primary xylem in the centre, five annual rings of secondary xylem (wood; each ring pale earlywood grading
# into dense latewood; the older, inner rings form darker heartwood, the outer, conducting rings sapwood),
# rays running radially and widening (dilating) in the phloem, the vascular cambium, secondary phloem, and
# the periderm (cork cambium and cork) whose outer layers fissure as the stem widens; bark is everything
# outside the vascular cambium. (B) The same tissues at cell level in a radial strip of a ring-porous wood
# (e.g. Quercus, Fraxinus), pith on the left: cells in radial files derived from cambial initials; wide,
# large vessels open each growing season in the earlywood, cells become narrow and thick-walled in the
# latewood, and the abrupt change from latewood to the next earlywood marks the ring boundary. Rays are files
# of radially elongated parenchyma; the secondary phloem has tangential bands of fibres. (C) A softwood
# (conifer) strip: tracheids only, no vessels.
import numpy as np

import wikibio as bio
from wikibio import botany as B

P = bio.P
fig, ax = bio.canvas(29.6, 14.0)

bio.panel(ax, "A", (0.2, 13.8))
bio.label(ax, (0.85, 13.77), "Woody stem, 5 years", size="title", ha="left", va="top")
c = (5.6, 6.6)
w = B.woody_stem(ax, c, 5.0, years=5)
items = [("cork", "Cork (phellem)"), ("phellogen", "Cork cambium"), ("secondary_phloem", "Secondary phloem"),
         ("cambium", "Vascular cambium"), ("latewood", "Latewood"), ("earlywood", "Earlywood"), ("annual_ring", "Annual ring boundary"),
         ("sapwood", "Sapwood"), ("heartwood", "Heartwood"), ("primary_xylem", "Primary xylem"), ("pith", "Pith")]
pts = sorted([(n, w[k]) for k, n in items if w.get(k) is not None], key=lambda t: -float(t[1][1]))
for k, (name, p) in enumerate(pts):
    bio.callout(ax, p, (11.6, 12.4 - k * 0.78), name, size="small")
bio.callout(ax, w["ray"], (3.0, 12.3), "Ray", size="small")
bio.callout(ax, w["dilated_ray"], (4.6, 0.7), "Dilated ray (phloem)", size="small")

bio.panel(ax, "B", (14.6, 13.8))
bio.label(ax, (15.25, 13.77), "Ring-porous wood (radial strip)", size="title", ha="left", va="top")
s = B.wood_strip(ax, (15.0, 7.6, 13.6, 4.4), years=3, kind="ring-porous")
X = s["x"]
top = 12.3
for name, x0, x1 in (("Pith", *X["pith"]), ("Secondary xylem (3 rings)", *X["wood"]), ("Bark", X["cambium"][1], X["cork"][1])):
    ax.plot([x0 + 0.03, x1 - 0.03], [top, top], color=P.muted(), lw=0.9)
    bio.label(ax, ((x0 + x1) / 2, top + 0.3), name, size="small")
rx = s["ring_x"]
for k in range(3):
    bio.label(ax, ((rx[k] + rx[k + 1]) / 2, 7.25), f"year {k + 1}", size="tiny", color=P.muted())
late = (rx[1] - 0.05 * (rx[1] - rx[0]), s["latewood"][1])
ray = ((rx[1] + rx[2]) / 2, s["ray"][1])
vs = s["vessels"]
first = vs[(vs[:, 0] < rx[1]) & (vs[:, 2] > 0.8 * vs[:, 2].max())]
v1 = first[np.argmin(first[:, 1])] if len(first) else vs[0]
bio.callout(ax, v1[:2] - [0, v1[2] * 0.6], (16.4, 6.3), "Earlywood vessel", size="small")
bio.callout(ax, late, (19.2, 6.3), "Latewood", size="small")
bio.callout(ax, ray, (21.6, 6.3), "Ray", size="small")
bio.callout(ax, s["cambium"], (24.6, 6.9), "Vascular cambium", size="small")
bio.callout(ax, s["phloem_fibres"], (25.6, 6.2), "Phloem fibres", size="small")
bio.callout(ax, s["cork"], (28.3, 6.9), "Cork", size="small")

bio.panel(ax, "C", (14.6, 5.0))
bio.label(ax, (15.25, 4.97), "Softwood (tracheids only)", size="title", ha="left", va="top")
t = B.wood_strip(ax, (15.0, 0.5, 13.6, 3.6), years=3, kind="softwood")
bio.callout(ax, t["tracheid"], (23.0, 4.75), "Tracheids", size="small")
bio.callout(ax, t["ring_boundary"], (26.2, 4.75), "Ring boundary", size="small")
