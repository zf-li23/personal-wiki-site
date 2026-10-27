"""The cytoskeleton (7.3.13-7.3.15; spindle elements for 7.3.20-7.3.22): actin filaments and the networks they
build, microtubules and their ends, centrioles and centrosomes, motors on their tracks, the axoneme,
intermediate-filament assembly and the mitotic spindle.

    from wikibio import cytoskel as C
    C.actin_filament(ax, (1, 2), (8, 2), states="DDDPPTTT", decorate=True)   two-stranded helix (minus -> plus)
    C.filament(ax, (1, 1), (4, 2))                         a filament as a line (for networks), plus end marked
    C.branch(ax, (1, 1), (6, 1), at=0.4, length=2)         Arp2/3 branch at 70 degrees
    C.lamellipodium(ax, 1, 9, front=5, depth=2.5)          dendritic network under a protruding membrane
    C.filopodium(ax, (3, 2), length=2.5, angle=80)        parallel bundle in a membrane tube (fascin rungs)
    C.stress_fiber(ax, (1, 1), (8, 1))                     antiparallel bundle with myosin II and alpha-actinin
    C.myosin_minifilament(ax, (4, 4), 1.6)                 bipolar myosin II filament
    C.microtubule_lattice(ax, (1, 3), (9, 3), cap=0.2, plus_end="growing")   alpha/beta lattice, GTP cap
    C.tube(ax, (1, 1), (6, 3))                             a microtubule as a hollow tube (overviews)
    C.mt_cross_section(ax, (2, 2), 0.6)                    13 protofilaments with the seam
    C.tubulin_dimer(ax, (1, 1), 0.5, beta="GTP")
    C.gamma_turc(ax, (3, 1), 1.0)                          ring template with a nascent microtubule
    C.centriole_section(ax, (5, 5), 0.8, kind="triplet")  nine triplets around a cartwheel
    C.centriole(ax, (5, 5), 1.2, 0.5, angle=0)            side view of a centriole barrel
    C.centrosome(ax, (6, 4), 0.7, microtubules=14, length=3)
    C.dynein(ax, (5, 1.2), (5, 3.5))                       AAA+ ring, stalk, linker, tail (+ dynactin, adaptor)
    C.myosin_v(ax, (2, 1), (4.2, 1), (3.1, 3))           two heads with long lever arms on actin
    C.myosin_head(ax, (3, 1), lever=60)                    one myosin head bound to a filament (cross-bridge cycle)
    C.if_assembly(ax, (1, 2), "tetramer")                 monomer, dimer, tetramer, ulf, filament
    C.if_filament(ax, (1, 1), (8, 1))                      a ropelike 10 nm filament
    C.axoneme(ax, (5, 5), 2.2, kind="9+2")                 cross-section with dynein arms, spokes, nexin
    C.doublet(ax, (2, 2), 0.25, angle=0)                   one outer doublet (A + B tubule)
    C.chromatid_pair(ax, (5, 4), 1.2)                       a replicated chromosome with two kinetochores
    C.kinetochore(ax, (5, 4), angle=0)                      outer plate with Ndc80 fibrils
    C.spindle(ax, (8, 5), 3.0, 2.2)                         poles, astral, interpolar and kinetochore microtubules
    C.end_label(ax, point, "+")                             plus/minus end mark
    C.nucleotide_legend(ax, (1, 1), kind="actin")

Nucleotide states are written T (ATP or GTP), P (ADP-Pi or GDP-Pi) and D (ADP or GDP); ``states`` strings run
from the minus end to the plus end and are stretched over the filament. Colours come from ``TOKENS`` (one
place to change); every function is deterministic (fixed seeds) and returns anchors for arrows and callouts.
Directions: the plus end of a filament is ``b`` in every ``(a, b)`` pair.
"""

import math

import numpy as np
from matplotlib.patches import Circle, Ellipse, PathPatch, Polygon
from matplotlib.path import Path

from . import palette as P
from .core import LINE, blob, label

# object -> palette token
TOKENS = {
    "actin": "actin",
    "tubulin": "channel",       # beta-tubulin; alpha-tubulin is the paler shade
    "gtp": "atp",               # nucleotide triphosphate state
    "gamma": "highlight",       # gamma-tubulin / gamma-TuRC
    "pcm": "neutral",           # pericentriolar material
    "centriole": "channel",
    "if": "positive",           # intermediate filaments
    "arp23": "antibody",
    "formin": "positive",
    "profilin": "metabolite",
    "thymosin": "neutral",
    "capping": "receptor",
    "cofilin": "drug",
    "gelsolin": "carbohydrate",
    "fascin": "golgi",
    "actinin": "lipid",
    "filamin": "lipid",
    "myosin": "myosin",
    "kinesin": "enzyme",
    "dynein": "protein",
    "dynactin": "neutral",
    "adaptor": "receptor",
    "cargo": "vesicle",
    "membrane": "membrane",
    "chromosome": "chromatin",
    "kinetochore": "negative",
    "spoke": "antibody",
    "nexin": "neutral",
    "map": "drug",
}


def tok(name):
    """Palette token used for a cytoskeletal object (see ``TOKENS``); unknown names pass through."""
    return TOKENS.get(name, name)


def _frame(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    L = float(np.linalg.norm(b - a))
    u = (b - a) / (L or 1)
    return a, b, L, u, np.array([-u[1], u[0]])


def state_color(token, state):
    """Fill of a subunit of ``token`` in nucleotide state T, P or D: NTP gold, NDP-Pi pale gold, NDP the token's own fill."""
    base = P.fill(tok(token))
    nt = P.fill(tok("gtp"))
    return {"T": nt, "P": P.light(tok("gtp")), "D": base}.get(state, base)


def _state_at(states, frac):
    if not states:
        return "D"
    k = min(len(states) - 1, int(frac * len(states)))
    return states[k]


def end_label(ax, point, sign, offset=(0, 0), size="normal", color=None):
    """A plus or minus end mark (``sign`` "+" or "-") at ``point`` + ``offset``."""
    txt = "+" if sign == "+" else "−"
    return label(ax, (point[0] + offset[0], point[1] + offset[1]), txt, size=size, bold=True, color=color)


# ---------------------------------------------------------------------------------------------
# actin


def actin_filament(ax, a, b, r=0.1, states=None, token="actin", decorate=False, ends=True, crossover=13, zorder=9):
    """An actin filament from its minus (pointed) end ``a`` to its plus (barbed) end ``b``: two strands of
    globular subunits winding around each other (crossover every ``crossover`` subunits, 36 nm in reality).

    ``states`` colours subunits by bound nucleotide (T, P, D; see the module doc). ``decorate=True`` adds
    myosin S1 "arrowheads" that point to the minus end, as in the classic decoration experiment.
    Returns a dict with ``minus``, ``plus``, ``centers`` (subunit centres from minus to plus) and ``axis``.
    """
    a, b, L, u, n = _frame(a, b)
    step = r * 1.05
    k = max(2, int(L / step))
    centers = []
    for i in range(k):
        t = (i + 0.5) * step
        s = i % 2
        ph = 2 * math.pi * t / (crossover * step) + s * math.pi
        off = math.sin(ph) * r * 0.78
        depth = math.cos(ph)
        c = a + u * t + n * off
        centers.append(c)
        st = _state_at(states, (i + 0.5) / k)
        fc = state_color(token, st)
        e = Ellipse(c, r * 2.15, r * 1.75, angle=math.degrees(math.atan2(u[1], u[0])) + 18, facecolor=fc,
                    edgecolor=P.edge(tok(token)), lw=0.55, zorder=zorder + (0.5 if depth > 0 else 0))
        ax.add_patch(e)
    if decorate:
        for i in range(2, k - 1, 5):
            c = a + u * (i * step) + n * 0.0
            for side in (1, -1):
                p0 = c + n * side * r * 1.0
                p1 = c + n * side * r * 2.1 + u * r * 1.3
                ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=P.edge(tok("myosin")), lw=LINE * 1.4,
                        solid_capstyle="round", zorder=zorder + 1)
    if ends:
        end_label(ax, b + u * r * 2.0, "+", size="small")
        end_label(ax, a - u * r * 2.0, "-", size="small")
    return {"minus": a, "plus": b, "centers": centers, "axis": u, "normal": n}


