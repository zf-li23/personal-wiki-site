"""Embryology: eggs and cleavage patterns, blastulae and gastrulae of the model species, the six
movements of epithelial sheets, the extraembryonic membranes and the placenta.

    from wikibio import embryology as E
    E.egg(ax, (2, 2), 1.0, "meso")                      yolk distribution: iso / meso / telo / centro
    E.cleavage(ax, (5, 2), 1.0, "spiral")               radial / unequal / spiral / spiral-sinistral /
                                                        bilateral / rotational / discoidal / superficial
    a = E.blastula(ax, (8, 2), 1.2, "frog")             sea-urchin / frog / zebrafish / chick / fly / mouse
    a = E.gastrula(ax, (11, 2), 1.2, "sea-urchin")      sea-urchin / frog / zebrafish / chick / mouse / human
    a = E.streak(ax, (2, 2), 1.5)                       chick blastoderm from above: streak, node, areas
    a = E.sheet(ax, (2, 2), 2.0, "invagination")        invagination / involution / epiboly / ingression /
                                                        delamination / convergent-extension
    a = E.amniote_egg(ax, (4, 3), 2.5)                  bird egg: amnion, chorion, allantois, yolk sac
    a = E.villus(ax, (0, 0, 8, 5))                      a chorionic villus in the intervillous space
    E.legend(ax, (1, 0.5), ("ectoderm", "mesoderm", "endoderm", "yolk"))

Conventions. Sections are drawn with the animal pole up; in sagittal sections of vertebrate gastrulae
dorsal is on the right (frog, zebrafish) and, in the mouse egg cylinder, anterior is on the left and
the proximal (extraembryonic) end up. Germ layers keep the colours of ``zoology.GERM`` (ectoderm blue,
mesoderm red, endoderm yellow); other tissues use ``TISSUE`` (yolk beige, trophoblast pink, epiblast
green, hypoblast and visceral endoderm pale yellow, amnion pale blue, extraembryonic mesoderm pale red,
fluid-filled cavities the pale "vacuole" wash). Every function returns a dict of anchor points (canvas
coordinates) named after the structures drawn, for ``bio.callout`` and arrows; ``"r"`` is the outline
radius where one applies. Drawing is deterministic.
"""

import math

import numpy as np
from matplotlib.patches import Circle, Ellipse, PathPatch
from matplotlib.path import Path

from . import palette as P
from .core import LINE, arrow, blob, polyline
from .zoology import GERM

TISSUE = {
    "ectoderm": GERM["ectoderm"], "mesoderm": GERM["mesoderm"], "endoderm": GERM["endoderm"],
    "yolk": "lipid_tail", "cytoplasm": "cytoplasm", "fluid": "vacuole", "blood": "blood",
    "trophoblast": "receptor", "syncytiotrophoblast": "drug", "epiblast": "positive", "hypoblast": "lipid",
    "amnion": "dna2", "chorion": "metabolite", "allantois": "carbohydrate", "extraembryonic-mesoderm": "rrna",
    "germline": "protein", "ysl": "atp", "maternal": "bone", "nucleus": "nucleus",
}
NAMES = {
    "ectoderm": "Ectoderm", "mesoderm": "Mesoderm", "endoderm": "Endoderm", "yolk": "Yolk", "fluid": "Fluid-filled cavity",
    "trophoblast": "Trophoblast", "syncytiotrophoblast": "Syncytiotrophoblast", "epiblast": "Epiblast",
    "hypoblast": "Hypoblast / VE", "amnion": "Amnion", "chorion": "Chorion", "allantois": "Allantois",
    "extraembryonic-mesoderm": "Extraembryonic mesoderm", "germline": "Germ line", "ysl": "Yolk syncytial layer",
    "cytoplasm": "Cytoplasm", "blood": "Blood", "maternal": "Maternal tissue",
}


def tok(name):
    """Palette token of a tissue name (``TISSUE``), or the name itself if it already is a token."""
    return TISSUE.get(name, name)


# ---------------------------------------------------------------------------------------------
# geometry helpers


def _arc(c, r, a0, a1, n=48):
    """Points on a circular arc from angle a0 to a1 (degrees); r may be a function of the angle."""
    t = np.radians(np.linspace(a0, a1, n))
    rr = np.array([r(math.degrees(x)) for x in t]) if callable(r) else np.full(n, float(r))
    return np.c_[c[0] + rr * np.cos(t), c[1] + rr * np.sin(t)]


def _sector(c, r0, r1, a0, a1, n=40):
    """An annular sector between radii r0 < r1 (numbers or functions of the angle in degrees)."""
    return np.vstack([_arc(c, r1, a0, a1, n), _arc(c, r0, a1, a0, n)])


def _patch(ax, pts, token, z=5, lw=LINE * 0.8, face=None, edge=None, ls="-", hole=None):
    """Fill a closed polygon (optionally with one polygonal hole) in a token's colours; returns the patch."""
    pts = np.asarray(pts, float)
    verts, codes = [pts, pts[:1]], [Path.MOVETO] + [Path.LINETO] * (len(pts) - 1) + [Path.CLOSEPOLY]
    if hole is not None:
        h = np.asarray(hole, float)[::-1]
        verts += [h, h[:1]]
        codes += [Path.MOVETO] + [Path.LINETO] * (len(h) - 1) + [Path.CLOSEPOLY]
    patch = PathPatch(Path(np.vstack(verts), codes), facecolor=face or P.fill(token), edgecolor=edge or P.edge(token),
                      lw=lw, zorder=z, joinstyle="round", ls=ls)
    ax.add_patch(patch)
    return patch


def _ellipse_pts(c, rx, ry, n=120, a0=0.0, a1=360.0):
    t = np.radians(np.linspace(a0, a1, n))
    return np.c_[c[0] + rx * np.cos(t), c[1] + ry * np.sin(t)]


def _nucleus(ax, xy, r, token, z):
    ax.add_patch(Circle(xy, r, facecolor=P.light(token), edgecolor=P.edge(token), lw=LINE * 0.5, zorder=z))


def _cells_ring(ax, c, r0, r1, a0, a1, n, token, z=6, nuclei=True, lw=LINE * 0.7):
    """n epithelial cells as annular sectors between radii r0 and r1 (numbers or functions of angle)."""
    tokens = token if isinstance(token, (list, tuple)) else [token] * n
    edges = np.linspace(a0, a1, n + 1)
    centres = []
    for k in range(n):
        p, q = edges[k], edges[k + 1]
        _patch(ax, _sector(c, r0, r1, p, q, 10), tokens[k], z=z, lw=lw)
        m = (p + q) / 2
        ra = r0(m) if callable(r0) else r0
        rb = r1(m) if callable(r1) else r1
        rm = (ra + rb) / 2
        xy = (c[0] + rm * math.cos(math.radians(m)), c[1] + rm * math.sin(math.radians(m)))
        centres.append(xy)
        if nuclei:
            w = min(rb - ra, rm * math.radians(q - p))
            _nucleus(ax, xy, 0.22 * w, tokens[k], z + 0.1)
    return centres


