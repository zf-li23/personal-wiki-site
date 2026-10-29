"""Gametes and fertilization, drawn natively: sperm, eggs with their envelopes, the egg cortex, zygotes.

    from wikibio import gametes as gam
    s = gam.sperm(ax, (2, 3), angle=0, length=4, kind="mammal")       tip of the head at (2, 3), swimming along +x
    e = gam.egg(ax, (8, 3), 2.0, kind="mammal", cumulus=True)          zona pellucida, cortical granules, MII spindle,
                                                                       first polar body, cumulus cells
    gam.egg(ax, (8, 3), 2.0, kind="urchin", jelly=True)                vitelline envelope and jelly coat
    gam.egg(ax, (8, 3), 2.0, kind="urchin", envelope="fertilization")  raised fertilization envelope, hyaline layer
    c = gam.cortex(ax, (0, 0, 10, 3), stage="before")                  magnified egg surface: "before", "exocytosis", "after"
    z = gam.zygote(ax, (5, 5), 1.6, stage="pronuclei")                 "pronuclei", "apposed", "spindle"

Every function returns a dict of anchors (canvas points) for callouts and arrows: ``sperm`` gives tip,
acrosome, nucleus, equatorial (the equatorial segment, where mammalian sperm fuse), midpiece, tail and,
for a reacted sea urchin sperm, process (the tip of the acrosomal process); ``egg`` gives center,
membrane, granule, zona (or envelope), space (perivitelline space), polar_body, spindle, nucleus, cumulus,
jelly, and ``at(angle, f)``, the point at angle (degrees) and fraction f of the egg radius.

Colours (palette tokens): sperm and egg chromatin "chromatin", acrosome "golgi" (it is a Golgi-derived
vesicle), midpiece "mitochondrion", cytoplasm "cytoplasm", egg membrane "membrane", cortical granules
"vesicle", zona pellucida and vitelline / fertilization envelope "bone", jelly coat and hyaline layer
"carbohydrate", cumulus cells "animal".
"""

import math

import numpy as np
from matplotlib.patches import Circle, Ellipse, PathPatch, Polygon, Wedge
from matplotlib.path import Path

from . import palette as P
from .core import LINE, blob


def _rot(angle):
    a = math.radians(angle)
    return np.array([math.cos(a), math.sin(a)]), np.array([-math.sin(a), math.cos(a)])


def _wash(token, light=0.55, dark=0.8):
    """A pale tint of a token for extracellular layers (opaque, theme aware)."""
    return P.mix(P.fill(token), P.surface(), dark if P.is_dark() else light)


def _ring(ax, center, r_out, r_in, face, edge, lw=LINE * 0.8, zorder=5):
    t = np.linspace(0, 2 * np.pi, 180)
    outer = np.c_[center[0] + r_out * np.cos(t), center[1] + r_out * np.sin(t)]
    inner = np.c_[center[0] + r_in * np.cos(t[::-1]), center[1] + r_in * np.sin(t[::-1])]
    verts = np.vstack([outer, inner])
    codes = ([Path.MOVETO] + [Path.LINETO] * (len(outer) - 2) + [Path.CLOSEPOLY]
             + [Path.MOVETO] + [Path.LINETO] * (len(inner) - 2) + [Path.CLOSEPOLY])
    ax.add_patch(PathPatch(Path(verts, codes), facecolor=face, edgecolor=edge, lw=lw, zorder=zorder))


# ------------------------------------------------------------------------------------------- sperm


