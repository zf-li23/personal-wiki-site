"""Parametric plant morphology: leaves, inflorescences, anatomical sections and plant architecture.

Everything here is generated from rules, so it can be varied freely (``plant`` has floral diagrams,
floral formulae, ferns and life cycles; templates of real plants come from the icon library).

    from wikibio import botany as B
    a = B.leaf(ax, (2, 1), 3.0, angle=90, shape="ovate", margin="serrate", venation="pinnate")
    bio.callout(ax, a["petiole"], (0.5, 1.5), "Petiole");  B.leaf_point(a, 0.6, -0.4);  B.vein_point(a, 2, 0.5, -0.5)
    B.compound_leaf(ax, (6, 1), 4.0, kind="imparipinnate", leaflets=4)
    B.shoot(ax, (10, 0.5), 5.0, arrangement="decussate");  B.bud(ax, (10, 6), 0.4)
    B.phyllotaxis(ax, (14, 3), 2.5, n=60, parastichies=(8, 13))
    B.inflorescence(ax, (18, 0.5), 4.0, kind="compound umbel");  B.flower(ax, (20, 5), 0.2)
    S = B.stem_section(ax, (4, 4), 3.0, kind="eudicot");  bio.callout(ax, S["xylem"], (8, 6), "Xylem")
    B.root_section(ax, (4, 4), 3.0, kind="monocot")
    B.leaf_anatomy(ax, (0, 0, 10, 3), kind="C4")
    B.woody_stem(ax, (5, 5), 4.0, years=5);  B.wood_strip(ax, (0, 0, 12, 3), years=3, kind="ring-porous")
    B.branching(ax, (2, 0), 4, kind="sympodial")
    B.lsystem_tree(ax, (3, 0), 6, habit="excurrent");  B.crown_tree(ax, (9, 0), 6)
    s = B.lsystem("A", {"A": "F[+A][-A]"}, 5);  t = B.turtle(s, angle=25)     the L-system engine itself
    o = B.blade_outline("cordate", 2.0, margin="crenate")                     outline only (no drawing)
    sec = B.Section(); sec.ring(...); sec.fill(...); sec.draw(ax)              cells for any new section

Catalogues: ``SHAPES``, ``APICES``, ``BASES``, ``MARGINS``, ``VENATION``, ``ARRANGEMENT``, ``INFLORESCENCES``,
``HABITS``; ``STYLE`` (cell drawing per tissue), ``TISSUE`` (tissue -> token), ``GOLDEN_ANGLE``.

Terminology follows the standard glossaries (Harris & Harris, Plant Identification Terminology, 2nd ed.;
Simpson, Plant Systematics, 3rd ed.; Beentje, The Kew Plant Glossary; Evert, Esau's Plant Anatomy;
Hallé, Oldeman & Tomlinson, Tropical Trees and Forests, for architecture).

Conventions
- Lengths are canvas units; angles in degrees, anticlockwise from +x (90 = up).
- Every drawing function returns a dict of anchors (canvas points) for ``bio.callout``.
- Leaves are built in a local frame: blade base (petiole attachment) at the origin, apex on +x. A
  half-outline is generated from the blade *shape* (width profile), then the *apex* and *base* zones
  are replaced by their type, then the *margin* (lobes, then teeth) is applied along the normal.
- Sections are built from cells: every tissue places seeds (rings, files, rows or a Poisson-disc fill
  with a cell size per tissue); a power (Laguerre) diagram of the weighted seeds gives cell outlines
  whose sizes match the seeds; cells are shrunk (walls, intercellular spaces), rounded and drawn by
  tissue style (thin or thick walls, lumen, chloroplasts, Casparian strips).
- Colours are palette tokens through ``TISSUE`` (an alias table local to this module).
"""

import math

import numpy as np
from matplotlib.collections import LineCollection, PolyCollection
from matplotlib.patches import Circle, Ellipse, PathPatch, Polygon
from matplotlib.path import Path

from . import palette as P
from .core import LINE, label

# Tissue and organ -> palette token (local aliases; dedicated tokens are requested in the report).
TISSUE = {
    "leaf": "plant", "stem": "plant", "flower": "petal", "flower2": "highlight", "bud": "sepal", "bract": "bract",
    "spathe": "bract", "receptacle": "ovary", "floret": "anther", "ray_floret": "highlight",
    "epidermis": "cell_wall", "collenchyma": "collenchyma", "cortex": "cytoplasm", "pith": "cytoplasm", "ground": "cytoplasm",
    "parenchyma": "parenchyma", "sclerenchyma": "sclerenchyma", "hypodermis": "protein",
    "endodermis": "endodermis", "casparian": "negative", "pericycle": "pericycle", "exodermis": "lipid",
    "xylem": "xylem", "protoxylem": "channel", "phloem": "phloem", "cambium": "cambium", "air": "extracellular",
    "palisade": "plant", "spongy": "plant", "mesophyll": "plant", "sheath": "bract", "kranz": "kranz",
    "guard": "chloroplast", "bulliform": "bulliform", "chloroplast": "chloroplast", "root_hair": "cell_wall",
    "earlywood": "earlywood", "latewood": "latewood", "ray": "lipid", "heartwood": "heartwood", "sapwood": "sapwood",
    "cork": "cork", "phellogen": "atp", "bark": "animal", "secondary_phloem": "lipid_head",
}

GOLDEN_ANGLE = 180.0 * (3.0 - math.sqrt(5.0))  # 137.507...°


def tok(name):
    """The palette token of a tissue / organ name (``TISSUE``), or the name itself if it is a token."""
    return TISSUE.get(name, name)


def _fill(name):
    return P.fill(tok(name))


def _edge(name):
    return P.edge(tok(name))


# ============================================================================ geometry helpers


def _rot(deg):
    a = math.radians(deg)
    return np.array([[math.cos(a), -math.sin(a)], [math.sin(a), math.cos(a)]])


def _place(local, base, angle):
    """Rotate local points (x along the organ axis) by ``angle`` and move the origin to ``base``."""
    return np.asarray(local, float) @ _rot(angle).T + np.asarray(base, float)


def _spline(points, n=60):
    """An open Catmull-Rom curve through the points (end points repeated)."""
    p = np.asarray(points, float)
    if len(p) < 3:
        t = np.linspace(0, 1, n)[:, None]
        return p[0] + (p[-1] - p[0]) * t
    q = np.vstack([p[0], p, p[-1]])
    out = []
    per = max(3, n // (len(p) - 1))
    for i in range(1, len(q) - 2):
        p0, p1, p2, p3 = q[i - 1], q[i], q[i + 1], q[i + 2]
        for t in np.linspace(0, 1, per, endpoint=False):
            t2, t3 = t * t, t * t * t
            out.append(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t2 + (-p0 + 3 * p1 - 3 * p2 + p3) * t3))
    out.append(p[-1])
    return np.array(out)


def _resample(p, n):
    p = np.asarray(p, float)
    keep = np.r_[True, np.hypot(*np.diff(p, axis=0).T) > 1e-12]
    p = p[keep]
    s = np.r_[0, np.cumsum(np.hypot(*np.diff(p, axis=0).T))]
    t = np.linspace(0, s[-1], n)
    return np.c_[np.interp(t, s, p[:, 0]), np.interp(t, s, p[:, 1])], s[-1]


def _bezier(a, c, b, n=40):
    t = np.linspace(0, 1, n)[:, None]
    a, c, b = (np.asarray(v, float) for v in (a, c, b))
    return (1 - t) ** 2 * a + 2 * (1 - t) * t * c + t ** 2 * b


def _smoothstep(x):
    x = np.clip(x, 0, 1)
    return x * x * (3 - 2 * x)


def _ray(poly, p, d):
    """Distance from p along unit direction d to the first crossing of the closed polyline ``poly``."""
    a = poly[:-1]
    b = poly[1:]
    e = b - a
    den = d[0] * e[:, 1] - d[1] * e[:, 0]
    ok = np.abs(den) > 1e-12
    w = a - p
    t = np.where(ok, (w[:, 0] * e[:, 1] - w[:, 1] * e[:, 0]) / np.where(ok, den, 1), np.inf)
    u = np.where(ok, (w[:, 0] * d[1] - w[:, 1] * d[0]) / np.where(ok, den, 1), -1)
    hit = ok & (t > 1e-6) & (u >= 0) & (u <= 1)
    return float(t[hit].min()) if hit.any() else 0.0


def _chaikin(poly, k=2):
    p = np.asarray(poly, float)
    for _ in range(k):
        q = np.roll(p, -1, axis=0)
        p = np.stack([0.75 * p + 0.25 * q, 0.25 * p + 0.75 * q], axis=1).reshape(-1, 2)
    return p


def _lw(size, base=1.0, ref=3.0):
    """Line width scaled with the organ size (canvas units), clipped to a readable range."""
    return base * float(np.clip(size / ref, 0.45, 1.5))


# ============================================================================ leaves

def _beta(a, b):
    m = a / (a + b)
    peak = m ** a * (1 - m) ** b

    def f(s):
        s = np.clip(s, 0, 1)
        return s ** a * (1 - s) ** b / peak
    return f


def _superellipse(p):
    return lambda s: np.clip(1 - np.abs(2 * np.clip(s, 0, 1) - 1) ** p, 0, 1) ** (1 / p)


def _rhombic(s):
    s = np.clip(s, 0, 1)
    return np.where(s < 0.45, s / 0.45, (1 - s) / 0.55)


def _deltoid(s):
    return np.clip(1 - np.clip(s, 0, 1), 0, 1) ** 0.95


def _spatulate(s):
    s = np.clip(s, 0, 1)
    return 0.16 + 0.84 * _beta(2.6, 0.55)(s)


# name: (width profile, width/length ratio, default apex, default base)
SHAPES = {
    "linear": (_superellipse(8), 0.11, "acute", "truncate"),
    "lanceolate": (_beta(0.6, 1.25), 0.27, "acuminate", "cuneate"),
    "oblanceolate": (_beta(1.25, 0.6), 0.27, "acute", "attenuate"),
    "elliptic": (_beta(0.8, 0.8), 0.5, "acute", "cuneate"),
    "oblong": (_superellipse(4), 0.42, "obtuse", "rounded"),
    "ovate": (_beta(0.55, 0.95), 0.62, "acute", "rounded"),
    "obovate": (_beta(0.95, 0.55), 0.62, "rounded", "cuneate"),
    "orbicular": (_superellipse(2), 1.0, "rounded", "rounded"),
    "cordate": (_beta(0.5, 0.95), 0.78, "acute", "cordate"),
    "reniform": (_superellipse(2), 1.45, "rounded", "cordate"),
    "sagittate": (_deltoid, 0.62, "acute", "sagittate"),
    "hastate": (_beta(0.5, 1.1), 0.36, "acute", "hastate"),
    "spatulate": (_spatulate, 0.42, "rounded", "attenuate"),
    "deltoid": (_deltoid, 1.0, "acute", "truncate"),
    "rhombic": (_rhombic, 0.62, "acute", "cuneate"),
    "flabellate": (None, 1.5, "truncate", "cuneate"),
    "palmately lobed": (None, 1.05, "acute", "cordate"),
}


def _circ(u):
    return np.sqrt(np.clip(1 - (1 - u) ** 2, 0, 1))


# name: (zone length in units of the local half-width, profile g(u), u = 0 at the tip)
APICES = {
    "acute": (1.0, lambda u: 1 - (1 - u) ** 1.25),
    "acuminate": (3.4, lambda u: u ** 1.9),
    "obtuse": (0.75, lambda u: 1 - (1 - u) ** 1.7),
    "rounded": (1.0, _circ),
    "truncate": (0.12, _circ),
    "emarginate": (1.0, _circ),
    "retuse": (1.0, _circ),
    "mucronate": (0.9, _circ),
    "cuspidate": (1.1, _circ),
    "aristate": (1.0, _circ),
}
BASES = {
    "cuneate": (1.0, lambda u: u ** 0.97),
    "attenuate": (3.4, lambda u: 0.04 + 0.96 * u ** 2.0),
    "rounded": (1.0, _circ),
    "obtuse": (0.7, lambda u: 1 - (1 - u) ** 1.7),
    "truncate": (0.1, _circ),
    "cordate": (1.0, _circ),
    "oblique": (1.0, _circ),
    "sagittate": None,
    "hastate": None,
}
MARGINS = ("entire", "sinuate", "serrate", "serrulate", "doubly serrate", "dentate", "crenate", "spinose", "lobed",
           "pinnatifid", "pinnatisect")
VENATION = ("pinnate", "brochidodromous", "arcuate", "palmate", "parallel", "dichotomous", "none")


def _zone(k, prof, h, L, end):
    """Zone length (fraction of L) such that its length is k times the half-width where it starts."""
    z = 0.2
    for _ in range(6):
        w = float(prof(1 - z if end == "apex" else z))
        z = float(np.clip(k * h * max(w, 0.05) / L, 0.02, 0.48))
    return z


def _half_outline(shape, L, W, apex, base, side=1, n=500):
    """Right half (side=1) of a blade, from the attachment (0, 0) to the apex (L, 0). Returns points."""
    prof, _, _, _ = SHAPES[shape]
    h = W / 2
    if shape == "flabellate":
        th = math.radians(62)
        edge = _spline([(0, 0), (0.45 * L * math.cos(th) * 0.98, 0.45 * L * math.sin(th) * 0.92),
                        (L * math.cos(th), L * math.sin(th))], 80)
        a = np.linspace(th, 0, 160)
        notch = 1 - 0.1 * np.exp(-(a / 0.08) ** 2)
        arc = np.c_[L * notch * np.cos(a), L * notch * np.sin(a)]
        pts = np.vstack([edge, arc[1:]])
        pts[:, 1] *= W / (2 * L * math.sin(th)) / 0.62 * 0.62
        return pts
    if shape == "palmately lobed":
        th = np.linspace(math.pi, 0, n)
        lobes = [(0, 1.0), (52, 0.86), (104, 0.52)]
        r = 0.36 + sum(A * np.exp(-np.abs(np.degrees(th) - t0) / 20.0) * 0.75 for t0, A in lobes)
        r = r * (1 - np.exp(-((math.pi - th) / 0.32) ** 2))
        pts = np.c_[r * np.cos(th), r * np.sin(th) * (W / 2) / 0.95]
        pts[:, 0] = (pts[:, 0] + 0.0) * L / 1.18
        return pts
    s = np.linspace(0, 1, n)
    w = prof(s)
    ka, ga = APICES[apex]
    za = _zone(ka, prof, h, L, "apex")
    wa = float(prof(1 - za))
    m = s > 1 - za
    w[m] = wa * ga((1 - s[m]) / za)
    lobed_base = base in ("sagittate", "hastate")
    if not lobed_base:
        kb, gb = BASES[base]
        if base == "oblique":
            kb, gb = (BASES["rounded"] if side > 0 else BASES["cuneate"])
        zb = _zone(kb, prof, h, L, "base")
        wb = float(prof(zb))
        m = s < zb
        w[m] = wb * gb(s[m] / zb)
    # light smoothing of the zone joins (keep the tip and base exact)
    k = 9
    ws = np.convolve(np.r_[np.full(k, w[0]), w, np.full(k, w[-1])], np.ones(2 * k + 1) / (2 * k + 1), mode="same")[k:-k]
    blend = np.minimum(1, np.minimum(s, 1 - s) / 0.04)
    w = w * (1 - blend) + ws * blend
    pts = np.c_[s * L, w * h]
    if apex in ("emarginate", "retuse"):
        d, c = (0.07, 0.35) if apex == "emarginate" else (0.03, 0.5)
        f = np.clip(1 - pts[:, 1] / (c * h), 0, 1) ** 1.6
        pts[:, 0] -= d * L * f * (pts[:, 0] > L * 0.6)
    elif apex in ("mucronate", "cuspidate", "aristate"):
        d, c = {"mucronate": (0.05, 0.05), "cuspidate": (0.12, 0.14), "aristate": (0.16, 0.025)}[apex]
        f = np.clip(1 - pts[:, 1] / (c * h + 1e-9), 0, 1) ** (1.0 if apex != "cuspidate" else 2.2)
        pts[:, 0] += d * L * f * (pts[:, 0] > L * 0.6)
        if apex == "aristate":  # a bristle: a thin line beyond the rounded tip
            tip = np.array([[L * (1 + d), 0.0]])
            pts = np.vstack([pts[pts[:, 0] < L * 0.995], [[L, 0.01 * h]], tip])
    if base == "cordate":
        deep = 0.2 if shape == "reniform" else 0.16
        yc = (0.32 if shape == "reniform" else 0.2) * h
        phi = 1 - np.exp(-(pts[:, 1] / yc) ** 2)
        psi = np.clip(1 - pts[:, 0] / (0.65 * L), 0, 1) ** 1.5
        pts[:, 0] -= deep * L * phi * psi
    elif base == "oblique" and side < 0:
        off = 0.12 * L
        pts[:, 0] = off + pts[:, 0] * (L - off) / L
        pts = np.vstack([[0, 0], pts])
    elif lobed_base:
        sj = 0.16 if base == "sagittate" else 0.2
        keep = s >= sj
        body = pts[keep]
        hj = body[0, 1]
        if base == "sagittate":
            lobe = _spline([(0, 0), (-0.14 * L, 0.18 * h), (-0.4 * L, 0.6 * h)], 50)
            outer = _spline([(-0.4 * L, 0.6 * h), (-0.18 * L, 0.98 * h), (body[0, 0] - 0.04 * L, hj * 1.02), body[0]], 50)
        else:
            lobe = _spline([(0, 0), (-0.05 * L, 0.6 * h), (-0.12 * L, 1.9 * h)], 50)
            outer = _spline([(-0.12 * L, 1.9 * h), (0.02 * L, 1.45 * h), (body[0, 0] - 0.02 * L, hj * 1.05), body[0]], 50)
        pts = np.vstack([lobe, outer[1:], body[1:]])
    return pts


def _lobes(pts, L, h, n, depth, shear=0.35):
    """Pinnate lobing: scale the half-width down towards narrow sinuses. Returns (points, tip idx, sinus idx)."""
    x, y = pts[:, 0], pts[:, 1]
    psi = (x - shear * y) / L * (n + 0.5)
    c = np.abs(np.cos(np.pi * psi)) ** 5
    fade = _smoothstep((x / L - 0.03) / 0.12) * _smoothstep((0.985 - x / L) / 0.05)
    out = np.c_[x, y * (1 - depth * c * fade)]
    tips, sinus = [], []
    for j in range(0, n + 1):  # lobes lie between sinuses (sinuses at integer psi)
        idx = np.where((psi > j + 0.05) & (psi < j + 0.95) & (x > 0.12 * L))[0]
        if len(idx):
            tips.append(int(idx[np.argmax(out[idx, 1])]))
    for j in range(1, n + 1):
        idx = np.where((psi > j - 0.3) & (psi < j + 0.3))[0]
        if len(idx):
            sinus.append(int(idx[np.argmin(out[idx, 1])]))
    return out, tips, sinus


