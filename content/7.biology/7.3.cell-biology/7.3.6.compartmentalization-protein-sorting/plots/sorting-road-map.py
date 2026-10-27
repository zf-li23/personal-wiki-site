"""Road map of protein sorting in a eukaryotic cell.

Every nuclear-encoded protein starts on ribosomes in the cytosol. Three kinds of transport take it
elsewhere: gated transport through nuclear pores (between topologically equivalent spaces),
transmembrane transport by protein translocators (cytosol into ER, mitochondria, plastids,
peroxisomes), and vesicular transport between the compartments of the secretory and endocytic
pathways, whose lumens are topologically equivalent to the outside of the cell. Boxes are tinted
by the colour of each organelle; the dashed line separates the compartments connected by vesicle
traffic (the endomembrane system) from the rest.
"""

import wikibio as bio
from matplotlib.patches import FancyBboxPatch

P = bio.P
fig, ax = bio.canvas(22.0, 11.0)

nodes = {
    "cytosol": ((11.0, 8.6), "Cytosol", "cytoplasm"),
    "nucleus": ((3.0, 8.6), "Nucleus", "nucleus"),
    "mito": ((17.2, 9.9), "Mitochondria", "mitochondrion"),
    "plastid": ((17.2, 8.6), "Plastids", "chloroplast"),
    "perox": ((17.2, 7.3), "Peroxisomes", "peroxisome"),
    "er": ((11.0, 5.6), "Endoplasmic reticulum", "er"),
    "golgi": ((11.0, 3.7), "Golgi apparatus", "golgi"),
    "sv": ((7.0, 2.45), "Secretory vesicles", "vesicle"),
    "pm": ((11.0, 0.9), "Cell exterior / plasma membrane", "extracellular"),
    "early": ((16.4, 3.7), "Early endosomes", "vesicle"),
    "late": ((19.6, 2.2), "Late endosomes", "lysosome"),
    "lyso": ((19.6, 0.9), "Lysosomes", "lysosome"),
}
W = {"cytosol": 3.4, "er": 4.6, "golgi": 3.8, "pm": 6.2, "sv": 3.0}
for k, (c, t, tok) in nodes.items():
    w = W.get(k, 3.4)
    bio.box(ax, c, w, 0.85, token=tok, text=t, size="small")

col = {"gated": P.edge("nucleus"), "tm": P.edge("negative"), "ves": P.edge("dna")}


def link(a, b, kind, bend=0.0, both=False):
    pa, pb = nodes[a][0], nodes[b][0]
    import numpy as np
    pa, pb = np.array(pa, float), np.array(pb, float)
    d = pb - pa
    wa, wb = W.get(a, 3.4) / 2, W.get(b, 3.4) / 2
    # shrink to box borders
    def edge_pt(p, q, w):
        v = q - p
        tx = abs(w / v[0]) if abs(v[0]) > 1e-9 else 1e9
        ty = abs(0.47 / v[1]) if abs(v[1]) > 1e-9 else 1e9
        return p + v * min(tx, ty, 1.0)
    s, e = edge_pt(pa, pb, wa), edge_pt(pb, pa, wb)
    bio.arrow(ax, tuple(s), tuple(e), kind="process", color=col[kind], bend=bend, lw=1.8, dashed=(kind == "gated"))
    if both:
        bio.arrow(ax, tuple(e), tuple(s), kind="process", color=col[kind], bend=bend, lw=1.8, dashed=(kind == "gated"))


link("cytosol", "nucleus", "gated", bend=0.15)
link("nucleus", "cytosol", "gated", bend=0.15)
for t in ("mito", "plastid", "perox", "er"):
    link("cytosol", t, "tm")
bio.arrow(ax, (10.4, 5.13), (10.4, 4.17), kind="process", color=col["ves"], lw=1.8)
bio.arrow(ax, (11.6, 4.17), (11.6, 5.13), kind="process", color=col["ves"], lw=1.8)
link("golgi", "sv", "ves")
link("sv", "pm", "ves")
link("golgi", "pm", "ves")
link("golgi", "early", "ves")
link("pm", "early", "ves", bend=-0.15)
link("early", "pm", "ves", bend=-0.15)
link("early", "late", "ves")
link("late", "lyso", "ves")
link("golgi", "late", "ves", bend=-0.25)

# endomembrane region
ax.add_patch(FancyBboxPatch((5.3, 0.25), 16.4, 6.0, boxstyle="round,pad=0,rounding_size=0.3", fill=False,
                            edgecolor=P.muted(), lw=0.9, ls=(0, (4, 3)), zorder=1))
bio.label(ax, (21.5, 5.95), "lumens topologically equivalent to the exterior", size="tiny", ha="right", color=P.muted())
bio.label(ax, (11.0, 10.2), "ribosomes: all nuclear-encoded proteins start here", size="tiny", color=P.muted())

# legend
lx, ly = 0.4, 4.6
for i, (kind, text) in enumerate((("gated", "gated (nuclear pores)"), ("tm", "transmembrane"), ("ves", "vesicular"))):
    y = ly - 0.75 * i
    bio.arrow(ax, (lx, y), (lx + 1.0, y), kind="process", color=col[kind], lw=1.8, dashed=(kind == "gated"))
    bio.label(ax, (lx + 1.2, y), text, size="small", ha="left")
