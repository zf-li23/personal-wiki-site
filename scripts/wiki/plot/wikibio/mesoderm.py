"""Mesoderm and its organs: the somite in transverse section, the presomitic mesoderm with the segmentation
clock, endochondral ossification and the growth plate, the nephric series and nephrogenesis, the bipotential
gonad and the genital ducts.

    from wikibio import mesoderm as M
    a = M.somite_section(ax, (6, 8), 10, "mature")        epithelial / early / mature (+ neural tube, notochord,
                                                            aorta, intermediate and lateral plate mesoderm)
    a = M.psm(ax, (1, 2), 12, phase=0.3)                    dorsal view: somites, PSM with cyclic gene stripes,
                                                            tail bud; optional FGF/Wnt and RA bars
    a = M.ossification(ax, (3, 4), 6, "primary")           condensation / cartilage / hypertrophy / collar /
                                                            primary / secondary / mature (a long bone)
    a = M.growth_plate(ax, (8, 1, 4, 8))                    zones of the growth plate in a box (x, y, w, h)
    a = M.nephric_series(ax, (1, 1), 14)                    pro-, meso- and metanephros along the nephric duct
    a = M.nephrogenesis(ax, (4, 3), 1.0, "s-shaped")       cap / vesicle / comma / s-shaped / nephron
    a = M.gonad(ax, (4, 4), 2.0, "testis")                 indifferent / testis / ovary (with the mesonephros)
    a = M.genital_ducts(ax, (4, 4), 6, "male")             indifferent / male / female

Conventions. Transverse sections are drawn dorsal up; dorsal views and lateral views anterior left. Germ layers
keep the colours of ``zoology.GERM`` and the neural tissues those of ``neurodev.TISSUE``; the mesodermal
derivatives have their own tokens (``TISSUE``): dermomyotome pale red, myotome muscle red, sclerotome bone,
syndetome gold, intermediate mesoderm lilac, cartilage pale blue, hypertrophic cartilage pale yellow, ureteric
epithelium blue, metanephric mesenchyme green, Wolffian duct blue, Muellerian duct purple, Sertoli cells teal,
Leydig cells gold, granulosa cells pink, germ cells violet. Every function is deterministic and returns a dict
of anchor points (canvas coordinates) for ``bio.callout`` and arrows.
"""

import math

import numpy as np
from matplotlib.patches import Circle, Ellipse, PathPatch, Polygon
from matplotlib.path import Path

from . import palette as P
from .core import LINE, blob, polyline, smooth_closed

TISSUE = {
    "epidermis": "ectoderm", "neural": "protein", "notochord": "drug", "endoderm": "endoderm", "crest": "cl",
    "paraxial": "mesoderm", "dermomyotome": "rrna", "myotome": "muscle", "sclerotome": "bone", "syndetome": "antibody",
    "intermediate": "metabolite", "lateral": "mesoderm", "aorta": "blood", "mesenchyme": "rrna",
    "cartilage": "dna2", "hypertrophic": "lipid", "bone": "bone", "marrow": "blood", "perichondrium": "enzyme",
    "ureteric": "channel", "metanephric": "carbohydrate", "glomerulus": "blood", "podocyte": "receptor",
    "proximal": "enzyme", "loop": "atp", "distal": "k", "wolffian": "channel", "mullerian": "k",
    "sertoli": "enzyme", "leydig": "atp", "granulosa": "receptor", "theca": "antibody", "germ": "protein",
    "gonad": "rrna", "mesonephros": "metabolite", "clock": "highlight", "fgf": "drug", "ra": "positive",
}


def tok(name):
    """Palette token of a tissue name (``TISSUE``), or the name itself."""
    return TISSUE.get(name, name)


def _patch(ax, pts, name, z, face=None, edge=None, lw=LINE * 0.8, ls="-"):
    t = tok(name)
    v = np.asarray(pts, float)
    p = PathPatch(Path(np.vstack([v, v[:1]]), closed=True), facecolor=face or P.fill(t), edgecolor=edge or P.edge(t),
                  lw=lw, zorder=z, joinstyle="round", linestyle=ls)
    ax.add_patch(p)
    return p


def _wash(name, t=0.55):
    """A pale wash of a tissue colour (darker wash in the dark theme)."""
    return P.mix(P.fill(tok(name)), P.surface(), 0.72 if P.is_dark() else t)


def _ell(c, rx, ry, n=90, a0=0.0, a1=360.0):
    t = np.radians(np.linspace(a0, a1, n))
    return np.c_[c[0] + rx * np.cos(t), c[1] + ry * np.sin(t)]


def _dots(ax, c, rx, ry, n, name, z, r=0.07, seed=0, face=None):
    """Scattered mesenchymal cells in an ellipse."""
    rng = np.random.default_rng(seed)
    k = 0
    while k < n:
        x, y = rng.uniform(-1, 1, 2)
        if x * x + y * y > 1:
            continue
        ax.add_patch(Ellipse((c[0] + rx * x, c[1] + ry * y), 2.4 * r, 1.6 * r, angle=rng.uniform(0, 180),
                             facecolor=face or P.fill(tok(name)), edgecolor=P.edge(tok(name)), lw=0.5, zorder=z))
        k += 1


def _line(ax, pts, name, lw=2.0, z=6, ls="-", color=None):
    p = np.asarray(pts, float)
    ax.plot(p[:, 0], p[:, 1], color=color or P.edge(tok(name)), lw=lw, zorder=z, solid_capstyle="round", linestyle=ls)


def _tube(ax, pts, w, name, z, ls="-", face=None):
    """A duct of width w along a polyline (filled band with a lumen line)."""
    q, nrm, _ = polyline(pts, n=200, closed=False)
    band = np.vstack([q + nrm * w / 2, (q - nrm * w / 2)[::-1]])
    _patch(ax, band, name, z, ls=ls, face=face)
    return q


# ---------------------------------------------------------------------------------------------
# somites


