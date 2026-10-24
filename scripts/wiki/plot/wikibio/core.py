"""Canvas, text, arrows and other annotation for biology figures.

Coordinates are in figure units chosen by the script (``canvas(w, h)`` gives an axes spanning
0..w by 0..h with equal aspect); ``scale`` sets inches per unit. Arrows follow SBGN semantics:

    kind="process"     filled triangle   conversion, transport, a reaction step
    kind="activation"  open arrowhead    positive influence / stimulation
    kind="inhibition"  bar               negative influence
    kind="catalysis"   open circle       catalysis
    kind="necessary"   bar + open head   necessary stimulation
    kind="link"        no head           association, leader lines
"""

import math

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch, PathPatch, Polygon
from matplotlib.path import Path

from . import palette as P

LINE = 1.3  # default line width (points)
FONT = {"title": 11.5, "normal": 9.5, "small": 8.0, "tiny": 6.8}


def canvas(width, height, scale=0.45):
    """A figure with one axes spanning 0..width × 0..height (equal aspect, no frame)."""
    fig, ax = plt.subplots(figsize=(width * scale, height * scale))
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.subplots_adjust(0, 0, 1, 1)
    return fig, ax


def label(ax, xy, text, size="normal", color=None, ha="center", va="center", italic=False, bold=False, rotation=0, zorder=20):
    """Text in the figure style (English only). ``italic=True`` for gene names and species."""
    return ax.text(*xy, text, fontsize=FONT.get(size, size), color=color or P.ink(), ha=ha, va=va,
                   style="italic" if italic else "normal", weight="bold" if bold else "normal",
                   rotation=rotation, zorder=zorder)


def callout(ax, point, text_xy, text, size="small", color=None):
    """A label joined to a point by a thin leader line ending in a small dot."""
    c = color or P.muted()
    ax.plot([text_xy[0], point[0]], [text_xy[1], point[1]], color=c, lw=0.7, zorder=19, solid_capstyle="round")
    ax.add_patch(Circle(point, 0.06, color=c, zorder=19))
    dx = point[0] - text_xy[0]
    ha = "right" if dx > 0.05 else "left" if dx < -0.05 else "center"
    return label(ax, (text_xy[0] - (0.08 if ha == "right" else -0.08 if ha == "left" else 0), text_xy[1]), text,
                 size=size, ha=ha)


def panel(ax, letter, xy):
    """Panel letter (A, B, …) in the top-left corner of a sub-figure."""
    return label(ax, xy, letter, size="title", bold=True, ha="left", va="top")


def scale_bar(ax, xy, length, text, size="small"):
    x, y = xy
    ax.plot([x, x + length], [y, y], color=P.ink(), lw=2.2, solid_capstyle="butt", zorder=19)
    label(ax, (x + length / 2, y - 0.22), text, size=size, va="top")


def _bezier(a, b, bend):
    a, b = np.asarray(a, float), np.asarray(b, float)
    d = b - a
    n = np.array([-d[1], d[0]])
    ctrl = (a + b) / 2 + bend * n
    t = np.linspace(0, 1, 60)[:, None]
    pts = (1 - t) ** 2 * a + 2 * (1 - t) * t * ctrl + t**2 * b
    return pts


