"""Biochemistry figures: enzyme kinetics, metabolic pathway maps, protein topology diagrams.

Kinetics
    rate(S, vmax, km, i=0, ki=inf, kiu=inf)    Michaelis-Menten rate with competitive (ki) and
                                               uncompetitive (kiu) inhibition terms; both = mixed
    apparent(vmax, km, i, ki, kiu)              (Vmax_app, Km_app) of that rate law

Pathway maps (metabolites as soft pills, reactions as SBGN process arrows)
    pw = metabolism.Pathway(ax)
    pw.node("glc", (3, 9), "Glucose")
    pw.node("g6p", (3, 7.5), "Glucose 6-phosphate")
    pw.step("glc", "g6p", enzyme="Hexokinase", side=("ATP", "ADP"))
    pw.step("g6p", "f6p", reversible=True)
    pw.step(a, b, bend=0.3)                     curved (cycles): see ``ring`` and ``cycle_bend``
Side species (``side``) form one arc on the arrow: the first joins, the second leaves; ``None``
omits one half (``side=(None, "CO₂")`` for a release). ``flip=True`` puts the arc on the other side.

Protein topology (secondary structure: strands yellow arrows, helices pink cylinders)
    strand(ax, a, b) / helix(ax, a, b)          elements from N-terminal end a to C-terminal end b
    loop(ax, points)                            a smooth connecting loop through points
    tops_strand(ax, xy, up=True) / tops_helix   TOPS symbols (triangles and circles, top views)
    ss_track(ax, x, y, segments, length)        a linear secondary-structure map along the sequence
"""

import math

import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Polygon

from . import palette as P
from .core import FONT, LINE, arrow, label

INF = float("inf")


# ---------------------------------------------------------------------------------------------
# kinetics


def rate(S, vmax, km, i=0.0, ki=INF, kiu=INF):
    """Initial rate v = Vmax [S] / (Km (1 + [I]/Ki) + [S] (1 + [I]/Ki')).

    ``ki`` is the dissociation constant of EI (competitive term), ``kiu`` of ESI (uncompetitive
    term); finite values for both give mixed inhibition, equal values pure noncompetitive.
    """
    S = np.asarray(S, float)
    a = 1 + i / ki
    b = 1 + i / kiu
    return vmax * S / (km * a + S * b)


def apparent(vmax, km, i=0.0, ki=INF, kiu=INF):
    """Apparent (Vmax, Km) of ``rate`` at inhibitor concentration i."""
    a, b = 1 + i / ki, 1 + i / kiu
    return vmax / b, km * a / b


# ---------------------------------------------------------------------------------------------
# pathway maps


def _text_size(ax, text, size, italic=False, bold=False):
    from .network import text_extent

    return text_extent(ax, text, size, italic=italic, bold=bold)


