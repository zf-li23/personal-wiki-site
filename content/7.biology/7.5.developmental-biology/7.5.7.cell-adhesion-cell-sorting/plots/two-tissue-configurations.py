"""Equilibrium configurations of two tissues by differential adhesion.

Adhesive energies per unit contact area E_AA > E_BB (A more cohesive), E_AB between them; the medium
does not adhere. Interfacial tensions: gamma_AO = E_AA/2, gamma_BO = E_BB/2,
gamma_AB = (E_AA + E_BB)/2 - E_AB.
A: regions in the plane (E_BB/E_AA, E_AB/E_AA): mixing if E_AB > (E_AA + E_BB)/2 (gamma_AB < 0);
complete engulfment of A by B if E_BB <= E_AB <= (E_AA + E_BB)/2; partial engulfment if
0 < E_AB < E_BB; separation if E_AB <= 0. Dots mark the cases of panel B.
B: axisymmetric equilibrium shapes of two equal volumes of A (red) and B (blue) for E_BB/E_AA = 0.5 and
E_AB/E_AA = 0.02, 0.15, 0.3 and 0.45, obtained by minimizing the total interfacial energy
gamma_AO S_AO + gamma_BO S_BO + gamma_AB S_AB over three spherical caps on a common contact circle
(radius a) at fixed volumes; then complete engulfment (E_AB/E_AA = 0.6; the position of the inner
sphere is not fixed by surface energy) and a mixed aggregate (E_AB/E_AA = 0.9).
"""

import numpy as np
from scipy.optimize import minimize

import wikibio as bio
from wikibio import charts

P = bio.P


def cap_area(a, h):
    return np.pi * (a * a + h * h)


def cap_vol(a, h):
    return np.pi * h * (3 * a * a + h * h) / 6


def shape(gAO, gBO, gAB):
    V = 4 * np.pi / 3

    def energy(z):
        a, h1, h2, h3 = z
        return gAO * cap_area(a, h1) + gBO * cap_area(a, h2) + gAB * cap_area(a, h3)

    cons = [{"type": "eq", "fun": lambda z: cap_vol(z[0], z[1]) - cap_vol(z[0], z[3]) - V},
            {"type": "eq", "fun": lambda z: cap_vol(z[0], z[2]) + cap_vol(z[0], z[3]) - V}]
    best = None
    for a0 in (0.3, 0.6, 0.9):
        r = minimize(energy, [a0, 1.5, 1.5, 0.0], constraints=cons, method="SLSQP",
                     bounds=[(1e-3, 3), (1e-3, 4), (1e-3, 4), (-3, 3)], options={"maxiter": 500, "ftol": 1e-12})
        if r.success and (best is None or r.fun < best.fun):
            best = r
    return best.x


def cap_curve(a, h, n=120):
    """Points of a spherical cap of base radius a and signed height h, from (-a, 0) to (a, 0)."""
    if abs(h) < 1e-6:
        return np.c_[np.linspace(-a, a, n), np.zeros(n)]
    R = (a * a + h * h) / (2 * abs(h))
    cz = np.sign(h) * (abs(h) - R)
    t0 = np.arctan2(-cz, -a)
    t1 = np.arctan2(-cz, a)
    if h > 0:
        ts = np.linspace(t0, t1 + (2 * np.pi if t1 > t0 else 0) - 2 * np.pi * (t1 > t0), n)
        ts = np.linspace(t0, t1 - 2 * np.pi if t1 > t0 else t1, n) if t1 > t0 else np.linspace(t0, t1, n)
    else:
        ts = np.linspace(t0, t1 + 2 * np.pi if t1 < t0 else t1, n)
    return np.c_[R * np.cos(ts), cz + R * np.sin(ts)]


fig, ax = bio.canvas(31.0, 11.0)
bio.panel(ax, "A", (0.1, 10.9))
pa = charts.axes_at(ax, (1.9, 1.6, 7.8, 8.0))
x = np.linspace(0, 1, 200)
cmix, ceng, cpar, csep = P.light("negative"), P.light("positive"), P.light("highlight"), P.light("neutral")
pa.fill_between(x, (1 + x) / 2, 1.0, color=cmix, lw=0)
pa.fill_between(x, x, (1 + x) / 2, color=ceng, lw=0)
pa.fill_between(x, 0, x, color=cpar, lw=0)
pa.fill_between(x, -0.1, 0, color=csep, lw=0)
for yy in ((1 + x) / 2, x):
    pa.plot(x, yy, color=P.muted(), lw=0.9)
