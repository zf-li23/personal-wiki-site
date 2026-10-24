"""Photosynthesis: the thylakoid membrane with its complexes, the Z-scheme and leaf gas-exchange models.

    from wikibio import photosynthesis as ps
    ps.thylakoid(ax, (0.5, 27.5), y=15)                  stroma (top) and lumen (bottom) around a bilayer
    a = ps.psii(ax, 4.5, 15)                              complexes return anchors (dicts of canvas points)
    ps.plastoquinone(ax, (7.5, 15), reduced=True)
    b = ps.cytb6f(ax, 10.5, 15);  ps.plastocyanin(ax, (12.4, 13.4))
    c = ps.psi(ax, 15, 15);  ps.ferredoxin(ax, (17, 16.6));  ps.fnr(ax, 19, 15)
    d = ps.atp_synthase(ax, 24, 15)
    ps.photon(ax, (2, 18.3), a["antenna"]);  ps.proton(ax, (6, 13))
    ps.z_scheme(ax, (2.5, 1.0, 24, 8))                    the Z-scheme on a midpoint-potential axis
    L = ps.leaf_section(ax, (0.5, 4, 7, 5), stoma_x=4)    a C3 leaf cross-section (anchors: pore, cavity, plastid)

Membrane proteins sit in a membrane centred at height y with half-thickness ``MH`` (as in ``cellbio``);
the stroma is above, the lumen below. Colours are tokens, named once in ``COLOR`` so every figure
draws a complex in the same colour (PSII teal, cytochrome b6f purple, PSI green, plastocyanin blue,
ferredoxin red-brown, FNR yellow, ATP synthase pink, plastoquinone pale yellow).

Models (pure functions): ``farquhar`` (C3 A/Ci, Farquhar, von Caemmerer & Berry 1980 with the 25 °C
kinetic constants of Bernacchi et al. 2001) and ``light_response`` (non-rectangular hyperbola).
"""

import math

import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch, Polygon, Rectangle

from . import palette as P
from .cell import bilayer
from .core import LINE, arrow, blob, box, label, shape
from .quant import Plot, line_color

MH = 0.37

# complex -> palette token (proposed dedicated tokens are listed in the gallery report)
COLOR = {
    "psii": "psii", "lhc": "lhc", "pq": "plastoquinone", "b6f": "cytb6f", "pc": "plastocyanin", "psi": "psi",
    "fd": "ferredoxin", "fnr": "fnr", "atp_synthase": "atp_synthase", "stalk": "neutral", "oec": "metabolite",
    "electron": "dna", "proton": "h", "light": "highlight",
}


def tint(token, light=0.62, dark=0.8):
    """A pale tint of a token's fill towards the page background (compartment washes)."""
    return P.mix(P.fill(token), P.surface(), dark if P.is_dark() else light)


def thylakoid(ax, xr, y, stroma=3.2, lumen=2.6, names=True, label_x=None, zorder=0):
    """Stroma (above) and thylakoid lumen (below) washes around a lipid bilayer from xr[0] to xr[1] at height y."""
    x0, x1 = xr
    ax.add_patch(Rectangle((x0, y + MH), x1 - x0, stroma, facecolor=tint("chloroplast", 0.55, 0.82), edgecolor="none",
                           zorder=zorder))
    ax.add_patch(Rectangle((x0, y - MH - lumen), x1 - x0, lumen, facecolor=tint("h", 0.72, 0.84), edgecolor="none",
                           zorder=zorder))
    bilayer(ax, [(x0, y), (x1, y)])
    if names:
        lx = label_x if label_x is not None else x0 + 0.25
        label(ax, (lx, y + MH + stroma - 0.35), "Stroma", size="small", bold=True, ha="left", color=P.muted())
        label(ax, (lx, y - MH - lumen + 0.35), "Thylakoid lumen", size="small", bold=True, ha="left", color=P.muted())
    return {"stroma": y + MH + stroma, "lumen": y - MH - lumen}


def _body(ax, center, rx, ry, token, seed, zorder=11, wobble=0.07):
    shape(ax, blob(center, rx, ry, wobble=wobble, seed=seed, k=10), token, lw=LINE * 0.9, zorder=zorder)


def _name(ax, xy, text, size="small", zorder=14):
    label(ax, xy, text, size=size, bold=True, color=P.on_fill(), zorder=zorder)