def somite_section(ax, center, width=10.0, stage="mature", signals=False, zorder=5):
    """A transverse section through the trunk of an amniote embryo at the level of a somite, dorsal up.

    ``center`` is the dorsal midline at the epidermis; the section is ``width`` wide and about 0.62 x width high.
    Stages: "epithelial" (a newly formed epithelial ball around a somitocoel), "early" (the ventromedial wall
    undergoes EMT into sclerotome, the dorsolateral wall remains as dermomyotome) and "mature" (dermomyotome,
    myotome beneath it, sclerotome around notochord and neural tube, syndetome between myotome and sclerotome).
    Paired dorsal aortae, intermediate mesoderm, the lateral plate split by the coelom, and the endoderm are
    drawn in every stage. Anchors (right side unless suffixed "_l"): "neural", "notochord", "epidermis", "somite",
    "somitocoel", "dermomyotome", "dml", "vll", "myotome", "sclerotome", "syndetome", "aorta", "intermediate",
    "somatic", "splanchnic", "coelom", "endoderm", "dorsal_tube", "floor".
    """
    s = width / 10.0
    cx, cy = center

    def T(p):
        p = np.asarray(p, float)
        return np.c_[cx + s * p[:, 0], cy + s * p[:, 1]]

    def pt(x, y):
        return (cx + s * x, cy + s * y)

    a = {}
    z = zorder
    # epidermis
    xs = np.linspace(-5, 5, 60)
    top = np.c_[xs, 0.04 * np.cos(xs * 0.6)]
    _patch(ax, T(np.vstack([top, (top - [0, 0.2])[::-1]])), "epidermis", z + 2)
    a["epidermis"] = pt(3.8, -0.1)
    # neural tube and notochord
    nt = _ell((0, -1.45), 0.75, 1.15)
    _patch(ax, T(nt), "neural", z + 2)
    _patch(ax, T(_ell((0, -1.45), 0.1, 0.75)), "extracellular", z + 2.1, edge=P.edge(tok("neural")))
    a["neural"], a["dorsal_tube"], a["floor"] = pt(0.45, -1.2), pt(0, -0.42), pt(0, -2.5)
    ax.add_patch(Circle(pt(0, -3.05), s * 0.33, facecolor=P.fill(tok("notochord")), edgecolor=P.edge(tok("notochord")),
                        lw=LINE * 0.8, zorder=z + 2))
    a["notochord"] = pt(0, -3.05)
    # endoderm
    xe = np.linspace(-5, 5, 40)
    eb = np.c_[xe, -5.55 + 0.12 * np.cos(xe * 0.5)]
    _patch(ax, T(np.vstack([eb, (eb - [0, 0.18])[::-1]])), "endoderm", z + 1)
    a["endoderm"] = pt(3.6, -5.65)
    for sg in (1, -1):
        sfx = "" if sg > 0 else "_l"
        # dorsal aorta
        ax.add_patch(Circle(pt(sg * 0.85, -4.05), s * 0.3, facecolor=P.fill(tok("aorta")), edgecolor=P.edge(tok("aorta")),
                            lw=LINE * 0.8, zorder=z + 2))
        a["aorta" + sfx] = pt(sg * 0.85, -4.05)
        # intermediate mesoderm
        _patch(ax, T(blob((sg * 2.85, -4.0), 0.5, 0.35, seed=7 + sg, wobble=0.06)), "intermediate", z + 2)
        a["intermediate" + sfx] = pt(sg * 2.85, -4.0)
        # lateral plate: somatic (upper) and splanchnic (lower) layers, coelom between
        x0, x1 = 3.4, 5.0
        up = np.array([(x0, -3.6), (x1, -3.35)])
        lo = np.array([(x0, -4.35), (x1, -4.65)])
        _patch(ax, T(np.vstack([up * [sg, 1], (up - [0, 0.22])[::-1] * [sg, 1]])), "lateral", z + 1.5,
               face=P.light(tok("lateral")))
        _patch(ax, T(np.vstack([lo * [sg, 1], (lo - [0, 0.22])[::-1] * [sg, 1]])), "lateral", z + 1.5,
               face=P.light(tok("lateral")))
        a["somatic" + sfx], a["splanchnic" + sfx] = pt(sg * 4.6, -3.5), pt(sg * 4.6, -4.7)
        a["coelom" + sfx] = pt(sg * 4.4, -4.1)
        # somite
        c = (sg * 2.3, -1.75)
        a["somite" + sfx] = pt(*c)
        if stage == "epithelial":
            n = 16
            for k in range(n):
                t0, t1 = 2 * math.pi * k / n, 2 * math.pi * (k + 1) / n
                tt = np.linspace(t0, t1, 6)
                outer = np.c_[c[0] + 1.05 * np.cos(tt), c[1] + 0.95 * np.sin(tt)]
                inner = np.c_[c[0] + 0.45 * np.cos(tt[::-1]), c[1] + 0.4 * np.sin(tt[::-1])]
                _patch(ax, T(np.vstack([outer, inner])), "paraxial", z + 2, lw=LINE * 0.5)
            _dots(ax, T([c])[0], s * 0.32, s * 0.28, 5, "paraxial", z + 2.5, r=0.06 * s, seed=3 + sg,
                  face=P.light(tok("paraxial")))
            a["somitocoel" + sfx] = pt(*c)
            a["dermomyotome" + sfx] = pt(c[0] + sg * 0.6, c[1] + 0.7)
            a["sclerotome" + sfx] = pt(c[0] - sg * 0.7, c[1] - 0.6)
        else:
            mature = stage == "mature"
            # dermomyotome: a curved epithelial plate on the dorsolateral side
            th = np.linspace(math.radians(25), math.radians(155), 40)
            cc = (c[0], c[1] - (0.2 if mature else 0.15))
            r0, r1 = (1.15, 0.92) if mature else (1.05, 0.8)
            arc_o = np.c_[cc[0] + r0 * np.cos(th) * 1.05, cc[1] + r0 * np.sin(th) * 0.95]
            arc_i = np.c_[cc[0] + r1 * np.cos(th[::-1]) * 1.05, cc[1] + r1 * np.sin(th[::-1]) * 0.95]
            _patch(ax, T(np.vstack([arc_o, arc_i])), "dermomyotome", z + 2.5)
            a["dermomyotome" + sfx] = T([(cc[0], cc[1] + (r0 + r1) / 2 * 0.95)])[0]
            lip_med = (cc[0] - sg * (r0 + r1) / 2 * 1.05 * math.cos(math.radians(25)), cc[1] + 0.45)
            lip_lat = (cc[0] + sg * (r0 + r1) / 2 * 1.05 * math.cos(math.radians(25)), cc[1] + 0.45)
            a["dml" + sfx], a["vll" + sfx] = T([lip_med])[0], T([lip_lat])[0]
            if mature:
                th2 = np.linspace(math.radians(30), math.radians(150), 30)
                m_o = np.c_[cc[0] + 0.9 * np.cos(th2) * 1.05, cc[1] + 0.9 * np.sin(th2) * 0.95]
                m_i = np.c_[cc[0] + 0.55 * np.cos(th2[::-1]) * 1.05, cc[1] + 0.55 * np.sin(th2[::-1]) * 0.95]
                _patch(ax, T(np.vstack([m_o, m_i])), "myotome", z + 2.4)
                for k in range(7):
                    tt = th2[3 + 4 * k] if 3 + 4 * k < len(th2) else th2[-2]
                    p0 = (cc[0] + 0.58 * math.cos(tt) * 1.05, cc[1] + 0.58 * math.sin(tt) * 0.95)
                    p1 = (cc[0] + 0.87 * math.cos(tt) * 1.05, cc[1] + 0.87 * math.sin(tt) * 0.95)
                    ax.plot(*T([p0, p1]).T, color=P.edge(tok("myotome")), lw=0.5, zorder=z + 2.45)
                a["myotome" + sfx] = T([(cc[0], cc[1] + 0.72 * 0.95)])[0]
                # syndetome: a thin strip of dorsal sclerotome under the ends of the myotome
                for side in (-1, 1):
                    tt = math.radians(90 + side * 70)
                    p = (cc[0] + 0.72 * math.cos(tt) * 1.05, cc[1] + 0.72 * math.sin(tt) * 0.95 - 0.12)
                    _patch(ax, T(blob(p, 0.2, 0.09, seed=11 + side, wobble=0.05, angle=side * 0.6)), "syndetome", z + 2.6)
                a["syndetome" + sfx] = T([(cc[0] + sg * 0.72 * math.cos(math.radians(20)) * 1.05,
                                           cc[1] + 0.72 * math.sin(math.radians(20)) * 0.95 - 0.12)])[0]
                # sclerotome: mesenchyme spreading ventromedially around notochord and neural tube
                scl = (sg * 1.3, -2.85)
                _dots(ax, T([scl])[0], s * 0.85, s * 0.7, 34, "sclerotome", z + 1.8, r=0.08 * s, seed=21 + sg)
                _dots(ax, T([(sg * 0.55, -3.2)])[0], s * 0.35, s * 0.35, 10, "sclerotome", z + 1.8, r=0.08 * s, seed=31 + sg)
                a["sclerotome" + sfx] = pt(sg * 1.55, -3.0)
            else:
                # ventromedial wall dissolves into sclerotome mesenchyme
                _dots(ax, T([(c[0] - sg * 0.2, c[1] - 0.55)])[0], s * 0.75, s * 0.5, 22, "sclerotome", z + 2,
                      r=0.08 * s, seed=41 + sg)
                a["sclerotome" + sfx] = pt(c[0] - sg * 0.35, c[1] - 0.6)
                a["myotome" + sfx] = a["dermomyotome" + sfx]
                a["syndetome" + sfx] = a["sclerotome" + sfx]
            a["somitocoel" + sfx] = pt(*c)
    return a


