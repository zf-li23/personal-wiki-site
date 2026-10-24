"""Colour tokens for biology figures, in a soft BioRender-like style that works on both site themes.

Every biological object has a token: a fill and an outline (a darker shade of the same hue). The
dark theme keeps object fills (soft colours stay readable on the dark surface), lightens outlines,
and turns pale compartment fills into translucent tints of their hue so cells do not glow white.
The renderer only recolours near-black and near-white; these tokens avoid both on purpose.

    from wikibio import palette as P
    P.fill("nucleus"), P.edge("nucleus"), P.ink(), P.protein(2)
"""

import matplotlib as mpl
from matplotlib.colors import to_hex, to_rgb

DARK_SURFACE = "#0f172a"  # site dark background (render_plot.THEMES)

# token: (fill, edge, kind) with kind "object" (solid things) or "space" (compartments: pale fills)
TOKENS = {
    # nucleic acids
    "dna": ("#6FA8DC", "#2F6CA8", "object"),
    "dna2": ("#A9CCEC", "#4C86BF", "object"),  # second strand / template
    "rna": ("#F0936B", "#C0562F", "object"),
    "mrna": ("#F0936B", "#C0562F", "object"),
    "trna": ("#F5B07E", "#C4733B", "object"),
    "rrna": ("#E9A3A0", "#B55B57", "object"),
    # membranes
    "lipid_head": ("#F6B26B", "#C97B2E", "object"),
    "lipid_tail": ("#EAD9BB", "#BFA57A", "object"),
    "membrane": ("#F8C98F", "#C98A3E", "object"),
    "cell_wall": ("#C7DB9C", "#7E9C3E", "object"),
    # macromolecules and small molecules
    "protein": ("#A893DA", "#6E55A8", "object"),
    "enzyme": ("#5FC3B9", "#2E8A83", "object"),
    "receptor": ("#F293B6", "#C2507D", "object"),
    "channel": ("#7FB6E8", "#3E7CB8", "object"),
    "antibody": ("#F7CF6B", "#C49A22", "object"),
    "carbohydrate": ("#9FD585", "#5C9A42", "object"),
    "lipid": ("#F9E29C", "#C9A93E", "object"),
    "metabolite": ("#C3B6E2", "#7E6BB0", "object"),
    "atp": ("#F5C242", "#B98A10", "object"),
    "drug": ("#F79A7B", "#C45B3A", "object"),
    # ions
    "ca": ("#F7C948", "#B98E12", "object"),
    "na": ("#8EC5FF", "#3F7FC4", "object"),
    "k": ("#C9A2FF", "#7E54C6", "object"),
    "cl": ("#9EDC9E", "#4E9A4E", "object"),
    "h": ("#FF9F9F", "#C75454", "object"),
    "mg": ("#BFE3D4", "#5E9E86", "object"),
    # compartments and cell types
    "cytoplasm": ("#FDF3E6", "#E0B98A", "space"),
    "extracellular": ("#F4F8FB", "#B8C7D4", "space"),
    "nucleus": ("#E8DFF7", "#9A84CF", "space"),
    "nucleolus": ("#CDBDEE", "#8D74C4", "object"),
    "chromatin": ("#B9A6E3", "#8068B8", "object"),
    "mitochondrion": ("#F9C8B6", "#D9765A", "object"),
    "matrix": ("#FCE3D8", "#D9765A", "space"),
    "er": ("#CFE5F5", "#6FA8D6", "object"),
    "golgi": ("#FBE2A4", "#D8A73A", "object"),
    "lysosome": ("#F6C6D9", "#C76A93", "object"),
    "peroxisome": ("#D8EFC8", "#7CB45E", "object"),
    "vesicle": ("#FCE8C8", "#D9A35C", "object"),
    "chloroplast": ("#BFE3A5", "#5E9E44", "object"),
    "thylakoid": ("#8CCB70", "#4C8A33", "object"),
    "vacuole": ("#E2F1F8", "#8CBCD3", "space"),
    "bacterium": ("#CFE8C4", "#6FA55C", "object"),
    "virus": ("#F4B6C2", "#BF6276", "object"),
    "blood": ("#E86A6A", "#A93636", "object"),
    "plant": ("#A9D58C", "#5E9644", "object"),
    # flower organs (floral diagrams, plant morphology)
    "sepal": ("#B5D99A", "#5E9644", "object"),
    "petal": ("#F4A9C4", "#C4517E", "object"),
    "tepal": ("#E9B8E0", "#A1559A", "object"),
    "anther": ("#F8D46B", "#C29A1E", "object"),
    "ovary": ("#CFE7B5", "#6E9E4A", "object"),
    "ovule": ("#FBE7C6", "#C9A066", "object"),
    "bract": ("#D3E2AE", "#86A04A", "object"),
    "animal": ("#E9C9A8", "#B08055", "object"),
    "neuron": ("#F7D08A", "#C2913A", "object"),
    "muscle": ("#F2A0A0", "#B85A5A", "object"),
    "bone": ("#F1E7D0", "#B9A67E", "object"),
    # semantic
    "positive": ("#7CCB8E", "#2E9E5B", "object"),  # activation, gain, wild type
    "negative": ("#F29A9A", "#D64545", "object"),  # inhibition, loss, mutant
    "highlight": ("#FFE08A", "#D9A400", "object"),
    "neutral": ("#D5DAE1", "#8A94A3", "object"),
}

