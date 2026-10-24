"""Network diagrams in SBGN notation (Systems Biology Graphical Notation, sbgn.github.io).

A ``Diagram`` is a small scene: create nodes with ids and positions, then connect them by id.
Arcs are routed between node centres and clipped at the node outlines, so they attach to borders;
arrowheads stop a hair short of the outline so the head never merges into it.

    from wikibio import network
    fig, ax = bio.canvas(12, 6)
    d = network.Diagram(ax)
    d.compartment("cyt", (0.3, 0.3, 11.7, 5.7), "Cytoplasm")
    d.macromolecule("mek", (2, 3), "MEK", states=["P", "P"])
    d.macromolecule("erk", (5, 3), "ERK")
    d.macromolecule("erkp", (9, 3), "ERK", states=["P", "P"])
    d.reaction(["erk"], ["erkp"], modifiers=[("mek", "catalysis")])

Process Description (PD) nodes
    macromolecule (rounded rectangle), simple_chemical (circle), nucleic_acid (bottom-rounded
    rectangle), unspecified (ellipse), perturbation (notched rectangle), complex (cut-corner box
    around member nodes), compartment (thick rounded container), process (small square with two
    ports; also association / dissociation / omitted / uncertain), empty (source / sink, the empty set).
    Decorations: state variables (``states``: small stadiums on the border, "P" for a phosphorylated
    site, "" for an unmodified one) and units of information (``units``: small boxes, "ct:gene",
    "mt:prot", "N:2" for a multimer).
Activity Flow (AF) nodes
    activity (rectangle, optional units of information), phenotype (hexagon), logic (AND / OR / NOT
    circle with two ports).
Arc kinds (``connect(kind=...)``)
    PD: consumption, production, catalysis, stimulation, inhibition, necessary, modulation
    AF: positive, negative, unknown, necessary, logic
    (and the core kinds process, activation, link)

Helpers: ``cascade`` (ligand → receptor → kinases → transcription factor → gene inside a cell) and
``motif`` (gene-regulatory network motifs: ffl, nar, par, toggle, repressilator).
"""

import math

import numpy as np
from matplotlib.font_manager import FontProperties
from matplotlib.patches import PathPatch, Polygon
from matplotlib.path import Path
from matplotlib.textpath import TextPath

from . import palette as P
from .cell import bilayer, membrane
from .core import FONT, LINE, arrow, label

# arc kind -> drawing kind (core.arrow kinds, plus "diamond")
ARC = {
    "consumption": "link", "production": "process", "catalysis": "catalysis", "stimulation": "activation",
    "inhibition": "inhibition", "necessary": "necessary", "modulation": "diamond",
    "positive": "activation", "negative": "inhibition", "unknown": "diamond", "logic": "link", "equivalence": "link",
    "process": "process", "activation": "activation", "link": "link",
}
_HEADLESS = {"link"}
zorder_label = 6

# positions of decorations on a node's bounding box, as fractions of the half-width / half-height
POS = {"t": (0, 1), "tl": (-0.55, 1), "tr": (0.55, 1), "b": (0, -1), "bl": (-0.55, -1), "br": (0.55, -1),
       "l": (-1, 0), "r": (1, 0)}


# ---------------------------------------------------------------------------------------------
# geometry helpers


def units_per_point(ax):
    """Data units per typographic point on a ``bio.canvas`` axes (fonts and line widths are in points)."""
    fig = ax.figure
    w_in = fig.get_figwidth() * ax.get_position().width
    x0, x1 = ax.get_xlim()
    return abs(x1 - x0) / (w_in * 72)


def text_extent(ax, text, size="normal", italic=False, bold=False):
    """(width, height) of a label in data units."""
    if not text:
        return 0.0, 0.0
    fp = FontProperties(size=FONT.get(size, size), style="italic" if italic else "normal", weight="bold" if bold else "normal")
    ext = TextPath((0, 0), text, prop=fp).get_extents()
    u = units_per_point(ax)
    return ext.width * u, ext.height * u


def _roundrect(cx, cy, w, h, r, rounded=(True, True, True, True), n=12):
    """Vertices of a rectangle with rounded corners (order: bottom-right, top-right, top-left, bottom-left)."""
    x0, x1, y0, y1 = cx - w / 2, cx + w / 2, cy - h / 2, cy + h / 2
    r = max(0.0, min(r, w / 2, h / 2))
    out = []
    corners = ((x1, y0, -1, 1, -90), (x1, y1, -1, -1, 0), (x0, y1, 1, -1, 90), (x0, y0, 1, 1, 180))
    for (px, py, sx, sy, a0), rd in zip(corners, rounded):
        if rd and r > 0:
            c = (px + sx * r, py + sy * r)
            t = np.radians(np.linspace(a0, a0 + 90, n))
            out.extend(np.c_[c[0] + r * np.cos(t), c[1] + r * np.sin(t)])
        else:
            out.append((px, py))
    return np.array(out, float)


def _ellipse(cx, cy, w, h, n=72):
    t = np.linspace(0, 2 * np.pi, n, endpoint=False)
    return np.c_[cx + w / 2 * np.cos(t), cy + h / 2 * np.sin(t)]


def _octagon(cx, cy, w, h, c):
    x0, x1, y0, y1 = cx - w / 2, cx + w / 2, cy - h / 2, cy + h / 2
    c = min(c, w / 2, h / 2)
    return np.array([(x0 + c, y0), (x1 - c, y0), (x1, y0 + c), (x1, y1 - c), (x1 - c, y1), (x0 + c, y1), (x0, y1 - c), (x0, y0 + c)])


def _hexagon(cx, cy, w, h):
    x0, x1, y0, y1 = cx - w / 2, cx + w / 2, cy - h / 2, cy + h / 2
    k = min(h * 0.45, w / 3)
    return np.array([(x0, cy), (x0 + k, y0), (x1 - k, y0), (x1, cy), (x1 - k, y1), (x0 + k, y1)])


def _notched(cx, cy, w, h):
    # SBGN perturbing agent: a rectangle whose left and right sides are notched inwards
    x0, x1, y0, y1 = cx - w / 2, cx + w / 2, cy - h / 2, cy + h / 2
    k = h * 0.35
    return np.array([(x0, y0), (x1, y0), (x1 - k, cy), (x1, y1), (x0, y1), (x0 + k, cy)])


