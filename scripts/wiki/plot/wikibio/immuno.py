"""Immunology parts: MHC class I and II with peptide, T-cell receptor, CD3, CD4, CD8, B-cell receptor,
cytokines and immune cells, drawn natively as domain diagrams (each Ig-like domain a rounded block).

Membrane molecules are anchored at a point (x, y) of a horizontal membrane and grow towards
``up=+1`` (above the membrane) or ``up=-1`` (below), so the two sides of an immunological synapse
can be drawn facing each other:

    a = immuno.mhc_i(ax, 6, 3.0)                    # on the APC membrane, pointing up
    b = immuno.tcr(ax, 6, 6.2, up=-1)               # on the T-cell membrane, pointing down
    immuno.cd8(ax, 7.2, 6.2, up=-1, reach=a["alpha3"][1])

Each function returns a dict of anchors (``top``: the distal tip; ``alpha3`` / ``beta2``: the
membrane-proximal domains that CD8 / CD4 bind). Pairings follow biology: MHC I presents a short
(8–10 residue) peptide in a groove closed at both ends and is bound by CD8 at its α3 domain; MHC II
presents a longer (13–25 residue) peptide in an open groove and is bound by CD4 (domain D1) at its β2
domain. ``immune_cell`` draws native cell glyphs (lymphocyte, plasma cell, memory cell, dendritic cell).

The default domain height ``H`` is 0.62 canvas units; pass ``h`` to scale a molecule.
"""

import math

import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch, PathPatch, Polygon
from matplotlib.path import Path

from . import palette as P
from .core import LINE, blob, label

H = 0.62
TM = 0.14  # half-length of a transmembrane segment beyond the anchor height

# default colours (palette tokens)
TOKENS = {k: k for k in ("mhc", "b2m", "mhc_b", "tcr_a", "tcr_b", "cd3", "cd8", "cd4", "peptide")}  # palette aliases


def domain(ax, center, w, h, token, text=None, size="tiny", groove=0.0, zorder=12, angle=0.0):
    """An Ig-like domain as a rounded block. ``groove`` > 0 cuts a concave notch of that depth into the top
    (as in the peptide-binding platform of MHC). Returns the block's (bottom, top) centre points."""
    x, y = center
    r = min(w, h) * 0.32
    x0, x1, y0, y1 = x - w / 2, x + w / 2, y - h / 2, y + h / 2
    t = np.linspace(0, math.pi / 2, 8)
    pts = []
    pts += list(np.c_[x1 - r + r * np.cos(-math.pi / 2 + t), y0 + r + r * np.sin(-math.pi / 2 + t)])
    pts += list(np.c_[x1 - r + r * np.cos(t), y1 - r + r * np.sin(t)])
    if groove > 0:
        g = np.linspace(0, math.pi, 14)
        gw = w * 0.42
        pts += list(np.c_[x + gw / 2 * np.cos(g), y1 - groove * np.sin(g)])
    pts += list(np.c_[x0 + r + r * np.cos(math.pi / 2 + t), y1 - r + r * np.sin(math.pi / 2 + t)])
    pts += list(np.c_[x0 + r + r * np.cos(math.pi + t), y0 + r + r * np.sin(math.pi + t)])
    pts = np.array(pts)
    if angle:
        c, s = math.cos(math.radians(angle)), math.sin(math.radians(angle))
        pts = (pts - center) @ np.array([[c, s], [-s, c]]) + center
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE * 0.8,
                         joinstyle="round", zorder=zorder))
    if text:
        label(ax, center, text, size=size, color=P.on_fill(), zorder=zorder + 1)
    return (x, y0), (x, y1)


def _flip(y0, dy, up):
    return y0 + up * dy


def _tm(ax, x, y, up, token, width=0.09, tail=0.25, zorder=11):
    """A transmembrane helix crossing the membrane at (x, y), with a short cytoplasmic tail."""
    ax.add_patch(FancyBboxPatch((x - width / 2, y - TM), width, 2 * TM, boxstyle="round,pad=0,rounding_size=0.03",
                                facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE * 0.6, zorder=zorder))
    ax.plot([x, x], [y - up * TM, y - up * (TM + tail)], color=P.edge(token), lw=LINE * 1.2, solid_capstyle="round",
            zorder=zorder)


