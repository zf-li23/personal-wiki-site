"""Plant morphology sheets: templates of real plants with part labels, comparison tables, native seed,
germination and fruit drawings.

Templates (``wikimedia/...`` icons with named parts, BIO_FIGURES.md section 5.1) carry the realistic
drawing; this module lays them out and labels them. Parametric botany (leaf shapes, phyllotaxis,
inflorescences, anatomical sections) lives in ``botany``; floral diagrams in ``plant``.

    from wikibio import plantmorph as PM
    s = PM.specimen(ax, "wikimedia/flower-section", at=(5, 4), height=5,
                    labels=[dict(part="petal", text="Petal", side="left"),
                            dict(at=(0.52, 0.93), text="Stigma", side="right")])
    PM.callouts(ax, [((3, 2), "Seed coat", "left"), ((4, 1), "Embryo", "right")], left=1.0, right=7.0)
    PM.sheet(ax, cells, origin=(0.5, 0.5), cell=(4, 4), cols=4)          # a grid of labelled specimens
    PM.table(ax, (0.5, 12), col_w=[3, 5, 5], row_h=[0.8, 2.4, 2.4], cells=[[...], ...])
    PM.seed(ax, (3, 3), 2.5, kind="eudicot")      # bean seed opened / maize grain in section
    PM.germination(ax, (1, 1), 4.0, kind="epigeal", stage=2)
    PM.fruit(ax, (2, 2), 2.0, kind="hesperidium")  # hesperidium, capsule, samara, caryopsis, achene

Icon ids must appear as string literals in the plot script (the build finds them there); this module only
forwards them to ``icons.icon``. Every function returns a dict of anchors for further callouts.
Label positions: ``labels`` items are dict(part=name | at=(fx, fy) as fractions of the drawn icon box
(0..1, y up), text, side "left"/"right", where "center"/"top"/"bottom"/"left"/"right"); labels on one side
are stacked in the order of their points so leader lines do not cross.
"""

import math

import numpy as np
from matplotlib.patches import Circle, PathPatch, Polygon
from matplotlib.path import Path

from . import palette as P
from .core import LINE, callout, label, smooth_closed
from .icons import icon as _icon
from .icons import icon_part as _icon_part

# Colour roles of the native drawings (existing palette tokens; one place to change them).
ROLE = {
    "seed_coat": "animal", "cotyledon": "golgi", "endosperm": "lipid", "aleurone": "atp", "embryo": "carbohydrate",
    "radicle": "positive", "pericarp": "atp", "soil": "animal", "shoot": "plant", "root": "bone", "scutellum": "ovule",
    "coleoptile": "chloroplast", "flavedo": "atp", "albedo": "bone", "segment": "drug", "vesicle": "rna",
    "wing": "bract", "seed": "animal", "fruit_wall": "ovary", "locule": "vesicle", "bulb_scale": "bone",
    "stem": "plant", "rhizome": "animal", "stolon": "plant",
}


def _fill(role):
    return P.fill(ROLE.get(role, role))


def _edge(role):
    return P.edge(ROLE.get(role, role))


def _patch(ax, pts, role, lw=LINE * 0.8, zorder=6, fill=None, alpha=None):
    pts = np.asarray(pts, float)
    path = Path(np.vstack([pts, pts[:1]]), closed=True)
    ax.add_patch(PathPatch(path, facecolor=fill or _fill(role), edgecolor=_edge(role), lw=lw, joinstyle="round",
                           zorder=zorder, alpha=alpha))


def _line(ax, pts, role, lw=LINE, zorder=6, color=None):
    pts = np.asarray(pts, float)
    ax.plot(pts[:, 0], pts[:, 1], color=color or _edge(role), lw=lw, solid_capstyle="round", zorder=zorder)


def _spline(points, n=80):
    """Smooth open curve through points (Catmull-Rom)."""
    p = np.asarray(points, float)
    if len(p) < 3:
        t = np.linspace(0, 1, n)[:, None]
        return p[0] + (p[-1] - p[0]) * t
    q = np.vstack([2 * p[0] - p[1], p, 2 * p[-1] - p[-2]])
    out = []
    per = max(2, n // (len(p) - 1))
    for i in range(1, len(q) - 2):
        p0, p1, p2, p3 = q[i - 1], q[i], q[i + 1], q[i + 2]
        for t in np.linspace(0, 1, per, endpoint=False):
            t2, t3 = t * t, t * t * t
            out.append(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t2 + (-p0 + 3 * p1 - 3 * p2 + p3) * t3))
    out.append(p[-1])
    return np.array(out)


def _tube(center_line, width_start, width_end=None):
    """Closed outline of a tapering tube around a polyline (for roots, stems, hypocotyls)."""
    c = np.asarray(center_line, float)
    w1 = width_start if width_end is None else width_end
    d = np.gradient(c, axis=0)
    d /= np.linalg.norm(d, axis=1)[:, None] + 1e-12
    nrm = np.c_[-d[:, 1], d[:, 0]]
    w = np.linspace(width_start, w1, len(c))[:, None] / 2
    return np.vstack([c + nrm * w, (c - nrm * w)[::-1]])


def _ellipse_pts(c, rx, ry, angle=0.0, n=120):
    t = np.linspace(0, 2 * np.pi, n, endpoint=False)
    a = math.radians(angle)
    x, y = rx * np.cos(t), ry * np.sin(t)
    return np.c_[c[0] + x * math.cos(a) - y * math.sin(a), c[1] + x * math.sin(a) + y * math.cos(a)]


# ---------------------------------------------------------------- labels


