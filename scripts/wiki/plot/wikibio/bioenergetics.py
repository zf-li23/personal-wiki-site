"""Oxidative phosphorylation: the inner mitochondrial membrane, the respiratory chain and ATP synthase.

    from wikibio import bioenergetics as be
    lim = be.inner_membrane(ax, (0.5, 21), y=8)         intermembrane space (P side) above, matrix (N side) below
    c1 = be.complex_i(ax, 3, 8)                         complexes return anchors (dicts of canvas points)
    c2 = be.complex_ii(ax, 6.6, 8)
    be.ubiquinone(ax, (8, 8), reduced=True)
    c3 = be.complex_iii(ax, 10.2, 8);  be.cytochrome_c(ax, (12, 9.6))
    c4 = be.complex_iv(ax, 13.8, 8)
    s = be.atp_synthase(ax, 18, 8, c_ring=8)
    be.electron_arrow(ax, a, b);  be.proton_arrow(ax, a, b, text="4 H⁺")
    A = be.respiratory_chain(ax, (0.5, 21), 8)         the whole chain with its electron and proton paths
    be.f1_top(ax, (4, 4), 1.3, states=("ATP", "empty", "ADP"), gamma=90)   F1 seen from the membrane
    be.c_ring(ax, (4, 4), 0.9, n=8)                   the c ring of Fo seen from above

Orientation: the N side (matrix: negative, alkaline) is below the membrane by default, as in most
textbook drawings; ``n_side="top"`` puts it above, which matches the stroma-up thylakoid of
``photosynthesis`` in side-by-side comparisons (the P side is always the other one). Peripheral domains
are drawn on the side where they sit in the cell: the matrix arm of Complex I, the succinate-binding
head of Complex II and F1 on the N side; the Rieske/cytochrome c1 domain of Complex III, the CuA
domain of Complex IV and cytochrome c on the P side.

Colours are tokens, named once in ``COLOR`` so every figure draws a complex in the same colour.
Homologous carriers share colours with ``photosynthesis``: Complex III and cytochrome b6f are purple,
ubiquinone and plastoquinone pale yellow, both ATP synthases pink; electrons are blue and protons red.

Models (pure functions): ``pmf`` (proton-motive force as the free energy per mole of protons),
``h_per_atp`` (protons per ATP from the c-ring size) and ``p_o`` (P/O ratio).
"""

import math

import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch, Polygon, Rectangle, Wedge

from . import palette as P
from .cell import bilayer
from .core import LINE, arrow, blob, label, shape
from .quant import line_color

MH = 0.37  # membrane half-thickness, as in cellbio and photosynthesis

# object -> palette token (aliases where the photosynthesis module already named one)
COLOR = {
    "complex_i": "channel", "complex_ii": "carbohydrate", "complex_iii": "cytb6f", "cyt_c": "drug",
    "complex_iv": "antibody", "q": "plastoquinone", "atp_synthase": "atp_synthase", "stalk": "neutral",
    "fes": "ca", "flavin": "highlight", "heme": "drug", "cu": "channel", "carrier": "neutral", "ucp": "positive",
    "electron": "dna", "proton": "h", "ims": "mitochondrion", "matrix": "matrix",
}


def _ns(n_side):
    """+1 when the N side (matrix) is above the membrane, -1 when it is below."""
    return 1 if n_side == "top" else -1


def tint(token, light=0.62, dark=0.8):
    """A pale tint of a token's fill towards the page background (compartment washes)."""
    return P.mix(P.fill(token), P.surface(), dark if P.is_dark() else light)


def _body(ax, center, rx, ry, token, seed, zorder=11, wobble=0.07):
    shape(ax, blob(center, rx, ry, wobble=wobble, seed=seed, k=10), token, lw=LINE * 0.9, zorder=zorder)


def _name(ax, xy, text, size="small", zorder=14):
    label(ax, xy, text, size=size, bold=True, color=P.on_fill(), zorder=zorder)


def _dot(ax, xy, token, r=0.07, zorder=13):
    ax.add_patch(Circle(xy, r, facecolor=P.fill(token), edgecolor=P.edge(token), lw=0.55, zorder=zorder))