def psm(ax, origin, length=12.0, height=1.2, phase=0.0, n_somites=4, front=0.42, gradients=True, waves=2.2,
        zorder=5):
    """Dorsal view of the paraxial mesoderm of one side (anterior left), with the segmentation clock.

    The strip starts at ``origin`` (lower-left corner) and is ``length`` long: ``n_somites`` epithelial somites
    on the left, then the presomitic mesoderm (PSM) and the tail bud on the right. The PSM is shaded by the
    expression of a cyclic gene, high where cos(2 pi (phase - psi(u))) is near 1, with a phase lag psi(u) =
    waves (1 - u)^2 that grows anteriorly (u = 0 at the anterior end of the PSM, 1 at the tail bud), so stripes
    narrow and slow down as they move forward, as in the embryo. ``front`` (0..1 along the PSM) marks the
    determination front. With ``gradients`` two bars below show FGF/Wnt (posterior) and retinoic acid
    (anterior). Anchors: "somites" (list of centres, oldest first), "s0" (forming somite), "psm", "tailbud",
    "front" (top of the front line), "fgf", "ra", "x_psm0", "x_tail", "y_mid".
    """
    x0, y0 = origin
    h = height
    a = {}
    w_s = h * 0.95
    gap = 0.1 * h
    xs = []
    for k in range(n_somites):
        xc = x0 + w_s / 2 + k * (w_s + gap)
        _patch(ax, blob((xc, y0 + h / 2), w_s / 2, h / 2 * 0.95, wobble=0.04, seed=k, k=8), "paraxial", zorder + 1)
        xs.append((xc, y0 + h / 2))
    a["somites"] = xs
    xp0 = x0 + n_somites * (w_s + gap)
    xt = x0 + length
    # PSM outline with rounded tail bud
    yy = np.linspace(0, 1, 30)
    outline = np.vstack([[xp0, y0], [xt - h * 0.6, y0],
                         np.c_[xt - h * 0.6 + h * 0.6 * np.sin(np.pi * yy), y0 + h * yy],
                         [[xp0, y0 + h]]])
    _patch(ax, outline, "paraxial", zorder, face=_wash("paraxial", 0.6))
    # cyclic expression
    n = 160
    us = np.linspace(0, 1, n + 1)
    base, wash = P.fill(tok("clock")), _wash("paraxial", 0.6)
    for i in range(n):
        u = 0.5 * (us[i] + us[i + 1])
        e = 0.5 * (1 + math.cos(2 * math.pi * (phase - waves * (1 - u) ** 2)))
        e = max(0.0, (e - 0.35) / 0.65)
        if e <= 0:
            continue
        xa, xb = xp0 + us[i] * (xt - xp0 - h * 0.6), xp0 + us[i + 1] * (xt - xp0 - h * 0.6)
        ax.add_patch(Polygon([(xa, y0 + 0.04), (xb, y0 + 0.04), (xb, y0 + h - 0.04), (xa, y0 + h - 0.04)], closed=True,
                             facecolor=P.mix(wash, base, e), edgecolor="none", zorder=zorder + 0.5))
    _patch(ax, outline, "paraxial", zorder + 0.6, face="none")
    a["s0"] = (xp0 + 0.35 * h, y0 + h / 2)
    a["psm"] = (xp0 + 0.55 * (xt - xp0), y0 + h / 2)
    a["tailbud"] = (xt - 0.3 * h, y0 + h / 2)
    a["x_psm0"], a["x_tail"], a["y_mid"] = xp0, xt, y0 + h / 2
    xf = xp0 + front * (xt - xp0 - h * 0.6)
    ax.plot([xf, xf], [y0 - 0.15 * h, y0 + h + 0.15 * h], color=P.ink(), lw=1.0, ls=(0, (3, 2)), zorder=zorder + 2)
    a["front"] = (xf, y0 + h + 0.15 * h)
    if gradients:
        yb = y0 - 0.55 * h
        nb = 80
        for name in ("fgf", "ra"):
            key = name
            yb_ = yb if key == "fgf" else yb - 0.32 * h
            for i in range(nb):
                xa = x0 + i / nb * length
                xb = x0 + (i + 1) / nb * length
                xm = 0.5 * (xa + xb)
                if key == "fgf":
                    v = max(0.0, (xm - xp0) / (xt - xp0)) ** 1.6
                else:
                    v = max(0.0, 1 - (xm - x0) / (xf - x0 + 0.3 * (xt - xf))) ** 1.2
                ax.add_patch(Polygon([(xa, yb_), (xb, yb_), (xb, yb_ + 0.22 * h), (xa, yb_ + 0.22 * h)], closed=True,
                                     facecolor=P.mix(P.surface(), P.fill(tok(name)), min(1.0, max(0.0, v))),
                                     edgecolor="none", zorder=zorder))
            ax.add_patch(Polygon([(x0, yb_), (xt, yb_), (xt, yb_ + 0.22 * h), (x0, yb_ + 0.22 * h)], closed=True,
                                 facecolor="none", edgecolor=P.edge(tok(name)), lw=0.6, zorder=zorder + 0.1))
            a[key] = (x0, yb_ + 0.11 * h)
    return a


# ---------------------------------------------------------------------------------------------
# bone


def _bone_outline(c, H, w_shaft, w_end, n=80):
    """Right half-width of a long bone as a function of y (dumbbell), and the closed outline."""
    ys = np.linspace(-H / 2, H / 2, n)
    t = (np.abs(ys) / (H / 2)) ** 4
    hw = w_shaft / 2 + (w_end - w_shaft) / 2 * t
    hw = hw * np.sqrt(np.clip(1 - (np.abs(ys) / (H / 2)) ** 12, 0.02, 1)) + 0.0
    right = np.c_[c[0] + hw, c[1] + ys]
    left = np.c_[c[0] - hw[::-1], c[1] + ys[::-1]]
    return ys, hw, np.vstack([right, left])


