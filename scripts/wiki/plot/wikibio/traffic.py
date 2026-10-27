"""Membrane traffic: coats and cages, buds and vesicles, GTPase switches, tethers, SNAREs and NSF (7.3.7-7.3.12).

    from wikibio import traffic as T
    T.band(ax, [(0, 2), (12, 2)])                        a membrane drawn as a filled band (any polyline)
    T.bud(ax, (0, 2), (12, 2), at=6, stage=0.7)           a membrane with a coated bud; returns anchors
    T.coated_vesicle(ax, (3, 4), 0.6, kind="copii")       a vesicle with its coat (copii, copi, clathrin, retromer, none)
    T.coat_arc(ax, (3, 4), 0.6, kind="clathrin")          only the coat, on an arc of a circle
    T.triskelion(ax, (2, 2), 0.9)                         one clathrin triskelion (three legs, terminal domains)
    T.cage(ax, (5, 5), 1.6, kind="clathrin")              a polyhedral cage in perspective (clathrin soccer ball, COPII cuboctahedron)
    T.dynamin(ax, (6, 3), 0.5, rings=3)                   a helical dynamin collar around a neck
    T.gtpase_cycle(ax, (6, 3), name="Rab")                GDP/GTP switch with GEF, GAP and optional GDI and effector
    T.tether(ax, (2, 1), (2, 3), kind="coiled")          a long coiled-coil tether or a multisubunit tethering complex
    T.snare_complex(ax, 5, 3.2, 1.8, zipped=0.6)          v- and t-SNARE helices zippering between two membranes
    T.nsf(ax, (8, 3), 0.5)                                the NSF hexamer (with alpha-SNAP adaptors)

Colours are palette tokens chosen once in ``TOKENS`` (clathrin, adaptor, COPII inner and outer layer,
COPI, small GTPase, v-SNARE, syntaxin, SNAP-25, ...); a script can override any of them by name.
Every function is deterministic and returns anchors (points or dicts of points) for arrows and callouts.
Membranes are drawn as bands of thickness ``MT``; "outside" of a bud is the side the coat is on (the
cytosol), as in all coated buds: coats assemble on the cytosolic face and buds grow into the cytosol.
"""

import math

import numpy as np
from matplotlib.patches import Circle, Ellipse, PathPatch, Polygon
from matplotlib.path import Path

from . import palette as P
from .core import LINE, arrow, box, label, polyline, reaction

MT = 0.16  # membrane band thickness (canvas units)

# object -> palette token (one place to change when the palette gains dedicated tokens)
TOKENS = {
    "clathrin": "antibody",
    "adaptor": "protein",
    "copii_outer": "positive",
    "copii_inner": "enzyme",
    "copi": "channel",
    "retromer": "drug",
    "gtpase": "drug",
    "dynamin": "metabolite",
    "gef": "enzyme",
    "gap": "neutral",
    "gdi": "lipid",
    "effector": "protein",
    "tether": "metabolite",
    "v_snare": "channel",
    "syntaxin": "receptor",
    "snap25": "positive",
    "nsf": "neutral",
    "snap": "highlight",
    "cargo": "highlight",
    "cargo_receptor": "receptor",
    "membrane": "membrane",
}


def tok(name):
    """The palette token used for a traffic object (``tok("clathrin")``); unknown names pass through."""
    return TOKENS.get(name, name)


# ---------------------------------------------------------------------------------------------
# membranes


def band(ax, points, thickness=MT, token="membrane", lumen=None, lumen_side=1, smooth=0, zorder=5):
    """A membrane along a polyline drawn as a filled band with two outlines.

    ``lumen`` tints a strip on one side (``lumen_side`` = +1 left of the direction of travel, -1 right)
    with a compartment token. ``smooth`` (points) applies a Gaussian smoothing to the centre line.
    Returns (centre points, unit normals).
    """
    q, nrm, length = polyline(points, n=max(60, int(np.hypot(*np.diff(np.asarray(points, float), axis=0).T).sum() / 0.03)))
    if smooth:
        q = _smooth(q, smooth)
        q, nrm, _ = polyline(q, n=len(q))
    a, b = q + nrm * thickness / 2, q - nrm * thickness / 2
    verts = np.vstack([a, b[::-1], a[:1]])
    ax.add_patch(PathPatch(Path(verts, closed=True), facecolor=P.fill(tok(token)), edgecolor="none", zorder=zorder))
    for line in (a, b):
        ax.plot(line[:, 0], line[:, 1], color=P.edge(tok(token)), lw=LINE * 0.75, zorder=zorder + 0.5,
                solid_joinstyle="round", solid_capstyle="butt")
    if lumen:
        w = 0.5
        side = q + nrm * lumen_side * (thickness / 2)
        far = q + nrm * lumen_side * (thickness / 2 + w)
        ax.add_patch(PathPatch(Path(np.vstack([side, far[::-1], side[:1]]), closed=True), facecolor=P.fill(lumen),
                               edgecolor="none", zorder=zorder - 1))
    return q, nrm