def callouts(ax, items, left=None, right=None, gap=0.42, size="small", top=None, bottom=None):
    """Leader-line labels stacked on the left and right of a drawing without crossings.

    items   list of (point, text, side) with side "left" or "right" (or a dict(point, text, side, y))
    left, right   x of the label column on each side
    gap     minimum vertical distance between labels; ``top``/``bottom`` clamp the column
    Returns {text: label xy}.
    """
    rows = []
    for it in items:
        if isinstance(it, dict):
            rows.append((tuple(it["point"]), it["text"], it.get("side", "right"), it.get("y")))
        else:
            p, t, s = it
            rows.append((tuple(p), t, s, None))
    out = {}
    for side, x in (("left", left), ("right", right)):
        sel = [r for r in rows if r[2] == side]
        if not sel:
            continue
        if x is None:
            raise ValueError(f"callouts: no x given for the {side} column")
        sel.sort(key=lambda r: -(r[3] if r[3] is not None else r[0][1]))
        ys = [r[3] if r[3] is not None else r[0][1] for r in sel]
        # push labels apart (top to bottom), then centre the stack on the points
        for _ in range(3):
            for i in range(1, len(ys)):
                if ys[i - 1] - ys[i] < gap:
                    ys[i] = ys[i - 1] - gap
            shift = (np.mean([r[0][1] for r in sel]) - np.mean(ys)) * 0.5
            if top is not None:
                shift = min(shift, top - ys[0])
            if bottom is not None:
                shift = max(shift, bottom - ys[-1])
            ys = [y + shift for y in ys]
            for i in range(1, len(ys)):
                if ys[i - 1] - ys[i] < gap:
                    ys[i] = ys[i - 1] - gap
        for (p, t, _, _), y in zip(sel, ys):
            callout(ax, p, (x, y), t, size=size)
            out[t] = (x, y)
    return out


def point_in(box, frac):
    """Canvas point at fractions (fx, fy) of a drawn icon box (x, y, w, h); fy = 0 is the bottom."""
    x, y, w, h = box
    return (x + frac[0] * w, y + frac[1] * h)


def specimen(ax, icon_id, at, height=None, width=None, labels=(), anchor="center", pad=0.5, left=None, right=None,
             gap=0.42, size="small", title=None, title_size="normal", italic=False, subtitle=None, zorder=10, **icon_kw):
    """Draw a template icon and label its parts; returns {"box", "points": {text: xy}, "labels"}.

    labels   dicts with ``part`` (a named part of the template; ``where`` picks the point on it) or ``at``
             (fractions of the drawn box, y up), ``text`` and ``side``; label columns sit ``pad`` outside
             the drawing unless ``left``/``right`` give their x
    title    text above the drawing (``italic`` for species names); ``subtitle`` below the title
    Other keywords go to ``icons.icon`` (``parts``, ``mute``, ``hide``, ``flip``, ``color``).
    """
    box = _icon(ax, icon_id, at=at, height=height if width is None else 1.0, width=width, anchor=anchor,
                zorder=zorder, **icon_kw)
    pts, items = {}, []
    for lab in labels:
        if "part" in lab:
            p = _icon_part(icon_id, lab["part"], at=at, height=height if width is None else 1.0, width=width, anchor=anchor,
                           flip=icon_kw.get("flip", False), where=lab.get("where", "center"))
        else:
            p = point_in(box, lab["at"])
        pts[lab["text"]] = p
        items.append(dict(point=p, text=lab["text"], side=lab.get("side", "right"), y=lab.get("y")))
    x0, y0, w, h = box
    lab_xy = callouts(ax, items, left=left if left is not None else x0 - pad, right=right if right is not None else x0 + w + pad,
                      gap=gap, size=size)
    if title:
        label(ax, (x0 + w / 2, y0 + h + 0.35), title, size=title_size, italic=italic, bold=not italic, va="bottom")
    if subtitle:
        label(ax, (x0 + w / 2, y0 - 0.3), subtitle, size="small", color=P.muted(), va="top")
    return {"box": box, "points": pts, "labels": lab_xy}


def sheet(ax, cells, origin, cell, cols, title_size="normal", draw_frame=False):
    """A grid of drawings with a title (and optional note) under each: cells are dicts with ``draw``
    (callable ``draw(ax, center, size)`` returning anything) and ``title``, ``note``, ``italic``.
    ``origin`` is the top-left corner, ``cell`` = (width, height). Returns the cell centres."""
    ox, oy = origin
    cw, ch = cell
    centers = []
    for k, c in enumerate(cells):
        r, q = divmod(k, cols)
        cx, cy = ox + (q + 0.5) * cw, oy - (r + 0.5) * ch
        centers.append((cx, cy))
        if draw_frame:
            ax.add_patch(PathPatch(Path([(cx - cw / 2 + 0.1, cy - ch / 2 + 0.1), (cx + cw / 2 - 0.1, cy - ch / 2 + 0.1),
                                         (cx + cw / 2 - 0.1, cy + ch / 2 - 0.1), (cx - cw / 2 + 0.1, cy + ch / 2 - 0.1),
                                         (0, 0)], [1, 2, 2, 2, 79]), fill=False, edgecolor=P.muted(), lw=0.5, zorder=1))
        c["draw"](ax, (cx, cy + 0.35), min(cw, ch) * 0.62)
        label(ax, (cx, cy - ch / 2 + 0.62), c["title"], size=title_size, bold=True, italic=c.get("italic", False))
        if c.get("note"):
            label(ax, (cx, cy - ch / 2 + 0.25), c["note"], size="tiny", color=P.muted())
    return centers


