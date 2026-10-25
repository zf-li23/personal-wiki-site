"""Glycan diagrams in the Symbol Nomenclature for Glycans (SNFG; Varki et al., Glycobiology 25:1323,
2015; current table at the NCBI SNFG page, Neelamegham et al., Glycobiology 29:620, 2019).

Each monosaccharide is a coloured shape: the shape gives the class (hexose circle, HexNAc square,
hexosamine diagonally divided square, hexuronate divided diamond, deoxyhexose triangle, pentose star,
nonulosonate diamond, ketohexose pentagon, ...) and the colour the stereochemistry (gluco blue, manno
green, galacto yellow, ...). The SNFG colours are part of the standard and therefore fixed constants
here (``COLORS``); outlines, linkage lines and text follow the palette, so the figures work in both themes.

    from wikibio import glycan as G
    G.symbol(ax, "GlcNAc", (2, 3))                                  # one symbol, returns its centre
    g = G.draw(ax, "Neu5Ac(a2-3)Gal(b1-4)[Fuc(a1-3)]GlcNAc(b1-", at=(8, 3), aglycone="R")
    g.xy(0)                                                        # centre of the first residue written
    G.n_glycan(ax, (10, 2), kind="complex")                        # textbook structures, see below
    G.legend(ax, (1, 1), ["Glc", "Gal", "Man", "GlcNAc", "GalNAc", "Fuc", "Neu5Ac", "Xyl"])

Structures are written in IUPAC condensed notation, non-reducing end first and the reducing end last;
a branch is a bracketed chain written before the residue it is attached to (``Man(a1-6)[Man(a1-3)]Man``).
Linkages are ``(a1-4)``, ``(b1-3)``, ``(a2-6)`` (``a``/``b`` or ``α``/``β``); a trailing ``(b1-`` on the
last residue is its bond to the aglycone. A modification written after the name (``Man6P``, ``GlcNAc6S``,
``GalNAc4S``) is drawn as a small label beside the symbol.

The layout follows SNFG practice: the reducing end on the right (``direction="left"`` grows the chain
leftwards; ``"up"``, ``"down"`` and ``"right"`` rotate it), the branch with the higher linkage position
above (the α1-6 arm of N-glycans on top), and fucose drawn beside its parent, off the main axis.
Linkage labels read ``β1–4`` (``labels="full"``), ``β4`` (``"short"``) or are omitted (``None``).

Textbook structures: ``n_glycan(kind="core" | "high-mannose" | "hybrid" | "complex")``,
``o_glycan(core=1..4 or "Tn" / "sialyl-Tn")``, ``abo(kind="H" | "A" | "B")`` and
``lewis(kind="x" | "sLex" | "a" | "b")``; each takes the same placement arguments as ``draw``.
All functions are deterministic and return the drawn ``Glycan`` (anchors for arrows and callouts).
"""

import math
import re

import numpy as np
from matplotlib.patches import Circle, Polygon

from . import palette as P
from .core import LINE, label

# SNFG colours (RGB values of the standard's CMYK definitions). White is kept just below the
# renderer's near-white threshold, so that it stays white in the dark theme.
COLORS = {
    "white": "#F0F0F0",
    "blue": "#0072BC",
    "green": "#00A651",
    "yellow": "#FFD400",
    "light_blue": "#8FCCE9",
    "pink": "#F69EA1",
    "purple": "#A54399",
    "brown": "#A17A4D",
    "orange": "#F47920",
    "red": "#ED1C24",
}

