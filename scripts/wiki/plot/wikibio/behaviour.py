"""Behavioural ecology: optimal foraging (marginal value theorem) and evolutionary game theory.

    from wikibio import behaviour as bh
    g = bh.gain(G=10, r=0.1)                                 a diminishing-returns gain function g(t)
    t_opt, rate = bh.mvt_optimum(g, tau=8)                   patch residence time maximizing g(t) / (tau + t)
    bh.mvt_panel(plot, g, taus=[5, 20], tokens=["dna", "rna"])   gain curve + tangents from (-tau, 0)
    bh.flower(ax, (3, 2), 0.3)                                a five-petalled flower (food patch item)
    M = bh.hawk_dove(V=2, C=3)                                payoff matrix (row player's payoff)
    bh.payoff_matrix(ax, (4, 3), ["Hawk", "Dove"], labels)    a 2x2 (or n x n) payoff table
    p = bh.replicator(M, p0=0.1, t=np.linspace(0, 30, 600))   two-strategy replicator dynamics

Models: Charnov (1976) marginal value theorem — leave a patch when the marginal gain rate g'(t) falls to
the best long-term rate R* = g(t*) / (tau + t*); graphically, t* is where the tangent from (-tau, 0)
touches g. Maynard Smith & Price (1973) hawk–dove game with replicator dynamics
dp/dt = p (1 - p) (W_H - W_D); for C > V the mixed ESS is p* = V / C.
"""

import math

import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch

from . import palette as P
from .core import LINE, label
from .quant import odeint_rk4


# ------------------------------------------------------------------ optimal foraging
class gain:
    """Diminishing-returns patch gain g(t) = G (1 - exp(-r t)) (callable; ``.d(t)`` is g'(t))."""

    def __init__(self, G=10.0, r=0.1):
        self.G, self.r = G, r

    def __call__(self, t):
        return self.G * (1 - np.exp(-self.r * np.asarray(t, float)))

    def d(self, t):
        return self.G * self.r * np.exp(-self.r * np.asarray(t, float))


def mvt_optimum(g, tau, t_max=None):
    """(t*, R*): the residence time maximizing the long-term rate R(t) = g(t) / (tau + t), and that rate.

    Golden-section search on (0, t_max]; R is unimodal for any concave gain function with g(0) = 0.
    """
    hi = t_max if t_max is not None else 50.0 / getattr(g, "r", 0.1)
    lo = 1e-9
    phi = (math.sqrt(5) - 1) / 2
    R = lambda t: float(g(t)) / (tau + t)  # noqa: E731
    a, b = lo, hi
    c, d = b - phi * (b - a), a + phi * (b - a)
    for _ in range(120):
        if R(c) > R(d):
            b, d = d, c
            c = b - phi * (b - a)
        else:
            a, c = c, d
            d = a + phi * (b - a)
    t = (a + b) / 2
    return t, R(t)


def mvt_panel(p, g, taus, tokens, t_max=None, lw=2.4, text=True, size="tiny"):
    """The marginal-value-theorem construction on a ``quant.Plot`` whose x axis runs from -tau_max to t_max.

    Draws g(t) for t >= 0, then for each travel time a tangent line from (-tau, 0) to (t*, g(t*)), a
    dotted drop to t* on the axis and the travel-time bracket below the axis. Returns [(tau, t*, R*), ...].
    """
    t_hi = t_max if t_max is not None else p.xlim[1]
    t = np.linspace(0, t_hi, 400)
    p.line(t, g(t), "ink", lw=lw)
    out = []
    for tau, tok in zip(taus, tokens):
        ts, rs = mvt_optimum(g, tau, t_max=t_hi)
        gx = float(g(ts))
        x_end = min(t_hi, ts + (t_hi - ts) * 0.35, max(p.ylim) / rs - tau - 1e-6)  # stay inside the y range
        xs = np.linspace(-tau, x_end, 60)
        p.line(xs, rs * (tau + xs), tok, lw=1.4)
        p.line([ts, ts], [p.ylim[0], gx], tok, lw=0.9, dotted=True)
        p.points([ts], [gx], tok, r=0.11, zorder=p.z + 5)
        p.points([-tau], [0], tok, r=0.09)
        out.append((tau, ts, rs))
    return out


