"""Kinds of nomenclatural types under the ICN (Art. 8-10) and how they arise.

Top: the protologue (the original publication of a name) and the original material it is based on.
If the author designated one specimen, it is the holotype, and duplicates of the same gathering are
isotypes; specimens cited besides the holotype are paratypes. If two or more specimens were designated
together, or no holotype was indicated, the cited specimens are syntypes. A lectotype is later chosen
from the original material when there is no holotype or it is lost (in the order of preference
isotype, syntype, isosyntype, paratype, other original material); a neotype is chosen from other
material only when all original material is missing; an epitype is an additional, interpretive type
chosen when the holotype, lectotype or neotype is ambiguous. A "topotype" (a specimen from the type
locality) has no status under the Code.
"""

import wikibio as bio
from matplotlib.patches import FancyBboxPatch

P = bio.P
fig, ax = bio.canvas(24, 13.6)


def node(xy, text, tok, w=4.2, h=1.0, sub=None):
    bio.box(ax, xy, w, h, token=tok, text=None)
    bio.label(ax, (xy[0], xy[1] + (0.15 if sub else 0)), text, size="normal", bold=True, color=P.on_fill())
    if sub:
        bio.label(ax, (xy[0], xy[1] - 0.25), sub, size="tiny", color=P.on_fill())


def link(a, b, text=None, dashed=False, kind="process"):
    bio.arrow(ax, a, b, kind=kind, dashed=dashed, color=P.muted(), shrink=0.0)
    if text:
        bio.label(ax, ((a[0] + b[0]) / 2 + 0.15, (a[1] + b[1]) / 2), text, size="tiny", ha="left",
                  color=P.muted())


# original material frame
ax.add_patch(FancyBboxPatch((0.5, 5.0), 15.4, 8.0, boxstyle="round,pad=0,rounding_size=0.3",
                            facecolor="none", edgecolor=P.edge("highlight"), lw=1.2, ls="--", zorder=2))
bio.label(ax, (0.8, 12.65), "Original material (cited or seen by the author of the name)", size="small",
          bold=True, ha="left", color=P.edge("highlight"))

node((8.2, 11.4), "Protologue", "neutral", w=5.2, sub="first publication of the name")
node((3.4, 8.6), "Holotype", "positive", sub="the one specimen designated")
node((3.4, 6.2), "Isotype", "positive", sub="duplicate of the holotype")
node((8.2, 8.6), "Paratype", "neutral", sub="other specimens cited")
node((13.0, 8.6), "Syntypes", "highlight", sub="several designated, or none")
node((13.0, 6.2), "Isosyntype", "highlight", sub="duplicate of a syntype")

link((7.0, 10.9), (4.4, 9.1), "one designated")
link((8.2, 10.9), (8.2, 9.1))
link((9.6, 10.9), (12.0, 9.1), "several / none")
link((3.4, 8.1), (3.4, 6.7), "same gathering")
link((13.0, 8.1), (13.0, 6.7), "same gathering")

# later designations
node((19.6, 10.4), "Lectotype", "petal", w=4.6, sub="chosen from original material")
node((19.6, 6.8), "Neotype", "petal", w=4.6, sub="only if all original material is lost")
node((19.6, 3.2), "Epitype", "chloroplast", w=4.6, sub="interpretive, added to an ambiguous type")
link((15.9, 10.4), (17.3, 10.4))
bio.label(ax, (16.6, 11.55), "no holotype:", size="tiny", color=P.muted())
bio.label(ax, (16.6, 11.15), "isotype >", size="tiny", color=P.muted())
bio.label(ax, (16.6, 10.75), "syntype >", size="tiny", color=P.muted())
bio.label(ax, (16.6, 9.95), "paratype", size="tiny", color=P.muted())
link((15.9, 6.8), (17.3, 6.8))
link((19.6, 6.3), (19.6, 3.7), dashed=True)
ax.plot([22.4, 22.4], [10.4, 3.2], color=P.muted(), lw=1.3, ls="--", zorder=4)
ax.plot([21.9, 22.4], [10.4, 10.4], color=P.muted(), lw=1.3, ls="--", zorder=4)
bio.arrow(ax, (22.4, 3.2), (21.95, 3.2), color=P.muted(), dashed=True)
bio.label(ax, (22.6, 6.0), "if ambiguous", size="tiny", ha="left", color=P.muted(), rotation=90)

# not a code term
bio.box(ax, (8.2, 2.6), 6.2, 1.2, token="neutral")
bio.label(ax, (8.2, 2.85), "\"Topotype\"", size="normal", bold=True, color=P.on_fill())
bio.label(ax, (8.2, 2.35), "from the type locality: no status under the ICN", size="tiny", color=P.on_fill())
bio.label(ax, (0.6, 0.5), "dashed frame: original material; arrows: how each kind of type arises", size="tiny",
          ha="left", color=P.muted())