class Pathway:
    """A metabolic map on a ``bio.canvas`` axes: metabolite nodes and reaction steps between them."""

    def __init__(self, ax, size="small", gap=0.1, enzyme_color=None):
        self.ax = ax
        self.size = size
        self.gap = gap
        self.nodes = {}
        self.enzyme_color = enzyme_color

    def node(self, id, at, text, token="metabolite", w=None, h=None, size=None, bold=False, zorder=12):
        """A metabolite: text in a soft rounded pill (the box fits the text). Returns its bbox."""
        size = size or self.size
        tw, th = _text_size(self.ax, text, size, bold=bold)
        from .network import units_per_point

        h = h or FONT.get(size, size) * 2.1 * units_per_point(self.ax)
        w = w or tw + h * 0.9
        x, y = at
        self.ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle=f"round,pad=0,rounding_size={h / 2}",
                                         facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE * 0.75, zorder=zorder))
        label(self.ax, at, text, size=size, color=P.on_fill(), bold=bold, zorder=zorder + 1)
        self.nodes[id] = (np.array(at, float), w, h)
        return (x - w / 2, y - h / 2, x + w / 2, y + h / 2)

    def anchor(self, id, side):
        """A point on a node's border: "t", "b", "l", "r"."""
        c, w, h = self.nodes[id]
        return c + {"t": (0, h / 2), "b": (0, -h / 2), "l": (-w / 2, 0), "r": (w / 2, 0)}[side]

    def _inside(self, id, p, pad):
        c, w, h = self.nodes[id]
        return abs(p[0] - c[0]) <= w / 2 + pad and abs(p[1] - c[1]) <= h / 2 + pad

    def step(self, a, b, enzyme=None, side=None, reversible=False, bend=0.0, flip=False, enzyme_flip=False,
             side_reach=0.55, side_span=0.7, side_size="tiny", enzyme_size="tiny", enzyme_offset=0.14, start=None, end=None,
             color=None, dashed=False):
        """A reaction arrow from node a to node b (ids, or explicit points ``start``/``end``).

        ``side=("ATP", "ADP")`` adds a co-substrate arc; ``enzyme`` is written on the other side.
        ``reversible`` draws heads at both ends. Returns (midpoint, unit tangent, unit left normal).
        """
        p0 = np.asarray(start if start is not None else self.nodes[a][0], float)
        p2 = np.asarray(end if end is not None else self.nodes[b][0], float)
        d = p2 - p0
        n = np.array([-d[1], d[0]])
        p1 = (p0 + p2) / 2 + bend * n
        t = np.linspace(0, 1, 400)

        def at(tt):
            return (1 - tt) ** 2 * p0 + 2 * (1 - tt) * tt * p1 + tt**2 * p2

        pts = at(t[:, None])
        t0 = 0.0
        if start is None:
            out = [k for k in range(len(t)) if not self._inside(a, pts[k], self.gap)]
            t0 = t[out[0]] if out else 0.0
        t1 = 1.0
        if end is None:
            out = [k for k in range(len(t)) if not self._inside(b, pts[k], self.gap)]
            t1 = t[out[-1]] if out else 1.0
        q0, q2 = at(t0), at(t1)
        q1 = (1 - t0) * (1 - t1) * p0 + ((1 - t0) * t1 + t0 * (1 - t1)) * p1 + t0 * t1 * p2
        dd = q2 - q0
        nn = np.array([-dd[1], dd[0]])
        sub_bend = float(np.dot(q1 - (q0 + q2) / 2, nn) / (np.dot(nn, nn) or 1))
        c = color or P.ink()
        mid = 0.25 * q0 + 0.5 * q1 + 0.25 * q2
        if reversible:
            # two halves from the midpoint, each with a head, following the same curve
            h0 = 0.5 * q0 + 0.5 * q1
            h2 = 0.5 * q1 + 0.5 * q2
            _quad_arrow(self.ax, mid, h0, q0, c, dashed)
            _quad_arrow(self.ax, mid, h2, q2, c, dashed)
        else:
            arrow(self.ax, q0, q2, kind="process", bend=sub_bend, color=c, dashed=dashed, head=0.2)
        tan = q2 - q0
        tan = tan / (np.linalg.norm(tan) or 1)
        left = np.array([-tan[1], tan[0]])
        sgn = -1 if flip else 1
        if side:
            self._side(mid, tan, left * sgn, side, side_reach, side_size, c, side_span)
        if enzyme:
            en = -left * sgn if not enzyme_flip else left * sgn
            tw, th = _text_size(self.ax, enzyme, enzyme_size)
            off = enzyme_offset + abs(en[0]) * tw / 2 + abs(en[1]) * th / 2
            label(self.ax, mid + en * off, enzyme, size=enzyme_size, color=self.enzyme_color or P.edge("enzyme"),
                  bold=True)
        return mid, tan, left

    def _side(self, mid, tan, nrm, side, reach, size, color, span=0.7):
        first, second = side
        r = reach
        s, e = mid - tan * r * span + nrm * r, mid + tan * r * span + nrm * r
        ctrl = mid + nrm * r * 0.05
        t = np.linspace(0, 1, 60)[:, None]
        tt = t[:, 0]
        arc = (1 - t) ** 2 * s + 2 * (1 - t) * t * ctrl + t**2 * e
        keep = np.ones(len(tt), bool)
        if first is None:
            keep &= tt >= 0.5
        if second is None:
            keep &= tt <= 0.5
        part = arc[keep]
        if second is not None:
            body = part[:-5]
            self.ax.plot(body[:, 0], body[:, 1], color=color, lw=LINE * 0.85, solid_capstyle="round", zorder=15)
            tip, tv = part[-1], part[-1] - part[-5]
            tv = tv / np.linalg.norm(tv)
            nv = np.array([-tv[1], tv[0]])
            self.ax.add_patch(Polygon([tip, tip - tv * 0.15 + nv * 0.07, tip - tv * 0.15 - nv * 0.07], closed=True,
                                      color=color, lw=0, zorder=15))
        else:
            self.ax.plot(part[:, 0], part[:, 1], color=color, lw=LINE * 0.85, solid_capstyle="round", zorder=15)
        for text, p, sgn in ((first, s, -1), (second, e, 1)):
            if text is None:
                continue
            tw, th = _text_size(self.ax, text, size)
            # beside the arc end: outward along the normal, extending away from the arrow's middle
            ext_n = abs(nrm[0]) * tw / 2 + abs(nrm[1]) * th / 2
            ext_t = abs(tan[0]) * tw / 2 + abs(tan[1]) * th / 2
            label(self.ax, p + nrm * (0.06 + ext_n) + tan * sgn * ext_t * 0.8, text, size=size)