def _clip_rect(ax, outline_patch, x0, x1, y0, y1, name, z, face=None):
    r = Polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], closed=True, facecolor=face or P.fill(tok(name)),
                edgecolor="none", zorder=z)
    ax.add_patch(r)
    r.set_clip_path(outline_patch)
    return r


def ossification(ax, center, height=6.0, stage="primary", zorder=5):
    """A developing long bone in longitudinal section (proximal up), at one stage of endochondral ossification.

    Stages: "condensation" (mesenchymal condensation), "cartilage" (a cartilage model in its perichondrium),
    "hypertrophy" (central chondrocytes enlarge), "collar" (a bone collar forms in the perichondrium, now
    periosteum), "primary" (blood vessels invade: primary ossification centre and marrow), "secondary" (secondary
    centres in the epiphyses, growth plates between), "mature" (epiphyses ossified, growth plates closed).
    Anchors: "center", "epiphysis", "growth_plate", "diaphysis", "marrow", "collar", "perichondrium",
    "secondary", "vessel", "top", "bottom", "right".
    """
    c = center
    H = height
    ys, hw, out = _bone_outline(c, H, 0.28 * H, 0.46 * H)
    a = {"center": c, "top": (c[0], c[1] + H / 2), "bottom": (c[0], c[1] - H / 2), "right": c[0] + 0.23 * H}
    z = zorder
    if stage == "condensation":
        _dots(ax, c, 0.2 * H, 0.45 * H, 70, "mesenchyme", z + 1, r=0.02 * H, seed=5)
        a.update(epiphysis=(c[0], c[1] + 0.3 * H), diaphysis=c, perichondrium=(c[0] + 0.2 * H, c[1]))
        return a
    base = "cartilage"
    op = _patch(ax, out, base, z + 1, edge=P.edge(tok("perichondrium")), lw=LINE * 1.1)
    for k in range(60):
        rng = np.random.default_rng(k)
        y = c[1] + rng.uniform(-0.45, 0.45) * H
        hwy = np.interp(y - c[1], ys, hw) * 0.85
        x = c[0] + rng.uniform(-1, 1) * hwy
        r = 0.018 * H
        ax.add_patch(Ellipse((x, y), 2 * r, 1.4 * r, facecolor=P.light(tok("cartilage")), edgecolor=P.edge(tok("cartilage")),
                             lw=0.4, zorder=z + 1.2))
    a["epiphysis"] = (c[0], c[1] + 0.36 * H)
    a["diaphysis"] = c
    a["perichondrium"] = (c[0] + 0.14 * H, c[1] + 0.12 * H)
    if stage == "cartilage":
        return a
    hyp_h = {"hypertrophy": 0.22, "collar": 0.3, "primary": 0.5, "secondary": 0.62, "mature": 0.0}[stage]
    if stage != "mature":
        _clip_rect(ax, op, c[0] - H, c[0] + H, c[1] - hyp_h * H / 2 - 0.06 * H, c[1] + hyp_h * H / 2 + 0.06 * H,
                   "hypertrophic", z + 1.3)
        for k in range(18):
            rng = np.random.default_rng(100 + k)
            y = c[1] + rng.uniform(-0.5, 0.5) * (hyp_h * H + 0.1 * H)
            x = c[0] + rng.uniform(-0.1, 0.1) * H
            ax.add_patch(Circle((x, y), 0.03 * H, facecolor=P.light(tok("hypertrophic")), edgecolor=P.edge(tok("hypertrophic")),
                                lw=0.4, zorder=z + 1.35))
    if stage in ("collar", "primary", "secondary", "mature"):
        # bone collar along the shaft
        yc = 0.22 * H if stage == "collar" else (0.32 * H if stage != "mature" else 0.45 * H)
        for sg in (-1, 1):
            yy = np.linspace(-yc, yc, 30)
            hwy = np.interp(yy, ys, hw)
            band = np.vstack([np.c_[c[0] + sg * hwy, c[1] + yy], np.c_[c[0] + sg * (hwy - 0.035 * H), c[1] + yy][::-1]])
            _patch(ax, band, "bone", z + 1.6)
        a["collar"] = (c[0] + 0.14 * H - 0.02 * H, c[1] - 0.1 * H)
    if stage in ("primary", "secondary", "mature"):
        mh = {"primary": 0.32, "secondary": 0.5, "mature": 0.62}[stage]
        _clip_rect(ax, op, c[0] - 0.105 * H, c[0] + 0.105 * H, c[1] - mh * H / 2, c[1] + mh * H / 2, "marrow", z + 1.5,
                   face=_wash("marrow", 0.7))
        # trabeculae
        rng = np.random.default_rng(9)
        for k in range(14):
            y = c[1] + rng.uniform(-0.5, 0.5) * mh * H
            x = c[0] + rng.uniform(-0.08, 0.08) * H
            ax.plot([x, x + rng.uniform(-0.03, 0.03) * H], [y, y + 0.05 * H], color=P.edge(tok("bone")), lw=1.4, zorder=z + 1.55)
        # vessel entering through the collar
        vx = [c[0] + 0.3 * H, c[0] + 0.17 * H, c[0] + 0.04 * H, c[0] - 0.02 * H]
        vy = [c[1] - 0.05 * H, c[1] - 0.02 * H, c[1] + 0.01 * H, c[1] + 0.08 * H]
        ax.plot(vx, vy, color=P.edge(tok("marrow")), lw=1.6, zorder=z + 1.7)
        a["vessel"] = (vx[0], vy[0])
        a["marrow"] = (c[0] - 0.04 * H, c[1] - 0.08 * H)
    if stage in ("secondary", "mature"):
        for sg in (-1, 1):
            ce = (c[0], c[1] + sg * 0.39 * H)
            if stage == "secondary":
                _patch(ax, blob(ce, 0.09 * H, 0.06 * H, seed=3 + sg, wobble=0.1), "bone", z + 1.8, face=_wash("marrow", 0.7))
                a["growth_plate" if sg > 0 else "growth_plate_l"] = (c[0] + 0.12 * H, c[1] + sg * 0.3 * H)
            else:
                _clip_rect(ax, op, c[0] - H, c[0] + H, ce[1] - 0.09 * H, ce[1] + 0.09 * H, "bone", z + 1.8,
                           face=_wash("marrow", 0.75))
                ax.plot([c[0] - 0.2 * H, c[0] + 0.2 * H], [c[1] + sg * 0.3 * H] * 2, color=P.edge(tok("bone")), lw=1.4,
                        zorder=z + 1.9, clip_path=op)
                a["growth_plate" if sg > 0 else "growth_plate_l"] = (c[0] + 0.1 * H, c[1] + sg * 0.3 * H)
        a["secondary"] = (c[0] + 0.04 * H, c[1] + 0.39 * H)
    return a


