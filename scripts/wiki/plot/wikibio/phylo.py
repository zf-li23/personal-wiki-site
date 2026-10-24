"""Phylogenetic trees and the geological time scale.

    from wikibio import phylo
    t = phylo.tree(ax, "((Homo_sapiens:6.4,Pan_troglodytes:6.4):80,Mus_musculus:86.4);",
                   origin=(1, 1), width=8, height=4, scaled=True, italic=True)
    t.time_axis(ax, ticks=[80, 40, 0])
    t.geo_scale(ax, y=0.6, ranks=("period",))

Layouts (``layout=``):

    "rectangular"   right-angled branches, root on the left (``direction="right"``) or at the bottom ("up")
    "slanted"       straight diagonal branches (the classic textbook cladogram)
    "circular"      root at the centre, tips on a circle (``center=``, ``radius=``, ``arc=``)

Branch lengths are drawn to scale with ``scaled=True`` (a phylogram, or a chronogram when the tree is
ultrametric: lengths in Myr give a time axis with ``Tree.time_axis`` and ``Tree.geo_scale``); otherwise
the tree is a cladogram with aligned tips. Clades are highlighted by ``clades=[dict(tips=[...] | node=name,
token="plant", style="band" | "branch" | "bar", label="Angiosperms")]``; events on branches or nodes by
``marks=[dict(node=..., kind="trait" | "loss" | "duplication" | "speciation" | "dot" | "star", text=...)]``.

Tip silhouettes: ``icons={"Mus musculus": "phylopic/mouse"}`` (or ``(id, {"rotate": 90, "flip": True})``).
The build finds icons by the string literals in the plot script, so the script must write every id as a
literal (a dict literal like the one above is enough); this module only forwards them to ``icons.icon``.

Newick: names with ``_`` become spaces (quote names with ``'...'`` to keep underscores), ``[...]`` comments
are ignored, a numeric internal label is read as a support value and any other internal label as the
node's name (``Name/95`` gives both).
"""

import math
import re

import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch, Polygon, RegularPolygon, Wedge

from . import palette as P
from .core import FONT, LINE, label, scale_bar as _scale_bar
from .icons import icon as _icon
from .icons import size as _icon_size

# ------------------------------------------------------------------ Newick


class Node:
    """A tree node: ``name``, branch ``length`` (to its parent), ``support``, ``children``, ``parent``."""

    def __init__(self, name=None, length=None, support=None):
        self.name, self.length, self.support = name, length, support
        self.children, self.parent = [], None
        # layout (filled by tree()): depth along the root-to-tip axis, breadth across it, xy on the canvas
        self.depth = self.breadth = 0.0
        self.xy = (0.0, 0.0)

    @property
    def is_leaf(self):
        return not self.children

    def walk(self):
        """Preorder traversal."""
        yield self
        for c in self.children:
            yield from c.walk()

    def leaves(self):
        return [n for n in self.walk() if n.is_leaf]

    def find(self, name):
        for n in self.walk():
            if n.name == name:
                return n
        raise KeyError(f"no node named {name!r} in the tree")

    def mrca(self, names):
        """Most recent common ancestor of the named nodes."""
        nodes = [self.find(n) for n in names]
        paths = []
        for n in nodes:
            p, path = n, []
            while p is not None:
                path.append(p)
                p = p.parent
            paths.append(path[::-1])
        anc = self
        for level in zip(*paths):
            if all(x is level[0] for x in level):
                anc = level[0]
            else:
                break
        return anc

    def ladderize(self, larger_last=True):
        for n in self.walk():
            n.children.sort(key=lambda c: len(c.leaves()), reverse=not larger_last)
        return self

    def __repr__(self):
        return f"Node({self.name!r}, {len(self.leaves())} tips)"


def parse(newick):
    """Parse a Newick string into a ``Node`` tree."""
    s = re.sub(r"\[[^\]]*\]", "", newick.strip())
    if not s.endswith(";"):
        s += ";"
    pos = 0

    def label_at():
        nonlocal pos
        if s[pos] == "'":
            end = s.index("'", pos + 1)
            text, pos = s[pos + 1:end], end + 1
            return text
        m = re.match(r"[^,():;]*", s[pos:])
        pos += m.end()
        text = m.group(0).strip()
        return text.replace("_", " ") if text else None

    def length_at():
        nonlocal pos
        if s[pos] == ":":
            m = re.match(r":\s*([-+0-9.eE]+)", s[pos:])
            pos += m.end()
            return float(m.group(1))
        return None

    def node_at():
        nonlocal pos
        n = Node()
        if s[pos] == "(":
            pos += 1
            while True:
                c = node_at()
                c.parent = n
                n.children.append(c)
                if s[pos] == ",":
                    pos += 1
                    continue
                if s[pos] == ")":
                    pos += 1
                    break
                raise ValueError(f"Newick: unexpected {s[pos]!r} at {pos}")
            text = label_at()
            if text:
                name, _, sup = text.partition("/")
                try:
                    n.support = float(name) if not sup else float(sup)
                    n.name = None if not sup else name
                except ValueError:
                    n.name = text
        else:
            n.name = label_at()
        n.length = length_at()
        return n

    root = node_at()
    if s[pos] != ";":
        raise ValueError(f"Newick: trailing text at {pos}: {s[pos:]!r}")
    return root


