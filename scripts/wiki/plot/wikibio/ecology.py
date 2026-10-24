"""Ecology figures: cycles (nutrient cycles, life cycles, the cell cycle), food webs, ecological
pyramids and population age pyramids.

    from wikibio import ecology
    ecology.cycle(ax, (6, 4), 3, ["G1", "S", "G2", "M"], arrow_labels=[None, None, None, "Cytokinesis"])
    ecology.food_web(ax, nodes, links, box=(1, 1, 10, 6), levels=["Producers", "Herbivores", "Carnivores"])
    ecology.pyramid(ax, (6, 1), [dict(text="Producers", value=20810), ...], scale="log", unit="kcal m⁻² yr⁻¹")
    ecology.age_pyramid(ax, (6, 1), ["0-4", "5-9", ...], male, female, scale=0.8)

Icons are passed by id (``icon="phylopic/herring"``); the plot script must contain each id as a string
literal (a dict literal is enough) so that the build can cache the figure and credit the icon.
"""

import math

import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch, Wedge

from . import palette as P
from .core import FONT, LINE, label
from .core import arrow as _core_arrow
from .icons import icon as _icon
from .icons import size as _icon_size


def _text_wh(ax, text, size="normal", bold=False, italic=False):
    t = ax.text(0, 0, text, fontsize=FONT.get(size, size), weight="bold" if bold else "normal",
                style="italic" if italic else "normal")
    bb = t.get_window_extent(ax.figure.canvas.get_renderer())
    t.remove()
    inv = ax.transData.inverted()
    (x0, y0), (x1, y1) = inv.transform([(bb.x0, bb.y0), (bb.x1, bb.y1)])
    return abs(x1 - x0), abs(y1 - y0)


def arrow(ax, a, b, **kw):
    """``core.arrow`` without pixel snapping: Agg snapping turns the float jitter of a sampled straight
    line into visible bumps, so the lines it draws are unsnapped."""
    n0 = len(ax.lines)
    pts = _core_arrow(ax, a, b, **kw)
    for line in ax.lines[n0:]:
        line.set_snap(False)
    return pts


def _tint(token, strength=0.3):
    return P.mix(P.surface(), P.fill(token), strength)


def _soft_ink(t=0.25):
    """Ink softened towards the background: for arrows that should not dominate."""
    return P.mix(P.ink(), P.surface(), t)


def fit_icon(ax, icon_id, at, w, h, color=None, flip=False, rotate=0.0, anchor="center", zorder=10):
    """Draw an icon scaled to fit inside a w × h box centred (or anchored) at ``at``; returns its box."""
    iw, ih = _icon_size(icon_id)
    if rotate % 180:
        iw, ih = ih, iw
    s = min(w / iw, h / ih)
    height = (ih if not rotate % 180 else iw) * s
    return _icon(ax, icon_id, at=at, height=height, anchor=anchor, color=color, flip=flip, rotate=rotate, zorder=zorder)


# -------------------------------------------------------------------- nodes


class _Node:
    def __init__(self, xy, w, h, shape):
        self.xy, self.w, self.h, self.shape = np.asarray(xy, float), w, h, shape

    def inside(self, p, margin=0.0):
        d = np.asarray(p, float) - self.xy
        if self.shape == "circle":
            r = max(self.w, self.h) / 2 + margin
            return np.hypot(*d) <= r
        return abs(d[0]) <= self.w / 2 + margin and abs(d[1]) <= self.h / 2 + margin

    def edge_toward(self, q, margin=0.1):
        """The point on this node's outline (plus margin) in the direction of q."""
        q = np.asarray(q, float)
        d = q - self.xy
        L = np.hypot(*d) or 1.0
        u = d / L
        if self.shape == "circle":
            return self.xy + u * (max(self.w, self.h) / 2 + margin)
        tx = (self.w / 2 + margin) / abs(u[0]) if abs(u[0]) > 1e-9 else np.inf
        ty = (self.h / 2 + margin) / abs(u[1]) if abs(u[1]) > 1e-9 else np.inf
        return self.xy + u * min(tx, ty)


