"""Small graphs drawn by hand for plot scripts: vertices at given coordinates, edges, arcs, labels.

Plot scripts import it as ``import wikigraph as G`` (render_plot.py puts this folder on the path).
Ink is black and vertex fills are white, which the renderer turns into light ink on a dark surface
for the dark theme; the accent colours below read on both backgrounds.

    import wikigraph as G

    pos = {"a": (0, 0), "b": (2, 0), "c": (1, 1.6)}
    fig, ax = G.canvas(4, 2.4)
    G.draw(ax, pos, [("a", "b", 3), ("b", "c", 1), ("c", "a", 2)], weights=True,
           highlight={("a", "b"): G.RED}, vertex_color={"c": G.BLUE})
    G.caption(ax, (1, -0.6), "a triangle")

Edges are tuples ``(u, v)`` or ``(u, v, label)``; with ``directed=True`` they are arcs drawn with
arrowheads. Parallel edges between the same pair are bent apart automatically, and ``(v, v)`` draws
a loop. ``highlight`` maps an edge ``(u, v)`` (either order for undirected graphs) or a vertex to a
colour and draws it thicker. Coordinates are in arbitrary units with equal aspect.

More: ``G.grid(rows, cols, w, h, titles)`` for step-by-step panels; ``vertex_notes={v: "d=3"}`` for
small labels beside vertices; ``label_pos`` to move weight labels along the edges; ``vertices=False``
to add a second set of edges (mixed graphs); ``G.curve(ax, [p, ..., q])`` for a smooth edge through
waypoints; ``G.colors({v: value})`` for a colour per vertex (Fiedler vectors, centralities).
"""

import math
from collections import defaultdict

import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb
from matplotlib.patches import Circle, FancyArrowPatch

INK = "black"
BLUE = "#2563eb"
RED = "#dc2626"
GREEN = "#16a34a"
AMBER = "#d97706"
VIOLET = "#7c3aed"
GREY = "#94a3b8"
ACCENTS = [BLUE, RED, GREEN, AMBER, VIOLET]

RADIUS = 0.22  # vertex radius (figure units)
EDGE = 1.4  # edge line width (points)
FONT = 10


def canvas(width, height, scale=0.9, margin=0.4):
    """A figure with one equal-aspect axes covering -margin..width+margin × -margin..height+margin."""
    fig, ax = plt.subplots(figsize=((width + 2 * margin) * scale, (height + 2 * margin) * scale))
    ax.set_xlim(-margin, width + margin)
    ax.set_ylim(-margin, height + margin)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.subplots_adjust(0, 0, 1, 1)
    return fig, ax


def panels(n, width, height, scale=0.9, margin=0.4, titles=None):
    """``n`` side-by-side canvases of the same size; returns (fig, [ax, ...])."""
    fig, axes = plt.subplots(1, n, figsize=(n * (width + 2 * margin) * scale, (height + 2 * margin + 0.4) * scale))
    axes = list(axes) if n > 1 else [axes]
    for i, ax in enumerate(axes):
        ax.set_xlim(-margin, width + margin)
        ax.set_ylim(-margin, height + margin)
        ax.set_aspect("equal")
        ax.axis("off")
        if titles:
            ax.set_title(titles[i], fontsize=FONT)
    fig.subplots_adjust(0.01, 0.01, 0.99, 0.92 if titles else 0.99, wspace=0.05)
    return fig, axes


def circle(names, radius=1.0, center=(0.0, 0.0), start=90.0):
    """Positions of ``names`` evenly on a circle, the first at angle ``start`` (degrees), counter-clockwise."""
    names = list(names)
    n = len(names)
    return {v: (center[0] + radius * math.cos(math.radians(start + 360.0 * i / n)),
                center[1] + radius * math.sin(math.radians(start + 360.0 * i / n))) for i, v in enumerate(names)}


def _key(u, v, directed):
    return (u, v) if directed or str(u) <= str(v) else (v, u)


def _lookup(table, u, v, directed):
    if not table:
        return None
    if (u, v) in table:
        return table[(u, v)]
    if not directed and (v, u) in table:
        return table[(v, u)]
    return None