def container_edge(token):
    """Outline / label colour of a compartment. ``P.edge`` lightens outlines for the dark theme, which turns
    the pale compartment tokens almost white; containers keep a muted version of their own hue instead."""
    if P.is_dark() and token in P.TOKENS and P.TOKENS[token][2] == "space":
        return P.mix(P.TOKENS[token][1], P.surface(), 0.15)
    return P.edge(token)


def _closed_path(v):
    v = np.asarray(v, float)
    return Path(np.vstack([v, v[:1]]), closed=True)


def _cumlen(pts):
    return np.r_[0, np.cumsum(np.hypot(*np.diff(pts, axis=0).T))]


def _trim(pts, start=0.0, end=0.0):
    """Cut ``start`` units of arc length from the beginning of a polyline and ``end`` from its end."""
    s = _cumlen(pts)
    total = s[-1]
    a, b = start, total - end
    if b - a < total * 0.05:
        a, b = total * 0.45, total * 0.55
    keep = (s > a) & (s < b)

    def at(t):
        return np.array([np.interp(t, s, pts[:, 0]), np.interp(t, s, pts[:, 1])])

    return np.vstack([at(a), pts[keep], at(b)])


def _quad(a, b, bend, n=120):
    a, b = np.asarray(a, float), np.asarray(b, float)
    d = b - a
    ctrl = (a + b) / 2 + bend * np.array([-d[1], d[0]])
    t = np.linspace(0, 1, n)[:, None]
    return (1 - t) ** 2 * a + 2 * (1 - t) * t * ctrl + t**2 * b


def _rounded_polyline(points, r, n=10):
    """A polyline through waypoints with corners rounded by radius ``r`` (elbow routing)."""
    p = [np.asarray(q, float) for q in points]
    out = [p[0]]
    for i in range(1, len(p) - 1):
        a, c, b = p[i - 1], p[i], p[i + 1]
        la, lb = np.linalg.norm(c - a), np.linalg.norm(b - c)
        rr = min(r, la / 2, lb / 2)
        if rr < 1e-6:
            out.append(c)
            continue
        s, e = c + (a - c) / la * rr, c + (b - c) / lb * rr
        for t in np.linspace(0, 1, n):
            out.append((1 - t) ** 2 * s + 2 * (1 - t) * t * c + t**2 * e)
    out.append(p[-1])
    # densify straight runs so that clipping against outlines is precise
    dense = [out[0]]
    for q0, q1 in zip(out[:-1], out[1:]):
        k = max(2, int(np.linalg.norm(q1 - q0) / 0.03))
        dense.extend(q0 + (q1 - q0) * t for t in np.linspace(0, 1, k)[1:])
    return np.array(dense)


def _simplify(pts, tol=2e-4):
    """Douglas-Peucker: drop points within ``tol`` of the chord (straight runs become one segment, which
    keeps Agg from snapping parts of a nearly straight line to different pixels)."""
    pts = np.asarray(pts, float)
    if len(pts) < 3:
        return pts
    a, b = pts[0], pts[-1]
    d = b - a
    L = np.hypot(*d)
    rel = pts - a
    dist = np.abs(rel[:, 0] * d[1] - rel[:, 1] * d[0]) / L if L > 1e-12 else np.hypot(*rel.T)
    i = int(np.argmax(dist))
    if dist[i] <= tol:
        return np.vstack([a, b])
    return np.vstack([_simplify(pts[: i + 1], tol)[:-1], _simplify(pts[i:], tol)])


def _clip_start(pts, path):
    """Drop the leading part of a polyline that lies inside ``path``; the new first point is on the outline."""
    inside = path.contains_points(pts)
    if not inside[0]:
        return pts
    out = np.nonzero(~inside)[0]
    if len(out) == 0:
        return pts
    i = out[0]
    lo, hi = pts[i - 1], pts[i]
    for _ in range(30):
        mid = (lo + hi) / 2
        if path.contains_point(mid):
            lo = mid
        else:
            hi = mid
    return np.vstack([hi, pts[i:]])


def _clip_end(pts, path):
    return _clip_start(pts[::-1], path)[::-1]


# ---------------------------------------------------------------------------------------------
# nodes


class Node:
    """A diagram node: its outline (for arc clipping), bounding box and optional process ports."""

    def __init__(self, id, kind, center, w, h, outline, token=None):
        self.id, self.kind, self.token = id, kind, token
        self.center = np.asarray(center, float)
        self.w, self.h = w, h
        self.outline = np.asarray(outline, float)
        self.path = _closed_path(self.outline)
        self.ports = None  # (in_port, out_port) for process and logic nodes
        self.slots = []

    @property
    def bbox(self):
        x, y = self.center
        return (x - self.w / 2, y - self.h / 2, x + self.w / 2, y + self.h / 2)

    def point(self, pos):
        """A point on the node border: a name from POS ("tl", "b", …) or an angle in degrees."""
        x, y = self.center
        if isinstance(pos, str):
            fx, fy = POS[pos]
            if self.kind in ("chemical", "unspecified", "empty", "logic", "association", "dissociation"):
                a = math.atan2(fy, fx * 0.8)
                return np.array([x + self.w / 2 * math.cos(a), y + self.h / 2 * math.sin(a)])
            return np.array([x + fx * self.w / 2, y + fy * self.h / 2])
        a = math.radians(pos)
        far = self.center + 4 * max(self.w, self.h) * np.array([math.cos(a), math.sin(a)])
        ray = np.c_[np.linspace(x, far[0], 400), np.linspace(y, far[1], 400)]
        return _clip_start(ray, self.path)[0]