def _chl_pair(ax, xy, zorder=13):
    # the special-pair chlorophylls (P680 / P700): two small rounded plates
    for dx in (-0.09, 0.09):
        ax.add_patch(FancyBboxPatch((xy[0] + dx - 0.05, xy[1] - 0.16), 0.1, 0.32, boxstyle="round,pad=0,rounding_size=0.04",
                                    facecolor=P.fill("thylakoid"), edgecolor=P.edge("thylakoid"), lw=0.7, zorder=zorder))


def psii(ax, x, y, text="PSII", antenna=True, zorder=11):
    """Photosystem II (one monomer of the dimer) with LHCII and the oxygen-evolving complex on the lumen side.

    Anchors: ``p680``, ``qb`` (plastoquinone site, stromal side), ``oec`` (Mn4CaO5 cluster), ``antenna``.
    """
    if antenna:
        for sx, seed in ((-1, 3), (1, 4)):
            _body(ax, (x + sx * 1.0, y + 0.05), 0.34, 0.62, COLOR["lhc"], seed, zorder=zorder - 1)
        label(ax, (x - 1.0, y + 0.85), "LHCII", size="tiny", color=P.ink(), va="bottom", zorder=zorder + 4)
    _body(ax, (x, y + 0.02), 0.72, 0.98, COLOR["psii"], 11, zorder=zorder)
    _body(ax, (x + 0.12, y - 1.02), 0.46, 0.3, COLOR["oec"], 12, zorder=zorder + 1)  # PsbO and the Mn cluster
    oec = (x + 0.12, y - 1.02)
    for k, (dx, dy) in enumerate(((-0.08, 0.05), (0.08, 0.05), (-0.08, -0.08), (0.08, -0.08))):
        ax.add_patch(Circle((oec[0] + dx, oec[1] + dy), 0.055, facecolor=P.fill("k"), edgecolor=P.edge("k"), lw=0.5,
                            zorder=zorder + 3))
    ax.add_patch(Circle((oec[0] + 0.0, oec[1] - 0.015), 0.04, facecolor=P.fill("ca"), edgecolor=P.edge("ca"), lw=0.5,
                        zorder=zorder + 4))
    _chl_pair(ax, (x - 0.12, y - 0.1), zorder + 2)
    _name(ax, (x + 0.02, y + 0.55), text)
    return {"p680": (x - 0.12, y - 0.1), "qb": (x + 0.6, y + 0.2), "oec": oec, "antenna": (x - 1.0, y + 0.5),
            "top": (x, y + 1.0), "bottom": (x, y - 1.32)}


def plastoquinone(ax, center, reduced=False, r=0.2, label_dy=0.6, zorder=14):
    """A plastoquinone (PQ) or plastoquinol (PQH2) molecule: a quinone ring with its isoprenoid tail.

    The name goes ``label_dy`` below the centre (by default just outside a membrane at the same height).
    """
    cx, cy = center
    th = np.radians(np.arange(6) * 60 + 30)
    ring = np.c_[cx + r * np.cos(th), cy + r * np.sin(th)]
    ax.plot([cx + r * 0.85, cx + r * 3.1], [cy, cy - r * 0.35], color=P.edge(COLOR["pq"]), lw=1.1, zorder=zorder - 1,
            solid_capstyle="round")
    ax.add_patch(Polygon(ring, closed=True, facecolor=P.fill(COLOR["pq"]), edgecolor=P.edge(COLOR["pq"]), lw=0.9, zorder=zorder))
    label(ax, (cx, cy - label_dy), "PQH₂" if reduced else "PQ", size="tiny", va="top", zorder=zorder + 1)
    return center


def cytb6f(ax, x, y, text="Cyt b₆f", zorder=11):
    """The cytochrome b6f complex (dimer) with the Rieske / cytochrome f domains on the lumen side.

    Anchors: ``qp`` (lumen-side quinol site), ``qn`` (stroma-side site), ``f`` (cytochrome f), ``top``, ``bottom``.
    """
    tok = COLOR["b6f"]
    for dx, seed in ((-0.48, 21), (0.48, 22)):
        _body(ax, (x + dx, y + 0.08), 0.52, 0.8, tok, seed, zorder=zorder)
    _body(ax, (x + 0.55, y - 0.98), 0.36, 0.32, tok, 23, zorder=zorder + 1)
    ax.add_patch(Circle((x + 0.55, y - 0.98), 0.09, facecolor=P.fill("drug"), edgecolor=P.edge("drug"), lw=0.6,
                        zorder=zorder + 2))  # haem f
    _name(ax, (x, y + 0.42), text)
    return {"qp": (x - 0.55, y - 0.25), "qn": (x - 0.55, y + 0.35), "f": (x + 0.55, y - 0.98), "top": (x, y + 0.9),
            "bottom": (x, y - 1.3)}