def arrow(ax, a, b, kind="process", bend=0.0, color=None, lw=LINE, dashed=False, shrink=0.0, head=0.22, zorder=15, bg=None):
    """An arrow from a to b (SBGN semantics, see module doc). ``bend`` curves it sideways.

    ``bg`` is the fill of open heads (activation, catalysis, modulation): pass the compartment's
    fill when the arrow lies on a tinted region; the default is the page background.
    """
    c = color or P.ink()
    bg = bg or P.surface()
    pts = _bezier(a, b, bend)
    if shrink:
        # trim both ends by `shrink` units (to stop short of objects)
        seg = np.cumsum(np.r_[0, np.hypot(*np.diff(pts, axis=0).T)])
        keep = (seg >= shrink) & (seg <= seg[-1] - shrink)
        pts = pts[keep]
    tip = pts[-1]
    tan = pts[-1] - pts[-4]
    tan = tan / (np.linalg.norm(tan) or 1)
    nrm = np.array([-tan[1], tan[0]])
    body = pts.copy()
    if kind in ("process", "activation", "necessary"):
        body = body[np.hypot(*(body - tip).T) >= head * 0.6]
        body = np.vstack([body, tip - tan * head * 0.6])
    elif kind == "catalysis":
        body = body[np.hypot(*(body - tip).T) >= head * 0.9]
    elif kind == "modulation":
        body = body[np.hypot(*(body - tip).T) >= head * 1.1]
    ax.plot(body[:, 0], body[:, 1], color=c, lw=lw, ls=(0, (3.2, 2.2)) if dashed else "-", solid_capstyle="round", zorder=zorder,
            snap=False)  # pixel snapping turns the sampled curve's float noise into visible bumps
    w = head * 0.55
    if kind == "process":
        ax.add_patch(Polygon([tip, tip - tan * head + nrm * w, tip - tan * head - nrm * w], closed=True, color=c, lw=0, zorder=zorder))
    elif kind in ("activation", "necessary"):
        ax.add_patch(Polygon([tip, tip - tan * head + nrm * w, tip - tan * head * 0.7, tip - tan * head - nrm * w],
                             closed=True, facecolor=bg, edgecolor=c, lw=lw * 0.9, zorder=zorder + 1))
        if kind == "necessary":
            bar = tip - tan * head * 1.25
            ax.plot(*np.array([bar + nrm * w * 1.1, bar - nrm * w * 1.1]).T, color=c, lw=lw, zorder=zorder)
    elif kind == "inhibition":
        ax.plot(*np.array([tip + nrm * w * 1.3, tip - nrm * w * 1.3]).T, color=c, lw=lw * 1.5, solid_capstyle="butt", zorder=zorder)
    elif kind == "catalysis":
        ax.add_patch(Circle(tip - tan * head * 0.45, head * 0.45, facecolor=bg, edgecolor=c, lw=lw * 0.9, zorder=zorder + 1))
    elif kind == "modulation":
        # SBGN modulation / unknown influence: an open diamond
        m = tip - tan * head * 0.6
        ax.add_patch(Polygon([tip, m + nrm * w * 0.9, tip - tan * head * 1.2, m - nrm * w * 0.9], closed=True,
                             facecolor=bg, edgecolor=c, lw=lw * 0.9, zorder=zorder + 1))
    elif kind != "link":
        raise ValueError(f"unknown arrow kind {kind!r}")
    return pts


def reaction(ax, a, b, side=None, bend=0.0, kind="process", color=None, reach=0.75):
    """A conversion arrow a → b with co-substrates entering and leaving on one arc, as in metabolic maps.

    ``side=("ATP", "ADP")`` draws an arc above the arrow (``reach`` < 0 puts it below): the first
    species joins the main arrow, the second leaves it.
    """
    pts = arrow(ax, a, b, kind=kind, bend=bend, color=color)
    if side:
        mid = pts[len(pts) // 2]
        d = np.asarray(b, float) - np.asarray(a, float)
        d /= np.linalg.norm(d)
        n = np.array([-d[1], d[0]]) * np.sign(reach)
        r = abs(reach)
        start, end = mid - d * r * 0.9 + n * r, mid + d * r * 0.9 + n * r
        t = np.linspace(0, 1, 50)[:, None]
        ctrl = mid - n * r * 0.35
        arc = (1 - t) ** 2 * start + 2 * (1 - t) * t * ctrl + t**2 * end
        c = color or P.ink()
        ax.plot(arc[:-6, 0], arc[:-6, 1], color=c, lw=LINE * 0.9, solid_capstyle="round", zorder=15)
        tip, tan = arc[-1], arc[-1] - arc[-6]
        tan /= np.linalg.norm(tan)
        nn = np.array([-tan[1], tan[0]])
        ax.add_patch(Polygon([tip, tip - tan * 0.17 + nn * 0.08, tip - tan * 0.17 - nn * 0.08], closed=True, color=c, lw=0, zorder=15))
        first, second = side
        label(ax, start + n * 0.22 - d * 0.1, first, size="small")
        label(ax, end + n * 0.22 + d * 0.1, second, size="small")
    return pts


def box(ax, center, w, h, token="neutral", text=None, radius=0.18, size="normal", italic=False, lw=LINE * 0.9, zorder=10):
    """A rounded box in a token's colours (SBGN 'macromolecule' / generic node)."""
    x, y = center
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle=f"round,pad=0,rounding_size={radius}",
                                facecolor=P.fill(token), edgecolor=P.edge(token), lw=lw, zorder=zorder))
    if text:
        label(ax, center, text, size=size, italic=italic, color=P.on_fill(), zorder=zorder + 1)


