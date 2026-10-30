"""Organogenesis: the heart from crescent to chambers, blood islands, vascular plexus and sprouting vessels, the
dorsal aorta with hemogenic endothelium, the primitive gut tube with its organ buds, the pharyngeal arches and
pouches, and the stages of gametogenesis (seminiferous tubule, germ-cell lineages, ovarian follicles).

    from wikibio import organogenesis as O
    h = O.heart(ax, (4, 4), 3.0, "crescent")        crescent / tube / looping / chambers (ventral view; the
                                                    embryo's right is on the viewer's left); colours by heart field
    O.band(ax, curve, 0.4, [(0, 0.3, "fhf"), (0.3, 1, "shf_a")])
                                                    a tube along a curve, coloured by arc-length fraction
    b = O.blood_island(ax, (2, 2), 0.8)             blood cells inside a ring of angioblasts
    O.plexus(ax, (0, 0, 6, 4), cell=0.9)            a primary capillary plexus (jittered honeycomb of vessels)
    s = O.sprout(ax, (3, 1), 90, 2.5)               a sprouting vessel: tip cell with filopodia and stalk cells
    a = O.aorta_section(ax, (5, 3), 1.5)            dorsal aorta in cross-section, hemogenic floor, budding clusters
    g = O.gut_tube(ax, (1, 3), 12)                  lateral view of the primitive gut tube (anterior left,
                                                    dorsal up) with pharyngeal pouches and organ buds
    p = O.pharynx(ax, (6, 4), 6, 7)                 frontal section: arches, pouches, clefts (both sides)
    t = O.seminiferous_tubule(ax, (4, 4), 3)        cross-section: spermatogonia to sperm, Sertoli and Leydig cells
    O.germ_lineage(ax, (1, 2), "sperm", step=2.2)   stages of spermatogenesis (with cytoplasmic bridges) or
                                                    oogenesis ("egg", with polar bodies)
    f = O.follicle(ax, (3, 3), 1.5, "antral")       primordial / primary / secondary / antral

Tissues keep one colour in every figure (``TISSUE``): the germ layers follow ``zoology.GERM`` (ectoderm blue,
mesoderm red, endoderm yellow); heart fields: first heart field red, anterior second heart field orange,
posterior second heart field pink, cardiac neural crest green (as in ``neurodev``), proepicardium and
epicardium purple; arteries red, veins blue; germ cells purple ("germline" of ``embryology``). Every function is
deterministic and returns a dict of anchor points (canvas coordinates) for ``bio.callout`` and arrows.
"""

import math

import numpy as np
from matplotlib.patches import Circle, Ellipse, PathPatch
from matplotlib.path import Path

from . import palette as P
from .core import LINE, blob, polyline

TISSUE = {
    "ectoderm": "ectoderm", "mesoderm": "mesoderm", "endoderm": "endoderm",
    "fhf": "muscle", "shf_a": "drug", "shf_p": "receptor", "crest": "cl", "epicardium": "protein",
    "endocardium": "metabolite", "cushion": "lipid", "myocardium": "muscle",
    "artery": "blood", "vein": "dna", "endothelium": "rrna", "tip": "atp", "blood_cell": "blood",
    "angioblast": "rrna", "hemogenic": "k", "hsc": "protein", "mesenchyme": "mesoderm",
    "germ": "protein", "sertoli": "animal", "leydig": "drug", "myoid": "muscle", "granulosa": "lipid_head",
    "theca": "receptor", "oocyte": "cytoplasm", "zona": "bone", "fluid": "vacuole",
    "thyroid": "carbohydrate", "lung": "dna2", "stomach": "lipid_head", "liver": "drug", "pancreas": "k",
    "gallbladder": "plant", "thymus": "protein", "parathyroid": "enzyme", "tonsil": "receptor",
    "middle_ear": "channel", "yolk": "lipid_tail", "allantois": "carbohydrate",
}


def tok(name):
    """Palette token of a tissue name (``TISSUE``), or the name itself if it already is a token."""
    return TISSUE.get(name, name)


def _wash(token, light=0.55, dark=0.78):
    """A pale, opaque tint of a token (theme aware)."""
    return P.mix(P.fill(tok(token)), P.surface(), dark if P.is_dark() else light)


def _poly(ax, pts, token, z=5, lw=LINE * 0.8, face=None, edge=None, ls="-"):
    v = np.asarray(pts, float)
    t = tok(token)
    p = PathPatch(Path(np.vstack([v, v[:1]]), closed=True), facecolor=face or P.fill(t), edgecolor=edge or P.edge(t),
                  lw=lw, zorder=z, joinstyle="round", ls=ls)
    ax.add_patch(p)
    return p


def _circ(ax, c, r, token, z=6, lw=LINE * 0.7, face=None):
    t = tok(token)
    ax.add_patch(Circle(c, r, facecolor=face or P.fill(t), edgecolor=P.edge(t), lw=lw, zorder=z))


def _nucleus(ax, c, r, token, z=7):
    t = tok(token)
    ax.add_patch(Circle(c, r, facecolor=P.edge(t), edgecolor="none", zorder=z))


