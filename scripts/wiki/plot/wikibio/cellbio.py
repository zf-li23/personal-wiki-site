"""Cell biology scenes: membrane transporters, transport steps across a bilayer, the cell-cycle wheel.

    cellbio.sides(ax, (x0, x1), y, half, "Extracellular", "Cytosol")   tinted spaces above / below a membrane
    cellbio.carrier(ax, x, y, open="out")                              an alternating-access carrier (uniporter, symporter)
    cellbio.pump(ax, x, y)                                             a P-type ATPase (transmembrane + cytoplasmic domains)
    cellbio.channel(ax, x, y)                                          an ion channel with an open pore
    cellbio.flux(ax, x, y_from, y_to, species)                         an arrow through the membrane with particles on it
    cellbio.cycle_wheel(ax, center, r, phases)                         a ring of phases (donut segments) with checkpoints

Membrane proteins sit in a membrane centred at height y with half-thickness ``mh`` (0.37 matches
``bio.bilayer`` with its default sizes). Particles are ``bio.ion`` discs or ``bio.molecule`` discs.
"""

import math

import numpy as np
from matplotlib.patches import PathPatch, Polygon, Rectangle, Wedge
from matplotlib.path import Path

from . import palette as P
from .core import LINE, arrow, label, smooth_closed
from .molecules import ion, molecule

MH = 0.37


def sides(ax, xr, y, half=MH, top="Extracellular", bottom="Cytosol", height=(3.0, 3.0), top_token="extracellular",
          bottom_token="cytoplasm", label_x=None, zorder=0):
    """Tint the spaces above and below a horizontal membrane and name them (left-aligned at ``label_x``)."""
    x0, x1 = xr
    ax.add_patch(Rectangle((x0, y + half), x1 - x0, height[0], facecolor=P.fill(top_token), edgecolor="none", zorder=zorder))
    ax.add_patch(Rectangle((x0, y - half - height[1]), x1 - x0, height[1], facecolor=P.fill(bottom_token), edgecolor="none", zorder=zorder))
    lx = label_x if label_x is not None else x0 + 0.25
    if top:
        label(ax, (lx, y + half + height[0] - 0.35), top, size="small", bold=True, ha="left", color=P.muted())
    if bottom:
        label(ax, (lx, y - half - height[1] + 0.35), bottom, size="small", bold=True, ha="left", color=P.muted())


def _lobe(cx, cy, w, h, angle, r=0.16, n=10):
    # rounded rectangle centred at (cx, cy), rotated by angle (degrees)
    pts = []
    for (sx, sy), a0 in (((1, 1), 0), ((-1, 1), 90), ((-1, -1), 180), ((1, -1), 270)):
        c = np.array([sx * (w / 2 - r), sy * (h / 2 - r)])
        for t in np.linspace(math.radians(a0), math.radians(a0 + 90), n):
            pts.append(c + r * np.array([math.cos(t), math.sin(t)]))
    pts = np.array(pts)
    th = math.radians(angle)
    R = np.array([[math.cos(th), math.sin(th)], [-math.sin(th), math.cos(th)]])
    return pts @ R + [cx, cy]


def carrier(ax, x, y, open="out", token="channel", mh=MH, width=1.25, text=None, zorder=11):
    """An alternating-access carrier: two halves forming a cleft open to the outside (top) or inside.

    Returns the (x, y) of the binding site in the cleft.
    """
    s = 1 if open == "out" else -1
    h = 2 * mh + 0.4
    tilt = 11 * s
    for side in (-1, 1):
        o = _lobe(x + side * width * 0.25, y, width * 0.5, h, -side * tilt, r=0.18)
        ax.add_patch(Polygon(o, closed=True, facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE * 0.9, joinstyle="round", zorder=zorder))
    hl = _lobe(x - width * 0.3, y + 0.1, width * 0.12, h * 0.55, tilt, r=0.05)
    ax.add_patch(Polygon(hl, closed=True, facecolor=P.light(token), edgecolor="none", alpha=0.6, zorder=zorder + 0.1))
    if text:
        label(ax, (x, y - s * (h / 2 + 0.25)), text, size="small", bold=True)
    return np.array([x, y + s * 0.12])


def channel(ax, x, y, token="channel", mh=MH, width=1.1, text=None, zorder=11):
    """An ion channel: two subunits around a water-filled pore (open)."""
    h = 2 * mh + 0.36
    for side in (-1, 1):
        o = _lobe(x + side * width * 0.32, y, width * 0.36, h, 0, r=0.16)
        ax.add_patch(Polygon(o, closed=True, facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE * 0.9, joinstyle="round", zorder=zorder))
        # selectivity-filter bulge towards the pore
        f = _lobe(x + side * width * 0.16, y + mh * 0.35, width * 0.12, 0.3, 0, r=0.05)
        ax.add_patch(Polygon(f, closed=True, facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE * 0.7, zorder=zorder + 0.1))
    if text:
        label(ax, (x, y - h / 2 - 0.25), text, size="small", bold=True)