def smooth_closed(points, n=200):
    """A smooth closed curve through control points (periodic Catmull–Rom)."""
    p = np.asarray(points, float)
    m = len(p)
    out = []
    for i in range(m):
        p0, p1, p2, p3 = p[(i - 1) % m], p[i], p[(i + 1) % m], p[(i + 2) % m]
        for t in np.linspace(0, 1, max(2, n // m), endpoint=False):
            t2, t3 = t * t, t * t * t
            out.append(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t2 + (-p0 + 3 * p1 - 3 * p2 + p3) * t3))
    out.append(out[0])
    return np.array(out)


def blob(center, rx, ry, wobble=0.08, seed=0, k=9, angle=0.0):
    """Vertices of an organic closed outline (deterministic for a given seed)."""
    rng = np.random.default_rng(seed)
    th = np.linspace(0, 2 * np.pi, k, endpoint=False)
    r = 1 + wobble * rng.uniform(-1, 1, k)
    pts = np.c_[rx * r * np.cos(th), ry * r * np.sin(th)]
    c, s = math.cos(angle), math.sin(angle)
    pts = pts @ np.array([[c, s], [-s, c]]) + np.asarray(center, float)
    return smooth_closed(pts)


def shape(ax, vertices, token="neutral", lw=LINE, zorder=5, alpha=1.0, fill=True):
    """Fill and outline a closed polygon in a token's colours."""
    v = np.asarray(vertices, float)
    path = Path(np.vstack([v, v[:1]]), closed=True)  # closed=True ignores the last vertex: repeat the first
    ax.add_patch(PathPatch(path, fill=fill, facecolor=P.fill(token), edgecolor=P.edge(token), lw=lw,
                           zorder=zorder, alpha=alpha if alpha < 0.999 else None, joinstyle="round"))


def polyline(points, n=400, closed=None):
    """Resample a polyline/curve evenly; returns (points, unit normals, arc length).

    A closed curve (first point == last, or ``closed=True``) is resampled without a seam: normals
    wrap around, so contours offset from it join cleanly.
    """
    p = np.asarray(points, float)
    keep = np.r_[True, np.hypot(*np.diff(p, axis=0).T) > 1e-9]
    p = p[keep]
    if closed is None:
        closed = len(p) > 2 and np.hypot(*(p[0] - p[-1])) < 1e-6
    if closed and np.hypot(*(p[0] - p[-1])) > 1e-6:
        p = np.vstack([p, p[:1]])
    seg = np.hypot(*np.diff(p, axis=0).T)
    s = np.r_[0, np.cumsum(seg)]
    t = np.linspace(0, s[-1], n, endpoint=not closed)
    q = np.c_[np.interp(t, s, p[:, 0]), np.interp(t, s, p[:, 1])]
    if closed:
        d = np.roll(q, -1, axis=0) - np.roll(q, 1, axis=0)
    else:
        d = np.gradient(q, axis=0)
    d /= np.linalg.norm(d, axis=1)[:, None]
    nrm = np.c_[-d[:, 1], d[:, 0]]
    if closed:  # repeat the first point so drawn contours close
        q, nrm = np.vstack([q, q[:1]]), np.vstack([nrm, nrm[:1]])
    return q, nrm, s[-1]
