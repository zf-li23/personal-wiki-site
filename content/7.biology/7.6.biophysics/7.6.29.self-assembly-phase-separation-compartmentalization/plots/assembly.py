"""Ordered self-assembly. A: equilibrium of linear aggregation. In isodesmic assembly every addition
has the same equilibrium constant K, so the fraction of subunits in polymers rises gradually with the
total concentration c (in units of 1/K). In nucleated (cooperative) assembly the first contact is weaker
by a factor sigma = 1e-3 (a nucleus must form before elongation), and polymer appears only above the
critical concentration c* = 1/K, after which the free subunit concentration stays at c*.
B, C: kinetics of icosahedral capsid assembly in a Zlotnick-type model: 12 pentameric subunits, a
trimer nucleus (two weak nucleation steps), then elongation in which each addition makes two to four
contacts. B: fraction of subunits in complete capsids against time for three total concentrations
(lag phase, then sigmoidal growth). C: yield of complete capsids at a fixed late time against the
total concentration and the contact free energy: too weak, nothing assembles; too strong or too
concentrated, nuclei form so fast that free subunits run out and partial shells are kinetically trapped."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.3))
fig.subplots_adjust(wspace=0.4, left=0.06, right=0.98, bottom=0.17, top=0.87)

# ---- A: equilibrium linear aggregation
ax = axs[0]
ctot = np.logspace(-2, 2, 300)


def polymer_fraction(c, sigma):
    # free monomer x (units 1/K); dimer+ concentrations: sigma * x^n for n >= 2 (sum n x^n)
    def mass(x):
        return x + sigma * (x / (1 - x) ** 2 - x)

    x = brentq(lambda x: mass(x) - c, 0, 1 - 1e-12)
    return 1 - x / c, x


for sigma, tok, lab in [(1.0, "dna", r"isodesmic ($\sigma = 1$)"), (1e-3, "blood", r"nucleated ($\sigma = 10^{-3}$)")]:
    fr = np.array([polymer_fraction(c, sigma)[0] for c in ctot])
    ax.plot(ctot, fr, color=charts.line(tok), lw=1.8, label=lab)
ax.axvline(1, color=P.muted(), lw=0.8, ls=":")
ax.text(1.15, 0.45, r"$c^* = 1/K$", fontsize=FT["tiny"], color=P.ink())
ax.set_xscale("log")
ax.set_ylim(0, 1.02)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"total subunit concentration $cK$", "fraction in polymers")
charts.title(ax, "A  Isodesmic vs nucleated")

# ---- B, C: capsid assembly kinetics (12 subunits, nucleus = 3)
N = 12
KNUC = 300.0
contacts = np.array([0, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4])  # contacts made when subunit i+1 joins (index i = size before)


def rhs(t, y, g):
    # y[i] = concentration of i+1-mers (dimensionless, k_on = 1)
    c1 = y[0]
    flux = np.zeros(N - 1)  # i -> i+1 net, i = 1..N-1
    for i in range(1, N):
        n_c = contacts[i] if i >= 3 else 1  # nucleation steps (to dimer, to trimer) make one weak contact
        kb = KNUC * np.exp(-g) if i < 3 else np.exp(-n_c * g)  # nucleation: one contact, entropically disfavored
        fwd = c1 * y[i - 1] * (1.0 if i > 1 else 0.5)
        bwd = kb * y[i]
        flux[i - 1] = fwd - bwd
    dy = np.zeros(N)
    dy[0] = -2 * flux[0] - np.sum(flux[1:])
    for i in range(1, N):
        dy[i] += flux[i - 1]
        if i < N - 1:
            dy[i] -= flux[i]
    return dy


def run(ctot, g, tmax):
    y0 = np.zeros(N)
    y0[0] = ctot
    sol = solve_ivp(rhs, (0, tmax), y0, args=(g,), method="LSODA", rtol=1e-6, atol=1e-12,
                    t_eval=np.clip(np.logspace(-2, np.log10(tmax), 160), 0, tmax))
    return sol.t, N * sol.y[-1] / ctot


ax = axs[1]
for c, tok in [(0.3, "dna"), (2.0, "bacterium"), (8.0, "blood")]:
    t, f = run(c, 4.0, 2e3)
    ax.plot(t, f, color=charts.line(tok), lw=1.8, label=fr"$c_{{\mathrm{{tot}}}} = {c:g}$")
ax.set_xscale("log")
ax.set_ylim(0, 1.02)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"time $t\,k_{\mathrm{on}}$", "fraction in complete capsids")
charts.title(ax, "B  Capsid assembly kinetics")

ax = axs[2]
cs = np.logspace(-1, 1.5, 14)
for g, tok in [(3.0, "dna"), (4.0, "bacterium"), (6.0, "blood")]:
    y = [run(c, g, 300.0)[1][-1] for c in cs]
    ax.plot(cs, y, "o-", ms=3, color=charts.line(tok), lw=1.5, label=fr"$\Delta g = {g:g}\,k_{{\mathrm{{B}}}}T$")
ax.set_xscale("log")
ax.set_ylim(0, 1.02)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, r"total concentration $c_{\mathrm{tot}}$", r"yield at $t = 300$")
charts.title(ax, "C  Kinetic trapping")