# name: (shape, colour); divided shapes use the colour for the coloured half and white for the other.
MONOSACCHARIDES = {
    # hexoses: circle
    "Hex": ("circle", "white"), "Glc": ("circle", "blue"), "Man": ("circle", "green"), "Gal": ("circle", "yellow"),
    "Gul": ("circle", "orange"), "Alt": ("circle", "pink"), "All": ("circle", "purple"), "Tal": ("circle", "light_blue"),
    "Ido": ("circle", "brown"),
    # N-acetylhexosamines: square
    "HexNAc": ("square", "white"), "GlcNAc": ("square", "blue"), "ManNAc": ("square", "green"),
    "GalNAc": ("square", "yellow"), "GulNAc": ("square", "orange"), "AltNAc": ("square", "pink"),
    "AllNAc": ("square", "purple"), "TalNAc": ("square", "light_blue"), "IdoNAc": ("square", "brown"),
    # hexosamines: diagonally divided square
    "HexN": ("divided_square", "white"), "GlcN": ("divided_square", "blue"), "ManN": ("divided_square", "green"),
    "GalN": ("divided_square", "yellow"),
    # hexuronates: horizontally divided diamond (L-iduronate and L-altruronate inverted)
    "HexA": ("divided_diamond", "white"), "GlcA": ("divided_diamond", "blue"), "ManA": ("divided_diamond", "green"),
    "GalA": ("divided_diamond", "yellow"), "GulA": ("divided_diamond", "orange"),
    "AltA": ("divided_diamond_inv", "pink"), "IdoA": ("divided_diamond_inv", "brown"),
    # deoxyhexoses: triangle
    "dHex": ("triangle", "white"), "Qui": ("triangle", "blue"), "Rha": ("triangle", "green"), "Fuc": ("triangle", "red"),
    # dideoxyhexoses: flat rectangle
    "ddHex": ("flat_rect", "white"), "Oli": ("flat_rect", "blue"), "Tyv": ("flat_rect", "green"),
    "Abe": ("flat_rect", "orange"), "Par": ("flat_rect", "pink"), "Dig": ("flat_rect", "purple"),
    "Col": ("flat_rect", "light_blue"),
    # pentoses: star
    "Pen": ("star", "white"), "Ara": ("star", "green"), "Lyx": ("star", "yellow"), "Xyl": ("star", "orange"),
    "Rib": ("star", "pink"),
    # nonulosonates (sialic acids): diamond
    "Nonu": ("diamond", "white"), "Kdn": ("diamond", "green"), "Neu5Ac": ("diamond", "purple"),
    "Neu5Gc": ("diamond", "light_blue"), "Neu": ("diamond", "brown"), "Sia": ("diamond", "red"),
    # assigned (flat hexagon)
    "Bac": ("hexagon", "blue"), "LDManHep": ("hexagon", "green"), "Kdo": ("hexagon", "yellow"),
    "Dha": ("hexagon", "orange"), "DDManHep": ("hexagon", "pink"), "MurNAc": ("hexagon", "purple"),
    "MurNGc": ("hexagon", "light_blue"), "Mur": ("hexagon", "brown"),
    # ketohexoses: pentagon
    "Tag": ("pentagon", "yellow"), "Sor": ("pentagon", "orange"), "Psi": ("pentagon", "pink"), "Fru": ("pentagon", "green"),
}

ALIASES = {"NeuAc": "Neu5Ac", "NeuGc": "Neu5Gc", "Mur2Ac": "MurNAc"}

# residues drawn beside their parent (off the main axis), as in the usual drawings of fucosylated glycans
SIDE = {"Fuc"}


def _resolve(name):
    """(base name, modification text) for a residue name such as 'Man6P' or 'GlcNAc6S'."""
    name = ALIASES.get(name, name)
    if name in MONOSACCHARIDES:
        return name, ""
    for base in sorted(MONOSACCHARIDES, key=len, reverse=True):
        if name.startswith(base) and re.fullmatch(r"(\d?[SP]|\d?Ac|\d?Me)+", name[len(base):]):
            return base, name[len(base):]
    raise KeyError(f"unknown monosaccharide {name!r}; see wikibio.glycan.MONOSACCHARIDES")


def _outline():
    return P.ink()


def _regular(n, r, rot=90.0):
    t = np.radians(rot + np.arange(n) * 360.0 / n)
    return np.c_[r * np.cos(t), r * np.sin(t)]


