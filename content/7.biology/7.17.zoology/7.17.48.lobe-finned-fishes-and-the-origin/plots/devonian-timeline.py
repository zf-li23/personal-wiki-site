# Ages of key fossils of the fish-tetrapod transition in the Middle and Late Devonian (approximate ages,
# rounded to 5 Myr, from the original descriptions and reviews: Zhu & Ahlberg 2004; Daeschler et al.
# 2006; Niedzwiedzki et al. 2010; Clack 2012; Cloutier et al. 2020). Bars show the uncertainty or range of
# the deposits; the Zachelmie trackways predate the body fossils of elpistostegalians and tetrapods.
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(24, 9.5)
X0, X1, A0, A1 = 3.0, 22.0, 400.0, 355.0


def X(age):
    return X0 + (A0 - age) / (A0 - A1) * (X1 - X0)


ROWS = [("Kenichthys (Yunnan): choana forming", 395, 395, "dna", False),
        ("Eusthenopteron, Gogonasus: tetrapodomorph fishes", 385, 380, "dna", False),
        ("Panderichthys, Elpistostege: elpistostegalians", 383, 378, "metabolite", False),
        ("Tiktaalik: 'fishapod' with neck and wrist", 375, 375, "metabolite", False),
        ("Acanthostega, Ichthyostega, Tulerpeton: limbed tetrapods", 368, 362, "highlight", False),
        ("Sinostega (Ningxia): tetrapod from China", 362, 358, "highlight", False),
        ("Zachelmie trackways (Poland): tetrapod footprints", 395, 393, "negative", True)]
top = 7.6
for i, (txt, a, b, tok, tracks) in enumerate(ROWS):
    yy = top - i * 0.85
    if a == b:
        ax.plot([X(a)], [yy], "o", ms=9, color=P.edge(tok), zorder=6)
    else:
        ax.plot([X(a), X(b)], [yy, yy], color=P.edge(tok), lw=6, solid_capstyle="round", zorder=6)
    bio.label(ax, (X(min(a, b)) + 0.3, yy), txt, size="small", ha="left", italic=False)
bio.label(ax, (X(395) - 0.2, top - 6 * 0.85 + 0.55), "footprints older than all body fossils with digits",
          size="tiny", color=P.muted(), ha="left")
for age in (400, 390, 380, 370, 360):
    ax.plot([X(age), X(age)], [1.75, top + 0.5], color=P.mix(P.muted(), P.surface(), 0.6), lw=0.6, ls=":",
            zorder=1)
    bio.label(ax, (X(age), 1.5), f"{age}", size="small", va="top")
bio.label(ax, (X1 + 0.4, 1.5), "Ma", size="small", ha="left", va="top")
phylo.geo_scale(ax, (X0, X1), (A0, A1), 0.85, ranks=("period", "epoch"), height=0.4)
