"""Lipids classified by biological function (after Lehninger, chapter 10), with representative members.
Storage lipids (left), membrane lipids (centre; the backbone, glycerol or sphingosine, and the head
group decide the subclass), and lipids present in small amounts that act as signals, cofactors and
pigments (right). Most of the third group, like sterols, are isoprenoids built from five-carbon units."""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24.0, 12.0)


def node(xy, text, tok, w=3.6, h=0.75, size="small", bold=False):
    bio.box(ax, xy, w, h, token=tok, radius=0.14)
    bio.label(ax, xy, text, size=size, color=P.on_fill(), bold=bold)
    return xy


def link(a, b):
    ax.plot([a[0], a[0], b[0], b[0]], [a[1] - 0.38, (a[1] + b[1]) / 2, (a[1] + b[1]) / 2, b[1] + 0.38], color=P.muted(),
            lw=0.9, zorder=2)


root = node((12.0, 11.2), "Lipids (insoluble in water, soluble in organic solvents)", "neutral", w=9.5, size="normal",
            bold=True)
cols = {"storage": (3.4, "lipid"), "membrane": (11.6, "membrane"), "active": (20.2, "metabolite")}
top = {
    "storage": node((3.4, 9.6), "Storage lipids", "lipid", bold=True),
    "membrane": node((11.6, 9.6), "Membrane (structural) lipids", "membrane", w=5.0, bold=True),
    "active": node((20.2, 9.6), "Signals, cofactors, pigments", "metabolite", w=4.8, bold=True),
}
for k in top.values():
    link(root, k)


def column(key, items, x, start=8.3, dy=0.95, w=3.6):
    prev = top[key]
    tok = cols[key][1]
    for i, (text, sub) in enumerate(items):
        y = start - i * dy
        node((x, y), text, tok, w=w)
        ax.plot([x - w / 2 - 0.3, x - w / 2], [y, y], color=P.muted(), lw=0.9)
        if sub:
            bio.label(ax, (x, y - 0.5), sub, size="tiny", color=P.muted())
    ax.plot([x - w / 2 - 0.3] * 2, [prev[1] - 0.38, start - (len(items) - 1) * dy], color=P.muted(), lw=0.9)


column("storage", [("triacylglycerols", "fats and oils"), ("waxes", "beeswax, cuticle")], 3.7, dy=1.25)
column("membrane", [("glycerophospholipids", "PC, PE, PS, PI, PG, cardiolipin"),
                    ("ether lipids", "plasmalogens, PAF"),
                    ("galactolipids, sulfolipids", "thylakoid membranes"),
                    ("archaeal ether lipids", "isoprenoid chains, tetraethers"),
                    ("sphingolipids", "sphingomyelin, cerebrosides, gangliosides"),
                    ("sterols", "cholesterol, phytosterols, ergosterol")], 12.0, dy=1.25, w=4.2)
column("active", [("phosphatidylinositols", "PIP2 → IP3 + DAG; PIP3"),
                  ("eicosanoids", "prostaglandins, thromboxanes, leukotrienes"),
                  ("steroid hormones", "cortisol, sex hormones, brassinolide"),
                  ("fat-soluble vitamins", "A, D, E, K"),
                  ("lipid quinones, dolichols", "ubiquinone, plastoquinone"),
                  ("carotenoids, polyketides", "β-carotene; erythromycin, lovastatin")], 20.6, dy=1.25, w=4.4)