def node(ax, xy, text=None, token="neutral", shape="box", w=None, h=None, size="normal", icon=None, icon_size=1.0,
         icon_color=None, icon_opts=None, draw=None, sub=None, bold=False, italic=False, zorder=10):
    """A diagram node: a rounded box / circle with text, an icon with a caption, or a custom drawing.

    shape   "box", "circle", "pill" or "none" (text only); with ``icon`` (an id) or ``draw`` (a function
            ``draw(ax, xy, icon_size)``) the picture is drawn at ``xy`` with the caption below it
    sub     a second, smaller line under the text (e.g. a pool size)
    Returns an object with the node's extent, used to trim arrows.
    """
    x, y = xy
    if icon or draw:
        s = icon_size
        wi = s * 1.4
        if icon:
            o = dict(icon_opts or {})
            bx = fit_icon(ax, icon, (x, y), o.pop("width", s * 1.7), s, color=icon_color or token, zorder=zorder, **o)
            wi = bx[2]
        else:
            draw(ax, (x, y), s)
        tw = th = sw = sh = 0.0
        if text:
            tw, th = _text_wh(ax, text, size, bold=bold, italic=italic)
            label(ax, (x, y - s / 2 - 0.12), text, size=size, va="top", bold=bold, italic=italic, zorder=zorder + 1)
        if sub:
            sw, sh = _text_wh(ax, sub, "small")
            label(ax, (x, y - s / 2 - 0.16 - th), sub, size="small", va="top", color=P.muted(), zorder=zorder + 1)
        top = y + s / 2
        bottom = y - s / 2 - (0.12 + th if text else 0) - (0.04 + sh if sub else 0)
        return _Node((x, (top + bottom) / 2), max(wi, tw, sw), top - bottom, "box")
    tw, th = _text_wh(ax, text or "", size, bold=bold, italic=italic) if text else (0.6, 0.3)
    sw, sh = _text_wh(ax, sub, "small") if sub else (0.0, 0.0)
    W = w or max(tw, sw) + 0.5
    H = h or th + (sh + 0.08 if sub else 0) + 0.36
    if shape == "circle":
        R = max(W, H) / 2 if w is None else w / 2
        ax.add_patch(Circle(xy, R, facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE * 0.9, zorder=zorder))
        W = H = 2 * R
    elif shape in ("box", "pill"):
        r = H / 2 if shape == "pill" else 0.18
        ax.add_patch(FancyBboxPatch((x - W / 2, y - H / 2), W, H, boxstyle=f"round,pad=0,rounding_size={min(r, W / 2)}",
                                    facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE * 0.9, zorder=zorder))
    space = P.TOKENS.get(token, (None, None, "object"))[2] == "space"  # pale compartments: dark in the dark theme
    tc = P.on_fill() if shape != "none" and not (space and P.is_dark()) else P.ink()
    if text:
        ty = y + (sh / 2 + 0.04 if sub else 0)
        label(ax, (x, ty), text, size=size, color=tc, bold=bold, italic=italic, zorder=zorder + 1)
    if sub:
        label(ax, (x, y - th / 2 - 0.02), sub, size="small", color=tc, zorder=zorder + 1)
    return _Node(xy, W, H, "circle" if shape == "circle" else "box")


def connect(ax, a, b, kind="process", bend=0.0, color=None, lw=LINE, dashed=False, margin=0.12, text=None,
            text_size="small", text_offset=0.25, text_side=1, text_at=0.5, zorder=15):
    """An arrow between two nodes (from ``node``), trimmed at their outlines; optional mid-arrow label.

    The label sits beside the arrow at fraction ``text_at`` of its length, on its upper side
    (``text_side=-1``: the lower side; for vertical arrows +1 is the right side).
    """
    pa, pb = a.edge_toward(b.xy, margin), b.edge_toward(a.xy, margin)
    if bend:
        # aim the trimmed ends along the curve rather than the chord
        d = b.xy - a.xy
        n = np.array([-d[1], d[0]])
        ctrl = (a.xy + b.xy) / 2 + bend * n
        pa, pb = a.edge_toward(ctrl, margin), b.edge_toward(ctrl, margin)
    pts = arrow(ax, pa, pb, kind=kind, bend=bend, color=color, lw=lw, dashed=dashed, zorder=zorder)
    if text:
        k = int(round(text_at * (len(pts) - 1)))
        mid = pts[k]
        t = pts[min(len(pts) - 1, k + 1)] - pts[max(0, k - 1)]
        t = t / (np.linalg.norm(t) or 1.0)
        n = np.array([-t[1], t[0]])
        if n[1] < 0 or (abs(n[1]) < 1e-6 and n[0] < 0):
            n = -n
        n = n * text_side
        q = mid + n * text_offset
        ha = "center" if abs(n[0]) < 0.4 else ("left" if n[0] > 0 else "right")
        label(ax, q, text, size=text_size, ha=ha, va="bottom" if n[1] > 0.4 else "top" if n[1] < -0.4 else "center",
              color=P.muted())
    return pts


