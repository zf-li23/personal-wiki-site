"""Animal morphology sheets: realistic templates (``wikimedia/...`` icons with named parts) laid out as
labelled specimens, homology rows and comparison tables, plus two native comparative schematics
(vertebrate hearts and brains) drawn in one consistent view so classes can be compared side by side.

    from wikibio import animalmorph as AM
    s = AM.Specimen("wikimedia/grasshopper", at=(8, 5), height=4)          # placement, nothing drawn yet
    s.draw(ax, parts={"forewing": "plant"}, mute="neutral")                 # = bio.icon(...)
    AM.callouts(ax, [(s.point("antenna"), "Antenna", "left"), (s.frac(0.5, 0.9), "Wing", "right")],
                left=2.0, right=14.0)
    AM.homology_row(ax, [("wikimedia/forelimb-human", "Human"), ...], parts=AM.FORELIMB, y=2, height=6, x=[2, 6, 10])
    AM.part_legend(ax, (1, 1), AM.FORELIMB, names={"humerus": "Humerus", ...})
    AM.table(ax, (0.5, 12), col_w=[3, 2, 2], row_h=[0.8, 1.6], cells=[[...], ...])
    AM.symmetry(ax, (x, y), "radial")          # glyphs for comparison sheets (also germ_layers, segmentation)
    AM.heart(ax, (x, y), 2.0, "amphibian")     # chambers coloured by blood oxygenation
    AM.brain(ax, (x, y), 3.0, "bird")          # dorsal view, regions coloured consistently

Icon ids must appear as string literals in the plot script (the build caches figures and prints the
attributions from them); this module only forwards the ids it is given. Every drawing function returns
anchors (dicts of canvas points) for callouts.
"""

import math

import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, PathPatch, Polygon
from matplotlib.path import Path

from . import palette as P
from .core import LINE, blob, callout, label, smooth_closed
from .icons import icon as _icon
from .icons import icon_part as _icon_part
from .icons import parts as _icon_parts

# --------------------------------------------------------------------------- colour roles
# Homologous parts share a colour in every figure, the same as in the parametric drawings of ``zoomorph``
# (palette aliases for bones, mouthparts and leg segments; one place to change them).
FORELIMB = {"humerus": "humerus", "radius": "radius", "ulna": "ulna", "carpals": "carpals",
            "metacarpals-phalanges": "metacarpals"}
MOUTHPARTS = {"labrum": "labrum", "mandible": "mandible", "maxilla": "maxilla", "labium": "labium"}
LEG = {"coxa": "coxa", "trochanter": "trochanter", "femur": "femur", "tibia": "tibia", "tarsus": "tarsus",
       "pretarsus": "tarsus"}
TAGMA = {"head": "receptor", "thorax": "enzyme", "abdomen": "antibody", "cephalothorax": "protein"}
# blood: oxygenated, deoxygenated, mixed (dedicated tokens requested; see the gallery report)
BLOOD = {"oxy": "blood", "deoxy": "channel", "mixed": "protein"}
BRAIN = {"olfactory-bulb": "petal", "cerebrum": "positive", "optic-lobe": "highlight", "cerebellum": "channel",
         "medulla": "neutral", "diencephalon": "golgi"}


# --------------------------------------------------------------------------- templates


class Specimen:
    """A template icon placement: holds the ``bio.icon`` arguments so the drawing and points on its parts
    agree. ``draw`` draws it (keywords go to ``bio.icon``: parts, mute, hide, color, alpha, zorder);
    ``point(part, where)`` is a point on a named part; ``frac(fx, fy)`` a point at fractions of the drawn
    box (y up); ``box`` is (x, y, w, h) after ``draw``."""

    def __init__(self, icon_id, at, height=None, width=None, anchor="center", flip=False, rotate=0.0):
        self.icon_id, self.at, self.anchor, self.flip, self.rotate = icon_id, tuple(at), anchor, flip, rotate
        self.height = height if width is None else 1.0
        self.width = width
        self.box = None

    def _kw(self):
        return dict(at=self.at, height=self.height, width=self.width, anchor=self.anchor, flip=self.flip, rotate=self.rotate)

    def draw(self, ax, **kw):
        self.box = _icon(ax, self.icon_id, **self._kw(), **kw)
        return self.box

    def point(self, part, where="center"):
        return _icon_part(self.icon_id, part, where=where, **self._kw())

    def frac(self, fx, fy):
        if self.box is None:
            raise RuntimeError("draw the specimen before asking for fractional points")
        x, y, w, h = self.box
        return (x + fx * w, y + fy * h)