def plastocyanin(ax, center, r=0.3, zorder=13):
    """Plastocyanin (PC), the soluble blue copper protein of the lumen."""
    ax.add_patch(Circle(center, r, facecolor=P.fill(COLOR["pc"]), edgecolor=P.edge(COLOR["pc"]), lw=0.9, zorder=zorder))
    label(ax, center, "PC", size="tiny", bold=True, color=P.on_fill(), zorder=zorder + 1)
    return center


def psi(ax, x, y, text="PSI", antenna=True, zorder=11):
    """Photosystem I with LHCI (right) and the stromal ridge carrying the FA/FB clusters.

    Anchors: ``p700``, ``pc_site`` (lumen side), ``fd_site`` (stromal ridge), ``antenna``.
    """
    if antenna:
        _body(ax, (x + 1.05, y + 0.05), 0.36, 0.62, COLOR["lhc"], 31, zorder=zorder - 1)
        label(ax, (x + 1.05, y + 0.85), "LHCI", size="tiny", color=P.ink(), va="bottom", zorder=zorder + 4)
    _body(ax, (x, y), 0.8, 0.9, COLOR["psi"], 32, zorder=zorder)
    _body(ax, (x - 0.15, y + 0.95), 0.42, 0.26, COLOR["psi"], 33, zorder=zorder + 1)
    for dx in (-0.1, 0.1):
        ax.add_patch(Circle((x - 0.15 + dx, y + 0.95), 0.07, facecolor=P.fill("drug"), edgecolor=P.edge("drug"), lw=0.5,
                            zorder=zorder + 2))
    _chl_pair(ax, (x + 0.15, y - 0.15), zorder + 2)
    _name(ax, (x + 0.15, y + 0.33), text)
    return {"p700": (x + 0.15, y - 0.15), "pc_site": (x - 0.2, y - 0.9), "fd_site": (x - 0.15, y + 1.2),
            "antenna": (x + 1.05, y + 0.5)}


def ferredoxin(ax, center, r=0.26, zorder=13):
    """Ferredoxin (Fd), a small soluble [2Fe-2S] protein of the stroma."""
    ax.add_patch(Circle(center, r, facecolor=P.fill(COLOR["fd"]), edgecolor=P.edge(COLOR["fd"]), lw=0.9, zorder=zorder))
    label(ax, center, "Fd", size="tiny", bold=True, color=P.on_fill(), zorder=zorder + 1)
    return center


def fnr(ax, x, y, text="FNR", zorder=12):
    """Ferredoxin–NADP+ reductase, a peripheral flavoprotein bound to the stromal face. Returns its centre."""
    c = (x, y + MH + 0.42)
    _body(ax, c, 0.48, 0.38, COLOR["fnr"], 41, zorder=zorder)
    _name(ax, c, text, size="tiny")
    return c