def draw(ax, pos, edges, directed=False, weights=False, labels=True, highlight=None, vertex_color=None,
         edge_color=INK, radius=RADIUS, width=EDGE, dashed=None, label_offset=0.16, vertex_labels=None,
         vertex_notes=None, note_offset=None, label_pos=0.5, vertices=True, label_color=None):
    """Draw a graph. Returns nothing; see the module docstring for the arguments.

    ``weights`` writes the third element of each edge tuple beside the edge, at the fraction
    ``label_pos`` of the way from u to v; ``dashed`` is a set of edges drawn dashed (for example
    non-tree edges); ``vertex_labels`` overrides the text inside a vertex (default: its name;
    ``labels=False`` draws empty vertices). ``vertex_notes`` maps a vertex to a small text written
    beside it (BFS layers, degrees, Dijkstra labels), below it by default, or to ``(text, (dx, dy))``
    for an explicit offset. ``vertices=False`` draws only the edges, so that a mixed graph can be
    drawn with two calls. ``label_color`` maps a vertex to the colour of its text (default: white on
    dark fills, ink otherwise). A copy of a parallel edge is addressed in ``highlight`` and
    ``dashed`` as ``(u, v, i)``, ``i`` counting the copies in the order they are listed.
    """
    highlight = highlight or {}
    vertex_color = vertex_color or {}
    dashed_idx = {(_key(*e[:2], directed), e[2]) for e in (dashed or []) if len(e) > 2}
    dashed = {_key(*e[:2], directed) for e in (dashed or []) if len(e) == 2}
    groups = defaultdict(list)
    for e in edges:
        groups[_key(e[0], e[1], directed) if e[0] != e[1] else (e[0], e[0])].append(e)
    for (a, b), group in groups.items():
        for i, e in enumerate(group):
            u, v = e[0], e[1]
            label = e[2] if len(e) > 2 else None
            mark = highlight.get((u, v, i)) or (None if directed else highlight.get((v, u, i))) \
                or _lookup(highlight, u, v, directed)
            colour = mark or edge_color
            lw = width * (2.0 if mark else 1.0)
            key = _key(u, v, directed)
            style = "--" if key in dashed or (key, i) in dashed_idx else "-"
            if u == v:
                _loop(ax, pos[u], radius, colour, lw, i)
                continue
            k = len(group)
            rad = 0.0 if k == 1 else 0.25 * (i - (k - 1) / 2)
            if not directed and (u, v) != (a, b):
                rad = -rad
            if directed and any(x[0] == v and x[1] == u for x in edges):
                rad = rad or 0.18  # an arc and its reverse are bent apart
            arrow = FancyArrowPatch(pos[u], pos[v], connectionstyle=f"arc3,rad={rad}",
                                    arrowstyle="-|>,head_length=6,head_width=3.2" if directed else "-",
                                    shrinkA=radius * _points_per_unit(ax), shrinkB=radius * _points_per_unit(ax),
                                    color=colour, lw=lw, linestyle=style, zorder=2)
            ax.add_patch(arrow)
            if weights and label is not None:
                (x0, y0), (x1, y1) = pos[u], pos[v]
                mx, my = x0 + label_pos * (x1 - x0), y0 + label_pos * (y1 - y0)
                dx, dy = x1 - x0, y1 - y0
                n = math.hypot(dx, dy) or 1.0
                nx, ny = -dy / n, dx / n
                bend = rad * n / 2
                off = label_offset + abs(bend)
                sign = 1 if bend >= 0 else -1
                ax.text(mx + sign * nx * off, my + sign * ny * off, str(label), fontsize=FONT - 1,
                        ha="center", va="center", color=colour, zorder=4)
    if not vertices:
        return
    for v, (x, y) in pos.items():
        ring = highlight.get(v, INK)
        fill = vertex_color.get(v, "white")
        ax.add_patch(Circle((x, y), radius, facecolor=fill, edgecolor=ring, lw=width * (2 if v in highlight else 1), zorder=3))
        if labels:
            text = (vertex_labels or {}).get(v, v)
            colour = (label_color or {}).get(v) or ("white" if _dark(fill) else INK)
            ax.text(x, y, str(text), fontsize=FONT, ha="center", va="center", zorder=5, color=colour)
        if vertex_notes and v in vertex_notes:
            note = vertex_notes[v]
            text, (dx, dy) = note if isinstance(note, tuple) else (note, note_offset or (0.0, -2.1 * radius))
            ax.text(x + dx, y + dy, str(text), fontsize=FONT - 2, ha="center", va="center", zorder=5, color=INK)


