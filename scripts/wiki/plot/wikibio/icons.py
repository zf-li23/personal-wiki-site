"""Vector icons from open libraries (Servier Medical Art, DBCLS, PhyloPic, …), drawn as matplotlib paths.

Icons live in ``scripts/wiki/plot/icons/<source>/<name>.json`` (converted from SVG by ``scripts/icons.py``)
and are listed in ``icons/manifest.json`` with author and licence. Always pass the id as a string
literal: the build reads the literals to cache figures and to print the attribution under them.

    icon(ax, "servier/heart", at=(3, 2), height=1.5)
    icon(ax, "phylopic/mouse", at=(6, 2), height=1, color="animal")   # silhouettes take a token
    icon(ax, "wikimedia/flower-section", at=(9, 2), height=3, parts={"ovary": "ovary"}, mute="neutral")
"""

import json
import os

import numpy as np
from matplotlib.colors import to_hex, to_rgb
from matplotlib.patches import PathPatch
from matplotlib.path import Path

from . import palette as P

ICON_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "icons")
_cache = {}


def load(icon_id):
    if icon_id not in _cache:
        path = os.path.join(ICON_DIR, icon_id + ".json")
        if not os.path.exists(path):
            raise FileNotFoundError(f"icon {icon_id!r} is not in the library; add it with scripts/icons.py (see BIO_FIGURES.md)")
        with open(path) as f:
            _cache[icon_id] = json.load(f)
    return _cache[icon_id]


def size(icon_id):
    """(width, height) of the icon's box in its own units."""
    d = load(icon_id)
    return d["box"][2], d["box"][3]


def _theme_colour(c, opacity=1.0):
    # Dark theme: keep illustration colours. Opaque near-black outlines become the ink colour, but
    # semi-transparent black/white layers are shading and highlights and must stay dark/light; both
    # are nudged off the renderer's recolouring thresholds (it would turn black into ink, white into the surface).
    if c is None:
        return None
    r, g, b = to_rgb(c)
    dark = max(r, g, b) < 0.22
    white = min(r, g, b) > 0.93
    if P.is_dark():
        if dark:
            return P.ink() if opacity > 0.85 else "#1d1d1d"
        if white:
            return "#eef1f5" if opacity > 0.85 else "#f4f4f4"
    else:
        if max(r, g, b) < 0.1:
            return "#1d1d1d"
        if min(r, g, b) > 0.95:
            return "#f8f9fa"
    return to_hex((r, g, b))


def _placement(icon_id, at, height, width, anchor, flip, rotate):
    """Map raw icon coordinates to canvas coordinates for the placement ``icon()`` uses."""
    d = load(icon_id)
    x0, y0, w, h = d["box"]
    s = height / h if width is None else width / w
    W, H = w * s, h * s
    ax_, ay_ = at
    dx = {"center": -W / 2, "bottom": -W / 2, "top": -W / 2, "left": 0, "right": -W}.get(anchor, -W / 2)
    dy = {"center": -H / 2, "bottom": 0, "top": -H, "left": -H / 2, "right": -H / 2}.get(anchor, -H / 2)
    th = np.radians(rotate)
    R = np.array([[np.cos(th), np.sin(th)], [-np.sin(th), np.cos(th)]])

    def tf(v):
        v = np.asarray(v, float)
        v = np.c_[(v[:, 0] - x0) * s, (h - (v[:, 1] - y0)) * s]  # SVG y points down
        if flip:
            v[:, 0] = W - v[:, 0]
        return (v + [dx, dy]) @ R + [ax_, ay_]

    corners = np.array([[dx, dy], [dx + W, dy], [dx, dy + H], [dx + W, dy + H]]) @ R + [ax_, ay_]
    return tf, s, corners


