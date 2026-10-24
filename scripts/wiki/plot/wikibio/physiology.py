"""Motors, muscle and organ-physiology parts: kinesin and optical traps (single-molecule biophysics),
the sarcomere with sliding filaments, and models for cardiac and muscle mechanics.

    physiology.kinesin(ax, rear=(3, 2.2), front=(4, 2.2), cargo=(4.2, 4.5))   # two-headed motor on a track
    physiology.bead(ax, (5, 5), 1.5)                                            # polystyrene bead
    physiology.optical_trap(ax, focus=(5, 5), half_height=4)                    # focused laser beam
    physiology.sarcomere(ax, x0=1, y=3, length=2.6, scale=3.0)                  # one sarcomere, Z to Z
    physiology.length_tension(SL)                                               # Gordon-Huxley-Julian curve
    physiology.cardiac_cycle()                                                  # time-varying elastance model

Sarcomere geometry (frog skeletal muscle, Gordon, Huxley & Julian 1966): thick filament 1.6 µm with
a 0.2 µm bare zone, thin filament 1.0 µm from each Z disc (0.05 µm thick; 2.05 µm Z to tip), so the
plateau of the length–tension curve spans 2.05–2.25 µm, active tension falls to zero at 3.65 µm, and thick filaments
reach the Z discs at 1.65 µm.
"""

import math

import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, PathPatch, Polygon
from matplotlib.path import Path

from . import palette as P
from .core import LINE, blob, label

# ---------------------------------------------------------------------------------------------
# molecular motors and single-molecule instruments


def motor_head(ax, center, size=0.5, token="enzyme", angle=0.0, seed=0, zorder=13):
    """A motor domain (kinesin or myosin head) as a soft blob with a highlight."""
    o = blob(center, size * 0.55, size * 0.42, wobble=0.06, seed=seed + 31, k=7, angle=math.radians(angle))
    ax.add_patch(PathPatch(Path(o, closed=True), facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE * 0.9, zorder=zorder))
    hl = blob((center[0] - size * 0.12, center[1] + size * 0.1), size * 0.2, size * 0.12, wobble=0.04, seed=seed + 7, k=6)
    ax.add_patch(PathPatch(Path(hl, closed=True), facecolor=P.light(token), edgecolor="none", zorder=zorder + 0.5))
    return o