class Diagram:
    """An SBGN scene on a ``bio.canvas`` axes. Sizes default to the text and are in data units.

    ``scale`` enlarges every glyph (node height, decorations, arrowheads) relative to the default,
    which is tuned for ``FONT["normal"]`` labels.
    """

    def __init__(self, ax, scale=1.0, size="normal"):
        self.ax = ax
        self.nodes = {}
        self.u = units_per_point(ax) * scale  # data units per point, scaled
        self.size = size
        self.fs = FONT.get(size, size)
        self.head = 6.5 * self.u

    # -- generic -------------------------------------------------------------------------------

    def __getitem__(self, id):
        return self.nodes[id]

    def _auto_size(self, text, w, h, italic=False, size=None, pad=9.0, minw=2.2):
        h = h if h is not None else 2.35 * FONT.get(size or self.size, size or self.size) * self.u
        if w is None:
            tw, _ = text_extent(self.ax, text, size or self.size, italic=italic)
            w = max(tw + 2 * pad * self.u, minw * h)
        return w, h

    def _add(self, node):
        if node.id in self.nodes:
            raise ValueError(f"duplicate node id {node.id!r}")
        self.nodes[node.id] = node
        return node

    def _patch(self, outline, token, lw=LINE, zorder=11, fill=None, edge=None, dashed=False):
        self.ax.add_patch(PathPatch(_closed_path(outline), facecolor=fill or P.fill(token), edgecolor=edge or P.edge(token),
                                    lw=lw, zorder=zorder, joinstyle="round", ls=(0, (3, 2)) if dashed else "-"))

    def _text(self, xy, text, size=None, italic=False, color=None, zorder=13, bold=False, ha="center", va="center"):
        if text:
            label(self.ax, xy, text, size=size or self.size, italic=italic, bold=bold, color=color or P.on_fill(),
                  ha=ha, va=va, zorder=zorder)

    def _entity(self, id, kind, shape, at, text, w, h, token, italic, states, units, multimer, size, zorder, clone=False):
        w, h = self._auto_size(text, w, h, italic=italic, size=size, minw=1.0 if kind in ("chemical", "empty") else 2.2)
        if kind == "chemical":
            w = h = max(w, h)
        outline = shape(at[0], at[1], w, h)
        node = self._add(Node(id, kind, at, w, h, outline, token))
        if multimer:
            off = 3.2 * self.u
            self._patch(shape(at[0] + off, at[1] - off, w, h), token, lw=LINE * 0.9, zorder=zorder - 0.4)
            units = list(units or []) + [f"N:{multimer if multimer is not True else 2}"]
        self._patch(outline, token, lw=LINE * 0.9, zorder=zorder)
        if clone:
            self._clone_marker(node, token, zorder)
        self._text(at, text, size=size, italic=italic, zorder=zorder + 1)
        for item in units or []:
            self.unit(id, *((item,) if isinstance(item, str) else item))
        for item in states or []:
            self.state(id, *((item,) if isinstance(item, str) else item))
        return node

    def _clone_marker(self, node, token, zorder):
        # SBGN clone marker: the lower part of the glyph filled darker (the entity appears several times)
        x0, y0, x1, y1 = node.bbox
        clip = _closed_path(node.outline)
        band = np.array([(x0 - 1, y0 - 1), (x1 + 1, y0 - 1), (x1 + 1, y0 + node.h * 0.3), (x0 - 1, y0 + node.h * 0.3)])
        p = PathPatch(_closed_path(band), facecolor=P.edge(token), edgecolor="none", zorder=zorder + 0.2)
        self.ax.add_patch(p)
        p.set_clip_path(PathPatch(clip, transform=self.ax.transData))

    def _slot(self, node, pos, order):
        if pos is not None:
            return pos
        for name in order:
            if name not in node.slots:
                return name
        return order[0]

    # -- decorations ---------------------------------------------------------------------------

    def state(self, id, value="", pos=None, token="highlight"):
        """A state variable on node ``id``: a stadium on the border holding ``value`` ("P", "P@S338", "GTP";
        "" for an unmodified site). Filled with ``token`` when it has a value."""
        node = self.nodes[id]
        pos = self._slot(node, pos, ("tr", "br", "bl", "tl", "t", "b"))
        node.slots.append(pos)
        c = node.point(pos)
        tw, _ = text_extent(self.ax, value, "tiny")
        h = 10.5 * self.u
        w = max(h * 1.15, tw + 6 * self.u)
        filled = bool(value)
        self._patch(_roundrect(c[0], c[1], w, h, h / 2), token, lw=LINE * 0.75, zorder=14,
                    fill=P.fill(token) if filled else P.light(node.token or "neutral"),
                    edge=P.edge(token) if filled else P.edge(node.token or "neutral"))
        self._text(c, value, size="tiny", zorder=15)
        return c

    def unit(self, id, text, shape="rect", pos=None):
        """A unit of information on node ``id`` ("ct:gene", "mt:prot", "N:2"…). ``shape`` "rect" or, for AF
        activity nodes, the entity glyph: "macromolecule", "nucleic", "chemical", "complex". In ``units=[…]``
        lists an item is a string or a tuple ``(text, shape[, pos])``."""
        node = self.nodes[id]
        pos = self._slot(node, pos, ("tl", "bl", "t", "tr", "b", "br"))
        node.slots.append(pos)
        c = node.point(pos)
        tw, _ = text_extent(self.ax, text, "tiny")
        h = 10 * self.u
        w = max(h * 1.3, tw + 6 * self.u)
        shp = {"rect": lambda: _roundrect(c[0], c[1], w, h, 0.8 * self.u),
               "macromolecule": lambda: _roundrect(c[0], c[1], w, h, h * 0.3),
               "nucleic": lambda: _roundrect(c[0], c[1], w, h, h * 0.4, rounded=(True, False, False, True)),
               "chemical": lambda: _roundrect(c[0], c[1], w, h, h / 2),
               "complex": lambda: _octagon(c[0], c[1], w, h, h * 0.3)}[shape]()
        self._patch(shp, None, lw=LINE * 0.7, zorder=14, fill=P.light(node.token or "neutral"), edge=P.edge(node.token or "neutral"))
        self._text(c, text, size="tiny", zorder=15)
        return c

    # -- PD entity pool nodes ------------------------------------------------------------------

    def macromolecule(self, id, at, text, w=None, h=None, token="protein", states=(), units=(), multimer=0,
                      italic=False, size=None, clone=False, zorder=11):
        """SBGN macromolecule (protein, RNA as a whole molecule): a rounded rectangle.
        ``multimer=2`` draws the stacked multimer glyph with the unit "N:2"."""
        r = None

        def shape(x, y, ww, hh):
            return _roundrect(x, y, ww, hh, r if r is not None else hh * 0.28)

        return self._entity(id, "macromolecule", shape, at, text, w, h, token, italic, states, units, multimer, size, zorder, clone)

    def nucleic_acid(self, id, at, text, w=None, h=None, token="dna", states=(), units=(), multimer=0,
                     italic=True, size=None, clone=False, zorder=11):
        """SBGN nucleic acid feature (gene, promoter, mRNA): a rectangle with rounded bottom corners.
        Add ``units=["ct:gene"]`` or ``["ct:mRNA"]`` for the material type."""

        def shape(x, y, ww, hh):
            return _roundrect(x, y, ww, hh, hh * 0.38, rounded=(True, False, False, True))

        return self._entity(id, "nucleic", shape, at, text, w, h, token, italic, states, units, multimer, size, zorder, clone)

    def simple_chemical(self, id, at, text, r=None, token="metabolite", states=(), units=(), size="small", clone=False, zorder=11):
        """SBGN simple chemical (metabolite, second messenger, ion): a circle sized to its label."""
        d = 2 * r if r else None

        def shape(x, y, ww, hh):
            return _ellipse(x, y, ww, hh)

        w = d
        if d is None:
            tw, _ = text_extent(self.ax, text, size)
            w = max(tw + 6 * self.u, 2.35 * FONT.get(self.size, self.size) * self.u)
        return self._entity(id, "chemical", shape, at, text, w, w, token, False, states, units, 0, size, zorder, clone)

    def unspecified(self, id, at, text, w=None, h=None, token="neutral", size=None, zorder=11):
        """SBGN unspecified entity: an ellipse."""
        return self._entity(id, "unspecified", _ellipse, at, text, w, h, token, False, (), (), 0, size, zorder)

    def perturbation(self, id, at, text, w=None, h=None, token="drug", size=None, zorder=11):
        """SBGN perturbing agent (drug, heat, light): a rectangle notched on both sides."""
        return self._entity(id, "perturbation", _notched, at, text, w, h, token, False, (), (), 0, size, zorder)

    def complex(self, id, members, text=None, pad=None, token="neutral", states=(), units=(), label_pos="b", zorder=9):
        """SBGN complex: a cut-corner box drawn around already placed member nodes."""
        pad = pad if pad is not None else 7 * self.u
        boxes = np.array([self.nodes[m].bbox for m in members])
        x0, y0 = boxes[:, 0].min() - pad, boxes[:, 1].min() - pad
        x1, y1 = boxes[:, 2].max() + pad, boxes[:, 3].max() + pad
        th = 0.0
        if text:
            _, th = text_extent(self.ax, "Hg", "small")
            th += 4 * self.u
            if label_pos == "b":
                y0 -= th
            else:
                y1 += th
        cx, cy, w, h = (x0 + x1) / 2, (y0 + y1) / 2, x1 - x0, y1 - y0
        outline = _octagon(cx, cy, w, h, 7 * self.u)
        node = self._add(Node(id, "complex", (cx, cy), w, h, outline, token))
        self._patch(outline, token, lw=LINE * 0.9, zorder=zorder, fill=P.mix(P.fill(token), P.surface(), 0.55))
        if text:
            ty = y0 + th / 2 + 1.5 * self.u if label_pos == "b" else y1 - th / 2 - 1.5 * self.u
            self._text((cx, ty), text, size="small", color=P.ink(), zorder=zorder + 0.5)
        for item in units or []:
            self.unit(id, *((item,) if isinstance(item, str) else item))
        for item in states or []:
            self.state(id, *((item,) if isinstance(item, str) else item))
        return node

    def empty(self, id, at, r=None, zorder=11):
        """SBGN source / sink: the empty set (a circle crossed by a diagonal), for synthesis and degradation."""
        r = r or 7.5 * self.u
        outline = _ellipse(at[0], at[1], 2 * r, 2 * r)
        node = self._add(Node(id, "empty", at, 2 * r, 2 * r, outline, "neutral"))
        self._patch(outline, None, lw=LINE * 0.9, zorder=zorder, fill=P.surface(), edge=P.ink())
        k = r * 1.25
        self.ax.plot([at[0] - k * 0.7, at[0] + k * 0.7], [at[1] - k * 0.7, at[1] + k * 0.7], color=P.ink(), lw=LINE * 0.9,
                     zorder=zorder + 1, solid_capstyle="round")
        return node

    def compartment(self, id, box, text=None, token="cytoplasm", style="box", membrane_token="membrane",
                    label_pos="tl", radius=None, outline=None, zorder=2):
        """SBGN compartment: a container ``box=(x0, y0, x1, y1)`` (or any closed ``outline``).

        style "box" is the SBGN glyph (thick rounded border); "membrane" draws a cell membrane
        (``wikibio.cell.membrane``: filled region and a double contour, e.g. a nucleus with
        ``token="nucleus", membrane_token="nucleus"``).
        """
        if outline is None:
            x0, y0, x1, y1 = box
            r = radius if radius is not None else 14 * self.u
            outline = _roundrect((x0 + x1) / 2, (y0 + y1) / 2, x1 - x0, y1 - y0, r, n=40)
        o = np.asarray(outline, float)
        x0, y0 = o.min(axis=0)
        x1, y1 = o.max(axis=0)
        node = Node(id, "compartment", ((x0 + x1) / 2, (y0 + y1) / 2), x1 - x0, y1 - y0, o, token)
        self.nodes[id] = node
        if style == "box":
            self._patch(o, token, lw=LINE * 2.1, zorder=zorder, edge=container_edge(token))
        elif style == "membrane":
            dense = _rounded_polyline(np.vstack([o, o[:1]]), 0.0)
            if P.TOKENS.get(membrane_token, ("", "", "object"))[2] == "space":
                self._envelope(dense, token, membrane_token, 4 * self.u, zorder)
            else:
                membrane(self.ax, dense, inside=token, token=membrane_token, thickness=4 * self.u, zorder=zorder)
        else:
            raise ValueError(f"unknown compartment style {style!r}")
        if text:
            self.compartment_label(id, text, label_pos)
        return node

    def _envelope(self, outline, inside, token, thickness, zorder):
        # a double membrane (nuclear envelope) in a compartment token: like cell.membrane, but the contour
        # keeps the muted compartment hue in the dark theme (see container_edge)
        o = np.asarray(outline, float)
        if np.allclose(o[0], o[-1]):
            o = o[:-1]
        keep = np.r_[True, np.hypot(*np.diff(o, axis=0).T) > 1e-9]
        o = o[keep]
        seg = np.roll(o, -1, axis=0) - np.roll(o, 1, axis=0)  # periodic tangent: no seam at the start point
        seg /= np.linalg.norm(seg, axis=1)[:, None]
        nrm = np.c_[-seg[:, 1], seg[:, 0]] * thickness / 2
        lines = [o + nrm, o - nrm]

        def area(p):
            return abs(np.sum(p[:, 0] * np.roll(p[:, 1], -1) - np.roll(p[:, 0], -1) * p[:, 1])) / 2

        outer = max(lines, key=area)
        self.ax.add_patch(PathPatch(_closed_path(outer), facecolor=P.fill(inside), edgecolor="none", zorder=zorder))
        for e in lines:
            self.ax.add_patch(PathPatch(_closed_path(e), fill=False, edgecolor=container_edge(token), lw=LINE * 0.9,
                                        zorder=zorder + 1, joinstyle="round"))

    def compartment_label(self, id, text, pos="tl"):
        node = self.nodes[id]
        x0, y0, x1, y1 = node.bbox
        m = 11 * self.u
        x = {"l": x0 + m, "c": (x0 + x1) / 2, "r": x1 - m}[pos[1] if len(pos) > 1 else "c"]
        y = y1 - m if pos[0] == "t" else y0 + m
        ha = {"l": "left", "c": "center", "r": "right"}[pos[1] if len(pos) > 1 else "c"]
        label(self.ax, (x, y), text, size="small", bold=True, color=container_edge(node.token), ha=ha,
              va="top" if pos[0] == "t" else "bottom", zorder=zorder_label)

    def membrane_line(self, points, detailed=True):
        """A plasma membrane along a polyline: a detailed lipid bilayer (``wikibio.cell.bilayer``) or a plain band."""
        pts = np.asarray(points, float)
        if detailed:
            bilayer(self.ax, pts, zorder=4)
        else:
            q = _rounded_polyline(pts, 0.0)
            seg = np.gradient(q, axis=0)
            seg /= np.linalg.norm(seg, axis=1)[:, None]
            nrm = np.c_[-seg[:, 1], seg[:, 0]] * 4.5 * self.u
            band = np.vstack([q + nrm, (q - nrm)[::-1]])
            self.ax.add_patch(PathPatch(_closed_path(band), facecolor=P.fill("membrane"), edgecolor="none", zorder=4))
            for side in (1, -1):
                e = q + side * nrm
                self.ax.plot(e[:, 0], e[:, 1], color=P.edge("membrane"), lw=LINE * 0.8, zorder=4.5)

    def cell_frame(self, box, membrane_y, nucleus=None, detailed=True, labels=True, nucleus_label="Nucleus"):
        """Extracellular space above ``membrane_y``, cytoplasm below, a plasma membrane between them and an
        optional nucleus ``(x0, y0, x1, y1)`` with a double envelope. Registers compartments
        "extracellular", "cytoplasm" and "nucleus"."""
        x0, y0, x1, y1 = box
        ax = self.ax
        ext = np.array([(x0, membrane_y), (x1, membrane_y), (x1, y1), (x0, y1)])
        cyt = np.array([(x0, y0), (x1, y0), (x1, membrane_y), (x0, membrane_y)])
        ax.add_patch(PathPatch(_closed_path(ext), facecolor=P.fill("extracellular"), edgecolor="none", zorder=1))
        ax.add_patch(PathPatch(_closed_path(cyt), facecolor=P.fill("cytoplasm"), edgecolor="none", zorder=1))
        self.nodes["extracellular"] = Node("extracellular", "compartment", ((x0 + x1) / 2, (membrane_y + y1) / 2), x1 - x0,
                                           y1 - membrane_y, ext, "extracellular")
        self.nodes["cytoplasm"] = Node("cytoplasm", "compartment", ((x0 + x1) / 2, (y0 + membrane_y) / 2), x1 - x0,
                                       membrane_y - y0, cyt, "cytoplasm")
        self.membrane_line([(x0, membrane_y), (x1, membrane_y)], detailed=detailed)
        if nucleus is not None:
            self.compartment("nucleus", nucleus, None, token="nucleus", style="membrane", membrane_token="nucleus", zorder=3)
        if labels:
            m = 8 * self.u
            label(ax, (x0 + m, y1 - m), "Extracellular", size="small", bold=True, color=container_edge("extracellular"), ha="left", va="top", zorder=5)
            off = (0.7 if detailed else 0.2) + m
            label(ax, (x0 + m, membrane_y - off), "Cytoplasm", size="small", bold=True, color=container_edge("cytoplasm"), ha="left", va="top", zorder=5)
            if nucleus is not None:
                self.compartment_label("nucleus", nucleus_label, "tl")

    # -- PD process nodes ----------------------------------------------------------------------

    def process(self, id, at, angle=0.0, kind="process", size=None, zorder=12):
        """SBGN process node with an input port (opposite ``angle``) and an output port (towards ``angle``, degrees).

        kind: "process" (square), "omitted" (square with //), "uncertain" (square with ?),
        "association" (filled disc), "dissociation" (disc in a circle).
        """
        s = size or 8.5 * self.u
        x, y = at
        if kind in ("association", "dissociation"):
            outline = _ellipse(x, y, s, s)
        else:
            outline = _roundrect(x, y, s, s, 0.0)
        node = self._add(Node(id, kind, at, s, s, outline))
        d = np.array([math.cos(math.radians(angle)), math.sin(math.radians(angle))])
        stub = s * 0.75
        pin, pout = node.center - d * (s / 2 + stub), node.center + d * (s / 2 + stub)
        node.ports = (pin, pout)
        c = P.ink()
        for a, b in ((pin, node.center - d * s / 2), (node.center + d * s / 2, pout)):
            self.ax.plot([a[0], b[0]], [a[1], b[1]], color=c, lw=LINE * 0.9, zorder=zorder, solid_capstyle="butt", snap=False)
        if kind == "association":
            self._patch(outline, None, lw=LINE * 0.9, zorder=zorder, fill=c, edge=c)
        else:
            self._patch(outline, None, lw=LINE * 0.9, zorder=zorder, fill=P.surface(), edge=c)
        if kind == "dissociation":
            self._patch(_ellipse(x, y, s * 0.55, s * 0.55), None, lw=LINE * 0.8, zorder=zorder + 0.5, fill=P.surface(), edge=c)
        elif kind == "omitted":
            for k in (-0.17, 0.17):
                self.ax.plot([x + k * s - 0.18 * s, x + k * s + 0.18 * s], [y - 0.3 * s, y + 0.3 * s], color=c, lw=LINE * 0.8, zorder=zorder + 1)
        elif kind == "uncertain":
            label(self.ax, at, "?", size="tiny", bold=True, color=c, zorder=zorder + 1)
        return node

    def reaction(self, inputs, outputs, at=None, id=None, kind="process", angle=None, modifiers=(), size=None):
        """A process with consumption arcs from ``inputs`` and production arcs to ``outputs`` (lists of node ids,
        or ``(id, {"bend": …, "via": […]})``), and modulation arcs ``modifiers=[(id, "catalysis"), …]``
        (each optionally with a dict of arc options). The node sits midway between the input and output
        centroids unless ``at`` is given; ``angle`` defaults to the input→output direction. Returns the id."""

        def split(items):
            return [(i, {}) if isinstance(i, str) else (i[0], i[1]) for i in items]

        ins, outs = split(inputs), split(outputs)
        ci = np.mean([self.nodes[i].center for i, _ in ins], axis=0) if ins else None
        co = np.mean([self.nodes[o].center for o, _ in outs], axis=0) if outs else None
        if at is None:
            at = (ci + co) / 2
        if angle is None:
            v = (co - ci) if (ci is not None and co is not None) else np.array([1.0, 0.0])
            angle = math.degrees(math.atan2(v[1], v[0]))
            angle = round(angle / 90) * 90 if min(abs(angle % 90), 90 - abs(angle % 90)) < 20 else angle
        id = id or f"_p{len(self.nodes)}"
        self.process(id, at, angle=angle, kind=kind, size=size)
        for i, opt in ins:
            self.connect(i, id, "consumption", **opt)
        for o, opt in outs:
            self.connect(id, o, "production", **opt)
        for m in modifiers:
            mid, mk = m[0], m[1]
            self.connect(mid, id, mk, **(m[2] if len(m) > 2 else {}))
        return id

    # -- AF nodes ------------------------------------------------------------------------------

    def activity(self, id, at, text, w=None, h=None, token="protein", units=(), states=(), italic=False, size=None, zorder=11):
        """SBGN AF biological activity: a rectangle (slightly softened corners) with optional units of
        information, e.g. ``units=[("LacI", "macromolecule")]`` or ``["mt:prot"]``."""

        def shape(x, y, ww, hh):
            return _roundrect(x, y, ww, hh, 2.2 * self.u)

        return self._entity(id, "activity", shape, at, text, w, h, token, italic, states, units, 0, size, zorder)

    def phenotype(self, id, at, text, w=None, h=None, token="highlight", size=None, zorder=11):
        """SBGN phenotype (a cellular outcome: proliferation, lactose utilisation): a hexagon."""
        w, h = self._auto_size(text, w, h, size=size, pad=15)
        return self._entity(id, "phenotype", _hexagon, at, text, w, h, token, False, (), (), 0, size, zorder)

    def logic(self, id, at, op="AND", angle=0.0, ports=True, zorder=12):
        """SBGN logical operator AND / OR / NOT (also "delay" in AF): a circle with input and output ports."""
        text = {"delay": "τ"}.get(op, op)
        tw, _ = text_extent(self.ax, text, "tiny", bold=True)
        d = max(tw + 6 * self.u, 17 * self.u)
        outline = _ellipse(at[0], at[1], d, d)
        node = self._add(Node(id, "logic", at, d, d, outline))
        self._patch(outline, None, lw=LINE * 0.9, zorder=zorder, fill=P.surface(), edge=P.ink())
        label(self.ax, at, text, size="tiny", bold=True, color=P.ink(), zorder=zorder + 1)
        if ports:
            dv = np.array([math.cos(math.radians(angle)), math.sin(math.radians(angle))])
            stub = d * 0.45
            pin, pout = node.center - dv * (d / 2 + stub), node.center + dv * (d / 2 + stub)
            node.ports = (pin, pout)
            for a, b in ((pin, node.center - dv * d / 2), (node.center + dv * d / 2, pout)):
                self.ax.plot([a[0], b[0]], [a[1], b[1]], color=P.ink(), lw=LINE * 0.9, zorder=zorder, solid_capstyle="butt", snap=False)
        return node

    # -- arcs ----------------------------------------------------------------------------------

    def connect(self, a, b, kind="stimulation", bend=0.0, via=None, dashed=False, color=None, lw=None, text=None,
                text_offset=(0.0, 0.0), text_at=0.5, loop=90.0, loop_size=None, start=None, end=None, gap=None,
                zorder=15):
        """An SBGN arc from node ``a`` to node ``b`` (ids), attached to their borders.

        ``bend`` curves it (as in ``core.arrow``); ``via`` routes it through waypoints (rounded elbows);
        ``a == b`` draws a self-loop leaving the node towards ``loop`` degrees. ``start``/``end`` override
        the attachment points; ``text`` labels the arc at fraction ``text_at`` of its length.
        Returns the drawn polyline.
        """
        if kind not in ARC:
            raise ValueError(f"unknown arc kind {kind!r}; one of {sorted(ARC)}")
        draw_kind = ARC[kind]
        A, B = self.nodes[a], self.nodes[b]
        clip_a = clip_b = True
        p0, p1 = A.center, B.center
        if A.ports is not None:
            p0, clip_a = A.ports[1], False
        if B.ports is not None and kind in ("consumption", "logic", "link", "equivalence"):
            p1, clip_b = B.ports[0], False
        if start is not None:
            p0, clip_a = np.asarray(start, float), False
        if end is not None:
            p1, clip_b = np.asarray(end, float), False
        if a == b and via is None:
            R = loop_size or 0.9 * max(A.w, A.h) + 0.4
            sp = math.radians(48)
            th = math.radians(loop)
            c = A.center
            d1 = np.array([math.cos(th - sp), math.sin(th - sp)])
            d2 = np.array([math.cos(th + sp), math.sin(th + sp)])
            t = np.linspace(0, 1, 200)[:, None]
            q0, q1, q2, q3 = c, c + d1 * R * 1.5, c + d2 * R * 1.5, c
            pts = (1 - t) ** 3 * q0 + 3 * (1 - t) ** 2 * t * q1 + 3 * (1 - t) * t**2 * q2 + t**3 * q3
        elif via:
            pts = _rounded_polyline([p0, *via, p1], 9 * self.u)
        else:
            pts = _quad(p0, p1, bend, n=220)
        if clip_a:
            pts = _clip_start(pts, A.path)
        if clip_b:
            pts = _clip_end(pts, B.path)
        g0 = 0.6 * self.u
        g1 = (gap if gap is not None else (0.6 if draw_kind in _HEADLESS else 2.2)) * self.u
        pts = _trim(pts, g0 if clip_a else 0.0, g1 if (clip_b or draw_kind not in _HEADLESS) else 0.0)
        self._draw_arc(pts, draw_kind, color or P.ink(), lw or LINE, dashed, zorder)
        if text:
            s = _cumlen(pts)
            k = np.searchsorted(s, s[-1] * text_at).clip(1, len(pts) - 1)
            tan = pts[k] - pts[k - 1]
            tan = tan / (np.linalg.norm(tan) or 1)
            nrm = np.array([-tan[1], tan[0]])
            off = nrm * 8 * self.u + np.asarray(text_offset, float)
            label(self.ax, pts[k] + off, text, size="tiny", color=P.muted(), zorder=zorder + 2)
        return pts

    def _draw_arc(self, pts, kind, color, lw, dashed, zorder):
        ax = self.ax
        head = self.head
        s = _cumlen(pts)
        total = s[-1]
        ls = (0, (3.2, 2.2)) if dashed else "-"
        if kind == "link":
            pts = _simplify(pts)
            ax.plot(pts[:, 0], pts[:, 1], color=color, lw=lw, ls=ls, solid_capstyle="round", zorder=zorder, snap=False)
            return
        tip = pts[-1]
        back = np.array([np.interp(max(total - head, 0), s, pts[:, 0]), np.interp(max(total - head, 0), s, pts[:, 1])])
        tan = tip - back
        tan = tan / (np.linalg.norm(tan) or 1)
        # where our line stops (distance before the tip): inside the head, so that core.arrow draws only the head
        stop = {"process": 0.6, "activation": 0.6, "necessary": 0.6, "catalysis": 0.9, "inhibition": 0.0, "diamond": 1.15}[kind] * head
        cut = max(total - stop, 0)
        body = np.vstack([pts[s < cut], [np.interp(cut, s, pts[:, 0]), np.interp(cut, s, pts[:, 1])]])
        body = _simplify(body)
        if len(body) > 1:
            ax.plot(body[:, 0], body[:, 1], color=color, lw=lw, ls=ls, solid_capstyle="butt" if stop else "round",
                    zorder=zorder, snap=False)
        if kind == "diamond":
            nrm = np.array([-tan[1], tan[0]])
            L, W = head * 1.15, head * 0.5
            ax.add_patch(Polygon([tip, tip - tan * L / 2 + nrm * W, tip - tan * L, tip - tan * L / 2 - nrm * W], closed=True,
                                 facecolor=P.surface(), edgecolor=color, lw=lw * 0.9, zorder=zorder + 1, joinstyle="miter"))
            return
        lead = {"catalysis": 0.93, "inhibition": 0.02}.get(kind, 0.62) * head
        arrow(ax, tip - tan * lead, tip, kind=kind, color=color, lw=lw, head=head, zorder=zorder)