def _bezier(pts, n=120):
    """A smooth open curve through control points (Catmull-Rom, end points repeated)."""
    p = np.asarray(pts, float)
    p = np.vstack([p[:1], p, p[-1:]])
    out = []
    for i in range(1, len(p) - 2):
        p0, p1, p2, p3 = p[i - 1], p[i], p[i + 1], p[i + 2]
        for t in np.linspace(0, 1, max(2, n // (len(p) - 3)), endpoint=False):
            t2, t3 = t * t, t * t * t
            out.append(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t2 + (-p0 + 3 * p1 - 3 * p2 + p3) * t3))
    out.append(p[-2])
    return np.array(out)


def band(ax, curve, width, segments=None, token="endoderm", lumen=None, z=5, smooth=True, n=400, edge=True):
    """Draw a tube of (possibly varying) ``width`` along ``curve`` (control points; smoothed unless smooth=False).

    ``segments`` is a list of (f0, f1, tissue) by fraction of arc length; ``lumen`` (a width fraction) draws a pale
    lumen down the middle. Returns dict with ``at(f, side=0)``: the point at fraction f, offset by side (-1..1) of the
    half-width, and ``q`` (resampled centre line).
    """
    c = _bezier(curve) if smooth else np.asarray(curve, float)
    q, nrm, L = polyline(c, n=n, closed=False)
    w = np.broadcast_to(np.asarray(width(np.linspace(0, 1, len(q))) if callable(width) else width, float), (len(q),))
    segs = segments or [(0.0, 1.0, token)]
    f = np.linspace(0, 1, len(q))
    for f0, f1, t in segs:
        k = (f >= f0 - 1e-9) & (f <= f1 + 1e-9)
        if k.sum() < 2:
            continue
        a = q[k] + nrm[k] * (w[k] / 2)[:, None]
        b = q[k] - nrm[k] * (w[k] / 2)[:, None]
        _poly(ax, np.vstack([a, b[::-1]]), t, z=z, lw=0, edge="none")
    if edge:
        tt = tok(segs[0][2])
        for s in (1, -1):
            e = q + s * nrm * (w / 2)[:, None]
            ax.plot(e[:, 0], e[:, 1], color=P.edge(tt), lw=LINE * 0.8, zorder=z + 0.2, solid_capstyle="round")
    if lumen:
        a = q + nrm * (w * lumen / 2)[:, None]
        b = q - nrm * (w * lumen / 2)[:, None]
        ax.add_patch(PathPatch(Path(np.vstack([a, b[::-1], a[:1]]), closed=True), facecolor=_wash("fluid", 0.2, 0.6),
                               edgecolor="none", zorder=z + 0.1))

    def at(fr, side=0.0):
        i = int(round(np.clip(fr, 0, 1) * (len(q) - 1)))
        return tuple(q[i] + nrm[i] * side * w[i] / 2)

    return {"at": at, "q": q, "nrm": nrm, "length": L}


# ------------------------------------------------------------------------------------------------- the heart


def heart(ax, center, size=3.0, stage="tube", fields=True, z=5):
    """The developing heart in ventral view (anterior up; the embryo's right on the viewer's left).

    stage "crescent": the cardiac crescent (first heart field) with the second heart field medial and dorsal to it;
          "tube": the linear heart tube, arterial pole up (outflow tract, future right ventricle, left ventricle,
          atria, sinus venosus with its two horns), second-heart-field cells joining both poles;
          "looping": the looped tube (ventricular bend to the embryo's right, atria moved dorsal and anterior);
          "chambers": a frontal section of the four-chambered heart with septa, valves and outflow vessels.
    With ``fields=True`` regions are coloured by origin (``TISSUE`` keys fhf, shf_a, shf_p, crest, epicardium);
    otherwise all myocardium is drawn in "myocardium". Returns anchors named after the structures.
    """
    cx, cy = center
    s = size
    col = (lambda k: k) if fields else (lambda k: "myocardium" if k in ("fhf", "shf_a", "shf_p") else k)
    A = {}
    if stage == "crescent":
        t = np.radians(np.linspace(200, 340, 120))
        r1, r2 = 0.95 * s, 0.62 * s
        outer = np.c_[cx + r1 * np.cos(t), cy + 0.25 * s + 0.75 * r1 * np.sin(t) + 0.55 * s]
        inner = np.c_[cx + r2 * np.cos(t[::-1]), cy + 0.25 * s + 0.75 * r2 * np.sin(t[::-1]) + 0.55 * s]
        _poly(ax, np.vstack([outer, inner]), col("fhf"), z=z + 1)
        r3 = 0.44 * s
        inner2 = np.c_[cx + r3 * np.cos(t), cy + 0.25 * s + 0.75 * r3 * np.sin(t) + 0.55 * s]
        _poly(ax, np.vstack([inner[::-1][8:-8], inner2[::-1][8:-8][::-1]]), col("shf_a") if fields else "myocardium", z=z)
        # posterior extension of the second field beside the foregut portal
        for sg in (-1, 1):
            arm = np.array([[cx + sg * 0.46 * s, cy + 0.22 * s], [cx + sg * 0.6 * s, cy - 0.35 * s], [cx + sg * 0.42 * s, cy - 0.45 * s],
                            [cx + sg * 0.3 * s, cy + 0.15 * s]])
            _poly(ax, _bezier(np.vstack([arm, arm[:1]]), 60), col("shf_p") if fields else "myocardium", z=z)
        ax.add_patch(Ellipse((cx, cy + 0.15 * s), 0.38 * s, 0.5 * s, facecolor=_wash("endoderm"), edgecolor=P.edge(tok("endoderm")),
                             lw=LINE * 0.7, zorder=z - 0.5))
        A.update(fhf=(cx - 0.78 * s * math.cos(math.radians(20)), cy + 0.55 * s - 0.2 * s), shf=(cx, cy + 0.25 * s),
                 shf_p=(cx + 0.52 * s, cy - 0.15 * s), foregut=(cx, cy + 0.15 * s), anterior=(cx, cy + 0.95 * s))
        return A

    if stage == "tube":
        L = 1.7 * s
        y0, y1 = cy - L / 2, cy + L / 2
        w = 0.36 * s
        curve = [(cx, y1), (cx, y0 + 0.25 * L), (cx, y0 + 0.08 * L)]
        segs = [(0.0, 0.2, col("shf_a")), (0.2, 0.42, col("shf_a")), (0.42, 0.72, col("fhf")), (0.72, 1.0, col("shf_p"))]
        b = band(ax, curve, lambda f: w * (0.75 + 0.35 * np.sin(np.pi * np.clip((f - 0.25) / 0.6, 0, 1))), segs, z=z + 1,
                 lumen=0.45, smooth=False)
        for sg in (-1, 1):  # sinus horns
            horn = _bezier([(cx, y0 + 0.08 * L), (cx + sg * 0.25 * s, y0), (cx + sg * 0.55 * s, y0 - 0.12 * s)], 60)
            band(ax, horn, 0.22 * s, [(0, 1, col("shf_p"))], z=z + 0.8, lumen=0.4, smooth=False)
        for f in (0.2, 0.42, 0.72):
            p, q = b["at"](f, 1.0), b["at"](f, -1.0)
            ax.plot([p[0], q[0]], [p[1], q[1]], color=P.muted(), lw=0.6, ls=(0, (2, 1.5)), zorder=z + 2)
        A.update(oft=b["at"](0.1), rv=b["at"](0.31), lv=b["at"](0.57), atria=b["at"](0.84), sinus=(cx, y0 - 0.02 * s),
                 arterial=(cx, y1), venous=(cx, y0 - 0.1 * s), side=lambda f, sd: b["at"](f, sd))
        if fields:
            for sg, f in ((1, 0.08), (-1, 0.9)):
                ax.add_patch(Ellipse(b["at"](f, sg * 2.2), 0.28 * s, 0.42 * s, facecolor=_wash(col("shf_a") if f < 0.5 else col("shf_p"), 0.35, 0.6),
                                     edgecolor=P.edge(tok(col("shf_a") if f < 0.5 else col("shf_p"))), lw=0.6, ls=(0, (2, 1.5)), zorder=z))
            A.update(shf_a=b["at"](0.08, 2.2), shf_p_src=b["at"](0.9, -2.2))
        return A

    if stage == "looping":
        # ventral view: the ventricular loop bulges to the embryo's right (viewer's left)
        curve = [(cx + 0.05 * s, cy + 0.95 * s), (cx - 0.15 * s, cy + 0.55 * s), (cx - 0.6 * s, cy + 0.2 * s), (cx - 0.55 * s, cy - 0.35 * s),
                 (cx - 0.05 * s, cy - 0.55 * s), (cx + 0.45 * s, cy - 0.3 * s), (cx + 0.4 * s, cy + 0.2 * s), (cx + 0.1 * s, cy + 0.42 * s)]
        segs = [(0.0, 0.17, col("shf_a")), (0.17, 0.4, col("shf_a")), (0.4, 0.68, col("fhf")), (0.68, 1.0, col("shf_p"))]
        b = band(ax, curve, lambda f: 0.36 * s * (0.8 + 0.35 * np.sin(np.pi * np.clip((f - 0.15) / 0.6, 0, 1))), segs, z=z + 1,
                 lumen=0.45)
        A.update(oft=b["at"](0.08), rv=b["at"](0.3), lv=b["at"](0.53), atria=b["at"](0.86), arterial=b["at"](0.0),
                 venous=b["at"](1.0))
        return A

    if stage == "chambers":
        # frontal section: RA and RV on the viewer's left, LA and LV on the right
        def blobp(c, rx, ry, seed, ang=0.0):
            return blob(c, rx, ry, wobble=0.04, seed=seed, k=10, angle=ang)

        wall = 0.11 * s
        parts = [("ra", (cx - 0.5 * s, cy + 0.35 * s), 0.38 * s, 0.33 * s, col("shf_p"), 0.2),
                 ("la", (cx + 0.52 * s, cy + 0.38 * s), 0.36 * s, 0.3 * s, col("shf_p"), -0.2),
                 ("rv", (cx - 0.38 * s, cy - 0.35 * s), 0.45 * s, 0.42 * s, col("shf_a"), -0.4),
                 ("lv", (cx + 0.3 * s, cy - 0.45 * s), 0.46 * s, 0.52 * s, col("fhf"), 0.5)]
        for i, (k, c, rx, ry, t, ang) in enumerate(parts):
            o = blobp(c, rx, ry, i + 3, ang)
            _poly(ax, o, t, z=z + 1, lw=LINE * 0.9)
            ii = blobp(c, rx - wall, ry - wall, i + 3, ang)
            _poly(ax, ii, "blood", z=z + 1.2, lw=0.6, face=_wash("blood", 0.75, 0.75), edge=P.edge(tok("endocardium")))
            A[k] = c
        # outflow vessels: aorta from LV (arches to the viewer's left over the top), pulmonary trunk from RV
        ao = _bezier([(cx + 0.05 * s, cy - 0.05 * s), (cx + 0.05 * s, cy + 0.75 * s), (cx - 0.25 * s, cy + 1.05 * s), (cx - 0.7 * s, cy + 0.95 * s)], 80)
        pt = _bezier([(cx - 0.2 * s, cy - 0.05 * s), (cx - 0.05 * s, cy + 0.55 * s), (cx + 0.35 * s, cy + 0.85 * s), (cx + 0.75 * s, cy + 0.9 * s)], 80)
        band(ax, pt, 0.2 * s, [(0, 1, "vein")], z=z + 0.6, lumen=0.5, smooth=False)
        band(ax, ao, 0.22 * s, [(0, 1, "artery")], z=z + 0.7, lumen=0.5, smooth=False)
        if fields:  # crest-derived septum at the base of the great arteries
            ax.add_patch(Ellipse((cx - 0.06 * s, cy + 0.2 * s), 0.16 * s, 0.32 * s, facecolor=P.fill(tok("crest")), edgecolor=P.edge(tok("crest")),
                                 lw=0.6, zorder=z + 1.5))
        # septa and valves
        ax.plot([cx - 0.02 * s, cx - 0.1 * s], [cy - 0.05 * s, cy - 0.85 * s], color=P.edge(tok(col("fhf"))), lw=LINE * 2.2, zorder=z + 1.6,
                solid_capstyle="round")
        for (x0, y0), (x1, y1) in (((cx - 0.75 * s, cy + 0.05 * s), (cx - 0.3 * s, cy + 0.08 * s)),
                                   ((cx + 0.25 * s, cy + 0.12 * s), (cx + 0.75 * s, cy + 0.1 * s))):
            ax.plot([x0, x1], [y0, y1], color=P.edge(tok("cushion")), lw=LINE * 2.0, zorder=z + 1.7, solid_capstyle="round")
        ax.plot([cx - 0.02 * s, cx + 0.03 * s], [cy + 0.1 * s, cy + 0.65 * s], color=P.muted(), lw=LINE * 1.2, zorder=z + 1.6,
                ls=(0, (2, 1.4)))
        if fields:  # epicardium around the ventricles
            o = np.vstack([blobp((cx - 0.38 * s, cy - 0.35 * s), 0.49 * s, 0.46 * s, 3 + 2, -0.4)])
            ax.plot(*o.T, color=P.edge(tok("epicardium")), lw=LINE * 1.4, zorder=z + 0.9)
            o = blobp((cx + 0.3 * s, cy - 0.45 * s), 0.5 * s, 0.56 * s, 3 + 3, 0.5)
            ax.plot(*o.T, color=P.edge(tok("epicardium")), lw=LINE * 1.4, zorder=z + 0.9)
        A.update(aorta=tuple(ao[-1]), pulmonary=tuple(pt[-1]), septum=(cx - 0.06 * s, cy - 0.5 * s), av_valve=(cx - 0.5 * s, cy + 0.06 * s),
                 oft_septum=(cx - 0.06 * s, cy + 0.2 * s), foramen=(cx + 0.02 * s, cy + 0.45 * s), epicardium=(cx + 0.3 * s, cy - 0.98 * s))
        return A
    raise ValueError(f"unknown stage {stage!r}")


# ------------------------------------------------------------------------------------------------- vessels


def blood_island(ax, center, r=0.8, n=7, seed=1, z=6):
    """A yolk-sac blood island: round primitive blood cells inside a ring of flattened angioblasts."""
    rng = np.random.default_rng(seed)
    cx, cy = center
    ax.add_patch(Circle(center, r, facecolor=_wash("blood", 0.8, 0.82), edgecolor="none", zorder=z - 0.5))
    m = 12
    for k in range(m):
        a = 2 * math.pi * k / m
        c = (cx + r * math.cos(a), cy + r * math.sin(a))
        ax.add_patch(Ellipse(c, 2 * math.pi * r / m * 1.05, 0.22 * r, angle=math.degrees(a) + 90, facecolor=P.fill(tok("angioblast")),
                             edgecolor=P.edge(tok("angioblast")), lw=0.6, zorder=z))
        _nucleus(ax, c, 0.06 * r, "angioblast", z + 0.1)
    pts = []
    while len(pts) < n:
        p = rng.uniform(-0.62, 0.62, 2) * r
        if np.hypot(*p) < 0.62 * r and all(np.hypot(*(p - q)) > 0.36 * r for q in pts):
            pts.append(p)
    for p in pts:
        _circ(ax, (cx + p[0], cy + p[1]), 0.17 * r, "blood_cell", z + 0.2, lw=0.6)
        _nucleus(ax, (cx + p[0], cy + p[1]), 0.06 * r, "blood_cell", z + 0.3)
    return {"center": center, "angioblast": (cx + r, cy), "blood": (cx + pts[0][0], cy + pts[0][1]), "r": r}


def plexus(ax, box, cell=0.9, width=0.16, token="endothelium", seed=2, z=5, blood=True):
    """A primary capillary plexus: a jittered honeycomb of vessel segments filling ``box`` = (x, y, w, h)."""
    x, y, w, h = box
    rng = np.random.default_rng(seed)
    dx, dy = cell, cell * math.sqrt(3) / 2
    nodes = {}
    for j in range(int(h / dy) + 2):
        for i in range(int(w / dx) + 2):
            px = x + i * dx + (dx / 2 if j % 2 else 0) + rng.uniform(-0.18, 0.18) * dx
            py = y + j * dy + rng.uniform(-0.18, 0.18) * dy
            nodes[(i, j)] = (min(max(px, x), x + w), min(max(py, y), y + h))
    edges = []
    for (i, j), p in nodes.items():
        for nb in ((i + 1, j), (i, j + 1), (i + (1 if j % 2 else -1), j + 1)):
            if nb in nodes and rng.random() > 0.18:
                edges.append((p, nodes[nb]))
    t = tok(token)
    for a, b in edges:
        ax.plot([a[0], b[0]], [a[1], b[1]], color=P.edge(t), lw=width * 72 * 0.45 * 1.25, solid_capstyle="round", zorder=z)
    for a, b in edges:
        ax.plot([a[0], b[0]], [a[1], b[1]], color=_wash("blood", 0.55, 0.6) if blood else P.fill(t), lw=width * 72 * 0.45 * 0.75,
                solid_capstyle="round", zorder=z + 0.1)
    return {"edges": edges, "center": (x + w / 2, y + h / 2)}


def sprout(ax, base, angle=90.0, length=2.5, stalk=3, width=0.42, parent=True, filopodia=7, seed=3, z=7):
    """A sprouting vessel growing from a parent vessel at ``base`` in direction ``angle`` (degrees).

    The leading tip cell (token "tip") extends filopodia; ``stalk`` stalk cells (endothelium) behind it form the
    lumenized trunk. ``parent=True`` draws a horizontal parent vessel through ``base``. Returns anchors tip, stalk,
    filopodium, parent.
    """
    rng = np.random.default_rng(seed)
    a = math.radians(angle)
    d = np.array([math.cos(a), math.sin(a)])
    n = np.array([-d[1], d[0]])
    b = np.asarray(base, float)
    A = {}
    if parent:
        L = length * 0.95
        pv = np.array([b - [L, 0], b + [L, 0]])
        band(ax, pv, width * 1.25, [(0, 1, "endothelium")], z=z - 1, lumen=0.55, smooth=False)
        A["parent"] = tuple(b - [L * 0.6, 0])
    ls = length * 0.72
    trunk = np.array([b, b + d * ls])
    band(ax, trunk, width, [(0, 1, "endothelium")], z=z, lumen=0.45, smooth=False)
    for k in range(1, stalk):
        p = b + d * ls * k / stalk
        ax.plot(*np.array([p + n * width / 2, p - n * width / 2]).T, color=P.edge(tok("endothelium")), lw=0.7, zorder=z + 0.3)
    for k in range(stalk):
        _nucleus(ax, tuple(b + d * ls * (k + 0.5) / stalk + n * width * 0.3 * (1 if k % 2 else -1)), width * 0.13, "endothelium", z + 0.4)
    tipc = b + d * (ls + length * 0.16)
    o = blob(tuple(tipc), length * 0.2, width * 0.62, wobble=0.12, seed=seed, k=9, angle=a)
    _poly(ax, o, "tip", z=z + 0.5)
    _nucleus(ax, tuple(tipc), width * 0.15, "tip", z + 0.6)
    t = tok("tip")
    ends = []
    for k in range(filopodia):
        ang = a + rng.uniform(-0.75, 0.75)
        st = tipc + d * length * 0.15 + n * rng.uniform(-0.15, 0.15) * width
        en = st + np.array([math.cos(ang), math.sin(ang)]) * length * rng.uniform(0.18, 0.34)
        ax.plot([st[0], en[0]], [st[1], en[1]], color=P.edge(t), lw=0.8, zorder=z + 0.4, solid_capstyle="round")
        ends.append(en)
    A.update(tip=tuple(tipc), stalk=tuple(b + d * ls * 0.5), filopodium=tuple(ends[0]), front=tuple(tipc + d * length * 0.45))
    return A


def aorta_section(ax, center, r=1.5, clusters=True, z=6):
    """Transverse section of the embryonic dorsal aorta (dorsal up): endothelium, hemogenic endothelium on the
    ventral floor, cells rounding up (endothelial-to-hematopoietic transition) and intra-aortic clusters.
    Returns anchors endothelium, hemogenic, cluster, lumen, mesenchyme."""
    cx, cy = center
    ax.add_patch(Circle(center, r * 1.55, facecolor=_wash("mesenchyme", 0.72, 0.82), edgecolor="none", zorder=z - 1))
    ax.add_patch(Circle(center, r, facecolor=_wash("blood", 0.82, 0.8), edgecolor="none", zorder=z - 0.5))
    m = 18
    for k in range(m):
        a = 2 * math.pi * (k + 0.5) / m
        hemo = math.sin(a) < -0.55
        t = "hemogenic" if hemo else "endothelium"
        c = (cx + r * math.cos(a), cy + r * math.sin(a))
        ax.add_patch(Ellipse(c, 2 * math.pi * r / m * 1.04, (0.24 if hemo else 0.13) * r, angle=math.degrees(a) + 90,
                             facecolor=P.fill(tok(t)), edgecolor=P.edge(tok(t)), lw=0.6, zorder=z))
        _nucleus(ax, c, 0.05 * r, t, z + 0.1)
    A = {"endothelium": (cx, cy + r), "hemogenic": (cx, cy - r), "lumen": (cx, cy + 0.3 * r), "mesenchyme": (cx + 1.35 * r, cy - 0.6 * r),
         "r": r}
    if clusters:
        for k, (dxf, dyf) in enumerate(((-0.28, -0.7), (-0.1, -0.62), (0.1, -0.66), (-0.18, -0.46), (0.03, -0.45))):
            c = (cx + dxf * r, cy + dyf * r)
            _circ(ax, c, 0.11 * r, "hsc", z + 0.3, lw=0.6)
            _nucleus(ax, c, 0.05 * r, "hsc", z + 0.4)
        A["cluster"] = (cx - 0.08 * r, cy - 0.55 * r)
        c = (cx + 0.55 * r, cy - 0.72 * r)  # a cell rounding up out of the floor
        _circ(ax, c, 0.12 * r, "hemogenic", z + 0.35, lw=0.6)
        _nucleus(ax, c, 0.05 * r, "hemogenic", z + 0.4)
        A["eht"] = c
    return A


# ------------------------------------------------------------------------------------------------- endoderm


def gut_tube(ax, start, length=12.0, h=0.5, buds=True, pouches=4, z=5):
    """Lateral view of the primitive gut tube (anterior left, dorsal up), about the fifth week of human development.

    The tube (endoderm) runs from the oropharyngeal membrane at ``start`` to the cloaca; ``buds=True`` adds the
    thyroid diverticulum, the pharyngeal pouches, the lung bud with trachea, the stomach, the hepatic diverticulum
    with the gallbladder, the dorsal and ventral pancreatic buds, the yolk stalk and the allantois. Returns anchors
    (pharynx, pouch1.., thyroid, lung, trachea, esophagus, stomach, liver, gallbladder, dorsal_pancreas,
    ventral_pancreas, midgut, yolk_stalk, hindgut, allantois, cloaca, foregut_end, midgut_end) and ``x(f)``.
    """
    x0, y0 = start
    L = length

    def X(f):
        return x0 + f * L

    # centre line: pharynx, esophagus, stomach (dorsal bend), duodenum, midgut loop towards the yolk stalk, hindgut
    cl = [(X(0.0), y0), (X(0.1), y0 + 0.05), (X(0.2), y0 + 0.1), (X(0.3), y0 + 0.05), (X(0.38), y0 - 0.05),
          (X(0.48), y0 - 0.2), (X(0.58), y0 - 0.55), (X(0.66), y0 - 0.65), (X(0.75), y0 - 0.45), (X(0.85), y0 - 0.1),
          (X(0.95), y0 - 0.15), (X(1.0), y0 - 0.35)]

    def width(f):
        w = np.full_like(f, h)
        w = w + 0.9 * h * np.exp(-((f - 0.06) / 0.07) ** 2)      # pharynx
        w = w + 1.0 * h * np.exp(-((f - 0.37) / 0.045) ** 2)     # stomach
        w = w + 0.6 * h * np.exp(-((f - 0.985) / 0.03) ** 2)     # cloaca
        return w

    b = band(ax, cl, width, [(0, 1, "endoderm")], z=z + 1, lumen=0.45)
    at = b["at"]
    A = {"x": X}
    A.update(pharynx=at(0.06), esophagus=at(0.25), stomach=at(0.37), midgut=at(0.66), hindgut=at(0.88), cloaca=at(0.99),
             foregut_end=at(0.44), midgut_end=at(0.8))
    if not buds:
        return A

    sc = h / 0.5  # bud sizes scale with the tube

    def bud(f, side, length_, wid, tissue, ang=0.0, z_=z + 0.9):
        length_, wid = length_ * sc, wid * sc
        p = np.asarray(at(f, side * 0.85))
        nrm = b["nrm"][int(round(f * (len(b["q"]) - 1)))] * side
        a = math.atan2(nrm[1], nrm[0]) + math.radians(ang)
        d = np.array([math.cos(a), math.sin(a)])
        cur = np.array([p - d * 0.1, p + d * length_ * 0.6, p + d * length_])
        bb = band(ax, cur, lambda f_: wid * (1 + 0.6 * f_ ** 2), [(0, 1, tissue)], z=z_, lumen=0.35)
        ax.add_patch(Circle(tuple(cur[-1]), wid * 0.8, facecolor=P.fill(tok(tissue)), edgecolor=P.edge(tok(tissue)), lw=LINE * 0.8,
                            zorder=z_ + 0.05))
        return tuple(cur[-1]), bb

    for k in range(pouches):  # pharyngeal pouches as dorsolateral outpockets
        f = 0.025 + k * 0.028
        tip, _ = bud(f, 1, 0.45 + 0.05 * (k == 2), 0.17, "endoderm", ang=-8)
        A[f"pouch{k + 1}"] = tip
    A["thyroid"], _ = bud(0.05, -1, 0.75, 0.16, "thyroid", ang=10)
    A["lung"], lb = bud(0.16, -1, 1.15, 0.22, "lung", ang=25)
    A["trachea"] = lb["at"](0.4)
    A["liver"], lv = bud(0.46, -1, 1.15, 0.3, "liver", ang=-15)
    A["gallbladder"] = (A["liver"][0] + 0.45 * sc, A["liver"][1] + 0.05)
    ax.add_patch(Ellipse(A["gallbladder"], 0.42 * sc, 0.26 * sc, facecolor=P.fill(tok("gallbladder")), edgecolor=P.edge(tok("gallbladder")),
                         lw=LINE * 0.8, zorder=z + 1.2))
    A["ventral_pancreas"], _ = bud(0.49, -1, 0.65, 0.17, "pancreas", ang=30)
    A["dorsal_pancreas"], _ = bud(0.48, 1, 0.75, 0.2, "pancreas", ang=10)
    # yolk stalk from the midgut, allantois from the hindgut (ventral)
    ys = np.asarray(at(0.66, -0.9))
    cur = np.array([ys, ys + [0.05, -0.8], ys + [0.0, -1.45]])
    band(ax, cur, 0.22, [(0, 1, "endoderm")], z=z + 0.8, lumen=0.35, smooth=False)
    ax.add_patch(Circle(tuple(cur[-1] + [0, -0.45]), 0.5, facecolor=_wash("yolk", 0.35, 0.6), edgecolor=P.edge(tok("yolk")),
                 lw=LINE * 0.8, zorder=z + 0.7))
    A["yolk_stalk"] = tuple(cur[1])
    al = np.asarray(at(0.965, -0.85))
    cur = np.array([al, al + [0.35, -0.55], al + [0.85, -0.85]])
    band(ax, cur, 0.2, [(0, 1, "allantois")], z=z + 0.8, lumen=0.35, smooth=False)
    A["allantois"] = tuple(cur[-1])
    return A


def pharynx(ax, center, w=6.0, h=7.0, arches=4, z=5):
    """Frontal (horizontal) section through the pharyngeal region, anterior (rostral) up.

    The endodermal pharynx runs down the middle; on each side ``arches`` arches (crest mesenchyme with a
    mesodermal core and an arch artery) are separated by endodermal pouches (inside) that meet ectodermal clefts
    (outside). Returns anchors arch1.., pouch1.., cleft1.., artery1.., core1.., lumen, plus left-side variants
    (``"pouch3_l"`` etc.).
    """
    cx, cy = center
    A = {}
    y_top, y_bot = cy + h / 2, cy - h / 2
    ys = np.linspace(y_top - h * 0.1, y_bot + h * 0.16, arches + 1)  # boundaries between arches: pouch levels
    # outer ectoderm outline (scalloped by arches)
    for sg, suff in ((1, ""), (-1, "_l")):
        out = [(cx, y_top)]
        for k in range(arches):
            ya, yb = ys[k], ys[k + 1]
            bulge = w * (0.47 - 0.035 * k)
            out += [(cx + sg * w * 0.28, ya), (cx + sg * bulge, (ya + yb) / 2 + 0.05 * h), (cx + sg * w * 0.3, yb)]
        out += [(cx + sg * w * 0.2, y_bot), (cx, y_bot)]
        o = _bezier(out, 240)
        # ectoderm rim and mesenchyme fill
        _poly(ax, np.vstack([o, [(cx, y_bot), (cx, y_top)]]), "crest", z=z, lw=0, face=_wash("crest", 0.45, 0.7), edge="none")
        ax.plot(*o.T, color=P.edge(tok("ectoderm")), lw=LINE * 2.2, zorder=z + 0.4, solid_capstyle="round")
        for k in range(arches):
            ya, yb = ys[k], ys[k + 1]
            core = ((cx + sg * w * 0.33), (ya + yb) / 2 + 0.05 * h)
            ax.add_patch(Ellipse(core, w * 0.1, (ya - yb) * 0.35, facecolor=_wash("mesoderm", 0.4, 0.65), edgecolor=P.edge(tok("mesoderm")),
                                 lw=0.6, zorder=z + 0.5))
            art = (cx + sg * w * 0.24, (ya + yb) / 2 + 0.05 * h)
            _circ(ax, art, w * 0.03, "artery", z + 0.6, lw=0.6)
            A[f"arch{k + 1}{suff}"] = (cx + sg * w * 0.4, (ya + yb) / 2 + 0.05 * h)
            A[f"core{k + 1}{suff}"] = core
            A[f"artery{k + 1}{suff}"] = art
        # clefts (ectodermal grooves) at the arch boundaries
        for k in range(1, arches + 1):
            yk = ys[k]
            xo = cx + sg * w * 0.3
            ax.plot([xo, xo - sg * w * 0.05], [yk, yk], color=P.edge(tok("ectoderm")), lw=LINE * 2.0, zorder=z + 0.45, solid_capstyle="round")
            A[f"cleft{k}{suff}"] = (xo + sg * 0.05, yk)
    # pharyngeal endoderm: lumen with lateral pouches at the arch boundaries
    lum = [(cx - w * 0.06, y_top)]
    right = []
    for k in range(1, arches + 1):
        yk = ys[k]
        right += [(cx + w * 0.1, yk + h * 0.05), (cx + w * 0.24, yk + 0.01 * h), (cx + w * 0.24, yk - 0.01 * h), (cx + w * 0.1, yk - h * 0.05)]
    right = [(cx + w * 0.06, y_top)] + right + [(cx + w * 0.05, y_bot)]
    left = [(2 * cx - x, y) for x, y in right][::-1]
    lum = _bezier(right, 260)
    lum_l = _bezier(left, 260)
    poly = np.vstack([lum, lum_l])
    _poly(ax, poly, "endoderm", z=z + 0.7, lw=LINE * 1.8, face=_wash("fluid", 0.15, 0.55), edge=P.edge(tok("endoderm")))
    for k in range(1, arches + 1):
        A[f"pouch{k}"] = (cx + w * 0.22, ys[k])
        A[f"pouch{k}_l"] = (cx - w * 0.22, ys[k])
    A["lumen"] = (cx, cy)
    A["ys"] = ys
    return A


# ------------------------------------------------------------------------------------------------- gametogenesis


def _cell(ax, c, r, token, z, nucleus=0.35, seed=0, wob=0.05, rx=None, ang=0.0):
    o = blob(c, rx or r, r, wobble=wob, seed=seed, k=8, angle=ang)
    _poly(ax, o, token, z=z, lw=LINE * 0.6)
    if nucleus:
        t = tok(token)
        ax.add_patch(Circle(c, r * nucleus, facecolor=P.light(t), edgecolor=P.edge(t), lw=0.5, zorder=z + 0.1))


def _sperm_mini(ax, head, ang, L, z, token="germ"):
    a = math.radians(ang)
    d = np.array([math.cos(a), math.sin(a)])
    h = np.asarray(head, float)
    t = tok(token)
    ax.add_patch(Ellipse(tuple(h), L * 0.16, L * 0.09, angle=ang, facecolor=P.fill(t), edgecolor=P.edge(t), lw=0.5, zorder=z))
    s = np.linspace(0, 1, 30)
    n = np.array([-d[1], d[0]])
    tail = h[None, :] - d[None, :] * (L * 0.08 + L * s[:, None]) + n[None, :] * (0.04 * L * np.sin(4 * np.pi * s))[:, None]
    ax.plot(tail[:, 0], tail[:, 1], color=P.edge(t), lw=0.55, zorder=z - 0.1)


def seminiferous_tubule(ax, center, r=3.0, seed=4, z=5):
    """Cross-section of a seminiferous tubule: basement membrane and peritubular myoid cells, Sertoli cells spanning
    the epithelium, spermatogonia on the basement membrane, spermatocytes, round and elongating spermatids, sperm
    tails in the lumen; Leydig cells and a capillary in the interstitium. Returns anchors."""
    rng = np.random.default_rng(seed)
    cx, cy = center
    ax.add_patch(Circle(center, r * 1.02, facecolor="none", edgecolor=P.edge(tok("myoid")), lw=LINE * 1.6, zorder=z + 2))
    ax.add_patch(Circle(center, r, facecolor=_wash("sertoli", 0.6, 0.75), edgecolor=P.edge(tok("sertoli")), lw=LINE * 0.8, zorder=z))
    ax.add_patch(Circle(center, r * 0.3, facecolor=_wash("fluid", 0.3, 0.6), edgecolor=P.edge(tok("sertoli")), lw=0.6, zorder=z + 0.1))
    A = {"center": center, "lumen": (cx, cy), "basement": (cx + r * 1.02, cy), "r": r}
    n_s = 9
    for k in range(n_s):  # Sertoli cells: radial columns with basal nuclei
        a = 2 * math.pi * k / n_s + 0.15
        p1 = (cx + r * 0.97 * math.cos(a), cy + r * 0.97 * math.sin(a))
        p0 = (cx + r * 0.32 * math.cos(a), cy + r * 0.32 * math.sin(a))
        ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=P.edge(tok("sertoli")), lw=0.6, zorder=z + 0.2)
        nc = (cx + r * 0.82 * math.cos(a + 0.12), cy + r * 0.82 * math.sin(a + 0.12))
        ax.add_patch(Ellipse(nc, r * 0.13, r * 0.07, angle=math.degrees(a), facecolor=P.edge(tok("sertoli")), edgecolor="none", zorder=z + 0.3))
        if k == 0:
            A["sertoli"] = nc
    layers = [(0.9, 0.075, 16, "spermatogonium", 1.0), (0.7, 0.095, 12, "spermatocyte", 0.9), (0.5, 0.055, 20, "spermatid", 0.55)]
    for rr, cr, n, key, nucf in layers:
        for k in range(n):
            a = 2 * math.pi * (k + rng.uniform(-0.2, 0.2)) / n
            c = (cx + r * rr * math.cos(a), cy + r * rr * math.sin(a))
            _cell(ax, c, cr * r, "germ", z + 0.5, nucleus=0.45 * nucf, seed=k + int(rr * 10), wob=0.06)
            if k == 0:
                A[key] = c
    for k in range(14):  # elongated spermatids at the lumen with tails into it
        a = 2 * math.pi * k / 14 + 0.1
        head = (cx + r * 0.34 * math.cos(a), cy + r * 0.34 * math.sin(a))
        _sperm_mini(ax, head, math.degrees(a) + 180, r * 0.25, z + 0.6)
        if k == 0:
            A["sperm"] = head
    for k, a in enumerate((0.8, 2.6, 4.3)):  # interstitium: Leydig cells
        c = (cx + r * 1.22 * math.cos(a), cy + r * 1.22 * math.sin(a))
        for j in range(3):
            cc = (c[0] + 0.18 * r * math.cos(a + 1.5 + j * 1.6), c[1] + 0.18 * r * math.sin(a + 1.5 + j * 1.6))
            _cell(ax, cc, 0.08 * r, "leydig", z + 0.2, nucleus=0.45, seed=20 + 3 * k + j)
        if k == 0:
            A["leydig"] = c
    cap = (cx + r * 1.2 * math.cos(3.6), cy + r * 1.2 * math.sin(3.6))
    _circ(ax, cap, 0.09 * r, "artery", z + 0.2, lw=0.8, face=_wash("blood", 0.6, 0.6))
    A["capillary"] = cap
    A["myoid"] = (cx + r * 1.02 * math.cos(-0.7), cy + r * 1.02 * math.sin(-0.7))
    return A