def flower(ax, center, r, token="petal", petals=5, angle=90.0, depleted=False, zorder=10):
    """A simple flower seen from above: ``petals`` ellipses around a disc (``depleted`` greys the centre)."""
    cx, cy = center
    for k in range(petals):
        a = math.radians(angle + k * 360 / petals)
        ax.add_patch(Ellipse((cx + r * 0.55 * math.cos(a), cy + r * 0.55 * math.sin(a)), r * 1.0, r * 0.62,
                             angle=math.degrees(a), facecolor=P.fill(token), edgecolor=P.edge(token), lw=0.7, zorder=zorder))
    core = "neutral" if depleted else "anther"
    ax.add_patch(Circle(center, r * 0.32, facecolor=P.fill(core), edgecolor=P.edge(core), lw=0.7, zorder=zorder + 1))


def patch(ax, center, r, n=5, depleted=0, seed=0, token="plant", flower_r=None, zorder=6):
    """A food patch: a pale disc with ``n`` flowers, the first ``depleted`` of them already emptied."""
    ax.add_patch(Circle(center, r, facecolor=P.mix(P.fill(token), P.surface(), 0.8 if P.is_dark() else 0.6),
                        edgecolor=P.edge(token), lw=LINE * 0.7, zorder=zorder))
    rng = np.random.default_rng(seed)
    fr = flower_r or r * 0.24
    pts = []
    for k in range(n):
        a = 2 * math.pi * k / n + rng.uniform(-0.3, 0.3)
        d = r * (0.5 if n > 1 else 0) + rng.uniform(-0.06, 0.06) * r
        pts.append((center[0] + d * math.cos(a), center[1] + d * math.sin(a)))
    for k, q in enumerate(pts):
        flower(ax, q, fr, depleted=k < depleted, angle=90 + 20 * k, zorder=zorder + 2)
    return pts


def timeline(ax, x0, y, segments, h=0.32, size="tiny", zorder=8):
    """A foraging time budget: ``segments`` = [(duration_in_canvas_units, token, text)], drawn left to right."""
    x = x0
    for w, tok, text in segments:
        ax.add_patch(FancyBboxPatch((x, y - h / 2), w, h, boxstyle="round,pad=0,rounding_size=0.06",
                                    facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, zorder=zorder))
        if text:
            label(ax, (x + w / 2, y), text, size=size, color=P.on_fill(), zorder=zorder + 1)
        x += w
    return x


# ------------------------------------------------------------------ evolutionary games
def hawk_dove(V=2.0, C=3.0):
    """Payoff matrix of the hawk–dove game (rows: focal strategy H, D; columns: opponent H, D)."""
    return np.array([[(V - C) / 2, V], [0.0, V / 2]])


def fitness(M, p):
    """Expected payoffs (W_1, W_2) of the two strategies when strategy 1 has frequency p."""
    p = np.asarray(p, float)
    w1 = M[0, 0] * p + M[0, 1] * (1 - p)
    w2 = M[1, 0] * p + M[1, 1] * (1 - p)
    return w1, w2


def replicator(M, p0, t):
    """Frequency of strategy 1 over time under the replicator equation dp/dt = p (1 - p) (W_1 - W_2)."""
    def f(_, y):
        w1, w2 = fitness(M, y[0])
        return np.array([y[0] * (1 - y[0]) * (w1 - w2)])
    return odeint_rk4(f, np.array([p0]), t)[:, 0]