def symbol(ax, name, xy, size=0.5, lw=None, zorder=12, mod=True):
    """Draw the SNFG symbol of ``name`` centred at ``xy`` (``size`` = width of a square/circle).

    Returns the centre as an array. ``mod=False`` suppresses the modification label of names like 'Man6P'.
    """
    base, extra = _resolve(name)
    shp, col = MONOSACCHARIDES[base]
    c = np.asarray(xy, float)
    h = size / 2
    fill, white = COLORS[col], COLORS["white"]
    lw = LINE * 0.75 if lw is None else lw
    edge = _outline()

    def poly(v, fc):
        ax.add_patch(Polygon(c + np.asarray(v), closed=True, facecolor=fc, edgecolor=edge, lw=lw, joinstyle="miter",
                             zorder=zorder))

    def half(v, fc):  # a coloured part without outline (the outline is drawn once around the whole shape)
        ax.add_patch(Polygon(c + np.asarray(v), closed=True, facecolor=fc, edgecolor="none", lw=0, zorder=zorder))

    def frame(v):
        ax.add_patch(Polygon(c + np.asarray(v), closed=True, fill=False, edgecolor=edge, lw=lw, joinstyle="miter",
                             zorder=zorder + 0.1))

    if shp == "circle":
        ax.add_patch(Circle(c, h * 1.05, facecolor=fill, edgecolor=edge, lw=lw, zorder=zorder))
    elif shp == "square":
        poly([(-h, -h), (h, -h), (h, h), (-h, h)], fill)
    elif shp == "divided_square":
        sq = [(-h, -h), (h, -h), (h, h), (-h, h)]
        half([(-h, -h), (h, h), (-h, h)], fill)  # upper-left half coloured
        half([(-h, -h), (h, -h), (h, h)], white)
        ax.plot([c[0] - h, c[0] + h], [c[1] - h, c[1] + h], color=edge, lw=lw * 0.8, zorder=zorder + 0.1)
        frame(sq)
    elif shp in ("diamond", "divided_diamond", "divided_diamond_inv"):
        r = h * 1.25
        dia = [(0, r), (r, 0), (0, -r), (-r, 0)]
        if shp == "diamond":
            poly(dia, fill)
        else:
            top, bottom = [(-r, 0), (0, r), (r, 0)], [(-r, 0), (r, 0), (0, -r)]
            inv = shp.endswith("_inv")
            half(top, white if inv else fill)
            half(bottom, fill if inv else white)
            ax.plot([c[0] - r, c[0] + r], [c[1], c[1]], color=edge, lw=lw * 0.8, zorder=zorder + 0.1)
            frame(dia)
    elif shp == "triangle":
        poly([(-h * 1.1, -h * 0.9), (h * 1.1, -h * 0.9), (0, h * 1.05)], fill)
    elif shp == "flat_rect":
        poly([(-h * 1.1, -h * 0.5), (h * 1.1, -h * 0.5), (h * 1.1, h * 0.5), (-h * 1.1, h * 0.5)], fill)
    elif shp == "star":
        outer, inner = _regular(5, h * 1.2), _regular(5, h * 0.5, rot=90 + 36)
        v = np.empty((10, 2))
        v[0::2], v[1::2] = outer, inner
        poly(v - [0, h * 0.08], fill)
    elif shp == "hexagon":
        poly([(-h * 1.2, 0), (-h * 0.65, h * 0.65), (h * 0.65, h * 0.65), (h * 1.2, 0), (h * 0.65, -h * 0.65),
              (-h * 0.65, -h * 0.65)], fill)
    elif shp == "pentagon":
        poly(_regular(5, h * 1.1) - [0, h * 0.06], fill)
    else:  # pragma: no cover
        raise ValueError(shp)
    if mod and extra:
        label(ax, c + [h * 0.95, h * 0.95], extra, size="tiny", ha="left", va="bottom", zorder=zorder + 1)
    return c


# ---------------------------------------------------------------------------------------------
# parsing IUPAC condensed notation

_TOKEN = re.compile(r"\s*(\[|\]|([A-Za-z][A-Za-z0-9]*)(\(([abαβ?])(\d|\?)-(\d|\?)?\)?)?)")


