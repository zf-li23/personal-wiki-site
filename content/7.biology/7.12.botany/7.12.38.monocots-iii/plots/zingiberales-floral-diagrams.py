# Floral diagrams of Zingiberales and Commelina (schematic; positions after Kress 1990). Petaloid
# staminodes are drawn as orange crescents inside the perianth, small staminodes as dots; the dashed line
# is the plane of symmetry. A: Musa, a compound tepal (three outer and two inner tepals connate) and one
# free inner tepal; five fertile stamens, the adaxial inner one a small staminode. B: Strelitzia, sepals
# 3, petals 3 (two connate into the arrow-shaped organ), five fertile stamens. C: Canna, a single
# fertile stamen with one theca (half anther), the other members petaloid staminodes. D: Zingiber, calyx
# and corolla tubular, one fertile stamen (inner adaxial), labellum of two connate inner staminodes, two
# small lateral staminodes (outer). E: Costus, labellum of five connate staminodes, one fertile stamen.
# F: Commelina, sepals 3, petals 3, three fertile stamens and three staminodes.
import wikibio as bio
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(36, 12.4)
R = 2.5
XS = [3.4, 9.4, 15.4, 21.4, 27.4, 33.0]
Y = 6.6


def head(i, letter, name):
    bio.panel(ax, letter, (XS[i] - 3.1, 12.2))
    bio.label(ax, (XS[i], 11.7), name, size="title")


def flower(i, peri, inner, ovary=True):
    wh = peri + inner
    if ovary:
        wh.append(dict(organ="gynoecium", n=3, placentation="axile", ovules=2, size=0.26))
    plant.floral_diagram(ax, (XS[i], Y), R, wh, symmetry="bilateral")


SEP = dict(organ="sepal", n=3, phase=180, width=46)
PET = dict(organ="petal", n=3, phase=0, width=44)

head(0, "A", r"$\it{Musa}$")
flower(0, [dict(organ="tepal", n=5, phase=180, members=[dict(angle=a) for a in (180, 300, 60, 240, 120)],
                width=40, connate=True), dict(organ="tepal", n=1, phase=0, width=34, r=0.8)],
       [dict(organ="stamen", n=5, members=[dict(angle=a) for a in (180, 300, 60, 120, 240)], r=0.56),
        dict(organ="staminode", n=1, phase=0, r=0.52)])
plant.floral_formula(ax, (XS[0], 1.6), "↑ P(3+2)+1 A5 G^(3:3:∞)", style="cn", size="normal")

head(1, "B", r"$\it{Strelitzia}$")
flower(1, [SEP, dict(organ="petal", n=3, phase=0, width=40, connate=[(1, 2)])],
       [dict(organ="stamen", n=5, members=[dict(angle=a) for a in (180, 300, 60, 120, 240)], r=0.56)])
plant.floral_formula(ax, (XS[1], 1.6), "↑ K3 C1+(2) A5 G^(3:3:∞)", style="cn", size="normal")

head(2, "C", r"$\it{Canna}$")
flower(2, [SEP, PET],
       [dict(organ="tepal", n=3, token="atp", members=[dict(angle=a) for a in (120, 180, 240)], width=34, r=0.58),
        dict(organ="tepal", n=1, token="atp", members=[dict(angle=300)], width=26, r=0.58),
        dict(organ="stamen", n=1, members=[dict(angle=40, scale=0.75)], r=0.56)])
plant.floral_formula(ax, (XS[2], 1.6), "↑ K3 C(3) A½ G^(3:3:∞)", style="cn", size="normal")

head(3, "D", r"$\it{Zingiber}$")
flower(3, [dict(SEP, connate=True), dict(PET, connate=True)],
       [dict(organ="tepal", n=1, token="atp", members=[dict(angle=180)], width=74, r=0.6),
        dict(organ="staminode", n=2, members=[dict(angle=60, scale=1.6), dict(angle=300, scale=1.6)], r=0.56),
        dict(organ="stamen", n=1, phase=0, r=0.55)])
plant.floral_formula(ax, (XS[3], 1.6), "↑ K(3) C(3) A1 G^(3:3:∞)", style="cn", size="normal")

head(4, "E", r"$\it{Costus}$")
flower(4, [dict(SEP, connate=True), dict(PET, connate=True)],
       [dict(organ="tepal", n=1, token="atp", members=[dict(angle=180)], width=150, r=0.6),
        dict(organ="stamen", n=1, phase=0, r=0.55)])
plant.floral_formula(ax, (XS[4], 1.6), "↑ K(3) C(3) A1 G^(3:3:∞)", style="cn", size="normal")

head(5, "F", r"$\it{Commelina}$")
plant.floral_diagram(ax, (XS[5], Y), R, [
    dict(organ="sepal", n=3, phase=180, width=44),
    dict(organ="petal", n=3, phase=0, width=48, members=[dict(scale=0.6), dict(scale=1.15), dict(scale=1.15)]),
    dict(organ="stamen", n=3, members=[dict(angle=a) for a in (180, 120, 240)], r=0.56),
    dict(organ="staminode", n=3, members=[dict(angle=a, scale=1.8) for a in (0, 60, 300)], r=0.56),
    dict(organ="gynoecium", n=3, placentation="axile", ovules=1, size=0.26)], symmetry="bilateral")
plant.floral_formula(ax, (XS[5], 1.6), "↑ K3 C3 A3 G_(3:3)", style="cn", size="normal")
