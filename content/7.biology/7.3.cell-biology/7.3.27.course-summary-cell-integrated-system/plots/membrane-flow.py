"""Map of membrane and protein flow through the compartments of an animal cell, with the rates of the course.

Boxes are compartments tinted by organelle colour; arrows are the main flows, coloured by direction
(secretory, endocytic, recycling and retrieval, translocation from the cytosol). Numbers are the
typical values quoted in chapters 7.3.6-7.3.11 and 7.3.16-7.3.17 (fibroblasts, HeLa cells,
pancreatic acinar cells); pH values are lumenal. Every compartment of constant size is a steady
state of its inflow and outflow, dA/dt = J_in - J_out (Eq. 8.4).
"""

import numpy as np

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(27.0, 14.6)

H = 0.95
nodes = {  # key: (center, width, text, token)
    "nucleus": ((3.0, 12.9), 4.2, "Nucleus", "nucleus"),
    "cytosol": ((11.6, 12.9), 6.2, "Cytosol (free ribosomes)", "cytoplasm"),
    "mito": ((22.6, 13.7), 4.4, "Mitochondria", "mitochondrion"),
    "perox": ((22.6, 12.5), 4.4, "Peroxisomes", "peroxisome"),
    "auto": ((17.6, 10.2), 3.8, "Autophagosome", "vesicle"),
    "er": ((6.0, 9.3), 4.8, "Endoplasmic reticulum", "er"),
    "golgi": ((6.0, 6.3), 4.8, "Golgi stack (cis → trans)", "golgi"),
    "tgn": ((6.0, 3.9), 3.4, "TGN", "golgi"),
    "granule": ((1.9, 2.3), 3.0, "Secretory granules", "vesicle"),
    "early": ((14.2, 4.6), 3.8, "Early endosome", "vesicle"),
    "recyc": ((14.2, 2.0), 3.8, "Recycling endosome", "vesicle"),
    "late": ((20.4, 5.8), 3.8, "Late endosome / MVB", "lysosome"),
    "lyso": ((23.8, 8.6), 3.4, "Lysosome", "lysosome"),
    "pm": ((13.5, 0.55), 26.4, "Plasma membrane and exterior", "extracellular"),
}
for k, (c, w, t, tok) in nodes.items():
    # compartment tints turn dark in the dark theme: write their names in the ink colour
    dark = tok in ("cytoplasm", "nucleus", "extracellular")
    bio.box(ax, c, w, H if k != "pm" else 0.8, token=tok, text=None if dark else t, size="small")
    if dark:
        bio.label(ax, c, t, size="small", color=P.ink())

COL = {
    "sec": P.edge("golgi"),
    "endo": P.edge("lysosome"),
    "ret": P.edge("dna"),
    "tm": P.edge("mitochondrion"),
}


def port(k, side, f=0.5):
    """A point on the border of box k: side in 'top', 'bottom', 'left', 'right'; f along the side."""
    (x, y), w, _, _ = nodes[k]
    h = 0.8 if k == "pm" else H
    if side == "top":
        return (x - w / 2 + f * w, y + h / 2)
    if side == "bottom":
        return (x - w / 2 + f * w, y - h / 2)
    if side == "left":
        return (x - w / 2, y - h / 2 + f * h)
    return (x + w / 2, y - h / 2 + f * h)


def flow(a, b, kind, text=None, at=None, ha="center", bend=0.0, dashed=False, size="tiny"):
    bio.arrow(ax, a, b, kind="process", color=COL[kind], lw=1.7, bend=bend, dashed=dashed, head=0.26)
    if text:
        m = at if at is not None else ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
        bio.label(ax, m, text, size=size, ha=ha, color=P.ink())


def note(xy, text, ha="center"):
    bio.label(ax, xy, text, size="tiny", ha=ha, color=P.muted())


# gated and transmembrane transport from the cytosol
flow(port("cytosol", "left", 0.7), port("nucleus", "right", 0.7), "tm", bend=0.0)
flow(port("nucleus", "right", 0.3), port("cytosol", "left", 0.3), "tm", dashed=True)
note((7.0, 13.85), "NPCs: up to 10³ macromolecules s⁻¹ per pore;")
note((7.0, 13.45), "≈ 3500 new ribosomes min⁻¹ exported (HeLa)")
flow(port("cytosol", "right", 0.75), port("mito", "left", 0.5), "tm")
flow(port("cytosol", "right", 0.35), port("perox", "left", 0.5), "tm")
note((17.3, 14.05), "posttranslational import (TOM/TIM, Δψ ≈ 160 mV; Pex5)")
flow(port("cytosol", "bottom", 0.12), port("er", "top", 0.75), "tm", text="SRP + Sec61\n(cotranslational)",
     at=(9.6, 11.0), ha="left")
