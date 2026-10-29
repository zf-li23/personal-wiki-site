# From sperm entry to the organizer in Xenopus. A: the fertilized egg; the sperm enters the pigmented animal
# hemisphere on the future ventral side. B: during the first cell cycle the cortex rotates by about 30 degrees
# relative to the core (cortical rotation), carrying vegetal dorsal determinants (Huluwa, Dishevelled, Wnt11 mRNA)
# to the side opposite sperm entry. C: in the late blastula, beta-catenin is nuclear on the dorsal side; the dorsal
# vegetal cells form the Nieuwkoop centre (orange) and induce the overlying marginal zone to become the organizer
# (green); germ-layer colours: animal cap, prospective ectoderm (blue); marginal zone, mesoderm (red); vegetal mass,
# endoderm (yellow). D: in the early gastrula the organizer is the dorsal lip of the blastopore, where involution
# begins.
import wikibio as bio
from wikibio import bodyaxes as BA

fig, ax = bio.canvas(24.0, 8.6)
P = bio.P
r = 2.2
xs = [3.0, 9.0, 15.0, 21.0]
y = 4.4
e = BA.amphibian(ax, (xs[0], y), r, stage="egg", rotation=0)
bio.callout(ax, e["sperm_entry"], (0.6, 7.8), "Sperm entry")
bio.label(ax, (xs[0], y + r + 0.9), "Animal pole", size="tiny", color=P.muted())
bio.label(ax, (xs[0], y - r - 0.5), "Vegetal pole", size="tiny", color=P.muted())
e2 = BA.amphibian(ax, (xs[1], y), r, stage="egg", rotation=30)
bio.arrow(ax, (xs[1] - 1.0, y - r - 0.35), (xs[1] + 1.0, y - r - 0.35), kind="process", bend=-0.25, color=P.edge("drug"))
bio.label(ax, (xs[1], y - r - 1.2), "cortex rotates 30°", size="tiny", color=P.muted())
for k in range(5):
    ax.add_patch(bio.core.Circle((xs[1] + 1.3 + 0.12 * k, y - 1.45 + 0.2 * k), 0.08, facecolor=P.edge("positive"), edgecolor="none", zorder=20))
bio.callout(ax, (xs[1] + 1.55, y - 0.85), (xs[1] + 2.4, y + r + 0.6), "dorsal determinants")
b = BA.amphibian(ax, (xs[2], y), r, stage="blastula")
bio.callout(ax, b["nieuwkoop"], (xs[2] + 1.4, 0.6), "Nieuwkoop centre")
bio.callout(ax, b["organizer"], (xs[2] + 2.0, y + r + 0.7), "Organizer")
g = BA.amphibian(ax, (xs[3], y), r, stage="gastrula")
bio.callout(ax, g["dorsal_lip"], (xs[3] + 1.2, 0.6), "Dorsal lip")
for k, (x, t) in enumerate(zip(xs, ["A  Fertilized egg", "B  Cortical rotation", "C  Late blastula", "D  Early gastrula"])):
    bio.label(ax, (x - r, 8.3), t, size="normal", bold=True, ha="left")
    bio.label(ax, (x - r - 0.25, y), "V", size="small", color=P.muted())
    bio.label(ax, (x + r + 0.25, y), "D", size="small", color=P.muted())