class Residue:
    """One monosaccharide of a parsed glycan: name, link to its parent and children."""

    def __init__(self, name, anomer=None, child_pos=None, parent_pos=None, index=0):
        self.name = name
        self.anomer = {"a": "α", "b": "β"}.get(anomer, anomer)
        self.child_pos = child_pos
        self.parent_pos = parent_pos
        self.index = index
        self.children = []
        self.parent = None
        self.xy = None

    def link_text(self, style="full"):
        if not self.anomer or style is None:
            return ""
        if style == "short":
            return f"{self.anomer}{self.parent_pos or ''}"
        return f"{self.anomer}{self.child_pos or '?'}–{self.parent_pos or ''}"


def parse(text):
    """Parse IUPAC condensed notation into a tree; returns (root residue, residues in written order)."""
    tokens, pos = [], 0
    while pos < len(text.rstrip()):
        m = _TOKEN.match(text, pos)
        if not m or m.end() == pos:
            raise ValueError(f"cannot parse glycan {text!r} at {text[pos:]!r}")
        pos = m.end()
        if m.group(1) in "[]":
            tokens.append(m.group(1))
        else:
            tokens.append(Residue(m.group(2), m.group(4), m.group(5), m.group(6), index=sum(isinstance(t, Residue) for t in tokens)))
    residues = [t for t in tokens if isinstance(t, Residue)]

    def build(i):
        node = tokens[i]
        i -= 1
        while i >= 0:
            t = tokens[i]
            if t == "]":
                child, i = build(i - 1)
                if i < 0 or tokens[i] != "[":
                    raise ValueError(f"unbalanced brackets in {text!r}")
                child.parent = node
                node.children.append(child)
                i -= 1
            elif t == "[":
                return node, i
            else:
                child, i = build(i)
                child.parent = node
                node.children.append(child)
                return node, i
        return node, i

    if not isinstance(tokens[-1], Residue):
        raise ValueError(f"glycan {text!r} must end with its reducing-end residue")
    root, i = build(len(tokens) - 1)
    if i >= 0:
        raise ValueError(f"unbalanced brackets in {text!r}")
    return root, residues


# ---------------------------------------------------------------------------------------------
# layout and drawing

_DIRS = {"left": ((-1, 0), (0, 1)), "right": ((1, 0), (0, 1)), "up": ((0, 1), (-1, 0)), "down": ((0, -1), (1, 0))}


def _key(r):
    p = r.parent_pos
    return -(int(p) if p and p.isdigit() else 0)


class Glycan:
    """A drawn glycan: residues (written order) with their centres; anchors for arrows and callouts."""

    def __init__(self, root, residues, stub=None):
        self.root = root
        self.residues = residues
        self.stub = stub  # end of the line to the aglycone, if drawn

    def xy(self, i):
        """Centre of the i-th residue as written in the notation (0 = first, non-reducing end)."""
        return np.asarray(self.residues[i].xy, float)

    def find(self, name, n=0):
        """Centre of the n-th residue with this name (written order)."""
        hits = [r for r in self.residues if r.name == name]
        return np.asarray(hits[n].xy, float)

    @property
    def reducing_end(self):
        return np.asarray(self.root.xy, float)

    def bounds(self):
        """(xmin, ymin, xmax, ymax) of the residue centres (and the aglycone stub)."""
        pts = np.array([r.xy for r in self.residues] + ([self.stub] if self.stub is not None else []), float)
        return (*pts.min(axis=0), *pts.max(axis=0))


def _layout(root, step, row):
    """Residue coordinates in a local frame: main axis u (towards the non-reducing end), cross axis v."""
    rows = [0]

    def place(node, depth):
        chain = sorted([c for c in node.children if c.name not in SIDE], key=_key)
        side = [c for c in node.children if c.name in SIDE]
        if not chain:
            v = -rows[0] * row
            rows[0] += 1
        else:
            vs = [place(c, depth + 1) for c in chain]
            v = (vs[0] + vs[-1]) / 2
        node._uv = (depth * step, v)
        for k, s in enumerate(side):
            s._uv = (depth * step, v + (-1 if k % 2 == 0 else 1) * row * 0.85)
            s._side = True
            for c in s.children:  # residues beyond a side residue (rare): continue along the main axis
                place(c, depth + 1)
        return v

    place(root, 0)


