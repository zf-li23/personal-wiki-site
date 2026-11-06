# Floral diagrams and floral formulae (course convention) of four Ranunculaceae. A: Ranunculus, sepals 5,
# petals 5 (nectar leaves with a basal nectary pit), stamens and carpels many, free, spiral; aggregate of
# achenes. B: Aquilegia, sepals 5 (petaloid), 5 long-spurred petals, many stamens with an inner whorl of
# staminodes, 5 carpels (follicles). C: Aconitum, zygomorphic: the adaxial sepal is a helmet that hides two
# long-clawed, spurred nectar leaves; many stamens; 3 carpels. D: Clematis, 4 petaloid valvate sepals, no
# petals, stamens and carpels many.
import wikibio as bio
from wikibio import plant

fig, ax = bio.canvas(32, 12.4)
R = 2.7
XS = [4.0, 12.0, 20.0, 28.0]
Y = 6.6


def head(i, letter, name):
    bio.panel(ax, letter, (XS[i] - 3.6, 12.2))
    bio.label(ax, (XS[i], 11.7), name, size="title", italic=True)


head(0, "A", "Ranunculus")
plant.floral_diagram(ax, (XS[0], Y), R, [
    dict(organ="sepal", n=5, phase=0, width=30),
    dict(organ="petal", n=5, width=32),
    dict(organ="stamen", n=12, r=0.58, phase=6), dict(organ="stamen", n=12, r=0.48, phase=21),
    dict(organ="gynoecium", n=12, fused=False, size=0.3, carpel_size=0.07)], symmetry="radial")
plant.floral_formula(ax, (XS[0], 1.5), "* K5 C5 A∞ G_∞:1:1", style="cn", size="normal")

head(1, "B", "Aquilegia")
plant.floral_diagram(ax, (XS[1], Y), R, [
    dict(organ="sepal", n=5, phase=0, width=30, token="petal"),
    dict(organ="petal", n=5, width=30),
    dict(organ="stamen", n=10, r=0.56), dict(organ="stamen", n=10, r=0.47, phase=18),
    dict(organ="staminode", n=10, r=0.38),
    dict(organ="gynoecium", n=5, fused=False, size=0.2)], symmetry="radial")
plant.floral_formula(ax, (XS[1], 1.5), "* K5 C5 A∞ G_5:1:∞", style="cn", size="normal")
bio.label(ax, (XS[1], 2.6), "petals with long spurs", size="small", color=bio.P.muted())

head(2, "C", "Aconitum")
plant.floral_diagram(ax, (XS[2], Y), R, [
    dict(organ="sepal", n=5, phase=0, width=28, token="petal",
         members=[dict(scale=1.5, width=50), dict(), dict(), dict(), dict()]),
    dict(organ="stamen", n=10, r=0.55, phase=10), dict(organ="stamen", n=10, r=0.45, phase=28),
    dict(organ="gynoecium", n=3, fused=False, size=0.18)], symmetry="bilateral")
for d in (-24, 24):
    plant.crescent(ax, (XS[2], Y), 0.74 * R, d, 11, 0.1 * R, token="petal")
plant.floral_formula(ax, (XS[2], 1.5), "↑ K5 C2 A∞ G_3:1:∞", style="cn", size="normal")
bio.label(ax, (XS[2], 2.6), "helmet (adaxial sepal) hides 2 nectar leaves", size="small", color=bio.P.muted())

head(3, "D", "Clematis")
plant.floral_diagram(ax, (XS[3], Y), R, [
    dict(organ="sepal", n=4, phase=45, width=42, token="petal"),
    dict(organ="stamen", n=12, r=0.6, phase=0), dict(organ="stamen", n=12, r=0.5, phase=15),
    dict(organ="gynoecium", n=10, fused=False, size=0.3, carpel_size=0.07)], symmetry="radial")
plant.floral_formula(ax, (XS[3], 1.5), "* K4 C0 A∞ G_∞:1:1", style="cn", size="normal")
bio.label(ax, (XS[3], 2.6), "petaloid valvate sepals, no petals", size="small", color=bio.P.muted())