def _dark(colour):
    """True for fills on which white text reads better than ink."""
    r, g, b = to_rgb(colour)
    return 0.299 * r + 0.587 * g + 0.114 * b < 0.55


def grid(rows, cols, width, height, scale=0.9, margin=0.4, titles=None):
    """A rows × cols grid of equal canvases; returns (fig, [ax, ...]) in reading order."""
    fig, axes = plt.subplots(rows, cols, figsize=(cols * (width + 2 * margin) * scale,
                                                  rows * (height + 2 * margin + (0.4 if titles else 0)) * scale))
    flat = list(axes.flat) if hasattr(axes, "flat") else [axes]
    for i, ax in enumerate(flat):
        ax.set_xlim(-margin, width + margin)
        ax.set_ylim(-margin, height + margin)
        ax.set_aspect("equal")
        ax.axis("off")
        if titles and i < len(titles):
            ax.set_title(titles[i], fontsize=FONT)
    fig.subplots_adjust(0.01, 0.01, 0.99, 0.95 if titles else 0.99, wspace=0.05, hspace=0.15)
    return fig, flat


def curve(ax, points, colour=INK, width=EDGE, directed=False, dashed=False, radius=RADIUS):
    """A smooth edge through the waypoints ``points`` (first and last are vertex centres), for edges
    that must go around other vertices (outer face of a dual, the long edges of K3,3)."""
    import numpy as np
    pts = np.asarray(points, dtype=float)
    ext = np.vstack([2 * pts[0] - pts[1], pts, 2 * pts[-1] - pts[-2]])
    out = []
    for i in range(1, len(ext) - 2):
        p0, p1, p2, p3 = ext[i - 1], ext[i], ext[i + 1], ext[i + 2]
        for t in np.linspace(0, 1, 24, endpoint=False):
            t2, t3 = t * t, t * t * t
            out.append(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t2 + (-p0 + 3 * p1 - 3 * p2 + p3) * t3))
    out.append(pts[-1])
    out = np.array(out)
    d = np.hypot(*(out - out[0]).T)
    e = np.hypot(*(out - out[-1]).T)
    out = out[(d >= radius) & (e >= radius)]
    style = "--" if dashed else "-"
    ax.plot(out[:, 0], out[:, 1], color=colour, lw=width, linestyle=style, zorder=2, solid_capstyle="round")
    if directed and len(out) >= 2:
        ax.annotate("", xy=out[-1], xytext=out[-2], arrowprops=dict(arrowstyle="-|>,head_length=0.6,head_width=0.3",
                                                                    color=colour, lw=width), zorder=2)


def colors(values, cmap="coolwarm", vmin=None, vmax=None):
    """Map vertex values to colours for ``vertex_color`` (diverging by default, centred on 0)."""
    import matplotlib
    vals = list(values.values())
    lo = min(vals) if vmin is None else vmin
    hi = max(vals) if vmax is None else vmax
    if vmin is None and vmax is None and lo < 0 < hi:
        m = max(-lo, hi)
        lo, hi = -m, m
    norm = matplotlib.colors.Normalize(lo, hi if hi > lo else lo + 1)
    cm = matplotlib.colormaps[cmap]
    return {v: matplotlib.colors.to_hex(cm(norm(x))) for v, x in values.items()}


def _points_per_unit(ax):
    """Points per data unit along x (axes have equal aspect)."""
    w_in = ax.figure.get_figwidth() * ax.get_position().width
    x0, x1 = ax.get_xlim()
    return 72.0 * w_in / (x1 - x0)


def _loop(ax, xy, radius, colour, lw, i):
    x, y = xy
    r = radius * (1.1 + 0.4 * i)
    ax.add_patch(Circle((x, y + radius + r * 0.9), r, fill=False, edgecolor=colour, lw=lw, zorder=1))


def caption(ax, xy, text, size=None):
    """A short English label (for example the name of a graph) at ``xy``."""
    ax.text(*xy, text, fontsize=size or FONT, ha="center", va="center", color=INK)
