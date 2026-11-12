# Representatives of the main groups of Hymenoptera (PhyloPic silhouettes, not to scale), with field
# characters and approximate numbers of described species (Aguiar et al. 2013; AntCat; Ascher and Pickering's
# bee catalogue). Sawflies have no waist; the apocritan groups have a narrow petiole.
import wikibio as bio
from wikibio.icons import size as icon_size

P = bio.P
CELLS = [
    ("Symphyta", "sawflies", "~8,500", "enzyme", "phylopic/sawfly", "larva shown: up to 8 pairs\nof prolegs, no crochets"),
    ("Ichneumonidae", "ichneumon wasps", "~25,000", "protein", "phylopic/ichneumon", "long antennae; long\novipositor; parasitoids"),
    ("Vespidae", "social and solitary wasps", "~5,000", "channel", "phylopic/wasp", "wings folded lengthwise;\nkidney-shaped eyes"),
    ("Formicidae", "ants", "~14,000", "channel", "phylopic/ant", "elbowed antennae;\npetiole with a node"),
    ("Anthophila", "bees", "~20,000", "channel", "phylopic/honey-bee", "branched hairs; pollen-\ncarrying legs or venter"),
]
NC, CW, CH = 5, 5.6, 5.4
W, H = NC * CW, CH + 1.6
fig, ax = bio.canvas(W, H)
for i, (grp, common, n, tok, icon, chars) in enumerate(CELLS):
    x0, y0 = i * CW, 0
    bio.label(ax, (x0 + CW / 2, y0 + CH - 0.35), grp, size="normal", bold=True)
    bio.label(ax, (x0 + CW / 2, y0 + CH - 0.85), f"{common} ({n} spp.)", size="tiny", color=P.muted())
    iw, ih = icon_size(icon)
    w = min(CW - 1.2, 2.6 * iw / ih)
    bio.icon(ax, icon, at=(x0 + CW / 2, y0 + 2.75), width=w, color=tok)
    bio.label(ax, (x0 + CW / 2, y0 + 0.75), chars, size="tiny")
for k, (name, tok) in enumerate([("Symphyta (paraphyletic)", "enzyme"), ("parasitoid Apocrita", "protein"),
                                 ("Aculeata", "channel")]):
    x = 1.0 + k * 7.0
    bio.box(ax, (x + 0.3, H - 0.8), 0.5, 0.5, token=tok)
    bio.label(ax, (x + 0.8, H - 0.8), name, size="small", ha="left")
bio.label(ax, (W - 0.3, H - 0.8), "Silhouettes not to scale", size="tiny", color=P.muted(), ha="right")
