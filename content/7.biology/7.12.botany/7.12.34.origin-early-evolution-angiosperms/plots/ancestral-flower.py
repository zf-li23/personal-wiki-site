# A: the ancestral flower of extant angiosperms as reconstructed by Sauquet et al. (2017, Nat. Commun. 8:
# 16047), drawn as a floral diagram: bisexual and actinomorphic; more than ten undifferentiated tepals in
# three or more whorls of three; more than ten stamens, also in whorls of three; five or more free carpels
# arranged in a spiral. B, C: male and female flowers of Amborella trichopoda for comparison: tepals
# spirally arranged and undifferentiated, numerous laminar stamens in the male flower; four to six free
# carpels and one to three staminodes in the female flower.
import wikibio as bio
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(30, 12.4)
R = 3.6

bio.panel(ax, "A", (0.3, 12.1))
bio.label(ax, (5.6, 11.6), "Reconstructed ancestral flower", size="title")
plant.floral_diagram(ax, (5.6, 5.9), R, [
    dict(organ="tepal", n=3, phase=0, r=1.0, width=30),
    dict(organ="tepal", n=3, phase=60, r=0.85, width=28),
    dict(organ="tepal", n=3, phase=0, r=0.70, width=26),
    dict(organ="stamen", n=3, phase=60, r=0.57),
    dict(organ="stamen", n=3, phase=0, r=0.48),
    dict(organ="stamen", n=3, phase=60, r=0.39),
    dict(organ="stamen", n=3, phase=0, r=0.31),
    dict(organ="gynoecium", n=6, fused=False, size=0.2),
], axis=False, bract=False, symmetry="radial")
bio.label(ax, (5.6, 1.5), "Tepals 3+3+3, stamens 3+3+3+3, carpels many, free", size="small")
bio.label(ax, (5.6, 0.8), "bisexual; whorled perianth; spiral gynoecium", size="small", color=P.muted())

bio.panel(ax, "B", (11.6, 12.1))
bio.label(ax, (16.2, 11.6), r"$\it{Amborella}$, male flower", size="title")
spiral_t = [dict(organ="tepal", n=1, phase=k * 137.5, r=0.98 - 0.035 * k, width=26) for k in range(10)]
spiral_a = [dict(organ="stamen", n=1, phase=20 + k * 137.5, r=0.6 - 0.022 * k) for k in range(15)]
plant.floral_diagram(ax, (16.2, 5.9), R * 0.85, spiral_t + spiral_a, axis=True, bract=False)
bio.label(ax, (16.2, 1.5), "9-11 tepals, 12-21 laminar stamens, spiral", size="small")

bio.panel(ax, "C", (22.2, 12.1))
bio.label(ax, (26.4, 11.6), r"$\it{Amborella}$, female flower", size="title")
spiral_f = [dict(organ="tepal", n=1, phase=k * 137.5, r=0.98 - 0.04 * k, width=28) for k in range(8)]
plant.floral_diagram(ax, (26.4, 5.9), R * 0.85, spiral_f + [
    dict(organ="staminode", n=2, phase=50, r=0.62),
    dict(organ="gynoecium", n=5, fused=False, size=0.3),
], axis=True, bract=False)
bio.label(ax, (26.4, 1.5), "7-8 tepals, 1-3 staminodes, 4-6 free carpels", size="small")
