"""Vapour pressures of a binary liquid mixture described by the one-parameter Margules model,
G^E_m = W x_A x_B, so ln gamma_A = (W/RT) x_B^2 and ln gamma_B = (W/RT) x_A^2 (Raoult convention).
p*_A = 40 kPa, p*_B = 60 kPa. Dashed: Raoult's law; dotted: Henry's-law tangents at infinite dilution."""

import numpy as np
import matplotlib.pyplot as plt

pA, pB = 40.0, 60.0
x = np.linspace(0, 1, 301)          # x_B
xa = 1 - x

fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharey=True)
for ax, w, title in [(axes[0], 1.2, "positive deviation, $W/RT$ = +1.2"), (axes[1], -1.2, "negative deviation, $W/RT$ = -1.2")]:
    gA = np.exp(w * x**2)
    gB = np.exp(w * xa**2)
    p_a, p_b = pA * xa * gA, pB * x * gB
    ax.plot(x, p_a, color="C0", lw=1.7, label=r"$p_\mathrm{A}$")
    ax.plot(x, p_b, color="C1", lw=1.7, label=r"$p_\mathrm{B}$")
    ax.plot(x, p_a + p_b, color="C2", lw=2.0, label=r"$p$")
    ax.plot(x, pA * xa, color="C0", lw=0.9, ls="--")
    ax.plot(x, pB * x, color="C1", lw=0.9, ls="--")
    ax.plot(x, pA * xa + pB * x, color="C2", lw=0.9, ls="--", label="Raoult")
    kB, kA = pB * np.exp(w), pA * np.exp(w)       # Henry constants k_x
    m = x < 0.45
    ax.plot(x[m], kB * x[m], color="C1", lw=1.0, ls=":", label=r"Henry, $k_{x,\mathrm{B}}x_\mathrm{B}$")
    m2 = x > 0.55
    ax.plot(x[m2], kA * (1 - x[m2]), color="C0", lw=1.0, ls=":")
    ax.set_title(title, fontsize=10)
    ax.set_xlabel(r"$x_\mathrm{B}$")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 110)
axes[0].set_ylabel(r"$p$ / kPa")
axes[0].legend(frameon=False, fontsize=8.5, loc="upper left")
fig.tight_layout()