# -------------------------------------------------------------------- cycle


def _arc(center, r, a0, a1, n=120):
    th = np.linspace(a0, a1, n)
    return np.c_[center[0] + r * np.cos(th), center[1] + r * np.sin(th)]


def _arc_arrow(ax, pts, kind="process", color=None, lw=LINE, dashed=False, head=0.24, zorder=15):
    """An arrow along a sampled curve (polyline), head at the last point."""
    c = color or P.ink()
    seg = np.r_[0, np.cumsum(np.hypot(*np.diff(pts, axis=0).T))]
    L = seg[-1]
    k = int(np.searchsorted(seg, L - head * 1.6))
    k = max(0, min(k, len(pts) - 2))
    if k > 0:
        ax.plot(pts[:k + 1, 0], pts[:k + 1, 1], color=c, lw=lw, ls=(0, (3.2, 2.2)) if dashed else "-",
                solid_capstyle="round", zorder=zorder)
    arrow(ax, pts[k], pts[-1], kind=kind, color=c, lw=lw, dashed=dashed, head=head, zorder=zorder)


def cycle(ax, center, radius, steps, start=90.0, clockwise=True, shape="box", token="neutral", size="normal",
          arrow_kind="process", arrow_color=None, arrow_lw=LINE * 1.2, arrow_radius=None, gap=0.12,
          arrow_labels=None, label_side="out", label_size="small", chords=None, sectors=None, angles=None,
          center_text=None, zorder=10):
    """Steps on a circle joined by curved arrows (a cycle diagram); returns the node objects.

    steps         list of str or dict(text, token, shape, icon, icon_size, icon_opts, draw, sub, w, h, bold, italic)
    start         angle (deg) of the first step; steps follow clockwise (or anticlockwise)
    angles        explicit angles (deg) per step, overriding the even spacing
    arrow_labels  text per arrow (arrow i goes from step i to step i+1), placed outside ("out") or inside
                  the circle; a dict(text, side, color, bold) per label also works
    chords        extra arrows through the inside: list of (i, j) or (i, j, dict(kind, bend, dashed, text, color))
    sectors       background bands: list of dict(start, end, token, text, r0, r1) with start/end in step units
                  (fractional: 0.5 is midway between steps 0 and 1), e.g. the haploid phase of a life cycle
    Each arrow follows the circle (``arrow_radius``) and stops ``gap`` short of the nodes.
    """
    n = len(steps)
    sgn = -1 if clockwise else 1
    if angles is None:
        angles = [start + sgn * 360.0 * i / n for i in range(n)]
    th = [math.radians(a) for a in angles]
    cx, cy = center
    ra = arrow_radius or radius

    def ang_at(u):
        # angle (rad) at a fractional step position u
        i = int(math.floor(u)) % n
        f = u - math.floor(u)
        a0, a1 = th[i], th[(i + 1) % n]
        d = (a1 - a0) % (2 * math.pi) if not clockwise else -((a0 - a1) % (2 * math.pi))
        return a0 + d * f

    # sectors first (background)
    for s in sectors or []:
        a0, a1 = math.degrees(ang_at(s["start"])), math.degrees(ang_at(s["end"]))
        if clockwise:
            a0, a1 = a1, a0
        r1 = s.get("r1", radius * 1.42)
        r0 = s.get("r0", radius * 0.55)
        ax.add_patch(Wedge(center, r1, a0, a1, width=r1 - r0, facecolor=_tint(s.get("token", "neutral"), s.get("strength", 0.28)),
                           edgecolor="none", lw=0, zorder=1))
        if s.get("text"):
            am = math.radians((a0 + a1) / 2) if a1 > a0 else math.radians((a0 + a1 + 360) / 2)
            rr = s.get("text_r", r0 + 0.35)
            label(ax, (cx + rr * math.cos(am), cy + rr * math.sin(am)), s["text"], size=s.get("text_size", "title"),
                  bold=True, color=P.edge(s.get("token", "neutral")), zorder=3)

    nodes = []
    for i, st in enumerate(steps):
        d = {"text": st} if isinstance(st, str) else dict(st)
        xy = (cx + radius * math.cos(th[i]), cy + radius * math.sin(th[i]))
        nodes.append(node(ax, xy, text=d.get("text"), token=d.get("token", token), shape=d.get("shape", shape),
                          w=d.get("w"), h=d.get("h"), size=d.get("size", size), icon=d.get("icon"),
                          icon_size=d.get("icon_size", 1.0), icon_color=d.get("icon_color"), icon_opts=d.get("icon_opts"),
                          draw=d.get("draw"), sub=d.get("sub"), bold=d.get("bold", False), italic=d.get("italic", False),
                          zorder=zorder))
        if d.get("extent"):  # caller-declared extent (w, h) for drawings and icons with captions
            nodes[-1].w, nodes[-1].h = d["extent"]
            if "offset" in d:
                nodes[-1].xy = nodes[-1].xy + np.asarray(d["offset"], float)

    labels = arrow_labels or [None] * n
    for i in range(n):
        j = (i + 1) % n
        a0, a1 = th[i], th[j]
        if clockwise:
            if a1 >= a0:
                a1 -= 2 * math.pi
        else:
            if a1 <= a0:
                a1 += 2 * math.pi
        pts = _arc(center, ra, a0, a1, 240)
        keep = np.array([not nodes[i].inside(p, gap) and not nodes[j].inside(p, gap) for p in pts])
        idx = np.flatnonzero(keep)
        if len(idx) < 4:
            continue
        # the longest run of points outside both nodes
        runs = np.split(idx, np.flatnonzero(np.diff(idx) > 1) + 1)
        run = max(runs, key=len)
        _arc_arrow(ax, pts[run], kind=arrow_kind, color=arrow_color, lw=arrow_lw, zorder=zorder + 5)
        lab = labels[i] if i < len(labels) else None
        if lab:
            ld = {"text": lab} if isinstance(lab, str) else dict(lab)
            side = ld.get("side", label_side)
            am = (a0 + a1) / 2
            off = ld.get("offset", 0.32)
            rr = ra + off if side == "out" else ra - off
            p = (cx + rr * math.cos(am), cy + rr * math.sin(am))
            ca = math.cos(am)
            if side == "out":
                ha = "left" if ca > 0.25 else "right" if ca < -0.25 else "center"
                va = "bottom" if math.sin(am) > 0.5 else "top" if math.sin(am) < -0.5 else "center"
            else:
                ha = "right" if ca > 0.25 else "left" if ca < -0.25 else "center"
                va = "top" if math.sin(am) > 0.5 else "bottom" if math.sin(am) < -0.5 else "center"
            label(ax, p, ld["text"], size=ld.get("size", label_size), ha=ha, va=va, bold=ld.get("bold", False),
                  italic=ld.get("italic", False), color=ld.get("color") or P.ink(), zorder=zorder + 6)

    for ch in chords or []:
        i, j = ch[0], ch[1]
        o = dict(ch[2]) if len(ch) > 2 else {}
        connect(ax, nodes[i], nodes[j], kind=o.get("kind", arrow_kind), bend=o.get("bend", 0.0),
                color=o.get("color", arrow_color), lw=o.get("lw", arrow_lw * 0.85), dashed=o.get("dashed", False),
                text=o.get("text"), text_size=o.get("text_size", label_size), zorder=zorder + 5)
    if center_text:
        label(ax, center, center_text, size="title", bold=True, color=P.muted())
    return nodes


