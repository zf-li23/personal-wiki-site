"""Neural development: neurulation in cross-section, dorso-ventral progenitor domains of the neural tube,
the layers of the developing cortex, the growth cone, and the optic cup with the lens.

    from wikibio import neurodev as N
    a = N.neurulation_section(ax, (6, 4), 10, "fold")      plate / fold / converge / tube (+ crest, notochord,
                                                            paraxial mesoderm, endoderm); returns anchors
    d = N.neural_tube_domains(ax, (4, 4), 6)               transverse section of the spinal cord with its
                                                            progenitor domains (dP1-dP6, p0-p3, pMN)
    c = N.cortex_layers(ax, (1, 1), 4, 6, "late")          VZ, SVZ, IZ, cortical plate, marginal zone, radial
                                                            glia and migrating neurons (inside-out)
    g = N.growth_cone(ax, (8, 3), angle=0, size=1.6)       axon shaft, central and peripheral domains, filopodia
    e = N.optic_cup(ax, (6, 3), 2.0, "cup")                vesicle / cup / lens-vesicle / eye

Tissues keep one colour in every figure (``TISSUE``). The germ layers follow ``zoology.GERM`` (surface
ectoderm blue, mesoderm red, endoderm yellow); the neural plate and tube, the neural crest and the notochord
use their own tokens so that the three ectodermal derivatives can be told apart. Every function is
deterministic and returns a dict of anchor points (canvas coordinates) for labels and arrows.
"""

import math

import numpy as np
from matplotlib.patches import Circle, PathPatch, Polygon, Rectangle
from matplotlib.path import Path

from . import palette as P
from .core import LINE, blob, polyline, smooth_closed

# tissue -> palette token; dedicated tokens ("neural", "neural_crest", "notochord") would replace these aliases
TISSUE = {
    "epidermis": "ectoderm",       # surface (non-neural) ectoderm
    "neural": "protein",           # neural plate, neural tube, neuroepithelium
    "crest": "cl",                 # neural crest
    "placode": "receptor",         # placodal ectoderm, lens
    "notochord": "drug",
    "somite": "mesoderm",          # paraxial mesoderm, somites
    "lateral": "mesoderm",         # intermediate and lateral plate mesoderm (drawn lighter)
    "endoderm": "endoderm",
    "rpe": "animal",               # retinal pigment epithelium
}

# default dorso-ventral progenitor domains of the spinal cord, dorsal to ventral: (name, token, relative height)
DV_DOMAINS = [
    ("dP1", "k", 1.0), ("dP2", "metabolite", 1.0), ("dP3", "carbohydrate", 1.0), ("dP4", "antibody", 1.0),
    ("dP5", "lipid", 1.0), ("dP6", "atp", 1.0), ("p0", "enzyme", 1.0), ("p1", "channel", 1.0),
    ("p2", "dna", 1.0), ("pMN", "receptor", 1.3), ("p3", "drug", 1.0),
]


def _patch(ax, verts, token, zorder, lw=LINE * 0.9, face=None, edge=None):
    v = np.asarray(verts, float)
    p = PathPatch(Path(np.vstack([v, v[:1]]), closed=True), facecolor=face or P.fill(token), edgecolor=edge or P.edge(token),
                  lw=lw, zorder=zorder, joinstyle="round")
    ax.add_patch(p)
    return p


def _band(curve, t_out, t_in, n=300):
    """Closed polygon of a band around a curve: offset by t_out on the left normal and t_in on the right."""
    q, nrm, _ = polyline(curve, n=n, closed=False)
    t_out = np.broadcast_to(np.asarray(t_out, float), (len(q),))
    t_in = np.broadcast_to(np.asarray(t_in, float), (len(q),))
    a = q + nrm * t_out[:, None]
    b = q - nrm * t_in[:, None]
    return np.vstack([a, b[::-1]]), q, nrm


def _arc(c, r, a0, a1, n=80):
    t = np.radians(np.linspace(a0, a1, n))
    return np.c_[c[0] + r * np.cos(t), c[1] + r * np.sin(t)]


def _sector(c, r_out, r_in, a0, a1, n=120):
    return np.vstack([_arc(c, r_out, a0, a1, n), _arc(c, r_in, a1, a0, n)])


def _cell_walls(ax, c, r_out, r_in, a0, a1, step, token, zorder):
    for a in np.arange(a0 + step / 2, a1, step):
        t = math.radians(a)
        ax.plot([c[0] + r_in * math.cos(t), c[0] + r_out * math.cos(t)], [c[1] + r_in * math.sin(t), c[1] + r_out * math.sin(t)],
                color=P.edge(token), lw=0.45, zorder=zorder)