def _smooth(q, sigma):
    """Gaussian smoothing of a sampled curve, ends fixed."""
    k = int(3 * sigma)
    if k < 1:
        return q
    w = np.exp(-0.5 * (np.arange(-k, k + 1) / sigma) ** 2)
    w /= w.sum()
    pad = np.vstack([np.repeat(q[:1], k, 0), q, np.repeat(q[-1:], k, 0)])
    out = np.c_[np.convolve(pad[:, 0], w, "valid"), np.convolve(pad[:, 1], w, "valid")]
    out[0], out[-1] = q[0], q[-1]
    return out


def bud(ax, a, b, at=None, stage=0.6, r=0.7, kind="clathrin", side=1, thickness=MT, cargo=0, lumen=None, zorder=5):
    """A straight membrane from a to b with a spherical bud growing towards ``side`` (+1: left of a->b).

    ``stage`` 0..1: 0 flat coated patch, 0.3 shallow pit, 0.6 deep pit, 0.85 constricted neck (omega),
    1 a detached vesicle beside the resealed membrane. The coat (``kind``: clathrin, copii, copi,
    retromer or None) sits on the convex side. ``cargo`` puts that many cargo dots in the lumen of the bud.
    Returns a dict with ``center`` (bud centre), ``neck`` (point at the neck on the membrane line),
    ``tip`` (apex of the bud) and ``normal`` (unit vector into the bud direction).
    """
    a, b = np.asarray(a, float), np.asarray(b, float)
    u = (b - a) / np.linalg.norm(b - a)
    n = np.array([-u[1], u[0]]) * (1 if side >= 0 else -1)
    s0 = np.linalg.norm(b - a) / 2 if at is None else float(at)
    base = a + u * s0
    stage = float(np.clip(stage, 0, 1))
    if stage >= 0.999:
        band(ax, [a, b], thickness=thickness, zorder=zorder)
        c = base + n * (r * 1.25 + thickness)
        coated_vesicle(ax, c, r, kind=kind, cargo=cargo, zorder=zorder)
        return {"center": c, "neck": base, "tip": c + n * r, "normal": n}
    # centre height of the sphere above the membrane line: from -0.95 r (almost flat) to +0.9 r (omega)
    h = r * np.interp(stage, [0, 0.3, 0.6, 0.85, 0.999], [-0.95, -0.45, 0.25, 0.82, 0.92])
    half = math.sqrt(max(r * r - h * h, 1e-6))
    c = base + n * h
    # sphere arc from the left intersection, round the far side, to the right intersection
    th0 = math.atan2(-h, -half)  # angle (in the local u, n frame) of the left intersection
    th1 = math.atan2(-h, half)
    if th1 > th0:
        th1 -= 2 * math.pi
    ts = np.linspace(th0, th1, 160)
    arc = np.array([c + r * (math.cos(t) * u + math.sin(t) * n) for t in ts])
    left = np.linspace(a, base - u * half, 40)
    right = np.linspace(base + u * half, b, 40)
    pts = np.vstack([left, arc, right])
    q, nrm = band(ax, pts, thickness=thickness, smooth=3, zorder=zorder)
    # the lumen of the bud (the far side of the membrane from the coat) can be tinted
    if lumen:
        ax.add_patch(Circle(c, r - thickness / 2, facecolor=P.fill(lumen), edgecolor="none", zorder=zorder - 1))
    if kind:
        if stage < 0.15:  # a flat patch: draw the coat along the membrane instead
            _coat_line(ax, base - u * 0.9 * r, base + u * 0.9 * r, n, kind, thickness, zorder)
        else:
            # local angle t (frame u, n) -> world angle, keeping the sweep direction
            au = math.degrees(math.atan2(u[1], u[0]))
            hand = 1 if side >= 0 else -1
            trim = math.radians(18)
            t0, t1 = th0 - trim, th1 + trim  # the sweep runs downwards from th0 to th1; stay clear of the neck
            coat_arc(ax, c, r + thickness / 2, kind=kind, start=au + hand * math.degrees(t0),
                     end=au + hand * math.degrees(t1), zorder=zorder + 1)
    if cargo and stage >= 0.45:  # soluble cargo inside the bud once it encloses a lumen
        _cargo_dots(ax, c, r * 0.55, cargo, zorder + 2)
    return {"center": c, "neck": base, "tip": c + n * r, "normal": n,
            "neck_halfwidth": half, "neck_center": base}


def _cargo_dots(ax, c, r, k, zorder):
    rng = np.random.default_rng(int(abs(c[0]) * 131 + abs(c[1]) * 17) % 9973)
    for _ in range(k):
        t, d = rng.uniform(0, 2 * np.pi), r * math.sqrt(rng.uniform(0.05, 1))
        ax.add_patch(Circle((c[0] + d * math.cos(t), c[1] + d * math.sin(t)), 0.07, facecolor=P.fill(tok("cargo")),
                            edgecolor=P.edge(tok("cargo")), lw=0.5, zorder=zorder))


# ---------------------------------------------------------------------------------------------
# coats