# -------------------------------------------------------------- text helpers


def _renderer(ax):
    return ax.figure.canvas.get_renderer()


def _data_per_point(ax):
    """Data units per typographic point (canvas axes have equal aspect)."""
    p0, p1 = ax.transData.transform([(0, 0), (1, 0)])
    px_per_unit = abs(p1[0] - p0[0])
    return ax.figure.dpi / 72 / px_per_unit


def _text_wh(ax, text, size="small", italic=False, bold=False):
    """(width, height) of a one-line label in data units."""
    t = ax.text(0, 0, text, fontsize=FONT.get(size, size), style="italic" if italic else "normal",
                weight="bold" if bold else "normal")
    bb = t.get_window_extent(_renderer(ax))
    t.remove()
    k = _data_per_point(ax) * 72 / ax.figure.dpi
    return bb.width * k, bb.height * k


def _tint(token, strength=0.32):
    """A soft background tint of a token that stays calm on both themes."""
    return P.mix(P.surface(), P.fill(token), strength if not P.is_dark() else strength * 0.9)


def _resolve(root, spec):
    if isinstance(spec, Node):
        return spec
    if isinstance(spec, str):
        return root.find(spec)
    return root.mrca(list(spec))


# ------------------------------------------------------------------- Tree


class Tree:
    """A drawn tree: ``root``, the coordinate mapping and helpers for axes, scale bars and time scales.

    ``tree.node(spec)`` returns a node (by name, or the MRCA of a list of tip names); ``node.xy`` is its
    position on the canvas. ``tree.x_of_age(a)`` maps an age (branch-length units before the tips) to
    the depth coordinate of rectangular and slanted trees.
    """

    def __init__(self, root, layout, direction, unit, d0, dmax, frame):
        self.root, self.layout, self.direction = root, layout, direction
        self.unit, self.d0, self.dmax = unit, d0, dmax
        self.frame = frame  # (x0, y0, width, height) or (cx, cy, radius)
        self.outer = 0.0  # depth coordinate (data units from the origin) of the outermost drawn element

    def node(self, spec):
        return _resolve(self.root, spec)

    def tips(self):
        return self.root.leaves()

    def x_of_age(self, age):
        """Depth coordinate (x for direction "right", y for "up") of an age before the tips."""
        d = self.d0 + (self.dmax - age) * self.unit
        x0, y0 = self.frame[0], self.frame[1]
        return (x0 if self.direction == "right" else y0) + d

    def scale_bar(self, ax, length, text=None, at=None, size="small"):
        """A bar ``length`` branch-length units long (default text: "<length> substitutions/site")."""
        if at is None:
            x0, y0 = self.frame[0], self.frame[1]
            at = (x0, y0 - 0.45)
        _scale_bar(ax, at, length * self.unit, text if text is not None else f"{length:g} substitutions/site", size=size)

    def time_axis(self, ax, ticks, y=None, unit="Ma", size="small", line=True, minor=None):
        """A time axis below a rectangular chronogram (``ticks`` in Ma; 0 = present)."""
        if self.direction != "right" or self.layout == "circular":
            raise ValueError("time_axis needs a rectangular or slanted tree with direction='right'")
        y = self.frame[1] - 0.35 if y is None else y
        xs = [self.x_of_age(t) for t in ticks]
        c = P.muted()
        if line:
            ax.plot([min(xs), max(xs)], [y, y], color=c, lw=0.9, zorder=18, solid_capstyle="butt")
        for t in minor or []:
            x = self.x_of_age(t)
            ax.plot([x, x], [y, y - 0.08], color=c, lw=0.7, zorder=18)
        for t, x in zip(ticks, xs):
            ax.plot([x, x], [y, y - 0.14], color=c, lw=0.9, zorder=18)
            label(ax, (x, y - 0.2), f"{t:g}", size=size, va="top", color=c)
        if unit:
            label(ax, (max(xs) + 0.25, y - 0.2), unit, size=size, ha="left", va="top", color=c)
        return y

    def time_lines(self, ax, ages, texts=None, y0=None, y1=None, size="tiny"):
        """Dashed vertical lines at given ages (mass extinctions, calibrations) with optional labels on top."""
        x0, yb, w, h = self.frame
        y0 = yb - 0.1 if y0 is None else y0
        y1 = yb + h + 0.2 if y1 is None else y1
        for i, a in enumerate(ages):
            x = self.x_of_age(a)
            ax.plot([x, x], [y0, y1], color=P.muted(), lw=0.8, ls=(0, (3, 2.5)), zorder=2)
            if texts and texts[i]:
                label(ax, (x, y1 + 0.08), texts[i], size=size, va="bottom", color=P.muted())

    def geo_scale(self, ax, y, ranks=("period",), height=0.42, age_range=None, **kw):
        """The geological time scale under a chronogram, aligned with ``x_of_age`` (see ``geo_scale``)."""
        old = age_range[0] if age_range else self.dmax + self.d0 / self.unit
        young = age_range[1] if age_range else 0.0
        return geo_scale(ax, (self.x_of_age(old), self.x_of_age(young)), (old, young), y, ranks=ranks, height=height, **kw)