def _quad_arrow(ax, a, ctrl, b, color, dashed):
    d = b - a
    n = np.array([-d[1], d[0]])
    bend = float(np.dot(ctrl - (a + b) / 2, n) / (np.dot(n, n) or 1))
    arrow(ax, a, b, kind="process", bend=bend, color=color, dashed=dashed, head=0.2)


def ring(center, r, n, start=90.0, clockwise=True):
    """Positions of n nodes evenly on a circle (angles in degrees, first at ``start``)."""
    s = -1 if clockwise else 1
    return [(center[0] + r * math.cos(math.radians(start + s * 360 * k / n)),
             center[1] + r * math.sin(math.radians(start + s * 360 * k / n))) for k in range(n)]


def cycle_bend(a, b, center, clockwise=True):
    """The ``bend`` that makes a step from a to b follow the circle through both points around center."""
    a, b, c = (np.asarray(v, float) for v in (a, b, center))
    r = np.linalg.norm(a - c)
    chord = np.linalg.norm(b - a)
    half = math.asin(min(1.0, chord / (2 * r)))
    sag = r * (1 - math.cos(half))
    return (2 * sag / chord) * (1 if clockwise else -1)


# ---------------------------------------------------------------------------------------------
# protein topology


def _frame(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    d = b - a
    L = np.linalg.norm(d)
    u = d / L
    return a, b, u, np.array([-u[1], u[0]]), L


def strand(ax, a, b, width=0.42, token="highlight", text=None, size="tiny", zorder=12):
    """A β-strand as a broad arrow from its N-terminal end a to its C-terminal end b (the head)."""
    a, b, u, n, L = _frame(a, b)
    hw, head = width / 2, min(width * 0.95, L * 0.45)
    neck = b - u * head
    poly = [a + n * hw, neck + n * hw, neck + n * hw * 1.6, b, neck - n * hw * 1.6, neck - n * hw, a - n * hw]
    ax.add_patch(Polygon(poly, closed=True, facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE * 0.85,
                         joinstyle="round", zorder=zorder))
    if text:
        label(ax, a + u * (L - head) * 0.5, text, size=size, color=P.on_fill(), zorder=zorder + 1)
    return {"n": a, "c": b}


def helix(ax, a, b, width=0.46, token="receptor", text=None, size="tiny", back=False, zorder=12):
    """An α-helix as a cylinder from its N-terminal end a to its C-terminal end b (the b cap faces the viewer).

    ``back=True`` draws it paler with a dashed outline: a helix behind the sheet (draw it with a
    lower zorder than the strands).
    """
    a, b, u, n, L = _frame(a, b)
    hw = width / 2
    ang = math.degrees(math.atan2(u[1], u[0]))
    e = width * 0.32  # depth of the elliptical caps
    face = P.mix(P.fill(token), P.surface(), 0.45) if back else P.fill(token)
    cap = P.mix(P.fill(token), P.surface(), 0.6) if back else P.light(token)
    ls = (0, (2.5, 1.8)) if back else "-"
    body = np.vstack([a + n * hw, b + n * hw, b - n * hw, a - n * hw])
    ax.add_patch(Polygon(body, closed=True, facecolor=face, edgecolor="none", zorder=zorder))
    ax.add_patch(Ellipse(a, e, width, angle=ang, facecolor=face, edgecolor=P.edge(token), lw=LINE * 0.85, ls=ls,
                         zorder=zorder - 0.1))
    for s in (1, -1):
        ax.plot(*np.array([a + n * hw * s, b + n * hw * s]).T, color=P.edge(token), lw=LINE * 0.85, ls=ls, zorder=zorder + 0.1)
    ax.add_patch(Ellipse(b, e, width, angle=ang, facecolor=cap, edgecolor=P.edge(token), lw=LINE * 0.85, ls=ls,
                         zorder=zorder + 0.2))
    if not back:  # a soft highlight stripe along the body
        ax.plot(*np.array([a + n * hw * 0.45 + u * e * 0.6, b + n * hw * 0.45 - u * e * 0.6]).T, color=P.light(token),
                lw=LINE * 1.6, solid_capstyle="round", zorder=zorder + 0.1)
    if text:
        label(ax, (a + b) / 2, text, size=size, color=P.on_fill(), zorder=zorder + 1)
    return {"n": a, "c": b}


def _open_spline(points, n=24):
    p = np.asarray(points, float)
    if len(p) < 3:
        return p
    ext = np.vstack([2 * p[0] - p[1], p, 2 * p[-1] - p[-2]])
    out = []
    for i in range(1, len(ext) - 2):
        p0, p1, p2, p3 = ext[i - 1], ext[i], ext[i + 1], ext[i + 2]
        for t in np.linspace(0, 1, n, endpoint=False):
            t2, t3 = t * t, t * t * t
            out.append(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t2 + (-p0 + 3 * p1 - 3 * p2 + p3) * t3))
    out.append(p[-1])
    return np.array(out)


