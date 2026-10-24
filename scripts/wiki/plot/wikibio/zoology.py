"""Zoology: animal body plans in cross-section, coloured by germ layer.

    from wikibio import zoology as zoo
    a = zoo.body_plan(ax, (4, 5), 2.2, "coelomate")       diploblast / acoelomate / pseudocoelomate / coelomate
    zoo.germ_layer_legend(ax, (1, 0.6))

Germ layers keep one colour in every figure (the embryology convention): ectoderm blue, mesoderm red,
endoderm yellow (``GERM``); mesoglea is a neutral jelly. Body cavities are pale washes: the gut lumen
neutral, the pseudocoel (a persistent blastocoel, not lined by mesoderm) lilac, the coelom (lined by
mesoderm on both sides) green. ``body_plan`` returns anchors for labels: the centre, a point in each
layer and cavity, and the outline radius.
"""

import numpy as np
from matplotlib.patches import PathPatch
from matplotlib.path import Path

from . import palette as P
from .core import LINE, label

# germ layer / cavity -> palette token (proposed dedicated tokens are listed in the gallery report)
GERM = {k: k for k in ("ectoderm", "mesoderm", "endoderm", "mesoglea")}  # palette aliases
CAVITY = {"gut": "neutral", "pseudocoel": "pseudocoel", "coelom": "coelom"}


def _wash(token, light=0.55, dark=0.78):
    return P.mix(P.fill(token), P.surface(), dark if P.is_dark() else light)


def _ellipse(c, rx, ry, n=160, reverse=False):
    t = np.linspace(0, 2 * np.pi, n)
    if reverse:
        t = t[::-1]
    return np.c_[c[0] + rx * np.cos(t), c[1] + ry * np.sin(t)]


def _ring(ax, c, r_out, r_in, aspect, face, edge, lw=LINE * 0.8, zorder=5):
    """An annulus between two concentric ellipses (r_in = 0: a full disc)."""
    outer = _ellipse(c, r_out, r_out * aspect)
    verts, codes = [outer], [Path.MOVETO] + [Path.LINETO] * (len(outer) - 2) + [Path.CLOSEPOLY]
    if r_in > 0:
        inner = _ellipse(c, r_in, r_in * aspect, reverse=True)
        verts.append(inner)
        codes += [Path.MOVETO] + [Path.LINETO] * (len(inner) - 2) + [Path.CLOSEPOLY]
    ax.add_patch(PathPatch(Path(np.vstack(verts), codes), facecolor=face, edgecolor=edge, lw=lw, zorder=zorder))


def _layer(ax, c, r_out, r_in, aspect, layer, zorder):
    tok = GERM[layer]
    _ring(ax, c, r_out, r_in, aspect, P.fill(tok), P.edge(tok), zorder=zorder)


def _space(ax, c, r_out, r_in, aspect, cavity, zorder):
    tok = CAVITY[cavity]
    _ring(ax, c, r_out, r_in, aspect, _wash(tok), P.edge(tok), lw=LINE * 0.5, zorder=zorder)


# radii as fractions of the outline radius, from the outside in: (name, kind, r_out, r_in)
PLANS = {
    "diploblast": [("ectoderm", "layer", 1.0, 0.8), ("mesoglea", "layer", 0.8, 0.7), ("endoderm", "layer", 0.7, 0.5),
                   ("gut", "space", 0.5, 0.0)],
    "acoelomate": [("ectoderm", "layer", 1.0, 0.86), ("mesoderm", "layer", 0.86, 0.42), ("endoderm", "layer", 0.42, 0.26),
                   ("gut", "space", 0.26, 0.0)],
    "pseudocoelomate": [("ectoderm", "layer", 1.0, 0.86), ("mesoderm", "layer", 0.86, 0.7), ("pseudocoel", "space", 0.7, 0.36),
                        ("endoderm", "layer", 0.36, 0.2), ("gut", "space", 0.2, 0.0)],
    "coelomate": [("ectoderm", "layer", 1.0, 0.87), ("mesoderm", "layer", 0.87, 0.74), ("coelom", "space", 0.74, 0.43),
                  ("mesoderm", "layer", 0.43, 0.35), ("endoderm", "layer", 0.35, 0.21), ("gut", "space", 0.21, 0.0)],
}