def inner_membrane(ax, xr, y, ims=3.0, matrix=3.0, n_side="bottom", names=True, label_x=None,
                   ims_text="Intermembrane space (P side)", matrix_text="Matrix (N side)", zorder=0):
    """Intermembrane space and matrix washes around the inner mitochondrial membrane (a bilayer from
    xr[0] to xr[1] at height y). ``ims`` and ``matrix`` are the heights of the two washes.

    Returns {"ims": far edge of the P-side wash, "matrix": far edge of the N-side wash, "p": +1/-1, "n": +1/-1}.
    """
    ns = _ns(n_side)
    x0, x1 = xr
    p_lo, p_h = (y + MH, ims) if ns < 0 else (y - MH - ims, ims)
    n_lo, n_h = (y - MH - matrix, matrix) if ns < 0 else (y + MH, matrix)
    ax.add_patch(Rectangle((x0, p_lo), x1 - x0, p_h, facecolor=tint(COLOR["ims"], 0.72, 0.84), edgecolor="none",
                           zorder=zorder))
    ax.add_patch(Rectangle((x0, n_lo), x1 - x0, n_h, facecolor=P.fill(COLOR["matrix"]), edgecolor="none", zorder=zorder))
    bilayer(ax, [(x0, y), (x1, y)])
    p_far = y - ns * (MH + ims)
    n_far = y + ns * (MH + matrix)
    if names:
        lx = label_x if label_x is not None else x0 + 0.25
        label(ax, (lx, p_far + ns * 0.35), ims_text, size="small", bold=True, ha="left", color=P.muted())
        label(ax, (lx, n_far - ns * 0.35), matrix_text, size="small", bold=True, ha="left", color=P.muted())
    return {"ims": p_far, "matrix": n_far, "p": -ns, "n": ns}


def complex_i(ax, x, y, text="I", n_side="bottom", zorder=11):
    """Complex I (NADH:ubiquinone oxidoreductase): an L-shaped complex, the hydrophilic arm with FMN and
    the chain of Fe–S clusters projecting into the matrix at ``x`` and the membrane arm extending to the left.

    Anchors: ``nadh`` (tip of the matrix arm, where NADH binds), ``fmn``, ``n2`` (last Fe–S cluster),
    ``q`` (quinone site at the base of the arm), ``pumps`` (x positions of the four proton paths in the
    membrane arm), ``top``, ``bottom``, ``center`` (of the membrane arm).
    """
    ns = _ns(n_side)
    tok = COLOR["complex_i"]
    _body(ax, (x - 0.8, y), 1.45, 0.56, tok, 51, zorder=zorder)
    arm = (x + 0.35, y + ns * 1.3)
    _body(ax, arm, 0.55, 1.08, tok, 52, zorder=zorder + 1)
    fmn = (x + 0.2, y + ns * 2.0)
    _dot(ax, fmn, COLOR["flavin"], r=0.09, zorder=zorder + 3)
    chain = [(x + 0.18 + 0.12 * (k % 2), y + ns * (1.72 - 0.3 * k)) for k in range(5)]
    for p in chain:
        _dot(ax, p, COLOR["fes"], r=0.065, zorder=zorder + 3)
    pumps = [x - 1.95 + 0.42 * k for k in range(4)]
    _name(ax, (arm[0] + 0.32, arm[1] + ns * 0.15), text)
    return {"nadh": (x + 0.35, y + ns * 2.4), "fmn": fmn, "n2": chain[-1], "q": (x + 0.5, y + ns * 0.3),
            "pumps": pumps, "top": (x - 0.8, y - ns * 0.56), "bottom": (x + 0.35, y + ns * 2.4),
            "center": (x - 0.8, y)}


