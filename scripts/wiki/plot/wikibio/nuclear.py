"""The cell nucleus (7.3.16-7.3.17): the nuclear envelope in section, nuclear pore complexes, the lamina and
LINC complexes, transport receptors and Ran, chromosome territories, the nucleolus and special chromosomes.

    from wikibio import nuclear as N
    env = N.envelope(ax, 0, 12, 4, pores=[4, 8], er=1.5)     cross-section strip: cytoplasm above, nucleus below;
                                                               ONM with ribosomes, perinuclear space, INM, lamina
    N.pore(ax, 6, 4, gap=0.6, width=1.6)                      side view of one NPC (rings, filaments, basket, FG mesh)
    N.pore_top(ax, (3, 3), 1.0)                               face view: eightfold spokes around the central channel
    N.lamina(ax, 0, 12, 3.6, depth=0.3)                       lamin meshwork strip under the inner membrane
    N.linc(ax, 2.0, env)                                      SUN-KASH bridge from the lamina to an actin filament
    N.karyopherin(ax, (2, 6), 0.45, kind="importin")         a HEAT-repeat arch (importin beta, exportin)
    N.ran(ax, (3, 6), "GTP")                                   Ran with its nucleotide
    N.cargo(ax, (2, 6), 0.3, signal="NLS")                    a cargo protein with its signal
    N.territories(ax, (6, 4), 3, 2.4, n=12)                  interphase nucleus divided into chromosome territories
    N.nucleolus(ax, (6, 4), 1.2, units=4)                     fibrillar centres, dense fibrillar component, granular component
    N.polytene(ax, 1, 11, 3, 0.7, puff=0.6)                  banded polytene chromosome with a puff
    N.lampbrush(ax, 1, 11, 3, loops=7)                        lampbrush chromosome axis with paired lateral loops

Colours are palette tokens chosen once in ``TOKENS``; a script can pass another token to any function.
Every function is deterministic and returns anchors (points or dicts of points) for arrows and callouts.
Sections are drawn with the cytoplasm above and the nucleoplasm below unless stated otherwise.
"""

import math
import zlib

import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch, PathPatch, Polygon, Rectangle
from matplotlib.path import Path

from . import palette as P
from .core import LINE, blob, label, polyline, smooth_closed
from .structures import ribosome

MT = 0.1  # membrane band thickness (canvas units)

TOKENS = {
    "membrane": "membrane",
    "lumen": "er",
    "nucleoplasm": "nucleus",
    "cytoplasm": "cytoplasm",
    "nup": "enzyme",
    "fg": "positive",
    "lamina": "drug",
    "sun": "receptor",
    "kash": "channel",
    "actin": "muscle",
    "importin": "protein",
    "importin_a": "metabolite",
    "exportin": "channel",
    "cargo": "highlight",
    "ran_gtp": "atp",
    "ran_gdp": "neutral",
    "ribosome": "rrna",
    "chromatin": "chromatin",
    "fc": "dna2",
    "dfc": "rrna",
    "gc": "nucleolus",
}

# territory colours (one per chromosome; light fills keep a nucleus readable)
TERRITORY_TOKENS = ["dna", "receptor", "enzyme", "antibody", "positive", "drug", "metabolite", "carbohydrate",
                    "channel", "lipid_head", "k", "muscle", "cl", "lysosome", "golgi", "na"]


def tok(name):
    """The palette token used for a nuclear object (``tok("lamina")``); unknown names pass through."""
    return TOKENS.get(name, name)


def _seed(*parts):
    return zlib.crc32("|".join(str(p) for p in parts).encode()) % 100_000


# ---------------------------------------------------------------------------------------------
# membranes


def _band(ax, pts, thickness=MT, token="membrane", closed=False, zorder=6):
    """A membrane along a polyline as a filled band with outlines (closed curves give a ring)."""
    q, nrm, _ = polyline(pts, n=max(80, int(len(pts) * 3)), closed=closed)
    a, b = q + nrm * thickness / 2, q - nrm * thickness / 2
    if closed:
        verts = np.vstack([a, b[::-1]])
        codes = [Path.MOVETO] + [Path.LINETO] * (len(a) - 1) + [Path.MOVETO] + [Path.LINETO] * (len(b) - 1)
        ax.add_patch(PathPatch(Path(verts, codes), facecolor=P.fill(token), edgecolor="none", zorder=zorder))
    else:
        ax.add_patch(Polygon(np.vstack([a, b[::-1]]), closed=True, facecolor=P.fill(token), edgecolor="none", zorder=zorder))
    for side in (a, b):
        ax.plot(side[:, 0], side[:, 1], color=P.edge(token), lw=LINE * 0.6, zorder=zorder + 0.1, solid_capstyle="butt")
    return q, nrm


