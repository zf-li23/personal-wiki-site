# Floral diagrams and floral formulae (course convention) in Asparagales, drawn for the resupinate orchid
# flower (labellum towards the bract). A: Neuwiedia (Apostasioideae), three fertile stamens: the median
# outer one and the two lateral inner ones. B: Cypripedium (Cypripedioideae), two fertile lateral inner
# stamens; the median outer stamen is a shield-shaped staminode. C: Orchidoideae and Epidendroideae, a
# single fertile median outer stamen; lateral inner stamens reduced to staminodes or lost. All three:
# ovary of three carpels, one locule, parietal placentation. D: Iris, three outer stamens, inferior
# three-locular ovary. E: Allium, six stamens, superior three-locular ovary with two ovules per locule.
# F: Lycoris, six stamens, inferior three-locular ovary.
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


def orchid(i, fertile, staminodes):
    outer = dict(organ="tepal", n=3, phase=0, width=40, keel=0.3)
    inner = dict(organ="tepal", n=3, phase=60, width=36,
                 members=[{}, dict(scale=1.45, token="highlight"), {}])
    wh = [outer, inner]
    if fertile:
        wh.append(dict(organ="stamen", n=len(fertile), members=[dict(angle=a) for a in fertile], r=0.52))
    if staminodes:
        wh.append(dict(organ="staminode", n=len(staminodes), members=[dict(angle=a, scale=1.6) for a in staminodes], r=0.5))
    wh.append(dict(organ="gynoecium", n=3, placentation="parietal", ovules=3, size=0.3, phase=0))
    out = plant.floral_diagram(ax, (XS[i], Y), R, wh, symmetry="bilateral")
    return out


head(0, "A", r"$\it{Neuwiedia}$")
orchid(0, [0, 60, 300], [])
plant.floral_formula(ax, (XS[0], 1.6), "↑ P3+3 A3 G^(3:1:∞)", style="cn", size="normal")
head(1, "B", r"$\it{Cypripedium}$")
orchid(1, [60, 300], [0])
plant.floral_formula(ax, (XS[1], 1.6), "↑ P3+3 A2 G^(3:1:∞)", style="cn", size="normal")
head(2, "C", "Orchidoideae")
o = orchid(2, [0], [60, 300])
plant.floral_formula(ax, (XS[2], 1.6), "↑ P3+3 A1 G^(3:1:∞)", style="cn", size="normal")
bio.callout(ax, o["whorls"][1][1], (XS[2] + 1.6, 2.9), "Labellum", size="tiny")

head(3, "D", r"$\it{Iris}$")
plant.floral_diagram(ax, (XS[3], Y), R, [
    dict(organ="tepal", n=3, phase=180, width=50), dict(organ="tepal", n=3, width=40),
    dict(organ="stamen", n=3, phase=180, r=0.6),
    dict(organ="gynoecium", n=3, placentation="axile", ovules=2, size=0.3)], symmetry="radial")
plant.floral_formula(ax, (XS[3], 1.6), "* P3+3 A3 G^(3:3:∞)", style="cn", size="normal")

head(4, "E", r"$\it{Allium}$")
plant.floral_diagram(ax, (XS[4], Y), R, [
    dict(organ="tepal", n=3, phase=180, width=46), dict(organ="tepal", n=3, width=44),
    dict(organ="stamen", n=3), dict(organ="stamen", n=3),
    dict(organ="gynoecium", n=3, placentation="axile", ovules=2, size=0.3)], symmetry="radial")
plant.floral_formula(ax, (XS[4], 1.6), "* P3+3 A3+3 G_(3:3:2)", style="cn", size="normal")

head(5, "F", r"$\it{Lycoris}$")
plant.floral_diagram(ax, (XS[5], Y), R, [
    dict(organ="tepal", n=3, phase=180, width=46, connate=True), dict(organ="tepal", n=3, width=44),
    dict(organ="stamen", n=3), dict(organ="stamen", n=3),
    dict(organ="gynoecium", n=3, placentation="axile", ovules=3, size=0.3)], symmetry="radial")
plant.floral_formula(ax, (XS[5], 1.6), "* P(3+3) A3+3 G^(3:3:∞)", style="cn", size="normal")