def coat_arc(ax, center, r, kind="clathrin", start=0.0, end=360.0, zorder=7):
    """The coat of a vesicle or bud on the arc ``start``..``end`` (degrees) of a circle of radius ``r``
    (the outer surface of the membrane). Kinds: ``clathrin`` (adaptor layer + bristle lattice of
    triskelion legs), ``copii`` (Sec23/24 inner layer + Sec13/31 rod cage), ``copi`` (coatomer
    layer), ``retromer`` (arch-shaped dimers). Returns the outer radius of the coat."""
    c = np.asarray(center, float)
    k_ = min(1.0, max(0.35, r / 0.6))  # coat dimensions shrink with small vesicles
    full = abs(end - start) >= 359.9
    span = end - start
    L = abs(math.radians(span)) * r

    def at(t, rr):
        return c + rr * np.array([math.cos(math.radians(t)), math.sin(math.radians(t))])

    if kind == "clathrin":
        k = max(3, int(L / (0.2 * k_)))
        ts = np.linspace(start, end, k, endpoint=not full)
        for t in ts:  # adaptors (AP complexes) on the membrane
            p = at(t, r + 0.07 * k_)
            ax.add_patch(Ellipse(p, 0.12 * k_, 0.09 * k_, angle=t, facecolor=P.fill(tok("adaptor")), edgecolor=P.edge(tok("adaptor")),
                                 lw=0.5, zorder=zorder))
        ro = r + 0.32 * k_
        ts2 = np.linspace(start, end, max(3, int(L / (0.26 * k_))), endpoint=not full)
        e = P.edge(tok("clathrin"))
        f = P.fill(tok("clathrin"))
        pts_in = [at(t, r + 0.16 * k_) for t in ts2]
        pts_out = [at(t + span / max(len(ts2), 1) * 0.5, ro) for t in ts2]
        for i, (p, q) in enumerate(zip(pts_in, pts_out)):  # zigzag lattice (legs seen edge-on)
            seg = [p, q]
            if i + 1 < len(pts_in) or full:
                seg.append(pts_in[(i + 1) % len(pts_in)])
            seg = np.array(seg)
            ax.plot(seg[:, 0], seg[:, 1], color=e, lw=3.0 * k_, zorder=zorder, solid_capstyle="round", solid_joinstyle="round")
            ax.plot(seg[:, 0], seg[:, 1], color=f, lw=1.7 * k_, zorder=zorder + 0.1 * k_, solid_capstyle="round", solid_joinstyle="round")
        return ro
    if kind == "copii":
        k = max(3, int(L / (0.24 * k_)))
        ts = np.linspace(start, end, k, endpoint=not full)
        for t in ts:  # Sec23/24 bow ties
            p = at(t, r + 0.09 * k_)
            ax.add_patch(Ellipse(p, 0.21 * k_, 0.13 * k_, angle=t + 90, facecolor=P.fill(tok("copii_inner")),
                                 edgecolor=P.edge(tok("copii_inner")), lw=0.5, zorder=zorder))
        ro = r + 0.34 * k_
        ts2 = np.linspace(start, end, max(3, int(L / (0.45 * k_))), endpoint=not full)
        e, f = P.edge(tok("copii_outer")), P.fill(tok("copii_outer"))
        outer = np.array([at(t, ro) for t in np.linspace(start, end, 120)])
        ax.plot(outer[:, 0], outer[:, 1], color=e, lw=2.8 * k_, zorder=zorder, solid_capstyle="round")
        ax.plot(outer[:, 0], outer[:, 1], color=f, lw=1.6 * k_, zorder=zorder + 0.1 * k_, solid_capstyle="round")
        for t in ts2:  # Sec13/31 rods reaching to the inner layer (vertices of the cage)
            p, q = at(t, r + 0.17 * k_), at(t, ro)
            ax.plot([p[0], q[0]], [p[1], q[1]], color=e, lw=2.6 * k_, zorder=zorder, solid_capstyle="round")
            ax.plot([p[0], q[0]], [p[1], q[1]], color=f, lw=1.4 * k_, zorder=zorder + 0.1 * k_, solid_capstyle="round")
            ax.add_patch(Circle(q, 0.055 * k_, facecolor=f, edgecolor=e, lw=0.6, zorder=zorder + 0.2 * k_))
        return ro
    if kind == "copi":
        k = max(3, int(L / (0.2 * k_)))
        ts = np.linspace(start, end, k, endpoint=not full)
        for i, t in enumerate(ts):  # coatomer: one dense layer of triad-like blobs
            p = at(t, r + 0.14 * k_)
            ax.add_patch(Ellipse(p, 0.27 * k_, 0.19 * k_, angle=t + (20 if i % 2 else -20), facecolor=P.fill(tok("copi")),
                                 edgecolor=P.edge(tok("copi")), lw=0.6, zorder=zorder))
        return r + 0.28 * k_
    if kind == "retromer":
        k = max(2, int(L / (0.38 * k_)))
        ts = np.linspace(start, end, k, endpoint=not full)
        for t in ts:
            arch = np.array([at(t - 8, r + 0.04 * k_), at(t - 5, r + 0.26 * k_), at(t + 5, r + 0.26 * k_), at(t + 8, r + 0.04 * k_)])
            ax.plot(arch[:, 0], arch[:, 1], color=P.edge(tok("retromer")), lw=3.0 * k_, zorder=zorder, solid_joinstyle="round")
            ax.plot(arch[:, 0], arch[:, 1], color=P.fill(tok("retromer")), lw=1.8 * k_, zorder=zorder + 0.1 * k_, solid_joinstyle="round")
        return r + 0.3 * k_
    if kind in (None, "none"):
        return r
    raise ValueError(f"unknown coat kind {kind!r}")


