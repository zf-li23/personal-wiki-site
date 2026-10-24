"""Electrophysiology and neuroscience parts: ion channels and pumps in a membrane, ion fluxes,
microelectrodes, equivalent-circuit symbols, and the standard Hodgkin–Huxley / LIF models.

Membrane pieces assume a horizontal membrane centred at height ``y`` (outside above, inside below)
with half-thickness ``membrane_half`` (0.45 matches ``bio.bilayer`` defaults):

    neuro.patch(ax, 0, 10, 3)                         # bilayer strip with Outside / Inside labels
    neuro.channel(ax, 2, 3, "na", open=True)          # voltage-gated Na+ channel (ion token colours)
    neuro.pump(ax, 6, 3)                              # Na+/K+-ATPase: 3 Na+ out, 2 K+ in
    neuro.flux(ax, 2, 3, "na", "in")                  # an ion crossing with an arrow

Circuit symbols (canvas units, drawn in ink): ``wire``, ``resistor`` (``variable=True`` for a
voltage-dependent conductance), ``capacitor``, ``battery`` (long plate = +), ``ground``,
``current_source``, ``node``. ``electrode(ax, tip, angle)`` draws a glass micropipette.

Models (SI-free, the conventional units): ``hh_rates`` / ``hh_simulate`` (Hodgkin & Huxley 1952,
squid axon at 6.3 °C, rest −65 mV: ḡNa 120, ḡK 36, ḡL 0.3 mS/cm², ENa 50, EK −77, EL −54.4 mV,
Cm 1 µF/cm²) and ``lif_rate`` (leaky integrate-and-fire firing rate).
"""

import math

import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch, Polygon

from . import palette as P
from .cell import bilayer
from .core import LINE, arrow, label
from .molecules import ION_TEXT

MEMBRANE_HALF = 0.45


# ---------------------------------------------------------------------------------------------
# membrane pieces


def patch(ax, x0, x1, y, outside="Outside", inside="Inside", labels=True, outside_token="extracellular",
          inside_token="cytoplasm", depth=1.6, zorder=4):
    """A membrane strip from x0 to x1 at height y: tinted bath above and cytoplasm below, bilayer between.

    ``depth`` is the height of each tinted compartment. Returns the membrane half-thickness.
    """
    ax.add_patch(FancyBboxPatch((x0, y), x1 - x0, depth, boxstyle="square,pad=0", facecolor=P.fill(outside_token),
                                edgecolor="none", zorder=zorder - 2))
    ax.add_patch(FancyBboxPatch((x0, y - depth), x1 - x0, depth, boxstyle="square,pad=0", facecolor=P.fill(inside_token),
                                edgecolor="none", zorder=zorder - 2))
    bilayer(ax, [(x0 + 0.1, y), (x1 - 0.1, y)], zorder=zorder)
    if labels:
        label(ax, (x0 + 0.15, y + depth - 0.2), outside, size="small", ha="left", va="top", color=P.muted())
        label(ax, (x0 + 0.15, y - depth + 0.2), inside, size="small", ha="left", va="bottom", color=P.muted())
    return MEMBRANE_HALF