def growth_plate(ax, box, columns=6, zorder=5):
    """The zones of an epiphyseal growth plate in a rectangle ``box`` = (x, y, w, h), epiphysis at the top.

    From top to bottom: secondary ossification centre (epiphyseal bone), resting zone (scattered small round
    chondrocytes), proliferative zone (stacked flat chondrocytes in columns), prehypertrophic zone,
    hypertrophic zone (large cells), and the ossification front with blood vessels and trabecular bone of the
    metaphysis. Anchors: one point per zone ("epiphysis", "resting", "proliferative", "prehypertrophic",
    "hypertrophic", "front", "metaphysis"), their y-limits in "y_<zone>" = (y0, y1), "left", "right".
    """
    x, y, w, h = box
    z = zorder
    frac = [("epiphysis", 0.14), ("resting", 0.12), ("proliferative", 0.28), ("prehypertrophic", 0.08),
            ("hypertrophic", 0.2), ("metaphysis", 0.18)]
    a = {"left": x, "right": x + w}
    ytop = y + h
    lim = {}
    for name, f in frac:
        lim[name] = (ytop - f * h, ytop)
        ytop -= f * h
    for name, (y0, y1) in lim.items():
        a["y_" + name] = (y0, y1)
        a[name] = (x + w * 0.5, 0.5 * (y0 + y1))
    a["front"] = (x + w * 0.5, lim["metaphysis"][1])
    # backgrounds
    def rect(y0, y1, face, edge="none", lw=0.0, zz=z):
        ax.add_patch(Polygon([(x, y0), (x + w, y0), (x + w, y1), (x, y1)], closed=True, facecolor=face, edgecolor=edge,
                             lw=lw, zorder=zz))
    rect(*lim["epiphysis"], _wash("marrow", 0.75))
    rect(lim["prehypertrophic"][0], lim["resting"][1], _wash("cartilage", 0.4))
    rect(*lim["hypertrophic"], _wash("hypertrophic", 0.35))
    rect(*lim["metaphysis"], _wash("marrow", 0.75))
    rng = np.random.default_rng(1)
    # epiphyseal bone trabeculae
    for k in range(10):
        yy = rng.uniform(*lim["epiphysis"])
        xx = x + rng.uniform(0.05, 0.9) * w
        ax.plot([xx, xx + 0.08 * w], [yy, yy + rng.uniform(-0.03, 0.03) * h], color=P.edge(tok("bone")), lw=2.0,
                zorder=z + 1, solid_capstyle="round")
    # resting zone
    y0, y1 = lim["resting"]
    for k in range(14):
        ax.add_patch(Circle((x + rng.uniform(0.06, 0.94) * w, rng.uniform(y0 + 0.012 * h, y1 - 0.012 * h)), 0.011 * h,
                            facecolor=P.fill(tok("cartilage")), edgecolor=P.edge(tok("cartilage")), lw=0.5, zorder=z + 1))
    dx = w / columns
    for j in range(columns):
        xc = x + dx * (j + 0.5)
        # proliferative: flat cells
        y0, y1 = lim["proliferative"]
        nrow = 9
        for i in range(nrow):
            yc = y1 - (i + 0.5) * (y1 - y0) / nrow
            ax.add_patch(Ellipse((xc, yc), 0.62 * dx, 0.55 * (y1 - y0) / nrow, facecolor=P.fill(tok("cartilage")),
                                 edgecolor=P.edge(tok("cartilage")), lw=0.5, zorder=z + 1))
        # prehypertrophic: slightly larger, rounder
        y0, y1 = lim["prehypertrophic"]
        for i in range(2):
            yc = y1 - (i + 0.5) * (y1 - y0) / 2
            ax.add_patch(Ellipse((xc, yc), 0.66 * dx, 0.75 * (y1 - y0) / 2, facecolor=P.fill(tok("hypertrophic")),
                                 edgecolor=P.edge(tok("cartilage")), lw=0.5, zorder=z + 1))
        # hypertrophic: large
        y0, y1 = lim["hypertrophic"]
        for i in range(3):
            yc = y1 - (i + 0.5) * (y1 - y0) / 3
            ax.add_patch(Ellipse((xc, yc), 0.78 * dx, 0.85 * (y1 - y0) / 3, facecolor=P.light(tok("hypertrophic")),
                                 edgecolor=P.edge(tok("hypertrophic")), lw=0.6, zorder=z + 1))
        # metaphysis: trabecula continuing each column's septum, vessel between
        y0, y1 = lim["metaphysis"]
        xs_ = x + dx * j
        if j > 0:
            ax.plot([xs_, xs_ + 0.05 * dx], [y1, y0 + 0.2 * (y1 - y0)], color=P.edge(tok("bone")), lw=2.2, zorder=z + 1,
                    solid_capstyle="round")
        ax.plot([xc, xc], [y0, y1 - 0.08 * (y1 - y0)], color=P.edge(tok("marrow")), lw=1.4, zorder=z + 1.1)
        ax.add_patch(Circle((xc, y1 - 0.08 * (y1 - y0)), 0.06 * dx, facecolor=P.fill(tok("marrow")), edgecolor=P.edge(tok("marrow")),
                            lw=0.5, zorder=z + 1.2))
    # outline and perichondrium
    ax.add_patch(Polygon([(x, y), (x + w, y), (x + w, y + h), (x, y + h)], closed=True, facecolor="none",
                         edgecolor=P.muted(), lw=0.8, zorder=z + 2))
    for xe in (x, x + w):
        ax.plot([xe, xe], [lim["metaphysis"][0], lim["resting"][1]], color=P.edge(tok("perichondrium")), lw=2.6,
                zorder=z + 2.1)
    return a


# ---------------------------------------------------------------------------------------------
# kidney


def _ub_tree(ax, root, direction, depth, length, z, name="ureteric", w=0.12, angle=32.0, seed=0, tips=None):
    """A symmetric-ish branching ureteric tree; collects tip positions in ``tips``."""
    rng = np.random.default_rng(seed)
    if tips is None:
        tips = []

    def rec(p, ang, d, L, ww):
        q = (p[0] + L * math.cos(math.radians(ang)), p[1] + L * math.sin(math.radians(ang)))
        _line(ax, [p, q], name, lw=ww * 28, z=z)
        if d == 0:
            tips.append((q, ang))
            return
        for sgn in (-1, 1):
            rec(q, ang + sgn * (angle + rng.uniform(-6, 6)), d - 1, L * 0.72, ww * 0.85)

    rec(root, direction, depth, length, w)
    return tips