# ----------------------------------------------------------------- food web

TROPHIC_LEVELS = ["Primary producers", "Primary consumers", "Secondary consumers", "Tertiary consumers", "Apex predators"]


def food_web(ax, nodes, links, box=(0, 0, 10, 6), levels=None, bands=True, icon_size=0.9, label_size="small",
             arrow_color=None, arrow_lw=LINE * 0.95, band_tokens=None, level_label_x=None, zorder=10):
    """A food web: organisms in rows by trophic level, arrows in the direction of energy flow (prey → consumer).

    nodes   {id: dict(level=0.., x=0..1 (position across the row; default even), text, icon, icon_opts,
            token (icon colour / box colour), size (icon height), sub)}
    links   [(prey, consumer)] or (prey, consumer, dict(bend, dashed, color, kind))
    box     (x0, y0, width, height): level 0 sits at the bottom
    levels  row names (default ``TROPHIC_LEVELS``); drawn at the left with alternating soft bands
    Returns {id: node object} (``.xy``) for further annotation.
    """
    x0, y0, W, H = box
    nlev = max(d["level"] for d in nodes.values()) + 1
    names = levels if levels is not None else TROPHIC_LEVELS[:nlev]
    dy = H / nlev
    lx = x0 if level_label_x is None else level_label_x
    lab_w = 0.0
    if names:
        lab_w = max(_text_wh(ax, s, "small", bold=True)[0] for s in names if s) + 0.4
    if bands:
        toks = band_tokens or ["plant", "positive", "highlight", "rna", "negative"]
        for k in range(nlev):
            ax.add_patch(FancyBboxPatch((x0, y0 + k * dy + 0.05), W, dy - 0.1, boxstyle="round,pad=0,rounding_size=0.2",
                                        facecolor=_tint(toks[k % len(toks)], 0.16), edgecolor="none", lw=0, zorder=1))
    if names:
        for k, s in enumerate(names):
            if s:
                label(ax, (lx + 0.2, y0 + (k + 0.5) * dy), s.replace(" ", "\n", 1) if len(s) > 12 else s, size="small",
                      ha="left", bold=True, color=P.muted(), zorder=3)
    # positions
    rows = {}
    for nid, d in nodes.items():
        rows.setdefault(d["level"], []).append(nid)
    xa, xb = x0 + lab_w + 0.3, x0 + W - 0.4
    objs = {}
    for k, ids in rows.items():
        for i, nid in enumerate(ids):
            d = nodes[nid]
            fx = d.get("x", (i + 0.5) / len(ids))
            xy = (xa + fx * (xb - xa), y0 + (k + 0.5) * dy + (0.18 if d.get("icon") else 0) + d.get("dy", 0))
            s = d.get("size", icon_size)
            if d.get("icon"):
                objs[nid] = node(ax, xy, text=d.get("text", nid), token=d.get("token", "animal"), icon=d["icon"],
                                 icon_size=s, icon_opts=d.get("icon_opts"), size=label_size, sub=d.get("sub"),
                                 italic=d.get("italic", False), zorder=zorder)
            else:
                objs[nid] = node(ax, xy, text=d.get("text", nid), token=d.get("token", "neutral"),
                                 shape=d.get("shape", "pill"), size=label_size, sub=d.get("sub"), zorder=zorder)
    c = arrow_color or _soft_ink(0.15)
    for ln in links:
        a, b = ln[0], ln[1]
        o = dict(ln[2]) if len(ln) > 2 else {}
        connect(ax, objs[a], objs[b], kind=o.get("kind", "process"), bend=o.get("bend", 0.0), color=o.get("color", c),
                lw=o.get("lw", arrow_lw), dashed=o.get("dashed", False), margin=0.08, zorder=zorder + 4)
    return objs