def _coat_line(ax, p, q, n, kind, thickness, zorder):
    """A flat coat patch along the membrane segment p-q, on the side of normal n."""
    p, q = np.asarray(p, float), np.asarray(q, float)
    m = (p + q) / 2
    # approximate by an arc of a very large circle
    R = 30.0
    c = m - n * R
    ang = math.degrees(math.atan2(n[1], n[0]))
    half = math.degrees(np.linalg.norm(q - p) / 2 / R)
    coat_arc(ax, c, R + thickness / 2, kind=kind, start=ang - half, end=ang + half, zorder=zorder + 1)


def coated_vesicle(ax, center, r, kind="clathrin", cargo=0, receptors=0, lumen="vesicle", thickness=MT, zorder=8):
    """A vesicle of radius ``r`` (to the membrane centre) with its coat; ``kind=None`` for an uncoated vesicle.
    ``cargo``: number of soluble cargo dots; ``receptors``: cargo receptors spanning the membrane.
    Returns the outer radius (the coat's)."""
    c = np.asarray(center, float)
    ax.add_patch(Circle(c, r - thickness / 2, facecolor=P.fill(lumen), edgecolor="none", zorder=zorder - 0.5))
    t = np.linspace(0, 2 * np.pi, 200)
    ring = np.c_[c[0] + r * np.cos(t), c[1] + r * np.sin(t)]
    band(ax, ring, thickness=thickness, zorder=zorder)
    if receptors:
        for k in range(receptors):
            th = 2 * np.pi * (k + 0.3) / receptors
            d = np.array([math.cos(th), math.sin(th)])
            p0, p1 = c + d * (r - 0.18), c + d * (r + 0.1)
            ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=P.edge(tok("cargo_receptor")), lw=2.6, zorder=zorder + 1,
                    solid_capstyle="round")
            ax.add_patch(Circle(c + d * (r - 0.25), 0.07, facecolor=P.fill(tok("cargo")), edgecolor=P.edge(tok("cargo")),
                                lw=0.5, zorder=zorder + 1.2))
    if cargo:
        _cargo_dots(ax, c, (r - thickness) * 0.6, cargo, zorder + 1)
    return coat_arc(ax, c, r + thickness / 2, kind=kind, zorder=zorder + 1) if kind else r


# ---------------------------------------------------------------------------------------------
# clathrin triskelion and polyhedral cages


def _leg_path(center, size, angle):
    """Centre line of one triskelion leg: proximal segment, knee, distal segment curving clockwise."""
    s = np.linspace(0, 1, 50)
    # in a local frame (x along the leg): straight proximal part, then a bend of about 55 degrees
    bend = np.clip((s - 0.45) / 0.55, 0, 1)
    theta = -math.radians(55) * bend ** 1.3
    ds = size / (len(s) - 1)
    x = np.cumsum(np.r_[0, np.cos(theta[:-1]) * ds])
    y = np.cumsum(np.r_[0, np.sin(theta[:-1]) * ds])
    c, sn = math.cos(angle), math.sin(angle)
    return np.c_[x * c - y * sn, x * sn + y * c] + np.asarray(center, float)


def triskelion(ax, center, size=1.0, angle=0.0, token=None, labels=False, zorder=12):
    """One clathrin triskelion: three heavy-chain legs (proximal, knee, distal, N-terminal domain) from
    a central hub. ``angle`` (degrees) rotates it; ``labels=True`` names the parts. Returns the three
    terminal-domain centres."""
    t = tok(token or "clathrin")
    e, f = P.edge(t), P.fill(t)
    ends = []
    for k in range(3):
        pts = _leg_path(center, size, math.radians(angle + 90 + 120 * k))
        ax.plot(pts[:, 0], pts[:, 1], color=e, lw=5.2, zorder=zorder, solid_capstyle="round")
        ax.plot(pts[:, 0], pts[:, 1], color=f, lw=3.4, zorder=zorder + 0.1, solid_capstyle="round")
        tip = pts[-1] + (pts[-1] - pts[-3]) / np.linalg.norm(pts[-1] - pts[-3]) * size * 0.07
        ax.add_patch(Circle(tip, size * 0.09, facecolor=f, edgecolor=e, lw=0.9, zorder=zorder + 0.2))
        ends.append(tip)
        # light chain on the proximal segment
        lc = pts[8:20]
        ax.plot(lc[:, 0], lc[:, 1], color=P.edge(tok("adaptor")), lw=1.4, zorder=zorder + 0.3, solid_capstyle="round")
    ax.add_patch(Circle(center, size * 0.08, facecolor=f, edgecolor=e, lw=0.9, zorder=zorder + 0.4))
    if labels:
        leg = _leg_path(center, size, math.radians(angle + 90))
        from .core import callout
        callout(ax, leg[14], leg[14] + np.array([-size * 0.9, size * 0.15]), "Light chain", size="tiny")
        callout(ax, leg[28], leg[28] + np.array([size * 0.7, size * 0.2]), "Knee", size="tiny")
        callout(ax, ends[0], ends[0] + np.array([size * 0.55, size * 0.1]), "Terminal domain", size="tiny")
        callout(ax, np.asarray(center, float), np.asarray(center, float) + np.array([size * 0.9, -size * 0.45]), "Hub (vertex)",
                size="tiny")
    return [np.asarray(p) for p in ends]