def germ_lineage(ax, start, kind="sperm", step=2.2, r=0.38, z=6):
    """A row of stages: kind "sperm": spermatogonium (type B), primary spermatocyte, two secondary spermatocytes,
    four spermatids, four sperm, joined by cytoplasmic bridges; kind "egg": oogonium, primary oocyte (grown),
    secondary oocyte with the first polar body, egg (ootid) with the second polar body. Returns the centre of each
    stage under its name (gonium, primary, secondary, spermatid / egg, sperm) and ``y``."""
    x, y = start
    A = {"y": y}
    if kind == "sperm":
        _cell(ax, (x, y), r, "germ", z, seed=1)
        A["gonium"] = (x, y)
        _cell(ax, (x + step, y), r * 1.25, "germ", z, seed=2)
        A["primary"] = (x + step, y)
        cols = [(2, r * 1.0, 0.75), (4, r * 0.72, 0.42)]
        for j, (m, rr, sp) in enumerate(cols):
            xs = x + step * (2 + j)
            yy = y + (np.arange(m) - (m - 1) / 2) * sp * 2.2 * r / 0.9
            for k, yk in enumerate(yy):
                _cell(ax, (xs, yk), rr, "germ", z, seed=10 * j + k, nucleus=0.42)
                if k:
                    ax.plot([xs, xs], [yy[k - 1] + rr * 0.95, yk - rr * 0.95], color=P.edge(tok("germ")), lw=LINE * 1.6, zorder=z - 0.1)
            A["secondary" if j == 0 else "spermatid"] = (xs, y)
            A[("secondary" if j == 0 else "spermatid") + "_top"] = (xs, yy[-1] + rr)
        xs = x + step * 4
        for k, yk in enumerate(y + (np.arange(4) - 1.5) * 0.42 * 2.2 * r / 0.9):
            _sperm_mini(ax, (xs + 0.25, yk), 0, r * 2.2, z)
        A["sperm"] = (xs, y)
        return A
    # oogenesis
    _cell(ax, (x, y), r, "germ", z, seed=1)
    A["gonium"] = (x, y)
    t = tok("oocyte")
    for j, (rr, pb) in enumerate(((r * 1.9, 0), (r * 1.9, 1), (r * 1.8, 2))):
        c = (x + step * (1 + j) + (j > 0) * 0.15, y)
        ax.add_patch(Circle(c, rr * 1.12, facecolor=_wash("zona", 0.45, 0.6), edgecolor=P.edge(tok("zona")), lw=0.7, zorder=z - 0.2))
        ax.add_patch(Circle(c, rr, facecolor=P.fill(t), edgecolor=P.edge(tok("germ")), lw=LINE * 0.8, zorder=z))
        if j == 0:
            ax.add_patch(Circle(c, rr * 0.33, facecolor=P.light(tok("germ")), edgecolor=P.edge(tok("germ")), lw=0.6, zorder=z + 0.1))
        else:
            ax.add_patch(Circle((c[0] + rr * 0.55, c[1] + rr * 0.55), rr * 0.09, facecolor=P.edge(tok("germ")), edgecolor="none", zorder=z + 0.2))
        for k in range(pb):
            pc = (c[0] + rr * (0.75 - 0.42 * k), c[1] + rr * (0.72 + 0.12 * k) + 0.04)
            _circ(ax, pc, rr * 0.16, "germ", z + 0.3, lw=0.6)
        A[("primary", "secondary", "egg")[j]] = c
        A[("primary", "secondary", "egg")[j] + "_top"] = (c[0], c[1] + rr * 1.15)
    return A