def sperm(ax, tip, angle=0.0, length=4.0, kind="mammal", acrosome="intact", wave=0.06, waves=1.6, zorder=12):
    """A spermatozoon with the tip of its head at ``tip``, swimming in direction ``angle`` (degrees).

    kind      "mammal" (flattened oval head, acrosomal cap over its front two thirds, long midpiece with a
              helix of mitochondria) or "urchin" (small conical head, a small acrosomal vesicle at the tip,
              a single ring-shaped mitochondrion)
    acrosome  "intact"; "reacted": the acrosome has undergone exocytosis (mammal: the cap is gone and the
              equatorial segment remains; urchin: the actin-filled acrosomal process, coated with bindin,
              projects from the tip)
    wave      amplitude of the flagellar wave as a fraction of ``length``; ``waves`` wavelengths along the tail
    Returns anchors: tip, acrosome, nucleus, equatorial, midpiece, tail (end), process (reacted urchin only).
    """
    d, n = _rot(angle)
    tip = np.asarray(tip, float)

    def pt(s, q):  # s: distance behind the tip, q: sideways offset
        return tip - s * d + q * n

    L = length
    if kind == "mammal":
        hl, hw, ml = 0.13 * L, 0.075 * L, 0.11 * L
    elif kind == "urchin":
        hl, hw, ml = 0.075 * L, 0.04 * L, 0.03 * L
    else:
        raise ValueError(f"unknown sperm kind {kind!r}")
    out = {"tip": tuple(tip)}

    # tail: principal piece with a travelling wave that grows towards the end, line tapering
    s0 = hl + ml
    s = np.linspace(s0, L, 160)
    u = (s - s0) / (L - s0)
    q = wave * L * np.sin(2 * np.pi * waves * u) * (0.25 + 0.75 * u)
    pts = np.array([pt(a, b) for a, b in zip(s, q)])
    for k in range(len(pts) - 1):
        w = LINE * (1.9 - 1.3 * u[k])
        ax.plot(pts[k:k + 2, 0], pts[k:k + 2, 1], color=P.edge("neutral"), lw=w, solid_capstyle="round", zorder=zorder)
    out["tail"] = tuple(pts[-1])

    # midpiece
    a, b = pt(hl * 0.95, 0), pt(s0, 0)
    if kind == "mammal":
        ax.plot([a[0], b[0]], [a[1], b[1]], color=P.edge("mitochondrion"), lw=LINE * 3.4, solid_capstyle="round", zorder=zorder + 0.5)
        k = 7
        for i in range(k):
            c = pt(hl + (i + 0.5) * ml / k, 0)
            e = Ellipse(c, ml / k * 0.95, hw * 0.42, angle=angle + (25 if i % 2 else -25), facecolor=P.fill("mitochondrion"),
                        edgecolor=P.edge("mitochondrion"), lw=LINE * 0.45, zorder=zorder + 0.6)
            ax.add_patch(e)
    else:
        c = pt(hl + ml * 0.5, 0)
        ax.add_patch(Ellipse(c, ml * 1.2, hw * 1.05, angle=angle, facecolor=P.fill("mitochondrion"), edgecolor=P.edge("mitochondrion"),
                             lw=LINE * 0.6, zorder=zorder + 0.6))
    out["midpiece"] = tuple(pt(hl + ml / 2, 0))

    # head (t = 0 is the tip, so the front of the head is the contiguous range |t| < t0)
    t = np.linspace(-np.pi, np.pi, 181)
    xs = hl / 2 * np.cos(t)
    if kind == "mammal":
        ys = hw / 2 * np.sin(t) * (1 - 0.12 * np.cos(t))  # oval, slightly pointed at the front
    else:
        ys = hw / 2 * np.sin(t) * (0.55 + 0.45 * np.cos(t + np.pi)) ** 0.8  # cone with a rounded base
    sh = hl / 2 - xs  # distance behind the tip
    head = np.array([pt(a, b) for a, b in zip(sh, ys)])
    ax.add_patch(Polygon(head, closed=True, facecolor=P.fill("chromatin"), edgecolor=P.edge("chromatin"), lw=LINE * 0.8,
                         zorder=zorder + 1))
    out["nucleus"] = tuple(pt(hl * 0.55, 0))

    if kind == "mammal":
        front = sh < hl * 0.66
        inner = head[front]
        out["equatorial"] = tuple(pt(hl * 0.68, hw * 0.47))
        if acrosome == "intact":
            # acrosomal cap over the anterior two thirds: a crescent between the head outline and an offset of it
            outer = np.array([pt(a - 0.05 * hl, b * 1.16) for a, b in zip(sh[front], ys[front])])
            ax.add_patch(Polygon(np.vstack([outer, inner[::-1]]), closed=True, facecolor=P.fill("golgi"), edgecolor=P.edge("golgi"),
                                 lw=LINE * 0.7, zorder=zorder + 1.5))
            out["acrosome"] = tuple(pt(hl * 0.1, hw * 0.3))
        else:
            # reacted: the exposed inner acrosomal membrane as a thin line on the front of the head
            ax.plot(inner[:, 0], inner[:, 1], color=P.edge("golgi"), lw=LINE * 1.2, zorder=zorder + 1.5)
            out["acrosome"] = tuple(pt(0, 0))
        # equatorial segment: a short band across the head behind the cap
        e1, e2 = pt(hl * 0.66, hw * 0.48), pt(hl * 0.66, -hw * 0.48)
        ax.plot([e1[0], e2[0]], [e1[1], e2[1]], color=P.edge("golgi"), lw=LINE * 1.4, solid_capstyle="round", zorder=zorder + 1.6)
    else:
        out["equatorial"] = tuple(pt(hl * 0.5, hw * 0.45))
        if acrosome == "intact":
            ax.add_patch(Ellipse(pt(hl * 0.06, 0), hl * 0.2, hw * 0.45, angle=angle, facecolor=P.fill("golgi"),
                                 edgecolor=P.edge("golgi"), lw=LINE * 0.6, zorder=zorder + 1.5))
            out["acrosome"] = tuple(pt(hl * 0.06, 0))
        else:
            # acrosomal process: actin filament bundle, bindin coat at the tip
            plen = 0.12 * L
            a, b = pt(0, 0), pt(-plen, 0)
            ax.plot([a[0], b[0]], [a[1], b[1]], color=P.edge("actin"), lw=LINE * 1.5, solid_capstyle="round", zorder=zorder + 1.4)
            for f in np.linspace(0.45, 1.0, 5):
                c = pt(-plen * f, 0)
                ax.add_patch(Circle(c, hw * 0.12, facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.5, zorder=zorder + 1.5))
            out["acrosome"] = tuple(pt(0, 0))
            out["process"] = tuple(b)
    return out


