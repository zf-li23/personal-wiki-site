"""Limb development and insect imaginal discs: the vertebrate limb bud with its signalling centres and axes,
schematic limb skeletons (stylopod, zeugopod, autopod and digits), a transverse section of the bud for the
dorso-ventral axis, the Drosophila wing disc with its compartments, the leg disc and its telescoped leg, and
a larva with its imaginal discs.

    from wikibio import limbdev as LD
    b = LD.limb_bud(ax, (2, 4), 5.0, 3.0, stage="early")      dorsal view, flank on the left, distal right,
                                                              anterior up; AER, progress zone, ZPA; returns
                                                              anchors and ``b["at"](s, a)`` (s = 0 base ... 1 tip,
                                                              a = -1 posterior ... +1 anterior) for placing marks
    LD.axes_glyph(ax, (1, 1), 1.0)                            P-D and A-P arrows, D-V as "out of the page"
    s = LD.limb_skeleton(ax, (2, 1), 6.0, digits=(1, 2, 3, 4, 5), upto="autopod")
                                                              digits listed anterior to posterior; identities
                                                              1-5 set length and phalanx number; mirror
                                                              duplications as (4, 3, 2, 2, 3, 4); colour by
                                                              segment ("segment") or by bone ("bone")
    x = LD.bud_section(ax, (8, 4), 4.0, 2.0)                  P-D x D-V section: dorsal and ventral ectoderm,
                                                              AER at their boundary, dorsal mesenchyme
    w = LD.WingDisc(ax, (6, 4), 3.0, 2.4)                     third-instar wing disc (anterior left, notum up);
        w.region("P", "posterior"); w.stripe(0.0, 0.18, "dpp"); w.dv_stripe(0.08, "wg"); w.gradient(...)
    LD.leg_disc(ax, (2, 2), 1.2, SEGMENTS)                    concentric folds of the leg disc
    LD.telescoped_leg(ax, (4, 2), 5.0, SEGMENTS)              the everted leg, the centre of the disc distal
    l = LD.larva(ax, (6, 3), 9.0)                             third-instar larva (lateral, anterior left) with
                                                              the imaginal discs; l["discs"][name]

Colours use palette tokens only: the bud mesenchyme is lateral plate mesoderm (``zoology.GERM`` mesoderm),
its jacket ectoderm; the AER is a ridge of ectoderm, the progress zone ``highlight``, the ZPA ``protein``.
Limb segments: stylopod ``humerus``, zeugopod ``radius``/``ulna``, autopod ``carpals``, ``metacarpals``,
``phalanges`` (the bone tokens of ``zoomorph.BONE``). Every function is deterministic and returns anchors in
canvas coordinates.
"""

import math

import numpy as np
from matplotlib.patches import Circle, Ellipse, PathPatch, Polygon
from matplotlib.path import Path

from . import palette as P
from .core import LINE, arrow, label, polyline, smooth_closed
from .zoology import GERM

ZONES = {"mesenchyme": GERM["mesoderm"], "ectoderm": GERM["ectoderm"], "aer": GERM["ectoderm"], "pz": "highlight",
         "zpa": "protein", "flank": GERM["mesoderm"]}
SEGMENT = {"stylopod": "humerus", "zeugopod": "radius", "autopod": "phalanges"}
# digit identity -> (number of phalanges, relative length of the digit)
DIGIT = {1: (2, 0.62), 2: (3, 0.86), 3: (3, 1.0), 4: (3, 0.93), 5: (3, 0.74)}
# leg segments of Drosophila from distal (disc centre) to proximal (disc rim): (name, token, relative length)
LEG = [("claw", "neutral", 0.10), ("tarsus", "tarsus", 0.26), ("tibia", "tibia", 0.24), ("femur", "femur", 0.24),
       ("trochanter", "trochanter", 0.06), ("coxa", "coxa", 0.10)]


def _wash(token, t=0.5):
    """A pale shade of a token's fill that keeps the hue in both themes."""
    return P.mix(P.fill(token), P.surface(), 0.62 if P.is_dark() else t)


def _frame(base, angle_deg, mirror=False):
    th = math.radians(angle_deg)
    ed = np.array([math.cos(th), math.sin(th)])
    ea = np.array([-math.sin(th), math.cos(th)]) * (-1 if mirror else 1)
    b = np.asarray(base, float)

    def to(u, v):
        u = np.asarray(u, float)
        v = np.asarray(v, float)
        return b + np.multiply.outer(u, ed) + np.multiply.outer(v, ea)

    return to


