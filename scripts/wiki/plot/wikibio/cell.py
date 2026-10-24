"""Membranes, cells and organelles, drawn natively in the palette's soft style.

    bilayer(ax, [(0, 2), (10, 2)])            a lipid bilayer along any polyline (detailed heads + tails)
    membrane(ax, outline, "cytoplasm")         a cell-scale membrane: filled region + double contour
    cell(ax, (5, 4), 4, 3, kind="animal")      a whole cell outline (animal, plant, bacterium)
    nucleus / mitochondrion / er / golgi / vesicle / lysosome / chloroplast / vacuole
"""

import math

import numpy as np
from matplotlib.patches import Circle, Ellipse, PathPatch
from matplotlib.path import Path

from . import palette as P
from .core import LINE, blob, polyline, smooth_closed


def bilayer(ax, points, spacing=0.22, head=0.085, tail=0.26, gap=0.04, closed=False, zorder=6):
    """A phospholipid bilayer along a polyline: two leaflets of heads (circles) with paired tails.

    The bilayer is centred on the line; it is 2*(tail + head) thick. Use for zoomed-in views
    (transport, signalling); for whole cells use ``membrane``.
    """
    pts = np.asarray(points, float)
    if closed:
        pts = np.vstack([pts, pts[:1]])
    q, nrm, length = polyline(pts, n=max(20, int(np.hypot(*np.diff(pts, axis=0).T).sum() / spacing) + 1))
    hc, he, tc = P.fill("lipid_head"), P.edge("lipid_head"), P.edge("lipid_tail")
    off = gap / 2 + tail
    for p, n in zip(q, nrm):
        for side in (1, -1):
            h = p + side * n * (off + head)
            for dx in (-0.035, 0.035):
                t = np.array([-n[1], n[0]]) * dx
                a, b = p + side * n * (gap / 2) + t, p + side * n * off + t
                ax.plot([a[0], b[0]], [a[1], b[1]], color=tc, lw=0.8, solid_capstyle="round", zorder=zorder)
            ax.add_patch(Circle(h, head, facecolor=hc, edgecolor=he, lw=0.55, zorder=zorder + 1))
    return q, nrm


def membrane(ax, outline, inside="cytoplasm", thickness=0.12, token="membrane", zorder=3):
    """A cell-scale membrane: the enclosed region filled with ``inside`` and a two-line contour."""
    o = np.asarray(outline, float)
    ax.add_patch(PathPatch(Path(o, closed=True), facecolor=P.fill(inside), edgecolor="none", zorder=zorder))
    q, nrm, _ = polyline(o, n=max(len(o), 200), closed=True)
    outer, inner = q + nrm * thickness / 2, q - nrm * thickness / 2
    # the band is a ring: outer contour plus reversed inner contour as one compound path (no seam)
    verts = np.vstack([outer, inner[::-1]])
    codes = [Path.MOVETO] + [Path.LINETO] * (len(outer) - 2) + [Path.CLOSEPOLY] + [Path.MOVETO] + [Path.LINETO] * (len(inner) - 2) + [Path.CLOSEPOLY]
    ax.add_patch(PathPatch(Path(verts, codes), facecolor=P.fill(token), edgecolor="none", zorder=zorder + 1))
    for line in (outer, inner):
        ax.plot(line[:, 0], line[:, 1], color=P.edge(token), lw=LINE * 0.8, zorder=zorder + 2, solid_joinstyle="round")


def cell(ax, center, rx, ry, kind="animal", seed=1, zorder=2):
    """A whole cell: ``kind`` animal (rounded, wobbly), plant (polygonal with wall and vacuole), bacterium (rod)."""
    x, y = center
    if kind == "animal":
        o = blob(center, rx, ry, wobble=0.06, seed=seed, k=11)
        membrane(ax, o, "cytoplasm", zorder=zorder)
        return o
    if kind == "plant":
        k = 8
        rng = np.random.default_rng(seed)
        th = np.linspace(0, 2 * np.pi, k, endpoint=False) + rng.uniform(-0.12, 0.12, k)
        corners = np.c_[x + rx * np.cos(th), y + ry * np.sin(th)]
        wall = _rounded_polygon(corners, 0.25)
        ax.add_patch(PathPatch(Path(wall, closed=True), facecolor=P.fill("cell_wall"), edgecolor=P.edge("cell_wall"), lw=LINE, zorder=zorder))
        inner = _rounded_polygon(np.array([x, y]) + (corners - [x, y]) * 0.9, 0.3)
        membrane(ax, inner, "cytoplasm", thickness=0.08, zorder=zorder + 1)
        vac = blob((x + rx * 0.08, y - ry * 0.05), rx * 0.55, ry * 0.5, wobble=0.07, seed=seed + 7, k=9)
        ax.add_patch(PathPatch(Path(vac, closed=True), facecolor=P.fill("vacuole"), edgecolor=P.edge("vacuole"), lw=LINE * 0.8, zorder=zorder + 4))
        return inner
    if kind == "bacterium":
        o = _capsule(center, rx, ry)
        ax.add_patch(PathPatch(Path(_capsule(center, rx + 0.12, ry + 0.12), closed=True), facecolor=P.fill("bacterium"),
                               edgecolor=P.edge("bacterium"), lw=LINE, zorder=zorder))
        membrane(ax, o, "cytoplasm", thickness=0.07, zorder=zorder + 1)
        return o
    raise ValueError(f"unknown cell kind {kind!r}")