def filament(ax, a, b, token="actin", lw=2.0, plus="dot", capped=False, zorder=8):
    """A filament drawn as a line from minus end ``a`` to plus end ``b`` (for networks and overviews).

    ``plus="dot"`` marks the growing plus end with a small bead, ``"none"`` leaves it bare;
    ``capped=True`` puts a capping-protein cap on the plus end instead. Returns the plus end.
    """
    a, b, L, u, n = _frame(a, b)
    ax.plot([a[0], b[0]], [a[1], b[1]], color=P.edge(tok(token)), lw=lw, solid_capstyle="round", zorder=zorder)
    ax.plot([a[0], b[0]], [a[1], b[1]], color=P.fill(tok(token)), lw=lw * 0.45, solid_capstyle="round", zorder=zorder + 0.1)
    if capped:
        cap(ax, b, u, size=lw * 0.045)
    elif plus == "dot":
        ax.add_patch(Circle(b, lw * 0.028, facecolor=P.fill(tok(token)), edgecolor=P.edge(tok(token)), lw=0.6,
                            zorder=zorder + 0.2))
    return b


def cap(ax, point, direction, size=0.09, token="capping", zorder=11):
    """A capping protein sitting on a plus end at ``point`` (``direction`` = filament axis, pointing outward)."""
    u = np.asarray(direction, float)
    u = u / (np.linalg.norm(u) or 1)
    c = np.asarray(point, float) + u * size * 0.6
    ax.add_patch(Ellipse(c, size * 2.4, size * 1.5, angle=math.degrees(math.atan2(u[1], u[0])) + 90,
                         facecolor=P.fill(tok(token)), edgecolor=P.edge(tok(token)), lw=0.6, zorder=zorder))
    return c


def arp23(ax, point, size=0.12, zorder=11):
    """The Arp2/3 complex at a branch point."""
    o = blob(point, size, size * 0.8, wobble=0.12, seed=23, k=7)
    ax.add_patch(PathPatch(Path(o, closed=True), facecolor=P.fill(tok("arp23")), edgecolor=P.edge(tok("arp23")),
                           lw=0.7, zorder=zorder))
    return tuple(point)


def branch(ax, a, b, at=0.5, length=1.5, side=1, angle=70.0, token="actin", lw=2.0, detailed=False, r=0.1,
           states=None, zorder=8):
    """A mother filament (a -> b) with a daughter nucleated by the Arp2/3 complex at fraction ``at``,
    growing at ``angle`` degrees towards its own plus end on ``side`` (+1 left of the mother, -1 right).

    ``detailed=True`` draws both filaments as subunit helices. Returns dict(branch, daughter_plus).
    """
    a, b, L, u, n = _frame(a, b)
    p = a + u * L * at
    th = math.radians(angle) * side
    d = np.array([u[0] * math.cos(th) - u[1] * math.sin(th), u[0] * math.sin(th) + u[1] * math.cos(th)])
    q = p + d * length
    if detailed:
        actin_filament(ax, a, b, r=r, states=states, token=token, ends=False, zorder=zorder)
        actin_filament(ax, p + d * r * 1.2, q, r=r, states=states, token=token, ends=False, zorder=zorder)
        arp23(ax, p + d * r * 0.6, size=r * 1.5, zorder=zorder + 3)
    else:
        filament(ax, a, b, token=token, lw=lw, zorder=zorder)
        filament(ax, p, q, token=token, lw=lw, zorder=zorder)
        arp23(ax, p, size=lw * 0.06, zorder=zorder + 3)
    return {"branch": p, "daughter_plus": q, "direction": d}


def _membrane_line(ax, pts, token="membrane", width=0.16, zorder=12):
    pts = np.asarray(pts, float)
    ax.plot(pts[:, 0], pts[:, 1], color=P.edge(tok(token)), lw=width * 72 * 0.45 + 1.2, solid_capstyle="round",
            solid_joinstyle="round", zorder=zorder)
    ax.plot(pts[:, 0], pts[:, 1], color=P.fill(tok(token)), lw=width * 72 * 0.45 - 0.4, solid_capstyle="round",
            solid_joinstyle="round", zorder=zorder + 0.1)


def lamellipodium(ax, x0, x1, front, depth=2.5, density=1.0, spread=35.0, lw=1.6, seed=4, membrane=True,
                  arp=True, capping=True, token="actin", zorder=8):
    """A dendritic actin network under a flat leading edge at height ``front`` between x0 and x1.

    Filaments point their plus ends upward (the protrusion direction) at about +-``spread`` degrees to the
    membrane normal; each one is a daughter that branched at 70 degrees from a mother of the opposite
    orientation (Arp2/3 complex at the branch point). Plus ends at the membrane are free and push it; the
    plus ends of older filaments behind the front are capped. The tree is built backward from the
    membrane until ``depth`` is filled. Returns dict(tips, capped, branches, membrane_y); deterministic
    for a given ``seed``.
    """
    rng = np.random.default_rng(seed)
    y0 = front - depth
    tips, capped, branches = [], [], []

    def unit(ang):
        return np.array([math.sin(math.radians(ang)), math.cos(math.radians(ang))])

    def make(plus, ang, is_capped, min_len, level):
        d = unit(ang)
        length = min_len + rng.uniform(0.35, 1.0)
        minus = plus - d * length
        # clip at the bottom and side walls
        for lim_ok in range(1):
            if minus[1] < y0:
                length = (plus[1] - y0) / d[1]
                minus = plus - d * length
            if minus[0] < x0 or minus[0] > x1:
                wall = x0 if minus[0] < x0 else x1
                length = (plus[0] - wall) / d[0]
                minus = plus - d * length
        if length < 0.12:
            return
        filament(ax, minus, plus, token=token, lw=lw, plus="none" if is_capped else "dot",
                 capped=is_capped and capping, zorder=zorder)
        (capped if is_capped else tips).append(plus)
        if minus[1] <= y0 + 0.05 or minus[0] <= x0 + 0.02 or minus[0] >= x1 - 0.02 or level > 12:
            return
        branches.append(minus)
        # the mother runs through the branch point with the opposite orientation; its plus end lies ahead
        md = unit(-ang)
        ahead = rng.uniform(0.15, 0.7)
        mplus = minus + md * ahead
        if mplus[1] > front - 0.08:
            mplus = minus + md * max(0.05, (front - 0.08 - minus[1]) / md[1])
        reach = mplus[1] >= front - 0.1
        make(mplus, -ang, not reach, float(np.linalg.norm(mplus - minus)), level + 1)
        # occasionally a second daughter from the same mother further back
        if rng.uniform() < 0.35 * density:
            q = minus - md * rng.uniform(0.3, 0.8)
            if y0 < q[1] < front - 0.4 and x0 < q[0] < x1:
                branches.append(q)
                tip = q + unit(ang) * rng.uniform(0.3, 0.9)
                make(tip, ang, True, float(np.linalg.norm(tip - q)), level + 1)

    n = max(2, int((x1 - x0) * 1.6 * density))
    for x in np.linspace(x0 + 0.15, x1 - 0.15, n) + rng.uniform(-0.12, 0.12, n):
        make(np.array([x, front - 0.06]), rng.choice([-spread, spread]) + rng.uniform(-6, 6), False, 0.0, 0)
    if arp:
        for p in branches:
            arp23(ax, p, size=lw * 0.055, zorder=zorder + 3)
    if membrane:
        _membrane_line(ax, [(x0 - 0.1, front), (x1 + 0.1, front)], zorder=zorder + 4)
    return {"tips": tips, "capped": capped, "branches": branches, "membrane_y": front}