def _open_spline(points, n=160):
    """Catmull-Rom spline through ``points`` (open curve, end tangents from the end segments)."""
    p = np.asarray(points, float)
    p = np.vstack([2 * p[0] - p[1], p, 2 * p[-1] - p[-2]])
    out = []
    m = len(p) - 3
    for i in range(m):
        p0, p1, p2, p3 = p[i], p[i + 1], p[i + 2], p[i + 3]
        for t in np.linspace(0, 1, max(4, n // m), endpoint=False):
            t2, t3 = t * t, t * t * t
            out.append(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t2 + (-p0 + 3 * p1 - 3 * p2 + p3) * t3))
    out.append(p[-2])
    return np.array(out)


def _patch(ax, pts, face, edge="none", lw=LINE * 0.8, z=5, closed=True, ls="-"):
    v = np.asarray(pts, float)
    if closed:
        v = np.vstack([v, v[:1]])
    p = PathPatch(Path(v, closed=closed), facecolor=face if closed else "none", edgecolor=edge, lw=lw, zorder=z,
                  joinstyle="round", capstyle="round", ls=ls)
    ax.add_patch(p)
    return p


def _band(curve, w_out, w_in, normals):
    """Polygon between offsets ``w_out`` (along normals) and ``-w_in`` of an open curve."""
    a = curve + normals * w_out
    b = curve - normals * w_in
    return np.vstack([a, b[::-1]])


def _outward(curve, normals, centre):
    """Flip normals so that they point away from ``centre``."""
    mid = len(curve) // 2
    if np.dot(normals[mid], curve[mid] - centre) < 0:
        return -normals
    return normals


def _arc_slice(curve, normals, f0, f1):
    seg = np.hypot(*np.diff(curve, axis=0).T)
    s = np.r_[0, np.cumsum(seg)]
    s /= s[-1]
    k = (s >= f0) & (s <= f1)
    return curve[k], normals[k]


# ---------------------------------------------------------------------------------------------------------------
# the limb bud


_BUD = {
    # control points (s = u / L, a = v / h) from posterior base to anterior base
    "early": [(0.0, -1.05), (0.4, -0.98), (0.78, -0.72), (1.0, 0.0), (0.8, 0.66), (0.42, 0.92), (0.0, 1.0)],
    "paddle": [(0.0, -0.9), (0.32, -0.84), (0.58, -0.98), (0.84, -1.12), (0.99, -0.55), (1.0, 0.1), (0.95, 0.7),
               (0.8, 1.05), (0.56, 0.88), (0.3, 0.8), (0.0, 0.88)],
}


def limb_bud(ax, base, length, width, angle=0.0, stage="early", mirror=False, aer=True, pz=True, zpa=True,
             flank=True, pz_depth=0.24, zones=None, lw=LINE, z=5):
    """A vertebrate limb bud in dorsal view, growing from the flank at ``base`` towards ``angle`` (degrees).

    ``length`` is the proximo-distal extent, ``width`` the antero-posterior width at the base. Anterior is to the
    left of the distal direction (up when the bud points right); ``mirror=True`` swaps it. stage: "early"
    (a rounded bump, chick HH20-21) or "paddle" (a stalk with a broad autopod plate, HH24-26). The mesenchyme is
    lateral plate mesoderm under an ectodermal jacket; ``aer`` draws the apical ectodermal ridge along the distal
    rim, ``pz`` the distal progress zone (``pz_depth`` as a fraction of the length), ``zpa`` the zone of
    polarizing activity at the posterior margin. ``zones`` overrides the tokens of ``ZONES``.
    Returns anchors "base", "tip", "aer", "pz", "zpa", "anterior", "posterior", "flank", "outline" (array) and
    "at": a function (s, a) -> canvas point, s = 0 at the base to 1 at the tip, a = -1 posterior to +1 anterior.
    """
    T = dict(ZONES, **(zones or {}))
    L, h = float(length), float(width) / 2
    to = _frame(base, angle, mirror)
    cp = np.array(_BUD[stage])
    local = _open_spline(np.c_[cp[:, 0] * L, cp[:, 1] * h], n=220)
    curve = to(local[:, 0], local[:, 1])
    fl = 1.9 * h
    depth = 0.32 * L
    out = []
    if flank:
        wall = np.vstack([to(-depth, -fl), to(0, -fl), curve, to(0, fl), to(-depth, fl)])
        _patch(ax, wall, _wash(T["flank"], 0.55), z=z)
        surface = np.vstack([to(0, -fl), curve, to(0, fl)])
        _patch(ax, to(np.array([-depth, -depth]), np.array([-fl, fl])), "none", P.muted(), lw=lw * 0.5, z=z + 0.1, closed=False,
               ls=(0, (3, 2)))
    else:
        surface = curve
        _patch(ax, np.vstack([curve, to(0, h * cp[-1, 1]), to(0, h * cp[0, 1])]), _wash(T["mesenchyme"], 0.45), z=z)
    # mesenchyme of the bud (a little more saturated than the flank)
    mes = _patch(ax, np.vstack([curve, curve[:1]]), _wash(T["mesenchyme"], 0.38), z=z + 0.2)
    pts, nrm, _ = polyline(curve, n=400, closed=False)
    centre = to(0.45 * L, 0.0)
    nrm = _outward(pts, nrm, centre)
    if pz:
        tip = to(L, 0)
        e = Ellipse(tuple(tip), 2 * pz_depth * L * 1.15, 2.6 * h, angle=angle, facecolor=_wash(T["pz"], 0.35),
                    edgecolor="none", zorder=z + 0.3)
        ax.add_patch(e)
        e.set_clip_path(mes)
    zc = to(0.62 * L if stage == "early" else 0.7 * L, -0.74 * h if stage == "early" else -0.86 * h)
    if zpa:
        zz = Ellipse(zc, 0.36 * L, 0.42 * h, angle=angle + (-20 if not mirror else 20), facecolor=P.fill(T["zpa"]),
                     edgecolor=P.edge(T["zpa"]), lw=lw * 0.7, zorder=z + 0.5)
        ax.add_patch(zz)
    # ectodermal jacket
    t = 0.035 * h + 0.02
    s_pts, s_nrm, _ = polyline(surface, n=500, closed=False)
    s_nrm = _outward(s_pts, s_nrm, centre)
    _patch(ax, _band(s_pts, t * 0.5, t * 0.5, s_nrm), P.fill(T["ectoderm"]), P.edge(T["ectoderm"]), lw=lw * 0.5, z=z + 0.6)
    aer_pt = to(L, 0)
    if aer:
        c, nm = _arc_slice(pts, nrm, 0.3, 0.7)
        k = np.linspace(0, 1, len(c))
        thick = (0.05 * h + 0.06) * np.sin(np.pi * k) ** 0.6 + t * 0.5
        poly = np.vstack([c + nm * thick[:, None], (c - nm * t * 0.5)[::-1]])
        _patch(ax, poly, P.fill(T["aer"]), P.edge(T["aer"]), lw=lw * 0.7, z=z + 0.7)
        aer_pt = c[len(c) // 2] + nm[len(c) // 2] * thick[len(c) // 2] * 0.6
    out = {
        "base": tuple(to(0, 0)), "tip": tuple(to(L, 0)), "aer": tuple(aer_pt), "pz": tuple(to((1 - pz_depth / 2) * L, 0)),
        "zpa": tuple(zc), "anterior": tuple(to(0.5 * L, 0.95 * h)), "posterior": tuple(to(0.5 * L, -1.0 * h)),
        "flank": tuple(to(-0.18 * L, 1.45 * h)), "outline": curve,
        "at": lambda s, a: tuple(to(s * L, a * h)),
    }
    return out


def axes_glyph(ax, at, size=1.0, angle=0.0, mirror=False, labels=True, color=None, z=18):
    """The three limb axes at ``at``: proximal -> distal along ``angle``, posterior -> anterior across it, and the
    dorso-ventral axis perpendicular to the page (dorsal towards the viewer, drawn as a dotted circle).
    Returns the tips {"distal", "anterior", "dorsal"}."""
    c = color or P.ink()
    to = _frame(at, angle, mirror)
    o = to(0, 0)
    d = to(size, 0)
    a = to(0, size * 0.85)
    arrow(ax, tuple(o), tuple(d), kind="process", color=c, lw=LINE * 0.8, head=0.14 * size + 0.04, zorder=z)
    arrow(ax, tuple(o), tuple(a), kind="process", color=c, lw=LINE * 0.8, head=0.14 * size + 0.04, zorder=z)
    dv = to(-0.42 * size, -0.42 * size)
    r = 0.13 * size + 0.03
    ax.add_patch(Circle(dv, r, facecolor="none", edgecolor=c, lw=LINE * 0.7, zorder=z))
    ax.add_patch(Circle(dv, r * 0.28, facecolor=c, edgecolor="none", zorder=z))
    if labels:
        fs = "tiny"
        label(ax, tuple(to(size + 0.12, 0)), "Distal", size=fs, ha="left" if abs(angle) < 90 else "right", color=c)
        label(ax, tuple(to(-0.1, -0.12)), "Proximal", size=fs, ha="right" if abs(angle) < 90 else "left", va="top", color=c)
        label(ax, tuple(to(0, size * 0.85 + 0.18)), "Anterior", size=fs, va="bottom", color=c)
        label(ax, tuple(dv + np.array([0, -r - 0.08])), "Dorsal (towards viewer)", size=fs, va="top", color=c)
    return {"distal": tuple(d), "anterior": tuple(a), "dorsal": tuple(dv)}


# ---------------------------------------------------------------------------------------------------------------
# skeletons


def _bone(ax, p0, p1, w, token, lw, z, face=None):
    """A long bone between p0 and p1: a shaft with slightly expanded ends."""
    p0, p1 = np.asarray(p0, float), np.asarray(p1, float)
    d = p1 - p0
    n = np.hypot(*d)
    if n < 1e-9:
        return
    e = d / n
    q = np.array([-e[1], e[0]])
    ts = np.linspace(0, 1, 9)
    prof = w * (0.5 - 0.06 * np.sin(np.pi * ts))
    left = [p0 + e * n * t + q * pw for t, pw in zip(ts, prof)]
    right = [p0 + e * n * t - q * pw for t, pw in zip(ts[::-1], prof[::-1])]
    cap0 = p0 - e * w * 0.35
    cap1 = p1 + e * w * 0.35
    pts = [cap0] + left + [cap1] + right
    v = smooth_closed(np.array(pts), 90)
    _patch(ax, v, face or P.fill(token), P.edge(token), lw=lw, z=z)


def _nodule(ax, c, rx, ry, token, lw, z, angle=0.0, face=None):
    ax.add_patch(Ellipse(c, 2 * rx, 2 * ry, angle=angle, facecolor=face or P.fill(token), edgecolor=P.edge(token), lw=lw,
                         zorder=z))


def limb_skeleton(ax, base, length, angle=0.0, digits=(1, 2, 3, 4, 5), upto="autopod", colored="segment",
                  width=None, mirror=False, proportions=(0.34, 0.28, 0.38), labels=False, digit_labels=False,
                  spread=None, muted=False, start="stylopod", lw=LINE * 0.6, z=8):
    """A schematic limb skeleton in dorsal view, proximal at ``base``, distal along ``angle``.

    ``digits`` lists digit identities from anterior to posterior (1-5; mirror duplications such as
    (4, 3, 2, 2, 3, 4) are allowed); identity sets the number of phalanges and the length (``DIGIT``).
    ``upto`` truncates the skeleton after "stylopod" or "zeugopod" (as after early removal of the AER), or
    after "carpals"; ``colored`` "segment" (stylopod, zeugopod, autopod), "bone" (bone tokens) or a single token.
    ``muted=True`` draws everything in the neutral shade; ``start="zeugopod"`` omits the stylopod (to draw a
    duplicated distal series beyond an existing skeleton). Returns anchors "stylopod", "zeugopod", "autopod",
    "wrist", "tip", "digits" (list of (identity, tip point)).
    """
    order = ["stylopod", "zeugopod", "carpals", "autopod"]
    stop = order.index(upto) if upto in order else 3
    L = float(length)
    W = width if width is not None else 0.075 * L
    to = _frame(base, angle, mirror)
    l1, l2, l3 = (L * f for f in proportions)

    def tok(part):
        if muted:
            return "neutral"
        if colored == "segment":
            return {"humerus": SEGMENT["stylopod"], "radius": SEGMENT["zeugopod"], "ulna": SEGMENT["zeugopod"],
                    "carpals": SEGMENT["autopod"], "metacarpals": SEGMENT["autopod"], "phalanges": SEGMENT["autopod"]}[part]
        if colored == "bone":
            return part
        return colored

    out = {"stylopod": tuple(to(l1 / 2, 0)), "digits": []}
    if start == "zeugopod":
        l1 = 0.0
    else:
        _bone(ax, to(0.02 * L, 0), to(l1, 0), W, tok("humerus"), lw, z)
    out["tip"] = tuple(to(l1 + W * 0.3, 0))
    if stop >= 1:
        g = W * 0.42
        y0 = l1 + (0.05 * L if l1 > 0 else 0.0)
        if l2 > 1e-6:
            _bone(ax, to(y0, g), to(y0 + l2, g * 1.1), W * 0.62, tok("radius"), lw, z)
            _bone(ax, to(y0, -g), to(y0 + l2, -g * 1.15), W * 0.72, tok("ulna"), lw, z)
        out["zeugopod"] = tuple(to(y0 + l2 / 2, 0))
        out["tip"] = tuple(to(y0 + l2 + W * 0.3, 0))
    wrist = l1 + l2 + 0.1 * L
    out["wrist"] = tuple(to(wrist, 0))
    n = len(digits)
    if stop >= 2:
        span = max(n, 2) * W * 1.15
        for r in range(2):
            k = max(2, n - 1 + r) if n > 1 else 1
            for j in range(k):
                v = (j - (k - 1) / 2) * span / k
                _nodule(ax, to(wrist + r * 0.05 * L, v), 0.02 * L, min(span / k * 0.4, 0.5 * W), tok("carpals"), lw, z,
                        angle=angle)
        out["autopod"] = tuple(to(wrist + 0.2 * L, 0))
        out["tip"] = tuple(to(wrist + 0.12 * L, 0))
    if stop >= 3 and n:
        fan = spread if spread is not None else min(5.0, 24.0 / max(n, 1))
        base_v = [((n - 1) / 2 - j) * W * 1.15 for j in range(n)]
        start = wrist + 0.1 * L
        for j, ident in enumerate(digits):
            nph, rel = DIGIT.get(abs(ident), (3, 0.9))
            ang = math.radians(((n - 1) / 2 - j) * fan)
            ln = l3 * rel
            p = np.array([start, base_v[j]])
            e = np.array([math.cos(ang), math.sin(ang)])
            mc = ln * (0.36 if nph == 3 else 0.42)
            q = p + e * mc
            _bone(ax, to(*p), to(*q), W * 0.5, tok("metacarpals"), lw, z)
            rest = ln - mc
            seg = rest / nph
            for k in range(nph):
                a = q + e * (seg * k + seg * 0.12)
                b = q + e * (seg * (k + 1) - seg * 0.05)
                _bone(ax, to(*a), to(*b), W * (0.44 - 0.04 * k), tok("phalanges"), lw, z)
            tip = to(*(q + e * rest))
            out["digits"].append((ident, tuple(tip)))
            if digit_labels:
                tl = to(*(q + e * (rest + 0.05 * L)))
                label(ax, tuple(tl), str(abs(ident)), size="tiny", color=P.ink(), ha="left" if abs(angle) < 90 else "right")
        out["tip"] = out["digits"][n // 2][1]
    if labels:
        off = max(n, 2) * W * 0.62 + 0.25
        label(ax, tuple(to(l1 / 2, -off)), "Stylopod", size="tiny", color=P.muted(), va="top")
        if stop >= 1:
            label(ax, tuple(to(l1 + 0.05 * L + l2 / 2, -off)), "Zeugopod", size="tiny", color=P.muted(), va="top")
        if stop >= 3:
            label(ax, tuple(to(wrist + 0.2 * L, -off)), "Autopod", size="tiny", color=P.muted(), va="top")
    return out


# ---------------------------------------------------------------------------------------------------------------
# a section through the bud (proximo-distal x dorso-ventral)


def bud_section(ax, base, length, height, dorsal="Wnt7a", ventral="En1", mesenchyme="Lmx1b", show_genes=True,
                dorsal_mes=True, mes="dorsal", dorsal_token="receptor", ventral_token="dna", lw=LINE, z=5):
    """A section of the limb bud through its proximo-distal and dorso-ventral axes (anterior-posterior axis
    perpendicular to the page): base (flank) at ``base`` on the left, distal right, dorsal up. Dorsal ectoderm
    (expressing ``dorsal``), ventral ectoderm (``ventral``), the AER at their boundary at the tip, and the dorsal
    half of the mesenchyme (``mesenchyme``) shaded (``mes``: "dorsal", "both" or "none"; ``dorsal_token`` and
    ``ventral_token`` colour the two ectoderms, e.g. both "receptor" for a double-dorsal mutant). Returns anchors "dorsal_ecto", "ventral_ecto", "aer",
    "dorsal_mes", "ventral_mes", "tip"."""
    L, h = float(length), float(height) / 2
    to = _frame(base, 0.0)
    cp = [(0.0, -1.0), (0.45, -0.92), (0.84, -0.62), (1.0, 0.0), (0.84, 0.62), (0.45, 0.92), (0.0, 1.0)]
    local = _open_spline(np.c_[[c[0] * L for c in cp], [c[1] * h for c in cp]], n=200)
    curve = to(local[:, 0], local[:, 1])
    _patch(ax, np.vstack([curve, curve[:1]]), _wash(ZONES["mesenchyme"], 0.42), z=z)
    if not dorsal_mes:
        mes = "none"
    if mes in ("dorsal", "both"):
        top = curve[curve[:, 1] >= to(0, 0)[1] - 1e-9]
        _patch(ax, np.vstack([top, to(0, 0)]), _wash("positive", 0.55), z=z + 0.1)
    if mes == "both":
        bot = curve[curve[:, 1] <= to(0, 0)[1] + 1e-9]
        _patch(ax, np.vstack([bot, to(0, 0)]), _wash("positive", 0.55), z=z + 0.1)
    pts, nrm, _ = polyline(curve, n=400, closed=False)
    nrm = _outward(pts, nrm, to(0.4 * L, 0))
    t = 0.07 * h + 0.03
    up = pts[:, 1] >= base[1]
    for mask, tk in ((up, dorsal_token), (~up, ventral_token)):
        c, nm = pts[mask], nrm[mask]
        if len(c) > 2:
            _patch(ax, _band(c, t, 0.0, nm), P.fill(tk), P.edge(tk), lw=lw * 0.5, z=z + 0.4)
    # AER at the boundary
    k = np.argmax(pts[:, 0])
    tip = pts[k]
    ax.add_patch(Ellipse(tip + nrm[k] * t * 0.6, 3.2 * t, 2.6 * t, facecolor=P.fill(ZONES["aer"]),
                         edgecolor=P.edge(ZONES["aer"]), lw=lw * 0.7, zorder=z + 0.5))
    out = {"dorsal_ecto": tuple(to(0.5 * L, 0.93 * h)), "ventral_ecto": tuple(to(0.5 * L, -0.93 * h)),
           "aer": tuple(tip + nrm[k] * t * 0.6), "dorsal_mes": tuple(to(0.45 * L, 0.42 * h)),
           "ventral_mes": tuple(to(0.45 * L, -0.42 * h)), "tip": tuple(tip)}
    if show_genes:
        label(ax, (out["dorsal_ecto"][0], out["dorsal_ecto"][1] + t + 0.25), dorsal, size="small", italic=True, va="bottom")
        label(ax, (out["ventral_ecto"][0], out["ventral_ecto"][1] - t - 0.25), ventral, size="small", italic=True, va="top")
        if mes in ("dorsal", "both"):
            label(ax, out["dorsal_mes"], mesenchyme, size="small", italic=True)
        if mes == "both":
            label(ax, out["ventral_mes"], mesenchyme, size="small", italic=True)
    return out


# ---------------------------------------------------------------------------------------------------------------
# Drosophila wing disc


class WingDisc:
    """A third-instar wing imaginal disc seen from the disc-proper side: anterior left, the notum (dorsal body
    wall) at the top, the wing pouch (future wing blade) an oval in the lower half ringed by the hinge folds.
    The anterior-posterior compartment boundary is a vertical line at ``ap`` (fraction of the half-width, right
    of the centre), the dorso-ventral boundary a horizontal line through the pouch centre.

        w = WingDisc(ax, (6, 4), 3.0, 2.5)
        w.region("P", "posterior")               fill a compartment ("A", "P", "D", "V") or "pouch", "notum"
        w.stripe(-0.16, 0.0, "dpp")              a vertical band (x in fractions of the half-width from the AP line)
        w.dv_stripe(0.07, "wg")                  a horizontal band along the DV boundary in the pouch
        w.gradient(lambda d: np.exp(-abs(d) / 0.3), "dpp")   shade the pouch by distance from the AP boundary
        w.boundaries()                           draw the two boundaries (dashed) and their names
    Methods return nothing; ``w.anchors`` holds named points.
    """

    def __init__(self, ax, center, rx, ry, ap=0.1, token="ectoderm", lw=LINE, z=5):
        self.ax, self.c, self.rx, self.ry, self.z, self.lw = ax, np.asarray(center, float), rx, ry, z, lw
        cx, cy = self.c
        pts = [(-1.0, -0.15), (-0.86, -0.72), (-0.45, -1.0), (0.1, -1.02), (0.62, -0.86), (0.95, -0.4), (0.98, 0.2),
               (0.8, 0.62), (0.42, 0.94), (-0.05, 1.0), (-0.55, 0.88), (-0.9, 0.48)]
        self.outline = smooth_closed(np.c_[cx + rx * np.array([p[0] for p in pts]), cy + ry * np.array([p[1] for p in pts])], 240)
        self.patch = _patch(ax, self.outline, _wash(token, 0.7), P.edge(token), lw=lw * 0.9, z=z)
        self.pc = np.array([cx - 0.02 * rx, cy - 0.33 * ry])
        self.prx, self.pry = 0.52 * rx, 0.44 * ry
        self.xap = cx + ap * rx
        self.ydv = self.pc[1]
        # hinge folds and notum
        for k, f in enumerate((1.28, 1.55)):
            e = Ellipse(self.pc, 2 * self.prx * f, 2 * self.pry * f, facecolor="none", edgecolor=P.edge(token), lw=lw * 0.45,
                        zorder=z + 2.4, ls=(0, (2, 2)))
            e.set_clip_path(self.patch)
            ax.add_patch(e)
        pouch = Ellipse(self.pc, 2 * self.prx, 2 * self.pry, facecolor=_wash(token, 0.55), edgecolor=P.edge(token), lw=lw * 0.6,
                        zorder=z + 0.2)
        ax.add_patch(pouch)
        self.pouch = pouch
        self.anchors = {
            "pouch": tuple(self.pc), "notum": (cx - 0.1 * rx, cy + 0.68 * ry), "hinge": (cx - 0.7 * rx, cy - 0.38 * ry),
            "ap_top": (self.xap, cy + 0.97 * ry), "ap_bottom": (self.xap, cy - 1.0 * ry),
            "dv_left": (self.pc[0] - self.prx, self.ydv), "dv_right": (self.pc[0] + self.prx, self.ydv),
            "A": (cx - 0.42 * rx, cy + 0.1 * ry), "P": (cx + 0.55 * rx, cy + 0.1 * ry),
            "D": (self.pc[0] - 0.25 * self.prx, self.ydv + 0.55 * self.pry), "V": (self.pc[0] - 0.25 * self.prx, self.ydv - 0.55 * self.pry),
        }

    def _clip(self, artist, pouch=False):
        artist.set_clip_path(self.pouch if pouch else self.patch)
        self.ax.add_artist(artist) if not isinstance(artist, (PathPatch, Polygon, Ellipse)) else self.ax.add_patch(artist)

    def region(self, which, token, shade=0.45, pouch_only=False):
        """Fill a compartment ("A", "P", "D", "V", or "pouch", "notum") with a wash of ``token``."""
        cx, cy = self.c
        big = 3 * max(self.rx, self.ry)
        if which == "A":
            v = [(cx - big, cy - big), (self.xap, cy - big), (self.xap, cy + big), (cx - big, cy + big)]
        elif which == "P":
            v = [(self.xap, cy - big), (cx + big, cy - big), (cx + big, cy + big), (self.xap, cy + big)]
        elif which == "D":
            v = [(cx - big, self.ydv), (cx + big, self.ydv), (cx + big, cy + big), (cx - big, cy + big)]
        elif which == "V":
            v = [(cx - big, cy - big), (cx + big, cy - big), (cx + big, self.ydv), (cx - big, self.ydv)]
        elif which == "pouch":
            e = Ellipse(self.pc, 2 * self.prx, 2 * self.pry, facecolor=_wash(token, shade), edgecolor="none", zorder=self.z + 0.6)
            self.ax.add_patch(e)
            return
        else:  # notum: the region above the outer hinge fold
            v = [(cx - big, self.pc[1] + 1.55 * self.pry), (cx + big, self.pc[1] + 1.55 * self.pry), (cx + big, cy + big),
                 (cx - big, cy + big)]
        p = Polygon(v, closed=True, facecolor=_wash(token, shade), edgecolor="none", zorder=self.z + 0.5)
        p.set_clip_path(self.pouch if pouch_only else self.patch)
        self.ax.add_patch(p)

    def stripe(self, x0, x1, token, pouch_only=False, shade=None, z=None):
        """A vertical band from x0 to x1 (fractions of the half-width, measured from the AP boundary)."""
        cy = self.c[1]
        big = 3 * self.ry
        a, b = self.xap + x0 * self.rx, self.xap + x1 * self.rx
        face = P.fill(token) if shade is None else _wash(token, shade)
        p = Polygon([(a, cy - big), (b, cy - big), (b, cy + big), (a, cy + big)], closed=True, facecolor=face,
                    edgecolor="none", zorder=z or self.z + 1.0)
        p.set_clip_path(self.pouch if pouch_only else self.patch)
        self.ax.add_patch(p)

    def dv_stripe(self, half, token, z=None, extend=1.0):
        """A horizontal band of half-height ``half`` (fraction of the pouch radius) along the DV boundary."""
        cx = self.pc[0]
        e = self.prx * extend
        p = Polygon([(cx - e, self.ydv - half * self.pry), (cx + e, self.ydv - half * self.pry), (cx + e, self.ydv + half * self.pry),
                     (cx - e, self.ydv + half * self.pry)], closed=True, facecolor=P.fill(token), edgecolor="none",
                    zorder=z or self.z + 1.1)
        p.set_clip_path(self.pouch)
        self.ax.add_patch(p)

    def gradient(self, func, token, pouch_only=True, n=60, z=None):
        """Shade by ``func(d)`` in [0, 1], d the signed distance from the AP boundary in half-widths."""
        cy = self.c[1]
        big = 3 * self.ry
        xs = np.linspace(self.c[0] - self.rx, self.c[0] + self.rx, n + 1)
        for a, b in zip(xs[:-1], xs[1:]):
            d = ((a + b) / 2 - self.xap) / self.rx
            f = float(np.clip(func(d), 0, 1))
            if f < 0.02:
                continue
            face = P.mix(P.surface(), P.fill(token), f)
            p = Polygon([(a, cy - big), (b + 1e-3, cy - big), (b + 1e-3, cy + big), (a, cy + big)], closed=True, facecolor=face,
                        edgecolor="none", zorder=z or self.z + 0.8)
            p.set_clip_path(self.pouch if pouch_only else self.patch)
            self.ax.add_patch(p)

    def boundaries(self, ap=True, dv=True, names=True, color=None):
        """Dashed lines on the compartment boundaries, with "A | P" and "D / V" names."""
        c = color or P.ink()
        cx, cy = self.c
        if ap:
            ln = self.ax.plot([self.xap, self.xap], [cy - 1.2 * self.ry, cy + 1.2 * self.ry], color=c, lw=self.lw * 0.8,
                              ls=(0, (4, 2)), zorder=self.z + 3)[0]
            ln.set_clip_path(self.patch)
        if dv:
            ln = self.ax.plot([self.pc[0] - 1.6 * self.prx, self.pc[0] + 1.6 * self.prx], [self.ydv, self.ydv], color=c,
                              lw=self.lw * 0.8, ls=(0, (1.5, 1.5)), zorder=self.z + 3)[0]
            ln.set_clip_path(self.patch)
        if names:
            for k in ("A", "P", "D", "V"):
                if (k in "AP" and ap) or (k in "DV" and dv):
                    label(self.ax, self.anchors[k], k, size="small", bold=True, color=c, zorder=self.z + 4)


# ---------------------------------------------------------------------------------------------------------------
# leg disc and eversion


def leg_disc(ax, center, r, segments=None, lw=LINE, z=5, labels=False):
    """The leg disc as concentric rings: the centre becomes the distal tip (claw), the rim the proximal coxa.
    ``segments`` as in ``LEG`` (distal first). Returns {name: point on the ring}."""
    segs = segments or LEG
    tot = sum(s[2] for s in segs)
    out = {}
    acc = 0.0
    rings = []
    for name, tk, f in segs:
        r0 = r * acc / tot
        acc += f
        r1 = r * acc / tot
        rings.append((name, tk, r0, r1))
    for name, tk, r0, r1 in rings[::-1]:
        ax.add_patch(Circle(center, r1, facecolor=_wash(tk, 0.35), edgecolor=P.edge(tk), lw=lw * 0.6, zorder=z))
        out[name] = (center[0] + (r0 + r1) / 2 * math.cos(math.radians(35)), center[1] + (r0 + r1) / 2 * math.sin(math.radians(35)))
    if labels:
        for name, *_ in rings:
            label(ax, out[name], name, size="tiny")
    return out


def telescoped_leg(ax, base, length, segments=None, angle=-90.0, radius=None, lw=LINE, z=5):
    """The everted adult leg drawn as tapering segments from the proximal coxa at ``base`` to the claw, along
    ``angle`` (default downwards). Segment colours match ``leg_disc``. Returns {name: segment centre}."""
    segs = (segments or LEG)[::-1]  # proximal first
    tot = sum(s[2] for s in segs)
    R = radius or 0.07 * length
    to = _frame(base, angle)
    out = {}
    u = 0.0
    for k, (name, tk, f) in enumerate(segs):
        ln = length * f / tot
        w0 = R * (1.0 - 0.55 * u / length)
        w1 = R * (1.0 - 0.55 * (u + ln) / length)
        if name == "claw":
            poly = [to(u, w0), to(u + ln, 0.15 * w1), to(u + ln * 1.1, -0.2 * w1), to(u, -w0)]
        else:
            poly = [to(u + 0.02 * ln, w0), to(u + 0.98 * ln, w1), to(u + 0.98 * ln, -w1), to(u + 0.02 * ln, -w0)]
        _patch(ax, smooth_closed(np.array(poly), 40) if name != "claw" else np.array(poly), _wash(tk, 0.35), P.edge(tk),
               lw=lw * 0.6, z=z)
        out[name] = tuple(to(u + ln / 2, 0))
        u += ln
    return out


# ---------------------------------------------------------------------------------------------------------------
# larva with imaginal discs


DISCS = [  # name, (s along body 0 anterior .. 1 posterior, a dorsal +1 .. ventral -1), (rx, ry) relative, token
    ("eye-antenna", (0.12, 0.25), (0.06, 0.20), "neuron"),
    ("leg 1", (0.24, -0.55), (0.03, 0.15), "tibia"),
    ("leg 2", (0.31, -0.55), (0.03, 0.15), "tibia"),
    ("leg 3", (0.38, -0.55), (0.03, 0.15), "tibia"),
    ("wing", (0.33, 0.45), (0.045, 0.22), "channel"),
    ("haltere", (0.40, 0.45), (0.026, 0.13), "receptor"),
    ("genital", (0.86, -0.35), (0.035, 0.15), "protein"),
]


def larva(ax, center, length, height=None, discs=True, token="animal", lw=LINE, z=5):
    """A third-instar Drosophila larva in lateral view (anterior left, dorsal up) with the imaginal discs
    (eye-antenna, three leg pairs, wing, haltere, genital) as coloured ovals inside the translucent body.
    Returns {"body", "head", "tail", "discs": {name: centre}}."""
    L = float(length)
    H = height or 0.24 * L
    cx, cy = center
    x0 = cx - L / 2
    top = [(x0, cy), (x0 + 0.05 * L, cy + 0.36 * H), (x0 + 0.25 * L, cy + 0.5 * H), (x0 + 0.6 * L, cy + 0.5 * H),
           (x0 + 0.9 * L, cy + 0.38 * H), (x0 + L, cy + 0.08 * H), (x0 + 0.99 * L, cy - 0.12 * H), (x0 + 0.88 * L, cy - 0.38 * H),
           (x0 + 0.6 * L, cy - 0.5 * H), (x0 + 0.25 * L, cy - 0.5 * H), (x0 + 0.05 * L, cy - 0.34 * H)]
    body = smooth_closed(np.array(top), 260)
    bp = _patch(ax, body, _wash(token, 0.72), P.edge(token), lw=lw * 0.9, z=z)
    # segment grooves
    for k in range(1, 12):
        x = x0 + (0.09 + 0.075 * k) * L
        ln = ax.plot([x, x], [cy - 0.6 * H, cy + 0.6 * H], color=P.edge(token), lw=lw * 0.35, zorder=z + 0.2)[0]
        ln.set_clip_path(bp)
    # mouth hooks
    ax.plot([x0 + 0.01 * L, x0 - 0.02 * L], [cy - 0.02 * H, cy - 0.14 * H], color=P.ink(), lw=lw * 0.9, zorder=z + 1,
            solid_capstyle="round")
    out = {"body": (cx, cy), "head": (x0, cy), "tail": (x0 + L, cy), "discs": {}}
    if discs:
        for name, (s, a), (rx, ry), tk in DISCS:
            c = (x0 + s * L, cy + a * 0.5 * H)
            ax.add_patch(Ellipse(c, 2 * rx * L, 2 * ry * H, facecolor=P.fill(tk), edgecolor=P.edge(tk), lw=lw * 0.6, zorder=z + 1))
            out["discs"][name] = c
    return out