def nephric_series(ax, origin, length=14.0, somites=True, gonad=False, zorder=5):
    """Lateral view of the intermediate mesoderm of an amniote embryo (anterior left, dorsal up).

    Along the nephric (Wolffian) duct, which runs from anterior to the cloaca at the posterior end: the
    pronephros (a few degenerating tubules, dashed), the mesonephros (S-shaped tubules with glomeruli) and the
    metanephros (the ureteric bud growing from the posterior duct into the metanephric mesenchyme). With
    ``somites`` a row of somites is drawn above for reference; with ``gonad`` the genital ridge lies along the
    mesonephros. Anchors: "pronephros", "mesonephros", "duct", "cloaca", "ureteric_bud", "metanephric",
    "gonad", "somites" (x positions), "y_duct".
    """
    x0, y0 = origin
    L = length
    z = zorder
    a = {}
    yd = y0 + 1.6
    a["y_duct"] = yd
    if somites:
        xs = []
        n = 16
        for k in range(n):
            xc = x0 + 0.4 + k * (L * 0.82 / n)
            _patch(ax, blob((xc, y0 + 4.1), 0.3, 0.32, seed=k, wobble=0.05, k=8), "paraxial", z, face=_wash("paraxial", 0.5))
            xs.append(xc)
        a["somites"] = xs
    # nephric duct to the cloaca
    xd1 = x0 + 0.86 * L
    duct = [(x0 + 0.5, yd), (xd1, yd), (xd1 + 0.35, yd - 0.6), (xd1 + 0.45, y0 + 0.2)]
    _tube(ax, duct, 0.16, "wolffian", z + 2)
    a["duct"] = (x0 + 0.42 * L, yd)
    _patch(ax, blob((xd1 + 0.55, y0 + 0.05), 0.6, 0.35, seed=4, wobble=0.05), "endoderm", z + 1)
    a["cloaca"] = (xd1 + 0.55, y0 + 0.05)
    # pronephros
    for k in range(3):
        xp = x0 + 0.8 + 0.45 * k
        _line(ax, [(xp, yd + 0.08), (xp - 0.15, yd + 0.55), (xp + 0.05, yd + 0.85)], "intermediate", lw=2.0, z=z + 1.5,
              ls=(0, (2, 1.5)))
    a["pronephros"] = (x0 + 1.25, yd + 0.6)
    # mesonephros
    xm0, xm1 = x0 + 0.17 * L, x0 + 0.62 * L
    _patch(ax, blob(((xm0 + xm1) / 2, yd + 0.65), (xm1 - xm0) / 2 + 0.3, 0.75, seed=8, wobble=0.03, k=10),
           "mesonephros", z, face=_wash("mesonephros", 0.6))
    nt = 9
    for k in range(nt):
        xp = xm0 + (k + 0.5) * (xm1 - xm0) / nt
        tt = np.linspace(0, 1, 20)
        cur = np.c_[xp + 0.16 * np.sin(2 * np.pi * tt), yd + 0.08 + 0.85 * tt]
        _line(ax, cur, "intermediate", lw=1.8, z=z + 1.5)
        ax.add_patch(Circle((xp, yd + 1.02), 0.13, facecolor=P.fill(tok("glomerulus")), edgecolor=P.edge(tok("glomerulus")),
                            lw=0.6, zorder=z + 1.6))
    a["mesonephros"] = ((xm0 + xm1) / 2, yd + 1.2)
    if gonad:
        _patch(ax, blob(((xm0 + xm1) / 2, yd + 1.85), (xm1 - xm0) / 2 * 0.8, 0.28, seed=12, wobble=0.04, k=10), "gonad", z + 0.5)
        a["gonad"] = ((xm0 + xm1) / 2, yd + 1.85)
    # metanephric mesenchyme and ureteric bud
    cm = (x0 + 0.76 * L, yd + 1.0)
    _patch(ax, blob(cm, 0.75, 0.55, seed=2, wobble=0.06), "metanephric", z + 1, face=_wash("metanephric", 0.4))
    a["metanephric"] = (cm[0] - 0.35, cm[1] + 0.35)
    tips = _ub_tree(ax, (xd1 - 0.6, yd + 0.06), 105, 2, 0.55, z + 2, w=0.1)
    a["ureteric_bud"] = (xd1 - 0.62, yd + 0.4)
    return a


def nephrogenesis(ax, center, size=1.0, stage="s-shaped", zorder=5):
    """One step of nephron formation next to a ureteric bud tip (the tip at the top, its stalk going up).

    Stages: "cap" (cap mesenchyme around the tip), "aggregate" (pretubular aggregate), "vesicle" (renal vesicle,
    epithelial), "comma", "s-shaped" (S-shaped body: proximal, middle and distal limbs, the distal end fused to
    the ureteric bud, endothelial cells in the proximal cleft) and "nephron" (glomerulus with podocytes,
    proximal tubule, loop of Henle, distal tubule, joined to the collecting duct). ``size`` scales the drawing
    (about 3 x 3 units at size 1). Anchors: "tip", "stalk", "structure", "proximal", "distal", "glomerulus",
    "loop", "cap".
    """
    cx, cy = center
    s = size
    z = zorder
    a = {}

    def pt(x, y):
        return (cx + s * x, cy + s * y)

    # ureteric bud: stalk from the top, T-shaped tip pointing down-left
    stalk = [pt(0.6, 1.5), pt(0.6, 0.6)]
    _tube(ax, stalk, 0.28 * s, "ureteric", z + 2)
    tip = [pt(0.1, 0.45), pt(0.6, 0.55), pt(1.1, 0.45)]
    _tube(ax, tip, 0.28 * s, "ureteric", z + 2)
    a["tip"], a["stalk"] = pt(0.6, 0.5), pt(0.6, 1.2)
    a["cap"] = pt(-0.05, 0.15)
    if stage in ("cap", "aggregate", "vesicle", "comma", "s-shaped"):
        _dots(ax, pt(0.6, 0.15), 0.8 * s, 0.22 * s, 24, "metanephric", z + 1, r=0.05 * s, seed=4)
    if stage == "cap":
        a["structure"] = a["cap"]
        return a
    if stage == "aggregate":
        _dots(ax, pt(-0.05, -0.35), 0.28 * s, 0.25 * s, 14, "metanephric", z + 1.5, r=0.05 * s, seed=6,
              face=P.fill(tok("metanephric")))
        a["structure"] = pt(-0.05, -0.35)
        return a
    if stage == "vesicle":
        _patch(ax, _ell(pt(-0.05, -0.4), 0.33 * s, 0.3 * s), "metanephric", z + 1.5)
        _patch(ax, _ell(pt(-0.05, -0.4), 0.15 * s, 0.13 * s), "extracellular", z + 1.6, edge=P.edge(tok("metanephric")))
        a["structure"] = pt(-0.05, -0.4)
        return a
    if stage == "comma":
        tt = np.linspace(0, 1, 40)
        cur = np.c_[cx + s * (0.25 - 0.45 * np.sin(np.pi * tt)), cy + s * (0.2 - 0.9 * tt)]
        _tube(ax, cur, 0.2 * s, "metanephric", z + 1.5)
        a["structure"], a["distal"], a["proximal"] = pt(-0.2, -0.3), pt(0.25, 0.2), pt(0.25, -0.7)
        return a
    if stage == "s-shaped":
        tt = np.linspace(0, 1, 80)
        xs_ = 0.5 * np.sin(2 * np.pi * tt * 1.0) * (1 - 0.2 * tt)
        cur = np.c_[cx + s * (0.35 - 0.0 * tt + xs_), cy + s * (0.3 - 1.4 * tt)]
        for (i0, i1, name) in ((0, 28, "distal"), (27, 56, "loop"), (55, 80, "proximal")):
            _tube(ax, cur[i0:i1], 0.2 * s, name, z + 1.5)
        _patch(ax, _ell(pt(-0.05, -1.05), 0.2 * s, 0.14 * s, a0=200, a1=340), "podocyte", z + 1.6)
        ax.add_patch(Circle(pt(-0.05, -1.05), 0.12 * s, facecolor=P.fill(tok("glomerulus")), edgecolor=P.edge(tok("glomerulus")),
                            lw=0.6, zorder=z + 1.7))
        a["structure"], a["distal"], a["proximal"], a["glomerulus"] = pt(0.0, -0.4), pt(0.65, 0.1), pt(-0.15, -0.55), pt(-0.05, -1.05)
        return a
    # mature nephron: glomerulus, proximal convoluted, loop down, distal back up to collecting duct
    gl = pt(-0.6, -0.2)
    ax.add_patch(Circle(gl, 0.26 * s, facecolor=P.fill(tok("podocyte")), edgecolor=P.edge(tok("podocyte")), lw=0.8, zorder=z + 1.5))
    ax.add_patch(Circle(gl, 0.15 * s, facecolor=P.fill(tok("glomerulus")), edgecolor=P.edge(tok("glomerulus")), lw=0.6, zorder=z + 1.6))
    tt = np.linspace(0, 1, 40)
    prox = np.c_[cx + s * (-0.35 + 0.35 * tt + 0.12 * np.sin(6 * np.pi * tt)), cy + s * (-0.2 - 0.25 * tt)]
    loop_dn = np.array([pt(0.0, -0.45), pt(0.0, -1.6)])
    loop_up = np.array([pt(0.25, -1.6), pt(0.25, -0.7)])
    dist = np.c_[cx + s * (0.25 + 0.2 * tt), cy + s * (-0.7 + 0.8 * tt)]
    _tube(ax, prox, 0.13 * s, "proximal", z + 1.5)
    _tube(ax, np.vstack([loop_dn, [pt(0.12, -1.75)], loop_up]), 0.11 * s, "loop", z + 1.5)
    _tube(ax, np.vstack([dist, [pt(0.5, 0.25)]]), 0.12 * s, "distal", z + 1.5)
    # collecting duct continuing the stalk
    _tube(ax, [pt(0.6, 0.6), pt(0.6, -1.8)], 0.22 * s, "ureteric", z + 1.8)
    a["structure"], a["glomerulus"], a["proximal"], a["loop"], a["distal"] = gl, gl, pt(-0.15, -0.35), pt(0.12, -1.7), pt(0.38, -0.3)
    a["collecting"] = pt(0.6, -1.2)
    return a


