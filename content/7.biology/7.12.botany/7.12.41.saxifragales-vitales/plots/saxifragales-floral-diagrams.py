# Floral diagrams and formulae (course convention) of Saxifragales and Vitales. A: Paeonia, sepals 5,
# petals 5-10, stamens many (centrifugal), a disc (dashed) around 2-5 free carpels. B: Hamamelis,
# tetramerous, calyx connate and adnate to the ovary, 4 strap-shaped petals, 4 fertile stamens alternating
# with 4 scale-like staminodes, half-inferior bicarpellate ovary with one ovule per locule. C: Saxifraga,
# perigynous (floral cup dashed), sepals 5, petals 5, stamens 10, two carpels fused below. D: Sedum,
# pentamerous, stamens 5 + 5, five free carpels. E: Vitis, calyx tiny and connate, 5 petals, 5 stamens
# opposite the petals, an intrastaminal disc, ovary of 2 locules with 2 ovules each.
import wikibio as bio
from wikibio import plant

fig, ax = bio.canvas(38, 12.4)
R = 2.5
XS = [3.6, 11.2, 18.8, 26.4, 34.0]
Y = 6.6


def head(i, letter, name):
    bio.panel(ax, letter, (XS[i] - 3.3, 12.2))
    bio.label(ax, (XS[i], 11.7), name, size="title", italic=True)


head(0, "A", "Paeonia")
plant.floral_diagram(ax, (XS[0], Y), R, [
    dict(organ="sepal", n=5, phase=0, width=30), dict(organ="petal", n=8, width=24),
    dict(organ="stamen", n=12, r=0.6), dict(organ="stamen", n=12, r=0.5, phase=15),
    dict(organ="gynoecium", n=3, fused=False, size=0.22)], symmetry="radial", hypanthium=0.38)
plant.floral_formula(ax, (XS[0], 1.5), "* K5 C5-10 A∞ G_2-5:1:∞", style="cn", size="normal")

head(1, "B", "Hamamelis")
plant.floral_diagram(ax, (XS[1], Y), R, [
    dict(organ="sepal", n=4, phase=45, width=40, connate=True), dict(organ="petal", n=4, width=12),
    dict(organ="stamen", n=4, r=0.55), dict(organ="staminode", n=4, r=0.55),
    dict(organ="gynoecium", n=2, placentation="axile", ovules=1, size=0.25)], symmetry="radial")
plant.floral_formula(ax, (XS[1], 1.5), "* K(4) C4 A4 G^(2:2:1)", style="cn", size="normal")
bio.label(ax, (XS[1], 2.6), "ovary half-inferior; 4 staminodes", size="small", color=bio.P.muted())

head(2, "C", "Saxifraga")
plant.floral_diagram(ax, (XS[2], Y), R, [
    dict(organ="sepal", n=5, phase=0, width=30), dict(organ="petal", n=5, width=26),
    dict(organ="stamen", n=5, r=0.6), dict(organ="stamen", n=5, r=0.5),
    dict(organ="gynoecium", n=2, placentation="axile", ovules=4, size=0.28)], symmetry="radial", hypanthium=0.68)
plant.floral_formula(ax, (XS[2], 1.5), "* K5 C5 A5+5 G^(2:2:∞)", style="cn", size="normal")
bio.label(ax, (XS[2], 2.6), "perigynous; styles 2, free", size="small", color=bio.P.muted())

head(3, "D", "Sedum")
plant.floral_diagram(ax, (XS[3], Y), R, [
    dict(organ="sepal", n=5, phase=0, width=30), dict(organ="petal", n=5, width=28),
    dict(organ="stamen", n=5, r=0.62), dict(organ="stamen", n=5, r=0.52),
    dict(organ="gynoecium", n=5, fused=False, size=0.28)], symmetry="radial")
plant.floral_formula(ax, (XS[3], 1.5), "* K5 C5 A5+5 G_5:1:∞", style="cn", size="normal")

head(4, "E", "Vitis")
plant.floral_diagram(ax, (XS[4], Y), R, [
    dict(organ="sepal", n=5, phase=0, width=34, connate=True, thickness=0.06),
    dict(organ="petal", n=5, width=32, r=0.8),
    dict(organ="stamen", n=5, phase=36, r=0.56),
    dict(organ="gynoecium", n=2, placentation="axile", ovules=2, size=0.26)], symmetry="radial", hypanthium=0.4)
plant.floral_formula(ax, (XS[4], 1.5), "* K(5) C5 A5 G_(2:2:2)", style="cn", size="normal")
bio.label(ax, (XS[4], 2.6), "stamens opposite petals; disc (dashed)", size="small", color=bio.P.muted())