PHI = (1 + 5 ** 0.5) / 2


def _even_perms(v):
    a, b, c = v
    return [(a, b, c), (b, c, a), (c, a, b)]


def polyhedron(kind="clathrin"):
    """(vertices, edges) of a cage: ``clathrin`` (truncated icosahedron, the 60-triskelion 'soccer ball':
    12 pentagons + 20 hexagons), ``cuboctahedron`` (the COPII Sec13/31 outer cage: 24 rods meeting at
    12 vertices), ``icosahedron``. Vertices are scaled to unit circumradius."""
    if kind in ("clathrin", "soccer", "truncated_icosahedron"):
        base = [(0, 1, 3 * PHI), (1, 2 + PHI, 2 * PHI), (PHI, 2, PHI ** 3)]
        vs = set()
        for b in base:
            for p in _even_perms(b):
                for sx in (1, -1):
                    for sy in (1, -1):
                        for sz in (1, -1):
                            vs.add((round(p[0] * sx, 9), round(p[1] * sy, 9), round(p[2] * sz, 9)))
        V = np.array(sorted(vs), float)
        d0 = 2.0
    elif kind == "cuboctahedron":
        vs = set()
        for i in range(3):
            for s1 in (1, -1):
                for s2 in (1, -1):
                    v = [0.0, 0.0, 0.0]
                    v[i], v[(i + 1) % 3] = s1, s2
                    vs.add(tuple(v))
        V = np.array(sorted(vs), float)
        d0 = math.sqrt(2)
    elif kind == "icosahedron":
        vs = set()
        for s1 in (1, -1):
            for s2 in (1, -1):
                for v in _even_perms((0.0, s1 * 1.0, s2 * PHI)):
                    vs.add(tuple(round(x, 9) for x in v))
        V = np.array(sorted(vs), float)
        d0 = 2.0
    else:
        raise ValueError(f"unknown polyhedron {kind!r}")
    D = np.linalg.norm(V[:, None] - V[None], axis=2)
    E = [(i, j) for i in range(len(V)) for j in range(i + 1, len(V)) if abs(D[i, j] - d0) < 1e-6]
    V = V / np.linalg.norm(V, axis=1).max()
    return V, E


def _rot(rx, ry, rz):
    rx, ry, rz = (math.radians(a) for a in (rx, ry, rz))
    Rx = np.array([[1, 0, 0], [0, math.cos(rx), -math.sin(rx)], [0, math.sin(rx), math.cos(rx)]])
    Ry = np.array([[math.cos(ry), 0, math.sin(ry)], [0, 1, 0], [-math.sin(ry), 0, math.cos(ry)]])
    Rz = np.array([[math.cos(rz), -math.sin(rz), 0], [math.sin(rz), math.cos(rz), 0], [0, 0, 1]])
    return Rz @ Ry @ Rx


def cage(ax, center, r, kind="clathrin", rotation=(20, 30, 0), token=None, hubs=True, vesicle=0.45, zorder=10):
    """A polyhedral coat cage seen in orthographic projection: back edges faint, front edges solid.

    ``kind`` as in ``polyhedron``; ``token`` defaults to clathrin (or the COPII outer layer for the
    cuboctahedron). ``hubs`` marks the front vertices (triskelion hubs / Sec13-31 vertices);
    ``vesicle`` draws the enclosed vesicle at that fraction of ``r`` (0 for none). Returns
    (projected vertex positions, edges)."""
    V, E = polyhedron(kind)
    t = tok(token or ("copii_outer" if kind == "cuboctahedron" else "clathrin"))
    R = _rot(*rotation)
    W = V @ R.T
    c = np.asarray(center, float)
    xy = W[:, :2] * r + c
    z = W[:, 2]
    if vesicle:
        ax.add_patch(Circle(c, r * vesicle, facecolor=P.fill("vesicle"), edgecolor=P.edge("vesicle"), lw=LINE * 0.8,
                            zorder=zorder))
    e, f = P.edge(t), P.fill(t)
    for i, j in sorted(E, key=lambda ij: z[ij[0]] + z[ij[1]]):
        zz = (z[i] + z[j]) / 2
        front = zz > -0.05
        seg = np.array([xy[i], xy[j]])
        if front:
            ax.plot(seg[:, 0], seg[:, 1], color=e, lw=3.6, zorder=zorder + 2 + zz, solid_capstyle="round")
            ax.plot(seg[:, 0], seg[:, 1], color=f, lw=2.1, zorder=zorder + 2.05 + zz, solid_capstyle="round")
        else:
            ax.plot(seg[:, 0], seg[:, 1], color=P.mix(e, P.surface(), 0.55), lw=1.4, zorder=zorder - 1 + zz,
                    solid_capstyle="round")
    if hubs:
        for i in range(len(V)):
            if z[i] > -0.05:
                ax.add_patch(Circle(xy[i], r * 0.035 + 0.02, facecolor=e, edgecolor="none", zorder=zorder + 3.2 + z[i]))
    return xy, E