def table(ax, origin, col_w, row_h, cells, header_rows=1, header_cols=1, size="small", lines=True, band=True):
    """A comparison table. ``cells[r][c]`` is text, None, or a callable ``draw(ax, box)`` with
    box = (x0, y0, w, h). ``origin`` is the top-left corner. Header row and column are bold; alternate
    rows get a faint band. Returns the list of cell boxes [[(x0, y0, w, h), ...], ...]."""
    ox, oy = origin
    xs = np.r_[ox, ox + np.cumsum(col_w)]
    ys = np.r_[oy, oy - np.cumsum(row_h)]
    boxes = []
    for r, row in enumerate(cells):
        brow = []
        if band and r >= header_rows and (r - header_rows) % 2 == 1:
            ax.add_patch(Polygon([(xs[0], ys[r + 1]), (xs[-1], ys[r + 1]), (xs[-1], ys[r]), (xs[0], ys[r])],
                                 closed=True, facecolor=P.mix(P.surface(), P.muted(), 0.08), lw=0, zorder=0))
        for c, v in enumerate(row):
            b = (xs[c], ys[r + 1], xs[c + 1] - xs[c], ys[r] - ys[r + 1])
            brow.append(b)
            if v is None:
                continue
            if callable(v):
                v(ax, b)
            else:
                bold = r < header_rows or c < header_cols
                label(ax, (b[0] + (0.12 if c < header_cols else b[2] / 2), b[1] + b[3] / 2), v, size=size, bold=bold,
                      ha="left" if c < header_cols else "center")
        boxes.append(brow)
    if lines:
        for k, y in enumerate(ys):
            if k in (0, header_rows, len(ys) - 1):
                ax.plot([xs[0], xs[-1]], [y, y], color=P.muted(), lw=0.9 if k != header_rows else 0.7, zorder=2)
    return boxes


def presence(ax, xy, state, size=0.17, token="positive"):
    """A character-state marker: True (filled), False (open), "partial" (half filled), None (dash)."""
    x, y = xy
    if state is None:
        ax.plot([x - size, x + size], [y, y], color=P.muted(), lw=1.2, zorder=12)
        return
    ax.add_patch(Circle(xy, size, facecolor=P.fill(token) if state is True else P.surface(), edgecolor=P.edge(token)
                        if state else P.muted(), lw=1.0, zorder=12))
    if state == "partial":
        th = np.linspace(-np.pi / 2, np.pi / 2, 30)
        ax.add_patch(Polygon(np.c_[x + size * np.cos(th), y + size * np.sin(th)], closed=True, facecolor=P.fill(token),
                             lw=0, zorder=13))


# ---------------------------------------------------------------- seeds


def seed(ax, center, size, kind="eudicot", angle=0.0, zorder=6):
    """A seed in section. ``kind``:

    "eudicot"   a bean (Phaseolus) opened along its plane of symmetry: testa (seed coat), the inner face of
                one cotyledon, the embryo axis (radicle, hypocotyl) next to the hilum, and the plumule
                (epicotyl with the first two foliage leaves) between the cotyledons; no endosperm
                (exalbuminous seed, the food is stored in the cotyledons)
    "monocot"   a maize grain (caryopsis) in median longitudinal section: pericarp fused with the testa,
                starchy endosperm under a one-cell aleurone layer, and the embryo at the base on one side:
                scutellum (the single cotyledon) against the endosperm, coleoptile sheathing the plumule,
                coleorhiza sheathing the radicle
    ``size`` is the length of the seed. Returns anchors (canvas points) for callouts.
    """
    c = np.asarray(center, float)
    s = size
    a = math.radians(angle)
    R = np.array([[math.cos(a), -math.sin(a)], [math.sin(a), math.cos(a)]])

    def T(p):
        p = np.atleast_2d(np.asarray(p, float))
        return p @ R.T * s + c

    out = {}
    if kind == "eudicot":
        # kidney outline in local units (length 1, along x); hilum on the concave lower side
        ctrl = [(-0.5, 0.02), (-0.44, 0.22), (-0.24, 0.33), (0.05, 0.34), (0.3, 0.3), (0.47, 0.16), (0.5, -0.02),
                (0.43, -0.2), (0.25, -0.3), (0.1, -0.26), (0.0, -0.17), (-0.1, -0.22), (-0.27, -0.29), (-0.44, -0.2)]
        outer = smooth_closed(ctrl, n=240)
        cx = outer.mean(axis=0)
        inner = cx + (outer - cx) * 0.9
        _patch(ax, T(outer), "seed_coat", zorder=zorder)
        _patch(ax, T(inner), "cotyledon", zorder=zorder + 1)
        # veins of the cotyledon (faint) and its edge
        for k in (-1, 1):
            v = _spline([(-0.32, 0.02 * k), (-0.05, 0.12 * k + 0.02), (0.25, 0.08 * k + 0.02)], 40)
            _line(ax, T(v), "cotyledon", lw=0.6, zorder=zorder + 2)
        # embryo axis: radicle + hypocotyl curved, tip towards the micropyle, lying along the hilum side
        axis_c = _spline([(0.1, -0.03), (0.04, -0.12), (-0.04, -0.18), (-0.14, -0.2)], 40)
        _patch(ax, T(_tube(axis_c, 0.1, 0.06)), "radicle", zorder=zorder + 3)
        # plumule: two small folded foliage leaves at the top of the axis
        for k, sg in enumerate((1, -1)):
            leafc = _spline([(0.1, -0.03), (0.17, 0.02 + 0.03 * sg), (0.24, 0.0 + 0.04 * sg)], 30)
            _patch(ax, T(_tube(leafc, 0.05, 0.015)), "embryo", zorder=zorder + 4)
        # hilum: the scar on the outside of the coat
        hil = _ellipse_pts((0.0, -0.205), 0.07, 0.025)
        _patch(ax, T(hil), "seed_coat", fill=P.edge(ROLE["seed_coat"]), zorder=zorder + 2)
        out.update(seed_coat=tuple(T((0.0, 0.335))[0]), cotyledon=tuple(T((-0.22, 0.12))[0]),
                   plumule=tuple(T((0.21, 0.02))[0]), hypocotyl=tuple(T((0.04, -0.11))[0]),
                   radicle=tuple(T((-0.13, -0.2))[0]), hilum=tuple(T((0.02, -0.225))[0]),
                   micropyle=tuple(T((-0.2, -0.27))[0]))
        return out
    if kind == "monocot":
        # flattened drop: tip cap at the bottom (attachment), silk scar at the top
        ctrl = [(-0.5, 0.0), (-0.46, 0.2), (-0.32, 0.31), (-0.1, 0.36), (0.12, 0.33), (0.32, 0.25), (0.46, 0.12),
                (0.5, -0.02), (0.44, -0.16), (0.3, -0.27), (0.08, -0.33), (-0.15, -0.33), (-0.36, -0.25), (-0.47, -0.14)]
        outer = smooth_closed(ctrl, n=260)
        cx = outer.mean(axis=0)
        # rotate so that the long axis is vertical (tip cap down)
        rot = np.array([[0, -1], [1, 0]])
        outer = (outer - cx) @ rot.T
        peri = outer * 0.955
        aleu = outer * 0.92
        _patch(ax, T(outer), "pericarp", zorder=zorder)
        _patch(ax, T(peri), "aleurone", zorder=zorder + 1)
        _patch(ax, T(aleu), "endosperm", zorder=zorder + 2)
        # embryo on the lower left side: scutellum shield, embryo axis inside it
        scut = smooth_closed([(-0.22, -0.42), (-0.3, -0.25), (-0.3, -0.02), (-0.22, 0.12), (-0.14, 0.02), (-0.1, -0.2),
                              (-0.12, -0.4)], n=160)
        _patch(ax, T(scut), "scutellum", zorder=zorder + 3)
        ax_c = [(-0.24, -0.36), (-0.24, 0.0)]
        emb = smooth_closed([(-0.265, -0.38), (-0.29, -0.2), (-0.28, 0.02), (-0.25, 0.08), (-0.21, 0.02), (-0.2, -0.2),
                             (-0.215, -0.38)], n=120)
        _patch(ax, T(emb), "embryo", zorder=zorder + 4)
        cole = smooth_closed([(-0.265, -0.06), (-0.272, 0.03), (-0.25, 0.085), (-0.225, 0.03), (-0.222, -0.06)], n=60)
        _patch(ax, T(cole), "coleoptile", zorder=zorder + 5)
        rad = smooth_closed([(-0.262, -0.37), (-0.272, -0.3), (-0.262, -0.22), (-0.222, -0.22), (-0.216, -0.3),
                             (-0.226, -0.37)], n=60)
        _patch(ax, T(rad), "radicle", zorder=zorder + 5)
        del ax_c
        out.update(pericarp=tuple(T(outer[np.argmax(outer[:, 0])])[0]), aleurone=tuple(T(aleu[np.argmax(aleu[:, 0] + aleu[:, 1])] * 1.02)[0]),
                   endosperm=tuple(T((0.08, 0.1))[0]), scutellum=tuple(T((-0.15, -0.12))[0]),
                   coleoptile=tuple(T((-0.247, 0.06))[0]), plumule=tuple(T((-0.247, 0.0))[0]),
                   radicle=tuple(T((-0.244, -0.3))[0]), coleorhiza=tuple(T((-0.244, -0.37))[0]),
                   embryo=tuple(T((-0.25, -0.15))[0]))
        return out
    raise ValueError(f"unknown seed kind {kind!r}")