def draw(ax, text, at=(0, 0), direction="left", step=1.15, row=1.0, size=0.5, labels="full", aglycone=None,
         stub=0.75, label_size="tiny", zorder=12):
    """Draw a glycan written in IUPAC condensed notation with its reducing end at ``at``.

    ``direction`` is the direction of growth towards the non-reducing end; ``step`` the distance between
    linked residues, ``row`` between branches; ``aglycone`` writes a label (e.g. "Asn", "Ser/Thr", "Cer")
    at the end of a short line from the reducing end. Returns a ``Glycan``.
    """
    root, residues = parse(text)
    _layout(root, step, row)
    (ux, uy), (vx, vy) = _DIRS[direction]
    v0 = root._uv[1]  # the reducing end sits at `at`
    a = np.asarray(at, float)
    for r in residues:
        u, v = r._uv
        v -= v0
        r.xy = a + u * np.array([ux, uy]) + v * np.array([vx, vy])
    edge = _outline()
    for r in residues:
        if r.parent is None:
            continue
        p, q = np.asarray(r.parent.xy), np.asarray(r.xy)
        ax.plot([p[0], q[0]], [p[1], q[1]], color=edge, lw=LINE * 0.75, zorder=zorder - 1, solid_capstyle="round")
        t = r.link_text(labels)
        if t:
            d = q - p
            d = d / (np.linalg.norm(d) or 1)
            uvec, vvec = np.array([ux, uy], float), np.array([vx, vy], float)
            n = np.array([-d[1], d[0]])
            if abs(d @ uvec) > 0.99:  # along the main axis: label on the upper (or +v) side
                ref = np.array([0.0, 1.0]) if abs(vy) > 0.5 else vvec
            elif abs(d @ vvec) > 0.99:  # perpendicular (side residues): label towards the reducing end
                ref = -uvec
            else:  # a branch: label on its outer side
                ref = vvec * np.sign(d @ vvec)
            if n @ ref < 0:
                n = -n
            if abs(n[0]) > abs(n[1]):
                ha, va = ("left" if n[0] > 0 else "right"), "center"
            else:
                ha, va = "center", ("bottom" if n[1] > 0 else "top")
            m = (p + q) / 2 + n * 0.09
            label(ax, m, t, size=label_size, color=P.muted(), zorder=zorder + 1, ha=ha, va=va)
    end = None
    if aglycone is not None or root.anomer:
        end = np.asarray(root.xy) - stub * np.array([ux, uy])
        ax.plot([root.xy[0], end[0]], [root.xy[1], end[1]], color=edge, lw=LINE * 0.75, zorder=zorder - 1)
        if root.anomer and labels:
            mid = (np.asarray(root.xy) + end) / 2
            label(ax, mid + np.array([vx, vy]) * 0.17 * (1 if vy >= 0 else -1), f"{root.anomer}{root.child_pos or ''}",
                  size=label_size, color=P.muted(), zorder=zorder + 1)
        if aglycone:
            ha = {"left": "left", "right": "right"}.get(direction, "center")
            off = -0.12 * np.array([ux, uy])
            va = "top" if direction == "up" else "bottom" if direction == "down" else "center"
            label(ax, end + off, aglycone, size="small", ha=ha, va=va, zorder=zorder + 1)
    for r in residues:
        symbol(ax, r.name, r.xy, size=size, zorder=zorder)
    return Glycan(root, residues, end)


# ---------------------------------------------------------------------------------------------
# textbook structures

N_GLYCANS = {
    "core": "Man(a1-6)[Man(a1-3)]Man(b1-4)GlcNAc(b1-4)GlcNAc(b1-",
    "high-mannose": ("Man(a1-2)Man(a1-6)[Man(a1-2)Man(a1-3)]Man(a1-6)[Man(a1-2)Man(a1-2)Man(a1-3)]"
                     "Man(b1-4)GlcNAc(b1-4)GlcNAc(b1-"),
    "hybrid": "Man(a1-6)[Man(a1-3)]Man(a1-6)[Gal(b1-4)GlcNAc(b1-2)Man(a1-3)]Man(b1-4)GlcNAc(b1-4)GlcNAc(b1-",
    "complex": ("Neu5Ac(a2-6)Gal(b1-4)GlcNAc(b1-2)Man(a1-6)[Neu5Ac(a2-6)Gal(b1-4)GlcNAc(b1-2)Man(a1-3)]"
                "Man(b1-4)GlcNAc(b1-4)[Fuc(a1-6)]GlcNAc(b1-"),
}