def callouts(ax, items, left=None, right=None, gap=0.42, size="small", top=None, bottom=None, color=None):
    """Leader-line labels in a column left and/or right of a drawing, ordered by the height of their points
    so leaders do not cross, and pushed apart to at least ``gap``. ``items``: (point, text, side) tuples or
    dicts with point, text, side and an optional fixed ``y``. ``top``/``bottom`` clamp the columns.
    Returns {text: label position}."""
    rows = []
    for it in items:
        if isinstance(it, dict):
            rows.append((tuple(it["point"]), it["text"], it.get("side", "right"), it.get("y")))
        else:
            rows.append((tuple(it[0]), it[1], it[2], None))
    out = {}
    for side, x in (("left", left), ("right", right)):
        sel = [r for r in rows if r[2] == side]
        if not sel:
            continue
        if x is None:
            raise ValueError(f"callouts: no x for the {side} column")
        sel.sort(key=lambda r: -(r[3] if r[3] is not None else r[0][1]))
        ys = [r[3] if r[3] is not None else r[0][1] for r in sel]
        fixed = [r[3] is not None for r in sel]
        for _ in range(4):
            for i in range(1, len(ys)):
                if ys[i - 1] - ys[i] < gap and not fixed[i]:
                    ys[i] = ys[i - 1] - gap
            if top is not None and ys[0] > top:
                d = ys[0] - top
                ys = [y - d if not f else y for y, f in zip(ys, fixed)]
            if bottom is not None and ys[-1] < bottom:
                d = bottom - ys[-1]
                ys = [y + d if not f else y for y, f in zip(ys, fixed)]
                for i in range(len(ys) - 2, -1, -1):
                    if ys[i] - ys[i + 1] < gap and not fixed[i]:
                        ys[i] = ys[i + 1] + gap
        for (p, t, _, _), y in zip(sel, ys):
            callout(ax, p, (x, y), t, size=size, color=color)
            out[t] = (x, y)
    return out


def homology_row(ax, items, parts, y, height, x, mute="neutral", title_size="normal", title_gap=0.35, italic=False,
                 widths=None, anchor="bottom", keep=()):
    """Templates side by side with the same parts coloured by the same tokens (homology, analogy, tagmata):
    ``items`` = [(icon_id, title), ...] or dicts (icon, title, subtitle, flip, rotate, height); ``parts`` maps part
    names to tokens; drawings stand on the line ``y`` (``anchor="bottom"``) at the x positions ``x``. Parts
    named in ``keep`` (e.g. an outline) are drawn in their original colours instead of being muted.
    Returns the list of ``Specimen`` objects (drawn)."""
    out = []
    for k, it in enumerate(items):
        if not isinstance(it, dict):
            it = dict(icon=it[0], title=it[1])
        h = it.get("height", height)
        w = widths[k] if widths else None
        s = Specimen(it["icon"], at=(x[k], y), height=h if w is None else None, width=w, anchor=anchor,
                     flip=it.get("flip", False), rotate=it.get("rotate", 0.0))
        s.draw(ax, parts={p: t for p, t in parts.items()}, mute=mute, hide=list(keep))
        if keep:
            other = [q for q in _icon_parts(it["icon"]) if q not in keep]
            _icon(ax, it["icon"], **s._kw(), hide=other, zorder=10.5)
        bx, by, bw, bh = s.box
        if it.get("title"):
            label(ax, (bx + bw / 2, by - title_gap), it["title"], size=title_size, bold=not italic, italic=italic, va="top")
        if it.get("subtitle"):
            label(ax, (bx + bw / 2, by - title_gap - 0.45), it["subtitle"], size="small", color=P.muted(), va="top",
                  italic=it.get("subtitle_italic", False))
        out.append(s)
    return out


