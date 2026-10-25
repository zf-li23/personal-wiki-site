"""Zoomorph: animal morphology generated from rules, so that characters can be varied systematically.

Every drawing is parametric (proportions, counts, types) rather than a fixed template, which makes it
suitable for comparison sheets: one generator, many taxa, the diagnostic character changed and labelled.

    from wikibio import zoomorph as zm
    a = zm.insect(ax, (5, 5), 4.0, order="Coleoptera")        dorsal view, wings and parts by order
    zm.insect(ax, (5, 5), 4.0, order="Orthoptera", view="lateral")
    zm.antenna(ax, (1, 1), 80, 2.0, "geniculate")              scape, pedicel, flagellum (+ club, arista ...)
    zm.head(ax, (3, 3), 1.0, "siphoning")                     lateral head, mouthparts coloured by homology
    zm.leg(ax, (2, 6), "raptorial", length=3)                  coxa, trochanter, femur, tibia, tarsus, claws
    zm.wing(ax, (0, 0), 3, "odonata_fore")                     outline + venation style of the order
    zm.raup_shell(ax, (5, 5), 3, W=2, D=0.1, T=2)             Raup's coiling model (gastropod, ammonoid, bivalve)
    zm.suture(ax, (1, 1), 6, "ammonitic")                      cephalopod suture lines
    zm.sea_star(ax, c, 2); zm.medusa(ax, c, 2); zm.ctenophore(ax, c, 2); zm.sponge(ax, c, 3, 3)
    zm.forelimb(ax, (5, 5), 6, "bat")                          tetrapod forelimb, one colour per bone

Colour conventions (palette tokens, the same in every figure):
    insect mouthparts ``MOUTH``: labrum yellow, mandible orange, maxilla blue, labium green, so that
        homologues read across types (the lepidopteran proboscis is maxillary, the bug's beak labial);
    antenna ``ANT``: scape, pedicel, flagellum; leg ``LEG``: coxa ... tarsus;
    wing types ``WING``: membrane, elytron, tegmen, corium (hemelytron), scales, haltere;
    forelimb bones ``BONE``: humerus, radius, ulna, carpals, metacarpals, phalanges.
Functions return dicts of anchors (canvas points) named by the anatomical part, for ``bio.callout``.
Angles are in degrees, counter-clockwise from the +x axis of the canvas.
"""

import math

import numpy as np
from matplotlib.collections import PolyCollection
from matplotlib.patches import Circle, PathPatch
from matplotlib.path import Path

from . import palette as P
from .core import LINE, polyline, smooth_closed

MOUTH = {"labrum": "labrum", "mandible": "mandible", "maxilla": "maxilla", "labium": "labium", "hypopharynx": "protein"}
ANT = {"scape": "antibody", "pedicel": "drug", "flagellum": "channel"}
LEG = {"coxa": "coxa", "trochanter": "trochanter", "femur": "femur", "tibia": "tibia", "tarsus": "tarsus",
       "pretarsus": "neutral"}
WING = {"membrane": "er", "elytron": "elytron", "tegmen": "tegmen", "corium": "bract", "scales": "antibody",
        "haltere": "haltere"}
BONE = {"humerus": "humerus", "radius": "radius", "ulna": "ulna", "carpals": "carpals", "metacarpals": "metacarpals",
        "phalanges": "phalanges"}
BODY = "animal"  # insect cuticle, radiate bodies
EYE = "neutral"  # compound eyes: drawn in the neutral token's outline shade
SHELL = "bone"


# ------------------------------------------------------------------ geometry helpers


def _dir(deg):
    r = math.radians(deg)
    return np.array([math.cos(r), math.sin(r)])


def _perp(u):
    return np.array([-u[1], u[0]])


class _Frame:
    """Local (x, y) -> canvas: mirror local x (optional), scale, rotate by ``angle`` degrees, translate."""

    def __init__(self, origin, scale=1.0, angle=0.0, mirror=False):
        self.o = np.asarray(origin, float)
        self.s = float(scale)
        self.m = -1.0 if mirror else 1.0
        self.angle = angle
        c, s = math.cos(math.radians(angle)), math.sin(math.radians(angle))
        self.R = np.array([[c, -s], [s, c]])

    def __call__(self, pts):
        a = np.asarray(pts, float)
        one = a.ndim == 1
        a = np.atleast_2d(a) * np.array([self.m, 1.0]) * self.s
        out = a @ self.R.T + self.o
        return out[0] if one else out

    def ang(self, deg):
        """A local direction (degrees) in canvas degrees."""
        if self.m < 0:
            deg = 180.0 - deg
        return deg + self.angle


def _patch(ax, pts, token=None, face=None, edge=None, lw=LINE * 0.8, z=5, alpha=None):
    v = np.asarray(pts, float)
    path = Path(np.vstack([v, v[:1]]), closed=True)
    fc = face if face is not None else P.fill(token)
    ec = edge if edge is not None else P.edge(token)
    p = PathPatch(path, facecolor=fc, edgecolor=ec, lw=lw, zorder=z, joinstyle="round",
                  alpha=alpha if alpha is not None and alpha < 0.999 else None)
    ax.add_patch(p)
    return p


def _line(ax, pts, color, lw=LINE * 0.6, z=6, dashed=False, **kw):
    p = np.asarray(pts, float)
    return ax.plot(p[:, 0], p[:, 1], color=color, lw=lw, zorder=z, solid_capstyle="round", solid_joinstyle="round",
                   ls=(0, (3, 2)) if dashed else "-", **kw)[0]


def _rod(a, b, widths, n=24, cap=0.9):
    """Outline of a rod from a to b with a width profile (``widths`` sampled evenly from a to b) and round caps."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    d = b - a
    L = float(np.linalg.norm(d)) or 1e-9
    u = d / L
    nv = _perp(u)
    w = np.atleast_1d(np.asarray(widths, float))
    t = np.linspace(0, 1, n)
    h = np.interp(t, np.linspace(0, 1, len(w)), w) / 2
    axis = a + np.outer(t * L, u)
    left, right = axis + np.outer(h, nv), axis - np.outer(h, nv)
    out = [left]
    if cap:
        ph = np.linspace(math.pi / 2, -math.pi / 2, 9)[1:-1]
        out.append(b + h[-1] * (np.outer(np.cos(ph) * cap, u) + np.outer(np.sin(ph), nv)))
    out.append(right[::-1])
    if cap:
        ph = np.linspace(-math.pi / 2, -3 * math.pi / 2, 9)[1:-1]
        out.append(a + h[0] * (np.outer(np.cos(ph) * cap, u) + np.outer(np.sin(ph), nv)))
    return np.vstack(out)


def _spline(points, n=80):
    """An open Catmull-Rom curve through ``points`` (end points kept)."""
    p = np.asarray(points, float)
    p = np.vstack([2 * p[0] - p[1], p, 2 * p[-1] - p[-2]])
    out = []
    per = max(2, n // (len(p) - 3))
    for i in range(1, len(p) - 2):
        p0, p1, p2, p3 = p[i - 1], p[i], p[i + 1], p[i + 2]
        for t in np.linspace(0, 1, per, endpoint=False):
            t2, t3 = t * t, t * t * t
            out.append(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t2 + (-p0 + 3 * p1 - 3 * p2 + p3) * t3))
    out.append(p[-2])
    return np.array(out)


def _band(path, w0, w1=None):
    """A closed band of width w0 (tapering to w1) along an open path."""
    q, nrm, _ = polyline(path, n=max(30, len(path)), closed=False)
    w = np.linspace(w0, w0 if w1 is None else w1, len(q))[:, None] / 2
    return np.vstack([q + nrm * w, (q - nrm * w)[::-1]])


def _ellipse(c, rx, ry, angle=0.0, n=60):
    t = np.linspace(0, 2 * np.pi, n, endpoint=False)
    p = np.c_[rx * np.cos(t), ry * np.sin(t)]
    a = math.radians(angle)
    R = np.array([[math.cos(a), -math.sin(a)], [math.sin(a), math.cos(a)]])
    return p @ R.T + np.asarray(c, float)


def _wash(token, k=0.55):
    """An opaque pale tint of a token's fill (light) or a dark tint (dark theme)."""
    return P.mix(P.fill(token), P.surface(), 0.72 if P.is_dark() else k)


def _tok(colored, part_token, plain):
    return part_token if colored else plain


# ------------------------------------------------------------------ antennae

ANTENNA_TYPES = ("filiform", "setaceous", "moniliform", "serrate", "clavate", "capitate", "pectinate", "plumose",
                 "lamellate", "geniculate", "aristate")


def _antenna_spec(kind, n=None):
    """Segments (part, length, widths, extra) in units of the antenna length (normalised later)."""
    S = [("scape", 0.11, (0.06, 0.075, 0.065), {}), ("pedicel", 0.055, (0.05, 0.055, 0.05), {})]
    if kind == "filiform":
        k = n or 10
        S += [("flagellum", 0.084, (0.038, 0.042, 0.04), {}) for _ in range(k)]
    elif kind == "setaceous":
        k = n or 14
        S = [("scape", 0.11, (0.07, 0.078, 0.066), {}), ("pedicel", 0.06, (0.055, 0.06, 0.052), {})]
        for i in range(k):
            w = 0.044 * (1 - i / k) + 0.008
            S.append(("flagellum", 0.058, (w, w * 0.92), {}))
    elif kind == "moniliform":
        k = n or 11
        S += [("flagellum", 0.075, (0.02, 0.07, 0.072, 0.02), {}) for _ in range(k)]
    elif kind == "serrate":
        k = n or 9
        S += [("flagellum", 0.088, (0.045, 0.045), {"serrate": 0.07}) for _ in range(k)]
    elif kind == "clavate":
        k = n or 10
        for i in range(k):
            w = 0.035 + 0.075 * (i / (k - 1)) ** 1.6
            S.append(("flagellum", 0.08, (w * 0.8, w, w * 0.9), {"club": i >= k - 4}))
    elif kind == "capitate":
        k = n or 8
        for i in range(k - 3):
            S.append(("flagellum", 0.075, (0.032, 0.036, 0.034), {}))
        for i in range(3):
            S.append(("flagellum", 0.075, (0.07, 0.14, 0.15, 0.12), {"club": True}))
    elif kind == "pectinate":
        k = n or 10
        S += [("flagellum", 0.075, (0.035, 0.038), {"branch": 0.2 * (0.55 + 0.45 * math.sin(math.pi * (i + 1) / (k + 1)))})
              for i in range(k)]
    elif kind == "plumose":
        k = n or 13
        S += [("flagellum", 0.064, (0.02, 0.026, 0.02), {"whorl": 0.15 * (1 - 0.45 * i / k)}) for i in range(k)]
    elif kind == "lamellate":
        k = n or 5
        S += [("flagellum", 0.075, (0.04, 0.048, 0.045), {}) for _ in range(k)]
        S += [("flagellum", 0.055, (0.05, 0.05), {"lamella": (0.3, 0.07), "club": True}) for _ in range(3)]
    elif kind == "geniculate":
        k = n or 10
        S = [("scape", 0.36, (0.055, 0.06, 0.075), {}), ("pedicel", 0.06, (0.05, 0.06, 0.055), {"elbow": 72})]
        for i in range(k):
            w = 0.042 + (0.02 if i >= k - 3 else 0)
            S.append(("flagellum", 0.058, (w * 0.85, w, w * 0.95), {}))
    elif kind == "aristate":
        S = [("scape", 0.1, (0.07, 0.09, 0.08), {}), ("pedicel", 0.17, (0.1, 0.15, 0.13), {}),
             ("flagellum", 0.3, (0.11, 0.19, 0.21, 0.19, 0.15, 0.08), {"arista": 1.05})]
    else:
        raise ValueError(f"unknown antenna type {kind!r}; one of {ANTENNA_TYPES}")
    return S