# ------------------------------------------------------------------ pyramid


def pyramid(ax, base, levels, width=8.0, height=0.9, scale="linear", min_width=0.9, gap=0.06,
            unit=None, value_fmt="{:,g}", transfer=False, label_inside=True, size="small", zorder=5):
    """An ecological pyramid (energy, biomass or numbers): one bar per trophic level, bottom to top.

    base    (x, y) of the centre of the bottom edge
    levels  list of dict(text, value, token), from producers upwards
    scale   bar width ∝ value ("linear"), √value ("sqrt"), log value ("log") or all equal ("equal");
            values that grow upwards give an inverted pyramid (e.g. marine biomass)
    transfer  annotate the ratio between consecutive levels at the right (e.g. "10.4%")
    Returns the list of (centre, width) of the bars.
    """
    x, y = base
    vals = [float(d.get("value", 1.0)) for d in levels]
    vmax, vmin = max(vals), min(vals)
    if scale == "linear":
        ws = [width * v / vmax for v in vals]
    elif scale == "sqrt":
        ws = [width * math.sqrt(v / vmax) for v in vals]
    elif scale == "log":
        lo = math.log10(vmin) - 0.5
        ws = [width * (math.log10(v) - lo) / (math.log10(vmax) - lo) for v in vals]
    else:
        ws = [width * (1 - 0.8 * i / max(1, len(vals) - 1)) for i in range(len(vals))]
    ws = [max(min_width, w_) for w_ in ws]
    out = []
    right = max(ws) / 2
    for i, (d, w_) in enumerate(zip(levels, ws)):
        yc = y + i * height + height / 2
        tok = d.get("token", "neutral")
        ax.add_patch(FancyBboxPatch((x - w_ / 2, yc - height / 2 + gap / 2), w_, height - gap,
                                    boxstyle="round,pad=0,rounding_size=0.08", facecolor=P.fill(tok), edgecolor=P.edge(tok),
                                    lw=LINE * 0.85, zorder=zorder))
        txt = d.get("text", "")
        val = d.get("value")
        vtxt = (value_fmt.format(val) + (f" {unit}" if unit else "")) if val is not None and d.get("show_value", True) else None
        tw, _ = _text_wh(ax, txt, size, bold=True)
        if label_inside and tw + 0.3 < w_:
            label(ax, (x, yc), txt, size=size, bold=True, color=P.on_fill(), zorder=zorder + 1)
            if vtxt:
                label(ax, (x + right + 0.3, yc), vtxt, size=size, ha="left", zorder=zorder + 1)
        else:
            s = txt + (f"   {vtxt}" if vtxt else "")
            label(ax, (x + max(w_ / 2, 0) + 0.3, yc), s if not label_inside else txt, size=size, ha="left", bold=False,
                  zorder=zorder + 1)
            if label_inside and vtxt:
                label(ax, (x + right + 0.3, yc), vtxt, size=size, ha="left", zorder=zorder + 1)
        out.append(((x, yc), w_))
    if transfer:
        tx = x - max(ws) / 2 - 0.35
        for i in range(1, len(vals)):
            ya, yb = out[i - 1][0][1], out[i][0][1]
            arrow(ax, (tx, ya + 0.1), (tx, yb - 0.1), kind="process", color=P.muted(), lw=LINE * 0.8, head=0.16)
            pct = 100 * vals[i] / vals[i - 1]
            label(ax, (tx - 0.15, (ya + yb) / 2), f"{pct:.3g}%", size="tiny", ha="right", color=P.muted())
    return out