def peptide(ax, a, b, n=None, token=None, r=0.06, zorder=15):
    """A peptide as a chain of residue beads from a to b."""
    tok = token or TOKENS["peptide"]
    a, b = np.asarray(a, float), np.asarray(b, float)
    n = n or max(3, int(np.linalg.norm(b - a) / (r * 1.8)) + 1)
    pts = np.linspace(a, b, n)
    ax.plot(pts[:, 0], pts[:, 1], color=P.edge(tok), lw=0.8, zorder=zorder)
    for p in pts:
        ax.add_patch(Circle(p, r, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.6, zorder=zorder + 0.5))


def mhc_i(ax, x, y, up=1, h=H, peptide_on=True, labels=True, token=None, b2m_token=None, zorder=12):
    """MHC class I: heavy chain (α1, α2 platform; α3 next to the membrane; transmembrane segment) with
    non-covalent β2-microglobulin beside α3, and a short peptide closed in the groove."""
    tok, tb = token or TOKENS["mhc"], b2m_token or TOKENS["b2m"]
    w = h * 0.95
    _tm(ax, x, y, up, tok)
    ya3 = _flip(y, TM + h / 2, up)
    domain(ax, (x, ya3), w, h, tok, "α3" if labels else None, zorder=zorder)
    domain(ax, (x + w * 1.02, ya3), w * 0.9, h * 0.85, tb, "β2m" if labels else None, zorder=zorder)
    yp = _flip(y, TM + h * 1.5 + 0.03, up)
    for k, name in ((0, "α1"), (1, "α2")):
        cx = x + (k - 0.5) * w * 1.02 + w * 0.5
        domain(ax, (cx, yp), w, h, tok, name if labels else None, zorder=zorder, angle=0 if up > 0 else 180)
    top = _flip(y, TM + 2 * h + 0.03, up)
    if peptide_on:
        peptide(ax, (x + w * 0.05, top), (x + w * 0.95, top), n=8)  # 8-10 residues, ends buried
    return {"top": (x + w / 2, top), "alpha3": (x - w / 2, ya3), "center_x": x + w / 2}


def mhc_ii(ax, x, y, up=1, h=H, peptide_on=True, labels=True, token=None, beta_token=None, zorder=12):
    """MHC class II: α chain (α1, α2) and β chain (β1, β2), each with a transmembrane segment; the α1β1 platform
    holds a longer peptide whose ends overhang the open groove. Returns anchors incl. ``beta2``."""
    ta, tb = token or TOKENS["mhc"], beta_token or TOKENS["mhc_b"]
    w = h * 0.95
    xa, xb = x - w * 0.51, x + w * 0.51
    for xx, tk in ((xa, ta), (xb, tb)):
        _tm(ax, xx, y, up, tk)
    y2 = _flip(y, TM + h / 2, up)
    domain(ax, (xa, y2), w, h, ta, "α2" if labels else None, zorder=zorder)
    domain(ax, (xb, y2), w, h, tb, "β2" if labels else None, zorder=zorder)
    y1 = _flip(y, TM + h * 1.5 + 0.03, up)
    domain(ax, (xa, y1), w, h, ta, "α1" if labels else None, zorder=zorder, angle=0 if up > 0 else 180)
    domain(ax, (xb, y1), w, h, tb, "β1" if labels else None, zorder=zorder, angle=0 if up > 0 else 180)
    top = _flip(y, TM + 2 * h + 0.03, up)
    if peptide_on:
        peptide(ax, (xa - w * 0.62, top), (xb + w * 0.62, top), n=15)  # 13-25 residues, open ends
    return {"top": (x, top), "beta2": (xb + w / 2, y2), "alpha2": (xa - w / 2, y2), "center_x": x}


