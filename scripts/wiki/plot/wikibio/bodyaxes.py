"""Body-axis figures of early embryos: the Drosophila egg chamber and blastoderm cross-section, amphibian eggs,
blastulae and gastrulae with their signalling centres, the chick blastoderm, the mouse egg cylinder and the ciliated
node that breaks left-right symmetry.

    from wikibio import bodyaxes as BA
    ch = BA.EggChamber(ax, (6, 4), 9, 4)               Drosophila egg chamber (anterior left, dorsal up), stage 9-10
    ch.cortex(150, 210, "receptor")                   paint a cortical crescent of the oocyte (degrees: 0 posterior,
                                                      90 dorsal, 180 anterior); ch.microtubules(); ch.anchors[...]
    xs = BA.FlyCrossSection(ax, (4, 4), 2.5, values=lambda s: np.exp(-s**2 / 0.045))
                                                      transverse section of the syncytial blastoderm (dorsal up);
                                                      s = 0 ventral midline ... 1 dorsal midline; xs.domain(0, 0.2, ...)
    a = BA.amphibian(ax, (4, 4), 2.2, stage="egg" | "blastula" | "gastrula", dorsal="right")
    c = BA.chick_blastoderm(ax, (4, 4), 2.5, stage="prestreak" | "streak")   (dorsal view, posterior down)
    m = BA.egg_cylinder(ax, (4, 4), 1.4, 3.0, streak=True)                    (mouse E6.5, sagittal; anterior left)
    n = BA.node_pit(ax, (6, 3), 4.0, n=7)              ventral view of the mouse node with rotating cilia and flow
    BA.cilium_cone(ax, (2, 1), 2.0, tilt=35, cone=30)  side view of one tilted, rotating node cilium over the wall

Germ layers use ``zoology.GERM`` (ectoderm blue, mesoderm red, endoderm yellow). Every drawing returns a dict of
anchors (or an object with ``anchors``) so that labels and arrows can be attached.
"""

import math

import numpy as np
from matplotlib.patches import Circle, Ellipse, PathPatch, Polygon
from matplotlib.path import Path

from . import palette as P
from .core import LINE, arrow, blob, label, smooth_closed
from .zoology import GERM


def _ell(c, rx, ry, t0=0.0, t1=2 * np.pi, n=200):
    t = np.linspace(t0, t1, n)
    return np.c_[c[0] + rx * np.cos(t), c[1] + ry * np.sin(t)]


def _poly(ax, pts, face, edge, lw=LINE * 0.8, zorder=5, closed=True, ls="-"):
    p = PathPatch(Path(np.vstack([pts, pts[:1]]) if closed else pts, closed=closed), facecolor=face, edgecolor=edge, lw=lw,
                  zorder=zorder, joinstyle="round", ls=ls)
    ax.add_patch(p)
    return p


def _wash(token, t=0.5):
    return P.mix(P.fill(token), P.surface(), 0.72 if P.is_dark() else t)


def _pigment():
    """Dark-brown cortical pigment of the amphibian animal hemisphere (readable in both themes)."""
    return P.mix(P.edge("animal"), "#3b2a1e", 0.25 if P.is_dark() else 0.45)


# ---------------------------------------------------------------------------------------------------------------
# Drosophila