def _teeth(pts, kind, L, n_teeth=None, depth=None):
    """Teeth along a half-outline (normal offsets). Returns (points, tooth-tip points)."""
    q, total = _resample(pts, 900)
    t = np.linspace(0, total, len(q))
    d = np.gradient(q, axis=0)
    d /= np.linalg.norm(d, axis=1)[:, None] + 1e-12
    nrm = np.c_[-d[:, 1], d[:, 0]]
    spec = {"serrate": (16, 0.03), "serrulate": (34, 0.012), "doubly serrate": (11, 0.045), "dentate": (14, 0.035),
            "crenate": (15, 0.028), "sinuate": (6, 0.035), "spinose": (7, 0.07)}[kind]
    nt = n_teeth or spec[0]
    dep = (depth or spec[1]) * L
    lam = total / nt
    phi = (t / lam) % 1.0
    if kind in ("serrate", "serrulate", "doubly serrate"):
        r = 0.78
        delta = np.where(phi < r, phi / r, 1 - (phi - r) / (1 - r)) - 1  # long proximal edge, short distal edge
        if kind == "doubly serrate":
            p2 = (phi * 3) % 1.0
            delta = 0.7 * delta + 0.3 * (np.where(p2 < r, p2 / r, 1 - (p2 - r) / (1 - r)) - 1)
        tip_phase = r
    elif kind == "dentate":
        delta = -np.abs(2 * phi - 1) ** 0.8  # tips at phi = 0.5, pointing outwards
        tip_phase = 0.5
    elif kind == "spinose":
        x = np.abs(2 * phi - 1)  # 0 at the spine tip, 1 in the sinus: concave arcs between sharp spines
        delta = -np.sqrt(np.clip(1 - (1 - x) ** 2, 0, 1))
        tip_phase = 0.5
    elif kind == "crenate":
        delta = np.sin(np.pi * phi) ** 0.7 - 1
        tip_phase = 0.5
    else:  # sinuate
        delta = (np.cos(2 * np.pi * (phi - 0.5)) - 1) / 2
        tip_phase = 0.5
    fade = _smoothstep(t / (0.1 * total)) * _smoothstep((total - t) / (0.07 * total))
    out = q + nrm * (delta * dep * fade)[:, None]
    tips = []
    for j in range(nt):
        tt = (j + tip_phase) * lam
        i = int(np.clip(np.searchsorted(t, tt), 0, len(t) - 1))
        if fade[i] > 0.5:
            tips.append(out[i])
    return out, np.array(tips) if tips else np.zeros((0, 2))


def blade_outline(shape="elliptic", length=1.0, width=None, apex=None, base=None, margin="entire", lobes=None,
                  teeth=None, depth=None):
    """The outline of a leaf blade in the local frame (base at the origin, apex on +x).

    shape   one of ``SHAPES`` (linear, lanceolate, oblanceolate, elliptic, oblong, ovate, obovate,
            orbicular, cordate, reniform, sagittate, hastate, spatulate, deltoid, rhombic, flabellate,
            palmately lobed); ``width`` defaults to the shape's usual width/length ratio
    apex    one of ``APICES`` (acute, acuminate, obtuse, rounded, truncate, emarginate, retuse,
            mucronate, cuspidate, aristate); base one of ``BASES`` (cuneate, attenuate, rounded, obtuse,
            truncate, cordate, oblique, sagittate, hastate)
    margin  one of ``MARGINS``; ``lobes`` (per side) for lobed / pinnatifid / pinnatisect, ``teeth``
            (per side) and ``depth`` (fraction of the length) for toothed margins
    Returns dict(outline=closed (N, 2) array, right=…, left=… half outlines (base → apex), tips=lobe
    or tooth tips (for craspedodromous veins), sinuses=…, length, width).
    """
    prof, ratio, apex0, base0 = SHAPES[shape]
    W = width if width is not None else ratio * length
    apex = apex or apex0
    base = base or base0
    L = length
    halves, tips, sinuses = {}, [], []
    for side in (1, -1):
        h = _half_outline(shape, L, W, apex, base, side=side)
        if margin in ("lobed", "pinnatifid", "pinnatisect"):
            n, dep = {"lobed": (lobes or 3, 0.5), "pinnatifid": (lobes or 5, 0.72), "pinnatisect": (lobes or 6, 0.92)}[margin]
            h, ti, si = _lobes(h, L, W / 2, n, dep)
            tips += [h[i] * [1, side] for i in ti]
            sinuses += [h[i] * [1, side] for i in si]
        elif margin != "entire":
            h, tt = _teeth(h, margin, L, n_teeth=teeth, depth=depth)
            tips += [p * [1, side] for p in tt]
        halves[side] = h * [1, side]
    if shape == "palmately lobed":
        # lobe tips: the outline points farthest from the attachment near each lobe direction
        for side in (1, -1):
            hh = halves[side]
            ang = np.degrees(np.arctan2(np.abs(hh[:, 1]), hh[:, 0]))
            for t0 in (0, 52, 104):
                idx = np.where(np.abs(ang - t0) < 14)[0]
                if len(idx) and not (t0 == 0 and side < 0):
                    j = idx[np.argmax(np.hypot(*hh[idx].T))]
                    tips.append(hh[j])
    outline = np.vstack([halves[1], halves[-1][::-1][1:]])
    return dict(outline=outline, right=halves[1], left=halves[-1], tips=np.array(tips).reshape(-1, 2),
                sinuses=np.array(sinuses).reshape(-1, 2), length=L, width=W, shape=shape, margin=margin)


