# Floral diagrams and floral formulae (course convention) of magnoliids and Chloranthales. A: Magnoliaceae
# (Magnolia grandiflora): tepals in three whorls of three, stamens and carpels numerous, free, spiral.
# B: Annonaceae: sepals 3, petals 3 + 3, stamens numerous, carpels numerous and free. C: Lauraceae
# (Cinnamomum): tepals 3 + 3, stamens in four whorls of three (fourth whorl staminodes), one carpel.
# D: Aristolochia: zygomorphic, perianth a single connate tube, six stamens adnate to the style, inferior
# six-locular ovary. E: Piper: naked flower in the axil of a bract, two stamens, ovary of three fused
# carpels with one basal ovule. F: Chloranthus: naked flower, a three-lobed stamen on one side of the
# single carpel.
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


head(0, "A", "Magnoliaceae")
plant.floral_diagram(ax, (XS[0], Y), R, [
    dict(organ="tepal", n=3, phase=0, r=1.0, width=34), dict(organ="tepal", n=3, phase=60, r=0.86, width=30),
    dict(organ="tepal", n=3, phase=0, r=0.72, width=28),
    dict(organ="stamen", n=8, phase=0, r=0.57), dict(organ="stamen", n=8, phase=22, r=0.47),
    dict(organ="gynoecium", n=8, fused=False, size=0.22)], axis=False, bract=False, symmetry="radial")
plant.floral_formula(ax, (XS[0], 1.6), "* P3+3+3 A∞ G_∞:1:2", style="cn", size="normal")

head(1, "B", "Annonaceae")
plant.floral_diagram(ax, (XS[1], Y), R, [
    dict(organ="sepal", n=3, phase=0, r=1.0, width=34), dict(organ="petal", n=3, phase=60, r=0.86, width=32),
    dict(organ="petal", n=3, phase=0, r=0.72, width=30),
    dict(organ="stamen", n=9, phase=0, r=0.56), dict(organ="stamen", n=9, phase=20, r=0.46),
    dict(organ="gynoecium", n=7, fused=False, size=0.22)], symmetry="radial")
plant.floral_formula(ax, (XS[1], 1.6), "* K3 C3+3 A∞ G_∞", style="cn", size="normal")

head(2, "C", "Lauraceae")
plant.floral_diagram(ax, (XS[2], Y), R, [
    dict(organ="tepal", n=3, phase=0, r=1.0, width=32), dict(organ="tepal", n=3, phase=60, r=0.85, width=30),
    dict(organ="stamen", n=3, phase=0, r=0.68), dict(organ="stamen", n=3, phase=60, r=0.56),
    dict(organ="stamen", n=3, phase=0, r=0.44), dict(organ="staminode", n=3, phase=60, r=0.33),
    dict(organ="gynoecium", n=1, placentation="basal", ovules=1, size=0.2)], symmetry="radial")
plant.floral_formula(ax, (XS[2], 1.6), "* P3+3 A3+3+3+3 G_1:1:1", style="cn", size="normal")

head(3, "D", r"$\it{Aristolochia}$")
plant.floral_diagram(ax, (XS[3], Y), R, [
    dict(organ="tepal", n=3, phase=0, r=0.95, width=58, connate=True),
    dict(organ="stamen", n=6, phase=30, r=0.55),
    dict(organ="gynoecium", n=6, placentation="axile", ovules=2, size=0.32)], symmetry="bilateral")
plant.floral_formula(ax, (XS[3], 1.6), "↑ P(3) A6 G^(6:6:∞)", style="cn", size="normal")

head(4, "E", r"$\it{Piper}$")
plant.floral_diagram(ax, (XS[4], Y), R, [
    dict(organ="stamen", n=2, phase=90, r=0.55),
    dict(organ="gynoecium", n=3, placentation="basal", ovules=1, size=0.3)], symmetry=None)
plant.floral_formula(ax, (XS[4], 1.6), "P0 A2 G_(3:1:1)", style="cn", size="normal")

head(5, "F", r"$\it{Chloranthus}$")
plant.floral_diagram(ax, (XS[5], Y), R, [
    dict(organ="stamen", n=3, phase=150, r=0.55, connate=True, members=[dict(r=0.55), dict(r=0.62), dict(r=0.55)]),
    dict(organ="gynoecium", n=1, placentation="basal", ovules=1, size=0.25)], symmetry=None)
plant.floral_formula(ax, (XS[5], 1.6), "P0 A(3) G1:1:1", style="cn", size="normal")