def part_legend(ax, xy, parts, names=None, step=None, size="small", swatch=0.34, vertical=False, gap=0.5):
    """A key of part colours starting at ``xy`` (left end, vertical centre of the row). ``names`` maps part
    names to display text (default: the part name capitalised). Rows advance by ``step`` (default: text width
    estimate) or, with ``vertical=True``, downwards by ``gap``. Returns the end x (or y)."""
    x, y = xy
    for p, tok in parts.items():
        text = (names or {}).get(p, p.replace("-", " ").capitalize())
        ax.add_patch(FancyBboxPatch((x, y - swatch / 2), swatch, swatch, boxstyle="round,pad=0,rounding_size=0.06",
                                    facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, zorder=20))
        label(ax, (x + swatch + 0.15, y), text, size=size, ha="left")
        if vertical:
            y -= gap
        else:
            x += step if step else swatch + 0.5 + 0.16 * len(text)
    return y if vertical else x


def bracket(ax, a, b, text, side=1, depth=0.18, size="small", color=None, offset=0.12, bold=False, token=None):
    """A square bracket from a to b (horizontal or vertical) with a label outside: marks a body region
    (tagma), a series of stages or a column group. ``side`` +1 puts the bracket above / right of the segment.
    With ``token`` the bracket is a coloured bar instead (tagma colour key)."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    d = b - a
    horizontal = abs(d[0]) >= abs(d[1])
    n = np.array([0.0, 1.0]) if horizontal else np.array([1.0, 0.0])
    n = n * side
    c = color or P.muted()
    if token:
        w = depth * 0.9
        q = [a, b, b + n * w, a + n * w]
        ax.add_patch(Polygon(q, closed=True, facecolor=P.fill(token), edgecolor=P.edge(token), lw=0.8, zorder=14))
        mid = (a + b) / 2 + n * (w + offset)
    else:
        pts = np.array([a, a + n * depth, b + n * depth, b])
        ax.plot(pts[:, 0], pts[:, 1], color=c, lw=0.9, zorder=14, solid_joinstyle="miter")
        mid = (a + b) / 2 + n * (depth + offset)
    if horizontal:
        label(ax, mid, text, size=size, va="bottom" if side > 0 else "top", bold=bold)
    else:
        label(ax, mid, text, size=size, ha="left" if side > 0 else "right", bold=bold)
    return tuple(mid)


def table(ax, origin, col_w, row_h, cells, header_rows=1, header_cols=1, size="small", band=True, align=None):
    """A comparison sheet. ``cells[r][c]`` is text, None or a callable ``draw(ax, box)`` with box = (x0, y0, w, h);
    ``origin`` is the top-left corner. Header row/column text is bold; alternate body rows get a faint band.
    ``align`` per column: "left" / "center" (default: header column left, others centred).
    Returns the cell boxes [[(x0, y0, w, h), ...], ...]."""
    ox, oy = origin
    xs = np.r_[ox, ox + np.cumsum(col_w)]
    ys = np.r_[oy, oy - np.cumsum(row_h)]
    boxes = []
    for r, row in enumerate(cells):
        brow = []
        if band and r >= header_rows and (r - header_rows) % 2 == 1:
            ax.add_patch(Polygon([(xs[0], ys[r + 1]), (xs[-1], ys[r + 1]), (xs[-1], ys[r]), (xs[0], ys[r])], closed=True,
                                 facecolor=P.mix(P.surface(), P.muted(), 0.09), lw=0, zorder=0))
        for c, v in enumerate(row):
            bx = (xs[c], ys[r + 1], xs[c + 1] - xs[c], ys[r] - ys[r + 1])
            brow.append(bx)
            if v is None:
                continue
            if callable(v):
                v(ax, bx)
                continue
            a = (align or {}).get(c, "left" if c < header_cols else "center")
            bold = r < header_rows or c < header_cols
            x = bx[0] + 0.12 if a == "left" else bx[0] + bx[2] / 2
            label(ax, (x, bx[1] + bx[3] / 2), v, size=size, bold=bold, ha=a)
        boxes.append(brow)
    for k in (0, header_rows, len(ys) - 1):
        ax.plot([xs[0], xs[-1]], [ys[k], ys[k]], color=P.muted(), lw=0.9 if k != header_rows else 0.7, zorder=2)
    return boxes


# --------------------------------------------------------------------------- character glyphs


def _ring(ax, c, r_out, r_in, face, edge, lw=0.8, zorder=12):
    t = np.linspace(0, 2 * np.pi, 90)
    outer = np.c_[c[0] + r_out * np.cos(t), c[1] + r_out * np.sin(t)]
    verts, codes = [outer], [Path.MOVETO] + [Path.LINETO] * (len(outer) - 2) + [Path.CLOSEPOLY]
    if r_in > 0:
        inner = np.c_[c[0] + r_in * np.cos(t[::-1]), c[1] + r_in * np.sin(t[::-1])]
        verts.append(inner)
        codes += [Path.MOVETO] + [Path.LINETO] * (len(inner) - 2) + [Path.CLOSEPOLY]
    ax.add_patch(PathPatch(Path(np.vstack(verts), codes), facecolor=face, edgecolor=edge, lw=lw, zorder=zorder))


def symmetry(ax, center, kind, r=0.32, token="animal", zorder=12):
    """Body symmetry glyph: "none" (irregular outline), "radial" (disc with many planes), "biradial"
    (two planes), "pentaradial" (five-armed star), "bilateral" (one mirror plane, head end up)."""
    cx, cy = center
    fc, ec = P.fill(token), P.edge(token)
    planes = []
    if kind == "none":
        pts = blob(center, r, r * 0.8, wobble=0.28, seed=5, k=8)
        ax.add_patch(Polygon(pts, closed=True, facecolor=fc, edgecolor=ec, lw=0.9, zorder=zorder))
    elif kind in ("radial", "biradial"):
        ax.add_patch(Circle(center, r, facecolor=fc, edgecolor=ec, lw=0.9, zorder=zorder))
        planes = [0, 45, 90, 135] if kind == "radial" else [0, 90]
        if kind == "biradial":
            ax.add_patch(Ellipse(center, 0.7 * r, 0.35 * r, facecolor=P.light(token), edgecolor=ec, lw=0.6, zorder=zorder + 1))
    elif kind == "pentaradial":
        th = np.pi / 2 + np.arange(10) * np.pi / 5
        rr = np.where(np.arange(10) % 2 == 0, r * 1.05, r * 0.42)
        ax.add_patch(Polygon(np.c_[cx + rr * np.cos(th), cy + rr * np.sin(th)], closed=True, facecolor=fc, edgecolor=ec,
                             lw=0.9, zorder=zorder, joinstyle="round"))
        planes = [90 + k * 36 for k in range(5)]
    elif kind == "bilateral":
        t = np.linspace(0, 2 * np.pi, 80)
        w = 0.55 * r * (1 + 0.25 * np.sin(t))  # broader at the head end
        ax.add_patch(Polygon(np.c_[cx + w * np.cos(t), cy + r * np.sin(t)], closed=True, facecolor=fc, edgecolor=ec, lw=0.9,
                             zorder=zorder))
        planes = [90]
    else:
        raise ValueError(f"unknown symmetry {kind!r}")
    for a in planes:
        u = np.array([math.cos(math.radians(a)), math.sin(math.radians(a))]) * r * 1.25
        ax.plot([cx - u[0], cx + u[0]], [cy - u[1], cy + u[1]], color=P.ink(), lw=0.7, ls=(0, (2.2, 1.6)), zorder=zorder + 2)
    return {"center": tuple(center), "r": r}


def germ_layers(ax, center, n, r=0.3, zorder=12):
    """Germ-layer glyph: concentric rings in the germ-layer colours (ectoderm blue, mesoderm red, endoderm
    yellow; zoology.GERM). ``n`` = 0 (no true tissues: a dashed open circle), 2 (diploblastic) or 3."""
    if n == 0:
        ax.add_patch(Circle(center, r, fill=False, edgecolor=P.muted(), lw=0.9, ls=(0, (2, 1.6)), zorder=zorder))
        return {"center": tuple(center)}
    layers = ["ectoderm", "endoderm"] if n == 2 else ["ectoderm", "mesoderm", "endoderm"]
    radii = np.linspace(r, r * 0.35, len(layers) + 1)
    for k, lay in enumerate(layers):
        _ring(ax, center, radii[k], radii[k + 1], P.fill(lay), P.edge(lay), lw=0.6, zorder=zorder + k)
    return {"center": tuple(center)}


def segmentation(ax, center, segmented, w=0.9, h=0.3, token="animal", n=5, zorder=12):
    """Segmentation glyph: a worm-like body of ``n`` repeated units (``segmented=True``), one undivided unit
    (False), or with ``segmented="tagmata"`` segments fused into three groups."""
    cx, cy = center
    x0 = cx - w / 2
    if segmented is True or segmented == "tagmata":
        groups = [[0], [1, 2], [3, 4]] if segmented == "tagmata" else [[k] for k in range(n)]
        m = n if segmented is True else 5
        sw = w / m
        toks = ["receptor", "enzyme", "antibody"] if segmented == "tagmata" else [token] * len(groups)
        for g, tok in zip(groups, toks):
            a, b = x0 + g[0] * sw, x0 + (g[-1] + 1) * sw
            ax.add_patch(FancyBboxPatch((a + 0.015, cy - h / 2), b - a - 0.03, h, boxstyle=f"round,pad=0,rounding_size={h * 0.4}",
                                        facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, zorder=zorder))
            for k in g[1:]:
                xx = x0 + k * sw
                ax.plot([xx, xx], [cy - h * 0.38, cy + h * 0.38], color=P.edge(tok), lw=0.6, zorder=zorder + 1)
    else:
        ax.add_patch(FancyBboxPatch((x0, cy - h / 2), w, h, boxstyle=f"round,pad=0,rounding_size={h * 0.45}",
                                    facecolor=P.fill(token), edgecolor=P.edge(token), lw=0.8, zorder=zorder))
    return {"center": tuple(center)}


# --------------------------------------------------------------------------- vertebrate hearts


def _blob(ax, c, rx, ry, token, zorder, lw=LINE * 0.8, angle=0.0, alpha=None):
    ax.add_patch(Ellipse(c, 2 * rx, 2 * ry, angle=angle, facecolor=P.fill(token), edgecolor=P.edge(token), lw=lw,
                         zorder=zorder, alpha=alpha))


def _vessel(ax, pts, token, w=0.16, zorder=6):
    pts = np.asarray(pts, float)
    ax.plot(pts[:, 0], pts[:, 1], color=P.edge(token), lw=w * 72 * 0.45 + 1.6, solid_capstyle="round", zorder=zorder)
    ax.plot(pts[:, 0], pts[:, 1], color=P.fill(token), lw=w * 72 * 0.45, solid_capstyle="round", zorder=zorder + 0.5)


def heart(ax, center, size, kind, labels=True, size_text="tiny", zorder=6):
    """A schematic vertebrate heart in ventral view (the animal's right on the viewer's left), chambers
    coloured by the blood they carry: deoxygenated (blue), oxygenated (red), mixed (purple; ``BLOOD``).

    kind: "fish" (sinus venosus, atrium, ventricle, bulbus arteriosus in series; deoxygenated blood only,
    pumped to the gills), "amphibian" (two atria, one undivided trabeculated ventricle, conus arteriosus),
    "reptile" (two atria, ventricle partly divided by an incomplete septum), "crocodilian" (four chambers;
    left and right aortae connected by the foramen of Panizza), "bird" / "mammal" (four chambers, complete
    septum; the systemic arch is the right one in birds, the left one in mammals).
    ``size`` is the heart height. Returns anchors of the chambers ("ra", "la", "v", "rv", "lv", "atrium",
    "sinus", "bulbus", "conus", "aorta", "septum", "panizza") present in that kind; chamber labels are the
    abbreviations RA, LA, V, RV, LV and, for the fish, SV (sinus venosus), A, V, B (bulbus arteriosus).
    """
    cx, cy = center
    s = size / 2.0
    A = {}
    oxy, deo, mix = BLOOD["oxy"], BLOOD["deoxy"], BLOOD["mixed"]
    T = lambda x, y: (cx + x * s, cy + y * s)  # noqa: E731
    if kind == "fish":
        # chambers in series, blood flowing right to left: sinus venosus -> atrium -> ventricle -> bulbus
        _vessel(ax, [T(1.45, 0.45), T(1.15, 0.2)], deo, w=0.16 * s, zorder=zorder - 1)
        _blob(ax, T(0.95, 0.1), 0.26 * s, 0.22 * s, deo, zorder)
        _blob(ax, T(0.38, 0.32), 0.42 * s, 0.32 * s, deo, zorder + 1)
        _blob(ax, T(-0.3, -0.25), 0.55 * s, 0.45 * s, deo, zorder + 2)
        _blob(ax, T(-1.0, 0.1), 0.28 * s, 0.19 * s, deo, zorder + 3, angle=25)
        _vessel(ax, [T(-1.2, 0.2), T(-1.5, 0.55)], deo, w=0.16 * s, zorder=zorder - 1)
        A.update(sinus=T(0.95, 0.1), atrium=T(0.38, 0.32), v=T(-0.3, -0.25), bulbus=T(-1.0, 0.1))
        names = dict(sinus="SV", atrium="A", v="V", bulbus="B")
    else:
        four = kind in ("crocodilian", "bird", "mammal")
        # atria on top, ventricle(s) below; viewer's left = animal's right = deoxygenated side
        _blob(ax, T(-0.52, 0.55), 0.42 * s, 0.32 * s, deo, zorder + 1)
        _blob(ax, T(0.52, 0.55), 0.38 * s, 0.3 * s, oxy, zorder + 1)
        A.update(ra=T(-0.52, 0.55), la=T(0.52, 0.55))
        vt = [(-0.85, 0.22), (0.85, 0.22), (0.78, -0.45), (0.0, -1.0), (-0.78, -0.45)]
        vpts = smooth_closed(np.array([T(*p) for p in vt]), n=160)
        if four:
            # complete septum: two ventricles
            left = vpts[vpts[:, 0] <= cx + 1e-9]
            right = vpts[vpts[:, 0] >= cx - 1e-9]
            for half, tok in ((left, deo), (right, oxy)):
                ax.add_patch(Polygon(half, closed=True, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=LINE * 0.8,
                                     zorder=zorder))
            ax.plot([cx, cx], [cy + 0.2 * s, cy - 0.98 * s], color=P.ink(), lw=LINE * 1.2, zorder=zorder + 2)
            A.update(rv=T(-0.4, -0.35), lv=T(0.4, -0.35), septum=T(0.0, -0.5))
        else:
            tok = mix
            ax.add_patch(Polygon(vpts, closed=True, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=LINE * 0.8, zorder=zorder))
            # tint the two sides: blood stays partly separated (strongly so in reptiles)
            sep = 0.45 if kind == "reptile" else 0.18
            for sgn, t2 in ((-1, deo), (1, oxy)):
                ax.add_patch(Ellipse(T(sgn * 0.42, -0.25), 0.7 * s, 0.9 * s, facecolor=P.fill(t2), lw=0, zorder=zorder + 0.5,
                                     alpha=sep))
            if kind == "reptile":
                ax.plot([cx, cx], [cy - 0.95 * s, cy - 0.2 * s], color=P.ink(), lw=LINE * 1.2, zorder=zorder + 2)
                A["septum"] = T(0.0, -0.55)
            else:  # amphibian: trabeculae
                for k in range(-3, 4):
                    x = 0.17 * k
                    ax.plot([cx + x * s, cx + x * 0.8 * s], [cy - 0.05 * s, cy - (0.62 - 0.06 * abs(k)) * s], color=P.edge(tok),
                            lw=0.6, zorder=zorder + 1)
            A["v"] = T(0.0, -0.4)
        # outflow
        if kind in ("amphibian",):
            _vessel(ax, [T(0.05, 0.1), T(0.05, 0.75), T(0.15, 1.15)], mix, w=0.2 * s, zorder=zorder - 1)
            A["conus"] = T(0.08, 0.9)
        elif kind in ("reptile", "crocodilian"):
            # pulmonary trunk from the right side; two aortae crossing
            _vessel(ax, [T(-0.25, 0.1), T(-0.35, 0.7), T(-0.7, 1.15)], deo, w=0.16 * s, zorder=zorder - 1)
            la_tok = oxy if kind == "crocodilian" else mix
            _vessel(ax, [T(0.15, 0.1), T(0.0, 0.8), T(-0.25, 1.2)], oxy, w=0.16 * s, zorder=zorder - 1)
            _vessel(ax, [T(-0.05, 0.1), T(0.15, 0.8), T(0.4, 1.2)], la_tok if kind == "reptile" else deo, w=0.16 * s,
                    zorder=zorder - 1.2)
            A["aorta"] = T(0.0, 0.85)
            if kind == "crocodilian":
                ax.add_patch(Circle(T(0.07, 0.62), 0.07 * s, facecolor=P.surface(), edgecolor=P.ink(), lw=0.8, zorder=zorder + 3))
                A["panizza"] = T(0.07, 0.62)
        else:  # bird / mammal
            _vessel(ax, [T(-0.2, 0.1), T(-0.2, 0.75), T(-0.6, 1.05)], deo, w=0.17 * s, zorder=zorder - 1)
            sgn = -1 if kind == "bird" else 1  # systemic arch: right (viewer's left) in birds, left in mammals
            arch = [T(0.18, 0.1), T(0.12, 0.85), T(sgn * 0.35, 1.15), T(sgn * 0.75, 0.95), T(sgn * 0.85, 0.55)]
            _vessel(ax, arch, oxy, w=0.18 * s, zorder=zorder - 0.8)
            A["aorta"] = T(sgn * 0.6, 1.05)
        names = dict(ra="RA", la="LA", v="V", rv="RV", lv="LV")
    if labels:
        for k, t in names.items():
            if k in A:
                label(ax, A[k], t, size=size_text, color=P.on_fill(), zorder=zorder + 20)
    return A


# --------------------------------------------------------------------------- vertebrate brains

# Dorsal-view proportions (length along the axis, half-width) of the brain regions by class, after the
# classical comparative series (Romer & Parsons; Butler & Hodos): midbrain optic lobes dominate in fishes,
# the cerebellum is tiny in amphibians, the cerebrum grows through reptiles to birds and mammals, where it
# covers the midbrain (and in mammals is folded into gyri); birds have large lateral optic lobes and a big,
# foliated cerebellum; olfactory bulbs shrink in birds.
_BRAIN = {
    "fish": [("olfactory-bulb", 0.14, 0.09), ("cerebrum", 0.2, 0.15), ("optic-lobe", 0.27, 0.21), ("cerebellum", 0.2, 0.15),
             ("medulla", 0.3, 0.12)],
    "amphibian": [("olfactory-bulb", 0.16, 0.09), ("cerebrum", 0.3, 0.16), ("optic-lobe", 0.2, 0.15),
                  ("cerebellum", 0.06, 0.12), ("medulla", 0.3, 0.11)],
    "reptile": [("olfactory-bulb", 0.16, 0.08), ("cerebrum", 0.32, 0.22), ("optic-lobe", 0.18, 0.16),
                ("cerebellum", 0.12, 0.13), ("medulla", 0.26, 0.11)],
    "bird": [("olfactory-bulb", 0.06, 0.05), ("cerebrum", 0.45, 0.26), ("optic-lobe", 0.0, 0.0), ("cerebellum", 0.22, 0.13),
             ("medulla", 0.22, 0.1)],
    "mammal": [("olfactory-bulb", 0.1, 0.07), ("cerebrum", 0.62, 0.29), ("optic-lobe", 0.0, 0.0), ("cerebellum", 0.24, 0.19),
               ("medulla", 0.16, 0.09)],
}


def brain(ax, center, length, cls, labels=False, size_text="tiny", zorder=6):
    """A vertebrate brain in dorsal view (rostral end up), regions coloured by ``BRAIN`` so classes can be
    compared: olfactory bulbs, cerebrum (telencephalon), optic lobes (midbrain tectum), cerebellum, medulla.
    ``cls``: "fish", "amphibian", "reptile", "bird", "mammal" (proportions in ``_BRAIN``; birds draw lateral
    optic lobes, mammals a gyrified cerebrum that covers the midbrain). ``length`` is the drawn length of
    the brain. Returns {region: point on it, "top", "bottom"}."""
    cx, cy = center
    regs = _BRAIN[cls]
    tot = sum(r[1] for r in regs)
    k = length / tot  # lengths are normalised to the drawn length
    wk = length / 1.7  # widths share one scale for all classes, so proportions stay comparable
    y = cy + length / 2
    A = {"top": (cx, y)}
    for name, ln, hw in regs:
        if ln == 0:
            continue
        L, W = ln * k, hw * wk
        yc = y - L / 2
        tok = BRAIN[name]
        if name == "medulla":
            pts = np.array([(cx - W, y + 0.05 * L), (cx + W, y + 0.05 * L), (cx + W * 0.55, y - L), (cx - W * 0.55, y - L)])
            ax.add_patch(Polygon(smooth_closed(pts, n=80), closed=True, facecolor=P.fill(tok), edgecolor=P.edge(tok),
                                 lw=LINE * 0.8, zorder=zorder))
            cw = W * 0.4
            ax.add_patch(Polygon([(cx - cw, y - L + 0.05 * L), (cx + cw, y - L + 0.05 * L), (cx + cw * 0.9, y - 1.35 * L),
                                  (cx - cw * 0.9, y - 1.35 * L)], closed=True, facecolor=P.fill(tok), edgecolor=P.edge(tok),
                                 lw=LINE * 0.8, zorder=zorder - 1))
            A["medulla"] = (cx, yc)
            A["spinal-cord"] = (cx, y - L - 0.25 * L)
        elif name == "cerebellum":
            _blob(ax, (cx, yc), W, L / 2 * 1.15, tok, zorder + 3)
            folds = 5 if cls in ("bird", "mammal") else 0
            for f in range(folds):
                yy = yc - L / 2 * 0.8 + f * L * 0.8 / max(folds - 1, 1)
                ww = W * math.sqrt(max(0.0, 1 - ((yy - yc) / (L / 2 * 1.15)) ** 2)) * 0.85
                ax.plot([cx - ww, cx + ww], [yy, yy], color=P.edge(tok), lw=0.6, zorder=zorder + 4)
            A["cerebellum"] = (cx, yc)
        else:  # paired structures
            for sgn in (-1, 1):
                ex = cx + sgn * W * 0.52
                _blob(ax, (ex, yc), W * 0.52, L / 2 * 1.05, tok, zorder + (5 if name == "cerebrum" else 2))
                if name == "cerebrum" and cls == "mammal":
                    # sulci: gently curved transverse lines, mirrored on the two hemispheres
                    for f in (-0.5, -0.1, 0.3, 0.65):
                        t = np.linspace(-0.8, 0.8, 20)
                        xs = ex + sgn * W * 0.45 * t
                        ys = yc + L / 2 * (f + 0.12 * np.cos(t * 2.2) - 0.05 * sgn * t)
                        ax.plot(xs, ys, color=P.edge(tok), lw=0.7, zorder=zorder + 6)
            A[name] = (cx + W * 0.52, yc)
        y -= L
        if name == "cerebrum" and cls == "bird":
            # optic lobes bulge laterally beneath the cerebrum's caudal edge
            tok2 = BRAIN["optic-lobe"]
            for sgn in (-1, 1):
                _blob(ax, (cx + sgn * hw * wk * 0.92, y + 0.03 * k), 0.09 * wk, 0.1 * k, tok2, zorder + 4)
            A["optic-lobe"] = (cx + hw * wk * 0.92, y + 0.03 * k)
    A["bottom"] = (cx, y)
    if labels:
        names = {"olfactory-bulb": "Olfactory bulb", "cerebrum": "Cerebrum", "optic-lobe": "Optic lobe",
                 "cerebellum": "Cerebellum", "medulla": "Medulla"}
        for k2, t in names.items():
            if k2 in A:
                label(ax, A[k2], t, size=size_text, color=P.on_fill(), zorder=zorder + 20)
    return A


__all__ = ["FORELIMB", "MOUTHPARTS", "LEG", "TAGMA", "BLOOD", "BRAIN", "Specimen", "callouts", "homology_row", "part_legend",
           "bracket", "table", "symmetry", "germ_layers", "segmentation", "heart", "brain"]
