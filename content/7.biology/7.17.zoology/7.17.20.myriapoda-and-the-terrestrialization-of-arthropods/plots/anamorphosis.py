# Postembryonic addition of legs in myriapods: number of leg pairs at successive stadia (stadium 1 = first
# free-living stage). Anamorphic centipedes: Scutigera coleoptrata (4, 5, 7, 9, 11, 13, 15), Lithobius forficatus
# (7, 8, 10, 12, 15), Craterostigmus (12, 15); epimorphic Scolopendra (21 from hatching). Symphyla
# (Scutigerella: 6 pairs at hatching, one added per moult to 12) and Pauropoda (3, 5, 6, 8, 9). Counts after
# Lewis (1981) and Brusca et al. (2023); after the last addition, moults continue without new legs.
import wikibio as bio
from wikibio import quant

P = bio.P
SERIES = [
    ("Scolopendra", "negative", [21, 21, 21, 21, 21, 21, 21]),
    ("Craterostigmus", "protein", [12, 15, 15, 15]),
    ("Scutigera", "dna", [4, 5, 7, 9, 11, 13, 15, 15]),
    ("Lithobius", "enzyme", [7, 8, 10, 12, 15, 15, 15]),
    ("Scutigerella", "rna", [6, 7, 8, 9, 10, 11, 12, 12]),
    ("Pauropus", "atp", [3, 5, 6, 8, 9, 9]),
]
fig, ax = bio.canvas(16, 9.6)
p = quant.Plot(ax, (2.0, 1.5, 9.4, 7.4), xlim=(1, 8), ylim=(0, 23), xlabel="Stadium", ylabel="Leg pairs",
               xticks=[1, 2, 3, 4, 5, 6, 7, 8], yticks=[0, 5, 10, 15, 20])
dy = {"Scutigera": 0.0, "Lithobius": -0.7, "Craterostigmus": 0.7}
for name, tok, legs in SERIES:
    xs = list(range(1, len(legs) + 1))
    p.steps(xs + [xs[-1] + 0.4], legs + [legs[-1]], token=tok, lw=1.6)
    p.points(xs, legs, token=tok, r=0.08)
    yl = legs[-1] + dy.get(name, 0.0)
    bio.label(ax, (p.X(xs[-1] + 0.5), p.Y(yl)), name, size="tiny", ha="left", color=quant.line_color(tok), italic=True)
p.hline(15, token="muted", text="15 pairs: anamorphic centipedes", side="left")
