"""The four outcomes of the Lotka-Volterra competition model in the phase plane.

dN1/dt = r1 N1 (K1 - N1 - a12 N2) / K1, dN2/dt = r2 N2 (K2 - N2 - a21 N1) / K2, with K1 = K2 = 100,
r1 = 1, r2 = 0.8. Lines: zero net growth isoclines of species 1 (N1 + a12 N2 = K1) and species 2
(N2 + a21 N1 = K2); gray: the direction field; thin lines: trajectories from several initial densities.
Filled points: stable equilibria; open: unstable node (origin) or saddle. A: a12 = 0.6, a21 = 1.4,
species 1 excludes species 2. B: a12 = 1.4, a21 = 0.6, species 2 wins. C: a12 = 1.5, a21 = 1.3, each
species inhibits the other more than itself: the interior equilibrium is a saddle whose stable manifold
(dashed) separates the basins of the two exclusion equilibria. D: a12 = 0.5, a21 = 0.6, stable coexistence.
"""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
K1 = K2 = 100.0
r1, r2 = 1.0, 0.8
CASES = [
    ("A", "Species 1 wins", 0.6, 1.4),
    ("B", "Species 2 wins", 1.4, 0.6),
    ("C", "Outcome depends on initial densities", 1.5, 1.3),
    ("D", "Stable coexistence", 0.5, 0.6),
]
c1, c2 = Q.line_color("dna"), Q.line_color("rna")


def field(a12, a21):
    def f(t, n):
        n1, n2 = n
        return [r1 * n1 * (K1 - n1 - a12 * n2) / K1, r2 * n2 * (K2 - n2 - a21 * n1) / K2]
    return f


def jac(a12, a21, n1, n2):
    return np.array([[r1 * (K1 - 2 * n1 - a12 * n2) / K1, -r1 * a12 * n1 / K1],
                     [-r2 * a21 * n2 / K2, r2 * (K2 - 2 * n2 - a21 * n1) / K2]])


fig, ax = bio.canvas(30.0, 30.0)
for k, (tag, name, a12, a21) in enumerate(CASES):
    x0 = 2.4 + (k % 2) * 15.0
    y0 = 17.0 - (k // 2) * 15.0
    pa = C.axes_at(ax, (x0, y0, 11.0, 11.0))
    lim = 1.25 * max(K1, K2, K1 / a12, K2 / a21)
    lim = min(lim, 220)
    f = field(a12, a21)
    g = np.linspace(0.5, lim, 24)
    X, Y = np.meshgrid(g, g)
    U, V = f(0, [X, Y])
    pa.streamplot(X, Y, U, V, color=P.mix(P.muted(), P.surface(), 0.45), linewidth=0.5, density=0.8,
                  arrowsize=0.7)
    n = np.linspace(0, lim, 50)
    pa.plot(n, (K1 - n) / a12, color=c1, lw=1.9, label="species 1 isocline")
    pa.plot(n, K2 - a21 * n, color=c2, lw=1.9, label="species 2 isocline")
    starts = [(5, 5), (lim * 0.9, 8), (8, lim * 0.9), (lim * 0.9, lim * 0.9), (lim * 0.5, 3), (3, lim * 0.5)]
    if tag == "C":
        starts += [(60, 75), (75, 60)]
    for s in starts:
        sol = solve_ivp(f, (0, 80), s, rtol=1e-8, max_step=0.2)
        pa.plot(sol.y[0], sol.y[1], color=P.ink(), lw=0.7, alpha=0.8)
    det = 1 - a12 * a21
    eqs = [(0, 0), (K1, 0), (0, K2)]
    ns = ((K1 - a12 * K2) / det, (K2 - a21 * K1) / det)
    if ns[0] > 0 and ns[1] > 0:
        eqs.append(ns)
    for e in eqs:
        ev = np.linalg.eigvals(jac(a12, a21, *e))
        stable = np.all(ev.real < 0)
        pa.plot(*e, "o", ms=6, mfc=P.ink() if stable else P.surface(), mec=P.ink(), mew=1.2, zorder=6,
                clip_on=False)
    if tag == "C":
        # Stable manifold of the saddle: integrate backward in time from points beside it.
        J = jac(a12, a21, *ns)
        w, v = np.linalg.eig(J)
        vs = v[:, np.argmin(w.real)]
        for sgn in (1, -1):
            p0 = np.array(ns) + sgn * 0.5 * vs
            back = solve_ivp(lambda t, y: [-z for z in f(t, y)], (0, 40), p0, rtol=1e-9, max_step=0.05)
            ok = (back.y[0] >= 0) & (back.y[1] >= 0) & (back.y[0] <= lim) & (back.y[1] <= lim)
            pa.plot(back.y[0][ok], back.y[1][ok], color=P.muted(), lw=1.3, ls=(0, (4, 2)))
    pa.set_xlim(0, lim)
    pa.set_ylim(0, lim)
    ticks = sorted({0, K1, round(K2 / a21)})
    pa.set_xticks(ticks)
    pa.set_xticklabels(["0" if t == 0 else ("$K_1$" if t == K1 else r"$K_2/\alpha_{21}$") for t in ticks])
    yt = sorted({0, K2, round(K1 / a12)})
    pa.set_yticks(yt)
    pa.set_yticklabels(["0" if t == 0 else ("$K_2$" if t == K2 else r"$K_1/\alpha_{12}$") for t in yt])
    C.style_axes(pa, "$N_1$", "$N_2$")
    if k == 0:
        pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
    bio.panel(ax, tag, (x0 - 2.0, y0 + 12.6))
    bio.label(ax, (x0, y0 + 12.2), f"{name}  ($\\alpha_{{12}}$ = {a12}, $\\alpha_{{21}}$ = {a21})", size="small", bold=True, ha="left")
