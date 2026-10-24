"""Plant figures: floral diagrams and floral formulae, simple plant schematics, plant life cycles.

    from wikibio import plant
    plant.floral_diagram(ax, (5, 5), 3, [
        dict(organ="tepal", n=3, phase=180), dict(organ="tepal", n=3),
        dict(organ="stamen", n=3), dict(organ="stamen", n=3),
        dict(organ="gynoecium", n=3, placentation="axile")])
    plant.floral_formula(ax, (5, 1), "* P3+3 A3+3 G_(3)")
    plant.alternation_of_generations(ax, (6, 6), 4, stages, meiosis=1, fertilization=4)

Floral diagram conventions (Eichler; Ronse De Craene, Floral Diagrams, 2010): the flower is seen from
above, the mother axis at the top (adaxial side) and the subtending bract at the bottom (abaxial side).
Sepals are drawn as crescents with a keel (midrib), petals and tepals as crescents, stamens as anther
cross-sections (four pollen sacs, introrse), staminodes as dots, and the gynoecium as a cross-section of
the ovary (locules, septa, ovules). Fusion is shown by lines: arcs between members of one whorl for
connation, radial lines between whorls for adnation. Angles are measured clockwise from the adaxial
side (0 = towards the axis, 180 = towards the bract).
"""

import math
import re

import numpy as np
from matplotlib.patches import Circle, Ellipse, PathPatch
from matplotlib.path import Path

from . import palette as P
from .core import FONT, LINE, label, smooth_closed

# Organ colours (tokens). The palette has no dedicated plant-organ tokens yet; these are the closest.
ORGAN_TOKEN = {"sepal": "sepal", "petal": "petal", "tepal": "tepal", "stamen": "anther", "staminode": "atp",
               "gynoecium": "ovary", "ovule": "ovule", "bract": "bract", "axis": "neutral"}


def _pol(c, r, deg):
    """Point at radius r and angle deg (clockwise from the top) around c."""
    a = math.radians(deg)
    return np.array([c[0] + r * math.sin(a), c[1] + r * math.cos(a)])


def _patch(ax, pts, token, lw=LINE * 0.85, zorder=6, fill=None, edge=None):
    ax.add_patch(PathPatch(Path(np.asarray(pts), closed=True), facecolor=fill or P.fill(token), edgecolor=edge or P.edge(token),
                           lw=lw, joinstyle="round", zorder=zorder))


def _cavity(token):
    """Fill of an empty space (locule) inside an organ of ``token``."""
    return P.mix(P.surface(), P.fill(token), 0.22)


# ---------------------------------------------------------- floral organs


def crescent(ax, c, r, deg, half_width, thickness, token="petal", keel=0.0, zorder=6):
    """A floral-diagram perianth member: a crescent centred on angle ``deg`` at radius r around c.

    ``half_width`` in degrees, ``thickness`` in canvas units; ``keel`` (fraction of thickness) adds the
    dorsal ridge drawn on sepals and bracts.
    """
    phi = np.linspace(-half_width, half_width, 81)
    prof = thickness * np.clip(np.cos(np.pi / 2 * phi / half_width), 0, None) ** 0.75
    bump = keel * thickness * np.exp(-(phi / (half_width * 0.12)) ** 2)
    outer = [_pol(c, r + 0.62 * p + b, deg + f) for f, p, b in zip(phi, prof, bump)]
    inner = [_pol(c, r - 0.38 * p, deg + f) for f, p in zip(phi[::-1], prof[::-1])]
    _patch(ax, outer + inner, token, zorder=zorder)
    if keel:
        # a short midrib line in the keel
        ax.plot(*np.array([_pol(c, r - 0.1 * thickness, deg), _pol(c, r + 0.55 * thickness + 0.6 * keel * thickness, deg)]).T,
                color=P.edge(token), lw=0.7, zorder=zorder + 1, solid_capstyle="round")
    return _pol(c, r, deg)


