"""Cell junctions, cell adhesion, the extracellular matrix and the plant cell wall (7.3.23).

    from wikibio import junctions as J
    a = J.epithelium(ax, 1, 13, 1.2, 6.0, n=3)            columnar cells on a basal lamina with the junctional
                                                           complex; returns anchors per junction type
    J.adherens_junction(ax, 6, 1, 6, pairs=3)             cadherin pairs, catenins, vinculin and an actin bundle
    J.desmosome(ax, 6, 1, 6)                               desmosomal cadherins, dense plaques, keratin loops
    J.tight_junction(ax, 6, 1, 6, strands=4)               kissing points of claudin strands between two membranes
    J.gap_junction(ax, 6, 1, 6, connexons=4)               paired connexons spanning a 3 nm gap
    J.hemidesmosome(ax, 1, 7, 3)                           alpha6beta4 integrin and plectin on a basal lamina
    J.focal_adhesion(ax, 1, 9, 3)                          integrins on fibronectin, talin, vinculin, a stress fiber
    J.integrin(ax, (4, 3), state="open")                  one alpha-beta heterodimer: "bent", "closed", "open"
    J.cadherin(ax, base, direction)                        one cadherin ectodomain (five EC domains, Ca2+ ions)
    J.triple_helix(ax, (1, 1), (8, 1))                     three intertwined collagen chains
    J.collagen_fibril(ax, (1, 1), 10, rows=5)              quarter-staggered tropocollagen molecules (D period)
    J.banded_fibril(ax, (1, 1), (8, 1))                    a fibril with gap/overlap banding
    J.proteoglycan(ax, (1, 1), (4, 1), chains=8)           a bottlebrush: core protein with GAG chains
    J.aggrecan_aggregate(ax, (1, 3), (11, 3), n=6)        aggrecan molecules bound to a hyaluronan chain
    J.laminin(ax, (3, 3), 1.0)                             cross-shaped heterotrimer with LG domains
    J.fibronectin(ax, (1, 1), (6, 1))                      disulfide-linked dimer of repeats with the RGD loop
    J.basal_lamina(ax, 1, 11, 2.0, depth=0.8)              laminin layer, type IV collagen net, nidogen, perlecan
    J.elastin(ax, (3, 3), 2.0, 1.4, stretch=0.0)           cross-linked random-coil network (stretch 0..1)
    J.cellulose_synthase(ax, (3, 3), 0.25)                 rosette of six lobes in face view
    J.band(ax, [(0, 2), (9, 2)]); J.globule(ax, (3, 3), 0.2, 0.15, "talin"); J.rope(ax, pts)   membrane, protein, keratin
    J.wall_face(ax, 1, 1, 6, 4)                            primary wall in face view: microfibrils, tethers, pectin
    J.wall_section(ax, 1, 11, 2.0)                         wall in section: middle lamella, primary and secondary walls
    J.plasmodesma(ax, (6, 3), wall=0.9, length=2.4)       a channel through a wall with its desmotubule

Colours are palette tokens chosen once in ``TOKENS`` (cadherin, catenins, vinculin, intermediate filaments,
claudin, connexin, integrin chains, talin, the matrix proteins, the wall polymers); a script can override any
of them by name. Every function is deterministic and returns anchors (points or dicts of points) for arrows
and callouts. Junction close-ups between two cells are drawn with the two plasma membranes vertical (cell 1
on the left, cell 2 on the right); cell-matrix junctions with the membrane horizontal and the cell above.
"""

import math

import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, PathPatch, Polygon
from matplotlib.path import Path

from . import palette as P
from .core import LINE, blob, label, polyline

MT = 0.14  # membrane band thickness (canvas units)

# object -> palette token (one place to change when the palette gains dedicated tokens)
TOKENS = {
    "membrane": "membrane",
    "cytoplasm": "cytoplasm",
    "space": "extracellular",
    "cadherin": "receptor",
    "desmo_cadherin": "drug",
    "p120": "lipid",
    "beta_catenin": "antibody",
    "alpha_catenin": "highlight",
    "vinculin": "enzyme",
    "actin": "actin",
    "if": "positive",            # intermediate filaments (keratin)
    "plaque": "golgi",           # plakoglobin, plakophilin
    "desmoplakin": "lipid",
    "claudin": "channel",
    "occludin": "na",
    "zo": "neutral",
    "connexin": "metabolite",
    "integrin_a": "protein",
    "integrin_b": "dna2",
    "talin": "antibody",
    "kindlin": "drug",
    "fak": "highlight",
    "plectin": "lipid",
    "col17": "rrna",
    "collagen": "rrna",
    "collagen_iv": "rrna",
    "laminin": "channel",
    "nidogen": "neutral",
    "fibronectin": "enzyme",
    "rgd": "highlight",
    "elastin": "k",
    "crosslink": "highlight",
    "hyaluronan": "carbohydrate",
    "gag": "carbohydrate",
    "core_protein": "protein",
    "link_protein": "highlight",
    "cellulose": "plant",
    "glycan": "golgi",
    "pectin": "carbohydrate",
    "lamella": "bract",
    "wall": "cell_wall",
    "secondary": "bone",
    "csc": "enzyme",
    "microtubule": "channel",
    "er": "er",
    "callose": "highlight",
    "nucleus": "nucleus",
}


def tok(name):
    """The palette token of a junction object (``tok("cadherin")``); unknown names pass through."""
    return TOKENS.get(name, name)


def _f(name):
    return P.fill(tok(name))


def _e(name):
    return P.edge(tok(name))


def _pt(ax, units):
    """Convert a length in canvas units to points (for line widths that must match drawn geometry)."""
    x0, x1 = ax.get_xlim()
    return units * ax.figure.get_figwidth() * 72 / (x1 - x0)


