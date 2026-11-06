# Nutrient depletion zones around a root: a numerical solution of radial diffusion towards a cylindrical root
# that absorbs with Michaelis-Menten kinetics (the classic single-root model of soil nutrient supply).
#   b dC/dt = (1/r) d/dr (r De dC/dr),  r0 < r < R;   flux into the root at r0: Imax C / (Km + C);  no flux at R.
# C is the concentration in the soil solution, De the effective diffusion coefficient of the solute in soil
# (the free-water value reduced by water content and tortuosity) and b the buffer power (total labile nutrient per
# unit dissolved). Illustrative values of the usual orders of magnitude: nitrate De = 5e-11 m2/s, b = 1,
# C0 = 1 mM, Km = 50 uM; potassium De = 2e-11, b = 10, C0 = 0.2 mM, Km = 20 uM; phosphate De = 1e-12, b = 200,
# C0 = 5 uM, Km = 3 uM; root radius r0 = 0.15 mm, Imax = 5e-8 mol m-2 s-1 for all three.
# A: profiles C/C0 against distance from the root surface after 1, 4 and 10 days (log distance axis).
# B: width of the depletion zone (distance at which C falls below 90 % of C0) against time.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
r0 = 0.15e-3
Imax = 5e-8
solutes = [("nitrate", 5e-11, 1.0, 1.0, 0.05, 30e-3, "dna"),
           ("potassium", 2e-11, 10.0, 0.2, 0.02, 10e-3, "k"),
           ("phosphate", 1e-12, 200.0, 5e-3, 3e-3, 2e-3, "rna")]
days = [1, 4, 10]


def solve(De, b, C0, Km, R):
    # finite volumes on a geometric grid, implicit Euler (uptake linearized at the old concentration);
    # concentrations in mol/m3 (= mM)
    from scipy.linalg import solve_banded
    n = 160
    edges = r0 + (R - r0) * (np.geomspace(1, 1001, n + 1) - 1) / 1000
    rc = 0.5 * (edges[1:] + edges[:-1])
    vol = 0.5 * (edges[1:] ** 2 - edges[:-1] ** 2) * b  # per radian per metre of root
    g = De * edges[1:-1] / np.diff(rc)  # conductance between neighbouring cells
    dt = 1800.0
    C = np.full(n, C0)
    out, widths = {}, []
    nsteps = int(days[-1] * 86400 / dt)
    for step in range(1, nsteps + 1):
        ab = np.zeros((3, n))
        diag = vol / dt
        diag = diag.copy()
        diag[:-1] += g
        diag[1:] += g
        diag[0] += r0 * Imax / (Km + C[0])
        ab[1] = diag
        ab[0, 1:] = -g
        ab[2, :-1] = -g
        C = solve_banded((1, 1), ab, vol / dt * C)
        t = step * dt / 86400
        if step % 8 == 0:
            below = rc[C < 0.9 * C0]
            widths.append((t, (below.max() - r0) * 1e3 if below.size else 0.0))
        for d in days:
            if d not in out and t >= d - 1e-9:
                out[d] = C.copy()
    return (rc - r0) * 1e3, out, np.array(widths)


fig, axs = plt.subplots(1, 2, figsize=(12.0, 4.3), gridspec_kw=dict(wspace=0.3, width_ratios=[1.35, 1]))
ax = axs[0]
styles = {1: ":", 4: "--", 10: "-"}
results = {}
for name, De, b, C0, Km, R, tok in solutes:
    x, out, w = solve(De, b, C0, Km, R)
    results[name] = w
    for d in days:
        ax.plot(np.maximum(x, 1e-3), out[d] / C0, color=charts.line(tok), lw=1.8, ls=styles[d])
    lx, ly = {"nitrate": (0.0015, 0.39), "potassium": (1.6, 0.45), "phosphate": (0.0035, 0.2)}[name]
    ax.text(lx, ly, name, color=charts.line(tok), fontsize=7.5)
for d in days:
    ax.plot([], [], color=P.muted(), ls=styles[d], label=f"{d} d")
ax.set_xscale("log")
ax.set_xlim(1e-3, 30)
ax.set_ylim(0, 1.08)
ax.legend(fontsize=7, frameon=False, loc="lower right")
charts.style_axes(ax, "distance from root surface / mm", "$C/C_0$ in soil solution")
charts.title(ax, "A   Concentration profiles")

ax = axs[1]
for name, De, b, C0, Km, R, tok in solutes:
    w = results[name]
    ax.plot(w[:, 0], w[:, 1], color=charts.line(tok), lw=2.0, label=name)
ax.set_yscale("log")
ax.set_ylim(0.01, 30)
ax.set_xlim(0, 10)
ax.legend(fontsize=7, frameon=False, loc="lower right")
charts.style_axes(ax, "time / d", "depletion-zone width / mm")
charts.title(ax, "B   Growth of the depletion zone")