# ---------------------------------------------------------------- germination


def _soil(ax, x0, x1, y, depth=0.6, zorder=2):
    ax.add_patch(Polygon([(x0, y - depth), (x1, y - depth), (x1, y), (x0, y)], closed=True, facecolor=P.mix(P.surface(), P.fill(ROLE["soil"]), 0.4),
                         edgecolor="none", lw=0, zorder=zorder))
    ax.plot([x0, x1], [y, y], color=_edge("soil"), lw=1.0, zorder=zorder + 1)


def _leaf_pair(ax, base, size, angle=90.0, role="shoot", zorder=8):
    """Two opposite simple leaves at a node (the first foliage leaves of a bean)."""
    out = []
    for sg in (1, -1):
        th = math.radians(angle - sg * 55)
        tip = (base[0] + size * math.cos(th), base[1] + size * math.sin(th))
        mid = ((base[0] + tip[0]) / 2, (base[1] + tip[1]) / 2)
        n = (-(tip[1] - base[1]), tip[0] - base[0])
        nl = math.hypot(*n) or 1
        n = (n[0] / nl * size * 0.28, n[1] / nl * size * 0.28)
        pts = _spline([base, (mid[0] + n[0], mid[1] + n[1]), tip], 30)
        pts2 = _spline([tip, (mid[0] - n[0], mid[1] - n[1]), base], 30)
        _patch(ax, np.vstack([pts, pts2]), role, zorder=zorder)
        _line(ax, [base, tip], role, lw=0.6, zorder=zorder + 1)
        out.append(tip)
    return out


def _roots(ax, start, length, n=4, seed=0, role="root", lw=1.4, zorder=5, spread=0.35):
    """A primary root with a few laterals (and root hairs near the tip are left out for clarity)."""
    rng = np.random.default_rng(seed)
    main = np.array([(start[0] + 0.05 * length * math.sin(t * 3), start[1] - t * length) for t in np.linspace(0, 1, 30)])
    _line(ax, main, role, lw=lw, zorder=zorder)
    for k in range(n):
        f = 0.25 + 0.6 * k / max(1, n - 1)
        p = main[int(f * 29)]
        sg = 1 if k % 2 else -1
        L = length * spread * (1 - 0.5 * f) * (0.8 + 0.4 * rng.random())
        lat = _spline([p, (p[0] + sg * L * 0.6, p[1] - L * 0.25), (p[0] + sg * L, p[1] - L * 0.55)], 20)
        _line(ax, lat, role, lw=lw * 0.6, zorder=zorder)
    return main[-1]


