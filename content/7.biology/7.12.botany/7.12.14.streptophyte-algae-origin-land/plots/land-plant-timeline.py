"""When did plants colonize the land? Molecular-clock estimate for the crown group of embryophytes (Morris et
al. 2018) against the earliest fossils: cryptospores (Rubinstein et al. 2010), trilete spores (Steemans et
al. 2009), Cooksonia, calcified charophytes, the Rhynie chert and the first liverwort macrofossil
(Metzgeriothallus). Ages in millions of years (Ma); ICS periods below."""
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(30, 11.0)
OLD, YOUNG = 560.0, 370.0
X0, X1 = 2.0, 29.0


def X(age):
    return X0 + (OLD - age) / (OLD - YOUNG) * (X1 - X0)


bio.label(ax, (15.5, 10.5), "Origin of land plants: molecular clock and fossils", size="normal", bold=True)
# molecular clock bar
y = 8.9
bio.shape(ax, [[X(515), y - 0.3], [X(470), y - 0.3], [X(470), y + 0.3], [X(515), y + 0.3]], token="dna", lw=1.0, zorder=5)
bio.label(ax, (X(515) - 0.2, y), "Crown embryophytes,\nmolecular clock", size="small", ha="right")
bio.label(ax, ((X(515) + X(470)) / 2, y + 0.65), "515–470 Ma", size="small", color=P.edge("dna"))
# fossils
EV = [
    (470, "Cryptospores\n(dyads, tetrads)", 6.9),
    (450, "Trilete spores", 5.6),
    (432, "Cooksonia", 6.9),
    (425, "Calcified charophytes", 4.3),
    (407, "Rhynie chert", 5.6),
    (385, "Liverwort macrofossil\n(Metzgeriothallus)", 6.9),
]
for age, text, yy in EV:
    ax.plot([X(age), X(age)], [3.0, yy - 0.3], color=P.muted(), lw=0.8, zorder=3, ls=(0, (2, 2)))
    bio.shape(ax, [[X(age), yy - 0.25], [X(age) + 0.25, yy], [X(age), yy + 0.25], [X(age) - 0.25, yy]], token="plant", lw=0.9,
              zorder=6)
    bio.label(ax, (X(age), yy + 0.55), text, size="small", va="bottom", italic=text in ("Cooksonia",))
    bio.label(ax, (X(age), yy - 0.5), f"{age}", size="tiny", va="top", color=P.muted())
bio.label(ax, (X0, 7.6), "Earliest fossils", size="small", ha="left", bold=True)
phylo.geo_scale(ax, (X0, X1), (OLD, YOUNG), y=3.0, ranks=("era", "period"), height=0.6)
for a in (550, 500, 450, 400):
    bio.label(ax, (X(a), 1.4), f"{a} Ma", size="tiny", color=P.muted())