def filopodium(ax, base, length=2.5, width=0.5, angle=90.0, n=5, fascin=True, membrane=True, tip=True,
               token="actin", lw=1.4, zorder=8):
    """A filopodium: ``n`` parallel actin filaments (plus ends at the tip) cross-linked by fascin, inside a
    finger of plasma membrane, with a tip complex (formin/Ena-VASP). Returns dict(tip, base, axis)."""
    a = np.asarray(base, float)
    th = math.radians(angle)
    u = np.array([math.cos(th), math.sin(th)])
    nn = np.array([-u[1], u[0]])
    tipc = a + u * length
    for i in range(n):
        off = (i - (n - 1) / 2) * (width * 0.7 / max(1, n - 1))
        s = a + nn * off - u * 0.3
        e = tipc + nn * off * 0.85 - u * 0.12
        filament(ax, s, e, token=token, lw=lw, plus="none", zorder=zorder)
    if fascin:
        for t in np.arange(0.25, length - 0.25, 0.32):
            p = a + u * t
            q0, q1 = p - nn * width * 0.33, p + nn * width * 0.33
            ax.plot([q0[0], q1[0]], [q0[1], q1[1]], color=P.edge(tok("fascin")), lw=1.1, zorder=zorder + 0.3)
    if tip:
        ax.add_patch(Ellipse(tipc - u * 0.06, width * 0.75, 0.16, angle=math.degrees(th) + 90,
                             facecolor=P.fill(tok("formin")), edgecolor=P.edge(tok("formin")), lw=0.6, zorder=zorder + 1))
    if membrane:
        s = np.linspace(-math.pi / 2, math.pi / 2, 30)
        hw = width / 2 + 0.06
        cap_pts = [tipc + u * hw * math.cos(t) * 0.9 + nn * hw * math.sin(t) for t in s]
        left = [a + nn * hw, tipc + nn * hw]
        right = [tipc - nn * hw, a - nn * hw]
        pts = np.vstack([left, cap_pts[::-1], right])
        ax.plot(pts[:, 0], pts[:, 1], color=P.edge(tok("membrane")), lw=2.6, solid_capstyle="round", zorder=zorder + 2)
        ax.plot(pts[:, 0], pts[:, 1], color=P.fill(tok("membrane")), lw=1.2, solid_capstyle="round", zorder=zorder + 2.1)
    return {"tip": tipc, "base": a, "axis": u}


def myosin_minifilament(ax, center, length=1.6, angle=0.0, heads=4, token="myosin", lw=2.4, zorder=10):
    """A bipolar myosin II filament: a central bare rod and heads pointing away from the centre at both ends."""
    c = np.asarray(center, float)
    th = math.radians(angle)
    u = np.array([math.cos(th), math.sin(th)])
    n = np.array([-u[1], u[0]])
    a, b = c - u * length / 2, c + u * length / 2
    ax.plot([a[0], b[0]], [a[1], b[1]], color=P.edge(tok(token)), lw=lw, solid_capstyle="round", zorder=zorder)
    for end, sgn in ((a, -1), (b, 1)):
        for k in range(heads):
            t = (k + 0.5) / heads * length * 0.32
            p = end - u * sgn * t
            side = 1 if k % 2 == 0 else -1
            q = p + u * sgn * 0.13 + n * side * 0.17
            ax.plot([p[0], q[0]], [p[1], q[1]], color=P.edge(tok(token)), lw=lw * 0.5, zorder=zorder)
            ax.add_patch(Ellipse(q, 0.16, 0.1, angle=math.degrees(th), facecolor=P.fill(tok(token)),
                                 edgecolor=P.edge(tok(token)), lw=0.5, zorder=zorder + 0.2))
    return {"left": a, "right": b}


def stress_fiber(ax, a, b, width=0.5, units=4, token="actin", lw=1.4, zorder=8):
    """A contractile bundle: antiparallel actin filaments, alpha-actinin dense bodies and myosin II minifilaments
    in a sarcomere-like repeat between ``a`` and ``b``. Returns dict(units=[centres of myosin filaments])."""
    a, b, L, u, n = _frame(a, b)
    seg = L / units
    mids = []
    for k in range(units + 1):
        p = a + u * k * seg
        ax.add_patch(Ellipse(p, 0.12, width * 1.05, angle=math.degrees(math.atan2(u[1], u[0])),
                             facecolor=P.fill(tok("actinin")), edgecolor=P.edge(tok("actinin")), lw=0.6, zorder=zorder + 1))
    for k in range(units):
        p0 = a + u * k * seg
        p1 = p0 + u * seg
        for j, off in enumerate((-0.35, -0.12, 0.12, 0.35)):
            o = n * off * width
            if j % 2 == 0:
                ax.plot(*np.array([p0 + o, p0 + u * seg * 0.62 + o]).T, color=P.edge(tok(token)), lw=lw, zorder=zorder)
            else:
                ax.plot(*np.array([p1 + o, p1 - u * seg * 0.62 + o]).T, color=P.edge(tok(token)), lw=lw, zorder=zorder)
        m = (p0 + p1) / 2
        mids.append(m)
        myosin_minifilament(ax, m, length=seg * 0.55, angle=math.degrees(math.atan2(u[1], u[0])), heads=2, lw=1.8,
                            zorder=zorder + 2)
    return {"units": mids}


# ---------------------------------------------------------------------------------------------
# microtubules


def tubulin_dimer(ax, center, size=0.4, angle=90.0, beta="GTP", zorder=10):
    """An alpha/beta-tubulin heterodimer, beta towards the plus end (``angle`` = direction of the plus end).
    ``beta`` is "GTP", "GDP-Pi" or "GDP". Returns the plus-end and minus-end points."""
    c = np.asarray(center, float)
    th = math.radians(angle)
    u = np.array([math.cos(th), math.sin(th)])
    st = {"GTP": "T", "GDP-Pi": "P", "GDP": "D"}.get(beta, "D")
    for sgn, fc in ((-1, P.light(tok("tubulin"))), (1, state_color("tubulin", st))):
        p = c + u * sgn * size * 0.25
        ax.add_patch(Ellipse(p, size * 0.5, size * 0.46, angle=math.degrees(th), facecolor=fc,
                             edgecolor=P.edge(tok("tubulin")), lw=0.6, zorder=zorder))
    return {"plus": c + u * size * 0.5, "minus": c - u * size * 0.5}


def microtubule_lattice(ax, a, b, width=0.8, rows=5, cap=0.15, plus_end="growing", dimer=None, curl=1.0,
                        ends=True, seed=1, zorder=9):
    """A microtubule seen from the side, minus end ``a`` to plus end ``b``: ``rows`` visible protofilaments of
    alpha (pale) and beta (coloured) tubulin, staggered as in the helical B lattice.

    ``cap`` is the fraction of the length at the plus end in the GTP state (GTP cap; a short GDP-Pi zone
    follows). ``plus_end`` is "growing" (a slightly flared sheet), "shrinking" (protofilaments peel back
    in curls, no cap) or "blunt". Returns dict(minus, plus, cap_start, axis, normal).
    """
    a, b, L, u, n = _frame(a, b)
    rng = np.random.default_rng(seed)
    dl = dimer or width / 3.2          # dimer length along the axis
    mono = dl / 2
    if plus_end == "shrinking":
        cap = 0.0
    cap_start = L * (1 - cap)
    ys = [(j - (rows - 1) / 2) / ((rows - 1) / 2 or 1) for j in range(rows)]   # -1..1 across the width
    for j, yy in enumerate(ys):
        # projected position and apparent width of this protofilament on a cylinder
        ang = math.asin(max(-1, min(1, yy * 0.92)))
        off = math.sin(ang) * width / 2
        w = width / rows * (0.55 + 0.45 * math.cos(ang)) * 1.15
        stagger = (j * 0.23 % 1.0) * dl
        extra = 0.0
        if plus_end == "growing":
            extra = rng.uniform(-1.5, 1.0) * dl if 0 < j < rows - 1 else rng.uniform(-2.5, -0.5) * dl
        if plus_end == "shrinking":
            extra = -rng.uniform(0.5, 2.5) * dl
        stop = L + extra
        t = -stagger
        k = 0
        while t + mono <= stop:
            if t >= 0:
                is_beta = k % 2 == 1
                st = "D"
                if t > cap_start:
                    st = "T"
                elif t > cap_start - 2 * dl and cap > 0:
                    st = "P"
                fc = state_color("tubulin", st) if is_beta else P.light(tok("tubulin"))
                c = a + u * (t + mono / 2) + n * off
                ax.add_patch(Ellipse(c, mono * 0.98, w * 0.92, angle=math.degrees(math.atan2(u[1], u[0])), facecolor=fc,
                                     edgecolor=P.edge(tok("tubulin")), lw=0.45, zorder=zorder + 0.3 * math.cos(ang)))
            t += mono
            k += 1
        if plus_end == "shrinking" and abs(yy) > 0.3:
            # curled protofilament ends peeling outward
            start = a + u * t + n * off
            outward = n * (1 if yy > 0 else -1)
            nseg = 5
            ang0 = 0.0
            p = start.copy()
            for q in range(nseg):
                ang0 += 0.55 * curl
                d = u * math.cos(ang0) + outward * math.sin(ang0)
                c = p + d * mono / 2
                is_beta = (k + q) % 2 == 1
                fc = state_color("tubulin", "D") if is_beta else P.light(tok("tubulin"))
                ax.add_patch(Ellipse(c, mono * 0.98, w * 0.92, angle=math.degrees(math.atan2(d[1], d[0])), facecolor=fc,
                                     edgecolor=P.edge(tok("tubulin")), lw=0.45, zorder=zorder + 0.5))
                p = p + d * mono
    if ends:
        end_label(ax, b + u * width * 0.55, "+", size="small")
        end_label(ax, a - u * width * 0.35, "-", size="small")
    return {"minus": a, "plus": b, "cap_start": a + u * cap_start, "axis": u, "normal": n}


