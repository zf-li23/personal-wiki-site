# Floral diagram of Camellia (Theaceae): bracteoles grading into sepals (spiral, dashed outline marks
# the bracteoles), five imbricate petals, numerous stamens in several whorls, the outer filaments
# connate in bundles and adnate to the petal bases (arcs), inner ones free; superior ovary of three
# fused carpels, axile placentation.
import wikibio as bio
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(16, 15)
plant.floral_diagram(ax, (8.0, 8.4), 4.6, [
    dict(organ="sepal", n=5, phase=0, r=1.04, width=30),
    dict(organ="petal", n=5, phase=36, r=0.88, width=34),
    dict(organ="stamen", n=10, phase=18, r=0.72, adnate=True, connate=True, size=0.13),
    dict(organ="stamen", n=10, phase=0, r=0.6, size=0.12),
    dict(organ="stamen", n=8, phase=10, r=0.49, size=0.11),
    dict(organ="gynoecium", n=3, placentation="axile", ovules=3, size=0.28)],
    bracteoles=True, symmetry="radial")
plant.floral_formula(ax, (8.0, 1.0), "* K5 C5 A∞ G_(3:3:∞)", style="cn")
bio.label(ax, (8.0, 14.6), "Camellia", italic=True, size="title")
