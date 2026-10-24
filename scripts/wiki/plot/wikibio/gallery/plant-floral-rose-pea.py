# Floral diagrams of two eudicots. (A) Rose (Rosa, Rosaceae): actinomorphic and perigynous, five
# sepals, five petals and many stamens on the rim of a floral cup (hypanthium, dashed), many free
# carpels. (B) Pea (Pisum sativum, Fabaceae): zygomorphic papilionaceous flower with the odd sepal
# abaxial, a large adaxial standard, two lateral wings and two connate keel petals, ten diadelphous
# stamens (nine connate, the adaxial vexillary stamen free) and one carpel with marginal placentation.
import wikibio as bio
from wikibio import plant

fig, ax = bio.canvas(24, 12)

bio.panel(ax, "A", (0.3, 11.7))
bio.label(ax, (6.0, 11.5), "Rosa", size="title", italic=True)
c = (6.0, 6.2)
rose = plant.floral_diagram(ax, c, 3.0, [
    dict(organ="sepal", n=5, phase=0, width=33),
    dict(organ="petal", n=5, width=34),
    dict(organ="stamen", n=13, r=0.6, size=0.11, phase=8),
    dict(organ="stamen", n=13, r=0.48, size=0.1, phase=22),
    dict(organ="gynoecium", n=14, fused=False, size=0.34, carpel_size=0.075),
], symmetry="radial", hypanthium=0.69)
plant.floral_formula(ax, (6.0, 0.6), "* K5 C5 A∞ G_∞")

bio.panel(ax, "B", (12.3, 11.7))
bio.label(ax, (18.0, 11.5), "Pisum sativum", size="title", italic=True)
c2 = (18.0, 6.2)
# petals: phase 216 puts member 0 at the lower right; members 0..4 = keel, wing, standard, wing, keel
pea = plant.floral_diagram(ax, c2, 3.0, [
    dict(organ="sepal", n=5, phase=180, connate=True, width=30),
    dict(organ="petal", n=5, phase=216, r=0.74, members=[
        dict(scale=0.9, r=0.66), dict(scale=1.05, r=0.74), dict(scale=1.45, width=44, r=0.8),
        dict(scale=1.05, r=0.74), dict(scale=0.9, r=0.66)], connate=[(4, 0)]),
    dict(organ="stamen", n=10, phase=0, r=0.47, size=0.12, connate=True, free=[0]),
    dict(organ="gynoecium", n=1, placentation="marginal", phase=0, ovules=2, size=0.25),
], symmetry="bilateral", bracteoles=False)
w = pea["whorls"]
bio.callout(ax, w[1][2], (22.2, 10.4), "Standard")
bio.callout(ax, w[1][3], (22.2, 7.6), "Wing")
bio.callout(ax, w[1][4], (22.2, 3.2), "Keel (2 connate petals)")
bio.callout(ax, w[2][0], (13.4, 8.4), "Vexillary stamen (free)")
bio.callout(ax, w[2][6], (13.4, 2.6), "Stamen tube (9 connate)")
bio.callout(ax, w[0][2], (13.4, 10.2), "Calyx (5 connate sepals)")
plant.floral_formula(ax, (18.0, 0.6), "↑ K(5) C1+2+(2) A(9)+1 G_1")