def _layout(root, scaled, layout):
    tips = root.leaves()
    for i, t in enumerate(tips):
        t.breadth = float(i)

    def breadth(n):
        if n.is_leaf:
            return n.breadth, n.breadth
        spans = [breadth(c) for c in n.children]
        lo, hi = spans[0][0], spans[-1][1]
        if layout == "slanted" and not scaled:
            n.breadth = (lo + hi) / 2
        else:
            n.breadth = (n.children[0].breadth + n.children[-1].breadth) / 2
        n._span = (lo, hi)
        return lo, hi

    breadth(root)
    if scaled:
        for n in root.walk():
            n.depth = (n.parent.depth if n.parent else 0.0) + (n.length or 0.0 if n.parent else 0.0)
    else:
        def height(n):
            n._h = 0 if n.is_leaf else 1 + max(height(c) for c in n.children)
            return n._h

        height(root)
        for n in root.walk():
            if layout == "slanted":
                lo, hi = getattr(n, "_span", (n.breadth, n.breadth))
                n.depth = -(hi - lo) / 2  # 45-degree diagonals; shifted below
            else:
                n.depth = -n._h
        m = min(n.depth for n in root.walk())
        for n in root.walk():
            n.depth -= m
    return max(t.depth for t in tips)


def _italic_of(italic, name):
    if callable(italic):
        return italic(name)
    if isinstance(italic, (set, list, tuple, frozenset)):
        return name in italic
    return bool(italic)