# ---------------------------------------------------------------------------------------------
# gonad and ducts


def gonad(ax, center, size=2.0, fate="indifferent", zorder=5):
    """A transverse section of the gonad on the ventromedial surface of the mesonephros (dorsal up).

    The mesonephros, in the upper part, contains the Wolffian (blue) and Muellerian (purple) ducts; the gonad
    hangs below it. Fates: "indifferent" (bipotential: coelomic epithelium, primitive sex cords, germ cells
    scattered), "testis" (testis cords of Sertoli cells around germ cells in the medulla, Leydig cells between
    them, a coelomic vessel under the tunica albuginea; Muellerian duct regressing) and "ovary" (cortical
    clusters: each germ cell in a ring of granulosa cells, theca between; Wolffian duct regressing). ``size`` is
    the radius of the gonad. Anchors: "gonad", "mesonephros", "wolffian", "mullerian", "epithelium", "cords",
    "germ", "sertoli", "leydig", "vessel", "granulosa", "theca", "medulla", "cortex".
    """
    cx, cy = center
    R = size
    z = zorder
    a = {}
    mes = (cx, cy + 1.25 * R)
    _patch(ax, blob(mes, 0.9 * R, 0.5 * R, seed=3, wobble=0.04), "mesonephros", z, face=_wash("mesonephros", 0.55))
    a["mesonephros"] = (mes[0] - 0.5 * R, mes[1] + 0.2 * R)
    wd, md = (mes[0] - 0.25 * R, mes[1] + 0.05 * R), (mes[0] + 0.45 * R, mes[1] - 0.05 * R)
    ls_w = (0, (2, 1.5)) if fate == "ovary" else "-"
    ls_m = (0, (2, 1.5)) if fate == "testis" else "-"
    _patch(ax, _ell(wd, 0.14 * R, 0.14 * R), "wolffian", z + 2, ls=ls_w, face=_wash("wolffian", 0.3) if fate == "ovary" else None)
    _patch(ax, _ell(md, 0.12 * R, 0.12 * R), "mullerian", z + 2, ls=ls_m, face=_wash("mullerian", 0.3) if fate == "testis" else None)
    a["wolffian"], a["mullerian"] = wd, md
    g = blob((cx, cy), 0.75 * R, R, seed=1, wobble=0.03, k=10)
    _patch(ax, g, "gonad", z + 1, face=_wash("gonad", 0.55), lw=LINE * (1.4 if fate == "testis" else 0.9),
           edge=P.edge(tok("gonad")))
    a["gonad"] = (cx, cy)
    a["epithelium"] = (cx + 0.73 * R, cy - 0.2 * R)
    rng = np.random.default_rng(7)

    def germ(p, r=0.09):
        ax.add_patch(Circle(p, r * R, facecolor=P.fill(tok("germ")), edgecolor=P.edge(tok("germ")), lw=0.6, zorder=z + 3))

    if fate == "indifferent":
        for k in range(5):
            y = cy + R * (0.55 - 0.27 * k)
            cur = np.c_[np.linspace(cx - 0.45 * R, cx + 0.45 * R, 12), y + 0.05 * R * np.sin(np.linspace(0, 6, 12))]
            _line(ax, cur, "sertoli", lw=3.5, z=z + 2, color=P.light(tok("sertoli")))
        for k in range(9):
            germ((cx + rng.uniform(-0.45, 0.45) * R, cy + rng.uniform(-0.75, 0.75) * R))
        a["cords"], a["germ"] = (cx - 0.3 * R, cy + 0.28 * R), (cx + 0.2 * R, cy)
    elif fate == "testis":
        cords = []
        for k in range(4):
            y = cy + R * (0.5 - 0.33 * k)
            cc = (cx, y)
            band = _ell(cc, 0.5 * R, 0.12 * R)
            _patch(ax, band, "sertoli", z + 2)
            for j in range(4):
                germ((cx + (-0.33 + 0.22 * j) * R, y), 0.065)
            cords.append(cc)
        for k in range(12):
            ax.add_patch(Circle((cx + rng.uniform(-0.42, 0.42) * R, cy + R * (0.335 - 0.33 * rng.integers(0, 3))),
                                0.045 * R, facecolor=P.fill(tok("leydig")), edgecolor=P.edge(tok("leydig")), lw=0.5, zorder=z + 2.5))
        tt = np.linspace(-0.8, 0.8, 30)
        ax.plot(cx + 0.66 * R * np.cos(tt), cy + 0.9 * R * np.sin(tt), color=P.edge(tok("aorta")), lw=1.8, zorder=z + 2.6)
        a["cords"], a["sertoli"], a["germ"] = cords[1], (cx + 0.45 * R, cords[1][1]), (cx - 0.11 * R, cords[2][1])
        a["leydig"] = (cx, cy - 0.325 * R)
        a["vessel"] = (cx + 0.66 * R * math.cos(0.3), cy + 0.9 * R * math.sin(0.3))
        a["medulla"] = (cx, cy)
    elif fate == "ovary":
        fol = []
        for k in range(11):
            t = 2 * math.pi * k / 11
            p = (cx + 0.55 * R * math.cos(t), cy + 0.78 * R * math.sin(t))
            ax.add_patch(Circle(p, 0.15 * R, facecolor=P.fill(tok("granulosa")), edgecolor=P.edge(tok("granulosa")), lw=0.6,
                                zorder=z + 2))
            germ(p, 0.07)
            fol.append(p)
        _dots(ax, (cx, cy), 0.3 * R, 0.5 * R, 12, "theca", z + 2, r=0.035 * R, seed=9)
        a["granulosa"], a["germ"], a["theca"] = (fol[0][0] + 0.12 * R, fol[0][1]), fol[2], (cx + 0.1 * R, cy - 0.1 * R)
        a["cortex"], a["medulla"] = fol[9], (cx, cy)
    return a