def _frame(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    L = float(np.linalg.norm(b - a))
    u = (b - a) / (L or 1)
    return a, b, L, u, np.array([-u[1], u[0]])


def _band(ax, points, thickness=MT, token="membrane", zorder=5):
    """A membrane along a polyline as a filled band with two outlines; returns (centre points, normals)."""
    pts = np.asarray(points, float)
    n = max(40, int(np.hypot(*np.diff(pts, axis=0).T).sum() / 0.03))
    q, nrm, _ = polyline(pts, n=n)
    a, b = q + nrm * thickness / 2, q - nrm * thickness / 2
    verts = np.vstack([a, b[::-1], a[:1]])
    ax.add_patch(PathPatch(Path(verts, closed=True), facecolor=_f(token), edgecolor="none", zorder=zorder))
    for line in (a, b):
        ax.plot(line[:, 0], line[:, 1], color=_e(token), lw=LINE * 0.7, zorder=zorder + 0.5, solid_capstyle="butt")
    return q, nrm


def _rect(ax, x0, y0, w, h, token, zorder=1, lw=0.0, alpha=1.0):
    ax.add_patch(FancyBboxPatch((x0, y0), w, h, boxstyle="square,pad=0", facecolor=_f(token),
                                edgecolor=_e(token) if lw else "none", lw=lw, zorder=zorder,
                                alpha=alpha if alpha < 0.999 else None))


def _bead(ax, xy, r, token, zorder=12, ry=None, angle=0.0, lw=0.7):
    ax.add_patch(Ellipse(xy, 2 * r, 2 * (ry or r), angle=angle, facecolor=_f(token), edgecolor=_e(token), lw=lw,
                         zorder=zorder))


def _blob(ax, center, rx, ry, token, seed=0, angle=0.0, zorder=12, lw=0.7):
    v = blob(center, rx, ry, wobble=0.07, seed=seed, k=8, angle=angle)
    ax.add_patch(PathPatch(Path(v, closed=True), facecolor=_f(token), edgecolor=_e(token), lw=lw, zorder=zorder))
    return v


def _line(ax, pts, token, lw=2.0, zorder=9, inner=True, ls="-"):
    pts = np.asarray(pts, float)
    ax.plot(pts[:, 0], pts[:, 1], color=_e(token), lw=lw, solid_capstyle="round", zorder=zorder, ls=ls)
    if inner:
        ax.plot(pts[:, 0], pts[:, 1], color=_f(token), lw=lw * 0.45, solid_capstyle="round", zorder=zorder + 0.05, ls=ls)


def _curve(points, n=80):
    """A smooth open curve through control points (Catmull-Rom)."""
    p = np.asarray(points, float)
    if len(p) < 3:
        t = np.linspace(0, 1, n)[:, None]
        return p[0] * (1 - t) + p[-1] * t
    ext = np.vstack([2 * p[0] - p[1], p, 2 * p[-1] - p[-2]])
    out = []
    per = max(4, n // (len(p) - 1))
    for i in range(1, len(ext) - 2):
        p0, p1, p2, p3 = ext[i - 1], ext[i], ext[i + 1], ext[i + 2]
        for t in np.linspace(0, 1, per, endpoint=False):
            t2, t3 = t * t, t * t * t
            out.append(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t2 + (-p0 + 3 * p1 - 3 * p2 + p3) * t3))
    out.append(p[-1])
    return np.array(out)


def band(ax, points, thickness=MT, token="membrane", zorder=5):
    """A membrane along a polyline (filled band with two outlines); returns (centre points, unit normals)."""
    return _band(ax, points, thickness=thickness, token=token, zorder=zorder)


def globule(ax, center, rx, ry, token, seed=0, angle=0.0, zorder=12):
    """A small globular protein (an organic blob in a junction token's colours); returns its outline."""
    return _blob(ax, center, rx, ry, token, seed=seed, angle=angle, zorder=zorder)


def rope(ax, points, width=0.16, strands=3, token="if", zorder=9):
    """An intermediate filament along any curve, drawn as a rope of twisted strands (nonpolar, no end marks)."""
    q, nrm, L = polyline(_curve(points, 120), n=max(80, int(np.hypot(*np.diff(np.asarray(points, float), axis=0).T).sum() * 50)))
    s = np.linspace(0, L, len(q))
    period = width * 2.4
    edge, fill = _e(token), _f(token)
    for k in range(strands):
        off = np.sin(2 * math.pi * s / period + 2 * math.pi * k / strands) * width * 0.36
        pts = q + nrm * off[:, None]
        ax.plot(pts[:, 0], pts[:, 1], color=edge, lw=width * 72 * 0.22 + 0.6, solid_capstyle="round", zorder=zorder + k * 0.01)
        ax.plot(pts[:, 0], pts[:, 1], color=fill, lw=width * 72 * 0.12, solid_capstyle="round", zorder=zorder + k * 0.01 + 0.005)
    return q


def actin_line(ax, a, b, lw=2.2, token="actin", zorder=9, plus=True):
    """An actin filament as a line with its plus end marked by a bead (overviews and close-ups)."""
    _line(ax, [a, b], token, lw=lw, zorder=zorder)
    if plus:
        ax.add_patch(Circle(b, lw * 0.03, facecolor=_f(token), edgecolor=_e(token), lw=0.6, zorder=zorder + 0.2))
    return np.asarray(b, float)


# ---------------------------------------------------------------------------------------------
# adhesion molecules


def cadherin(ax, base, direction, n=5, domain=0.2, token="cadherin", ca=True, bend=0.12, zorder=12):
    """One cadherin ectodomain from the membrane point ``base`` towards ``direction``: ``n`` EC domains
    (ellipses) on a gently curved rod, with Ca2+ ions (small dots) in the linkers. Returns the tip point."""
    d = np.asarray(direction, float)
    d = d / np.linalg.norm(d)
    nrm = np.array([-d[1], d[0]])
    base = np.asarray(base, float)
    pts = []
    for k in range(n):
        t = (k + 0.5) / n
        pts.append(base + d * (k + 0.5) * domain * 1.7 + nrm * bend * math.sin(math.pi * t) * domain * 2)
    ang = math.degrees(math.atan2(d[1], d[0]))
    for k, p in enumerate(pts):
        _bead(ax, p, domain * 0.95, token, ry=domain * 0.7, angle=ang, zorder=zorder, lw=0.6)
        if ca and k < n - 1:
            m = (p + pts[k + 1]) / 2
            ax.add_patch(Circle(m + nrm * domain * 0.5, domain * 0.17, facecolor=P.fill("ca"), edgecolor=P.edge("ca"),
                                lw=0.4, zorder=zorder + 0.5))
    return pts[-1] + d * domain * 0.9


def _tail(ax, base, direction, length, token, lw=1.6, zorder=11):
    d = np.asarray(direction, float) / np.linalg.norm(direction)
    p = np.asarray(base, float) + d * length
    _line(ax, [base, p], token, lw=lw, zorder=zorder, inner=False)
    return p


def _membranes(ax, x, y0, y1, gap, thickness=MT, shape=None, zorder=5):
    """Two vertical membranes at x -/+ gap/2 (optionally reshaped by ``shape(y) -> offset``)."""
    ys = np.linspace(y0, y1, 200)
    out = []
    for s in (-1, 1):
        off = np.full_like(ys, gap / 2) if shape is None else shape(ys)
        out.append(_band(ax, np.c_[x + s * off, ys], thickness, zorder=zorder))
    return out


def _space(ax, x, y0, y1, gap, zorder=1):
    _rect(ax, x - gap / 2, y0, gap, y1 - y0, "space", zorder=zorder)


def adherens_junction(ax, x, y0, y1, gap=2.0, pairs=3, actin=True, depth=1.7, zorder=10):
    """Close-up of an adherens junction between cell 1 (left) and cell 2 (right).

    Classical cadherins from both membranes meet tip to tip (strand-swapped EC1 domains) in the
    intercellular space; on each tail p120-catenin binds near the membrane and beta-catenin further in,
    alpha-catenin binds beta-catenin and, with vinculin, links the complex to an actin bundle that runs
    parallel to the membrane (the adhesion belt, cut lengthwise). Returns a dict of anchors.
    """
    _space(ax, x, y0, y1, gap, zorder=zorder - 9)
    _membranes(ax, x, y0, y1, gap, zorder=zorder - 5)
    ys = np.linspace(y0, y1, pairs + 2)[1:-1]
    dom = gap / 2 / 5 / 1.7 * 1.12
    A = {}
    for k, y in enumerate(ys):
        for s in (-1, 1):
            mx = x + s * gap / 2
            tip = cadherin(ax, (mx - s * MT / 2, y), (-s, 0.0), n=5, domain=dom, bend=0.25 * s, zorder=zorder + 2)
            inner = np.array([mx + s * MT / 2, y])
            t = _tail(ax, inner, (s, 0), depth * 0.55, "cadherin", zorder=zorder)
            p120 = inner + np.array([s * 0.28, 0.22])
            _blob(ax, p120, 0.18, 0.12, "p120", seed=k * 3 + (s > 0), zorder=zorder + 3)
            beta = t + np.array([0, 0.0])
            _blob(ax, beta, 0.24, 0.15, "beta_catenin", seed=10 + k + (s > 0), zorder=zorder + 3)
            alpha = beta + np.array([s * 0.42, 0.12])
            _blob(ax, alpha, 0.24, 0.13, "alpha_catenin", seed=20 + k + (s > 0), angle=0.4 * s, zorder=zorder + 3)
            vin = alpha + np.array([s * 0.22, -0.26])
            _blob(ax, vin, 0.16, 0.12, "vinculin", seed=30 + k + (s > 0), zorder=zorder + 3)
            rec = {"cadherin": tip - np.array([-s * dom * 2.5, 0]), "p120": p120, "beta": beta, "alpha": alpha, "vinculin": vin}
            A.setdefault("pairs_left" if s < 0 else "pairs_right", []).append(rec)
            if k == len(ys) // 2:
                key = "left" if s < 0 else "right"
                A[key] = {"cadherin": tip - np.array([-s * dom * 2.5, 0]), "p120": p120, "beta": beta, "alpha": alpha,
                          "vinculin": vin, "membrane": np.array([mx, y + (ys[1] - ys[0]) * 0.5 if pairs > 1 else y + 0.6]),
                          "ca": (np.array([mx - s * MT / 2, y]) + tip) / 2}
    if actin:
        for s in (-1, 1):
            for j, dx in enumerate((depth + 0.05, depth + 0.3)):
                ax_ = x + s * (gap / 2 + dx)
                a, b = (ax_, y0 + 0.15), (ax_, y1 - 0.15)
                if j:
                    a, b = b, a
                actin_line(ax, a, b, lw=2.4, zorder=zorder)
            A["left" if s < 0 else "right"]["actin"] = np.array([x + s * (gap / 2 + depth + 0.18), y1 - 0.4])
    A["space"] = np.array([x, y1 - 0.25])
    return A


def desmosome(ax, x, y0, y1, gap=1.6, plaque=0.38, loops=3, reach=1.6, zorder=10):
    """Close-up of a desmosome: desmogleins and desmocollins meet in the intercellular space (the dense midline),
    the outer dense plaque (plakoglobin, plakophilin) lines each membrane, desmoplakin forms the inner plaque
    and keratin filaments loop into it. Returns a dict of anchors."""
    _space(ax, x, y0, y1, gap, zorder=zorder - 9)
    _membranes(ax, x, y0, y1, gap, zorder=zorder - 5)
    h = (y1 - y0) * 0.62
    ym = (y0 + y1) / 2
    dom = gap / 2 / 5 / 1.7 * 1.12
    for k, y in enumerate(np.linspace(ym - h / 2 + 0.1, ym + h / 2 - 0.1, 6)):
        for s in (-1, 1):
            cadherin(ax, (x + s * (gap / 2 - MT / 2), y), (-s, 0.0), n=5, domain=dom, bend=0.18 * s * (1 if k % 2 else -1),
                     token="desmo_cadherin", ca=False, zorder=zorder + 2)
    ax.plot([x, x], [ym - h / 2, ym + h / 2], color=_e("desmo_cadherin"), lw=0.8, ls=(0, (2, 1.5)), zorder=zorder + 3)
    A = {"midline": np.array([x, ym + h / 2 - 0.05]), "cadherin": np.array([x - gap / 4, ym - h / 2 + 0.3])}
    for s in (-1, 1):
        xo = x + s * (gap / 2 + MT / 2 + 0.04)
        v = np.array([[xo, ym - h / 2], [xo + s * plaque, ym - h / 2 + 0.06], [xo + s * plaque, ym + h / 2 - 0.06],
                      [xo, ym + h / 2]])
        ax.add_patch(Polygon(v, closed=True, facecolor=_f("plaque"), edgecolor=_e("plaque"), lw=0.8, zorder=zorder + 2))
        xi = xo + s * (plaque + 0.22)
        for j, y in enumerate(np.linspace(ym - h / 2 + 0.25, ym + h / 2 - 0.25, 4)):
            _blob(ax, (xi, y), 0.12, 0.16, "desmoplakin", seed=40 + j + (s > 0), zorder=zorder + 2)
        for j in range(loops):
            yc = ym + (j - (loops - 1) / 2) * h / (loops + 0.2)
            r = h / (loops + 0.6) / 2 * 0.8
            R = reach
            pts = [(xi + s * R, yc - r * 1.25), (xi + s * R * 0.45, yc - r * 0.95), (xi + s * 0.15, yc - r * 0.55), (xi + s * 0.08, yc),
                   (xi + s * 0.15, yc + r * 0.55), (xi + s * R * 0.45, yc + r * 0.95), (xi + s * R, yc + r * 1.25)]
            rope(ax, pts, width=0.13, token="if", zorder=zorder)
        key = "left" if s < 0 else "right"
        A[key] = {"plaque": np.array([xo + s * plaque * 0.5, ym + h / 2 - 0.15]), "desmoplakin": np.array([xi, ym - h / 2 + 0.25]),
                  "if": np.array([xi + s * reach * 0.8, ym + h / 2 * 0.62])}
    return A


def tight_junction(ax, x, y0, y1, strands=4, gap=0.9, zorder=10):
    """Close-up of a tight junction: the two membranes meet at ``strands`` kissing points, each formed by a
    pair of claudin tetraspans (with occludin), which seal the paracellular space. Scaffold proteins (ZO)
    link the strands to actin. Returns a dict of anchors (``kiss`` lists the contact points)."""
    ys = np.linspace(y0 + (y1 - y0) * 0.18, y1 - (y1 - y0) * 0.18, strands)
    w = (y1 - y0) / (strands + 1) * 0.28

    def shape(y):
        off = np.full_like(y, gap / 2)
        for yk in ys:
            off -= (gap / 2 - MT * 0.6) * np.exp(-0.5 * ((y - yk) / w) ** 2)
        return off

    yy = np.linspace(y0, y1, 300)
    xl, xr = x - shape(yy), x + shape(yy)
    ax.add_patch(Polygon(np.vstack([np.c_[xl, yy], np.c_[xr, yy][::-1]]), closed=True, facecolor=_f("space"), edgecolor="none",
                         zorder=zorder - 9))
    _membranes(ax, x, y0, y1, gap, shape=shape, zorder=zorder - 5)
    A = {"kiss": [], "claudin": None}
    for k, y in enumerate(ys):
        for s in (-1, 1):
            cx = x + s * MT * 0.6
            ax.add_patch(FancyBboxPatch((cx - 0.1, y - 0.16), 0.2, 0.32, boxstyle="round,pad=0,rounding_size=0.06",
                                        facecolor=_f("claudin" if k % 3 else "occludin"), edgecolor=_e("claudin" if k % 3 else "occludin"),
                                        lw=0.7, zorder=zorder + 2))
            zo = (x + s * 0.65, y)
            _blob(ax, zo, 0.2, 0.13, "zo", seed=50 + k + (s > 0), zorder=zorder + 2)
        A["kiss"].append(np.array([x, y]))
    A["claudin"] = np.array([x - MT * 0.6, ys[1]])
    A["occludin"] = np.array([x + MT * 0.6, ys[0]])
    A["zo"] = np.array([x + 0.7, ys[-1]])
    for s in (-1, 1):
        actin_line(ax, (x + s * 1.15, y0 + 0.1), (x + s * 1.15, y1 - 0.1), lw=2.2, zorder=zorder)
    A["actin"] = np.array([x + 1.15, ys[-1] + w * 2])
    return A


def connexon_pair(ax, x, y, gap=0.3, width=0.9, height=None, open=True, zorder=12):
    """One gap-junction channel: two connexons (hexamers of connexin, side view shows three subunits each)
    docked across the gap, with a central aqueous pore. Returns the pore centre."""
    height = height or 0.62
    for s in (-1, 1):
        x0 = x + s * gap / 2
        for j, dy in enumerate((-width / 2, -width / 6, width / 6)):
            xs = [x0, x0 + s * height]
            ax.add_patch(FancyBboxPatch((min(xs), y + dy + 0.015), height, width / 3 - 0.03, boxstyle="round,pad=0,rounding_size=0.05",
                                        facecolor=_f("connexin") if j != 1 else P.light(tok("connexin")), edgecolor=_e("connexin"),
                                        lw=0.7, zorder=zorder + (0 if j == 1 else 0.2)))
    if open:
        ax.plot([x - gap / 2 - height + 0.02, x + gap / 2 + height - 0.02], [y, y], color=P.surface(), lw=1.6, zorder=zorder + 0.5)
    return np.array([x, y])


def gap_junction(ax, x, y0, y1, connexons=4, gap=0.3, molecules=True, zorder=10):
    """Close-up of a gap junction: the membranes run parallel about 3 nm apart and are bridged by docked
    connexon pairs; small molecules (< 1 kDa) pass through the pores. Returns a dict of anchors."""
    _space(ax, x, y0, y1, gap, zorder=zorder - 9)
    _membranes(ax, x, y0, y1, gap, zorder=zorder - 5)
    ys = np.linspace(y0, y1, connexons + 2)[1:-1]
    pores = [connexon_pair(ax, x, y, gap=gap + MT * 0.2, zorder=zorder + 2) for y in ys]
    A = {"pores": pores, "connexon": np.array([x + gap / 2 + 0.3, ys[-1] + 0.3]), "gap": np.array([x, y1 - 0.15])}
    if molecules:
        rng = np.random.default_rng(3)
        k = len(ys) // 2
        for j, dx in enumerate((-1.4, -0.95, 0.0, 0.95)):
            p = (x + dx, ys[k] + (0.0 if abs(dx) < 1 else rng.uniform(-0.1, 0.1)))
            ax.add_patch(Circle(p, 0.07, facecolor=P.fill("metabolite" if j % 2 else "atp"), edgecolor=P.edge("metabolite"), lw=0.4,
                                zorder=zorder + 4))
        ax.annotate("", xy=(x + 1.35, ys[k]), xytext=(x - 1.75, ys[k]),
                    arrowprops=dict(arrowstyle="-|>", color=P.ink(), lw=0.9, shrinkA=0, shrinkB=0), zorder=zorder + 5)
        A["flux"] = np.array([x + 1.35, ys[k]])
        big = (x - 1.3, ys[0] - 0.05)
        ax.add_patch(Circle(big, 0.22, facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.6, zorder=zorder + 4))
        A["protein"] = np.array(big)
    return A


# ---------------------------------------------------------------------------------------------
# integrins and cell-matrix junctions


def integrin(ax, base, state="open", scale=1.0, ligand=None, zorder=12):
    """One integrin heterodimer standing on a horizontal membrane at ``base`` (the membrane centre line), with
    the cell above. ``state``: "bent" (inactive, headpiece folded towards the membrane), "closed"
    (extended, legs together) or "open" (extended, legs and cytoplasmic tails separated, high affinity).
    ``ligand`` (a token) draws a bound matrix ligand on the head. The extracellular part points down.
    Returns a dict: head, alpha_tail, beta_tail (cytoplasmic ends), alpha_leg, beta_leg."""
    x, y = base
    s = scale
    sep = {"bent": 0.12, "closed": 0.12, "open": 0.42}[state] * s
    out = {}
    # transmembrane segments and cytoplasmic tails (upwards, into the cell)
    for k, (sx, t) in enumerate(((-1, "integrin_a"), (1, "integrin_b"))):
        xm = x + sx * sep / 2
        ax.plot([xm, xm], [y - MT * 0.6, y + MT * 0.6], color=_e(t), lw=3.2 * s, solid_capstyle="round", zorder=zorder)
        tail = np.array([xm + sx * 0.05 * s, y + (0.42 if k else 0.3) * s])
        ax.plot([xm, tail[0]], [y + MT * 0.6, tail[1]], color=_e(t), lw=2.0 * s, solid_capstyle="round", zorder=zorder)
        out["alpha_tail" if k == 0 else "beta_tail"] = tail
    if state == "bent":
        # legs go down, then the headpiece folds back up towards the membrane
        for k, (sx, t) in enumerate(((-1, "integrin_a"), (1, "integrin_b"))):
            xm = x + sx * sep / 2
            knee = np.array([xm + sx * 0.05 * s, y - 0.95 * s])
            _line(ax, [(xm, y - MT * 0.6), knee], t, lw=4.6 * s, zorder=zorder - 0.5)
            out["alpha_leg" if k == 0 else "beta_leg"] = (np.array([xm, y - MT]) + knee) / 2
        head = np.array([x + 0.55 * s, y - 0.55 * s])
        _line(ax, [(x, y - 0.95 * s), head], "integrin_b", lw=4.0 * s, zorder=zorder - 0.4)
        _blob(ax, head + np.array([-0.06, 0.0]) * s, 0.26 * s, 0.2 * s, "integrin_a", seed=61, zorder=zorder + 0.2)
        _blob(ax, head + np.array([0.16, -0.12]) * s, 0.2 * s, 0.17 * s, "integrin_b", seed=62, zorder=zorder + 0.3)
    else:
        L = 1.35 * s
        for k, (sx, t) in enumerate(((-1, "integrin_a"), (1, "integrin_b"))):
            xm = x + sx * sep / 2
            foot = np.array([xm + sx * (0.06 if state == "open" else 0.0) * s, y - L])
            _line(ax, [(xm, y - MT * 0.6), foot], t, lw=4.6 * s, zorder=zorder - 0.5)
            out["alpha_leg" if k == 0 else "beta_leg"] = (np.array([xm, y - MT]) + foot) / 2
        head = np.array([x, y - L - 0.22 * s])
        _blob(ax, head + np.array([-0.17, 0.0]) * s, 0.27 * s, 0.22 * s, "integrin_a", seed=63, zorder=zorder + 0.2)
        hb = head + (np.array([0.24, -0.04]) if state == "open" else np.array([0.18, 0.0])) * s
        _blob(ax, hb, 0.2 * s, 0.18 * s, "integrin_b", seed=64, zorder=zorder + 0.3)
        if state == "open":
            # hybrid domain swing-out
            _line(ax, [(x + sep / 2 + 0.03 * s, y - L), hb + np.array([0.05, 0.1]) * s], "integrin_b", lw=3.4 * s, zorder=zorder)
        if ligand:
            lig = head + np.array([0.0, -0.36]) * s
            _blob(ax, lig, 0.3 * s, 0.13 * s, ligand, seed=65, zorder=zorder + 0.5)
            out["ligand"] = lig
    out["head"] = head
    out["mg"] = head + np.array([0.0, -0.18]) * s
    return out


def _ecm_fiber(ax, x0, x1, y, token="fibronectin", r=0.11, gap=0.02, zorder=9):
    n = int((x1 - x0) / (2 * r + gap))
    xs = x0 + r + np.arange(n) * (2 * r + gap)
    for k, xx in enumerate(xs):
        _bead(ax, (xx, y + 0.03 * math.sin(k * 1.3)), r, token, ry=r * 0.75, zorder=zorder, lw=0.5)
    return xs


def focal_adhesion(ax, x0, x1, y, integrins=4, fiber=True, zorder=10):
    """A focal adhesion seen in section: the plasma membrane runs horizontally at ``y`` with the cell above
    and a fibronectin fibril below. Activated integrins bind the fibril; talin (a long rod bound to the
    beta tail and actin), kindlin, vinculin, paxillin and FAK form the plaque, on which a stress fiber ends.
    Returns a dict of anchors."""
    _rect(ax, x0, y - 1.9, x1 - x0, 1.9 - MT / 2, "space", zorder=zorder - 9)
    _band(ax, [(x0, y), (x1, y)], zorder=zorder - 5)
    xs = np.linspace(x0, x1, integrins + 2)[1:-1]
    _ecm_fiber(ax, x0 + 0.1, x1 - 0.1, y - 1.85, zorder=zorder - 2)
    A = {"integrins": [], "talin": None}
    for k, xx in enumerate(xs):
        a = integrin(ax, (xx, y), state="open", scale=0.95, zorder=zorder + 1)
        A["integrins"].append(a["head"])
        bt = a["beta_tail"]
        top = np.array([xx + 0.9, y + 1.25])
        _line(ax, [bt, (xx + 0.35, y + 0.75), top], "talin", lw=3.6, zorder=zorder + 2)
        _blob(ax, bt + np.array([0.0, 0.12]), 0.16, 0.12, "talin", seed=70 + k, zorder=zorder + 3)
        _blob(ax, a["beta_tail"] + np.array([0.2, -0.02]), 0.11, 0.1, "kindlin", seed=80 + k, zorder=zorder + 3)
        v = np.array([xx + 0.38, y + 0.92])
        _blob(ax, v, 0.16, 0.12, "vinculin", seed=90 + k, zorder=zorder + 3)
        if k % 2 == 0:
            _blob(ax, a["alpha_tail"] + np.array([-0.15, 0.18]), 0.15, 0.11, "fak", seed=100 + k, zorder=zorder + 3)
        if k == 1:
            A.update(talin=(bt + top) / 2 + np.array([0.08, 0.05]), vinculin=v, kindlin=a["beta_tail"] + np.array([0.24, -0.04]),
                     fak=a["alpha_tail"] + np.array([-0.15, 0.18]), integrin=a["alpha_leg"], ligand=a["head"] + np.array([0, -0.35]))
    if fiber:
        # a stress fiber descending onto the plaque (filaments ending at the talin rods)
        for k, xx in enumerate(xs):
            a = np.array([xx + 0.9, y + 1.25])
            b = np.array([x1 + 1.6, y + 2.0 + 0.08 * k])
            actin_line(ax, b, a, lw=2.2, zorder=zorder + 1, plus=True)
        A["actin"] = np.array([x1 + 0.9, y + 1.85])
    A["fibronectin"] = np.array([x0 + 0.5, y - 1.85])
    A["membrane"] = np.array([x0 + 0.25, y])
    return A


def hemidesmosome(ax, x0, x1, y, lamina=True, zorder=10):
    """A hemidesmosome in section: the basal membrane of an epithelial cell at ``y`` (cell above),
    alpha6beta4 integrins and type XVII collagen (BP180) bound to laminin-332 of the basal lamina below,
    an inner plaque of plectin and BP230, and keratin filaments looping into it. Returns a dict of anchors."""
    _rect(ax, x0, y - 1.6, x1 - x0, 1.6 - MT / 2, "space", zorder=zorder - 9)
    _band(ax, [(x0, y), (x1, y)], zorder=zorder - 5)
    if lamina:
        basal_lamina(ax, x0, x1, y - 0.95, depth=0.6, zorder=zorder - 3)
    xs = np.linspace(x0 + 0.5, x1 - 0.5, 5)
    A = {}
    for k, xx in enumerate(xs):
        if k % 2 == 0:
            a = integrin(ax, (xx, y), state="closed", scale=0.62, zorder=zorder + 1)
            ax.plot([xx + 0.04, xx + 0.04], [a["beta_tail"][1], y + 0.65], color=_e("integrin_b"), lw=2.0, solid_capstyle="round",
                    zorder=zorder + 1)
            if k == 2:
                A["integrin"] = a["beta_leg"]
        else:
            ax.plot([xx, xx + 0.1, xx - 0.05, xx + 0.05], [y + 0.45, y, y - 0.5, y - 0.95], color=_e("col17"), lw=1.6, zorder=zorder + 1)
            _blob(ax, (xx + 0.05, y - 0.9), 0.12, 0.1, "col17", seed=110 + k, zorder=zorder + 2)
            if k == 1:
                A["col17"] = np.array([xx + 0.02, y - 0.5])
    v = np.array([[x0 + 0.3, y + 0.38], [x1 - 0.3, y + 0.38], [x1 - 0.45, y + 0.78], [x0 + 0.45, y + 0.78]])
    ax.add_patch(Polygon(v, closed=True, facecolor=_f("plectin"), edgecolor=_e("plectin"), lw=0.8, zorder=zorder + 2))
    A["plaque"] = np.array([x1 - 0.6, y + 0.6])
    w = x1 - x0
    for j in range(3):
        xc = x0 + w * (0.25 + 0.25 * j)
        r = w * 0.09
        pts = [(xc - r * 1.6, y + 3.0), (xc - r * 1.05, y + 1.6), (xc - r * 0.5, y + 0.95), (xc, y + 0.82), (xc + r * 0.5, y + 0.95),
               (xc + r * 1.05, y + 1.6), (xc + r * 1.6, y + 3.0)]
        rope(ax, pts, width=0.13, token="if", zorder=zorder + 1)
    A["if"] = np.array([x0 + w * 0.5 + w * 0.15, y + 2.4])
    A["lamina"] = np.array([x0 + 0.3, y - 1.1])
    return A


# ---------------------------------------------------------------------------------------------
# the epithelium overview


def epithelium(ax, x0, x1, y0, height, n=3, gap=0.16, microvilli=True, junctions=True, lamina=True, matrix=True, zorder=6):
    """A simple columnar epithelium of ``n`` cells standing on a basal lamina (bottom at ``y0``), with
    microvilli at the apical surface and, when ``junctions``, the junctional complex in each lateral space:
    tight junction at the apex, the adherens belt with its actin bundle, desmosomes with keratin filaments,
    gap junctions lower down, and at the base hemidesmosomes and actin-linked cell-matrix junctions.
    Returns a dict of anchors (points in the first lateral space, at the base, and per cell)."""
    w = (x1 - x0 - (n - 1) * gap) / n
    yb = y0 + (0.5 if lamina else 0.0)
    yt = yb + height
    A = {"cells": []}
    if lamina:
        basal_lamina(ax, x0 - 0.2, x1 + 0.2, y0 + 0.35, depth=0.35, zorder=zorder - 1, detailed=False)
        A["lamina"] = np.array([x0 + 0.2, y0 + 0.2])
        if matrix:
            for k in range(int((x1 - x0) / 0.9)):
                xx = x0 + 0.3 + k * 0.9
                ax.plot([xx, xx + 0.5], [y0 - 0.15, y0 - 0.35], color=_e("collagen"), lw=2.4, solid_capstyle="round", zorder=zorder - 2)
            A["connective"] = np.array([x0 + 0.6, y0 - 0.3])
    for i in range(n):
        cx0 = x0 + i * (w + gap)
        ax.add_patch(FancyBboxPatch((cx0, yb), w, height, boxstyle="round,pad=0,rounding_size=0.25", facecolor=_f("cytoplasm"),
                                    edgecolor=_e("membrane"), lw=LINE * 1.6, zorder=zorder))
        nc = (cx0 + w / 2, yb + height * 0.3)
        ax.add_patch(Ellipse(nc, w * 0.5, height * 0.26, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=LINE,
                             zorder=zorder + 1))
        A["cells"].append({"nucleus": np.array(nc), "apical": np.array([cx0 + w / 2, yt]), "center": np.array([cx0 + w / 2, yb + height / 2])})
        if microvilli:
            m = int(w / 0.26)
            for j in range(m):
                mx = cx0 + 0.2 + j * (w - 0.4) / max(1, m - 1)
                ax.add_patch(FancyBboxPatch((mx - 0.07, yt - 0.05), 0.14, 0.55, boxstyle="round,pad=0,rounding_size=0.07",
                                            facecolor=_f("cytoplasm"), edgecolor=_e("membrane"), lw=LINE * 0.9, zorder=zorder - 0.5))
                ax.plot([mx, mx], [yt - 0.25, yt + 0.42], color=_e("actin"), lw=0.7, zorder=zorder + 0.6)
    A["apical"] = np.array([x0 + w / 2, yt + 0.5])
    if not junctions:
        return A
    zj = zorder + 3
    yTJ, yAJ = yt - 0.32, yt - 0.75
    for i in range(n - 1):
        gx = x0 + (i + 1) * w + i * gap + gap / 2
        # tight junction: a dark seal bridging the space
        ax.add_patch(FancyBboxPatch((gx - gap / 2 - 0.08, yTJ - 0.14), gap + 0.16, 0.28, boxstyle="round,pad=0,rounding_size=0.05",
                                    facecolor=_f("claudin"), edgecolor=_e("claudin"), lw=0.8, zorder=zj))
        # adherens belt: cadherin ticks across the space
        for dy in (-0.12, 0.0, 0.12):
            ax.plot([gx - gap / 2 - 0.05, gx + gap / 2 + 0.05], [yAJ + dy, yAJ + dy], color=_e("cadherin"), lw=1.3, zorder=zj)
        ax.add_patch(Ellipse((gx, yAJ), gap + 0.28, 0.42, facecolor="none", edgecolor=_e("cadherin"), lw=0.8, zorder=zj))
        # desmosomes: plaques on both sides with keratin loops
        for yd in (yb + height * 0.62, yb + height * 0.43):
            for s in (-1, 1):
                px = gx + s * (gap / 2 + 0.1)
                ax.add_patch(FancyBboxPatch((px - 0.06, yd - 0.2), 0.12, 0.4, boxstyle="round,pad=0,rounding_size=0.04",
                                            facecolor=_f("plaque"), edgecolor=_e("plaque"), lw=0.8, zorder=zj))
            ax.plot([gx, gx], [yd - 0.17, yd + 0.17], color=_e("desmo_cadherin"), lw=1.4, zorder=zj)
        # gap junction: a row of connexon bars
        ygj = yb + height * 0.2
        for dy in np.linspace(-0.25, 0.25, 4):
            ax.plot([gx - gap / 2 - 0.06, gx + gap / 2 + 0.06], [ygj + dy, ygj + dy], color=_e("connexin"), lw=2.2,
                    solid_capstyle="butt", zorder=zj)
        if i == 0:
            A.update(tight=np.array([gx, yTJ]), adherens=np.array([gx, yAJ]), desmosome=np.array([gx, yb + height * 0.62]),
                     gap=np.array([gx, ygj]))
    # adhesion-belt actin bundles inside each cell, under the apex
    for i in range(n):
        cx0 = x0 + i * (w + gap)
        ax.plot([cx0 + 0.12, cx0 + w - 0.12], [yAJ, yAJ], color=_e("actin"), lw=2.6, solid_capstyle="round", zorder=zj - 0.5)
        ax.plot([cx0 + 0.12, cx0 + w - 0.12], [yAJ, yAJ], color=_f("actin"), lw=1.0, solid_capstyle="round", zorder=zj - 0.4)
        # keratin network spanning the cell between desmosomes and hemidesmosomes
        ys = (yb + height * 0.62, yb + height * 0.43)
        pts_l = [(cx0 + 0.25, ys[0]), (cx0 + w * 0.3, yb + height * 0.55), (cx0 + w * 0.45, yb + height * 0.2), (cx0 + w * 0.35, yb + 0.25)]
        pts_r = [(cx0 + w - 0.25, ys[1]), (cx0 + w * 0.7, yb + height * 0.5), (cx0 + w * 0.6, yb + height * 0.22), (cx0 + w * 0.68, yb + 0.25)]
        for pts in (pts_l, pts_r):
            c = _curve(pts, 60)
            ax.plot(c[:, 0], c[:, 1], color=_e("if"), lw=1.4, zorder=zj - 0.6, solid_capstyle="round")
        # hemidesmosomes and an actin-linked cell-matrix junction at the base
        for hx in (cx0 + w * 0.3, cx0 + w * 0.72):
            ax.add_patch(FancyBboxPatch((hx - 0.22, yb + 0.06), 0.44, 0.13, boxstyle="round,pad=0,rounding_size=0.04",
                                        facecolor=_f("plectin"), edgecolor=_e("plectin"), lw=0.8, zorder=zj))
            for dx in (-0.12, 0.0, 0.12):
                ax.plot([hx + dx, hx + dx], [yb - 0.05, yb + 0.08], color=_e("integrin_b"), lw=1.2, zorder=zj)
        if i == 0:
            A["hemidesmosome"] = np.array([cx0 + w * 0.3, yb + 0.1])
            A["keratin"] = np.array(c[len(c) // 2])
            A["belt"] = np.array([cx0 + w * 0.5, yAJ])
        if i == n - 1:
            fx = cx0 + w * 0.5
            ax.add_patch(FancyBboxPatch((fx - 0.2, yb + 0.06), 0.4, 0.12, boxstyle="round,pad=0,rounding_size=0.04",
                                        facecolor=_f("talin"), edgecolor=_e("talin"), lw=0.8, zorder=zj))
            for k in range(3):
                ax.plot([fx - 0.1 + 0.1 * k, fx + 0.7 + 0.1 * k], [yb + 0.18, yb + 0.75 + 0.05 * k], color=_e("actin"), lw=1.3, zorder=zj - 0.5)
            A["focal"] = np.array([fx, yb + 0.12])
    return A


# ---------------------------------------------------------------------------------------------
# extracellular matrix


def triple_helix(ax, a, b, width=0.3, pitch=None, tokens=("collagen", "collagen", "collagen_iv"), shades=(0.0, 0.25, 0.5),
                 lw=None, zorder=10):
    """Three intertwined polypeptide chains (the collagen triple helix): sinusoids 120 degrees out of phase,
    drawn front strand over back strand. ``shades`` lighten successive chains. Returns (a, b)."""
    a, b, L, u, n = _frame(a, b)
    pitch = pitch or width * 3.0
    s = np.linspace(0, L, max(200, int(L * 80)))
    lw = lw or width * 72 * 0.16
    for k in range(3):
        ph = 2 * math.pi * s / pitch + 2 * math.pi * k / 3
        off = np.sin(ph) * width / 2
        depth = np.cos(ph)
        pts = a + np.outer(s, u) + np.outer(off, n)
        base = P.fill(tok(tokens[k]))
        col = P.mix(base, P.surface(), shades[k]) if shades[k] else base
        edge = P.edge(tok(tokens[k]))
        # split into front/back runs so that crossings read in depth
        for front in (False, True):
            mask = depth > 0 if front else depth <= 0
            run = np.where(mask, 1.0, np.nan)
            ax.plot(pts[:, 0] * run, pts[:, 1] * run, color=edge, lw=lw + 1.0, solid_capstyle="round", zorder=zorder + (1 if front else 0) + k * 0.01)
            ax.plot(pts[:, 0] * run, pts[:, 1] * run, color=col, lw=lw, solid_capstyle="round", zorder=zorder + (1 if front else 0) + k * 0.01 + 0.005)
    return a, b


def tropocollagen(ax, a, b, width=0.09, token="collagen", zorder=10):
    """A collagen molecule (300 nm rod) as a slim capsule with knobbed telopeptide ends."""
    a, b, L, u, n = _frame(a, b)
    w = _pt(ax, width)
    a1, b1 = a + u * width / 2, b - u * width / 2
    ax.plot([a1[0], b1[0]], [a1[1], b1[1]], color=_e(token), lw=w + 0.9, solid_capstyle="round", zorder=zorder)
    ax.plot([a1[0], b1[0]], [a1[1], b1[1]], color=_f(token), lw=w, solid_capstyle="round", zorder=zorder + 0.01)
    return a, b


def collagen_fibril(ax, origin, length, rows=5, D=1.0, row_h=0.26, width=0.1, crosslinks=True, shade=True, token="collagen", zorder=10):
    """Quarter-staggered packing of collagen molecules in a fibril (side view of ``rows`` rows starting at
    ``origin``): each molecule is 4.4 D long, molecules in a row are separated by a 0.6 D gap, and each row is
    shifted by D from the one below, which gives the 67 nm D period of alternating gap and overlap zones.
    ``shade`` tints the gap zones; ``crosslinks`` marks lysyl-oxidase cross-links near the ends.
    Returns dict(gap=(x0, x1) of one gap zone, overlap=(x0, x1), molecule=point, D=D)."""
    x0, y0 = origin
    mol, gapL = 4.46 * D, 0.54 * D
    rep = mol + gapL  # = 5 D
    res = {"D": D}
    if shade:
        # gap zones recur every D: the first 0.54 D of each period
        k = 0
        while x0 + k * D < x0 + length:
            gs = x0 + k * D
            ge = min(gs + 0.54 * D, x0 + length)
            ax.add_patch(FancyBboxPatch((gs, y0 - row_h * 0.6), ge - gs, rows * row_h + row_h * 0.2, boxstyle="square,pad=0",
                                        facecolor=P.mix(P.muted(), P.surface(), 0.62), edgecolor="none", zorder=zorder - 2))
            if k == 1:
                res["gap"] = (gs, ge)
                res["overlap"] = (ge, gs + D)
            k += 1
    for r in range(rows):
        y = y0 + r * row_h
        # row r: molecules start at x0 + 0.54 D + r D + 5 m D, so its gaps fall in the shaded zones
        x = x0 + gapL + r * D - 2 * rep
        while x < x0 + length:
            m0, m1 = max(x, x0), min(x + mol, x0 + length)
            if m1 > m0 + 0.05:
                tropocollagen(ax, (m0, y), (m1, y), width=width, token=token, zorder=zorder)
                if crosslinks and r < rows - 1:
                    for cx in (x + 0.2, x + mol - 0.2):
                        if m0 + 0.05 < cx < m1 - 0.05:
                            ax.plot([cx, cx + 0.06], [y, y + row_h], color=_e("crosslink"), lw=1.3, zorder=zorder + 0.5)
            if r == rows // 2 and "molecule" not in res and m1 - m0 > 2:
                res["molecule"] = np.array([(m0 + m1) / 2, y])
            x += rep
    return res


def banded_fibril(ax, a, b, width=0.5, D=0.3, token="collagen", zorder=10):
    """A collagen fibril as a cylinder with the D-period banding of negatively stained fibrils."""
    a, b, L, u, n = _frame(a, b)
    w = _pt(ax, width)
    a1, b1 = a + u * width / 2, b - u * width / 2
    ax.plot([a1[0], b1[0]], [a1[1], b1[1]], color=_e(token), lw=w + 1.0, solid_capstyle="round", zorder=zorder)
    ax.plot([a1[0], b1[0]], [a1[1], b1[1]], color=_f(token), lw=w, solid_capstyle="round", zorder=zorder + 0.01)
    k = 0
    while (k + 0.54) * D < L - width * 0.5:
        p = a + u * ((k + 0.27) * D)
        if k * D >= width * 0.5:
            ax.plot(*np.array([p + n * width * 0.47, p - n * width * 0.47]).T, color=_e(token), lw=_pt(ax, 0.54 * D), alpha=0.45,
                    solid_capstyle="butt", zorder=zorder + 0.02)
        k += 1
    return a, b


def gag_chain(ax, start, direction, length, token="gag", lw=1.3, wiggle=0.06, zorder=10):
    """A glycosaminoglycan chain: a zigzag of disaccharide units from ``start`` along ``direction``."""
    d = np.asarray(direction, float) / np.linalg.norm(direction)
    nrm = np.array([-d[1], d[0]])
    m = max(3, int(length / 0.09))
    pts = [np.asarray(start, float) + d * length * k / m + nrm * wiggle * (1 if k % 2 else -1) * (k > 0) for k in range(m + 1)]
    pts = np.array(pts)
    ax.plot(pts[:, 0], pts[:, 1], color=_e(token), lw=lw, solid_joinstyle="round", zorder=zorder)
    return pts[-1]


def proteoglycan(ax, a, b, chains=8, chain_len=0.7, token="core_protein", gag="gag", lw=2.4, zorder=10):
    """A proteoglycan as a bottlebrush: a core protein from ``a`` to ``b`` with ``chains`` GAG chains on
    alternating sides. Returns dict(core=midpoint, gag=tip of one chain)."""
    a, b, L, u, n = _frame(a, b)
    out = {"core": (a + b) / 2}
    for k in range(chains):
        t = (k + 0.6) / (chains + 0.2)
        p = a + u * L * t
        side = 1 if k % 2 == 0 else -1
        d = n * side * 0.92 + u * 0.38
        tip = gag_chain(ax, p, d, chain_len * (0.85 + 0.15 * math.sin(k * 2.1)), token=gag, zorder=zorder - 0.2)
        if k == 2:
            out["gag"] = tip
    _line(ax, [a, b], token, lw=lw, zorder=zorder)
    return out


def aggrecan_aggregate(ax, a, b, n=6, chain_len=0.45, core=1.6, zorder=10):
    """An aggrecan aggregate: a long hyaluronan chain (``a`` to ``b``) carrying ``n`` aggrecan molecules on
    alternating sides, each bound through its N-terminal domain and a link protein. Returns anchors."""
    a, b, L, u, nn = _frame(a, b)
    s = np.linspace(0, L, 300)
    ha = a + np.outer(s, u) + np.outer(np.sin(s * 2.2) * 0.05, nn)
    ax.plot(ha[:, 0], ha[:, 1], color=_e("hyaluronan"), lw=3.2, solid_capstyle="round", zorder=zorder + 1)
    ax.plot(ha[:, 0], ha[:, 1], color=_f("hyaluronan"), lw=1.4, solid_capstyle="round", zorder=zorder + 1.05)
    out = {"hyaluronan": ha[len(ha) // 12]}
    for k in range(n):
        t = (k + 0.5) / n
        p = a + u * L * t
        side = 1 if k % 2 == 0 else -1
        tip = p + nn * side * core
        r = proteoglycan(ax, p + nn * side * 0.12, tip, chains=12, chain_len=chain_len, lw=2.0, zorder=zorder)
        _bead(ax, p + nn * side * 0.07 + u * 0.12, 0.08, "link_protein", zorder=zorder + 2, lw=0.5)
        if k == 1:
            out.update(aggrecan=r["core"], gag=r["gag"], link=p + nn * side * 0.07 + u * 0.12)
    return out


def laminin(ax, center, size=1.0, angle=0.0, token="laminin", zorder=11):
    """A laminin heterotrimer: an asymmetric cross of three short arms (alpha, beta, gamma N-termini with
    globular domains) and a long coiled-coil arm ending in the five LG domains of the alpha chain.
    Returns dict(lg=point of the LG domains, center=center)."""
    c = np.asarray(center, float)
    th = math.radians(angle)
    R = np.array([[math.cos(th), -math.sin(th)], [math.sin(th), math.cos(th)]])

    def p(x, y):
        return c + R @ np.array([x, y]) * size

    arms = [((0, 0), (0, 0.55)), ((0, 0), (-0.45, 0.05)), ((0, 0), (0.45, 0.05)), ((0, 0), (0, -0.95))]
    for k, (s0, s1) in enumerate(arms):
        _line(ax, [p(*s0), p(*s1)], token, lw=2.6 * size + 0.4, zorder=zorder)
        if k < 3:
            _bead(ax, p(*s1), 0.07 * size + 0.02, token, zorder=zorder + 0.2, lw=0.5)
            mid = (np.asarray(s0) + np.asarray(s1)) * 0.55
            _bead(ax, p(*mid), 0.05 * size + 0.015, token, zorder=zorder + 0.2, lw=0.5)
    lg = []
    for j in range(5):
        a = math.radians(-90 + (j - 2) * 34)
        q = p(0.0, -0.95) + R @ np.array([math.cos(a), math.sin(a)]) * 0.13 * size
        _bead(ax, q, 0.065 * size + 0.015, token, zorder=zorder + 0.3, lw=0.5)
        lg.append(q)
    return {"lg": np.mean(lg, axis=0), "center": c, "top": p(0, 0.55)}


def fibronectin(ax, a, b, repeats=11, rgd=True, token="fibronectin", zorder=11):
    """A fibronectin dimer: two strings of repeats (type I, II and III modules as beads) joined near their
    C termini by disulfide bonds at ``b``; the RGD-containing type III repeat (III-10) is highlighted.
    Returns dict(rgd=point, dimer=b)."""
    a, b, L, u, n = _frame(a, b)
    out = {"dimer": b}
    for s in (1, -1):
        ends = a + n * s * L * 0.18
        pts = [ends + (b - ends) * (k + 0.5) / repeats for k in range(repeats)]
        for k, q in enumerate(pts):
            hl = rgd and k == repeats - 4
            _bead(ax, q, L / repeats * 0.42, "rgd" if hl else token, zorder=zorder, lw=0.5)
            if hl and s == 1:
                out["rgd"] = q
    ax.plot([b[0] - u[0] * 0.05, b[0] + u[0] * 0.12], [b[1] - u[1] * 0.05, b[1] + u[1] * 0.12], color=P.edge("highlight"), lw=1.2, zorder=zorder + 1)
    return out


def collagen_iv_net(ax, x0, x1, y0, y1, cell=0.6, token="collagen_iv", seed=2, zorder=9):
    """A two-dimensional "chicken-wire" network of type IV collagen (head-to-head dimers and lateral
    associations) filling a rectangle. Returns a point on the net."""
    rng = np.random.default_rng(seed)
    xs = np.arange(x0, x1 + cell, cell)
    rows = np.arange(y0, y1 + 1e-6, cell * 0.85)
    nodes = {}
    for i, y in enumerate(rows):
        for j, x in enumerate(xs):
            xx = x + (cell / 2 if i % 2 else 0) + rng.uniform(-0.12, 0.12) * cell
            yy = y + rng.uniform(-0.12, 0.12) * cell
            nodes[(i, j)] = (min(max(xx, x0), x1), min(max(yy, y0), y1))
    col = _e(token)
    for (i, j), p in nodes.items():
        for q in ((i, j + 1), (i + 1, j), (i + 1, j + (1 if i % 2 else -1))):
            if q in nodes:
                r = nodes[q]
                ax.plot([p[0], r[0]], [p[1], r[1]], color=col, lw=1.1, solid_capstyle="round", zorder=zorder)
        ax.add_patch(Circle(p, 0.045, facecolor=_f(token), edgecolor=col, lw=0.4, zorder=zorder + 0.1))
    return np.array(nodes[(len(rows) // 2, 1)])


def basal_lamina(ax, x0, x1, y_top, depth=0.8, detailed=True, zorder=8):
    """The basal lamina as a strip below ``y_top``: a laminin polymer (upper layer, facing the cells), a type IV
    collagen network beneath, nidogen bridges and perlecan; ``detailed=False`` draws a plain tinted strip
    (for overviews). Returns a dict of anchors."""
    y0 = y_top - depth
    _rect(ax, x0, y0, x1 - x0, depth, "laminin", zorder=zorder - 1, alpha=0.35)
    if not detailed:
        ax.plot([x0, x1], [y_top, y_top], color=_e("laminin"), lw=0.8, zorder=zorder)
        ax.plot([x0, x1], [y0, y0], color=_e("laminin"), lw=0.8, zorder=zorder)
        return {"lamina": np.array([x0 + 0.3, y_top - depth / 2])}
    out = {}
    net = collagen_iv_net(ax, x0 + 0.05, x1 - 0.05, y0 + 0.08, y0 + depth * 0.45, cell=max(0.25, depth * 0.18), zorder=zorder)
    out["collagen_iv"] = net
    n = max(2, int((x1 - x0) / 0.9))
    for k in range(n):
        cx = x0 + (k + 0.5) * (x1 - x0) / n
        # LG domains face the cells (receptor binding); the short arms polymerize below
        r = laminin(ax, (cx, y_top - depth * (0.5 if k % 2 else 0.58)), size=depth * 0.42, angle=180, zorder=zorder + 1)
        if k == 0:
            out["laminin"] = r["center"]
        if k < n - 1:
            nx = cx + (x1 - x0) / n * 0.5
            ax.plot([nx - 0.12, nx + 0.12], [y_top - depth * 0.62, y0 + depth * 0.35], color=_e("nidogen"), lw=1.8, solid_capstyle="round",
                    zorder=zorder + 1.2)
            if k == 1:
                out["nidogen"] = np.array([nx, (y_top - depth * 0.62 + y0 + depth * 0.35) / 2])
    pg = proteoglycan(ax, (x1 - 1.3, y0 + depth * 0.5), (x1 - 0.4, y0 + depth * 0.5), chains=4, chain_len=depth * 0.3, lw=1.8, zorder=zorder + 1.5)
    out["perlecan"] = pg["core"]
    return out


def elastin(ax, center, w=2.0, h=1.4, stretch=0.0, chains=7, seed=5, token="elastin", zorder=10):
    """A network of elastin molecules: random coils joined by cross-links (dots); ``stretch`` from 0 (relaxed,
    coiled) to 1 (stretched along x: chains straightened). Returns dict(crosslink=point)."""
    rng = np.random.default_rng(seed)
    cx, cy = center
    sx = 1 + 0.9 * stretch
    sy = 1 - 0.35 * stretch
    xl = np.linspace(-w / 2, w / 2, 5)
    yl = np.linspace(-h / 2, h / 2, chains)
    nodes = {}
    for i, y in enumerate(yl):
        for j, x in enumerate(xl):
            nodes[(i, j)] = np.array([cx + x * sx + rng.uniform(-0.08, 0.08), cy + y * sy + rng.uniform(-0.06, 0.06)])
    out = {}
    for i in range(chains):
        for j in range(len(xl) - 1):
            p, q = nodes[(i, j)], nodes[(i, j + 1)]
            m = 30
            t = np.linspace(0, 1, m)
            amp = (1 - stretch) * 0.13 + 0.02
            freq = rng.integers(2, 4)
            ph = rng.uniform(0, 2 * math.pi)
            d = q - p
            nrm = np.array([-d[1], d[0]]) / (np.linalg.norm(d) or 1)
            pts = p + np.outer(t, d) + np.outer(np.sin(2 * math.pi * freq * t + ph) * np.sin(math.pi * t) * amp, nrm)
            ax.plot(pts[:, 0], pts[:, 1], color=_e(token), lw=1.8, solid_capstyle="round", zorder=zorder)
            ax.plot(pts[:, 0], pts[:, 1], color=_f(token), lw=0.8, solid_capstyle="round", zorder=zorder + 0.01)
    for (i, j), p in nodes.items():
        if 0 < j < len(xl) - 1 and (i + j) % 2 == 0 and i < chains - 1:
            q = nodes[(i + 1, j)]
            ax.plot([p[0], q[0]], [p[1], q[1]], color=_e(token), lw=1.0, zorder=zorder - 0.1, ls=(0, (1.5, 1.2)))
            ax.add_patch(Circle(p, 0.06, facecolor=_f("crosslink"), edgecolor=_e("crosslink"), lw=0.5, zorder=zorder + 0.2))
            out.setdefault("crosslink", p)
    return out


# ---------------------------------------------------------------------------------------------
# plant cell wall


def cellulose_synthase(ax, center, r=0.22, token="csc", zorder=12):
    """A cellulose synthase complex (rosette) in face view: six lobes, each a trimer of CesA proteins."""
    c = np.asarray(center, float)
    for k in range(6):
        a = math.pi / 2 + k * math.pi / 3
        _bead(ax, c + r * 0.55 * np.array([math.cos(a), math.sin(a)]), r * 0.33, token, zorder=zorder, lw=0.6)
    return c


def wall_face(ax, x0, y0, w, h, spacing=0.45, angle2=90.0, tethers=True, pectin=True, seed=7, zorder=8):
    """The primary cell wall in face view: two lamellae of parallel cellulose microfibrils (the upper one at
    ``angle2`` degrees to the lower), cross-linking glycans tethering neighbouring microfibrils, and a pectin
    gel filling the spaces. Returns a dict of anchors."""
    rng = np.random.default_rng(seed)
    _rect(ax, x0, y0, w, h, "wall", zorder=zorder - 2, alpha=0.35)
    out = {}
    if pectin:
        for k in range(int(w * h * 5)):
            p = (x0 + rng.uniform(0.08, w - 0.08), y0 + rng.uniform(0.08, h - 0.08))
            ang = rng.uniform(0, 2 * math.pi)
            t = np.linspace(0, 1, 12)
            pts = np.c_[p[0] + 0.18 * t * math.cos(ang) + 0.03 * np.sin(t * 9), p[1] + 0.18 * t * math.sin(ang) + 0.03 * np.cos(t * 9)]
            ax.plot(pts[:, 0], pts[:, 1], color=_e("pectin"), lw=0.7, alpha=0.8, zorder=zorder - 1)
            if "pectin" not in out and p[1] < y0 + 0.6 and x0 + w * 0.35 < p[0] < x0 + w * 0.65:
                out["pectin"] = np.array(p)
    lw = 3.0
    ys = np.arange(y0 + spacing / 2, y0 + h, spacing)
    for y in ys:
        _line(ax, [(x0 + 0.05, y), (x0 + w - 0.05, y)], "cellulose", lw=lw, zorder=zorder)
    out["microfibril"] = np.array([x0 + w * 0.9, ys[0]])
    if angle2 is not None:
        xs = np.arange(x0 + spacing / 2, x0 + w, spacing)
        for x in xs:
            _line(ax, [(x, y0 + 0.05), (x, y0 + h - 0.05)], "cellulose", lw=lw, zorder=zorder + 1)
        out["microfibril2"] = np.array([xs[-1], y0 + h * 0.85])
    if tethers:
        for j in range(len(ys) - 1):
            for _ in range(int(w / 0.8)):
                xx = x0 + rng.uniform(0.15, w - 0.15)
                pts = [(xx, ys[j]), (xx + 0.08, (ys[j] * 2 + ys[j + 1]) / 3), (xx - 0.06, (ys[j] + 2 * ys[j + 1]) / 3), (xx + 0.02, ys[j + 1])]
                c = _curve(pts, 30)
                ax.plot(c[:, 0], c[:, 1], color=_e("glycan"), lw=1.3, zorder=zorder + 0.5)
                if j == 0:
                    out.setdefault("glycan", c[len(c) // 2])
    return out


def wall_section(ax, x0, x1, y, primary=0.5, secondary=(0.25, 0.7, 0.2), lamella=0.25, csc=3, microtubules=True, zorder=8):
    """A plant cell wall in section, cell 1 below and cell 2 above the middle lamella at ``y``: the pectin-rich
    middle lamella, the two primary walls, on the lower cell the three layers S1, S2, S3 of a secondary wall
    (``secondary=None`` for none), then the plasma membrane of each cell, with cellulose synthase complexes
    in the lower membrane and cortical microtubules beneath them. Returns a dict of anchors."""
    out = {}
    _rect(ax, x0, y - lamella / 2, x1 - x0, lamella, "lamella", zorder=zorder)
    out["lamella"] = np.array([x0 + 0.3, y])
    # primary walls (microfibrils seen as dots or lines)
    for s in (1, -1):
        yy = y + s * lamella / 2
        lo, hi = sorted((yy, yy + s * primary))
        _rect(ax, x0, lo, x1 - x0, hi - lo, "wall", zorder=zorder)
        for k, xx in enumerate(np.arange(x0 + 0.12, x1, 0.22)):
            ax.add_patch(Circle((xx, (lo + hi) / 2 + 0.08 * ((k % 2) - 0.5)), 0.04, color=_e("cellulose"), lw=0, zorder=zorder + 0.5))
        out["primary2" if s > 0 else "primary"] = np.array([x0 + 0.3, (lo + hi) / 2])
    ytop = y + lamella / 2 + primary
    ybot = y - lamella / 2 - primary
    if secondary:
        for j, (t, kind) in enumerate(zip(secondary, ("S1", "S2", "S3"))):
            lo = ybot - t
            _rect(ax, x0, lo, x1 - x0, t, "secondary", zorder=zorder)
            ax.plot([x0, x1], [lo, lo], color=_e("secondary"), lw=0.6, zorder=zorder + 0.3)
            # microfibril orientation differs between layers: draw short hatching
            step = 0.25
            for xx in np.arange(x0 + 0.1, x1 - 0.1, step):
                if kind == "S2":
                    ax.plot([xx, xx + 0.12], [lo + t * 0.15, lo + t * 0.85], color=_e("cellulose"), lw=0.9, zorder=zorder + 0.4)
                else:
                    ax.plot([xx, xx + 0.17], [lo + t * 0.5, lo + t * 0.5], color=_e("cellulose"), lw=0.9, zorder=zorder + 0.4)
            out[kind] = np.array([x0 + 0.3, lo + t / 2])
            ybot = lo
    _band(ax, [(x0, ybot - MT / 2), (x1, ybot - MT / 2)], zorder=zorder + 1)
    _band(ax, [(x0, ytop + MT / 2), (x1, ytop + MT / 2)], zorder=zorder + 1)
    out["membrane"] = np.array([x0 + 0.3, ybot - MT / 2])
    out["membrane2"] = np.array([x0 + 0.3, ytop + MT / 2])
    xs = np.linspace(x0, x1, csc + 2)[1:-1]
    for k, xx in enumerate(xs):
        ax.add_patch(FancyBboxPatch((xx - 0.22, ybot - MT / 2 - 0.2), 0.44, 0.4, boxstyle="round,pad=0,rounding_size=0.1",
                                    facecolor=_f("csc"), edgecolor=_e("csc"), lw=0.8, zorder=zorder + 2))
        ax.plot([xx, xx], [ybot - MT / 2 + 0.2, ybot + 0.12], color=_e("cellulose"), lw=1.6, zorder=zorder + 2)
        if k == 0:
            out["csc"] = np.array([xx, ybot - MT / 2])
    if microtubules:
        ym = ybot - MT / 2 - 0.55
        ax.plot([x0 + 0.1, x1 - 0.1], [ym, ym], color=_e("microtubule"), lw=4.5, solid_capstyle="round", zorder=zorder + 1)
        ax.plot([x0 + 0.1, x1 - 0.1], [ym, ym], color=_f("microtubule"), lw=2.4, solid_capstyle="round", zorder=zorder + 1.1)
        out["microtubule"] = np.array([x1 - 0.5, ym])
    out["cytoplasm"] = np.array([x0 + 0.3, ybot - 1.0])
    out["top"] = ytop + MT
    out["bottom"] = ybot - MT
    return out


def plasmodesma(ax, center, wall=0.9, length=None, width=0.42, height=1.6, desmotubule=True, callose=True, cells=True, zorder=10):
    """A plasmodesma through a vertical wall of thickness ``wall`` centred at ``center``: the plasma membrane
    lines the channel and is continuous between the two cells, the desmotubule (appressed ER) runs through
    the centre and joins ER cisternae on both sides, and the cytoplasmic sleeve between them is the path for
    small molecules. Optional callose collars at the necks regulate the size-exclusion limit.
    Returns a dict of anchors."""
    cx, cy = center
    length = length or wall * 3.2
    xl, xr = cx - wall / 2, cx + wall / 2
    yt, yb = cy + width / 2, cy - width / 2
    H = height
    if cells:
        _rect(ax, cx - length / 2, cy - H, length / 2 - wall / 2, 2 * H, "cytoplasm", zorder=zorder - 4)
        _rect(ax, xr, cy - H, length / 2 - wall / 2, 2 * H, "cytoplasm", zorder=zorder - 4)
    # wall blocks above and below the channel
    for lo, hi in ((yt + MT / 2, cy + H), (cy - H, yb - MT / 2)):
        _rect(ax, xl, lo, wall, hi - lo, "wall", zorder=zorder - 2)
        for k, yy in enumerate(np.arange(lo + 0.1, hi, 0.18)):
            ax.add_patch(Circle((cx + 0.15 * ((k % 3) - 1), yy), 0.035, color=_e("cellulose"), lw=0, zorder=zorder - 1.5))
    ax.plot([cx, cx], [cy + H, yt + MT], color=_e("lamella"), lw=1.0, ls=(0, (3, 2)), zorder=zorder - 1)
    ax.plot([cx, cx], [cy - H, yb - MT], color=_e("lamella"), lw=1.0, ls=(0, (3, 2)), zorder=zorder - 1)
    # plasma membrane: down the wall face, through the channel, up the other face (top and bottom halves)
    r = 0.18
    for s in (1, -1):
        yc = cy + s * width / 2
        pts = [(cx - length / 2, cy + s * H), (xl - MT / 2, cy + s * H), (xl - MT / 2, yc + s * r)]
        arc1 = [(xl - MT / 2 + r - r * math.cos(t), yc + s * r - s * r * math.sin(t)) for t in np.linspace(0, math.pi / 2, 8)]
        arc2 = [(xr + MT / 2 - r + r * math.sin(t), yc + s * r - s * r * math.cos(t)) for t in np.linspace(0, math.pi / 2, 8)]
        pts = [(xl - MT / 2, cy + s * H)] + arc1 + arc2 + [(xr + MT / 2, cy + s * H)]
        _band(ax, pts, zorder=zorder)
    out = {"wall": np.array([cx + wall * 0.3, cy + H * 0.8]), "membrane": np.array([xl - MT / 2, cy + H * 0.6]),
           "sleeve": np.array([cx + wall * 0.25, cy + width * 0.3])}
    _rect(ax, xl, yb + MT / 2, wall, width - MT, "cytoplasm", zorder=zorder - 3)
    if desmotubule:
        dw = width * 0.32
        ex = length / 2 - 0.1
        # ER cisternae on both sides joined by the desmotubule
        for s in (-1, 1):
            ax.add_patch(FancyBboxPatch((cx + s * (wall / 2 + 0.25) - (0 if s > 0 else ex - wall / 2), cy - 0.25), ex - wall / 2 - 0.25, 0.5,
                                        boxstyle="round,pad=0,rounding_size=0.2", facecolor=_f("er"), edgecolor=_e("er"), lw=0.9,
                                        zorder=zorder - 0.5))
        ax.add_patch(FancyBboxPatch((xl - 0.35, cy - dw / 2), wall + 0.7, dw, boxstyle="round,pad=0,rounding_size=0.04",
                                    facecolor=_f("er"), edgecolor=_e("er"), lw=0.9, zorder=zorder + 0.5))
        out["desmotubule"] = np.array([cx - wall * 0.2, cy])
        out["er"] = np.array([cx + wall / 2 + 0.6, cy - 0.25])
    if callose:
        for s in (-1, 1):
            for t in (1, -1):
                xc = cx + s * (wall / 2 - 0.08)
                yc = cy + t * (width / 2 + MT + 0.12)
                ax.add_patch(Ellipse((xc, yc), 0.22, 0.2, facecolor=_f("callose"), edgecolor=_e("callose"), lw=0.6, zorder=zorder + 0.8))
        out["callose"] = np.array([cx + wall / 2 - 0.08, cy + width / 2 + MT + 0.12])
    return out