def neurulation_section(ax, center, width=12.0, stage="plate", crest=True, notochord=True, mesoderm=True, endoderm=True,
                        migrating=True, zorder=5):
    """A transverse section through a vertebrate (amniote) embryo during neurulation, dorsal up.

    ``center`` is the dorsal midline at the level of the flat ectoderm and ``width`` the width of the section
    (height about 0.55 x width). Stages:

    - "plate": the thickened neural plate in the midline of the ectoderm, neural plate border (crest) at its edges;
    - "fold": the plate bends at the median hinge point above the notochord, the neural folds rise;
    - "converge": the folds bend at the dorsolateral hinge points and approach each other;
    - "tube": the closed neural tube under a continuous epidermis, neural crest cells delaminating dorsally
      (and, with ``migrating``, streaming ventro-laterally), somites beside the tube.

    Returns anchors: "neural", "lumen" (tube), "mhp", "dlhp_l", "dlhp_r", "crest_l", "crest_r", "epidermis_l",
    "epidermis_r", "notochord", "somite_l", "somite_r", "lateral_l", "lateral_r", "endoderm", "groove".
    """
    s = width / 12.0
    cx, cy = center

    def T(pts):
        p = np.asarray(pts, float)
        return np.c_[cx + s * p[:, 0], cy + s * p[:, 1]]

    def pt(x, y):
        return (cx + s * x, cy + s * y)

    ne, ep, nc = TISSUE["neural"], TISSUE["epidermis"], TISSUE["crest"]
    te, tn = 0.22, 0.55                     # thickness of epidermis and neuroepithelium (local units)
    a = {}
    z = zorder + 2

    if stage == "plate":
        half = 2.2
        _patch(ax, T([(-half, 0.1), (half, 0.1), (half, -tn + 0.1), (-half, -tn + 0.1)]), ne, z)
        for x in np.arange(-half + 0.2, half, 0.3):
            ax.plot(*T([(x, 0.1), (x, -tn + 0.1)]).T, color=P.edge(ne), lw=0.45, zorder=z + 0.1)
        for sgn in (-1, 1):
            x0, x1 = sgn * half, sgn * 6.0
            _patch(ax, T([(x0 + sgn * 0.45, 0.1), (x1, 0.1), (x1, 0.1 - te), (x0 + sgn * 0.45, 0.1 - te)]), ep, z)
            if crest:
                _patch(ax, T([(x0, 0.1), (x0 + sgn * 0.45, 0.1), (x0 + sgn * 0.45, 0.1 - te - 0.12), (x0, -tn + 0.1)]), nc, z + 0.2)
            key = "r" if sgn > 0 else "l"
            a["crest_" + key] = pt(sgn * (half + 0.22), -0.05)
            a["epidermis_" + key] = pt(sgn * 4.5, 0.0)
            a["dlhp_" + key] = pt(sgn * 1.6, -0.2)
        a["neural"], a["mhp"], a["groove"] = pt(0.9, -0.2), pt(0, -0.2), pt(0, 0.1)
        y_meso = -1.25
    elif stage in ("fold", "converge"):
        phi = 62.0 if stage == "fold" else 128.0      # half-angle of the bent plate (degrees)
        R = 2.6 if stage == "fold" else 1.5
        yb = -0.55                                     # bottom of the outer (basal) surface at the midline
        c = (0.0, yb + R)
        r_in = R - tn
        a0, a1 = -90 - phi, -90 + phi
        _patch(ax, T(_sector(c, R, r_in, a0, a1)), ne, z)
        cs = np.c_[c[0], c[1]]
        sc = np.array([cx + s * c[0], cy + s * c[1]])
        _cell_walls(ax, sc, s * R, s * r_in, a0, a1, 9.0 if stage == "fold" else 11.0, ne, z + 0.1)
        # wedge-shaped cells of the median hinge point: a darker strip at the bottom
        _patch(ax, T(_sector(c, R, r_in, -96, -84, 20)), ne, z + 0.2, face=P.edge(ne))
        for sgn in (-1, 1):
            key = "r" if sgn > 0 else "l"
            ang = -90 + sgn * phi                      # angle of the fold tip
            tip = (c[0] + R * math.cos(math.radians(ang)), c[1] + R * math.sin(math.radians(ang)))
            tip_in = (c[0] + r_in * math.cos(math.radians(ang)), c[1] + r_in * math.sin(math.radians(ang)))
            # epidermis: from the fold apex down the outer face of the fold, then out to the flat ectoderm
            ro = R + 0.42
            arc = _arc(c, ro, ang + sgn * 4, ang - sgn * (40 if stage == "fold" else 95), 30)
            if sgn < 0:
                arc = _arc(c, ro, ang - 4, ang + (40 if stage == "fold" else 95), 30)
            last = arc[-1]
            lat = np.array([[last[0] + sgn * 0.9, last[1] - 0.25], [sgn * 4.5, min(last[1] - 0.45, -0.1)], [sgn * 6.0, min(last[1] - 0.5, -0.1)]])
            apex = (c[0] + (R + 0.2) * math.cos(math.radians(ang + sgn * 6)), c[1] + (R + 0.2) * math.sin(math.radians(ang + sgn * 6)))
            curve = np.vstack([[apex], arc, lat])
            poly, q, nrm = _band(T(curve), s * te / 2, s * te / 2)
            _patch(ax, poly, ep, z - 0.1)
            if crest:
                cc = ((tip[0] + tip_in[0]) / 2 + 0.05 * sgn, (tip[1] + tip_in[1]) / 2)
                o = blob(T([cc])[0], s * 0.42, s * 0.34, wobble=0.06, seed=3 + sgn, k=8, angle=math.radians(ang))
                _patch(ax, o, nc, z + 0.3)
                a["crest_" + key] = T([cc])[0]
            hinge = -90 + sgn * (phi - 28)
            a["dlhp_" + key] = T([(c[0] + (R - tn / 2) * math.cos(math.radians(hinge)), c[1] + (R - tn / 2) * math.sin(math.radians(hinge)))])[0]
            a["epidermis_" + key] = T([lat[1]])[0]
        a["mhp"] = pt(0, yb + tn / 2)
        a["neural"] = T([(c[0] + (R - tn / 2) * math.cos(math.radians(-90 + phi * 0.55)), c[1] + (R - tn / 2) * math.sin(math.radians(-90 + phi * 0.55)))])[0]
        a["groove"] = pt(0, yb + tn + 0.5)
        y_meso = yb - 0.85
    elif stage == "tube":
        R, r_l = 1.25, 0.32
        c = (0.0, -1.55)
        # neural tube: thick wall around a slit-like lumen
        outline = smooth_closed(np.c_[c[0] + R * 0.82 * np.cos(np.linspace(0, 2 * np.pi, 12, endpoint=False)),
                                      c[1] + R * np.sin(np.linspace(0, 2 * np.pi, 12, endpoint=False))])
        _patch(ax, T(outline), ne, z)
        th = np.linspace(0, 2 * np.pi, 60)
        _patch(ax, T(np.c_[c[0] + r_l * 0.35 * np.cos(th), c[1] + R * 0.62 * np.sin(th)]), "extracellular", z + 0.1,
               face=P.fill("extracellular"), edge=P.edge(ne))
        for k in range(14):
            t = 2 * math.pi * (k + 0.5) / 14
            p0 = (c[0] + r_l * 0.35 * math.cos(t), c[1] + R * 0.62 * math.sin(t))
            p1 = (c[0] + R * 0.82 * math.cos(t) * 0.97, c[1] + R * math.sin(t) * 0.97)
            ax.plot(*T([p0, p1]).T, color=P.edge(ne), lw=0.45, zorder=z + 0.05)
        # epidermis: continuous over the tube
        curve = np.array([(-6.0, 0.0), (-2.5, 0.0), (0.0, 0.05), (2.5, 0.0), (6.0, 0.0)])
        poly, _, _ = _band(T(curve), s * te / 2, s * te / 2)
        _patch(ax, poly, ep, z)
        if crest:
            pts = [(-0.35, -0.42), (0.0, -0.32), (0.35, -0.42), (-0.15, -0.62), (0.18, -0.6)]
            if migrating:
                pts += [(-0.95, -0.55), (0.95, -0.55), (-1.5, -0.95), (1.5, -0.95), (-1.55, -1.6), (1.55, -1.6), (-1.75, -2.2), (1.75, -2.2)]
            for k, (x, y) in enumerate(pts):
                o = blob(pt(x, y), s * 0.19, s * 0.13, wobble=0.12, seed=20 + k, k=7, angle=0.4 * k)
                _patch(ax, o, nc, z + 0.3, lw=LINE * 0.7)
            a["crest_l"], a["crest_r"] = pt(-0.95, -0.55), pt(0.95, -0.55)
        a["neural"], a["lumen"] = pt(0.75, -1.9), pt(0, -1.55)
        a["mhp"], a["groove"] = pt(0, -1.55 - R), pt(0, -0.32)
        a["dlhp_l"], a["dlhp_r"] = pt(-0.9, -0.9), pt(0.9, -0.9)
        a["epidermis_l"], a["epidermis_r"] = pt(-4.5, 0.0), pt(4.5, 0.0)
        y_meso = -1.55 - R - 0.1
    else:
        raise ValueError(f"unknown stage {stage!r}")

    # mesoderm and endoderm below the ectoderm
    zm = zorder
    if notochord:
        rn = 0.42
        yn = y_meso - rn if stage != "tube" else y_meso - rn
        ax.add_patch(Circle(pt(0, yn), s * rn, facecolor=P.fill(TISSUE["notochord"]), edgecolor=P.edge(TISSUE["notochord"]),
                            lw=LINE * 0.9, zorder=zm + 1))
        a["notochord"] = pt(0, yn)
    if mesoderm:
        for sgn in (-1, 1):
            key = "r" if sgn > 0 else "l"
            if stage == "tube":
                sc_ = (sgn * 2.55, -1.75)
                o = blob(pt(*sc_), s * 0.95, s * 0.85, wobble=0.05, seed=40 + sgn, k=9)
                _patch(ax, o, TISSUE["somite"], zm + 1)
                o2 = blob(pt(*sc_), s * 0.38, s * 0.3, wobble=0.05, seed=50 + sgn, k=8)
                _patch(ax, o2, TISSUE["somite"], zm + 1.1, face=P.light(TISSUE["somite"]))
                a["somite_" + key] = pt(sc_[0] + sgn * 0.45, sc_[1] + 0.45)
                ylp = -2.2
            else:
                sc_ = (sgn * 1.9, y_meso - 0.45)
                o = blob(pt(*sc_), s * 0.95, s * 0.45, wobble=0.05, seed=40 + sgn, k=9)
                _patch(ax, o, TISSUE["somite"], zm + 1)
                a["somite_" + key] = pt(*sc_)
                ylp = y_meso - 0.45
            # lateral plate mesoderm: two thin sheets splitting around the coelom
            x0, x1 = sgn * (3.45 if stage == "tube" else 3.0), sgn * 6.0
            for dy, k in ((0.18, 0), (-0.2, 1)):
                pts = [(x0, ylp + dy * 0.4), (x1, ylp + dy), (x1, ylp + dy - 0.2), (x0, ylp + dy * 0.4 - 0.2)]
                _patch(ax, T(pts), TISSUE["lateral"], zm + 0.8, face=P.light(TISSUE["lateral"]), edge=P.edge(TISSUE["lateral"]))
            a["lateral_" + key] = pt(sgn * 5.0, ylp)
    if endoderm:
        ye = (a["notochord"][1] - cy) / s - 0.75 if notochord else y_meso - 1.3
        if stage == "tube":
            ye = -3.75
        poly, _, _ = _band(T(np.array([(-6.0, ye), (0.0, ye - 0.05), (6.0, ye)])), s * 0.11, s * 0.11)
        _patch(ax, poly, TISSUE["endoderm"], zm + 0.5)
        a["endoderm"] = pt(3.5, ye)
    return a