def tube(ax, a, b, width=0.22, token="tubulin", plus="none", lw=0.9, zorder=8):
    """A microtubule as a hollow tube (two walls and a pale lumen) from minus end ``a`` to plus end ``b``.
    ``plus`` = "dot" marks the plus end. Returns the plus end."""
    a, b, L, u, n = _frame(a, b)
    hw = width / 2
    quad = [a + n * hw, b + n * hw, b - n * hw, a - n * hw]
    ax.add_patch(Polygon(quad, closed=True, facecolor=P.light(tok(token)), edgecolor="none", zorder=zorder))
    for s in (1, -1):
        p, q = a + n * hw * s, b + n * hw * s
        ax.plot([p[0], q[0]], [p[1], q[1]], color=P.edge(tok(token)), lw=lw, solid_capstyle="butt", zorder=zorder + 0.1)
    if plus == "dot":
        ax.add_patch(Circle(b, hw * 0.9, facecolor=P.fill(tok("gtp")), edgecolor=P.edge(tok(token)), lw=0.5,
                            zorder=zorder + 0.2))
    return b


def mt_line(ax, a, b, token="tubulin", lw=1.5, plus=False, dashed=False, zorder=8):
    """A microtubule as a single line (spindles and dense arrays); ``plus=True`` adds a plus-end tick."""
    a, b, L, u, n = _frame(a, b)
    ax.plot([a[0], b[0]], [a[1], b[1]], color=P.edge(tok(token)), lw=lw, solid_capstyle="round",
            ls=(0, (3, 2)) if dashed else "-", zorder=zorder)
    if plus:
        ax.add_patch(Circle(b, lw * 0.03, facecolor=P.fill(tok(token)), edgecolor=P.edge(tok(token)), lw=0.5, zorder=zorder + 0.1))
    return b


def mt_cross_section(ax, center, r=0.5, n=13, seam=True, token="tubulin", zorder=10):
    """A microtubule in cross-section: ``n`` protofilaments in a ring (25 nm across); the seam is marked
    by a small gap. Returns the list of protofilament centres."""
    c = np.asarray(center, float)
    pr = r * math.sin(math.pi / n) * 1.05
    cs = []
    for i in range(n):
        th = math.pi / 2 + 2 * math.pi * i / n
        p = c + r * np.array([math.cos(th), math.sin(th)])
        cs.append(p)
        fc = P.fill(tok(token)) if i % 2 == 0 else P.light(tok(token))
        ax.add_patch(Circle(p, pr, facecolor=fc, edgecolor=P.edge(tok(token)), lw=0.6, zorder=zorder))
    if seam:
        th = math.pi / 2 - math.pi / n
        p = c + (r + pr * 1.9) * np.array([math.cos(th), math.sin(th)])
        q = c + (r - pr * 1.9) * np.array([math.cos(th), math.sin(th)])
        ax.plot([p[0], q[0]], [p[1], q[1]], color=P.muted(), lw=0.8, ls=(0, (2, 1.5)), zorder=zorder + 1)
    return cs


def gamma_turc(ax, center, width=1.0, microtubule=True, mt_length=1.2, zorder=10):
    """A gamma-tubulin ring complex seen obliquely (a lock-washer ring of gamma-tubulins on accessory proteins)
    templating the minus end of a microtubule that grows upward. Returns the microtubule plus end."""
    c = np.asarray(center, float)
    rx, ry = width / 2, width * 0.18
    ax.add_patch(Ellipse(c - np.array([0, ry * 0.9]), width * 1.08, ry * 2.6, facecolor=P.light(tok("pcm")),
                         edgecolor=P.edge(tok("pcm")), lw=0.7, zorder=zorder - 1))
    pts = []
    for i in range(13):
        th = 2 * math.pi * i / 13 - math.pi / 2
        pts.append((c + np.array([rx * math.cos(th), ry * math.sin(th)]), math.sin(th)))
    for p, s in sorted(pts, key=lambda x: -x[1]):
        ax.add_patch(Circle(p, width * 0.085, facecolor=P.fill(tok("gamma")), edgecolor=P.edge(tok("gamma")), lw=0.5,
                            zorder=zorder + (0.4 if s < 0 else 0)))
    top = c
    if microtubule:
        a = c + np.array([0, ry * 0.4])
        top = a + np.array([0, mt_length])
        microtubule_lattice(ax, a, top, width=width * 0.92, rows=5, cap=0.25, plus_end="growing", ends=False,
                            zorder=zorder - 0.5)
    return top


def _triplet(ax, center, r, angle, k=3, token="centriole", zorder=10):
    """k fused tubules (A, B, C) along a line at ``angle`` (degrees), A first; returns their centres."""
    c = np.asarray(center, float)
    th = math.radians(angle)
    d = np.array([math.cos(th), math.sin(th)])
    out = []
    for i in range(k):
        p = c + d * (i - (k - 1) / 2) * r * 1.55
        out.append(p)
        fc = P.fill(tok(token)) if i == 0 else P.light(tok(token))
        ax.add_patch(Circle(p, r, facecolor=fc, edgecolor=P.edge(tok(token)), lw=0.7, zorder=zorder + (k - i) * 0.01))
    return out


def centriole_section(ax, center, r=0.8, kind="triplet", cartwheel=True, tilt=40.0, zorder=10):
    """A centriole or basal body in cross-section: nine microtubule triplets (A innermost) arranged like a
    pinwheel around a cartwheel hub (SAS-6 ring) with nine spokes. ``kind`` "doublet" draws a transition-zone
    style ring of doublets. Returns the list of A-tubule centres."""
    c = np.asarray(center, float)
    k = 3 if kind == "triplet" else 2 if kind == "doublet" else 1
    tr = r * 0.11
    As = []
    for i in range(9):
        th = math.pi / 2 - 2 * math.pi * i / 9
        radial = np.array([math.cos(th), math.sin(th)])
        tang = np.array([math.sin(th), -math.cos(th)])
        mid = c + radial * r * 0.82
        ang = math.radians(tilt)
        d = radial * math.cos(ang) + tang * math.sin(ang)  # from A (inner) outward-clockwise
        start = mid - d * tr * 1.55 * (k - 1) / 2
        pts = _triplet(ax, start + d * tr * 1.55 * (k - 1) / 2, tr, math.degrees(math.atan2(d[1], d[0])), k=k,
                       zorder=zorder)
        As.append(pts[0])
    if cartwheel:
        hub = r * 0.17
        ax.add_patch(Circle(c, hub, facecolor=P.light(tok("pcm")), edgecolor=P.edge(tok("pcm")), lw=0.7, zorder=zorder - 0.5))
        for p in As:
            d = (p - c) / np.linalg.norm(p - c)
            q0, q1 = c + d * hub, p - d * tr
            ax.plot([q0[0], q1[0]], [q0[1], q1[1]], color=P.edge(tok("pcm")), lw=0.8, zorder=zorder - 0.6)
    return As