def icon(ax, icon_id, at=(0, 0), height=1.0, width=None, anchor="center", color=None, flip=False, rotate=0.0, alpha=1.0,
         zorder=10, parts=None, hide=(), mute=None):
    """Draw an icon with its ``anchor`` ("center", "bottom", "left", …) at ``at``, scaled to ``height``.

    ``color`` (a palette token or hex) recolours a monochrome icon such as a PhyloPic silhouette;
    multicolour illustrations keep their own colours. Templates with named parts (``parts(icon_id)``)
    can be edited by part: ``parts={"petal": "petal", "stamen": "anther"}`` recolours those parts with
    tokens, ``hide=["label-lines"]`` leaves parts out, and ``mute="neutral"`` draws every part not in
    ``parts`` in that token's light shade, so the recoloured parts stand out. Returns the bounding box
    (x, y, w, h).
    """
    d = load(icon_id)
    tf, s, corners = _placement(icon_id, at, height, width, anchor, flip, rotate)
    parts = parts or {}
    mono = d.get("mono", False)
    for item in d["items"]:
        part = item.get("p")
        if part in hide:
            continue
        path = Path(tf(item["v"]), item["c"])
        fc, ec = item.get("f"), item.get("s")
        tok = parts.get(part) if part else None
        if tok is not None:
            fc = P.fill(tok) if fc else None
            ec = P.edge(tok) if ec else None
        elif mute is not None:
            fc = P.light(mute) if fc else None
            ec = P.edge(mute) if ec else None
        elif color is not None and (mono or item.get("mono_part")):
            fc = P.fill(color) if fc else None
            ec = P.edge(color) if ec else None
        else:
            op = item.get("o", 1.0)
            fc, ec = _theme_colour(fc, op), _theme_colour(ec, op)
        a = alpha * item.get("o", 1.0)
        # fill=False (not facecolor="none") and alpha only when < 1: the dark-theme recolouring would
        # otherwise turn an invisible face opaque.
        ax.add_patch(PathPatch(path, fill=fc is not None, facecolor=fc or (0, 0, 0, 0), edgecolor=ec or (0, 0, 0, 0),
                               lw=item.get("w", 0) * s * 72 / 100 if ec else 0, alpha=a if a < 0.999 else None,
                               zorder=zorder, joinstyle="round", capstyle="round"))
    # bounding box (x, y, w, h) of the drawn icon, rotation included (it turns about ``at``)
    lo, hi = corners.min(axis=0), corners.max(axis=0)
    return (lo[0], lo[1], hi[0] - lo[0], hi[1] - lo[1])


def parts(icon_id):
    """Names of the parts of a template icon (empty for icons without named parts)."""
    return list(load(icon_id).get("parts", []))


def icon_part(icon_id, part, at=(0, 0), height=1.0, width=None, anchor="center", flip=False, rotate=0.0, where="center"):
    """Canvas point on a named part of an icon placed with the same arguments as ``icon()``, for callouts:
    ``bio.callout(ax, bio.icon_part("wikimedia/flower", "ovary", at=…, height=…), text_xy, "Ovary")``.
    ``where`` is "center" (the point of the part nearest its centroid, so a part made of separate pieces
    still gets a point on itself) or "top" / "bottom" / "left" / "right"."""
    d = load(icon_id)
    tf, _, _ = _placement(icon_id, at, height, width, anchor, flip, rotate)
    pts = [tf(it["v"]) for it in d["items"] if it.get("p") == part]
    if not pts:
        raise KeyError(f"icon {icon_id!r} has no part {part!r}; parts: {', '.join(parts(icon_id)) or 'none'}")
    v = np.vstack(pts)
    if where == "center":
        p = v[np.argmin(np.hypot(*(v - v.mean(axis=0)).T))]
    else:
        k = {"top": (1, np.argmax), "bottom": (1, np.argmin), "left": (0, np.argmin), "right": (0, np.argmax)}[where]
        p = v[k[1](v[:, k[0]])]
    return (float(p[0]), float(p[1]))