# ---------------------------------------------------------------------------------------------
# dynamin, tethers, GTPase switches


def dynamin(ax, center, width, rings=3, pitch=0.16, axis=90.0, token=None, zorder=12):
    """A helical dynamin collar of ``rings`` turns around a membrane neck of outer ``width``, the helix
    axis at ``axis`` degrees (90: vertical neck). Returns the two ends of the collar on its axis."""
    t = tok(token or "dynamin")
    c = np.asarray(center, float)
    a = math.radians(axis)
    ua = np.array([math.cos(a), math.sin(a)])
    un = np.array([-ua[1], ua[0]])
    s = np.linspace(-rings / 2, rings / 2, 240 * rings)
    pts = c[None] + np.outer(s * pitch, ua) + np.outer(np.sin(2 * np.pi * s) * (width / 2 + 0.06), un) \
        + np.outer(np.cos(2 * np.pi * s) * 0.05, ua)
    front = np.cos(2 * np.pi * s) > 0
    for mask, lw_e, lw_f, z in ((~front, 3.0, 1.8, zorder - 2), (front, 4.0, 2.6, zorder)):
        seg = np.where(mask[:, None], pts, np.nan)
        ax.plot(seg[:, 0], seg[:, 1], color=P.edge(t), lw=lw_e, zorder=z, solid_capstyle="round")
        ax.plot(seg[:, 0], seg[:, 1], color=P.fill(t), lw=lw_f, zorder=z + 0.1, solid_capstyle="round")
    return c - ua * pitch * rings / 2, c + ua * pitch * rings / 2


def tether(ax, base, tip, kind="coiled", token=None, text=None, zorder=11):
    """A tethering factor from ``base`` (anchored on the target membrane) to ``tip`` (grasping the vesicle):
    ``coiled`` draws a long coiled-coil protein (golgin, EEA1), ``complex`` a multisubunit tethering
    complex (exocyst, HOPS, TRAPP) as a stalk of stacked subunits. Returns the tip."""
    t = tok(token or "tether")
    a, b = np.asarray(base, float), np.asarray(tip, float)
    d = b - a
    L = np.linalg.norm(d)
    u = d / L
    n = np.array([-u[1], u[0]])
    if kind == "coiled":
        s = np.linspace(0, 1, 300)
        for ph in (0, math.pi):
            pts = a + np.outer(s * L, u) + np.outer(0.05 * np.sin(2 * np.pi * s * L / 0.22 + ph), n)
            ax.plot(pts[:, 0], pts[:, 1], color=P.edge(t), lw=1.6, zorder=zorder, solid_capstyle="round")
        ax.add_patch(Circle(b, 0.1, facecolor=P.fill(t), edgecolor=P.edge(t), lw=0.8, zorder=zorder + 0.5))
    elif kind == "complex":
        k = max(3, int(L / 0.32))
        for i in range(k):
            p = a + u * L * (i + 0.5) / k + n * 0.04 * (-1) ** i
            ax.add_patch(Ellipse(p, L / k * 1.15, 0.28, angle=math.degrees(math.atan2(u[1], u[0])),
                                 facecolor=P.fill(t) if i % 2 == 0 else P.light(t), edgecolor=P.edge(t), lw=0.7,
                                 zorder=zorder + i * 0.01))
    else:
        raise ValueError(f"unknown tether kind {kind!r}")
    if text:
        label(ax, b + n * 0.35, text, size="tiny")
    return b


def _bw(text):
    """Width of a small label box that fits ``text`` (small font)."""
    return max(1.0, 0.15 * len(text) + 0.35)