def tcr(ax, x, y, up=-1, h=H, labels=True, cd3=True, cd3_side="both", zorder=12):
    """The αβ T-cell receptor: α and β chains, each with a constant (C) domain next to the membrane and a
    variable (V) domain whose CDR loops contact the peptide–MHC. ``cd3=True`` adds the CD3 εγ / εδ
    dimers and the ζζ tails that signal; ``cd3_side`` ("both", "left", "right") places the two CD3 dimers
    on both sides or together on one side (to leave room for a co-receptor). Returns ``top``."""
    ta, tb = TOKENS["tcr_a"], TOKENS["tcr_b"]
    w = h * 0.9
    xa, xb = x - w * 0.51, x + w * 0.51
    for xx, tk in ((xa, ta), (xb, tb)):
        _tm(ax, xx, y, up, tk)
    yc = _flip(y, TM + h / 2, up)
    domain(ax, (xa, yc), w, h, ta, "Cα" if labels else None, zorder=zorder)
    domain(ax, (xb, yc), w, h, tb, "Cβ" if labels else None, zorder=zorder)
    yv = _flip(y, TM + h * 1.5 + 0.03, up)
    domain(ax, (xa, yv), w, h, ta, "Vα" if labels else None, zorder=zorder)
    domain(ax, (xb, yv), w, h, tb, "Vβ" if labels else None, zorder=zorder)
    if cd3:
        tc = TOKENS["cd3"]
        slots = {"both": [(-1, 0), (-1, 1), (1, 0), (1, 1)], "left": [(-1, k) for k in range(4)],
                 "right": [(1, k) for k in range(4)]}[cd3_side]
        for side, k in slots:
            cx = x + side * (w * 1.3 + k * w * 0.62)
            _tm(ax, cx, y, up, tc, width=0.07, tail=0.2)
            domain(ax, (cx, _flip(y, TM + h * 0.33, up)), w * 0.58, h * 0.62, tc, None, zorder=zorder - 1)
        for dx in (-0.07, 0.07):
            ax.plot([x + dx, x + dx], [y - up * TM * 0.5, y - up * (TM + 0.55)], color=P.edge(tc), lw=LINE * 1.3,
                    zorder=zorder - 1)
        if labels:
            sx = 1 if cd3_side == "right" else -1
            far = max(k for _, k in slots)
            label(ax, (x + sx * (w * 1.3 + far * w * 0.31), _flip(y, TM + h * 0.33 + h * 0.62, up)), "CD3", size="tiny",
                  color=P.muted())
    return {"top": (x, _flip(y, TM + 2 * h + 0.03, up)), "center_x": x}


def cd8(ax, x, y, up=-1, reach=None, h=H, labels=True, label_side=1, zorder=12):
    """The CD8αβ co-receptor: two Ig-like heads on long stalks; ``reach`` is the height of the heads' centre
    (set it to the α3 domain of the MHC I it binds). ``label_side`` −1 writes "CD8" on the left."""
    tok = TOKENS["cd8"]
    w = h * 0.78
    yr = reach if reach is not None else _flip(y, TM + 1.6 * h, up)
    for k, xx in enumerate((x - w * 0.52, x + w * 0.52)):
        _tm(ax, xx, y, up, tok, width=0.07)
        ax.plot([xx, xx], [y + up * TM, yr - up * h * 0.4], color=P.edge(tok), lw=LINE * 1.4, zorder=zorder - 1)
        domain(ax, (xx, yr), w, h * 0.8, tok, ("α", "β")[k] if labels else None, zorder=zorder)
    if labels:
        label(ax, (x + label_side * w * 1.15, (y + yr) / 2), "CD8", size="small", ha="left" if label_side > 0 else "right")
    return {"head": (x, yr)}


def cd4(ax, x, y, up=-1, reach=None, h=H, labels=True, zorder=12):
    """CD4: four Ig-like domains D1–D4 in a row from the membrane (D4) to the tip (D1), which binds the β2
    domain of MHC II at height ``reach``."""
    tok = TOKENS["cd4"]
    w = h * 0.78
    _tm(ax, x, y, up, tok, width=0.08)
    end = reach if reach is not None else _flip(y, TM + 4 * h * 0.8, up)
    start = y + up * TM
    n = 4
    step = (end - start) / n
    for k in range(n):
        cy = start + step * (k + 0.5)
        domain(ax, (x, cy), w, abs(step) * 0.94, tok, f"D{4 - k}" if labels else None, zorder=zorder)
    if labels:
        label(ax, (x + w * 0.75, start + step * 2), "CD4", size="small", ha="left")
    return {"head": (x, start + step * (n - 0.5))}