def tree(ax, newick, origin=(0, 0), width=8.0, height=5.0, layout="rectangular", direction="right",
         center=None, radius=None, start=90.0, arc=360.0, scaled=False, span=None, root_edge=0.0,
         ladderize=False, tip_labels=True, tip_text=None, italic=False, label_size="small", tip_rotation=0,
         align=False, icons=None, icon_size=None, icon_width=None, icon_color=None, icon_position="label",
         clades=None, marks=None, support=None, support_min=0, color=None, lw=LINE * 1.1, zorder=8):
    """Draw a phylogenetic tree; returns a ``Tree`` (node positions, axis and time-scale helpers).

    newick       Newick string or a parsed ``Node``
    origin, width, height   the box of a rectangular/slanted tree (root edge to tips; labels go outside)
    center, radius, start, arc   a circular tree: tips on ``radius``, first tip at angle ``start`` (deg),
                 spread clockwise over ``arc`` degrees
    direction    "right" (root left) or "up" (root at the bottom) for rectangular and slanted trees
    scaled       branch lengths to scale; ``span`` maps that many length units onto the box (default: the
                 root-to-tip depth plus ``root_edge``, a stem drawn below the root)
    tip_text     {tip: displayed text}; ``italic`` True / False / set of tips / callable (species names)
    align        draw labels in one column with dotted guides (phylograms)
    icons        {tip: icon id or (id, options)}; ids must also appear as literals in the plot script
    clades       list of dict(tips=[...] or node=name, token, style "band"/"branch"/"bar" (or a list),
                 label, italic)
    marks        list of dict(node=name | [tips], kind, text, at=fraction along the branch, token, side (+1/-1),
                 size, offset, shift=(dx, dy), ha, va, text_size); kinds: see ``marker``
    support      None, "label" (numbers) or "dot" (filled dot when support >= ``support_min``)
    """
    root = parse(newick) if isinstance(newick, str) else newick
    if ladderize:
        root.ladderize(larger_last=(ladderize != "down"))
    if layout not in ("rectangular", "slanted", "circular"):
        raise ValueError(f"unknown layout {layout!r}")
    circ = layout == "circular"
    if not circ and direction not in ("right", "up"):
        raise ValueError("direction must be 'right' or 'up'")
    dtip = _layout(root, scaled, layout)
    tips = root.leaves()
    n = len(tips)
    ink = color or P.ink()

    # --- coordinate mapping: (depth d, breadth b) in data units -> canvas xy
    if circ:
        cx, cy = center if center is not None else origin
        R = radius if radius is not None else min(width, height) / 2
        total = span if span is not None else dtip + root_edge
        unit = R / total if total else 1.0
        d0 = (total - dtip) * unit
        full = arc >= 359.9
        step = arc / (n if full else max(1, n - 1))

        def ang(b):
            return math.radians(start - b * step)

        def xy(d, b):
            a = ang(b)
            return (cx + d * math.cos(a), cy + d * math.sin(a))

        spacing = R * math.radians(step)
        frame = (cx, cy, R)
    else:
        x0, y0 = origin
        L = width if direction == "right" else height
        B = height if direction == "right" else width
        total = span if span is not None else dtip + root_edge
        unit = L / total if total else 1.0
        d0 = (total - dtip) * unit
        spacing = B / max(1, n - 1)

        if direction == "right":
            def xy(d, b):
                return (x0 + d, y0 + height - b * spacing)
        else:
            def xy(d, b):
                return (x0 + b * spacing, y0 + d)
        frame = (x0, y0, width, height)

    def D(node):
        return d0 + node.depth * unit

    for nd in root.walk():
        nd.xy = xy(D(nd), nd.breadth)
    T = Tree(root, layout, direction, unit, d0, dtip, frame)
    T.stem = xy(D(root) - root_edge * unit, root.breadth) if root_edge else None

    # --- clade colours for branches
    clades = [dict(c) for c in (clades or [])]
    branch_token = {}
    for c in clades:
        c["node"] = _resolve(root, c.get("node") or c.get("tips"))
        c["leafset"] = set(id(t) for t in c["node"].leaves())
        styles = c.get("style", "band")
        c["styles"] = [styles] if isinstance(styles, str) else list(styles)
        if "branch" in c["styles"]:
            for nd in c["node"].walk():
                branch_token[id(nd)] = c.get("token", "neutral")
    # nested clades: outer ones get the outer bar columns
    for c in clades:
        inner = [d for d in clades if d is not c and d["leafset"] < c["leafset"]]
        c["level"] = 0
    for _ in clades:
        for c in clades:
            inner = [d for d in clades if d is not c and d["leafset"] < c["leafset"]]
            c["level"] = max([0] + [d["level"] + 1 for d in inner])

    def bcol(nd):
        tok = branch_token.get(id(nd))
        return P.edge(tok) if tok else ink

    def blw(nd):
        return lw * 1.35 if id(nd) in branch_token else lw

    # --- branches
    def seg(points, c, w):
        p = np.asarray(points)
        ax.plot(p[:, 0], p[:, 1], color=c, lw=w, solid_capstyle="round", solid_joinstyle="round", zorder=zorder)

    if root_edge and not circ:
        seg([xy(D(root) - root_edge * unit, root.breadth), root.xy], bcol(root), blw(root))
    elif root_edge and circ:
        seg([xy(D(root) - root_edge * unit, root.breadth), root.xy], bcol(root), blw(root))
    for nd in root.walk():
        if nd.is_leaf:
            continue
        if layout == "rectangular":
            b_lo, b_hi = nd.children[0].breadth, nd.children[-1].breadth
            # the connector: coloured where it leads to coloured children
            for c in nd.children:
                seg([xy(D(nd), nd.breadth), xy(D(nd), c.breadth)], bcol(c) if id(nd) in branch_token else ink,
                    blw(nd) if id(nd) in branch_token else lw)
                seg([xy(D(nd), c.breadth), xy(D(c), c.breadth)], bcol(c), blw(c))
            del b_lo, b_hi
        elif layout == "slanted":
            for c in nd.children:
                seg([nd.xy, c.xy], bcol(c), blw(c))
        else:  # circular: arc at the node radius, radial lines to children
            r = D(nd)
            bs = np.linspace(nd.children[0].breadth, nd.children[-1].breadth, 64)
            for c in nd.children:
                part = np.linspace(nd.breadth, c.breadth, 40)
                seg([xy(r, b) for b in part], bcol(c) if id(nd) in branch_token else ink,
                    blw(nd) if id(nd) in branch_token else lw)
                seg([xy(r, c.breadth), xy(D(c), c.breadth)], bcol(c), blw(c))
            del bs

    # --- tip labels
    tip_text = tip_text or {}
    pad = 0.18
    dmax_tip = max(D(t) for t in tips)
    label_end = {}
    fs = label_size
    for t in tips:
        text = tip_text.get(t.name, t.name or "")
        it = _italic_of(italic, t.name)
        w_, h_ = _text_wh(ax, text, fs, italic=it) if (tip_labels and text) else (0.0, 0.0)
        d_lab = (dmax_tip if align else D(t)) + pad
        if align and D(t) < dmax_tip - 1e-6:
            p = np.asarray([xy(D(t) + 0.06, t.breadth), xy(dmax_tip + 0.06, t.breadth)])
            ax.plot(p[:, 0], p[:, 1], color=P.muted(), lw=0.6, ls=(0, (1, 2)), zorder=zorder - 1)
        extent = w_
        if tip_labels and text:
            if circ:
                a = ang(t.breadth)
                deg = math.degrees(a)
                right = math.cos(a) >= -1e-9
                ax.text(*xy(d_lab, t.breadth), text, fontsize=FONT.get(fs, fs), color=P.ink(), rotation=deg if right else deg + 180,
                        rotation_mode="anchor", ha="left" if right else "right", va="center",
                        style="italic" if it else "normal", zorder=20)
            elif direction == "right":
                label(ax, xy(d_lab, t.breadth), text, size=fs, ha="left", italic=it)
            else:
                if tip_rotation:
                    label(ax, xy(d_lab, t.breadth), text, size=fs, ha="left", va="center", italic=it, rotation=tip_rotation)
                    ax.texts[-1].set_rotation_mode("anchor")
                else:
                    label(ax, xy(d_lab, t.breadth), text, size=fs, va="bottom", italic=it)
                    extent = h_
        label_end[id(t)] = d_lab + extent

    # --- icons
    outer = max(label_end.values()) if label_end else dmax_tip
    if icons:
        isz = icon_size or min(spacing * 0.82, 1.6)
        iwd = icon_width or isz * 2.2
        col = (max(label_end.values()) + pad * 1.4) if icon_position == "label" else None
        for t in tips:
            spec = icons.get(t.name)
            if not spec:
                continue
            iid, opt = (spec, {}) if isinstance(spec, str) else (spec[0], dict(spec[1]))
            rot = opt.get("rotate", 0.0)
            w0, h0 = _icon_size(iid)
            if rot % 180:
                w0, h0 = h0, w0
            # fit the icon into its box: along the tree axis iwd (right) / isz (up), across: the tip spacing
            if circ or direction == "right":
                bw, bh = iwd, isz
            else:
                bw, bh = min(spacing * 0.9, iwd), isz
            s = min(bw / w0, bh / h0) * opt.get("scale", 1.0)
            W, H = w0 * s, h0 * s
            along = H if (not circ and direction == "up") else W
            dstart = col if col is not None else D(t) + pad
            at = xy(dstart + along / 2, t.breadth)
            tok = opt.get("color") or icon_color
            for c in sorted(clades, key=lambda c: -len(c["leafset"])):  # innermost coloured clade wins
                if (id(t) in c["leafset"] and opt.get("color") is None and icon_color is None
                        and ("band" in c["styles"] or "branch" in c["styles"])):
                    tok = P.edge(c.get("token", "neutral"))  # the darker shade reads on the clade's tint
            tok = tok or P.muted()
            hh = (h0 if not rot % 180 else w0) * s
            _icon(ax, iid, at=at, height=hh, anchor="center", color=tok, flip=opt.get("flip", False), rotate=rot, zorder=zorder + 2)
            outer = max(outer, dstart + along)
    T.outer = outer

    # --- clade decorations
    col_w = {}
    for c in clades:
        if "bar" in c["styles"] or "band" in c["styles"]:
            if c.get("label"):
                w_, h_ = _text_wh(ax, c["label"], "small", italic=c.get("italic", False), bold=True)
                col_w[c["level"]] = max(col_w.get(c["level"], 0), w_ if (not circ and direction == "right") else h_)
    def col_start(level):
        x = outer + pad * 2
        for k in range(level):
            x += 0.28 + col_w.get(k, 0) + pad * 2.2
        return x

    for c in clades:
        nd = c["node"]
        tok = c.get("token", "neutral")
        lo, hi = nd._span if not nd.is_leaf else (nd.breadth, nd.breadth)
        cs = col_start(c["level"])
        if "band" in c["styles"]:
            d_in = D(nd) - (c.get("pad", 0.35))
            d_out = cs - pad if ("bar" not in c["styles"]) else cs - pad
            if circ:
                a1, a2 = math.degrees(ang(hi + 0.5)), math.degrees(ang(lo - 0.5))
                ax.add_patch(Wedge(frame[:2], d_out, a1, a2, width=d_out - max(d_in, 0), facecolor=_tint(tok), edgecolor="none",
                                   lw=0, zorder=1))
            elif layout == "slanted":
                # follow the clade's triangle so that the outgroup's diagonal branches stay outside
                lt, rt = nd.leaves()[0], nd.leaves()[-1]
                g = 0.45

                def side(tip, b_edge):
                    if abs(tip.breadth - nd.breadth) < 1e-9:
                        return xy(d_in, b_edge)
                    slope = (D(tip) - D(nd)) / (tip.breadth - nd.breadth)
                    return xy(min(d_out, d_in + slope * (b_edge - nd.breadth)), b_edge)

                poly = [xy(d_in, nd.breadth), side(lt, lo - g), xy(d_out, lo - g), xy(d_out, hi + g), side(rt, hi + g)]
                c_ = _tint(tok)
                ax.add_patch(Polygon(poly, closed=True, facecolor=c_, edgecolor=c_, lw=6, joinstyle="round", zorder=1))
            else:
                (xa, ya), (xb, yb) = xy(d_in, lo - 0.48), xy(d_out, hi + 0.48)
                xl, xr, yl, yr = min(xa, xb), max(xa, xb), min(ya, yb), max(ya, yb)
                ax.add_patch(FancyBboxPatch((xl, yl), xr - xl, yr - yl, boxstyle="round,pad=0,rounding_size=0.18",
                                            facecolor=_tint(tok), edgecolor="none", lw=0, zorder=1))
        if c.get("label") or "bar" in c["styles"]:
            bar = "bar" in c["styles"]
            ec = P.edge(tok)
            if circ:
                rr = cs
                if bar:
                    bs = np.linspace(lo - 0.35, hi + 0.35, 60)
                    p = np.array([xy(rr, b) for b in bs])
                    ax.plot(p[:, 0], p[:, 1], color=ec, lw=2.4, solid_capstyle="round", zorder=zorder)
                if c.get("label"):
                    a = ang((lo + hi) / 2)
                    deg = math.degrees(a)
                    up = math.sin(a) >= 0
                    ax.text(*xy(rr + 0.22, (lo + hi) / 2), c["label"], fontsize=FONT["small"], weight="bold", color=ec,
                            rotation=deg - 90 if up else deg + 90, rotation_mode="anchor", ha="center",
                            va="bottom" if up else "top", style="italic" if c.get("italic") else "normal", zorder=20)
            elif direction == "right":
                (bx, by1), (_, by2) = xy(cs, lo - 0.3), xy(cs, hi + 0.3)
                if bar:
                    ax.plot([bx, bx], [by1, by2], color=ec, lw=2.4, solid_capstyle="round", zorder=zorder)
                if c.get("label"):
                    label(ax, (bx + (0.2 if bar else 0.0), (by1 + by2) / 2), c["label"], size="small", ha="left", bold=True,
                          color=ec, italic=c.get("italic", False))
            else:
                (bx1, by), (bx2, _) = xy(cs, lo - 0.3), xy(cs, hi + 0.3)
                if bar:
                    ax.plot([bx1, bx2], [by, by], color=ec, lw=2.4, solid_capstyle="round", zorder=zorder)
                if c.get("label"):
                    label(ax, ((bx1 + bx2) / 2, by + (0.14 if bar else 0.0)), c["label"], size="small", va="bottom", bold=True,
                          color=ec, italic=c.get("italic", False))

    # --- support values
    if support:
        for nd in root.walk():
            if nd.is_leaf or nd.support is None or nd is root:
                continue
            if support == "dot":
                ok = nd.support >= support_min
                ax.add_patch(Circle(nd.xy, 0.075 if ok else 0.06, facecolor=ink if ok else P.surface(), edgecolor=ink,
                                    lw=0.8, zorder=zorder + 3))
            elif nd.support >= support_min:
                x, y = nd.xy
                if not circ and direction == "right":
                    label(ax, (x - 0.13, y + 0.1), f"{nd.support:g}", size="tiny", ha="right", va="bottom", color=P.muted())
                else:
                    label(ax, (x - 0.07, y - 0.05), f"{nd.support:g}", size="tiny", ha="right", va="top", color=P.muted())

    # --- marks
    for m in marks or []:
        _mark(ax, T, m, xy, D, ink, zorder)
    return T