def gtpase_cycle(ax, center, w=4.0, h=2.2, name="Rab", gef="GEF", gap="GAP", gdi=None, effector=None,
                 membrane=True, gdp_anchored=True, size="small", zorder=10):
    """The GDP/GTP switch of a small GTPase: X-GDP (left) and X-GTP (right); the upper arrow is nucleotide
    exchange (GDP out, GTP in) catalysed by the GEF, the lower one hydrolysis (Pi out) stimulated by the GAP.

    ``membrane=True`` lays a membrane under the two states (the GTP form is membrane-bound by its lipid
    anchor or amphipathic helix; ``gdp_anchored=False`` leaves the GDP form soluble, as for Sar1 and Arf). ``gdi`` (a name, e.g. "GDI") adds the cytosolic X-GDP-GDI complex
    above, extracting the GDP form and redelivering it; ``effector`` adds the effector bound to X-GTP.
    Returns a dict of anchors (gdp, gtp, gef, gap, gdi, effector, membrane_y).
    """
    cx, cy = center
    gdp, gtp = np.array([cx - w / 2, cy]), np.array([cx + w / 2, cy])
    bw, bh = 1.45, 0.62
    t = tok("gtpase")
    out = {"gdp": gdp, "gtp": gtp}
    if membrane:
        my = cy - bh / 2 - 0.95
        band(ax, [(cx - w / 2 - 1.3, my), (cx + w / 2 + 1.3, my)], zorder=zorder - 3)
        out["membrane_y"] = my
        for p in ((gdp, gtp) if gdp_anchored else (gtp,)):  # C-terminal tail and lipid anchor reaching into the membrane
            ax.plot([p[0], p[0]], [p[1] - bh / 2, my], color=P.edge(t), lw=1.6, zorder=zorder - 1)
    box(ax, gdp, bw, bh, token=t, text=f"{name}·GDP", size=size, zorder=zorder)
    box(ax, gtp, bw, bh, token=t, text=f"{name}·GTP", size=size, zorder=zorder)
    reaction(ax, gdp + (bw / 2 + 0.1, 0.18), gtp + (-bw / 2 - 0.1, 0.18), side=("GDP", "GTP"), bend=0.14, reach=0.5)
    reaction(ax, gtp + (-bw / 2 - 0.1, -0.18), gdp + (bw / 2 + 0.1, -0.18), side=None, bend=0.14)
    ge = np.array([cx, cy + 1.45])
    ga = np.array([cx - 0.35 - (_bw(gap) - 1.0) / 2, cy - 0.95])
    box(ax, ge, _bw(gef), 0.45, token=tok("gef"), text=gef, size=size, zorder=zorder)
    box(ax, ga, _bw(gap), 0.42, token=tok("gap"), text=gap, size=size, zorder=zorder)
    arrow(ax, ge - (0, 0.24), (cx, cy + 0.36), kind="catalysis", head=0.18)
    arrow(ax, (cx - 0.15, cy - 0.73), (cx - 0.12, cy - 0.37), kind="catalysis", head=0.18)
    pi = np.array([cx + 0.75, cy - 0.78])
    label(ax, pi, "Pᵢ", size=size)
    arrow(ax, (cx + 0.2, cy - 0.33), pi + (-0.18, 0.13), kind="process", head=0.12, lw=LINE * 0.8)
    out.update(gef=ge, gap=ga)
    if effector:
        ew = _bw(effector)
        ef = gtp + np.array([bw / 2 + 0.2 + ew / 2, 0.65])
        box(ax, ef, ew, 0.45, token=tok("effector"), text=effector, size=size, zorder=zorder)
        arrow(ax, gtp + (bw / 2 - 0.1, 0.25), ef - (ew / 2 - 0.05, 0.1), kind="link", lw=LINE * 1.2)
        out["effector"] = ef
    if gdi:
        gd = gdp + np.array([-0.75, h + 0.35])
        box(ax, gd, 2.0, 0.5, token=tok("gdi"), text=f"{name}·GDP·{gdi}", size=size, zorder=zorder)
        arrow(ax, gdp + (-0.2, bh / 2), gd + (0.25, -0.27), kind="process", bend=-0.15)
        arrow(ax, gd + (-0.4, -0.27), gdp + (-0.6, bh / 2), kind="process", bend=-0.15)
        mid = (gdp + gd) / 2
        label(ax, mid + (0.45, 0.0), "extraction", size="tiny", color=P.muted(), ha="left")
        label(ax, mid + (-0.6, 0.0), "delivery", size="tiny", color=P.muted(), ha="right")
        out["gdi"] = gd
    return out


# ---------------------------------------------------------------------------------------------
# SNAREs and NSF


def _helix(ax, pts, token, lw=3.2, wave=0.035, period=0.14, zorder=12):
    """A helix along a path drawn as a thick ribbon with a slight wave."""
    q, nrm, L = polyline(pts, n=max(30, int(np.hypot(*np.diff(np.asarray(pts, float), axis=0).T).sum() / 0.01)))
    s = np.r_[0, np.cumsum(np.hypot(*np.diff(q, axis=0).T))]
    w = q + nrm * (wave * np.sin(2 * np.pi * s / period))[:, None]
    ax.plot(w[:, 0], w[:, 1], color=P.edge(token), lw=lw + 1.4, zorder=zorder, solid_capstyle="round")
    ax.plot(w[:, 0], w[:, 1], color=P.fill(token), lw=lw, zorder=zorder + 0.1, solid_capstyle="round")
    return q


def _curve(a, b, c, n=40):
    """Quadratic Bezier a -> b with control c."""
    t = np.linspace(0, 1, n)[:, None]
    return (1 - t) ** 2 * np.asarray(a) + 2 * (1 - t) * t * np.asarray(c) + t ** 2 * np.asarray(b)