def neural_tube_domains(ax, center, height=6.0, domains=None, roof=True, floor=True, notochord=True, mantle=True,
                        zorder=5):
    """Transverse section of the spinal cord (dorsal up) with its progenitor domains in the ventricular zone.

    ``domains``: list of (name, token, relative height), dorsal to ventral (default ``DV_DOMAINS``); the domains are
    stacked between the roof plate and the floor plate along the slit-shaped lumen. Returns a dict with the canvas
    point of each domain on the right side of the lumen (key = domain name, for labels), and "roof", "floor",
    "notochord", "lumen", "mantle", "top", "bottom", "right" (x of the outer surface).
    """
    domains = domains or DV_DOMAINS
    cx, cy = center
    H = height
    W = 0.62 * H
    t = np.linspace(0, 2 * np.pi, 16, endpoint=False)
    rx = W / 2 * (1 + 0.06 * np.sin(t))
    outer = smooth_closed(np.c_[cx + rx * np.cos(t), cy + H / 2 * np.sin(t)])
    ne = TISSUE["neural"]
    _patch(ax, outer, ne, zorder, face=P.light(ne) if mantle else None)
    # ventricular zone: the inner band around the lumen
    vz_w = 0.17 * W
    lum_w = 0.035 * W
    yt, yb = cy + 0.40 * H, cy - 0.40 * H       # lumen spans between roof and floor plates
    ys = np.linspace(yb, yt, 60)
    prof = np.sqrt(np.clip(1 - ((ys - cy) / (0.40 * H)) ** 2, 0, 1)) ** 0.35
    lumen = np.vstack([np.c_[cx + lum_w * prof, ys], np.c_[cx - lum_w * prof, ys][::-1]])
    vz = np.vstack([np.c_[cx + (lum_w + vz_w) * prof + 0.0, ys], np.c_[cx - (lum_w + vz_w) * prof, ys][::-1]])
    clip = PathPatch(Path(np.vstack([vz, vz[:1]]), closed=True), transform=ax.transData, facecolor="none", edgecolor="none")
    ax.add_patch(clip)
    tot = sum(d[2] for d in domains)
    a = {}
    y = yt
    for name, tok, rel in domains:
        h = (yt - yb) * rel / tot
        r = Rectangle((cx - W, y - h), 2 * W, h, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.5, zorder=zorder + 1)
        ax.add_patch(r)
        r.set_clip_path(clip)
        a[name] = (cx + lum_w + vz_w * 0.9, y - h / 2)
        y -= h
    _patch(ax, vz, ne, zorder + 1.2, face="none", edge=P.edge(ne), lw=LINE * 0.6).set_fill(False)
    _patch(ax, lumen, "extracellular", zorder + 1.5, face=P.fill("extracellular"), edge=P.edge(ne), lw=LINE * 0.6)
    if roof:
        o = blob((cx, cy + 0.455 * H), 0.13 * W, 0.05 * H, wobble=0.04, seed=1, k=8)
        _patch(ax, o, "atp", zorder + 2)
        a["roof"] = (cx, cy + 0.455 * H)
    if floor:
        o = blob((cx, cy - 0.455 * H), 0.13 * W, 0.05 * H, wobble=0.04, seed=2, k=8)
        _patch(ax, o, "drug", zorder + 2, face=P.light("drug"))
        a["floor"] = (cx, cy - 0.455 * H)
    if notochord:
        ax.add_patch(Circle((cx, cy - 0.5 * H - 0.12 * H), 0.1 * H, facecolor=P.fill(TISSUE["notochord"]),
                            edgecolor=P.edge(TISSUE["notochord"]), lw=LINE * 0.9, zorder=zorder + 1))
        a["notochord"] = (cx, cy - 0.62 * H)
    a["lumen"], a["mantle"] = (cx, cy), (cx - 0.33 * W, cy - 0.05 * H)
    a["top"], a["bottom"], a["right"] = (cx, cy + H / 2), (cx, cy - H / 2), cx + W / 2
    return a