def centriole(ax, center, length=1.2, width=0.5, angle=90.0, token="centriole", zorder=10):
    """A centriole seen from the side: a short barrel with microtubule blades (stripes). ``angle`` is its axis."""
    c = np.asarray(center, float)
    th = math.radians(angle)
    u = np.array([math.cos(th), math.sin(th)])
    n = np.array([-u[1], u[0]])
    a, b = c - u * length / 2, c + u * length / 2
    quad = [a + n * width / 2, b + n * width / 2, b - n * width / 2, a - n * width / 2]
    ax.add_patch(Polygon(quad, closed=True, facecolor=P.light(tok(token)), edgecolor=P.edge(tok(token)), lw=0.8,
                         joinstyle="round", zorder=zorder))
    for s in np.linspace(-0.36, 0.36, 5):
        p, q = a + n * width * s, b + n * width * s
        ax.plot([p[0], q[0]], [p[1], q[1]], color=P.fill(tok(token)), lw=1.3, solid_capstyle="butt", zorder=zorder + 0.1)
    return {"proximal": a, "distal": b}


def centrosome(ax, center, size=0.7, microtubules=12, length=3.0, seed=2, pcm=True, centrioles=True,
               angles=None, lw=1.3, line=True, zorder=9):
    """A centrosome: a pair of orthogonal centrioles (one side view, one cross-section) in a cloud of
    pericentriolar material, with ``microtubules`` growing outward (minus ends in the PCM).

    ``angles`` limits the directions (degrees, list or (start, stop)); ``line=False`` draws tubes.
    Returns dict(center, plus_ends).
    """
    c = np.asarray(center, float)
    rng = np.random.default_rng(seed)
    if pcm:
        o = blob(c, size, size * 0.9, wobble=0.12, seed=seed + 5, k=10)
        ax.add_patch(PathPatch(Path(o, closed=True), facecolor=P.light(tok("pcm")), edgecolor=P.edge(tok("pcm")),
                               lw=0.7, zorder=zorder))
        for _ in range(int(14 * size)):
            a_, d_ = rng.uniform(0, 2 * math.pi), size * 0.8 * math.sqrt(rng.uniform(0.1, 1))
            p = c + d_ * np.array([math.cos(a_), math.sin(a_)])
            ax.add_patch(Circle(p, size * 0.05, facecolor=P.fill(tok("gamma")), edgecolor="none", zorder=zorder + 0.2))
    if centrioles:
        centriole(ax, c + np.array([-size * 0.15, 0.0]), length=size * 0.85, width=size * 0.36, angle=90,
                  zorder=zorder + 1)
        centriole_section(ax, c + np.array([size * 0.38, -size * 0.05]), r=size * 0.2, cartwheel=False, zorder=zorder + 1)
    if angles is None:
        angs = np.linspace(0, 360, microtubules, endpoint=False) + rng.uniform(-10, 10, microtubules)
    elif len(angles) == 2 and not isinstance(angles[0], (list, tuple)):
        angs = np.linspace(angles[0], angles[1], microtubules)
    else:
        angs = np.asarray(angles, float)
    plus = []
    for k, an in enumerate(angs):
        d = np.array([math.cos(math.radians(an)), math.sin(math.radians(an))])
        Lk = length * rng.uniform(0.65, 1.0)
        s = c + d * size * 0.75
        e = c + d * (size + Lk)
        if line:
            mt_line(ax, s, e, lw=lw, plus=True, zorder=zorder - 1)
        else:
            tube(ax, s, e, width=lw * 0.12, plus="dot", zorder=zorder - 1)
        plus.append(e)
    return {"center": c, "plus_ends": plus}


# ---------------------------------------------------------------------------------------------
# motors


def _head(ax, center, size, token, angle=0.0, seed=0, zorder=13):
    o = blob(center, size * 0.55, size * 0.42, wobble=0.07, seed=seed + 31, k=7, angle=math.radians(angle))
    ax.add_patch(PathPatch(Path(o, closed=True), facecolor=P.fill(tok(token)), edgecolor=P.edge(tok(token)), lw=LINE * 0.85,
                           zorder=zorder))
    hl = blob((center[0] - size * 0.12, center[1] + size * 0.1), size * 0.2, size * 0.12, wobble=0.04, seed=seed + 7, k=6)
    ax.add_patch(PathPatch(Path(hl, closed=True), facecolor=P.light(tok(token)), edgecolor="none", zorder=zorder + 0.5))


def _coil(ax, a, b, token, width=0.1, lw=LINE * 1.1, zorder=12):
    a, b, L, u, n = _frame(a, b)
    k = max(2, int(L / 0.4))
    s = np.linspace(0, 1, 140)
    for ph, tone in ((0.0, P.edge(tok(token))), (math.pi, P.mix(P.edge(tok(token)), P.fill(tok(token)), 0.5))):
        off = np.sin(2 * math.pi * k * s + ph) * width / 2
        pts = a + np.outer(s * L, u) + np.outer(off, n)
        ax.plot(pts[:, 0], pts[:, 1], color=tone, lw=lw, solid_capstyle="round", zorder=zorder + (0.2 if ph else 0))


def myosin_head(ax, attach, size=0.6, lever=60.0, bound=True, gap=0.0, token="myosin", light_chains=2, lever_len=None,
                nucleotide=None, zorder=13):
    """One myosin head (motor domain) on an actin filament below it, with its lever arm.

    ``attach`` is the binding site on the filament; the head sits above it (lifted by ``gap`` when detached);
    ``lever`` is the lever-arm angle from the filament axis (degrees; about 90 pre-stroke, 45 post-stroke
    for a filament whose plus end points right). ``nucleotide`` writes "ATP", "ADP·Pi" or "ADP" on the
    head. Returns the end of the lever arm (where the tail continues)."""
    p = np.asarray(attach, float)
    hc = p + np.array([0, size * 0.42 + gap])
    _head(ax, hc, size, token, angle=0.0, seed=3, zorder=zorder)
    ll = lever_len or size * 1.6
    th = math.radians(180 - lever)
    d = np.array([math.cos(th), math.sin(th)])
    base = hc + np.array([0, size * 0.3])
    end = base + d * ll
    ax.plot([base[0], end[0]], [base[1], end[1]], color=P.edge(tok(token)), lw=LINE * 2.2, solid_capstyle="round",
            zorder=zorder - 0.5)
    for k in range(light_chains):
        q = base + d * ll * (0.35 + 0.4 * k / max(1, light_chains - 1 or 1))
        ax.add_patch(Ellipse(q, size * 0.3, size * 0.2, angle=math.degrees(th), facecolor=P.fill("metabolite"),
                             edgecolor=P.edge("metabolite"), lw=0.5, zorder=zorder - 0.3))
    if nucleotide:
        label(ax, hc + np.array([size * 0.05, -size * 0.02]), nucleotide, size="tiny", color=P.on_fill(), zorder=zorder + 1)
    return end


def myosin_v(ax, rear, front, cargo, head=0.45, token="myosin", zorder=13):
    """Myosin V on actin: two heads bound ``front - rear`` apart (36 nm in reality), long lever arms with six
    light chains each meeting at the neck, and a coiled-coil tail to ``cargo``. Returns the neck point."""
    r, f = np.asarray(rear, float), np.asarray(front, float)
    for h, s in ((r, 1), (f, 2)):
        _head(ax, h + np.array([0, head * 0.35]), head, token, seed=s, zorder=zorder)
    neck = (r + f) / 2 + np.array([0, np.linalg.norm(f - r) * 0.62])
    for h in (r, f):
        base = h + np.array([0, head * 0.6])
        ax.plot([base[0], neck[0]], [base[1], neck[1]], color=P.edge(tok(token)), lw=LINE * 1.8, solid_capstyle="round",
                zorder=zorder - 0.6)
        for k in range(6):
            q = base + (neck - base) * (0.12 + 0.8 * k / 5)
            ax.add_patch(Circle(q, head * 0.13, facecolor=P.fill("metabolite"), edgecolor=P.edge("metabolite"), lw=0.4,
                                zorder=zorder - 0.4))
    _coil(ax, neck, cargo, token, zorder=zorder - 1)
    return neck