def complex_ii(ax, x, y, text="II", n_side="bottom", zorder=11):
    """Complex II (succinate dehydrogenase): a small membrane anchor (subunits C, D with heme b) and the
    matrix head (A with FAD, B with three Fe–S clusters). It pumps no protons.

    Anchors: ``succinate`` (outer edge of the head), ``fad``, ``q`` (quinone site in the anchor), ``top``, ``bottom``.
    """
    ns = _ns(n_side)
    tok = COLOR["complex_ii"]
    _body(ax, (x, y), 0.4, 0.55, tok, 61, zorder=zorder)
    head = (x, y + ns * 1.1)
    _body(ax, head, 0.58, 0.6, tok, 62, zorder=zorder + 1)
    fad = (x - 0.12, y + ns * 1.35)
    _dot(ax, fad, COLOR["flavin"], r=0.09, zorder=zorder + 3)
    for k in range(3):
        _dot(ax, (x + 0.12 - 0.06 * k, y + ns * (1.0 - 0.25 * k)), COLOR["fes"], r=0.06, zorder=zorder + 3)
    _dot(ax, (x - 0.05, y - ns * 0.15), COLOR["heme"], r=0.06, zorder=zorder + 3)
    _name(ax, (x + 0.2, y + ns * 1.05), text, size="tiny")
    return {"succinate": (x, y + ns * 1.72), "fad": fad, "q": (x + 0.15, y + ns * 0.2),
            "top": (x, y - ns * 0.55), "bottom": (x, y + ns * 1.72)}


def complex_iii(ax, x, y, text="III", n_side="bottom", zorder=11):
    """Complex III (cytochrome bc1 complex), a dimer, with the Rieske Fe–S / cytochrome c1 domain on the P side.

    Anchors: ``qp`` (quinol-oxidizing site, P side), ``qn`` (quinone-reducing site, N side), ``bl``, ``bh``
    (the two hemes of cytochrome b), ``rieske``, ``c1`` (cytochrome c1 domain), ``top``, ``bottom``.
    """
    ns = _ns(n_side)
    tok = COLOR["complex_iii"]
    for dx, seed in ((-0.5, 71), (0.5, 72)):
        _body(ax, (x + dx, y + ns * 0.05), 0.55, 0.85, tok, seed, zorder=zorder)
    c1 = (x + 0.6, y - ns * 1.02)
    _body(ax, c1, 0.42, 0.32, tok, 73, zorder=zorder + 1)
    _dot(ax, c1, COLOR["heme"], r=0.08, zorder=zorder + 3)
    rieske = (x + 0.15, y - ns * 0.62)
    _dot(ax, rieske, COLOR["fes"], r=0.07, zorder=zorder + 3)
    bl, bh = (x - 0.45, y - ns * 0.22), (x - 0.45, y + ns * 0.28)
    for p in (bl, bh):
        _dot(ax, p, COLOR["heme"], r=0.065, zorder=zorder + 3)
    _name(ax, (x + 0.42, y + ns * 0.12), text)
    return {"qp": (x - 0.9, y - ns * 0.3), "qn": (x - 0.9, y + ns * 0.35), "bl": bl, "bh": bh, "rieske": rieske,
            "c1": c1, "top": (x, y - ns * 0.9), "bottom": (x, y + ns * 0.9)}


def cytochrome_c(ax, center, r=0.27, text="c", zorder=13):
    """Cytochrome c, the small soluble heme protein of the intermembrane space. Returns its centre."""
    tok = COLOR["cyt_c"]
    ax.add_patch(Circle(center, r, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.9, zorder=zorder))
    if text:
        label(ax, center, text, size="tiny", bold=True, italic=True, color=P.on_fill(), zorder=zorder + 1)
    return center