def atp_synthase(ax, x, y, text="ATP synthase", c_ring=14, zorder=11):
    """Chloroplast ATP synthase: CF0 (c-ring in the membrane) and the CF1 head (alpha3 beta3) in the stroma.

    Anchors: ``channel`` (proton path through CF0), ``head`` (CF1 centre), ``top``, ``bottom``.
    """
    tok, st = COLOR["atp_synthase"], COLOR["stalk"]
    # c-ring: a rounded block with vertical subunit stripes
    w = 1.3
    ax.add_patch(FancyBboxPatch((x - w / 2, y - MH - 0.08), w, 2 * MH + 0.16, boxstyle="round,pad=0,rounding_size=0.14",
                                facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=LINE * 0.9, zorder=zorder))
    for k in range(1, 7):
        xx = x - w / 2 + k * w / 7
        ax.plot([xx, xx], [y - MH + 0.02, y + MH - 0.02], color=P.edge(tok), lw=0.6, zorder=zorder + 1)
    # subunit a (proton half-channels) beside the ring, peripheral stalk up to the head
    ax.add_patch(FancyBboxPatch((x + w / 2 - 0.02, y - MH - 0.02), 0.36, 2 * MH + 0.04, boxstyle="round,pad=0,rounding_size=0.1",
                                facecolor=P.fill(st), edgecolor=P.edge(st), lw=LINE * 0.8, zorder=zorder))
    ax.add_patch(FancyBboxPatch((x + w / 2 + 0.06, y + MH), 0.16, 1.55, boxstyle="round,pad=0,rounding_size=0.07",
                                facecolor=P.fill(st), edgecolor=P.edge(st), lw=LINE * 0.8, zorder=zorder - 1))
    # central stalk and the CF1 head
    ax.add_patch(FancyBboxPatch((x - 0.11, y + MH), 0.22, 1.05, boxstyle="round,pad=0,rounding_size=0.08",
                                facecolor=P.fill(st), edgecolor=P.edge(st), lw=LINE * 0.8, zorder=zorder - 1))
    hy = y + MH + 1.45
    for k, dx in enumerate((-0.55, -0.18, 0.18, 0.55)):
        t = tok if k % 2 == 0 else st
        ax.add_patch(FancyBboxPatch((x + dx - 0.2, hy - 0.5), 0.4, 1.0, boxstyle="round,pad=0,rounding_size=0.18",
                                    facecolor=P.fill(t) if t == tok else P.light(tok), edgecolor=P.edge(tok), lw=LINE * 0.85,
                                    zorder=zorder + (1 if k in (1, 2) else 0)))
    label(ax, (x, y - MH - 0.3), "CF₀", size="tiny", va="top", zorder=zorder + 3)
    label(ax, (x - 0.95, hy + 0.35), "CF₁", size="tiny", ha="right", zorder=zorder + 3)
    if text:
        label(ax, (x, hy + 0.65), text, size="small", bold=True, va="bottom", zorder=zorder + 3)
    return {"channel": (x + w / 2 + 0.16, y), "head": (x, hy), "top": (x, hy + 0.5), "bottom": (x, y - MH - 0.1),
            "ring": (x, y)}


def proton(ax, center, text="H⁺", r=0.13, side="right", zorder=17):
    """A proton (small disc in the H+ token) with its label beside it."""
    ax.add_patch(Circle(center, r, facecolor=P.fill("h"), edgecolor=P.edge("h"), lw=0.7, zorder=zorder))
    if text:
        dx = r + 0.05
        label(ax, (center[0] + (dx if side == "right" else -dx), center[1]), text, size="tiny",
              ha="left" if side == "right" else "right", zorder=zorder + 1)