def cortex_layers(ax, origin, width=4.0, height=6.0, stage="late", glia=4, seed=0, zorder=5):
    """A strip of developing neocortex, apical (ventricle) at the bottom and pial surface at the top.

    stage "early": neuroepithelium and preplate only; "mid": VZ, SVZ, IZ and a thin cortical plate; "late": the
    cortical plate with three birth cohorts of neurons coloured deep (early-born) to superficial (late-born),
    showing the inside-out order. Radial glia have their soma in the VZ and a basal fibre to the pia; outer radial
    glia (oRG) sit in the SVZ with a basal fibre only; migrating neurons ride on the fibres.
    Returns {"VZ": y, "SVZ": y, "IZ": y, "CP": y, "MZ": y, "ventricle": y, "pia": y, "cohorts": [tokens]}.
    """
    x0, y0 = origin
    w, h = width, height
    rng = np.random.default_rng(seed)
    if stage == "early":
        layers = [("VZ", 0.75, "cytoplasm"), ("PP", 0.25, "neutral")]
    elif stage == "mid":
        layers = [("VZ", 0.25, "cytoplasm"), ("SVZ", 0.17, "cytoplasm"), ("IZ", 0.28, "extracellular"), ("CP", 0.2, "neutral"),
                  ("MZ", 0.1, "extracellular")]
    else:
        layers = [("VZ", 0.14, "cytoplasm"), ("SVZ", 0.18, "cytoplasm"), ("IZ", 0.2, "extracellular"), ("CP", 0.4, "neutral"),
                  ("MZ", 0.08, "extracellular")]
    a = {}
    y = y0
    for name, frac, tok in layers:
        hh = frac * h
        face = P.mix(P.fill(tok), P.surface(), 0.55) if tok == "neutral" else P.fill(tok)
        ax.add_patch(Rectangle((x0, y), w, hh, facecolor=face, edgecolor=P.edge("neutral"), lw=0.5, zorder=zorder))
        a[name] = y + hh / 2
        a[name + "_range"] = (y, y + hh)
        y += hh
    a["ventricle"], a["pia"] = y0, y0 + h
    ne = TISSUE["neural"]
    xs = x0 + (np.arange(glia) + 0.5) * w / glia
    vz0, vz1 = a["VZ_range"]
    for k, x in enumerate(xs):
        ys = vz0 + (0.25 + 0.5 * ((k * 0.37) % 1)) * (vz1 - vz0)
        ax.plot([x, x + 0.03 * w * math.sin(k)], [ys, y0 + h], color=P.edge(ne), lw=0.8, zorder=zorder + 1)
        ax.plot([x, x], [y0, ys], color=P.edge(ne), lw=0.8, zorder=zorder + 1)
        ax.add_patch(Circle((x, ys), 0.035 * w + 0.02, facecolor=P.fill(ne), edgecolor=P.edge(ne), lw=0.7, zorder=zorder + 2))
        ax.plot([x - 0.04 * w, x + 0.04 * w + 0.03 * w * math.sin(k)], [y0 + h - 0.01, y0 + h - 0.01], color=P.edge(ne), lw=2.0,
                zorder=zorder + 2, solid_capstyle="round")
    cohorts = ["enzyme", "antibody", "receptor"]
    a["cohorts"] = cohorts
    if stage in ("mid", "late"):
        s0, s1 = a["SVZ_range"]
        for k, x in enumerate(xs[:-1]):
            xo = x + 0.5 * w / glia
            yo = s0 + 0.55 * (s1 - s0)
            ax.plot([xo, xo], [yo, y0 + h], color=P.edge(ne), lw=0.7, ls=(0, (3, 1.5)), zorder=zorder + 1)
            ax.add_patch(Circle((xo, yo), 0.03 * w + 0.02, facecolor=P.light(ne), edgecolor=P.edge(ne), lw=0.7, zorder=zorder + 2))
        c0, c1 = a["CP_range"]
        n_coh = 1 if stage == "mid" else 3
        for j in range(n_coh):
            band = (c0 + (c1 - c0) * j / n_coh, c0 + (c1 - c0) * (j + 1) / n_coh)
            tok = cohorts[j]
            for i in range(int(4 * w)):
                x = x0 + (i + 0.5) * w / int(4 * w) + rng.uniform(-0.05, 0.05)
                yy = band[0] + (band[1] - band[0]) * rng.uniform(0.25, 0.75)
                r = 0.06 * w ** 0.5 * 0.5 + 0.03
                tri = [(x, yy + 1.4 * r), (x - r, yy - 0.7 * r), (x + r, yy - 0.7 * r)]
                ax.add_patch(Polygon(tri, closed=True, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.5, zorder=zorder + 3))
        # neurons migrating along radial glial fibres through the IZ (the youngest cohort)
        i0, i1 = a["IZ_range"]
        tok = cohorts[n_coh - 1]
        for k, x in enumerate(xs):
            yy = i0 + (0.3 + 0.4 * ((k * 0.61) % 1)) * (i1 - i0)
            ax.add_patch(Polygon([(x + 0.07, yy + 0.16), (x - 0.02, yy - 0.08), (x + 0.12, yy - 0.08)], closed=True,
                                 facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.5, zorder=zorder + 3))
    return a