def body_plan(ax, center, r, kind="coelomate", aspect=None, cuticle=None, mesenteries=True, zorder=5):
    """A body cross-section of one grade of organization, layers coloured by germ layer.

    kind: "diploblast" (cnidarian: ectoderm, mesoglea, endoderm around the gastrovascular cavity),
    "acoelomate" (flatworm: mesoderm fills the space between gut and body wall; drawn flattened),
    "pseudocoelomate" (nematode: mesoderm lines only the body wall; the gut is endoderm alone; a cuticle),
    "coelomate" (annelid: mesoderm lines body wall and gut; the coelom is divided by dorsal and ventral mesenteries).

    Returns {"center", "r", "aspect", <layer or cavity name>: a point in the middle of it} (the coelomate's
    second mesoderm layer is "splanchnic", the first "somatic").
    """
    if kind not in PLANS:
        raise ValueError(f"unknown body plan {kind!r}")
    asp = aspect if aspect is not None else (0.62 if kind == "acoelomate" else 1.0)
    cut = cuticle if cuticle is not None else (kind == "pseudocoelomate")
    anchors = {"center": tuple(center), "r": r, "aspect": asp}
    seen = set()
    for z, (name, what, ro, ri) in enumerate(PLANS[kind]):
        (_layer if what == "layer" else _space)(ax, center, ro * r, ri * r, asp, name, zorder + z)
        key = name
        if kind == "coelomate" and name == "mesoderm":
            key = "splanchnic" if "mesoderm" in seen else "somatic"
            seen.add("mesoderm")
        rm = (ro + ri) / 2 * r
        anchors[key] = (center[0] + rm * 0.7071, center[1] + rm * asp * 0.7071) if ri > 0 else tuple(center)
    if kind == "coelomate" and mesenteries:
        # dorsal and ventral mesenteries: mesoderm strips joining splanchnic and somatic layers
        tok = GERM["mesoderm"]
        w = 0.05 * r
        for s in (1, -1):
            y0, y1 = 0.42 * r * s, 0.75 * r * s
            xs = [center[0] - w, center[0] + w, center[0] + w, center[0] - w]
            ys = [center[1] + y0, center[1] + y0, center[1] + y1, center[1] + y1]
            ax.fill(xs, ys, facecolor=P.fill(tok), edgecolor="none", zorder=zorder + 10)
            for dx in (-w, w):
                ax.plot([center[0] + dx] * 2, [center[1] + y0 + 0.01 * s, center[1] + y1 - 0.01 * s], color=P.edge(tok),
                        lw=LINE * 0.6, zorder=zorder + 11)
        anchors["mesentery"] = (center[0], center[1] + 0.6 * r)
        anchors["coelom"] = (center[0] + 0.585 * r * 0.7071, center[1] + 0.585 * r * 0.7071)
    if cut:
        o = _ellipse(center, r * 1.035, r * 1.035 * asp)
        ax.add_patch(PathPatch(Path(o, closed=True), fill=False, edgecolor=P.edge("neutral"), lw=LINE * 1.6, zorder=zorder + 12))
        anchors["cuticle"] = (center[0] - r * 1.035 * 0.7071, center[1] + r * 1.035 * asp * 0.7071)
    return anchors


def germ_layer_legend(ax, xy, items=("ectoderm", "mesoderm", "endoderm", "mesoglea"), cavities=(), step=3.0, size="small",
                      swatch=0.32):
    """A one-row key of germ-layer colours (and optionally cavity washes) starting at ``xy``."""
    x, y = xy
    names = {"ectoderm": "Ectoderm", "mesoderm": "Mesoderm", "endoderm": "Endoderm", "mesoglea": "Mesoglea",
             "gut": "Gut lumen", "pseudocoel": "Pseudocoel", "coelom": "Coelom"}
    for it in list(items) + list(cavities):
        if it in GERM:
            fc, ec = P.fill(GERM[it]), P.edge(GERM[it])
        else:
            fc, ec = _wash(CAVITY[it]), P.edge(CAVITY[it])
        ax.add_patch(PathPatch(Path(_ellipse((x + swatch / 2, y), swatch / 2, swatch / 2)), facecolor=fc, edgecolor=ec, lw=0.9,
                               zorder=20))
        label(ax, (x + swatch + 0.15, y), names.get(it, it), size=size, ha="left")
        x += step
    return x


__all__ = ["GERM", "CAVITY", "PLANS", "body_plan", "germ_layer_legend"]