# --------------------------------------------------------------------------------------------- egg


def _spindle(ax, c, size, angle, zorder):
    """A small barrel-shaped meiotic spindle with chromosomes on its metaphase plate."""
    d, n = _rot(angle)
    c = np.asarray(c, float)
    for f in np.linspace(-1, 1, 5):
        pts = [c + d * size * x + n * size * 0.45 * f * (1 - x * x) ** 0.7 for x in np.linspace(-1, 1, 20)]
        pts = np.array(pts)
        ax.plot(pts[:, 0], pts[:, 1], color=P.edge("neutral"), lw=0.6, zorder=zorder)
    for f in np.linspace(-0.6, 0.6, 4):
        p = c + n * size * 0.42 * f
        ax.add_patch(Ellipse(p, size * 0.18, size * 0.13, angle=angle + 90, facecolor=P.fill("chromatin"),
                             edgecolor=P.edge("chromatin"), lw=0.5, zorder=zorder + 0.2))


def egg(ax, center, r=2.0, kind="mammal", zona=True, granules=True, polar_bodies=None, spindle=None, cumulus=False,
        jelly=False, envelope="vitelline", nucleus=None, seed=0, zorder=6):
    """An egg (oocyte) in section, radius ``r`` (the egg cell itself; envelopes lie outside it).

    kind          "mammal": zona pellucida (thick glycoprotein shell) around a narrow perivitelline space; the
                  egg is arrested in metaphase of meiosis II (``spindle`` under the first polar body).
                  "urchin": meiosis is complete (a haploid female pronucleus, ``nucleus``); a thin vitelline
                  envelope lies on the membrane and ``jelly`` adds the jelly coat.
    envelope      urchin only: "vitelline" (before fertilization) or "fertilization" (raised and hardened
                  fertilization envelope with the hyaline layer below it, cortical granules gone)
    granules      cortical granules under the membrane
    polar_bodies  number drawn in the perivitelline space (default 1 for mammals, 0 for urchins)
    cumulus       mammal only: cumulus cells in their hyaluronan matrix around the zona
    """
    x, y = center
    c = np.asarray(center, float)
    rng = np.random.default_rng(seed)
    if polar_bodies is None:
        polar_bodies = 1 if kind == "mammal" else 0
    if spindle is None:
        spindle = kind == "mammal"
    if nucleus is None:
        nucleus = kind == "urchin"
    out = {"center": (x, y)}

    def at(angle, f=1.0):
        a = math.radians(angle)
        return (x + f * r * math.cos(a), y + f * r * math.sin(a))

    out["at"] = at
    fert = kind == "urchin" and envelope == "fertilization"
    if kind == "mammal":
        z_in, z_out = 1.06 * r, 1.26 * r
        if cumulus:
            ax.add_patch(Circle(c, 2.05 * r, facecolor=_wash("carbohydrate", 0.72, 0.86), edgecolor="none", zorder=zorder - 2))
            m = int(46 * r)
            for i in range(m):
                a = rng.uniform(0, 2 * np.pi)
                d = rng.uniform(1.36, 1.95) * r
                if i < 24:  # the corona radiata: a tighter inner ring
                    a, d = 2 * np.pi * i / 24 + rng.uniform(-0.05, 0.05), 1.36 * r
                p = (x + d * math.cos(a), y + d * math.sin(a))
                o = blob(p, 0.12 * r, 0.085 * r, wobble=0.12, seed=int(rng.integers(1e6)), k=7, angle=a)
                ax.add_patch(PathPatch(Path(o, closed=True), facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=LINE * 0.5,
                                       zorder=zorder - 1))
                ax.add_patch(Circle(p, 0.035 * r, facecolor=P.edge("animal"), edgecolor="none", zorder=zorder - 0.9))
            out["cumulus"] = (x + 1.7 * r * math.cos(math.radians(-35)), y + 1.7 * r * math.sin(math.radians(-35)))
        if zona:
            zc = P.mix(P.fill("bone"), P.surface(), 0.4 if P.is_dark() else 0.15)
            _ring(ax, c, z_out, z_in, zc, P.edge("bone"), lw=LINE * 0.8, zorder=zorder)
            ax.add_patch(Circle(c, z_in, facecolor=P.fill("extracellular"), edgecolor=P.edge("bone"), lw=LINE * 0.5, zorder=zorder + 0.1))
            out["zona"] = at(30, (z_in + z_out) / 2 / r)
        out["space"] = at(-60, 1.03)
    else:
        if jelly:
            ax.add_patch(Circle(c, 1.75 * r, facecolor=_wash("carbohydrate", 0.7, 0.85), edgecolor=P.edge("carbohydrate"),
                                lw=LINE * 0.4, ls=(0, (3, 3)), zorder=zorder - 2))
            out["jelly"] = at(35, 1.5)
        if fert:
            env = 1.16 * r
            ax.add_patch(Circle(c, env, facecolor=P.fill("extracellular"), edgecolor=P.edge("bone"), lw=LINE * 1.6, zorder=zorder))
            ax.add_patch(Circle(c, 1.035 * r, facecolor=_wash("carbohydrate", 0.45, 0.7), edgecolor="none", zorder=zorder + 0.1))
            out["envelope"] = at(30, 1.16)
            out["hyaline"] = at(-30, 1.018)
            out["space"] = at(-70, 1.09)
        else:
            out["envelope"] = at(30, 1.025)
            out["space"] = at(-60, 1.0)

    # the egg cell
    ax.add_patch(Circle(c, r, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("membrane"), lw=LINE * 1.2, zorder=zorder + 1))
    out["membrane"] = at(150, 1.0)
    if kind == "urchin" and not fert:
        # thin vitelline envelope lying on the membrane
        ax.add_patch(Circle(c, 1.03 * r, facecolor="none", edgecolor=P.edge("bone"), lw=LINE * 0.9, zorder=zorder + 1.1))

    # yolk platelets / cytoplasmic texture: sparse speckles
    for _ in range(int(40 * r)):
        a, d = rng.uniform(0, 2 * np.pi), r * 0.85 * math.sqrt(rng.uniform(0, 1))
        ax.add_patch(Circle((x + d * math.cos(a), y + d * math.sin(a)), rng.uniform(0.012, 0.03) * r,
                            facecolor=P.mix(P.edge("cytoplasm"), P.fill("cytoplasm"), 0.55), edgecolor="none", zorder=zorder + 1.2))

    if granules and not fert:
        m = int(62 if kind == "urchin" else 46)
        for i in range(m):
            a = 2 * np.pi * (i + 0.5 * rng.uniform()) / m
            if kind == "mammal" and spindle and abs(((math.degrees(a) - 90 + 180) % 360) - 180) < 28:
                continue  # the cortex over the meiotic spindle is free of cortical granules
            p = (x + 0.925 * r * math.cos(a), y + 0.925 * r * math.sin(a))
            ax.add_patch(Circle(p, 0.035 * r, facecolor=P.fill("vesicle"), edgecolor=P.edge("vesicle"), lw=LINE * 0.4,
                                zorder=zorder + 1.5))
        out["granule"] = at(200, 0.925)

    if spindle:
        _spindle(ax, at(90, 0.82), 0.12 * r, 90, zorder + 2)
        out["spindle"] = at(90, 0.82)
    if nucleus:
        p = at(110, 0.35)
        ax.add_patch(Circle(p, 0.16 * r, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=LINE * 0.9, zorder=zorder + 2))
        for k in range(6):
            q = (p[0] + 0.07 * r * math.cos(k * 1.1), p[1] + 0.07 * r * math.sin(k * 1.7))
            ax.add_patch(Circle(q, 0.022 * r, facecolor=P.fill("chromatin"), edgecolor="none", zorder=zorder + 2.1))
        out["nucleus"] = p
    for k in range(polar_bodies):
        a = 90 + (k - (polar_bodies - 1) / 2) * 14
        p = at(a, 1.105 if kind == "mammal" else (1.08 if fert else 1.06))
        rp = 0.075 * r
        ax.add_patch(Circle(p, rp, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("membrane"), lw=LINE * 0.7, zorder=zorder + 2))
        ax.add_patch(Circle(p, rp * 0.42, facecolor=P.fill("chromatin"), edgecolor="none", zorder=zorder + 2.1))
        out["polar_body"] = p
    return out


