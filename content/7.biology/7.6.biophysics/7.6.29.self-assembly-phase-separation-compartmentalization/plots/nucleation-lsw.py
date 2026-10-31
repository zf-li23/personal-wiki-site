"""Nucleation and Ostwald ripening of droplets. A: classical nucleation theory: free energy of a
spherical droplet of radius R, Delta G(R) = 4 pi R^2 gamma - (4 pi/3) R^3 Delta mu / v, in units with
gamma a^2 = k_B T and v = (4 pi/3) a^3, for three supersaturations Delta mu/k_B T; the maximum at the
critical radius R* = 2 gamma v / Delta mu is the nucleation barrier. B: barrier height
Delta G* = 16 pi gamma^3 v^2 / (3 Delta mu^2) for condensate-like parameters (molecular volume in the
dense phase v = 4e-25 m^3, surface tensions 0.1, 1 and 10 uN/m) against the supersaturation ln(c/c_sat):
with ultralow surface tensions the barrier exceeds 10 k_B T (shaded band 10-30 k_B T) only very close
to saturation. C, D: Lifshitz-Slyozov-Wagner coarsening, simulated for 40 000 droplets with the
diffusion-limited growth law dR/dt = (1/R)(1/R_c - 1/R) (radii in units of the initial mean, time in
units of R0^3 c_in/(D c_0 l_gamma)), the critical radius R_c equal to the mean radius by conservation
of droplet volume. C: the cube of the mean radius grows linearly, at a rate that approaches the LSW value 4/9
(dashed) slowly from the narrow initial distribution, and the number of droplets falls as 1/t. D: the scaled size distribution at late times approaches the universal LSW
distribution (curve), which ends sharply at 1.5 times the mean radius."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 4, figsize=(11.4, 3.1))
fig.subplots_adjust(wspace=0.5, left=0.05, right=0.985, bottom=0.17, top=0.87)

ax = axs[0]
r = np.linspace(0, 14, 400)
for dmu, tok in [(1.0, "dna"), (1.5, "bacterium"), (2.5, "blood")]:
    dG = 4 * np.pi * r ** 2 - r ** 3 * dmu
    ax.plot(r, dG, color=charts.line(tok), lw=1.6, label=rf"$\Delta\mu = {dmu:g}\,k_{{\mathrm{{B}}}}T$")
    rs = 8 * np.pi / (3 * dmu)
    ax.plot([rs], [4 * np.pi * rs ** 2 - rs ** 3 * dmu], "o", ms=3.5, color=charts.line(tok))
ax.axhline(0, color=P.muted(), lw=0.7)
ax.set_ylim(-150, 330)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "droplet radius $R/a$", r"$\Delta G(R)/k_{\mathrm{B}}T$")
charts.title(ax, "A  Nucleation barrier")

ax = axs[1]
kT = 4.1e-21
v = 4e-25
lnS = np.logspace(-4, 0, 200)
ax.axhspan(10, 30, color=P.fill("highlight"), alpha=0.35, lw=0)
for g, tok in [(1e-7, "dna"), (1e-6, "bacterium"), (1e-5, "blood")]:
    dGs = 16 * np.pi * g ** 3 * v ** 2 / (3 * (lnS * kT) ** 2) / kT
    ax.loglog(lnS, dGs, color=charts.line(tok), lw=1.6, label=rf"$\gamma = {g * 1e6:g}\ \mu\mathrm{{N\,m^{{-1}}}}$")
ax.set_ylim(1e-3, 1e5)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, r"supersaturation $\ln(c/c_{\mathrm{sat}})$", r"$\Delta G^*/k_{\mathrm{B}}T$")
charts.title(ax, "B  Condensates")

# ---- LSW simulation in the variable u = R^3
rng = np.random.default_rng(0)
u = np.clip(rng.normal(1.0, 0.25, 40000), 0.3, None) ** 3
t = 0.0
rec_t, rec_R3, rec_N = [], [], []
nxt = 0.5
while t < 200:
    R = np.cbrt(u)
    Rc = R.mean()
    dt = 0.003 * Rc ** 3
    u = u + dt * 3 * (R / Rc - 1)
    u = u[u > 0]
    t += dt
    if t >= nxt:
        R = np.cbrt(u)
        rec_t.append(t)
        rec_R3.append(R.mean() ** 3)
        rec_N.append(len(u))
        nxt += 2.0
final_R = np.cbrt(u)

ax = axs[2]
rec_t, rec_R3, rec_N = map(np.array, (rec_t, rec_R3, rec_N))
ax.plot(rec_t, rec_R3, color=charts.line("protein"), lw=1.8, label=r"$\langle R\rangle^3$")
ax.plot(rec_t, rec_R3[-1] + 4 / 9 * (rec_t - rec_t[-1]), "--", color=P.muted(), lw=1.0, label="slope 4/9")
ax2 = ax.twinx()
ax2.plot(rec_t, rec_N, color=charts.line("bacterium"), lw=1.4, label="number")
ax2.set_ylim(0, 42000)
charts.style_axes(ax2, None, None, box=True)
ax2.text(150, 9000, "number of\ndroplets", fontsize=FT["tiny"], color=charts.line("bacterium"), ha="center")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "time $t$", r"$\langle R\rangle^3 / R_0^3$")
charts.title(ax, "C  LSW coarsening")

ax = axs[3]
rho = final_R / final_R.mean()
ax.hist(rho, bins=np.linspace(0, 1.7, 30), density=True, color=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.5,
        label=f"simulation, t = {rec_t[-1]:.0f}")
x = np.linspace(1e-4, 1.5 - 1e-4, 400)
lsw = x ** 2 * (3 / (3 + x)) ** (7 / 3) * (1.5 / (1.5 - x)) ** (11 / 3) * np.exp(-x / (1.5 - x))
lsw /= np.trapezoid(lsw, x)
ax.plot(x, lsw, color=charts.line("blood"), lw=1.6, label="LSW distribution")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"scaled radius $R/\langle R\rangle$", "probability density")
charts.title(ax, "D  Size distribution")