def channel(ax, x, y, ion="na", open=True, membrane_half=MEMBRANE_HALF, token=None, text=None, show_ion=True,
            gate=None, width=0.9, text_dy=None, zorder=11):
    """An ion channel spanning the membrane: two subunits around a pore, in the colour of its ion.

    ``open=False`` closes the pore (subunits meet at the gate). ``gate`` draws an inactivation ball
    and chain on the cytoplasmic side ("ball": hanging free, "plug": blocking the pore). ``text``
    labels the channel below the membrane. Returns the pore's top and bottom points.
    """
    tok = token or ("neutral" if ion in (None, "leak") else ion)
    mh = membrane_half
    w = width
    gap = 0.16 if open else 0.02
    for side in (-1, 1):
        xc = x + side * (gap / 2 + w * 0.22)
        top, bot = y + mh + 0.18, y - mh - 0.18
        # each subunit narrows towards the pore at mid-membrane (selectivity filter)
        inner = x + side * gap / 2
        pts = [(inner, top), (xc + side * w * 0.22, top), (xc + side * w * 0.26, y), (xc + side * w * 0.22, bot),
               (inner, bot), (inner + side * (0.0 if open else 0.0), y + 0.05)]
        poly = Polygon(pts, closed=True, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=LINE * 0.8, joinstyle="round",
                       zorder=zorder)
        ax.add_patch(poly)
    if open and show_ion and ion not in (None, "leak"):
        ax.add_patch(Circle((x, y + 0.05), 0.075, facecolor=P.light(tok), edgecolor=P.edge(tok), lw=0.7, zorder=zorder + 1))
    if gate in ("ball", "plug"):
        anchor = (x + w * 0.42, y - mh - 0.18)
        ball = (x + w * 0.62, y - mh - 0.62) if gate == "ball" else (x, y - mh - 0.24)
        t = np.linspace(0, 1, 30)
        cx = anchor[0] + (ball[0] - anchor[0]) * t
        cy = anchor[1] + (ball[1] - anchor[1]) * t - 0.12 * np.sin(np.pi * t)
        ax.plot(cx, cy, color=P.edge(tok), lw=LINE * 0.8, zorder=zorder)
        ax.add_patch(Circle(ball, 0.13, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=LINE * 0.8, zorder=zorder + 1))
    if text:
        dy = text_dy if text_dy is not None else (0.95 if gate == "ball" else 0.45)
        label(ax, (x, y - mh - dy), text, size="small", va="top")
    return (x, y + mh + 0.18), (x, y - mh - 0.18)


def pump(ax, x, y, membrane_half=MEMBRANE_HALF, text="Na⁺/K⁺-ATPase", ions=True, zorder=11):
    """The Na⁺/K⁺ pump (P-type ATPase): 3 Na⁺ out and 2 K⁺ in per ATP hydrolysed."""
    mh = membrane_half
    tok = "enzyme"
    ax.add_patch(FancyBboxPatch((x - 0.45, y - mh - 0.25), 0.9, 2 * mh + 0.5, boxstyle="round,pad=0,rounding_size=0.25",
                                facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=LINE * 0.9, zorder=zorder))
    ax.add_patch(Circle((x, y - mh - 0.42), 0.26, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=LINE * 0.9, zorder=zorder))
    label(ax, (x, y - mh - 0.42), "ATP", size="tiny", color=P.on_fill(), zorder=zorder + 1)
    if ions:
        arrow(ax, (x - 0.2, y - mh - 0.15), (x - 0.2, y + mh + 0.75), kind="process", color=P.edge("na"), lw=1.1, head=0.16,
              zorder=zorder + 2)
        arrow(ax, (x + 0.2, y + mh + 0.75), (x + 0.2, y - mh - 0.15), kind="process", color=P.edge("k"), lw=1.1, head=0.16,
              zorder=zorder + 2)
        label(ax, (x - 0.3, y + mh + 0.75), "3 Na⁺", size="tiny", ha="right", va="center")
        label(ax, (x + 0.3, y + mh + 0.75), "2 K⁺", size="tiny", ha="left", va="center")
    if text:
        label(ax, (x, y - mh - 0.8), text, size="small", va="top")


def flux(ax, x, y, ion, direction="in", membrane_half=MEMBRANE_HALF, reach=0.75, r=0.13, text=True, dx=0.0, zorder=14):
    """An ion crossing the membrane at x: a disc on the source side and an arrow to the other side."""
    mh = membrane_half
    s = -1 if direction == "in" else 1
    start = (x + dx, y - s * (mh + reach))
    end = (x + dx, y + s * (mh + reach * 0.75))
    ax.add_patch(Circle(start, r, facecolor=P.fill(ion), edgecolor=P.edge(ion), lw=0.8, zorder=zorder))
    arrow(ax, (start[0], start[1] + s * r * 1.3), end, kind="process", color=P.edge(ion), lw=1.2, head=0.17, zorder=zorder)
    if text:
        label(ax, (start[0] + r + 0.06, start[1]), ION_TEXT.get(ion, ion), size="tiny", ha="left", zorder=zorder)
    return start, end


