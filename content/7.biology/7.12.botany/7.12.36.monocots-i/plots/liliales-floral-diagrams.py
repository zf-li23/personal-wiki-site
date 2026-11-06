# Floral diagrams and floral formulae (course convention) of families in this chapter. A: Lilium
# (Liliaceae): two whorls of three tepals, two whorls of three stamens, three fused carpels with axile
# placentation. B: Alisma (Alismataceae): sepals 3, petals 3, stamens 6, numerous free carpels in one
# ring. C: Hydrocharitaceae, female flower: sepals 3, petals 3, inferior ovary with parietal placentas.
# D: Dioscorea, female flower: six tepals connate at the base, three staminodes, three locules with two
# ovules each (ovary inferior). E: Smilax, male flower: tepals 3 + 3, stamens 3 + 3.
# F: Paris (Melanthiaceae): sepals and petals 5 each (4-10 in the genus), stamens twice as many, ovary
# with 5 locules.
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


T6 = [dict(organ="tepal", n=3, phase=180, keel=0.3, width=50), dict(organ="tepal", n=3, width=46)]

head(0, "A", r"$\it{Lilium}$")
plant.floral_diagram(ax, (XS[0], Y), R, T6 + [dict(organ="stamen", n=3), dict(organ="stamen", n=3),
    dict(organ="gynoecium", n=3, placentation="axile", ovules=2, size=0.3)], symmetry="radial")
plant.floral_formula(ax, (XS[0], 1.6), "* P3+3 A3+3 G_(3:3:∞)", style="cn", size="normal")

head(1, "B", r"$\it{Alisma}$")
plant.floral_diagram(ax, (XS[1], Y), R, [
    dict(organ="sepal", n=3, phase=180, width=48), dict(organ="petal", n=3, width=46),
    dict(organ="stamen", n=6, phase=30),
    dict(organ="gynoecium", n=12, fused=False, rings=[(0.3, 12, 0)], size=0.36)], symmetry="radial")
plant.floral_formula(ax, (XS[1], 1.6), "* K3 C3 A6 G_∞", style="cn", size="normal")

head(2, "C", "Hydrocharitaceae ♀")
plant.floral_diagram(ax, (XS[2], Y), R, [
    dict(organ="sepal", n=3, phase=180, width=48), dict(organ="petal", n=3, width=46),
    dict(organ="gynoecium", n=6, placentation="parietal", ovules=3, size=0.36)], symmetry="radial")
plant.floral_formula(ax, (XS[2], 1.6), "* K3 C3 G^(6:1:∞)", style="cn", size="normal")

head(3, "D", r"$\it{Dioscorea}$ ♀")
plant.floral_diagram(ax, (XS[3], Y), R, [
    dict(organ="tepal", n=3, phase=180, width=52, connate=True), dict(organ="tepal", n=3, width=48),
    dict(organ="staminode", n=3),
    dict(organ="gynoecium", n=3, placentation="axile", ovules=2, size=0.32)], symmetry="radial")
plant.floral_formula(ax, (XS[3], 1.6), "* P(3+3) G^(3:3:2)", style="cn", size="normal")

head(4, "E", r"$\it{Smilax}$ ♂")
plant.floral_diagram(ax, (XS[4], Y), R, T6 + [dict(organ="stamen", n=3), dict(organ="stamen", n=3)],
                     symmetry="radial")
plant.floral_formula(ax, (XS[4], 1.6), "* P3+3 A3+3", style="cn", size="normal")

head(5, "F", r"$\it{Paris}$")
plant.floral_diagram(ax, (XS[5], Y), R, [
    dict(organ="sepal", n=5, phase=180, width=30), dict(organ="petal", n=5, width=10, thickness=0.1),
    dict(organ="stamen", n=5), dict(organ="stamen", n=5),
    dict(organ="gynoecium", n=5, placentation="axile", ovules=2, size=0.3)], axis=False, bract=False,
    symmetry="radial")
plant.floral_formula(ax, (XS[5], 1.6), "* K5 C5 A5+5 G_(5:5:∞)", style="cn", size="normal")