def germination(ax, base, height, kind="epigeal", stage=3, zorder=6):
    """One stage of seed germination of a legume, drawn on a soil line at ``base`` (x, ground y).

    kind   "epigeal" (bean, Phaseolus): the hypocotyl elongates, forms a hook that pulls the cotyledons
           out of the soil, then straightens; the cotyledons become the first green organs above ground
           "hypogeal" (pea, Pisum): the cotyledons stay in the seed below ground; the epicotyl elongates
           and forms the hook; scale leaves, then foliage leaves above ground
    stage  1: radicle emerged; 2: hook breaking the soil surface; 3: seedling established
    Returns anchors (radicle/root, hypocotyl or epicotyl, cotyledons, leaves, seed, soil).
    """
    x, g = base
    h = height
    out = {"soil": (x + h * 0.45, g)}
    _soil(ax, x - h * 0.42, x + h * 0.42, g, depth=h * 0.55, zorder=zorder - 4)
    sd = (x, g - h * 0.18)
    cot_size = h * 0.11
    if kind == "epigeal":
        if stage == 1:
            seed(ax, sd, h * 0.2, kind="eudicot", angle=-10, zorder=zorder)
            tip = _roots(ax, (sd[0] - h * 0.02, sd[1] - h * 0.04), h * 0.16, n=0, zorder=zorder - 1, lw=1.8)
            out.update(seed=sd, radicle=tuple(tip))
            return out
        root_top = (x, g - h * 0.2)
        tip = _roots(ax, root_top, h * 0.32, n=4, zorder=zorder - 1)
        out["root"] = tuple(tip)
        if stage == 2:
            hook = _spline([root_top, (x, g - h * 0.02), (x + h * 0.02, g + h * 0.12), (x + h * 0.09, g + h * 0.17),
                            (x + h * 0.15, g + h * 0.12), (x + h * 0.16, g + h * 0.04)], 60)
            _patch(ax, _tube(hook, h * 0.035, h * 0.03), "stem", zorder=zorder)
            cot = hook[-1]
            for sg in (-1, 1):
                _patch(ax, _ellipse_pts((cot[0] + sg * h * 0.03, cot[1] - h * 0.03), cot_size * 0.45, cot_size * 0.65, angle=sg * 10),
                       "cotyledon", zorder=zorder + 1)
            out.update(hypocotyl=tuple(hook[30]), cotyledons=(cot[0] + h * 0.05, cot[1] - h * 0.03))
            return out
        top = (x, g + h * 0.42)
        stem = _spline([root_top, (x + h * 0.01, g + h * 0.15), top], 40)
        _patch(ax, _tube(stem, h * 0.04, h * 0.03), "stem", zorder=zorder)
        for sg in (-1, 1):
            _patch(ax, _ellipse_pts((x + sg * h * 0.075, top[1] - h * 0.01), cot_size * 0.75, cot_size * 0.45, angle=sg * 20),
                   "cotyledon", zorder=zorder + 2)
        epi = _spline([top, (x, top[1] + h * 0.14)], 10)
        _patch(ax, _tube(epi, h * 0.025, h * 0.02), "stem", zorder=zorder + 1)
        leaves = _leaf_pair(ax, tuple(epi[-1]), h * 0.2, zorder=zorder + 3)
        out.update(hypocotyl=tuple(stem[20]), cotyledons=(x + h * 0.13, top[1]), epicotyl=tuple(epi[5]),
                   leaves=tuple(leaves[0]))
        return out
    if kind == "hypogeal":
        seed(ax, sd, h * 0.17, kind="eudicot", angle=200 if stage > 1 else -10, zorder=zorder)
        out["seed"] = (sd[0] - h * 0.09, sd[1])
        if stage == 1:
            tip = _roots(ax, (sd[0], sd[1] - h * 0.04), h * 0.14, n=0, zorder=zorder - 1, lw=1.8)
            out["radicle"] = tuple(tip)
            return out
        tip = _roots(ax, (sd[0], sd[1] - h * 0.04), h * 0.3, n=4, zorder=zorder - 1)
        out["root"] = tuple(tip)
        if stage == 2:
            hook = _spline([(sd[0], sd[1] + h * 0.03), (x, g + h * 0.08), (x + h * 0.04, g + h * 0.15),
                            (x + h * 0.1, g + h * 0.13), (x + h * 0.11, g + h * 0.06)], 50)
            _patch(ax, _tube(hook, h * 0.03, h * 0.022), "stem", zorder=zorder + 1)
            out["epicotyl"] = tuple(hook[25])
            return out
        stem = _spline([(sd[0], sd[1] + h * 0.03), (x + h * 0.01, g + h * 0.2), (x, g + h * 0.55)], 40)
        _patch(ax, _tube(stem, h * 0.03, h * 0.022), "stem", zorder=zorder + 1)
        # scale leaves low on the epicotyl, then a foliage leaf pair (pea leaves are compound; simplified)
        for f, sg in ((0.35, 1), (0.48, -1)):
            p = stem[int(f * 39)]
            _patch(ax, _ellipse_pts((p[0] + sg * h * 0.025, p[1] + h * 0.01), h * 0.02, h * 0.008, angle=sg * 35), "shoot",
                   zorder=zorder + 2)
        leaves = _leaf_pair(ax, tuple(stem[-1]), h * 0.17, zorder=zorder + 3)
        out.update(epicotyl=tuple(stem[24]), leaves=tuple(leaves[0]))
        return out
    raise ValueError(f"unknown germination kind {kind!r}")


# ---------------------------------------------------------------- fruits drawn natively