def anther(ax, xy, deg, size, token="stamen", introrse=True, zorder=7):
    """An anther in cross-section (two thecae with two pollen sacs each), facing the floral centre.

    ``deg``: the anther's angle around the flower (its back points outwards along it).
    """
    a = math.radians(deg)
    u = np.array([math.sin(a), math.cos(a)])  # radial outwards
    t = np.array([math.cos(a), -math.sin(a)])  # tangential
    sgn = -1 if introrse else 1  # pollen sacs towards the centre for introrse anthers
    half = [(0.0, 0.16), (0.28, 0.34), (0.72, 0.3), (0.98, 0.02), (0.82, -0.3), (0.5, -0.4), (0.22, -0.26), (0.0, -0.12)]
    pts = half + [(-x, y) for x, y in half[::-1]]
    local = np.array([(x, -sgn * y) for x, y in pts]) * size / 2
    world = np.asarray(xy) + local[:, :1] * t + local[:, 1:] * u * -1
    outline = smooth_closed(world[::-1], n=160)
    _patch(ax, outline, token, zorder=zorder)
    sac = P.mix(P.fill(token), "#ffffff", 0.55)
    for x in (-0.66, -0.3, 0.3, 0.66):
        p = np.asarray(xy) + t * x * size / 2 + u * (sgn * 0.06 * size)
        ax.add_patch(Ellipse(p, 0.32 * size / 2 * 1.2, 0.36 * size / 2 * 1.2, angle=-deg, facecolor=sac,
                             edgecolor=P.edge(token), lw=0.5, zorder=zorder + 1))
    ax.add_patch(Circle(np.asarray(xy) - u * sgn * 0.02 * size, 0.07 * size, facecolor=P.edge(token), edgecolor="none",
                        zorder=zorder + 1))


def _ovule(ax, xy, deg, size, zorder=9):
    ax.add_patch(Ellipse(xy, size * 0.75, size, angle=-deg, facecolor=P.fill(ORGAN_TOKEN["ovule"]),
                         edgecolor=P.edge(ORGAN_TOKEN["ovule"]), lw=0.6, zorder=zorder))