def coiled_coil(ax, a, b, width=0.12, turns=None, token="enzyme", lw=LINE * 1.2, zorder=12):
    """Two α-helices wound around each other from a to b (the stalk of kinesin or myosin)."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    L = np.linalg.norm(b - a)
    u = (b - a) / L
    n = np.array([-u[1], u[0]])
    k = turns or max(2, int(L / 0.45))
    s = np.linspace(0, 1, 160)
    for ph, tone in ((0.0, P.edge(token)), (math.pi, P.mix(P.edge(token), P.fill(token), 0.5))):
        off = np.sin(2 * math.pi * k * s + ph) * width / 2
        pts = a + np.outer(s * L, u) + np.outer(off, n)
        ax.plot(pts[:, 0], pts[:, 1], color=tone, lw=lw, solid_capstyle="round", zorder=zorder + (0.2 if ph else 0))


def kinesin(ax, rear, front, cargo, head=0.5, token="enzyme", neck=0.45, labels=False, zorder=13):
    """Kinesin-1 walking hand-over-hand: two heads bound at ``rear`` and ``front`` on the track, neck linkers
    joining above them, and a coiled-coil stalk to ``cargo`` (where the tail binds). Returns the neck point."""
    r, f = np.asarray(rear, float), np.asarray(front, float)
    motor_head(ax, r, head, token, seed=1, zorder=zorder)
    motor_head(ax, f, head, token, seed=2, zorder=zorder)
    neckp = (r + f) / 2 + np.array([0, head * 0.4 + neck])
    for h in (r, f):
        top = h + np.array([0, head * 0.35])
        ax.plot([top[0], neckp[0]], [top[1], neckp[1]], color=P.edge(token), lw=LINE * 1.1, solid_capstyle="round",
                zorder=zorder - 0.5)
    coiled_coil(ax, neckp, cargo, token=token, zorder=zorder - 1)
    if labels:
        label(ax, (r[0], r[1] - head * 0.95), "trailing", size="tiny", va="top")
        label(ax, (f[0], f[1] - head * 0.95), "leading", size="tiny", va="top")
    return tuple(neckp)


def bead(ax, center, r, token="neutral", zorder=11):
    """A polystyrene (or silica) bead: a sphere with a soft highlight."""
    ax.add_patch(Circle(center, r, facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE, zorder=zorder))
    ax.add_patch(Ellipse((center[0] - r * 0.35, center[1] + r * 0.38), r * 0.6, r * 0.38, angle=30,
                         facecolor=P.light(token), edgecolor="none", zorder=zorder + 0.5))


def optical_trap(ax, focus, half_height=4.0, waist=0.18, spread=2.2, token="highlight", strength=0.55, zorder=2):
    """A focused laser beam (hourglass) with its focus at ``focus``: the optical trap. ``spread`` is the beam's
    half-width at ±``half_height``. Drawn as a pale tint (opaque), so it sits under the objects it traps."""
    x, y = focus
    s = np.linspace(-1, 1, 60)
    hw = np.sqrt(waist**2 + (spread**2 - waist**2) * s**2)
    ys = y + s * half_height
    pts = np.r_[np.c_[x - hw, ys], np.c_[x + hw, ys][::-1]]
    col = P.mix(P.fill(token), P.surface(), strength + (0.25 if P.is_dark() else 0.0))
    ax.add_patch(Polygon(pts, closed=True, facecolor=col, edgecolor="none", zorder=zorder))
    # beam edges
    for sign in (-1, 1):
        ax.plot(x + sign * hw, ys, color=P.mix(P.edge(token), P.surface(), 0.35), lw=0.7, zorder=zorder + 0.1)
    return (x, y)


# ---------------------------------------------------------------------------------------------
# sarcomere

THICK = 1.6       # µm, myosin (thick) filament length
BARE = 0.2        # µm, central bare zone without heads
THIN = 1.0        # µm, actin (thin) filament length from the Z-disc face
ZDISC = 0.05      # µm


def sarcomere(ax, x0, y, length, scale=3.0, rows=3, spacing=0.42, labels=True, bands=True, titin=True, zorder=8,
              thick_token="myosin", thin_token="actin", z_token="neutral", band_y=None, detail=True):
    """One sarcomere from Z disc to Z disc, drawn to scale: ``length`` in µm, ``scale`` canvas units per µm,
    left Z disc at x0 and the filament lattice centred at height y (``rows`` thick filaments).

    Thin (actin) filaments run from each Z disc towards the centre; thick (myosin) filaments with
    heads pointing away from the bare zone sit around the M line; titin springs join thick filaments to
    the Z discs. ``bands=True`` draws brackets for the A band, I band and H zone above the lattice and
    labels Z discs and the M line below. ``detail=False`` draws a simplified glyph (filaments as lines,
    heads as short bristles) for small sarcomeres, e.g. above a length–tension curve. Returns a dict of
    the band edges in canvas x.
    """
    s = scale
    L = length
    xm = x0 + L * s / 2
    h = (rows - 0.5) * spacing + 0.25
    zx = [x0, x0 + L * s]
    ys = [y + (i - (rows - 1) / 2) * spacing for i in range(rows)]
    thin_y = [yy + spacing / 2 for yy in ys[:-1]] + [ys[0] - spacing / 2, ys[-1] + spacing / 2]
    thin_y = sorted(set(round(v, 6) for v in thin_y))
    # thin filaments (from each Z disc, length THIN, they may overlap in the middle at short lengths)
    for zxi, d in ((zx[0], 1), (zx[1], -1)):
        start = zxi + d * ZDISC * s / 2
        end = start + d * THIN * s
        for yy in thin_y:
            if detail:
                _actin_line(ax, start, end, yy, thin_token, zorder)
            else:
                ax.plot([start, end], [yy, yy], color=P.edge(thin_token), lw=1.4, solid_capstyle="butt", zorder=zorder)
    # thick filaments
    a0, a1 = xm - THICK * s / 2, xm + THICK * s / 2
    for yy in ys:
        if not detail:
            ax.plot([a0, a1], [yy, yy], color=P.edge(thick_token), lw=2.6, solid_capstyle="round", zorder=zorder + 1)
            for side in (-1, 1):
                for xx in np.arange(BARE / 2 + 0.06, THICK / 2, 0.12):
                    hx = xm + side * xx * s
                    ax.plot([hx, hx + side * 0.05], [yy - 0.1, yy + 0.1], color=P.edge(thick_token), lw=0.7, zorder=zorder + 1)
            continue
        ax.add_patch(FancyBboxPatch((a0, yy - 0.055), THICK * s, 0.11, boxstyle="round,pad=0,rounding_size=0.05",
                                    facecolor=P.fill(thick_token), edgecolor=P.edge(thick_token), lw=0.7, zorder=zorder + 1))
        n = int((THICK - BARE) / 2 / 0.09)
        for side in (-1, 1):
            for k in range(n):
                hx = xm + side * (BARE / 2 * s + (k + 0.5) * (THICK - BARE) / 2 / n * s)
                for up in (-1, 1):
                    if (k + (up > 0)) % 2:
                        continue
                    tip = (hx + side * 0.1, yy + up * 0.16)
                    ax.plot([hx, tip[0]], [yy + up * 0.05, tip[1]], color=P.edge(thick_token), lw=0.9, zorder=zorder + 1)
                    ax.add_patch(Circle(tip, 0.045, facecolor=P.fill(thick_token), edgecolor=P.edge(thick_token), lw=0.5,
                                        zorder=zorder + 1.5))
    # titin: a spring from the thick filament ends to the Z discs
    if titin and detail:
        for yy in ys:
            for zxi, ax_end in ((zx[0] + ZDISC * s / 2, a0), (zx[1] - ZDISC * s / 2, a1)):
                xs = np.linspace(zxi, ax_end, 60)
                ax.plot(xs, yy + 0.035 * np.sin(np.linspace(0, 2 * math.pi * max(2, abs(ax_end - zxi) / 0.12), 60)),
                        color=P.muted(), lw=0.6, zorder=zorder - 0.5)
    # Z discs (zig-zag) and M line
    for zxi in zx:
        if detail:
            zz = np.linspace(y - h, y + h, 13)
            xx = zxi + np.where(np.arange(13) % 2, 1, -1) * max(ZDISC * s * 0.9, 0.06)
            ax.plot(xx, zz, color=P.edge(z_token), lw=LINE * 1.6, solid_joinstyle="miter", zorder=zorder + 2)
        else:
            ax.plot([zxi, zxi], [y - h, y + h], color=P.edge(z_token), lw=LINE * 1.6, zorder=zorder + 2)
    ax.plot([xm, xm], [y - h + 0.08, y + h - 0.08], color=P.edge(thick_token), lw=LINE * (1.2 if detail else 0.8),
            zorder=zorder + 2)
    edges = {"Z": zx, "M": xm, "A": (a0, a1), "I": ((zx[0], a0), (a1, zx[1])),
             "H": (xm - max(0.0, L / 2 - THIN - ZDISC / 2) * s, xm + max(0.0, L / 2 - THIN - ZDISC / 2) * s),
             "top": y + h, "bottom": y - h}
    if bands:
        from .quant import bracket
        by = band_y if band_y is not None else y + h + 0.25
        bracket(ax, (a0, by), (a1, by), "A band", side=-1, offset=0.12)
        for i0, i1 in ((zx[0], a0), (a1, zx[1])):
            bracket(ax, (i0, by), (i1, by), "I" if i1 - i0 < 0.9 else "I band", side=-1, offset=0.12)
        hz = edges["H"]
        if hz[1] - hz[0] > 0.05:
            bracket(ax, (hz[0], by + 0.75), (hz[1], by + 0.75), "H zone", side=-1, offset=0.12, color=P.muted())
    if labels:
        for zxi in zx:
            label(ax, (zxi, y - h - 0.15), "Z", size="small", va="top", bold=True)
        label(ax, (xm, y - h - 0.15), "M", size="small", va="top", bold=True)
    return edges


def _actin_line(ax, a, b, y, token, zorder):
    """A thin filament as a beaded double strand along y from x=a to x=b (two offset rows of subunits)."""
    lo, hi = sorted((a, b))
    r = 0.045
    xs = np.arange(lo + r, hi - r * 0.5, r * 1.8)
    for k, x in enumerate(xs):
        off = 0.025 * (1 if k % 2 else -1)
        ax.add_patch(Circle((x, y + off), r, facecolor=P.fill(token) if k % 2 else P.light(token), edgecolor=P.edge(token),
                            lw=0.35, zorder=zorder))


def overlap(SL):
    """Length (µm) of thin–thick filament overlap that carries myosin heads, for sarcomere length SL (µm)."""
    SL = np.asarray(SL, float)
    gap = SL / 2 - (THIN + ZDISC / 2)  # M line to thin-filament tip (negative: thin filaments overlap)
    return np.clip(THICK / 2 - np.maximum(gap, BARE / 2), 0, (THICK - BARE) / 2)


def length_tension(SL):
    """Relative active isometric tension of frog skeletal muscle against sarcomere length (µm), after Gordon,
    Huxley & Julian (1966): zero at 1.27 µm, shoulder 0.87 at 1.67 µm, plateau 2.0–2.25 µm, zero at 3.65 µm."""
    xs = [1.27, 1.67, 2.0, 2.25, 3.65]
    ys = [0.0, 0.87, 1.0, 1.0, 0.0]
    SL = np.asarray(SL, float)
    return np.interp(SL, xs, ys, left=0.0, right=0.0)


# ---------------------------------------------------------------------------------------------
# heart: time-varying elastance model of the left heart


def _activation(t, T, tp, tr):
    """Double-Hill-free normalized activation: a raised-cosine twitch rising for tp and relaxing for tr (s)."""
    tc = np.mod(t, T)
    a = np.where(tc < tp, 0.5 * (1 - np.cos(np.pi * tc / tp)),
                 np.where(tc < tp + tr, 0.5 * (1 + np.cos(np.pi * (tc - tp) / tr)), 0.0))
    return a


def cardiac_cycle(hr=75.0, beats=6, dt=2e-4, params=None):
    """Simulate the left heart and systemic circulation (lumped model) and return the last beat.

    Left atrium and left ventricle are time-varying elastances E(t) = E_min + (E_max − E_min)·a(t), the
    mitral valve a diode with resistance and inertance, the aortic valve an ideal diode, the aorta a three-element Windkessel
    (characteristic impedance, compliance, peripheral resistance) draining into a venous reservoir that
    fills the atrium. Units: mL, mmHg, s. Returns a dict with t (s, from atrial activation of the beat),
    p_lv, p_ao, p_la (mmHg), v_lv (mL), flows q_mv, q_av (mL/s), and event times (s): mitral closure,
    aortic opening, aortic closure, mitral opening, and the ventricular activation onset.
    """
    p = {"Emax_lv": 3.0, "Emin_lv": 0.07, "V0_lv": 10.0, "Emax_la": 0.25, "Emin_la": 0.15, "V0_la": 4.0,
         "R_mv": 0.004, "L_mv": 8e-4, "R_av": 0.004, "Zc": 0.03, "C_ao": 1.3, "R_p": 1.05, "C_v": 18.0, "R_v": 0.015,
         "pr": 0.14, "tp_lv": 0.33, "tr_lv": 0.10, "tp_la": 0.09, "tr_la": 0.09}
    p.update(params or {})
    T = 60.0 / hr
    n = int(beats * T / dt)
    t = np.arange(n) * dt
    a_la = _activation(t, T, p["tp_la"], p["tr_la"])
    a_lv = _activation(t - p["pr"], T, p["tp_lv"], p["tr_lv"])
    E_la = p["Emin_la"] + (p["Emax_la"] - p["Emin_la"]) * a_la
    E_lv = p["Emin_lv"] + (p["Emax_lv"] - p["Emin_lv"]) * a_lv
    V_lv, V_la, P_ao, P_v = 120.0, 60.0, 80.0, 8.0  # initial guesses (mL, mL, mmHg, mmHg)
    q_mv = 0.0  # mitral flow carries inertia (blood mass), so the valve closes only once flow has reversed
    out = np.empty((n, 7))
    for i in range(n):
        p_lv = E_lv[i] * (V_lv - p["V0_lv"])
        p_la = E_la[i] * (V_la - p["V0_la"])
        q_mv = max(0.0, q_mv + dt * (p_la - p_lv - p["R_mv"] * q_mv) / p["L_mv"])
        # aortic valve feeds the Windkessel through Zc: q_av from p_lv - (P_ao + q_av Zc) over R_av
        q_av = max(0.0, (p_lv - P_ao) / (p["R_av"] + p["Zc"]))
        p_root = P_ao + q_av * p["Zc"]
        q_p = (P_ao - P_v) / p["R_p"]
        q_v = max(0.0, (P_v - p_la) / p["R_v"])
        out[i] = (p_lv, p_root, p_la, V_lv, q_mv, q_av, P_v)
        V_lv += dt * (q_mv - q_av)
        V_la += dt * (q_v - q_mv)
        P_ao += dt * (q_av - q_p) / p["C_ao"]
        P_v += dt * (q_p - q_v) / p["C_v"]
    k = t >= (beats - 1) * T
    o = out[k]
    tt = t[k] - (beats - 1) * T
    res = {"t": tt, "p_lv": o[:, 0], "p_ao": o[:, 1], "p_la": o[:, 2], "v_lv": o[:, 3], "q_mv": o[:, 4], "q_av": o[:, 5],
           "T": T, "t_qrs": p["pr"]}
    mv_open, av_open = o[:, 4] > 1e-6, o[:, 5] > 1e-6

    def edges(b):
        d = np.diff(b.astype(int))
        return tt[1:][d == 1], tt[1:][d == -1]

    mo, mc = edges(mv_open)
    ao, ac = edges(av_open)
    res.update({"aortic_open": ao[0] if len(ao) else np.nan, "aortic_close": ac[0] if len(ac) else np.nan})
    before = mc[mc < res["aortic_open"]] if len(mc) else mc
    res["mitral_close"] = before[-1] if len(before) else np.nan
    after = mo[mo > res["aortic_close"]] if len(mo) else mo
    res["mitral_open"] = after[0] if len(after) else np.nan
    return res


def ecg(t, t_qrs, T, pr=0.16):
    """A schematic ECG (mV) built from Gaussian P, Q, R, S and T waves aligned to ventricular activation at t_qrs."""
    t = np.asarray(t, float)
    waves = [(-pr + 0.06, 0.025, 0.15), (-0.02, 0.008, -0.12), (0.0, 0.01, 1.1), (0.022, 0.009, -0.25), (0.30, 0.045, 0.3)]
    v = np.zeros_like(t)
    for off, w, amp in waves:
        for k in (-1, 0, 1):
            v += amp * np.exp(-0.5 * ((t - (t_qrs + off + k * T)) / w) ** 2)
    return v


__all__ = ["motor_head", "coiled_coil", "kinesin", "bead", "optical_trap", "sarcomere", "overlap", "length_tension",
           "cardiac_cycle", "ecg", "THICK", "THIN", "BARE", "ZDISC"]
