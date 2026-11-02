"""A minimal model of the CI-Cro switch of phage lambda (dimensionless; not fitted to data).

dc/dt = 4 (0.05 + c^2) / (1 + c^2 + 4 r^2) - (1 + d) c     (CI: activates its own promoter P_RM,
                                                            which Cro represses; d = extra removal of CI
                                                            by RecA-stimulated self-cleavage)
dr/dt = 3 / (1 + 4 c^2 + (r/3)^2) - r                     (Cro: from P_R, repressed by CI and, weakly,
                                                            by Cro itself)
A: d = 0. The nullclines cross three times: a lysogenic state (CI high), a lytic state (Cro high) and a
saddle between them; trajectories from different initial conditions go to one or the other.
B: d = 1 (DNA damage): the lysogenic state has disappeared and every trajectory goes to the lytic state.
C: CI at the fixed points against d (solid: stable, dashed: unstable). The lysogenic state ends in a
saddle-node bifurcation at d_c; the lytic state exists for all d, so the decision is irreversible.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P


def F(c, r, d):
    return 4 * (0.05 + c ** 2) / (1 + c ** 2 + 4 * r ** 2) - (1 + d) * c


def G(c, r):
    return 3 / (1 + 4 * c ** 2 + (r / 3) ** 2) - r


def r_null(c):
    return brentq(lambda r: G(c, r), 0, 5)


def fixed_points(d):
    cs = np.linspace(1e-4, 5, 801)
    v = np.array([F(c, r_null(c), d) for c in cs])
    out = []
    for i in np.where(np.sign(v[:-1]) != np.sign(v[1:]))[0]:
        c = brentq(lambda c: F(c, r_null(c), d), cs[i], cs[i + 1])
        out.append((c, r_null(c)))
    return out


def stable(c, r, d, h=1e-6):
    J = np.array([[(F(c + h, r, d) - F(c - h, r, d)) / (2 * h), (F(c, r + h, d) - F(c, r - h, d)) / (2 * h)],
                  [(G(c + h, r) - G(c - h, r)) / (2 * h), (G(c, r + h) - G(c, r - h)) / (2 * h)]])
    return np.all(np.linalg.eigvals(J).real < 0)


fig, axes = plt.subplots(1, 3, figsize=(11, 3.5))
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.16, top=0.86, wspace=0.32)
cg = np.linspace(0, 4.5, 300)
for ax, d, title in [(axes[0], 0.0, "A  No damage: two stable states"), (axes[1], 1.0, "B  DNA damage (d = 1): lysis only")]:
    C, R = np.meshgrid(np.linspace(0.05, 4.4, 14), np.linspace(0.05, 2.5, 12))
    U, V = F(C, R, d), G(C, R)
    nrm = np.hypot(U / 4.5, V / 2.6) + 1e-12
    ax.quiver(C, R, 0.04 * U / nrm, 0.04 * 2.6 / 4.5 * V / nrm, color=P.muted(), alpha=0.6, angles="xy",
              scale_units="xy", scale=0.55, width=0.004, headwidth=4, headlength=4, pivot="mid")
    ax.contour(cg, np.linspace(0, 2.6, 300), F(*np.meshgrid(cg, np.linspace(0, 2.6, 300)), d), levels=[0],
               colors=[charts.line("protein")], linewidths=1.5)
    ax.plot(cg, [r_null(c) for c in cg], color=charts.line("receptor"), lw=1.5)
    for c0, r0 in [(0.3, 2.4), (4.3, 0.2), (2.0, 0.5), (1.0, 1.0), (4.3, 1.4), (0.6, 0.1)]:
        s = solve_ivp(lambda t, z: [F(z[0], z[1], d), G(z[0], z[1])], (0, 30), [c0, r0], max_step=0.05)
        ax.plot(s.y[0], s.y[1], color=P.ink(), lw=0.8)
    for c, r in fixed_points(d):
        st = stable(c, r, d)
        ax.plot(c, r, "o", ms=6, color=P.ink(), mfc=P.ink() if st else "none")
    ax.text(3.0, 2.35, "CI nullcline", fontsize=7, color=charts.line("protein"))
    ax.text(3.0, 2.15, "Cro nullcline", fontsize=7, color=charts.line("receptor"))
    ax.set_xlim(0, 4.5)
    ax.set_ylim(0, 2.6)
    charts.style_axes(ax, "CI, c", "Cro, r")
    charts.title(ax, title)

ax = axes[2]
ds = np.linspace(0, 1.5, 301)
br = {"lys": [], "sad": [], "lyt": []}
for d in ds:
    fp = fixed_points(d)
    br["lyt"].append((d, fp[0][0]))
    if len(fp) == 3:
        br["sad"].append((d, fp[1][0]))
        br["lys"].append((d, fp[2][0]))
lys, sad, lyt = (np.array(br[k]) for k in ("lys", "sad", "lyt"))
ax.plot(lys[:, 0], lys[:, 1], color=charts.line("protein"), lw=1.8, label="lysogenic (stable)")
ax.plot(sad[:, 0], sad[:, 1], color=P.muted(), lw=1.2, ls="--", label="saddle")
ax.plot(lyt[:, 0], lyt[:, 1], color=charts.line("receptor"), lw=1.8, label="lytic (stable)")
ax.axvline(lys[-1, 0], color=P.muted(), lw=0.7, ls=":")
ax.text(lys[-1, 0] + 0.03, 0.6, f"d_c = {lys[-1, 0]:.2f}", fontsize=7, color=P.ink())
ax.set_ylim(0, 4)
ax.legend(fontsize=7, frameon=False, loc="upper right")
charts.style_axes(ax, "extra CI removal, d", "CI at fixed points")
charts.title(ax, "C  Induction is a saddle-node bifurcation")