# ---------------------------------------------------------------------------------------------
# helpers: signalling cascade and gene-regulatory motifs


def cascade(ax, box, ligand="EGF", receptor="EGFR", chain=("GRB2", "SOS", "RAS", "RAF", "MEK", "ERK"), tf="ELK1",
            gene="FOS", phenotype=None, states=None, tokens=None, detailed_membrane=True, nucleus_frac=0.27,
            arc="positive", receptor_dimer=True, zigzag=0.15):
    """A signalling cascade inside a cell: ligand (extracellular) → receptor (in the plasma membrane) →
    ``chain`` (cytoplasm, top to bottom) → transcription factor ``tf`` → ``gene`` (nucleus) → optional
    ``phenotype`` (a hexagon in the cytoplasm beside the nucleus).

    ``chain`` items are names or dicts ``{"text", "kind": "macromolecule" | "chemical", "states", "token"}``;
    ``states`` maps a node name to its state variables (e.g. ``{"MEK": ["P", "P"]}``; the receptor defaults
    to ``["P"]`` on its cytoplasmic side, the transcription factor to ``["P"]``). The chain is laid out in a
    zig-zag of half-width ``zigzag`` × box width, with state variables on the outer side; arcs are AF
    ``positive`` influences (``arc=``). Returns the ``Diagram``; node ids are "ligand", "receptor",
    "c0" … "cN", "tf", "gene" and "phenotype".
    """
    x0, y0, x1, y1 = box
    d = Diagram(ax)
    states = states or {}
    tokens = tokens or {}
    W, H = x1 - x0, y1 - y0
    ym = y1 - 0.13 * H
    ny1 = y0 + nucleus_frac * H
    pad = 0.04 * W
    nx1 = x1 - pad
    if phenotype:
        pw, _ = d._auto_size(phenotype, None, None, pad=15)
        nx1 = x1 - pad - pw - 0.35
    nuc = (x0 + pad, y0 + 0.03 * H, nx1, ny1)
    d.cell_frame(box, ym, nucleus=nuc, detailed=detailed_membrane)
    cx = (x0 + x1) / 2
    half = 0.36 if detailed_membrane else 0.08  # half-thickness of the drawn membrane

    def placed(st, outer):
        # state variables away from the arcs, which arrive and leave on the inner side of the zig-zag
        order = {"l": ("tl", "bl", "l"), "r": ("tr", "br", "r"), "c": ("br", "bl", "b")}[outer]
        return [(v, order[i % len(order)]) if isinstance(v, str) else v for i, v in enumerate(st)]

    rec = d.macromolecule("receptor", (cx, ym), receptor, token=tokens.get(receptor, "receptor"),
                          states=placed(states.get(receptor, ["P"]), "c"), multimer=2 if receptor_dimer else 0)
    lig_y = ym + max(rec.h / 2, half) + (y1 - ym - max(rec.h / 2, half)) * 0.5
    d.macromolecule("ligand", (cx, lig_y), ligand, token=tokens.get(ligand, "drug"), states=states.get(ligand, ()))
    d.connect("ligand", "receptor", arc)
    items = [c if isinstance(c, dict) else {"text": c} for c in chain]
    h = rec.h
    top = ym - max(rec.h / 2, half) - 1.25 * h
    bottom = ny1 + 1.1 * h
    n = len(items)
    ys = np.linspace(top, bottom, n) if n > 1 else [top]
    zig = zigzag * W
    prev = "receptor"
    for k, (item, y) in enumerate(zip(items, ys)):
        text = item["text"]
        side = (1 if k % 2 else -1) if n > 1 else 0
        x = cx + side * zig
        nid = f"c{k}"
        st = placed(item.get("states", states.get(text, ())), {-1: "l", 1: "r", 0: "c"}[side])
        tok = item.get("token", tokens.get(text, P.protein(k + 1)))
        if item.get("kind") == "chemical":
            d.simple_chemical(nid, (x, y), text, token=tok)
        else:
            d.macromolecule(nid, (x, y), text, token=tok, states=st)
        d.connect(prev, nid, arc)
        prev = nid
    # nucleus: transcription factor and its target gene
    nw = nuc[2] - nuc[0]
    ty = ny1 - 0.33 * (ny1 - nuc[1])
    gy = nuc[1] + 0.3 * (ny1 - nuc[1])
    d.macromolecule("tf", (nuc[0] + 0.3 * nw, ty), tf, token=tokens.get(tf, "antibody"), states=placed(states.get(tf, ["P"]), "l"))
    d.nucleic_acid("gene", (nuc[0] + 0.68 * nw, gy), gene, units=[("ct:gene", "rect", "bl")])
    d.connect(prev, "tf", arc)
    d.connect("tf", "gene", "necessary" if arc == "positive" else arc)
    if phenotype:
        px = (nx1 + x1) / 2
        d.phenotype("phenotype", (px, gy), phenotype, w=x1 - nx1 - 0.25)
        d.connect("gene", "phenotype", arc)
    return d


