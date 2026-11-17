"""Adsorption-inhibition model of antifreeze proteins.

A: schematic of an ice front pinned by adsorbed AFP molecules spaced d apart: between them the front can only advance
by bulging; a bulge of radius r is in equilibrium at a supercooling dT = 2 gamma T_m / (rho_ice L_f r)
(Gibbs-Thomson), and the smallest radius it can have between two pinning points is d/2.
B: thermal hysteresis TH = 4 gamma T_m / (rho_ice L_f d) with d = (sigma_max theta)^(-1/2) and Langmuir coverage
theta = K c / (1 + K c). gamma = 0.03 J/m2, T_m = 273.15 K, rho_ice L_f = 917 * 3.34e5 J/m3.
Illustrative parameters: a fish AFP (saturating spacing 90 nm, K = 1 / 0.5 mM) and a hyperactive insect AFP
(saturating spacing 20 nm, K = 1 / 0.02 mM). Grey: colligative freezing-point depression of an ideal solute
(1.86 K kg/mol) at the same molar concentration.
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle

import wikibio as bio

P = bio.P
gamma, Tm, rhoL = 0.03, 273.15, 917 * 3.34e5
pref = 4 * gamma * Tm / rhoL  # K m

fig, (ax, bx) = plt.subplots(1, 2, figsize=(12.0, 4.6), gridspec_kw={"width_ratios": [1.0, 1.25]})
ax.set_xlim(-0.5, 6.5)
ax.set_ylim(-2.2, 3.0)
ax.set_aspect("equal")
ax.axis("off")
ax.fill_between([-0.5, 6.5], -2.2, 0, color=P.fill("dna"), alpha=0.35, lw=0)
xs = [0, 2, 4, 6]
for x0, x1 in zip(xs[:-1], xs[1:]):
    ax.add_patch(Arc(((x0 + x1) / 2, 0), x1 - x0, x1 - x0, theta1=0, theta2=180, color=P.edge("dna"), lw=2.0))
    ax.fill_between(np.linspace(x0, x1, 50), 0, np.sqrt(np.maximum(1 - (np.linspace(x0, x1, 50) - (x0 + x1) / 2) ** 2, 0)),
                    color=P.fill("dna"), alpha=0.35, lw=0)
for x in xs:
    ax.add_patch(Circle((x, 0), 0.22, fc=P.fill("protein"), ec=P.edge("protein"), lw=1.2, zorder=5))
ax.annotate("", xy=(2, -0.6), xytext=(4, -0.6), arrowprops=dict(arrowstyle="<->", color=P.ink(), lw=1.0))
ax.text(3, -0.95, "$d$", ha="center", fontsize=10, color=P.ink())
ax.plot([3, 3 + 0.707], [0, 0.707], color=P.ink(), lw=1.0)
ax.text(3.55, 0.25, "$r = d/2$", fontsize=9, color=P.ink())
ax.text(3, -1.7, "ice", ha="center", fontsize=10, color=P.edge("dna"))
ax.text(3, 2.4, "supercooled water", ha="center", fontsize=10, color=P.ink())
ax.text(0, -0.65, "AFP", ha="center", fontsize=8.5, color=P.edge("protein"))
ax.set_title("A  Ice front pinned between adsorbed AFPs", loc="left", fontsize=10)

c = np.logspace(-4, 1.3, 300)  # mM
for dsat, K, tok, lab in ((90e-9, 1 / 0.5, "plant", "fish AFP (illustrative)"),
                          (20e-9, 1 / 0.02, "highlight", "hyperactive insect AFP (illustrative)")):
    theta = K * c / (1 + K * c)
    th = pref * np.sqrt(theta) / dsat
    bx.plot(c, th, color=P.edge(tok), lw=2.2, label=lab)
bx.plot(c, 1.86 * c * 1e-3, color=P.muted(), lw=1.6, ls=":", label="colligative depression, same molarity")
bx.axhline(1.2, color=P.edge("negative"), lw=1.0, ls="--")
bx.text(1.2e-4, 1.3, "needed by an Antarctic fish (about 1.2 K)", fontsize=8, color=P.edge("negative"))
bx.set_xscale("log")
bx.set_xlim(1e-4, 20)
bx.set_ylim(0, 6)
bx.set_xlabel("AFP concentration / mM")
bx.set_ylabel("thermal hysteresis / K")
bx.legend(frameon=False, fontsize=8, loc="upper left", bbox_to_anchor=(0.0, 0.92))
bx.set_title("B  Hysteresis rises as the square root of coverage", loc="left", fontsize=10)
for s in ("top", "right"):
    bx.spines[s].set_visible(False)
fig.tight_layout()
