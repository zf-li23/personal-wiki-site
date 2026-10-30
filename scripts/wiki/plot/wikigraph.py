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
"""

import math
from collections import defaultdict

import matplotlib.pyplot as plt
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
         edge_color=INK, radius=RADIUS, width=EDGE, dashed=None, label_offset=0.16, vertex_labels=None):
    """Draw a graph. Returns nothing; see the module docstring for the arguments.

    ``weights`` writes the third element of each edge tuple beside the edge; ``dashed`` is a set of
    edges drawn dashed (for example non-tree edges); ``vertex_labels`` overrides the text inside a
    vertex (default: its name; ``labels=False`` draws empty vertices).
    """
    highlight = highlight or {}
    vertex_color = vertex_color or {}
    dashed = {_key(*e[:2], directed) for e in (dashed or [])}
    groups = defaultdict(list)
    for e in edges:
        groups[_key(e[0], e[1], directed) if e[0] != e[1] else (e[0], e[0])].append(e)
    for (a, b), group in groups.items():
        for i, e in enumerate(group):
            u, v = e[0], e[1]
            label = e[2] if len(e) > 2 else None
            colour = _lookup(highlight, u, v, directed) or edge_color
            lw = width * (2.0 if _lookup(highlight, u, v, directed) else 1.0)
            style = "--" if _key(u, v, directed) in dashed else "-"
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
                mx, my = (x0 + x1) / 2, (y0 + y1) / 2
                dx, dy = x1 - x0, y1 - y0
                n = math.hypot(dx, dy) or 1.0
                nx, ny = -dy / n, dx / n
                bend = rad * n / 2
                off = label_offset + abs(bend)
                sign = 1 if bend >= 0 else -1
                ax.text(mx + sign * nx * off, my + sign * ny * off, str(label), fontsize=FONT - 1,
                        ha="center", va="center", color=colour, zorder=4)
    for v, (x, y) in pos.items():
        ring = highlight.get(v, INK)
        fill = vertex_color.get(v, "white")
        ax.add_patch(Circle((x, y), radius, facecolor=fill, edgecolor=ring, lw=width * (2 if v in highlight else 1), zorder=3))
        if labels:
            text = (vertex_labels or {}).get(v, v)
            light = fill not in ("white", "#ffffff")
            ax.text(x, y, str(text), fontsize=FONT, ha="center", va="center", zorder=5,
                    color="white" if light else INK)


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