def dynein(ax, track_point, cargo, size=0.6, dynactin=True, adaptor=True, two_heads=True, token="dynein", zorder=13):
    """Cytoplasmic dynein-1 bound to a microtubule at ``track_point`` (below the motor), with its tail to
    ``cargo`` (above). Each head is a ring of six AAA+ domains with a coiled-coil stalk ending in the
    microtubule-binding domain and a linker across the ring; dynactin (Arp1 rod) and an activating adaptor
    (coiled coil, e.g. BICD2) join the tails. Returns dict(heads, tail_top)."""
    t = np.asarray(track_point, float)
    cg = np.asarray(cargo, float)
    heads = []
    offs = (-size * 0.65, size * 0.65) if two_heads else (0.0,)
    for k, dx in enumerate(offs):
        mtbd = t + np.array([dx * 0.35, 0])
        ring = t + np.array([dx, size * 1.7])
        ax.plot([mtbd[0], ring[0] - dx * 0.2], [mtbd[1], ring[1] - size * 0.45], color=P.edge(tok(token)), lw=LINE * 1.0,
                zorder=zorder - 1)
        ax.add_patch(Circle(mtbd, size * 0.1, facecolor=P.fill(tok(token)), edgecolor=P.edge(tok(token)), lw=0.5,
                            zorder=zorder))
        for i in range(6):
            th = 2 * math.pi * i / 6 + 0.3
            q = ring + size * 0.32 * np.array([math.cos(th), math.sin(th)])
            ax.add_patch(Circle(q, size * 0.17, facecolor=P.fill(tok(token)) if i % 2 else P.light(tok(token)),
                                edgecolor=P.edge(tok(token)), lw=0.55, zorder=zorder + 0.1 * i))
        ax.plot([ring[0] - size * 0.35, ring[0] + size * 0.3], [ring[1] + size * 0.25, ring[1] + size * 0.05],
                color=P.edge(tok(token)), lw=LINE * 1.6, solid_capstyle="round", zorder=zorder + 1)
        heads.append(ring)
    neck = (heads[0] + heads[-1]) / 2 + np.array([0, size * 0.8])
    for h in heads:
        ax.plot([h[0], neck[0]], [h[1] + size * 0.35, neck[1]], color=P.edge(tok(token)), lw=LINE * 1.3, zorder=zorder - 0.5)
    ax.plot([neck[0], cg[0]], [neck[1], cg[1]], color=P.edge(tok(token)), lw=LINE * 1.5, solid_capstyle="round",
            zorder=zorder - 0.5)
    if dynactin:
        d0 = neck + np.array([size * 0.55, size * 0.1])
        d1 = d0 + (cg - neck) * 0.75 + np.array([size * 0.2, 0])
        a, b, L, u, n = _frame(d0, d1)
        for i in range(int(L / (size * 0.18)) + 1):
            q = a + u * i * size * 0.18
            ax.add_patch(Circle(q, size * 0.1, facecolor=P.fill(tok("dynactin")), edgecolor=P.edge(tok("dynactin")),
                                lw=0.4, zorder=zorder - 0.3))
    if adaptor:
        _coil(ax, neck + np.array([-size * 0.25, size * 0.1]), cg + np.array([-size * 0.2, 0]), tok("adaptor"),
              width=0.08, lw=LINE * 0.9, zorder=zorder - 0.2)
    return {"heads": heads, "tail_top": cg}


# ---------------------------------------------------------------------------------------------
# intermediate filaments


def _if_monomer(ax, a, b, w=0.12, token="if", head=True, tail=True, zorder=10):
    """One IF protein: a central alpha-helical rod (stripes) with globular head (N, at a) and tail (C, at b)."""
    a, b, L, u, n = _frame(a, b)
    quad = [a + n * w / 2, b + n * w / 2, b - n * w / 2, a - n * w / 2]
    ax.add_patch(Polygon(quad, closed=True, facecolor=P.fill(tok(token)), edgecolor=P.edge(tok(token)), lw=0.5,
                         joinstyle="round", zorder=zorder))
    if head:
        ax.add_patch(Circle(a - u * w * 0.6, w * 0.75, facecolor=P.light(tok(token)), edgecolor=P.edge(tok(token)), lw=0.5,
                            zorder=zorder + 0.1))
    if tail:
        ax.add_patch(Circle(b + u * w * 0.7, w * 0.85, facecolor=P.light(tok(token)), edgecolor=P.edge(tok(token)), lw=0.5,
                            zorder=zorder + 0.1))


def if_assembly(ax, origin, stage="monomer", length=2.4, w=0.12, token="if", zorder=10):
    """One stage of intermediate-filament assembly, drawn from ``origin`` (left end) to the right:
    "monomer" (head-rod-tail), "dimer" (parallel coiled coil), "tetramer" (two dimers antiparallel and
    staggered: no polarity), "ulf" (unit-length filament, eight tetramers side by side), "filament"
    (ULFs annealed end to end and compacted). Returns the (x0, y0, x1, y1) extent."""
    o = np.asarray(origin, float)
    u, n = np.array([1.0, 0]), np.array([0, 1.0])
    if stage == "monomer":
        _if_monomer(ax, o, o + u * length, w, token, zorder=zorder)
        return (o[0] - w, o[1] - w, o[0] + length + w, o[1] + w)
    if stage == "dimer":
        _coil(ax, o, o + u * length, tok(token), width=w * 1.6, lw=LINE * 1.6, zorder=zorder)
        for p, r in ((o - u * w * 0.6, 0.75), (o + u * (length + w * 0.7), 0.85)):
            for s in (1, -1):
                ax.add_patch(Circle(p + n * s * w * 0.6, w * r, facecolor=P.light(tok(token)), edgecolor=P.edge(tok(token)),
                                    lw=0.5, zorder=zorder + 0.1))
        return (o[0] - w, o[1] - w * 2, o[0] + length + w, o[1] + w * 2)
    if stage == "tetramer":
        sh = length * 0.45
        if_assembly(ax, o + n * w * 1.4, "dimer", length, w, token, zorder)
        # antiparallel partner: drawn with its N-terminus on the right
        p0 = o - n * w * 1.4 + u * sh
        _coil(ax, p0, p0 + u * length, tok(token), width=w * 1.6, lw=LINE * 1.6, zorder=zorder)
        for p, r in ((p0 + u * (length + w * 0.6), 0.75), (p0 - u * w * 0.7, 0.85)):
            for s in (1, -1):
                ax.add_patch(Circle(p + n * s * w * 0.6, w * r, facecolor=P.light(tok(token)), edgecolor=P.edge(tok(token)),
                                    lw=0.5, zorder=zorder + 0.1))
        return (o[0] - w, o[1] - w * 3.5, o[0] + sh + length + w, o[1] + w * 3.5)
    if stage == "ulf":
        L2 = length * 0.6
        for k in range(8):
            y = (k - 3.5) * w * 1.25
            sh = (k % 2) * L2 * 0.45
            p = o + n * y + u * sh
            ax.plot([p[0], p[0] + L2], [p[1], p[1]], color=P.edge(tok(token)), lw=w * 72 * 0.45, solid_capstyle="round",
                    zorder=zorder)
            ax.plot([p[0], p[0] + L2], [p[1], p[1]], color=P.fill(tok(token)), lw=w * 72 * 0.28, solid_capstyle="round",
                    zorder=zorder + 0.1)
        return (o[0], o[1] - w * 5, o[0] + L2 * 1.45, o[1] + w * 5)
    if stage == "filament":
        if_filament(ax, o, o + u * length, width=w * 4.0, token=token, zorder=zorder)
        return (o[0], o[1] - w * 2, o[0] + length, o[1] + w * 2)
    raise ValueError(f"unknown stage {stage!r}")