flow(port("cytosol", "bottom", 0.85), port("auto", "top", 0.4), "tm", text="phagophore\n(ATG proteins)", at=(16.9, 11.95),
     ha="left")

# secretory pathway
flow(port("er", "bottom", 0.3), port("golgi", "top", 0.3), "sec", text="COPII", at=(4.55, 7.8), ha="right")
flow(port("golgi", "top", 0.7), port("er", "bottom", 0.7), "ret", dashed=True, text="COPI, KDEL\nreceptor", at=(7.5, 7.8),
     ha="left")
note((9.1, 6.3), "transit ≈ 20 min,", ha="left")
note((9.1, 5.9), "pH 6.7 → 6.0", ha="left")
flow(port("golgi", "bottom", 0.5), port("tgn", "top", 0.5), "sec")
flow(port("tgn", "left", 0.5), port("granule", "top", 0.5), "sec", bend=0.25, text="sorting by\naggregation", at=(2.2, 4.3),
     ha="center")
note((3.5, 1.75), "pH 5.0–5.5", ha="left")
flow(port("granule", "bottom", 0.5), (1.9, 0.95), "sec", text="  regulated, Ca²⁺ (ms)", at=(2.0, 1.25), ha="left")
flow(port("tgn", "bottom", 0.4), (5.85, 0.95), "sec", text="constitutive\n(min)", at=(7.1, 2.0), ha="left")
flow(port("tgn", "right", 0.65), port("early", "left", 0.75), "sec", text="M6P receptors\n(hydrolases)", at=(10.3, 5.35))
flow(port("early", "left", 0.25), port("tgn", "right", 0.25), "ret", dashed=True, text="retromer", at=(10.3, 3.55))

# endocytic pathway
flow((12.8, 0.95), port("early", "bottom", 0.13), "endo", bend=-0.2)
note((12.3, 1.75), "endocytosis 1–3 % of surface min⁻¹,", ha="right")
note((12.3, 1.38), "≈ 2500 coated vesicles min⁻¹", ha="right")
flow(port("early", "bottom", 0.82), port("recyc", "top", 0.82), "ret", dashed=True)
flow(port("recyc", "bottom", 0.5), (14.2, 0.95), "ret", dashed=True)
note((17.3, 2.95), "fast and slow recycling;", ha="left")
note((17.3, 2.55), "LDLR round trip ≈ 10 min", ha="left")
note((14.2, 5.35), "pH 6.0–6.5, Rab5, PI(3)P")
flow(port("early", "right", 0.6), port("late", "left", 0.5), "endo", text="Rab5 → Rab7 conversion\n(after ≈ 10 min)",
     at=(17.3, 6.15))
note((20.4, 5.05), "pH 5.0–6.0, Rab7, ESCRT")
flow(port("late", "top", 0.75), port("lyso", "bottom", 0.25), "endo", text="fusion", at=(22.0, 7.3), ha="right")
flow(port("auto", "right", 0.5), port("lyso", "left", 0.7), "endo", text="autophagic flux", at=(21.2, 10.05), ha="left")
note((23.8, 9.35), "pH 4.5–5.0; mTORC1")
flow((25.0, 0.95), port("lyso", "bottom", 0.85), "endo", bend=0.15, text="phagocytosis,\nmacropinocytosis",
     at=(25.3, 4.2), ha="center")

note((13.5, 0.05), "every compartment of constant size: dA/dt = J_in − J_out (Eq. 8.4)")

# legend
lx, ly = 9.8, 9.6
for i, (k, t, d) in enumerate((("tm", "translocation / gated", False), ("sec", "secretory (outward)", False),
                                ("endo", "endocytic (inward)", False), ("ret", "recycling and retrieval", True))):
    y = ly - 0.55 * i
    bio.arrow(ax, (lx, y), (lx + 1.0, y), kind="process", color=COL[k], lw=1.7, dashed=d, head=0.24)
    bio.label(ax, (lx + 1.25, y), t, size="tiny", ha="left")
