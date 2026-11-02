"""The eight sign combinations of the feed-forward loop X -> Y -> Z, X -> Z.

Each arrow is an activation (open head) or a repression (bar). In a coherent FFL the sign of the
direct path X -> Z equals the product of the signs on the indirect path X -> Y -> Z; in an
incoherent FFL the two paths have opposite signs. Signs are listed as (X->Y, X->Z, Y->Z).
"""

import wikibio as bio
from wikibio import network

P = bio.P

types = [
    ("C1", "+++", "coherent"), ("C2", "--+", "coherent"), ("C3", "+--", "coherent"), ("C4", "-+-", "coherent"),
    ("I1", "++-", "incoherent"), ("I2", "---", "incoherent"), ("I3", "+-+", "incoherent"), ("I4", "-++", "incoherent"),
]

fig, ax = bio.canvas(16, 9.4)
bio.label(ax, (0.3, 9.05), "Coherent: indirect path has the same sign as the direct path", size="small", ha="left",
          color=P.muted())
bio.label(ax, (0.3, 4.55), "Incoherent: the two paths have opposite signs", size="small", ha="left", color=P.muted())
for k, (name, signs, kind) in enumerate(types):
    col, row = k % 4, k // 4
    cx = 2.0 + 4.0 * col
    cy = 6.6 - 4.5 * row
    tok = ["positive" if kind == "coherent" else "negative"] * 3
    network.motif(ax, "ffl", (cx, cy), size=3.0, signs=signs, token=[P.protein(1), P.protein(2), P.protein(3)],
                  italic=False)
    bio.label(ax, (cx + 1.25, cy + 1.35), name, size="normal", bold=True)