def if_filament(ax, a, b, width=0.3, strands=4, token="if", zorder=9):
    """A 10 nm intermediate filament drawn as a rope of twisted strands (nonpolar: no end marks)."""
    a, b, L, u, n = _frame(a, b)
    s = np.linspace(0, 1, max(60, int(L * 40)))
    turns = L / (width * 2.2)
    edge, fill = P.edge(tok(token)), P.fill(tok(token))
    for k in range(strands):
        ph = 2 * math.pi * k / strands
        off = np.sin(2 * math.pi * turns * s + ph) * width * 0.38
        pts = a + np.outer(s * L, u) + np.outer(off, n)
        ax.plot(pts[:, 0], pts[:, 1], color=edge, lw=width * 72 * 0.2 + 0.8, solid_capstyle="round", zorder=zorder + k * 0.01)
        ax.plot(pts[:, 0], pts[:, 1], color=fill, lw=width * 72 * 0.12, solid_capstyle="round", zorder=zorder + k * 0.01 + 0.005)
    return {"a": a, "b": b}


# ---------------------------------------------------------------------------------------------
# cilia


def doublet(ax, center, r=0.25, angle=0.0, token="tubulin", zorder=10):
    """An outer doublet of the axoneme in cross-section: a complete A tubule and an incomplete B tubule
    attached to it, B lying in direction ``angle`` (degrees) from A. Returns dict(A, B)."""
    c = np.asarray(center, float)
    th = math.radians(angle)
    d = np.array([math.cos(th), math.sin(th)])
    A = c - d * r * 0.5
    B = c + d * r * 0.62
    rb = r * 1.08
    # B tubule: an arc that closes on the A tubule wall
    t = np.linspace(th - math.radians(140), th + math.radians(140), 40)
    arc = np.c_[B[0] + rb * np.cos(t), B[1] + rb * np.sin(t)]
    ax.plot(arc[:, 0], arc[:, 1], color=P.edge(tok(token)), lw=r * 72 * 0.24 + 0.8, solid_capstyle="round", zorder=zorder)
    ax.plot(arc[:, 0], arc[:, 1], color=P.light(tok(token)), lw=r * 72 * 0.13, solid_capstyle="round", zorder=zorder + 0.05)
    ax.add_patch(Circle(A, r, facecolor=P.light(tok(token)), edgecolor=P.edge(tok(token)), lw=r * 72 * 0.24 + 0.8,
                        zorder=zorder + 0.1))
    ax.add_patch(Circle(A, r * 0.6, facecolor=P.surface(), edgecolor="none", zorder=zorder + 0.15))
    ax.add_patch(Circle(B, rb * 0.62, facecolor=P.surface(), edgecolor="none", zorder=zorder + 0.06))
    return {"A": A, "B": B}


def axoneme(ax, center, R=2.0, kind="9+2", arms=True, spokes=True, nexin=True, membrane=True, labels=False,
            arm_token="dynein", zorder=9):
    """An axoneme in cross-section, viewed from the base towards the tip: nine outer doublets around a
    central pair (``kind`` "9+2") or none ("9+0", primary or nodal cilium). Outer and inner dynein arms on
    each A tubule point clockwise towards the B tubule of the neighbouring doublet; radial spokes run
    inward to the central sheath; nexin links join neighbours. Returns a dict of anchor points:
    doublets (list of dicts), outer_arm, inner_arm, spoke, central_pair, nexin, membrane."""
    c = np.asarray(center, float)
    r = R * 0.13
    out = {"doublets": []}
    if membrane:
        ax.add_patch(Circle(c, R * 1.3, facecolor=P.fill("cytoplasm"), edgecolor=P.edge(tok("membrane")), lw=2.4,
                            zorder=zorder - 2))
    pos = []
    for i in range(9):
        th = math.pi / 2 - 2 * math.pi * i / 9
        p = c + R * np.array([math.cos(th), math.sin(th)])
        tang = np.array([math.sin(th), -math.cos(th)])  # clockwise direction
        pos.append((p, th, tang))
    for i, (p, th, tang) in enumerate(pos):
        # B tubule outward-clockwise of A
        radial = np.array([math.cos(th), math.sin(th)])
        dvec = tang * 0.55 + radial * 0.75
        ang = math.degrees(math.atan2(dvec[1], dvec[0]))
        d = doublet(ax, p, r, angle=ang, zorder=zorder)
        out["doublets"].append(d)
    for i, (p, th, tang) in enumerate(pos):
        A = out["doublets"][i]["A"]
        radial = np.array([math.cos(th), math.sin(th)])
        nxt = out["doublets"][(i + 1) % 9]
        if arms:
            for kind_, rad, tk in (("outer", 0.55, 1.0), ("inner", -0.25, 0.85)):
                base = A - tang * r * 0.6 + radial * r * rad
                tip = base - tang * r * 1.9 * tk + radial * r * 0.35 * (1 if kind_ == "outer" else -1)
                hook = tip - radial * r * 0.55 * (1 if kind_ == "outer" else -1)
                pts = np.array([base, tip, hook])
                ax.plot(pts[:, 0], pts[:, 1], color=P.edge(tok(arm_token)), lw=r * 72 * 0.28 + 0.6, solid_capstyle="round",
                        solid_joinstyle="round", zorder=zorder + 0.5)
                ax.plot(pts[:, 0], pts[:, 1], color=P.fill(tok(arm_token)), lw=r * 72 * 0.16, solid_capstyle="round",
                        solid_joinstyle="round", zorder=zorder + 0.55)
                if i == 0:
                    out[kind_ + "_arm"] = tip
        if nexin:
            q0 = A - radial * r * 0.7
            q1 = nxt["A"] - radial * r * 0.7
            mid = (q0 + q1) / 2 - radial * r * 0.25
            pts = np.array([q0, mid, q1])
            ax.plot(pts[:, 0], pts[:, 1], color=P.edge(tok("nexin")), lw=0.9, zorder=zorder - 0.5)
            if i == 0:
                out["nexin"] = mid
        if spokes and kind == "9+2":
            s0 = A - radial * r * 1.0
            s1 = c + radial * R * 0.42
            ax.plot([s0[0], s1[0]], [s0[1], s1[1]], color=P.edge(tok("spoke")), lw=1.4, zorder=zorder - 0.5)
            ax.add_patch(Ellipse(s1, r * 0.9, r * 0.5, angle=math.degrees(th) + 90, facecolor=P.fill(tok("spoke")),
                                 edgecolor=P.edge(tok("spoke")), lw=0.5, zorder=zorder - 0.4))
            if i == 0:
                out["spoke"] = (s0 + s1) / 2
    if kind == "9+2":
        ax.add_patch(Circle(c, R * 0.34, facecolor="none", edgecolor=P.muted(), lw=0.8, ls=(0, (2, 1.5)), zorder=zorder - 0.6))
        for s in (-1, 1):
            q = c + np.array([s * r * 1.15, 0])
            ax.add_patch(Circle(q, r, facecolor=P.light(tok("tubulin")), edgecolor=P.edge(tok("tubulin")),
                                lw=r * 72 * 0.24 + 0.8, zorder=zorder))
            ax.add_patch(Circle(q, r * 0.6, facecolor=P.surface(), edgecolor="none", zorder=zorder + 0.1))
        ax.plot([c[0] - r * 0.2, c[0] + r * 0.2], [c[1], c[1]], color=P.edge(tok("tubulin")), lw=1.2, zorder=zorder + 0.2)
        out["central_pair"] = c
    out["membrane"] = c + np.array([0, R * 1.3])
    if labels:
        label(ax, c + np.array([0, -R * 1.55]), kind, size="small")
    return out


# ---------------------------------------------------------------------------------------------
# spindle elements


def kinetochore(ax, center, angle=0.0, size=0.35, fibrils=3, token="kinetochore", zorder=12):
    """A kinetochore on a centromere: an outer plate facing direction ``angle`` (degrees) with Ndc80 fibrils
    that bind microtubule ends. Returns the attachment point (just outside the plate)."""
    c = np.asarray(center, float)
    th = math.radians(angle)
    u = np.array([math.cos(th), math.sin(th)])
    n = np.array([-u[1], u[0]])
    ax.add_patch(Ellipse(c, size * 0.32, size, angle=math.degrees(th), facecolor=P.fill(tok(token)),
                         edgecolor=P.edge(tok(token)), lw=0.7, zorder=zorder))
    for k in range(fibrils):
        s = (k - (fibrils - 1) / 2) / max(1, fibrils - 1) * size * 0.6
        p0 = c + n * s + u * size * 0.14
        p1 = p0 + u * size * 0.38
        ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=P.edge(tok(token)), lw=0.9, zorder=zorder - 0.1)
    return c + u * size * 0.5