def snare_complex(ax, x, y_top, y_bot, zipped=0.5, length=2.2, direction=-1, thickness=MT, membranes=True,
                  labels=False, zorder=12):
    """A trans-SNARE complex between a vesicle membrane (horizontal, at ``y_top``) and a target membrane
    (at ``y_bot``). The transmembrane domains sit at ``x``; the four-helix bundle lies between the
    membranes and extends from its N-terminal end (``length`` away, on the side ``direction``) towards
    the membranes. ``zipped`` 0..1 is the fraction of the bundle assembled, from the N-terminal end:
    the unzipped C-terminal parts of the v-SNARE (vesicle) and of syntaxin and SNAP-25 (target) diverge
    to their anchors. ``membranes=False`` omits the two membrane bands (draw them yourself). Returns
    a dict with the bundle ends ('n_end', 'c_end') and the anchors ('v_anchor', 't_anchor')."""
    ym = (y_top + y_bot) / 2
    xN = x + direction * length
    xz = xN - direction * length * float(np.clip(zipped, 0, 1)) * 0.82
    if membranes:
        span = (min(x, xN) - 0.8, max(x, xN) + 0.8)
        band(ax, [(span[0], y_top), (span[1], y_top)], thickness=thickness, zorder=zorder - 4)
        band(ax, [(span[0], y_bot), (span[1], y_bot)], thickness=thickness, zorder=zorder - 4)
    gap = 0.075
    rows = {"v_snare": 1.5, "syntaxin": 0.5, "snap25": -0.5, "snap25b": -1.5}
    anchors = {"v_snare": (x, y_top), "syntaxin": (x, y_bot), "snap25": (x - direction * 0.35, y_bot),
               "snap25b": (x - direction * 0.35, y_bot)}
    for key, row in rows.items():
        token = tok("snap25" if key.startswith("snap25") else key)
        yy = ym + row * gap
        zipped_part = [(xN, yy), (xz, yy)]
        ax_ = anchors[key]
        tail_end = (ax_[0], ax_[1] + (-thickness / 2 if key == "v_snare" else thickness / 2))
        ctrl = (xz + (x - xz) * 0.6, yy + (0.15 if key == "v_snare" else -0.15) * (1 + abs(row)))
        tail = _curve((xz, yy), tail_end, ctrl)
        path = np.vstack([zipped_part[0:1], tail])
        _helix(ax, path, token, lw=2.6, zorder=zorder + (0.3 - 0.1 * row))
    # transmembrane domains and the SNAP-25 palmitoyl linker
    for key, (xx, yy) in (("v_snare", anchors["v_snare"]), ("syntaxin", anchors["syntaxin"])):
        token = tok(key)
        ax.add_patch(Ellipse((xx, yy), 0.12, thickness * 1.6, facecolor=P.fill(token), edgecolor=P.edge(token), lw=0.8,
                             zorder=zorder + 1))
    pa = anchors["snap25"]
    ax.add_patch(Circle((pa[0], pa[1] + thickness / 2 + 0.03), 0.05, facecolor=P.fill(tok("snap25")),
                        edgecolor=P.edge(tok("snap25")), lw=0.7, zorder=zorder + 1))
    # syntaxin's N-terminal Habc domain
    hx = xN + direction * 0.25
    ax.add_patch(Ellipse((hx, ym + 0.02), 0.42, 0.26, facecolor=P.fill(tok("syntaxin")), edgecolor=P.edge(tok("syntaxin")),
                         lw=0.8, zorder=zorder + 0.5))
    ax.plot([hx - direction * 0.18, xN], [ym, ym + 0.5 * gap], color=P.edge(tok("syntaxin")), lw=1.2, zorder=zorder + 0.4)
    out = {"n_end": np.array([xN, ym]), "c_end": np.array([xz, ym]), "v_anchor": np.array(anchors["v_snare"]),
           "t_anchor": np.array(anchors["syntaxin"]), "habc": np.array([hx, ym])}
    if labels:
        from .core import callout
        xm = (xN + xz) / 2
        callout(ax, (xm, ym + 1.5 * gap + 0.04), (xm - direction * 0.15, ym + 0.5), "v-SNARE", size="tiny")
        callout(ax, out["habc"] + (direction * 0.2, 0.05), (hx + direction * 0.35, ym + 0.5), "Syntaxin", size="tiny")
        callout(ax, (xm, ym - 1.5 * gap - 0.04), (xm - direction * 0.15, ym - 0.5), "SNAP-25", size="tiny")
    return out


def nsf(ax, center, r=0.5, snaps=3, token=None, text=None, zorder=12):
    """The NSF hexamer seen from the top (six AAA+ subunits in a ring) with ``snaps`` alpha-SNAP adaptors
    on one side. Returns the centre."""
    t = tok(token or "nsf")
    c = np.asarray(center, float)
    for k in range(6):
        th = 2 * np.pi * k / 6 + np.pi / 6
        p = c + 0.62 * r * np.array([math.cos(th), math.sin(th)])
        ax.add_patch(Circle(p, 0.36 * r, facecolor=P.fill(t) if k % 2 else P.light(t), edgecolor=P.edge(t), lw=0.8,
                            zorder=zorder))
    for k in range(snaps):
        th = -np.pi / 2 + (k - (snaps - 1) / 2) * 0.55
        p = c + 1.12 * r * np.array([math.cos(th), math.sin(th)])
        ax.add_patch(Ellipse(p, 0.42 * r, 0.24 * r, angle=math.degrees(th), facecolor=P.fill(tok("snap")),
                             edgecolor=P.edge(tok("snap")), lw=0.7, zorder=zorder + 0.2))
    if text:
        label(ax, c, text, size="tiny", color=P.on_fill(), zorder=zorder + 1)
    return c


__all__ = ["MT", "TOKENS", "tok", "band", "bud", "coat_arc", "coated_vesicle", "triskelion", "polyhedron", "cage", "dynamin",
           "tether", "gtpase_cycle", "snare_complex", "nsf"]