def growth_cone(ax, tip, angle=0.0, size=1.5, shaft=3.0, filopodia=7, token="neuron", seed=0, zorder=8):
    """The tip of a growing axon: shaft with microtubules, the central domain, the actin-rich peripheral domain
    (lamellipodial veils) and filopodia fanning out ahead. ``tip`` is the leading edge, ``angle`` the direction of
    growth in degrees. Returns {"shaft", "central", "peripheral", "filopodia": [tips], "back"}.
    """
    rng = np.random.default_rng(seed)
    th = math.radians(angle)
    u = np.array([math.cos(th), math.sin(th)])
    v = np.array([-u[1], u[0]])
    tip = np.asarray(tip, float)
    L = size
    base = tip - u * L                       # where the cone meets the shaft
    back = base - u * shaft

    def W(a_, b_):
        return base + u * a_ * L + v * b_ * L

    # palm of the cone (peripheral domain): a fan whose front edge is W(0.6 + 0.4 cos t, 0.62 sin t)
    front = [W(0.6 + 0.4 * math.cos(t), 0.62 * math.sin(t)) for t in np.linspace(1.35, -1.35, 9)]
    fan = smooth_closed(np.vstack([[W(0.02, 0.16)], [W(0.22, 0.46)], front, [W(0.22, -0.46)], [W(0.02, -0.16)]]), n=160)
    actin = "actin"
    a = {}
    # filopodia: from the front edge, roughly radially
    tips = []
    for k, t in enumerate(np.linspace(-1.15, 1.15, filopodia)):
        t = t + rng.uniform(-0.06, 0.06)
        p0 = W(0.6 + 0.37 * math.cos(t), 0.58 * math.sin(t))
        ln = 0.5 + 0.25 * rng.uniform()
        d = u * math.cos(t * 0.8) + v * math.sin(t * 0.8)
        p1 = p0 + d * ln * L
        ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=P.edge(actin), lw=1.6, solid_capstyle="round", zorder=zorder)
        tips.append(tuple(p1))
    _patch(ax, fan, actin, zorder + 0.5, face=P.light(actin))
    # shaft
    shaft_poly = np.vstack([back + v * 0.11 * L, base + v * 0.13 * L, base - v * 0.13 * L, back - v * 0.11 * L])
    _patch(ax, shaft_poly, token, zorder + 0.6)
    # central domain
    cdom = blob(tuple(W(0.22, 0)), 0.3 * L, 0.24 * L, wobble=0.05, seed=seed + 5, k=8, angle=th)
    _patch(ax, cdom, token, zorder + 0.7)
    # microtubules: run along the shaft and splay in the central domain, a few exploring the periphery
    for k, off in enumerate((-0.06, 0.0, 0.06)):
        p0, p1 = back + v * off * L, base + v * off * L
        ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=P.edge("dna"), lw=0.8, zorder=zorder + 0.8)
    for t in (-0.5, -0.15, 0.2, 0.55):
        q0 = base + v * 0.04 * t * L
        q1 = W(0.38 + 0.12 * abs(t), 0.32 * t)
        ax.plot([q0[0], q1[0]], [q0[1], q1[1]], color=P.edge("dna"), lw=0.8, zorder=zorder + 0.8)
    q = W(0.62, 0.15)
    ax.plot([W(0.4, 0.1)[0], q[0]], [W(0.4, 0.1)[1], q[1]], color=P.edge("dna"), lw=0.8, ls=(0, (2, 1)), zorder=zorder + 0.8)
    a["shaft"], a["central"], a["peripheral"] = tuple(base - u * shaft * 0.5), tuple(W(0.22, 0)), tuple(W(0.62, -0.35))
    a["filopodia"], a["back"], a["base"] = tips, tuple(back), tuple(base)
    return a