_MARK_TOKEN = {"trait": "positive", "loss": "negative", "duplication": "negative", "speciation": "dna", "dot": "neutral",
               "star": "highlight"}


def _branch_frame(T, node, at, xy, D):
    """Point at fraction ``at`` along the branch leading to ``node`` and the branch direction there."""
    par = node.parent
    if par is None and T.stem is not None:
        a, b = np.asarray(T.stem, float), np.asarray(node.xy, float)
        d = b - a
        return a + d * at, d / (np.linalg.norm(d) or 1.0)
    if par is None:
        p = np.asarray(node.xy, float)
        return p, np.array([1.0, 0.0]) if T.direction == "right" else np.array([0.0, 1.0])
    if T.layout == "slanted":
        a, b = np.asarray(par.xy, float), np.asarray(node.xy, float)
    else:  # rectangular / circular: the part of the branch at the child's breadth
        a, b = np.asarray(xy(D(par), node.breadth), float), np.asarray(node.xy, float)
    d = b - a
    nrm = np.linalg.norm(d) or 1.0
    return a + d * at, d / nrm


def marker(ax, xy, kind, token=None, size=0.2, direction=(1.0, 0.0), zorder=12):
    """One event symbol: "trait" (bar across a branch running along ``direction``), "loss" (crossed bar),
    "duplication" (square), "speciation" (circle), "dot", "star", "line" (a branch-colour swatch). Used by ``tree(marks=...)`` and legends."""
    tok = token or _MARK_TOKEN.get(kind, "neutral")
    p = np.asarray(xy, float)
    u = np.asarray(direction, float)
    u = u / (np.linalg.norm(u) or 1.0)
    n = np.array([-u[1], u[0]])
    s = size
    fc, ec = P.fill(tok), P.edge(tok)
    z = zorder
    if kind in ("trait", "loss"):
        hw = s * 0.32
        q = [p + n * s * 1.1 + u * hw, p + n * s * 1.1 - u * hw, p - n * s * 1.1 - u * hw, p - n * s * 1.1 + u * hw]
        ax.add_patch(Polygon(q, closed=True, facecolor=fc, edgecolor=ec, lw=0.8, zorder=z, joinstyle="round"))
        if kind == "loss":
            for sg in (1, -1):
                a, b = p + (n + sg * u) * s * 0.75, p - (n + sg * u) * s * 0.75
                ax.plot([a[0], b[0]], [a[1], b[1]], color=ec, lw=1.0, zorder=z + 1)
    elif kind == "line":  # a branch-colour swatch for legends
        a, b = p - u * s * 1.2, p + u * s * 1.2
        ax.plot([a[0], b[0]], [a[1], b[1]], color=ec, lw=LINE * 1.5, solid_capstyle="round", zorder=z)
    elif kind == "duplication":
        ax.add_patch(RegularPolygon(p, 4, radius=s * 0.85, orientation=math.pi / 4, facecolor=fc, edgecolor=ec, lw=0.9, zorder=z))
    elif kind == "speciation":
        ax.add_patch(Circle(p, s * 0.55, facecolor=fc, edgecolor=ec, lw=0.9, zorder=z))
    elif kind == "dot":
        ax.add_patch(Circle(p, s * 0.45, facecolor=fc, edgecolor=ec, lw=0.9, zorder=z))
    elif kind == "star":
        th = np.pi / 2 + np.arange(10) * np.pi / 5
        r = np.where(np.arange(10) % 2 == 0, s * 0.95, s * 0.42)
        ax.add_patch(Polygon(p + np.c_[r * np.cos(th), r * np.sin(th)], closed=True, facecolor=fc, edgecolor=ec, lw=0.9,
                             joinstyle="round", zorder=z))
    else:
        raise ValueError(f"unknown mark kind {kind!r}")


