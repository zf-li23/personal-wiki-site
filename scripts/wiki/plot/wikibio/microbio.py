"""Microbiology figures: bacterial cell shapes and flagella, the Gram-positive and Gram-negative cell
envelopes in cross-section, and batch growth (Monod kinetics, a Baranyi lag, death after starvation).

    from wikibio import microbio as M
    M.coccus(ax, (2, 2), 0.4, gram="+")                          # whole cells, coloured by Gram stain
    M.bacillus(ax, (5, 2), 1.6, 0.6, flagella="peritrichous")    # monotrichous / lophotrichous / amphitrichous
    M.vibrio(ax, (8, 2), 1.4, 0.45, flagella="monotrichous")
    M.spirillum(ax, (10, 2), (13, 2), width=0.28, turns=2.5, flagella="amphitrichous")
    M.spirochete(ax, (14, 2), (17, 2))
    M.chain(ax, (1, 5), 5, 0.3) / M.cluster(ax, (4, 5), 0.3) / M.diplococcus(ax, (7, 5), 0.3)

    env = M.envelope(ax, 1, 8, y=4, kind="gram-")                # cross-section; returns the layer heights
    t, N, S = M.batch_growth(t, mu_max=0.9, Ks=0.01, Y=1.7e9, S0=2.0, N0=1e5, q0=0.2, kd=0.1, tau_s=10)

Gram-stain colours: ``gram="+"`` uses the ``protein`` token (purple, crystal violet retained),
``gram="-"`` the ``receptor`` token (pink, safranin counterstain). Envelope parts use semantic tokens
(see ``TOK``); cross-sections are schematic: the relative thicknesses are right (Gram-positive wall
20-80 nm, Gram-negative peptidoglycan 2-7 nm, outer membrane about 7 nm), individual molecules are not
to scale.
"""

import math

import numpy as np
from matplotlib.patches import Circle, PathPatch, Polygon, Rectangle
from matplotlib.path import Path

from . import palette as P
from .core import LINE, polyline

# semantic names of envelope parts -> palette tokens (candidates for palette.ALIASES)
TOK = {
    # palette aliases where the part has one; the rest name the token they share
    "gram+": "gram_pos", "gram-": "gram_neg", "nag": "nag", "nam": "nam", "peptide": "peptide",
    "teichoic": "teichoic", "lipid_a": "lipid_a", "core": "carbohydrate", "o_antigen": "o_antigen", "porin": "porin",
    "lipoprotein": "protein", "transporter": "enzyme", "flagellum": "flagellum", "nucleoid": "dna",
}


def _tok(name):
    return TOK.get(name, name)


def gram_token(gram):
    """The token of a Gram-stained cell: "+" purple, "-" pink, None the neutral bacterium colour."""
    return {"+": TOK["gram+"], "-": TOK["gram-"]}.get(gram, "bacterium")


# ------------------------------------------------------------------ whole cells


def _rot(pts, center, angle):
    c, s = math.cos(angle), math.sin(angle)
    return np.asarray(pts, float) @ np.array([[c, s], [-s, c]]) + np.asarray(center, float)


def _body(ax, outline, token, zorder, highlight=True):
    """Fill + outline + a soft inner highlight band for a cell outline."""
    o = np.asarray(outline, float)
    ax.add_patch(PathPatch(Path(np.vstack([o, o[:1]]), closed=True), facecolor=P.fill(token), edgecolor=P.edge(token),
                           lw=LINE, zorder=zorder, joinstyle="round"))
    if highlight:
        c = o.mean(axis=0)
        inner = c + (o - c) * 0.78
        ax.add_patch(PathPatch(Path(np.vstack([inner, inner[:1]]), closed=True), facecolor=P.light(token), edgecolor="none",
                               alpha=0.55, zorder=zorder + 0.2))