def loop(ax, points, color=None, lw=LINE * 1.3, dashed=False, zorder=10):
    """A connecting loop (coil) as a smooth curve through the given points."""
    s = _open_spline(points)
    ax.plot(s[:, 0], s[:, 1], color=color or P.muted(), lw=lw, solid_capstyle="round", solid_joinstyle="round",
            ls=(0, (3, 2)) if dashed else "-", zorder=zorder)
    return s


def terminus(ax, xy, text, size="small"):
    """An N or C terminus marker (bold letter)."""
    label(ax, xy, text, size=size, bold=True)


def tops_strand(ax, xy, r=0.32, up=True, token="highlight", text=None, zorder=12):
    """TOPS strand symbol: a triangle pointing up (strand runs towards the viewer) or down."""
    x, y = xy
    s = 1 if up else -1
    tri = [(x, y + s * r), (x - r * 0.9, y - s * r * 0.6), (x + r * 0.9, y - s * r * 0.6)]
    ax.add_patch(Polygon(tri, closed=True, facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE * 0.85,
                         joinstyle="round", zorder=zorder))
    if text:
        label(ax, (x, y - s * r * 0.12), text, size="tiny", color=P.on_fill(), zorder=zorder + 1)


def tops_helix(ax, xy, r=0.34, token="receptor", text=None, zorder=12):
    """TOPS helix symbol: a circle (the helix seen end-on)."""
    ax.add_patch(Circle(xy, r, facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE * 0.85, zorder=zorder))
    if text:
        label(ax, xy, text, size="tiny", color=P.on_fill(), zorder=zorder + 1)


def ss_track(ax, x, y, segments, length, scale=None, height=0.42, ticks=None, helix_token="receptor",
             strand_token="highlight", labels=True, zorder=12):
    """A linear secondary-structure map: coil as a line, helices as ribbon spirals, strands as arrows.

    ``segments`` = [("helix" | "strand", first_residue, last_residue, name), …] (1-based residues);
    ``scale`` is canvas units per residue (default: fit 10 units). ``ticks`` = residue spacing for
    the ruler below. Returns the x position of a residue as a function.
    """
    scale = scale or 10.0 / length

    def X(res):
        return x + (res - 1) * scale

    ax.plot([X(1), X(length)], [y, y], color=P.muted(), lw=LINE * 1.1, solid_capstyle="round", zorder=zorder - 1)
    for kind, a, b, name in segments:
        xa, xb = X(a), X(b)
        if kind == "helix":
            turns = max(1.0, (b - a + 1) / 3.6)  # 3.6 residues per turn
            t = np.linspace(0, 1, 200)
            xs = xa + (xb - xa) * t
            ph = 2 * np.pi * turns * t
            top = y + height / 2 * np.sin(ph)
            # ribbon of finite width: offset copies, back faces in the darker shade
            wdt = height * 0.2
            back = np.cos(ph) < 0
            for face, tone in ((True, P.edge(helix_token)), (False, P.fill(helix_token))):
                m = back if face else ~back
                xx = np.where(m, xs, np.nan)
                ax.fill_between(xx, top - wdt, top + wdt, color=tone, lw=0, zorder=zorder + (0 if face else 1))
            ax.plot(xs, top + wdt, color=P.edge(helix_token), lw=0.6, zorder=zorder + 1.1)
            ax.plot(xs, top - wdt, color=P.edge(helix_token), lw=0.6, zorder=zorder + 1.1)
        elif kind == "strand":
            strand(ax, (xa, y), (xb, y), width=height * 0.62, token=strand_token, zorder=zorder)
        else:
            raise ValueError(f"unknown segment kind {kind!r}")
        if labels and name:
            label(ax, ((xa + xb) / 2, y + height / 2 + 0.2), name, size="tiny", va="bottom")
    if ticks:
        base = y - height / 2 - 0.25
        ax.plot([X(1), X(length)], [base, base], color=P.muted(), lw=0.6, zorder=zorder - 1)
        for r in range(0, length + 1, ticks):
            rr = max(r, 1)
            ax.plot([X(rr), X(rr)], [base, base - 0.08], color=P.muted(), lw=0.6, zorder=zorder - 1)
            label(ax, (X(rr), base - 0.14), str(rr), size="tiny", va="top", color=P.muted())
    return X