class EggChamber:
    """A Drosophila egg chamber at stage 9-10 in a sagittal section: anterior left, dorsal up.

    Fifteen nurse cells (seven drawn) fill the anterior part and are joined to the oocyte by ring canals; the oocyte
    fills the posterior part. A follicular epithelium surrounds both: squamous over the nurse cells, columnar over the
    oocyte. ``nucleus`` places the oocyte nucleus: "dorsal" (anterior-dorsal corner, stage 8 onwards) or "posterior"
    (stage 6-7, before it migrates). ``boundary`` is the nurse-cell/oocyte boundary as a fraction of the length.

    ``anchors``: centre, oocyte, nucleus, anterior (oocyte anterior cortex), posterior (posterior pole of the oocyte),
    dorsal_anterior (cortex next to the nucleus), nurse (a nurse cell), ring_canal, border_cells, follicle_dorsal,
    follicle_ventral, follicle_posterior, follicle_nurse (squamous cells), stalk.
    """

    def __init__(self, ax, center, length=9.0, height=4.2, nucleus="dorsal", boundary=0.47, border_cells=True,
                 zorder=5):
        self.ax, self.z = ax, zorder
        cx, cy = center
        self.c = np.array(center, float)
        a, b = length / 2, height / 2
        self.a, self.b = a, b
        xb = cx - a + boundary * length  # anterior border of the oocyte (at the midline)
        self.xb = xb
        t = np.linspace(0, 2 * np.pi, 360, endpoint=False)
        # slightly egg-shaped chamber, fuller posteriorly
        rx = a * (1 + 0.04 * np.cos(t))
        inner = np.c_[cx + rx * np.cos(t), cy + b * np.sin(t)]
        nrm = np.c_[b * np.cos(t), rx * np.sin(t)]
        nrm /= np.linalg.norm(nrm, axis=1)[:, None]
        over_oocyte = inner[:, 0] > xb - 0.15 * b
        thick = np.where(over_oocyte, 0.15 * height, 0.045 * height)
        # smooth the step in epithelial height
        k = 31
        ker = np.hanning(k) / np.hanning(k).sum()
        thick = np.convolve(np.r_[thick[-k:], thick, thick[:k]], ker, mode="same")[k:-k]
        outer = inner + nrm * thick[:, None]
        self.inner, self.outer, self.nrm, self.thick, self.t = inner, outer, nrm, thick, t
        ftok = "mg"
        ring = np.vstack([outer, outer[:1], inner[::-1], inner[-1:]])
        codes = [Path.MOVETO] + [Path.LINETO] * len(outer) + [Path.MOVETO] + [Path.LINETO] * len(inner)
        ax.add_patch(PathPatch(Path(ring, codes), facecolor=P.fill(ftok), edgecolor=P.edge(ftok), lw=LINE * 0.8,
                               zorder=zorder))
        # follicle cell boundaries and nuclei
        nseg = 64
        for j in range(nseg):
            i = int(j * len(t) / nseg)
            p, q = inner[i], outer[i]
            ax.plot([p[0], q[0]], [p[1], q[1]], color=P.edge(ftok), lw=0.5, zorder=zorder + 0.2)
            i2 = int((j + 0.5) * len(t) / nseg)
            m = (inner[i2] + outer[i2]) / 2
            ax.add_patch(Ellipse(m, min(0.09 * height, thick[i2] * 0.55 + 0.03), thick[i2] * 0.45 + 0.03,
                                 angle=math.degrees(math.atan2(nrm[i2, 1], nrm[i2, 0])), facecolor=P.edge(ftok),
                                 edgecolor="none", zorder=zorder + 0.3))
        # oocyte: the inner region posterior of a gently convex boundary
        ys = np.linspace(cy + b * 0.995, cy - b * 0.995, 60)
        bound = np.c_[xb - 0.12 * b * (1 - ((ys - cy) / b) ** 2), ys]

        def side(mask_fn):
            pts = inner[mask_fn(inner)]
            return pts

        oo_pts = inner[inner[:, 0] >= np.interp(inner[:, 1], ys[::-1], bound[::-1, 0])]
        ang = np.arctan2(oo_pts[:, 1] - cy, oo_pts[:, 0] - cx)
        oo_pts = oo_pts[np.argsort(-ang)]  # from top (dorsal) clockwise round the posterior to the bottom
        oocyte = np.vstack([bound[:1], oo_pts[oo_pts[:, 1] > cy], oo_pts[oo_pts[:, 1] <= cy], bound[-1:]])
        oocyte = np.vstack([oocyte, bound[::-1]])
        # order: dorsal end of boundary -> posterior cortex -> ventral end -> back up the boundary
        top = oo_pts[oo_pts[:, 1] > cy]
        top = top[np.argsort(top[:, 0])]
        bot = oo_pts[oo_pts[:, 1] <= cy]
        bot = bot[np.argsort(-bot[:, 0])]
        oocyte = np.vstack([bound[:1], top, bot, bound[-1:], bound[::-1]])
        self.oocyte_outline = oocyte
        _poly(ax, oocyte, P.fill("cytoplasm"), P.edge("cytoplasm"), lw=LINE * 0.8, zorder=zorder + 1)
        self.clip = PathPatch(Path(np.vstack([oocyte, oocyte[:1]]), closed=True), transform=ax.transData,
                              facecolor="none", edgecolor="none")
        ax.add_patch(self.clip)
        # nurse cells: the anterior region, packed with large cells with polyploid nuclei
        ntok = "animal"
        nurse_c = [(0.3, 0.0), (0.55, 0.45), (0.55, -0.45), (0.78, 0.0), (0.2, 0.58), (0.2, -0.58), (0.05, 0.0)]
        ax_len = xb - (cx - a)
        cells = []
        for k_, (fx, fy) in enumerate(nurse_c):
            px = cx - a + (0.1 + 0.8 * fx) * ax_len
            py = cy + fy * b * 0.95
            r = 0.21 * height if k_ < 4 else 0.17 * height
            cells.append((px, py, r))
        nurse_clip = PathPatch(Path(np.vstack([inner, inner[:1]]), closed=True), transform=ax.transData, facecolor="none",
                               edgecolor="none")
        ax.add_patch(nurse_clip)
        for k_, (px, py, r) in enumerate(cells):
            o = blob((px, py), r, r * 0.92, wobble=0.06, seed=3 + k_, k=7)
            pp = _poly(ax, o, P.fill(ntok), P.edge(ntok), lw=LINE * 0.7, zorder=zorder + 0.6 + 0.01 * k_)
            pp.set_clip_path(nurse_clip)
            nu = Circle((px, py), r * 0.5, facecolor=P.light("nucleolus"), edgecolor=P.edge("nucleolus"), lw=LINE * 0.6,
                        zorder=zorder + 0.7)
            ax.add_patch(nu)
            nu.set_clip_path(nurse_clip)
        self.nurse_cells = cells
        # ring canals on the oocyte boundary
        rc = []
        for fy in (0.45, 0.0, -0.45):
            p = (np.interp(cy + fy * b, ys[::-1], bound[::-1, 0]) - 0.02, cy + fy * b)
            ax.add_patch(Circle(p, 0.07 * height, facecolor="none", edgecolor=P.edge("protein"), lw=LINE * 1.1,
                                zorder=zorder + 3))
            rc.append(p)
        # border cells: a small cluster migrating between the nurse cells towards the oocyte
        bc = (xb - 0.35 * b, cy + 0.12 * b)
        if border_cells:
            for k_, (dx, dy) in enumerate([(0, 0), (0.09, 0.06), (0.08, -0.07), (-0.07, 0.05), (-0.05, -0.07)]):
                ax.add_patch(Circle((bc[0] + dx * height, bc[1] + dy * height), 0.055 * height, facecolor=P.fill(ftok),
                                    edgecolor=P.edge(ftok), lw=0.6, zorder=zorder + 3))
        # oocyte nucleus
        if nucleus == "dorsal":
            nuc = (xb + 0.42 * b, cy + 0.68 * b)
        else:
            nuc = (cx + a * 0.9, cy)
        self.nuc = nuc
        ax.add_patch(Circle(nuc, 0.1 * height, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=LINE * 0.8,
                            zorder=zorder + 4))
        ax.add_patch(Circle(nuc, 0.03 * height, facecolor=P.edge("nucleolus"), edgecolor="none", zorder=zorder + 4.1))
        # stalk cells at both ends
        for sgn in (-1, 1):
            x0 = cx + sgn * (a * (1 + 0.04 * sgn) + 0.045 * height)
            ax.add_patch(Ellipse((x0 + sgn * 0.14 * height, cy), 0.3 * height, 0.12 * height, facecolor=P.fill(ftok),
                                 edgecolor=P.edge(ftok), lw=0.7, zorder=zorder - 0.1))
        post = (cx + a * 1.04 - 0.02 * height, cy)
        self.anchors = {
            "center": tuple(self.c), "oocyte": (xb + (post[0] - xb) * 0.55, cy - 0.15 * b), "nucleus": nuc,
            "anterior": (np.interp(cy, ys[::-1], bound[::-1, 0]) + 0.05, cy - 0.2 * b), "posterior": post,
            "dorsal_anterior": (nuc[0], cy + b * 0.97), "nurse": cells[0][:2], "ring_canal": rc[1],
            "border_cells": bc, "follicle_dorsal": (nuc[0] + 0.25 * b, cy + b + 0.075 * height),
            "follicle_ventral": (nuc[0] + 0.25 * b, cy - b - 0.075 * height),
            "follicle_posterior": (cx + a * 1.04 + 0.07 * height, cy), "follicle_nurse": (cx - 0.5 * a, cy + b + 0.02 * height),
            "stalk": (cx - a - 0.3 * height, cy),
        }

    def _cortex_point(self, deg, depth=0.0):
        """Point on the oocyte cortex at ``deg`` (0 posterior, 90 dorsal, 180 anterior, 270 ventral)."""
        cx, cy = self.c
        th = math.radians(deg)
        # ray from an interior reference point
        ref = np.array([self.xb + 0.6 * (cx + self.a - self.xb), cy])
        d = np.array([math.cos(th), math.sin(th)])
        pts = self.oocyte_outline
        # nearest outline point to the ray
        rel = pts - ref
        proj = rel @ d
        perp = np.abs(rel[:, 0] * d[1] - rel[:, 1] * d[0])
        score = np.where(proj > 0, perp, 1e9)
        p = pts[int(np.argmin(score))]
        return p - d * depth

    def cortex(self, deg0, deg1, token, width=0.22, alpha=1.0, fade=True):
        """Paint a cortical crescent of the oocyte between two angles (localized mRNA or protein)."""
        degs = np.linspace(deg0, deg1, 40)
        outer = np.array([self._cortex_point(d, -0.05) for d in degs])
        w = np.sin(np.linspace(0, np.pi, len(degs))) if fade else np.ones(len(degs))
        w = 0.25 + 0.75 * w
        inner = np.array([self._cortex_point(d, width * wi) for d, wi in zip(degs, w)])
        pts = np.vstack([outer, inner[::-1]])
        p = Polygon(pts, closed=True, facecolor=P.edge(token), edgecolor="none", zorder=self.z + 2,
                    alpha=alpha if alpha < 0.999 else None)
        self.ax.add_patch(p)
        p.set_clip_path(self.clip)
        return tuple(self._cortex_point((deg0 + deg1) / 2, width * 0.5))

    def anterior_cap(self, token, width=0.35):
        """bicoid-like localization: a thin cap along the anterior boundary of the oocyte."""
        cx, cy = self.c
        ys = np.linspace(cy + self.b * 0.8, cy - self.b * 0.8, 40)
        x = self.xb - 0.12 * self.b * (1 - ((ys - cy) / self.b) ** 2)
        w = width * (0.35 + 0.65 * np.cos(np.linspace(-1.2, 1.2, len(ys))))
        pts = np.vstack([np.c_[x + 0.04, ys], np.c_[x + w, ys][::-1]])
        p = Polygon(pts, closed=True, facecolor=P.edge(token), edgecolor="none", zorder=self.z + 2)
        self.ax.add_patch(p)
        p.set_clip_path(self.clip)
        return (float(x[len(x) // 2] + width * 0.5), cy)

    def microtubules(self, token="neutral", n=9):
        """A weakly polarized microtubule network: minus ends at the anterior and lateral cortex, plus ends
        biased towards the posterior (drawn as faint curves, the plus ends marked with a small bar)."""
        cx, cy = self.c
        col = P.mix(P.edge(token), P.surface(), 0.25)
        for k in range(n):
            f = (k + 0.5) / n
            y0 = cy + (f - 0.5) * 1.5 * self.b
            p0 = np.array([self.xb + 0.05, y0])
            p1 = np.array([self.xb + (cx + self.a - self.xb) * (0.55 + 0.25 * (1 - abs(f - 0.5) * 2)),
                           cy + (f - 0.5) * 0.7 * self.b])
            mid = (p0 + p1) / 2 + np.array([0, 0.08 * self.b * (1 if f > 0.5 else -1)])
            tt = np.linspace(0, 1, 40)[:, None]
            pts = (1 - tt) ** 2 * p0 + 2 * (1 - tt) * tt * mid + tt ** 2 * p1
            ln, = self.ax.plot(pts[:, 0], pts[:, 1], color=col, lw=0.8, zorder=self.z + 1.5)
            ln.set_clip_path(self.clip)
        return (self.xb + 0.3 * (cx + self.a - self.xb), cy)


class FlyCrossSection:
    """Transverse section of a Drosophila syncytial or cellular blastoderm: dorsal up, ventral down.

    A ring of peripheral nuclei surrounds the yolk; outside it lie the plasma membrane, the perivitelline space and
    the vitelline membrane. ``values(s)`` (s = 0 at the ventral midline, 1 at the dorsal midline, symmetric on both
    sides) colours the nuclei from pale to ``token`` (for a nuclear gradient such as Dorsal). ``domain`` draws
    expression domains as bands just outside the embryo.

    ``anchors``: center, ventral, dorsal, left, right, yolk, perivitelline, vitelline, nucleus (a ventral nucleus).
    """

    def __init__(self, ax, center, r=2.5, n=40, values=None, token="dna", yolk=True, cells=False, zorder=5):
        self.ax, self.c, self.r, self.z, self.n = ax, np.array(center, float), r, zorder, n
        cx, cy = center
        # vitelline membrane and perivitelline space
        ax.add_patch(Circle(center, r * 1.09, facecolor=P.fill("extracellular"), edgecolor=P.edge("neutral"), lw=LINE * 1.1,
                            zorder=zorder))
        ax.add_patch(Circle(center, r, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("membrane"), lw=LINE * 0.9,
                            zorder=zorder + 0.1))
        if yolk:
            ax.add_patch(Circle(center, r * 0.72, facecolor=_wash("bone", 0.25), edgecolor="none", zorder=zorder + 0.2))
            rng = np.random.default_rng(4)
            for _ in range(70):
                rr = r * 0.66 * math.sqrt(rng.random())
                th = rng.random() * 2 * np.pi
                ax.add_patch(Circle((cx + rr * math.cos(th), cy + rr * math.sin(th)), r * (0.025 + 0.02 * rng.random()),
                                    facecolor=P.fill("bone"), edgecolor=P.edge("bone"), lw=0.3, zorder=zorder + 0.3))
        self.nuclei = []
        for k in range(n):
            th = -np.pi / 2 + (k + 0.5) * 2 * np.pi / n  # start beside the ventral midline
            s = abs(((th + np.pi / 2 + np.pi) % (2 * np.pi)) - np.pi) / np.pi  # 0 ventral, 1 dorsal
            p = (cx + 0.86 * r * math.cos(th), cy + 0.86 * r * math.sin(th))
            v = float(np.clip(values(s), 0, 1)) if values else 0.0
            face = P.mix(P.light("nucleus"), P.edge(token), v) if values else P.fill("nucleus")
            ax.add_patch(Ellipse(p, 0.16 * r, 0.1 * r, angle=math.degrees(th) + 90 + 90, facecolor=face,
                                 edgecolor=P.edge("nucleus"), lw=0.6, zorder=zorder + 1))
            self.nuclei.append((p, s))
            if cells:
                a0 = th - np.pi / n
                q0 = (cx + 0.74 * r * math.cos(a0), cy + 0.74 * r * math.sin(a0))
                q1 = (cx + r * math.cos(a0), cy + r * math.sin(a0))
                ax.plot([q0[0], q1[0]], [q0[1], q1[1]], color=P.edge("membrane"), lw=0.5, zorder=zorder + 0.9)
        if cells:
            ax.add_patch(Circle(center, 0.74 * r, facecolor="none", edgecolor=P.edge("membrane"), lw=0.6, zorder=zorder + 0.9))
        self.anchors = {
            "center": tuple(center), "ventral": (cx, cy - r * 1.09), "dorsal": (cx, cy + r * 1.09),
            "left": (cx - r * 1.09, cy), "right": (cx + r * 1.09, cy), "yolk": (cx, cy + 0.2 * r),
            "perivitelline": (cx + r * 1.045 * 0.7071, cy - r * 1.045 * 0.7071),
            "vitelline": (cx - r * 1.09 * 0.7071, cy - r * 1.09 * 0.7071), "nucleus": (cx, cy - 0.86 * r),
        }

    def point(self, s, side=1, radius=1.0):
        """Point at fraction ``s`` from the ventral (0) to the dorsal (1) midline, on the right (side=1) or left."""
        th = -np.pi / 2 + side * s * np.pi
        return (self.c[0] + radius * self.r * math.cos(th), self.c[1] + radius * self.r * math.sin(th))

    def domain(self, s0, s1, token, ring=0, width=0.11, both=True):
        """An expression domain from s0 to s1 drawn as a band outside the embryo (``ring`` stacks bands outward)."""
        r0 = self.r * (1.14 + ring * (width + 0.03))
        for side in ((1, -1) if both else (1,)):
            th = -np.pi / 2 + side * np.linspace(s0, s1, 60) * np.pi
            outer = np.c_[self.c[0] + (r0 + width * self.r) * np.cos(th), self.c[1] + (r0 + width * self.r) * np.sin(th)]
            inner = np.c_[self.c[0] + r0 * np.cos(th), self.c[1] + r0 * np.sin(th)]
            _poly(self.ax, np.vstack([outer, inner[::-1]]), P.fill(token), P.edge(token), lw=0.6, zorder=self.z + 2)
        return self.point((s0 + s1) / 2, 1, (r0 + width * self.r / 2) / self.r)


# ---------------------------------------------------------------------------------------------------------------
# amphibians


def amphibian(ax, center, r=2.0, stage="blastula", dorsal="right", rotation=0.0, sperm=True, regions=True, zorder=5):
    """An amphibian (Xenopus) embryo, animal pole up.

    stage "egg": a fertilized egg, pigmented animal hemisphere and pale vegetal hemisphere, the sperm entry point on
    the future ventral side; ``rotation`` (degrees, about 30 in Xenopus) draws the cortex displaced relative to the
    core, the cortical rotation that moves vegetal dorsal determinants to the side opposite sperm entry.
    stage "blastula": a section of the late blastula: animal cap (prospective ectoderm), marginal zone (mesoderm)
    and vegetal mass (endoderm) in germ-layer colours around an animal blastocoel; with ``regions`` the Nieuwkoop
    centre (dorsal vegetal cells) and the organizer (dorsal marginal zone) are outlined.
    stage "gastrula": a sagittal section of the early gastrula with bottle cells and the dorsal blastopore lip,
    involuting mesoderm and the forming archenteron.

    Returns anchors: center, animal, vegetal, dorsal, ventral, and per stage sperm_entry, cortex, core (egg);
    blastocoel, animal_cap, marginal_dorsal, marginal_ventral, vegetal, nieuwkoop, organizer (blastula);
    dorsal_lip, archenteron, blastocoel, involuting, bottle_cells, ectoderm, endoderm (gastrula).
    """
    cx, cy = center
    sd = 1 if dorsal == "right" else -1
    A = {"center": (cx, cy), "animal": (cx, cy + r), "vegetal": (cx, cy - r), "dorsal": (cx + sd * r, cy),
         "ventral": (cx - sd * r, cy)}
    if stage == "egg":
        # vitelline envelope
        ax.add_patch(Circle(center, r * 1.08, facecolor="none", edgecolor=P.edge("neutral"), lw=LINE * 0.8, zorder=zorder))
        ax.add_patch(Circle(center, r, facecolor=P.fill("bone"), edgecolor=P.edge("bone"), lw=LINE, zorder=zorder + 0.1))
        rot = math.radians(rotation) * sd
        # pigmented animal cortex: a cap above the equator, displaced by the cortical rotation
        th = np.linspace(-0.05 * np.pi, 1.05 * np.pi, 120) + rot
        cap = np.c_[cx + r * np.cos(th), cy + r * np.sin(th)]
        chord = np.c_[np.linspace(cap[-1, 0], cap[0, 0], 30), np.linspace(cap[-1, 1], cap[0, 1], 30)]
        mid = (cap[0] + cap[-1]) / 2
        bow = np.array([math.sin(rot), -math.cos(rot)]) * 0.16 * r
        chord = chord + bow * np.sin(np.linspace(0, np.pi, 30))[:, None]
        _poly(ax, np.vstack([cap, chord]), _pigment(), P.edge("animal"), lw=LINE * 0.7, zorder=zorder + 0.2)
        # grey crescent: the zone of lighter pigment opposite sperm entry, revealed by the rotation
        if rotation:
            th2 = np.linspace(-0.05 * np.pi + rot - sd * 0.0, -0.05 * np.pi + rot + sd * 0.0, 2)
            g0, g1 = (-0.06 * np.pi, -0.06 * np.pi + rot) if sd > 0 else (np.pi + 0.06 * np.pi + rot, np.pi + 0.06 * np.pi)
            tt = np.linspace(min(g0, g1), max(g0, g1), 40)
            outer = np.c_[cx + r * np.cos(tt), cy + r * np.sin(tt)]
            inner = np.c_[cx + 0.86 * r * np.cos(tt), cy + 0.86 * r * np.sin(tt)]
            _poly(ax, np.vstack([outer, inner[::-1]]), P.mix(P.fill("animal"), P.fill("neutral"), 0.5), P.edge("neutral"),
                  lw=0.5, zorder=zorder + 0.25)
            A["grey_crescent"] = (cx + sd * 0.93 * r * math.cos(0.12), cy + 0.93 * r * math.sin(-0.12))
        # core cytoplasm outline (the inner, non-rotating part)
        ax.add_patch(Circle(center, r * 0.86, facecolor="none", edgecolor=P.edge("bone"), lw=0.6, ls=(0, (2, 2)),
                            zorder=zorder + 0.3))
        # female pronucleus near the animal pole
        ax.add_patch(Circle((cx, cy + 0.55 * r), 0.09 * r, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"),
                            lw=0.7, zorder=zorder + 0.5))
        if sperm:
            se = (cx - sd * r * math.cos(math.radians(35)), cy + r * math.sin(math.radians(35)))
            ax.add_patch(Circle(se, 0.07 * r, facecolor=P.edge("drug"), edgecolor="none", zorder=zorder + 0.6))
            A["sperm_entry"] = se
        A["cortex"] = (cx + sd * r * 0.93, cy - 0.25 * r)
        A["core"] = (cx, cy - 0.3 * r)
        return A
    if stage == "blastula":
        ax.add_patch(Circle(center, r, facecolor=P.fill(GERM["endoderm"]), edgecolor=P.edge(GERM["endoderm"]), lw=LINE,
                            zorder=zorder))
        # marginal zone band and animal cap (as annular sectors above the vegetal mass)
        def sector(t0, t1, r0, r1, tok, z):
            tt = np.linspace(t0, t1, 80)
            outer = np.c_[cx + r1 * np.cos(tt), cy + r1 * np.sin(tt)]
            inner = np.c_[cx + r0 * np.cos(tt), cy + r0 * np.sin(tt)]
            _poly(ax, np.vstack([outer, inner[::-1]]), P.fill(tok), P.edge(tok), lw=LINE * 0.7, zorder=z)
        # animal cap: top of the sphere; marginal zone: a ring between ~5 and ~35 degrees above the equator
        sector(math.radians(35), math.radians(145), 0.0, r, GERM["ectoderm"], zorder + 0.2)
        sector(math.radians(-8), math.radians(35), 0.0, r, GERM["mesoderm"], zorder + 0.2)
        sector(math.radians(145), math.radians(188), 0.0, r, GERM["mesoderm"], zorder + 0.2)
        # blastocoel: an off-centre cavity in the animal half
        bl = blob((cx, cy + 0.32 * r), 0.55 * r, 0.36 * r, wobble=0.04, seed=2, k=8)
        _poly(ax, bl, P.fill("vacuole"), P.edge("vacuole"), lw=LINE * 0.7, zorder=zorder + 0.5)
        ax.add_patch(Circle(center, r, facecolor="none", edgecolor=P.ink(), lw=LINE * 0.9, zorder=zorder + 0.6))
        A.update({"blastocoel": (cx, cy + 0.32 * r), "animal_cap": (cx, cy + 0.85 * r),
                  "marginal_dorsal": (cx + sd * 0.82 * r * math.cos(math.radians(14)), cy + 0.82 * r * math.sin(math.radians(14))),
                  "marginal_ventral": (cx - sd * 0.82 * r * math.cos(math.radians(14)), cy + 0.82 * r * math.sin(math.radians(14))),
                  "vegetal": (cx, cy - 0.55 * r)})
        if regions:
            # Nieuwkoop centre: dorsal vegetal cells; organizer: dorsal marginal zone just above it
            nk = blob((cx + sd * 0.55 * r, cy - 0.32 * r), 0.3 * r, 0.22 * r, wobble=0.03, seed=5, k=7, angle=sd * 0.5)
            _poly(ax, nk, P.fill("drug"), P.edge("drug"), lw=LINE * 0.8, zorder=zorder + 0.8)
            tt = np.linspace(math.radians(-8), math.radians(32), 30)
            if sd < 0:
                tt = np.pi - tt
            outer = np.c_[cx + 1.0 * r * np.cos(tt), cy + 1.0 * r * np.sin(tt)]
            inner = np.c_[cx + 0.66 * r * np.cos(tt), cy + 0.66 * r * np.sin(tt)]
            _poly(ax, np.vstack([outer, inner[::-1]]), P.fill("positive"), P.edge("positive"), lw=LINE * 0.8,
                  zorder=zorder + 0.85)
            A["nieuwkoop"] = (cx + sd * 0.55 * r, cy - 0.32 * r)
            A["organizer"] = (cx + sd * 0.86 * r * math.cos(math.radians(12)), cy + 0.86 * r * math.sin(math.radians(12)))
        return A
    if stage == "gastrula":
        from .core import polyline

        def ang(deg):
            # angle measured on the dorsal side (mirrored when dorsal is on the left)
            t = math.radians(deg)
            return t if sd > 0 else np.pi - t

        def arc_band(d0, d1, r0, r1, tok, z, n=80):
            tt = np.array([ang(d) for d in np.linspace(d0, d1, n)])
            outer = np.c_[cx + r1 * np.cos(tt), cy + r1 * np.sin(tt)]
            inner = np.c_[cx + r0 * np.cos(tt), cy + r0 * np.sin(tt)]
            _poly(ax, np.vstack([outer, inner[::-1]]), P.fill(tok), P.edge(tok), lw=LINE * 0.7, zorder=z)

        ax.add_patch(Circle(center, r, facecolor=P.fill(GERM["endoderm"]), edgecolor=P.edge(GERM["endoderm"]), lw=LINE,
                            zorder=zorder))
        lip_deg = -38
        # ectoderm: the outer layer of the animal half, down to the lip dorsally and to the ventral marginal zone
        arc_band(lip_deg + 10, 205, 0.8 * r, r, GERM["ectoderm"], zorder + 0.2)
        # ventral marginal zone mesoderm (not yet involuted), on the surface just above the ventral equator
        arc_band(198, 222, 0.8 * r, r, GERM["mesoderm"], zorder + 0.25)
        # involuted dorsal mesoderm: a layer inside the ectoderm, from the lip up along the blastocoel roof
        arc_band(lip_deg + 4, 62, 0.64 * r, 0.8 * r, GERM["mesoderm"], zorder + 0.3)
        # archenteron: a lumen inside the involuted layer, opening at the blastopore
        tt = np.array([ang(d) for d in np.linspace(lip_deg + 2, 38, 60)])
        wv = np.linspace(0.07, 0.025, len(tt)) * r
        outer = np.c_[cx + (0.63 * r) * np.cos(tt), cy + (0.63 * r) * np.sin(tt)]
        inner = np.c_[cx + (0.63 * r - wv) * np.cos(tt), cy + (0.63 * r - wv) * np.sin(tt)]
        _poly(ax, np.vstack([outer, inner[::-1]]), P.fill("vacuole"), P.edge("vacuole"), lw=0.7, zorder=zorder + 0.35)
        # blastocoel, displaced ventrally and towards the animal pole
        bl = blob((cx - sd * 0.18 * r, cy + 0.28 * r), 0.45 * r, 0.36 * r, wobble=0.04, seed=3, k=8)
        _poly(ax, bl, P.fill("vacuole"), P.edge("vacuole"), lw=LINE * 0.7, zorder=zorder + 0.4)
        # blastopore groove and bottle cells at the dorsal lip
        t_l = ang(lip_deg)
        lip = np.array([cx + r * math.cos(t_l), cy + r * math.sin(t_l)])
        inward = -np.array([math.cos(t_l), math.sin(t_l)])
        tang = np.array([-inward[1], inward[0]])
        for k in range(4):
            p = lip + inward * (0.06 + 0.02 * k) * r + tang * (k - 1.5) * 0.045 * r
            ax.add_patch(Ellipse(p, 0.03 * r, 0.13 * r, angle=math.degrees(math.atan2(inward[1], inward[0])) + 90,
                                 facecolor=_pigment(), edgecolor="none", zorder=zorder + 0.9))
        ax.add_patch(Circle(center, r, facecolor="none", edgecolor=P.ink(), lw=LINE * 0.9, zorder=zorder + 1))
        t_m = ang(20)
        t_a = ang(0)
        A.update({"dorsal_lip": tuple(lip), "bottle_cells": tuple(lip + inward * 0.1 * r),
                  "archenteron": (cx + 0.6 * r * math.cos(t_a), cy + 0.6 * r * math.sin(t_a)),
                  "blastocoel": (cx - sd * 0.18 * r, cy + 0.28 * r),
                  "involuting": (cx + 0.72 * r * math.cos(t_m), cy + 0.72 * r * math.sin(t_m)),
                  "ectoderm": (cx - sd * 0.2 * r, cy + 0.9 * r), "endoderm": (cx - sd * 0.1 * r, cy - 0.5 * r),
                  "ventral_mesoderm": (cx + 0.9 * r * math.cos(ang(210)), cy + 0.9 * r * math.sin(ang(210)))})
        return A
    raise ValueError(f"unknown stage {stage!r}")


# ---------------------------------------------------------------------------------------------------------------
# chick and mouse


def chick_blastoderm(ax, center, r=2.5, stage="streak", streak=0.55, zorder=5):
    """The chick blastoderm in dorsal view, anterior up, posterior down.

    The area opaca (outer ring over the yolk) surrounds the translucent area pellucida. stage "prestreak": the
    posterior marginal zone (PMZ) and Koller's sickle at the posterior edge; stage "streak": the primitive streak
    extending anteriorly from the posterior edge to ``streak`` × the diameter, with Hensen's node at its tip.
    Returns anchors: center, opaca, pellucida, anterior, posterior, pmz, sickle, streak, node, hypoblast.
    """
    cx, cy = center
    ax.add_patch(Ellipse(center, 2.3 * r, 2.3 * r * 0.95, facecolor=_wash("bone", 0.1), edgecolor=P.edge("bone"), lw=LINE,
                         zorder=zorder))
    ax.add_patch(Ellipse(center, 2 * r * 0.72, 2 * r * 0.82, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("cytoplasm"),
                         lw=LINE * 0.8, zorder=zorder + 0.1))
    A = {"center": (cx, cy), "opaca": (cx + 1.0 * r, cy + 0.3 * r), "pellucida": (cx - 0.35 * r, cy + 0.35 * r),
         "anterior": (cx, cy + 0.82 * r), "posterior": (cx, cy - 0.82 * r)}
    # posterior marginal zone: a crescent at the posterior border between pellucida and opaca
    tt = np.linspace(math.radians(240), math.radians(300), 40)
    outer = np.c_[cx + 0.92 * r * np.cos(tt), cy + 0.98 * r * np.sin(tt)]
    inner = np.c_[cx + 0.72 * r * np.cos(tt), cy + 0.82 * r * np.sin(tt)]
    _poly(ax, np.vstack([outer, inner[::-1]]), P.fill("drug"), P.edge("drug"), lw=0.7, zorder=zorder + 0.3)
    A["pmz"] = (cx + 0.82 * r * math.cos(math.radians(255)), cy + 0.9 * r * math.sin(math.radians(255)))
    # Koller's sickle just inside it
    tt = np.linspace(math.radians(245), math.radians(295), 40)
    sk = np.c_[cx + 0.69 * r * np.cos(tt), cy + 0.79 * r * np.sin(tt)]
    ax.plot(sk[:, 0], sk[:, 1], color=P.edge("protein"), lw=LINE * 2.0, solid_capstyle="round", zorder=zorder + 0.4)
    A["sickle"] = tuple(sk[len(sk) // 2])
    if stage == "streak":
        y0, y1 = cy - 0.78 * r, cy - 0.78 * r + streak * 2 * r * 0.82
        ys = np.linspace(y0, y1, 40)
        w = 0.075 * r * (0.6 + 0.4 * (ys - y0) / (y1 - y0))
        _poly(ax, np.vstack([np.c_[cx - w, ys], np.c_[cx + w, ys][::-1]]), P.fill(GERM["mesoderm"]),
              P.edge(GERM["mesoderm"]), lw=0.8, zorder=zorder + 0.6)
        ax.plot([cx, cx], [y0 + 0.05 * r, y1 - 0.08 * r], color=P.edge(GERM["mesoderm"]), lw=0.7, zorder=zorder + 0.7)
        ax.add_patch(Circle((cx, y1), 0.12 * r, facecolor=P.fill("positive"), edgecolor=P.edge("positive"), lw=LINE * 0.8,
                            zorder=zorder + 0.8))
        A["streak"] = (cx, (y0 + y1) / 2)
        A["node"] = (cx, y1)
    A["hypoblast"] = (cx + 0.3 * r, cy + 0.45 * r)
    return A


def egg_cylinder(ax, center, w=1.3, h=3.0, streak=True, ave="anterior", node=True, zorder=5):
    """The mouse egg cylinder at about E6.5 in sagittal section: anterior left, posterior right, distal down.

    The cup-shaped epiblast (prospective ectoderm, blue) lines the proamniotic cavity in the distal half; the
    extra-embryonic ectoderm (ExE) forms the proximal half; visceral endoderm covers both. ``ave`` places the
    anterior visceral endoderm: "distal" (DVE, about E5.5) or "anterior" (AVE, after its migration). With ``streak``
    the primitive streak forms in the posterior epiblast (mesoderm, red) and, with ``node``, ends at the distal tip.
    Returns anchors: center, epiblast, exe, cavity, visceral_endoderm, ave, streak, node, anterior, posterior,
    proximal, distal.
    """
    cx, cy = center
    t = np.linspace(0, 2 * np.pi, 240)
    # visceral endoderm outline: a cylinder with a rounded distal tip
    def cyl(ww, hh, dy=0.0):
        pts = []
        for tt in t:
            x = ww * math.cos(tt)
            y = hh * math.sin(tt)
            if y > 0:
                y = y * 0.4 + hh * 0.6 * (1 if math.sin(tt) > 0 else 0)  # flatter, squarer top half
            pts.append((cx + x, cy + y + dy))
        return np.array(pts)
    ve = np.c_[cx + w * np.cos(t), cy + h / 2 * np.sin(t)]
    _poly(ax, ve, P.fill(GERM["endoderm"]), P.edge(GERM["endoderm"]), lw=LINE * 0.8, zorder=zorder)
    inner = np.c_[cx + (w - 0.13) * np.cos(t), cy + (h / 2 - 0.13) * np.sin(t)]
    # ExE: proximal half (upper)
    up = inner[inner[:, 1] >= cy]
    _poly(ax, np.vstack([up, [[cx - w + 0.13, cy]]]), P.fill("receptor"), P.edge("receptor"), lw=LINE * 0.7,
          zorder=zorder + 0.1)
    lo = inner[inner[:, 1] <= cy]
    _poly(ax, np.vstack([lo, [[cx + w - 0.13, cy]]]), P.fill(GERM["ectoderm"]), P.edge(GERM["ectoderm"]), lw=LINE * 0.7,
          zorder=zorder + 0.1)
    # proamniotic cavity
    cav = np.c_[cx + (w - 0.42) * np.cos(t), cy - 0.05 + (h / 2 - 0.45) * np.sin(t)]
    _poly(ax, cav, P.fill("vacuole"), P.edge("vacuole"), lw=0.7, zorder=zorder + 0.2)
    A = {"center": (cx, cy), "epiblast": (cx - w + 0.27, cy - 0.45 * h / 2), "exe": (cx - w + 0.27, cy + 0.5 * h / 2),
         "cavity": (cx, cy), "visceral_endoderm": (cx - w - 0.0, cy + 0.15), "anterior": (cx - w, cy),
         "posterior": (cx + w, cy), "proximal": (cx, cy + h / 2), "distal": (cx, cy - h / 2)}
    # AVE: thickened visceral endoderm
    if ave:
        th = (np.linspace(1.42 * np.pi, 1.58 * np.pi, 30) if ave == "distal" else np.linspace(1.05 * np.pi, 1.3 * np.pi, 30))
        outer = np.c_[cx + (w + 0.08) * np.cos(th), cy + (h / 2 + 0.08) * np.sin(th)]
        inn = np.c_[cx + (w - 0.12) * np.cos(th), cy + (h / 2 - 0.12) * np.sin(th)]
        _poly(ax, np.vstack([outer, inn[::-1]]), P.fill("positive"), P.edge("positive"), lw=0.8, zorder=zorder + 0.4)
        m = th[len(th) // 2]
        A["ave"] = (cx + (w + 0.05) * math.cos(m), cy + (h / 2 + 0.05) * math.sin(m))
    if streak:
        th = np.linspace(1.62 * np.pi, 2.0 * np.pi, 30)
        outer = np.c_[cx + (w - 0.1) * np.cos(th), cy + (h / 2 - 0.1) * np.sin(th)]
        inn = np.c_[cx + (w - 0.45) * np.cos(th), cy + (h / 2 - 0.45) * np.sin(th)]
        _poly(ax, np.vstack([outer, inn[::-1]]), P.fill(GERM["mesoderm"]), P.edge(GERM["mesoderm"]), lw=0.8,
              zorder=zorder + 0.3)
        A["streak"] = (cx + (w - 0.27) * math.cos(1.8 * np.pi), cy + (h / 2 - 0.27) * math.sin(1.8 * np.pi))
        if node:
            p = (cx + 0.12, cy - h / 2 + 0.22)
            ax.add_patch(Circle(p, 0.17, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.8, zorder=zorder + 0.5))
            A["node"] = p
    return A


def node_pit(ax, center, width=4.0, n=7, phase=0.0, flow=True, zorder=5):
    """The mouse node in ventral view: an oval pit of ciliated cells (anterior up).

    Seen from the ventral side the embryo's left lies on the viewer's right. Each pit cell carries one motile
    cilium, drawn as a short stalk with an ellipse for the clockwise rotation (viewed from the cilium tip); the
    posterior tilt (out of the page) makes the cone an ellipse. ``flow`` draws the leftward flow across the pit.
    Returns anchors: center, left (embryo's left, viewer's right), right, anterior, posterior, cilium (one cilium),
    crown (a perinodal crown cell).
    """
    cx, cy = center
    rx, ry = width / 2, width / 2 * 0.62
    # crown cells around the pit
    ax.add_patch(Ellipse(center, 2 * rx + 0.9, 2 * ry + 0.9, facecolor=P.fill("mg"), edgecolor=P.edge("mg"), lw=LINE * 0.8,
                         zorder=zorder))
    for k in range(18):
        th = 2 * np.pi * k / 18
        p0 = (cx + (rx + 0.02) * math.cos(th), cy + (ry + 0.02) * math.sin(th))
        p1 = (cx + (rx + 0.45) * math.cos(th), cy + (ry + 0.45) * math.sin(th))
        ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=P.edge("mg"), lw=0.5, zorder=zorder + 0.1)
    ax.add_patch(Ellipse(center, 2 * rx, 2 * ry, facecolor=P.fill("extracellular"), edgecolor=P.edge("channel"), lw=LINE,
                         zorder=zorder + 0.2))
    # pit cells: a hexagonal-ish array inside the pit, each with a cilium
    rng = np.random.default_rng(11)
    cil = []
    rows = 3
    for j in range(rows):
        y = cy + (j - (rows - 1) / 2) * ry * 0.58
        m = n - abs(j - (rows - 1) // 2) * 2
        for i in range(m):
            x = cx + (i - (m - 1) / 2) * (2 * rx * 0.82 / max(n - 1, 1))
            if ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 > 0.82:
                continue
            ax.add_patch(Ellipse((x, y), 0.42, 0.34, facecolor=P.fill("channel"), edgecolor=P.edge("channel"), lw=0.5,
                                 zorder=zorder + 0.3, alpha=0.55))
            # rotation ellipse (cone projected; posterior tilt shifts it down) and the cilium
            e = Ellipse((x, y - 0.06), 0.36, 0.22, facecolor="none", edgecolor=P.edge("dna"), lw=0.7, zorder=zorder + 0.5)
            ax.add_patch(e)
            ph = phase + rng.uniform(0, 2 * np.pi)
            tip = (x + 0.18 * math.cos(ph), y - 0.06 + 0.11 * math.sin(ph))
            ax.plot([x, tip[0]], [y, tip[1]], color=P.ink(), lw=1.0, zorder=zorder + 0.6)
            # arrowhead on the ellipse showing clockwise sense (viewed from the tip = ventral view)
            a0 = math.radians(80)
            p = np.array([x + 0.18 * math.cos(a0), y - 0.06 + 0.11 * math.sin(a0)])
            d = np.array([math.sin(a0) * 0.18, -math.cos(a0) * 0.11])
            d /= np.linalg.norm(d)
            nn = np.array([-d[1], d[0]])
            ax.add_patch(Polygon([p + d * 0.07, p - d * 0.03 + nn * 0.04, p - d * 0.03 - nn * 0.04], closed=True,
                                 facecolor=P.edge("dna"), edgecolor="none", zorder=zorder + 0.6))
            cil.append((x, y))
    if flow:
        for dy in (-0.35, 0.35):
            arrow(ax, (cx - rx * 0.55, cy + dy * ry), (cx + rx * 0.62, cy + dy * ry), kind="process",
                  color=P.edge("positive"), lw=LINE * 1.3, head=0.25, zorder=zorder + 1)
    return {"center": (cx, cy), "left": (cx + rx + 0.45, cy), "right": (cx - rx - 0.45, cy), "anterior": (cx, cy + ry + 0.45),
            "posterior": (cx, cy - ry - 0.45), "cilium": cil[len(cil) // 2] if cil else (cx, cy),
            "crown": (cx + 0.75 * rx, cy + ry + 0.22)}


def cilium_cone(ax, base, length=2.0, tilt=35.0, cone=30.0, phases=8, wall=3.0, zorder=5):
    """Side view of one node cilium over the cell surface (the wall), posterior to the right.

    The cilium rotates on a cone of half-angle ``cone`` whose axis is tilted posteriorly by ``tilt`` (degrees from
    the vertical). Drawn: the wall, the axis, the cone outline (an ellipse traced by the tip) and the cilium at
    ``phases`` positions, darker in the half of the cycle far from the wall. Returns anchors: base, tip_high (tip
    farthest from the wall), tip_low, axis_end, wall_left, wall_right.
    """
    bx, by = base
    ax.plot([bx - wall, bx + wall], [by, by], color=P.edge("channel"), lw=LINE * 1.6, zorder=zorder, solid_capstyle="butt")
    for k in range(13):
        x = bx - wall + k * 2 * wall / 12
        ax.plot([x, x - 0.18], [by, by - 0.18], color=P.edge("channel"), lw=0.6, zorder=zorder)
    T, C = math.radians(tilt), math.radians(cone)
    nvec = np.array([math.sin(T), 0.0, math.cos(T)])  # x posterior, y out of page (left-right), z up
    e1 = np.array([0.0, 1.0, 0.0])
    e2 = np.cross(nvec, e1)
    tips = []
    for ph in np.linspace(0, 2 * np.pi, 120):
        v = length * (math.cos(C) * nvec + math.sin(C) * (math.cos(ph) * e1 + math.sin(ph) * e2))
        tips.append(v)
    tips = np.array(tips)
    pts2 = np.c_[bx + tips[:, 0], by + tips[:, 2]]
    ax.plot(pts2[:, 0], pts2[:, 1], color=P.muted(), lw=0.8, ls=(0, (3, 2)), zorder=zorder + 0.2)
    ax.plot([bx, bx + length * 1.15 * nvec[0]], [by, by + length * 1.15 * nvec[2]], color=P.muted(), lw=0.8,
            ls=(0, (1, 2)), zorder=zorder + 0.2)
    for k in range(phases):
        ph = 2 * np.pi * k / phases
        v = length * (math.cos(C) * nvec + math.sin(C) * (math.cos(ph) * e1 + math.sin(ph) * e2))
        far = v[2] > length * math.cos(C) * math.cos(T)
        col = P.edge("dna") if far else P.mix(P.edge("dna"), P.surface(), 0.55)
        s = np.linspace(0, 1, 20)
        curve = np.c_[bx + s * v[0], by + s * v[2]]
        ax.plot(curve[:, 0], curve[:, 1], color=col, lw=1.6 if far else 1.1, zorder=zorder + 0.4 + (0.1 if far else 0))
    ax.add_patch(Circle(base, 0.08, facecolor=P.ink(), edgecolor="none", zorder=zorder + 0.6))
    hi = pts2[int(np.argmax(pts2[:, 1]))]
    lo = pts2[int(np.argmin(pts2[:, 1]))]
    return {"base": base, "tip_high": tuple(hi), "tip_low": tuple(lo),
            "axis_end": (bx + length * 1.15 * nvec[0], by + length * 1.15 * nvec[2]), "wall_left": (bx - wall, by),
            "wall_right": (bx + wall, by)}


__all__ = ["EggChamber", "FlyCrossSection", "amphibian", "chick_blastoderm", "egg_cylinder", "node_pit", "cilium_cone"]
