"""Where the gametophyte lives: a schematic (not to scale) of the two generations in five land plants.
Orange: gametophyte (n); blue: sporophyte (2n); grey ring: spore wall. Moss: the sporophyte grows on the
free-living gametophyte. Fern: both generations free-living, the gametophyte small. Selaginella: unisexual
gametophytes develop inside the spore wall after the spores are shed. Pine: the megaspore stays in the
ovule and the female gametophyte (with archegonia) develops on the parent sporophyte; the male gametophyte
is the pollen grain. Angiosperm: the ovule is enclosed in the ovary, the female gametophyte is a 7-celled
embryo sac without archegonia and the pollen grain has 2-3 cells. Rows below: the facts compared."""
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30, 17)
G, S = "rna", "dna"  # gametophyte, sporophyte
PANELS = ["Moss", "Fern", "Selaginella", "Pine", "Angiosperm"]
ICON = {"Moss": "phylopic/moss", "Fern": "phylopic/fern", "Selaginella": "phylopic/selaginella",
        "Pine": "phylopic/pine", "Angiosperm": "phylopic/magnolia"}
W = 5.6
X = [0.6 + k * (W + 0.3) for k in range(5)]
YB, YT = 7.4, 14.2  # drawing area of each panel


def box(x, y, w, h, tok, z=4, alpha_light=False):
    fc = P.light(tok) if alpha_light else P.fill(tok)
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.3", facecolor=fc,
                                edgecolor=P.edge(tok), lw=1.0, zorder=z))


def ell(c, w, h, tok, z=5, light=False):
    ax.add_patch(Ellipse(c, w, h, facecolor=P.light(tok) if light else P.fill(tok), edgecolor=P.edge(tok), lw=1.0,
                         zorder=z))


def dot(c, r, tok, z=7):
    ax.add_patch(Circle(c, r, facecolor=P.edge(tok), edgecolor="none", zorder=z))


for k, name in enumerate(PANELS):
    x0 = X[k]
    cx = x0 + W / 2
    ax.add_patch(FancyBboxPatch((x0, YB - 0.2), W, YT - YB + 2.3, boxstyle="round,pad=0,rounding_size=0.25",
                                facecolor="none", edgecolor=P.muted(), lw=0.6, zorder=1))
    bio.label(ax, (cx - 0.5, YT + 1.55), name, size="normal", bold=True, italic=(name == "Selaginella"))
    bio.icon(ax, ICON[name], at=(x0 + W - 0.7, YT + 1.45), height=0.9, color=P.edge("plant"))

    if name == "Moss":
        box(cx - 1.8, YB + 0.4, 3.6, 3.6, G)           # leafy gametophyte
        box(cx - 0.12, YB + 4.0, 0.24, 2.2, S, z=5)     # seta
        ell((cx, YB + 6.5), 0.7, 1.1, S)                # capsule
        bio.label(ax, (cx, YB + 2.2), "gametophyte", size="small", color=P.on_fill())
        bio.label(ax, (cx + 1.3, YB + 6.5), "sporophyte", size="small", ha="left")
    elif name == "Fern":
        box(cx - 2.2, YB + 1.5, 3.0, 5.0, S)
        bio.label(ax, (cx - 0.7, YB + 4.0), "sporophyte", size="small", color=P.on_fill())
        ell((cx + 1.7, YB + 0.9), 1.0, 0.7, G)
        bio.label(ax, (cx + 1.7, YB + 1.6), "prothallus", size="small")
    elif name == "Selaginella":
        box(cx - 2.2, YB + 1.8, 2.6, 4.7, S)
        bio.label(ax, (cx - 0.9, YB + 4.2), "sporophyte", size="small", color=P.on_fill())
        for c, r, lab in (((cx + 1.5, YB + 1.3), 0.62, "mega-"), ((cx + 1.6, YB + 3.1), 0.32, "micro-")):
            ax.add_patch(Circle(c, r, facecolor=P.fill(G), edgecolor=P.muted(), lw=2.2, zorder=5))
            bio.label(ax, (c[0], c[1] - r - 0.3), lab + "spore", size="tiny")
        bio.label(ax, (cx + 1.5, YB + 4.2), "shed", size="tiny", color=P.muted())
    elif name == "Pine":
        box(cx - 2.4, YB + 0.4, 4.8, 6.0, S, z=3)
        bio.label(ax, (cx, YB + 5.9), "sporophyte (tree, cone)", size="small", color=P.on_fill())
        ell((cx - 0.4, YB + 2.7), 2.6, 3.6, S, light=True)  # ovule: integument + nucellus
        ell((cx - 0.4, YB + 2.5), 1.6, 2.4, G, z=6)         # female gametophyte
        for dx in (-0.3, 0.3):
            dot((cx - 0.4 + dx, YB + 3.4), 0.16, G)          # archegonia
        bio.label(ax, (cx - 0.4, YB + 0.75), "ovule", size="tiny", color=P.ink())
        ax.add_patch(Circle((cx + 1.65, YB + 3.6), 0.34, facecolor=P.fill(G), edgecolor=P.edge(G), lw=1.0, zorder=6))
        bio.label(ax, (cx + 1.65, YB + 4.25), "pollen", size="tiny", color=P.on_fill())
    else:
        box(cx - 2.4, YB + 0.4, 4.8, 6.0, S, z=3)
        bio.label(ax, (cx, YB + 5.9), "sporophyte (flower)", size="small", color=P.on_fill())
        ell((cx - 0.4, YB + 2.7), 3.0, 4.0, S, light=True)  # ovary wall
        ell((cx - 0.4, YB + 2.5), 1.7, 2.6, S, z=6)         # ovule
        ell((cx - 0.4, YB + 2.5), 0.55, 1.1, G, z=7)        # embryo sac
        bio.label(ax, (cx - 0.4, YB + 0.95), "ovary", size="tiny", color=P.ink())
        ax.add_patch(Circle((cx + 1.65, YB + 3.6), 0.26, facecolor=P.fill(G), edgecolor=P.edge(G), lw=1.0, zorder=6))
        bio.label(ax, (cx + 1.65, YB + 4.2), "pollen", size="tiny", color=P.on_fill())

# comparison rows
ROWS = [
    ("Dominant generation", ["gametophyte", "sporophyte", "sporophyte", "sporophyte", "sporophyte"]),
    ("Gametophyte lives", ["free, on soil", "free, on soil", "inside spore wall", "in ovule / pollen",
                           "in ovule / pollen"]),
    ("Female gametophyte", ["leafy shoot", "heart-shaped thallus", "inside megaspore", "thousands of cells",
                            "7 cells, 8 nuclei"]),
    ("Male gametophyte", ["leafy shoot", "same thallus", "1 cell + antheridium", "4 cells when shed",
                          "2-3 cells"]),
    ("Archegonia", ["yes", "yes", "yes", "yes (2-3)", "none"]),
    ("Sperm reach the egg", ["swimming", "swimming", "swimming", "pollen tube", "pollen tube"]),
    ("Embryo fed by", ["gametophyte", "gametophyte (foot)", "gametophyte", "gametophyte (n)",
                       "endosperm (3n)"]),
]
y = 6.5
for head, vals in ROWS:
    bio.label(ax, (0.6, y), head, size="small", bold=True, ha="left")
    y -= 0.42
    for k, v in enumerate(vals):
        bio.label(ax, (X[k] + W / 2, y), v, size="small")
    y -= 0.5