def ions(ax, box, kind, n, r=0.1, seed=0, zorder=8):
    """Scatter ``n`` small ion discs of ``kind`` in box (x0, y0, w, h), deterministically and without overlap."""
    x0, y0, w, h = box
    rng = np.random.default_rng(seed + sum(map(ord, kind)))
    placed = []
    tries = 0
    while len(placed) < n and tries < 4000:
        tries += 1
        p = (x0 + r + rng.uniform(0, w - 2 * r), y0 + r + rng.uniform(0, h - 2 * r))
        if all(math.hypot(p[0] - q[0], p[1] - q[1]) > 2.4 * r for q in placed):
            placed.append(p)
    for p in placed:
        ax.add_patch(Circle(p, r, facecolor=P.fill(kind), edgecolor=P.edge(kind), lw=0.6, zorder=zorder))
    return placed


def electrode(ax, tip, angle=60.0, length=3.0, width=0.32, text=None, wire=True, zorder=16):
    """A glass micropipette whose fine tip is at ``tip``; ``angle`` (degrees) points from tip to shank."""
    th = math.radians(angle)
    u = np.array([math.cos(th), math.sin(th)])
    n = np.array([-u[1], u[0]])
    t = np.asarray(tip, float)
    taper = t + u * length * 0.45
    end = t + u * length
    glass = [t + n * 0.02, taper + n * width / 2, end + n * width / 2, end - n * width / 2, taper - n * width / 2, t - n * 0.02]
    ax.add_patch(Polygon(glass, closed=True, facecolor=P.light("vacuole"), edgecolor=P.edge("vacuole"), lw=LINE * 0.8,
                         joinstyle="round", zorder=zorder))
    # filling solution and the Ag/AgCl wire
    sol = [t + u * 0.25 + n * 0.02, taper + n * width * 0.32, end - u * 0.05 + n * width * 0.32,
           end - u * 0.05 - n * width * 0.32, taper - n * width * 0.32, t + u * 0.25 - n * 0.02]
    ax.add_patch(Polygon(sol, closed=True, facecolor=P.fill("channel"), edgecolor="none", zorder=zorder + 0.5))
    if wire:
        a, b = t + u * length * 0.55, end + u * 0.6
        ax.plot([a[0], b[0]], [a[1], b[1]], color=P.muted(), lw=1.1, zorder=zorder + 1)
    if text:
        q = end + u * 0.75
        label(ax, q, text, size="small", ha="center", va="bottom" if u[1] > 0 else "top")
    return end + u * 0.6


# ---------------------------------------------------------------------------------------------
# circuit symbols (drawn in ink; positions in canvas units)


def wire(ax, *points, lw=1.1, color=None, zorder=14):
    """A wire through the given points."""
    p = np.asarray(points, float)
    ax.plot(p[:, 0], p[:, 1], color=color or P.ink(), lw=lw, solid_joinstyle="miter", solid_capstyle="round", zorder=zorder)


def node(ax, xy, r=0.06, zorder=15):
    """A junction dot."""
    ax.add_patch(Circle(xy, r, color=P.ink(), lw=0, zorder=zorder))