def bcr(ax, x, y, up=1, size=1.0, token="antibody", zorder=12):
    """A membrane-bound antibody (B-cell receptor) anchored at (x, y)."""
    from .structures import antibody

    _tm(ax, x, y, up, token, width=0.09)
    antibody(ax, (x, y + up * (TM + 0.55 * size)), size=size, angle=0 if up > 0 else 180, token=token, zorder=zorder)


def cytokine(ax, center, token="drug", r=0.12, zorder=13):
    """A cytokine (small secreted protein) as a disc with a highlight."""
    ax.add_patch(Circle(center, r, facecolor=P.fill(token), edgecolor=P.edge(token), lw=0.7, zorder=zorder))
    ax.add_patch(Circle((center[0] - r * 0.3, center[1] + r * 0.3), r * 0.3, facecolor=P.light(token), edgecolor="none",
                        zorder=zorder + 0.5))


def immune_cell(ax, center, r=0.6, kind="lymphocyte", token="neutral", receptor_token=None, receptors=0, seed=0,
                text=None, size="tiny", zorder=10):
    """A native immune-cell glyph: ``kind`` lymphocyte (large nucleus, thin cytoplasm), plasma (eccentric
    nucleus, abundant rough ER), memory (lymphocyte with a double outline), dendritic (stellate processes).
    ``receptors`` draws that many small Y-shaped receptors around the surface in ``receptor_token``."""
    x, y = center
    rng = np.random.default_rng(seed)
    if kind == "dendritic":
        th = np.linspace(0, 2 * math.pi, 9, endpoint=False) + 0.3
        pts = []
        for a in th:
            pts.append((x + r * 0.62 * math.cos(a - 0.35), y + r * 0.62 * math.sin(a - 0.35)))
            pts.append((x + r * 1.35 * math.cos(a), y + r * 1.35 * math.sin(a)))
        from .core import smooth_closed

        o = smooth_closed(pts)
    elif kind == "plasma":
        o = blob(center, r * 1.15, r * 0.85, wobble=0.04, seed=seed + 3, k=8)
    else:
        o = blob(center, r, r * 0.95, wobble=0.05, seed=seed + 5, k=8)
    ax.add_patch(PathPatch(Path(o, closed=True), facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE, zorder=zorder))
    if kind == "memory":
        o2 = blob(center, r * 1.12, r * 1.07, wobble=0.05, seed=seed + 5, k=8)
        ax.add_patch(PathPatch(Path(o2, closed=True), fill=False, edgecolor=P.edge(token), lw=LINE * 0.7, zorder=zorder))
    if kind == "plasma":
        for k in range(4):
            yy = y - r * 0.45 + k * r * 0.3
            xs = np.linspace(x - r * 0.95, x + r * 0.05, 30)
            ax.plot(xs, yy + 0.04 * r * np.sin(xs * 18), color=P.edge("er"), lw=0.9, zorder=zorder + 0.5)
        nc, nr = (x + r * 0.5, y + r * 0.05), r * 0.42
    elif kind == "dendritic":
        nc, nr = (x, y), r * 0.42
    else:
        nc, nr = (x + r * 0.08, y - r * 0.04), r * 0.7
    ax.add_patch(Circle(nc, nr, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=LINE * 0.7, zorder=zorder + 1))
    if receptors and receptor_token:
        for k in range(receptors):
            a = 2 * math.pi * (k + 0.25) / receptors + rng.uniform(-0.1, 0.1)
            base = np.array([x + r * math.cos(a), y + r * math.sin(a)])
            u = np.array([math.cos(a), math.sin(a)])
            n = np.array([-u[1], u[0]])
            stem = base + u * r * 0.22
            c = P.edge(receptor_token)
            ax.plot(*np.array([base, stem]).T, color=c, lw=1.3, zorder=zorder + 2, solid_capstyle="round")
            for s in (-1, 1):
                ax.plot(*np.array([stem, stem + u * r * 0.16 + n * s * r * 0.13]).T, color=c, lw=1.3, zorder=zorder + 2,
                        solid_capstyle="round")
    if text:
        label(ax, (x, y - r * 1.25 - 0.1), text, size=size, va="top")
    return o


__all__ = ["domain", "peptide", "mhc_i", "mhc_ii", "tcr", "cd8", "cd4", "bcr", "cytokine", "immune_cell", "TOKENS", "H"]