def genital_ducts(ax, center, height=6.0, sex="indifferent", zorder=5):
    """Frontal view of the internal genital tract (cranial up), indifferent, male or female.

    "indifferent": paired gonads with both the Wolffian (mesonephric) and Muellerian (paramesonephric) ducts
    running to the urogenital sinus. "male": testes, epididymis and vas deferens with the seminal vesicles from the
    Wolffian ducts; the Muellerian ducts regressed (dashed remnants). "female": ovaries, oviducts with fimbriae,
    the fused uterus and upper vagina from the Muellerian ducts; the Wolffian ducts regressed (dashed).
    Anchors: "gonad", "gonad_l", "wolffian", "mullerian", "sinus", "epididymis", "vas", "vesicle", "oviduct",
    "uterus", "vagina".
    """
    cx, cy = center
    H = height
    s = H / 6.0
    z = zorder
    a = {}

    def pt(x, y):
        return (cx + s * x, cy + s * y)

    sinus = pt(0, -2.6)
    _patch(ax, blob(sinus, 0.7 * s, 0.35 * s, seed=2, wobble=0.04), "endoderm", z + 1)
    a["sinus"] = sinus
    for sg in (1, -1):
        sfx = "" if sg > 0 else "_l"
        g = pt(sg * 2.0, 1.9)
        gname = {"indifferent": "gonad", "male": "sertoli", "female": "granulosa"}[sex]
        _patch(ax, blob(g, 0.45 * s, 0.7 * s, seed=4 + sg, wobble=0.03), gname, z + 2,
               face=_wash(gname, 0.4) if sex == "indifferent" else None)
        a["gonad" + sfx] = g
        # Wolffian duct: lateral path from the gonad down to the sinus
        wpath = [pt(sg * 1.6, 1.5), pt(sg * 1.5, 0.4), pt(sg * 1.0, -1.2), pt(sg * 0.35, -2.4)]
        # Muellerian duct: lateral funnel above, crossing medially, the two fusing in the midline
        mpath = [pt(sg * 2.6, 2.8), pt(sg * 2.3, 0.9), pt(sg * 1.2, -0.6), pt(sg * 0.12, -1.3), pt(sg * 0.12, -2.35)]
        if sex == "male":
            _tube(ax, mpath, 0.1 * s, "mullerian", z + 1, ls=(0, (2, 2)), face=_wash("mullerian", 0.2))
            # epididymis: coiled near the testis
            tt = np.linspace(0, 1, 60)
            epi = np.c_[cx + s * (sg * (1.55 + 0.12 * np.sin(14 * np.pi * tt))), cy + s * (2.4 - 1.4 * tt)]
            _line(ax, epi, "wolffian", lw=2.2, z=z + 3)
            _tube(ax, [pt(sg * 1.55, 1.0)] + wpath[1:], 0.16 * s, "wolffian", z + 3)
            _patch(ax, blob(pt(sg * 0.75, -1.65), 0.22 * s, 0.4 * s, seed=8 + sg, wobble=0.1, angle=sg * 0.5), "wolffian", z + 3.1,
                   face=P.light(tok("wolffian")))
            a["epididymis" + sfx], a["vas" + sfx], a["vesicle" + sfx] = pt(sg * 1.6, 1.9), pt(sg * 1.35, -0.2), pt(sg * 0.75, -1.65)
            a["mullerian" + sfx] = pt(sg * 2.2, 0.6)
        elif sex == "female":
            _tube(ax, wpath, 0.09 * s, "wolffian", z + 1, ls=(0, (2, 2)), face=_wash("wolffian", 0.2))
            _tube(ax, mpath[:3], 0.18 * s, "mullerian", z + 3)
            # fimbriae
            for k in range(4):
                t = math.radians(60 + 25 * k) if sg > 0 else math.radians(120 - 25 * k)
                p0 = pt(sg * 2.6, 2.8)
                ax.plot([p0[0], p0[0] + 0.35 * s * math.cos(t)], [p0[1], p0[1] + 0.35 * s * math.sin(t)],
                        color=P.edge(tok("mullerian")), lw=1.6, zorder=z + 3)
            a["oviduct" + sfx] = pt(sg * 2.35, 1.2)
            a["wolffian" + sfx] = pt(sg * 1.45, 0.3)
        else:
            _tube(ax, wpath, 0.14 * s, "wolffian", z + 2)
            _tube(ax, mpath, 0.14 * s, "mullerian", z + 2.5)
            a["wolffian" + sfx], a["mullerian" + sfx] = pt(sg * 1.5, 0.3), pt(sg * 2.35, 1.4)
    if sex == "female":
        ut = [pt(-1.25, -0.5), pt(1.25, -0.5), pt(0.55, -1.6), pt(0.3, -2.45), pt(-0.3, -2.45), pt(-0.55, -1.6)]
        _patch(ax, smooth_closed(ut, 120), "mullerian", z + 3.2)
        a["uterus"], a["vagina"] = pt(0, -1.1), pt(0, -2.3)
    return a


# ---------------------------------------------------------------------------------------------
# public drawing helpers


def tube(ax, points, width, tissue, zorder=5, dashed=False):
    """Draw a duct of the given width along a polyline in a tissue's colours (dashed: regressing)."""
    return _tube(ax, points, width, tissue, zorder, ls=(0, (2, 1.5)) if dashed else "-")


def cells(ax, center, rx, ry, n, tissue, zorder=5, r=0.07, seed=0, faded=False):
    """Scatter n small mesenchymal cells in an ellipse (faded: dying or inactive cells, neutral colour)."""
    _dots(ax, center, rx, ry, n, tissue, zorder, r=r, seed=seed, face=P.light("neutral") if faded else None)


def ureteric_tree(ax, root, direction=-90.0, depth=3, length=0.8, zorder=6, width=0.08, angle=34.0, seed=0):
    """A bifurcating ureteric bud tree from ``root`` (direction in degrees); returns the list of tip points."""
    return [p for p, _ in _ub_tree(ax, root, direction, depth, length, zorder, w=width, angle=angle, seed=seed)]