def _frame(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    L = np.linalg.norm(b - a)
    u = (b - a) / L
    return a, b, L, u, np.array([-u[1], u[0]])


def resistor(ax, a, b, length=0.8, width=0.22, variable=False, text=None, text_side=1, color=None, lw=1.1, zorder=14):
    """A resistor (zig-zag) between a and b, with leads; ``variable=True`` adds the diagonal arrow."""
    a, b, L, u, n = _frame(a, b)
    c = color or P.ink()
    m = (a + b) / 2
    s0, s1 = m - u * length / 2, m + u * length / 2
    k = 6
    zz = [s0] + [s0 + u * length * (i + 0.5) / k + n * width * (1 if i % 2 == 0 else -1) for i in range(k)] + [s1]
    wire(ax, a, s0, color=c, lw=lw, zorder=zorder)
    wire(ax, *zz, color=c, lw=lw, zorder=zorder)
    wire(ax, s1, b, color=c, lw=lw, zorder=zorder)
    if variable:
        p, q = m - u * length * 0.55 - n * width * 2.0, m + u * length * 0.55 + n * width * 2.0
        arrow(ax, p, q, kind="process", color=c, lw=lw * 0.9, head=0.15, zorder=zorder)
    if text:
        label(ax, m + n * text_side * (width + 0.45), text, size="small", ha="center")
    return m


def capacitor(ax, a, b, gap=0.16, plate=0.55, text=None, text_side=1, color=None, lw=1.1, zorder=14):
    """A capacitor (two parallel plates) between a and b."""
    a, b, L, u, n = _frame(a, b)
    c = color or P.ink()
    m = (a + b) / 2
    p0, p1 = m - u * gap / 2, m + u * gap / 2
    wire(ax, a, p0, color=c, lw=lw, zorder=zorder)
    wire(ax, p1, b, color=c, lw=lw, zorder=zorder)
    for p in (p0, p1):
        wire(ax, p - n * plate / 2, p + n * plate / 2, color=c, lw=lw * 1.8, zorder=zorder)
    if text:
        label(ax, m + n * text_side * (plate / 2 + 0.3), text, size="small")
    return m


def battery(ax, a, b, gap=0.16, text=None, text_side=1, color=None, lw=1.1, zorder=14):
    """A battery (EMF) between a and b; the long plate (+) faces b."""
    a, b, L, u, n = _frame(a, b)
    c = color or P.ink()
    m = (a + b) / 2
    p0, p1 = m - u * gap / 2, m + u * gap / 2
    wire(ax, a, p0, color=c, lw=lw, zorder=zorder)
    wire(ax, p1, b, color=c, lw=lw, zorder=zorder)
    wire(ax, p0 - n * 0.14, p0 + n * 0.14, color=c, lw=lw * 2.2, zorder=zorder)
    wire(ax, p1 - n * 0.3, p1 + n * 0.3, color=c, lw=lw, zorder=zorder)
    if text:
        label(ax, m + n * text_side * 0.6, text, size="small")
    return m


def current_source(ax, a, b, r=0.28, text=None, text_side=1, color=None, lw=1.1, zorder=14):
    """An ideal current source (circle with an arrow pointing from a to b)."""
    a, b, L, u, n = _frame(a, b)
    c = color or P.ink()
    m = (a + b) / 2
    wire(ax, a, m - u * r, color=c, lw=lw, zorder=zorder)
    wire(ax, m + u * r, b, color=c, lw=lw, zorder=zorder)
    ax.add_patch(Circle(m, r, facecolor=P.surface(), edgecolor=c, lw=lw, zorder=zorder))
    arrow(ax, m - u * r * 0.65, m + u * r * 0.7, kind="process", color=c, lw=lw * 0.9, head=0.14, zorder=zorder + 1)
    if text:
        label(ax, m + n * text_side * (r + 0.35), text, size="small")
    return m


def ground(ax, xy, color=None, lw=1.1, zorder=14):
    """An earth symbol hanging below xy."""
    x, y = xy
    c = color or P.ink()
    wire(ax, (x, y), (x, y - 0.18), color=c, lw=lw, zorder=zorder)
    for k, w in enumerate((0.3, 0.2, 0.1)):
        wire(ax, (x - w, y - 0.18 - k * 0.09), (x + w, y - 0.18 - k * 0.09), color=c, lw=lw, zorder=zorder)


# ---------------------------------------------------------------------------------------------
# models

HH = {"gNa": 120.0, "gK": 36.0, "gL": 0.3, "ENa": 50.0, "EK": -77.0, "EL": -54.387, "Cm": 1.0}


def hh_rates(V):
    """Hodgkin–Huxley rate constants (1/ms) at membrane potential V (mV, rest −65 mV): αm, βm, αh, βh, αn, βn."""
    V = np.asarray(V, float)
    x = V + 40.0
    am = np.where(np.abs(x) < 1e-6, 1.0, 0.1 * x / (1 - np.exp(-x / 10)))
    bm = 4.0 * np.exp(-(V + 65) / 18)
    ah = 0.07 * np.exp(-(V + 65) / 20)
    bh = 1.0 / (1 + np.exp(-(V + 35) / 10))
    y = V + 55.0
    an = np.where(np.abs(y) < 1e-6, 0.1, 0.01 * y / (1 - np.exp(-y / 10)))
    bn = 0.125 * np.exp(-(V + 65) / 80)
    return am, bm, ah, bh, an, bn


def hh_steady(V):
    """Steady-state gates (m∞, h∞, n∞) at V."""
    am, bm, ah, bh, an, bn = hh_rates(V)
    return am / (am + bm), ah / (ah + bh), an / (an + bn)


def hh_simulate(I, t, V0=-65.0, params=None):
    """Integrate the HH equations (RK4) for injected current density ``I(t)`` (µA/cm², a function of t or an
    array matching ``t`` per column for several runs). Returns V, m, h, n (arrays of shape (len(t), runs)).
    """
    p = dict(HH, **(params or {}))
    t = np.asarray(t, float)
    Iarr = np.array([np.atleast_1d(I(tt)) for tt in t]) if callable(I) else np.atleast_2d(np.asarray(I, float).T).T
    runs = Iarr.shape[1]
    m0, h0, n0 = hh_steady(V0)
    y = np.array([[V0] * runs, [m0] * runs, [h0] * runs, [n0] * runs], float)
    out = np.empty((len(t), 4, runs))
    out[0] = y

    def f(y, Ii):
        V, m, h, n = y
        am, bm, ah, bh, an, bn = hh_rates(V)
        INa = p["gNa"] * m**3 * h * (V - p["ENa"])
        IK = p["gK"] * n**4 * (V - p["EK"])
        IL = p["gL"] * (V - p["EL"])
        return np.array([(Ii - INa - IK - IL) / p["Cm"], am * (1 - m) - bm * m, ah * (1 - h) - bh * h, an * (1 - n) - bn * n])

    for i in range(len(t) - 1):
        dt = t[i + 1] - t[i]
        Ia, Ib = Iarr[i], Iarr[i + 1]
        Im = (Ia + Ib) / 2
        k1 = f(y, Ia)
        k2 = f(y + dt / 2 * k1, Im)
        k3 = f(y + dt / 2 * k2, Im)
        k4 = f(y + dt * k3, Ib)
        y = y + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        out[i + 1] = y
    return out[:, 0], out[:, 1], out[:, 2], out[:, 3]


def lif_rate(I, tau=20.0, R=10.0, v_th=15.0, v_reset=0.0, t_ref=2.0):
    """Firing rate (Hz) of a leaky integrate-and-fire neuron, τ dV/dt = −V + R I (V relative to rest, mV;
    τ and t_ref in ms; R in MΩ and I in nA): r = 1 / (t_ref + τ ln((RI − V_reset)/(RI − V_th))) above rheobase."""
    I = np.asarray(I, float)
    mu = R * I
    with np.errstate(divide="ignore", invalid="ignore"):
        T = t_ref + tau * np.log((mu - v_reset) / (mu - v_th))
        r = np.where(mu > v_th, 1000.0 / T, 0.0)
    return r


__all__ = ["patch", "channel", "pump", "flux", "ions", "electrode", "wire", "node", "resistor", "capacitor", "battery",
           "current_source", "ground", "HH", "hh_rates", "hh_steady", "hh_simulate", "lif_rate", "MEMBRANE_HALF"]