def follicle(ax, center, r=1.5, stage="antral", seed=5, z=5):
    """An ovarian follicle at ``stage`` "primordial" (oocyte with a flat layer of pregranulosa cells),
    "primary" (one cuboidal granulosa layer, zona pellucida), "secondary" (several layers, theca) or "antral"
    (Graafian: antrum, cumulus oophorus, theca interna and externa). ``r`` is the outer radius for "antral" and
    scales the others. Returns anchors oocyte, zona, granulosa, theca, antrum, cumulus."""
    rng = np.random.default_rng(seed)
    cx, cy = center
    A = {}
    g = tok("granulosa")
    ro = {"primordial": 0.28, "primary": 0.34, "secondary": 0.38, "antral": 0.3}[stage] * r
    oc = (cx - 0.25 * r, cy + 0.12 * r) if stage == "antral" else (cx, cy)
    if stage in ("secondary", "antral"):
        rt = (0.95 if stage == "antral" else 0.8) * r
        ax.add_patch(Circle(center, rt, facecolor=_wash("theca", 0.55, 0.72), edgecolor=P.edge(tok("theca")), lw=LINE * 0.7, zorder=z))
        A["theca"] = (cx + rt * 0.92, cy - rt * 0.3)
    if stage == "antral":
        rg = 0.8 * r
        ax.add_patch(Circle(center, rg, facecolor=P.fill(g), edgecolor=P.edge(g), lw=LINE * 0.7, zorder=z + 0.2))
        an = blob((cx + 0.12 * r, cy - 0.05 * r), 0.6 * r, 0.56 * r, wobble=0.04, seed=seed, k=9)
        _poly(ax, an, "fluid", z=z + 0.3, lw=0.6, face=_wash("fluid", 0.15, 0.55), edge=P.edge(g))
        cum = blob(oc, ro * 1.75, ro * 1.6, wobble=0.06, seed=seed + 1, k=8)
        _poly(ax, cum, g, z=z + 0.4, lw=0.6)
        A.update(antrum=(cx + 0.35 * r, cy - 0.25 * r), cumulus=(oc[0] - ro * 1.45, oc[1] - ro * 0.7), granulosa=(cx + 0.74 * r, cy + 0.2 * r))
        for k in range(60):  # granulosa cell nuclei in the mural layer
            a = 2 * math.pi * k / 60
            rr = rg * rng.uniform(0.84, 0.95)
            ax.add_patch(Circle((cx + rr * math.cos(a), cy + rr * math.sin(a)), 0.018 * r, facecolor=P.edge(g), edgecolor="none", zorder=z + 0.25))
    else:
        layers = {"primordial": 1, "primary": 1, "secondary": 3}[stage]
        thick = (0.06 if stage == "primordial" else 0.11) * r
        rg = ro * 1.12 + thick * layers
        ax.add_patch(Circle(oc, rg, facecolor=P.fill(g), edgecolor=P.edge(g), lw=LINE * 0.7, zorder=z + 0.2))
        for L in range(layers):
            rr = ro * 1.12 + thick * (L + 0.5)
            m = int(2 * math.pi * rr / (thick * (2.2 if stage == "primordial" else 1.1)))
            for k in range(m):
                a = 2 * math.pi * (k + 0.5 * (L % 2)) / m
                if stage == "primordial":
                    ax.add_patch(Ellipse((oc[0] + rr * math.cos(a), oc[1] + rr * math.sin(a)), thick * 1.8, thick * 0.55, angle=math.degrees(a) + 90,
                                         facecolor=P.edge(g), edgecolor="none", zorder=z + 0.3))
                else:
                    ax.add_patch(Circle((oc[0] + rr * math.cos(a), oc[1] + rr * math.sin(a)), thick * 0.22, facecolor=P.edge(g), edgecolor="none",
                                        zorder=z + 0.3))
        A["granulosa"] = (oc[0] + rg * 0.95, oc[1])
    if stage != "primordial":
        ax.add_patch(Circle(oc, ro * 1.12, facecolor=_wash("zona", 0.4, 0.55), edgecolor=P.edge(tok("zona")), lw=0.6, zorder=z + 0.5))
        A["zona"] = (oc[0], oc[1] + ro * 1.08)
    ax.add_patch(Circle(oc, ro, facecolor=P.fill(tok("oocyte")), edgecolor=P.edge(tok("germ")), lw=LINE * 0.8, zorder=z + 0.6))
    ax.add_patch(Circle((oc[0] + 0.15 * ro, oc[1] + 0.1 * ro), 0.32 * ro, facecolor=P.light(tok("germ")), edgecolor=P.edge(tok("germ")),
                        lw=0.6, zorder=z + 0.7))
    A["oocyte"] = oc
    A["center"] = center
    return A


__all__ = ["TISSUE", "tok", "band", "heart", "blood_island", "plexus", "sprout", "aorta_section", "gut_tube", "pharynx",
           "seminiferous_tubule", "germ_lineage", "follicle"]