def _sector(c, r0, r1, a0, a1, n=40):
    arc1 = [_pol(c, r1, a) for a in np.linspace(a0, a1, n)]
    arc0 = [_pol(c, r0, a) for a in np.linspace(a1, a0, max(4, n // 3))]
    return np.array(arc1 + arc0)


def _rounded(pts, k=14):
    # smooth a polygon by resampling a few control points along it
    p = np.asarray(pts)
    idx = np.linspace(0, len(p) - 1, k, endpoint=False).astype(int)
    return smooth_closed(p[idx], n=200)


def ovary(ax, c, radius, n=3, placentation="axile", phase=0.0, ovules=2, token="gynoecium", zorder=8):
    """An ovary cross-section with ``n`` carpels. placentation: "axile" (n locules, ovules on the central
    axis), "parietal" (one locule, ovules on the wall where carpels meet), "free-central" (one locule,
    central column), "marginal" (a single carpel, ovules along its ventral suture, which faces the axis)
    or "basal" (one locule, one ovule). ``ovules`` = ovules per locule (axile) or per placenta.
    """
    c = np.asarray(c, float)
    ax.add_patch(Circle(c, radius, facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE * 0.9, zorder=zorder))
    cav = _cavity(token)
    os_ = radius * 0.17
    if placentation == "axile" and n > 1:
        span = 360.0 / n
        for k in range(n):
            mid = phase + k * span
            sec = _sector(c, radius * 0.2, radius * 0.8, mid - span / 2 + 9, mid + span / 2 - 9)
            _patch(ax, _rounded(sec, 16), token, fill=cav, edge=P.edge(token), lw=0.7, zorder=zorder + 1)
            for j in range(ovules):
                f = (j + 0.5) / ovules - 0.5
                p = _pol(c, radius * 0.4, mid + f * span * 0.5)
                _ovule(ax, p, mid + f * span * 0.5, os_, zorder=zorder + 2)
        ax.add_patch(Circle(c, radius * 0.1, facecolor=P.edge(token), edgecolor="none", zorder=zorder + 2))
    elif placentation in ("parietal", "free-central", "basal"):
        ax.add_patch(Circle(c, radius * 0.78, facecolor=cav, edgecolor=P.edge(token), lw=0.7, zorder=zorder + 1))
        if placentation == "parietal":
            span = 360.0 / n
            for k in range(n):
                a = phase + k * span + span / 2  # carpel margins meet between carpel midribs
                pl = _pol(c, radius * 0.7, a)
                ax.add_patch(Circle(pl, radius * 0.13, facecolor=P.fill(token), edgecolor=P.edge(token), lw=0.7, zorder=zorder + 2))
                for j in range(ovules):
                    f = (j + 0.5) / ovules - 0.5
                    _ovule(ax, _pol(c, radius * 0.52, a + f * 26), a, os_, zorder=zorder + 3)
        elif placentation == "free-central":
            ax.add_patch(Circle(c, radius * 0.22, facecolor=P.fill(token), edgecolor=P.edge(token), lw=0.7, zorder=zorder + 2))
            m = max(4, ovules * 2)
            for j in range(m):
                a = phase + j * 360 / m
                _ovule(ax, _pol(c, radius * 0.36, a), a, os_ * 0.9, zorder=zorder + 3)
        else:
            _ovule(ax, c, 0, os_ * 1.6, zorder=zorder + 3)
    elif placentation == "marginal":
        # a single carpel: ventral suture towards ``phase`` (default adaxial), ovules from both margins
        inner = [c + np.array([radius * 0.62 * math.sin(t), radius * 0.74 * math.cos(t)]) for t in np.linspace(0, 2 * math.pi, 60)]
        rot = math.radians(-phase)
        R = np.array([[math.cos(rot), -math.sin(rot)], [math.sin(rot), math.cos(rot)]])
        inner = [(p - c) @ R.T + c for p in inner]
        _patch(ax, inner, token, fill=cav, edge=P.edge(token), lw=0.7, zorder=zorder + 1)
        for j, side in enumerate((-1, 1) * max(1, ovules // 2)):
            p = _pol(c, radius * 0.42, phase + side * 32)
            _ovule(ax, p, phase + side * 32, os_ * 1.1, zorder=zorder + 2)
        # the ventral suture
        ax.plot(*np.array([_pol(c, radius * 0.74, phase), _pol(c, radius, phase)]).T, color=P.edge(token), lw=0.9,
                zorder=zorder + 2)
    else:
        raise ValueError(f"unknown placentation {placentation!r}")


def carpel(ax, c, size, deg, token="gynoecium", zorder=8):
    """A free carpel (apocarpous gynoecium) in cross-section, its ventral side facing the floral centre."""
    ovary(ax, c, size, n=1, placentation="marginal", phase=deg + 180, token=token, zorder=zorder)


# ------------------------------------------------------------ the diagram

_RANK = {"bract": 0, "sepal": 1, "tepal": 2, "petal": 3, "stamen": 4, "staminode": 4, "gynoecium": 5}


def floral_diagram(ax, center, radius, whorls, axis=True, bract=True, bracteoles=False, symmetry=None, hypanthium=None,
                   zorder=5):
    """Draw a floral diagram; returns {"whorls": [[member xy, ...], ...], "axis": xy, "bract": xy}.

    whorls (outermost first): dicts with
        organ     "sepal", "petal", "tepal", "stamen", "staminode" or "gynoecium"
        n         number of members
        phase     angle (deg, clockwise from the axis side) of member 0; default: alternating with the
                  previous whorl (the alternation rule); the first whorl defaults to an adaxial member
        r         radius (fraction of ``radius``); default spaced evenly from the outside in
        width, thickness   member half-width (deg) and thickness (fraction of ``radius``)
        connate   True (all neighbours fused), False, or a list of (i, j) neighbour pairs; with ``free=[k]``
                  the members k stay free (e.g. the vexillary stamen of diadelphous legume stamens)
        adnate    True: each member is joined by a line to the member of the previous whorl at its angle
                  (e.g. epipetalous stamens)
        members   per-member overrides: list of dicts (scale, width, r, token, keel)
        token     colour token; keel (sepals default 0.5)
        gynoecium: carpels ``n``, ``placentation`` (see ``ovary``), ``ovules``, ``fused`` (False: free
                  carpels, ``n`` of them on rings or a spiral), ``size`` (fraction of ``radius``)
    symmetry      None, "radial" or "bilateral" (dashed median plane through axis and bract)
    hypanthium    radius (fraction of ``radius``) of a circle marking a floral cup (perigynous flowers)
    """
    c = np.asarray(center, float)
    R = radius
    peri = [w for w in whorls if w["organ"] != "gynoecium"]
    k_out = len(peri)
    out = {"whorls": []}
    prev = None
    ring = {}
    for i, w in enumerate(peri):
        ring[id(w)] = w.get("r", 0.95 - (0.95 - 0.5) * (i / max(1, k_out - 1)) if k_out > 1 else 0.85)
    if axis:
        out["axis"] = _pol(c, R * 1.22, 0)
        ax.add_patch(Circle(out["axis"], R * 0.075, facecolor=P.fill(ORGAN_TOKEN["axis"]), edgecolor=P.edge(ORGAN_TOKEN["axis"]),
                            lw=LINE * 0.9, zorder=zorder))
    if bract:
        out["bract"] = crescent(ax, c, R * 1.24, 180, 34, R * 0.14, token=ORGAN_TOKEN["bract"], keel=0.55, zorder=zorder)
    if bracteoles:
        for a in (90, 270):
            crescent(ax, c, R * 1.18, a, 16, R * 0.09, token=ORGAN_TOKEN["bract"], keel=0.5, zorder=zorder)
    if hypanthium:
        ax.add_patch(Circle(c, hypanthium * R, fill=False, edgecolor=P.edge(ORGAN_TOKEN["bract"]), lw=1.2,
                            ls=(0, (4, 2.5)), zorder=zorder))
    if symmetry == "bilateral":
        ax.plot([c[0], c[0]], [c[1] - R * 1.38, c[1] + R * 1.35], color=P.muted(), lw=0.8, ls=(0, (4, 3)), zorder=zorder - 1)

    for w in whorls:
        organ = w["organ"]
        tok = w.get("token", ORGAN_TOKEN.get(organ, "neutral"))
        n = w.get("n", 5)
        if organ == "gynoecium":
            g = w.get("size", 0.3) * R
            if w.get("fused", True) or n == 1:
                pl = w.get("placentation", "axile" if n > 1 else "marginal")
                ph = w.get("phase", (prev["_phase"] + 180.0 / prev["n"]) if prev else 0.0)
                ovary(ax, c, g, n=n, placentation=pl, phase=ph if pl != "marginal" else w.get("phase", 0.0),
                      ovules=w.get("ovules", 2), token=tok, zorder=zorder + 3)
                out["whorls"].append([c])
            else:
                pos = []
                rings = w.get("rings")
                cs = w.get("carpel_size", 0.11) * R
                if rings is None:  # golden-angle spiral filling the disc
                    for k in range(n):
                        rr = g * 0.95 * math.sqrt((k + 0.5) / n)
                        pos.append((_pol(c, rr, k * 137.508), k * 137.508))
                else:
                    for rr, m, ph in rings:
                        for k in range(m):
                            a = ph + k * 360 / m
                            pos.append((_pol(c, rr * R, a), a))
                for p, a in pos:
                    carpel(ax, p, cs, a, token=tok, zorder=zorder + 3)
                out["whorls"].append([p for p, _ in pos])
            continue
        r = ring[id(w)] * R
        if "phase" in w:
            phase = w["phase"]
        elif prev is None:
            phase = 0.0
        else:
            phase = prev["_phase"] + 180.0 / n
        w["_phase"] = phase
        members = w.get("members") or [{}] * n
        angles = [phase + k * 360.0 / n for k in range(n)]
        pts = []
        base_hw = w.get("width", min(0.88 * 180.0 / n, 58))
        th = w.get("thickness", 0.17 if organ in ("sepal", "tepal", "petal") else 0.0) * R
        for k, a in enumerate(angles):
            m = members[k] if k < len(members) else {}
            a = m.get("angle", a)
            angles[k] = a
            rr = m.get("r", ring[id(w)]) * R
            sc = m.get("scale", 1.0)
            mt = m.get("token", tok)
            if organ in ("sepal", "petal", "tepal"):
                keel = m.get("keel", w.get("keel", 0.5 if organ == "sepal" else 0.0))
                pts.append(crescent(ax, c, rr, a, m.get("width", base_hw) * sc, th * sc, token=mt, keel=keel, zorder=zorder + 1 + k % 2))
            elif organ == "stamen":
                s = w.get("size", min(0.24, 0.85 * rr / R * math.pi / n * 1.6)) * R * sc
                p = _pol(c, rr, a)
                anther(ax, p, a, s, token=mt, zorder=zorder + 2)
                pts.append(p)
            elif organ == "staminode":
                p = _pol(c, rr, a)
                ax.add_patch(Circle(p, R * 0.03 * sc, facecolor=P.fill(mt), edgecolor=P.edge(mt), lw=0.7, zorder=zorder + 2))
                pts.append(p)
            else:
                raise ValueError(f"unknown organ {organ!r}")
        # fusion lines
        conn = w.get("connate", False)
        pairs = []
        if conn is True:
            free = set(w.get("free", []))
            pairs = [(k, (k + 1) % n) for k in range(n) if k not in free and (k + 1) % n not in free]
        elif conn:
            pairs = list(conn)
        ec = P.edge(tok)
        for i0, i1 in pairs:
            a0, a1 = angles[i0], angles[i1]
            if (a1 - a0) % 360 > 180:
                a0, a1 = a1, a0
            span = (a1 - a0) % 360
            hw0 = (members[i0] if i0 < len(members) else {}).get("width", base_hw) if organ != "stamen" else 360 / n * 0.18
            hw1 = (members[i1] if i1 < len(members) else {}).get("width", base_hw) if organ != "stamen" else 360 / n * 0.18
            if organ in ("sepal", "petal", "tepal"):
                hw0 *= (members[i0] if i0 < len(members) else {}).get("scale", 1.0) * 0.92
                hw1 *= (members[i1] if i1 < len(members) else {}).get("scale", 1.0) * 0.92
            rr = ring[id(w)] * R - (0.06 * R if organ == "stamen" else 0)
            aa = np.linspace(a0 + hw0, a0 + span - hw1, 20)
            if len(aa) and aa[-1] > aa[0]:
                arc = np.array([_pol(c, rr, x) for x in aa])
                ax.plot(arc[:, 0], arc[:, 1], color=ec, lw=1.3, solid_capstyle="round", zorder=zorder + 3)
        if w.get("adnate") and prev is not None:
            pr = ring[id(prev)] * R
            for k, a in enumerate(angles):
                ax.plot(*np.array([_pol(c, r + 0.07 * R, a), _pol(c, pr - 0.04 * R, a)]).T, color=ec, lw=1.1,
                        zorder=zorder + 3, solid_capstyle="round")
        w["n"] = n
        prev = w
        out["whorls"].append(pts)
    return out


# --------------------------------------------------------- floral formula

_SYMBOL = {"*": "✱", "✱": "✱", "⊕": "✱", "act": "✱", "↑": "↑", "zyg": "↑", "|": "↑", "⚥": "⚥", "♂": "♂", "♀": "♀"}


def floral_formula(ax, xy, formula, size="title", ha="center", color=None, zorder=20):
    """Render a floral formula, e.g. ``"* K5 C5 A∞ G_(5)"`` or ``"↑ K(5) C1+2+(2) A(9)+1 G_1"``.

    Tokens are separated by spaces: a symmetry symbol (``*`` actinomorphic, ``↑`` zygomorphic, ``⚥``),
    then organs K (calyx), C (corolla), P (perianth of tepals), A (androecium), G (gynoecium) followed by
    the number of members: ``5``, ``∞`` (or ``inf``), sums ``3+3`` for whorls, parentheses for connation
    ``(5)``. After G, ``_`` marks a superior ovary (line below the number) and ``^`` an inferior one (line
    above). Square brackets around tokens mark adnation: ``[C(5) A5]`` draws an arc joining them.
    Returns the (x0, x1) extent of the formula.
    """
    color = color or P.ink()
    fs = FONT.get(size, size)
    toks = formula.split()
    items = []  # (kind, text, extra)
    for tok in toks:
        open_b, close_b = tok.startswith("["), tok.endswith("]")
        tok = tok.strip("[]")
        if tok in _SYMBOL:
            items.append(dict(kind="sym", text=_SYMBOL[tok], open=open_b, close=close_b))
            continue
        m = re.fullmatch(r"([KCPAG])([_^]?)(.*)", tok)
        if not m:
            items.append(dict(kind="text", text=tok, open=open_b, close=close_b))
            continue
        letter, pos, count = m.groups()
        count = count.replace("inf", "∞")
        items.append(dict(kind="organ", text=letter, count=count, pos=pos, open=open_b, close=close_b))
    # measure
    ren = ax.figure.canvas.get_renderer()
    inv = ax.transData.inverted()

    def wh(text, fsz):
        t = ax.text(0, 0, text, fontsize=fsz)
        bb = t.get_window_extent(ren)
        t.remove()
        (x0, y0), (x1, y1) = inv.transform([(bb.x0, bb.y0), (bb.x1, bb.y1)])
        return abs(x1 - x0), abs(y1 - y0)

    sub = fs * 0.78
    space = wh("M", fs)[0] * 0.55
    widths = []
    for it in items:
        if it["kind"] == "organ":
            w0 = wh(it["text"], fs)[0]
            w1 = wh(it["count"], sub)[0] if it["count"] else 0
            it["w0"], it["w1"] = w0, w1
            widths.append(w0 + w1 + wh(" ", sub)[0] * 0.1)
        else:
            widths.append(wh(it["text"], fs)[0])
    total = sum(widths) + space * (len(items) - 1)
    x = xy[0] - (total / 2 if ha == "center" else total if ha == "right" else 0)
    y = xy[1]
    H = wh("K", fs)[1]
    spans = []
    for it, w in zip(items, widths):
        x0 = x
        if it["kind"] == "organ":
            ax.text(x, y, it["text"], fontsize=fs, color=color, ha="left", va="baseline", zorder=zorder)
            cx = x + it["w0"] + 0.02
            if it["count"]:
                ax.text(cx, y - H * 0.22, it["count"], fontsize=sub, color=color, ha="left", va="baseline", zorder=zorder)
                if it["pos"]:
                    yl = y - H * 0.38 if it["pos"] == "_" else y + H * 0.62
                    ax.plot([cx, cx + it["w1"]], [yl, yl], color=color, lw=1.0, zorder=zorder, solid_capstyle="butt")
        else:
            ax.text(x, y, it["text"], fontsize=fs, color=color, ha="left", va="baseline", zorder=zorder)
        spans.append((x0, x0 + w, it))
        x += w + space
    # adnation arcs
    start = None
    for x0, x1, it in spans:
        if it["open"]:
            start = (x0 + x1) / 2
        if it["close"] and start is not None:
            end = (x0 + x1) / 2
            t = np.linspace(0, math.pi, 40)
            yb = y + H * 1.05
            ax.plot(start + (end - start) * (1 - np.cos(t)) / 2, yb + H * 0.32 * np.sin(t), color=color, lw=0.9, zorder=zorder)
            start = None
    return (xy[0] - total / 2 if ha == "center" else x0, x)


# ---------------------------------------------------------- schematics


def _place(local, base, angle):
    a = math.radians(angle)
    Rm = np.array([[math.cos(a), -math.sin(a)], [math.sin(a), math.cos(a)]])
    return np.asarray(local) @ Rm.T + np.asarray(base, float)


def leaf(ax, base, length, width, angle=90.0, token="plant", veins=True, shape="lanceolate", zorder=6):
    """A simple leaf from ``base`` pointing along ``angle`` (deg, anticlockwise from +x).

    shape: "lanceolate", "ovate" or "linear"; ``veins`` draws the midrib and a few secondary veins.
    """
    s = np.linspace(0, 1, 40)
    if shape == "ovate":
        hw = width / 2 * np.sin(np.pi * s ** 0.75) ** 0.9
    elif shape == "linear":
        hw = width / 2 * np.minimum(1, 6 * s) * np.minimum(1, 4 * (1 - s)) ** 0.8
    else:
        hw = width / 2 * np.sin(np.pi * s) ** 0.85 * (1 - 0.25 * s)
    upper = np.c_[s * length, hw]
    lower = np.c_[s[::-1] * length, -hw[::-1]]
    pts = _place(np.vstack([upper, lower]), base, angle)
    _patch(ax, pts, token, lw=LINE * 0.7, zorder=zorder)
    if veins and length > 0.25:
        ec = P.edge(token)
        mid = _place(np.c_[s * length * 0.96, 0 * s], base, angle)
        ax.plot(mid[:, 0], mid[:, 1], color=ec, lw=0.7, zorder=zorder + 1, solid_capstyle="round")
        for f in (0.25, 0.45, 0.65):
            for sg in (1, -1):
                k = int(f * 39)
                q = _place([(f * length, 0), ((f + 0.12) * length, sg * hw[k] * 0.75)], base, angle)
                ax.plot(q[:, 0], q[:, 1], color=ec, lw=0.5, zorder=zorder + 1, solid_capstyle="round")
    return _place([(length, 0)], base, angle)[0]


def frond(ax, base, length, angle=90.0, pinnae=9, curl=0.12, token="plant", sori=False, zorder=6):
    """A once-pinnate fern frond: a curved rachis with alternating pinnae; ``sori`` dots their undersides."""
    s = np.linspace(0, 1, 60)
    rach = np.c_[s * length, curl * length * s ** 2]
    pts = _place(rach, base, angle)
    ec = P.edge(token)
    ax.plot(pts[:, 0], pts[:, 1], color=ec, lw=1.3, zorder=zorder + 1, solid_capstyle="round")
    for k in range(pinnae):
        f = 0.18 + 0.78 * k / max(1, pinnae - 1)
        i = int(f * 59)
        d = pts[min(59, i + 1)] - pts[max(0, i - 1)]
        da = math.degrees(math.atan2(d[1], d[0]))
        side = 1 if k % 2 == 0 else -1
        L = length * (0.34 * (1 - f) ** 0.6 + 0.05)
        a = da + side * 58
        leaf(ax, pts[i], L, L * 0.32, a, token=token, veins=False, zorder=zorder)
        if sori and L > 0.12:
            for g in (0.3, 0.5, 0.7):
                for sg in (1, -1):
                    q = _place([(g * L, sg * L * 0.07)], pts[i], a)[0]
                    ax.add_patch(Circle(q, L * 0.035 + 0.01, facecolor=P.edge("animal"), edgecolor="none", zorder=zorder + 2))
    tip = pts[-1]
    leaf(ax, tip, length * 0.08, length * 0.03, angle + math.degrees(math.atan(2 * curl)), token=token, veins=False, zorder=zorder)
    return tip


def fiddlehead(ax, base, size, angle=90.0, token="plant", zorder=6):
    """A young, coiled frond (crozier)."""
    t = np.linspace(0, 1, 120)
    stem = np.c_[np.zeros(40), np.linspace(0, size * 0.65, 40)]
    th = np.linspace(0, 3.4 * np.pi, 80)
    rr = size * 0.2 * np.exp(-0.17 * th)
    spiral = np.c_[size * 0.2 - rr * np.cos(th), size * 0.65 + rr * np.sin(th)]
    del t
    pts = _place(np.vstack([stem, spiral])[:, ::-1] * [1, 1], base, angle - 90)
    ax.plot(pts[:, 0], pts[:, 1], color=P.edge(token), lw=2.0, zorder=zorder, solid_capstyle="round")


def fern(ax, base, size, token="plant", sori=True, zorder=6):
    """A fern sporophyte: rhizome, roots, three fronds (one fertile with sori) and a fiddlehead."""
    x, y = base
    ax.plot([x - size * 0.32, x + size * 0.3], [y, y + size * 0.02], color=P.edge("animal"), lw=3.2, zorder=zorder + 2,
            solid_capstyle="round")
    for k, dx in enumerate(np.linspace(-0.28, 0.26, 7)):
        ang = -90 + (k - 3) * 14
        q = _place([(0, 0), (size * 0.14, size * 0.02), (size * 0.24, -size * 0.03)], (x + dx * size, y), ang)
        ax.plot(q[:, 0], q[:, 1], color=P.edge("animal"), lw=0.7, zorder=zorder + 1, solid_capstyle="round")
    frond(ax, (x - size * 0.08, y), size * 0.95, 112, pinnae=11, curl=-0.1, token=token, zorder=zorder)
    frond(ax, (x + size * 0.05, y), size * 1.0, 78, pinnae=11, curl=0.1, token=token, sori=sori, zorder=zorder)
    frond(ax, (x - size * 0.2, y), size * 0.7, 140, pinnae=9, curl=-0.14, token=token, zorder=zorder)
    fiddlehead(ax, (x + size * 0.2, y), size * 0.3, angle=80, token=token, zorder=zorder + 1)


def prothallus(ax, center, size, token="plant", gametangia=True, sporophyte=False, zorder=6):
    """A fern gametophyte (prothallus): a heart-shaped thallus with rhizoids, antheridia (small, among the
    rhizoids) and archegonia (near the apical notch); ``sporophyte=True`` adds a young sporophyte."""
    cx, cy = center
    t = np.linspace(0, 2 * np.pi, 200)
    # heart: notch at the top
    hx = 16 * np.sin(t) ** 3
    hy = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    pts = np.c_[hx, hy] / 32 * size + [cx, cy]
    _patch(ax, pts, token, lw=LINE * 0.8, zorder=zorder)
    ec = P.edge(token)
    for k in range(9):
        x0 = cx + (k - 4) * size * 0.06
        y0 = cy - size * 0.38
        q = np.c_[np.linspace(x0, x0 + (k - 4) * size * 0.02, 10),
                  np.linspace(y0, y0 - size * (0.25 + 0.05 * (k % 3)), 10)]
        q[:, 0] += np.sin(np.linspace(0, 3, 10)) * size * 0.015
        ax.plot(q[:, 0], q[:, 1], color=P.muted(), lw=0.6, zorder=zorder - 1)
    if gametangia:
        for k in range(5):  # antheridia near the rhizoids
            p = (cx + (k - 2) * size * 0.09, cy - size * 0.2 + (k % 2) * size * 0.05)
            ax.add_patch(Circle(p, size * 0.032, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.5,
                                zorder=zorder + 1))
        for k in range(3):  # archegonia below the notch
            p = (cx + (k - 1) * size * 0.08, cy + size * 0.12)
            ax.add_patch(Ellipse(p, size * 0.05, size * 0.08, facecolor=P.fill("receptor"), edgecolor=P.edge("receptor"),
                                 lw=0.5, zorder=zorder + 1))
    if sporophyte:
        frond(ax, (cx, cy + size * 0.1), size * 0.75, 95, pinnae=5, curl=0.08, token=token, zorder=zorder + 2)
        q = np.c_[np.linspace(cx, cx + size * 0.05, 10), np.linspace(cy + size * 0.1, cy - size * 0.55, 10)]
        ax.plot(q[:, 0], q[:, 1], color=P.edge("animal"), lw=0.9, zorder=zorder + 2)


def sporangium(ax, center, size, token="animal", open_=False, spores=True, zorder=6):
    """A leptosporangium on its stalk, with the annulus (row of thickened cells) over the capsule."""
    cx, cy = center
    ax.plot([cx, cx], [cy - size * 0.6, cy - size * 0.2], color=P.edge(token), lw=1.0, zorder=zorder)
    ax.add_patch(Ellipse((cx, cy), size * 0.62, size * 0.5, facecolor=P.light(token), edgecolor=P.edge(token), lw=0.9,
                         zorder=zorder))
    th = np.linspace(-0.2 * np.pi, 1.1 * np.pi, 13)
    for a in th:
        p0 = (cx + size * 0.31 * np.cos(a), cy + size * 0.25 * np.sin(a))
        p1 = (cx + size * 0.38 * np.cos(a), cy + size * 0.31 * np.sin(a))
        ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=P.edge(token), lw=1.4, zorder=zorder + 1, solid_capstyle="butt")
    if spores:
        for k in range(5):
            a = k * 2 * np.pi / 5
            ax.add_patch(Circle((cx + size * 0.13 * np.cos(a), cy + size * 0.1 * np.sin(a)), size * 0.055,
                                facecolor=P.fill(token), edgecolor=P.edge(token), lw=0.4, zorder=zorder + 1))


def spores(ax, center, size, n=6, token="animal", zorder=6):
    """Scattered bean-shaped (monolete) spores."""
    rng = np.random.default_rng(3)
    for k in range(n):
        p = np.asarray(center) + rng.uniform(-0.5, 0.5, 2) * size
        e = Ellipse(p, size * 0.26, size * 0.17, angle=rng.uniform(0, 180), facecolor=P.fill(token), edgecolor=P.edge(token),
                    lw=0.7, zorder=zorder)
        ax.add_patch(e)


def cell(ax, center, size, token="receptor", nucleus=True, zorder=6):
    """A round cell (egg, zygote) with a nucleus."""
    ax.add_patch(Circle(center, size / 2, facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE * 0.8, zorder=zorder))
    if nucleus:
        ax.add_patch(Circle(center, size * 0.17, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.7, zorder=zorder + 1))


def sperm(ax, center, size, angle=0.0, token="dna", zorder=6):
    """A multiflagellate (fern, cycad) sperm: a coiled cell body with a tuft of flagella."""
    th = np.linspace(0, 2.6 * np.pi, 80)
    r = size * 0.28 * (1 - th / (3.2 * np.pi))
    body = np.c_[r * np.cos(th), r * np.sin(th)]
    p = _place(body, center, angle)
    ax.plot(p[:, 0], p[:, 1], color=P.edge(token), lw=2.2, zorder=zorder, solid_capstyle="round")
    for k in range(5):
        q = np.c_[np.linspace(0, size * 0.55, 20), size * 0.05 * np.sin(np.linspace(0, 6, 20) + k)]
        q = _place(q, p[0], angle + 100 + k * 12)
        ax.plot(q[:, 0], q[:, 1], color=P.edge(token), lw=0.5, zorder=zorder)


# ---------------------------------------------------------- life cycles


def alternation_of_generations(ax, center, radius, stages, meiosis, fertilization, diploid_token="dna",
                               haploid_token="rna", start=90.0, labels=None, arrow_labels=None, **kw):
    """A plant life cycle on a circle with the diploid (2n) and haploid (n) phases as background sectors.

    stages         steps as for ``ecology.cycle`` (str or dict with text, draw, icon, extent, …)
    meiosis        index i: the arrow from stage i to i+1 is meiosis (2n → n)
    fertilization  index j: the arrow from stage j to j+1 is fertilization (n → 2n)
    Returns the node objects of ``ecology.cycle``.
    """
    from .ecology import cycle

    n = len(stages)
    al = list(arrow_labels or [None] * n)
    al += [None] * (n - len(al))
    al[meiosis] = dict(text="Meiosis", bold=True, color=P.edge(haploid_token), size="normal")
    al[fertilization] = dict(text="Fertilization", bold=True, color=P.edge(diploid_token), size="normal")
    lab = labels or ("Diploid (2n)", "Haploid (n)")
    f0, f1 = meiosis + 0.5, fertilization + 0.5
    sectors = [dict(start=f1, end=f0 + (n if f0 < f1 else 0), token=diploid_token, text=lab[0]),
               dict(start=f0, end=f1 + (n if f1 < f0 else 0), token=haploid_token, text=lab[1])]
    for s in sectors:
        s.setdefault("r0", radius * 0.38)
        s.setdefault("r1", radius * 1.36)
        s.setdefault("text_r", radius * 0.18)
    nodes = cycle(ax, center, radius, stages, start=start, arrow_labels=al, sectors=sectors, **kw)
    return nodes