MOTIFS = ("ffl", "nar", "par", "toggle", "repressilator")


def motif(ax, kind, at, size=2.4, names=None, signs=None, gate=None, inputs=None, token=None, italic=True, diagram=None):
    """A gene-regulatory network motif drawn with AF activity nodes, centred at ``at`` (spanning about ``size``).

    kind:
      "ffl"            feed-forward loop X → Y → Z with X → Z; ``signs`` "C1" (coherent type 1, default),
                       "I1" (incoherent type 1: Y ⊣ Z), or a 3-string such as "+-+" for X→Y, X→Z, Y→Z;
                       ``gate="AND"`` / "OR" joins the two inputs of Z with a logical operator
      "nar" / "par"    negative / positive autoregulation of X
      "toggle"         two mutually repressing genes (Gardner et al. 2000)
      "repressilator"  three genes in a cycle of repression (Elowitz & Leibler 2000)

    ``inputs={"X": "Sx"}`` adds an external signal acting on a node (``"Sx"`` or ``("IPTG", "negative")``).
    Returns the ``Diagram`` (node ids are the names).
    """
    d = diagram or Diagram(ax)
    cx, cy = at
    s = size
    defaults = {"ffl": "XYZ", "nar": "X", "par": "X", "toggle": ("lacI", "cI"), "repressilator": ("lacI", "tetR", "cI")}
    names = list(names or defaults[kind])
    toks = token or [P.protein(i + 1) for i in range(len(names))]
    if isinstance(toks, str):
        toks = [toks] * len(names)

    def node(name, xy, k):
        d.activity(name, xy, name, token=toks[k], italic=italic, w=None)

    if kind == "ffl":
        X, Y, Z = names
        node(X, (cx - 0.25 * s, cy + 0.45 * s), 0)
        node(Y, (cx + 0.35 * s, cy), 1)
        node(Z, (cx - 0.25 * s, cy - 0.45 * s), 2)
        sg = {"C1": "+++", "I1": "++-"}.get(signs or "C1", signs)
        k = ["positive" if c == "+" else "negative" for c in sg]
        d.connect(X, Y, k[0])
        if gate:
            gx, gy = cx - 0.25 * s, cy - 0.17 * s
            d.logic("_gate", (gx, gy), gate, angle=-90)
            d.connect(X, "_gate", "logic")
            d.connect(Y, "_gate", "logic")
            d.connect("_gate", Z, "positive")
        else:
            d.connect(X, Z, k[1])
            d.connect(Y, Z, k[2])
    elif kind in ("nar", "par"):
        (X,) = names
        node(X, (cx, cy - 0.12 * s), 0)
        d.connect(X, X, "negative" if kind == "nar" else "positive", loop=90, loop_size=0.42 * s)
    elif kind == "toggle":
        A, B = names
        half = max(0.3 * s, max(d._auto_size(nm, None, None, italic=italic)[0] for nm in names) / 2 + 0.7)
        node(A, (cx - half, cy), 0)
        node(B, (cx + half, cy), 1)
        d.connect(A, B, "negative", bend=-0.3)
        d.connect(B, A, "negative", bend=-0.3)
    elif kind == "repressilator":
        wmax = max(d._auto_size(nm, None, None, italic=italic)[0] for nm in names)
        r = max(0.38 * s, 0.95 * wmax)
        pos = [(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a))) for a in (90, -30, 210)]
        for k, (nm, p) in enumerate(zip(names, pos)):
            node(nm, p, k)
        for k in range(3):
            d.connect(names[k], names[(k + 1) % 3], "negative", bend=-0.16)
    else:
        raise ValueError(f"unknown motif {kind!r}; one of {MOTIFS}")
    for target, sig in (inputs or {}).items():
        text, ak = (sig, "positive") if isinstance(sig, str) else sig
        n = d.nodes[target]
        tx, ty = n.center
        # the signal enters from the free side: above for top nodes, below otherwise
        up = ty >= cy
        sy = ty + (1 if up else -1) * (n.h / 2 + 1.5 * n.h)
        sid = f"_in_{target}"
        tw, th = text_extent(ax, text, "small")
        d.nodes[sid] = Node(sid, "text", (tx, sy), tw + 0.1, th + 0.1, _roundrect(tx, sy, tw + 0.12, th + 0.12, 0.0))
        label(ax, (tx, sy), text, size="small", color=P.ink())
        d.connect(sid, target, ak)
    return d