def chromatid_pair(ax, center, length=1.2, width=0.22, angle=90.0, kinetochores=True, token="chromosome",
                   facing=0.0, zorder=11):
    """A replicated (mitotic) chromosome: two sister chromatids joined at the centromere, axis along
    ``angle`` (degrees). Kinetochores face ``facing`` and ``facing + 180`` degrees. Returns dict(kinetochores,
    attach) with the two attachment points."""
    c = np.asarray(center, float)
    th = math.radians(angle)
    u = np.array([math.cos(th), math.sin(th)])
    n = np.array([-u[1], u[0]])
    for s in (1, -1):
        # each chromatid bends slightly at the centromere
        pts = [c - u * length / 2 + n * s * width * 0.95, c + n * s * width * 0.55, c + u * length / 2 + n * s * width * 0.95]
        pts = np.array(pts)
        ax.plot(pts[:, 0], pts[:, 1], color=P.edge(tok(token)), lw=width * 72 * 0.9 + 1.1, solid_capstyle="round",
                solid_joinstyle="round", zorder=zorder)
        ax.plot(pts[:, 0], pts[:, 1], color=P.fill(tok(token)), lw=width * 72 * 0.9 - 0.6, solid_capstyle="round",
                solid_joinstyle="round", zorder=zorder + 0.05)
    out = {"kinetochores": [], "attach": []}
    if kinetochores:
        for f in (facing, facing + 180.0):
            d = np.array([math.cos(math.radians(f)), math.sin(math.radians(f))])
            kc = c + d * width * 1.05
            out["kinetochores"].append(kc)
            out["attach"].append(kinetochore(ax, kc, angle=f, size=width * 1.6, zorder=zorder + 0.5))
    return out


def spindle(ax, center, half_length=3.0, height=2.2, chromosomes=3, astral=5, interpolar=2, kmts=2, angle=0.0,
            chrom_length=0.9, lw=1.3, centrosomes=True, stage="metaphase", zorder=9):
    """A bipolar mitotic spindle with poles at +-``half_length`` along ``angle``: kinetochore microtubules
    from each pole to the sister kinetochores of ``chromosomes`` aligned on the metaphase plate,
    interpolar microtubules that overlap antiparallel at the equator, and astral microtubules radiating
    away from the plate. ``stage="anaphase"`` separates the sisters halfway towards the poles.

    Returns dict(poles, kinetochores, kmt, interpolar, astral, overlap, chromosomes) with points or
    segments for callouts."""
    c = np.asarray(center, float)
    th = math.radians(angle)
    u = np.array([math.cos(th), math.sin(th)])
    n = np.array([-u[1], u[0]])
    poles = [c - u * half_length, c + u * half_length]
    out = {"poles": poles, "kinetochores": [], "kmt": [], "interpolar": [], "astral": [], "chromosomes": []}
    ys = [(k - (chromosomes - 1) / 2) * height / max(1, chromosomes) for k in range(chromosomes)]
    for y in ys:
        cc = c + n * y
        if stage == "anaphase":
            for s in (-1, 1):
                q = cc + u * s * half_length * 0.45
                # a single chromatid dragged by its kinetochore (arms trailing)
                pts = np.array([q - u * s * chrom_length * 0.3 + n * chrom_length * 0.4, q, q - u * s * chrom_length * 0.3 - n * chrom_length * 0.4])
                ax.plot(pts[:, 0], pts[:, 1], color=P.edge(tok("chromosome")), lw=lw * 6.5, solid_capstyle="round",
                        solid_joinstyle="round", zorder=zorder + 2)
                ax.plot(pts[:, 0], pts[:, 1], color=P.fill(tok("chromosome")), lw=lw * 5.0, solid_capstyle="round",
                        solid_joinstyle="round", zorder=zorder + 2.05)
                at = kinetochore(ax, q, angle=math.degrees(th) + (0 if s > 0 else 180), size=0.3, zorder=zorder + 2.5)
                out["kinetochores"].append(at)
                pole = poles[1] if s > 0 else poles[0]
                for k in range(kmts):
                    off = n * (k - (kmts - 1) / 2) * 0.08
                    mt_line(ax, pole, at + off, lw=lw, zorder=zorder)
                    out["kmt"].append((pole, at + off))
            out["chromosomes"].append(cc)
            continue
        cp = chromatid_pair(ax, cc, length=chrom_length, width=0.15, angle=math.degrees(th) + 90, facing=math.degrees(th),
                            zorder=zorder + 2)
        out["chromosomes"].append(cc)
        for at, pole in zip(cp["attach"], (poles[1], poles[0])):
            out["kinetochores"].append(at)
            for k in range(kmts):
                off = n * (k - (kmts - 1) / 2) * 0.08
                mt_line(ax, pole, at + off, lw=lw, zorder=zorder)
                out["kmt"].append((pole, at + off))
    # interpolar microtubules: from each pole past the equator
    for k in range(interpolar):
        y = (k - (interpolar - 1) / 2) * height * 0.9 / max(1, interpolar) + height * 0.5 / max(1, chromosomes)
        for s, pole in ((1, poles[0]), (-1, poles[1])):
            end = c + n * (y + s * 0.07) + u * s * half_length * 0.25
            bow = (pole + end) / 2 + n * y * 0.35
            pts = np.array([pole, bow, end])
            t = np.linspace(0, 1, 30)[:, None]
            curve = (1 - t) ** 2 * pts[0] + 2 * (1 - t) * t * pts[1] + t**2 * pts[2]
            ax.plot(curve[:, 0], curve[:, 1], color=P.edge(tok("tubulin")), lw=lw, solid_capstyle="round", zorder=zorder - 0.2)
            out["interpolar"].append(end)
    out["overlap"] = c + n * ((0 - (interpolar - 1) / 2) * height * 0.9 / max(1, interpolar) + height * 0.5 / max(1, chromosomes))
    # astral microtubules
    for s, pole in ((-1, poles[0]), (1, poles[1])):
        for k in range(astral):
            a_ = (k - (astral - 1) / 2) / max(1, astral - 1) * math.radians(110)
            d = u * s * math.cos(a_) + n * math.sin(a_)
            e = pole + d * half_length * 0.55
            mt_line(ax, pole, e, lw=lw, plus=True, zorder=zorder - 0.3)
            out["astral"].append(e)
    if centrosomes:
        for pole in poles:
            o = blob(pole, 0.28, 0.26, wobble=0.1, seed=7, k=8)
            ax.add_patch(PathPatch(Path(o, closed=True), facecolor=P.light(tok("pcm")), edgecolor=P.edge(tok("pcm")),
                                   lw=0.7, zorder=zorder + 1))
            centriole(ax, pole, length=0.22, width=0.1, angle=math.degrees(th) + 90, zorder=zorder + 1.2)
            centriole(ax, pole + n * 0.12 + u * 0.05, length=0.2, width=0.09, angle=math.degrees(th), zorder=zorder + 1.3)
    return out


# ---------------------------------------------------------------------------------------------
# legends


def nucleotide_legend(ax, at, kind="actin", size=0.28, step=1.9, labels=None):
    """A row of three swatches for the nucleotide states of actin (ATP, ADP-Pi, ADP) or beta-tubulin (GTP, GDP-Pi,
    GDP), starting at ``at``."""
    x, y = at
    names = labels or ({"actin": ("ATP", "ADP·Pi", "ADP"), "tubulin": ("GTP", "GDP·Pi", "GDP")}[kind])
    for k, (st, name) in enumerate(zip("TPD", names)):
        p = (x + k * step, y)
        ax.add_patch(Ellipse(p, size * 1.2, size, facecolor=state_color(kind, st), edgecolor=P.edge(tok(kind)), lw=0.6,
                             zorder=20))
        label(ax, (p[0] + size * 0.9, y), name, size="tiny", ha="left")