def complex_iv(ax, x, y, text="IV", n_side="bottom", zorder=11):
    """Complex IV (cytochrome oxidase) with the CuA domain of subunit II on the P side; hemes a and a3 and
    CuB form the oxygen-reducing centre in the membrane.

    Anchors: ``cua`` (where cytochrome c delivers electrons), ``a``, ``a3cub`` (the binuclear centre),
    ``o2`` (N-side point where O2 is reduced with substrate protons), ``top``, ``bottom``.
    """
    ns = _ns(n_side)
    tok = COLOR["complex_iv"]
    _body(ax, (x, y + ns * 0.05), 0.72, 0.86, tok, 81, zorder=zorder)
    cua = (x + 0.3, y - ns * 1.02)
    _body(ax, cua, 0.45, 0.3, tok, 82, zorder=zorder + 1)
    for dx in (-0.07, 0.07):
        _dot(ax, (cua[0] + dx, cua[1]), COLOR["cu"], r=0.06, zorder=zorder + 3)
    a, a3 = (x + 0.25, y - ns * 0.1), (x - 0.15, y + ns * 0.12)
    _dot(ax, a, COLOR["heme"], r=0.065, zorder=zorder + 3)
    _dot(ax, a3, COLOR["heme"], r=0.065, zorder=zorder + 3)
    _dot(ax, (a3[0] - 0.15, a3[1]), COLOR["cu"], r=0.055, zorder=zorder + 3)
    _name(ax, (x - 0.1, y + ns * 0.5), text)
    return {"cua": cua, "a": a, "a3cub": a3, "o2": (x - 0.3, y + ns * 1.05), "top": (x, y - ns * 0.86),
            "bottom": (x, y + ns * 0.9)}


def ubiquinone(ax, center, reduced=False, r=0.2, label_dy=0.6, text=None, zorder=14):
    """Ubiquinone (Q) or ubiquinol (QH2): a quinone ring with its isoprenoid tail, freely diffusing in
    the bilayer. The name goes ``label_dy`` below the centre (negative: above)."""
    cx, cy = center
    tok = COLOR["q"]
    th = np.radians(np.arange(6) * 60 + 30)
    ring = np.c_[cx + r * np.cos(th), cy + r * np.sin(th)]
    ax.plot([cx + r * 0.85, cx + r * 3.1], [cy, cy - r * 0.35], color=P.edge(tok), lw=1.1, zorder=zorder - 1,
            solid_capstyle="round")
    ax.add_patch(Polygon(ring, closed=True, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.9, zorder=zorder))
    t = text if text is not None else ("QH₂" if reduced else "Q")
    if t:
        label(ax, (cx, cy - label_dy), t, size="tiny", va="top" if label_dy > 0 else "bottom", zorder=zorder + 1)
    return center


def atp_synthase(ax, x, y, text="ATP synthase", c_ring=8, n_side="bottom", zorder=11):
    """Mitochondrial ATP synthase: Fo in the membrane (c ring and subunit a with its two half-channels)
    and the F1 head (alpha3 beta3) on the N side, joined by the central (gamma, epsilon) and peripheral (b) stalks.

    ``c_ring`` sets the number of stripes drawn on the ring (half of the c subunits are visible).
    Anchors: ``channel`` (proton path at subunit a), ``a``, ``ring``, ``head`` (F1 centre), ``top``, ``bottom``.
    """
    ns = _ns(n_side)
    tok, st = COLOR["atp_synthase"], COLOR["stalk"]
    w = 1.3
    ax.add_patch(FancyBboxPatch((x - w / 2, y - MH - 0.08), w, 2 * MH + 0.16, boxstyle="round,pad=0,rounding_size=0.14",
                                facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=LINE * 0.9, zorder=zorder))
    nstripe = max(3, int(round(c_ring / 2)))
    for k in range(1, nstripe):
        xx = x - w / 2 + k * w / nstripe
        ax.plot([xx, xx], [y - MH + 0.02, y + MH - 0.02], color=P.edge(tok), lw=0.6, zorder=zorder + 1)
    ax_ = x + w / 2 + 0.16
    ax.add_patch(FancyBboxPatch((x + w / 2 - 0.02, y - MH - 0.02), 0.36, 2 * MH + 0.04,
                                boxstyle="round,pad=0,rounding_size=0.1", facecolor=P.fill(st), edgecolor=P.edge(st),
                                lw=LINE * 0.8, zorder=zorder))
    # peripheral stalk from subunit a to the top of F1, central stalk from the ring into F1
    y0s = y + MH if ns > 0 else y - MH - 1.55
    ax.add_patch(FancyBboxPatch((x + w / 2 + 0.06, y0s), 0.16, 1.55, boxstyle="round,pad=0,rounding_size=0.07",
                                facecolor=P.fill(st), edgecolor=P.edge(st), lw=LINE * 0.8, zorder=zorder - 1))
    y0c = y + MH if ns > 0 else y - MH - 1.05
    ax.add_patch(FancyBboxPatch((x - 0.11, y0c), 0.22, 1.05, boxstyle="round,pad=0,rounding_size=0.08",
                                facecolor=P.fill(st), edgecolor=P.edge(st), lw=LINE * 0.8, zorder=zorder - 1))
    hy = y + ns * (MH + 1.45)
    for k, dx in enumerate((-0.55, -0.18, 0.18, 0.55)):
        ax.add_patch(FancyBboxPatch((x + dx - 0.2, hy - 0.5), 0.4, 1.0, boxstyle="round,pad=0,rounding_size=0.18",
                                    facecolor=P.fill(tok) if k % 2 == 0 else P.light(tok), edgecolor=P.edge(tok),
                                    lw=LINE * 0.85, zorder=zorder + (1 if k in (1, 2) else 0)))
    label(ax, (x, y - ns * (MH + 0.3)), "F$_\\mathrm{o}$", size="tiny", va="top" if ns > 0 else "bottom", zorder=zorder + 3)
    label(ax, (x - 0.95, hy), "F$_1$", size="tiny", ha="right", zorder=zorder + 3)
    if text:
        label(ax, (x, hy + ns * 0.65), text, size="small", bold=True, va="bottom" if ns > 0 else "top", zorder=zorder + 3)
    return {"channel": (ax_, y), "a": (ax_, y), "ring": (x, y), "head": (x, hy), "top": (x, y - ns * (MH + 0.1)),
            "bottom": (x, hy + ns * 0.5)}


