"""Plant figures: floral diagrams and floral formulae, simple plant schematics, plant life cycles, fungal,
fern and cone structures.

    from wikibio import plant
    plant.floral_diagram(ax, (5, 5), 3, [
        dict(organ="tepal", n=3, phase=180), dict(organ="tepal", n=3),
        dict(organ="stamen", n=3), dict(organ="stamen", n=3),
        dict(organ="gynoecium", n=3, placentation="axile")])
    plant.floral_formula(ax, (5, 1), "* P3+3 A3+3 G_(3)")
    plant.alternation_of_generations(ax, (6, 6), 4, stages, meiosis=1, fertilization=4)
    plant.floral_diagram_from_formula(ax, (5, 5), 3, "* K5 C5 A5+5 G_(5:5:2)")   whorls from a formula
    plant.floral_formula(ax, (5, 1), "* K5 C5 A∞ G_(5:5:2)", style="cn");  plant.floral_formula_tex("…")
    plant.life_cycle(ax, (6, 6), 3, kind="haplontic")       haplontic, diplontic, haplodiplontic, triphasic

Fungi (traditionally part of botany courses): ``hypha`` (septate, coenocytic, clamp connections), ``ascus``
and ``basidium`` (by developmental stage), ``paraphysis``, ``hymenium`` (a palisade along any curve),
``ascocarp`` (apothecium, perithecium, cleistothecium, pseudothecium in section), ``mushroom`` (agaric
basidiocarp, section or side view), ``gill_section``. Ferns: ``pinnule`` (sorus and indusium types),
``leptosporangium`` (annulus, stomium; closed, open, ejected). Cones: ``cone_scale`` (bract–scale complex
with ovules, microsporophyll) and ``cone`` (seed, pollen, lycopod, *Selaginella*, *Equisetum* strobili;
section or outside). Colours of these parts: ``PART``.

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
from .core import FONT, LINE, label, polyline, smooth_closed

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


def floral_formula(ax, xy, formula, size="title", ha="center", color=None, zorder=20, style="western"):
    """Render a floral formula, e.g. ``"* K5 C5 A∞ G_(5)"`` or ``"↑ K(5) C1+2+(2) A(9)+1 G_1"``.

    Tokens are separated by spaces: a symmetry symbol (``*`` actinomorphic, ``↑`` zygomorphic, ``⚥``),
    then organs K (calyx), C (corolla), P (perianth of tepals), A (androecium), G (gynoecium) followed by
    the number of members: ``5``, ``∞`` (or ``inf``), sums ``3+3`` for whorls, parentheses for connation
    ``(5)``. After G, ``_`` marks a superior ovary (line below the number) and ``^`` an inferior one (line
    above). Square brackets around tokens mark adnation: ``[C(5) A5]`` draws an arc joining them.
    ``G_(5:5:2)`` gives carpels : locules : ovules per locule.

    ``style="cn"`` follows the Chinese textbooks (the site's convention, as in the page text
    ``$\\ast K_5 C_5 A_\\infty \\underline{G}_{(5:5:2)}$``): the actinomorphy sign is the asterisk ∗ and the
    ovary line runs under (superior) or over (inferior) the letter G itself. ``floral_formula_tex`` gives the
    matching KaTeX source. Returns the (x0, x1) extent of the formula.
    """
    color = color or P.ink()
    fs = FONT.get(size, size)
    toks = formula.split()
    items = []  # (kind, text, extra)
    for tok in toks:
        open_b, close_b = tok.startswith("["), tok.endswith("]")
        tok = tok.strip("[]")
        if tok in _SYMBOL:
            sym = _SYMBOL[tok]
            if style == "cn" and sym == "✱":
                sym = r"$\ast$"
            items.append(dict(kind="sym", text=sym, open=open_b, close=close_b))
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
                if it["pos"] and style == "cn":
                    yl = y - H * 0.14 if it["pos"] == "_" else y + H * 1.06
                    ax.plot([x, x + it["w0"]], [yl, yl], color=color, lw=1.0, zorder=zorder, solid_capstyle="butt")
                elif it["pos"]:
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


# ------------------------------------------------- floral formula helpers: KaTeX, diagram from formula

_TEX_SYMBOL = {"✱": r"\ast", "↑": r"\uparrow", "⚥": r"\text{⚥}", "♂": r"\text{♂}", "♀": r"\text{♀}"}


def _formula_tokens(formula):
    """Split a floral formula into dicts: kind "sym" (text), "organ" (letter, pos, count) or "text"."""
    out = []
    depth = 0
    for tok in formula.split():
        opened = tok.startswith("[")
        closed = tok.endswith("]")
        depth += opened
        inside = depth > 0
        depth -= closed
        tok = tok.strip("[]")
        if tok in _SYMBOL:
            out.append(dict(kind="sym", text=_SYMBOL[tok]))
            continue
        m = re.fullmatch(r"([KCPAG])([_^]?)(.*)", tok)
        if not m:
            out.append(dict(kind="text", text=tok))
            continue
        letter, pos, count = m.groups()
        out.append(dict(kind="organ", letter=letter, pos=pos, count=count.replace("inf", "∞"), adnate=inside and not opened))
    return out


def floral_formula_tex(formula):
    """The KaTeX source of a floral formula in the Chinese textbook style used on the site.

    ``floral_formula_tex("* K5 C5 A∞ G_(5:5:2)")`` -> ``r"\\ast K_{5} C_{5} A_{\\infty} \\underline{G}_{(5:5:2)}"``;
    ``G^…`` (inferior ovary) gives ``\\overline{G}``. Same input syntax as ``floral_formula``; use it to keep
    the page text and a plot label (``floral_formula(..., style="cn")``) identical.
    """
    parts = []
    for t in _formula_tokens(formula):
        if t["kind"] == "sym":
            parts.append(_TEX_SYMBOL.get(t["text"], t["text"]))
        elif t["kind"] == "text":
            parts.append(t["text"])
        else:
            g = t["letter"]
            if t["pos"] == "_":
                g = r"\underline{%s}" % g
            elif t["pos"] == "^":
                g = r"\overline{%s}" % g
            cnt = t["count"].replace("∞", r"\infty ").replace(" )", ")").strip()
            parts.append(f"{g}_{{{cnt}}}" if cnt else g)
    return " ".join(parts)


def _terms(count):
    """'(9)+1' -> [(9, True), (1, False)]; '∞' -> [(None, False)]; '(5:5:2)' -> [((5, 5, 2), True)]."""
    out = []
    for term in count.split("+"):
        term = term.strip()
        if not term:
            continue
        conn = term.startswith("(") and term.endswith(")")
        term = term.strip("()")
        if ":" in term:
            val = tuple(None if v in ("∞", "") else int(v) for v in term.split(":"))
        else:
            val = None if term == "∞" else int(term)
        out.append((val, conn))
    return out


def _member_order(n, phase, bilateral):
    """Member indices in the order groups are assigned: around the circle, or (bilateral flowers) by
    distance from the adaxial side, in mirror pairs."""
    if not bilateral:
        return list(range(n))
    ang = [((phase + k * 360.0 / n) % 360.0) for k in range(n)]
    return sorted(range(n), key=lambda k: (round(min(ang[k], 360 - ang[k]), 6), ang[k]))


def floral_diagram_from_formula(ax, center, radius, formula, whorl_kw=None, gynoecium=None, **kw):
    """A floral diagram generated from a floral formula (same syntax as ``floral_formula``), e.g.
    ``"* K5 C5 A5+5 G_(5:5:2)"`` (one whorl per term of A without connation, and of P with equal terms), ``"↑ K(5) C1+2+(2) A(9)+1 G_1"`` (one
    whorl for K and C; in a zygomorphic flower the terms are assigned from the adaxial side in mirror
    pairs, single members first, so ``1+2+(2)`` gives standard, wings and the connate keel, and the odd
    sepal is put abaxial), ``"* P3+3 A3+3 G_(3:3:∞)"``. Stamens in square brackets with the corolla
    (``[C(5) A5]``) are drawn adnate (epipetalous).

    Parentheses give connation; for G, ``(n)`` is a syncarpous ovary and ``(c:l:o)`` gives carpels,
    locules and ovules per locule (locules = carpels: axile; one locule: parietal; one carpel: marginal),
    a bare ``n`` gives free carpels, ``∞`` many free carpels on a spiral. ``A∞`` draws two whorls of
    twice the perianth number. ``whorl_kw`` = {"K": dict(...), "A": [dict(...), dict(...)]} overrides the
    generated whorl dicts (see ``floral_diagram``); ``gynoecium`` overrides the gynoecium dict; other
    keywords go to ``floral_diagram``. Returns its result plus "whorls_spec" (the whorl dicts used).
    """
    toks = _formula_tokens(formula)
    bilateral = any(t["kind"] == "sym" and t["text"] == "↑" for t in toks)
    organs = {t["letter"]: t for t in toks if t["kind"] == "organ"}
    whorl_kw = whorl_kw or {}
    name = {"K": "sepal", "C": "petal", "P": "tepal", "A": "stamen"}
    whorls = []
    base_n = None

    def extra(letter, i):
        e = whorl_kw.get(letter)
        if isinstance(e, (list, tuple)):
            return dict(e[i]) if i < len(e) else {}
        return dict(e or {})

    for letter in ("K", "P", "C", "A"):
        if letter not in organs:
            continue
        terms = _terms(organs[letter]["count"])
        if not terms or all(v == 0 for v, _ in terms):
            continue
        if letter == "A" and terms[0][0] is None:  # numerous stamens: two whorls
            m = 2 * (base_n or 5)
            for i in range(2):
                w = dict(organ="stamen", n=m, connate=terms[0][1])
                w.update(extra(letter, i))
                whorls.append(w)
            continue
        separate = len(terms) > 1 and ((letter == "P" and len({v for v, _ in terms}) == 1)
                                       or (letter == "A" and not any(cn for _, cn in terms)))
        if separate:
            for i, (v, conn) in enumerate(terms):
                w = dict(organ=name[letter], n=v, connate=conn, adnate=organs[letter]["adnate"] and i == 0)
                w.update(extra(letter, i))
                whorls.append(w)
            base_n = base_n or terms[0][0]
            continue
        n = sum(v for v, _ in terms)
        w = dict(organ=name[letter], n=n, adnate=organs[letter]["adnate"])
        if len(terms) == 1:
            w["connate"] = terms[0][1]
        else:
            w["_groups"] = terms
        if letter == "K" and bilateral and "C" in organs:
            ct = _terms(organs["C"]["count"])
            if ct and ct[0][0] and ct[0][0] % 2 == 1:
                w["phase"] = 180.0  # odd sepal abaxial, so that an odd petal (standard) is adaxial
        w.update(extra(letter, 0))
        whorls.append(w)
        base_n = base_n or n
    # phases (the alternation rule of floral_diagram), needed to resolve connation groups
    prev = None
    for w in whorls:
        if "phase" not in w:
            w["phase"] = 0.0 if prev is None else prev["phase"] + 180.0 / w["n"]
        prev = w
        groups = w.pop("_groups", None)
        if groups:
            order = _member_order(w["n"], w["phase"], bilateral)
            groups = sorted(groups, key=lambda g: 0 if g[0] == 1 else 1)  # single members first
            owner, k = {}, 0
            for gi, (v, conn) in enumerate(groups):
                for idx in order[k:k + v]:
                    owner[idx] = (gi, conn)
                k += v
            n = w["n"]
            w["connate"] = [(i, (i + 1) % n) for i in range(n)
                            if owner[i][1] and owner[(i + 1) % n][0] == owner[i][0]]
    if "G" in organs:
        terms = _terms(organs["G"]["count"])
        v, conn = terms[0] if terms else (1, False)
        g = dict(organ="gynoecium")
        if isinstance(v, tuple):
            carp = v[0] or 3
            loc = v[1] if len(v) > 1 and v[1] else carp
            ov = v[2] if len(v) > 2 else 2
            g.update(n=carp, ovules=min(4, ov or 4))
            g["placentation"] = "marginal" if carp == 1 else "axile" if loc == carp else "parietal"
        elif conn or v == 1:
            g.update(n=v or 3, placentation="marginal" if v == 1 else "axile")
        else:
            g.update(n=v or 12, fused=False)
            if v and v <= 10:
                g["rings"] = [(0.22, v, prev["phase"] + 180.0 / v if prev else 0.0)]
        g.update(gynoecium or {})
        whorls.append(g)
    if bilateral:
        kw.setdefault("symmetry", "bilateral")
    out = floral_diagram(ax, center, radius, whorls, **kw)
    out["whorls_spec"] = whorls
    return out


# ------------------------------------------------------------- life-cycle types

LIFE_CYCLES = {
    # kind: (stages, meiosis index, fertilization index, arrow labels)
    "haplontic": (["Haploid thallus (n)", "Gametes (n)", "Zygote (2n)", "Meiospores (n)"], 2, 1,
                  ["Gametogenesis", None, None, "Germination"]),
    "diplontic": (["Diploid thallus (2n)", "Gametangia (2n)", "Gametes (n)", "Zygote (2n)"], 1, 2,
                  [None, None, None, "Growth"]),
    "haplodiplontic": (["Sporophyte (2n)", "Sporangium (2n)", "Spores (n)", "Gametophyte (n)", "Gametes (n)", "Zygote (2n)"],
                       1, 4, [None, None, "Germination", None, None, "Growth"]),
    "triphasic": (["Tetrasporophyte (2n)", "Tetraspores (n)", "Gametophytes (n)", "Gametes (n)", "Carposporophyte (2n)",
                   "Carpospores (2n)"], 1, 3, [None, "Germination", None, None, None, "Germination"]),
}
LIFE_CYCLES["zygotic"] = LIFE_CYCLES["haplontic"]
LIFE_CYCLES["gametic"] = LIFE_CYCLES["diplontic"]
LIFE_CYCLES["sporic"] = LIFE_CYCLES["haplodiplontic"]


def life_cycle(ax, center, radius, kind="haplodiplontic", stages=None, meiosis=None, fertilization=None, arrow_labels=None,
               **kw):
    """A life-cycle circle of one of the three basic types (plus the red-algal triphasic cycle), with the
    diploid and haploid phases as background sectors and the meiosis and fertilization arrows labelled.

    kind   "haplontic" (= "zygotic": zygotic meiosis, the zygote is the only diploid cell; *Chlamydomonas*,
           *Spirogyra*), "diplontic" (= "gametic": gametic meiosis, gametes are the only haploid cells; *Fucus*,
           diatoms, animals), "haplodiplontic" (= "sporic": sporic meiosis, alternation of a sporophyte and a
           gametophyte; *Ulva*, kelps, land plants) or "triphasic" (*Polysiphonia*: gametophyte, carposporophyte,
           tetrasporophyte)
    stages replaces the default stage texts (str or dicts as for ``ecology.cycle``: text, draw, icon, …);
           with a different number of stages pass ``meiosis`` / ``fertilization`` (arrow indices) too
    Other keywords go to ``alternation_of_generations`` / ``ecology.cycle`` (e.g. ``labels``, ``gap``,
    ``shape``, ``start``). Returns the node objects.
    """
    default, mei, fert, al = LIFE_CYCLES[kind]
    st = list(stages) if stages is not None else list(default)
    if stages is not None and len(st) != len(default) and (meiosis is None or fertilization is None):
        raise ValueError("life_cycle: pass meiosis= and fertilization= with a custom number of stages")
    mei = mei if meiosis is None else meiosis
    fert = fert if fertilization is None else fertilization
    if arrow_labels is None:
        arrow_labels = al if len(al) == len(st) else None
    return alternation_of_generations(ax, center, radius, st, meiosis=mei, fertilization=fert, arrow_labels=arrow_labels,
                                      **kw)


# ------------------------------------------------------------- fungi

# Colour roles for fungi, fern sori and cones (existing palette tokens; change them here only).
PART = {
    "hypha": "lipid_tail", "paraphysis": "lipid_tail", "ascus": "ovule", "ascospore": "drug", "basidium": "ovule",
    "basidiospore": "drug", "ascocarp": "golgi", "peridium": "animal", "stroma": "animal", "pileus": "animal",
    "context": "bone", "lamella": "golgi", "stipe": "bone", "annulus": "neutral", "volva": "neutral", "nucleus": "chromatin",
    "sporangium": "animal", "indusium": "bone", "spore": "animal", "ovuliferous_scale": "animal", "bract_scale": "bract",
    "ovule": "ovule", "pollen_sac": "anther", "cone_axis": "bone", "wing": "bract", "sporophyll": "plant",
    "sporangiophore": "plant", "megagametophyte": "lipid", "archegonium": "receptor",
}


def _poly(ax, pts, token, lw=LINE * 0.85, zorder=6, fill=None, edge=None):
    """Like ``_patch`` but keeps every vertex (the polygon is closed explicitly)."""
    pts = np.asarray(pts, float)
    pts = np.vstack([pts, pts[:1]])
    return ax.add_patch(PathPatch(Path(pts, closed=True), facecolor=fill or P.fill(token), edgecolor=edge or P.edge(token), lw=lw,
                                  joinstyle="round", zorder=zorder))


def _pt(name):
    return PART.get(name, name)


def _loc(base, angle, flip=False):
    """Map local (x along ``angle``, y to its left; to its right if ``flip``) to canvas points."""
    k = np.array([1.0, -1.0 if flip else 1.0])
    return lambda pts: _place(np.atleast_2d(np.asarray(pts, float)) * k, base, angle)


def _nuclei(ax, pts, r, zorder):
    for p in pts:
        ax.add_patch(Circle(p, r, facecolor=P.fill(_pt("nucleus")), edgecolor=P.edge(_pt("nucleus")), lw=0.4, zorder=zorder))


def hypha(ax, points, width=0.14, septa=0.9, nuclei=1, clamps=False, token="hypha", tip=True, zorder=6):
    """A hypha along a polyline (canvas points; smooth it first for curves): a tube with a rounded tip.

    septa   spacing of the cross walls (canvas units; each with a central pore), or None / 0 for a
            coenocytic hypha (no septa, many scattered nuclei)
    nuclei  nuclei per compartment: 1 (monokaryon), 2 (dikaryon), 0 (none drawn)
    clamps  True: a clamp connection beside every septum (dikaryotic hyphae of Basidiomycota)
    Returns {"path", "tip", "septa": [xy], "nuclei": [xy], "clamps": [xy], "wall": xy}.
    """
    q, nrm, L = polyline(points, n=max(40, int(60 * np.hypot(*np.ptp(np.asarray(points, float), axis=0)) / width / 4)))
    h = width / 2
    left, right = q + nrm * h, q - nrm * h
    out = dict(path=q, tip=q[-1], septa=[], nuclei=[], clamps=[], wall=left[len(left) // 3])
    d = q[-1] - q[-2]
    d /= np.hypot(*d) or 1
    cap = []
    if tip:
        a0 = math.atan2(nrm[-1][1], nrm[-1][0])
        cap = [q[-1] + h * np.array([math.cos(a0 - t), math.sin(a0 - t)]) for t in np.linspace(0, math.pi, 14)]
    outline = np.vstack([left, cap, right[::-1]]) if tip else np.vstack([left, right[::-1]])
    fc, ec = P.fill(_pt(token)), P.edge(_pt(token))
    ax.add_patch(PathPatch(Path(outline), facecolor=fc, edgecolor="none", zorder=zorder))
    ax.plot(*np.vstack([left, cap, right[::-1]]).T if tip else left.T, color=ec, lw=0.8, zorder=zorder + 0.1, solid_capstyle="round")
    if not tip:
        ax.plot(*right.T, color=ec, lw=0.8, zorder=zorder + 0.1)
    s = np.r_[0, np.cumsum(np.hypot(*np.diff(q, axis=0).T))]

    def at(u):
        i = int(np.clip(np.searchsorted(s, u), 1, len(s) - 1))
        return q[i], nrm[i]
    if septa:
        marks = np.arange(septa, s[-1] - septa * 0.4, septa)
        for u in marks:
            p, n_ = at(u)
            for sg in (1, -1):
                ax.plot(*np.array([p + sg * n_ * h * 0.95, p + sg * n_ * h * 0.22]).T, color=ec, lw=1.2, zorder=zorder + 0.2,
                        solid_capstyle="butt")
            out["septa"].append(p)
            if clamps:
                t_ = np.array([n_[1], -n_[0]])  # along the hypha (tip direction)
                arc = [p + n_ * h * 0.9 + t_ * (width * 0.9 * math.cos(a)) + n_ * width * 0.55 * math.sin(a)
                       for a in np.linspace(math.pi * 0.95, math.pi * 0.05, 16)]
                arc = np.array(arc)
                ax.plot(*arc.T, color=ec, lw=width * 30, zorder=zorder - 0.1, solid_capstyle="round")
                ax.plot(*arc.T, color=fc, lw=width * 30 - 1.6, zorder=zorder - 0.05, solid_capstyle="round")
                out["clamps"].append(arc[len(arc) // 2])
        bounds = np.r_[0, marks, s[-1]]
        for u0, u1 in zip(bounds[:-1], bounds[1:]):
            for j in range(nuclei):
                f = (j + 1) / (nuclei + 1)
                p, n_ = at(u0 + (u1 - u0) * (0.3 + 0.4 * f))
                out["nuclei"].append(p)
    elif nuclei:
        for u in np.arange(width * 2.5, s[-1] - width, width * 2.2):
            p, n_ = at(u)
            out["nuclei"].append(p + n_ * h * 0.35 * math.sin(u * 7.0))
    if nuclei:
        _nuclei(ax, out["nuclei"], width * 0.2, zorder + 0.3)
    return out


def _club(L, W, base_frac=0.32, taper=0.3, n=70):
    """Half-width profile of a club-shaped cell along its axis (x from 0 to L), rounded apex."""
    a = W / 2
    s = np.linspace(0, L, n)
    hw = a * (base_frac + (1 - base_frac) * np.clip(s / (taper * L), 0, 1) ** 0.6)
    cap0 = L - a
    m = s > cap0
    hw[m] = np.minimum(hw[m], a * np.sqrt(np.clip(1 - ((s[m] - cap0) / a) ** 2, 0, 1)))
    return s, hw


def _cell_outline(s, hw):
    return np.vstack([np.c_[s, hw], np.c_[s[::-1], -hw[::-1]]])


ASCUS_STAGES = ("dikaryotic", "karyogamy", "meiosis", "mitosis", "mature", "young")


def ascus(ax, base, length, angle=90.0, width=None, stage="mature", spores=8, arrangement="uniseriate", operculum=False,
          bitunicate=False, token="ascus", spore_token="ascospore", zorder=8):
    """An ascus (sac-like meiosporangium of Ascomycota) from ``base`` along ``angle``.

    stage        "young" (empty), "dikaryotic" (two nuclei), "karyogamy" (one diploid nucleus), "meiosis"
                 (four nuclei), "mitosis" (eight nuclei), "mature" (eight ascospores, or ``spores``)
    arrangement  "uniseriate" (one row) or "biseriate" (two staggered rows)
    operculum    True: a lid at the apex (operculate asci of Pezizales)
    bitunicate   True: the two-layered wall (inner wall line) of Dothideomycetes
    Returns {"base", "apex", "wall", "spores": [xy], "nuclei": [xy]}.
    """
    W = width or 0.22 * length
    f = _loc(base, angle)
    s, hw = _club(length, W)
    out_ = f(_cell_outline(s, hw))
    _poly(ax, out_, _pt(token), lw=0.8, zorder=zorder)
    ec = P.edge(_pt(token))
    out = dict(base=f([0, 0])[0], apex=f([length, 0])[0], wall=f([0.55 * length, hw[len(hw) // 2]])[0], spores=[], nuclei=[])
    if bitunicate:
        inner = _cell_outline(s[s < length * 0.96] * 0.97 + length * 0.01, hw[s < length * 0.96] * 0.78)
        ax.plot(*f(np.vstack([inner, inner[:1]])).T, color=ec, lw=0.55, zorder=zorder + 0.1)
    if operculum:
        a = W / 2
        t = np.linspace(-0.75, 0.75, 12)
        lid = np.c_[length - a + a * np.cos(t) * 0.82, a * np.sin(t) * 0.82]
        ax.plot(*f(lid).T, color=ec, lw=0.9, zorder=zorder + 0.2)
    a = W / 2
    if stage == "mature":
        lo, hi = 0.3 * length, length - 0.35 * a
        if arrangement == "biseriate":
            rows = int(math.ceil(spores / 2))
            d = (hi - lo) / rows
            for k in range(spores):
                r_, sg = k // 2, (1 if k % 2 == 0 else -1)
                x = lo + d * (r_ + 0.5 + 0.25 * sg)
                out["spores"].append(f([x, sg * a * 0.34])[0])
            rx, ry = d * 0.45, a * 0.34
        else:
            d = (hi - lo) / spores
            for k in range(spores):
                out["spores"].append(f([lo + d * (k + 0.5), 0])[0])
            rx, ry = d * 0.46, min(a * 0.62, d * 0.34)
        for p in out["spores"]:
            ax.add_patch(Ellipse(p, 2 * rx, 2 * ry, angle=angle, facecolor=P.fill(_pt(spore_token)),
                                 edgecolor=P.edge(_pt(spore_token)), lw=0.5, zorder=zorder + 1))
    elif stage != "young":
        k = {"dikaryotic": 2, "karyogamy": 1, "meiosis": 4, "mitosis": 8}[stage]
        lo, hi = 0.4 * length, length - 0.6 * a
        xs = [0.5 * (lo + hi)] if k == 1 else list(np.linspace(lo, hi, k))
        out["nuclei"] = [f([x, (0.25 * a if (j % 2 and k > 2) else -0.25 * a if k > 2 else 0)])[0] for j, x in enumerate(xs)]
        _nuclei(ax, out["nuclei"], a * (0.42 if k == 1 else 0.3 if k == 2 else 0.24), zorder + 1)
    return out


def paraphysis(ax, base, length, angle=90.0, width=None, token="paraphysis", septa=2, zorder=7):
    """A paraphysis (sterile filament among asci): a thin septate hypha with a swollen tip."""
    w = width or length * 0.07
    f = _loc(base, angle)
    pts = f(np.c_[np.linspace(0, length * 0.94, 12), np.zeros(12)])
    hypha(ax, pts, width=w, septa=length / (septa + 1) if septa else None, nuclei=0, token=token, zorder=zorder)
    ax.add_patch(Circle(f([length * 0.94, 0])[0], w * 0.85, facecolor=P.fill(_pt(token)), edgecolor=P.edge(_pt(token)),
                        lw=0.7, zorder=zorder + 0.15))
    return f([length, 0])[0]


BASIDIUM_STAGES = ("dikaryotic", "karyogamy", "meiosis", "sterigmata", "mature", "young")


def basidium(ax, base, length, angle=90.0, width=None, stage="mature", spores=4, token="basidium", spore_token="basidiospore",
             zorder=8):
    """A holobasidium (club-shaped meiosporangium of Agaricomycetes) from ``base`` along ``angle``.

    stage "young", "dikaryotic" (two nuclei), "karyogamy" (diploid nucleus), "meiosis" (four nuclei),
          "sterigmata" (four sterigmata with spore initials), "mature" (basidiospores on the sterigmata,
          each with its hilar appendix offset to the inner side, as for ballistospores)
    Returns {"base", "apex", "sterigmata": [tip xy], "spores": [xy], "nuclei": [xy], "wall"}.
    """
    W = width or 0.3 * length
    f = _loc(base, angle)
    s, hw = _club(length, W, base_frac=0.38, taper=0.85)
    _poly(ax, f(_cell_outline(s, hw)), _pt(token), lw=0.8, zorder=zorder)
    a = W / 2
    out = dict(base=f([0, 0])[0], apex=f([length, 0])[0], wall=f([0.5 * length, hw[len(hw) // 2]])[0], sterigmata=[], spores=[],
               nuclei=[])
    if stage in ("sterigmata", "mature"):
        offs = np.linspace(-1, 1, spores) if spores > 1 else [0.0]
        ec = P.edge(_pt(token))
        for o in offs:
            th = o * (0.95 if spores > 2 else 0.6)  # radians from the axis
            root = np.array([length - a + a * math.cos(th) * 0.9, a * math.sin(th) * 0.9])
            u = np.array([math.cos(th * 1.15), math.sin(th * 1.15)])
            sl = length * 0.28
            pts = np.array([root + u * sl * t + np.array([0, -o * sl * 0.12 * t * t]) for t in np.linspace(0, 1, 10)])
            wp = f(pts)
            ax.plot(*wp.T, color=ec, lw=2.0, zorder=zorder - 0.1, solid_capstyle="round")
            ax.plot(*wp.T, color=P.fill(_pt(token)), lw=0.9, zorder=zorder + 0.05, solid_capstyle="round")
            tip = pts[-1]
            out["sterigmata"].append(f(tip)[0])
            if stage == "mature":
                d = (pts[-1] - pts[-3]) / (np.hypot(*(pts[-1] - pts[-3])) or 1)
                nn = np.array([-d[1], d[0]]) * (-1 if o > 0 else 1)
                sp_len = length * 0.22
                c = tip + d * sp_len * 0.45 + nn * sp_len * 0.12
                ang = angle + math.degrees(math.atan2(d[1], d[0])) + (12 if o <= 0 else -12)
                p = f(c)[0]
                ax.add_patch(Ellipse(p, sp_len, sp_len * 0.6, angle=ang, facecolor=P.fill(_pt(spore_token)),
                                     edgecolor=P.edge(_pt(spore_token)), lw=0.5, zorder=zorder + 1))
                out["spores"].append(p)
            else:
                p = f(tip + u * length * 0.03)[0]
                ax.add_patch(Circle(p, length * 0.05, facecolor=P.fill(_pt(spore_token)), edgecolor=P.edge(_pt(spore_token)),
                                    lw=0.5, zorder=zorder + 1))
                out["spores"].append(p)
    elif stage != "young":
        k = {"dikaryotic": 2, "karyogamy": 1, "meiosis": 4}[stage]
        xs = [0.7 * length] if k == 1 else list(np.linspace(0.55 * length, length - 0.6 * a, k))
        out["nuclei"] = [f([x, (0.3 * a * (-1) ** j if k == 4 else 0)])[0] for j, x in enumerate(xs)]
        _nuclei(ax, out["nuclei"], a * (0.4 if k == 1 else 0.28), zorder + 1)
    return out


def hymenium(ax, curve, height, kind="ascus", side=1, spacing=None, paraphyses=True, seed=0, stage=None, zorder=8, **kw):
    """A hymenium (fertile layer) along a curve: a palisade of asci and paraphyses, or of basidia, standing
    on the curve's normal (``side`` = ±1 picks the side). ``height`` is the length of the cells.

    kind     "ascus" or "basidium"; ``stage`` fixes the stage of all fertile cells (default: mostly mature,
             with a few young ones, as in a real hymenium); ``kw`` go to ``ascus`` / ``basidium``
    Returns {"ascus" | "basidium", "paraphysis", "spore", "base": [xy of every cell base], "cells": [anchors]}.
    """
    rng = np.random.default_rng(seed)
    sp = spacing or height * (0.16 if kind == "ascus" else 0.34)
    q, nrm, L = polyline(curve, n=400)
    m = max(2, int(L / sp))
    out = dict(base=[], cells=[])
    for k in range(m):
        i = int((k + 0.5) / m * (len(q) - 1))
        p, n_ = q[i], nrm[i] * side
        ang = math.degrees(math.atan2(n_[1], n_[0]))
        if kind == "ascus":
            if paraphyses and k % 2 == 1:
                tip = paraphysis(ax, p, height * rng.uniform(0.95, 1.05), ang, zorder=zorder - 0.5)
                out.setdefault("paraphysis", tip - n_ * height * 0.3)
                continue
            st = stage or ("mature" if rng.uniform() < 0.75 else "young")
            ln = height * (rng.uniform(0.92, 1.0) if st == "mature" else rng.uniform(0.55, 0.75))
            a = ascus(ax, p, ln, ang, stage=st, zorder=zorder + (k % 3) * 0.01, **kw)
            out.setdefault("ascus", (a["base"] + a["apex"]) / 2)
            if a["spores"]:
                out.setdefault("spore", a["spores"][-2])
        else:
            st = stage or rng.choice(["mature", "mature", "sterigmata", "young"])
            ln = height * (rng.uniform(0.9, 1.0) if st != "young" else rng.uniform(0.6, 0.8))
            a = basidium(ax, p, ln * 0.62, ang, stage=st, zorder=zorder + (k % 3) * 0.01, **kw)
            out.setdefault("basidium", (a["base"] + a["apex"]) / 2)
            if a["spores"] and st == "mature":
                out.setdefault("spore", a["spores"][0])
        out["base"].append(p)
        out["cells"].append(a)
    return out


def _cav(token):
    """Fill of an empty cavity inside a fungal or plant structure of ``token``."""
    return P.mix(P.surface(), P.fill(_pt(token)), 0.5 if P.is_dark() else 0.3)


def ascocarp(ax, center, size, kind="apothecium", stalk=False, appendages="hooked", detail=True, zorder=6):
    """An ascoma (ascocarp) in median section: ``size`` is its width (apothecium) or height (others).

    kind  "apothecium" (open cup or disc with an exposed hymenium; Pezizales, lichen fruit bodies),
          "perithecium" (flask with a neck and ostiole, periphyses in the neck; Sordariomycetes),
          "cleistothecium" (closed sphere with scattered asci; Eurotiales, Erysiphales),
          "pseudothecium" (ascostroma: a locule dissolved in stromatic tissue, bitunicate asci among
          pseudoparaphyses; Dothideomycetes)
    stalk       apothecium on a stipe; ``appendages`` for cleistothecia: "hooked", "simple", "dichotomous" or None
    detail      False draws the tissues without individual asci (for small icons)
    Returns anchors: hymenium, ascus, paraphysis, excipulum / wall, ostiole, neck, periphyses, appendage,
    stroma, locule, cavity (whichever apply).
    """
    c = np.asarray(center, float)
    S = size
    out = {}
    tk = _pt("ascocarp")
    if kind == "apothecium":
        x = np.linspace(-S / 2, S / 2, 60)
        top = c[1] - 0.05 * S * (1 - (2 * x / S) ** 2)  # slightly concave disc
        t = np.linspace(0, math.pi, 50)
        depth = 0.3 * S
        bottom = np.c_[(S / 2 + 0.03 * S) * np.cos(t), c[1] - depth * np.sin(t) * 0.95 + 0.03 * S * np.cos(t) ** 2]
        bottom[:, 0] = -bottom[:, 0]
        body = np.vstack([np.c_[x[::-1], top[::-1]] + [c[0], 0], [c[0] - S / 2 - 0.03 * S, c[1] + 0.03 * S],
                          bottom + [c[0], 0]])
        if stalk:
            sw = 0.09 * S
            st = np.array([[c[0] - sw, c[1] - depth * 0.8], [c[0] - sw * 1.2, c[1] - depth - 0.35 * S],
                           [c[0] + sw * 1.2, c[1] - depth - 0.35 * S], [c[0] + sw, c[1] - depth * 0.8]])
            _poly(ax, st, tk, lw=0.9, zorder=zorder - 0.1)
            out["stipe"] = c + [0, -depth - 0.2 * S]
        _poly(ax, body, tk, lw=0.9, zorder=zorder)
        hh = 0.13 * S
        base_curve = np.c_[x * 0.97 + c[0], top - hh]
        band = np.vstack([np.c_[x * 0.97 + c[0], top], base_curve[::-1]])
        _poly(ax, band, "highlight", lw=0.0, zorder=zorder + 0.1, fill=P.light(tk), edge="none")
        out["excipulum"] = c + [0.25 * S, -0.2 * S]
        out["hymenium"] = c + [-0.2 * S, -0.06 * S]
        if detail:
            h = hymenium(ax, base_curve, hh * 0.98, kind="ascus", side=1, zorder=zorder + 1)
            out.update({k: v for k, v in h.items() if k in ("ascus", "paraphysis", "spore")})
        return out
    if kind == "perithecium":
        R = 0.3 * S
        bc = c + [0, -0.12 * S]
        nw, nt = 0.09 * S, bc[1] + 0.62 * S
        ang = np.linspace(math.radians(70), math.radians(-250), 80)
        circ = np.c_[bc[0] + R * np.cos(ang), bc[1] + R * np.sin(ang)]
        neck_l = np.array([[bc[0] - nw, bc[1] + R * 0.95], [bc[0] - nw * 0.85, nt]])
        neck_r = np.array([[bc[0] + nw * 0.85, nt], [bc[0] + nw, bc[1] + R * 0.95]])
        outline = np.vstack([neck_r, circ, neck_l])
        _poly(ax, outline, tk, lw=0.9, zorder=zorder)
        Ri, cw = R * 0.8, nw * 0.32
        angi = np.linspace(math.radians(80), math.radians(-260), 80)
        cav = np.vstack([[[bc[0] + cw, nt + 0.01 * S], [bc[0] + cw, bc[1] + Ri * 0.98]],
                         np.c_[bc[0] + Ri * np.cos(angi), bc[1] + Ri * np.sin(angi)],
                         [[bc[0] - cw, bc[1] + Ri * 0.98], [bc[0] - cw, nt + 0.01 * S]]])
        _poly(ax, cav, tk, lw=0.7, zorder=zorder + 0.1, fill=_cav("ascocarp"))
        out.update(wall=bc + [R * 0.92, -R * 0.3], neck=bc + [nw * 0.9, R * 1.4], ostiole=np.array([bc[0], nt]),
                   cavity=bc + [0, R * 0.3])
        for k in range(7):  # periphyses lining the neck canal
            y = bc[1] + Ri + (nt - bc[1] - Ri) * (k + 0.5) / 7
            for sg in (-1, 1):
                ax.plot([bc[0] + sg * cw, bc[0] + sg * cw * 0.35], [y, y + 0.015 * S], color=P.edge(_pt("paraphysis")),
                        lw=0.6, zorder=zorder + 0.2)
        out["periphyses"] = np.array([bc[0] + cw * 0.6, bc[1] + Ri + 0.05 * S])
        if detail:
            aim = bc + [0, R * 0.35]
            for k, a in enumerate(np.linspace(math.radians(205), math.radians(335), 9)):
                p = bc + Ri * 0.97 * np.array([math.cos(a), math.sin(a)])
                d = aim - p
                ln = np.hypot(*d) * 0.95
                ang_ = math.degrees(math.atan2(d[1], d[0]))
                if k % 2:
                    paraphysis(ax, p, ln * 0.9, ang_, zorder=zorder + 0.5)
                else:
                    a_ = ascus(ax, p, ln, ang_, zorder=zorder + 1)
                    out.setdefault("ascus", (a_["base"] + a_["apex"]) / 2)
                    out.setdefault("spore", a_["spores"][-3])
        return out
    if kind == "cleistothecium":
        R = 0.32 * S
        wall = "peridium"
        if appendages:
            rng = np.random.default_rng(5)
            for k in range(10):
                a = 2 * math.pi * (k + 0.3) / 10 + rng.uniform(-0.1, 0.1)
                u = np.array([math.cos(a), math.sin(a)])
                p0, L = c + u * R * 0.95, R * 1.1
                nn = np.array([-u[1], u[0]])
                if appendages == "hooked":
                    pts = [p0 + u * L * t for t in np.linspace(0, 1, 10)]
                    th = np.linspace(0, 1.4 * math.pi, 14)
                    rr = L * 0.09
                    end = pts[-1]
                    pts += [end + nn * rr - nn * rr * np.cos(x) + u * rr * np.sin(x) for x in th]
                    pts = np.array(pts)
                elif appendages == "dichotomous":
                    pts = np.array([p0 + u * L * 0.7 * t for t in np.linspace(0, 1, 6)])
                    for sg in (-1, 1):
                        v = u * math.cos(0.5) + sg * nn * math.sin(0.5)
                        br = np.array([pts[-1] + v * L * 0.35 * t for t in np.linspace(0, 1, 5)])
                        ax.plot(*br.T, color=P.edge(_pt(wall)), lw=0.8, zorder=zorder - 0.2, solid_capstyle="round")
                else:
                    pts = np.array([p0 + u * L * t + nn * 0.08 * L * math.sin(3 * t) for t in np.linspace(0, 1, 10)])
                ax.plot(*np.asarray(pts).T, color=P.edge(_pt(wall)), lw=0.9, zorder=zorder - 0.2, solid_capstyle="round")
                if k == 1:
                    out["appendage"] = np.asarray(pts)[len(pts) // 2]
        ax.add_patch(Circle(c, R, facecolor=P.fill(_pt(wall)), edgecolor=P.edge(_pt(wall)), lw=0.9, zorder=zorder))
        ax.add_patch(Circle(c, R * 0.84, facecolor=_cav("ascocarp"), edgecolor=P.edge(_pt(wall)), lw=0.6, zorder=zorder + 0.1))
        out.update(peridium=c + [R * 0.92, R * 0.3], cavity=c)
        if detail:
            spots = [(-0.35, 0.3, 30), (0.3, 0.32, -40), (0.0, -0.05, 90), (-0.38, -0.38, 140), (0.36, -0.35, 50)]
            for k, (dx, dy, a) in enumerate(spots):
                p = c + np.array([dx, dy]) * R
                ax.add_patch(Ellipse(p, R * 0.5, R * 0.4, angle=a, facecolor=P.fill(_pt("ascus")), edgecolor=P.edge(_pt("ascus")),
                                     lw=0.6, zorder=zorder + 0.3))
                for j in range(8):
                    t_ = 2 * math.pi * j / 8
                    rr = R * (0.12 if j % 2 else 0.07)
                    q = p + rr * np.array([math.cos(t_), math.sin(t_)])
                    ax.add_patch(Circle(q, R * 0.045, facecolor=P.fill(_pt("ascospore")), edgecolor=P.edge(_pt("ascospore")),
                                        lw=0.3, zorder=zorder + 0.4))
                if k == 1:
                    out["ascus"] = p + [R * 0.18, 0]
                    out["spore"] = p
        return out
    if kind == "pseudothecium":
        w, h = 0.95 * S, 0.62 * S
        st = smooth_closed([c + [-w / 2, -h / 2], c + [w / 2, -h / 2], c + [w / 2 * 1.02, h / 3], c + [0.1 * w, h / 2],
                            c + [-0.1 * w, h / 2], c + [-w / 2 * 1.02, h / 3]], n=200)
        _poly(ax, st, _pt("stroma"), lw=0.9, zorder=zorder)
        lc = c + [0, -0.05 * S]
        loc = np.c_[lc[0] + 0.3 * S * np.cos(np.linspace(0, 2 * math.pi, 80)), lc[1] + 0.2 * S * np.sin(np.linspace(0, 2 * math.pi, 80))]
        _poly(ax, loc, _pt("stroma"), lw=0.6, zorder=zorder + 0.1, fill=_cav("stroma"))
        ax.add_patch(PathPatch(Path(np.array([[lc[0] - 0.03 * S, lc[1] + 0.18 * S], [lc[0] - 0.025 * S, c[1] + h / 2],
                                              [lc[0] + 0.025 * S, c[1] + h / 2], [lc[0] + 0.03 * S, lc[1] + 0.18 * S]])),
                               facecolor=_cav("stroma"), edgecolor=P.edge(_pt("stroma")), lw=0.6, zorder=zorder + 0.12))
        out.update(stroma=c + [0.38 * w, -0.2 * h], locule=lc + [0.22 * S, 0.08 * S], ostiole=np.array([lc[0], c[1] + h / 2]))
        if detail:
            for k, x in enumerate(np.linspace(-0.22, 0.22, 7)):
                p = lc + [x * S, -0.19 * S * math.sqrt(max(0.0, 1 - (x / 0.3) ** 2))]
                if k % 2:
                    ax.plot([p[0], p[0] + x * 0.1 * S], [p[1], lc[1] + 0.17 * S], color=P.edge(_pt("paraphysis")), lw=0.7,
                            zorder=zorder + 0.3)
                    out.setdefault("pseudoparaphysis", np.array([p[0], lc[1] + 0.05 * S]))
                else:
                    a_ = ascus(ax, p, 0.27 * S, 90 - x * 60, bitunicate=True, arrangement="biseriate", zorder=zorder + 0.5)
                    out.setdefault("ascus", (a_["base"] + a_["apex"]) / 2)
        return out
    raise ValueError(f"unknown ascocarp {kind!r}")


def mushroom(ax, base, height, section=True, annulus=True, volva=False, mycelium=True, zorder=6):
    """An agaric basidiocarp (mushroom) standing on ``base``, ``height`` tall: pileus (cap) with its
    context (flesh) and lamellae (gills), stipe, optional annulus (ring, remnant of the partial veil) and
    volva (cup, remnant of the universal veil, as in *Amanita*), and mycelial strands below.

    section  True: median longitudinal section (cuticle, flesh and the profile of a lamella); False:
             side view (gill edges seen under the cap)
    Returns anchors: pileus, cuticle, context, lamella, gill_edge, stipe, annulus, volva, mycelium.
    """
    b = np.asarray(base, float)
    H = height
    W = 0.44 * H
    ym = 0.66 * H  # cap margin height
    out = {}
    t = np.linspace(0, math.pi, 80)
    dome = np.c_[W * np.cos(t), ym + (H - ym) * np.sin(t) ** 0.75 + 0.03 * H * np.sin(t)]
    under_flesh = np.array([[-W * 0.96, ym - 0.005 * H], [-0.06 * H, ym + 0.08 * H], [0.06 * H, ym + 0.08 * H],
                            [W * 0.96, ym - 0.005 * H]])
    sw0, sw1 = 0.05 * H, 0.068 * H
    bulb = 0.1 * H if volva else sw1
    stipe = np.array([[-sw0, ym + 0.06 * H], [-sw0 * 1.05, 0.4 * H], [-sw1, 0.12 * H], [-bulb, 0.04 * H], [-bulb * 0.7, 0],
                      [bulb * 0.7, 0], [bulb, 0.04 * H], [sw1, 0.12 * H], [sw0 * 1.05, 0.4 * H], [sw0, ym + 0.06 * H]])
    if mycelium:
        rng = np.random.default_rng(2)
        for k in range(6):
            x0 = (k - 2.5) / 2.5 * bulb * 0.7
            pts = np.c_[np.linspace(x0, x0 + (k - 2.5) * 0.06 * H, 12), np.linspace(0, -0.12 * H - 0.03 * H * (k % 2), 12)]
            pts[:, 0] += 0.01 * H * np.sin(np.linspace(0, 6, 12) + rng.uniform(0, 3))
            ax.plot(*(pts + b).T, color=P.edge(_pt("hypha")), lw=0.8, zorder=zorder - 0.5, solid_capstyle="round")
        out["mycelium"] = b + [0.12 * H, -0.08 * H]
    _poly(ax, smooth_closed(stipe + b, n=160), _pt("stipe"), lw=0.9, zorder=zorder)
    out["stipe"] = b + [sw0 * 0.9, 0.35 * H]
    # gills: the lamella profile (section) or the gill edges under the cap (side view)
    gill_edge = []
    for sg in (-1, 1):
        xs = np.linspace(0.06 * H, W * 0.95, 30)
        f_ = (xs - 0.06 * H) / (W * 0.95 - 0.06 * H)
        y_top = ym + 0.08 * H - 0.085 * H * f_
        y_edge = y_top - 0.1 * H * np.sin(np.pi * f_ ** 0.8) - 0.01 * H
        gill = np.vstack([np.c_[sg * xs, y_top], np.c_[sg * xs[::-1], y_edge[::-1]]]) + b
        _poly(ax, gill, _pt("lamella"), lw=0.8, zorder=zorder + 0.5)
        gill_edge.append(np.c_[sg * xs, y_edge] + b)
        if not section:
            for x in np.linspace(0.08 * H, W * 0.9, 9):
                fx = (x - 0.06 * H) / (W * 0.95 - 0.06 * H)
                yt = ym + 0.08 * H - 0.085 * H * fx
                ye = yt - 0.1 * H * math.sin(math.pi * fx ** 0.8) - 0.01 * H
                ax.plot([b[0] + sg * x, b[0] + sg * x * 1.01], [b[1] + yt, b[1] + ye], color=P.edge(_pt("lamella")), lw=0.5,
                        zorder=zorder + 0.6)
    out["lamella"] = gill_edge[1][14] + [0, 0.04 * H]
    out["gill_edge"] = gill_edge[1][12]
    cap = np.vstack([dome, under_flesh]) + b
    _poly(ax, cap, _pt("pileus"), lw=0.9, zorder=zorder + 1)
    out["pileus"] = b + [W * 0.55, ym + (H - ym) * 0.85]
    if section:
        inner = np.vstack([np.c_[dome[:, 0] * 0.93, ym + (dome[:, 1] - ym) * 0.86 + 0.005 * H], under_flesh]) + b
        _poly(ax, inner, _pt("context"), lw=0.6, zorder=zorder + 1.1)
        st_in = np.array([[-sw0 * 0.8, ym + 0.1 * H], [-sw0 * 0.85, 0.4 * H], [-sw1 * 0.8, 0.12 * H], [-bulb * 0.8, 0.04 * H],
                          [-bulb * 0.55, 0.012 * H], [bulb * 0.55, 0.012 * H], [bulb * 0.8, 0.04 * H], [sw1 * 0.8, 0.12 * H],
                          [sw0 * 0.85, 0.4 * H], [sw0 * 0.8, ym + 0.1 * H]])
        _poly(ax, smooth_closed(st_in + b, n=160), _pt("context"), lw=0.0, zorder=zorder + 1.05, edge="none")
        out["context"] = b + [-W * 0.3, ym + 0.15 * H]
        out["cuticle"] = b + [-W * 0.62, ym + (H - ym) * 0.8]
    if annulus:
        ya = ym - 0.07 * H
        for sg in (-1, 1):
            ring = np.array([[sg * sw0 * 0.95, ya + 0.025 * H], [sg * (sw0 + 0.03 * H), ya + 0.005 * H],
                             [sg * (sw0 + 0.05 * H), ya - 0.05 * H], [sg * (sw0 + 0.025 * H), ya - 0.04 * H],
                             [sg * sw0 * 1.0, ya - 0.01 * H]]) + b
            _poly(ax, ring, _pt("annulus"), lw=0.7, zorder=zorder + 0.8)
        out["annulus"] = b + [sw0 + 0.05 * H, ya - 0.03 * H]
    if volva:
        # a membranous cup with a torn rim around the stipe base
        cup = np.array([[-bulb * 1.3, 0.14 * H], [-bulb * 1.08, 0.1 * H], [-bulb * 1.12, 0.03 * H], [-bulb * 0.8, -0.01 * H],
                        [bulb * 0.8, -0.01 * H], [bulb * 1.12, 0.03 * H], [bulb * 1.08, 0.1 * H], [bulb * 1.3, 0.14 * H],
                        [bulb * 1.32, 0.06 * H], [bulb * 1.0, -0.03 * H], [-bulb * 1.0, -0.03 * H], [-bulb * 1.32, 0.06 * H]]) + b
        _poly(ax, cup, _pt("volva"), lw=0.7, zorder=zorder + 0.8)
        out["volva"] = b + [bulb * 1.2, 0.05 * H]
    return out


def gill_section(ax, box, gills=3, kind="basidium", seed=0, zorder=6):
    """Lamellae (gills) of an agaric in transverse section, hanging from the cap context: each gill has a
    central trama of parallel hyphae, a subhymenium, and a hymenium of basidia (``kind="basidium"``) or
    asci on both faces. ``box`` = (x0, y0, x1, y1). Returns anchors: context, trama, subhymenium,
    hymenium, basidium, spore."""
    x0, y0, x1, y1 = box
    W, Hh = x1 - x0, y1 - y0
    out = {}
    ctop = y1 - 0.18 * Hh
    ax.add_patch(PathPatch(Path(np.array([[x0, ctop], [x1, ctop], [x1, y1], [x0, y1]])), facecolor=P.fill(_pt("context")),
                           edgecolor=P.edge(_pt("context")), lw=0.8, zorder=zorder))
    out["context"] = np.array([x0 + 0.1 * W, (ctop + y1) / 2])
    pitch = W / gills
    gw = pitch * 0.3
    for g in range(gills):
        cx = x0 + pitch * (g + 0.5)
        bottom = y0 + 0.05 * Hh
        sh = np.array([[cx - gw / 2, ctop + 0.01 * Hh], [cx - gw / 2 * 0.95, bottom + gw * 0.5], [cx, bottom],
                       [cx + gw / 2 * 0.95, bottom + gw * 0.5], [cx + gw / 2, ctop + 0.01 * Hh]])
        _poly(ax, smooth_closed(sh, n=80)[:], _pt("lamella"), lw=0.7, zorder=zorder + 0.2)
        for j in (-1, 0, 1):  # trama hyphae
            xs = cx + j * gw * 0.14
            ax.plot([xs, xs], [ctop, bottom + gw * 0.5], color=P.edge(_pt("hypha")), lw=0.6, zorder=zorder + 0.3)
        hh = min(pitch * 0.26, Hh * 0.2)
        for sg in (-1, 1):
            xb = cx + sg * gw / 2 * 0.97
            curve = np.c_[np.full(20, xb), np.linspace(ctop - 0.02 * Hh, bottom + gw * 0.7, 20)]
            h = hymenium(ax, curve, hh, kind=kind, side=sg, seed=seed + g * 2 + (sg > 0),
                         spacing=hh * 0.2, zorder=zorder + 0.5)
            if g == gills - 1 and sg == 1:
                out.update({k: v for k, v in h.items() if k in ("basidium", "spore", "ascus", "paraphysis")})
        if g == 0:
            out["trama"] = np.array([cx, (ctop + bottom) / 2])
            out["subhymenium"] = np.array([cx + gw * 0.42, (ctop + bottom) / 2 - 0.1 * Hh])
            out["hymenium"] = np.array([cx - gw * 0.6, (ctop + bottom) / 2 + 0.05 * Hh])
    return out


# ------------------------------------------------------------- fern sori and sporangia

SORI = ("round", "linear", "costal", "marginal", "terminal", "acrostichoid")
INDUSIA = (None, "peltate", "reniform", "linear", "false", "cup")


def _sporangia_disc(ax, c, R, r, token, zorder):
    n = max(3, int(0.8 * (R / r) ** 2))
    pts = []
    for k in range(n):
        rr = max(0.0, R - r) * math.sqrt((k + 0.5) / n)
        a = k * 2.39996
        pts.append(np.asarray(c) + rr * np.array([math.cos(a), math.sin(a)]))
    for p in pts:
        ax.add_patch(Circle(p, r, facecolor=P.fill(_pt(token)), edgecolor=P.edge(_pt(token)), lw=0.45, zorder=zorder))
    return pts


def _sporangia_strip(ax, a, b, w, r, token, zorder):
    a, b = np.asarray(a, float), np.asarray(b, float)
    L = np.hypot(*(b - a))
    u = (b - a) / (L or 1)
    nrm = np.array([-u[1], u[0]])
    rows = max(1, int(round(w / (2.1 * r))))
    pts = []
    for j in range(rows):
        off = (j - (rows - 1) / 2) * 2.0 * r
        m = max(1, int(L / (2.05 * r)))
        for k in range(m):
            pts.append(a + u * (L * (k + 0.5) / m + (r if j % 2 else 0) * 0.5) + nrm * off)
    for p in pts:
        ax.add_patch(Circle(p, r, facecolor=P.fill(_pt(token)), edgecolor=P.edge(_pt(token)), lw=0.45, zorder=zorder))
    return pts


def pinnule(ax, base, length, angle=90.0, width=None, sorus="round", indusium=None, token="plant", zorder=6):
    """A fern pinnule (ultimate leaf segment) seen from below (abaxial side) with its sori.

    sorus     "round" (on the veins, between costa and margin: *Dryopteris*, *Polypodium*), "linear"
              (along the veinlets: *Asplenium*), "costal" (continuous, parallel to the costa: *Blechnum*),
              "marginal" (continuous along the margin: *Pteris*), "terminal" (at vein ends at the margin:
              *Adiantum*, *Dennstaedtia*), "acrostichoid" (sporangia over the whole lamina: *Acrostichum*)
              or None (sterile)
    indusium  None (exindusiate), "peltate" (umbrella-like, attached at the centre: *Polystichum*),
              "reniform" (kidney-shaped, attached at the sinus: *Dryopteris*), "linear" (a flap along one
              side of a linear sorus: *Asplenium*, *Blechnum*), "false" (the reflexed leaf margin: *Pteris*,
              *Adiantum*), "cup" (a cup at the vein end: *Dennstaedtia*)
    Returns anchors: costa, vein, margin, sorus, sporangium, indusium, sori (list).
    """
    L = length
    W = width or 0.42 * L
    f = _loc(base, angle)
    s = np.linspace(0, 1, 120)
    hw = W / 2 * np.clip(s / 0.08, 0, 1) ** 0.5
    m = s > 0.62
    hw[m] = W / 2 * np.sqrt(np.clip(1 - ((s[m] - 0.62) / 0.38) ** 2, 0, 1)) ** 0.9
    outline = np.vstack([np.c_[s * L, hw], np.c_[s[::-1] * L, -hw[::-1]]])

    def hw_at(x):
        return float(np.interp(x / L, s, hw))
    blade = _poly(ax, f(outline), token, lw=0.9, zorder=zorder)
    n_before = len(ax.patches)
    ec = P.edge(token)
    ax.plot(*f(np.c_[s[:-6] * L, s[:-6] * 0]).T, color=ec, lw=1.2, zorder=zorder + 0.2, solid_capstyle="round")
    out = dict(costa=f([0.3 * L, 0])[0], margin=f([0.5 * L, hw_at(0.5 * L)])[0], sori=[])
    nv = 6
    veins = []
    for k in range(nv):
        x0 = L * (0.12 + 0.72 * k / (nv - 1))
        for sg in (1, -1):
            x1 = x0 + 0.5 * hw_at(x0)
            y1 = sg * hw_at(x1) * 0.94
            fork = np.array([x0 + 0.22 * hw_at(x0), sg * 0.4 * abs(y1)])
            v = np.array([[x0, 0], fork, [x1, y1]])
            v2 = np.array([fork, [x1 + 0.2 * hw_at(x0), sg * hw_at(x1 + 0.2 * hw_at(x0)) * 0.94]])
            for vv in (v, v2):
                ax.plot(*f(vv).T, color=ec, lw=0.55, zorder=zorder + 0.1, solid_capstyle="round")
            veins.append((v, v2, sg))
    out["vein"] = f((veins[2][0][1] + veins[2][0][2]) / 2)[0]
    sp_tok = "sporangium"
    r = 0.022 * L
    ind_fc, ind_ec = P.fill(_pt("indusium")), P.edge(_pt("indusium"))
    z = zorder + 1

    def ind_patch(pts, z_=None):
        _poly(ax, f(pts), _pt("indusium"), lw=0.6, zorder=z_ or z + 0.5)
    if sorus == "round":
        R = 0.06 * L
        for k, (v, v2, sg) in enumerate(veins):
            if k < 2 or k >= len(veins) - 2:
                continue
            c = v[0] + (v[2] - v[0]) * 0.5
            cw = f(c)[0]
            pts = _sporangia_disc(ax, cw, R, r, sp_tok, z)
            out["sori"].append(cw)
            out.setdefault("sporangium", pts[-1])
            if indusium == "peltate":
                ax.add_patch(Circle(cw, R * 0.78, facecolor=ind_fc, edgecolor=ind_ec, lw=0.6, zorder=z + 0.5))
                ax.add_patch(Circle(cw, R * 0.14, facecolor=ind_ec, edgecolor="none", zorder=z + 0.6))
            elif indusium == "reniform":
                toward = math.atan2(-sg, 0)  # sinus faces the costa
                th = np.linspace(0, 2 * math.pi, 80)
                rr = R * 0.85 * (1 - 0.55 * np.exp(-((((th - toward + math.pi) % (2 * math.pi)) - math.pi) / 0.45) ** 2))
                pts_ = c + np.c_[rr * np.cos(th), rr * np.sin(th)]
                ind_patch(pts_)
                att = c + 0.4 * R * np.array([math.cos(toward), math.sin(toward)])
                ax.add_patch(Circle(f(att)[0], R * 0.1, facecolor=ind_ec, edgecolor="none", zorder=z + 0.6))
        if out["sori"]:
            out["sorus"] = out["sori"][len(out["sori"]) // 2]
            if indusium:
                out["indusium"] = out["sori"][1] + (f([[0.0, 0.03 * L]])[0] - f([[0.0, 0.0]])[0])
    elif sorus == "linear":
        for k, (v, v2, sg) in enumerate(veins):
            if k < 2 or k >= len(veins) - 1:
                continue
            a_, b_ = v[0] + (v[2] - v[0]) * 0.18, v[0] + (v[2] - v[0]) * 0.8
            w = 0.045 * L
            pts = _sporangia_strip(ax, f(a_)[0], f(b_)[0], w, r, sp_tok, z)
            out["sori"].append(f((a_ + b_) / 2)[0])
            out.setdefault("sporangium", pts[0])
            if indusium == "linear":
                u = (b_ - a_) / np.hypot(*(b_ - a_))
                nn = np.array([-u[1], u[0]]) * sg
                flap = np.array([a_ + nn * w * 0.15, b_ + nn * w * 0.15, b_ - nn * w * 0.35, a_ - nn * w * 0.35])
                ind_patch(flap)
                out.setdefault("indusium", f((a_ + b_) / 2 - nn * w * 0.1)[0])
        out["sorus"] = out["sori"][len(out["sori"]) // 2] if out["sori"] else None
    elif sorus == "costal":
        for sg in (1, -1):
            a_, b_ = np.array([0.1 * L, sg * 0.1 * W]), np.array([0.78 * L, sg * 0.1 * W])
            w = 0.12 * W
            pts = _sporangia_strip(ax, f(a_)[0], f(b_)[0], w, r, sp_tok, z)
            out["sori"].append(f((a_ + b_) / 2)[0])
            out.setdefault("sporangium", pts[0])
            if indusium:
                flap = np.array([a_ + [0, sg * w * 0.9], b_ + [0, sg * w * 0.9], b_ + [0, sg * w * 0.05], a_ + [0, sg * w * 0.05]])
                ind_patch(flap)
                out.setdefault("indusium", f((a_ + b_) / 2 + [0, sg * w * 0.5])[0])
        out["sorus"] = out["sori"][0]
    elif sorus in ("marginal", "terminal"):
        band = 0.12 * W
        xs = np.linspace(0.1 * L, 0.93 * L, 40)
        for sg in (1, -1):
            edge_pts = np.c_[xs, [sg * max(0.0, hw_at(x) - band * 0.55) for x in xs]]
            if sorus == "marginal":
                pts = []
                for p0, p1 in zip(edge_pts[:-1:3], edge_pts[3::3]):
                    pts += _sporangia_strip(ax, f(p0)[0], f(p1)[0], band * 0.8, r, sp_tok, z)
                out.setdefault("sporangium", pts[len(pts) // 3])
                out["sori"].append(f(edge_pts[20])[0])
            else:
                for v, v2, sg2 in veins:
                    if sg2 != sg:
                        continue
                    end = v2[-1]
                    c = end * [1, 0.86]
                    pts = _sporangia_disc(ax, f(c)[0], 0.045 * L, r * 0.9, sp_tok, z)
                    out["sori"].append(f(c)[0])
                    out.setdefault("sporangium", pts[0])
                    if indusium == "cup":
                        th = np.linspace(0, math.pi, 30)
                        cup = c + np.c_[0.055 * L * np.cos(th), -sg * 0.055 * L * np.sin(th) * 0.9]
                        cup = np.vstack([cup, cup[::-1] * [1, 1] + [0, sg * 0.012 * L]])
                        ind_patch(cup, z - 0.2)
                        out.setdefault("indusium", f(c - [0, sg * 0.045 * L])[0])
            if indusium == "false":
                outer = np.c_[xs, [sg * hw_at(x) * 1.0 for x in xs]]
                inner = np.c_[xs, [sg * max(0.0, hw_at(x) - band * 0.62) for x in xs]]
                if sorus == "terminal":  # separate reflexed flaps over each sorus
                    for v, v2, sg2 in veins:
                        if sg2 != sg:
                            continue
                        x_ = v2[-1][0]
                        sel = (xs > x_ - 0.06 * L) & (xs < x_ + 0.06 * L)
                        if sel.sum() > 2:
                            ind_patch(np.vstack([outer[sel], inner[sel][::-1]]), z + 0.5)
                else:
                    ind_patch(np.vstack([outer, inner[::-1]]), z + 0.5)
                out.setdefault("indusium", f(np.array([0.55 * L, sg * (hw_at(0.55 * L) - band * 0.5)]))[0])
        out["sorus"] = out["sori"][len(out["sori"]) // 2] if out["sori"] else None
    elif sorus == "acrostichoid":
        rng = np.random.default_rng(1)
        pts = []
        for x in np.arange(0.08 * L, 0.97 * L, 1.9 * r):
            h_ = hw_at(x) - 1.2 * r
            for y in np.arange(-h_, h_ + 1e-9, 1.9 * r):
                pts.append(f([x + rng.uniform(-0.3, 0.3) * r, y])[0])
        for p in pts:
            ax.add_patch(Circle(p, r, facecolor=P.fill(_pt(sp_tok)), edgecolor=P.edge(_pt(sp_tok)), lw=0.4, zorder=z))
        out["sporangium"] = pts[len(pts) // 2]
        out["sorus"] = pts[len(pts) // 3]
    elif sorus is not None:
        raise ValueError(f"unknown sorus {sorus!r}")
    for patch in ax.patches[n_before:]:  # sori and indusia stay on the lamina
        patch.set_clip_path(blade)
    return out


def leptosporangium(ax, center, size, stage="closed", annulus=13, spores=True, token="sporangium", zorder=6):
    """A leptosporangium (polypod fern) in side view: stalk, lens-shaped capsule, the vertical annulus of
    ``annulus`` cells with thickened inner and radial walls running over the top, and the stomium (thin-walled
    lip cells) on the side where the capsule opens.

    stage  "closed"; "open" (the annulus has dried and bent back, tearing the capsule open at the
           stomium; the spores lie exposed in the cup); "ejected" (the annulus has snapped back after
           cavitation, throwing the spores out)
    Returns anchors: capsule, annulus, stomium, stalk, spores (list), lip.
    """
    c = np.asarray(center, float)
    S = size
    rx, ry = 0.42 * S, 0.36 * S
    tk = _pt(token)
    fc, ec = P.fill(tk), P.edge(tk)
    out = dict(spores=[])
    # stalk (three rows of cells)
    sb, st = c + [0, -ry * 0.9], c + [0, -ry - 0.6 * S]
    w = 0.06 * S
    _poly(ax, [sb + [-w, 0], st + [-w * 0.8, 0], st + [w * 0.8, 0], sb + [w, 0]], tk, lw=0.7, zorder=zorder - 0.2,
          fill=P.light(tk))
    for k in range(1, 5):
        y = sb[1] + (st[1] - sb[1]) * k / 5
        ax.plot([c[0] - w * 0.85, c[0] + w * 0.85], [y, y], color=ec, lw=0.5, zorder=zorder - 0.1)
    out["stalk"] = c + [w, -ry - 0.3 * S]
    a0, a1 = math.radians(-58), math.radians(205)  # annulus from beside the stalk over the top
    s0, s1 = math.radians(212), math.radians(250)  # stomium

    def ell(a, k=1.0):
        return c + np.array([rx * k * math.cos(a), ry * k * math.sin(a)])
    band = 0.14 * S
    if stage == "closed" or stage == "ejected":
        th = np.linspace(0, 2 * math.pi, 100)
        cap = np.c_[c[0] + rx * np.cos(th), c[1] + ry * np.sin(th)]
        _poly(ax, cap, tk, lw=0.8, zorder=zorder, fill=P.light(tk))
        # annulus cells (closed: on the capsule rim; ejected: same place, the capsule empty and torn)
        angs = np.linspace(a0, a1, annulus + 1)
        center_line = None
    else:
        # open: the annulus straightens and curls backwards from its base beside the stalk
        n = 60
        base = ell(a0)
        length = (a1 - a0) * (rx + ry) / 2
        length *= 0.9
        kappa = -2.5 / length  # it rises beside the stalk and bends back, away from the stomium
        pts, phi = [base], math.radians(100)
        for i in range(n):
            phi += kappa * length / n
            pts.append(pts[-1] + length / n * np.array([math.cos(phi), math.sin(phi)]))
        center_line = np.array(pts)
        # the remaining cup of the capsule (from the stomium round the bottom to the annulus base)
        th = np.linspace(math.radians(165), a0 + 2 * math.pi, 50)
        cup = np.c_[c[0] + rx * np.cos(th), c[1] + ry * np.sin(th)]
        _poly(ax, cup, tk, lw=0.8, zorder=zorder, fill=P.light(tk))
        angs = None
    cells = []
    if angs is not None:
        for i in range(annulus):
            q = [ell(angs[i], 1.0), ell(angs[i + 1], 1.0), ell(angs[i + 1], 1 + band / ry), ell(angs[i], 1 + band / ry)]
            cells.append(q)
    else:
        q_, nrm_, _ = polyline(center_line, n=annulus * 8 + 1)
        # outward side is to the right of the curve's direction for the closed case: inner wall = left
        for i in range(annulus):
            j0, j1 = i * 8, (i + 1) * 8
            p0, p1 = q_[j0], q_[j1]
            n0, n1 = nrm_[j0], nrm_[j1]
            cells.append([p0, p1, p1 - n1 * band, p0 - n0 * band])
        # torn capsule wall carried on the inner face of the annulus
        wall = np.vstack([q_, (q_ + nrm_ * 0.08 * S)[::-1]])
        _poly(ax, wall, tk, lw=0.5, zorder=zorder - 0.05, fill=P.light(tk))
    for i, q in enumerate(cells):
        _poly(ax, q, tk, lw=0.5, zorder=zorder + 0.5)
        ax.plot(*np.array([q[0], q[3]]).T, color=ec, lw=1.6, zorder=zorder + 0.6, solid_capstyle="butt")  # radial wall
        ax.plot(*np.array([q[0], q[1]]).T, color=ec, lw=1.8, zorder=zorder + 0.6, solid_capstyle="butt")  # inner wall
    ax.plot(*np.array([cells[-1][1], cells[-1][2]]).T, color=ec, lw=1.6, zorder=zorder + 0.6, solid_capstyle="butt")
    mid = cells[annulus // 2]
    out["annulus"] = (mid[2] + mid[3]) / 2
    # stomium lip cells
    if stage != "open":
        for a in (s0 + 0.12, s1 - 0.12):
            p = ell(a, 1.0)
            ax.add_patch(Ellipse(p, 0.13 * S, 0.08 * S, angle=math.degrees(a) + 90, facecolor=fc, edgecolor=ec, lw=0.6,
                                 zorder=zorder + 0.4))
        out["stomium"] = ell((s0 + s1) / 2, 1.05)
    else:
        out["stomium"] = ell(s1, 1.0)
    out["lip"] = out["stomium"]
    out["capsule"] = c + [rx * 0.2, -ry * 0.35]
    if spores:
        rng = np.random.default_rng(4)
        if stage == "closed":
            pts = [c + rng.uniform(-1, 1, 2) * [rx * 0.6, ry * 0.55] for _ in range(14)]
        elif stage == "open":
            pts = [c + [rng.uniform(-0.6, 0.6) * rx, rng.uniform(-0.7, -0.05) * ry] for _ in range(12)]
        else:
            pts = [c + [-rx * 1.3 - rng.uniform(0, 1.6) * S, rng.uniform(-0.2, 1.0) * S] for _ in range(14)]
        for p in pts:
            ax.add_patch(Ellipse(p, 0.1 * S, 0.07 * S, angle=rng.uniform(0, 180), facecolor=P.fill(_pt("spore")),
                                 edgecolor=P.edge(_pt("spore")), lw=0.4, zorder=zorder + 0.3))
        out["spores"] = pts
    return out


# ------------------------------------------------------------- cones and strobili


def _pollen_grain(ax, p, r, zorder):
    """A bisaccate (winged) pine pollen grain: the body and two air sacs."""
    for sg in (-1, 1):
        ax.add_patch(Circle(np.asarray(p) + [sg * r * 0.8, -r * 0.2], r * 0.65, facecolor=P.light(_pt("pollen_sac")),
                            edgecolor=P.edge(_pt("pollen_sac")), lw=0.35, zorder=zorder))
    ax.add_patch(Ellipse(p, r * 1.5, r * 1.1, facecolor=P.fill(_pt("pollen_sac")), edgecolor=P.edge(_pt("pollen_sac")),
                         lw=0.4, zorder=zorder + 0.01))


def cone_scale(ax, base, size, kind="ovulate", view="adaxial", angle=90.0, seeds=False, bract=0.5, flip=False, zorder=6):
    """One cone scale of a conifer, from its attachment on the cone axis (``base``) along ``angle``.

    kind  "ovulate" (= "seed": the bract–scale complex: a bract with the ovuliferous scale in its axil,
          two inverted ovules on the scale's upper face, micropyles towards the axis) or "pollen" (a
          microsporophyll with two pollen sacs, microsporangia, on its lower face)
    view  "adaxial" (seen from the cone axis side) or "section" (radial longitudinal section; the adaxial
          side is to the left of ``angle``); "abaxial" for pollen scales shows the pollen sacs
    seeds True: winged seeds instead of ovules (adaxial view of a mature seed scale)
    bract length of the bract scale (fraction of ``size``; long and exserted in *Pseudotsuga*)
    flip  mirror image (the adaxial side to the right of ``angle``), for scales on the left of an axis
    Returns anchors: scale, bract, ovule (or seed, wing), micropyle, pollen_sac, apophysis, umbo, ovules.
    """
    S = size
    f = _loc(base, angle, flip)
    out = {}
    if kind in ("ovulate", "seed"):
        if view == "section":
            br = np.array([[0, -0.02 * S], [bract * S * 0.9, -0.05 * S], [bract * S, -0.07 * S], [bract * S * 0.85, -0.085 * S],
                           [0.05 * S, -0.07 * S]])
            _poly(ax, f(br), _pt("bract_scale"), lw=0.7, zorder=zorder)
            out["bract"] = f([bract * S * 0.6, -0.065 * S])[0]
            sc = np.array([[0, 0], [0.75 * S, 0.02 * S], [0.97 * S, 0.06 * S], [1.0 * S, 0.0], [0.92 * S, -0.06 * S],
                           [0.7 * S, -0.045 * S], [0.04 * S, -0.03 * S]])
            _poly(ax, f(smooth_closed(sc, n=120)), _pt("ovuliferous_scale"), lw=0.8, zorder=zorder + 0.1)
            out["scale"] = f([0.55 * S, -0.01 * S])[0]
            out["apophysis"] = f([0.93 * S, 0.0])[0]
            # ovule on the upper face, micropyle pointing to the axis
            oc = np.array([0.2 * S, 0.075 * S])
            ov = np.c_[oc[0] + 0.12 * S * np.cos(np.linspace(0, 2 * math.pi, 50)),
                       oc[1] + 0.055 * S * np.sin(np.linspace(0, 2 * math.pi, 50))]
            _poly(ax, f(ov), _pt("ovule"), lw=0.7, zorder=zorder + 0.3)
            nu = np.c_[oc[0] + 0.022 * S + 0.08 * S * np.cos(np.linspace(0, 2 * math.pi, 40)),
                       oc[1] + 0.035 * S * np.sin(np.linspace(0, 2 * math.pi, 40))]
            _poly(ax, f(nu), _pt("megagametophyte"), lw=0.5, zorder=zorder + 0.4)
            for sg in (-1, 1):  # micropylar arms
                ax.plot(*f([[oc[0] - 0.11 * S, oc[1] + sg * 0.02 * S], [oc[0] - 0.15 * S, oc[1] + sg * 0.035 * S]]).T,
                        color=P.edge(_pt("ovule")), lw=0.8, zorder=zorder + 0.4)
            out["ovule"] = f(oc + [0.06 * S, 0.03 * S])[0]
            out["megagametophyte"] = f(oc + [0.03 * S, 0])[0]
            out["micropyle"] = f(oc - [0.13 * S, 0])[0]
            out["ovules"] = [out["ovule"]]
            return out
        # adaxial view
        if bract:
            br = np.array([[0, -0.08 * S], [0.6 * bract * S, -0.13 * S], [bract * S, 0], [0.6 * bract * S, 0.13 * S], [0, 0.08 * S]])
            _poly(ax, f(smooth_closed(br, n=80)), _pt("bract_scale"), lw=0.7, zorder=zorder)
            out["bract"] = f([bract * S * 0.85, 0.06 * S])[0] if bract > 0.9 else f([bract * S * 0.5, -0.11 * S])[0]
        x = np.linspace(0, 1, 60)
        hw = S * (0.11 + 0.27 * np.clip(x / 0.75, 0, 1) ** 0.8)
        cap = x > 0.82
        hw[cap] = np.minimum(hw[cap], S * 0.38 * np.sqrt(np.clip(1 - ((x[cap] - 0.82) / 0.18) ** 2, 0, 1)))
        sc = np.vstack([np.c_[x * S, hw], np.c_[x[::-1] * S, -hw[::-1]]])
        _poly(ax, f(sc), _pt("ovuliferous_scale"), lw=0.8, zorder=zorder + 0.1)
        # apophysis (exposed tip) and umbo
        m = x > 0.8
        ap = np.vstack([np.c_[x[m] * S, hw[m]], np.c_[x[m][::-1] * S, -hw[m][::-1]]])
        _poly(ax, f(ap), _pt("ovuliferous_scale"), lw=0.6, zorder=zorder + 0.2,
              fill=P.mix(P.fill(_pt("ovuliferous_scale")), P.edge(_pt("ovuliferous_scale")), 0.35))
        ax.add_patch(Circle(f([0.9 * S, 0])[0], 0.035 * S, facecolor=P.edge(_pt("ovuliferous_scale")), edgecolor="none",
                            zorder=zorder + 0.3))
        out.update(scale=f([0.5 * S, 0.2 * S])[0], apophysis=f([0.86 * S, 0.22 * S])[0], umbo=f([0.9 * S, 0])[0], ovules=[])
        for sg in (-1, 1):
            oc = np.array([0.2 * S, sg * 0.1 * S])
            if seeds:
                wing = np.array([oc + [-0.05 * S, -sg * 0.0], oc + [0.25 * S, sg * 0.08 * S], oc + [0.55 * S, sg * 0.1 * S],
                                 oc + [0.62 * S, sg * 0.03 * S], oc + [0.4 * S, -sg * 0.06 * S], oc + [0.05 * S, -sg * 0.07 * S]])
                _poly(ax, f(smooth_closed(wing, n=80)), _pt("wing"), lw=0.6, zorder=zorder + 0.35)
                out.setdefault("wing", f(oc + [0.4 * S, sg * 0.02 * S])[0])
            ax.add_patch(Ellipse(f(oc)[0], 0.17 * S, 0.11 * S, angle=angle, facecolor=P.fill(_pt("ovule")),
                                 edgecolor=P.edge(_pt("ovule")), lw=0.7, zorder=zorder + 0.4))
            if not seeds:
                for s2 in (-1, 1):
                    ax.plot(*f([[oc[0] - 0.08 * S, oc[1] + s2 * 0.02 * S], [oc[0] - 0.12 * S, oc[1] + s2 * 0.04 * S]]).T,
                            color=P.edge(_pt("ovule")), lw=0.8, zorder=zorder + 0.4)
            out["ovules"].append(f(oc)[0])
        out["seed" if seeds else "ovule"] = out["ovules"][0]
        out["micropyle"] = f([0.07 * S, 0.1 * S])[0]
        return out
    if kind == "pollen":
        x = np.linspace(0, 1, 50)
        hw = S * (0.06 + 0.16 * np.clip(x / 0.6, 0, 1))
        cap = x > 0.7
        hw[cap] = np.minimum(hw[cap], S * 0.22 * np.sqrt(np.clip(1 - ((x[cap] - 0.7) / 0.3) ** 2, 0, 1)))
        if view == "section":
            sc = np.array([[0, 0.02 * S], [0.7 * S, 0.03 * S], [0.98 * S, 0.1 * S], [1.0 * S, 0.02 * S], [0.75 * S, -0.03 * S],
                           [0, -0.02 * S]])
            _poly(ax, f(smooth_closed(sc, n=80)), _pt("sporophyll"), lw=0.8, zorder=zorder)
            sac = np.c_[0.42 * S + 0.26 * S * np.cos(np.linspace(0, 2 * math.pi, 60)),
                        -0.1 * S + 0.08 * S * np.sin(np.linspace(0, 2 * math.pi, 60))]
            _poly(ax, f(sac), _pt("pollen_sac"), lw=0.7, zorder=zorder + 0.1, fill=P.light(_pt("pollen_sac")))
            for k in range(5):
                _pollen_grain(ax, f([0.26 * S + k * 0.08 * S, -0.1 * S + (k % 2 - 0.5) * 0.03 * S])[0], 0.022 * S, zorder + 0.2)
            out.update(scale=f([0.85 * S, 0.04 * S])[0], pollen_sac=f([0.6 * S, -0.15 * S])[0], pollen=f([0.42 * S, -0.1 * S])[0])
            return out
        sc = np.vstack([np.c_[x * S, hw], np.c_[x[::-1] * S, -hw[::-1]]])
        _poly(ax, f(sc), _pt("sporophyll"), lw=0.8, zorder=zorder)
        out["scale"] = f([0.88 * S, 0])[0]
        if view == "abaxial":
            for sg in (-1, 1):
                ax.add_patch(Ellipse(f([0.38 * S, sg * 0.085 * S])[0], 0.5 * S, 0.14 * S, angle=angle,
                                     facecolor=P.fill(_pt("pollen_sac")), edgecolor=P.edge(_pt("pollen_sac")), lw=0.7,
                                     zorder=zorder + 0.1))
            out["pollen_sac"] = f([0.38 * S, 0.085 * S])[0]
        return out
    raise ValueError(f"unknown cone scale {kind!r}")


CONES = ("seed", "pollen", "lycopod", "selaginella", "equisetum")


def cone(ax, base, height, kind="seed", section=True, levels=None, zorder=6):
    """A cone (strobilus) standing on ``base``, ``height`` tall, in longitudinal section or external view.

    kind  "seed" (conifer ovulate cone: bract–scale complexes with ovules), "pollen" (conifer pollen cone:
          microsporophylls with pollen sacs), "lycopod" (*Lycopodium*: sporophylls with one adaxial
          sporangium each), "selaginella" (heterosporous: megasporangia with four megaspores below,
          microsporangia above), "equisetum" (peltate sporangiophores, sporangia hanging towards the axis)
    section  True: median longitudinal section; False: external view (spiral scales, or the hexagonal
             shields of *Equisetum*)
    Returns anchors: axis, peduncle, scale / sporophyll / sporangiophore, bract, ovule, pollen_sac, sporangium,
    megasporangium, microsporangium, shield; "units": list of per-level anchor dicts (section).
    """
    b = np.asarray(base, float)
    H = height
    out = dict(units=[])
    aw = 0.05 * H if kind in ("seed", "pollen") else 0.035 * H
    top = b + [0, H * 0.96]
    n = levels or {"seed": 7, "pollen": 9, "lycopod": 9, "selaginella": 9, "equisetum": 6}[kind]
    if not section:
        return _cone_outside(ax, b, H, kind, zorder, out)
    _poly(ax, [b + [-aw, 0], top + [-aw * 0.6, 0], top + [aw * 0.6, 0], b + [aw, 0]], _pt("cone_axis"), lw=0.8, zorder=zorder + 1)
    out["axis"] = b + [aw * 0.2, H * 0.5]
    out["peduncle"] = b + [aw, H * 0.04]
    for k in range(2 * n):
        side = 1 if k % 2 == 0 else -1
        j = k / 2
        y = H * (0.1 + 0.8 * j / n)
        prof = math.sin(math.pi * (j + 0.8) / (n + 1.0)) ** 0.7
        p = b + [side * aw * 0.9, y]
        u = {}
        if kind == "seed":
            L = 0.5 * H * prof
            ang = 90 - side * 62
            u = cone_scale(ax, p, L, "ovulate", view="section", angle=ang, flip=side < 0, zorder=zorder + 0.02 * k)
        elif kind == "pollen":
            L = 0.28 * H * prof
            ang = 90 - side * 70
            u = cone_scale(ax, p, L, "pollen", view="section", angle=ang, flip=side < 0, zorder=zorder + 0.02 * k)
        elif kind in ("lycopod", "selaginella"):
            L = 0.32 * H * prof
            ang = 90 - side * 55
            f = _loc(p, ang)
            leaf = np.array([[0, 0.01 * L], [0.6 * L, 0.06 * L], [L, 0.0], [0.6 * L, -0.06 * L], [0, -0.04 * L]])
            _poly(ax, f(smooth_closed(leaf, n=60)), _pt("sporophyll"), lw=0.7, zorder=zorder + 0.02 * k)
            sgn = 1 if side > 0 else -1  # adaxial side = towards the cone apex
            sc = np.array([0.24 * L, sgn * 0.13 * L])
            mega = kind == "selaginella" and j < n / 2
            r_ = 0.12 * L if not mega else 0.15 * L
            ax.add_patch(Ellipse(f(sc)[0], 2.2 * r_, 1.5 * r_, angle=ang, facecolor=P.light(_pt("sporangium")),
                                 edgecolor=P.edge(_pt("sporangium")), lw=0.7, zorder=zorder + 0.1 + 0.02 * k))
            if mega:
                for t_ in range(4):
                    q = sc + np.array([math.cos(t_ * math.pi / 2 + 0.6), math.sin(t_ * math.pi / 2 + 0.6)]) * r_ * 0.45
                    ax.add_patch(Circle(f(q)[0], r_ * 0.38, facecolor=P.fill(_pt("spore")), edgecolor=P.edge(_pt("spore")),
                                        lw=0.4, zorder=zorder + 0.2 + 0.02 * k))
                out.setdefault("megasporangium", f(sc)[0])
            else:
                for t_ in range(7):
                    q = sc + np.array([math.cos(t_ * 2.4), math.sin(t_ * 2.4)]) * r_ * 0.5 * math.sqrt((t_ + 0.5) / 7)
                    ax.add_patch(Circle(f(q)[0], r_ * 0.13, facecolor=P.fill(_pt("spore")), edgecolor=P.edge(_pt("spore")),
                                        lw=0.3, zorder=zorder + 0.2 + 0.02 * k))
                if kind == "selaginella":
                    out.setdefault("microsporangium", f(sc)[0])
            u = dict(sporophyll=f([0.7 * L, 0])[0], sporangium=f(sc)[0])
        elif kind == "equisetum":
            L = 0.2 * H * (0.6 + 0.4 * prof)
            f = _loc(p, 90 - side * 90)
            ax.plot(*f([[0, 0], [L, 0]]).T, color=P.edge(_pt("sporangiophore")), lw=2.0, zorder=zorder + 0.3)
            shield = np.array([[L, -0.38 * L], [L * 1.12, -0.36 * L], [L * 1.12, 0.36 * L], [L, 0.38 * L]])
            _poly(ax, f(shield), _pt("sporangiophore"), lw=0.8, zorder=zorder + 0.4)
            for sg in (-1, 1):
                sac = np.array([L * 0.6, sg * 0.2 * L])
                ax.add_patch(Ellipse(f(sac)[0], 0.75 * L, 0.26 * L, angle=0, facecolor=P.light(_pt("sporangium")),
                                     edgecolor=P.edge(_pt("sporangium")), lw=0.6, zorder=zorder + 0.35))
            u = dict(sporangiophore=f([L * 0.4, 0])[0], shield=f([L * 1.06, 0.2 * L])[0], sporangium=f([L * 0.6, 0.2 * L])[0])
        out["units"].append(u)
    mid = out["units"][len(out["units"]) // 2 - 1] if out["units"] else {}
    for key in ("scale", "bract", "ovule", "micropyle", "pollen_sac", "sporophyll", "sporangium", "sporangiophore", "shield"):
        if key in mid:
            out[key] = mid[key]
    return out


def _cone_outside(ax, b, H, kind, zorder, out):
    """External view of a cone: scales on spirals (back to front), or Equisetum's hexagonal shields."""
    R0 = {"seed": 0.3, "pollen": 0.16, "lycopod": 0.14, "selaginella": 0.14, "equisetum": 0.17}[kind] * H
    ax.plot([b[0], b[0]], [b[1], b[1] + 0.08 * H], color=P.edge(_pt("cone_axis")), lw=2.0, zorder=zorder)
    out["peduncle"] = b + [0, 0.04 * H]

    def radius(z):
        return R0 * max(0.0, math.sin(math.pi * min(1.0, max(0.0, z)) ** 0.85)) ** 0.6
    if kind == "equisetum":
        rows, per = 9, 7
        hexes = []
        for r_ in range(rows):
            z = 0.1 + 0.85 * (r_ + 0.5) / rows
            Rz = radius(z)
            for k in range(per):
                th = 2 * math.pi * (k + 0.5 * (r_ % 2)) / per
                if math.cos(th) < 0.05:
                    continue
                x = Rz * math.sin(th)
                sz = 0.85 * H / rows * 0.55
                hexes.append((math.cos(th), b + [x, 0.08 * H + z * 0.9 * H], sz * (0.35 + 0.65 * math.cos(th)), sz))
        for depth, p, sx, sy in sorted(hexes, key=lambda t: t[0]):
            hx = [p + [sx * math.cos(a), sy * math.sin(a)] for a in np.linspace(0, 2 * math.pi, 7)[:-1] + math.pi / 6]
            _poly(ax, hx, _pt("sporangiophore"), lw=0.7, zorder=zorder + depth)
            ax.add_patch(Circle(p, sy * 0.12, facecolor=P.edge(_pt("sporangiophore")), edgecolor="none", zorder=zorder + depth + 0.01))
        out["shield"] = hexes[len(hexes) // 2][1]
        out["sporangiophore"] = out["shield"]
        return out
    N = {"seed": 70, "pollen": 90, "lycopod": 110, "selaginella": 110}[kind]
    items = []
    for k in range(N):
        z = (k + 0.5) / N
        th = k * math.radians(137.508)
        if math.cos(th) < -0.1:
            continue
        Rz = radius(z)
        x = Rz * math.sin(th)
        y = 0.08 * H + z * 0.9 * H
        items.append((math.cos(th), z, np.array([b[0] + x, b[1] + y]), Rz))
    tk = _pt("ovuliferous_scale") if kind == "seed" else _pt("sporophyll") if kind != "pollen" else _pt("pollen_sac")
    d = math.sqrt(2 * math.pi * R0 * 0.9 * H * 0.75 / N)  # spacing of scales on the surface
    for depth, z, p, Rz in sorted(items, key=lambda t: (t[0], t[1])):
        w = 1.25 * d * (0.3 + 0.7 * max(0.0, depth)) * (0.5 + 0.5 * Rz / R0)
        h = 1.05 * d * (0.6 + 0.4 * Rz / R0)
        if kind == "seed":  # rhombic apophysis with a central umbo
            pts = [p + [0, h * 0.55], p + [w * 0.5, 0], p + [0, -h * 0.45], p + [-w * 0.5, 0]]
            _poly(ax, smooth_closed(pts, n=40), tk, lw=0.6, zorder=zorder + depth + z * 0.01)
            ax.add_patch(Circle(p, h * 0.07, facecolor=P.edge(tk), edgecolor="none", zorder=zorder + depth + z * 0.01 + 0.001))
        else:  # imbricate pointed scales
            pts = [p + [-w * 0.45, -h * 0.3], p + [0, h * 0.6], p + [w * 0.45, -h * 0.3], p + [0, -h * 0.45]]
            _poly(ax, smooth_closed(pts, n=30), tk, lw=0.5, zorder=zorder + depth + z * 0.01)
    out["scale"] = items[len(items) // 2][2]
    out["sporophyll"] = out["scale"]
    out["axis"] = b + [0, 0.5 * H]
    return out