def _cells_strip(ax, pts, thick, n, token, z=6, nuclei=True, lw=LINE * 0.7, k=10):
    """n cells along an open centreline ``pts``, each a quadrilateral of the given thickness
    (a number or a function of the fraction 0..1 along the line). Returns the cell centres."""
    q, nrm, _ = polyline(pts, n * k + 1, closed=False)
    tokens = token if isinstance(token, (list, tuple)) else [token] * n
    centres = []
    for i in range(n):
        s = slice(i * k, (i + 1) * k + 1)
        f = (np.arange(i * k, (i + 1) * k + 1)) / (n * k)
        h = np.array([thick(x) for x in f]) if callable(thick) else np.full(len(f), float(thick))
        outer = q[s] + nrm[s] * (h[:, None] / 2)
        inner = q[s] - nrm[s] * (h[:, None] / 2)
        _patch(ax, np.vstack([outer, inner[::-1]]), tokens[i], z=z, lw=lw)
        mid = q[i * k + k // 2]
        centres.append((float(mid[0]), float(mid[1])))
        if nuclei:
            seg = np.hypot(*(q[(i + 1) * k] - q[i * k]))
            _nucleus(ax, mid, 0.22 * min(seg, h[k // 2]), tokens[i], z + 0.1)
    return centres


def _round_cell(ax, xy, rx, ry, token, z=6, angle=0.0, seed=0, nucleus=True, face=None):
    o = blob(xy, rx, ry, wobble=0.04, seed=seed, k=8, angle=angle)
    ax.add_patch(PathPatch(Path(o, closed=True), facecolor=face or P.fill(token), edgecolor=P.edge(token), lw=LINE * 0.8, zorder=z))
    if nucleus:
        _nucleus(ax, xy, 0.3 * min(rx, ry), token, z + 0.1)


def _dots(ax, region_pts, spacing, r, token, z, seed=0, jitter=0.3):
    """Small dots (yolk platelets, nuclei) scattered on a jittered grid inside a polygon."""
    path = Path(region_pts)
    x0, y0 = region_pts.min(0)
    x1, y1 = region_pts.max(0)
    rng = np.random.default_rng(seed)
    out = []
    for yy in np.arange(y0 + spacing / 2, y1, spacing):
        for xx in np.arange(x0 + spacing / 2, x1, spacing):
            p = (xx + rng.uniform(-jitter, jitter) * spacing, yy + rng.uniform(-jitter, jitter) * spacing)
            if path.contains_point(p, radius=-r * 2):
                ax.add_patch(Circle(p, r, facecolor=P.edge(token), edgecolor="none", zorder=z))
                out.append(p)
    return out


def _clip_lines(ax, patch, segments, token, lw=LINE * 0.5, z=None):
    """Thin lines (cell boundaries drawn over a tissue region) clipped to ``patch``."""
    for seg in segments:
        seg = np.asarray(seg, float)
        (ln,) = ax.plot(seg[:, 0], seg[:, 1], color=P.edge(token), lw=lw, zorder=z or patch.get_zorder() + 0.1,
                        solid_capstyle="round")
        ln.set_clip_path(patch)


def _pt(c, r, a):
    return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))


# ---------------------------------------------------------------------------------------------
# eggs and cleavage


def egg(ax, c, r=1.0, yolk="iso", z=5):
    """An egg in section coloured by yolk distribution (yolk platelets as dots).

    yolk: "iso" (little, even: sea urchin, mammals), "meso" (moderate, vegetal: amphibians),
    "telo" (dense, all but a small blastodisc: birds, fish), "centro" (central: insects, drawn elongated).
    Returns anchors: animal, vegetal, nucleus, yolk, r.
    """
    x, y = c
    yk, cy = tok("yolk"), tok("cytoplasm")
    if yolk == "centro":
        outline = _ellipse_pts(c, 1.35 * r, 0.62 * r)
        _patch(ax, outline, cy, z=z, lw=LINE)
        inner = _ellipse_pts(c, 1.2 * r, 0.5 * r)
        _patch(ax, inner, yk, z=z + 0.1, lw=LINE * 0.6)
        _dots(ax, inner, 0.17 * r, 0.035 * r, yk, z + 0.2, seed=3)
        _nucleus(ax, c, 0.13 * r, "nucleus", z + 0.4)
        return {"animal": (x, y + 0.62 * r), "vegetal": (x, y - 0.62 * r), "nucleus": c, "yolk": (x + 0.6 * r, y),
                "periplasm": (x, y + 0.56 * r), "r": r}
    outline = _ellipse_pts(c, r, r)
    _patch(ax, outline, cy, z=z, lw=LINE)
    if yolk == "iso":
        _dots(ax, _ellipse_pts(c, 0.9 * r, 0.9 * r), 0.2 * r, 0.03 * r, yk, z + 0.2, seed=1, jitter=0.35)
        nuc = c
    elif yolk == "meso":
        lo = np.vstack([_arc(c, 0.98 * r, -170, -10), [_pt(c, 0.98 * r, -170)]])
        reg = np.vstack([_arc(c, r * 0.985, 195, 345), [(x, y - 0.15 * r)]])
        _patch(ax, _arc(c, r * 0.985, 192, 348, 60), yk, z=z + 0.05, lw=0, face=P.mix(P.fill(yk), P.fill(cy), 0.25))
        _dots(ax, reg, 0.15 * r, 0.04 * r, yk, z + 0.2, seed=2)
        _dots(ax, _ellipse_pts((x, y + 0.05 * r), 0.85 * r, 0.25 * r), 0.24 * r, 0.025 * r, yk, z + 0.2, seed=4)
        del lo
        nuc = (x, y + 0.5 * r)
    elif yolk == "telo":
        _patch(ax, outline, yk, z=z + 0.05, lw=LINE)
        _dots(ax, _ellipse_pts(c, 0.88 * r, 0.88 * r), 0.16 * r, 0.04 * r, yk, z + 0.2, seed=5)
        cap = np.vstack([_arc(c, r, 62, 118, 30), _ellipse_pts((x, y + 0.86 * r), 0.47 * r, 0.1 * r, 30, 180, 360)])
        _patch(ax, cap, cy, z=z + 0.3, lw=LINE * 0.8)
        nuc = (x, y + 0.9 * r)
    else:
        raise ValueError(f"unknown yolk distribution {yolk!r}")
    _nucleus(ax, nuc, 0.11 * r if yolk != "telo" else 0.06 * r, "nucleus", z + 0.5)
    return {"animal": (x, y + r), "vegetal": (x, y - r), "nucleus": nuc, "yolk": (x, y - 0.6 * r), "r": r}


def cleavage(ax, c, r=1.0, pattern="radial", z=5, labels=False):
    """An early cleavage stage that shows the pattern of a cleavage type.

    "radial" (8-cell, side view: tiers stacked directly above each other), "unequal" (amphibian 8-cell:
    the third, equatorial furrow displaced towards the animal pole), "spiral" / "spiral-sinistral"
    (8-cell from the animal pole: the micromere quartet 1a–1d sits over the furrows, turned clockwise or
    anticlockwise), "bilateral" (ascidian 8-cell from the vegetal pole, mirror-symmetric about the
    midline; the posterior-vegetal pair carries the yellow crescent), "rotational" (mammalian 4-cell: the
    two blastomeres divide in perpendicular planes, inside the zona), "discoidal" (furrows cut only a
    blastodisc on the yolk), "superficial" (syncytial nuclei in the cortex around a central yolk).
    Returns anchors (cell names where they exist: A, B, C, D, 1a…1d for spiral; "crescent" for bilateral).
    """
    x, y = c
    cy, yk = tok("cytoplasm"), tok("yolk")
    out = {"r": r}
    if pattern in ("radial", "unequal"):
        top_h, bot_h = (0.42, 0.42) if pattern == "radial" else (0.3, 0.56)
        yb = y - r + bot_h * r * 1.05
        yt = yb + bot_h * r + top_h * r
        for dz, light in ((0.16, True), (0.0, False)):  # back row, then front row
            for k, dx in enumerate((-0.48, 0.48)):
                face = P.mix(P.fill(cy), P.surface(), 0.35) if light else None
                _round_cell(ax, (x + dx * r, yb + dz * r), 0.47 * r, bot_h * r, yk if pattern == "unequal" else cy, z + (0 if light else 1),
                            seed=k + 3, face=face)
                _round_cell(ax, (x + dx * r, yt + dz * r), 0.47 * r, top_h * r, cy, z + (0 if light else 1), seed=k + 7, face=face)
        out.update(animal=(x, yt + top_h * r + 0.16 * r), vegetal=(x, yb - bot_h * r), animal_tier=(x + 0.48 * r, yt),
                   vegetal_tier=(x + 0.48 * r, yb))
        return out
    if pattern.startswith("spiral"):
        sgn = -1 if pattern == "spiral" else 1  # dextral: micromeres displaced clockwise seen from the animal pole
        names = "ABCD"
        for k in range(4):
            a = 135 - 90 * k  # A top-left, then B, C, D clockwise
            p = _pt(c, 0.5 * r, a)
            _round_cell(ax, p, 0.5 * r, 0.5 * r, cy, z, seed=k, face=P.mix(P.fill(cy), P.surface(), 0.2))
            out[names[k]] = p
        for k in range(4):
            a = 135 - 90 * k + sgn * 45 * 0.6  # over the furrows, turned
            p = _pt(c, 0.42 * r, a)
            _round_cell(ax, p, 0.26 * r, 0.26 * r, tok("ectoderm"), z + 1, seed=k + 10)
            out["1" + names[k].lower()] = p
        # rotation arrow (sense of the shift)
        arc = _arc(c, 1.15 * r, 60, 20) if sgn < 0 else _arc(c, 1.15 * r, 120, 160)
        arrow(ax, arc[0], arc[-1], kind="process", bend=-0.25 * sgn, head=0.16 * r, lw=LINE * 0.9, color=P.muted())
        out["arrow"] = tuple(arc[len(arc) // 2])
        return out
    if pattern == "bilateral":
        # vegetal view, anterior up: four pairs mirror-symmetric about the midline
        pos = [(-0.42, 0.45), (0.42, 0.45), (-0.42, -0.4), (0.42, -0.4)]
        for k, (dx, dy) in enumerate(pos):
            for side in (0,):
                del side
            rx, ry = 0.4 * r, 0.42 * r
            _round_cell(ax, (x + dx * r, y + dy * r), rx, ry, cy, z, seed=k + 20)
        for dx in (-0.42, 0.42):  # posterior-vegetal pair (B4.1) with the yellow crescent
            cre = _ellipse_pts((x + dx * r, y - 0.62 * r), 0.3 * r, 0.12 * r, 40, 180, 360)
            cre = np.vstack([cre, _ellipse_pts((x + dx * r, y - 0.6 * r), 0.3 * r, 0.05 * r, 40, 0, -180)[::-1][::-1]])
            _patch(ax, cre, "highlight", z=z + 1.5, lw=LINE * 0.6)
        ax.plot([x, x], [y - 1.0 * r, y + 1.0 * r], color=P.muted(), lw=0.9, ls=(0, (3, 2)), zorder=z + 2)
        out.update(crescent=(x + 0.42 * r, y - 0.66 * r), midline=(x, y + 0.98 * r), anterior=(x, y + 0.9 * r),
                   posterior=(x, y - 0.9 * r))
        return out
    if pattern == "rotational":
        # inside the zona: one blastomere divided meridionally (left, side by side in depth), the other equatorially
        ax.add_patch(Circle(c, 1.12 * r, facecolor=P.mix(P.fill("bone"), P.surface(), 0.3), edgecolor=P.edge("bone"), lw=LINE * 0.9, zorder=z))
        ax.add_patch(Circle(c, 1.0 * r, facecolor=P.fill("extracellular"), edgecolor=P.edge("bone"), lw=LINE * 0.6, zorder=z + 0.1))
        _round_cell(ax, (x - 0.42 * r, y + 0.3 * r), 0.42 * r, 0.42 * r, "animal", z + 1, seed=1, face=P.mix(P.fill("animal"), P.surface(), 0.3))
        _round_cell(ax, (x - 0.5 * r, y - 0.12 * r), 0.43 * r, 0.43 * r, "animal", z + 2, seed=2)
        _round_cell(ax, (x + 0.48 * r, y + 0.42 * r), 0.42 * r, 0.4 * r, "animal", z + 2, seed=3)
        _round_cell(ax, (x + 0.48 * r, y - 0.42 * r), 0.42 * r, 0.4 * r, "animal", z + 2, seed=4)
        out.update(meridional=(x - 0.5 * r, y), equatorial=(x + 0.48 * r, y), zona=_pt(c, 1.06 * r, 60))
        return out
    if pattern == "discoidal":
        _patch(ax, _ellipse_pts(c, r, r), yk, z=z, lw=LINE)
        _dots(ax, _ellipse_pts(c, 0.88 * r, 0.88 * r), 0.16 * r, 0.035 * r, yk, z + 0.1, seed=6)
        cap = np.vstack([_arc(c, r, 50, 130, 40), _ellipse_pts((x, y + 0.7 * r), 0.64 * r, 0.12 * r, 40, 180, 360)])
        patch = _patch(ax, cap, cy, z=z + 0.3, lw=LINE * 0.8)
        segs = [[(x + dx * r, y + 1.2 * r), (x + dx * r, y + 0.74 * r)] for dx in (-0.36, -0.12, 0.12, 0.36)]
        _clip_lines(ax, patch, segs, cy, lw=LINE * 0.8)
        out.update(blastodisc=(x, y + 0.85 * r), yolk=(x, y - 0.3 * r), furrow=(x + 0.12 * r, y + 0.78 * r))
        return out
    if pattern == "superficial":
        outline = _ellipse_pts(c, 1.35 * r, 0.62 * r)
        _patch(ax, outline, cy, z=z, lw=LINE)
        inner = _ellipse_pts(c, 1.22 * r, 0.5 * r)
        _patch(ax, inner, yk, z=z + 0.1, lw=LINE * 0.6)
        _dots(ax, inner, 0.17 * r, 0.03 * r, yk, z + 0.2, seed=7)
        t = np.radians(np.linspace(0, 360, 34, endpoint=False))
        for tt in t:
            ax.add_patch(Circle((x + 1.28 * r * math.cos(tt), y + 0.56 * r * math.sin(tt)), 0.045 * r,
                                facecolor=P.edge("nucleus"), edgecolor="none", zorder=z + 0.5))
        for k, (dx, dy) in enumerate(((1.45, 0.08), (1.47, -0.12), (1.38, -0.28), (1.36, 0.24))):
            _round_cell(ax, (x + dx * r, y + dy * r), 0.1 * r, 0.1 * r, tok("germline"), z + 0.6, seed=k, nucleus=False)
        out.update(nuclei=(x, y + 0.56 * r), yolk=(x - 0.3 * r, y), pole_cells=(x + 1.5 * r, y), anterior=(x - 1.35 * r, y),
                   posterior=(x + 1.35 * r, y))
        return out
    raise ValueError(f"unknown cleavage pattern {pattern!r}")


# ---------------------------------------------------------------------------------------------
# blastulae


def blastula(ax, c, r=1.2, species="sea-urchin", z=5):
    """A blastula (or its equivalent) in section, animal pole up, cells coloured by prospective germ layer.

    species: "sea-urchin" (hollow coeloblastula, vegetal plate thickened), "frog" (multilayered animal
    cap, blastocoel displaced to the animal half, large yolky vegetal cells), "zebrafish" (blastoderm on the
    yolk cell: enveloping layer, deep cells, yolk syncytial layer), "chick" (area pellucida over the
    subgerminal cavity, area opaca on the yolk, hypoblast islands; posterior on the right), "fly" (cellular
    blastoderm around the yolk, pole cells posterior; anterior on the left), "mouse" (blastocyst: polar and
    mural trophectoderm, epiblast and primitive endoderm).
    """
    x, y = c
    ec, me, en = tok("ectoderm"), tok("mesoderm"), tok("endoderm")
    fl = tok("fluid")
    out = {"r": r}
    if species == "sea-urchin":
        ax.add_patch(Circle(c, 1.04 * r, facecolor="none", edgecolor=P.muted(), lw=LINE * 0.6, zorder=z))
        ax.add_patch(Circle(c, 0.98 * r, facecolor=P.fill(fl), edgecolor="none", zorder=z - 0.5))
        thick = lambda a: 0.98 * r - (0.3 if abs(((a + 90 + 180) % 360) - 180) < 40 else 0.17) * r  # noqa: E731
        n = 36
        tokens = []
        for k in range(n):
            a = -90 + (k + 0.5) * 360 / n
            d = abs(((a + 90 + 180) % 360) - 180)
            tokens.append(me if d < 12 else en if d < 40 else ec)
        _cells_ring(ax, c, thick, 0.98 * r, -90, 270, n, tokens, z=z + 1)
        out.update(blastocoel=(x, y + 0.1 * r), hyaline=_pt(c, 1.04 * r, 35), animal=(x, y + r), vegetal=(x, y - r),
                   vegetal_plate=_pt(c, 0.78 * r, -62), skeletogenic=_pt(c, 0.78 * r, -90), ectoderm=_pt(c, 0.88 * r, 150))
        return out
    if species == "frog":
        outer = _ellipse_pts(c, r, r)
        bc = (x - 0.05 * r, y + 0.32 * r)
        hole = _ellipse_pts(bc, 0.55 * r, 0.33 * r)
        # bands by latitude
        ya, yv = y + 0.05 * r, y - 0.3 * r
        ang_a = math.degrees(math.asin((ya - y) / r))
        ang_v = math.degrees(math.asin((yv - y) / r))
        top = np.vstack([_arc(c, r, ang_a, 180 - ang_a, 60)])
        mid = np.vstack([_arc(c, r, ang_v, ang_a, 20), _arc(c, r, 180 - ang_a, 180 - ang_v, 20)])
        bot = _arc(c, r, 180 - ang_v, 360 + ang_v, 60)
        _patch(ax, outer, en, z=z, lw=0)
        _patch(ax, bot, en, z=z + 0.1, lw=0)
        _patch(ax, mid, me, z=z + 0.1, lw=0)
        _patch(ax, top, ec, z=z + 0.1, lw=0)
        tissue = _patch(ax, outer, ec, z=z + 0.2, lw=LINE, face="none", hole=hole)
        tissue.set_facecolor("none")
        ax.add_patch(PathPatch(Path(np.vstack([hole, hole[:1]]), closed=True), facecolor=P.fill(fl), edgecolor=P.edge(ec),
                               lw=LINE * 0.8, zorder=z + 0.3))
        # cell boundaries: small cells in the animal cap, large ones in the vegetal mass
        clip = PathPatch(Path(np.vstack([outer, outer[:1]]), closed=True), facecolor="none", edgecolor="none", zorder=z)
        ax.add_patch(clip)
        segs = []
        for a in np.arange(6, 180, 12):
            segs.append([_pt(c, 0.55 * r, a), _pt(c, 1.2 * r, a)])
        for rr in (0.78, 0.89):
            segs.append(_arc(c, rr * r, 0, 180, 40))
        for yy in np.arange(y - 0.92 * r, ya, 0.27 * r):
            segs.append([(x - r, yy), (x + r, yy)])
        for k, yy in enumerate(np.arange(y - r, ya, 0.27 * r)):
            for xx in np.arange(x - r + (0.15 * r if k % 2 else 0), x + r, 0.3 * r):
                segs.append([(xx, yy), (xx, yy + 0.27 * r)])
        _clip_lines(ax, clip, segs, "neutral", lw=LINE * 0.35, z=z + 0.15)
        out.update(blastocoel=bc, animal_cap=(x, y + 0.82 * r), marginal_zone=_pt(c, 0.85 * r, -8), vegetal=(x, y - 0.6 * r),
                   animal=(x, y + r), vegetal_pole=(x, y - r))
        return out
    if species == "zebrafish":
        yc = (x, y - 0.25 * r)
        ry = 0.78 * r
        _patch(ax, _ellipse_pts(yc, ry, ry), tok("yolk"), z=z, lw=LINE)
        _dots(ax, _ellipse_pts(yc, 0.7 * ry, 0.7 * ry), 0.14 * r, 0.03 * r, tok("yolk"), z + 0.1, seed=8)
        # blastoderm cap (dome over the top of the yolk)
        cap_out = np.vstack([_arc(yc, 1.32 * ry, 30, 150, 50)])
        cap_in = _arc(yc, ry * 1.01, 150, 30, 50)
        cap = np.vstack([cap_out, cap_in])
        _patch(ax, cap, tok("epiblast"), z=z + 0.3, lw=LINE * 0.8)
        evl = np.vstack([_arc(yc, 1.32 * ry, 29, 151, 50), _arc(yc, 1.25 * ry, 151, 29, 50)])
        _patch(ax, evl, ec, z=z + 0.4, lw=LINE * 0.7)
        ysl = np.vstack([_arc(yc, ry * 1.01, 22, 158, 50), _arc(yc, ry * 0.93, 158, 22, 50)])
        _patch(ax, ysl, tok("ysl"), z=z + 0.35, lw=LINE * 0.6)
        for a in np.linspace(26, 154, 12):
            ax.add_patch(Circle(_pt(yc, ry * 0.97, a), 0.025 * r, facecolor=P.edge(tok("ysl")), edgecolor="none", zorder=z + 0.5))
        clip = _patch(ax, cap, tok("epiblast"), z=z + 0.31, lw=0, face="none")
        segs = [[_pt(yc, ry, a), _pt(yc, 1.4 * ry, a)] for a in np.arange(30, 151, 9)]
        segs += [_arc(yc, rr * ry, 30, 150, 40) for rr in (1.09, 1.17)]
        _clip_lines(ax, clip, segs, tok("epiblast"), lw=LINE * 0.45)
        out.update(evl=_pt(yc, 1.29 * ry, 120), deep=_pt(yc, 1.13 * ry, 75), ysl=_pt(yc, 0.97 * ry, 40), yolk=(x, yc[1] - 0.2 * r),
                   margin=_pt(yc, 1.15 * ry, 30), animal=(x, yc[1] + 1.32 * ry))
        return out
    if species == "chick":
        w = 1.6 * r
        yk = tok("yolk")
        _patch(ax, np.array([(x - 1.7 * r, y - 0.8 * r), (x + 1.7 * r, y - 0.8 * r), (x + 1.7 * r, y - 0.05 * r),
                             (x - 1.7 * r, y - 0.05 * r)]), yk, z=z, lw=0)
        _dots(ax, np.array([(x - 1.7 * r, y - 0.8 * r), (x + 1.7 * r, y - 0.8 * r), (x + 1.7 * r, y - 0.1 * r),
                            (x - 1.7 * r, y - 0.1 * r)]), 0.16 * r, 0.03 * r, yk, z + 0.1, seed=9)
        cav = _ellipse_pts((x, y - 0.05 * r), 0.95 * r, 0.16 * r, 80, 180, 360)
        _patch(ax, cav, tok("fluid"), z=z + 0.2, lw=LINE * 0.5)
        _cells_strip(ax, [(x - w, y + 0.02 * r), (x + w, y + 0.02 * r)], 0.14 * r, 30, tok("epiblast"), z=z + 0.4)
        for side in (-1, 1):  # area opaca: thicker, on the yolk
            _patch(ax, np.array([(x + side * 0.98 * r, y - 0.05 * r), (x + side * w, y - 0.05 * r),
                                 (x + side * w, y - 0.18 * r), (x + side * 0.98 * r, y - 0.12 * r)]), tok("epiblast"), z=z + 0.35,
                   lw=LINE * 0.6, face=P.mix(P.fill(tok("epiblast")), P.fill(yk), 0.5))
        for k, xx in enumerate((-0.55, -0.15, 0.3)):
            _round_cell(ax, (x + xx * r, y - 0.11 * r), 0.12 * r, 0.045 * r, tok("hypoblast"), z + 0.5, seed=k, nucleus=False)
        _patch(ax, _ellipse_pts((x + 0.85 * r, y - 0.1 * r), 0.14 * r, 0.06 * r), tok("hypoblast"), z=z + 0.5, lw=LINE * 0.6,
               face=P.edge(tok("hypoblast")))
        out.update(area_pellucida=(x - 0.2 * r, y + 0.08 * r), area_opaca=(x - 1.3 * r, y - 0.05 * r), subgerminal_cavity=(x, y - 0.13 * r),
                   hypoblast=(x - 0.15 * r, y - 0.11 * r), kollers_sickle=(x + 0.85 * r, y - 0.1 * r), yolk=(x, y - 0.55 * r),
                   posterior=(x + 1.6 * r, y + 0.1 * r), anterior=(x - 1.6 * r, y + 0.1 * r))
        return out
    if species == "fly":
        outline = _ellipse_pts(c, 1.4 * r, 0.62 * r)
        _patch(ax, outline, tok("cytoplasm"), z=z, lw=LINE)
        inner = _ellipse_pts(c, 1.18 * r, 0.42 * r)
        _patch(ax, inner, tok("yolk"), z=z + 0.1, lw=LINE * 0.6)
        _dots(ax, inner, 0.15 * r, 0.03 * r, tok("yolk"), z + 0.2, seed=10)
        # columnar cells between the two ellipses
        n = 44
        t = np.linspace(0, 2 * np.pi, n + 1)
        for k in range(n):
            tt = np.linspace(t[k], t[k + 1], 6)
            o = np.c_[x + 1.4 * r * np.cos(tt), y + 0.62 * r * np.sin(tt)]
            i_ = np.c_[x + 1.19 * r * np.cos(tt[::-1]), y + 0.43 * r * np.sin(tt[::-1])]
            ang = (t[k] + t[k + 1]) / 2
            if abs(math.cos(ang)) > 0.97 and math.cos(ang) > 0:
                continue  # posterior pole: pole cells sit here
            _patch(ax, np.vstack([o, i_]), tok("ectoderm") if math.sin(ang) > -0.55 else tok("mesoderm"), z=z + 0.3, lw=LINE * 0.5)
        for k, (dx, dy) in enumerate(((1.47, 0.1), (1.5, -0.1), (1.42, 0.27), (1.42, -0.27), (1.56, 0.02))):
            _round_cell(ax, (x + dx * r, y + dy * r), 0.1 * r, 0.1 * r, tok("germline"), z + 0.6, seed=k, nucleus=False)
        out.update(blastoderm=(x - 0.4 * r, y + 0.53 * r), yolk=(x, y), pole_cells=(x + 1.55 * r, y),
                   ventral=(x, y - 0.53 * r), anterior=(x - 1.4 * r, y), posterior=(x + 1.4 * r, y))
        return out
    if species == "mouse":
        ax.add_patch(Circle(c, 1.12 * r, facecolor=P.mix(P.fill("bone"), P.surface(), 0.3), edgecolor=P.edge("bone"), lw=LINE * 0.9, zorder=z))
        ax.add_patch(Circle(c, 1.0 * r, facecolor=P.fill(fl), edgecolor=P.edge("bone"), lw=LINE * 0.6, zorder=z + 0.1))
        _cells_ring(ax, c, 0.85 * r, 0.99 * r, -90, 270, 22, tok("trophoblast"), z=z + 0.5, nuclei=True)
        icm = (x, y + 0.5 * r)
        for k, (dx, dy) in enumerate(((-0.3, 0.6), (0.0, 0.66), (0.3, 0.6), (-0.15, 0.42), (0.15, 0.42), (-0.42, 0.42), (0.42, 0.42))):
            _round_cell(ax, (x + dx * r, y + dy * r), 0.15 * r, 0.12 * r, tok("epiblast"), z + 1, seed=k)
        for k, dx in enumerate((-0.42, -0.21, 0.0, 0.21, 0.42)):
            _round_cell(ax, (x + dx * r, y + 0.26 * r), 0.11 * r, 0.06 * r, tok("hypoblast"), z + 1.2, seed=k + 9)
        out.update(epiblast=icm, primitive_endoderm=(x + 0.21 * r, y + 0.26 * r), polar_te=_pt(c, 0.92 * r, 80),
                   mural_te=_pt(c, 0.92 * r, -60), blastocoel=(x, y - 0.25 * r), zona=_pt(c, 1.06 * r, 150))
        return out
    raise ValueError(f"unknown species {species!r}")


# ---------------------------------------------------------------------------------------------
# gastrulae


def gastrula(ax, c, r=1.2, species="sea-urchin", z=5, epiboly=0.6):
    """A gastrula in section, coloured by germ layer.

    "sea-urchin" (archenteron invaginated from the vegetal plate, primary mesenchyme in the blastocoel,
    secondary mesenchyme at the archenteron tip), "frog" (mid-gastrula, sagittal, dorsal right: bottle cells
    at the dorsal lip, involuted mesoderm under the ectoderm, archenteron, shrinking blastocoel, yolk
    plug), "zebrafish" (shield stage at ``epiboly`` coverage: germ ring and shield on the dorsal side,
    right), "chick" (transverse section through the primitive streak), "mouse" (egg cylinder at E7,
    anterior left), "human" (day-14 conceptus implanted in the endometrium).
    """
    x, y = c
    ec, me, en, fl = tok("ectoderm"), tok("mesoderm"), tok("endoderm"), tok("fluid")
    out = {"r": r}
    if species == "sea-urchin":
        ax.add_patch(Circle(c, 0.98 * r, facecolor=P.fill(fl), edgecolor="none", zorder=z - 0.5))
        gap = 16
        _cells_ring(ax, c, 0.82 * r, 0.98 * r, -90 + gap, 270 - gap, 32, ec, z=z + 1)
        # archenteron: a U of endoderm cells from one lip of the blastopore round the tip to the other
        lipL, lipR = _pt(c, 0.9 * r, -90 - gap + 1), _pt(c, 0.9 * r, -90 + gap - 1)
        h = 0.95
        top = y + (h - 1) * r + 0.45 * r
        cl = [lipL, (x - 0.2 * r, y - 0.55 * r), (x - 0.15 * r, top - 0.2 * r), (x, top), (x + 0.15 * r, top - 0.2 * r),
              (x + 0.2 * r, y - 0.55 * r), lipR]
        q, _, _ = polyline(cl, 200, closed=False)
        from scipy.ndimage import gaussian_filter1d  # smooth the centreline
        q = np.c_[gaussian_filter1d(q[:, 0], 8, mode="nearest"), gaussian_filter1d(q[:, 1], 8, mode="nearest")]
        q[0], q[-1] = lipL, lipR
        _patch(ax, np.vstack([q, q[:1]]), fl, z=z + 0.6, lw=0)
        toks = [en] * 14
        toks[6] = toks[7] = me
        _cells_strip(ax, q, 0.13 * r, 14, toks, z=z + 1)
        tip = (x, top)
        # secondary mesenchyme filopodia to the animal wall
        for dx in (-0.35, 0.0, 0.35):
            end = _pt(c, 0.82 * r, 90 + dx * 60)
            ax.plot([x + dx * 0.15 * r, end[0]], [top + 0.05 * r, end[1]], color=P.edge(me), lw=0.7, zorder=z + 0.8)
        # primary mesenchyme cells: two ventrolateral clusters near the vegetal wall
        for k, a in enumerate((-125, -115, -105, -75, -65, -55, -140, -40)):
            _round_cell(ax, _pt(c, 0.72 * r, a), 0.055 * r, 0.055 * r, me, z + 1.2, seed=k, nucleus=False)
        out.update(archenteron=(x, y - 0.35 * r), blastopore=(x, y - 0.98 * r), tip=tip, smc=(x + 0.05 * r, top + 0.1 * r),
                   pmc=_pt(c, 0.72 * r, -125), blastocoel=(x + 0.45 * r, y + 0.25 * r), ectoderm=_pt(c, 0.9 * r, 150),
                   animal=(x, y + r))
        return out
    if species == "frog":
        outer = _ellipse_pts(c, r, r)
        _patch(ax, outer, en, z=z, lw=LINE)
        _dots(ax, _ellipse_pts((x - 0.15 * r, y - 0.3 * r), 0.45 * r, 0.32 * r), 0.13 * r, 0.025 * r, en, z + 0.05, seed=11)
        lipD, lipV = -50, -115
        # blastocoel (ventral-animal, shrinking as the mesoderm advances)
        bc = (x - 0.36 * r, y + 0.3 * r)
        _patch(ax, _ellipse_pts(bc, 0.27 * r, 0.24 * r), fl, z=z + 0.2, lw=LINE * 0.6)
        # involuted mesoderm under the dorsal ectoderm (towards the animal pole) and a short ventral band
        _patch(ax, _sector(c, 0.68 * r, 0.84 * r, lipD + 4, 100, 60), me, z=z + 0.3, lw=LINE * 0.7)
        _patch(ax, _sector(c, 0.72 * r, 0.84 * r, 205, lipV + 360 - 4, 20), me, z=z + 0.3, lw=LINE * 0.7)
        # archenteron: a crescent under the dorsal mesoderm (endoderm roof between them), joined to the
        # surface by the slit of the blastopore
        _patch(ax, _sector(c, 0.5 * r, lambda a: r * (0.65 - 0.1 * max(0, (a - 40) / 40)), lipD - 2, 80, 50), fl, z=z + 0.35, lw=LINE * 0.6)
        _patch(ax, _sector(c, 0.55 * r, 1.01 * r, lipD - 7, lipD - 1, 6), fl, z=z + 0.36, lw=0)
        # ectoderm covering everything except the yolk plug
        sec = _sector(c, 0.84 * r, r, lipD, lipV + 360, 120)
        _patch(ax, sec, ec, z=z + 0.4, lw=LINE * 0.8)
        clip = _patch(ax, sec, ec, z=z + 0.41, lw=0, face="none")
        _clip_lines(ax, clip, [[_pt(c, 0.8 * r, a), _pt(c, 1.05 * r, a)] for a in np.arange(lipD + 8, lipV + 360, 10)], ec, lw=LINE * 0.45)
        # bottle cells lining the blastopore: wedges with their narrow apical necks at the surface
        for k, a in enumerate((lipD - 8.5, lipD - 11, lipD - 13.5)):
            p0, p1 = _pt(c, 0.995 * r, a), _pt(c, 0.995 * r, a - 1.2)
            q0, q1 = _pt(c, 0.74 * r, a + 1.0), _pt(c, 0.74 * r, a - 3.6)
            _patch(ax, np.array([p0, q0, q1, p1]), en, z=z + 0.6, lw=LINE * 0.6, face=P.mix(P.fill(en), P.edge(en), 0.4))
        out.update(ectoderm=_pt(c, 0.92 * r, 140), mesoderm=_pt(c, 0.76 * r, 40), archenteron=_pt(c, 0.57 * r, 20), blastocoel=bc,
                   yolk_plug=_pt(c, 0.96 * r, (lipD + lipV) / 2 - 8), dorsal_lip=_pt(c, r, lipD), ventral_lip=_pt(c, r, lipV),
                   bottle_cells=_pt(c, 0.9 * r, lipD - 11), endoderm=(x - 0.15 * r, y - 0.3 * r), animal=(x, y + r), dorsal=(x + r, y),
                   ventral=(x - r, y), blastopore=_pt(c, r, lipD - 4))
        return out
    if species == "zebrafish":
        ry = 0.9 * r
        _patch(ax, _ellipse_pts(c, ry, ry), tok("yolk"), z=z, lw=LINE)
        _dots(ax, _ellipse_pts(c, 0.78 * ry, 0.78 * ry), 0.15 * r, 0.03 * r, tok("yolk"), z + 0.1, seed=12)
        lat = 90 - 180 * epiboly  # latitude of the margin (degrees)
        # YSL under the blastoderm
        _patch(ax, _sector(c, 0.93 * ry, 1.0 * ry, lat - 6, 180 - lat + 6, 80), tok("ysl"), z=z + 0.2, lw=LINE * 0.5)
        dors = lat + 16  # centre of the shield (dorsal, right)
        top = lambda a: ry * (1.15 + 0.11 * math.exp(-(((a - dors) / 11.0) ** 2)))  # noqa: E731
        # epiblast (prospective ectoderm) over the top, thickened in the shield
        _patch(ax, _sector(c, ry * 1.0, top, lat, 180 - lat, 120), ec, z=z + 0.3, lw=LINE * 0.7)
        # germ ring: involuted hypoblast (mesendoderm) under the epiblast near the margin; thicker in the shield
        _patch(ax, _sector(c, ry * 1.0, ry * 1.07, 154 - lat, 180 - lat, 20), me, z=z + 0.35, lw=LINE * 0.6)
        _patch(ax, _sector(c, ry * 1.0, lambda a: ry * (1.07 + 0.05 * math.exp(-(((a - dors) / 11.0) ** 2))), lat, lat + 34, 30), me,
               z=z + 0.35, lw=LINE * 0.6)
        # enveloping layer
        _patch(ax, _sector(c, top, lambda a: top(a) + 0.045 * ry, lat - 1, 181 - lat, 120), "dna2", z=z + 0.4, lw=LINE * 0.6)
        out.update(evl=_pt(c, 1.17 * ry, 120), epiblast=_pt(c, 1.1 * ry, 100), hypoblast=_pt(c, 1.035 * ry, 180 - lat - 10),
                   shield=_pt(c, 1.2 * ry, dors), germ_ring=_pt(c, 1.05 * ry, 180 - lat - 6), ysl=_pt(c, 0.96 * ry, 60),
                   yolk=(x, y - 0.3 * r), margin=_pt(c, 1.1 * ry, lat), dorsal=(x + 1.2 * ry, y), ventral=(x - 1.2 * ry, y))
        return out
    if species == "chick":
        w = 1.7 * r
        groove = lambda xx: -0.12 * r * math.exp(-((xx - x) / (0.12 * r)) ** 2)  # noqa: E731
        xs = np.linspace(x - w, x + w, 120)
        top = np.c_[xs, [y + 0.3 * r + groove(t) for t in xs]]
        _cells_strip(ax, top, 0.16 * r, 34, ec, z=z + 0.4)
        # lower layer: definitive endoderm in the middle, hypoblast pushed aside
        n = 26
        lower = [(x - w + (k + 0.5) * 2 * w / n) for k in range(n)]
        toks = [en if abs(t - x) < 0.8 * r else tok("hypoblast") for t in lower]
        _cells_strip(ax, [(x - w, y - 0.45 * r), (x + w, y - 0.45 * r)], 0.1 * r, n, toks, z=z + 0.4)
        # ingressing mesoderm: mesenchymal cells between the layers, spreading laterally from the streak
        rng = np.random.default_rng(14)
        for k in range(26):
            side = -1 if k % 2 else 1
            d = (k // 2 + 1) / 13
            px = x + side * (0.08 + 1.35 * d) * r + rng.uniform(-0.06, 0.06) * r
            py = y + 0.02 * r - 0.06 * r * d + rng.uniform(-0.12, 0.12) * r
            _round_cell(ax, (px, py), 0.07 * r, 0.05 * r, me, z + 0.5, angle=side * 0.3, seed=k, nucleus=False)
        for k, dy in enumerate((0.18, 0.06, -0.08)):  # cells passing through the streak
            _round_cell(ax, (x + (k - 1) * 0.04 * r, y + dy * r), 0.05 * r, 0.08 * r, me if k < 2 else en, z + 0.6, seed=k + 40,
                        nucleus=False)
        for side in (-1, 1):
            arrow(ax, (x + side * 0.25 * r, y + 0.43 * r), (x + side * 0.07 * r, y + 0.36 * r), kind="process", head=0.1 * r,
                  lw=LINE * 0.8, color=P.muted())
            arrow(ax, (x + side * 0.12 * r, y - 0.05 * r), (x + side * 0.7 * r, y - 0.12 * r), kind="process", head=0.1 * r,
                  lw=LINE * 0.8, color=P.muted(), bend=0.08 * side)
        arrow(ax, (x, y - 0.12 * r), (x, y - 0.36 * r), kind="process", head=0.1 * r, lw=LINE * 0.8, color=P.muted())
        out.update(epiblast=(x - 1.2 * r, y + 0.3 * r), groove=(x, y + 0.2 * r), mesoderm=(x + 1.0 * r, y - 0.05 * r),
                   endoderm=(x - 0.4 * r, y - 0.45 * r), hypoblast=(x + 1.4 * r, y - 0.45 * r), streak=(x, y + 0.1 * r))
        return out
    if species == "mouse":
        # proximal (top) to distal (bottom); anterior left, posterior right
        cup_o = np.vstack([[(x - 0.55 * r, y + 0.25 * r)], _arc((x, y - 0.35 * r), 0.55 * r, 180, 360, 50), [(x + 0.55 * r, y + 0.25 * r)]])
        # visceral endoderm around everything
        ve = np.vstack([[(x - 0.66 * r, y + 1.0 * r)], [(x - 0.66 * r, y + 0.25 * r)], _arc((x, y - 0.35 * r), 0.66 * r, 180, 360, 50),
                        [(x + 0.66 * r, y + 0.25 * r)], [(x + 0.66 * r, y + 1.0 * r)]])
        inner = np.vstack([[(x + 0.55 * r, y + 1.0 * r)], [(x + 0.55 * r, y + 0.25 * r)], _arc((x, y - 0.35 * r), 0.55 * r, 0, -180, 50),
                           [(x - 0.55 * r, y + 0.25 * r)], [(x - 0.55 * r, y + 1.0 * r)]])
        _patch(ax, np.vstack([ve, inner]), tok("hypoblast"), z=z + 0.2, lw=LINE * 0.7)
        # extraembryonic ectoderm (proximal half)
        _patch(ax, np.array([(x - 0.55 * r, y + 0.25 * r), (x + 0.55 * r, y + 0.25 * r), (x + 0.55 * r, y + 1.0 * r),
                             (x - 0.55 * r, y + 1.0 * r)]), tok("trophoblast"), z=z + 0.3, lw=LINE * 0.7)
        _patch(ax, np.vstack([_arc((x, y + 1.0 * r), 0.55 * r, 180, 0, 30)]), tok("trophoblast"), z=z + 0.3, lw=LINE * 0.7,
               face=P.mix(P.fill(tok("trophoblast")), P.edge(tok("trophoblast")), 0.25))
        # epiblast cup with the proamniotic cavity
        cup_i = np.vstack([[(x + 0.35 * r, y + 0.25 * r)], _arc((x, y - 0.35 * r), 0.35 * r, 0, -180, 50), [(x - 0.35 * r, y + 0.25 * r)]])
        _patch(ax, np.vstack([cup_o, cup_i]), tok("epiblast"), z=z + 0.4, lw=LINE * 0.7)
        _patch(ax, np.vstack([[(x - 0.35 * r, y + 0.55 * r)], [(x - 0.35 * r, y + 0.25 * r)], _arc((x, y - 0.35 * r), 0.35 * r, 180, 360, 50),
                              [(x + 0.35 * r, y + 0.25 * r)], [(x + 0.35 * r, y + 0.55 * r)]]), fl, z=z + 0.45, lw=LINE * 0.5)
        # primitive streak (posterior) and mesoderm wings between epiblast and VE
        _patch(ax, _sector((x, y - 0.35 * r), 0.55 * r, 0.65 * r, -70, 20, 30), me, z=z + 0.5, lw=LINE * 0.6)
        _patch(ax, np.array([(x + 0.55 * r, y + 0.2 * r), (x + 0.65 * r, y + 0.2 * r), (x + 0.65 * r, y - 0.2 * r), (x + 0.55 * r, y - 0.2 * r)]), me,
               z=z + 0.5, lw=LINE * 0.6)
        _patch(ax, _sector((x, y - 0.35 * r), 0.66 * r, 0.76 * r, 170, 230, 20), tok("hypoblast"), z=z + 0.5, lw=LINE * 0.7,
               face=P.edge(tok("hypoblast")))
        ax.add_patch(Circle(_pt((x, y - 0.35 * r), 0.6 * r, -88), 0.07 * r, facecolor=P.fill(me), edgecolor=P.edge(me), lw=LINE * 0.6,
                            zorder=z + 0.6))
        out.update(epiblast=_pt((x, y - 0.35 * r), 0.45 * r, 200), proamniotic=(x, y - 0.1 * r), ve=_pt((x, y - 0.35 * r), 0.62 * r, 250),
                   ave=_pt((x, y - 0.35 * r), 0.72 * r, 200), streak=_pt((x, y - 0.35 * r), 0.6 * r, -30), node=_pt((x, y - 0.35 * r), 0.6 * r, -88),
                   exe=(x, y + 0.65 * r), ectoplacental=(x, y + 1.3 * r), anterior=(x - 0.8 * r, y), posterior=(x + 0.8 * r, y))
        return out
    if species == "human":
        mat = tok("maternal")
        _patch(ax, np.array([(x - 1.6 * r, y - 1.2 * r), (x + 1.6 * r, y - 1.2 * r), (x + 1.6 * r, y + 1.3 * r), (x - 1.6 * r, y + 1.3 * r)]),
               mat, z=z - 0.2, lw=0, face=P.mix(P.fill(mat), P.surface(), 0.25))
        # syncytiotrophoblast with lacunae of maternal blood, cytotrophoblast, chorionic cavity
        st = blob((x, y), 1.25 * r, 1.05 * r, wobble=0.06, seed=4, k=14)
        _patch(ax, st, tok("syncytiotrophoblast"), z=z, lw=LINE * 0.8)
        rng = np.random.default_rng(7)
        for k in range(11):
            a = 360 * k / 11 + rng.uniform(-8, 8)
            p = _pt(c, 1.1 * r, a)
            ax.add_patch(Ellipse(p, 0.22 * r, 0.11 * r, angle=a + 90, facecolor=P.fill(tok("blood")), edgecolor=P.edge(tok("blood")), lw=0.6,
                                 zorder=z + 0.1))
        _patch(ax, _ellipse_pts(c, 0.98 * r, 0.85 * r), tok("trophoblast"), z=z + 0.2, lw=LINE * 0.7)
        _patch(ax, _ellipse_pts(c, 0.9 * r, 0.77 * r), tok("extraembryonic-mesoderm"), z=z + 0.25, lw=LINE * 0.6)
        _patch(ax, _ellipse_pts(c, 0.83 * r, 0.7 * r), fl, z=z + 0.3, lw=LINE * 0.5)
        # connecting stalk to the bilaminar disc, amniotic cavity above, yolk sac below
        d = (x, y + 0.15 * r)
        _patch(ax, np.array([(x - 0.1 * r, y + 0.7 * r), (x + 0.1 * r, y + 0.7 * r), (x + 0.12 * r, y + 0.42 * r), (x - 0.12 * r, y + 0.42 * r)]),
               tok("extraembryonic-mesoderm"), z=z + 0.35, lw=LINE * 0.6)
        amn = np.vstack([_ellipse_pts((x, d[1] + 0.04 * r), 0.42 * r, 0.3 * r, 60, 0, 180)])
        _patch(ax, np.vstack([amn, _ellipse_pts((x, d[1] + 0.04 * r), 0.36 * r, 0.24 * r, 60, 180, 0)]), tok("amnion"), z=z + 0.4, lw=LINE * 0.5)
        _patch(ax, _ellipse_pts((x, d[1] + 0.04 * r), 0.36 * r, 0.24 * r, 60, 0, 180), fl, z=z + 0.38, lw=0)
        _patch(ax, np.array([(x - 0.44 * r, d[1] + 0.06 * r), (x + 0.44 * r, d[1] + 0.06 * r), (x + 0.44 * r, d[1] - 0.04 * r),
                             (x - 0.44 * r, d[1] - 0.04 * r)]), tok("epiblast"), z=z + 0.45, lw=LINE * 0.6)
        _patch(ax, np.array([(x - 0.44 * r, d[1] - 0.04 * r), (x + 0.44 * r, d[1] - 0.04 * r), (x + 0.44 * r, d[1] - 0.1 * r),
                             (x - 0.44 * r, d[1] - 0.1 * r)]), tok("hypoblast"), z=z + 0.45, lw=LINE * 0.6)
        ys = np.vstack([_ellipse_pts((x, d[1] - 0.1 * r), 0.44 * r, 0.42 * r, 60, 180, 360)])
        _patch(ax, np.vstack([ys, _ellipse_pts((x, d[1] - 0.1 * r), 0.39 * r, 0.37 * r, 60, 360, 180)]), tok("hypoblast"), z=z + 0.4,
               lw=LINE * 0.5)
        _patch(ax, _ellipse_pts((x, d[1] - 0.1 * r), 0.39 * r, 0.37 * r, 60, 180, 360), fl, z=z + 0.38, lw=0)
        out.update(syncytiotrophoblast=_pt(c, 1.18 * r, 30), lacuna=_pt(c, 1.1 * r, 360 * 3 / 11), cytotrophoblast=_pt(c, 0.94 * r, -30),
                   exmeso=_pt(c, 0.86 * r, -150), chorionic_cavity=(x + 0.6 * r, y - 0.3 * r), amniotic_cavity=(x, d[1] + 0.2 * r),
                   epiblast=(x + 0.4 * r, d[1] + 0.01 * r), hypoblast=(x - 0.4 * r, d[1] - 0.07 * r), yolk_sac=(x, d[1] - 0.35 * r),
                   stalk=(x, y + 0.6 * r), endometrium=(x - 1.45 * r, y + 1.15 * r))
        return out
    raise ValueError(f"unknown species {species!r}")


def streak(ax, c, r=1.5, length=0.62, z=5):
    """A chick blastoderm seen from above at the definitive-streak stage (anterior up): area opaca,
    area pellucida, the primitive streak with its groove and Hensen's node, and arrows of the epiblast
    flowing towards the streak. ``length`` is the streak length as a fraction of the pellucida length."""
    x, y = c
    _patch(ax, _ellipse_pts(c, 1.0 * r, 1.0 * r), tok("yolk"), z=z, lw=LINE * 0.8, face=P.mix(P.fill(tok("yolk")), P.fill("animal"), 0.4))
    pel = blob((x, y + 0.02 * r), 0.55 * r, 0.75 * r, wobble=0.02, seed=2, k=10)
    pel = np.asarray(pel)
    pel[:, 0] = x + (pel[:, 0] - x) * (1 + 0.18 * (pel[:, 1] - y) / r)  # pear shape: wider anteriorly
    _patch(ax, pel, tok("epiblast"), z=z + 0.2, lw=LINE * 0.8, face=P.mix(P.fill(tok("epiblast")), P.surface(), 0.45))
    y_post, y_node = y - 0.68 * r, y - 0.68 * r + length * 1.4 * r
    ax.plot([x - 0.025 * r, x - 0.025 * r], [y_post, y_node], color=P.edge(tok("mesoderm")), lw=LINE * 2.2, zorder=z + 0.5, solid_capstyle="round")
    ax.plot([x + 0.025 * r, x + 0.025 * r], [y_post, y_node], color=P.edge(tok("mesoderm")), lw=LINE * 2.2, zorder=z + 0.5, solid_capstyle="round")
    ax.plot([x, x], [y_post + 0.02 * r, y_node - 0.02 * r], color=P.fill(tok("mesoderm")), lw=LINE * 1.2, zorder=z + 0.55, solid_capstyle="round")
    ax.add_patch(Circle((x, y_node), 0.06 * r, facecolor=P.fill(tok("mesoderm")), edgecolor=P.edge(tok("mesoderm")), lw=LINE * 0.8, zorder=z + 0.6))
    for side in (-1, 1):
        for k, yy in enumerate(np.linspace(y_post + 0.15 * r, y_node - 0.1 * r, 3)):
            a = (x + side * 0.38 * r, yy + 0.12 * r)
            b = (x + side * 0.1 * r, yy - 0.04 * r)
            arrow(ax, a, b, kind="process", bend=-0.15 * side, head=0.07 * r, lw=LINE * 0.7, color=P.muted())
    return {"node": (x, y_node), "streak": (x, (y_post + y_node) / 2), "groove": (x, y_post + 0.2 * r), "area_pellucida": (x - 0.35 * r, y + 0.4 * r),
            "area_opaca": (x - 0.8 * r, y - 0.3 * r), "anterior": (x, y + r), "posterior": (x, y - r), "r": r}


# ---------------------------------------------------------------------------------------------
# epithelial sheet movements


def sheet(ax, c, w=2.0, kind="invagination", token=None, z=5):
    """A small diagram of one of the six cell movements of gastrulation, in a box of width ``w``
    (height about 0.8 w) centred on c. Motion is shown by grey arrows.

    "invagination" (a sheet folds inwards), "involution" (a sheet rolls over a lip and spreads on the
    inner surface), "epiboly" (a sheet thins and spreads over a deeper layer or the yolk), "ingression"
    (single cells leave the epithelium and become mesenchymal), "delamination" (one sheet splits into two),
    "convergent-extension" (cells intercalate: the tissue narrows and lengthens; seen from above).
    """
    x, y = c
    t = tok(token or "ectoderm")
    m = P.muted()
    hd = 0.07 * w
    out = {}
    if kind == "invagination":
        xs = np.linspace(x - 0.5 * w, x + 0.5 * w, 80)
        ys = y + 0.18 * w - 0.32 * w * np.exp(-((xs - x) / (0.13 * w)) ** 2)
        _cells_strip(ax, np.c_[xs, ys], 0.08 * w, 15, t, z=z)
        for side in (-1, 1):
            arrow(ax, (x + side * 0.32 * w, y + 0.32 * w), (x + side * 0.12 * w, y + 0.3 * w), kind="process", head=hd, lw=LINE * 0.8, color=m)
        arrow(ax, (x, y + 0.1 * w), (x, y - 0.18 * w), kind="process", head=hd, lw=LINE * 0.8, color=m)
        out.update(pit=(x, y - 0.14 * w))
    elif kind == "involution":
        lip = (x + 0.2 * w, y)
        top = [(x - 0.5 * w, y + 0.16 * w), (x + 0.05 * w, y + 0.16 * w)]
        arc = _arc(lip, 0.16 * w, 90, -90, 30)
        bot = [(x + 0.05 * w, y - 0.16 * w), (x - 0.4 * w, y - 0.16 * w)]
        cl = np.vstack([top, arc, bot])
        _cells_strip(ax, cl, 0.08 * w, 16, t, z=z)
        arrow(ax, (x - 0.35 * w, y + 0.3 * w), (x - 0.02 * w, y + 0.3 * w), kind="process", head=hd, lw=LINE * 0.8, color=m)
        arrow(ax, (lip[0] + 0.12 * w, lip[1] + 0.28 * w), (lip[0] + 0.12 * w, lip[1] - 0.28 * w), kind="process", head=hd, bend=0.45,
              lw=LINE * 0.8, color=m)
        arrow(ax, (x + 0.02 * w, y - 0.3 * w), (x - 0.35 * w, y - 0.3 * w), kind="process", head=hd, lw=LINE * 0.8, color=m)
        out.update(lip=(x + 0.36 * w, y))
    elif kind == "epiboly":
        R = 0.3 * w
        yc = (x, y - 0.06 * w)
        _patch(ax, _ellipse_pts(yc, R, R), tok("yolk"), z=z, lw=LINE * 0.8)
        _cells_ring(ax, yc, R, lambda a: R + 0.07 * w * (0.55 + 0.45 * max(0.0, 1 - abs(a - 90) / 70)), 15, 165, 13, t, z=z + 1)
        for side in (-1, 1):
            a0, a1 = (30, -20) if side > 0 else (150, 200)
            p, q = _pt(yc, R + 0.12 * w, a0), _pt(yc, R + 0.12 * w, a1)
            arrow(ax, p, q, kind="process", head=hd, bend=-0.25 * side, lw=LINE * 0.8, color=m)
        out.update(margin=_pt(yc, R, 15), yolk=(x, yc[1] - 0.1 * w))
    elif kind == "ingression":
        _cells_strip(ax, [(x - 0.5 * w, y + 0.22 * w), (x + 0.5 * w, y + 0.22 * w)], 0.12 * w, 11,
                     [t] * 5 + [tok("mesoderm")] + [t] * 5, z=z)
        _round_cell(ax, (x + 0.05 * w, y - 0.08 * w), 0.05 * w, 0.07 * w, tok("mesoderm"), z + 1, angle=0.4, seed=1)
        _round_cell(ax, (x - 0.15 * w, y - 0.26 * w), 0.06 * w, 0.05 * w, tok("mesoderm"), z + 1, seed=2)
        _round_cell(ax, (x + 0.22 * w, y - 0.28 * w), 0.06 * w, 0.05 * w, tok("mesoderm"), z + 1, seed=3)
        arrow(ax, (x + 0.12 * w, y + 0.08 * w), (x + 0.12 * w, y - 0.14 * w), kind="process", head=hd, lw=LINE * 0.8, color=m)
        out.update(cell=(x + 0.05 * w, y - 0.08 * w))
    elif kind == "delamination":
        _cells_strip(ax, [(x - 0.5 * w, y + 0.2 * w), (x + 0.5 * w, y + 0.2 * w)], 0.1 * w, 11, t, z=z)
        _cells_strip(ax, [(x - 0.42 * w, y - 0.06 * w), (x + 0.42 * w, y - 0.06 * w)], 0.08 * w, 9, tok("endoderm"), z=z)
        for dx in (-0.25, 0.0, 0.25):
            arrow(ax, (x + dx * w, y + 0.12 * w), (x + dx * w, y + 0.0 * w), kind="process", head=hd * 0.8, lw=LINE * 0.7, color=m)
        out.update(outer=(x, y + 0.2 * w), inner=(x, y - 0.06 * w))
    elif kind == "convergent-extension":
        cols = 6
        cw, ch = 0.075 * w, 0.075 * w
        for k in range(cols):  # before: a wide, short array (left)
            for j in range(3):
                face = P.fill(t) if (k + j) % 2 else P.mix(P.fill(t), P.edge(t), 0.3)
                _patch(ax, np.array([(0, 0), (cw, 0), (cw, ch), (0, ch)]) + (x - 0.47 * w + k * cw, y - 0.12 * w + j * ch), t, z=z, lw=LINE * 0.5,
                       face=face)
        for k in range(2):  # after: narrow, long (right)
            for j in range(9):
                face = P.fill(t) if (k + j) % 2 else P.mix(P.fill(t), P.edge(t), 0.3)
                _patch(ax, np.array([(0, 0), (cw, 0), (cw, ch), (0, ch)]) + (x + 0.27 * w + k * cw, y - 0.33 * w + j * ch), t, z=z, lw=LINE * 0.5,
                       face=face)
        arrow(ax, (x - 0.02 * w, y), (x + 0.2 * w, y), kind="process", head=hd, lw=LINE, color=m)
        xl, xr, ym = x - 0.47 * w, x - 0.47 * w + cols * cw, y - 0.12 * w + 1.5 * ch
        arrow(ax, (xl - 0.1 * w, ym), (xl - 0.01 * w, ym), kind="process", head=hd * 0.8, lw=LINE * 0.7, color=m)
        arrow(ax, (xr + 0.1 * w, ym + 0.12 * w), (xr + 0.01 * w, ym + 0.12 * w), kind="process", head=hd * 0.8, lw=LINE * 0.7, color=m)
        arrow(ax, (x + 0.27 * w + cw, y + 0.36 * w), (x + 0.27 * w + cw, y + 0.44 * w), kind="process", head=hd * 0.8, lw=LINE * 0.7, color=m)
        arrow(ax, (x + 0.27 * w + cw, y - 0.36 * w), (x + 0.27 * w + cw, y - 0.44 * w), kind="process", head=hd * 0.8, lw=LINE * 0.7, color=m)
        out.update(before=(x - 0.47 * w + cols * cw / 2, y), after=(x + 0.27 * w + cw, y))
    else:
        raise ValueError(f"unknown movement {kind!r}")
    return out


# ---------------------------------------------------------------------------------------------
# extraembryonic membranes and the placenta


def amniote_egg(ax, c, r=2.5, z=5):
    """A bird egg in section (about day 5): embryo enclosed by the amnion, the chorion under the shell, the
    allantois between them, the yolk sac spreading over the yolk; albumen in the remaining space."""
    x, y = c
    shell = _ellipse_pts(c, 1.25 * r, 0.95 * r)
    _patch(ax, shell, "bone", z=z, lw=LINE * 1.4)
    _patch(ax, _ellipse_pts(c, 1.2 * r, 0.9 * r), "extracellular", z=z + 0.1, lw=0)
    # chorion just inside the shell membrane
    _patch(ax, _ellipse_pts(c, 1.16 * r, 0.86 * r), tok("chorion"), z=z + 0.2, lw=LINE * 0.8, face="none")
    # yolk with the yolk sac (vascularized endoderm + splanchnic mesoderm) over its upper part
    yc = (x - 0.05 * r, y - 0.2 * r)
    _patch(ax, _ellipse_pts(yc, 0.62 * r, 0.55 * r), tok("yolk"), z=z + 0.3, lw=LINE * 0.6)
    _patch(ax, _sector(yc, lambda a: 0.55 * r * 0.62 / math.hypot(0.62 * math.sin(math.radians(a)), 0.55 * math.cos(math.radians(a))),
                       lambda a: 0.6 * r * 0.65 / math.hypot(0.65 * math.sin(math.radians(a)), 0.6 * math.cos(math.radians(a))), 10, 170, 60),
           tok("hypoblast"), z=z + 0.35, lw=LINE * 0.6)
    for a in np.linspace(25, 155, 6):
        p = _pt(yc, 0.56 * r, a)
        q = _pt(yc, 0.3 * r, a - 8)
        ax.plot([p[0], q[0]], [p[1], q[1]], color=P.edge(tok("blood")), lw=0.8, zorder=z + 0.36)
    # embryo in the amniotic cavity, on top of the yolk sac
    ec = (x - 0.05 * r, y + 0.52 * r)
    _patch(ax, _ellipse_pts(ec, 0.42 * r, 0.24 * r), tok("amnion"), z=z + 0.5, lw=LINE * 0.8)
    _patch(ax, _ellipse_pts(ec, 0.38 * r, 0.2 * r), tok("fluid"), z=z + 0.55, lw=0)
    emb = blob((ec[0], ec[1] - 0.02 * r), 0.3 * r, 0.09 * r, wobble=0.08, seed=3, k=9)
    ax.add_patch(PathPatch(Path(emb, closed=True), facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=LINE * 0.8, zorder=z + 0.6))
    # allantois: a sac from the hindgut spreading under the chorion
    al = blob((x + 0.75 * r, y + 0.35 * r), 0.32 * r, 0.42 * r, wobble=0.06, seed=5, k=9)
    _patch(ax, al, tok("allantois"), z=z + 0.45, lw=LINE * 0.8)
    ax.plot([ec[0] + 0.25 * r, x + 0.5 * r], [ec[1] - 0.06 * r, y + 0.3 * r], color=P.edge(tok("allantois")), lw=LINE * 1.2, zorder=z + 0.62)
    on_oval = lambda f, a: (x + f * 1.25 * r * math.cos(math.radians(a)), y + f * 0.95 * r * math.sin(math.radians(a)))  # noqa: E731
    return {"shell": on_oval(1.0, 125), "chorion": on_oval(0.93, 60), "amnion": (ec[0] - 0.42 * r, ec[1]), "amniotic_cavity": (ec[0] - 0.2 * r, ec[1] + 0.12 * r),
            "embryo": ec, "allantois": (x + 0.8 * r, y + 0.45 * r), "yolk_sac": _pt(yc, 0.6 * r, 150), "yolk": (yc[0], yc[1] - 0.2 * r),
            "albumen": (x - 0.95 * r, y - 0.35 * r), "r": r}


def villus(ax, box, z=5):
    """A chorionic villus tree hanging from the chorionic plate into the intervillous space of a human
    placenta (haemochorial): maternal blood enters from a spiral artery and leaves by an endometrial
    vein; fetal blood arrives in umbilical arteries (deoxygenated) and returns by the umbilical vein.
    ``box`` = (x0, y0, w, h); the chorionic plate is at the top, the decidua at the bottom."""
    x0, y0, w, h = box
    bl, dn = tok("blood"), "dna"
    # intervillous space (maternal blood wash)
    _patch(ax, np.array([(x0, y0 + 0.18 * h), (x0 + w, y0 + 0.18 * h), (x0 + w, y0 + 0.82 * h), (x0, y0 + 0.82 * h)]), bl, z=z, lw=0,
           face=P.mix(P.fill(bl), P.surface(), 0.72 if not P.is_dark() else 0.82))
    _patch(ax, np.array([(x0, y0), (x0 + w, y0), (x0 + w, y0 + 0.18 * h), (x0, y0 + 0.18 * h)]), tok("maternal"), z=z + 0.1, lw=LINE * 0.6)
    _patch(ax, np.array([(x0, y0 + 0.82 * h), (x0 + w, y0 + 0.82 * h), (x0 + w, y0 + h), (x0, y0 + h)]), tok("chorion"), z=z + 0.1, lw=LINE * 0.6)
    # villus: stem from the plate branching downwards (syncytiotrophoblast cover)
    cx = x0 + 0.5 * w
    branches = [[(cx, y0 + 0.82 * h), (cx, y0 + 0.5 * h)], [(cx, y0 + 0.62 * h), (cx - 0.18 * w, y0 + 0.4 * h)],
                [(cx, y0 + 0.62 * h), (cx + 0.18 * w, y0 + 0.4 * h)], [(cx, y0 + 0.5 * h), (cx - 0.05 * w, y0 + 0.3 * h)],
                [(cx, y0 + 0.5 * h), (cx + 0.07 * w, y0 + 0.32 * h)]]
    tips = []
    for b in branches:
        (ax_, ay), (bx, by) = b
        ax.plot([ax_, bx], [ay, by], color=P.edge(tok("syncytiotrophoblast")), lw=LINE * 9, solid_capstyle="round", zorder=z + 0.3)
        ax.plot([ax_, bx], [ay, by], color=P.fill(tok("syncytiotrophoblast")), lw=LINE * 7.5, solid_capstyle="round", zorder=z + 0.31)
        tips.append((bx, by))
    for b in branches:  # fetal vessels inside: artery (blue, deoxygenated) and vein (red)
        (ax_, ay), (bx, by) = b
        v = np.array([bx - ax_, by - ay])
        n_ = np.array([-v[1], v[0]]) / np.hypot(*v) * 0.012 * w
        ax.plot([ax_ + n_[0], bx + n_[0]], [ay + n_[1], by + n_[1]], color=P.edge(dn), lw=LINE * 1.2, solid_capstyle="round", zorder=z + 0.4)
        ax.plot([ax_ - n_[0], bx - n_[0]], [ay - n_[1], by - n_[1]], color=P.edge(bl), lw=LINE * 1.2, solid_capstyle="round", zorder=z + 0.4)
    # maternal spiral artery and vein in the decidua
    xa, xv = x0 + 0.2 * w, x0 + 0.82 * w
    sp = np.c_[xa + 0.025 * w * np.sin(np.linspace(0, 6 * np.pi, 60)), np.linspace(y0, y0 + 0.2 * h, 60)]
    ax.plot(sp[:, 0], sp[:, 1], color=P.edge(bl), lw=LINE * 2.2, zorder=z + 0.2, solid_capstyle="round")
    ax.plot([xv, xv], [y0, y0 + 0.2 * h], color=P.edge(dn), lw=LINE * 2.2, zorder=z + 0.2, solid_capstyle="round")
    # umbilical vessels on the plate
    ax.plot([x0 + 0.05 * w, cx - 0.02 * w], [y0 + 0.9 * h, y0 + 0.9 * h], color=P.edge(dn), lw=LINE * 2, zorder=z + 0.2)
    ax.plot([cx + 0.02 * w, x0 + 0.95 * w], [y0 + 0.9 * h, y0 + 0.9 * h], color=P.edge(bl), lw=LINE * 2, zorder=z + 0.2)
    return {"spiral_artery": (xa, y0 + 0.1 * h), "vein": (xv, y0 + 0.1 * h), "intervillous": (x0 + 0.2 * w, y0 + 0.6 * h),
            "villus": (cx + 0.18 * w, y0 + 0.4 * h), "tip": tips[1], "chorionic_plate": (x0 + 0.5 * w, y0 + 0.91 * h),
            "umbilical_artery": (x0 + 0.15 * w, y0 + 0.9 * h), "umbilical_vein": (x0 + 0.85 * w, y0 + 0.9 * h),
            "decidua": (x0 + 0.5 * w, y0 + 0.09 * h), "jet": (xa, y0 + 0.26 * h)}


def legend(ax, xy, items=("ectoderm", "mesoderm", "endoderm"), step=2.6, size="small", swatch=0.3, rows=1):
    """A key of tissue colours (``TISSUE`` names) starting at ``xy``; with ``rows`` > 1, items wrap."""
    from .core import label
    x, y = xy
    per = math.ceil(len(items) / rows)
    for k, it in enumerate(items):
        xx, yy = x + (k % per) * step, y - (k // per) * 0.5
        t = tok(it)
        ax.add_patch(Circle((xx + swatch / 2, yy), swatch / 2, facecolor=P.fill(t), edgecolor=P.edge(t), lw=0.9, zorder=20))
        label(ax, (xx + swatch + 0.12, yy), NAMES.get(it, it), size=size, ha="left")


__all__ = ["TISSUE", "NAMES", "tok", "egg", "cleavage", "blastula", "gastrula", "streak", "sheet", "amniote_egg", "villus", "legend"]