def optic_cup(ax, center, r=2.0, stage="cup", labels=False, zorder=5):
    """The developing vertebrate eye in section, brain to the left and surface ectoderm to the right.

    stage "vesicle": the optic vesicle bulges from the diencephalon and contacts the surface ectoderm, which
    thickens into the lens placode; "cup": the vesicle folds into the two-layered optic cup (inner neural retina,
    outer retinal pigment epithelium) while the lens placode invaginates as the lens pit; "lens-vesicle": the lens
    vesicle has pinched off and the surface ectoderm has closed over it (future corneal epithelium); "eye": lens
    fibres fill the lens, the retina is thick and layered, the optic stalk carries the optic nerve.
    ``center`` is the centre of the cup. Returns anchors "retina", "rpe", "lens", "stalk", "ectoderm", "brain",
    "placode", "cornea", "lumen".
    """
    cx, cy = center
    ne, ep, pl, rp = TISSUE["neural"], TISSUE["epidermis"], TISSUE["placode"], TISSUE["rpe"]
    a = {}
    xe = cx + 1.05 * r                              # surface ectoderm (vertical band)
    te = 0.12 * r
    # brain wall on the left and the optic stalk
    bx = cx - 2.0 * r
    brain = np.array([(bx - 0.5 * r, cy - 2.0 * r), (bx + 0.25 * r, cy - 2.0 * r), (bx + 0.25 * r, cy + 2.0 * r), (bx - 0.5 * r, cy + 2.0 * r)])
    _patch(ax, brain, ne, zorder)
    a["brain"] = (bx - 0.1 * r, cy + 1.4 * r)
    if stage == "vesicle":
        # optic vesicle: a hollow balloon on a broad stalk
        ves = smooth_closed([(bx + 0.2 * r, cy + 0.55 * r), (cx - 0.6 * r, cy + 0.75 * r), (cx + 0.3 * r, cy + 0.95 * r),
                             (cx + 0.95 * r, cy + 0.45 * r), (cx + 0.95 * r, cy - 0.45 * r), (cx + 0.3 * r, cy - 0.95 * r),
                             (cx - 0.6 * r, cy - 0.75 * r), (bx + 0.2 * r, cy - 0.55 * r)])
        _patch(ax, ves, ne, zorder + 1)
        inner = smooth_closed([(bx + 0.2 * r, cy + 0.3 * r), (cx - 0.6 * r, cy + 0.48 * r), (cx + 0.25 * r, cy + 0.7 * r),
                               (cx + 0.72 * r, cy + 0.3 * r), (cx + 0.72 * r, cy - 0.3 * r), (cx + 0.25 * r, cy - 0.7 * r),
                               (cx - 0.6 * r, cy - 0.48 * r), (bx + 0.2 * r, cy - 0.3 * r)])
        _patch(ax, inner, "extracellular", zorder + 1.1, face=P.fill("extracellular"), edge=P.edge(ne), lw=LINE * 0.6)
        _patch(ax, [(xe - te / 2, cy - 2.0 * r), (xe + te / 2, cy - 2.0 * r), (xe + te / 2, cy + 2.0 * r), (xe - te / 2, cy + 2.0 * r)], ep, zorder)
        _patch(ax, [(xe - te / 2 - 0.12 * r, cy - 0.55 * r), (xe + te / 2, cy - 0.6 * r), (xe + te / 2, cy + 0.6 * r),
                    (xe - te / 2 - 0.12 * r, cy + 0.55 * r)], pl, zorder + 0.5)
        a["retina"], a["rpe"] = (cx + 0.85 * r, cy), (cx, cy + 0.85 * r)
        a["placode"], a["lens"] = (xe, cy + 0.3 * r), (xe, cy)
        a["stalk"], a["lumen"] = (cx - 1.1 * r, cy + 0.6 * r), (cx, cy)
        a["ectoderm"] = (xe, cy + 1.5 * r)
        return a
    # optic cup: inner neural retina (thick) and outer RPE (thin), opening to the right
    open_ang = 48 if stage != "eye" else 40
    ro, ri = 1.0 * r, 0.56 * r if stage != "eye" else 0.5 * r
    rpe_t = 0.1 * r
    a0, a1 = open_ang, 360 - open_ang
    _patch(ax, _sector((cx, cy), ro, ro - rpe_t, a0, a1), rp, zorder + 1)
    _patch(ax, _sector((cx, cy), ro - rpe_t - (0.04 * r if stage != "eye" else 0.0), ri, a0, a1), ne, zorder + 1)
    if stage == "eye":
        # retinal layers: two thin lines inside the neural retina
        for f in (0.35, 0.68):
            rr = ri + f * (ro - rpe_t - ri)
            ax.plot(*_arc((cx, cy), rr, a0 + 4, a1 - 4).T, color=P.edge(ne), lw=0.6, zorder=zorder + 1.2)
    # optic stalk: hollow tube from the back of the cup to the brain
    sy = 0.2 * r
    _patch(ax, [(bx + 0.2 * r, cy - sy), (cx - ro + 0.05 * r, cy - sy), (cx - ro + 0.05 * r, cy + sy), (bx + 0.2 * r, cy + sy)], ne, zorder + 0.8)
    if stage == "eye":
        ax.plot([bx + 0.25 * r, cx - ri], [cy, cy], color=P.edge("neuron"), lw=2.0, zorder=zorder + 1.5)
    a["retina"] = (cx + (ri + 0.25 * r) * math.cos(math.radians(140)), cy + (ri + 0.25 * r) * math.sin(math.radians(140)))
    a["rpe"] = (cx + (ro - rpe_t / 2) * math.cos(math.radians(220)), cy + (ro - rpe_t / 2) * math.sin(math.radians(220)))
    a["stalk"] = (cx - 1.4 * r, cy + sy)
    a["lumen"] = (cx - ri * 0.5, cy)
    # lens and surface ectoderm
    if stage == "cup":
        # lens pit: the placode invaginates into the mouth of the cup
        pit = np.vstack([_arc((xe + 0.15 * r, cy), 0.62 * r, 118, 242, 60)])
        poly, _, _ = _band(pit, 0.12 * r, 0.12 * r)
        _patch(ax, poly, pl, zorder + 2)
        for sgn in (1, -1):
            seg = np.array([(xe, cy + sgn * 2.0 * r), (xe, cy + sgn * 0.62 * r)])
            poly, _, _ = _band(seg, te / 2, te / 2)
            _patch(ax, poly, ep, zorder + 2)
        a["lens"] = (xe - 0.45 * r, cy)
        a["placode"] = (xe - 0.45 * r, cy - 0.3 * r)
        a["ectoderm"] = (xe, cy + 1.5 * r)
        a["cornea"] = (xe, cy + 0.9 * r)
        return a
    lr = 0.45 * r if stage == "lens-vesicle" else 0.42 * r
    lc = (cx + 0.62 * r, cy)
    ax.add_patch(Circle(lc, lr, facecolor=P.fill(pl), edgecolor=P.edge(pl), lw=LINE * 0.9, zorder=zorder + 2))
    if stage == "lens-vesicle":
        ax.add_patch(Circle((lc[0] + 0.08 * r, lc[1]), lr * 0.55, facecolor=P.fill("extracellular"), edgecolor=P.edge(pl),
                            lw=LINE * 0.6, zorder=zorder + 2.1))
    else:
        # lens fibres (elongated cells of the posterior lens epithelium) and the anterior lens epithelium
        th = np.linspace(-80, 80, 9)
        for t in th:
            tt = math.radians(t)
            ax.plot([lc[0] - lr * 0.85 * math.cos(tt) * 0.9, lc[0] + lr * 0.45 * math.cos(tt)],
                    [lc[1] + lr * 0.9 * math.sin(tt), lc[1] + lr * 0.9 * math.sin(tt)], color=P.edge(pl), lw=0.5, zorder=zorder + 2.1)
        ax.plot(*_arc(lc, lr * 0.93, -70, 70, 40).T, color=P.edge(pl), lw=1.4, zorder=zorder + 2.2)
    seg = np.array([(xe, cy - 2.0 * r), (xe, cy + 2.0 * r)])
    poly, _, _ = _band(seg, te / 2, te / 2)
    _patch(ax, poly, ep, zorder + 2)
    if stage == "eye":
        # corneal stroma behind the epithelium (from neural crest mesenchyme)
        _patch(ax, [(xe - te / 2 - 0.12 * r, cy - 0.75 * r), (xe - te / 2, cy - 0.8 * r), (xe - te / 2, cy + 0.8 * r),
                    (xe - te / 2 - 0.12 * r, cy + 0.75 * r)], TISSUE["crest"], zorder + 2.1)
    a["lens"], a["placode"] = lc, lc
    a["ectoderm"], a["cornea"] = (xe, cy + 1.5 * r), (xe, cy + 0.55 * r)
    return a


__all__ = ["TISSUE", "DV_DOMAINS", "neurulation_section", "neural_tube_domains", "cortex_layers", "growth_cone", "optic_cup"]