def _vein_lines(o, venation, secondaries=None, tertiary=None, angle=None, seed=0):
    """Vein polylines in the local frame: list of (points, order) with order 1 (primary) .. 3."""
    L, W = o["length"], o["width"]
    out = []
    poly = np.vstack([o["outline"], o["outline"][:1]])
    if venation == "none":
        return out
    if venation == "dichotomous":
        # isotomous dichotomies: a binary tree whose 2^K ends meet the distal margin
        K = secondaries or 4
        arc = np.vstack([o["left"][::-1], o["right"]])
        far = arc[np.hypot(*arc.T) > 0.82 * L]
        far = far[np.argsort(np.arctan2(far[:, 1], far[:, 0]))]
        targets, _ = _resample(far, 2 ** K + 2)
        targets = targets[1:-1] * 0.985
        ang_t = np.arctan2(targets[:, 1], targets[:, 0])
        r_end = np.hypot(*targets.T)

        def node(lo, hi, d):
            if hi - lo == 1:
                return targets[lo]
            a = ang_t[lo:hi].mean()
            r = float(r_end[lo:hi].mean()) * (0.06 + 0.94 * (d / K) ** 0.9)
            return np.array([r * math.cos(a), r * math.sin(a)])

        def split(lo, hi, d, start):
            here = node(lo, hi, d)
            out.append((np.vstack([start, here]), 1 if d <= 1 else 2))
            if hi - lo > 1:
                m = (lo + hi) // 2
                split(lo, m, d + 1, here)
                split(m, hi, d + 1, here)
        split(0, len(targets), 0, np.zeros(2))
        return out
    if venation == "parallel":
        right = o["right"]
        xs = right[:, 0]
        order = np.argsort(xs)
        xg = np.linspace(0, L, 120)
        hw = np.interp(xg, xs[order], np.abs(right[order, 1]))
        nv = secondaries or (2 if W < 0.15 * L else 4)
        out.append((np.c_[xg, 0 * xg], 1))
        for j in range(1, nv + 1):
            f = j / (nv + 0.6)
            for sg in (1, -1):
                out.append((np.c_[xg, sg * f * hw * 0.98], 2))
        if tertiary:
            rng = np.random.default_rng(seed)
            for x in np.linspace(0.08 * L, 0.92 * L, 22):
                j = rng.integers(0, nv)
                f0, f1 = j / (nv + 0.6), (j + 1) / (nv + 0.6)
                hh = float(np.interp(x, xg, hw))
                sg = 1 if rng.random() < 0.5 else -1
                out.append((np.array([[x, sg * f0 * hh], [x + 0.01 * L, sg * f1 * hh]]), 3))
        return out
    if venation == "palmate":
        tips = o["tips"] if len(o["tips"]) else None
        dirs = []
        if tips is not None and o["shape"] == "palmately lobed":
            dirs = [t for t in tips]
        else:
            for a in (0, 42, 80):
                for sg in ((1,) if a == 0 else (1, -1)):
                    d = np.array([math.cos(math.radians(a)), sg * math.sin(math.radians(a)) * W / L])
                    d /= np.linalg.norm(d)
                    dirs.append(d * _ray(poly, np.zeros(2), d) * 0.94)
        origin = np.zeros(2)
        prim = []
        for t in dirs:
            t = np.asarray(t, float) * 0.97
            ctrl = t * 0.5 + np.array([-t[1], t[0]]) * 0.03
            c = _bezier(origin, ctrl, t, 40)
            prim.append(c)
            out.append((c, 1))
            # secondaries on both sides of each primary
            ln = np.linalg.norm(t)
            u = t / (ln + 1e-9)
            for f in (0.3, 0.5, 0.7):
                p = origin + t * f
                for sg in (1, -1):
                    a = math.radians(48 * sg)
                    dv = np.array([u[0] * math.cos(a) - u[1] * math.sin(a), u[0] * math.sin(a) + u[1] * math.cos(a)])
                    r = _ray(poly, p, dv)
                    if r > 0.06 * L:
                        q = p + dv * r * 0.88
                        out.append((_bezier(p, p + dv * r * 0.45 + u * r * 0.15, q, 20), 2))
        if tertiary:
            out += _reticulate(o, seed, L)
        return out
    # pinnate families
    style = {"pinnate": "craspedodromous", "brochidodromous": "brochidodromous", "arcuate": "arcuate"}[venation]
    xs_tip = L
    mid = np.c_[np.linspace(0, xs_tip * 0.985, 60), np.zeros(60)]
    out.append((mid, 1))
    ns = secondaries or 7
    for sg, half in ((1, o["right"]), (-1, o["left"])):
        q, total = _resample(half, 400)
        tips = o["tips"]
        own = tips[(tips[:, 1] * sg > 0)] if len(tips) else tips
        curves = []
        if style == "arcuate":
            # secondaries leave the midrib along its lower half and curve up, parallel to the margin
            hx = np.sort(q[:, 0])
            hy = np.abs(q[np.argsort(q[:, 0]), 1])
            for k in range(ns):
                x0 = L * (0.05 + 0.5 * k / max(1, ns - 1))
                xe = min(x0 + 0.5 * L, 0.95 * L)
                ye = 0.72 * float(np.interp(xe, hx, hy))
                xm = x0 + 0.16 * L
                ym = 0.85 * float(np.interp(xm, hx, hy))
                c = _bezier(np.array([x0, 0.0]), np.array([xm, sg * ym * 1.05]), np.array([xe, sg * ye]), 40)
                curves.append(c)
                out.append((c, 2))
            targets = []
        elif style == "craspedodromous" and len(own):
            # one secondary per lobe / per second or third tooth
            own = own[np.argsort(own[:, 0])]
            if o["margin"] not in ("lobed", "pinnatifid", "pinnatisect", "spinose"):
                step = max(1, int(round(len(own) / ns)))
                own = own[step // 2::step]
            targets = list(own)
        else:
            fr = np.linspace(0.12, 0.86, ns)
            idx = (fr * (len(q) - 1)).astype(int)
            targets = [q[i] for i in idx]
        for k, tgt in enumerate(targets):
            tgt = np.asarray(tgt, float)
            span = abs(tgt[1])
            if span < 0.02 * L:
                continue
            ang = math.radians(angle if angle is not None else 55)
            x0 = tgt[0] - span / math.tan(ang) * 0.85
            x0 = float(np.clip(x0, 0.02 * L, 0.9 * L))
            if o["shape"] in ("cordate", "reniform", "sagittate", "hastate") and k == 0:
                x0 = 0.0
            p0 = np.array([x0, 0.0])
            end = tgt if style == "craspedodromous" else p0 + (tgt - p0) * 0.82
            ctrl = p0 + (end - p0) * 0.45 + np.array([-(end - p0)[0] * 0.12, (end - p0)[1] * 0.12])
            c = _bezier(p0, ctrl, end, 40)
            curves.append(c)
            out.append((c, 2))
        if style == "brochidodromous":
            for a, b in zip(curves[:-1], curves[1:]):
                pa, pb = a[-1], b[int(len(b) * 0.82)]
                mid_ = (pa + pb) / 2
                n_ = np.array([0, sg]) * np.hypot(*(pb - pa)) * 0.35
                out.append((_bezier(pa, mid_ + n_, pb, 20), 2))
        if tertiary == "percurrent":
            for a, b in zip(curves[:-1], curves[1:]):
                for f in (0.3, 0.5, 0.7):
                    pa, pb = a[int(f * (len(a) - 1))], b[int(f * 0.92 * (len(b) - 1))]
                    out.append((_bezier(pa, (pa + pb) / 2 + np.array([0.01 * L, 0]), pb, 8), 3))
    if tertiary == "reticulate":
        out += _reticulate(o, seed, L)
    return out


def _reticulate(o, seed, L):
    """Fine reticulate (areolate) venation: edges of a Voronoi diagram of random points in the blade."""
    from scipy.spatial import Voronoi

    rng = np.random.default_rng(seed + 11)
    poly = Path(o["outline"])
    lo, hi = o["outline"].min(axis=0), o["outline"].max(axis=0)
    n = int(70 * (hi - lo).prod() / (0.18 * L) ** 2 / 10) + 30
    pts = lo + rng.uniform(0, 1, (n * 3, 2)) * (hi - lo)
    pts = pts[poly.contains_points(pts)][:n]
    if len(pts) < 5:
        return []
    vor = Voronoi(pts)
    out = []
    for (i, j) in vor.ridge_vertices:
        if i >= 0 and j >= 0:
            out.append((vor.vertices[[i, j]], 4))
    return out


def leaf(ax, base, length, angle=90.0, shape="elliptic", width=None, apex=None, base_type=None, margin="entire",
         venation="pinnate", secondaries=None, tertiary=None, lobes=None, teeth=None, depth=None, petiole=None,
         stipules=False, token="leaf", vein_angle=None, mirror=False, seed=0, zorder=6, lw=None):
    """A simple leaf: petiole (from ``base``) and blade pointing along ``angle``; see ``blade_outline``.

    venation  "pinnate" (craspedodromous: secondaries end at the margin), "brochidodromous" (looping),
              "arcuate" (secondaries curving towards the apex), "palmate", "parallel", "dichotomous", "none"
    tertiary  None, "percurrent" (ladder-like cross veins) or "reticulate" (areoles)
    petiole   length (default 0.25 × blade length; 0 = sessile); ``stipules`` adds a pair at its base
    Returns anchors: base, attachment (blade base), apex, blade, margin, midrib, secondary, tertiary,
    petiole, stipule, lobe, sinus, tooth; and ``outline`` (canvas points) and ``patch``.
    """
    o = blade_outline(shape, length, width, apex, base_type, margin, lobes, teeth, depth)
    pet = 0.25 * length if petiole is None else petiole
    if mirror:
        for k in ("outline", "right", "left", "tips", "sinuses"):
            o[k] = o[k] * [1, -1]
    ang = angle
    attach = np.asarray(base, float) + pet * np.array([math.cos(math.radians(ang)), math.sin(math.radians(ang))])

    def W(p):
        return _place(p, attach, ang)
    s = _lw(length, 1.0) if lw is None else lw
    fc, ec = _fill(token), _edge(token)
    outline = W(o["outline"])
    patch = PathPatch(Path(np.vstack([outline, outline[:1]]), closed=True), facecolor=fc, edgecolor=ec,
                      lw=LINE * 0.75 * s, joinstyle="round", zorder=zorder)
    ax.add_patch(patch)
    anchors = dict(base=np.asarray(base, float), attachment=attach, outline=outline, patch=patch)
    if pet > 0:
        ax.plot([base[0], attach[0]], [base[1], attach[1]], color=ec, lw=2.0 * s, solid_capstyle="round", zorder=zorder - 0.5)
        anchors["petiole"] = (np.asarray(base, float) + attach) / 2
    veins = _vein_lines(o, venation, secondaries, tertiary, vein_angle, seed)
    widths = {1: 1.05 * s, 2: 0.6 * s, 3: 0.35 * s, 4: 0.28 * s}
    vc = {1: ec, 2: ec, 3: P.mix(ec, fc, 0.3), 4: P.mix(ec, fc, 0.45)}
    groups = {}
    for pts, order in veins:
        groups.setdefault(order, []).append(W(pts))
    for order, segs in groups.items():
        lc = LineCollection(segs, colors=vc[order], linewidths=widths[order], capstyle="round", zorder=zorder + 0.2 + 0.01 * (5 - order))
        lc.set_clip_path(patch)
        ax.add_collection(lc)
    L = length
    anchors["apex"] = W(o["right"][-1:])[0] if venation != "dichotomous" else W([[L * 0.86, 0]])[0]
    anchors["blade"] = W([[0.55 * L, 0.18 * o["width"]]])[0]
    r = o["right"]
    anchors["margin"] = W(r[np.argmax(np.abs(r[:, 1]))][None])[0]
    anchors["midrib"] = W([[0.42 * L, 0]])[0]
    anchors["frame"] = (attach, ang, L, o["width"], -1 if mirror else 1)
    anchors["veins"] = groups
    centre = W([[0.5 * L, 0.2 * o["width"]]])[0]
    for order, key in ((2, "secondary"), (3, "tertiary"), (4, "tertiary")):
        if order in groups and key not in anchors:  # the vein point nearest the middle of the blade's right half
            pts_ = np.vstack([g[len(g) // 2][None] for g in groups[order]])
            anchors[key] = pts_[np.argmin(np.hypot(*(pts_ - centre).T))]
    if len(o["tips"]):
        t = o["tips"][np.argsort(o["tips"][:, 0])]
        anchors["tooth" if margin not in ("lobed", "pinnatifid", "pinnatisect") else "lobe"] = W(t[len(t) // 2][None])[0]
        anchors["tips"] = W(t)
    if len(o["sinuses"]):
        anchors["sinus"] = W(o["sinuses"][len(o["sinuses"]) // 2][None])[0]
    if stipules:
        st = []
        for sg in (1, -1):
            a2 = ang + 30 * sg
            sl = max(0.1 * length, 0.1)
            so = blade_outline("ovate", sl, sl * 0.55, "acute", "rounded")
            pts = _place(so["outline"], base, a2)
            ax.add_patch(PathPatch(Path(np.vstack([pts, pts[:1]]), closed=True), facecolor=fc, edgecolor=ec, lw=LINE * 0.6 * s,
                                   zorder=zorder - 0.3))
            st.append(_place([[sl * 0.5, 0]], base, a2)[0])
        anchors["stipule"] = st[0]
        anchors["stipules"] = st
    return anchors


def leaf_point(a, u, v):
    """A point of a drawn leaf in its own frame: u along the midrib (0 base .. 1 apex), v across
    (-1 .. 1 of the half-width; positive to the left of the midrib looking towards the apex)."""
    attach, ang, L, W, sg = a["frame"]
    return _place([[u * L, v * W / 2 * sg]], attach, ang)[0]


def vein_point(a, order, u, v):
    """The point on a vein of ``order`` (1 midrib, 2 secondary, 3 tertiary, 4 areoles) of a drawn leaf
    nearest to ``leaf_point(a, u, v)``."""
    q = leaf_point(a, u, v)
    pts = np.vstack(a["veins"][order])
    return pts[np.argmin(np.hypot(*(pts - q).T))]


# ---------------------------------------------------------------------------- compound leaves


def compound_leaf(ax, base, length, angle=90.0, kind="imparipinnate", leaflets=4, leaflet=None, petiole=None,
                  pinnae=3, stipules=False, token="leaf", zorder=6):
    """A compound leaf. ``kind``: "paripinnate" (even-pinnate, no terminal leaflet), "imparipinnate"
    (odd-pinnate), "bipinnate" (pinnae bearing pinnules), "palmate" (digitate: leaflets from the petiole
    tip), "trifoliate" (pinnately trifoliolate: the terminal leaflet on a longer petiolule).

    ``leaflets``: pairs of leaflets (pinnate) or leaflets per pinna side (bipinnate) or number of leaflets
    (palmate); ``pinnae``: pairs of pinnae (bipinnate); ``leaflet``: keyword overrides for ``leaf``.
    Returns anchors: base, petiole, rachis, leaflet, terminal, petiolule, pinna, rachilla, pinnule,
    stipule, leaflets (list of leaflet anchors).
    """
    lf = dict(shape="elliptic", venation="pinnate", secondaries=4, apex="acute", base_type="cuneate")
    lf.update(leaflet or {})
    s = _lw(length, 1.0, ref=5.0)
    ec = _edge(token)
    a = math.radians(angle)
    u = np.array([math.cos(a), math.sin(a)])
    b = np.asarray(base, float)
    pet = (0.22 if kind != "palmate" else 0.42) * length if petiole is None else petiole
    out = dict(base=b, leaflets=[])
    if stipules:
        for sg in (1, -1):
            sa = leaf(ax, b, 0.12 * length, angle + 35 * sg, shape="ovate", petiole=0, venation="none", token=token,
                      zorder=zorder - 0.4)
            out.setdefault("stipules", []).append(sa["blade"])
        out["stipule"] = out["stipules"][0]

    def line(p, q, w):
        ax.plot([p[0], q[0]], [p[1], q[1]], color=ec, lw=w, solid_capstyle="round", zorder=zorder + 0.5)

    top = b + u * pet
    line(b, top, 2.0 * s)
    out["petiole"] = b + u * pet * 0.5
    if kind == "palmate":
        n = leaflets if leaflets >= 3 else 5
        ll = (length - pet) * 0.95
        spread = 230 if n >= 5 else 150
        for k in range(n):
            f = (k - (n - 1) / 2) / max(1, (n - 1) / 2)
            ang = angle + f * spread / 2
            sz = ll * 0.8 * (1 - 0.4 * abs(f) ** 1.5)
            la = leaf(ax, top, sz, ang, petiole=0.06 * sz, token=token, zorder=zorder, **lf)
            out["leaflets"].append(la)
        out["leaflet"] = out["leaflets"][n // 2 + 1 if n > 2 else 0]["blade"]
        out["terminal"] = out["leaflets"][n // 2]["blade"]
        out["petiolule"] = out["leaflets"][n // 2]["petiole"]
        return out
    if kind == "trifoliate":
        ll = (length - pet) * 0.62
        rach = top + u * ll * 0.32
        line(top, rach, 1.4 * s)
        out["rachis"] = (top + rach) / 2
        for sg in (1, -1):
            la = leaf(ax, top, ll * 0.85, angle + 62 * sg, petiole=0.05 * ll, token=token, zorder=zorder, **lf)
            out["leaflets"].append(la)
        la = leaf(ax, rach, ll, angle, petiole=0.07 * ll, token=token, zorder=zorder, **lf)
        out["leaflets"].append(la)
        out["terminal"], out["leaflet"] = la["blade"], out["leaflets"][0]["blade"]
        out["petiolule"] = la["petiole"]
        return out
    if kind == "bipinnate":
        rl = length - pet
        tip = top + u * rl * 0.92
        line(top, tip, 1.5 * s)
        out["rachis"] = top + u * rl * 0.12
        for k in range(pinnae):
            f = (k + 0.5) / pinnae
            p = top + u * rl * (0.12 + 0.8 * f) * 0.92
            pl = rl * 0.5 * (1 - 0.45 * f)
            for sg in (1, -1):
                pa = angle + 58 * sg
                v = np.array([math.cos(math.radians(pa)), math.sin(math.radians(pa))])
                q = p + v * pl
                line(p, q, 1.0 * s)
                if k == 0 and sg == 1:
                    out["rachilla"] = p + v * pl * 0.5
                    out["pinna"] = p + v * pl * 0.75
                for j in range(leaflets):
                    g = (j + 0.6) / (leaflets + 0.4)
                    pp = p + v * pl * g
                    sz = pl * 0.3 * (1 - 0.35 * g)
                    for sg2 in (1, -1):
                        la = leaf(ax, pp, sz, pa + 62 * sg2, petiole=0, token=token, zorder=zorder,
                                  **{**lf, "venation": "none" if sz < 0.5 else lf["venation"], "secondaries": 3})
                        if k == 0 and sg == 1 and j == 1 and sg2 == 1:
                            out["pinnule"] = la["blade"]
                            out["leaflets"].append(la)
                la = leaf(ax, p + v * pl, pl * 0.22, pa, petiole=0, token=token, zorder=zorder,
                          **{**lf, "venation": "none"})
        out["leaflet"] = out.get("pinnule")
        return out
    # pinnate
    n = leaflets
    rl = length - pet
    ll = rl / (n + 0.6) * 1.55
    last = top + u * rl * (n - 0.3) / (n + 0.6) if kind == "paripinnate" else top + u * rl * (n - 0.15) / (n + 0.6)
    line(top, last + (u * 0.08 * ll if kind == "paripinnate" else 0), 1.5 * s)
    out["rachis"] = top + u * rl * 0.5 / (n + 0.6)
    for k in range(n):
        p = top + u * rl * (k + 0.5) / (n + 0.6)
        for sg in (1, -1):
            la = leaf(ax, p, ll * (1 - 0.12 * k / max(1, n - 1)), angle + 62 * sg, petiole=0.06 * ll, token=token,
                      zorder=zorder, mirror=sg < 0, **lf)
            out["leaflets"].append(la)
    out["leaflet"] = out["leaflets"][2 if n > 1 else 0]["blade"]
    out["petiolule"] = out["leaflets"][0]["petiole"]
    if kind == "imparipinnate":
        la = leaf(ax, last, ll * 0.95, angle, petiole=0.08 * ll, token=token, zorder=zorder, **lf)
        out["leaflets"].append(la)
        out["terminal"] = la["blade"]
    else:
        out["rachis_tip"] = last + u * 0.08 * ll
    return out


# ---------------------------------------------------------------------------- leaves on a stem


ARRANGEMENT = {"alternate": (1, 180.0), "distichous": (1, 180.0), "spiral": (1, GOLDEN_ANGLE), "opposite": (2, 0.0),
               "decussate": (2, 90.0), "whorled": (3, 60.0)}


def shoot(ax, base, height, arrangement="alternate", nodes=4, leaf_length=None, leaf_kw=None, elevation=38.0,
          divergence=None, per_node=None, buds=True, view=None, token="leaf", stem_token="stem", zorder=6):
    """A leafy shoot in side view: an upright stem with nodes, internodes and leaves.

    arrangement  "alternate" (distichous: one leaf per node, successive leaves 180° apart), "spiral"
                 (one leaf per node, golden-angle divergence), "opposite" (two per node, all pairs in one
                 plane), "decussate" (pairs, successive pairs at 90°), "whorled" (three or more per node)
    Leaves are placed around the stem in 3D (azimuth from the divergence angle, ``elevation`` above
    horizontal) and projected: leaves facing the viewer are foreshortened, those behind the stem are
    drawn behind it and faded; ``view`` (default: 0 for leaves in the picture plane, else 28°) turns the
    shoot about its axis so that no leaf is seen end-on. Returns anchors: node, internode, leaf, petiole,
    axillary_bud, apical_bud,
    stem, nodes (list).
    """
    per, div = ARRANGEMENT[arrangement]
    if view is None:  # leaves in the picture plane need no turn; otherwise avoid end-on leaves
        view = 0.0 if arrangement in ("alternate", "distichous", "opposite") else 28.0
    per = per_node or per
    div = divergence if divergence is not None else div
    b = np.asarray(base, float)
    ll = leaf_length or height * 0.32
    s = _lw(height, 1.0, ref=5.0)
    ec = _edge(stem_token)
    y_nodes = [b[1] + height * (0.16 + 0.74 * (k / max(1, nodes - 1)) ** 0.92) for k in range(nodes)]
    top = b + [0, height]
    ax.plot([b[0], top[0]], [b[1], top[1] - 0.05], color=ec, lw=3.0 * s, solid_capstyle="round", zorder=zorder + 1)
    ax.plot([b[0], top[0]], [b[1], top[1] - 0.05], color=_fill(stem_token), lw=1.6 * s, solid_capstyle="round",
            zorder=zorder + 1.1)
    out = dict(base=b, stem=b + [0, height * 0.08], nodes=[], apical_bud=top)
    # apical bud
    ax.add_patch(Ellipse(top, 0.12 * ll + 0.05, 0.3 * ll + 0.1, facecolor=_fill("bud"), edgecolor=_edge("bud"), lw=0.8 * s,
                         zorder=zorder + 1.3))
    lk = dict(shape="elliptic", venation="pinnate", secondaries=4, petiole=0.18 * ll)
    lk.update(leaf_kw or {})
    az0 = 0.0
    for k, y in enumerate(y_nodes):
        node = np.array([b[0], y])
        out["nodes"].append(node)
        ax.plot([b[0] - 0.06 * s * 1.4, b[0] + 0.06 * s * 1.4], [y, y], color=ec, lw=1.0 * s, zorder=zorder + 1.2)
        for j in range(per):
            az = az0 + k * div + j * 360.0 / per
            if arrangement == "whorled":
                az = k * div + j * 360.0 / per + 90
            azr = math.radians(az + view)
            # 3D direction: x to the right, depth towards the viewer, z up
            ce, se = math.cos(math.radians(elevation)), math.sin(math.radians(elevation))
            dx, dy = math.cos(azr) * ce, math.sin(azr) * ce
            front = dy  # > 0 towards the viewer
            proj = np.array([dx, se])
            plen = np.hypot(*proj)
            ang = math.degrees(math.atan2(proj[1], proj[0]))
            lt = ll * (0.35 + 0.65 * plen) * (1 - 0.15 * k / max(1, nodes - 1))
            wid = SHAPES[lk["shape"]][1] * ll
            if abs(dx) < 0.35:  # leaf seen nearly end-on: draw it narrow and short
                wid *= 0.9
            z = zorder + (2 if front > 0.05 else -1)
            tk = token
            la = leaf(ax, node, lt, ang, width=wid, token=tk, zorder=z, petiole=lk.get("petiole", 0.18 * ll) * (0.4 + 0.6 * plen),
                      **{kk: v for kk, v in lk.items() if kk not in ("petiole",)})
            if front < -0.05:
                la["patch"].set_alpha(0.55)
            if k == 1 and "leaf" not in out and front >= -0.05:
                out["leaf"], out["petiole"] = la["blade"], la.get("petiole")
            if buds and front >= -0.05:
                v = np.array([math.cos(math.radians(ang)), math.sin(math.radians(ang))])
                bp = node + (v + np.array([0, 1.0])) / np.hypot(*(v + np.array([0, 1.0]))) * 0.1 * ll + [0, 0.04]
                ax.add_patch(Ellipse(bp, 0.08 * ll + 0.03, 0.15 * ll + 0.05, angle=math.degrees(math.atan2(v[1] + 1, v[0])) - 90,
                                     facecolor=_fill("bud"), edgecolor=_edge("bud"), lw=0.6 * s, zorder=zorder + 1.25))
                if "axillary_bud" not in out and k >= 1:
                    out["axillary_bud"] = bp
    out.setdefault("leaf", out["nodes"][0])
    out["node"] = out["nodes"][1] if nodes > 1 else out["nodes"][0]
    out["internode"] = (out["nodes"][1] + out["nodes"][2]) / 2 if nodes > 2 else b + [0, height * 0.3]
    return out


def phyllotaxis(ax, center, radius, n=55, divergence=GOLDEN_ANGLE, parastichies=(8, 13), numbers=0, angle_arc=True,
                tokens=("dna", "rna"), token="leaf", zorder=6):
    """Spiral phyllotaxis seen from above (Vogel's model: primordium k at angle k × divergence and radius
    ∝ √k, youngest in the centre). ``parastichies`` = pairs (m, n) of Fibonacci numbers: lines joining
    primordia k and k + m (and k + n) show the two families of contact spirals. ``numbers``: label the
    youngest primordia 1..numbers; ``angle_arc`` marks the divergence angle between primordia 1 and 2.
    Returns anchors: center, primordia (array, index 0 = youngest), arc (label point of the angle).
    """
    c = np.asarray(center, float)
    k = np.arange(1, n + 1)
    r = radius * np.sqrt(k / n) * 0.93
    th = np.radians(90 - (k - 1) * divergence)
    pts = c + np.c_[r * np.cos(th), r * np.sin(th)]
    size = radius * 0.62 / math.sqrt(n) * (0.55 + 0.6 * np.sqrt(k / n))
    out = dict(center=c, primordia=pts)
    for m, tkn in zip(parastichies or (), tokens):
        segs = [pts[[i, i + m]] for i in range(n - m)]
        ax.add_collection(LineCollection(segs, colors=P.edge(tkn) if not P.is_dark() else P.fill(tkn), linewidths=1.0,
                                         zorder=zorder - 1, alpha=0.9))
    for i in range(n - 1, -1, -1):
        ax.add_patch(Circle(pts[i], size[i], facecolor=_fill(token), edgecolor=_edge(token), lw=0.7, zorder=zorder))
    ax.add_patch(Circle(c, size[0] * 0.7, facecolor=_fill("bud"), edgecolor=_edge("bud"), lw=0.7, zorder=zorder + 0.5))
    for i in range(min(numbers, n)):
        label(ax, pts[i], str(i + 1), size="tiny", color=P.on_fill(), zorder=zorder + 2)
    if angle_arc:
        a0, a1 = 90.0, 90.0 - divergence
        rr = radius * 0.32
        aa = np.radians(np.linspace(a0, a1, 50))
        ax.plot(c[0] + rr * np.cos(aa), c[1] + rr * np.sin(aa), color=P.ink(), lw=1.1, zorder=zorder + 3)
        for i in (0, 1):
            p = pts[i]
            d = (p - c) / (np.hypot(*(p - c)) + 1e-9)
            ax.plot([c[0], c[0] + d[0] * rr * 1.25], [c[1], c[1] + d[1] * rr * 1.25], color=P.ink(), lw=0.9, ls=(0, (3, 2)),
                    zorder=zorder + 3)
        am = math.radians((a0 + a1) / 2)
        out["arc"] = c + rr * np.array([math.cos(am), math.sin(am)])
    return out


# ============================================================================ inflorescences


def flower(ax, xy, r, stage="open", token="flower", angle=90.0, zorder=8):
    """A small flower glyph for inflorescence diagrams: "open" (five petals around the centre), "bud"
    (a closed ovoid bud pointing along ``angle``) or "floret" (a minute disc floret)."""
    xy = np.asarray(xy, float)
    if stage == "bud":
        ax.add_patch(Ellipse(xy, r * 1.15, r * 1.7, angle=angle - 90, facecolor=_fill("bud"), edgecolor=_edge("bud"),
                             lw=0.7, zorder=zorder))
        return xy
    if stage == "floret":
        ax.add_patch(Circle(xy, r, facecolor=_fill("floret"), edgecolor=_edge("floret"), lw=0.5, zorder=zorder))
        return xy
    for k in range(5):
        a = math.radians(angle + k * 72)
        ax.add_patch(Circle(xy + 0.55 * r * np.array([math.cos(a), math.sin(a)]), 0.5 * r, facecolor=_fill(token),
                            edgecolor=_edge(token), lw=0.6, zorder=zorder))
    ax.add_patch(Circle(xy, 0.3 * r, facecolor=_fill("floret"), edgecolor=_edge("floret"), lw=0.5, zorder=zorder + 0.1))
    return xy


def _bract(ax, at, angle, size, zorder=6):
    o = blade_outline("lanceolate", size, size * 0.38, "acute", "rounded")
    pts = _place(o["outline"], at, angle)
    ax.add_patch(PathPatch(Path(np.vstack([pts, pts[:1]]), closed=True), facecolor=_fill("bract"), edgecolor=_edge("bract"),
                           lw=0.6, zorder=zorder))
    return _place([[size * 0.5, 0]], at, angle)[0]


INFLORESCENCES = ("raceme", "spike", "catkin", "corymb", "umbel", "compound umbel", "panicle", "spadix", "capitulum",
                  "scorpioid cyme", "helicoid cyme", "dichasium")


def inflorescence(ax, base, height, kind="raceme", flowers=None, bracts=True, zorder=6):
    """An inflorescence in side view, in the schematic style of botany manuals. Flower size shows the
    order of opening: older flowers are larger; buds sit where the youngest flowers are (the apex of
    racemose, indeterminate types; the periphery of cymose, determinate types).

    kind  "raceme", "spike", "catkin" (ament: a pendulous spike of reduced unisexual flowers among
          scale-like bracts), "corymb", "umbel", "compound umbel", "panicle", "spadix" (with its
          spathe), "capitulum" (head, with involucre), "scorpioid cyme" and "helicoid cyme"
          (monochasia: one branch per node, alternating sides or always the same side), "dichasium"
          (dichasial cyme: two branches below each terminal flower)
    Returns anchors: peduncle, rachis (main axis), pedicel, flower, bud, bract, terminal, and per type
    ray / umbellet / involucre / involucel / spathe / spadix / phyllary / ray_floret / disc_floret /
    receptacle / branch; ``flowers``: list of flower centres.
    """
    b = np.asarray(base, float)
    H = height
    s = _lw(H, 1.0, ref=4.0)
    ec = _edge("stem")
    out = dict(base=b, flowers=[])
    r0 = 0.052 * H

    def seg(p, q, w=1.6, z=zorder):
        ax.plot([p[0], q[0]], [p[1], q[1]], color=ec, lw=w * s, solid_capstyle="round", zorder=z)

    def curve(pts, w=1.6, z=zorder):
        pts = np.asarray(pts)
        ax.plot(pts[:, 0], pts[:, 1], color=ec, lw=w * s, solid_capstyle="round", zorder=z)

    def fl(p, f, ang=90, kind_=None):
        """flower at p with age fraction f (0 oldest .. 1 youngest)"""
        st = kind_ or ("bud" if f > 0.78 else "open")
        r = r0 * (1.05 - 0.45 * f) if st == "open" else r0 * 0.55
        flower(ax, p, r, stage=st, angle=ang, zorder=zorder + 2)
        out["flowers"].append(np.asarray(p, float))
        if st == "bud":
            out.setdefault("bud", np.asarray(p, float))
        else:
            out.setdefault("flower", np.asarray(p, float))
        return r

    if kind in ("raceme", "spike", "panicle"):
        n = flowers or {"raceme": 7, "spike": 12, "panicle": 6}[kind]
        y0 = 0.3 if kind != "spike" else 0.25
        top = b + [0, H * 0.97]
        seg(b, top, 1.8)
        out["peduncle"] = b + [0, H * y0 * 0.5]
        out["rachis"] = b + [0, H * 0.62]
        for k in range(n):
            f = k / max(1, n - 1)
            y = H * (y0 + (0.9 - y0) * f)
            p = b + [0, y]
            side = 1 if k % 2 == 0 else -1
            if kind == "spike":
                q = p + [side * r0 * 0.75, 0.15 * r0]
                fl(q, f * 0.95)
                continue
            if kind == "raceme":
                a = math.radians(90 - side * 52)
                pl = H * 0.17 * (1 - 0.45 * f)
                q = p + pl * np.array([math.cos(a), math.sin(a)])
                seg(p, q, 0.9)
                if k == 1:
                    out["pedicel"] = (p + q) / 2
                if bracts:
                    bp = _bract(ax, p, math.degrees(a) - side * 28, H * 0.07, zorder=zorder - 0.5)
                    out.setdefault("bract", bp)
                fl(q, f * 0.95, ang=math.degrees(a))
                continue
            # panicle: branches are racemes, longer below (pyramidal); the lower ones branch again
            a = math.radians(90 - side * 50)
            bl = H * (0.36 - 0.26 * f)
            u = np.array([math.cos(a), math.sin(a)])
            q = p + bl * u
            seg(p, q, 1.2)
            if k == 0:
                out["branch"] = p + 0.45 * bl * u
            m = 3 if f < 0.5 else 2
            for j in range(m):
                g = (j + 1) / (m + 0.6)
                pp = p + bl * g * u
                aa = math.radians(90 - side * 38 * (1 if j % 2 == 0 else -0.5))
                pl = H * 0.08 * (1 - 0.3 * g)
                qq = pp + pl * np.array([math.cos(aa), math.sin(aa)])
                seg(pp, qq, 0.8)
                if k == 0 and j == 0:
                    out["pedicel"] = (pp + qq) / 2
                fl(qq, min(0.95, f * 0.7 + g * 0.3), ang=math.degrees(aa))
            fl(q, min(0.95, f * 0.7 + 0.35), ang=math.degrees(a))
        fl(top, 1.0)
        out["terminal"] = top
        return out
    if kind == "catkin":
        twig0, twig1 = b + [-0.25 * H, H], b + [0.3 * H, H * 1.02]
        seg(twig0, twig1, 2.4)
        att = b + [0.05 * H, H * 1.01]
        t = np.linspace(0, 1, 30)
        ax_pts = np.c_[att[0] + 0.12 * H * np.sin(t * 1.4), att[1] - 0.82 * H * t]
        curve(ax_pts, 1.2, z=zorder - 1)
        out["peduncle"] = ax_pts[2]
        n = flowers or 22
        sc = []
        for k in range(n):  # imbricate scale-like bracts, each with a minute flower in its axil
            g = 0.05 + 0.93 * k / (n - 1)
            i = int(g * 29)
            p = ax_pts[i]
            w = 0.12 * H * (1 - 0.45 * abs(g - 0.35) ** 1.2)
            for side in ((-1, 1) if k % 2 == 0 else (0,)):
                q = p + [side * w * 0.42, -0.01 * H]
                ang = -90 + side * 40
                tri = _place([[0, -0.5], [1.0, -0.25], [1.15, 0], [1.0, 0.25], [0, 0.5]], (0, 0), 0) * [w * 0.62, w * 0.62]
                pts = _place(_chaikin(tri, 2), q - 0.25 * w * np.array([math.cos(math.radians(ang)), math.sin(math.radians(ang))]), ang)
                ax.add_patch(Polygon(pts, closed=True, facecolor=_fill("bract"), edgecolor=_edge("bract"), lw=0.55,
                                     zorder=zorder + k * 0.01 + (0.005 if side == 0 else 0)))
                ax.add_patch(Circle(q + [side * w * 0.22, -w * 0.34], w * 0.11, facecolor=_fill("floret"),
                                    edgecolor=_edge("floret"), lw=0.4, zorder=zorder + k * 0.01 + 0.006))
                sc.append(q)
        out["bract"] = sc[len(sc) // 2]
        out["flower"] = sc[len(sc) // 2 + 1] + [0.02 * H, -0.03 * H]
        out["rachis"] = ax_pts[15]
        out["flowers"] = sc
        return out
    if kind == "corymb":
        n = flowers or 7
        topy = H * 0.9
        ax_top = b + [0, H * 0.74]
        seg(b, ax_top, 1.8)
        out["peduncle"] = b + [0, H * 0.18]
        out["rachis"] = b + [0, H * 0.6]
        for k in range(n):
            f = k / max(1, n - 1)
            y = H * (0.36 + 0.38 * f)
            p = b + [0, y]
            side = 1 if k % 2 == 0 else -1
            x = side * H * 0.42 * (1 - f) ** 0.9 + side * 0.02 * H
            q = b + [x, topy - 0.03 * H * (1 - f)]
            ctrl = p + [x * 0.2, (q[1] - p[1]) * 0.6]
            curve(_bezier(p, ctrl, q, 20), 0.9)
            if k == 0:
                out["pedicel"] = _bezier(p, ctrl, q, 20)[10]
            if bracts:
                bp = _bract(ax, p, 90 - side * 70, H * 0.06, zorder=zorder - 0.5)
                out.setdefault("bract", bp)
            fl(q, f * 0.95)
        fl(ax_top + [0, 0.12 * H], 1.0)
        seg(ax_top, ax_top + [0, 0.12 * H], 0.9)
        out["terminal"] = ax_top + [0, 0.12 * H]
        return out
    if kind in ("umbel", "compound umbel"):
        node = b + [0, H * (0.5 if kind == "umbel" else 0.42)]
        seg(b, node, 1.8)
        out["peduncle"] = (b + node) / 2

        def umbel(c, R, n, spread, level):
            pts = []
            for k in range(n):
                f = (k - (n - 1) / 2) / ((n - 1) / 2)
                a = math.radians(90 - f * spread / 2)
                rr = R * (1 - 0.1 * abs(f))
                q = c + rr * np.array([math.cos(a), math.sin(a) * 1.0])
                seg(c, q, 1.1 if level == 0 else 0.8)
                pts.append(q)
            if bracts:  # involucre (involucel) of bracts at the base of the rays
                for sg in (-1, 1):
                    for d in (25, 60):
                        _bract(ax, c, 90 - sg * (90 + d), R * (0.2 if level == 0 else 0.3), zorder=zorder - 0.5)
            return pts
        if kind == "umbel":
            pts = umbel(node, H * 0.4, flowers or 9, 130, 0)
            for k, q in enumerate(pts):
                f = abs(k - (len(pts) - 1) / 2) / ((len(pts) - 1) / 2)
                fl(q, 0.85 - 0.75 * f)  # outer flowers open first (centripetal)
            out["pedicel"] = (node + pts[2]) / 2
            out["involucre"] = node + [0.06 * H, -0.04 * H]
            return out
        rays = umbel(node, H * 0.33, flowers or 5, 120, 0)
        out["ray"] = (node + rays[1]) / 2
        out["involucre"] = node + [0.06 * H, -0.04 * H]
        for j, c in enumerate(rays):
            pts = umbel(c, H * 0.12, 5, 120, 1)
            for k, q in enumerate(pts):
                f = abs(k - 2) / 2
                r = r0 * 0.55
                flower(ax, q, r, stage="open" if f > 0.4 else "bud", zorder=zorder + 2)
                out["flowers"].append(q)
            if j == len(rays) - 2:
                out["umbellet"] = c + [0, H * 0.09]
                out["involucel"] = c + [0.035 * H, -0.03 * H]
                out["pedicel"] = (c + pts[3]) / 2
                out["flower"] = pts[4]
        return out
    if kind == "spadix":
        seg(b, b + [0, 0.25 * H], 2.2)
        out["peduncle"] = b + [0, 0.12 * H]
        sp = leaf(ax, b + [0, 0.18 * H], 0.8 * H, 90, shape="ovate", width=0.48 * H, apex="acuminate", base_type="rounded",
                  venation="parallel", secondaries=5, petiole=0, token="spathe", zorder=zorder - 1)
        ol = sp["outline"]
        out["spathe"] = ol[np.argmax(ol[:, 0])]
        c = b + [0, 0.5 * H]
        L, Wd = 0.5 * H, 0.1 * H
        ax.add_patch(Ellipse(c, Wd, L, facecolor=_fill("floret"), edgecolor=_edge("floret"), lw=0.9 * s, zorder=zorder + 1))
        for i in range(14):
            yy = c[1] - L * 0.44 + L * 0.88 * i / 13
            hw = Wd / 2 * math.sqrt(max(0, 1 - ((yy - c[1]) / (L / 2)) ** 2))
            for j in range(-2, 3):
                xx = c[0] + (j + (0.5 if i % 2 else 0)) * Wd * 0.2
                if abs(xx - c[0]) < hw * 0.85:
                    ax.add_patch(Circle((xx, yy), Wd * 0.07, facecolor=_edge("floret"), edgecolor="none", zorder=zorder + 1.1))
        out["spadix"] = c + [Wd * 0.3, 0.1 * H]
        out["flower"] = c + [0, -0.15 * H]
        return out
    if kind == "capitulum":
        # an oblique view from above: involucre below the rim, ray florets around the disc
        top = b + [0, 0.62 * H]
        seg(b, top, 1.8)
        out["peduncle"] = b + [0, 0.3 * H]
        R, sq = 0.17 * H, 0.38
        c = top + [0, 0.07 * H]
        for row, (dy, n, sz) in enumerate(((-0.02, 9, 0.1), (0.01, 8, 0.085))):
            for k in range(n):
                f = (k - (n - 1) / 2) / ((n - 1) / 2)
                p = top + [f * R * 0.85, dy * H]
                _bract(ax, p, 90 - f * 40, sz * H, zorder=zorder + 0.5 + row * 0.1)
        out["phyllary"] = top + [R * 0.75, 0.0]
        out["involucre"] = out["phyllary"]
        n_r = 18
        for front in (False, True):
            for k in range(n_r):
                phi = 2 * math.pi * (k + 0.25) / n_r
                if (math.sin(phi) < 0) != front:
                    continue
                d = np.array([math.cos(phi), math.sin(phi) * sq])
                p0 = c + d * R * 0.85
                tip = c + d * 0.47 * H
                mid = (p0 + tip) / 2
                ln = np.hypot(*(tip - p0))
                ang = math.degrees(math.atan2(*(tip - p0)[::-1]))
                wd = 0.065 * H * (0.55 + 0.45 * abs(math.cos(phi)) ** 0.5) * (1 if abs(math.cos(phi)) > 0.3 else 0.85)
                ax.add_patch(Ellipse(mid, ln, wd * (sq + (1 - sq) * abs(math.cos(phi))), angle=ang, facecolor=_fill("ray_floret"),
                                     edgecolor=_edge("ray_floret"), lw=0.6, zorder=zorder + (4 if front else 1)))
                if front and math.cos(phi) > 0.3 and "ray_floret" not in out:
                    out["ray_floret"] = tip * 0.7 + mid * 0.3
            if not front:
                ax.add_patch(Ellipse(c, 2 * R, 2 * R * sq, facecolor=_fill("floret"), edgecolor=_edge("floret"), lw=0.8 * s,
                                     zorder=zorder + 2))
                for rr in (0.25, 0.5, 0.75):
                    m = int(6 + 18 * rr)
                    for q in range(m):
                        t = 2 * math.pi * q / m + rr
                        ax.add_patch(Circle(c + [R * rr * math.cos(t), R * rr * sq * math.sin(t)], 0.011 * H,
                                            facecolor=_edge("floret"), edgecolor="none", zorder=zorder + 2.1))
        out["disc_floret"] = c + [0.3 * R, 0.1 * R * sq]
        out["receptacle"] = top + [0, 0.02 * H]
        out["flower"] = out["disc_floret"]
        return out
    if kind in ("scorpioid cyme", "helicoid cyme"):
        n = flowers or 6
        p = b
        a = 90.0
        l0 = 0.45 * H
        prev = None
        for k in range(n):
            if k == 0:
                start, ang, ln = b, 90.0, l0
            else:
                start = prev[0] + (prev[1] - prev[0]) * 0.8  # from the axil of a bract below the last flower
                if kind == "scorpioid cyme":
                    ang = 90 + (-1) ** k * 42
                else:
                    ang = 90 - 30 * k
                ln = l0 * 0.5 * 0.86 ** k
            u = np.array([math.cos(math.radians(ang)), math.sin(math.radians(ang))])
            end = start + u * ln
            seg(start, end, 1.6 if k == 0 else 1.2)
            if k > 0 and bracts:
                _bract(ax, start, ang + (-1) ** k * 40 if kind == "scorpioid cyme" else ang + 50, 0.06 * H,
                       zorder=zorder - 0.5)
                out.setdefault("bract", start)
            fl(end, min(0.95, k / (n - 1)), ang=ang)
            if k == 0:
                out["terminal"] = end
            prev = (start, end)
        out["peduncle"] = b + [0, 0.15 * H]
        return out
    if kind == "dichasium":
        def branch(p, ang, ln, d):
            u = np.array([math.cos(math.radians(ang)), math.sin(math.radians(ang))])
            q = p + u * ln
            seg(p, q, 1.6 - 0.3 * d)
            fl(q, [0.0, 0.4, 0.82, 0.95][d], ang=ang)
            if d == 0:
                out["terminal"] = q
            if d < 3:
                fork = p + u * ln * 0.62
                for sg in (-1, 1):
                    if bracts:
                        _bract(ax, fork, ang + sg * 75, 0.05 * H * (1 - 0.2 * d), zorder=zorder - 0.5)
                    branch(fork, ang + sg * (40 - 4 * d), ln * 0.6, d + 1)
                if d == 0:
                    out["bract"] = fork + [0.03 * H, 0]
        branch(b, 90.0, 0.55 * H, 0)
        out["peduncle"] = b + [0, 0.15 * H]
        return out
    raise ValueError(f"unknown inflorescence {kind!r}")


# ============================================================================ anatomy: cells from seeds

# tissue style: (token, wall line width, gap (fraction of cell radius), lumen (thick wall: lumen as fraction
# of the cell, 0 = thin wall), chloroplasts per unit perimeter (in cell radii))
STYLE = {
    "epidermis": ("epidermis", 0.7, 0.06, 0, 0),
    "root_hair": ("epidermis", 0.7, 0.06, 0, 0),
    "guard": ("guard", 0.7, 0.08, 0, 0.9),
    "bulliform": ("bulliform", 0.6, 0.06, 0, 0),
    "collenchyma": ("collenchyma", 1.3, 0.04, 0, 0),
    "cortex": ("cortex", 0.55, 0.12, 0, 0),
    "pith": ("pith", 0.55, 0.08, 0, 0),
    "ground": ("ground", 0.55, 0.08, 0, 0),
    "parenchyma": ("parenchyma", 0.5, 0.06, 0, 0),
    "sclerenchyma": ("sclerenchyma", 0.6, 0.04, 0.45, 0),
    "hypodermis": ("hypodermis", 0.6, 0.04, 0.5, 0),
    "exodermis": ("exodermis", 0.7, 0.05, 0, 0),
    "endodermis": ("endodermis", 0.8, 0.04, 0, 0),
    "pericycle": ("pericycle", 0.6, 0.05, 0, 0),
    "phloem": ("phloem", 0.5, 0.06, 0, 0),
    "cambium": ("cambium", 0.5, 0.06, 0, 0),
    "xylem": ("xylem", 0.6, 0.04, 0.72, 0),
    "protoxylem": ("xylem", 0.6, 0.04, 0.6, 0),
    "xylem_parenchyma": ("xylem", 0.4, 0.06, 0, 0),
    "palisade": ("palisade", 0.6, 0.1, 0, 0.75),
    "spongy": ("spongy", 0.6, 0.24, 0, 0.6),
    "mesophyll": ("mesophyll", 0.6, 0.1, 0, 0.65),
    "sheath": ("sheath", 0.6, 0.05, 0, 0.25),
    "kranz": ("kranz", 0.7, 0.05, 0, 1.5),
    "air": (None, 0, 0, 0, 0),
}


def _power_cells(pts, wts):
    """Power (Laguerre) diagram of weighted points: list of convex polygons (None for hidden points)."""
    from scipy.spatial import ConvexHull

    z = (pts ** 2).sum(axis=1) - wts
    hull = ConvexHull(np.c_[pts, z], qhull_options="Qt")
    eq = hull.equations
    low = eq[:, 2] < -1e-12
    simp = hull.simplices[low]
    e = eq[low]
    centres = np.c_[-e[:, 0] / (2 * e[:, 2]), -e[:, 1] / (2 * e[:, 2])]
    owner = simp.ravel()
    fidx = np.repeat(np.arange(len(simp)), 3)
    order = np.argsort(owner, kind="stable")
    owner, fidx = owner[order], fidx[order]
    starts = np.searchsorted(owner, np.arange(len(pts)))
    ends = np.searchsorted(owner, np.arange(len(pts)), side="right")
    cells = []
    for i in range(len(pts)):
        f = fidx[starts[i]:ends[i]]
        if len(f) < 3:
            cells.append(None)
            continue
        c = centres[f]
        m = c.mean(axis=0)
        a = np.arctan2(c[:, 1] - m[1], c[:, 0] - m[0])
        c = c[np.argsort(a)]
        keep = np.r_[True, np.hypot(*np.diff(c, axis=0).T) > 1e-9]
        cells.append(c[keep])
    return cells


class Section:
    """A tissue section built from cells. Add seeds (centre, cell size = diameter, tissue tag); ``draw``
    computes the power diagram (weights = (size/2)², so a cell reaches half its size towards each
    neighbour) and draws every cell in its tissue's ``STYLE``. Ghost seeds bound the diagram (they are
    not drawn); ``mirror_circle`` / ``mirror_line`` add them as reflections so that outer walls lie on
    the section's surface.
    """

    def __init__(self, seed=0):
        self.p, self.size, self.tag, self.meta = [], [], [], []
        self.rng = np.random.default_rng(seed)

    def add(self, pts, size, tag, **meta):
        pts = np.atleast_2d(np.asarray(pts, float))
        sz = np.broadcast_to(np.asarray(size, float), (len(pts),))
        for p, z in zip(pts, sz):
            self.p.append(p)
            self.size.append(float(z))
            self.tag.append(tag)
            self.meta.append(meta)
        return pts

    def ring(self, c, r, size, tag, spacing=None, phase=0.0, jitter=0.0, arc=None, **meta):
        """Seeds on a circle of radius r (one layer of cells of radial size ``size``, tangential
        ``spacing``); ``arc`` = (a0, a1) radians limits it to an arc."""
        sp = spacing or size
        a0, a1 = arc or (0.0, 2 * math.pi)
        n = max(3, int(round((a1 - a0) * r / sp)))
        a = a0 + (np.arange(n) + 0.5) * (a1 - a0) / n + phase
        rr = r + self.rng.uniform(-jitter, jitter, n) * size
        pts = np.c_[c[0] + rr * np.cos(a), c[1] + rr * np.sin(a)]
        return self.add(pts, size, tag, **meta)

    def row(self, x0, x1, y, size, tag, spacing=None, jitter=0.0, **meta):
        sp = spacing or size
        n = max(1, int(round((x1 - x0) / sp)))
        x = x0 + (np.arange(n) + 0.5) * (x1 - x0) / n + self.rng.uniform(-jitter, jitter, n) * sp
        return self.add(np.c_[x, np.full(n, y)], size, tag, **meta)

    def fill(self, bbox, fn, smin, tries=3.0, eta=0.93, **meta):
        """Poisson-disc fill of bbox (x0, y0, x1, y1): ``fn(points) -> (tags, sizes)`` gives each
        candidate's tissue (None = outside) and cell size; seeds keep 0.5 (s_i + s_j) × eta apart."""
        x0, y0, x1, y1 = bbox
        n = int(tries * (x1 - x0) * (y1 - y0) / (smin * smin)) + 10
        cand = np.c_[self.rng.uniform(x0, x1, n), self.rng.uniform(y0, y1, n)]
        tags, sizes = fn(cand)
        sizes = np.asarray(sizes, float)
        ok = np.array([t is not None for t in tags])
        ok &= self.rng.uniform(0, 1, n) < (smin / np.maximum(sizes, smin)) ** 2 * 1.6
        cand, sizes = cand[ok], sizes[ok]
        tags = [t for t, o in zip(tags, ok) if o]
        g = smin
        grid = {}
        allp = list(zip(self.p, self.size))
        smax = max([smin] + list(sizes) + self.size)

        def key(p):
            return (int(math.floor(p[0] / g)), int(math.floor(p[1] / g)))
        for p, z in allp:
            grid.setdefault(key(p), []).append((p, z))
        for p, z, t in zip(cand, sizes, tags):
            reach = int(math.ceil((z + smax) / 2 / g))
            kx, ky = key(p)
            bad = False
            for ix in range(kx - reach, kx + reach + 1):
                for iy in range(ky - reach, ky + reach + 1):
                    for q, zq in grid.get((ix, iy), ()):
                        if (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 < (0.5 * (z + zq) * eta) ** 2:
                            bad = True
                            break
                    if bad:
                        break
                if bad:
                    break
            if not bad:
                grid.setdefault((kx, ky), []).append((p, z))
                self.add(p, z, t, **meta)

    def mirror_circle(self, c, R):
        """Ghosts: reflections of the outermost seeds across the circle of radius R."""
        c = np.asarray(c, float)
        P_ = np.array(self.p)
        d = np.hypot(*(P_ - c).T)
        sz = np.array(self.size)
        m = d > R - 1.6 * sz
        for p, dd, z in zip(P_[m], d[m], sz[m]):
            q = c + (p - c) * (2 * R - dd) / dd
            self.add(q, z, "ghost")
        # a far ring keeps the diagram bounded
        self.ring(c, R * 1.6, R * 0.3, "ghost")

    def mirror_line(self, y, above=True, x0=-1e9, x1=1e9):
        P_ = np.array(self.p)
        sz = np.array(self.size)
        m = (P_[:, 1] > y - 1.6 * sz) if above else (P_[:, 1] < y + 1.6 * sz)
        m &= (P_[:, 0] > x0) & (P_[:, 0] < x1)
        for p, z in zip(P_[m], sz[m]):
            self.add([p[0], 2 * y - p[1]], z, "ghost")

    def box_ghosts(self, bbox, size):
        x0, y0, x1, y1 = bbox
        for x in np.arange(x0 - 2 * size, x1 + 2 * size, size):
            self.add([[x, y0 - 2 * size], [x, y1 + 2 * size]], size, "ghost")
        for y in np.arange(y0 - size, y1 + size, size):
            self.add([[x0 - 2 * size, y], [x1 + 2 * size, y]], size, "ghost")

    def draw(self, ax, clip=None, zorder=5, style=None):
        """Draw all cells; returns {tag: [cell polygons]} and stores ``self.cells`` (index → polygon)."""
        st = dict(STYLE)
        st.update(style or {})
        pts = np.array(self.p)
        wts = (np.array(self.size) / 2) ** 2
        pts = pts + self.rng.normal(0, 1e-6, pts.shape)  # break lattice degeneracies
        cells = _power_cells(pts, wts)
        self.cells = cells
        groups = {}
        lumens = {}
        plastids = []
        for i, (poly, tag) in enumerate(zip(cells, self.tag)):
            if poly is None or tag == "ghost" or st.get(tag, (None,))[0] is None:
                continue
            token, lw, gap, lumen, chl = st[tag]
            cen = poly.mean(axis=0)
            area = 0.5 * abs(np.dot(poly[:, 0], np.roll(poly[:, 1], 1)) - np.dot(poly[:, 1], np.roll(poly[:, 0], 1)))
            r = math.sqrt(area / math.pi)
            if r <= 0 or r > 3 * self.size[i]:
                continue
            k = max(0.2, 1 - gap)
            sh = cen + (poly - cen) * k
            sh = _chaikin(sh, 2)
            groups.setdefault(tag, []).append(sh)
            if lumen:
                lumens.setdefault(tag, []).append(_chaikin(cen + (poly - cen) * k * lumen, 1))
            if chl:
                q, per = _resample(np.vstack([sh, sh[:1]]), 200)
                n = int(chl * per / (r * 0.55)) if r > 0 else 0
                ref = self.meta[i].get("centrifugal")
                for j in range(n):
                    pp = q[int((j + 0.5) / n * (len(q) - 1))]
                    if ref is not None and np.dot(pp - cen, cen - np.asarray(ref)) < 0.1 * r * np.hypot(*(cen - np.asarray(ref))):
                        continue
                    inw = cen - pp
                    inw /= np.hypot(*inw) + 1e-12
                    plastids.append((pp + inw * r * 0.16, math.degrees(math.atan2(inw[1], inw[0])) + 90, r,
                                     tok(token) == "thylakoid"))
        colls = []
        for tag, polys in groups.items():
            token, lw, gap, lumen, chl = st[tag]
            t = tok(token)
            if lumen:
                fc = P.mix(P.edge(t), P.fill(t), 0.35)
            else:
                fc = P.fill(t)
            pc = PolyCollection(polys, facecolors=fc, edgecolors=P.edge(t), linewidths=lw, zorder=zorder, joinstyle="round")
            colls.append(pc)
            if lumen:
                colls.append(PolyCollection(lumens[tag], facecolors=P.mix(P.surface(), P.fill(t), 0.45), edgecolors="none",
                                            zorder=zorder + 0.1))
        if plastids:
            ell, light_ = [], []
            for p, a, r, on_dark in plastids:
                rx, ry = (r * 0.19, r * 0.1) if on_dark else (r * 0.13, r * 0.075)
                t = np.linspace(0, 2 * np.pi, 10)
                ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
                e = np.c_[rx * np.cos(t), ry * np.sin(t)] @ np.array([[ca, sa], [-sa, ca]]) + p
                (light_ if on_dark else ell).append(e)
            colls.append(PolyCollection(ell, facecolors=P.fill("thylakoid"), edgecolors=P.edge("thylakoid"), linewidths=0.3,
                                        zorder=zorder + 0.2))
            if light_:  # chloroplasts in dark green (chlorenchyma-rich) cells are drawn light
                colls.append(PolyCollection(light_, facecolors=P.fill("chloroplast"), edgecolors=P.edge("thylakoid"),
                                            linewidths=0.3, zorder=zorder + 0.2))
        for c in colls:
            if clip is not None:
                c.set_clip_path(clip)
            ax.add_collection(c)
        self.groups = groups
        return groups

    def anchor(self, tag, near=None):
        """A point inside a drawn cell of ``tag`` (the one nearest ``near``)."""
        g = self.groups.get(tag)
        if not g:
            return None
        cs = np.array([p.mean(axis=0) for p in g])
        if near is None:
            return cs[len(cs) // 2]
        return cs[np.argmin(np.hypot(*(cs - np.asarray(near)).T))]


def _casparian(ax, c, r, seeds_angles, size, zorder=7):
    """Casparian strips: short dark bands in the radial walls of an endodermis ring (seen in section)."""
    a = np.sort(np.asarray(seeds_angles))
    mids = (a + np.roll(a, -1) + np.r_[np.zeros(len(a) - 1), 2 * math.pi]) / 2
    segs = []
    for m in mids:
        u = np.array([math.cos(m), math.sin(m)])
        segs.append([c + u * (r - size * 0.12), c + u * (r + size * 0.12)])
    ax.add_collection(LineCollection(segs, colors=P.edge(tok("casparian")), linewidths=2.2, zorder=zorder, capstyle="butt"))


def _surface(ax, c, R, token="epidermis", lw=1.1, zorder=7):
    ax.add_patch(Circle(c, R, fill=False, edgecolor=P.edge(tok(token)), lw=lw, zorder=zorder))


def stem_section(ax, center, radius, kind="eudicot", bundles=None, label_angle=30.0, seed=1, zorder=5):
    """A young (primary) stem in transverse section, built from cells.

    kind "eudicot": epidermis, collenchyma, cortex, a ring of open collateral bundles (sclerenchyma
         cap, phloem outside, fascicular cambium, xylem inside with protoxylem towards the pith), pith
         rays between the bundles and a parenchymatous pith (e.g. Helianthus).
    kind "monocot": epidermis, sclerenchymatous hypodermis and ground tissue with scattered closed
         bundles (more and smaller towards the periphery), each in a sclerenchyma sheath with phloem
         outwards, two large metaxylem vessels, protoxylem and a protoxylem lacuna (e.g. Zea).
    Returns anchors (canvas points): epidermis, collenchyma, cortex, bundle, phloem, cambium, xylem,
    protoxylem, cap (sclerenchyma), pith, pith_ray, hypodermis, ground, sheath, lacuna, metaxylem; they lie
    near one radius at ``label_angle`` (degrees), so labels stacked beside it in the anchors' vertical
    order have leaders that do not cross.
    """
    c = np.asarray(center, float)
    R = radius
    S = Section(seed)
    out = {}
    if kind == "eudicot":
        nb = bundles or 10
        e = 0.042 * R
        S.ring(c, R - e / 2, e, "epidermis", spacing=e * 1.5)
        for k, rr in enumerate((R - e - 0.02 * R, R - e - 0.058 * R, R - e - 0.096 * R)):
            S.ring(c, rr, 0.038 * R, "collenchyma", phase=0.3 * k)
        ab = math.radians(label_angle) + 2 * math.pi * np.arange(nb) / nb
        rc, rx0 = 0.56 * R, 0.4 * R

        def hw(r):  # bundle half-width (radians) as a function of radius: a teardrop
            t = np.clip((r - rx0) / (0.69 * R - rx0), 0, 1)
            return (0.05 + 0.17 * np.sin(np.pi * np.clip(t * 0.85 + 0.1, 0, 1)) ** 0.8) * (0.62 / np.maximum(r / R, 0.3))

        for a in ab:
            # cambium: one layer of flat cells; vessels in radial files with the largest next to the cambium
            S.ring(c, rc, 0.018 * R, "cambium", spacing=0.03 * R, arc=(a - hw(rc) * 0.95, a + hw(rc) * 0.95))
            for f in (-0.55, 0.0, 0.55):
                for rr, sz in ((0.43, 0.03), (0.475, 0.045), (0.522, 0.058)):
                    if rr * R > rx0 + 0.01 * R:
                        th = a + f * hw(rr * R) * (0.75 if rr > 0.45 else 0.3)
                        S.add(c + rr * R * np.array([math.cos(th), math.sin(th)]), sz * R, "xylem" if rr > 0.44 else "protoxylem")
        rng_cap = (0.635 * R, 0.69 * R)

        def tissue(p):
            d = np.hypot(*(p - c).T)
            th = np.arctan2(p[:, 1] - c[1], p[:, 0] - c[0])
            dth = np.abs((th[:, None] - ab[None, :] + np.pi) % (2 * np.pi) - np.pi).min(axis=1)
            inb = dth < hw(d)
            incap = dth < hw(np.full_like(d, 0.6 * R)) * 0.85
            tags, sizes = [], []
            for dd, ib, dcap in zip(d, inb, incap):
                if dd > R - e - 0.125 * R:
                    tags.append(None)
                    sizes.append(1)
                elif dcap and rng_cap[0] < dd < rng_cap[1] + 0.02 * R:
                    tags.append("sclerenchyma")
                    sizes.append(0.026 * R)
                elif ib and rc + 0.012 * R < dd <= rng_cap[0]:
                    tags.append("phloem")
                    sizes.append(0.024 * R)
                elif ib and rx0 < dd < rc - 0.012 * R:
                    tags.append("xylem_parenchyma")
                    sizes.append(0.022 * R)
                elif dd > 0.69 * R:
                    tags.append("cortex")
                    sizes.append(0.075 * R)
                elif dd > rx0:
                    tags.append("parenchyma")
                    sizes.append(0.055 * R)
                else:
                    tags.append("pith")
                    sizes.append(0.1 * R * (0.8 + 0.25 * dd / rx0))
            return tags, sizes
        S.fill((c[0] - R, c[1] - R, c[0] + R, c[1] + R), tissue, 0.02 * R)
        S.mirror_circle(c, R)
        S.draw(ax, zorder=zorder)
        _surface(ax, c, R, zorder=zorder + 1)
        a0 = ab[0]
        u = np.array([math.cos(a0), math.sin(a0)])
        out.update(epidermis=c + u * (R - e / 2), collenchyma=S.anchor("collenchyma", c + u * R * 0.9),
                   cortex=S.anchor("cortex", c + u * R * 0.77), cap=S.anchor("sclerenchyma", c + u * R * 0.66),
                   phloem=S.anchor("phloem", c + u * R * 0.6), cambium=S.anchor("cambium", c + u * rc),
                   xylem=S.anchor("xylem", c + u * R * 0.52), protoxylem=S.anchor("protoxylem", c + u * R * 0.43),
                   bundle=c + u * R * 0.55, pith=c + u * R * 0.2)
        am = ab[0] - math.pi / nb
        out["pith_ray"] = S.anchor("parenchyma", c + R * 0.55 * np.array([math.cos(am), math.sin(am)]))
        out["section"] = S
        return out
    # monocot
    e = 0.045 * R
    S.ring(c, R - e / 2, e, "epidermis", spacing=e * 1.4)
    for k, rr in enumerate((R - e - 0.02 * R, R - e - 0.058 * R)):
        S.ring(c, rr, 0.036 * R, "hypodermis", phase=0.4 * k)
    # bundle positions: Poisson in the disc, denser and smaller towards the periphery
    rng = np.random.default_rng(seed + 5)
    B_ = []
    for _ in range(4000):
        p = rng.uniform(-1, 1, 2) * R * 0.86
        d = np.hypot(*p)
        if d > 0.855 * R:
            continue
        rb = R * (0.085 - 0.04 * (d / R) ** 2)
        gap = rb * (2.4 + 2.6 * (1 - d / R))
        if all(np.hypot(*(p - q)) > (gap + gq) / 2 for q, _, gq in B_):
            B_.append((p, rb, gap))
        if len(B_) >= (bundles or 60):
            break
    bundle_list = []
    for p, rb, _ in B_:
        bc = c + p
        d = np.hypot(*p)
        u = p / d if d > 1e-6 else np.array([0, 1.0])
        v = np.array([-u[1], u[0]])
        bundle_list.append((bc, rb, u, v))
        S.ring(bc, rb * 1.02, rb * 0.26, "sclerenchyma", spacing=rb * 0.24)
        S.add(bc + rb * (0.0 * u + 0.44 * v), rb * 0.46, "xylem")
        S.add(bc + rb * (0.0 * u - 0.44 * v), rb * 0.46, "xylem")
        S.add(bc - rb * 0.33 * u, rb * 0.22, "protoxylem")
        S.add(bc - rb * 0.62 * u, rb * 0.36, "air")
    centres = np.array([b[0] for b in bundle_list])
    rbs = np.array([b[1] for b in bundle_list])
    us = np.array([b[2] for b in bundle_list])

    def tissue(p):
        d = np.hypot(*(p - c).T)
        dist = np.hypot(p[:, None, 0] - centres[None, :, 0], p[:, None, 1] - centres[None, :, 1])
        j = np.argmin(dist / rbs[None, :], axis=1)
        rel = dist[np.arange(len(p)), j] / rbs[j]
        along = ((p - centres[j]) * us[j]).sum(axis=1) / rbs[j]
        tags, sizes = [], []
        for dd, rr, al, jj in zip(d, rel, along, j):
            if dd > R - e - 0.08 * R:
                tags.append(None)
                sizes.append(1)
            elif rr < 0.86:
                if al > 0.22:
                    tags.append("phloem")
                    sizes.append(rbs[jj] * 0.17)
                else:
                    tags.append("xylem_parenchyma")
                    sizes.append(rbs[jj] * 0.17)
            elif rr < 1.2:
                tags.append(None)
                sizes.append(1)
            else:
                tags.append("ground")
                sizes.append(R * (0.085 - 0.03 * (dd / R) ** 2))
        return tags, sizes
    S.fill((c[0] - R, c[1] - R, c[0] + R, c[1] + R), tissue, float(rbs.min()) * 0.17)
    S.mirror_circle(c, R)
    S.draw(ax, zorder=zorder)
    _surface(ax, c, R, zorder=zorder + 1)
    # anchors on a mid-radius bundle on the right
    ul = np.array([math.cos(math.radians(label_angle)), math.sin(math.radians(label_angle))])
    score = [np.hypot(*(b[0] - c - ul * 0.62 * R)) for b in bundle_list]
    bc, rb, u, v = bundle_list[int(np.argmin(score))]
    out.update(epidermis=c + ul * (R - e / 2), hypodermis=S.anchor("hypodermis", c + ul * R * 0.92),
               ground=S.anchor("ground", c + ul * 0.3 * R), bundle=bc, sheath=bc + v * rb * 0.95 * np.sign(v @ [ul[1], -ul[0]] + 1e-9),
               phloem=bc + u * rb * 0.5, xylem=bc + v * rb * 0.44, metaxylem=bc + v * rb * 0.44, protoxylem=bc - u * rb * 0.33,
               lacuna=bc - u * rb * 0.62, section=S)
    return out


def root_section(ax, center, radius, kind="eudicot", poles=None, hairs=5, label_angle=30.0, seed=2, zorder=5):
    """A young root in transverse section (zone of maturation), built from cells.

    kind "eudicot": epidermis with root hairs, a wide parenchymatous cortex with intercellular spaces,
         endodermis (Casparian strips in the radial walls), pericycle, and a small stele with a xylem
         star (``poles`` arms, default 4: tetrarch; protoxylem exarch at the arm tips, metaxylem towards
         the centre) alternating with phloem strands; no pith (e.g. Ranunculus).
    kind "monocot": as above with an exodermis, but a polyarch stele (default 14 poles): a ring of
         protoxylem poles alternating with phloem, large metaxylem vessels inside them and a central
         pith (e.g. Zea, Iris).
    Returns anchors: epidermis, root_hair, cortex, exodermis, endodermis, casparian, pericycle, xylem,
    protoxylem, metaxylem, phloem, pith, stele (near the radius at ``label_angle``; a phloem strand lies on it).
    """
    c = np.asarray(center, float)
    R = radius
    S = Section(seed)
    out = {}
    mono = kind == "monocot"
    e = 0.05 * R
    S.ring(c, R - e / 2, e, "epidermis", spacing=e * 1.25)
    r_end = (0.45 if mono else 0.34) * R
    se = 0.045 * R
    endo = S.ring(c, r_end, se, "endodermis", spacing=se * 1.05)
    endo_ang = np.arctan2(endo[:, 1] - c[1], endo[:, 0] - c[0])
    r_per = r_end - se / 2 - 0.018 * R
    S.ring(c, r_per, 0.034 * R, "pericycle", spacing=0.036 * R, phase=0.02)
    S.ring(c, r_end + se / 2 + 0.032 * R, 0.064 * R, "cortex", spacing=0.07 * R, phase=0.03)  # innermost cortex layer
    if mono:
        S.ring(c, R - e - 0.024 * R, 0.045 * R, "exodermis", spacing=0.05 * R)
    rs = r_per - 0.02 * R  # stele inside the pericycle
    n = poles or (14 if mono else 4)
    pole_ang = 2 * math.pi * np.arange(n) / n + math.radians(label_angle) - math.pi / n
    xyl = []
    if mono:
        for a in pole_ang:
            u = np.array([math.cos(a), math.sin(a)])
            S.add(c + u * (rs - 0.025 * R), 0.028 * R, "protoxylem")
            xyl.append(c + u * (rs - 0.025 * R))
            a2 = a + math.pi / n * 0.0
            S.add(c + np.array([math.cos(a2), math.sin(a2)]) * (rs * 0.62), 0.07 * R, "xylem")
    else:
        S.add(c, 0.075 * R, "xylem")
        for a in pole_ang:
            u = np.array([math.cos(a), math.sin(a)])
            v = np.array([-u[1], u[0]])
            for rr, sz in ((0.098, 0.058), (0.165, 0.05), (0.222, 0.04), (0.265, 0.027)):
                if rr * R < rs - 0.008 * R:
                    S.add(c + u * rr * R, sz * R, "xylem" if rr < 0.25 else "protoxylem")
            for rr, sz in ((0.135, 0.03), (0.195, 0.026)):  # the arms widen towards the centre
                for sg in (-1, 1):
                    S.add(c + u * rr * R + sg * v * (0.04 if rr < 0.15 else 0.033) * R, sz * R, "xylem")
    ph_ang = pole_ang + math.pi / n

    def tissue(p):
        d = np.hypot(*(p - c).T)
        th = np.arctan2(p[:, 1] - c[1], p[:, 0] - c[0])
        dph = np.abs((th[:, None] - ph_ang[None, :] + np.pi) % (2 * np.pi) - np.pi).min(axis=1)
        tags, sizes = [], []
        for dd, dp in zip(d, dph):
            if dd > R - e - (0.05 if mono else 0.004) * R or (r_per - 0.02 * R < dd < r_end + se / 2 + 0.07 * R):
                tags.append(None)
                sizes.append(1)
            elif dd > r_end:
                tags.append("cortex")
                sizes.append(R * (0.1 + 0.04 * (dd - r_end) / (R - r_end)) * (0.8 if mono else 1))
            elif mono and dd < rs * 0.48:
                tags.append("pith")
                sizes.append(0.06 * R)
            elif dd < rs and dp * dd < (0.055 if mono else 0.052) * R and dd > (rs * 0.7 if mono else 0.15 * R):
                tags.append("phloem")
                sizes.append(0.022 * R)
            elif dd < rs:
                tags.append("parenchyma")
                sizes.append(0.026 * R)
            else:
                tags.append(None)
                sizes.append(1)
        return tags, sizes
    S.fill((c[0] - R, c[1] - R, c[0] + R, c[1] + R), tissue, 0.022 * R)
    S.mirror_circle(c, R)
    # root hairs: tubular outgrowths of some epidermal cells (trichoblasts)
    S.draw(ax, zorder=zorder)
    _surface(ax, c, R, zorder=zorder + 1)
    _casparian(ax, c, r_end, endo_ang, se, zorder=zorder + 1.5)
    hair_pts = []
    hair_ang = [label_angle + 62 + k * 360 / max(hairs, 1) for k in range(hairs)]
    hair_ang = [h for h in hair_ang if abs((h - label_angle + 180) % 360 - 180) > 40]  # keep the label side clear
    for k, h in enumerate(hair_ang):
        a = math.radians(h)
        u = np.array([math.cos(a), math.sin(a)])
        v = np.array([-u[1], u[0]])
        t = np.linspace(0, 1, 30)
        ln = R * (0.35 + 0.12 * (k % 3))
        path = c + u * (R - e * 0.3) + np.outer(t * ln, u) + np.outer(np.sin(t * 3.0 + k) * 0.04 * R * t, v)
        ax.plot(path[:, 0], path[:, 1], color=_edge("root_hair"), lw=3.0 * _lw(R, 1, 3), solid_capstyle="round", zorder=zorder + 0.5)
        ax.plot(path[:, 0], path[:, 1], color=_fill("root_hair"), lw=1.6 * _lw(R, 1, 3), solid_capstyle="round", zorder=zorder + 0.6)
        hair_pts.append(path[20])
    a0 = pole_ang[0]
    u = np.array([math.cos(a0), math.sin(a0)])
    up = np.array([math.cos(ph_ang[0]), math.sin(ph_ang[0])])
    ea = np.sort(endo_ang)
    wall = (ea + np.roll(ea, -1) + np.r_[np.zeros(len(ea) - 1), 2 * math.pi]) / 2
    wa = wall[np.argmin(np.abs((wall - ph_ang[0] - 0.12 + np.pi) % (2 * np.pi) - np.pi))]
    out.update(epidermis=S.anchor("epidermis", c + up * R), root_hair=hair_pts[0] if hair_pts else None,
               cortex=S.anchor("cortex", c + up * (r_end + R) / 2), endodermis=S.anchor("endodermis", c + up * r_end),
               casparian=c + np.array([math.cos(wa), math.sin(wa)]) * r_end,
               pericycle=S.anchor("pericycle", c + up * r_per), phloem=S.anchor("phloem", c + up * rs * 0.8),
               protoxylem=S.anchor("protoxylem", c + u * rs), metaxylem=S.anchor("xylem", c + u * rs * (0.62 if mono else 0.2)),
               stele=c + up * rs * 0.5, section=S)
    out["xylem"] = out["metaxylem"]
    if mono:
        out["exodermis"] = S.anchor("exodermis", c + up * R * 0.92)
        out["pith"] = c + up * 0.1 * R
    return out


def leaf_anatomy(ax, box, kind="C3", veins=None, stomata=None, label_x=0.72, seed=3, zorder=5):
    """A leaf blade in transverse section (adaxial side up), built from cells; ``box`` = (x0, y0, w, h)
    spans lower to upper surface. Cells carry chloroplasts according to their tissue.

    kind "C3": dorsiventral eudicot leaf: cuticle, upper epidermis, one layer of palisade mesophyll,
         spongy mesophyll with large air spaces, veins with a pale parenchymatous bundle sheath (xylem
         adaxial, phloem abaxial), lower epidermis with stomata over substomatal cavities.
    kind "C4": Kranz anatomy of a C4 grass (e.g. Zea): closely spaced veins, each in a bundle sheath of
         large cells with many chloroplasts (centrifugal), surrounded by a wreath of radially arranged
         mesophyll cells; bulliform cells in the upper epidermis; stomata on both surfaces.
    Returns anchors: cuticle, upper_epidermis, lower_epidermis, palisade, spongy, mesophyll, sheath,
    vein, xylem, phloem, stoma, guard_cell, air_space, bulliform (taken near x = x0 + label_x × w), and
    ``veins`` (centres).
    """
    x0, y0, w, h = box
    x1, y1 = x0 + w, y0 + h
    S = Section(seed)
    out = {}
    e = 0.1 * h
    pad = 0.35 * h
    xa, xb = x0 - pad, x1 + pad
    c4 = kind.upper() == "C4"
    yu = y1 - e / 2  # upper epidermis
    yl = y0 + e * 0.45
    # veins
    if c4:
        gap = 0.95 * h
        nv = veins or max(1, int(round(w / gap)))
    else:
        nv = veins or max(1, int(round(w / (2.2 * h))))
        gap = w / nv
    vx = [x0 + (k + 0.5) * w / nv for k in range(nv)]
    vy = y0 + h * (0.5 if c4 else 0.43)
    rb = (0.17 if c4 else 0.15) * h
    ext = list(vx)
    if c4:  # neighbouring veins outside the box so the cut edges look continuous
        step = w / nv
        ext = [vx[0] - step] + vx + [vx[-1] + step]
    # stomata
    st_x = []
    ns = stomata if stomata is not None else (max(1, nv) if not c4 else nv)
    for k in range(ns):
        xs = (vx[k % nv] + w / nv / 2) if c4 else (x0 + (k + 0.5) * w / ns + 0.7 * h)
        if x0 + 0.2 * h < xs < x1 - 0.2 * h:
            st_x.append(xs)
    bull = []
    top_st = []
    if c4:  # intercostal zones of the upper surface: alternately a stoma and a group of bulliform cells
        for k, v in enumerate(vx[:-1] if nv > 1 else vx):
            (bull if k % 2 == 0 else top_st).append(v + w / nv / 2)

    def epidermis(y, size, stx, upper):
        xs = np.arange(xa, xb, size * 1.55) + size * 0.4
        for x in xs:
            if any(abs(x - s) < size * 1.2 for s in stx):
                continue
            if upper and any(abs(x - b) < 0.2 * h for b in bull):
                continue
            S.add([x, y], size, "epidermis")
        for s in stx:
            gy = y
            S.add([[s - size * 0.42, gy], [s + size * 0.42, gy]], size * 0.72, "guard")
            S.add([s, gy], size * 0.2, "air")
            cav = gy + (-1 if upper else 1) * (size / 2 + 0.11 * h)
            S.add([s, cav], 0.2 * h, "air")
        if upper:  # bulliform cells: a fan of large, thin-walled epidermal cells
            for bc in bull:
                for dx, sz in ((-0.13, 0.15), (0.0, 0.2), (0.13, 0.15)):
                    S.add([bc + dx * h, y1 - sz * h * 0.5], sz * h * 0.85, "bulliform")
    epidermis(yu, e, top_st, True)
    epidermis(yl, e * 0.9, st_x, False)
    # a film of tiny air seeds bounds the inner walls of the epidermis (cells do not bulge into air spaces)
    S.row(xa, xb, yl + e * 0.45 + 0.012 * h, 0.024 * h, "air", spacing=0.03 * h)
    if c4:
        for x in np.arange(xa, xb, 0.03 * h):
            if all(abs(x - b) > 0.3 * h for b in bull):
                S.add([x, yu - e / 2 - 0.012 * h], 0.024 * h, "air")
    if not c4:
        pal_h = 0.3 * h
        yp = y1 - e - pal_h / 2 - 0.01 * h
        S.row(xa, xb, yp, pal_h, "palisade", spacing=0.095 * h)
        top_meso, bot_meso = yp - pal_h / 2, yl + e * 0.45 + 0.02 * h
    else:
        top_meso, bot_meso = y1 - e - 0.02 * h, yl + e * 0.45 + 0.02 * h
    for v in ext:
        if c4:
            S.ring((v, vy), rb, 0.085 * h, "kranz", spacing=0.075 * h, centrifugal=(v, vy))
            S.ring((v, vy), rb + 0.0425 * h + 0.07 * h, 0.14 * h, "mesophyll", spacing=0.062 * h, phase=0.1)
        else:
            S.ring((v, vy), rb, 0.07 * h, "sheath", spacing=0.065 * h)
        # xylem towards the upper side, phloem below
        S.add([[v - 0.045 * h, vy + 0.04 * h], [v + 0.045 * h, vy + 0.04 * h]], 0.05 * h, "xylem")
        S.add([v, vy + 0.075 * h], 0.03 * h, "protoxylem")
    vxa = np.array(ext)
    rng = np.random.default_rng(seed + 9)

    def tissue(p):
        tags, sizes = [], []
        for x, y in p:
            dv = np.hypot(vxa - x, vy - y).min()
            if y > top_meso or y < bot_meso:
                tags.append(None)
                sizes.append(1)
            elif dv < rb * 0.75:
                if y > vy + 0.005 * h:
                    tags.append("xylem_parenchyma")
                    sizes.append(0.025 * h)
                else:
                    tags.append("phloem")
                    sizes.append(0.022 * h)
            elif dv < rb + (0.26 if c4 else 0.075) * h:
                tags.append(None)
                sizes.append(1)
            elif not c4 and y > top_meso - 0.06 * h:
                tags.append(None)
                sizes.append(1)
            elif rng.random() < (0.1 if c4 else 0.12):  # intercellular air spaces
                tags.append("air")
                sizes.append((0.1 if c4 else 0.13) * h)
            else:
                tags.append("mesophyll" if c4 else "spongy")
                sizes.append((0.115 if c4 else 0.15) * h)
        return tags, sizes
    S.fill((xa, y0, xb, y1), tissue, 0.022 * h)
    S.mirror_line(y1, above=True)
    S.mirror_line(y0, above=False)
    S.box_ghosts((xa - pad, y0 - h, xb + pad, y1 + h), 0.3 * h)
    clip = Polygon([(x0, y0 - 0.02 * h), (x1, y0 - 0.02 * h), (x1, y1 + 0.02 * h), (x0, y1 + 0.02 * h)], closed=True,
                   transform=ax.transData, facecolor="none", edgecolor="none")
    S.draw(ax, clip=clip, zorder=zorder)
    # cuticle on both surfaces
    for y in (y1, y0):
        ax.plot([x0, x1], [y, y], color=P.edge(tok("epidermis")), lw=1.6, zorder=zorder + 1, solid_capstyle="butt")
    out["veins"] = [np.array([v, vy]) for v in vx]
    xl = x0 + label_x * w  # anchors are taken near this x (labels to the right do not cross the figure)
    v0 = min(vx, key=lambda v: abs(v - xl))
    out.update(cuticle=np.array([xl + 0.12 * w, y1]), upper_epidermis=S.anchor("epidermis", (xl + 0.06 * w, yu)),
               lower_epidermis=S.anchor("epidermis", (xl + 0.1 * w, yl)), vein=np.array([v0, vy]),
               sheath=S.anchor("kranz" if c4 else "sheath", (v0 + rb, vy + 0.02 * h)), xylem=S.anchor("xylem", (v0 + 0.05 * h, vy + 0.04 * h)),
               phloem=S.anchor("phloem", (v0 + 0.05 * h, vy - 0.07 * h)))
    if st_x:
        sx_ = min(st_x, key=lambda x: abs(x - xl))
        out["stoma"] = np.array([sx_, yl])
        out["guard_cell"] = S.anchor("guard", (sx_ + 0.05 * h, yl))
        out["air_space"] = np.array([sx_, yl + e / 2 + 0.11 * h])
    if c4:
        out["mesophyll"] = S.anchor("mesophyll", (v0 + rb + 0.15 * h, vy + 0.2 * h))
        out["kranz"] = out["sheath"]
        if bull:
            out["bulliform"] = S.anchor("bulliform", (min(bull, key=lambda x: abs(x - xl)), y1))
    else:
        out["palisade"] = S.anchor("palisade", (xl + 0.08 * w, y1 - e - 0.15 * h))
        out["spongy"] = S.anchor("spongy", (xl + 0.1 * w, y0 + 0.3 * h))
        out["mesophyll"] = out["palisade"]
    out["section"] = S
    return out


# ============================================================================ secondary growth


def _ring_path(c, r_of_theta, n=240):
    th = np.linspace(0, 2 * np.pi, n)
    r = r_of_theta(th)
    return np.c_[c[0] + r * np.cos(th), c[1] + r * np.sin(th)]


def _annulus(ax, c, r_in, r_out, face, edge=None, lw=0.0, zorder=5):
    """Fill between two closed curves (r_in, r_out: functions of theta)."""
    a = _ring_path(c, r_out)
    b = _ring_path(c, r_in)[::-1]
    verts = np.vstack([a, a[:1], b, b[:1]])
    codes = np.r_[Path.MOVETO, np.full(len(a), Path.LINETO), Path.MOVETO, np.full(len(b), Path.LINETO)]
    codes[len(a)] = Path.CLOSEPOLY
    codes[-1] = Path.CLOSEPOLY
    return ax.add_patch(PathPatch(Path(verts, codes), facecolor=face, edgecolor=edge or "none", lw=lw, zorder=zorder))


def woody_stem(ax, center, radius, years=5, widths=None, heartwood=2, rays=28, seed=4, zorder=5):
    """A woody stem in transverse section after ``years`` seasons of secondary growth: pith, primary
    xylem, annual rings of secondary xylem (earlywood pale, latewood dark; the inner ``heartwood``
    rings darker), rays, vascular cambium, secondary phloem with dilated rays, and the periderm
    (cork cambium and cork) with a fissured surface. Ring widths vary by year (``widths``, relative).
    Returns anchors: pith, primary_xylem, secondary_xylem, annual_ring, earlywood, latewood, heartwood,
    sapwood, ray, dilated_ray, cambium, secondary_phloem, phellogen, cork, periderm, bark, rings (radii).
    """
    c = np.asarray(center, float)
    R = radius
    rng = np.random.default_rng(seed)
    wid = np.asarray(widths if widths is not None else (1.0, 0.75, 1.2, 0.55, 0.95, 0.8, 1.1, 0.7)[:years], float)
    r_p, r_x0, r_cam = 0.07 * R, 0.1 * R, 0.78 * R
    edges = r_x0 + (r_cam - r_x0) * np.r_[0, np.cumsum(wid)] / wid.sum()
    wob = [(rng.uniform(0, 2 * np.pi), rng.uniform(0.004, 0.012)) for _ in edges]

    def R_(r, k):
        ph, a = wob[min(k, len(wob) - 1)]
        return lambda th: r * (1 + a * np.sin(3 * th + ph) + 0.5 * a * np.sin(5 * th + 2 * ph))
    # bark: cork with a fissured outline, then secondary phloem
    fiss = lambda th: R * (0.97 - 0.035 * np.abs(np.sin(7.5 * th + 0.4)) ** 6 - 0.012 * np.sin(23 * th) ** 2)  # noqa: E731
    cork = _annulus(ax, c, R_(0.905 * R, 0), fiss, _fill("cork"), P.edge(tok("cork")), 0.9, zorder)
    for k in range(5):  # cork cell layers
        rr = 0.915 * R + k * 0.012 * R
        ln, = ax.plot(*_ring_path(c, R_(rr, 0)).T, color=P.edge(tok("cork")), lw=0.35, zorder=zorder + 0.1)
        ln.set_clip_path(cork)
    _annulus(ax, c, R_(0.895 * R, 0), R_(0.905 * R, 0), _fill("phellogen"), None, 0, zorder + 0.2)
    _annulus(ax, c, R_(r_cam + 0.012 * R, 0), R_(0.895 * R, 0), _fill("secondary_phloem"), None, 0, zorder)
    _annulus(ax, c, R_(r_cam, 0), R_(r_cam + 0.012 * R, 0), _fill("cambium"), P.edge(tok("cambium")), 0.4, zorder + 0.2)
    # secondary xylem: rings from the inside out
    n_heart = min(heartwood, years)
    for k in range(years):
        r0, r1 = edges[k], edges[k + 1]
        late = r1 - 0.32 * (r1 - r0)
        heart = k < n_heart
        ew = P.mix(_fill("earlywood"), _fill("heartwood"), 0.7) if heart else _fill("earlywood")
        lw_ = P.mix(_fill("latewood"), P.edge(tok("heartwood")), 0.55) if heart else P.mix(_fill("latewood"), P.edge(tok("latewood")), 0.3)
        _annulus(ax, c, R_(r0, k), R_(late, k + 1), ew, None, 0, zorder)
        # a gradient from early- to latewood: a few thin bands
        for j in range(3):
            f0 = late + (r1 - late) * j / 3
            f1 = late + (r1 - late) * (j + 1) / 3
            _annulus(ax, c, R_(f0, k + 1), R_(f1, k + 1), P.mix(ew, lw_, (j + 1) / 3), None, 0, zorder)
        ax.plot(*_ring_path(c, R_(r1, k + 1)).T, color=P.edge(tok("latewood")), lw=0.7, zorder=zorder + 0.3)
    # primary xylem (small bumps around the pith) and pith
    th = np.linspace(0, 2 * np.pi, 400)
    rp = r_x0 * (1 + 0.12 * np.abs(np.sin(5 * th)) ** 2)
    ax.add_patch(Polygon(np.c_[c[0] + rp * np.cos(th), c[1] + rp * np.sin(th)], closed=True, facecolor=_fill("xylem"),
                         edgecolor=_edge("xylem"), lw=0.6, zorder=zorder + 0.4))
    ax.add_patch(Circle(c, r_p, facecolor=_fill("pith"), edgecolor=_edge("pith"), lw=0.6, zorder=zorder + 0.5))
    # rays: start at different years, run through the cambium and dilate in the phloem
    ray_th = []
    segs, wedges = [], []
    for k in range(rays):
        t0 = 2 * np.pi * k / rays + rng.uniform(-0.05, 0.05)
        start = edges[0] if k % 3 == 0 else edges[min(years - 1, 1 + k % max(1, years - 1))]
        u = np.array([math.cos(t0), math.sin(t0)])
        segs.append([c + u * start, c + u * r_cam])
        ray_th.append(t0)
        if k % 3 == 0:
            v = np.array([-u[1], u[0]])
            wedges.append([c + u * r_cam - v * 0.004 * R, c + u * 0.895 * R - v * 0.03 * R, c + u * 0.895 * R + v * 0.03 * R,
                           c + u * r_cam + v * 0.004 * R])
        else:
            segs.append([c + u * r_cam, c + u * 0.895 * R])
    ax.add_collection(LineCollection(segs, colors=P.edge(tok("ray")), linewidths=0.8, zorder=zorder + 0.35))
    ax.add_collection(PolyCollection(wedges, facecolors=_fill("ray"), edgecolors=P.edge(tok("ray")), linewidths=0.5,
                                     zorder=zorder + 0.36))
    k_s = years - 1
    a = math.radians(62)
    u = np.array([math.cos(a), math.sin(a)])
    rm = (edges[k_s] + edges[k_s + 1]) / 2
    out = dict(pith=c, primary_xylem=c + u * r_x0 * 1.05, secondary_xylem=c + u * rm, rings=edges,
               earlywood=c + u * (edges[k_s] + 0.3 * (edges[k_s + 1] - edges[k_s])),
               latewood=c + u * (edges[k_s + 1] - 0.1 * (edges[k_s + 1] - edges[k_s])),
               annual_ring=c + u * edges[k_s + 1], heartwood=c + u * (edges[0] + edges[n_heart]) / 2 if n_heart else None,
               sapwood=c + u * (edges[n_heart] + r_cam) / 2, cambium=c + u * (r_cam + 0.006 * R),
               secondary_phloem=c + u * 0.85 * R, phellogen=c + u * 0.9 * R, cork=c + u * 0.94 * R, periderm=c + u * 0.93 * R,
               bark=c + u * 0.88 * R)
    ra = np.array(ray_th)

    def near(deg, pool):
        d = np.abs((ra[pool] - math.radians(deg) + np.pi) % (2 * np.pi) - np.pi)
        return float(ra[pool][np.argmin(d)])
    t0 = near(135, np.arange(len(ra)))
    out["ray"] = c + np.array([math.cos(t0), math.sin(t0)]) * (edges[years - 1] + r_cam) / 2
    t0 = near(225, np.arange(0, len(ra), 3))
    out["dilated_ray"] = c + np.array([math.cos(t0), math.sin(t0)]) * 0.86 * R
    return out


def wood_strip(ax, box, years=3, kind="ring-porous", files=None, seed=5, zorder=5):
    """A radial strip through a woody stem at cell level (pith on the left, bark on the right; rows are
    radial files of cells derived from cambial initials): pith, primary xylem, ``years`` annual rings
    whose cells shrink and thicken from earlywood to latewood, rays (files of radially elongated
    parenchyma), vessels ("ring-porous": large earlywood vessels; "diffuse-porous": scattered; "softwood":
    tracheids only), vascular cambium, secondary phloem (sieve tubes with fibre bands), phellogen and cork.
    ``box`` = (x0, y0, w, h). Returns anchors: pith, primary_xylem, earlywood, latewood, ring_boundary,
    vessel, tracheid, ray, cambium, secondary_phloem, phloem_fibres, phellogen, cork, and ``x`` (zone edges).
    """
    x0, y0, w, h = box
    rng = np.random.default_rng(seed)
    nf = files or max(8, int(round(h / (w / 70))))
    fh = h / nf
    ray_rows = set(range(3, nf, 6))
    cells = {}

    def add(tag, x, y, cw, chh):
        cells.setdefault(tag, []).append((x, y, cw, chh))
    # zone widths (fractions of w)
    z = dict(pith=0.08, primary=0.05, wood=0.6, cambium=0.025, phloem=0.13, phellogen=0.012, cork=0.1)
    tot = sum(z.values())
    xs = {}
    x = x0
    for k_ in ("pith", "primary", "wood", "cambium", "phloem", "phellogen", "cork"):
        xs[k_] = (x, x + z[k_] / tot * w)
        x += z[k_] / tot * w
    ring_x = np.linspace(*xs["wood"], years + 1)
    out = {"x": xs}
    for i in range(nf):
        yc = y0 + (i + 0.5) * fh
        ray = i in ray_rows
        # pith: large parenchyma (two rows per three files)
        if i % 2 == 0:
            xx = xs["pith"][0]
            while xx < xs["pith"][1] - 1e-9:
                cw = min(fh * 2.0, xs["pith"][1] - xx)
                add("pith", xx + cw / 2, yc + fh / 2 if i + 1 < nf else yc, cw, fh * 2 if i + 1 < nf else fh)
                xx += cw
        xx = xs["primary"][0]
        while xx < xs["primary"][1] - 1e-9:
            cw = min(fh * 0.7, xs["primary"][1] - xx)
            add("protoxylem", xx + cw / 2, yc, cw, fh)
            xx += cw
        for k in range(years):
            a, b = ring_x[k], ring_x[k + 1]
            xx = a
            while xx < b - 1e-9:
                f = (xx - a) / (b - a)
                if ray:
                    cw = fh * 2.6
                    tag = "ray"
                else:
                    cw = fh * (1.25 - 0.95 * _smoothstep((f - 0.55) / 0.4))
                    tag = "earlywood" if f < 0.7 else "latewood"
                cw = min(cw, b - xx)
                add(tag, xx + cw / 2, yc, cw, fh)
                xx += cw
        # cambium: thin, tangentially flattened initials and derivatives
        xx = xs["cambium"][0]
        while xx < xs["cambium"][1] - 1e-9:
            cw = min(fh * 0.32, xs["cambium"][1] - xx)
            add("cambium", xx + cw / 2, yc, cw, fh)
            xx += cw
        xx = xs["phloem"][0]
        j = 0
        while xx < xs["phloem"][1] - 1e-9:
            if ray:
                cw, tag = fh * 2.2, "ray"
            elif j % 7 in (4, 5):
                cw, tag = fh * 0.55, "sclerenchyma"  # tangential bands of phloem fibres
            else:
                cw, tag = fh * 0.95, "phloem"
            cw = min(cw, xs["phloem"][1] - xx)
            add(tag, xx + cw / 2, yc, cw, fh * (1.0 + (0.25 if ray else 0)))
            xx += cw
            j += 1
        x_pg = xs["phellogen"]
        add("phellogen", (x_pg[0] + x_pg[1]) / 2, yc, x_pg[1] - x_pg[0], fh)
        xx = xs["cork"][0]
        while xx < xs["cork"][1] - 1e-9:
            cw = min(fh * 0.45, xs["cork"][1] - xx)
            add("cork", xx + cw / 2, yc, cw, fh)
            xx += cw
    # vessels
    vessels = []
    if kind != "softwood":
        for k in range(years):
            a, b = ring_x[k], ring_x[k + 1]
            if kind == "ring-porous":
                cand = [(a + (b - a) * rng.uniform(0.05, 0.16), y0 + h * rng.uniform(0.05, 0.95), fh * rng.uniform(1.4, 1.9))
                        for _ in range(int(nf * 0.5))]
                cand += [(a + (b - a) * rng.uniform(0.3, 0.9), y0 + h * rng.uniform(0.05, 0.95), fh * 0.6) for _ in range(nf // 4)]
            else:
                cand = [(a + (b - a) * rng.uniform(0.05, 0.92), y0 + h * rng.uniform(0.05, 0.95), fh * rng.uniform(0.8, 1.15))
                        for _ in range(int(nf * 0.6))]
            for vx_, vy_, vr in cand:
                row = int((vy_ - y0) / fh)
                if any(abs(row - rr) <= 1 for rr in ray_rows) and vr > fh * 0.7:
                    continue
                if all(math.hypot(vx_ - p, vy_ - q) > (vr + r) * 1.1 for p, q, r in vessels):
                    if vx_ - vr > a and vx_ + vr < b:
                        vessels.append((vx_, vy_, vr))
    vs = np.array(vessels) if vessels else np.zeros((0, 3))
    cl = Polygon([(x0, y0), (x0 + w, y0), (x0 + w, y0 + h), (x0, y0 + h)], closed=True, transform=ax.transData,
                 facecolor="none", edgecolor="none")
    styles = {"pith": ("pith", 0.5, 0), "protoxylem": ("xylem", 0.5, 0.55), "earlywood": ("earlywood", 0.5, 0.78),
              "latewood": ("latewood", 0.5, 0.45), "ray": ("ray", 0.5, 0), "cambium": ("cambium", 0.45, 0),
              "phloem": ("secondary_phloem", 0.45, 0), "sclerenchyma": ("sclerenchyma", 0.45, 0.4),
              "phellogen": ("phellogen", 0.5, 0), "cork": ("cork", 0.45, 0)}
    anchor = {}
    for tag, lst in cells.items():
        token, lw, lumen = styles[tag]
        t = tok(token)
        polys, lums = [], []
        for (cx, cy, cw, ch) in lst:
            if len(vs) and tag in ("earlywood", "latewood") and (np.hypot(vs[:, 0] - cx, vs[:, 1] - cy) < vs[:, 2] + 0.25 * fh).any():
                continue
            gx, gy = min(cw, ch) * 0.06, min(cw, ch) * 0.06
            rect = np.array([[cx - cw / 2 + gx, cy - ch / 2 + gy], [cx + cw / 2 - gx, cy - ch / 2 + gy],
                             [cx + cw / 2 - gx, cy + ch / 2 - gy], [cx - cw / 2 + gx, cy + ch / 2 - gy]])
            polys.append(_chaikin(rect, 2))
            if lumen:
                m = np.array([cx, cy])
                lums.append(_chaikin(m + (rect - m) * [lumen, lumen + (1 - lumen) * 0.45], 2))
        fc = P.mix(P.edge(t), P.fill(t), 0.35) if lumen else P.fill(t)
        pc = PolyCollection(polys, facecolors=fc, edgecolors=P.edge(t), linewidths=lw, zorder=zorder)
        pc.set_clip_path(cl)
        ax.add_collection(pc)
        if lums:
            lc = PolyCollection(lums, facecolors=P.mix(P.surface(), P.fill(t), 0.5), edgecolors="none", zorder=zorder + 0.1)
            lc.set_clip_path(cl)
            ax.add_collection(lc)
        mid = lst[len(lst) // 2]
        anchor[tag] = np.array(mid[:2])
    if len(vs):
        t = tok("xylem")
        polys = [np.c_[vx_ + vr * np.cos(np.linspace(0, 2 * np.pi, 30)), vy_ + vr * np.sin(np.linspace(0, 2 * np.pi, 30))]
                 for vx_, vy_, vr in vs]
        lums = [np.c_[vx_ + vr * 0.8 * np.cos(np.linspace(0, 2 * np.pi, 30)), vy_ + vr * 0.8 * np.sin(np.linspace(0, 2 * np.pi, 30))]
                for vx_, vy_, vr in vs]
        ax.add_collection(PolyCollection(polys, facecolors=P.mix(P.edge(t), P.fill(t), 0.35), edgecolors=P.edge(t), linewidths=0.6,
                                         zorder=zorder + 0.2))
        ax.add_collection(PolyCollection(lums, facecolors=P.mix(P.surface(), P.fill(t), 0.5), edgecolors="none", zorder=zorder + 0.3))
        big = vs[np.argmax(vs[:, 2])] if kind == "ring-porous" else vs[len(vs) // 2]
        out["vessel"] = big[:2]
        out["vessels"] = vs
    ax.add_patch(PathPatch(Path([(x0, y0), (x0 + w, y0), (x0 + w, y0 + h), (x0, y0 + h), (x0, y0)], closed=True), fill=False,
                           edgecolor=P.muted(), lw=0.6, zorder=zorder + 0.5))
    # anchors in the last ring, away from rays
    a, b = ring_x[-2], ring_x[-1]
    r_ok = [i for i in range(nf) if all(abs(i - rr) > 1 for rr in ray_rows)]
    yy = y0 + (r_ok[len(r_ok) // 2] + 0.5) * fh
    yr = y0 + (sorted(ray_rows)[len(ray_rows) // 2] + 0.5) * fh
    out.update(pith=np.array([(xs["pith"][0] + xs["pith"][1]) / 2, yy]),
               primary_xylem=np.array([(xs["primary"][0] + xs["primary"][1]) / 2, yy]),
               earlywood=np.array([a + 0.35 * (b - a), yy]), latewood=np.array([a + 0.88 * (b - a), yy]),
               tracheid=np.array([a + 0.5 * (b - a), yy]), ring_boundary=np.array([b, yy]), ray=np.array([a + 0.5 * (b - a), yr]),
               cambium=np.array([(xs["cambium"][0] + xs["cambium"][1]) / 2, yy]),
               secondary_phloem=np.array([xs["phloem"][0] + 0.15 * (xs["phloem"][1] - xs["phloem"][0]), yy]),
               phloem_fibres=anchor.get("sclerenchyma"), phellogen=np.array([(xs["phellogen"][0] + xs["phellogen"][1]) / 2, yy]),
               cork=np.array([(xs["cork"][0] + xs["cork"][1]) / 2, yy]), ring_x=ring_x)
    if "vessel" not in out:
        out["vessel"] = None
    return out


# ============================================================================ plant architecture


def lsystem(axiom, rules, n):
    """Rewrite ``axiom`` n times with ``rules`` (dict: symbol -> replacement), a bracketed L-system."""
    s = axiom
    for _ in range(n):
        s = "".join(rules.get(ch, ch) for ch in s)
    return s


def turtle(s, start=(0.0, 0.0), heading=90.0, step=1.0, angle=25.0, decay=0.78, tropism=(0.0, 0.0), bend=0.0,
           jitter=0.0, seed=0):
    """Interpret an L-system string with a 2D turtle. Symbols: F draw a segment, f move, + / - turn
    left / right by ``angle``, [ ] push / pop, ! shorten the step by ``decay`` (also for the rest of the
    branch), K mark a terminal structure (flower, inflorescence), L mark a leaf / foliage. ``tropism`` is
    a direction (e.g. (0, -1) gravitropism) towards which each segment bends with susceptibility ``bend``;
    ``jitter`` (degrees) adds deterministic noise to turns.
    Returns dict(segments=[(p0, p1, parent, order)], marks=[(kind, point, heading)]).
    """
    rng = np.random.default_rng(seed)
    p = np.asarray(start, float)
    h = math.radians(heading)
    st = step
    parent, order = -1, 0
    stack = []
    segs, marks = [], []
    T = np.asarray(tropism, float)
    for ch in s:
        if ch in "Ff":
            d = np.array([math.cos(h), math.sin(h)])
            if bend and np.hypot(*T) > 0:
                cr = d[0] * T[1] - d[1] * T[0]
                h += bend * cr
                d = np.array([math.cos(h), math.sin(h)])
            q = p + d * st
            if ch == "F":
                segs.append((p.copy(), q.copy(), parent, order))
                parent = len(segs) - 1
            p = q
        elif ch in "+-":
            a = math.radians(angle + (rng.normal(0, jitter) if jitter else 0))
            h += a if ch == "+" else -a
        elif ch == "[":
            stack.append((p.copy(), h, st, parent, order))
            order += 1
        elif ch == "]":
            p, h, st, parent, order = stack.pop()
        elif ch == "!":
            st *= decay
        elif ch in "KL":
            marks.append((ch, p.copy(), h))
    return dict(segments=segs, marks=marks)


def _pipe_widths(segs, tip=1.0, exp=2.0):
    """Pipe-model widths: a segment's cross-section is the sum of its children's (da Vinci's rule)."""
    n = len(segs)
    area = np.zeros(n)
    has_child = np.zeros(n, bool)
    for i in range(n - 1, -1, -1):
        par = segs[i][2]
        if not has_child[i]:
            area[i] = tip ** exp
        if par >= 0:
            if not has_child[par]:
                area[par] = 0
                has_child[par] = True
            area[par] += area[i]
    return area ** (1 / exp)


def _draw_tree(ax, segs, width=0.9, max_lw=9.0, token="bark", zorder=5):
    if not segs:
        return np.zeros(0)
    w = _pipe_widths(segs)
    lw = np.clip(width * w, 0.4, max_lw)
    lines = [[s[0], s[1]] for s in segs]
    ax.add_collection(LineCollection(lines, colors=P.edge(tok(token)), linewidths=lw, capstyle="round", zorder=zorder))
    return lw


def _foliage(ax, pts, r, token="leaf", seed=0, zorder=6):
    """Clumps of foliage (overlapping discs) at branch ends."""
    rng = np.random.default_rng(seed)
    discs = []
    for p in pts:
        for _ in range(2):
            q = np.asarray(p) + rng.normal(0, r * 0.35, 2)
            rr = r * rng.uniform(0.7, 1.1)
            t = np.linspace(0, 2 * np.pi, 18)
            discs.append(np.c_[q[0] + rr * np.cos(t), q[1] + rr * np.sin(t)])
    ax.add_collection(PolyCollection(discs, facecolors=P.fill(tok(token)), edgecolors=P.edge(tok(token)), linewidths=0.5,
                                     zorder=zorder))


HABITS = ("excurrent", "fastigiate", "weeping", "leeuwenberg", "dichotomous", "palm")


def lsystem_tree(ax, base, height, habit="excurrent", width=None, foliage=True, seed=0, zorder=5):
    """A tree habit generated by an L-system (see ``lsystem``, ``turtle``), scaled to ``height``.

    habit "excurrent": monopodial leader with tiers of plagiotropic laterals, longer below (a conical
          conifer crown; Massart's model, e.g. Picea, Abies)
          "fastigiate": narrow upright branches (e.g. Populus nigra 'Italica')
          "weeping": pendulous branches bending under gravitropism (e.g. Salix babylonica)
          "leeuwenberg": sympodial: every module ends in an inflorescence and is continued by several
          equal lateral modules (Leeuwenberg's model, e.g. Plumeria)
          "dichotomous": repeated equal forking of the apex (isotomy), as in early land plants
          "palm": unbranched monopodial trunk with a crown of pinnate leaves (Corner's model)
    The drawing fits ``height`` × ``width`` (default 0.8 × height). Returns anchors: trunk, crown, branch,
    apex, and inflorescence / sporangium when present.
    """
    b = np.asarray(base, float)
    width = width or 0.8 * height
    out = dict(base=b)
    if habit == "palm":
        top = b + [0.06 * height, 0.78 * height]
        t = np.linspace(0, 1, 30)
        trunk = np.c_[b[0] + 0.06 * height * t ** 2, b[1] + 0.78 * height * t]
        ax.plot(trunk[:, 0], trunk[:, 1], color=P.edge(tok("bark")), lw=6.0, solid_capstyle="butt", zorder=zorder)
        for k in range(1, 14):  # leaf scars
            q = trunk[int(k / 14 * 29)]
            ax.plot([q[0] - 0.035 * height, q[0] + 0.035 * height], [q[1], q[1] + 0.005 * height], color=P.fill(tok("bark")),
                    lw=0.8, zorder=zorder + 0.1)
        for k, a in enumerate((165, 140, 115, 92, 68, 42, 18, 200, -20)):
            ln = 0.33 * height * (0.75 if a in (200, -20) else 1)
            a_ = math.radians(a)
            tip = top + ln * np.array([math.cos(a_), math.sin(a_)])
            sag = np.array([0, -0.18 * height * abs(math.cos(a_))])
            rach = _bezier(top, (top + tip) / 2 + sag * -0.2 + [0, 0.05 * height], tip + sag, 30)
            ax.plot(rach[:, 0], rach[:, 1], color=P.edge(tok("leaf")), lw=1.4, zorder=zorder + 1)
            segs = []
            for j in range(4, 29, 2):
                p0 = rach[j]
                d = rach[j + 1] - rach[j - 1]
                d /= np.hypot(*d)
                nrm = np.array([-d[1], d[0]])
                L = 0.09 * height * (1 - 0.6 * j / 29)
                for sg in (1, -1):
                    segs.append([p0, p0 + (nrm * sg * 0.75 + d * 0.35) * L - [0, 0.25 * L]])
            ax.add_collection(LineCollection(segs, colors=P.edge(tok("leaf")) if not P.is_dark() else P.fill(tok("leaf")),
                                             linewidths=1.3, capstyle="round", zorder=zorder + 0.9))
        out.update(trunk=b + [0.01 * height, 0.35 * height], crown=top + [0.2 * height, 0.05 * height], apex=top)
        return out
    spec = {  # axiom, rules, iterations, branching angle, decay, tropism, susceptibility
        "excurrent": ("A", {"A": "FF[+B][-B]A", "B": "F[+L][-L]B"}, 9, 80, 0.98, (0, -1), 0.04),
        "fastigiate": ("A", {"A": "F[+B]F[-B]A", "B": "!F[+L][-L]B"}, 7, 30, 0.9, (0, 1), 0.3),
        "weeping": ("FFFFA", {"A": "F[+B][-B]FA", "B": "F[-L]F[+L]B"}, 6, 48, 0.95, (0, -1), 0.3),
        "leeuwenberg": ("FA", {"A": "F[+!A][-!A][!A]"}, 4, 38, 0.72, (0, 1), 0.02),
        "dichotomous": ("A", {"A": "F[+!A][-!A]"}, 7, 22, 0.82, (0, 0), 0.0),
    }[habit]
    axiom, rules, n, ang, dec, trop, bend = spec
    s = lsystem(axiom, rules, n)
    s = s.replace("A", "LK" if habit == "leeuwenberg" else "L").replace("B", "L")
    t = turtle(s, start=(0, 0), step=1.0, angle=ang, decay=dec, tropism=trop, bend=bend, jitter=3.0 if habit != "dichotomous" else 0,
               seed=seed)
    pts = np.array([q for s_ in t["segments"] for q in s_[:2]])
    lo, hi = pts.min(axis=0), pts.max(axis=0)
    sc = min(height / (hi[1] - lo[1]), width / max(hi[0] - lo[0], 1e-9))
    off = np.array([(lo[0] + hi[0]) / 2 * 0, lo[1]])
    segs = [((p0 - off) * sc + b, (p1 - off) * sc + b, par, o) for p0, p1, par, o in t["segments"]]
    marks = [(k, (p - off) * sc + b, h) for k, p, h in t["marks"]]
    lw = _draw_tree(ax, segs, width={"excurrent": 1.5, "fastigiate": 1.2, "weeping": 1.5, "leeuwenberg": 1.4,
                                     "dichotomous": 1.2}[habit], zorder=zorder)
    ends = [p for k, p, h in marks if k == "L"]
    if foliage and habit != "dichotomous":
        _foliage(ax, ends, height * {"excurrent": 0.025, "fastigiate": 0.03, "weeping": 0.02, "leeuwenberg": 0.045}[habit],
                 token="leaf", seed=seed, zorder=zorder + 1)
    if habit == "dichotomous":
        for p in ends:
            ax.add_patch(Ellipse(p, 0.025 * height, 0.04 * height, facecolor=_fill("ovule"), edgecolor=_edge("ovule"), lw=0.6,
                                 zorder=zorder + 1))
        out["sporangium"] = ends[len(ends) // 2]
    if habit == "leeuwenberg":
        for k, p, h in marks:
            if k == "K":
                flower(ax, p + [0, 0.03 * height], 0.022 * height, zorder=zorder + 2)
        out["inflorescence"] = [p for k, p, h in marks if k == "K"][0]
    trunk_i = int(np.argmax(lw))
    out["trunk"] = (segs[trunk_i][0] + segs[trunk_i][1]) / 2
    br = [i for i, s_ in enumerate(segs) if s_[3] == 1]
    if br:
        i = br[len(br) // 3]
        out["branch"] = (segs[i][0] + segs[i][1]) / 2
    out["apex"] = max((s_[1] for s_ in segs), key=lambda q: q[1])
    out["crown"] = b + [0, 0.7 * height]
    return out


def crown_tree(ax, base, height, crown=(0.55, 0.42), attractors=420, seed=0, foliage=True, zorder=5):
    """A broad-crowned (decurrent) tree grown by space colonisation (Runions et al. 2007): attraction
    points fill an elliptical crown; every node grows towards the points within its radius of influence,
    points within the kill distance are removed. Branch widths follow the pipe model.
    ``crown`` = (half-width, half-height) as fractions of the height. Returns anchors: trunk, branch, crown.
    """
    from scipy.spatial import cKDTree

    b = np.asarray(base, float)
    H = height
    rx, ry = crown[0] * H, crown[1] * H
    cc = b + [0, H - ry]
    rng = np.random.default_rng(seed)
    A = []
    while len(A) < attractors:
        q = rng.uniform(-1, 1, 2)
        if q @ q < 1 and q[1] > -0.75:
            A.append(cc + q * [rx, ry])
    A = np.array(A)
    step = 0.022 * H
    di, dk = 0.16 * H, 0.035 * H
    nodes = [b.copy()]
    parent = [-1]
    # trunk up to the crown
    while nodes[-1][1] < cc[1] - ry * 0.55:
        nodes.append(nodes[-1] + [0, step])
        parent.append(len(nodes) - 2)
    for _ in range(140):
        if len(A) == 0:
            break
        tree = cKDTree(np.array(nodes))
        d, idx = tree.query(A, distance_upper_bound=di)
        grow = {}
        for a, dd, i in zip(A, d, idx):
            if np.isfinite(dd):
                v = (a - nodes[i]) / max(dd, 1e-9)
                grow.setdefault(int(i), []).append(v)
        if not grow:
            break
        for i, vs in grow.items():
            v = np.sum(vs, axis=0)
            nv = np.hypot(*v)
            if nv < 1e-6:
                continue
            nodes.append(nodes[i] + v / nv * step)
            parent.append(i)
        tree = cKDTree(np.array(nodes))
        d, _ = tree.query(A)
        A = A[d > dk]
    segs = [(nodes[parent[i]], nodes[i], parent[i] - 1 if parent[i] > 0 else -1, 0) for i in range(1, len(nodes))]
    # fix parent indices to segment indices (segment j ends at node j + 1)
    segs = [(p0, p1, (parent[i + 1] - 1), o) for i, (p0, p1, _, o) in enumerate(segs)]
    _draw_tree(ax, segs, width=0.85, max_lw=8.0, zorder=zorder)
    if foliage:
        has_child = set(s[2] for s in segs)
        ends = [s[1] for j, s in enumerate(segs) if j not in has_child]
        _foliage(ax, ends, 0.04 * H, seed=seed, zorder=zorder + 1)
    out = dict(base=b, trunk=b + [0, 0.15 * H], crown=cc + [rx * 0.6, ry * 0.4])
    mid = [j for j, s in enumerate(segs) if 0.35 * H < s[1][1] - b[1] < 0.6 * H and abs(s[1][0] - b[0]) > 0.12 * H]
    if mid:
        out["branch"] = segs[mid[0]][1]
    return out


MODULE_TOKENS = ("dna", "rna", "enzyme", "protein", "antibody", "receptor")


def _mod_color(k):
    t = MODULE_TOKENS[k % len(MODULE_TOKENS)]
    return P.fill(t) if P.is_dark() else P.edge(t)


def branching(ax, base, height, kind="monopodial", zorder=5):
    """Branching patterns as module diagrams; each module (the product of one apical meristem) has its
    own colour. kind "monopodial" (the main axis grows on from its terminal bud; laterals subordinate),
    "sympodial" (monochasial: each module ends in a flower or dies back and growth continues from one
    lateral bud below it), "dichasial" (sympodial with two continuation modules, a false dichotomy) or
    "dichotomous" (the apex itself divides into two equal apices: true dichotomy).
    Returns anchors: apex (terminal bud), module (list of module midpoints), flower, lateral, fork.
    """
    b = np.asarray(base, float)
    H = height
    out = dict(module=[])
    lw = 2.6 * _lw(H, 1.0, 4.0)

    def seg(p, q, k, w=1.0):
        ax.plot([p[0], q[0]], [p[1], q[1]], color=_mod_color(k), lw=lw * w, solid_capstyle="round", zorder=zorder)

    def bud(p, ang, k):
        ax.add_patch(Ellipse(p, 0.04 * H, 0.075 * H, angle=ang - 90, facecolor=_fill("bud"), edgecolor=_edge("bud"), lw=0.7,
                             zorder=zorder + 1))

    if kind == "monopodial":
        top = b + [0, H]
        seg(b, top, 0)
        bud(top + [0, 0.03 * H], 90, 0)
        out["apex"] = top + [0, 0.03 * H]
        out["module"].append(b + [0, 0.5 * H])
        for j, (y, side) in enumerate(((0.25, 1), (0.45, -1), (0.65, 1), (0.82, -1))):
            p = b + [0, y * H]
            ln = (0.42 - 0.35 * y) * H
            a = math.radians(90 - side * 55)
            q = p + ln * np.array([math.cos(a), math.sin(a)])
            seg(p, q, 1, 0.75)
            bud(q + 0.02 * H * np.array([math.cos(a), math.sin(a)]), math.degrees(a), 1)
            if j == 0:
                out["lateral"] = (p + q) / 2
                for f in (0.5,):
                    pp = p + (q - p) * f
                    a2 = a + side * math.radians(40) * -1
                    qq = pp + 0.1 * H * np.array([math.cos(a2), math.sin(a2)])
                    seg(pp, qq, 2, 0.5)
        return out
    if kind == "sympodial":
        p = b
        ang = 90.0
        for k in range(5):
            ln = (0.36 if k == 0 else 0.26) * H * (0.92 ** k)
            u = np.array([math.cos(math.radians(ang)), math.sin(math.radians(ang))])
            q = p + u * ln
            seg(p, q, k)
            out["module"].append((p + q) / 2)
            flower(ax, q + u * 0.025 * H, 0.03 * H, zorder=zorder + 1)
            out.setdefault("flower", q + u * 0.025 * H)
            p = p + u * ln * 0.72
            ang = 90 + (24 if k % 2 == 0 else -24)
        out["apex"] = out["module"][-1]
        return out
    if kind in ("dichasial", "dichotomous"):
        def rec(p, ang, ln, d, k):
            u = np.array([math.cos(math.radians(ang)), math.sin(math.radians(ang))])
            q = p + u * ln
            seg(p, q, k if kind == "dichasial" else 0, 1.0 - 0.15 * d)
            if d == 0:
                out["module"].append((p + q) / 2)
            if d == 3:
                if kind == "dichotomous":
                    bud(q + u * 0.02 * H, ang, 0)
                    out.setdefault("apex", q + u * 0.02 * H)
                else:
                    flower(ax, q + u * 0.02 * H, 0.025 * H, zorder=zorder + 1)
                return
            if kind == "dichasial":
                flower(ax, q + u * 0.02 * H, 0.028 * H * (1 - 0.15 * d), zorder=zorder + 1)
                out.setdefault("flower", q + u * 0.02 * H)
                fork = p + u * ln * 0.8
                for j, sg in enumerate((-1, 1)):
                    rec(fork, ang + sg * 34, ln * 0.68, d + 1, 2 * k + 1 + j)
            else:
                out.setdefault("fork", q)
                for sg in (-1, 1):
                    rec(q, ang + sg * 26, ln * 0.78, d + 1, 0)
        rec(b, 90.0, 0.32 * H if kind == "dichasial" else 0.3 * H, 0, 0)
        return out
    raise ValueError(f"unknown branching {kind!r}")


def bud(ax, xy, size, angle=90.0, zorder=7):
    """A bud (ovoid, bud scales suggested by a midline) pointing along ``angle``; returns its centre."""
    xy = np.asarray(xy, float)
    ax.add_patch(Ellipse(xy, size * 0.55, size, angle=angle - 90, facecolor=_fill("bud"), edgecolor=_edge("bud"), lw=0.8,
                         zorder=zorder))
    u = np.array([math.cos(math.radians(angle)), math.sin(math.radians(angle))])
    ax.plot(*np.array([xy - u * size * 0.1, xy + u * size * 0.42]).T, color=_edge("bud"), lw=0.6, zorder=zorder + 0.1)
    return xy