# Explicit dark-theme fills for compartments whose automatic tint would look muddy.
DARK_FILL = {"cytoplasm": "#1f2a40", "extracellular": "#162036", "matrix": "#5e4148", "vacuole": "#1d3346"}

# Ordered colours for anonymous proteins/categories (distinct, soft, colour-blind aware order).
PROTEIN_CYCLE = ["protein", "enzyme", "receptor", "antibody", "channel", "drug", "carbohydrate", "metabolite"]

# Standard schemes (fills) for sequences: nucleotides as in sequence logos, amino acids by property.
NUCLEOTIDE = {"A": "#57B65F", "C": "#4E8FD6", "G": "#F2A93B", "T": "#E5544F", "U": "#E5544F", "N": "#A0A7B2"}
AMINO_ACID_CLASS = {
    "hydrophobic": ("#8FB8E8", "GAVLIMPFW"),  # Lehninger-style: nonpolar aliphatic + F, W
    "polar": ("#8FD29A", "STCNQY"),
    "positive": ("#F28C8C", "KRH"),
    "negative": ("#C9A2FF", "DE"),
}


def is_dark() -> bool:
    return to_hex(mpl.rcParams["figure.facecolor"]).lower() == DARK_SURFACE


def mix(a, b, t):
    """Blend colour a towards b by t (0..1)."""
    ra, rb = to_rgb(a), to_rgb(b)
    return to_hex(tuple(x + (y - x) * t for x, y in zip(ra, rb)))


def _safe(c):
    # keep clear of the renderer's near-white / near-black recolouring thresholds
    r, g, b = to_rgb(c)
    if min(r, g, b) > 0.94:
        return mix(c, "#9aa4b2", 0.06)
    if max(r, g, b) < 0.11:
        return mix(c, "#ffffff", 0.08)
    return to_hex((r, g, b))


# Semantic names that share another token's colours until they need their own. Scripts name what
# they draw (``"actin"``, ``"mhc"``); giving an alias its own colour later is a one-line change here.
ALIASES = {
    "actin": "muscle", "myosin": "protein",
    "mhc": "protein", "mhc_b": "enzyme", "b2m": "metabolite", "tcr_a": "channel", "tcr_b": "dna2",
    "cd3": "neutral", "cd4": "drug", "cd8": "positive", "peptide": "highlight",
}


def _token(name):
    name = ALIASES.get(name, name)
    if name in TOKENS:
        return TOKENS[name]
    if name.startswith("#"):
        return (name, mix(name, "#1f2937", 0.35), "object")
    raise KeyError(f"unknown colour token {name!r}; see wikibio.palette.TOKENS")


def fill(name) -> str:
    f, e, kind = _token(name)
    if is_dark() and kind == "space":
        return _safe(DARK_FILL.get(name) or mix(e, DARK_SURFACE, 0.72))
    return _safe(f)


def _luminance(c):
    r, g, b = (((v / 12.92) if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4) for v in to_rgb(c))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def edge(name) -> str:
    """Outline colour. In the dark theme it stays darker than the fill (so outlines of overlapping
    objects remain visible) but is lifted towards the fill until it stands off the dark background;
    compartments keep their light-theme outline, which reads well on their dark tints."""
    f, e, kind = _token(name)
    if not is_dark():
        return _safe(e)
    if kind == "space":
        return _safe(e)
    c, t = mix(e, f, 0.25), 0.25
    while _luminance(c) < 0.16 and t < 0.9:
        t += 0.1
        c = mix(e, f, t)
    return _safe(c)


def light(name) -> str:
    """A paler shade of the fill, for highlights and inner regions."""
    f, e, kind = _token(name)
    base = fill(name)
    return _safe(mix(base, DARK_SURFACE, 0.35) if is_dark() and kind == "space" else mix(base, "#ffffff", 0.45))


def ink() -> str:
    """Text and line colour (labels, arrows, leaders)."""
    return "#e2e8f0" if is_dark() else "#2b2f36"


def on_fill() -> str:
    """Text colour on top of an object fill (object fills stay pastel in both themes, so always dark)."""
    return "#2b2f36"


def muted() -> str:
    """Secondary text and guide lines."""
    return "#94a3b8" if is_dark() else "#6b7280"


def surface() -> str:
    return DARK_SURFACE if is_dark() else "#ffffff"


def protein(i: int) -> str:
    """The token name of the i-th anonymous protein colour."""
    return PROTEIN_CYCLE[i % len(PROTEIN_CYCLE)]