def payoff_matrix(ax, center, strategies, cells, w=1.9, h=0.95, tokens=None, size="small", header="small",
                  highlight=None, row_title="Focal", col_title="Opponent", zorder=8):
    """A payoff table: ``cells[i][j]`` (text) is the payoff to a focal player using strategy i against j.

    ``tokens`` colour the row/column headers per strategy; ``highlight`` = (i, j) tints one cell.
    Returns the canvas centre of every cell as {(i, j): xy}.
    """
    n = len(strategies)
    cx, cy = center
    x0, y1 = cx - n * w / 2, cy + n * h / 2
    tokens = tokens or ["neutral"] * n
    pos = {}
    for i in range(n):
        for j in range(n):
            x, y = x0 + j * w, y1 - (i + 1) * h
            hl = highlight is not None and (i, j) in (highlight if isinstance(highlight, list) else [highlight])
            fc = P.mix(P.fill("highlight"), P.surface(), 0.55) if hl else P.surface()
            ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="square,pad=0", facecolor=fc, edgecolor=P.muted(), lw=0.8,
                                        zorder=zorder))
            pos[(i, j)] = (x + w / 2, y + h / 2)
            label(ax, pos[(i, j)], cells[i][j], size=size, zorder=zorder + 2)
    hw = 1.25
    for k, s in enumerate(strategies):
        tok = tokens[k]
        # column header (opponent) above, row header (focal) left
        ax.add_patch(FancyBboxPatch((x0 + k * w + 0.06, y1 + 0.06), w - 0.12, 0.5, boxstyle="round,pad=0,rounding_size=0.1",
                                    facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, zorder=zorder))
        label(ax, (x0 + (k + 0.5) * w, y1 + 0.31), s, size=header, bold=True, color=P.on_fill(), zorder=zorder + 2)
        ax.add_patch(FancyBboxPatch((x0 - hw - 0.06, y1 - (k + 1) * h + 0.06), hw, h - 0.12,
                                    boxstyle="round,pad=0,rounding_size=0.1", facecolor=P.fill(tok), edgecolor=P.edge(tok),
                                    lw=0.8, zorder=zorder))
        label(ax, (x0 - hw / 2 - 0.06, y1 - (k + 0.5) * h), s, size=header, bold=True, color=P.on_fill(), zorder=zorder + 2)
    if col_title:
        label(ax, (cx, y1 + 0.85), col_title, size="tiny", color=P.muted())
    if row_title:
        label(ax, (x0 - hw / 2 - 0.06, y1 + 0.31), row_title, size="tiny", color=P.muted())
    return pos


def phase_line(ax, x, y0, y1, fixed, stable, rhs, n=7, color=None, size="tiny", zorder=12):
    """A vertical 1-D phase line from y0 (p = 0) to y1 (p = 1): fixed points (filled if stable) and flow arrows.

    ``fixed`` are the p values of equilibria, ``stable`` booleans, ``rhs(p)`` the right-hand side (sign gives direction).
    """
    from .core import arrow
    c = color or P.ink()
    ax.plot([x, x], [y0, y1], color=P.muted(), lw=1.0, zorder=zorder - 1)
    Y = lambda p: y0 + (y1 - y0) * p  # noqa: E731
    pts = sorted(fixed)
    for a, b in zip(pts[:-1], pts[1:]):
        m = (a + b) / 2
        s = np.sign(rhs(m))
        if s == 0:
            continue
        lo, hi = Y(a) + 0.25, Y(b) - 0.25
        if hi - lo < 0.2:
            continue
        arrow(ax, (x, lo if s > 0 else hi), (x, hi if s > 0 else lo), kind="process", color=c, lw=1.2, head=0.18, zorder=zorder)
    for p_, st in zip(fixed, stable):
        ax.add_patch(Circle((x, Y(p_)), 0.12, facecolor=c if st else P.surface(), edgecolor=c, lw=1.0, zorder=zorder + 1))


__all__ = ["gain", "mvt_optimum", "mvt_panel", "flower", "patch", "timeline", "hawk_dove", "fitness", "replicator",
           "payoff_matrix", "phase_line"]