# ------------------------------------------------------------------------------------------ cortex


def cortex(ax, box, stage="before", kind="urchin", granules=6, zorder=6):
    """A magnified strip of the egg surface, outside at the top, cytoplasm at the bottom.

    stage "before": cortical granules under the plasma membrane (with microvilli), the vitelline envelope
    (urchin) or zona pellucida (mammal) on top, attached by posts; "exocytosis": granules fusing with the
    membrane and releasing their contents, the envelope beginning to lift; "after": urchin: the envelope is
    raised far from the membrane and hardened (the fertilization envelope), a hyaline layer covers the
    membrane; mammal: the zona is modified (hardened, ZP2 cleaved), granules gone.
    Returns anchors: membrane, granule, envelope, space, hyaline, contents, cytoplasm.
    """
    x0, y0, w, h = box
    out = {}
    ym = y0 + 0.42 * h  # membrane level
    ax.add_patch(Polygon([(x0, y0), (x0 + w, y0), (x0 + w, ym), (x0, ym)], closed=True, facecolor=P.fill("cytoplasm"),
                         edgecolor="none", zorder=zorder))
    ax.add_patch(Polygon([(x0, ym), (x0 + w, ym), (x0 + w, y0 + h), (x0, y0 + h)], closed=True, facecolor=P.fill("extracellular"),
                         edgecolor="none", zorder=zorder))
    gw = w / granules
    gr = min(0.17 * h, 0.32 * gw)
    # membrane with microvilli (bumps), opened where granules fuse
    xs = np.linspace(x0, x0 + w, 400)
    ph = ((xs - x0) / (gw / 3.0)) % 1.0  # microvilli: rounded fingers, three per granule spacing
    vill = 0.07 * h * np.sqrt(np.clip(1 - ((ph - 0.5) / 0.18) ** 2, 0, None))
    ys = ym + (vill if stage != "after" or kind == "mammal" else 0.6 * vill)
    ax.plot(xs, ys, color=P.edge("membrane"), lw=LINE * 1.6, zorder=zorder + 2, solid_capstyle="butt")
    out["membrane"] = (x0 + 0.08 * w, ym)
    out["cytoplasm"] = (x0 + 0.5 * w, y0 + 0.12 * h)
    # envelope position
    env_h = 0.06 * h if kind == "urchin" else 0.2 * h
    if stage == "before":
        ye = ym + 0.1 * h
    elif stage == "exocytosis":
        ye = ym + 0.2 * h
    else:
        ye = ym + (0.42 * h if kind == "urchin" else 0.1 * h)
    zcol = P.mix(P.fill("bone"), P.surface(), 0.4 if P.is_dark() else 0.15)
    thick = env_h * (2.2 if (stage == "after" and kind == "urchin") else 1.0)
    ax.add_patch(Polygon([(x0, ye), (x0 + w, ye), (x0 + w, ye + thick), (x0, ye + thick)], closed=True,
                         facecolor=P.edge("bone") if (stage == "after" and kind == "mammal") else zcol, edgecolor=P.edge("bone"),
                         lw=LINE * (1.2 if stage == "after" else 0.8), zorder=zorder + 1))
    out["envelope"] = (x0 + 0.9 * w, ye + thick / 2)
    out["space"] = (x0 + 0.92 * w, (ym + ye) / 2)
    # posts linking envelope and membrane (cut after exocytosis)
    if stage == "before" or (stage == "exocytosis"):
        for i in range(granules * 2):
            px = x0 + (i + 0.25) * gw / 2
            top = ye if stage == "before" else (ye if i % 2 else ym + 0.11 * h)
            ax.plot([px, px], [ym, top], color=P.edge("bone"), lw=LINE * 0.6, zorder=zorder + 0.5,
                    ls="-" if stage == "before" else (0, (2, 1.5)))
    for i in range(granules):
        gx = x0 + (i + 0.5) * gw
        if stage == "before":
            ax.add_patch(Circle((gx, ym - gr * 1.25), gr, facecolor=P.fill("vesicle"), edgecolor=P.edge("vesicle"), lw=LINE * 0.7,
                                zorder=zorder + 1.5))
            out.setdefault("granule", (gx, ym - gr * 1.25))
        elif stage == "exocytosis":
            if i % 2 == 0:
                # omega figure: granule membrane continuous with the plasma membrane, contents spilling out
                ax.add_patch(Wedge((gx, ym), gr * 1.1, 180, 360, width=gr * 0.18, facecolor=P.edge("membrane"), edgecolor="none",
                                   zorder=zorder + 2.1))
                ax.add_patch(Wedge((gx, ym), gr * 0.92, 180, 360, facecolor=P.light("vesicle"), edgecolor="none", zorder=zorder + 1.9))
                ax.add_patch(Polygon([(gx - gr * 0.95, ym - 0.01), (gx + gr * 0.95, ym - 0.01), (gx + gr * 0.95, ym + 0.03 * h),
                                      (gx - gr * 0.95, ym + 0.03 * h)], closed=True, facecolor=P.fill("extracellular"),
                                     edgecolor="none", zorder=zorder + 2.2))
                rng = np.random.default_rng(i + 7)
                for _ in range(10):
                    p = (gx + rng.uniform(-1.4, 1.4) * gr, ym + rng.uniform(0.15, 0.85) * (ye - ym))
                    ax.add_patch(Circle(p, gr * 0.12, facecolor=P.fill("vesicle"), edgecolor=P.edge("vesicle"), lw=0.4, zorder=zorder + 1.6))
                out.setdefault("contents", (gx + gr * 0.5, ym + 0.55 * (ye - ym)))
            else:
                ax.add_patch(Circle((gx, ym - gr * 1.25), gr, facecolor=P.fill("vesicle"), edgecolor=P.edge("vesicle"), lw=LINE * 0.7,
                                    zorder=zorder + 1.5))
                out.setdefault("granule", (gx, ym - gr * 1.25))
    if stage == "after" and kind == "urchin":
        hy = 0.1 * h
        ax.add_patch(Polygon([(x0, ym), (x0 + w, ym), (x0 + w, ym + hy), (x0, ym + hy)], closed=True,
                             facecolor=_wash("carbohydrate", 0.35, 0.6), edgecolor="none", zorder=zorder + 1.2))
        out["hyaline"] = (x0 + 0.1 * w, ym + hy / 2)
    return out