def legend(ax, xy, items, size="small", step=0.5, marker_size=0.2):
    """A key for event symbols: ``items`` = [(kind, text) or (kind, text, token)], listed downwards from ``xy``."""
    x, y = xy
    for it in items:
        kind, text = it[0], it[1]
        marker(ax, (x, y), kind, it[2] if len(it) > 2 else None, size=marker_size)
        label(ax, (x + 0.45, y), text, size=size, ha="left")
        y -= step
    return y


def _mark(ax, T, m, xy, D, ink, zorder):
    node = T.node(m["node"])
    kind = m.get("kind", "trait")
    tok = m.get("token", _MARK_TOKEN.get(kind, "neutral"))
    at = m.get("at", 0.5 if kind in ("trait", "loss") else 1.0)
    p, u = _branch_frame(T, node, at, xy, D)
    n = np.array([-u[1], u[0]])
    side = m.get("side", 1)
    # labels go to the side "below" a rightward branch / "right" of an upward one by default
    if n[1] > 0 or (abs(n[1]) < 1e-9 and n[0] < 0):
        n = -n
    n = n * side
    s = m.get("size", 0.2)
    marker(ax, p, kind, tok, size=s, direction=u, zorder=zorder + 4)
    if m.get("text"):
        off = m.get("offset", s * 1.35)
        q = p + n * off
        ha = "center"
        va = "top" if n[1] < -0.5 else "bottom" if n[1] > 0.5 else "center"
        if abs(n[1]) <= 0.5:
            ha = "left" if n[0] > 0 else "right"
        elif abs(n[0]) > 0.3:
            ha = "left" if n[0] > 0 else "right"
        q = q + np.asarray(m.get("shift", (0.0, 0.0)), float)
        label(ax, q, m["text"], size=m.get("text_size", "tiny"), ha=m.get("ha", ha), va=m.get("va", va), color=m.get("text_color") or P.ink(),
              italic=m.get("italic", False))