def antenna(ax, base, angle, length, kind="filiform", colored=True, color=BODY, curve=0.0, mirror=False, width=1.0,
            segments=None, thickness=None, lw=LINE * 0.6, z=7):
    """One insect antenna from ``base`` towards ``angle`` (degrees), ``length`` long.

    kind: filiform, setaceous, moniliform, serrate, clavate, capitate, pectinate, plumose, lamellate,
    geniculate (elbowed after the long scape), aristate (three segments, the postpedicel bearing a
    feathery arista). ``colored`` paints scape, pedicel and flagellum with ``ANT`` (else ``color``);
    ``curve`` bends the antenna (degrees per segment, sign = direction); ``mirror`` puts lateral
    processes (serrations, pectinations, lamellae, the elbow) on the other side; ``segments`` overrides
    the number of flagellomeres; ``width`` scales the thickness, or ``thickness`` sets the flagellum
    width in canvas units (so long and short antennae of one insect are equally slender).
    Returns {"base", "tip", "scape", "pedicel", "flagellum", "club", "branch", "lamella", "arista", "setae"}.
    """
    spec = _antenna_spec(kind, segments)
    total = sum(s[1] for s in spec)
    k = length / total
    kw = (thickness / 0.042) if thickness else k * width
    side = -1.0 if mirror else 1.0  # lateral processes on the right of the direction (side=+1)
    p = np.asarray(base, float)
    a = float(angle)
    out = {"base": tuple(p), "flagellum": [], "club": []}
    thin = lw * max(0.35, min(1.0, length / 2.5))
    for i, (part, L, ws, extra) in enumerate(spec):
        tok = _tok(colored, ANT[part], color)
        u = _dir(a)
        nv = _perp(u)
        L *= k
        w = np.asarray(ws, float) * kw
        q = p + u * L
        if "serrate" in extra:
            e = extra["serrate"] * kw
            h = w[0] / 2
            poly = [p + nv * h, q + nv * h * 1.1, q - nv * (h + e) * side + u * 0.0, p + u * L * 0.25 - nv * h * side]
            poly = np.array(poly) if side > 0 else np.array([p + nv * h * -1, q - nv * h * 1.1, q + nv * (h + e), p + u * L * 0.25 + nv * h])
            _patch(ax, poly, tok, lw=thin, z=z)
        else:
            _patch(ax, _rod(p, q, w, n=28, cap=0.6), tok, lw=thin, z=z)
        mid = p + u * L / 2
        if "branch" in extra:  # pectination: a long lateral process
            bl = extra["branch"] * length
            b0 = mid - nv * side * w.max() * 0.3
            b1 = b0 + _dir(a - side * 62) * bl
            _patch(ax, _rod(b0, b1, (w.max() * 0.45, w.max() * 0.3), n=8, cap=0.6), tok, lw=thin * 0.8, z=z - 0.1)
            out["branch"] = tuple(b1 * 0.6 + b0 * 0.4)
        if "whorl" in extra:  # plumose: whorls of long setae on both sides
            sl = extra["whorl"] * length
            for s in (1, -1):
                for j, off in enumerate((-0.25, 0.25)):
                    s0 = mid + u * L * off
                    s1 = s0 + _dir(a + s * (55 + 12 * j)) * sl
                    _line(ax, [s0, s1], P.edge(tok), lw=thin * 0.55, z=z - 0.1)
            out["setae"] = tuple(mid + _dir(a + 60) * sl * 0.7)
        if "lamella" in extra:  # lamellate club: plate-like flagellomeres extended to one side
            ll, lwid = extra["lamella"]
            l0 = mid
            l1 = l0 + _dir(a - side * 58) * ll * length
            _patch(ax, _rod(l0, l1, (lwid * length * 0.7, lwid * length, lwid * length * 0.8), n=14, cap=1.0), tok,
                   lw=thin, z=z + 0.1 + i * 0.01)
            out["lamella"] = tuple((l0 + l1) / 2)
        if "arista" in extra:  # aristate: a dorsal bristle from the base of the postpedicel, plumose
            al = extra["arista"] * length
            a0 = p + u * L * 0.32 - nv * side * w.max() * 0.38
            ang = a - side * 30
            pts = [a0 + _dir(ang) * al * t + _dir(ang - side * 90) * al * 0.06 * math.sin(math.pi * t) for t in np.linspace(0, 1, 20)]
            pts = np.array(pts)
            ec = P.edge(tok)
            _patch(ax, _band(pts, w.max() * 0.16, w.max() * 0.03), tok, lw=thin * 0.5, z=z + 0.2)
            for t in np.linspace(0.12, 0.85, 9):
                j = int(t * 19)
                for s in (1, -1):
                    h = al * 0.07 * (1 - 0.6 * t)
                    _line(ax, [pts[j], pts[j] + _dir(ang + s * 55) * h], ec, lw=thin * 0.5, z=z + 0.2)
            out["arista"] = tuple(pts[12])
        if part == "flagellum":
            out["flagellum"].append(tuple(mid))
            if extra.get("club"):
                out["club"].append(tuple(mid))
        else:
            out[part] = tuple(mid)
        p = q - u * L * 0.04
        a += curve + side * extra.get("elbow", 0) * -1.0
    out["tip"] = tuple(p)
    out["flagellum"] = out["flagellum"][len(out["flagellum"]) // 2] if out["flagellum"] else out["tip"]
    out["club"] = out["club"][len(out["club"]) // 2] if out["club"] else None
    return out


# ------------------------------------------------------------------ heads and mouthparts

MOUTHPART_TYPES = ("chewing", "piercing-sucking", "siphoning", "sponging", "vestigial")


def head(ax, at, size, mouthparts="chewing", facing="right", colored=True, color=BODY, antenna_kind=None,
         antenna_length=None, antenna_thickness=None, lw=LINE * 0.75, z=10):
    """A lateral view of an insect head with its mouthparts; ``size`` is half the head capsule's height.

    mouthparts: "chewing" (hypognathous orthopteran: labrum, toothed mandibles, maxillae with 5-segmented
    palps, labium with 3-segmented palps), "piercing-sucking" (heteropteran: a 4-segmented labial rostrum
    sheathing mandibular and maxillary stylets, shown in feeding pose), "siphoning" (lepidopteran: a coiled
    proboscis of the two maxillary galeae, upturned labial palps, mandibles absent), "sponging" (muscid fly:
    rostrum, haustellum of the labium, labella with pseudotracheae, maxillary palps; mandibles absent),
    "vestigial" (adult mayfly: non-functional remnants). ``colored`` paints parts with ``MOUTH``.
    ``antenna_kind`` / ``antenna_length`` add an antenna at the socket (``None``: the default of the type;
    ``False``: none; ``antenna_thickness`` in canvas units). Returns anchors: "head", "eye", "antenna" (socket), and one per part drawn
    ("labrum", "mandible", "maxilla", "maxillary_palp", "labium", "labial_palp", "rostrum", "stylets",
    "proboscis", "haustellum", "labella").
    """
    F = _Frame(at, size, 0.0, mirror=(facing == "left"))
    E = P.edge(color)
    out = {}

    def part(pts, name, key=None, smooth=True, zz=0.0):
        tok = _tok(colored, MOUTH[name], color)
        v = smooth_closed(pts, 120) if smooth else np.asarray(pts, float)
        _patch(ax, F(v), tok, lw=lw, z=z + zz)
        out[key or name] = tuple(F(np.mean(np.asarray(pts, float), axis=0)))

    def chain(base, deg, lengths, w0, w1, name, key, zz=0.3):
        tok = _tok(colored, MOUTH[name], color)
        p = np.asarray(base, float)
        mids = []
        for i, L in enumerate(lengths):
            ww = w0 + (w1 - w0) * i / max(1, len(lengths) - 1)
            q = p + _dir(deg + 6 * i) * L
            _patch(ax, F(_rod(p, q, (ww, ww * 1.05, ww * 0.9), n=10, cap=0.7)), tok, lw=lw * 0.8, z=z + zz)
            mids.append((p + q) / 2)
            p = q - _dir(deg + 6 * i) * L * 0.05
        out[key] = tuple(F(mids[len(mids) // 2]))
        return p

    mp = mouthparts
    if mp in ("chewing", "vestigial"):
        cap = _ellipse((0, 0), 0.8, 1.0)
        eye_c, eye_r, sock = (0.02, 0.34), (0.3, 0.42), (0.47, 0.5)
        ak, al, adeg = "filiform", 1.6, 62
    elif mp == "piercing-sucking":
        cap = smooth_closed([(-0.95, 0.15), (-0.6, 0.5), (0.1, 0.58), (0.75, 0.38), (1.22, 0.06), (1.25, -0.1), (0.9, -0.32),
                             (0.2, -0.55), (-0.6, -0.5), (-0.95, -0.2)], 160)
        eye_c, eye_r, sock = (-0.38, 0.22), (0.27, 0.3), (0.62, 0.12)
        ak, al, adeg = "filiform", 1.5, 38
    elif mp == "siphoning":
        cap = _ellipse((0, 0), 0.75, 0.82)
        eye_c, eye_r, sock = (0.02, 0.08), (0.5, 0.56), (0.25, 0.74)
        ak, al, adeg = "clavate", 1.7, 72
    elif mp == "sponging":
        cap = smooth_closed([(-0.5, 0.8), (0.1, 0.95), (0.5, 0.72), (0.66, 0.15), (0.52, -0.55), (0.1, -0.85), (-0.4, -0.72),
                             (-0.62, 0.0)], 160)
        eye_c, eye_r, sock = (-0.06, 0.16), (0.46, 0.64), (0.56, 0.36)
        ak, al, adeg = "aristate", 0.55, -55
    else:
        raise ValueError(f"unknown mouthpart type {mp!r}; one of {MOUTHPART_TYPES}")

    _patch(ax, F(cap), color, lw=lw, z=z + 0.5)
    out["head"] = tuple(F((-0.35, -0.1) if mp != "piercing-sucking" else (0.3, -0.2)))
    _patch(ax, F(_ellipse(eye_c, *eye_r)), face=P.edge(EYE), edge=P.edge(EYE), lw=lw * 0.6, z=z + 0.6)
    _patch(ax, F(_ellipse((eye_c[0] + eye_r[0] * 0.3, eye_c[1] + eye_r[1] * 0.35), eye_r[0] * 0.22, eye_r[1] * 0.16)),
           face=P.light(EYE), edge=P.light(EYE), lw=0, z=z + 0.65)
    out["eye"] = tuple(F(eye_c))
    out["antenna"] = tuple(F(sock))
    if antenna_kind is not False:
        k = antenna_kind or ak
        L = antenna_length if antenna_length is not None else al
        antenna(ax, F(sock), F.ang(adeg), L * size, k, colored=colored, color=color, curve=-2 if F.m > 0 else 2,
                mirror=(F.m < 0), lw=lw * 0.8, thickness=antenna_thickness if k not in ("aristate", "lamellate") else None,
                z=z + 0.7)

    if mp == "chewing":
        part([(0.42, -0.8), (0.72, -0.82), (0.78, -1.2), (0.6, -1.34), (0.44, -1.2)], "labrum", zz=0.45)
        mand = [(0.1, -0.78), (0.48, -0.86), (0.6, -1.28), (0.52, -1.36), (0.56, -1.45), (0.42, -1.45), (0.45, -1.56),
                (0.27, -1.42), (0.06, -1.08)]
        part(mand, "mandible", smooth=False, zz=0.4)
        part([(-0.22, -0.88), (0.08, -0.98), (0.16, -1.5), (0.02, -1.62), (-0.16, -1.3)], "maxilla", zz=0.3)
        chain((-0.02, -1.22), -62, [0.16, 0.16, 0.2, 0.2, 0.18], 0.09, 0.075, "maxilla", "maxillary_palp", zz=0.35)
        part([(-0.62, -0.8), (-0.24, -0.92), (-0.2, -1.5), (-0.42, -1.6), (-0.6, -1.22)], "labium", zz=0.25)
        chain((-0.42, -1.4), -104, [0.17, 0.18, 0.18], 0.09, 0.08, "labium", "labial_palp", zz=0.28)
    elif mp == "vestigial":
        part([(0.2, -0.88), (0.45, -0.9), (0.42, -1.05), (0.24, -1.05)], "maxilla", zz=0.3)
        part([(-0.25, -0.9), (0.05, -0.95), (0.02, -1.1), (-0.22, -1.08)], "labium", zz=0.25)
    elif mp == "piercing-sucking":
        part([(1.0, -0.2), (1.22, -0.14), (1.2, -0.34), (1.06, -0.42)], "labrum", smooth=False, zz=0.45)
        tok = _tok(colored, MOUTH["labium"], color)
        p = np.array([1.0, -0.33])
        mids = []
        for i, L in enumerate((0.42, 0.48, 0.45, 0.36)):
            d = _dir(-80 + 3 * i)
            q = p + d * L
            w = 0.18 - 0.025 * i
            _patch(ax, F(_rod(p, q, (w, w * 1.05, w * 0.92), n=12, cap=0.6)), tok, lw=lw * 0.8, z=z + 0.3)
            mids.append((p + q) / 2)
            p = q - d * 0.02
        out["labium"] = out["rostrum"] = tuple(F(mids[1]))
        d = _dir(-77)
        nv = _perp(d)
        for s, nm in ((1, "mandible"), (-1, "maxilla")):
            a0 = p - d * 0.05 + nv * s * 0.025
            a1 = a0 + d * 0.7 + nv * s * 0.06
            _line(ax, F([a0, a0 + d * 0.35 + nv * s * 0.015, a1]), P.edge(_tok(colored, MOUTH[nm], color)), lw=lw * 1.8, z=z + 0.25)
        out["stylets"] = tuple(F(p + d * 0.45))
        out["mandible"] = tuple(F(p + d * 0.6 + nv * 0.05))
        out["maxilla"] = tuple(F(p + d * 0.6 - nv * 0.05))
    elif mp == "siphoning":
        part([(0.1, -0.62), (0.4, -0.62), (0.42, -0.78), (0.12, -0.8)], "labium", key="labium", zz=0.35)
        chain((0.38, -0.62), 48, [0.32, 0.32, 0.22], 0.17, 0.11, "labium", "labial_palp", zz=0.5)
        th = np.linspace(0, 2.3 * 2 * np.pi, 160)
        rr = 0.46 * np.exp(-th / 9.5)
        cx, cy = 0.18, -1.32
        spiral = np.c_[cx + rr * np.cos(th + 0.25 * np.pi), cy + rr * np.sin(th + 0.25 * np.pi)]
        lead = _spline([(0.22, -0.72), (0.38, -0.85), spiral[0]], 20)
        path = np.vstack([lead, spiral[1:]])
        tok = _tok(colored, MOUTH["maxilla"], color)
        _patch(ax, F(_band(path, 0.11, 0.045)), tok, lw=lw * 0.8, z=z + 0.2)
        out["proboscis"] = out["maxilla"] = tuple(F(spiral[25]))
    elif mp == "sponging":
        _patch(ax, F(smooth_closed([(-0.08, -0.7), (0.42, -0.68), (0.5, -1.12), (0.06, -1.2)], 80)),
               face=P.light(color), edge=E, lw=lw, z=z + 0.2)
        out["rostrum"] = tuple(F((0.2, -0.95)))
        chain((0.42, -0.84), -28, [0.18, 0.18], 0.07, 0.12, "maxilla", "maxillary_palp", zz=0.4)
        out["maxilla"] = out["maxillary_palp"]
        part([(0.06, -1.12), (0.5, -1.1), (0.56, -1.62), (0.14, -1.64)], "labium", key="haustellum", zz=0.3)
        part([(0.46, -1.1), (0.58, -1.1), (0.62, -1.56), (0.52, -1.58)], "labrum", smooth=False, zz=0.35)
        tok = _tok(colored, MOUTH["labium"], color)
        lab = _ellipse((0.36, -1.82), 0.44, 0.21, n=80)
        _patch(ax, F(lab), face=P.light(tok), edge=P.edge(tok), lw=lw, z=z + 0.32)
        for k in range(-3, 4):
            t = np.linspace(0, 1, 12)
            pts = np.c_[0.36 + 0.4 * t * math.sin(k * 0.38), -1.66 - 0.32 * t * math.cos(k * 0.38) * 0.6]
            _line(ax, F(pts), P.edge(tok), lw=lw * 0.45, z=z + 0.33)
        out["labella"] = tuple(F((0.36, -1.86)))
        out["labium"] = out["haustellum"]
    return out


# ------------------------------------------------------------------ legs

LEG_TYPES = ("cursorial", "saltatorial", "raptorial", "fossorial", "natatorial")

# segments: (part, length, widths); extras by part. Default (plate) pose angles: coxa, trochanter, femur, tibia, tarsus.
_LEGS = {
    "cursorial": dict(seg=[("coxa", 0.13, (0.1, 0.09)), ("trochanter", 0.07, (0.07, 0.06)),
                           ("femur", 0.32, (0.07, 0.08, 0.07)), ("tibia", 0.33, (0.05, 0.055)), ("tarsus", 0.27, (0.036, 0.03))],
                      tarsomeres=5, spines={"tibia": (8, 0.05, 1), "femur": (3, 0.03, -1)},
                      pose=(-80, -60, -10, -70, -35)),
    "saltatorial": dict(seg=[("coxa", 0.09, (0.1, 0.09)), ("trochanter", 0.06, (0.08, 0.07)),
                             ("femur", 0.47, (0.1, 0.19, 0.17, 0.12, 0.07)), ("tibia", 0.45, (0.045, 0.04)),
                             ("tarsus", 0.14, (0.04, 0.035))],
                        tarsomeres=3, spines={"tibia": (9, 0.05, 1)}, pattern="herringbone", spur=True,
                        pose=(-95, -130, 160, -35, -10)),
    "raptorial": dict(seg=[("coxa", 0.32, (0.08, 0.1, 0.09)), ("trochanter", 0.06, (0.07, 0.07)),
                           ("femur", 0.38, (0.08, 0.11, 0.1, 0.07)), ("tibia", 0.24, (0.05, 0.05, 0.04)),
                           ("tarsus", 0.2, (0.028, 0.022))],
                      tarsomeres=5, spines={"femur": (7, 0.06, -1), "tibia": (6, 0.045, -1)}, hook=True,
                      pose=(-60, -30, 40, -150, -110), tarsus_from=0.9),
    "fossorial": dict(seg=[("coxa", 0.12, (0.13, 0.12)), ("trochanter", 0.07, (0.1, 0.09)),
                           ("femur", 0.26, (0.13, 0.2, 0.17)), ("tibia", 0.2, (0.15, 0.22, 0.25)), ("tarsus", 0.11, (0.04, 0.035))],
                      tarsomeres=3, dactyls=4, pose=(-70, -40, -15, -40, -110), tarsus_from=0.55),
    "natatorial": dict(seg=[("coxa", 0.17, (0.14, 0.12)), ("trochanter", 0.07, (0.08, 0.07)),
                            ("femur", 0.3, (0.08, 0.09, 0.08)), ("tibia", 0.17, (0.08, 0.11, 0.12)),
                            ("tarsus", 0.36, (0.085, 0.07, 0.05))],
                       tarsomeres=5, fringe={"tibia": 0.07, "tarsus": 0.09}, pose=(-30, -10, 0, -25, -15)),
}


def leg(ax, base, kind="cursorial", length=1.0, angles=None, angle=0.0, mirror=False, colored=True, color=BODY,
        width=1.0, lw=LINE * 0.7, z=6, spines=True):
    """A segmented insect leg from the body (``base``): coxa, trochanter, femur, tibia, tarsus, claws.

    kind: "cursorial" (running: slender, e.g. cockroach), "saltatorial" (jumping hind leg: enlarged femur
    with herringbone muscle pattern, long spiny tibia; grasshopper), "raptorial" (grasping foreleg: long
    coxa, spiny femur and tibia folding on it like a jack-knife; mantis), "fossorial" (digging foreleg:
    broad femur and tibia with strong dactyls; mole cricket), "natatorial" (swimming hind leg: flattened
    tibia and tarsus fringed with long setae; diving beetle). ``length`` is the sum of segment lengths;
    ``angles`` gives absolute directions (degrees) of coxa, trochanter, femur, tibia and tarsus (default: a
    plate pose); ``angle`` rotates them, ``mirror`` reflects them left-right (and the spine side).
    ``colored`` paints segments with ``LEG``. Returns anchors per segment, "claws", and "joints" (list).
    """
    S = _LEGS[kind]
    ang = list(angles if angles is not None else S["pose"])
    ang = [(180.0 - a if mirror else a) + angle for a in ang]
    side = -1.0 if mirror else 1.0
    p = np.asarray(base, float)
    out = {"joints": [tuple(p)]}
    thin = lw * max(0.4, min(1.0, length / 3.0))
    total = sum(s[1] for s in S["seg"])
    k = length / total
    ends = {}
    for (part, L, ws), a in zip(S["seg"], ang):
        tok = _tok(colored, LEG[part], color)
        u = _dir(a)
        nv = _perp(u)
        L *= k
        w = np.asarray(ws, float) * k * width
        if part == "tarsus" and "tarsus_from" in S:
            tb, tq = ends["tibia"]
            p = tb + (tq - tb) * S["tarsus_from"]
        q = p + u * L
        zz = z + {"coxa": 0.1, "trochanter": 0.2, "femur": 0.3, "tibia": 0.4, "tarsus": 0.45 if "tarsus_from" in S else 0.35}[part]
        if part == "tarsus":
            n = S["tarsomeres"]
            ls = np.array([1.4] + [1.0] * (n - 2) + [1.3])[:n]
            ls = ls / ls.sum() * L
            pp = p
            for j, lj in enumerate(ls):
                qq = pp + u * lj
                wj = w[0] + (w[-1] - w[0]) * j / max(1, n - 1)
                _patch(ax, _rod(pp, qq, (wj * 0.8, wj, wj * 0.85), n=10, cap=0.6), tok, lw=thin * 0.8, z=zz)
                if "fringe" in S and part in S["fringe"]:
                    _fringe(ax, pp, qq, S["fringe"][part] * k, tok, thin, zz - 0.05)
                pp = qq - u * lj * 0.04
            # pretarsus: two claws
            ct = _tok(colored, LEG["pretarsus"], color)
            for s in (1, -1):
                c0 = pp
                c1 = pp + u * w[-1] * 1.6 + nv * s * w[-1] * 0.9
                c2 = c1 - nv * s * w[-1] * 0.4 + u * w[-1] * 0.3
                _line(ax, [c0, c1, c2], P.edge(ct), lw=thin * 1.1, z=zz + 0.05)
            out["claws"] = tuple(pp + u * w[-1] * 1.3)
            q = pp
        else:
            _patch(ax, _rod(p, q, w, n=24, cap=0.7), tok, lw=thin, z=zz)
            if "fringe" in S and part in S["fringe"]:
                _fringe(ax, p + u * L * 0.15, q, S["fringe"][part] * k, tok, thin, zz - 0.05)
        if part == "femur" and S.get("pattern") == "herringbone":
            for t in np.linspace(0.18, 0.85, 8):
                c = p + u * L * t
                hw = np.interp(t, np.linspace(0, 1, len(w)), w) / 2 * 0.75
                _line(ax, [c + nv * hw, c + u * L * 0.05, c - nv * hw], P.edge(tok), lw=thin * 0.45, z=zz + 0.02)
        if spines and part in S.get("spines", {}):
            cnt, sl, sd = S["spines"][part]
            for t in np.linspace(0.25, 0.92, cnt):
                c = p + u * L * t
                hw = np.interp(t, np.linspace(0, 1, len(w)), w) / 2
                b0 = c + nv * hw * sd * side * 0.9
                tip = b0 + (nv * sd * side + u * 0.6) * sl * k / np.linalg.norm(nv + u * 0.6)
                _patch(ax, [b0 - u * sl * k * 0.25, tip, b0 + u * sl * k * 0.2], tok, lw=thin * 0.5, z=zz - 0.02)
        if part == "tibia" and S.get("hook"):
            hw = w[-1] / 2
            b0 = q - nv * side * hw * 0.2
            _patch(ax, [b0 + nv * side * hw, b0 + u * hw * 3.2 - nv * side * hw * 1.2, b0 - nv * side * hw], tok, lw=thin * 0.6,
                   z=zz + 0.01)
        if part == "tibia" and S.get("spur"):
            for s in (0.6, 1.0):
                b0 = q + nv * side * w[-1] * 0.4
                _line(ax, [b0, b0 + _dir(a + side * 25 * s) * w[-1] * 2.5], P.edge(tok), lw=thin * 0.8, z=zz + 0.01)
        if part == "tibia" and S.get("dactyls"):
            n = S["dactyls"]
            for j in range(n):
                tt = 0.45 + 0.55 * j / (n - 1)
                hw = np.interp(tt, np.linspace(0, 1, len(w)), w) / 2
                b0 = p + u * L * tt - nv * side * hw * 0.85
                d = _dir(a - side * (65 - 12 * j))
                ln = w.max() * 0.55
                _patch(ax, [b0 - u * ln * 0.22, b0 + d * ln, b0 + u * ln * 0.22], tok, lw=thin * 0.6, z=zz + 0.01)
            out["dactyls"] = tuple(p + u * L * 0.8 - nv * side * w.max() * 0.7)
        out[part] = tuple((p + q) / 2)
        ends[part] = (p, q)
        out["joints"].append(tuple(q))
        p = q - u * L * 0.04
    return out


def _fringe(ax, a, b, ln, tok, lw, z):
    a, b = np.asarray(a, float), np.asarray(b, float)
    u = (b - a) / (np.linalg.norm(b - a) or 1)
    nv = _perp(u)
    for t in np.linspace(0.05, 0.95, 7):
        c = a + (b - a) * t
        for s in (1, -1):
            _line(ax, [c, c + (nv * s + u * 0.5) * ln], P.edge(tok), lw=lw * 0.4, z=z)


# ------------------------------------------------------------------ wings

# outlines in wing coordinates: base (0, 0), length 1 along +x, costal margin on the +y side
_WING_OUTLINES = {
    "diptera": [(0, 0), (0.12, 0.06), (0.45, 0.14), (0.8, 0.16), (0.98, 0.08), (1.0, -0.02), (0.9, -0.15), (0.6, -0.23),
                (0.3, -0.2), (0.12, -0.12), (0.04, -0.05)],
    "hymenoptera_fore": [(0, 0), (0.15, 0.06), (0.5, 0.11), (0.85, 0.11), (1.0, 0.03), (0.97, -0.07), (0.75, -0.17),
                         (0.4, -0.18), (0.15, -0.1), (0.04, -0.04)],
    "hymenoptera_hind": [(0, 0), (0.2, 0.05), (0.6, 0.08), (0.95, 0.05), (1.0, 0.0), (0.9, -0.09), (0.5, -0.15), (0.2, -0.12),
                         (0.05, -0.05)],
    "lepidoptera_fore": [(0, 0), (0.3, 0.09), (0.7, 0.12), (1.0, 0.05), (0.93, -0.2), (0.8, -0.42), (0.62, -0.55),
                         (0.35, -0.44), (0.12, -0.2), (0.03, -0.06)],
    "lepidoptera_hind": [(0, 0), (0.25, 0.1), (0.55, 0.07), (0.8, -0.08), (0.88, -0.35), (0.74, -0.62), (0.48, -0.72),
                         (0.22, -0.54), (0.06, -0.22)],
    "odonata_fore": [(0, 0), (0.2, 0.04), (0.6, 0.07), (0.92, 0.065), (1.0, 0.0), (0.96, -0.065), (0.7, -0.1), (0.35, -0.11),
                     (0.12, -0.08), (0.03, -0.03)],
    "odonata_hind": [(0, 0), (0.2, 0.04), (0.6, 0.07), (0.92, 0.065), (1.0, 0.0), (0.95, -0.075), (0.7, -0.13),
                     (0.4, -0.17), (0.18, -0.21), (0.05, -0.12)],
    "ephemeroptera_fore": [(0, 0), (0.3, 0.07), (0.7, 0.11), (1.0, 0.08), (0.88, -0.22), (0.58, -0.42), (0.3, -0.38),
                           (0.1, -0.18)],
    "ephemeroptera_hind": [(0, 0), (0.3, 0.12), (0.7, 0.1), (0.95, -0.12), (0.65, -0.38), (0.28, -0.3), (0.06, -0.1)],
    "neuroptera_fore": [(0, 0), (0.2, 0.08), (0.6, 0.13), (0.9, 0.11), (1.0, 0.02), (0.94, -0.1), (0.7, -0.19), (0.4, -0.21),
                        (0.15, -0.15), (0.03, -0.05)],
    "neuroptera_hind": [(0, 0), (0.2, 0.07), (0.6, 0.12), (0.9, 0.1), (1.0, 0.01), (0.93, -0.09), (0.7, -0.16),
                        (0.4, -0.18), (0.15, -0.12), (0.03, -0.04)],
    "tegmen": [(0, 0), (0.2, 0.06), (0.6, 0.085), (0.93, 0.065), (1.0, 0.0), (0.95, -0.07), (0.7, -0.11), (0.35, -0.12),
               (0.1, -0.08), (0.02, -0.03)],
    "blattodea_fore": [(0, 0), (0.2, 0.09), (0.6, 0.13), (0.9, 0.1), (1.0, 0.0), (0.93, -0.12), (0.7, -0.19), (0.35, -0.2),
                       (0.1, -0.13), (0.02, -0.04)],
    "fan": [(0, 0), (0.3, 0.07), (0.7, 0.09), (1.0, 0.02), (0.96, -0.22), (0.82, -0.47), (0.58, -0.64), (0.32, -0.62),
            (0.13, -0.4), (0.03, -0.12)],
    "hemelytron": [(0, 0), (0.2, 0.08), (0.6, 0.12), (0.9, 0.1), (1.0, 0.0), (0.95, -0.1), (0.7, -0.16), (0.35, -0.16),
                   (0.1, -0.1), (0.02, -0.03)],
    "coleoptera_hind": [(0, 0), (0.15, 0.06), (0.5, 0.11), (0.85, 0.12), (1.0, 0.04), (0.96, -0.1), (0.7, -0.22),
                        (0.4, -0.26), (0.15, -0.18), (0.04, -0.06)],
}
# elytron: lateral margin (spline from base to tip), closed by the straight sutural margin
_ELYTRON = [(0, 0), (0.02, 0.2), (0.12, 0.33), (0.4, 0.37), (0.72, 0.31), (0.93, 0.15), (1.0, 0.0)]

# kind -> (outline, fill role, venation style)
WING_KINDS = {
    "diptera": ("diptera", "membrane", "fly"),
    "hymenoptera_fore": ("hymenoptera_fore", "membrane", "reduced"),
    "hymenoptera_hind": ("hymenoptera_hind", "membrane", "reduced_hind"),
    "lepidoptera_fore": ("lepidoptera_fore", "scales", "scaled"),
    "lepidoptera_hind": ("lepidoptera_hind", "scales", "scaled"),
    "odonata_fore": ("odonata_fore", "membrane", "odonata"),
    "odonata_hind": ("odonata_hind", "membrane", "odonata"),
    "ephemeroptera_fore": ("ephemeroptera_fore", "membrane", "dense"),
    "ephemeroptera_hind": ("ephemeroptera_hind", "membrane", "dense"),
    "neuroptera_fore": ("neuroptera_fore", "membrane", "net"),
    "neuroptera_hind": ("neuroptera_hind", "membrane", "net"),
    "orthoptera_fore": ("tegmen", "tegmen", "tegmen"),
    "orthoptera_hind": ("fan", "membrane", "fan"),
    "blattodea_fore": ("blattodea_fore", "tegmen", "tegmen"),
    "blattodea_hind": ("fan", "membrane", "fan"),
    "hemelytron": ("hemelytron", "corium", "hemelytron"),
    "hemiptera_hind": ("hymenoptera_fore", "membrane", "fly"),
    "elytron": (None, "elytron", "elytron"),
    "coleoptera_hind": ("coleoptera_hind", "membrane", "beetle"),
}


def wing(ax, base, length, kind="diptera", angle=0.0, mirror=False, colored=True, color=BODY, chord=1.0, lw=LINE * 0.7,
         z=4, alpha=0.62, venation=True):
    """One wing from ``base`` towards ``angle`` (degrees), ``length`` long; the costal margin is on the left of
    the direction (``mirror=True`` puts it on the right, for wings of the left side pointing left).

    kind: see ``WING_KINDS`` (diptera, hymenoptera_fore/hind, lepidoptera_fore/hind, odonata_fore/hind,
    ephemeroptera_fore/hind, neuroptera_fore/hind, orthoptera_fore (tegmen)/hind (fan), blattodea_fore/hind,
    hemelytron, hemiptera_hind, elytron, coleoptera_hind). Fills follow ``WING`` (membranes translucent);
    venation styles: fly, reduced (closed cells, pterostigma), odonata (dense, nodus, pterostigma), dense
    (mayfly), net (lacewing: costal crossveins, marginal forks), tegmen, fan (anal fan), hemelytron
    (corium + clavus, membrane with a few veins), elytron (striae), scaled (scale rows, discal cell).
    ``chord`` scales the width. Returns anchors: "base", "tip", "wing" (a point on the blade), "costa",
    and where present "pterostigma", "nodus", "hamuli", "membrane", "corium", "clavus", "scales", "fan",
    "discal_cell", "anal", "outline" (canvas polygon).
    """
    outline_key, role, style = WING_KINDS[kind]
    F = _Frame(base, length, angle, mirror=False)
    sy = -1.0 if mirror else 1.0

    def T(pts):
        a = np.atleast_2d(np.asarray(pts, float)) * np.array([1.0, sy * chord])
        return F(a)

    tok = _tok(colored, WING[role], color)
    if role == "membrane":
        face, edge, al = P.fill(tok), P.edge(tok), alpha
    else:
        face, edge, al = P.fill(tok), P.edge(tok), None
    if outline_key is None:  # elytron
        lat = _spline(_ELYTRON, 90)
        local = np.vstack([lat, np.c_[np.linspace(1.0, 0.0, 20)[1:], np.zeros(19)]])
    else:
        local = smooth_closed(_WING_OUTLINES[outline_key], 220)[:-1]
    poly = T(local)
    patch = _patch(ax, poly, face=face, edge=edge, lw=lw, z=z, alpha=al)
    vc = P.edge(tok)
    vl = lw * max(0.35, min(0.9, length / 4.5))
    out = {"base": tuple(F((0, 0))), "outline": poly}
    q, nrm, Ltot = polyline(local, n=400, closed=True)
    q = q[:-1]
    iapex = int(np.argmax(q[:, 0] - 0.2 * np.abs(q[:, 1])))
    out["tip"] = tuple(T(q[iapex])[0])
    s_arc = np.r_[0, np.cumsum(np.hypot(*np.diff(q, axis=0).T))]
    s_arc /= s_arc[-1]
    f_apex = s_arc[iapex]

    def at_f(f):
        return q[min(len(q) - 1, int(f * (len(q) - 1)))]

    def bez(e, s0=(0.025, 0.0), k=0.5, ky=0.3):
        e = np.asarray(e, float)
        s0 = np.asarray(s0, float)
        c = np.array([e[0] * k, e[1] * ky])
        t = np.linspace(0, 1, 30)[:, None]
        return (1 - t) ** 2 * s0 + 2 * (1 - t) * t * c + t**2 * e

    def draw(pts, w=1.0, zz=0.2, dashed=False):
        _line(ax, T(pts), vc, lw=vl * w, z=z + zz, dashed=dashed)

    clip_items = []

    def veins(n, f0, f1, k=0.5, ky=0.3, w=1.0, stop=1.0):
        vs = []
        for f in np.linspace(f0, f1, n):
            v = bez(at_f(f), k=k, ky=ky)
            if stop < 1.0:
                v = v[: int(len(v) * stop)]
            vs.append(v)
            draw(v, w)
        return vs

    def cross(vs, m, t0=0.15, t1=0.95, w=0.5):
        for a, b in zip(vs[:-1], vs[1:]):
            for t in np.linspace(t0, t1, m):
                i = int(t * (min(len(a), len(b)) - 1))
                draw([a[i], b[i]], w, zz=0.15)

    if venation:
        costa = q[: iapex + 1]
        draw(costa, 1.5)
        out["costa"] = tuple(T(at_f(f_apex * 0.45))[0])
        if style == "fly":
            vs = veins(6, f_apex * 0.97, 0.86, k=0.5, ky=0.25)
            cross(vs[1:4], 1, 0.45, 0.45, w=0.9)
            out["anal"] = tuple(T(at_f(0.8))[0])
        elif style == "beetle":
            veins(5, f_apex * 0.9, 0.88, k=0.45, ky=0.2)
            draw([at_f(f_apex * 0.6) - [0, 0.04], at_f(0.65) + [0, 0.05]], 0.6, dashed=True)  # folding line
        elif style in ("reduced", "reduced_hind"):
            vs = veins(5, f_apex * 0.75, 0.88, k=0.55, ky=0.3, stop=0.72 if style == "reduced" else 0.6)
            cross(vs, 2, 0.4, 0.68 if style == "reduced" else 0.55, w=0.9)
            if style == "reduced":
                st = [at_f(f_apex * 0.6), at_f(f_apex * 0.72)]
                cell = np.array([st[0], st[1], st[1] - [0.0, 0.045], st[0] - [0.0, 0.035]])
                _patch(ax, T(cell), face=P.edge(tok), edge=P.edge(tok), lw=vl * 0.5, z=z + 0.25)
                out["pterostigma"] = tuple(T(cell.mean(axis=0))[0])
            else:  # hamuli: hooks on the costal margin of the hind wing
                for f in np.linspace(f_apex * 0.38, f_apex * 0.52, 5):
                    c = at_f(f)
                    draw([c, c + [0.012, 0.035], c + [0.03, 0.03]], 0.8, zz=0.3)
                out["hamuli"] = tuple(T(at_f(f_apex * 0.45))[0])
        elif style in ("odonata", "dense", "net"):
            nv = 9 if style == "odonata" else 10 if style == "dense" else 8
            vs = veins(nv, f_apex * (0.98 if style != "net" else 0.95), 0.9, k=0.55, ky=0.22 if style != "dense" else 0.35)
            cross(vs, 14 if style == "odonata" else 10 if style == "dense" else 7, w=0.45)
            sc = bez(at_f(f_apex * (0.5 if style == "odonata" else 0.85)), k=0.5, ky=0.4)
            draw(sc, 0.9)
            if style in ("odonata", "net"):  # costal (antenodal) crossveins
                for f in np.linspace(f_apex * 0.06, f_apex * (0.48 if style == "odonata" else 0.82), 9 if style == "odonata" else 14):
                    c = at_f(f)
                    j = int(np.argmin(np.hypot(*(sc - c).T)))
                    j2 = int(np.argmin(np.abs(sc[:, 0] - c[0])))
                    draw([c, sc[j2] if j2 > 0 else sc[j]], 0.45, zz=0.15)
            if style == "net":  # marginal forks
                for v in vs[1:]:
                    e = v[-1]
                    m = v[-6]
                    d = e - m
                    nn = _perp(d / (np.linalg.norm(d) or 1))
                    draw([m, e + nn * 0.02], 0.5)
                    draw([m, e - nn * 0.02], 0.5)
            if style == "odonata":
                nd = at_f(f_apex * 0.5)
                draw([nd, nd - [0, 0.07]], 1.3, zz=0.3)
                out["nodus"] = tuple(T(nd)[0])
                a0, a1 = at_f(f_apex * 0.84), at_f(f_apex * 0.92)
                cell = np.array([a0, a1, a1 - [0, 0.04], a0 - [0, 0.04]])
                _patch(ax, T(cell), face=P.edge(tok), edge=P.edge(tok), lw=vl * 0.5, z=z + 0.25)
                out["pterostigma"] = tuple(T(cell.mean(axis=0))[0])
        elif style == "tegmen":
            vs = veins(9, f_apex * 0.95, 0.9, k=0.55, ky=0.2, w=0.7)
            cross(vs, 9, w=0.35)
        elif style == "fan":
            vs = veins(14, f_apex * 0.95, 0.96, k=0.35, ky=0.15, w=0.7)
            cross(vs[:5], 6, w=0.35)
            out["fan"] = tuple(T(at_f(0.6) * 0.75)[0])
        elif style == "hemelytron":
            xc = 0.64
            # corium (sclerotized basal part) and clavus; the apical membrane stays translucent
            mem = P.fill(WING["membrane"]) if colored else P.light(color)
            patch.set_facecolor(mem)
            patch.set_alpha(alpha)
            cor = local[local[:, 0] <= xc]
            cut = np.array([[xc, cor[:, 1].max()], [xc + 0.08, 0.0], [xc - 0.06, cor[:, 1].min()]])
            corium = np.vstack([local[(local[:, 0] <= xc) & (local[:, 1] >= 0)], cut, local[(local[:, 0] <= xc) & (local[:, 1] < 0)]])
            hull = _order_ring(corium)
            _patch(ax, T(hull), face=P.fill(tok), edge=P.edge(tok), lw=lw, z=z + 0.1)
            cl = np.array([(0.03, -0.02), (0.3, -0.08), (0.55, -0.15)])
            draw(_spline(cl, 20), 1.0, zz=0.3)
            for f in (0.42, 0.5, 0.58, 0.66):
                e = at_f(f)
                draw(_spline([(xc + 0.04, 0.0), ((xc + e[0]) / 2, e[1] * 0.4), e], 15), 0.6, zz=0.3)
            out["corium"] = tuple(T((0.35, 0.04))[0])
            out["clavus"] = tuple(T((0.3, -0.12))[0])
            out["membrane"] = tuple(T((0.86, -0.02))[0])
        elif style == "elytron":
            for j in range(1, 8):
                yy = j * 0.042
                xs = np.linspace(0.05 + 0.1 * (j > 5), 0.92 - 0.06 * j, 30)
                pts = np.c_[xs, np.full_like(xs, yy)]
                draw(pts, 0.5, dashed=True)
            out["elytron"] = tuple(T((0.45, 0.2))[0])
        elif style == "scaled":
            if outline_key == "lepidoptera_fore":
                dc = [(0.08, -0.02), (0.5, 0.0), (0.58, -0.12), (0.45, -0.2), (0.1, -0.08)]
            else:
                dc = [(0.08, -0.04), (0.45, -0.1), (0.5, -0.25), (0.35, -0.3), (0.08, -0.12)]
            band = P.mix(P.fill(tok), P.edge(tok), 0.55)
            # dark marginal band, scale rows clipped to the wing, discal cell
            for i, t in enumerate(np.linspace(0, 1, 2)):
                pass
            inner = (local - local.mean(axis=0)) * 0.8 + local.mean(axis=0) * 1.0
            inner = inner + (np.array([0.0, 0.0]) - inner) * 0.06
            mb = _patch(ax, T(local), face=band, edge=P.edge(tok), lw=lw, z=z + 0.05)
            ip = _patch(ax, T(inner), face=P.fill(tok), edge=P.fill(tok), lw=0, z=z + 0.07)
            clip_items += [mb, ip]
            rows = []
            for yy in np.arange(-0.75, 0.2, 0.05):
                xs = np.arange(0.04, 1.05, 0.045) + (0.0225 if int(round(yy / 0.05)) % 2 else 0)
                for xx in xs:
                    rows.append(T(np.c_[xx + 0.016 * np.cos(np.linspace(-1.3, 1.3, 6)), yy + 0.02 * np.sin(np.linspace(-1.3, 1.3, 6))]))
            for r in rows:
                ln = ax.plot(r[:, 0], r[:, 1], color=P.edge(tok), lw=vl * 0.3, zorder=z + 0.09, alpha=0.55)[0]
                ln.set_clip_path(patch)
            draw(_spline(dc + [dc[0]], 30), 0.7, zz=0.12)
            out["discal_cell"] = tuple(T(np.mean(dc, axis=0))[0])
            out["scales"] = tuple(T((0.65, -0.25 if outline_key == "lepidoptera_fore" else -0.45))[0])
            spot = (0.55, -0.12) if outline_key == "lepidoptera_fore" else (0.5, -0.4)
            sp = T(_ellipse(spot, 0.04, 0.04))
            _patch(ax, sp, face=P.edge(tok), edge=P.edge(tok), lw=0, z=z + 0.1)
        else:
            raise ValueError(style)
    out["wing"] = tuple(T(local.mean(axis=0) * 0.6 + q[iapex] * 0.4)[0]) if outline_key else tuple(T((0.5, 0.18))[0])
    out.setdefault("membrane", out["wing"] if role == "membrane" else None)
    return out


def _order_ring(pts):
    p = np.asarray(pts, float)
    c = p.mean(axis=0)
    a = np.arctan2(p[:, 1] - c[1], p[:, 0] - c[0])
    return p[np.argsort(a)]


def haltere(ax, base, length, angle=-60.0, colored=True, color=BODY, lw=LINE * 0.6, z=6):
    """A dipteran haltere (the club-shaped, reduced hind wing). Returns {"haltere": knob centre}."""
    tok = _tok(colored, WING["haltere"], color)
    b = np.asarray(base, float)
    e = b + _dir(angle) * length
    _line(ax, [b, e], P.edge(tok), lw=lw * 1.4, z=z)
    _patch(ax, _ellipse(e, length * 0.22, length * 0.16, angle), tok, lw=lw * 0.8, z=z + 0.1)
    return {"haltere": tuple(e)}


# ------------------------------------------------------------------ whole insects

# Body proportions as fractions of the body length (head front to abdomen tip): (length, width).
# Wings: (kind, length, angle) for the right side, spread as in a set specimen.
ORDERS = {
    "Ephemeroptera": dict(head=(0.07, 0.1), pro=(0.05, 0.085, "plain"), ptero=(0.17, 0.13), abd=(0.71, 0.085, "slender", 10),
                          eye=0.55, antenna=("setaceous", 0.1), mouth="vestigial", legs=("cursorial",) * 3,
                          leg_len=(0.55, 0.35, 0.38), fore=("ephemeroptera_fore", 0.7, 22), hind=("ephemeroptera_hind", 0.24, -18),
                          cerci=1.0, caudal=True, common="Mayflies"),
    "Odonata": dict(head=(0.07, 0.15), pro=(0.035, 0.08, "plain"), ptero=(0.13, 0.12), abd=(0.76, 0.06, "slender", 10),
                    eye=0.9, antenna=("setaceous", 0.05), mouth="chewing", legs=("cursorial",) * 3, leg_len=(0.25, 0.28, 0.32),
                    leg_pose="basket", fore=("odonata_fore", 0.62, 4), hind=("odonata_hind", 0.6, -10), cerci=0.05,
                    common="Dragonflies, damselflies"),
    "Orthoptera": dict(head=(0.12, 0.15), pro=(0.14, 0.17, "saddle"), ptero=(0.15, 0.16), abd=(0.59, 0.14, "oval", 9),
                       eye=0.35, antenna=("filiform", 0.32), mouth="chewing", legs=("cursorial", "cursorial", "saltatorial"),
                       leg_len=(0.4, 0.42, 1.0), fore=("orthoptera_fore", 0.58, 14), hind=("orthoptera_hind", 0.56, -8),
                       cerci=0.05, common="Grasshoppers, crickets"),
    "Blattodea": dict(head=(0.1, 0.16), pro=(0.17, 0.36, "shield"), ptero=(0.14, 0.3), abd=(0.59, 0.34, "broad", 8),
                      eye=0.3, antenna=("setaceous", 0.85), mouth="chewing", legs=("cursorial",) * 3, leg_len=(0.5, 0.6, 0.75),
                      fore=("blattodea_fore", 0.6, 10), hind=("blattodea_hind", 0.55, -12), cerci=0.12,
                      common="Cockroaches, termites"),
    "Hemiptera": dict(head=(0.12, 0.17), pro=(0.14, 0.34, "trapezoid"), ptero=(0.2, 0.3), abd=(0.54, 0.34, "broad", 6),
                      eye=0.35, antenna=("filiform", 0.42), ant_segments=3, mouth="piercing-sucking", legs=("cursorial",) * 3,
                      leg_len=(0.5, 0.55, 0.68), fore=("hemelytron", 0.6, 12), hind=("hemiptera_hind", 0.48, -14),
                      scutellum=True, cerci=0.0, common="True bugs"),
    "Neuroptera": dict(head=(0.1, 0.13), pro=(0.08, 0.1, "plain"), ptero=(0.17, 0.14), abd=(0.65, 0.11, "slender", 9),
                       eye=0.45, antenna=("filiform", 0.55), mouth="chewing", legs=("cursorial",) * 3, leg_len=(0.4, 0.42, 0.48),
                       fore=("neuroptera_fore", 0.82, 10), hind=("neuroptera_hind", 0.74, -10), cerci=0.0,
                       common="Lacewings, antlions"),
    "Coleoptera": dict(head=(0.12, 0.2), pro=(0.18, 0.4, "trapezoid"), ptero=(0.1, 0.38), abd=(0.6, 0.44, "broad", 6),
                       eye=0.25, antenna=("filiform", 0.42), mouth="chewing", legs=("cursorial",) * 3, leg_len=(0.5, 0.55, 0.62),
                       fore=("elytron", 0.66, None), hind=("coleoptera_hind", 0.95, 14), elytra=True, cerci=0.0,
                       common="Beetles"),
    "Hymenoptera": dict(head=(0.13, 0.2), pro=(0.05, 0.16, "plain"), ptero=(0.25, 0.2), abd=(0.57, 0.2, "petiolate", 6),
                        eye=0.45, antenna=("geniculate", 0.42), mouth="chewing", legs=("cursorial",) * 3,
                        leg_len=(0.5, 0.55, 0.7), fore=("hymenoptera_fore", 0.68, 10), hind=("hymenoptera_hind", 0.45, -8),
                        cerci=0.0, common="Bees, wasps, ants, sawflies"),
    "Lepidoptera": dict(head=(0.1, 0.13), pro=(0.06, 0.13, "plain"), ptero=(0.22, 0.17), abd=(0.62, 0.12, "slender", 8),
                        eye=0.5, antenna=("clavate", 0.6), mouth="siphoning", legs=("cursorial",) * 3, leg_len=(0.3, 0.42, 0.45),
                        fore=("lepidoptera_fore", 0.86, 22), hind=("lepidoptera_hind", 0.7, -20), cerci=0.0, hairy=True,
                        common="Butterflies, moths"),
    "Diptera": dict(head=(0.16, 0.3), pro=(0.04, 0.2, "plain"), ptero=(0.33, 0.3), abd=(0.47, 0.3, "oval", 5),
                    eye=0.95, antenna=("aristate", 0.09), mouth="sponging", legs=("cursorial",) * 3, leg_len=(0.6, 0.65, 0.75),
                    fore=("diptera", 0.82, -6), hind=None, halteres=True, cerci=0.0, common="True flies"),
    "Mantodea": dict(head=(0.08, 0.15), pro=(0.27, 0.07, "plain"), ptero=(0.13, 0.11), abd=(0.52, 0.13, "slender", 8),
                     eye=0.5, antenna=("setaceous", 0.32), mouth="chewing", legs=("raptorial", "cursorial", "cursorial"),
                     leg_len=(0.7, 0.55, 0.65), fore=("orthoptera_fore", 0.42, 12), hind=("orthoptera_hind", 0.4, -10),
                     cerci=0.06, common="Mantises"),
}

_ABDOMEN = {
    "oval": [(0, 0.12), (0.1, 0.55), (0.3, 0.9), (0.55, 1.0), (0.8, 0.95), (1.0, 0.72)],
    "slender": [(0, 0.45), (0.05, 0.75), (0.3, 0.82), (0.7, 0.85), (0.9, 0.95), (1.0, 1.0)],
    "petiolate": [(0, 0.08), (0.1, 0.55), (0.3, 0.98), (0.55, 1.0), (0.74, 0.62), (0.81, 0.18), (0.94, 0.17), (1.0, 0.3)],
    "broad": [(0, 0.3), (0.1, 0.72), (0.3, 0.96), (0.6, 1.0), (0.85, 0.96), (1.0, 0.86)],
}


def _profile(kind, n=60):
    pts = np.asarray(_ABDOMEN[kind], float)
    t = np.linspace(0, 1, n)
    return t, np.interp(t, pts[:, 0], pts[:, 1])


def insect(ax, at, size, order="Coleoptera", view="dorsal", angle=0.0, colored=False, color=BODY, wings=True,
           highlight=(), lw=LINE * 0.7, z=5, **override):
    """A whole insect generated from body-plan rules; ``size`` is the body length (head to abdomen tip).

    order: a key of ``ORDERS`` (Ephemeroptera, Odonata, Orthoptera, Blattodea, Hemiptera, Neuroptera,
    Coleoptera, Hymenoptera, Lepidoptera, Diptera, Mantodea); any field of the spec can be overridden by
    keyword (``legs=("fossorial", "cursorial", "cursorial")``, ``antenna=("pectinate", 0.5)``, ...).
    view: "dorsal" (head up when ``angle=0``; wings spread as in a set specimen, beetles with the left
    elytron closed) or "lateral" (head to the right; wings folded over the abdomen; legs on the near side).
    Wings are coloured by type (``WING``) whatever ``colored`` says; ``colored`` paints antennae, legs and
    mouthparts by part; ``highlight`` lists leg pairs ("fore", "mid", "hind") to paint by segment anyway.
    Returns anchors: "head", "eye", "antenna" (a point on it), "pronotum", "thorax", "abdomen", "cerci",
    "caudal_filament", "forewing", "hindwing", "elytron", "haltere", "scutellum", "pterostigma", "nodus",
    "hamuli", "corium", "membrane", "scales", "fan", "legs" ({"fore": anchors, ...}), "mouthparts" (lateral).
    """
    S = dict(ORDERS[order])
    S.update(override)
    if view == "lateral":
        return _insect_lateral(ax, at, size, S, angle, colored, color, wings, highlight, lw, z)
    hl, hw = S["head"]
    pl, pw, pshape = S["pro"]
    tl, tw = S["ptero"]
    al_, aw, ashape, nseg = S["abd"]
    tot = hl + pl + tl + al_
    s = size / tot
    F = _Frame(at, s, angle)
    # y positions (local, body length tot, centred at the middle of the body)
    y0 = -tot / 2
    ya = (y0, y0 + al_)
    yt = (ya[1], ya[1] + tl)
    yp = (yt[1], yt[1] + pl)
    yh = (yp[1], yp[1] + hl)
    out = {"legs": {}}
    E = P.edge(color)

    # legs (under the body)
    kinds = S["legs"]
    lens = S["leg_len"]
    attach = {"fore": (pw * 0.4, yp[0] + pl * 0.45), "mid": (tw * 0.42, yt[0] + tl * 0.62), "hind": (tw * 0.4, yt[0] + tl * 0.2)}
    basket = S.get("leg_pose") == "basket"
    poses = {"fore": (60, 50, 45, 95, 80), "mid": (-5, -10, 15, -55, -65), "hind": (-35, -40, -25, -100, -105)}
    if basket:  # Odonata: legs held forward under the thorax
        poses = {"fore": (70, 60, 55, 110, 100), "mid": (40, 30, 35, 100, 95), "hind": (10, 5, 20, 95, 90)}
    for pair, kind in zip(("fore", "mid", "hind"), kinds):
        pose = list(poses[pair])
        if kind == "saltatorial":
            pose = [-40, -45, -45, 130, -80]
        elif kind == "raptorial":
            pose = [80, 75, 60, -125, -95]
        elif kind == "fossorial":
            pose = [55, 45, 30, 50, 90]
        elif kind == "natatorial":
            pose = [-30, -35, -40, -50, -55]
        L = lens[("fore", "mid", "hind").index(pair)] * s * tot
        lc = colored or pair in highlight
        for m in (False, True):
            bx, by = attach[pair]
            base = F((-bx if m else bx, by))
            ang = [F.ang(a) for a in pose] if not m else [F.ang(180 - a) for a in pose]
            a = leg(ax, base, kind, L, angles=ang, colored=lc, color=color, lw=lw * 0.9, z=z - 1.5, width=1.0)
            if not m:
                out["legs"][pair] = a

    # wings (under the body, over the legs)
    fw, hwing = S["fore"], S["hind"]
    wz = z - 0.8
    wb_f = (tw * 0.38, yt[1] - tl * 0.22)
    wb_h = (tw * 0.4, yt[0] + tl * 0.32)
    if wings and S.get("elytra"):
        # right side: elytron raised and hind wing unfolded; left side: elytron closed over the abdomen
        hk, hlen, hang = hwing
        r = wing(ax, F(wb_h), hlen * size, hk, angle=F.ang(hang), z=wz - 0.3)
        out["hindwing"] = r["wing"]
        out["hindwing_fold"] = r.get("costa")
        el_len = (yt[1] - tl * 0.1) - (ya[0] + al_ * 0.02)
        ec = wing(ax, F((-0.004, yt[1] - tl * 0.1)), el_len * s, "elytron", angle=F.ang(-90), mirror=True, chord=aw / 0.74 / el_len,
                  z=z + 0.6)
        ro = wing(ax, F((tw * 0.25, yt[1] - tl * 0.1)), el_len * s * 0.95, "elytron", angle=F.ang(-62), mirror=False,
                  chord=aw / 0.74 / el_len, z=wz)
        out["elytron"] = ec["elytron"]
        out["elytron_open"] = ro["elytron"]
        out["forewing"] = ro["elytron"]
    elif wings:
        for m in (False, True):
            sgn = -1 if m else 1
            if hwing:
                hk, hlen, hang = hwing
                r = wing(ax, F((sgn * wb_h[0], wb_h[1])), hlen * size, hk,
                         angle=F.ang(hang if not m else 180 - hang), mirror=m, z=wz - 0.2)
                if not m:
                    out["hindwing"] = r["wing"]
                    for kk in ("hamuli", "fan", "scales", "pterostigma"):
                        if r.get(kk):
                            out["hind_" + kk] = r[kk]
            fk, flen, fang = fw
            r = wing(ax, F((sgn * wb_f[0], wb_f[1])), flen * size, fk, angle=F.ang(fang if not m else 180 - fang), mirror=m, z=wz)
            if not m:
                out["forewing"] = r["wing"]
                for kk in ("pterostigma", "nodus", "corium", "membrane", "clavus", "scales", "discal_cell", "costa"):
                    if r.get(kk):
                        out[kk] = r[kk]
        if S.get("halteres"):
            for m in (False, True):
                sg = -1 if m else 1
                hb = F((sg * tw * 0.36, yt[0] + tl * 0.18))
                h = haltere(ax, hb, size * 0.08, angle=F.ang(-60 if not m else -120), z=wz + 0.1)
                if not m:
                    out["haltere"] = h["haltere"]

    # abdomen
    t, w = _profile(ashape)
    yy = ya[0] + t * al_
    xr = w * aw / 2
    outline = np.vstack([np.c_[xr, yy], np.c_[-xr, yy][::-1]])
    _patch(ax, F(outline), color, lw=lw, z=z)
    for k in range(1, nseg):
        ty = k / nseg
        if ashape == "petiolate" and ty > 0.72:
            continue
        wy = np.interp(ty, t, w) * aw / 2 * 0.96
        yk = ya[0] + ty * al_
        arc = np.c_[np.linspace(-wy, wy, 12), yk + 0.012 * al_ * np.cos(np.linspace(-1.2, 1.2, 12))]
        _line(ax, F(arc), E, lw=lw * 0.5, z=z + 0.05)
    out["abdomen"] = tuple(F((aw * 0.18, ya[0] + al_ * 0.45)))
    if ashape == "petiolate":
        out["petiole"] = tuple(F((0, ya[0] + al_ * 0.88)))
    # cerci / caudal filaments
    cl = S.get("cerci", 0)
    tip = (0, ya[0] + al_ * 0.01)
    if cl:
        for sg in (1, -1):
            pts = _spline([tip, (sg * cl * 0.15 * tot, ya[0] - cl * 0.5 * tot), (sg * cl * 0.28 * tot, ya[0] - cl * tot)], 30)
            if cl > 0.3:
                _line(ax, F(pts), E, lw=lw * 0.9, z=z + 0.1)
            else:
                _patch(ax, F(_band(pts, aw * 0.12, aw * 0.04)), color, lw=lw * 0.6, z=z - 0.05)
            if sg == 1:
                out["cerci"] = tuple(F(pts[len(pts) // 2]))
        if S.get("caudal"):
            _line(ax, F([(0, ya[0]), (0, ya[0] - cl * tot * 1.05)]), E, lw=lw * 0.9, z=z + 0.1)
            out["caudal_filament"] = tuple(F((0, ya[0] - cl * tot * 0.6)))
    # thorax
    th = _ellipse((0, (yt[0] + yt[1]) / 2), tw / 2, tl / 2 * 1.08, n=60)
    _patch(ax, F(th), color, lw=lw, z=z + 0.2)
    out["thorax"] = tuple(F((tw * 0.15, (yt[0] + yt[1]) / 2)))
    if S.get("scutellum"):
        sc = [(-tw * 0.28, yt[1] - tl * 0.08), (tw * 0.28, yt[1] - tl * 0.08), (0, yt[0] - tl * 0.25)]
        _patch(ax, F(sc), face=P.light(color), edge=E, lw=lw, z=z + 0.7)
        out["scutellum"] = tuple(F((0, yt[0] + tl * 0.25)))
    # head
    hc = (0, (yh[0] + yh[1]) / 2)
    hd = _ellipse(hc, hw / 2, hl / 2 * 1.1, n=60)
    hz = z + 0.4
    _patch(ax, F(hd), color, lw=lw, z=hz)
    out["head"] = tuple(F(hc))
    er = S.get("eye", 0.4)
    ex = hw / 2 * (1 - 0.35 * er)
    erx, ery = hw * 0.22 * (0.6 + er), hl * 0.3 * (0.7 + er)
    for sg in (1, -1):
        if er > 0.8:  # holoptic: eyes meeting on top of the head
            e = _ellipse((sg * hw * 0.25, hc[1] + hl * 0.05), hw * 0.29, hl * 0.52, n=40)
        else:
            e = _ellipse((sg * ex, hc[1] + hl * 0.08), erx, ery, n=40)
        _patch(ax, F(e), face=P.edge(EYE), edge=P.edge(EYE), lw=lw * 0.5, z=hz + 0.1)
    out["eye"] = tuple(F((ex if er <= 0.8 else hw * 0.3, hc[1] + hl * 0.08)))
    if S["mouth"] == "chewing":
        for sg in (1, -1):
            mb = np.array([sg * hw * 0.12, yh[1] - hl * 0.05])
            md = [mb, mb + [sg * hw * 0.16, hl * 0.22], mb + [-sg * hw * 0.04, hl * 0.34], mb + [-sg * hw * 0.02, hl * 0.12]]
            _patch(ax, F(smooth_closed(md, 30)), _tok(colored, MOUTH["mandible"], color), lw=lw * 0.6, z=hz - 0.05)
        out["mandibles"] = tuple(F((hw * 0.12, yh[1] + hl * 0.2)))
    if S["mouth"] == "siphoning":
        for sg in (1, -1):
            pp = _spline([(sg * hw * 0.08, yh[1] - hl * 0.1), (sg * hw * 0.09, yh[1] + hl * 0.25), (sg * hw * 0.05, yh[1] + hl * 0.45)], 20)
            _patch(ax, F(_band(pp, hw * 0.09, hw * 0.04)), _tok(colored, MOUTH["labium"], color), lw=lw * 0.5, z=hz - 0.05)
        out["labial_palps"] = tuple(F((hw * 0.1, yh[1] + hl * 0.3)))
    # pronotum
    pc = (0, (yp[0] + yp[1]) / 2)
    if pshape == "shield":  # cockroach: covers most of the head
        pn = _ellipse((0, yp[0] + pl * 0.55), pw / 2, pl * 0.72, n=70)
        pz = hz + 0.3
    elif pshape == "trapezoid":
        pn = smooth_closed([(-pw * 0.5, yp[0] + pl * 0.05), (pw * 0.5, yp[0] + pl * 0.05), (pw * 0.4, yp[1] - pl * 0.1),
                            (-pw * 0.4, yp[1] - pl * 0.1)], 60)
        pn = smooth_closed([(-pw * 0.5, yp[0]), (0, yp[0] - pl * 0.05), (pw * 0.5, yp[0]), (pw * 0.46, yp[0] + pl * 0.6),
                            (pw * 0.33, yp[1]), (0, yp[1] + pl * 0.03), (-pw * 0.33, yp[1]), (-pw * 0.46, yp[0] + pl * 0.6)], 80)
        pz = z + 0.65
    elif pshape == "saddle":
        pn = smooth_closed([(-pw * 0.5, yp[0] - pl * 0.1), (0, yp[0] - pl * 0.18), (pw * 0.5, yp[0] - pl * 0.1),
                            (pw * 0.46, yp[1]), (0, yp[1] + pl * 0.02), (-pw * 0.46, yp[1])], 80)
        pz = z + 0.65
    else:
        pn = _ellipse(pc, pw / 2, pl / 2 * 1.15, n=50)
        pz = z + 0.3
    _patch(ax, F(pn), face=P.light(color) if pshape in ("shield", "saddle", "trapezoid") else P.fill(color), edge=E, lw=lw, z=pz)
    out["pronotum"] = tuple(F((pw * 0.2, pc[1])))
    if pshape == "saddle":
        _line(ax, F([(-pw * 0.3, yp[0] + pl * 0.4), (pw * 0.3, yp[0] + pl * 0.4)]), E, lw=lw * 0.5, z=pz + 0.05)
    # antennae
    ak, alen = S["antenna"]
    for m in (False, True):
        sg = -1 if m else 1
        sock = (sg * hw * 0.22, yh[1] - hl * 0.15)
        dep = 70 if ak not in ("setaceous", "aristate") else 75
        if ak == "aristate":
            dep = 100
        a = antenna(ax, F(sock), F.ang(dep if not m else 180 - dep), alen * size, ak, colored=colored, color=color,
                    mirror=m, curve=(-1.5 if not m else 1.5) if ak not in ("geniculate",) else 0, lw=lw * 0.8,
                    segments=S.get("ant_segments"), thickness=None if ak in ("aristate", "lamellate") else size * 0.016 * S.get("ant_thick", 1.0),
                    z=hz + 0.5)
        if not m:
            out["antenna"] = a["flagellum"]
            out["antenna_club"] = a.get("club")
    return out


def _insect_lateral(ax, at, size, S, angle, colored, color, wings, highlight, lw, z):
    hl, hw = S["head"]
    pl, pw, pshape = S["pro"]
    tl, tw = S["ptero"]
    al_, aw, ashape, nseg = S["abd"]
    tot = hl + pl + tl + al_
    s = size / tot
    F = _Frame(at, s, angle)
    x0 = -tot / 2
    xa = (x0, x0 + al_)
    xt = (xa[1], xa[1] + tl)
    xp = (xt[1], xt[1] + pl)
    xh = (xp[1], xp[1] + hl)
    E = P.edge(color)
    out = {"legs": {}}
    depth = S.get("depth", 0.85)
    th_h = tw * depth
    ab_h = aw * depth * (0.8 if ashape == "broad" else 1.0)
    # abdomen: profile along x (tip at x0), dorsal side flatter
    t, w = _profile(ashape)
    xx = xa[0] + t * al_
    top = w * ab_h * 0.45
    bot = -w * ab_h * 0.55
    ab = np.vstack([np.c_[xx, top], np.c_[xx, bot][::-1]])
    _patch(ax, F(ab), color, lw=lw, z=z)
    for k in range(1, nseg):
        tk = k / nseg
        if ashape == "petiolate" and tk > 0.72:
            continue
        hh = np.interp(tk, t, w)
        xk = xa[0] + tk * al_
        _line(ax, F([(xk, hh * ab_h * 0.43), (xk + 0.01 * al_, -hh * ab_h * 0.53)]), E, lw=lw * 0.5, z=z + 0.05)
    out["abdomen"] = tuple(F((xa[0] + al_ * 0.45, 0)))
    cy = 0.0
    th = _ellipse(((xt[0] + xt[1]) / 2, cy + th_h * 0.05), tl / 2 * 1.08, th_h / 2, n=60)
    _patch(ax, F(th), color, lw=lw, z=z + 0.2)
    out["thorax"] = tuple(F(((xt[0] + xt[1]) / 2, cy)))
    pr_h = pw * depth if pshape != "shield" else th_h
    pn = _ellipse(((xp[0] + xp[1]) / 2, cy + th_h * 0.1), pl / 2 * 1.15, min(pr_h, th_h) / 2 * 0.95, n=50)
    _patch(ax, F(pn), face=P.light(color) if pshape in ("saddle", "shield", "trapezoid") else P.fill(color), edge=E, lw=lw, z=z + 0.4)
    out["pronotum"] = tuple(F(((xp[0] + xp[1]) / 2, cy + th_h * 0.1)))
    # legs on the near side, hanging to a common ground line
    ground = cy - th_h * 0.5 - S.get("clearance", 0.18) * tot
    lens = S["leg_len"]
    attach = {"fore": ((xp[0] + xp[1]) / 2, cy - pr_h * 0.35), "mid": (xt[0] + tl * 0.65, cy - th_h * 0.4),
              "hind": (xt[0] + tl * 0.25, cy - th_h * 0.38)}
    poses = {"fore": (-80, -50, -25, -80, -10), "mid": (-95, -75, -15, -105, -170), "hind": (-100, -135, -160, -95, -170)}
    special = {"saltatorial": (-100, -140, 158, -32, -175), "raptorial": (-55, -25, 38, -150, -105),
               "fossorial": (-65, -30, -5, -45, -110), "natatorial": (-140, -165, -172, -178, 178)}
    for pair, kind in zip(("fore", "mid", "hind"), S["legs"]):
        pose = special.get(kind, poses[pair])
        L = lens[("fore", "mid", "hind").index(pair)] * size
        lc = colored or pair in highlight
        base = F(attach[pair])
        a = leg(ax, base, kind, L, angles=[F.ang(v) for v in pose], colored=lc, color=color, lw=lw * 0.9,
                z=z + (1.0 if lc else -1.0))
        out["legs"][pair] = a
    out["ground"] = ground
    # wings folded over the abdomen (costa below), or halteres
    if wings and S.get("fore"):
        fk, flen, _ = S["fore"]
        if fk == "elytron":  # a dome over the dorsum, from the scutellum to the abdomen tip
            x1, x2 = xt[1] - tl * 0.12, xa[0] + al_ * 0.02
            xc, hx = (x1 + x2) / 2, (x1 - x2) / 2
            yb, H = -ab_h * 0.12, max(ab_h * 0.62, th_h * 0.58)
            tt = np.linspace(0, np.pi, 60)
            dome = np.c_[xc + hx * np.cos(tt), yb + H * np.sin(tt) ** 0.8]
            el = np.vstack([dome, np.c_[np.linspace(x2, x1, 12)[1:-1], np.full(10, yb)]])
            xs = xc + hx * np.cos(tt)
            topc, botc = yb + H * np.sin(tt) ** 0.8, np.full(60, yb)
            tok = _tok(True, WING["elytron"], color)
            _patch(ax, F(el), tok, lw=lw, z=z + 0.6)
            for f in (0.3, 0.55, 0.78):
                _line(ax, F(np.c_[xs[4:-4], (botc + (topc - botc) * f)[4:-4]]), P.edge(tok), lw=lw * 0.4, z=z + 0.65, dashed=True)
            out["forewing"] = out["elytron"] = tuple(F((xs[20], (topc[20] + botc[20]) / 2)))
        else:
            r = wing(ax, F((xt[1] - tl * 0.25, cy + th_h * 0.35)), flen * size * 0.95, fk, angle=F.ang(184), mirror=False,
                     chord=0.75, z=z + 0.6)
            out["forewing"] = r["wing"]
        if S.get("halteres"):
            out["haltere"] = haltere(ax, F((xt[0] + tl * 0.15, cy + th_h * 0.1)), size * 0.07, angle=F.ang(-120), z=z + 0.7)["haltere"]
    # head with mouthparts
    hsz = hl * s * 0.62 * S.get("head_scale", 1.0)
    hc = F(((xh[0] + xh[1]) / 2 + hl * 0.05, cy + th_h * 0.12))
    mp = S["mouth"]
    a = head(ax, hc, hsz, mp, facing="right", colored=colored, color=color, antenna_kind=S["antenna"][0],
             antenna_length=S["antenna"][1] * size / hsz, antenna_thickness=size * 0.014, lw=lw, z=z + 1.2)
    out["head"] = a["head"]
    out["eye"] = a["eye"]
    out["mouthparts"] = a
    cl = S.get("cerci", 0)
    if cl:
        tipx = xa[0] + al_ * 0.01
        pts = _spline([(tipx, 0), (tipx - cl * tot * 0.5, cl * tot * 0.08), (tipx - cl * tot, cl * tot * 0.12)], 30)
        if cl > 0.3:
            _line(ax, F(pts), E, lw=lw * 0.9, z=z + 0.1)
        else:
            _patch(ax, F(_band(pts, ab_h * 0.12, ab_h * 0.04)), color, lw=lw * 0.6, z=z - 0.05)
        out["cerci"] = tuple(F(pts[len(pts) // 2]))
    return out


# ------------------------------------------------------------------ mollusc shells (Raup's model)


def raup_geometry(W=2.0, D=0.0, T=2.0, S=1.0, turns=None, n_theta=None, n_phi=18, rmin=0.02, hand=1):
    """Raup's (1966) coiling model in 3D: a generating curve (an ellipse of axial/radial ratio ``S``) revolves
    about the coiling axis, growing by ``W`` per revolution (whorl expansion rate); ``D`` is the distance of
    its inner edge from the axis relative to its outer edge; ``T`` is the translation along the axis per unit
    radial distance (0: planispiral). The aperture is the last curve (theta = 0, outer radius 1).
    Returns (theta, X, Y, Z, centres) with X, Y, Z of shape (n_theta, n_phi + 1), the apex at the top.
    """
    W = max(float(W), 1.0001)
    if turns is None:
        turns = min(7.0, math.log(1 / rmin) / math.log(W))
    if n_theta is None:
        n_theta = int(max(36, min(300, 42 * turns)))
    th = np.linspace(-turns * 2 * np.pi, 0, n_theta)
    R = W ** (th / (2 * np.pi))
    rc = R * (1 + D) / 2
    a = R * (1 - D) / 2
    b = a * S
    zc = -T * rc
    ph = np.linspace(0, 2 * np.pi, n_phi + 1)
    rad = rc[:, None] + a[:, None] * np.cos(ph)[None, :]
    X = rad * np.cos(th)[:, None]
    Y = hand * rad * np.sin(th)[:, None]
    Z = zc[:, None] + b[:, None] * np.sin(ph)[None, :]
    C = np.c_[rc * np.cos(th), hand * rc * np.sin(th), zc]
    return th, X, Y, Z, C


def raup_shell(ax, center, size, W=2.0, D=0.0, T=2.0, S=1.0, turns=None, elev=12.0, azim=-25.0, token=SHELL, hand=-1,
               bands=5, n_phi=28, n_theta=None, rmin=0.02, z=5, fit=None):
    """Draw a shell from Raup's parameters (see ``raup_geometry``), shaded flat facets, fitted into a square of
    side ``size`` (or ``fit=(width, height)``) centred at ``center``. ``elev`` tilts the view (90: looking down
    the coiling axis, as for a planispiral shell seen from the side), ``azim`` turns the shell about its axis,
    ``hand`` = -1 dextral (apex up, aperture on the right facing the viewer), 1 sinistral; every ``bands``-th row of facets is darker (growth lines).

    Typical values: gastropod W 1.5-4, D 0-0.4, T 1-6; ammonoid / Nautilus W 1.5-3.5, D 0-0.5, T 0;
    bivalve W 10-10^4, D 0-0.2, T 0-1 (one valve). Returns anchors "apex", "aperture" (centre of the
    aperture), "lip" (outer lip), "body_whorl", "spire", "suture", "umbilicus", "axis" ((top, bottom)),
    and "project" (a function mapping 3D shell coordinates to the canvas).
    """
    th, X, Y, Z, C = raup_geometry(W, D, T, S, turns, n_theta, n_phi, rmin, hand)
    e, g = math.radians(elev), math.radians(azim)

    def rot(x, y, zz):
        xr = x * math.cos(g) - y * math.sin(g)
        yr = x * math.sin(g) + y * math.cos(g)
        return xr, yr, zz

    def screen(x, y, zz):
        xr, yr, zr = rot(x, y, zz)
        return xr, zr * math.cos(e) + yr * math.sin(e), -yr * math.cos(e) + zr * math.sin(e)

    sx, sy, dep = screen(X, Y, Z)
    pts = np.stack([sx, sy], axis=-1)
    if fit is None:
        fit = (size, size)
    lo, hi = pts.reshape(-1, 2).min(axis=0), pts.reshape(-1, 2).max(axis=0)
    k = min(fit[0] / (hi[0] - lo[0] or 1), fit[1] / (hi[1] - lo[1] or 1))
    off = np.asarray(center, float) - (lo + hi) / 2 * k

    def project(p3):
        p3 = np.asarray(p3, float)
        a, b, _ = screen(p3[..., 0], p3[..., 1], p3[..., 2])
        return np.stack([a, b], axis=-1) * k + off

    P3 = np.stack([X, Y, Z], axis=-1)
    pc = pts * k + off
    q = np.stack([pc[:-1, :-1], pc[1:, :-1], pc[1:, 1:], pc[:-1, 1:]], axis=2)  # (nt-1, np, 4, 2)
    d = (dep[:-1, :-1] + dep[1:, :-1] + dep[1:, 1:] + dep[:-1, 1:]) / 4
    e1 = P3[1:, :-1] - P3[:-1, :-1]
    e2 = P3[:-1, 1:] - P3[:-1, :-1]
    n = np.cross(e1, e2)
    mid = (P3[:-1, :-1] + P3[1:, 1:]) / 2
    out_dir = mid - ((C[:-1] + C[1:]) / 2)[:, None, :]
    n *= np.sign(np.sum(n * out_dir, axis=-1, keepdims=True) + 1e-12)
    n /= np.linalg.norm(n, axis=-1, keepdims=True) + 1e-12
    # camera and light directions in shell coordinates (undo the azimuth turn)
    cam_r = np.array([0.0, -math.cos(e), math.sin(e)])
    li_r = np.array([-0.5, -0.55, 0.67])
    li_r /= np.linalg.norm(li_r)

    def unrot(v):
        x, y, zz = v
        return np.array([x * math.cos(g) + y * math.sin(g), -x * math.sin(g) + y * math.cos(g), zz])

    cam, li = unrot(cam_r), unrot(cam_r * 0.4 + li_r)
    li /= np.linalg.norm(li)
    facing = n @ cam
    inten = np.clip(n @ li, 0, 1)
    dark, base, lite = P.edge(token), P.fill(token), P.light(token)
    levels = 11
    tones_out = [P.mix(dark, base, t / (levels - 1) * 2) if t < (levels - 1) / 2 else P.mix(base, lite, (t - (levels - 1) / 2) / ((levels - 1) / 2))
                 for t in range(levels)]
    inner = P.mix(dark, base, 0.12)
    cols = np.empty(d.shape, dtype=object)
    for i in range(d.shape[0]):
        band = bands and (i % bands == 0)
        for j in range(d.shape[1]):
            if facing[i, j] <= 0:
                c = inner
            else:
                lvl = int(round((0.25 + 0.75 * inten[i, j]) * (levels - 1)))
                c = tones_out[max(0, min(levels - 1, lvl - (1 if band else 0)))]
            cols[i, j] = c
    order = np.argsort(d, axis=None)
    polys = q.reshape(-1, 4, 2)[order]
    fc = cols.reshape(-1)[order]
    ax.add_collection(PolyCollection(list(polys), facecolors=list(fc), edgecolors=list(fc), linewidths=0.25, zorder=z,
                                     antialiaseds=True))
    tang = C[-1] - C[-2]
    tang /= np.linalg.norm(tang) or 1
    ap_n = np.asarray(rot(*tang))
    if abs(ap_n @ np.array([0.0, -math.cos(e), math.sin(e)])) > 0.35:  # aperture faces the viewer: draw its lip
        _line(ax, pc[-1], P.edge(token), lw=LINE * 0.8, z=z + 0.1)
    out = {"project": project}
    out["apex"] = tuple(project(C[0]))
    out["aperture"] = tuple(project(C[-1]))
    out["lip"] = tuple(pc[-1, 0])
    last = th > -2 * np.pi
    dc = np.where(last, screen(*C.T)[2], -np.inf)
    i_front = int(np.argmax(dc))
    out["body_whorl"] = tuple(pc[i_front, 0])
    i_up = int(np.argmin(np.abs(th - (th[i_front] - 2 * np.pi))))
    out["spire"] = tuple(pc[i_up, 0]) if th[0] < th[i_front] - 2 * np.pi else out["apex"]
    jj = int(round(n_phi * 0.3))
    out["suture"] = tuple(pc[i_front, jj])
    rad_end = (1 - D) / 2 * S
    zb = C[-1, 2] - rad_end
    out["umbilicus"] = tuple(project((0, 0, zb if T else 0)))
    out["axis"] = (tuple(project((0, 0, C[0, 2] + 0.15 * abs(C[-1, 2] - C[0, 2] + 1e-9) + 0.05))), tuple(project((0, 0, zb - 0.15))))
    out["scale"] = k
    return out


SUTURE_TYPES = ("orthoceratitic", "goniatitic", "ceratitic", "ammonitic")


def suture(ax, start, width, kind="ammonitic", lobes=3, amplitude=None, color=None, lw=LINE * 1.0, z=8, seed=3):
    """A cephalopod suture line (where a septum meets the shell wall), drawn left to right from ``start``; the
    aperture is up (+y), so saddles point up and lobes down. kind: "orthoceratitic" (straight to gently
    curved, nautiloids), "goniatitic" (smooth saddles, pointed lobes), "ceratitic" (smooth saddles, finely
    denticulate lobes), "ammonitic" (saddles and lobes both intricately frilled). Returns {"saddle", "lobe",
    "line" (points)}.
    """
    x0, y0 = start
    A = amplitude if amplitude is not None else width * 0.11
    x = np.linspace(0, width, 1400)
    th = 2 * np.pi * lobes * x / width
    c = (1 + np.cos(th)) / 2
    if kind == "orthoceratitic":
        y = A * 0.35 * np.cos(th / 2)
    elif kind == "goniatitic":
        y = A * (2 * c**0.35 - 1)
    else:
        y = A * (2 * c**0.6 - 1)
    pts = np.c_[x0 + x, y0 + y]
    if kind in ("ceratitic", "ammonitic"):
        q, nrm, _ = polyline(pts, n=1400, closed=False)
        rng = np.random.default_rng(seed)
        s = np.linspace(0, 1, len(q))
        f = np.zeros(len(q))
        if kind == "ceratitic":
            mask = np.clip((0.42 - c) / 0.2, 0, 1)
            f = A * 0.11 * np.abs(np.sin(2 * np.pi * lobes * 7 * s)) * mask
            f = -f
        else:  # fluted: second- and third-order lobes and saddles on every element
            for lvl, (fq, am) in enumerate(((7, 0.2), (21, 0.075), (63, 0.025))):
                f += A * am * np.sin(2 * np.pi * lobes * fq * s + (0.5 * np.pi if lvl else 0) + 0.15 * rng.uniform(-1, 1))
        pts = q + nrm * f[:, None]
    col = color or P.ink()
    _line(ax, pts, col, lw=lw, z=z)
    i_s = int(len(x) * (0.0 + 1.0 / lobes) * 0.999)
    i_l = int(len(x) * 0.5 / lobes)
    return {"saddle": tuple(pts[min(i_s, len(pts) - 1)]), "lobe": tuple(pts[i_l]), "line": pts}


def bivalve(ax, center, size, ribs=0, growth=7, token=SHELL, lw=LINE * 0.8, z=5):
    """The outside of a left bivalve valve (anterior to the left), ``size`` wide: umbo (beak) near the anterior
    end of the dorsal margin, ligament behind it, commarginal growth lines and optional radial ribs.
    Returns anchors "umbo", "ligament", "hinge", "growth_line", "ventral", "anterior", "posterior", "rib".
    """
    k = size
    c = np.asarray(center, float)
    ctrl = [(-0.16, 0.42), (0.1, 0.4), (0.38, 0.27), (0.5, 0.02), (0.4, -0.27), (0.02, -0.4), (-0.36, -0.3), (-0.5, -0.04),
            (-0.4, 0.26)]
    out_l = smooth_closed(ctrl, 200)
    U = np.array([-0.16, 0.44])
    V = out_l * k + c
    patch = _patch(ax, V, token, lw=lw, z=z)
    for sc in np.linspace(0.22, 0.9, growth):
        g = (U + (out_l - U) * sc) * k + c
        ln = _line(ax, g, P.edge(token), lw=lw * 0.5, z=z + 0.1)
        ln.set_clip_path(patch)
    if ribs:
        for t in np.linspace(0.32, 0.92, ribs):
            m = out_l[int(t * (len(out_l) - 1))]
            ln = _line(ax, [U * k + c, m * k + c], P.edge(token), lw=lw * 0.4, z=z + 0.1)
            ln.set_clip_path(patch)
    _patch(ax, _ellipse(U * k + c + [0, -0.03 * k], 0.07 * k, 0.05 * k, -20), face=P.light(token), edge=P.edge(token), lw=lw * 0.7,
           z=z + 0.2)
    lig = (np.array([[-0.06, 0.43], [0.16, 0.39], [0.15, 0.36], [-0.06, 0.4]])) * k + c
    _patch(ax, lig, face=P.edge(token), edge=P.edge(token), lw=lw * 0.5, z=z + 0.2)
    sg = (U + (out_l - U) * 0.56) * k + c
    return {"umbo": tuple(U * k + c), "ligament": tuple(lig.mean(axis=0)), "hinge": tuple(np.array([-0.32, 0.33]) * k + c),
            "growth_line": tuple(sg[110]), "ventral": tuple(np.array([0.02, -0.4]) * k + c),
            "anterior": tuple(np.array([-0.5, -0.04]) * k + c), "posterior": tuple(np.array([0.5, 0.02]) * k + c),
            "rib": tuple(((U + out_l[100]) / 2) * k + c)}


# ------------------------------------------------------------------ radiate and asymmetric bodies


def planes(ax, center, r, angles, color=None, lw=LINE * 0.9, z=30, extend=1.12):
    """Dashed lines through ``center`` marking planes of symmetry at ``angles`` (degrees); returns their ends."""
    c = np.asarray(center, float)
    col = color or P.edge("highlight")
    ends = []
    for a in angles:
        u = _dir(a) * r * extend
        _line(ax, [c - u, c + u], col, lw=lw, z=z, dashed=True)
        ends.append((tuple(c - u), tuple(c + u)))
    return ends


def sea_star(ax, center, r, arms=5, view="aboral", token="drug", disc=0.3, angle=90.0, lw=LINE * 0.8, z=5):
    """A sea star (Asteroidea) seen from above ("aboral": spines, madreporite in one interradius, anus) or
    below ("oral": mouth, ambulacral grooves lined by rows of tube feet). Pentaradial for ``arms=5``.
    Returns anchors "center", "arms" (tips), "arm", "disc", "madreporite", "anus", "mouth", "groove", "tube_feet".
    """
    c = np.asarray(center, float)
    a0 = math.radians(angle)
    ph = np.linspace(0, 2 * np.pi, 900, endpoint=False)
    sector = 2 * np.pi / arms
    dd = (ph - a0 + sector / 2) % sector - sector / 2
    f = np.cos(dd * arms / 2) ** 2
    rr = r * (disc + (1 - disc) * f ** 1.6)
    rr = np.minimum(rr, r * (1 - 0.18 * (np.abs(dd) / (sector / 2)) ** 0.0 * 0))  # keep tips at r
    outline = np.c_[c[0] + rr * np.cos(ph), c[1] + rr * np.sin(ph)]
    _patch(ax, outline, token, lw=lw, z=z)
    tips = [tuple(c + _dir(angle + 360 * k / arms) * r * 0.97) for k in range(arms)]
    out = {"center": tuple(c), "arms": tips, "arm": tuple(c + _dir(angle) * r * 0.6), "disc": tuple(c + _dir(angle + 180 / arms) * r * disc * 0.6)}
    E = P.edge(token)
    if view == "aboral":
        for k in range(arms):
            u = _dir(angle + 360 * k / arms)
            nv = _perp(u)
            for t in np.linspace(0.22, 0.88, 8):
                hw = r * (disc + (1 - disc) * 0.0) * 0.35 * (1 - t) + r * 0.015
                for off, sz in ((0, 0.035), (hw, 0.025), (-hw, 0.025)):
                    ax.add_patch(Circle(c + u * r * t + nv * off, r * sz * (1.1 - 0.5 * t), facecolor=P.light(token), edgecolor=E,
                                        lw=lw * 0.4, zorder=z + 0.2))
        mp = c + _dir(angle + 180 / arms) * r * disc * 0.55
        ax.add_patch(Circle(mp, r * 0.07, facecolor=P.mix(P.fill(token), E, 0.5), edgecolor=E, lw=lw * 0.7, zorder=z + 0.3))
        for j in range(5):
            aa = j * 36
            _line(ax, [mp - _dir(aa) * r * 0.055, mp + _dir(aa) * r * 0.055], E, lw=lw * 0.4, z=z + 0.35)
        out["madreporite"] = tuple(mp)
        ax.add_patch(Circle(c, r * 0.025, facecolor=E, edgecolor=E, lw=0, zorder=z + 0.3))
        out["anus"] = tuple(c)
    else:
        for k in range(arms):
            u = _dir(angle + 360 * k / arms)
            nv = _perp(u)
            g0, g1 = c + u * r * 0.12, c + u * r * 0.93
            _patch(ax, _rod(g0, g1, (r * 0.12, r * 0.08, r * 0.02), n=16, cap=0.4), face=P.light(token), edge=E, lw=lw * 0.5, z=z + 0.1)
            for t in np.linspace(0.2, 0.85, 9):
                for s in (1, -1):
                    w = r * 0.035 * (1.05 - 0.6 * t)
                    ax.add_patch(Circle(c + u * r * t + nv * s * w * 0.9, w * 0.55, facecolor=P.fill("highlight"),
                                        edgecolor=P.edge("highlight"), lw=lw * 0.35, zorder=z + 0.2))
            if k == 0:
                out["groove"] = tuple(c + u * r * 0.5)
                out["tube_feet"] = tuple(c + u * r * 0.62 + nv * r * 0.03)
        ax.add_patch(Circle(c, r * 0.12, facecolor=P.light(token), edgecolor=E, lw=lw * 0.6, zorder=z + 0.3))
        ax.add_patch(Circle(c, r * 0.055, facecolor=E, edgecolor=E, lw=0, zorder=z + 0.35))
        out["mouth"] = tuple(c)
    return out


def medusa(ax, center, r, token="channel", angle=0.0, lw=LINE * 0.8, z=5):
    """A scyphozoan medusa (moon jelly, Aurelia) in oral view: tetramerous radial symmetry. Four oral arms
    lie on the perradii around the square mouth; four horseshoe gonads lie interradially; branched per- and
    interradial canals alternate with unbranched adradial canals and join the ring canal; eight rhopalia
    sit in marginal notches; short tentacles fringe the bell margin. Returns anchors "bell", "mouth",
    "oral_arm", "gonad", "radial_canal", "ring_canal", "rhopalium", "tentacles".
    """
    c = np.asarray(center, float)
    E = P.edge(token)
    _patch(ax, _ellipse(c, r, r, n=200), face=_wash(token, 0.7), edge=E, lw=lw, z=z)
    for k in range(200):
        a = 2 * np.pi * k / 200
        u = np.array([math.cos(a), math.sin(a)])
        _line(ax, [c + u * r, c + u * r * 1.05], E, lw=lw * 0.35, z=z - 0.1)
    rc = 0.9 * r
    _patch(ax, _ellipse(c, rc, rc, n=200), face="none", edge=E, lw=lw * 0.6, z=z + 0.1)
    out = {"bell": tuple(c + _dir(angle + 67) * r * 0.75), "ring_canal": tuple(c + _dir(angle + 112) * rc)}
    for k in range(16):
        a = angle + 22.5 * k
        u = _dir(a)
        p0 = c + u * r * 0.28
        p1 = c + u * rc
        _line(ax, [p0, p1], E, lw=lw * 0.55, z=z + 0.1)
        if k % 2 == 0:  # branched per- and interradial canals
            m = c + u * r * 0.6
            for s in (1, -1):
                for t in (0.72, 0.82):
                    _line(ax, [m + u * r * (t - 0.6), c + _dir(a + s * 7 * (t - 0.6) / 0.2) * rc], E, lw=lw * 0.4, z=z + 0.1)
        if k == 2:
            out["radial_canal"] = tuple(c + u * r * 0.55)
    for k in range(8):
        a = angle + 45 * k
        u = _dir(a)
        ax.add_patch(Circle(c + u * r * 0.985, r * 0.03, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"),
                            lw=lw * 0.5, zorder=z + 0.3))
        if k == 1:
            out["rhopalium"] = tuple(c + u * r * 0.985)
    gt = "petal"
    for k in range(4):
        a = angle + 45 + 90 * k
        u = _dir(a)
        th = np.linspace(-150, 150, 40)
        rr = r * 0.17
        cc = c + u * r * 0.4
        arc = np.array([cc + _dir(a + 180 + t) * rr for t in th])
        _patch(ax, _band(arc, r * 0.07), gt, lw=lw * 0.6, z=z + 0.2)
        if k == 0:
            out["gonad"] = tuple(arc[8])
    for k in range(4):
        a = angle + 90 * k
        u = _dir(a)
        nv = _perp(u)
        pts = []
        for t in np.linspace(0.06, 0.5, 14):
            pts.append(c + u * r * t + nv * r * (0.035 + 0.02 * math.sin(t * 60)))
        for t in np.linspace(0.5, 0.06, 14):
            pts.append(c + u * r * t - nv * r * (0.035 + 0.02 * math.sin(t * 60 + 1)))
        _patch(ax, np.array(pts), face=P.light("receptor"), edge=P.edge("receptor"), lw=lw * 0.6, z=z + 0.3)
        if k == 0:
            out["oral_arm"] = tuple(c + u * r * 0.38)
    sq = [c + _dir(angle + 45 + 90 * k) * r * 0.09 for k in range(4)]
    _patch(ax, np.array(sq), face=P.edge("receptor"), edge=P.edge("receptor"), lw=lw * 0.6, z=z + 0.4)
    out["mouth"] = tuple(c)
    out["tentacles"] = tuple(c + _dir(angle - 30) * r * 1.03)
    return out


def ctenophore(ax, center, r, token="dna2", angle=0.0, lw=LINE * 0.8, z=5):
    """A cydippid ctenophore (Pleurobrachia) in aboral view: biradial symmetry. Eight comb rows; the apical
    organ (statocyst) at the centre; two tentacle sheaths with branched tentacles in the tentacular plane
    (``angle``); the flattened pharynx (dashed, beneath) in the perpendicular stomodeal plane.
    Returns anchors "statocyst", "comb_row", "tentacle", "tentacle_sheath", "pharynx", "body".
    """
    c = np.asarray(center, float)
    E = P.edge(token)
    body = _ellipse(c, r, r * 0.86, angle, n=160)
    _patch(ax, body, face=_wash(token, 0.6), edge=E, lw=lw, z=z)
    out = {"body": tuple(c + _dir(angle + 120) * r * 0.75)}
    ph = _ellipse(c, r * 0.12, r * 0.42, angle, n=60)
    _patch(ax, ph, face="none", edge=E, lw=lw * 0.7, z=z + 0.1).set_linestyle((0, (3, 2)))
    out["pharynx"] = tuple(c + _dir(angle + 90) * r * 0.42)
    for q in range(4):
        for s in (-1, 1):
            a = angle + 45 + 90 * q + s * 17
            u = _dir(a)
            nv = _perp(u)
            for t in np.linspace(0.3, 0.88, 11):
                p = c + u * r * t * (0.93 if q % 2 else 1.0)
                _patch(ax, [p + nv * r * 0.045, p + nv * r * 0.045 + u * r * 0.025, p - nv * r * 0.045 + u * r * 0.025, p - nv * r * 0.045],
                       face=P.fill("highlight"), edge=P.edge("highlight"), lw=lw * 0.35, z=z + 0.2)
            if q == 0 and s == 1:
                out["comb_row"] = tuple(c + u * r * 0.6)
    for s in (1, -1):
        u = _dir(angle + (0 if s > 0 else 180))
        sc = c + u * r * 0.42
        _patch(ax, _ellipse(sc, r * 0.16, r * 0.07, angle, n=40), face=P.light("receptor"), edge=P.edge("receptor"), lw=lw * 0.6,
               z=z + 0.25)
        nv = _perp(u)
        pts = np.array([sc + u * r * t + nv * r * 0.12 * math.sin(t * 5.5) * s for t in np.linspace(0.1, 1.25, 50)])
        _line(ax, pts, P.edge("receptor"), lw=lw * 0.9, z=z + 0.3)
        for i in range(6, 50, 5):
            d = pts[min(49, i + 1)] - pts[i]
            d /= np.linalg.norm(d)
            _line(ax, [pts[i], pts[i] + _perp(d) * r * 0.1 + d * r * 0.04], P.edge("receptor"), lw=lw * 0.4, z=z + 0.3)
            _line(ax, [pts[i], pts[i] - _perp(d) * r * 0.1 + d * r * 0.04], P.edge("receptor"), lw=lw * 0.4, z=z + 0.3)
        if s > 0:
            out["tentacle_sheath"] = tuple(sc)
            out["tentacle"] = tuple(pts[38])
    ax.add_patch(Circle(c, r * 0.07, facecolor=P.light("neutral"), edgecolor=P.edge("neutral"), lw=lw * 0.6, zorder=z + 0.4))
    ax.add_patch(Circle(c, r * 0.025, facecolor=P.edge("neutral"), edgecolor=P.edge("neutral"), lw=0, zorder=z + 0.45))
    out["statocyst"] = tuple(c)
    return out


def sponge(ax, center, width, height, token="antibody", tubes=((-0.25, 0.22, 0.95), (0.12, 0.17, 0.62), (0.36, 0.13, 0.4)),
           seed=2, lw=LINE * 0.8, z=5):
    """An asymmetrical sponge (Porifera): an irregular base with chimneys of unequal height ``tubes`` =
    ((x, half-width, top) as fractions of ``width`` / ``height``), each ending in an osculum; ostia dot the
    surface. Returns anchors "osculum", "ostium", "body".
    """
    c = np.asarray(center, float)
    W, H = width, height
    rng = np.random.default_rng(seed)
    base_y = -0.5
    pts = [(-0.5, base_y), (-0.15, base_y - 0.03), (0.2, base_y + 0.01), (0.5, base_y)]
    tl = sorted(tubes, key=lambda t: -t[0])
    pts.append((0.52, base_y + 0.22))
    for i, (x, hw, top) in enumerate(tl):
        y_top = base_y + top
        pts += [(x + hw, y_top - 0.25 * top), (x + hw * 0.95, y_top), (x - hw * 0.95, y_top), (x - hw, y_top - 0.25 * top)]
        if i < len(tl) - 1:
            nx = tl[i + 1][0] + tl[i + 1][1]
            pts.append(((x - hw + nx) / 2, base_y + 0.3 + 0.05 * rng.uniform(-1, 1)))
    pts.append((-0.55, base_y + 0.25))
    pts = np.array(pts)
    pts = pts + rng.uniform(-0.012, 0.012, pts.shape)
    outline = smooth_closed(pts * [W, H], 300) + c
    patch = _patch(ax, outline, token, lw=lw, z=z)
    E = P.edge(token)
    out = {"body": tuple(c + np.array([0.0, -0.3]) * [W, H])}
    for i, (x, hw, top) in enumerate(tubes):
        oc = c + np.array([x, base_y + top - 0.01]) * [W, H]
        _patch(ax, _ellipse(oc, hw * W * 0.72, 0.035 * H + hw * W * 0.12, n=40), face=P.mix(P.fill(token), E, 0.7), edge=E,
               lw=lw * 0.7, z=z + 0.2)
        if i == 0:
            out["osculum"] = tuple(oc)
    k = 0
    for _ in range(400):
        p = c + rng.uniform(-0.5, 0.5, 2) * [W, H]
        if patch.get_path().contains_point(p, radius=-0.08 * min(W, H)):
            ax.add_patch(Circle(p, 0.012 * min(W, H) * 1.6, facecolor=E, edgecolor=E, lw=0, zorder=z + 0.1))
            k += 1
            if k == 1:
                out["ostium"] = tuple(p)
            if k > 45:
                break
    return out


# ------------------------------------------------------------------ vertebrate forelimbs

# Proportions in units of a human humerus. Digits: angle (deg, -90 = straight down), metacarpal (length, width),
# phalanx lengths; options dx/dy (base offset), w (phalanx width), tip ("claw", "hoof", None).
FORELIMBS = {
    "human": dict(humerus=(1.0, 0.1), radius=(0.8, 0.065), ulna=(0.86, 0.07, 0.07, 1.0), gap=0.13, carpals=([4, 4], 0.36, 0.16),
                  digits=[("I", -128, (0.22, 0.06), [0.15, 0.11], dict(dx=-0.03, dy=0.06)),
                          ("II", -98, (0.34, 0.052), [0.2, 0.12, 0.085], {}),
                          ("III", -90, (0.32, 0.052), [0.22, 0.14, 0.09], {}),
                          ("IV", -83, (0.29, 0.048), [0.2, 0.13, 0.085], {}),
                          ("V", -76, (0.26, 0.046), [0.15, 0.1, 0.08], {})]),
    "cat": dict(humerus=(1.0, 0.1), radius=(0.96, 0.07), ulna=(1.05, 0.065, 0.11, 1.0), gap=0.12, carpals=([3, 4], 0.3, 0.14),
                digits=[("I", -112, (0.12, 0.05), [0.1, 0.09], dict(tip="claw", dy=0.04)),
                        ("II", -96, (0.38, 0.05), [0.18, 0.11, 0.11], dict(tip="claw")),
                        ("III", -91, (0.43, 0.05), [0.19, 0.12, 0.11], dict(tip="claw")),
                        ("IV", -87, (0.42, 0.05), [0.19, 0.12, 0.11], dict(tip="claw")),
                        ("V", -82, (0.35, 0.047), [0.17, 0.1, 0.1], dict(tip="claw"))]),
    "whale": dict(humerus=(0.5, 0.2), radius=(0.6, 0.15), ulna=(0.55, 0.13, 0.04, 1.0), gap=0.19, carpals=([3, 3], 0.48, 0.18),
                  digits=[("I", -100, (0.13, 0.07), [0.09], {}),
                          ("II", -94, (0.22, 0.075), [0.16, 0.14, 0.12, 0.1, 0.08, 0.07, 0.06], {}),
                          ("III", -89, (0.21, 0.075), [0.15, 0.13, 0.11, 0.09, 0.07], {}),
                          ("IV", -85, (0.17, 0.07), [0.12, 0.1, 0.08], {}),
                          ("V", -81, (0.12, 0.06), [0.08], {})], skin="flipper"),
    "bat": dict(humerus=(1.0, 0.1), radius=(1.55, 0.075), ulna=(1.55, 0.05, 0.05, 0.33), gap=0.11, carpals=([2, 3], 0.2, 0.1),
                digits=[("I", -150, (0.12, 0.05), [0.15, 0.1], dict(tip="claw", dx=-0.03, dy=0.03)),
                        ("II", -122, (1.4, 0.046), [0.12], dict(w=0.038)),
                        ("III", -103, (1.5, 0.048), [0.7, 0.6, 0.2], dict(w=0.038)),
                        ("IV", -82, (1.35, 0.046), [0.55, 0.45], dict(w=0.036)),
                        ("V", -62, (1.25, 0.044), [0.45, 0.35], dict(w=0.034))], skin="patagium"),
    "bird": dict(humerus=(1.0, 0.1), radius=(1.05, 0.045), ulna=(1.1, 0.075, 0.06, 1.0), gap=0.12, carpals=([2], 0.2, 0.08),
                 digits=[("alula", -104, (0.1, 0.05), [0.17], dict(dx=-0.02, dy=0.0, w=0.04)),
                         ("major", -90, (0.55, 0.055), [0.26, 0.12], dict(w=0.06)),
                         ("minor", -87, (0.5, 0.03), [0.1], dict(dx=0.02, w=0.03))], fused=True),
    "horse": dict(humerus=(0.8, 0.17), radius=(1.0, 0.11), ulna=(1.0, 0.07, 0.15, 0.45), gap=0.1, carpals=([3, 4], 0.24, 0.15),
                  digits=[("II", -91.5, (0.6, 0.034), [], dict(dx=0.032, taper=True, back=True)),
                          ("III", -90, (1.0, 0.09), [0.32, 0.17, 0.16], dict(w=0.085, tip="hoof")),
                          ("IV", -88.5, (0.6, 0.034), [], dict(dx=-0.032, taper=True, back=True))]),
}


def _long(a, b, w, knob=1.3):
    return _rod(a, b, (w * knob, w * 0.85, w * 0.72, w * 0.85, w * knob * 0.95), n=30, cap=0.8)


def _hull(pts):
    p = sorted(map(tuple, np.asarray(pts, float)))
    if len(p) < 3:
        return np.array(p)

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower, upper = [], []
    for q in p:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], q) <= 0:
            lower.pop()
        lower.append(q)
    for q in reversed(p):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], q) <= 0:
            upper.pop()
        upper.append(q)
    return np.array(lower[:-1] + upper[:-1])


def forelimb(ax, at, height, taxon="human", width=None, colored=True, color="bone", skin=True, lw=LINE * 0.7, z=5, spec=None):
    """A tetrapod forelimb skeleton (anterior view, shoulder at the top, radius and thumb on the left),
    bones coloured by homology (``BONE``): humerus, radius, ulna, carpals, metacarpals, phalanges.
    taxon: "human", "cat" (digitigrade, claws, short digit I), "whale" (toothed whale flipper: short broad
    bones, hyperphalangy of digits II-III), "bat" (long radius, reduced ulna, elongated metacarpals and
    phalanges of II-V supporting the patagium, free clawed thumb), "bird" (thin radius, stout ulna, two free
    carpals, carpometacarpus of fused metacarpals with alular, major and minor digits), "horse" (radius with
    the ulna reduced and fused, one digit III on a cannon bone, splint metacarpals II and IV, hoof); or a
    custom ``spec`` in the format of ``FORELIMBS``. Fitted into ``height`` (and ``width``), centred at ``at``;
    not to scale between taxa. Returns anchors per bone class, "digits" ({name: tip}), "shoulder", "elbow",
    "wrist", "olecranon", "skin".
    """
    S = spec or FORELIMBS[taxon]
    items = []  # (part, polygon, z offset)
    hl, hw = S["humerus"]
    sh = np.array([0.0, 0.0])
    el = np.array([0.0, -hl])
    items.append(("humerus", _long(sh, el, hw), 0.2))
    g = S["gap"]
    rl, rw = S["radius"]
    ul, uw, olec, frac = S["ulna"]
    r0 = el + [-g / 2, 0.02]
    r1 = r0 + [0, -rl]
    items.append(("radius", _long(r0, r1, rw), 0.3))
    u0 = el + [g / 2, olec]
    u1 = u0 + [0, -(ul + olec) * frac]
    if frac < 0.999:
        items.append(("ulna", _rod(u0, u1, (uw * 1.4, uw, uw * 0.55, uw * 0.15), n=24, cap=0.6), 0.25))
    else:
        items.append(("ulna", _long(u0, u1, uw), 0.25))
    wrist_y = min(r1[1], el[1] - ul + 0.02) - 0.02
    rows, CW, CH = S["carpals"]
    yb = wrist_y
    for nrow in rows:
        rh = CH / len(rows)
        for j in range(nrow):
            cw = CW / nrow
            cx = -CW / 2 + cw * (j + 0.5)
            cy = yb - rh / 2
            box = smooth_closed([(cx - cw * 0.44, cy - rh * 0.42), (cx + cw * 0.44, cy - rh * 0.42), (cx + cw * 0.46, cy + rh * 0.42),
                                 (cx - cw * 0.46, cy + rh * 0.42)], 40)
            items.append(("carpals", box, 0.35))
        yb -= rh
    bottom = yb
    digits = S["digits"]
    nd = len(digits)
    tips, meta_mid, phal_mid, longest = {}, None, None, -1
    meta_ends = []
    for k, (name, ang, (ml, mw), phal, opt) in enumerate(digits):
        u = _dir(ang)
        bx = -CW / 2 + CW * (k + 0.5) / nd + opt.get("dx", 0)
        p = np.array([bx, bottom + 0.01 + opt.get("dy", 0)])
        q = p + u * ml
        if opt.get("taper"):
            items.append(("metacarpals", _rod(p, q, (mw * 1.2, mw, mw * 0.5, mw * 0.15), n=24, cap=0.6), 0.32 if opt.get("back") else 0.4))
        else:
            items.append(("metacarpals", _long(p, q, mw, knob=1.2), 0.4))
        meta_ends.append((p, q))
        if ml > longest:
            longest, meta_mid = ml, (p + q) / 2
            main = k
        pw = opt.get("w", mw * 0.85)
        pp = q - u * 0.01
        for i, L in enumerate(phal):
            qq = pp + u * L
            w = pw * (1 - 0.12 * i)
            last = i == len(phal) - 1
            if last and opt.get("tip") == "claw":
                nv = _perp(u)
                poly = [pp + nv * w * 0.55, qq + nv * w * 0.05 + u * L * 0.15, pp - nv * w * 0.55]
                items.append(("phalanges", np.array(poly), 0.45))
            elif last and opt.get("tip") == "hoof":
                nv = _perp(u)
                poly = [pp + nv * w * 0.55, qq + nv * w * 1.0, qq - nv * w * 1.0, pp - nv * w * 0.55]
                items.append(("phalanges", smooth_closed(poly, 40), 0.45))
            elif last:
                items.append(("phalanges", _rod(pp, qq, (w * 1.1, w * 0.75, w * 0.45), n=16, cap=0.8), 0.45))
            else:
                items.append(("phalanges", _long(pp, qq, w, knob=1.15), 0.45))
            if k == main and i == 0:
                phal_mid = (pp + qq) / 2
            pp = qq - u * 0.01
        tips[name] = pp
    if phal_mid is None:
        phal_mid = meta_mid
    if S.get("fused"):  # carpometacarpus: metacarpals fused at both ends
        ps = np.array([e[0] for e in meta_ends])
        qs = np.array([e[1] for e in meta_ends[1:]])
        items.append(("metacarpals", smooth_closed(_hull(np.vstack([ps + [0, 0.035], ps - [0, 0.05]])), 40), 0.38))
        items.append(("metacarpals", smooth_closed(_hull(np.vstack([qs + [0, 0.04], qs - [0, 0.02]])), 40), 0.38))
    skin_poly = None
    kind = S.get("skin")
    if skin and kind == "flipper":
        allp = np.vstack([it[1] for it in items if it[0] != "humerus"])
        hull = _hull(allp)
        cen = hull.mean(axis=0)
        hull = cen + (hull - cen) * 1.12
        skin_poly = smooth_closed(hull, 160)
    elif skin and kind == "patagium":
        thumb = tips["I"] if "I" in tips else meta_ends[0][1]
        order = [tips[n] for n in ("II", "III", "IV", "V")]
        wr = np.array([0.0, bottom])
        poly = [sh + [-0.08, 0.0], r0 + (r1 - r0) * 0.55 + [-0.12, 0], thumb * 0.5 + wr * 0.5, order[0]]
        for a, b in zip(order[:-1], order[1:]):
            m = (a + b) / 2
            poly.append(m + (wr - m) * 0.28)
            poly.append(b)
        body = np.array([0.42, bottom * 0.8])
        m = (order[-1] + body) / 2
        poly += [m + (wr - m) * 0.3, body, np.array([0.36, -hl * 0.55]), sh + [0.16, -0.05]]
        skin_poly = np.array(poly)
    allp = np.vstack([it[1] for it in items] + ([skin_poly] if skin_poly is not None else []))
    lo, hi = allp.min(axis=0), allp.max(axis=0)
    k = height / (hi[1] - lo[1])
    if width:
        k = min(k, width / (hi[0] - lo[0]))
    off = np.asarray(at, float) - (lo + hi) / 2 * k

    def T(p):
        return np.asarray(p, float) * k + off

    if skin_poly is not None:
        _patch(ax, T(skin_poly), face=_wash("neutral", 0.6), edge=P.edge("neutral"), lw=lw * 0.8, z=z)
    for part, poly, zz in items:
        tok = BONE[part] if colored else color
        _patch(ax, T(poly), tok, lw=lw, z=z + zz)
    out = {"humerus": tuple(T((sh + el) / 2)), "radius": tuple(T(r0 + (r1 - r0) * 0.5)),
           "ulna": tuple(T(u0 + (u1 - u0) * (0.45 if frac > 0.9 else 0.4))), "carpals": tuple(T((0, (wrist_y + bottom) / 2))),
           "metacarpals": tuple(T(meta_mid)), "phalanges": tuple(T(phal_mid)), "digits": {n: tuple(T(p)) for n, p in tips.items()},
           "shoulder": tuple(T(sh)), "elbow": tuple(T(el)), "wrist": tuple(T((0, wrist_y))), "olecranon": tuple(T(u0)),
           "scale": k}
    if skin_poly is not None:
        out["skin"] = tuple(T(skin_poly[len(skin_poly) // 3]))
    return out


__all__ = [
    "MOUTH", "ANT", "LEG", "WING", "BONE", "ORDERS", "ANTENNA_TYPES", "MOUTHPART_TYPES", "LEG_TYPES", "WING_KINDS", "SUTURE_TYPES",
    "FORELIMBS", "antenna", "head", "leg", "wing", "haltere", "insect", "raup_geometry", "raup_shell", "suture", "bivalve",
    "planes", "sea_star", "medusa", "ctenophore", "sponge", "forelimb",
]
