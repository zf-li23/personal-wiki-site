# Floral diagram and formula of a lily (Lilium, Liliaceae): a trimerous monocot flower with two whorls
# of free tepals, two whorls of stamens and a superior ovary of three fused carpels with axile
# placentation. Each whorl alternates with the next; the outer tepal whorl has its median member
# abaxial (towards the bract), as in most monocots.
import wikibio as bio
from wikibio import plant

fig, ax = bio.canvas(14, 11)
c = (6.0, 6.0)
out = plant.floral_diagram(ax, c, 3.2, [
    dict(organ="tepal", n=3, phase=180, keel=0.35, width=52),
    dict(organ="tepal", n=3, width=48),
    dict(organ="stamen", n=3),
    dict(organ="stamen", n=3),
    dict(organ="gynoecium", n=3, placentation="axile", ovules=2, size=0.3),
], symmetry="radial")

w = out["whorls"]  # members in order of their angle, clockwise from the axis side
bio.callout(ax, w[0][1], (1.0, 8.6), "Outer tepal")
bio.callout(ax, w[1][1], (11.0, 9.4), "Inner tepal")
bio.callout(ax, w[2][1], (11.0, 7.7), "Stamen (outer whorl)")
bio.callout(ax, (c[0] + 0.5, c[1] + 0.05), (11.0, 6.0), "Ovary: 3 fused carpels,\naxile placentation")
bio.callout(ax, w[3][1], (11.0, 4.2), "Stamen (inner whorl)")
bio.callout(ax, out["axis"], (1.0, 10.3), "Axis")
bio.callout(ax, out["bract"], (1.0, 1.4), "Bract")
plant.floral_formula(ax, (6.0, 0.35), "* P3+3 A3+3 G_(3)")