def _rounded(points, r, n=10):
    """An open polyline with its interior corners replaced by circular-ish fillets of radius r."""
    p = np.asarray(points, float)
    out = [p[0]]
    for i in range(1, len(p) - 1):
        p0, p1, p2 = p[i - 1], p[i], p[i + 1]
        d0, d2 = np.linalg.norm(p0 - p1), np.linalg.norm(p2 - p1)
        rr = min(r, d0 / 2, d2 / 2)
        a = p1 + (p0 - p1) / d0 * rr
        b = p1 + (p2 - p1) / d2 * rr
        for t in np.linspace(0, 1, n):
            out.append((1 - t) ** 2 * a + 2 * (1 - t) * t * p1 + t**2 * b)
    out.append(p[-1])
    return np.array(out)


def _arc(c, r, a0, a1, n=24):
    t = np.radians(np.linspace(a0, a1, n))
    return np.c_[c[0] + r * np.cos(t), c[1] + r * np.sin(t)]


def envelope(ax, x0, x1, y, gap=0.5, pores=(), pore_width=1.4, er=None, er_height=1.6, ribosomes=True, lamina_depth=0.28,
             heterochromatin=True, tint=(2.0, 2.0), labels=True, draw_pores=True, zorder=5):
    """A horizontal section of the nuclear envelope between ``x0`` and ``x1``, centred at height ``y``.

    The outer nuclear membrane (ONM) lies at ``y + gap/2`` and the inner (INM) at ``y - gap/2``; between them
    the perinuclear space is tinted like the ER lumen. At each x in ``pores`` the two membranes join around a
    pore of diameter ``pore_width`` (and an NPC is drawn unless ``draw_pores=False``). ``er`` (an x position)
    draws an ER tube rising from the ONM with a continuous lumen. ``tint`` = (cytoplasm height, nucleoplasm
    height) shades the two spaces. Returns a dict: onm, inm (y values), pores (NPC anchor dicts), er_top, lumen.
    """
    top, bot = y + gap / 2, y - gap / 2
    r = gap / 2
    if tint:
        ax.add_patch(Rectangle((x0, top), x1 - x0, tint[0], facecolor=P.fill(tok("cytoplasm")), edgecolor="none", zorder=zorder - 3))
        ax.add_patch(Rectangle((x0, bot - tint[1]), x1 - x0, tint[1], facecolor=P.fill(tok("nucleoplasm")), edgecolor="none",
                               zorder=zorder - 3))
    pores = sorted(pores)
    hw = pore_width / 2
    edges = [x0] + [v for p in pores for v in (p - hw, p + hw)] + [x1]
    segs = [(edges[2 * i], edges[2 * i + 1]) for i in range(len(edges) // 2)]
    lumens = []
    for i, (a, b) in enumerate(segs):
        left_open, right_open = i == 0, i == len(segs) - 1
        tube = er is not None and a + 0.4 < er < b - 0.4
        # outline of this lumen segment: along the ONM (left to right, optionally up the ER tube) then back along the INM
        start = (a, top) if left_open else (a + r, top)
        end = (b, top) if right_open else (b - r, top)
        if tube:
            h1 = top + er_height
            left_part = _rounded([start, (er - r, top), (er - r, h1)], r * 0.9)
            right_part = _rounded([(er + r, h1), (er + r, top), end], r * 0.9)
            up = np.vstack([left_part, _arc((er, h1), r, 180, 0)[1:-1], right_part])
        else:
            up = np.array([start, end])
        low = np.array([(b if right_open else b - r, bot), (a if left_open else a + r, bot)])
        if right_open:
            right = np.empty((0, 2))
        else:
            right = _arc((b - r, y), r, 90, -90)
        if left_open:
            left = np.empty((0, 2))
        else:
            left = _arc((a + r, y), r, 270, 90)
        ring = np.vstack([up, right[1:-1] if len(right) else right, low, left[1:-1] if len(left) else left])
        ax.add_patch(Polygon(ring, closed=True, facecolor=P.fill(tok("lumen")), edgecolor="none", zorder=zorder))
        closed = not (left_open or right_open)
        if closed:
            _band(ax, np.vstack([ring, ring[:1]]), token=tok("membrane"), closed=True, zorder=zorder + 0.5)
        else:
            # open ends are cut by the figure edge: draw the membrane as one open band around the closed side(s)
            if left_open and right_open:
                _band(ax, up, token=tok("membrane"), zorder=zorder + 0.5)
                _band(ax, low, token=tok("membrane"), zorder=zorder + 0.5)
            elif left_open:
                _band(ax, np.vstack([up, right[1:-1], low]), token=tok("membrane"), zorder=zorder + 0.5)
            else:
                _band(ax, np.vstack([low, left[1:-1], up]), token=tok("membrane"), zorder=zorder + 0.5)
        lumens.append(((a + b) / 2, y))
    out = {"onm": top + MT / 2, "inm": bot - MT / 2, "pores": [], "lumen": lumens, "er_top": None}
    if er is not None:
        out["er_top"] = (er, top + er_height + r)
    # ribosomes on the cytosolic face of the ONM and the ER tube
    if ribosomes:
        xs = np.arange(x0 + 0.35, x1 - 0.2, 0.55)
        for xr in xs:
            if any(abs(xr - p) < hw + 0.3 for p in pores) or (er is not None and abs(xr - er) < r + 0.3):
                continue
            ribosome(ax, (xr, top + MT + 0.13), size=0.26, token=tok("ribosome"), zorder=zorder + 1)
        if er is not None:
            for yy in np.arange(top + 0.45, top + er_height - 0.1, 0.5):
                for sg in (-1, 1):
                    _side_ribosome(ax, (er + sg * (r + MT + 0.13), yy), sg, zorder + 1)
    # lamina and peripheral heterochromatin
    if lamina_depth:
        gaps = [(p - hw - 0.05, p + hw + 0.05) for p in pores]
        lamina(ax, x0, x1, bot - MT / 2 - 0.02, depth=lamina_depth, gaps=gaps, zorder=zorder + 0.3)
        if heterochromatin:
            rng = np.random.default_rng(_seed("hc", x0, x1, y))
            yy = bot - MT / 2 - lamina_depth - 0.18
            for xc in np.arange(x0 + 0.3, x1 - 0.2, 0.32):
                if any(abs(xc - p) < hw + 0.25 for p in pores):
                    continue
                rad = rng.uniform(0.11, 0.17)
                ax.add_patch(Circle((xc + rng.uniform(-0.06, 0.06), yy - rng.uniform(0, 0.12)), rad,
                                    facecolor=P.fill(tok("chromatin")), edgecolor=P.edge(tok("chromatin")), lw=0.5,
                                    zorder=zorder + 0.2))
    if draw_pores:
        for p in pores:
            out["pores"].append(pore(ax, p, y, gap=gap, width=pore_width, zorder=zorder + 2))
    if labels:
        lx = x0 + 0.15
        label(ax, (lx, top + tint[0] - 0.3 if tint else top + 1.0), "Cytoplasm", size="small", bold=True, ha="left",
              color=P.muted())
        label(ax, (lx, bot - tint[1] + 0.3 if tint else bot - 1.0), "Nucleoplasm", size="small", bold=True, ha="left",
              color=P.muted())
    return out


def _side_ribosome(ax, c, sg, z):
    x, yy = c
    o = blob((x + sg * 0.03, yy), 0.1, 0.13, wobble=0.05, seed=_seed("sr", round(x, 2), round(yy, 2)), k=7)
    ax.add_patch(PathPatch(Path(o, closed=True), facecolor=P.fill(tok("ribosome")), edgecolor=P.edge(tok("ribosome")),
                           lw=LINE * 0.6, zorder=z))


def lamina(ax, x0, x1, y, depth=0.28, gaps=(), token=None, zorder=6):
    """A strip of lamin meshwork hanging below height ``y`` (the inner membrane) from x0 to x1.

    Filaments are drawn as a deterministic, roughly orthogonal lattice tilted by 45 degrees; ``gaps``
    [(xa, xb)] leaves room for pores. Returns the y of the lower edge of the lamina.
    """
    t = token or tok("lamina")
    step = depth * 0.95
    lines = []
    for x in np.arange(x0 - depth, x1 + depth, step):
        lines.append(((x, y), (x + depth, y - depth)))
        lines.append(((x + depth, y), (x, y - depth)))
    for (a, b) in lines:
        xs = np.linspace(a[0], b[0], 12)
        ys = np.linspace(a[1], b[1], 12)
        keep = (xs >= x0) & (xs <= x1)
        for ga, gb in gaps:
            keep &= ~((xs > ga) & (xs < gb))
        if keep.sum() < 2:
            continue
        # split into runs of kept points
        runs, cur = [], []
        for k, ok in enumerate(keep):
            if ok:
                cur.append(k)
            elif cur:
                runs.append(cur)
                cur = []
        if cur:
            runs.append(cur)
        for run in runs:
            if len(run) < 2:
                continue
            ax.plot(xs[run], ys[run], color=P.edge(t), lw=2.2, solid_capstyle="round", zorder=zorder)
            ax.plot(xs[run], ys[run], color=P.fill(t), lw=1.1, solid_capstyle="round", zorder=zorder + 0.05)
    return y - depth


# ---------------------------------------------------------------------------------------------
# the nuclear pore complex


def _wavy(a, b, amp, waves, phase=0.0, n=40):
    a, b = np.asarray(a, float), np.asarray(b, float)
    t = np.linspace(0, 1, n)
    d = b - a
    nrm = np.array([-d[1], d[0]]) / (np.linalg.norm(d) or 1)
    return a + np.outer(t, d) + np.outer(amp * np.sin(2 * np.pi * waves * t + phase) * np.sin(np.pi * t), nrm)


def pore(ax, x, y, gap=0.5, width=1.4, fg=True, filaments=True, basket=True, token=None, fg_token=None, zorder=8):
    """Side view of a nuclear pore complex sitting in an envelope whose perinuclear space is centred at ``y``.

    Drawn without membranes (``envelope`` draws them): the inner ring lining the pore membrane, the
    cytoplasmic and nuclear rings, cytoplasmic filaments, the nuclear basket and the FG-repeat mesh filling
    the central channel. Returns anchors: top (cytoplasmic mouth), bottom (nuclear mouth), center, channel
    (half-width of the open channel), filaments (tips), basket (distal ring).
    """
    t = token or tok("nup")
    ft = fg_token or tok("fg")
    hw = width / 2
    top, bot = y + gap / 2, y - gap / 2
    ring_w = 0.26
    inner_x = hw - MT / 2 - ring_w  # inner face of the inner ring
    # inner ring (spokes) lining the pore membrane on both sides
    for sg in (-1, 1):
        cx = x + sg * (hw - MT / 2 - ring_w / 2)
        ax.add_patch(FancyBboxPatch((cx - ring_w / 2, bot - 0.02), ring_w, gap + 0.04, boxstyle="round,pad=0,rounding_size=0.06",
                                    facecolor=P.fill(t), edgecolor=P.edge(t), lw=LINE * 0.7, zorder=zorder + 1))
        # cytoplasmic and nuclear rings: wider blocks capping the pore on each face
        for yy, s in ((top + MT + 0.1, 1), (bot - MT - 0.1, -1)):
            bx0 = x + sg * (hw - 0.12)
            bx1 = x + sg * (inner_x - 0.04)
            xa, xb = min(bx0, bx1), max(bx0, bx1)
            ax.add_patch(FancyBboxPatch((xa, yy - 0.12), xb - xa, 0.24, boxstyle="round,pad=0,rounding_size=0.08",
                                        facecolor=P.fill(t), edgecolor=P.edge(t), lw=LINE * 0.7, zorder=zorder + 1.2))
    out = {"top": (x, top + MT + 0.25), "bottom": (x, bot - MT - 0.25), "center": (x, y), "channel": inner_x,
           "filaments": [], "basket": None}
    if fg:
        rng = np.random.default_rng(_seed("fg", round(x, 3), round(y, 3)))
        yy = np.linspace(bot - MT - 0.05, top + MT + 0.05, 9)
        for sg in (-1, 1):
            for k, yk in enumerate(yy):
                a = (x + sg * inner_x, yk)
                reach = inner_x * rng.uniform(0.75, 1.15)
                b = (x + sg * (inner_x - reach), yk + rng.uniform(-0.18, 0.18))
                pts = _wavy(a, b, 0.05, rng.uniform(1.5, 2.5), phase=rng.uniform(0, 6.3))
                ax.plot(pts[:, 0], pts[:, 1], color=P.edge(ft), lw=0.9, alpha=0.8, zorder=zorder + 0.8, solid_capstyle="round")
    if filaments:
        for sg in (-1, 1):
            for k, dx in enumerate((0.05, 0.3)):
                a = np.array([x + sg * (hw - 0.2 - dx), top + MT + 0.2])
                b = a + np.array([sg * (0.15 + 0.1 * k), 0.55 + 0.12 * k])
                pts = _wavy(a, b, 0.05, 1.2, phase=0.8 * k)
                ax.plot(pts[:, 0], pts[:, 1], color=P.edge(t), lw=1.6, solid_capstyle="round", zorder=zorder + 1)
                out["filaments"].append(tuple(b))
    if basket:
        yb = bot - MT - 0.75
        for sg in (-1, 1):
            for dx in (0.05, 0.28):
                a = (x + sg * (hw - 0.2 - dx), bot - MT - 0.2)
                b = (x + sg * (0.18 + dx * 0.4), yb)
                ax.plot([a[0], b[0]], [a[1], b[1]], color=P.edge(t), lw=1.4, solid_capstyle="round", zorder=zorder + 1)
        ax.add_patch(FancyBboxPatch((x - 0.32, yb - 0.07), 0.64, 0.14, boxstyle="round,pad=0,rounding_size=0.06",
                                    facecolor=P.fill(t), edgecolor=P.edge(t), lw=LINE * 0.7, zorder=zorder + 1.2))
        out["basket"] = (x, yb)
    return out


def pore_top(ax, center, r, spokes=8, token=None, fg=True, membrane=True, zorder=8):
    """Face view of an NPC: ``spokes`` subunits in a ring around the central channel (eightfold symmetry),
    with the pore membrane as a pale ring and FG-repeat strands in the channel. Returns the centre."""
    t = token or tok("nup")
    x, y = center
    if membrane:
        ax.add_patch(Circle(center, r * 1.32, facecolor=P.fill(tok("membrane")), edgecolor=P.edge(tok("membrane")), lw=LINE * 0.6,
                            zorder=zorder))
        ax.add_patch(Circle(center, r * 1.08, facecolor=P.surface(), edgecolor=P.edge(tok("membrane")), lw=LINE * 0.6,
                            zorder=zorder + 0.1))
    for k in range(spokes):
        a = 2 * math.pi * k / spokes + math.pi / spokes
        c = (x + 0.74 * r * math.cos(a), y + 0.74 * r * math.sin(a))
        w, h = 0.3 * r, 0.24 * r
        verts = blob(c, w, h, wobble=0.05, seed=_seed("spoke", k), k=7, angle=a)
        ax.add_patch(PathPatch(Path(verts, closed=True), facecolor=P.fill(t), edgecolor=P.edge(t), lw=LINE * 0.8, zorder=zorder + 1))
    if fg:
        rng = np.random.default_rng(_seed("fgtop", round(x, 2), round(y, 2)))
        for k in range(16):
            a = 2 * math.pi * k / 16 + rng.uniform(-0.1, 0.1)
            p0 = (x + 0.44 * r * math.cos(a), y + 0.44 * r * math.sin(a))
            p1 = (x + rng.uniform(-0.12, 0.12) * r, y + rng.uniform(-0.12, 0.12) * r)
            pts = _wavy(p0, p1, 0.04 * r, 1.5, phase=k)
            ax.plot(pts[:, 0], pts[:, 1], color=P.edge(tok("fg")), lw=0.8, alpha=0.8, zorder=zorder + 0.5)
    return center


def linc(ax, x, env, reach=1.1, token_sun=None, token_kash=None, actin=True, zorder=9):
    """A LINC complex at ``x`` in an ``envelope`` (its returned dict): a SUN trimer spanning the INM, its
    coiled-coil stalk crossing the perinuclear space to the SUN domain, which binds the KASH peptide of a
    nesprin in the ONM; the nesprin's spectrin-repeat rod reaches ``reach`` into the cytoplasm (to an actin
    filament if ``actin``). Returns anchors: sun, kash, tip."""
    ts, tk = token_sun or tok("sun"), token_kash or tok("kash")
    onm, inm = env["onm"], env["inm"]
    mid = (onm + inm) / 2
    # SUN: nucleoplasmic N-terminal domain below the INM, transmembrane segment, stalk, SUN domain
    ax.add_patch(FancyBboxPatch((x - 0.11, inm - 0.32), 0.22, 0.2, boxstyle="round,pad=0,rounding_size=0.06", facecolor=P.fill(ts),
                                edgecolor=P.edge(ts), lw=LINE * 0.7, zorder=zorder))
    ax.plot([x, x], [inm - 0.12, mid - 0.02], color=P.edge(ts), lw=2.4, solid_capstyle="butt", zorder=zorder)
    ax.add_patch(Circle((x, mid + 0.02), 0.09, facecolor=P.fill(ts), edgecolor=P.edge(ts), lw=LINE * 0.7, zorder=zorder + 0.2))
    # KASH: peptide bound to SUN, transmembrane in ONM, rod of spectrin repeats into the cytoplasm
    ax.plot([x + 0.06, x + 0.06], [mid + 0.08, onm + 0.05], color=P.edge(tk), lw=2.0, solid_capstyle="butt", zorder=zorder + 0.3)
    yy = onm + 0.12
    pts = []
    for k in range(int(reach / 0.22)):
        c = (x + 0.06 + 0.1 * math.sin(k * 1.3), yy + 0.11 + k * 0.22)
        ax.add_patch(FancyBboxPatch((c[0] - 0.07, c[1] - 0.09), 0.14, 0.18, boxstyle="round,pad=0,rounding_size=0.05",
                                    facecolor=P.fill(tk), edgecolor=P.edge(tk), lw=LINE * 0.6, zorder=zorder + 0.3))
        pts.append(c)
    tip = (pts[-1][0], pts[-1][1] + 0.1) if pts else (x, onm)
    if actin:
        ta = tok("actin")
        for k in range(9):
            cx = tip[0] - 0.8 + k * 0.2
            ax.add_patch(Circle((cx, tip[1] + 0.13 + 0.045 * (k % 2)), 0.075, facecolor=P.fill(ta), edgecolor=P.edge(ta), lw=0.5,
                                zorder=zorder + 0.4))
    return {"sun": (x, mid), "kash": (x + 0.06, onm), "tip": tip}


# ---------------------------------------------------------------------------------------------
# transport receptors, Ran, cargo


def karyopherin(ax, center, r=0.45, kind="importin", angle=90.0, token=None, text=None, size="tiny", zorder=13):
    """A karyopherin drawn as an arch of HEAT repeats (a C-shaped superhelix seen side on), opening towards
    ``angle`` (degrees). ``kind`` selects the default colour: importin (importin beta), exportin, importin_a.
    Returns anchors: center, mouth (the point inside the arch where a cargo or Ran sits), back."""
    t = token or tok(kind)
    x, y = center
    span = 250.0
    a0 = angle + 180 - span / 2
    n = 12
    for k in range(n):
        a = math.radians(a0 + span * (k + 0.5) / n)
        c = (x + r * math.cos(a), y + r * math.sin(a))
        verts = blob(c, 0.42 * r * math.pi * span / 360 / n * 2.1, 0.32 * r, wobble=0.03, seed=_seed(kind, k), k=6, angle=a)
        ax.add_patch(PathPatch(Path(verts, closed=True), facecolor=P.fill(t), edgecolor=P.edge(t), lw=LINE * 0.55,
                               zorder=zorder + k * 0.001))
    ar = math.radians(angle)
    if text:  # the name sits below the arch
        label(ax, (x, y - r * 1.25), text, size=size, va="top", zorder=zorder + 1)
    return {"center": center, "mouth": (x + 0.15 * r * math.cos(ar), y + 0.15 * r * math.sin(ar)),
            "back": (x - r * math.cos(ar), y - r * math.sin(ar))}


def ran(ax, center, state="GTP", r=0.2, text=None, zorder=14):
    """Ran as a small disc labelled with its nucleotide (``state`` "GTP" or "GDP"). Returns the centre."""
    t = tok("ran_gtp" if state == "GTP" else "ran_gdp")
    ax.add_patch(Circle(center, r, facecolor=P.fill(t), edgecolor=P.edge(t), lw=LINE * 0.8, zorder=zorder))
    label(ax, center, text if text is not None else ("T" if state == "GTP" else "D"), size="tiny", bold=True, color=P.on_fill(),
          zorder=zorder + 0.5)
    return center


def cargo(ax, center, r=0.28, signal="NLS", token=None, angle=-90.0, zorder=13):
    """A folded cargo protein with a short signal tail (``signal`` text, e.g. "NLS" or "NES"; None for none)
    pointing towards ``angle``. Returns anchors: center, signal (tip of the tail)."""
    t = token or tok("cargo")
    x, y = center
    verts = blob(center, r, r * 0.85, wobble=0.08, seed=_seed("cargo", signal), k=8)
    ax.add_patch(PathPatch(Path(verts, closed=True), facecolor=P.fill(t), edgecolor=P.edge(t), lw=LINE * 0.8, zorder=zorder))
    out = {"center": center, "signal": None}
    if signal:
        a = math.radians(angle)
        p0 = (x + r * 0.9 * math.cos(a), y + r * 0.9 * math.sin(a))
        p1 = (x + (r + 0.22) * math.cos(a), y + (r + 0.22) * math.sin(a))
        ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=P.edge(tok("receptor")), lw=2.6, solid_capstyle="round", zorder=zorder - 0.1)
        out["signal"] = p1
    return out


# ---------------------------------------------------------------------------------------------
# the interphase nucleus


def _inside(pts, cx, cy, rx, ry):
    return ((pts[:, 0] - cx) / rx) ** 2 + ((pts[:, 1] - cy) / ry) ** 2 <= 1


def territories(ax, center, rx, ry, n=12, seed=1, highlight=None, tokens=None, nucleoli=(), lamina=True, envelope=True,
                fill="light", shrink=0.9, zorder=6):
    """An interphase nucleus (ellipse ``rx`` × ``ry``) divided into ``n`` chromosome territories.

    Territories are Lloyd-relaxed Voronoi cells of the nuclear interior drawn as rounded blobs that leave a
    thin interchromatin space between them; ``nucleoli`` [(x, y, r)] are excluded (draw them afterwards).
    ``highlight`` {index: token} fills chosen territories strongly; others use pale fills. Returns a dict with
    the outline and a list of territories, each {"center", "outline", "token"}.
    """
    cx, cy = center
    toks = tokens or TERRITORY_TOKENS
    highlight = dict(highlight or {})
    outline = blob(center, rx, ry, wobble=0.025, seed=seed + 100, k=10)
    if envelope:
        ax.add_patch(PathPatch(Path(outline, closed=True), facecolor=P.fill(tok("nucleoplasm")), edgecolor=P.edge(tok("nucleoplasm")),
                               lw=LINE * 1.6, zorder=zorder))
        q, nrm, _ = polyline(outline, n=300, closed=True)
        inward = -nrm if _ccw_area(outline) < 0 else nrm
        inner = q + inward * 0.08
        ax.plot(inner[:, 0], inner[:, 1], color=P.edge(tok("nucleoplasm")), lw=LINE * 0.7, zorder=zorder + 0.1)
        if lamina:
            lam = q + inward * 0.16
            ax.plot(lam[:, 0], lam[:, 1], color=P.edge(tok("lamina")), lw=2.6, zorder=zorder + 0.15)
            ax.plot(lam[:, 0], lam[:, 1], color=P.fill(tok("lamina")), lw=1.2, zorder=zorder + 0.16)
    g = 0.06
    xs, ys = np.meshgrid(np.arange(cx - rx, cx + rx, g), np.arange(cy - ry, cy + ry, g))
    grid = np.c_[xs.ravel(), ys.ravel()]
    grid = grid[_inside(grid, cx, cy, rx * 0.93, ry * 0.93)]
    for (nx, ny, nr) in nucleoli:
        grid = grid[np.hypot(grid[:, 0] - nx, grid[:, 1] - ny) > nr + 0.12]
    rng = np.random.default_rng(seed)
    seeds = grid[rng.choice(len(grid), n, replace=False)]
    for _ in range(40):
        d = np.hypot(grid[:, None, 0] - seeds[None, :, 0], grid[:, None, 1] - seeds[None, :, 1])
        own = d.argmin(1)
        seeds = np.array([grid[own == k].mean(0) if (own == k).any() else seeds[k] for k in range(n)])
    d = np.hypot(grid[:, None, 0] - seeds[None, :, 0], grid[:, None, 1] - seeds[None, :, 1])
    own = d.argmin(1)
    out = {"outline": outline, "territories": []}
    for k in range(n):
        pts = grid[own == k]
        c = pts.mean(0)
        ang = np.arctan2(pts[:, 1] - c[1], pts[:, 0] - c[0])
        rad = np.hypot(pts[:, 0] - c[0], pts[:, 1] - c[1])
        m = 14
        ctrl = []
        for j in range(m):
            a = -math.pi + 2 * math.pi * (j + 0.5) / m
            sel = np.abs((ang - a + math.pi) % (2 * math.pi) - math.pi) < math.pi / m
            rr = (np.percentile(rad[sel], 97) if sel.sum() > 2 else rad.mean()) * shrink
            ctrl.append((c[0] + rr * math.cos(a), c[1] + rr * math.sin(a)))
        verts = smooth_closed(ctrl, n=140)
        tkn = highlight.get(k, toks[k % len(toks)])
        face = P.fill(tkn) if (k in highlight or fill == "full") else P.light(tkn)
        ax.add_patch(PathPatch(Path(verts, closed=True), facecolor=face, edgecolor=P.edge(tkn), lw=LINE * 0.6,
                               zorder=zorder + 0.3 + (0.05 if k in highlight else 0)))
        out["territories"].append({"center": tuple(c), "outline": verts, "token": tkn})
    return out


def _ccw_area(v):
    v = np.asarray(v, float)
    return 0.5 * np.sum(v[:-1, 0] * v[1:, 1] - v[1:, 0] * v[:-1, 1])


def nucleolus(ax, center, r, units=3, seed=2, tokens=None, zorder=9):
    """A nucleolus in section: a granular component (GC) enclosing ``units`` fibrillar centres (FC), each
    surrounded by a shell of dense fibrillar component (DFC). ``tokens`` = (fc, dfc, gc) overrides the colours.
    Returns {"gc": outline, "units": [(center, r_fc, r_dfc), ...], "center", "r"}."""
    tf, td, tg = tokens or (tok("fc"), tok("dfc"), tok("gc"))
    gc = blob(center, r, r * 0.92, wobble=0.07, seed=seed, k=9)
    ax.add_patch(PathPatch(Path(gc, closed=True), facecolor=P.fill(tg), edgecolor=P.edge(tg), lw=LINE * 0.8, zorder=zorder))
    rng = np.random.default_rng(seed)
    units_out = []
    for k in range(units):
        if units == 1:
            c = np.asarray(center, float)
        else:
            a = 2 * math.pi * k / units + rng.uniform(-0.3, 0.3) + 0.4
            c = np.asarray(center, float) + 0.45 * r * np.array([math.cos(a), math.sin(a)])
        rf = r * rng.uniform(0.12, 0.17) * (1.4 if units == 1 else 1.0)
        rd = rf + r * 0.12
        dfc = blob(tuple(c), rd, rd * 0.95, wobble=0.12, seed=seed + 10 + k, k=8)
        ax.add_patch(PathPatch(Path(dfc, closed=True), facecolor=P.fill(td), edgecolor=P.edge(td), lw=LINE * 0.6, zorder=zorder + 0.2))
        ax.add_patch(Circle(tuple(c), rf, facecolor=P.light(tf), edgecolor=P.edge(tf), lw=LINE * 0.6, zorder=zorder + 0.3))
        units_out.append((tuple(c), rf, rd))
    # granules of the GC
    for _ in range(int(60 * r * r)):
        a, d = rng.uniform(0, 2 * math.pi), r * 0.85 * math.sqrt(rng.uniform(0, 1))
        p = np.asarray(center, float) + d * np.array([math.cos(a), math.sin(a)])
        if any(np.hypot(*(p - np.asarray(u[0]))) < u[2] + 0.05 for u in units_out):
            continue
        ax.add_patch(Circle(tuple(p), r * 0.035, facecolor=P.edge(tg), edgecolor="none", alpha=0.55, zorder=zorder + 0.1))
    return {"gc": gc, "units": units_out, "center": center, "r": r}


# ---------------------------------------------------------------------------------------------
# special chromosomes


def polytene(ax, x0, x1, y, h=0.7, puff=None, puff_width=0.9, seed=4, token=None, zorder=8):
    """A stretch of a polytene chromosome from x0 to x1 (half-height ``h``/2) with dark bands and pale
    interbands; ``puff`` (fraction of the length) swells one region into a decondensed puff with a halo of
    RNA. Returns a dict: xmap (fraction -> x), puff (centre) and bands [(xa, xb)]."""
    t = token or tok("chromatin")
    L = x1 - x0
    s = np.linspace(0, 1, 400)
    xs = x0 + s * L
    half = np.full_like(s, h / 2)
    pc = None
    if puff is not None:
        w = puff_width / L
        bump = np.exp(-(((s - puff) / (w / 2.2)) ** 2))
        half = half * (1 + 0.9 * bump)
        pc = (x0 + puff * L, y)
        # RNA halo around the puff
        halo = smooth_closed([(pc[0] + 0.62 * puff_width * math.cos(a), y + (h * 0.95) * math.sin(a))
                              for a in np.linspace(0, 2 * math.pi, 12, endpoint=False)], n=120)
        ax.add_patch(PathPatch(Path(halo, closed=True), facecolor=P.light("rna"), edgecolor=P.edge("rna"), lw=0.6,
                               ls=(0, (2, 2)), zorder=zorder - 0.5))
    wob = 0.03 * np.sin(s * 37) * h
    top, bot = y + half + wob, y - half + wob
    body = np.vstack([np.c_[xs, top], np.c_[xs[::-1], bot[::-1]]])
    ax.add_patch(Polygon(body, closed=True, facecolor=P.light(t), edgecolor="none", zorder=zorder))
    rng = np.random.default_rng(seed)
    bands = []
    f = 0.01
    while f < 0.99:
        w = rng.choice([0.006, 0.01, 0.016, 0.026], p=[0.3, 0.3, 0.25, 0.15])
        dark = rng.uniform(0.6, 1.0)
        if puff is not None and abs(f - puff) < (puff_width / L) * 0.55:
            dark *= 0.25
        fa, fb = f, min(f + w, 0.995)
        m = (s >= fa) & (s <= fb)
        if m.sum() >= 2:
            poly = np.vstack([np.c_[xs[m], top[m]], np.c_[xs[m][::-1], bot[m][::-1]]])
            ax.add_patch(Polygon(poly, closed=True, facecolor=P.mix(P.fill(t), P.edge(t), dark), edgecolor="none", zorder=zorder + 0.1))
            bands.append((x0 + fa * L, x0 + fb * L))
        f = fb + rng.uniform(0.008, 0.03)
    ax.plot(xs, top, color=P.edge(t), lw=LINE * 0.7, zorder=zorder + 0.2)
    ax.plot(xs, bot, color=P.edge(t), lw=LINE * 0.7, zorder=zorder + 0.2)
    return {"xmap": lambda frac: x0 + frac * L, "puff": pc, "bands": bands}


def lampbrush(ax, x0, x1, y, loops=7, loop_height=1.1, token=None, seed=5, zorder=8):
    """A lampbrush chromosome: a beaded axis of chromomeres with pairs of lateral loops (one per sister
    chromatid, above and below). Each loop is a transcription unit: the RNP fibrils (short hairs) grow longer
    along the loop in the direction of transcription. Returns a dict: axis (x0, x1, y) and loops (apex points)."""
    t = token or tok("chromatin")
    rng = np.random.default_rng(seed)
    xs = np.linspace(x0, x1, int((x1 - x0) / 0.13) + 1)
    for k, xc in enumerate(xs):
        ax.add_patch(Circle((xc, y + 0.03 * math.sin(k)), 0.075 + 0.03 * rng.uniform(), facecolor=P.fill(t), edgecolor=P.edge(t),
                            lw=0.5, zorder=zorder + 0.5))
    apexes = []
    pos = np.linspace(x0 + 0.6, x1 - 0.6, loops)
    for k, xc in enumerate(pos):
        for sg in (1, -1):
            hgt = loop_height * rng.uniform(0.75, 1.15)
            wid = rng.uniform(0.35, 0.55)
            ctrl = [(xc - 0.06, y), (xc - wid * 0.5, y + sg * hgt * 0.45), (xc - wid * 0.35, y + sg * hgt * 0.92),
                    (xc + wid * 0.25, y + sg * hgt), (xc + wid * 0.5, y + sg * hgt * 0.5), (xc + 0.06, y)]
            q, nrm, _ = polyline(_catmull(ctrl), n=90)
            cen = q.mean(0)
            ax.plot(q[:, 0], q[:, 1], color=P.edge("dna"), lw=0.9, zorder=zorder + 0.2)
            for j in range(5, len(q) - 4, 3):
                ln = 0.03 + 0.22 * j / len(q)  # nascent RNP fibrils lengthen along the transcription unit
                d = nrm[j] if np.dot(nrm[j], q[j] - cen) > 0 else -nrm[j]
                p1 = q[j] + d * ln
                ax.plot([q[j, 0], p1[0]], [q[j, 1], p1[1]], color=P.edge("rna"), lw=0.8, alpha=0.9, zorder=zorder + 0.1)
            apexes.append(tuple(q[len(q) // 2]))
    return {"axis": (x0, x1, y), "loops": apexes}


def _catmull(p, n=20):
    p = np.asarray(p, float)
    p = np.vstack([p[0], p, p[-1]])
    out = []
    for i in range(1, len(p) - 2):
        p0, p1, p2, p3 = p[i - 1], p[i], p[i + 1], p[i + 2]
        for t in np.linspace(0, 1, n, endpoint=False):
            t2, t3 = t * t, t * t * t
            out.append(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t2 + (-p0 + 3 * p1 - 3 * p2 + p3) * t3))
    out.append(p[-2])
    return np.array(out)