def fruit(ax, center, size, kind="hesperidium", zorder=6):
    """Fruit types that have no template, drawn natively; ``size`` is the fruit diameter or length.

    "hesperidium"   citrus in cross-section: rind (exocarp with oil glands = flavedo, white spongy
                    mesocarp = albedo), segments (carpels, axile placentation) filled with juice vesicles
                    (hairs of the endocarp), seeds near the central axis
    "capsule"       a loculicidal capsule of three carpels (lily, iris type), opened along the midribs,
                    seen from above, seeds in the locules
    "samara"        a winged schizocarp of maple (Acer): two mericarps, each a seed-bearing nutlet with a wing
    "caryopsis"     a grass grain in section (pericarp fused with the seed coat); see ``seed(kind="monocot")``
    "achene"        a sunflower-type achene (cypsela): thin dry pericarp free from the single seed inside
    Returns anchors.
    """
    c = np.asarray(center, float)
    r = size / 2
    out = {}
    if kind == "hesperidium":
        _patch(ax, _ellipse_pts(c, r, r, n=180), "flavedo", zorder=zorder)
        _patch(ax, _ellipse_pts(c, r * 0.88, r * 0.88, n=180), "albedo", zorder=zorder + 1)
        n = 10
        for k in range(n):
            a0, a1 = 2 * np.pi * k / n + 0.03, 2 * np.pi * (k + 1) / n - 0.03
            th = np.linspace(a0, a1, 30)
            ro, ri = r * 0.8, r * 0.13
            seg = np.vstack([np.c_[c[0] + ro * np.cos(th), c[1] + ro * np.sin(th)],
                             np.c_[c[0] + ri * np.cos(th[::-1]), c[1] + ri * np.sin(th[::-1])]])
            seg = smooth_closed(seg[::3], n=120)
            _patch(ax, seg, "segment", zorder=zorder + 2)
            # juice vesicles: short spindles radiating in the segment
            for j, f in enumerate((0.35, 0.55, 0.72)):
                for u in (0.3, 0.7):
                    am = a0 + (a1 - a0) * u
                    p = (c[0] + r * f * math.cos(am), c[1] + r * f * math.sin(am))
                    _patch(ax, _ellipse_pts(p, r * 0.07, r * 0.018, angle=math.degrees(am), n=24), "vesicle", lw=0.5,
                           zorder=zorder + 3)
            if k % 3 == 0:
                am = (a0 + a1) / 2
                p = (c[0] + r * 0.2 * math.cos(am), c[1] + r * 0.2 * math.sin(am))
                _patch(ax, _ellipse_pts(p, r * 0.06, r * 0.035, angle=math.degrees(am), n=30), "seed", zorder=zorder + 4)
        _patch(ax, _ellipse_pts(c, r * 0.1, r * 0.1, n=40), "albedo", zorder=zorder + 3)
        for k in range(28):  # oil glands in the flavedo
            am = 2 * np.pi * k / 28 + 0.1
            ax.add_patch(Circle((c[0] + r * 0.94 * math.cos(am), c[1] + r * 0.94 * math.sin(am)), r * 0.018,
                                facecolor=_edge("flavedo"), lw=0, zorder=zorder + 2))
        am = math.radians(54)
        out.update(flavedo=(c[0] + r * 0.97 * math.cos(am), c[1] + r * 0.97 * math.sin(am)),
                   albedo=(c[0] + r * 0.84 * math.cos(am + 0.15), c[1] + r * 0.84 * math.sin(am + 0.15)),
                   segment=(c[0] + r * 0.5 * math.cos(-0.33), c[1] + r * 0.5 * math.sin(-0.33)),
                   vesicle=(c[0] + r * 0.62 * math.cos(-0.97), c[1] + r * 0.62 * math.sin(-0.97)),
                   seed=(c[0] + r * 0.2, c[1] + r * 0.02), axis=tuple(c))
        return out
    if kind == "capsule":
        for k in range(3):
            am = math.radians(90 + 120 * k)
            vc = (c[0] + r * 0.42 * math.cos(am), c[1] + r * 0.42 * math.sin(am))
            # each valve: a carpel wall split along its midrib (gap at the outer edge)
            th = np.linspace(am - 1.0, am + 1.0, 50)
            outer = np.c_[c[0] + r * 0.95 * np.cos(th), c[1] + r * 0.95 * np.sin(th)]
            inner = np.c_[c[0] + r * 0.12 * np.cos(th[::-1]), c[1] + r * 0.12 * np.sin(th[::-1])]
            wall = smooth_closed(np.vstack([outer, inner])[::2], n=140)
            _patch(ax, wall, "fruit_wall", zorder=zorder)
            loc = c + (wall - c) * 0.78 + (np.asarray(vc) - c) * 0.18
            _patch(ax, loc, "locule", zorder=zorder + 1)
            # split along the midrib: a notch drawn as a surface-coloured wedge
            tip = (c[0] + r * 1.0 * math.cos(am), c[1] + r * 1.0 * math.sin(am))
            base = (c[0] + r * 0.55 * math.cos(am), c[1] + r * 0.55 * math.sin(am))
            nrm = (-math.sin(am) * r * 0.08, math.cos(am) * r * 0.08)
            ax.add_patch(Polygon([base, (tip[0] + nrm[0], tip[1] + nrm[1]), (tip[0] - nrm[0], tip[1] - nrm[1])], closed=True,
                                 facecolor=P.surface(), edgecolor="none", zorder=zorder + 2))
            for j, f in enumerate((0.25, 0.4)):
                for sg in (-1, 1):
                    p = (c[0] + r * f * math.cos(am + sg * 0.42), c[1] + r * f * math.sin(am + sg * 0.42))
                    _patch(ax, _ellipse_pts(p, r * 0.07, r * 0.045, angle=math.degrees(am), n=30), "seed", zorder=zorder + 3)
            if k == 0:
                out.update(valve=tuple(outer[12]), locule=tuple(loc[len(loc) // 3]), split=tip,
                           seed=(c[0] + r * 0.4 * math.cos(am + 0.42), c[1] + r * 0.4 * math.sin(am + 0.42)))
        _patch(ax, _ellipse_pts(c, r * 0.12, r * 0.12, n=30), "fruit_wall", zorder=zorder + 3)
        out["axis"] = tuple(c)
        return out
    if kind == "samara":
        # two mericarps joined at the base (fruit stalk at c), wings spreading upwards at ~ 60 degrees
        stalk_top = (c[0], c[1] - r * 0.3)
        _line(ax, [stalk_top, (c[0], c[1] - r * 0.9)], "wing", lw=1.4, zorder=zorder)
        for sg in (-1, 1):
            nut = np.array((c[0] + sg * r * 0.16, c[1] - r * 0.24))
            ang = math.radians(90 - sg * 42)
            u = np.array((math.cos(ang), math.sin(ang)))
            v = np.array((-u[1], u[0])) * sg  # towards the outside of the pair
            L = r * 1.15
            # leading (inner) edge nearly straight and thick-veined; trailing edge a broad rounded bulge
            lead = _spline([nut, nut + u * L * 0.5 - v * r * 0.04, nut + u * L], 40)
            trail = _spline([nut + u * L, nut + u * L * 0.92 + v * r * 0.3, nut + u * L * 0.55 + v * r * 0.42,
                             nut + u * L * 0.22 + v * r * 0.22, nut], 60)
            wing = np.vstack([lead, trail])
            _patch(ax, wing, "wing", zorder=zorder)
            for f in (0.35, 0.55, 0.75, 0.9):  # veins fanning from the nutlet into the wing
                q1 = trail[int((1 - f) * 59)]
                _line(ax, _spline([nut + u * r * 0.1, (nut + u * r * 0.1 + q1) / 2 - v * r * 0.03, q1], 20), "wing", lw=0.5,
                      zorder=zorder + 1)
            _line(ax, lead, "wing", lw=1.1, zorder=zorder + 1)
            _patch(ax, _ellipse_pts(nut, r * 0.17, r * 0.12, angle=math.degrees(ang), n=40), "seed", zorder=zorder + 2)
            if sg == 1:
                out.update(wing=tuple(trail[20]), nutlet=tuple(nut), mericarp=tuple(nut + u * L))
        out["stalk"] = (c[0], c[1] - r * 0.7)
        return out
    if kind == "caryopsis":
        a = seed(ax, center, size, kind="monocot", zorder=zorder)
        return a
    if kind == "achene":
        ctrl = [(0, -0.5), (0.2, -0.38), (0.27, -0.05), (0.22, 0.3), (0.12, 0.46), (0.0, 0.5), (-0.12, 0.46), (-0.22, 0.3),
                (-0.27, -0.05), (-0.2, -0.38)]
        wall = smooth_closed(ctrl, n=180) * size + c
        _patch(ax, wall, "pericarp", zorder=zorder)
        cav = c + (wall - c) * 0.85
        _patch(ax, cav, "locule", zorder=zorder + 1)
        sd = c + (wall - c) * 0.72 + np.array([0, -size * 0.03])
        _patch(ax, sd, "seed", zorder=zorder + 2)
        emb = c + (wall - c) * 0.55 + np.array([0, -size * 0.04])
        _patch(ax, emb, "cotyledon", zorder=zorder + 3)
        for k in range(5):  # longitudinal ribs of the pericarp
            u = -0.18 + 0.09 * k
            _line(ax, np.c_[c[0] + u * size * np.ones(2), c[1] + np.array([-0.42, 0.42]) * size], "pericarp", lw=0.4, zorder=zorder + 1)
        out.update(pericarp=tuple(wall[30]), seed=tuple(sd[60]), cavity=tuple(cav[100]), embryo=tuple(c))
        return out
    raise ValueError(f"unknown fruit kind {kind!r}")


# ---------------------------------------------------------------- vegetative organs drawn natively


def bulb(ax, base, height, zorder=6):
    """An onion bulb in longitudinal section: fleshy scale leaves (leaf bases) on a short disc-shaped stem
    (basal plate), a terminal bud in the centre, dry outer scales (tunic) and adventitious roots below.
    ``base`` is the centre of the basal plate. Returns anchors."""
    x, y = base
    h = height
    w = h * 0.42
    out = {}
    for k in range(5):
        f = 1 - k * 0.17
        ctrl = [(0, 0.02), (w * 0.95 * f, h * 0.18), (w * 0.9 * f, h * 0.48 * (0.6 + 0.4 * f)), (w * 0.25 * f, h * 0.82 * (0.75 + 0.25 * f)),
                (0, h * (0.98 if k == 0 else 0.9 * (0.7 + 0.3 * f))), (-w * 0.25 * f, h * 0.82 * (0.75 + 0.25 * f)),
                (-w * 0.9 * f, h * 0.48 * (0.6 + 0.4 * f)), (-w * 0.95 * f, h * 0.18)]
        pts = smooth_closed(ctrl, n=200) + (x, y)
        role = "seed_coat" if k == 0 else "bulb_scale"
        _patch(ax, pts, role, zorder=zorder + k, fill=P.light(ROLE[role]) if k % 2 == 0 and k else None)
        if k == 0:
            out["tunic"] = (x - w * 0.88, y + h * 0.35)
        if k == 2:
            out["scale"] = (x - w * 0.6, y + h * 0.3)
    bud = smooth_closed([(0, 0.02), (w * 0.12, h * 0.2), (0, h * 0.52), (-w * 0.12, h * 0.2)], n=60) + (x, y)
    _patch(ax, bud, "shoot", zorder=zorder + 6)
    out["bud"] = (x, y + h * 0.35)
    plate = _ellipse_pts((x, y + h * 0.02), w * 0.55, h * 0.05, n=60)
    _patch(ax, plate, "stem", fill=P.light("plant"), zorder=zorder + 7)
    out["basal_plate"] = (x + w * 0.3, y + h * 0.02)
    for k in range(7):
        u = -0.4 + 0.8 * k / 6
        rl = _spline([(x + u * w, y - h * 0.02), (x + u * w * 1.3, y - h * 0.15), (x + u * w * 1.1 + 0.05, y - h * 0.3)], 20)
        _line(ax, rl, "root", lw=1.1, zorder=zorder - 1)
    out["roots"] = (x + w * 0.45, y - h * 0.22)
    return out


def rhizome(ax, start, length, zorder=6, nodes=5):
    """A rhizome: a horizontal underground stem with nodes, scale leaves, adventitious roots at the nodes
    and an aerial shoot from a bud; ``start`` is the older end on the soil-level reference line minus depth.
    Returns anchors."""
    x, y = start
    L = length
    out = {}
    stem = np.array([(x + t * L, y + 0.04 * L * math.sin(t * 5)) for t in np.linspace(0, 1, 60)])
    _patch(ax, _tube(stem, L * 0.06, L * 0.045), "rhizome", zorder=zorder)
    out["rhizome"] = tuple(stem[15])
    for k in range(nodes):
        f = (k + 0.5) / nodes
        p = stem[int(f * 59)]
        _line(ax, [(p[0], p[1] - L * 0.03), (p[0], p[1] + L * 0.03)], "rhizome", lw=1.0, zorder=zorder + 1)
        sc = _spline([(p[0], p[1] + L * 0.025), (p[0] + L * 0.04, p[1] + L * 0.045), (p[0] + L * 0.07, p[1] + L * 0.03)], 20)
        _line(ax, sc, "rhizome", lw=1.2, zorder=zorder + 1)
        for sg in (-0.6, 0.4):
            rl = _spline([(p[0], p[1] - L * 0.025), (p[0] + sg * L * 0.06, p[1] - L * 0.12), (p[0] + sg * L * 0.04, p[1] - L * 0.2)], 20)
            _line(ax, rl, "root", lw=0.9, zorder=zorder - 1)
        if k == 1:
            out["node"] = (p[0], p[1] + L * 0.03)
            out["scale_leaf"] = tuple(sc[-1])
        if k == 2:
            out["roots"] = tuple(rl[-1])
    tip = stem[-1]
    shoot = _spline([stem[-12], (stem[-12][0] + L * 0.02, stem[-12][1] + L * 0.25), (stem[-12][0] + L * 0.01, stem[-12][1] + L * 0.5)], 30)
    _patch(ax, _tube(shoot, L * 0.03, L * 0.02), "stem", zorder=zorder + 2)
    _leaf_pair(ax, tuple(shoot[-1]), L * 0.18, zorder=zorder + 3)
    out["shoot"] = tuple(shoot[20])
    out["tip"] = (tip[0] + L * 0.02, tip[1])
    return out


def stolon(ax, start, length, zorder=6):
    """A stolon (runner, strawberry type): a thin horizontal stem above ground from a mother plant
    rooting at a node into a daughter plantlet. ``start`` is the base of the mother plant. Returns anchors."""
    x, y = start
    L = length
    out = {}
    for dx in (0.0, L):
        for k, a in enumerate((60, 90, 120)):
            th = math.radians(a)
            base = (x + dx, y)
            tip = (base[0] + L * (0.28 if dx == 0 else 0.2) * math.cos(th), base[1] + L * (0.28 if dx == 0 else 0.2) * math.sin(th))
            _line(ax, [base, tip], "stem", lw=1.2, zorder=zorder)
            _patch(ax, _ellipse_pts(tip, L * (0.07 if dx == 0 else 0.05), L * (0.05 if dx == 0 else 0.035), angle=a, n=40), "shoot",
                   zorder=zorder + 1)
        for sg in (-1, 0, 1):
            rl = _spline([(x + dx, y), (x + dx + sg * L * 0.05, y - L * 0.08), (x + dx + sg * L * 0.07, y - L * 0.16)], 20)
            _line(ax, rl, "root", lw=0.9, zorder=zorder - 1)
    run = _spline([(x + L * 0.03, y + L * 0.02), (x + L * 0.5, y + L * 0.08), (x + L * 0.97, y + L * 0.01)], 50)
    _line(ax, run, "stolon", lw=1.6, zorder=zorder)
    out.update(stolon=tuple(run[25]), mother=(x, y + L * 0.2), plantlet=(x + L, y + L * 0.15), node_roots=(x + L, y - L * 0.12))
    return out


def pollen(ax, center, size, apertures=3, zorder=6):
    """A pollen grain in polar view showing its apertures: 1 = monosulcate (one long furrow; monocots,
    magnoliids, ANA grade, also gymnosperms), 3 = tricolpate (three furrows; eudicots). ``size`` is the
    diameter. Returns anchors (grain, aperture)."""
    c = np.asarray(center, float)
    r = size / 2
    if apertures == 1:
        _patch(ax, _ellipse_pts(c, r * 1.3, r * 0.78), "anther", zorder=zorder)
        _patch(ax, _ellipse_pts(c, r, r * 0.11), "anther", fill=_edge("anther"), zorder=zorder + 1)
        return {"grain": (c[0], c[1] + r * 0.6), "aperture": (c[0] + r * 0.5, c[1])}
    _patch(ax, _ellipse_pts(c, r, r), "anther", zorder=zorder)
    for k in range(apertures):
        a = math.radians(90 + 360 / apertures * k)
        p = (c[0] + r * 0.69 * math.cos(a), c[1] + r * 0.69 * math.sin(a))
        _patch(ax, _ellipse_pts(p, r * 0.4, r * 0.09, angle=math.degrees(a)), "anther", fill=_edge("anther"), zorder=zorder + 1)
    return {"grain": (c[0] - r * 0.5, c[1] - r * 0.4), "aperture": (c[0], c[1] + r * 0.69)}