def carrier(ax, x, y, text=None, token=None, width=0.7, zorder=11):
    """A generic inner-membrane carrier (adenine nucleotide translocase, phosphate carrier, UCP1): a
    two-lobed body spanning the bilayer. Returns its centre."""
    tok = token or COLOR["carrier"]
    for dx, seed in ((-width / 4, 91), (width / 4, 92)):
        _body(ax, (x + dx, y), width / 4 + 0.05, MH + 0.2, tok, seed + int(10 * x) % 7, zorder=zorder)
    if text:
        _name(ax, (x, y), text, size="tiny")
    return (x, y)


def proton(ax, center, text="H⁺", r=0.13, side="right", zorder=17):
    """A proton (small disc in the H+ token) with its label beside it."""
    ax.add_patch(Circle(center, r, facecolor=P.fill(COLOR["proton"]), edgecolor=P.edge(COLOR["proton"]), lw=0.7,
                        zorder=zorder))
    if text:
        dx = r + 0.05
        label(ax, (center[0] + (dx if side == "right" else -dx), center[1]), text, size="tiny",
              ha="left" if side == "right" else "right", zorder=zorder + 1)


def electron_arrow(ax, a, b, bend=0.0, lw=1.6, dashed=False, head=0.2, zorder=16):
    """An electron-transfer step (blue process arrow) from a to b."""
    return arrow(ax, a, b, kind="process", color=line_color(COLOR["electron"]), lw=lw, head=head, bend=bend,
                 dashed=dashed, zorder=zorder)


def proton_arrow(ax, a, b, text=None, side="right", bend=0.0, lw=1.3, disc="start", dashed=False, zorder=17):
    """A proton movement (red process arrow) from a to b, with a labelled proton disc at the start
    (``disc="start"``), at the end (``"end"``) or none (``None``)."""
    arrow(ax, a, b, kind="process", color=line_color(COLOR["proton"]), lw=lw, head=0.18, bend=bend, dashed=dashed,
          zorder=zorder)
    if disc:
        proton(ax, a if disc == "start" else b, text=text, side=side, zorder=zorder + 1)