pa.axhline(0, color=P.muted(), lw=0.9)
fs = bio.core.FONT["tiny"]
pa.text(0.2, 0.86, "mixing", fontsize=fs, color=P.ink())
pa.text(0.2, 0.43, "complete\nengulfment", fontsize=fs, color=P.ink())
pa.text(0.62, 0.22, "partial\nengulfment", fontsize=fs, color=P.ink())
pa.text(0.4, -0.065, "separation", fontsize=fs, color=P.ink())
cases = [0.02, 0.15, 0.3, 0.45, 0.6, 0.9]
pa.plot([0.5] * len(cases), cases, "o", color=P.ink(), ms=3.5)
pa.set_xlim(0, 1)
pa.set_ylim(-0.1, 1.0)
charts.style_axes(pa, "E_BB / E_AA", "E_AB / E_AA")
charts.title(pa, "Outcome of mixing two cell types")

bio.panel(ax, "B", (11.0, 10.9))
EAA, EBB = 1.0, 0.5
gAO, gBO = EAA / 2, EBB / 2
cols = {"A": ("mesoderm",), "B": ("ectoderm",)}
xs = [13.4, 17.6, 21.8, 26.0, 15.5, 23.9]
ys = [7.6, 7.6, 7.6, 7.6, 2.8, 2.8]
for k, EAB in enumerate(cases):
    cx, cy = xs[k], ys[k]
    gAB = (EAA + EBB) / 2 - EAB
    sc = 1.0
    if k < 4:
        a, h1, h2, h3 = shape(gAO, gBO, gAB)
        top = cap_curve(a, h1)          # A-O, above
        bot = cap_curve(a, -h2)         # B-O, below
        mid = cap_curve(a, h3)          # A-B interface
        polyA = np.vstack([top, mid[::-1]])
        polyB = np.vstack([bot, mid[::-1]])
        rot = np.array([[0, -1], [1, 0]])  # A to the left, B to the right
        for poly, tok in ((polyB, "ectoderm"), (polyA, "mesoderm")):
            pts = (poly @ rot.T) * sc + np.array([cx, cy])
            bio.shape(ax, pts, tok, lw=1.0, zorder=5)
        lab = f"E_AB/E_AA = {EAB:g}"
    elif k == 4:
        Rb = 2 ** (1 / 3)
        t = np.linspace(0, 2 * np.pi, 200)
        bio.shape(ax, np.c_[cx + Rb * np.cos(t), cy + Rb * np.sin(t)], "ectoderm", lw=1.0)
        bio.shape(ax, np.c_[cx + 0.15 + np.cos(t), cy + 0.08 + np.sin(t)], "mesoderm", lw=1.0, zorder=6)
        lab = "E_AB/E_AA = 0.6 (complete)"
    else:
        rng = np.random.default_rng(3)
        Rb = 2 ** (1 / 3)
        t = np.linspace(0, 2 * np.pi, 200)
        ax.plot(cx + Rb * np.cos(t), cy + Rb * np.sin(t), color=P.muted(), lw=0.8)
        g = np.arange(-1.2, 1.25, 0.24)
        for gx in g:
            for gy in g:
                if gx * gx + gy * gy < 1.2:
                    tok = "mesoderm" if rng.random() < 0.5 else "ectoderm"
                    tt = np.linspace(0, 2 * np.pi, 20)
                    bio.shape(ax, np.c_[cx + gx + 0.11 * np.cos(tt), cy + gy + 0.11 * np.sin(tt)], tok, lw=0.4)
        lab = "E_AB/E_AA = 0.9 (mixed)"
    bio.label(ax, (cx, cy - 2.05), lab, size="tiny")
bio.label(ax, (19.7, 10.4), "E_BB/E_AA = 0.5;  A red, B blue", size="small")