def _capsule(center, rx, ry, n=120):
    x, y = center
    r = ry
    L = max(rx - r, 0)
    top = np.c_[np.linspace(x - L, x + L, n // 4), np.full(n // 4, y + r)]
    t = np.linspace(np.pi / 2, -np.pi / 2, n // 4)
    right = np.c_[x + L + r * np.cos(t), y + r * np.sin(t)]
    bottom = np.c_[np.linspace(x + L, x - L, n // 4), np.full(n // 4, y - r)]
    t2 = np.linspace(-np.pi / 2, -3 * np.pi / 2, n // 4)
    left = np.c_[x - L + r * np.cos(t2), y + r * np.sin(t2)]
    return np.vstack([top, right, bottom, left])


def _rounded_polygon(corners, r, n=8):
    c = np.asarray(corners, float)
    out = []
    for i in range(len(c)):
        p0, p1, p2 = c[i - 1], c[i], c[(i + 1) % len(c)]
        a = p1 + (p0 - p1) / np.linalg.norm(p0 - p1) * r
        b = p1 + (p2 - p1) / np.linalg.norm(p2 - p1) * r
        for t in np.linspace(0, 1, n):
            out.append((1 - t) ** 2 * a + 2 * (1 - t) * t * p1 + t**2 * b)
    return np.array(out)


def nucleus(ax, center, r, pores=10, nucleolus=True, chromatin=True, seed=3, zorder=8):
    """A nucleus: double nuclear envelope with pores, chromatin speckles and a nucleolus."""
    x, y = center
    o = blob(center, r, r * 0.9, wobble=0.04, seed=seed, k=9)
    ax.add_patch(PathPatch(Path(o, closed=True), facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=LINE * 1.6, zorder=zorder))
    q, nrm, _ = polyline(o, n=max(len(o), 200), closed=True)
    inward = nrm if _ccw(o) else -nrm
    inner = q + inward * 0.09
    ax.plot(inner[:, 0], inner[:, 1], color=P.edge("nucleus"), lw=LINE * 0.7, zorder=zorder + 1)
    for i in np.linspace(0, len(q) - 1, pores, endpoint=False).astype(int):
        ax.add_patch(Circle(q[i] + inward[i] * 0.045, 0.055, facecolor=P.fill("nucleus"), edgecolor="none", zorder=zorder + 2))
    rng = np.random.default_rng(seed)
    if chromatin:
        for _ in range(int(28 * r)):
            a, d = rng.uniform(0, 2 * np.pi), r * 0.75 * math.sqrt(rng.uniform(0.05, 1))
            ax.add_patch(Circle((x + d * math.cos(a), y + 0.9 * d * math.sin(a)), rng.uniform(0.025, 0.06),
                                color=P.fill("chromatin"), alpha=0.7, lw=0, zorder=zorder + 1))
    if nucleolus:
        nl = blob((x + r * 0.22, y + r * 0.15), r * 0.26, r * 0.22, wobble=0.1, seed=seed + 1, k=7)
        ax.add_patch(PathPatch(Path(nl, closed=True), facecolor=P.fill("nucleolus"), edgecolor=P.edge("nucleolus"), lw=LINE * 0.7, zorder=zorder + 2))
    return o


def mitochondrion(ax, center, length, width, angle=0.0, cristae=6, zorder=8):
    """A mitochondrion: outer membrane, and an inner membrane folded into finger-like cristae around the matrix."""
    o = _transform(_capsule((0, 0), length / 2, width / 2), center, angle)
    ax.add_patch(PathPatch(Path(o, closed=True), facecolor=P.fill("mitochondrion"), edgecolor=P.edge("mitochondrion"), lw=LINE * 1.1, zorder=zorder))
    inner = _capsule((0, 0), length / 2 - 0.09, width / 2 - 0.09, n=400)
    # push the inner membrane inward in alternating fingers along the top and bottom edges
    L = length / 2 - width / 2
    depth = (width - 0.18) * 0.62
    folded = inner.copy()
    xs = np.linspace(-L * 0.95, L * 0.95, cristae)
    for i, xx in enumerate(xs):
        top = i % 2 == 0
        sel = (np.abs(inner[:, 0] - xx) < 0.09) & ((inner[:, 1] > 0) if top else (inner[:, 1] < 0))
        prof = np.cos((inner[sel, 0] - xx) / 0.09 * np.pi / 2) ** 2
        folded[sel, 1] -= np.sign(inner[sel, 1]) * depth * prof
    ax.add_patch(PathPatch(Path(_transform(folded, center, angle), closed=True), facecolor=P.fill("matrix"),
                           edgecolor=P.edge("mitochondrion"), lw=LINE * 0.75, zorder=zorder + 1, joinstyle="round"))
    return o


def er(ax, center, width, height, sheets=4, angle=0.0, zorder=7):
    """Rough endoplasmic reticulum: stacked wavy cisternae with ribosome dots."""
    for i in range(sheets):
        y = -height / 2 + (i + 0.5) * height / sheets
        x = np.linspace(-width / 2, width / 2, 80)
        mid = y + 0.08 * np.sin(x * 2.2 + i)
        th = 0.09
        sheet = np.c_[np.r_[x, x[::-1]], np.r_[mid + th, (mid - th)[::-1]]]
        ax.add_patch(PathPatch(Path(_transform(sheet, center, angle), closed=True), facecolor=P.fill("er"), edgecolor=P.edge("er"),
                               lw=LINE * 0.7, zorder=zorder, joinstyle="round"))
        for xx in x[::7]:
            yy = y + 0.08 * np.sin(xx * 2.2 + i) + th + 0.05
            ax.add_patch(Circle(_transform(np.array([[xx, yy]]), center, angle)[0], 0.035, color=P.edge("er"), lw=0, zorder=zorder + 1))


def golgi(ax, center, width, cisternae=5, curve=0.35, angle=0.0, zorder=7):
    """A Golgi stack: curved cisternae with budding vesicles at the trans face."""
    for i in range(cisternae):
        w = width * (1 - 0.08 * abs(i - cisternae / 2))
        x = np.linspace(-w / 2, w / 2, 60)
        y = i * 0.24 - curve * (1 - (2 * x / w) ** 2)
        th = 0.07
        c = np.c_[np.r_[x, x[::-1]], np.r_[y + th, (y - th)[::-1]]]
        ax.add_patch(PathPatch(Path(_transform(c, center, angle), closed=True), facecolor=P.fill("golgi"), edgecolor=P.edge("golgi"),
                               lw=LINE * 0.7, zorder=zorder, joinstyle="round"))
    for j, xx in enumerate((-0.45, 0.0, 0.45)):
        p = _transform(np.array([[xx * width, cisternae * 0.24 + 0.08]]), center, angle)[0]
        vesicle(ax, p, 0.1, zorder=zorder)


def vesicle(ax, center, r, token="vesicle", cargo=None, zorder=8):
    """A vesicle (lysosome, endosome…): membrane circle; ``cargo`` token adds content dots."""
    ax.add_patch(Circle(center, r, facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE * 0.9, zorder=zorder))
    if cargo:
        rng = np.random.default_rng(int(center[0] * 100 + center[1] * 7) % 997)
        for _ in range(max(2, int(r * 14))):
            a, d = rng.uniform(0, 2 * np.pi), r * 0.6 * math.sqrt(rng.uniform())
            ax.add_patch(Circle((center[0] + d * math.cos(a), center[1] + d * math.sin(a)), r * 0.12, color=P.edge(cargo), alpha=0.8, lw=0, zorder=zorder + 1))


def lysosome(ax, center, r, zorder=8):
    vesicle(ax, center, r, token="lysosome", cargo="#c76a93", zorder=zorder)


def chloroplast(ax, center, length, width, angle=0.0, grana=4, zorder=8):
    """A chloroplast: envelope, stroma, and grana stacks of thylakoids joined by lamellae."""
    o = _transform(_ellipse(length / 2, width / 2), center, angle)
    ax.add_patch(PathPatch(Path(o, closed=True), facecolor=P.fill("chloroplast"), edgecolor=P.edge("chloroplast"), lw=LINE * 1.2, zorder=zorder))
    xs = np.linspace(-length * 0.32, length * 0.32, grana)
    ax.plot(*_transform(np.c_[xs, np.zeros_like(xs)], center, angle).T, color=P.edge("thylakoid"), lw=LINE * 0.8, zorder=zorder + 1)
    for xx in xs:
        for k in range(4):
            yy = (k - 1.5) * 0.085
            disc = _ellipse(0.16, 0.035, n=30) + [xx, yy]
            ax.add_patch(PathPatch(Path(_transform(disc, center, angle), closed=True), facecolor=P.fill("thylakoid"),
                                   edgecolor=P.edge("thylakoid"), lw=0.5, zorder=zorder + 2))


def vacuole(ax, center, rx, ry, seed=5, zorder=6):
    o = blob(center, rx, ry, wobble=0.07, seed=seed, k=9)
    ax.add_patch(PathPatch(Path(o, closed=True), facecolor=P.fill("vacuole"), edgecolor=P.edge("vacuole"), lw=LINE * 0.8, zorder=zorder))


def _ccw(pts):
    p = np.asarray(pts, float)
    return 0.5 * np.sum(p[:-1, 0] * p[1:, 1] - p[1:, 0] * p[:-1, 1]) > 0


def _ellipse(rx, ry, n=100):
    t = np.linspace(0, 2 * np.pi, n)
    return np.c_[rx * np.cos(t), ry * np.sin(t)]


def _transform(pts, center, angle):
    c, s = math.cos(math.radians(angle)), math.sin(math.radians(angle))
    return np.asarray(pts, float) @ np.array([[c, s], [-s, c]]) + np.asarray(center, float)
