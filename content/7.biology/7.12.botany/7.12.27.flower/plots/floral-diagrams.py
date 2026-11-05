# Floral diagrams with the floral formulae in the course convention. A: lily (Lilium): two whorls of three
# tepals, two whorls of three stamens, a three-carpellate syncarpous superior ovary with axile placentation.
# B: Brassica (Brassicaceae): four sepals in two pairs, four petals in a cross, six tetradynamous stamens
# (two short outer, four long inner) and two fused carpels divided by a false septum. C: pea (Pisum
# sativum): zygomorphic, odd sepal abaxial, standard adaxial, two wings, two connate keel petals, nine
# connate stamens plus one free, one carpel. D: a wheat floret: lemma (the subtending bract, below),
# palea (above), two lodicules, three stamens and one ovary with two feathery stigmas.
import wikibio as bio
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(34.0, 10.6)
R = 2.6

bio.panel(ax, "A", (0.3, 10.4))
bio.label(ax, (4.6, 10.1), "Lilium", size="title", italic=True)
plant.floral_diagram_from_formula(ax, (4.6, 5.6), R, "* P3+3 A3+3 G_(3:3:∞)", symmetry="radial")
plant.floral_formula(ax, (4.6, 0.8), "* P3+3 A3+3 G_(3:3:∞)", style="cn")

bio.panel(ax, "B", (8.8, 10.4))
bio.label(ax, (13.1, 10.1), "Brassica", size="title", italic=True)
plant.floral_diagram(ax, (13.1, 5.6), R, [
    dict(organ="sepal", n=2, phase=0, width=40, r=0.98),
    dict(organ="sepal", n=2, phase=90, width=40, r=0.9),
    dict(organ="petal", n=4, phase=45, width=30, r=0.78),
    dict(organ="stamen", n=2, phase=90, r=0.56, size=0.11),
    dict(organ="stamen", n=2, phase=-22, r=0.44, size=0.12),
    dict(organ="stamen", n=2, phase=22, r=0.44, size=0.12),
    dict(organ="gynoecium", n=2, placentation="parietal", ovules=2, size=0.24, phase=90),
], symmetry="radial")
plant.floral_formula(ax, (13.1, 0.8), "* K2+2 C4 A2+4 G_(2:2:∞)", style="cn")

bio.panel(ax, "C", (17.3, 10.4))
bio.label(ax, (21.6, 10.1), "Pisum sativum", size="title", italic=True)
pea = plant.floral_diagram(ax, (21.6, 5.6), R, [
    dict(organ="sepal", n=5, phase=180, connate=True, width=30),
    dict(organ="petal", n=5, phase=216, r=0.74, members=[
        dict(scale=0.9, r=0.66), dict(scale=1.05, r=0.74), dict(scale=1.45, width=44, r=0.8),
        dict(scale=1.05, r=0.74), dict(scale=0.9, r=0.66)], connate=[(4, 0)]),
    dict(organ="stamen", n=10, phase=0, r=0.47, size=0.12, connate=True, free=[0]),
    dict(organ="gynoecium", n=1, placentation="marginal", phase=0, ovules=2, size=0.25),
], symmetry="bilateral")
w = pea["whorls"]
bio.callout(ax, w[1][2], (24.6, 9.4), "Standard", size="tiny")
bio.callout(ax, w[1][4], (24.9, 2.6), "Keel", size="tiny")
bio.callout(ax, w[1][3], (25.0, 6.9), "Wing", size="tiny")
plant.floral_formula(ax, (21.6, 0.8), "↑ K(5) C1+2+(2) A(9)+1 G_1:1:∞", style="cn")

bio.panel(ax, "D", (25.8, 10.4))
bio.label(ax, (30.1, 10.1), "Triticum floret", size="title", italic=False)
wh = plant.floral_diagram(ax, (30.1, 5.6), R, [
    dict(organ="sepal", n=1, phase=0, width=50, r=0.98, token="bract"),
    dict(organ="petal", n=1, phase=148, width=14, r=0.78, token="petal"),
    dict(organ="petal", n=1, phase=212, width=14, r=0.78, token="petal"),
    dict(organ="stamen", n=3, phase=180, r=0.5, size=0.13),
    dict(organ="gynoecium", n=1, placentation="basal", ovules=1, size=0.22),
], symmetry="bilateral", axis=True, bract=True)
bio.callout(ax, wh["bract"], (27.0, 1.9), "Lemma", size="tiny")
bio.callout(ax, wh["whorls"][0][0], (27.0, 9.3), "Palea", size="tiny")
bio.callout(ax, wh["whorls"][1][0], (33.6, 3.2), "Lodicules", size="tiny")
bio.callout(ax, wh["whorls"][3][0], (33.6, 7.6), "Stamens (3)", size="tiny")
bio.label(ax, (30.1, 0.8), "2 lodicules, 3 stamens, 1 ovary with 1 ovule", size="small", color=P.muted())
