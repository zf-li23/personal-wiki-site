"""Types of vascular bundles in transverse section (schematic; xylem blue, phloem orange, cambium
yellow; the outside of the organ is at the top). A: open collateral bundle, phloem outside the xylem with a
fascicular cambium between them (eudicot stems). B: closed collateral bundle, no cambium (monocot
stems). C: bicollateral bundle, phloem on both the outer and the inner side of the xylem (Cucurbitaceae,
Solanaceae). D: amphicribral (concentric) bundle, phloem surrounding the xylem (many fern rhizomes). E:
amphivasal (concentric) bundle, xylem surrounding the phloem (rhizomes of Acorus and Convallaria). F:
radial arrangement of the primary root: xylem arms alternating with phloem strands on different radii.
"""

from matplotlib.patches import Rectangle

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24.0, 15.0)
COL = {"xylem": "xylem", "phloem": "phloem", "cambium": "cambium", "inner-phloem": "phloem", "outer-phloem": "phloem"}

cells = [
    ("A", "Open collateral", "eudicot stem", "wikimedia/vascular-bundle-collateral-open", (4.0, 11.0), 5.0),
    ("B", "Closed collateral", "monocot stem", "wikimedia/vascular-bundle-collateral-closed", (12.0, 11.0), 5.0),
    ("C", "Bicollateral", "pumpkin, tomato", "wikimedia/vascular-bundle-bicollateral", (20.0, 11.0), 5.0),
    ("D", "Amphicribral", "fern rhizome", "wikimedia/vascular-bundle-amphicribral", (4.0, 3.9), 4.4),
    ("E", "Amphivasal", "Acorus, Convallaria", "wikimedia/vascular-bundle-amphivasal", (12.0, 3.9), 4.4),
    ("F", "Radial", "primary root", "wikimedia/vascular-bundle-radial", (20.0, 3.9), 4.4),
]
for letter, name, ex, icon_id, at, h in cells:
    bio.panel(ax, letter, (at[0] - 3.8, at[1] + 3.6))
    bio.label(ax, (at[0] - 3.1, at[1] + 3.55), name, size="small", ha="left", va="top")
    bio.label(ax, (at[0] - 3.1, at[1] + 3.0), ex, size="tiny", color=P.muted(), ha="left", va="top", italic=(letter == "E"))
# icons must appear as literals
bio.icon(ax, "wikimedia/vascular-bundle-collateral-open", at=(4.0, 11.0), height=5.0, parts=COL)
bio.icon(ax, "wikimedia/vascular-bundle-collateral-closed", at=(12.0, 11.0), height=5.0, parts=COL)
bio.icon(ax, "wikimedia/vascular-bundle-bicollateral", at=(20.0, 11.0), height=5.0, parts=COL)
bio.icon(ax, "wikimedia/vascular-bundle-amphicribral", at=(4.0, 3.9), height=4.4, parts=COL)
bio.icon(ax, "wikimedia/vascular-bundle-amphivasal", at=(12.0, 3.9), height=4.4, parts=COL)
bio.icon(ax, "wikimedia/vascular-bundle-radial", at=(20.0, 3.9), height=4.4, parts=COL)


def lab(icon_id, part, at, h, text_xy, text):
    p = bio.icon_part(icon_id, part, at=at, height=h)
    bio.callout(ax, p, text_xy, text, size="tiny")


lab("wikimedia/vascular-bundle-collateral-open", "phloem", (4.0, 11.0), 5.0, (7.2, 12.6), "Phloem")
lab("wikimedia/vascular-bundle-collateral-open", "cambium", (4.0, 11.0), 5.0, (7.2, 11.1), "Cambium")
lab("wikimedia/vascular-bundle-collateral-open", "xylem", (4.0, 11.0), 5.0, (7.2, 9.6), "Xylem")
lab("wikimedia/vascular-bundle-bicollateral", "outer-phloem", (20.0, 11.0), 5.0, (23.0, 12.8), "Outer phloem")
lab("wikimedia/vascular-bundle-bicollateral", "inner-phloem", (20.0, 11.0), 5.0, (23.0, 9.0), "Inner phloem")
bio.label(ax, (12.0, 7.6), "no cambium", size="tiny", color=P.muted())
for k, (tk, name) in enumerate((("xylem", "Xylem"), ("phloem", "Phloem"), ("cambium", "Cambium"))):
    x = 8.0 + k * 3.2
    ax.add_patch(Rectangle((x, 0.45), 0.45, 0.45, facecolor=P.fill(tk), edgecolor=P.edge(tk), lw=1.0, zorder=5))
    bio.label(ax, (x + 0.65, 0.68), name, size="small", ha="left")
bio.label(ax, (21.0, 0.68), "outer side of the organ at the top", size="tiny", color=P.muted())