# --------------------------------------------------- geological time scale

# International Chronostratigraphic Chart v2024/12 (International Commission on Stratigraphy): base ages
# in Ma; colours are the CGMW RGB codes used by the chart. Entries: (name, base, top, colour, abbreviation).
EONS = [
    ("Phanerozoic", 538.8, 0.0, "#9AD9DD", "Phan."),
    ("Proterozoic", 2500.0, 538.8, "#F73563", "Prot."),
    ("Archean", 4031.0, 2500.0, "#F0047F", "Arch."),
    ("Hadean", 4567.0, 4031.0, "#AE027E", "Had."),
]
ERAS = [
    ("Cenozoic", 66.0, 0.0, "#F2F91D", "Cz"),
    ("Mesozoic", 251.902, 66.0, "#67C5CA", "Mz"),
    ("Paleozoic", 538.8, 251.902, "#99C08D", "Pz"),
    ("Neoproterozoic", 1000.0, 538.8, "#FEB342", "NP"),
    ("Mesoproterozoic", 1600.0, 1000.0, "#FDB462", "MP"),
    ("Paleoproterozoic", 2500.0, 1600.0, "#F74370", "PP"),
    ("Neoarchean", 2800.0, 2500.0, "#F99BC1", "NA"),
    ("Mesoarchean", 3200.0, 2800.0, "#F768A9", "MA"),
    ("Paleoarchean", 3600.0, 3200.0, "#F4449F", "PA"),
    ("Eoarchean", 4031.0, 3600.0, "#DA037F", "EA"),
    ("Hadean", 4567.0, 4031.0, "#AE027E", "Had."),
]
PERIODS = [
    ("Quaternary", 2.58, 0.0, "#F9F97F", "Q"),
    ("Neogene", 23.04, 2.58, "#FFE619", "N"),
    ("Paleogene", 66.0, 23.04, "#FD9A52", "Pg"),
    ("Cretaceous", 143.1, 66.0, "#7FC64E", "K"),
    ("Jurassic", 201.4, 143.1, "#34B2C9", "J"),
    ("Triassic", 251.902, 201.4, "#812B92", "T"),
    ("Permian", 298.9, 251.902, "#F04028", "P"),
    ("Carboniferous", 358.86, 298.9, "#67A599", "C"),
    ("Devonian", 419.62, 358.86, "#CB8C37", "D"),
    ("Silurian", 443.1, 419.62, "#B3E1B6", "S"),
    ("Ordovician", 486.85, 443.1, "#009270", "O"),
    ("Cambrian", 538.8, 486.85, "#7FA056", "Cm"),
    ("Ediacaran", 635.0, 538.8, "#FED96A", "Ed"),
    ("Cryogenian", 720.0, 635.0, "#FECC5C", "Cr"),
    ("Tonian", 1000.0, 720.0, "#FEBF4E", "To"),
    ("Stenian", 1200.0, 1000.0, "#FED99A", "St"),
    ("Ectasian", 1400.0, 1200.0, "#FDCC8A", "Ec"),
    ("Calymmian", 1600.0, 1400.0, "#FDC07A", "Ca"),
    ("Statherian", 1800.0, 1600.0, "#F875A7", "Sa"),
    ("Orosirian", 2050.0, 1800.0, "#F76898", "Or"),
    ("Rhyacian", 2300.0, 2050.0, "#F75B89", "Rh"),
    ("Siderian", 2500.0, 2300.0, "#F74F7C", "Si"),
]
EPOCHS = [  # Cenozoic epochs only
    ("Holocene", 0.0117, 0.0, "#FEF2E0", "H"),
    ("Pleistocene", 2.58, 0.0117, "#FFF2AE", "Ple"),
    ("Pliocene", 5.333, 2.58, "#FFFF99", "Pli"),
    ("Miocene", 23.04, 5.333, "#FFFF00", "Mio"),
    ("Oligocene", 33.9, 23.04, "#FDC07A", "Oli"),
    ("Eocene", 56.0, 33.9, "#FDB46C", "Eo"),
    ("Paleocene", 66.0, 56.0, "#FDA75F", "Pal"),
]
RANKS = {"eon": EONS, "era": ERAS, "period": PERIODS, "epoch": EPOCHS}