def _capsule(length, width, n=80):
    r = width / 2
    L = max(length / 2 - r, 0)
    t = np.linspace(-np.pi / 2, np.pi / 2, n // 2)
    right = np.c_[L + r * np.cos(t), r * np.sin(t)]
    left = np.c_[-L - r * np.cos(t), -r * np.sin(t)]
    return np.vstack([right, left])


def flagellum(ax, base, direction, length=1.6, amplitude=0.12, waves=2.5, token=None, lw=1.1, hook=True, zorder=4):
    """A flagellum: a hook at ``base`` and a sinusoidal filament of ``length`` along ``direction`` (radians)."""
    tok = _tok(token or "flagellum")
    col = P.mix(P.fill(tok), P.surface(), 0.3) if P.is_dark() else P.edge(tok)
    s = np.linspace(0, length, 120)
    env = np.clip(s / (0.25 * length), 0, 1)  # the wave grows away from the hook
    w = amplitude * env * np.sin(2 * np.pi * waves * s / length)
    pts = _rot(np.c_[s, w], base, direction)
    ax.plot(pts[:, 0], pts[:, 1], color=col, lw=lw, solid_capstyle="round", zorder=zorder)
    if hook:
        ax.add_patch(Circle(base, 0.045, color=col, zorder=zorder + 0.1))
    return pts[-1]


def coccus(ax, center, r, gram=None, token=None, zorder=8):
    """A spherical cell (coccus). Returns its outline."""
    th = np.linspace(0, 2 * np.pi, 90, endpoint=False)
    o = np.c_[center[0] + r * np.cos(th), center[1] + r * np.sin(th)]
    _body(ax, o, token or gram_token(gram), zorder)
    return o


def diplococcus(ax, center, r, angle=0.0, gram=None, token=None, zorder=8):
    """A pair of cocci (Neisseria-like: flattened where they touch)."""
    d = np.array([math.cos(angle), math.sin(angle)]) * r * 0.95
    c = np.asarray(center, float)
    return [coccus(ax, c - d, r, gram, token, zorder), coccus(ax, c + d, r, gram, token, zorder + 0.5)]


def chain(ax, start, n, r, angle=0.0, gram=None, token=None, wiggle=0.12, seed=1, zorder=8):
    """A chain of ``n`` cocci (Streptococcus); the chain bends slightly (deterministic for ``seed``)."""
    rng = np.random.default_rng(seed)
    p = np.asarray(start, float)
    a = angle
    out = []
    for i in range(n):
        out.append(coccus(ax, p, r, gram, token, zorder + i * 0.01))
        a += rng.uniform(-wiggle, wiggle) * 2
        p = p + np.array([math.cos(a), math.sin(a)]) * r * 1.9
    return out


def cluster(ax, center, r, n=9, gram=None, token=None, seed=3, zorder=8):
    """A grape-like cluster of cocci (Staphylococcus), packed on a jittered hexagonal grid."""
    rng = np.random.default_rng(seed)
    pts = []
    for i, j in [(0, 0), (1, 0), (-1, 0), (0.5, 0.87), (-0.5, 0.87), (0.5, -0.87), (-0.5, -0.87), (1.5, 0.87), (-1, 1.74),
                 (0, 1.74), (1, -1.74), (1.5, -0.87)][:n]:
        pts.append(np.asarray(center) + np.array([i, j]) * r * 1.9 + rng.uniform(-0.06, 0.06, 2) * r)
    order = np.argsort([-p[1] for p in pts])  # back (top) first
    return [coccus(ax, pts[k], r, gram, token, zorder + 0.01 * m) for m, k in enumerate(order)]


def _attach_flagella(ax, poles, side_points, kind, length, angle, zorder):
    """Flagella on a rod: ``poles`` = [(point, outward angle), ...] (two poles), ``side_points`` for peritrichous."""
    if not kind:
        return
    if kind == "monotrichous":
        flagellum(ax, poles[0][0], poles[0][1], length, zorder=zorder)
    elif kind == "amphitrichous":
        for p, a in poles:
            flagellum(ax, p, a, length, zorder=zorder)
    elif kind == "lophotrichous":
        p, a = poles[0]
        for da in (-0.45, -0.15, 0.15, 0.45):
            flagellum(ax, p, a + da, length * (1 - abs(da) * 0.3), amplitude=0.1, zorder=zorder)
    elif kind == "peritrichous":
        for p, a in side_points:
            flagellum(ax, p, a, length * 0.85, amplitude=0.1, waves=2.2, zorder=zorder)
    else:
        raise ValueError(f"unknown flagellation {kind!r}")


def bacillus(ax, center, length, width, angle=0.0, gram=None, token=None, flagella=None, flagellum_length=1.4,
             dividing=False, zorder=8):
    """A rod (bacillus), optionally dividing (a septum constriction) and with flagella
    (``"monotrichous"``, ``"lophotrichous"``, ``"amphitrichous"``, ``"peritrichous"``).
    Returns dict(outline, poles=[(xy, outward angle)])."""
    a = math.radians(angle)
    o = _capsule(length, width)
    if dividing:
        x = o[:, 0]
        o = o.copy()
        o[:, 1] *= 1 - 0.38 * np.exp(-(x / (width * 0.35)) ** 2)
    O = _rot(o, center, a)
    poles = [(_rot([[length / 2, 0]], center, a)[0], a), (_rot([[-length / 2, 0]], center, a)[0], a + math.pi)]
    side = []
    for k, (fx, sgn) in enumerate(((-0.3, 1), (0.15, 1), (0.38, -1), (-0.1, -1), (0.48, 0), (-0.48, 0))):
        if sgn == 0:
            p = [np.sign(fx) * length / 2 * 0.98, 0.18 * width * (1 if k % 2 else -1)]
            dirn = a + (0 if fx > 0 else math.pi) + (0.5 if k % 2 else -0.5)
        else:
            p = [fx * length, sgn * width / 2]
            dirn = a + sgn * math.pi / 2 + (0.5 if fx > 0 else -0.5) * sgn
        side.append((_rot([p], center, a)[0], dirn))
    _attach_flagella(ax, poles, side, flagella, flagellum_length, a, zorder - 1)
    _body(ax, O, token or gram_token(gram), zorder)
    if dividing:
        s = _rot([[0, -width * 0.31], [0, width * 0.31]], center, a)
        ax.plot(s[:, 0], s[:, 1], color=P.edge(token or gram_token(gram)), lw=LINE * 0.8, zorder=zorder + 0.3)
    return dict(outline=O, poles=poles)


def vibrio(ax, center, length, width, angle=0.0, bend=0.35, gram="-", token=None, flagella="monotrichous",
           flagellum_length=1.4, zorder=8):
    """A comma-shaped curved rod (Vibrio) with a polar flagellum by default."""
    a = math.radians(angle)
    s = np.linspace(-length / 2 + width / 2, length / 2 - width / 2, 40)
    R = length / (2 * max(bend, 1e-3))
    spine = np.c_[s, (s**2) / (2 * R) - (length / 2) ** 2 / (2 * R) * 0.5]
    q, nrm, _ = polyline(spine, n=60, closed=False)
    r = width / 2
    top, bot = q + nrm * r, q - nrm * r
    d_end = q[-1] - q[-2]
    ang_end = math.atan2(d_end[1], d_end[0])
    t = np.linspace(math.pi / 2, -math.pi / 2, 20) + ang_end
    cap_end = q[-1] + r * np.c_[np.cos(t), np.sin(t)]
    d0 = q[0] - q[1]
    ang0 = math.atan2(d0[1], d0[0])
    t0 = np.linspace(math.pi / 2, -math.pi / 2, 20) + ang0
    cap0 = q[0] + r * np.c_[np.cos(t0), np.sin(t0)]
    o = np.vstack([top, cap_end, bot[::-1], cap0])
    O = _rot(o, center, a)
    pole = _rot([q[-1] + np.array([math.cos(ang_end), math.sin(ang_end)]) * r], center, a)[0]
    poles = [(pole, a + ang_end), (_rot([q[0] + np.array([math.cos(ang0), math.sin(ang0)]) * r], center, a)[0], a + ang0)]
    _attach_flagella(ax, poles, [], flagella, flagellum_length, a, zorder - 1)
    _body(ax, O, token or gram_token(gram), zorder)
    return dict(outline=O, poles=poles)


def _helix_tube(a, b, width, turns, amplitude):
    a, b = np.asarray(a, float), np.asarray(b, float)
    L = np.linalg.norm(b - a)
    s = np.linspace(0, L, max(200, int(turns * 60)))
    y = amplitude * np.sin(2 * np.pi * turns * s / L)
    ang = math.atan2(*(b - a)[::-1])
    return _rot(np.c_[s, y], a, ang), ang


def spirillum(ax, a, b, width=0.28, turns=2.0, amplitude=0.35, gram="-", token=None, flagella="amphitrichous",
              flagellum_length=1.0, zorder=8):
    """A rigid helical cell (Spirillum) from a to b, drawn as a thick wave with rounded ends; flagella in
    tufts or single at the poles."""
    spine, ang = _helix_tube(a, b, width, turns, amplitude)
    tok = token or gram_token(gram)
    # draw as a polygon band so the outline is exact in canvas units
    q, nrm, _ = polyline(spine, n=300, closed=False)
    r = width / 2
    top, bot = q + nrm * r, q - nrm * r
    caps = []
    for end, sgn in ((q[-1], 1), (q[0], -1)):
        d = q[-1] - q[-2] if sgn > 0 else q[0] - q[1]
        e = math.atan2(d[1], d[0])
        t = np.linspace(math.pi / 2, -math.pi / 2, 16) + e
        caps.append(end + r * np.c_[np.cos(t), np.sin(t)])
    o = np.vstack([top, caps[0], bot[::-1], caps[1]])
    poles = []
    for idx, nb in ((-1, -2), (0, 1)):
        d = q[idx] - q[nb]
        e = math.atan2(d[1], d[0])
        poles.append((q[idx] + np.array([math.cos(e), math.sin(e)]) * r, e))
    kind = flagella
    if kind == "amphitrichous":  # draw tufts at both poles (Spirillum volutans)
        for p, e in poles:
            for da in (-0.3, 0.0, 0.3):
                flagellum(ax, p, e + da, flagellum_length, amplitude=0.08, zorder=zorder - 1)
    else:
        _attach_flagella(ax, poles, [], kind, flagellum_length, ang, zorder - 1)
    _body(ax, o, tok, zorder, highlight=False)
    ax.plot(q[:, 0], q[:, 1], color=P.light(tok), lw=1.2, zorder=zorder + 0.2, solid_capstyle="round")
    return dict(outline=o, poles=poles)


def spirochete(ax, a, b, width=0.13, turns=7.0, amplitude=0.13, gram="-", token=None, endoflagella=True, zorder=8):
    """A thin, tightly coiled spirochete (Treponema, Borrelia); its flagella lie in the periplasm
    (endoflagella), drawn as a dashed line along the cell."""
    tok = token or gram_token(gram)
    spine, ang = _helix_tube(a, b, width, turns, amplitude)
    q, nrm, _ = polyline(spine, n=400, closed=False)
    r = width / 2
    o = np.vstack([q + nrm * r, (q - nrm * r)[::-1]])
    _body(ax, o, tok, zorder, highlight=False)
    if endoflagella:
        ax.plot(q[:, 0], q[:, 1], color=P.edge(tok), lw=0.7, ls=(0, (2, 1.5)), zorder=zorder + 0.3)
    return dict(outline=o)


# ------------------------------------------------------------------ envelope cross-sections

HEAD, TAIL, SPACING = 0.085, 0.26, 0.22
LEAFLET = HEAD * 2 + TAIL  # thickness of one leaflet (heads + tails)


def _free(x, skip):
    return all(not (a <= x <= b) for a, b in skip)


def leaflet(ax, x0, x1, y, side=1, skip=(), spacing=SPACING, zorder=6):
    """One phospholipid leaflet along a horizontal line at the bilayer mid-plane ``y``: heads on ``side``
    (+1 above, -1 below), tails towards y. ``skip`` = [(xa, xb), ...] leaves gaps for proteins."""
    hc, he, tc = P.fill("lipid_head"), P.edge("lipid_head"), P.edge("lipid_tail")
    for x in np.arange(x0 + spacing / 2, x1, spacing):
        if not _free(x, skip):
            continue
        for dx in (-0.035, 0.035):
            ax.plot([x + dx, x + dx], [y + side * 0.02, y + side * (0.02 + TAIL)], color=tc, lw=0.8, solid_capstyle="round",
                    zorder=zorder)
        ax.add_patch(Circle((x, y + side * (0.02 + TAIL + HEAD)), HEAD, facecolor=hc, edgecolor=he, lw=0.55, zorder=zorder + 1))


def bilayer(ax, x0, x1, y, skip=(), zorder=6):
    """A horizontal phospholipid bilayer centred on y (thickness 2 * (TAIL + 2 HEAD) + gap), with gaps."""
    leaflet(ax, x0, x1, y, 1, skip, zorder=zorder)
    leaflet(ax, x0, x1, y, -1, skip, zorder=zorder)
    return y - 0.02 - TAIL - 2 * HEAD, y + 0.02 + TAIL + 2 * HEAD


def _sugar(ax, c, r, token, zorder):
    """A sugar residue as a small hexagon (SNFG-like shape, palette colour)."""
    th = np.linspace(0, 2 * np.pi, 7)[:-1] + np.pi / 6
    ax.add_patch(Polygon(np.c_[c[0] + r * np.cos(th), c[1] + r * np.sin(th)], closed=True, facecolor=P.fill(token),
                         edgecolor=P.edge(token), lw=0.55, zorder=zorder))


def peptidoglycan(ax, x0, x1, y0, layers=1, spacing=0.36, bead=0.075, pitch=0.2, seed=2, zorder=7):
    """Peptidoglycan (murein): ``layers`` glycan strands of alternating NAG / NAM residues (hexagons)
    joined by short peptide cross-links (yellow bars) between neighbouring strands. Strands start at
    height y0 and are ``spacing`` apart. Returns the top y of the mesh."""
    rng = np.random.default_rng(seed)
    nag, nam, pep = _tok("nag"), _tok("nam"), _tok("peptide")
    xs = np.arange(x0 + pitch / 2, x1 - pitch / 4, pitch)
    for L in range(layers):
        y = y0 + L * spacing
        # strands are finite: break each layer at a few random points (glycan chains are 5-100 residues)
        breaks = set(rng.choice(len(xs), size=max(1, len(xs) // 14), replace=False).tolist())
        ax.plot([x0 + 0.02, x1 - 0.02], [y, y], color=P.edge(nag), lw=0.7, zorder=zorder - 0.5)
        for i, x in enumerate(xs):
            if i in breaks:
                continue
            _sugar(ax, (x, y), bead, nam if i % 2 else nag, zorder)
        if L < layers - 1:
            off = (L % 2) * 2
            for i in range(1 + off, len(xs), 4):
                ax.plot([xs[i], xs[i]], [y + bead, y + spacing - bead], color=P.edge(pep), lw=1.4, solid_capstyle="round",
                        zorder=zorder - 0.3)
    if layers == 1:  # a single sheet still carries cross-links to the neighbouring strand (in the plane)
        for i in range(1, len(xs), 4):
            ax.plot([xs[i], xs[i]], [y0 + bead, y0 + bead + 0.12], color=P.edge(pep), lw=1.4, solid_capstyle="round",
                    zorder=zorder - 0.3)
    return y0 + (layers - 1) * spacing + bead


def teichoic_acid(ax, base, top, bead=0.055, token=None, wave=0.05, anchor=None, zorder=9):
    """A teichoic acid: a chain of polyol-phosphate units from ``base`` up to height ``top``. ``anchor``
    = "lipid" draws a glycolipid anchor (lipoteichoic acid in the membrane), "wall" a linkage unit to
    peptidoglycan (wall teichoic acid)."""
    tok = _tok(token or "teichoic")
    x, y = base
    n = max(2, int((top - y) / (bead * 2.1)))
    ys = np.linspace(y, top, n)
    xs = x + wave * np.sin(np.linspace(0, 3 * np.pi, n))
    ax.plot(xs, ys, color=P.edge(tok), lw=0.8, zorder=zorder - 0.1)
    for a, b in zip(xs, ys):
        ax.add_patch(Circle((a, b), bead, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.5, zorder=zorder))
    if anchor == "lipid":
        for dx in (-0.035, 0.035):
            ax.plot([x + dx, x + dx], [y - 0.02, y - 0.02 - TAIL], color=P.edge("lipid_tail"), lw=0.9, zorder=zorder - 0.2)
    elif anchor == "wall":
        ax.add_patch(Rectangle((x - 0.05, y - 0.12), 0.1, 0.12, facecolor=P.fill(_tok("nam")), edgecolor=P.edge(_tok("nam")),
                               lw=0.5, zorder=zorder))
    return (float(xs[-1]), float(ys[-1]))


def lps(ax, x, y, o_units=4, unit=3, seed=0, zorder=9):
    """One lipopolysaccharide molecule in the outer leaflet whose mid-plane is y: lipid A (a pair of
    glucosamines with six acyl chains pointing down), the core oligosaccharide and an O-antigen of
    ``o_units`` repeating units of ``unit`` sugars (0 for rough LPS). Returns the top point."""
    rng = np.random.default_rng(seed)
    la, core, oa = _tok("lipid_a"), _tok("core"), _tok("o_antigen")
    tc = P.edge("lipid_tail")
    for dx in (-0.15, -0.09, -0.03, 0.03, 0.09, 0.15):
        ax.plot([x + dx, x + dx], [y + 0.02, y + 0.02 + TAIL], color=tc, lw=0.8, solid_capstyle="round", zorder=zorder - 0.5)
    hy = y + 0.02 + TAIL + HEAD
    for dx in (-0.08, 0.08):
        ax.add_patch(Circle((x + dx, hy), HEAD * 1.05, facecolor=P.fill(la), edgecolor=P.edge(la), lw=0.6, zorder=zorder))
    # core: a short branched chain
    yy, xx = hy + HEAD + 0.07, x
    pts = []
    for k in range(4):
        pts.append((xx, yy))
        yy += 0.15
        xx += rng.uniform(-0.04, 0.04)
    ax.plot([p[0] for p in pts], [p[1] for p in pts], color=P.edge(core), lw=0.6, zorder=zorder - 0.2)
    for p in pts:
        _sugar(ax, p, 0.065, core, zorder)
    _sugar(ax, (pts[1][0] + 0.13, pts[1][1] + 0.04), 0.055, core, zorder)
    top = pts[-1]
    if o_units:
        chain = []
        xx, yy = top[0], top[1] + 0.13
        phase = rng.uniform(0, 2 * np.pi)
        for k in range(o_units * unit):
            chain.append((xx + 0.05 * math.sin(phase + k * 0.7), yy))
            yy += 0.115
        ax.plot([p[0] for p in [top] + chain], [p[1] for p in [top] + chain], color=P.edge(oa), lw=0.6, zorder=zorder - 0.2)
        for k, p in enumerate(chain):
            ax.add_patch(Circle(p, 0.05, facecolor=P.fill(oa) if (k // unit) % 2 == 0 else P.light(oa), edgecolor=P.edge(oa),
                                lw=0.5, zorder=zorder))
        top = chain[-1]
    return top


def porin(ax, x, y, width=0.95, height=None, token=None, zorder=11):
    """A porin (trimeric beta-barrel, side view) spanning the outer membrane at mid-plane y: barrel
    walls with beta-strand stripes around an open, water-filled channel."""
    tok = _tok(token or "porin")
    h = height or 2 * LEAFLET + 0.22
    for side in (-1, 1):
        xi = x + side * 0.09
        xo = x + side * width / 2
        pts = [(xi, y - h / 2), (xo, y - h / 2 + 0.06), (xo + side * 0.03, y), (xo, y + h / 2 - 0.06), (xi, y + h / 2)]
        ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=LINE * 0.8, joinstyle="round",
                             zorder=zorder))
        for t in np.linspace(0.2, 0.8, 4):  # beta strands, tilted
            xa = xi + (xo - xi) * t
            ax.plot([xa - side * 0.05, xa + side * 0.05], [y - h / 2 + 0.12, y + h / 2 - 0.12], color=P.edge(tok), lw=0.6,
                    zorder=zorder + 0.1)
    return (x, y + h / 2), (x, y - h / 2)


def transporter(ax, x, y, width=0.75, token=None, zorder=11):
    """An integral membrane protein (transporter) spanning a bilayer at mid-plane y."""
    from .molecules import protein as _protein

    _protein(ax, (x, y), width, 2 * LEAFLET + 0.45, _tok(token or "transporter"), wobble=0.06, zorder=zorder)


def lipoprotein(ax, x, y_pg, y_om, token=None, zorder=10):
    """Braun's lipoprotein (Lpp): a helical rod from the peptidoglycan (covalent link) up to a lipid
    anchor in the inner leaflet of the outer membrane (mid-plane y_om)."""
    tok = _tok(token or "lipoprotein")
    top = y_om - 0.02 - TAIL * 0.3
    s = np.linspace(y_pg, top - 0.1, 60)
    ax.plot(x + 0.06 * np.sin((s - y_pg) * 28), s, color=P.edge(tok), lw=1.6, zorder=zorder, solid_capstyle="round")
    for dx in (-0.035, 0.035):
        ax.plot([x + dx, x + dx], [top - 0.1, y_om - 0.02], color=P.edge("lipid_tail"), lw=0.9, zorder=zorder)
    ax.add_patch(Circle((x, top - 0.12), 0.05, color=P.edge(tok), zorder=zorder + 0.1))


def _band(ax, x0, x1, y0, y1, color, zorder=1):
    ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, facecolor=color, edgecolor="none", zorder=zorder))


def periplasm_color():
    """Background of the periplasm: between the extracellular and cytoplasmic tints."""
    return P.mix(P.fill("extracellular"), P.fill("vacuole"), 0.6)


def envelope(ax, x0, x1, y, kind="gram-", pg_layers=None, top=None, seed=4, zorder=5):
    """A cell-envelope cross-section from x0 to x1, cytoplasmic membrane mid-plane at y (cytoplasm below).

    ``kind="gram+"``: membrane (with transporters), thick multilayer peptidoglycan, wall and lipoteichoic
    acids. ``kind="gram-"``: inner membrane, periplasm with one or two peptidoglycan strands, Braun's
    lipoprotein, outer membrane with an LPS outer leaflet and porins.
    Background bands (cytoplasm, periplasm, outside) are drawn up to ``top``. Returns a dict of the
    heights of every layer (for brackets and callouts) and the x of drawn proteins.
    """
    rng = np.random.default_rng(seed)
    L = dict(im=y)
    im_lo, im_hi = y - LEAFLET - 0.02, y + LEAFLET + 0.02
    L["im_lo"], L["im_hi"] = im_lo, im_hi
    W = x1 - x0
    tr = [x0 + W * 0.22, x0 + W * 0.68]
    L["transporters"] = tr
    if kind == "gram+":
        layers = pg_layers or 7
        pg0 = im_hi + 0.42
        pg_top = peptidoglycan(ax, x0, x1, pg0, layers=layers, spacing=0.36, seed=seed, zorder=zorder + 2)
        L.update(pg_lo=pg0 - 0.08, pg_hi=pg_top)
        top = top or pg_top + 1.4
        _band(ax, x0, x1, y - 1.3, y, P.fill("cytoplasm"), zorder)
        _band(ax, x0, x1, y, im_hi + 0.42 - 0.1, periplasm_color(), zorder)
        _band(ax, x0, x1, im_hi + 0.32, top, P.fill("extracellular"), zorder)
        # wall-associated background tint to read the wall as one layer
        _band(ax, x0, x1, pg0 - 0.12, pg_top + 0.05, P.mix(P.fill("extracellular"), P.fill(_tok("nag")), 0.22), zorder + 0.5)
        bilayer(ax, x0, x1, y, skip=[(t - 0.42, t + 0.42) for t in tr], zorder=zorder + 1)
        for t in tr:
            transporter(ax, t, y, zorder=zorder + 4)
        # wall teichoic acids (from the outer PG strands) and lipoteichoic acids (from the membrane)
        wta, lta = [], []
        for k, fx in enumerate(np.linspace(0.06, 0.94, 9)):
            xx = x0 + W * fx + rng.uniform(-0.05, 0.05)
            if any(abs(xx - t) < 0.5 for t in tr):
                continue
            if k % 2 == 0:
                tip = teichoic_acid(ax, (xx, pg0 + 0.36 * (layers - 3)), pg_top + rng.uniform(0.6, 0.95), anchor="wall",
                                    zorder=zorder + 5)
                wta.append((xx, tip))
            else:
                tip = teichoic_acid(ax, (xx, im_hi - HEAD), pg_top + rng.uniform(0.25, 0.55), anchor="lipid", zorder=zorder + 5)
                lta.append((xx, tip))
        L.update(wta=wta, lta=lta, top=top, bottom=y - 1.3)
        return L
    # gram-negative
    peri_h = 2.0
    om = im_hi + peri_h + LEAFLET + 0.02
    om_lo, om_hi = om - LEAFLET - 0.02, om + LEAFLET + 0.02
    pg_y = om_lo - 0.55
    top = top or om_hi + 2.1
    _band(ax, x0, x1, y - 1.3, y, P.fill("cytoplasm"), zorder)
    _band(ax, x0, x1, y, om, periplasm_color(), zorder)
    _band(ax, x0, x1, om, top, P.fill("extracellular"), zorder)
    bilayer(ax, x0, x1, y, skip=[(t - 0.42, t + 0.42) for t in tr], zorder=zorder + 1)
    for t in tr:
        transporter(ax, t, y, zorder=zorder + 4)
    layers = pg_layers or 1
    pg_top = peptidoglycan(ax, x0, x1, pg_y, layers=layers, spacing=0.3, seed=seed, zorder=zorder + 2)
    pr = [x0 + W * 0.36, x0 + W * 0.83]
    lpp = [x0 + W * 0.12, x0 + W * 0.69]
    for xx in lpp:
        lipoprotein(ax, xx, pg_top, om, zorder=zorder + 3)
    skip = [(p - 0.55, p + 0.55) for p in pr]
    leaflet(ax, x0, x1, om, -1, skip=skip + [(xx - 0.05, xx + 0.05) for xx in lpp], zorder=zorder + 1)
    tips = []
    xs = np.arange(x0 + 0.24, x1 - 0.2, 0.44)
    for k, xx in enumerate(xs):
        if not _free(xx, [(p - 0.68, p + 0.68) for p in pr]):
            continue
        units = int(rng.integers(1, 5)) if k % 3 else 0  # LPS chains vary in length; some are rough (no O-antigen)
        tips.append(lps(ax, xx, om, o_units=units, seed=seed + k, zorder=zorder + 3))
    for p in pr:
        porin(ax, p, om, zorder=zorder + 4)
    L.update(om=om, om_lo=om_lo, om_hi=om_hi, pg_lo=pg_y - 0.08, pg_hi=pg_top, porins=pr, lipoproteins=lpp,
             lps_x=list(xs), lps_tips=tips, lipid_a=om_hi, core=om_hi + 0.55, top=top, bottom=y - 1.3)
    return L


# ------------------------------------------------------------------ growth


def batch_growth(t, mu_max=1.0, Ks=0.01, Y=1.7e9, S0=2.0, N0=1e5, q0=0.2, kd=0.0, tau_s=6.0):
    """Batch culture: Monod growth on one limiting substrate, a Baranyi-Roberts lag and death after starvation.

        dN/dt = (alpha mu_max S / (Ks + S) - kd sigma) N        alpha = q / (1 + q),   dq/dt = mu_max q
        dS/dt = -alpha mu_max S / (Ks + S) N / Y                dsigma/dt = (Ks / (Ks + S) - sigma) / tau_s

    N in cells per mL, S in g/L, Y in cells mL^-1 per g L^-1. The physiological state q0 sets the lag
    lambda = ln(1 + 1/q0) / mu_max; sigma (0..1) is the starvation level, which rises with time constant
    tau_s once the substrate is exhausted, so a stationary plateau precedes first-order death (rate kd).
    Returns (t, N, S).
    """
    from scipy.integrate import solve_ivp

    def f(_, u):
        lnN, S, lnq, sig = u
        q = math.exp(min(lnq, 50.0))
        S = max(S, 0.0)
        g = q / (1 + q) * mu_max * S / (Ks + S)
        N = math.exp(lnN)
        return [g - kd * sig, -g * N / Y, mu_max, (Ks / (Ks + S) - sig) / tau_s]

    t = np.asarray(t, float)
    sol = solve_ivp(f, (t[0], t[-1]), [math.log(N0), S0, math.log(q0), 0.0], t_eval=t, method="LSODA", rtol=1e-8,
                    atol=1e-10)
    return t, np.exp(sol.y[0]), np.maximum(sol.y[1], 0)


def lag_time(mu_max, q0):
    """Baranyi lag: lambda = ln(1 + 1/q0) / mu_max."""
    return math.log(1 + 1 / q0) / mu_max


def monod(S, mu_max, Ks):
    """Monod specific growth rate mu(S) = mu_max S / (Ks + S)."""
    S = np.asarray(S, float)
    return mu_max * S / (Ks + S)


def gompertz(t, y0, A, mu, lam):
    """Zwietering (1990) modified Gompertz curve for log10 counts: maximum specific rate mu (log10 per h),
    lag lam (h), asymptotic increase A (log10)."""
    t = np.asarray(t, float)
    return y0 + A * np.exp(-np.exp(mu * math.e / A * (lam - t) + 1))


__all__ = ["TOK", "gram_token", "flagellum", "coccus", "diplococcus", "chain", "cluster", "bacillus", "vibrio", "spirillum",
           "spirochete", "leaflet", "bilayer", "peptidoglycan", "teichoic_acid", "lps", "porin", "transporter",
           "lipoprotein", "periplasm_color", "envelope", "batch_growth", "lag_time", "monod", "gompertz"]