def respiratory_chain(ax, xr, y, ims=3.4, matrix=3.6, complex2=True, synthase=True, protons=True, labels=True,
                      c_ring=8, n_side="bottom"):
    """The respiratory chain in the inner membrane from xr[0] to xr[1] (at least 20 units wide):
    Complexes I and II reduce the ubiquinone pool, Complex III passes electrons to cytochrome c, Complex IV
    reduces O2; with ``protons`` the per-pair proton movements (4 + 4 + 2 pumped, 2 taken up at Qn) are
    drawn, and with ``synthase`` the ATP synthase that lets them return.

    Returns a dict with the membrane limits (``lim``) and the anchors of every component
    (``c1``, ``c2``, ``c3``, ``c4``, ``q``, ``cytc``, ``atp``).
    """
    ns = _ns(n_side)
    x0 = xr[0]
    lim = inner_membrane(ax, xr, y, ims=ims, matrix=matrix, n_side=n_side, names=labels)
    ec = line_color(COLOR["electron"])
    out = {"lim": lim}
    c1 = complex_i(ax, x0 + 3.3, y, n_side=n_side)
    out["c1"] = c1
    if complex2:
        out["c2"] = complex_ii(ax, x0 + 7.0, y, n_side=n_side)
    q = (x0 + 5.35, y + ns * 0.02)
    ubiquinone(ax, q, reduced=True, label_dy=-0.45 * ns if ns < 0 else 0.45, text="QH₂")
    out["q"] = q
    c3 = complex_iii(ax, x0 + 10.3, y, n_side=n_side)
    out["c3"] = c3
    cyt = cytochrome_c(ax, (x0 + 12.15, y - ns * 1.55))
    out["cytc"] = cyt
    c4 = complex_iv(ax, x0 + 13.9, y, n_side=n_side)
    out["c4"] = c4

    # electron path
    nadh = c1["nadh"]
    electron_arrow(ax, (nadh[0] - 1.25, nadh[1] + ns * 0.35), (nadh[0] - 0.4, nadh[1] + ns * 0.05), bend=0.15 * ns)
    electron_arrow(ax, (c1["q"][0] + 0.35, c1["q"][1] - ns * 0.1), (q[0] - 0.3, q[1] + ns * 0.05), bend=-0.1 * ns)
    if complex2:
        c2 = out["c2"]
        s0 = c2["succinate"]
        electron_arrow(ax, (s0[0] - 0.95, s0[1] + ns * 0.4), (s0[0] - 0.3, s0[1] + ns * 0.02), bend=0.2 * ns)
        electron_arrow(ax, (c2["q"][0] - 0.45, c2["q"][1]), (q[0] + 0.45, q[1] + ns * 0.12), bend=0.1 * ns)
    electron_arrow(ax, (q[0] + 0.1, q[1] - ns * 0.3), (c3["qp"][0] + 0.05, c3["qp"][1] - ns * 0.05),
                   bend=-0.22 * ns if complex2 else 0.0, dashed=complex2)
    electron_arrow(ax, (c3["c1"][0] + 0.38, c3["c1"][1] - ns * 0.05), (cyt[0] - 0.3, cyt[1] + ns * 0.05), bend=-0.2 * ns)
    electron_arrow(ax, (cyt[0] + 0.3, cyt[1] + ns * 0.05), (c4["cua"][0] - 0.42, c4["cua"][1] - ns * 0.05),
                   bend=-0.2 * ns)
    if labels:
        label(ax, (nadh[0] - 1.35, nadh[1] + ns * 0.6), "NADH", size="tiny", ha="center")
        label(ax, (nadh[0] + 0.85, nadh[1] + ns * 0.45), "NAD⁺ + H⁺", size="tiny", ha="center")
        if complex2:
            s0 = out["c2"]["succinate"]
            label(ax, (s0[0] - 1.1, s0[1] + ns * 0.65), "Succinate", size="tiny")
            label(ax, (s0[0] + 0.95, s0[1] + ns * 0.45), "Fumarate", size="tiny")
        o2 = c4["o2"]
        label(ax, (o2[0] + 0.1, o2[1] + ns * 0.45), "½O₂ + 2H⁺ → H₂O", size="tiny", ha="center")
    if protons:
        pz = y - ns * (MH + 1.2)  # where pumped protons end on the P side
        nz = y + ns * (MH + 0.9)
        for k, px in enumerate(c1["pumps"]):
            proton_arrow(ax, (px, nz + ns * 0.55), (px, pz + ns * 0.3), text="H⁺" if k == 3 else None, disc="end",
                         side="right")
        label(ax, (c1["pumps"][0] - 0.25, pz - ns * 0.05), "4 H⁺", size="tiny", ha="right", color=line_color(COLOR["proton"]))
        proton_arrow(ax, (c3["qn"][0] + 0.1, nz + ns * 0.55), (c3["qn"][0] + 0.25, c3["qn"][1] + ns * 0.05), text="2 H⁺",
                     side="left")
        proton_arrow(ax, (c3["qp"][0] + 0.2, c3["qp"][1] - ns * 0.15), (c3["qp"][0] - 0.25, pz), text="4 H⁺", disc="end",
                     side="left")
        proton_arrow(ax, (c4["a3cub"][0] + 1.1, nz + ns * 0.55), (c4["a3cub"][0] + 1.1, pz + ns * 0.3), text="2 H⁺",
                     disc="end", side="right")
    if synthase:
        s = atp_synthase(ax, xr[1] - 3.2, y, c_ring=c_ring, n_side=n_side)
        out["atp"] = s
        ch = s["channel"]
        if protons:
            proton_arrow(ax, (ch[0], y - ns * (MH + 1.3)), (ch[0], y + ns * (MH + 0.3)), text="H⁺",
                         side="right", lw=1.8)
        hd = s["head"]
        arrow(ax, (hd[0] - 1.35, hd[1] - ns * 0.35), (hd[0] - 1.35, hd[1] + ns * 0.55), kind="process", color=P.ink(),
              lw=1.1, head=0.16)
        label(ax, (hd[0] - 1.5, hd[1] - ns * 0.55), "ADP + Pᵢ", size="tiny", ha="center")
        label(ax, (hd[0] - 1.45, hd[1] + ns * 0.8), "ATP", size="tiny", bold=True, ha="center")
    return out


