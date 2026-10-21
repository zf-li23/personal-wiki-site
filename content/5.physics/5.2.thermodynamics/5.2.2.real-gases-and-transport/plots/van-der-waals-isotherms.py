"""Van der Waals isotherms in reduced variables, with the Maxwell equal-area construction below the critical point."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq


def p_vdw(v, t):
    # reduced van der Waals equation: (p + 3/v^2)(3v - 1) = 8t
    return 8 * t / (3 * v - 1) - 3 / v**2


def volumes(p, t):
    # real roots of 3p v^3 - (p + 8t) v^2 + 9v - 3 = 0 with v > 1/3
    roots = np.roots([3 * p, -(p + 8 * t), 9, -3])
    real = np.sort(roots[np.abs(roots.imag) < 1e-9].real)
    return real[real > 1 / 3]


def maxwell_construction(t):
    # equal-area rule: choose the vapour pressure so that the two loops have equal area
    vs = np.linspace(0.34, 50, 200000)
    ps = p_vdw(vs, t)
    dp = np.diff(ps)
    turn = np.where(np.sign(dp[1:]) != np.sign(dp[:-1]))[0]
    p_lo, p_hi = max(ps[turn[0] + 1], 1e-9), ps[turn[1] + 1]

    def area(p):
        v = volumes(p, t)
        vl, vg = v[0], v[-1]
        integral = (8 * t / 3) * np.log((3 * vg - 1) / (3 * vl - 1)) + 3 / vg - 3 / vl
        return integral - p * (vg - vl)

    p_sat = brentq(area, p_lo + 1e-12, p_hi - 1e-12)
    v = volumes(p_sat, t)
    return v[0], v[-1], p_sat


fig, ax = plt.subplots(figsize=(6.8, 4.6))
v = np.linspace(0.42, 5, 1500)

temps = [0.85, 0.9, 0.95, 1.0, 1.1, 1.2]
coex_l, coex_g, coex_p = [], [], []
for i, t in enumerate(temps):
    p = p_vdw(v, t)
    if t < 1:
        vl, vg, ps = maxwell_construction(t)
        inside = (v > vl) & (v < vg)
        ax.plot(v[~inside & (v < vl)], p[~inside & (v < vl)], color=f"C{i}", lw=1.6, label=f"T/Tc = {t}")
        ax.plot(v[v > vg], p[v > vg], color=f"C{i}", lw=1.6)
        ax.plot(v[inside], p[inside], color=f"C{i}", lw=1, ls="--")
        ax.plot([vl, vg], [ps, ps], color=f"C{i}", lw=1.6)
    else:
        ax.plot(v, p, color=f"C{i}", lw=1.6, label=f"T/Tc = {t}")

# coexistence (binodal) curve
for t in np.linspace(0.8, 0.999, 60):
    vl, vg, ps = maxwell_construction(t)
    coex_l.append(vl)
    coex_g.append(vg)
    coex_p.append(ps)
vb = np.concatenate([coex_l, [1.0], coex_g[::-1]])
pb = np.concatenate([coex_p, [1.0], coex_p[::-1]])
ax.plot(vb, pb, color="0.5", lw=1, ls=":", label="coexistence curve")
ax.plot([1], [1], "o", color="black", ms=4)
ax.annotate("critical point", (1, 1), (1.4, 1.35), fontsize=9, arrowprops=dict(arrowstyle="->", lw=0.8))

ax.set_xlim(0.4, 5)
ax.set_ylim(0, 2)
ax.set_xlabel(r"reduced volume $V_{\mathrm{m}}/V_{\mathrm{m,c}}$")
ax.set_ylabel(r"reduced pressure $p/p_{\mathrm{c}}$")
ax.set_title("Van der Waals isotherms (dashed: metastable and unstable parts)")
ax.legend(fontsize=8, loc="upper right")
fig.tight_layout()
