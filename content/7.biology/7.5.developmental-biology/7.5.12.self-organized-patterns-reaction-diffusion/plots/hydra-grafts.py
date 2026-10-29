"""Axial grafts in Hydra and what they say about head formation.

Left: a Hydra polyp (silhouette) and its axis divided into the head (H: hypostome and tentacles),
four levels of the body column (1 at the top to 4 near the foot) and the basal disc (B). Right: grafts of pieces
of column onto a host column 1-2-3-4, with the junction marked by a gap, and whether a second head forms at the
junction. A piece of upper column grafted to the host forms a head if it is large enough (1 alone does not,
1-2 does) and if it is far enough from an existing head (H-1-2 does not, H-1-2-3 does): head formation is
self-enhancing within a piece and inhibited over a range of two to three column levels by an existing head.
"""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26.0, 12.0)
bio.icon(ax, "phylopic/hydra", at=(2.2, 6.4), height=6.5, color="animal")
tok = {"H": "negative", "1": "highlight", "2": "na", "3": "protein", "4": "neutral", "B": "bone"}
for k, s_ in enumerate("H1234B"):
    bio.box(ax, (5.6, 10.0 - 1.45 * k), 1.0, 1.2, tok[s_], text=s_, size="small")
bio.label(ax, (5.6, 1.0), "body axis", size="tiny", color=P.muted())
bio.label(ax, (2.2, 2.4), "Hydra polyp", size="tiny", color=P.muted())
rows = (("1", "no head"), ("12", "head forms"), ("H12", "no head"), ("H123", "head forms"))
bio.label(ax, (8.0, 11.2), "graft  |  host 1 2 3 4", size="small", bold=True, ha="left")
for r, (donor, result) in enumerate(rows):
    y = 9.6 - 2.3 * r
    x = 8.0
    for s in donor:
        bio.box(ax, (x + 0.55, y), 1.0, 0.9, tok[s], text=s, size="small")
        x += 1.1
    x += 0.5
    for s in "1234":
        bio.box(ax, (x + 0.55, y), 1.0, 0.9, tok[s], text=s, size="small")
        x += 1.1
    head = result == "head forms"
    bio.label(ax, (17.4, y), result, size="small", ha="left", color=P.edge("positive" if head else "negative"), bold=True)
    bio.label(ax, (21.0, y), ("piece too small" if donor == "1" else "large enough" if donor == "12"
                              else "existing head 2 levels away" if donor == "H12" else "existing head 3 levels away"),
              size="tiny", ha="left", color=P.muted())
bio.label(ax, (16.5, 0.6), "short-range self-activation, long-range inhibition", size="small", color=P.ink())