def _text_on(hex_colour):
    r, g, b = (int(hex_colour[i:i + 2], 16) / 255 for i in (1, 3, 5))
    lum = 0.2126 * r + 0.7152 * g + 0.0722 * b
    return "#ffffff" if lum < 0.45 else P.on_fill()


def geo_scale(ax, coords, ages, y, ranks=("period",), height=0.42, orientation="horizontal", size="tiny",
              labels="auto", edge=True, zorder=6):
    """The ICS geological time scale as stacked colour bands.

    coords  (start, end) canvas coordinates (x for horizontal, y for vertical) of the ages in ``ages``
    ages    (old, young) in Ma, e.g. (500, 0); units outside the range are clipped
    y       top edge of the first row (horizontal) or left edge of the first column (vertical)
    ranks   rows from top to bottom (or columns from left to right): any of "eon", "era", "period", "epoch"
    labels  "auto" (full name, else the ICS abbreviation, else nothing, whichever fits), "full", "abbr", None

    Returns the coordinate just past the last row (to place more content below). Colours are the ICS
    chart colours and stay the same in both themes; labels switch to white on the dark units.
    """
    (c0, c1), (a0, a1) = coords, ages

    def pos(a):
        return c0 + (a0 - a) / (a0 - a1) * (c1 - c0)

    edge_c = P.surface()
    k = 0
    for k, rank in enumerate(ranks):
        for name, base, top, col, abbr in RANKS[rank]:
            lo_a, hi_a = min(base, a0), max(top, a1)
            if lo_a <= hi_a:
                continue
            p0, p1 = pos(lo_a), pos(hi_a)
            length = abs(p1 - p0)
            if orientation == "horizontal":
                rect = (min(p0, p1), y - (k + 1) * height, length, height)
            else:
                rect = (y + k * height, min(p0, p1), height, length)
            ax.add_patch(FancyBboxPatch(rect[:2], rect[2], rect[3], boxstyle="square,pad=0", facecolor=col,
                                        edgecolor=edge_c if edge else "none", lw=0.6, zorder=zorder))
            if not labels:
                continue
            cx, cy = rect[0] + rect[2] / 2, rect[1] + rect[3] / 2
            room = length - 0.08
            choice = None
            cands = {"full": [name], "abbr": [abbr], "auto": [name, abbr]}[labels]
            for txt in cands:
                w_, h_ = _text_wh(ax, txt, size)
                if (w_ if orientation == "horizontal" else h_) <= room:
                    choice = txt
                    break
            if choice:
                label(ax, (cx, cy), choice, size=size, color=_text_on(col), rotation=0 if orientation == "horizontal" else 90,
                      zorder=zorder + 1)
    return y - len(ranks) * height if orientation == "horizontal" else y + len(ranks) * height


def period_of(age):
    """The ICS period containing an age (Ma)."""
    for name, base, top, *_ in PERIODS:
        if top <= age <= base:
            return name
    return None
