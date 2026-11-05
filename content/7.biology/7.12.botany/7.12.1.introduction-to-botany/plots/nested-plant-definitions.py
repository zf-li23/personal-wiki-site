"""Nested circumscriptions of "plants", from the broadest clade (Archaeplastida, all eukaryotes with
primary plastids) to the narrowest (Embryophyta, land plants), with the vascular and seed plants
inside the land plants. Each box is a clade; its defining features are listed under the name, and
silhouettes show representative members that belong to that box but not to the next one inside.
"""

import wikibio as bio
from matplotlib.patches import FancyBboxPatch

P = bio.P
fig, ax = bio.canvas(24, 14)


def tint(tok):
    """Pale box fill: a light tint of the token, or a dark tint of its hue in the dark theme."""
    if P.is_dark():
        return P.mix(P.edge(tok), P.DARK_SURFACE, 0.74)
    return P.mix(P.fill(tok), "#ffffff", 0.5)


levels = [
    # (x0, y0, w, h, token, name, defining features: written below by hand)
    (0.4, 0.4, 23.2, 13.2, "neutral", "Archaeplastida",
     "primary plastid from a cyanobacterium (two envelope membranes)"),
    (5.4, 0.9, 17.7, 11.7, "chloroplast", "Viridiplantae (green plants)",
     "chlorophylls a and b; starch stored inside the plastid"),
    (9.6, 1.4, 13.0, 10.2, "plant", "Streptophyta",
     "phragmoplast; cellulose-synthase rosettes; sperm with lateral flagella"),
    (13.4, 1.9, 8.7, 8.7, "positive", "Embryophyta (land plants)",
     "embryo retained on the mother plant; cuticle; multicellular gametangia and sporangia"),
    (16.7, 2.4, 5.0, 5.6, "highlight", "Tracheophyta",
     "xylem with lignified tracheids; branched sporophyte"),
    (18.3, 2.9, 3.1, 2.6, "petal", "Spermatophyta", "seeds"),
]
for x0, y0, w, h, tok, name, feat in levels:
    ax.add_patch(FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0,rounding_size=0.35",
                                facecolor=tint(tok), edgecolor=P.edge(tok), lw=1.3, zorder=2))
    bio.label(ax, (x0 + 0.3, y0 + h - 0.35), name, size="normal", bold=True, ha="left", va="top",
              color=P.edge(tok))

# features: written in the free left strip of each box
bio.label(ax, (0.7, 12.5), "primary plastid from a\ncyanobacterium\n(two envelope membranes)", size="small",
          ha="left", va="top")
bio.label(ax, (5.7, 11.5), "chlorophylls a and b;\nstarch stored inside\nthe plastid", size="small",
          ha="left", va="top")
bio.label(ax, (9.9, 10.5), "phragmoplast;\ncellulose-synthase\nrosettes", size="small", ha="left", va="top")
bio.label(ax, (13.7, 9.5), "embryo retained on the mother plant;\ncuticle; multicellular\ngametangia "
          "and sporangia", size="small", ha="left", va="top")
bio.label(ax, (17.0, 7.0), "lignified xylem;\nbranched sporophyte", size="small", ha="left", va="top")
bio.label(ax, (18.6, 4.4), "seeds", size="small", ha="left", va="top")

# representative members of each ring (outside the next box inside)
bio.icon(ax, "phylopic/porphyra", at=(2.0, 6.5), height=1.8, color=P.edge("petal"))
bio.label(ax, (2.0, 5.2), "red algae", size="small")
bio.label(ax, (2.0, 4.4), "(also glaucophytes)", size="tiny")
bio.icon(ax, "phylopic/chlamydomonas", at=(7.0, 6.5), height=1.6, color=P.edge("chloroplast"))
bio.icon(ax, "phylopic/ulva", at=(7.4, 3.8), height=1.6, color=P.edge("chloroplast"))
bio.label(ax, (7.3, 2.4), "Chlorophyta", size="small")
bio.icon(ax, "phylopic/chara", at=(11.0, 6.0), height=2.2, color=P.edge("plant"))
bio.icon(ax, "phylopic/zygnema", at=(11.6, 3.4), height=1.4, color=P.edge("plant"))
bio.label(ax, (11.4, 2.1), "charophytes", size="small")
bio.icon(ax, "phylopic/moss", at=(14.4, 6.0), height=1.8, color=P.edge("positive"))
bio.icon(ax, "phylopic/liverwort", at=(15.4, 4.0), height=1.2, color=P.edge("positive"))
bio.label(ax, (15.0, 2.6), "bryophytes", size="small")
bio.icon(ax, "phylopic/fern", at=(17.4, 4.0), height=1.5, color=P.edge("highlight"))
bio.label(ax, (17.4, 2.9), "ferns,\nlycophytes", size="tiny")
bio.icon(ax, "phylopic/pine", at=(19.1, 3.6), height=1.0, color=P.edge("petal"))
bio.icon(ax, "phylopic/magnolia", at=(20.5, 3.6), height=1.0, color=P.edge("petal"))