def age_pyramid(ax, center, ages, left, right, scale=1.0, bar=0.36, gap=1.1, tokens=("dna", "rna"),
                sides=("Male", "Female"), ticks=None, unit="%", size="tiny", title=None, zorder=5):
    """A population age–sex pyramid: horizontal bars per age class, ``left`` (males) and ``right`` (females).

    center  (x, y) of the bottom of the central age-label column
    ages    age-class labels from youngest (bottom) to oldest
    left, right   values per class (e.g. % of the population); ``scale`` = data units per value unit
    bar     bar height (classes are spaced by ``bar`` + a small gap); ``gap`` = width of the label column
    ticks   values for the axis below both halves (default: a few round numbers)
    """
    cx, cy = center
    step = bar * 1.18
    for i, (a, l, r) in enumerate(zip(ages, left, right)):
        y = cy + i * step + step / 2
        for v, sgn, tok in ((l, -1, tokens[0]), (r, 1, tokens[1])):
            w_ = v * scale
            x0 = cx + sgn * gap / 2
            ax.add_patch(FancyBboxPatch((min(x0, x0 + sgn * w_), y - bar / 2), w_, bar, boxstyle="round,pad=0,rounding_size=0.04",
                                        facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.7, zorder=zorder))
        label(ax, (cx, y), a, size=size, color=P.muted(), zorder=zorder + 1)
    top = cy + len(ages) * step
    vmax = max(max(left), max(right))
    if ticks is None:
        m = 10 ** math.floor(math.log10(vmax))
        st = m if vmax / m < 4 else 2 * m if vmax / m < 8 else 5 * m
        ticks = [k * st for k in range(int(vmax / st) + 1 + (1 if vmax % st else 0))]
    c = P.muted()
    yb = cy - 0.08
    for sgn in (-1, 1):
        x0 = cx + sgn * gap / 2
        x1 = x0 + sgn * ticks[-1] * scale
        ax.plot([x0, x1], [yb, yb], color=c, lw=0.8, zorder=zorder)
        for t in ticks:
            xt = x0 + sgn * t * scale
            ax.plot([xt, xt], [yb, yb - 0.1], color=c, lw=0.8, zorder=zorder)
            label(ax, (xt, yb - 0.15), f"{t:g}", size=size, va="top", color=c)
    if unit:
        label(ax, (cx, yb - 0.15), unit, size=size, va="top", color=c)
    if sides:
        label(ax, (cx - gap / 2 - ticks[-1] * scale * 0.5, top + 0.12), sides[0], size="small", va="bottom", bold=True,
              color=P.edge(tokens[0]))
        label(ax, (cx + gap / 2 + ticks[-1] * scale * 0.5, top + 0.12), sides[1], size="small", va="bottom", bold=True,
              color=P.edge(tokens[1]))
    if title:
        label(ax, (cx, top + 0.62), title, size="normal", va="bottom", bold=True)
    return top