# ------------------------------------------------------------------------------------------ zygote


def _aster(ax, c, r, zorder, n=22, seed=4):
    rng = np.random.default_rng(seed)
    for k in range(n):
        a = 2 * np.pi * k / n + rng.uniform(-0.08, 0.08)
        L = r * rng.uniform(0.6, 1.0)
        ax.plot([c[0], c[0] + L * math.cos(a)], [c[1], c[1] + L * math.sin(a)], color=P.edge("neutral"), lw=0.55, zorder=zorder)
    ax.add_patch(Circle(c, r * 0.06, facecolor=P.edge("neutral"), edgecolor="none", zorder=zorder + 0.1))


def _pronucleus(ax, c, rr, token, zorder, seed):
    o = blob(c, rr, rr * 0.95, wobble=0.04, seed=seed, k=8)
    ax.add_patch(PathPatch(Path(o, closed=True), facecolor=P.fill("nucleus"), edgecolor=P.edge(token), lw=LINE * 1.0, zorder=zorder))
    rng = np.random.default_rng(seed)
    for _ in range(9):
        a, d = rng.uniform(0, 2 * np.pi), rr * 0.6 * math.sqrt(rng.uniform(0, 1))
        ax.add_patch(Circle((c[0] + d * math.cos(a), c[1] + d * math.sin(a)), rr * 0.09, facecolor=P.fill("chromatin"),
                            edgecolor="none", zorder=zorder + 0.1))