def f1_top(ax, center, r, states=("ATP", "empty", "ADP"), gamma=None, start=90.0, names=True, zorder=10):
    """The F1 head seen from the membrane: three alpha and three beta subunits arranged like the
    segments of an orange around the central gamma subunit, whose asymmetric protrusion points at angle
    ``gamma`` (degrees; by default at the open beta subunit, which gamma holds in the empty conformation). ``states`` are the beta conformations clockwise from ``start``: "ATP" (beta-ATP,
    tight), "ADP" (beta-ADP, loose) or "empty" (open); each is labelled and the bound nucleotide drawn.

    Returns {"beta": [centres], "alpha": [centres], "gamma": tip}.
    """
    cx, cy = center
    tok = COLOR["atp_synthase"]
    betas, alphas = [], []
    for k in range(6):
        ang = math.radians(start - 60 * k)
        c = (cx + 0.62 * r * math.cos(ang), cy + 0.62 * r * math.sin(ang))
        is_beta = k % 2 == 0
        rr = 0.36 * r if is_beta else 0.33 * r
        if is_beta:
            st = states[k // 2]
            # an open beta subunit is drawn slightly swollen and paler
            f = P.light(tok) if st == "empty" else P.fill(tok)
            ax.add_patch(Circle(c, rr * (1.06 if st == "empty" else 1.0), facecolor=f, edgecolor=P.edge(tok),
                                lw=LINE * 0.9, zorder=zorder + 1))
            betas.append(c)
            if st in ("ATP", "ADP"):
                ax.add_patch(Circle(c, rr * 0.38, facecolor=P.fill("atp" if st == "ATP" else "metabolite"),
                                    edgecolor=P.edge("atp" if st == "ATP" else "metabolite"), lw=0.7, zorder=zorder + 2))
            if names:
                tx = {"ATP": "β-ATP", "ADP": "β-ADP", "empty": "β-empty"}[st]
                if math.sin(ang) > 0.5:
                    lp, va = (c[0], c[1] + rr + 0.08 * r), "bottom"
                    ha = "center"
                else:
                    sx = 1 if math.cos(ang) > 0 else -1
                    lp, va = (c[0] + sx * 0.12 * r, c[1] - rr - 0.06 * r), "top"
                    ha = "left" if sx > 0 else "right"
                label(ax, lp, tx, size="tiny", va=va, ha=ha, zorder=zorder + 3)
        else:
            ax.add_patch(Circle(c, rr, facecolor=P.fill(COLOR["stalk"]), edgecolor=P.edge(COLOR["stalk"]), lw=LINE * 0.8,
                                zorder=zorder))
            alphas.append(c)
    # gamma: a small hub with an eccentric lobe
    if gamma is None:
        k = list(states).index("empty") if "empty" in states else 0
        gamma = start - 120 * k
    g = math.radians(gamma)
    tip = (cx + 0.3 * r * math.cos(g), cy + 0.3 * r * math.sin(g))
    ax.add_patch(Wedge((cx, cy), 0.34 * r, gamma - 35, gamma + 35, facecolor=P.fill("positive"), edgecolor=P.edge("positive"),
                       lw=0.8, zorder=zorder + 4))
    ax.add_patch(Circle((cx, cy), 0.15 * r, facecolor=P.fill("positive"), edgecolor=P.edge("positive"), lw=0.8,
                        zorder=zorder + 4))
    return {"beta": betas, "alpha": alphas, "gamma": tip}


def c_ring(ax, center, r, n=8, mark=True, zorder=10):
    """The c ring of Fo seen along the rotation axis: ``n`` c subunits, each with its essential
    carboxylate (Glu or Asp) marked on the outer face. Returns the subunit centres."""
    cx, cy = center
    tok = COLOR["atp_synthase"]
    rs = min(0.95 * r * math.sin(math.pi / n), 0.35 * r)
    pts = []
    for k in range(n):
        ang = math.radians(90 - 360 * k / n)
        p = (cx + r * math.cos(ang), cy + r * math.sin(ang))
        ax.add_patch(Circle(p, rs, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=LINE * 0.8, zorder=zorder))
        if mark:
            q = (cx + (r + rs * 0.55) * math.cos(ang), cy + (r + rs * 0.55) * math.sin(ang))
            ax.add_patch(Circle(q, rs * 0.25, facecolor=P.fill("negative"), edgecolor=P.edge("negative"), lw=0.5,
                                zorder=zorder + 1))
        pts.append(p)
    return pts


# ----------------------------------------------------------------------- models
F = 96.485  # Faraday constant, kJ V^-1 mol^-1
R = 8.314462618e-3  # gas constant, kJ K^-1 mol^-1


def pmf(dpH, dpsi, T=310.15):
    """Free energy released when one mole of protons returns from the P to the N side (kJ/mol, positive):
    2.303 R T dpH + F dpsi, with dpH = pH(N) - pH(P) and dpsi = psi(P) - psi(N) in volts."""
    return math.log(10) * R * T * dpH + F * dpsi


def h_per_atp(c, transport=1.0):
    """Protons per ATP: c/3 through Fo (c subunits per ring, three ATP per turn) plus ``transport`` for
    the phosphate carrier (and the electrogenic ATP/ADP exchange)."""
    return c / 3.0 + transport


def p_o(c, h_pumped=10.0, transport=1.0):
    """P/O ratio: protons pumped per pair of electrons (10 from NADH, 6 from succinate) divided by protons per ATP."""
    return h_pumped / h_per_atp(c, transport)


__all__ = ["COLOR", "MH", "tint", "inner_membrane", "complex_i", "complex_ii", "complex_iii", "cytochrome_c",
           "complex_iv", "ubiquinone", "atp_synthase", "carrier", "proton", "electron_arrow", "proton_arrow",
           "respiratory_chain", "f1_top", "c_ring", "pmf", "h_per_atp", "p_o", "F", "R"]