def photon(ax, a, b, text="hν", waves=4, amp=0.12, zorder=16):
    """A light quantum: a wavy arrow from a to b in the light colour, labelled near its start."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    d = b - a
    L = np.linalg.norm(d)
    u, n = d / L, np.array([-d[1], d[0]]) / L
    t = np.linspace(0, 1, 160)
    core = L * 0.8
    s = t * core
    w = amp * np.sin(2 * np.pi * waves * t) * np.minimum(1, (1 - t) * 6)
    pts = a + np.outer(s, u) + np.outer(w, n)
    c = line_color(COLOR["light"])
    ax.plot(pts[:, 0], pts[:, 1], color=c, lw=1.5, zorder=zorder, solid_capstyle="round")
    arrow(ax, pts[-1], b, kind="process", color=c, lw=1.5, head=0.22, zorder=zorder)
    if text:
        label(ax, a - u * 0.05 + n * 0.3, text, size="small", italic=True, color=c, zorder=zorder + 1)


# ----------------------------------------------------------------------- the Z-scheme
# (name, midpoint potential E_m / V at pH 7, x position, group). Values: Blankenship, Molecular Mechanisms of
# Photosynthesis (2nd ed. 2014), Rappaport & Diner (2008) for PSII; excited states from E_m - E_00
# (680 nm = 1.82 eV, 700 nm = 1.77 eV).
Z_CARRIERS = [
    ("H₂O", 0.82, 0.5, "water"),
    ("Mn₄CaO₅", 0.9, 1.5, "psii"),
    ("Tyr Z", 1.0, 2.5, "psii"),
    ("P680", 1.2, 3.5, "psii"),
    ("P680*", -0.62, 3.5, "psii"),
    ("Pheo", -0.5, 4.5, "psii"),
    ("Q_A", -0.1, 5.5, "psii"),
    ("Q_B", 0.0, 6.5, "psii"),
    ("PQ pool", 0.1, 7.6, "pq"),
    ("FeS (Rieske)", 0.3, 8.75, "b6f"),
    ("Cyt f", 0.35, 9.9, "b6f"),
    ("PC", 0.37, 10.9, "pc"),
    ("P700", 0.45, 11.9, "psi"),
    ("P700*", -1.32, 11.9, "psi"),
    ("A₀", -1.05, 12.85, "psi"),
    ("A₁", -0.8, 13.7, "psi"),
    ("F_X", -0.7, 14.55, "psi"),
    ("F_A/F_B", -0.55, 15.45, "psi"),
    ("Fd", -0.42, 16.4, "fd"),
    ("FNR", -0.36, 17.35, "fnr"),
    ("NADP⁺", -0.32, 18.35, "nadp"),
]
_GROUP_TOKEN = {"water": "neutral", "psii": COLOR["psii"], "pq": COLOR["pq"], "b6f": COLOR["b6f"], "pc": COLOR["pc"],
                "psi": COLOR["psi"], "fd": COLOR["fd"], "fnr": COLOR["fnr"], "nadp": "metabolite"}


def _carrier_text(name):
    sub = {"Q_A": "Q$_\\mathrm{A}$", "Q_B": "Q$_\\mathrm{B}$", "F_X": "F$_\\mathrm{X}$", "F_A/F_B": "F$_\\mathrm{A}$/F$_\\mathrm{B}$"}
    return sub.get(name, name)


def z_scheme(ax, box_, carriers=None, xlim=(0, 19), ylim=(1.45, -1.55), cyclic=True, box_w=0.95, box_h=0.42,
             yticks=(-1.5, -1.0, -0.5, 0.0, 0.5, 1.0), spans=True):
    """The Z-scheme of linear electron flow on a midpoint-potential axis (negative, reducing, at the top).

    ``box_`` is the canvas box of the plot; carriers are ``(name, E_m, x, group)`` (default ``Z_CARRIERS``).
    Draws the carriers as boxes in their complex's colour, electron-transfer arrows, the two photochemical
    steps (photon arrows), the complexes as shaded bands and, with ``cyclic``, cyclic electron flow around
    PSI. Returns ``(plot, positions)`` with positions = {name: canvas xy}.
    """
    cs = carriers or Z_CARRIERS
    p = Plot(ax, box_, xlim, ylim, ylabel="Midpoint potential $E_{\\mathrm{m}}$ / V",
             yticks=[(v, f"{v:+.1f}".replace("+0.0", "0").replace("-", "−")) for v in yticks], ylabel_offset=0.95)
    pos = {name: p.xy(x, e) for name, e, x, g in cs}
    if spans:
        for g, text in (("psii", "Photosystem II"), ("b6f", "Cyt b₆f"), ("psi", "Photosystem I")):
            xs = [x for name, e, x, gg in cs if gg == g]
            if xs:
                p.span(min(xs) - 0.5, max(xs) + 0.5, _GROUP_TOKEN[g], text=text,
                       strength=0.8, size="small", color=P.ink())
    ec = line_color(COLOR["electron"])
    names = [c[0] for c in cs]
    # photochemistry: P -> P*
    for ground, excited, nm in (("P680", "P680*", 680), ("P700", "P700*", 700)):
        if ground in pos and excited in pos:
            a, b = pos[ground], pos[excited]
            lc = line_color(COLOR["light"])
            arrow(ax, (a[0], a[1] + box_h / 2 + 0.05), (b[0], b[1] - box_h / 2 - 0.05), kind="process", color=lc,
                  lw=3.2, head=0.36, zorder=14)
            ev = 1239.84 / nm
            photon(ax, (a[0] - 1.75, (a[1] + b[1]) / 2 + 0.5), (a[0] - 0.22, (a[1] + b[1]) / 2 + 0.1), text=None, waves=3)
            label(ax, (a[0] - 1.85, (a[1] + b[1]) / 2 + 1.22), f"hν, {nm} nm", size="tiny", color=lc, ha="center")
            label(ax, (a[0] - 1.85, (a[1] + b[1]) / 2 + 0.9), f"({ev:.2f} eV)", size="tiny", color=lc, ha="center")
    # electron transfer along the listed order; the step into an excited state is photochemical (drawn above)
    widths = {name: box_w * (1.5 if name == "FeS (Rieske)" else 1.22 if name in ("Mn₄CaO₅", "PQ pool", "F_A/F_B") else 1.0)
              for name in names}

    def edge_pt(name, v):
        # where the ray from a box centre along v leaves the box
        c = np.asarray(pos[name])
        tx = (widths[name] / 2 + 0.05) / abs(v[0]) if abs(v[0]) > 1e-9 else 1e9
        ty = (box_h / 2 + 0.05) / abs(v[1]) if abs(v[1]) > 1e-9 else 1e9
        return c + v * min(tx, ty)

    for a_, b_ in zip(names[:-1], names[1:]):
        if b_.endswith("*") or a_ in ("P680", "P700"):
            continue
        d = np.asarray(pos[b_]) - np.asarray(pos[a_])
        u = d / np.linalg.norm(d)
        arrow(ax, edge_pt(a_, u), edge_pt(b_, -u), kind="process", color=ec, lw=1.3, head=0.18, zorder=13)
    for name, e, x, g in cs:
        box(ax, pos[name], widths[name], box_h, _GROUP_TOKEN.get(g, "neutral"), text=_carrier_text(name), size="tiny",
            radius=0.12, zorder=16)
    if cyclic and "Fd" in pos and "PQ pool" in pos:
        a, b = np.asarray(pos["Fd"]), np.asarray(pos["PQ pool"])
        arrow(ax, (a[0] - 0.1, a[1] - box_h / 2 - 0.05), (b[0] + 0.1, b[1] - box_h / 2 - 0.06), kind="process", bend=0.1,
              color=ec, lw=1.1, dashed=True, head=0.18, zorder=12)
    return p, pos


# ----------------------------------------------------------------------- leaf gas-exchange models
# Bernacchi et al. (2001) Plant Cell Environ. 24:253, 25 °C (units: umol mol-1 for CO2, mmol mol-1 for O2)
KC, KO, GAMMA_STAR, O2 = 404.9, 278.4, 42.75, 210.0


def farquhar(ci, vcmax=100.0, j=160.0, rd=1.0, tpu=None):
    """Net CO2 assimilation of a C3 leaf (umol m-2 s-1) at intercellular CO2 ``ci`` (umol mol-1).

    Returns (A, Ac, Aj[, Ap]): Rubisco-limited Ac = Vcmax (Ci - G*) / (Ci + Kc (1 + O/Ko)) - Rd,
    RuBP-regeneration-limited Aj = J (Ci - G*) / (4 Ci + 8 G*) - Rd, and A = min. With ``tpu`` the
    triose-phosphate-use limit Ap = 3 TPU - Rd is included.
    """
    ci = np.asarray(ci, float)
    ac = vcmax * (ci - GAMMA_STAR) / (ci + KC * (1 + O2 / KO)) - rd
    aj = j * (ci - GAMMA_STAR) / (4 * ci + 8 * GAMMA_STAR) - rd
    if tpu is None:
        return np.minimum(ac, aj), ac, aj
    ap = np.full_like(ci, 3 * tpu - rd)
    return np.minimum(np.minimum(ac, aj), ap), ac, aj, ap


def light_response(i, phi=0.05, amax=25.0, theta=0.7, rd=1.5):
    """Non-rectangular hyperbola: net assimilation at photon flux ``i`` (umol m-2 s-1).

    theta A^2 - (phi I + Amax) A + phi I Amax = 0 (smaller root), minus dark respiration Rd.
    phi is the apparent quantum yield (initial slope), theta the curvature (0 Blackman-like ... 1 rectangular).
    """
    i = np.asarray(i, float)
    s = phi * i + amax
    return (s - np.sqrt(s * s - 4 * theta * phi * i * amax)) / (2 * theta) - rd


def _cell_box(ax, x, y, w, h, token, r=0.12, zorder=6):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                                facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE * 0.75, zorder=zorder))


def _plastid(ax, xy, rx=0.13, ry=0.07, angle=0.0, zorder=8):
    t = np.linspace(0, 2 * np.pi, 30)
    c, s = math.cos(math.radians(angle)), math.sin(math.radians(angle))
    v = np.c_[rx * np.cos(t), ry * np.sin(t)] @ np.array([[c, s], [-s, c]]) + xy
    shape(ax, v, "chloroplast", lw=0.6, zorder=zorder)


def leaf_section(ax, box_, stoma_x=None, palisade=7, zorder=5):
    """A C3 leaf in cross-section (adaxial side up): epidermes, palisade and spongy mesophyll with
    chloroplasts, intercellular air spaces, and one stoma in the lower epidermis.

    ``box_`` = (x0, y0, w, h) spans lower to upper epidermis. Returns anchors: ``pore`` (stomatal pore),
    ``cavity`` (substomatal cavity), ``air`` (outside, below the pore), ``cell`` (a spongy cell beside the
    cavity) and ``plastid`` (a chloroplast in it).
    """
    x0, y0, w, h = box_
    sx = stoma_x if stoma_x is not None else x0 + w / 2
    ep = h * 0.1
    # upper epidermis
    n = max(3, int(round(w / 0.85)))
    cw = w / n
    for k in range(n):
        _cell_box(ax, x0 + cw * (k + 0.5), y0 + h - ep / 2, cw - 0.05, ep, "cell_wall", r=0.08, zorder=zorder)
    # palisade mesophyll
    pw = w / palisade
    ph = h * 0.4
    py = y0 + h - ep - 0.06 - ph / 2
    for k in range(palisade):
        cx = x0 + pw * (k + 0.5)
        _cell_box(ax, cx, py, pw - 0.14, ph, "plant", r=0.16, zorder=zorder)
        for j, f in enumerate((-0.32, 0.0, 0.32)):
            _plastid(ax, (cx + (0.07 if j % 2 else -0.07), py + f * ph), angle=90, zorder=zorder + 1)
    # spongy mesophyll: loosely packed rounded cells, leaving an air space above the stoma
    sy0, sy1 = y0 + ep + 0.08, py - ph / 2 - 0.08
    rng = np.random.default_rng(7)
    cell = plastid = None
    m = max(3, int(w / 1.05))
    for k in range(m):
        cx = x0 + (k + 0.5) * w / m
        if abs(cx - sx) < 0.55:
            continue  # substomatal cavity
        for row, fy in enumerate((0.28, 0.74)):
            jitter = rng.uniform(-0.08, 0.08)
            cy = sy0 + (sy1 - sy0) * fy + jitter
            rx, ry = 0.36, (sy1 - sy0) * 0.19
            shape(ax, blob((cx + (0.16 if row else -0.1), cy), rx, ry, wobble=0.1, seed=k * 3 + row, k=8), "plant", lw=LINE * 0.75,
                  zorder=zorder)
            pl = (cx + (0.16 if row else -0.1) + 0.12, cy + 0.05)
            _plastid(ax, pl, zorder=zorder + 1)
            _plastid(ax, (pl[0] - 0.25, pl[1] - 0.08), angle=30, zorder=zorder + 1)
            if row == 1 and (cell is None or abs(cx - sx) < abs(cell[0] - sx)) and cx > sx:
                cell, plastid = (cx + 0.16, cy), pl
    # lower epidermis with the stoma (guard cells seen in section)
    for k in range(n):
        cx = x0 + cw * (k + 0.5)
        if abs(cx - sx) < 0.6:
            continue
        _cell_box(ax, cx, y0 + ep / 2, cw - 0.05, ep, "cell_wall", r=0.08, zorder=zorder)
    for side in (-1, 1):
        shape(ax, blob((sx + side * 0.3, y0 + ep / 2), 0.2, ep * 0.62, wobble=0.04, seed=40 + side, k=8), "plant",
              lw=LINE * 0.8, zorder=zorder + 1)
    return {"pore": (sx, y0 + ep / 2), "cavity": (sx, (sy0 + sy1) / 2), "air": (sx, y0 - 0.6), "cell": cell,
            "plastid": plastid, "top": y0 + h, "bottom": y0}


__all__ = ["COLOR", "MH", "tint", "thylakoid", "psii", "plastoquinone", "cytb6f", "plastocyanin", "psi", "ferredoxin",
           "fnr", "atp_synthase", "proton", "photon", "Z_CARRIERS", "z_scheme", "farquhar", "light_response", "leaf_section",
           "KC", "KO", "GAMMA_STAR", "O2"]