def zygote(ax, center, r=1.6, stage="pronuclei", polar_bodies=2, zona=True, aster=True, tail=True, zorder=6):
    """A mammalian zygote: male (from the sperm) and female pronuclei, the sperm aster, two polar bodies.

    stage "pronuclei": the pronuclei far apart, the male near the sperm entry point with its aster;
          "apposed": the pronuclei side by side at the centre; "spindle": pronuclear envelopes broken
          down, maternal and paternal chromosomes on one first-mitotic spindle.
    Returns anchors: male, female, aster, polar_body, tail, center.
    """
    c = np.asarray(center, float)
    out = {"center": tuple(c)}
    if zona:
        zc = P.mix(P.fill("bone"), P.surface(), 0.4 if P.is_dark() else 0.15)
        _ring(ax, c, 1.26 * r, 1.06 * r, zc, P.edge("bone"), zorder=zorder)
        ax.add_patch(Circle(c, 1.06 * r, facecolor=P.fill("extracellular"), edgecolor=P.edge("bone"), lw=LINE * 0.5, zorder=zorder + 0.1))
    ax.add_patch(Circle(c, r, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("membrane"), lw=LINE * 1.2, zorder=zorder + 1))
    for k in range(polar_bodies):
        a = math.radians(90 + (k - (polar_bodies - 1) / 2) * 16)
        p = c + 1.105 * r * np.array([math.cos(a), math.sin(a)])
        ax.add_patch(Circle(p, 0.075 * r, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("membrane"), lw=LINE * 0.7, zorder=zorder + 2))
        ax.add_patch(Circle(p, 0.03 * r, facecolor=P.fill("chromatin"), edgecolor="none", zorder=zorder + 2.1))
        out["polar_body"] = tuple(p)
    entry = c + r * np.array([math.cos(math.radians(-20)), math.sin(math.radians(-20))])
    if stage == "pronuclei":
        male, female, rr = c + r * np.array([0.42, -0.12]), c + r * np.array([-0.3, 0.38]), 0.19 * r
    else:
        male, female, rr = c + r * np.array([0.2, 0.0]), c + r * np.array([-0.2, 0.02]), 0.19 * r
    if tail:
        t = np.linspace(0, 1, 40)
        pts = male[None, :] * (1 - t[:, None]) + entry[None, :] * t[:, None]
        pts = pts + np.c_[np.zeros_like(t), 0.04 * r * np.sin(6 * t)]
        ax.plot(pts[:, 0], pts[:, 1], color=P.edge("neutral"), lw=LINE * 0.9, zorder=zorder + 1.5, ls=(0, (3, 2)))
        out["tail"] = tuple(pts[25])
    if stage in ("pronuclei", "apposed"):
        if aster:
            ac = male + (female - male) / np.linalg.norm(female - male) * rr * 1.25
            _aster(ax, ac, r * (0.55 if stage == "pronuclei" else 0.45), zorder + 1.6)
            out["aster"] = tuple(ac + np.array([0, -0.3 * r]))
        _pronucleus(ax, male, rr * 0.9, "dna", zorder + 2, seed=3)
        _pronucleus(ax, female, rr, "receptor", zorder + 2, seed=5)
    else:
        _spindle(ax, c, 0.32 * r, 0, zorder + 2)
        for k, f in enumerate(np.linspace(-0.6, 0.6, 6)):
            p = c + np.array([0, 0.32 * r * 0.42 * f])
            ax.add_patch(Ellipse(p, 0.32 * r * 0.2, 0.32 * r * 0.14, angle=90, facecolor=P.fill("dna" if k % 2 else "receptor"),
                                 edgecolor=P.edge("dna" if k % 2 else "receptor"), lw=0.5, zorder=zorder + 2.3))
        if aster:
            for s in (-1, 1):
                _aster(ax, c + np.array([s * 0.36 * r, 0]), r * 0.3, zorder + 1.6, n=16, seed=6 + s)
    out["male"], out["female"] = tuple(male), tuple(female)
    return out


__all__ = ["sperm", "egg", "cortex", "zygote"]