def pump(ax, x, y, token="enzyme", mh=MH, width=1.5, text=None, zorder=11):
    """A P-type ATPase: a transmembrane domain and the cytoplasmic A, P and N domains (ATP binds N/P).

    The headpiece hangs below the right half; transport arrows fit through the left half
    (x - width/4). Returns the point where ATP binds (beside the N domain).
    """
    h = 2 * mh + 0.36
    o = _lobe(x, y, width, h, 0, r=0.2)
    ax.add_patch(Polygon(o, closed=True, facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE * 0.9, joinstyle="round", zorder=zorder))
    for k in range(4):  # helix bundle hints
        xx = x + (k - 1.5) * width * 0.22
        ax.plot([xx, xx], [y - h / 2 + 0.12, y + h / 2 - 0.12], color=P.light(token), lw=LINE * 1.4, solid_capstyle="round", zorder=zorder + 0.1)
    yb = y - h / 2
    # the cytoplasmic headpiece hangs below the right half, leaving the left half free for arrows
    doms = [("A", (x + width * 0.3, yb - 0.36), 0.62, 0.55), ("P", (x + width * 0.72, yb - 0.5), 0.7, 0.55),
            ("N", (x + width * 0.62, yb - 1.08), 0.72, 0.6)]
    for name, c, w, hh in doms:
        b = smooth_closed(np.array([(-w / 2, 0), (-w * 0.35, hh * 0.45), (0, hh / 2), (w * 0.4, hh * 0.4), (w / 2, 0),
                                    (w * 0.35, -hh * 0.45), (0, -hh / 2), (-w * 0.4, -hh * 0.4)]) + c)
        ax.add_patch(PathPatch(Path(b, closed=True), facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE * 0.8, zorder=zorder - 0.2))
        label(ax, c, name, size="tiny", color=P.on_fill(), bold=True, zorder=zorder + 0.5)
    if text:
        label(ax, (x, y + h / 2 + 0.3), text, size="small", bold=True)
    return np.array([x + width * 0.98, yb - 1.1])


def flux(ax, x, y_from, y_to, species=(), spacing=0.5, kind="process", color=None, offset=0.0, zorder=16, bg=None):
    """A vertical transport arrow from y_from to y_to at x, with particles drawn beside its start.

    ``species`` = [("na", 3), ("glucose", 1)] — an ion kind (ca, na, k, cl, h, mg) or a
    ("molecule", token, text) tuple, with a count; particles sit beside the tail of the arrow.
    """
    arrow(ax, (x + offset, y_from), (x + offset, y_to), kind=kind, color=color, zorder=zorder, bg=bg)
    s = np.sign(y_to - y_from)
    k = 0
    for item, count in species:
        for _ in range(count):
            py = y_from - s * 0.15 + s * 0.0
            px = x + offset + 0.32 + 0.42 * k
            if isinstance(item, tuple):
                molecule(ax, (px, py), token=item[1], text=item[2], r=0.18, zorder=zorder + 1)
            else:
                ion(ax, (px, py), item, r=0.15, text=False, zorder=zorder + 1)
            k += 1


def cycle_wheel(ax, center, r, phases, width=0.9, start=90.0, gap=1.2, size="normal", zorder=8):
    """A ring of phases going clockwise from ``start`` (degrees).

    ``phases`` = [(name, fraction, token), …] (fractions sum to 1). Returns {name: (a0, a1)} with
    each segment's start and end angle, for placing checkpoints and labels.
    """
    out = {}
    a = start
    for name, frac, token in phases:
        a1 = a - 360 * frac
        ax.add_patch(Wedge(center, r + width / 2, a1 + gap / 2, a - gap / 2, width=width, facecolor=P.fill(token),
                           edgecolor=P.edge(token), lw=LINE * 0.9, zorder=zorder))
        mid = math.radians((a + a1) / 2)
        label(ax, (center[0] + r * math.cos(mid), center[1] + r * math.sin(mid)), name, size=size, bold=True,
              color=P.on_fill(), zorder=zorder + 1)
        out[name] = (a, a1)
        a = a1
    # direction arrowhead at the outer rim
    return out


def checkpoint(ax, center, r, angle, width=0.9, text=None, text_r=None, color=None, size="small", ha=None, text_xy=None):
    """A checkpoint bar across the ring at ``angle`` (degrees) with an optional label outside
    (at radius ``text_r``, or at ``text_xy`` joined by a thin leader)."""
    c = color or P.edge("negative")
    th = math.radians(angle)
    u = np.array([math.cos(th), math.sin(th)])
    a, b = np.asarray(center) + u * (r - width / 2 - 0.12), np.asarray(center) + u * (r + width / 2 + 0.12)
    ax.plot(*np.array([a, b]).T, color=c, lw=LINE * 3.0, solid_capstyle="round", zorder=20)
    if text and text_xy is not None:
        ax.plot([b[0], text_xy[0]], [b[1], text_xy[1]], color=c, lw=0.7, zorder=19)
        h = ha or ("left" if text_xy[0] > b[0] + 0.05 else "right" if text_xy[0] < b[0] - 0.05 else "center")
        off = 0.08 if h == "left" else -0.08 if h == "right" else 0.0
        label(ax, (text_xy[0] + off, text_xy[1]), text, size=size, ha=h, color=c, bold=True)
    elif text:
        t = np.asarray(center) + u * (text_r or r + width / 2 + 0.45)
        h = ha or ("left" if u[0] > 0.2 else "right" if u[0] < -0.2 else "center")
        label(ax, t, text, size=size, ha=h, color=c, bold=True)