O_GLYCANS = {
    "Tn": "GalNAc(a1-",
    "sialyl-Tn": "Neu5Ac(a2-6)GalNAc(a1-",
    1: "Gal(b1-3)GalNAc(a1-",
    2: "Gal(b1-3)[GlcNAc(b1-6)]GalNAc(a1-",
    3: "GlcNAc(b1-3)GalNAc(a1-",
    4: "GlcNAc(b1-6)[GlcNAc(b1-3)]GalNAc(a1-",
}

# blood-group antigens on a type 2 chain (Gal(b1-4)GlcNAc), as on erythrocyte glycolipids and glycoproteins
ABO = {
    "H": "Fuc(a1-2)Gal(b1-4)GlcNAc(b1-",
    "A": "GalNAc(a1-3)[Fuc(a1-2)]Gal(b1-4)GlcNAc(b1-",
    "B": "Gal(a1-3)[Fuc(a1-2)]Gal(b1-4)GlcNAc(b1-",
}

LEWIS = {
    "x": "Gal(b1-4)[Fuc(a1-3)]GlcNAc(b1-",
    "sLex": "Neu5Ac(a2-3)Gal(b1-4)[Fuc(a1-3)]GlcNAc(b1-",
    "a": "Gal(b1-3)[Fuc(a1-4)]GlcNAc(b1-",
    "b": "Fuc(a1-2)Gal(b1-3)[Fuc(a1-4)]GlcNAc(b1-",
}


def n_glycan(ax, at, kind="complex", aglycone="Asn", **kw):
    """An N-linked glycan on Asn: the common core ('core'), 'high-mannose' (Man9GlcNAc2), 'hybrid', or
    'complex' (biantennary, disialylated, core-fucosylated)."""
    return draw(ax, N_GLYCANS[kind], at=at, aglycone=aglycone, **kw)


def o_glycan(ax, at, core=1, aglycone="Ser/Thr", **kw):
    """A mucin-type O-glycan on Ser/Thr: cores 1-4, the Tn antigen ('Tn') or sialyl-Tn ('sialyl-Tn')."""
    return draw(ax, O_GLYCANS[core], at=at, aglycone=aglycone, **kw)


def abo(ax, at, kind="A", aglycone="R", **kw):
    """The H (blood group O), A or B antigen on a type 2 precursor chain."""
    return draw(ax, ABO[kind], at=at, aglycone=aglycone, **kw)


def lewis(ax, at, kind="sLex", aglycone="R", **kw):
    """Lewis antigens: 'x', 'sLex' (sialyl Lewis x, the selectin ligand), 'a', 'b' (H. pylori adhesin ligand)."""
    return draw(ax, LEWIS[kind], at=at, aglycone=aglycone, **kw)


def legend(ax, at, names, cols=1, dx=2.6, dy=0.75, size=0.42, text=None, label_size="small"):
    """A key of symbols with their names, filled column by column from ``at`` (top-left entry).

    ``text`` maps a name to the label printed (default: the name itself). Returns the entry centres.
    """
    out = {}
    per = math.ceil(len(names) / cols)
    x0, y0 = at
    for k, name in enumerate(names):
        i, j = divmod(k, per)
        c = (x0 + i * dx, y0 - j * dy)
        symbol(ax, name, c, size=size)
        label(ax, (c[0] + size * 0.95, c[1]), (text or {}).get(name, name), size=label_size, ha="left")
        out[name] = np.asarray(c, float)
    return out


__all__ = ["COLORS", "MONOSACCHARIDES", "symbol", "parse", "draw", "Glycan", "Residue", "n_glycan", "o_glycan", "abo",
           "lewis", "legend", "N_GLYCANS", "O_GLYCANS", "ABO", "LEWIS"]

