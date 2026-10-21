"""Photoelectric effect: current-voltage curves (schematic) and the linear stopping voltage versus frequency."""

import numpy as np
import matplotlib.pyplot as plt

h = 6.62607015e-34
e = 1.602176634e-19

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.0))

U = np.linspace(-3, 6, 900)


def current(U, Uc, im, scale=1.2):
    i = im * (1 - np.exp(-(U + Uc) / scale))
    return np.where(U > -Uc, i, 0.0)


ax1.plot(U, current(U, 1.5, 1.0), color="C0", lw=1.8, label="frequency ν1, intensity I")
ax1.plot(U, current(U, 1.5, 2.0), color="C0", lw=1.8, ls="--", label="frequency ν1, intensity 2I")
ax1.plot(U, current(U, 2.4, 1.4), color="C3", lw=1.8, label="frequency ν2 > ν1")
ax1.axhline(0, color="0.5", lw=0.8)
ax1.axvline(0, color="0.5", lw=0.8)
for Uc, col in [(1.5, "C0"), (2.4, "C3")]:
    ax1.plot([-Uc], [0], "o", color=col, ms=4)
ax1.text(-1.4, -0.22, "-U_c(ν1)", fontsize=8, ha="left", color="C0")
ax1.text(-2.5, -0.22, "-U_c(ν2)", fontsize=8, ha="right", color="C3")
ax1.text(4.2, 2.08, "saturation  i_m ∝ I", fontsize=8, color="0.4", ha="center")
ax1.set_xlim(-3, 6)
ax1.set_ylim(-0.35, 2.4)
ax1.set_xlabel("anode voltage  U / V")
ax1.set_ylabel("photocurrent  i  (arb. units)")
ax1.set_title("Current-voltage curves (schematic)")
ax1.legend(loc="center right", fontsize=8, frameon=False)

nu = np.linspace(0, 16e14, 400)
for i, (name, W) in enumerate([("W_0 = 2.3 eV", 2.3), ("W_0 = 4.3 eV", 4.3)]):
    nu0 = W * e / h
    nn = nu[nu >= nu0]
    ax2.plot(nn / 1e14, h * nn / e - W, color=f"C{i}", lw=1.8, label=name)
    ax2.plot(nu / 1e14, h * nu / e - W, color=f"C{i}", lw=0.8, ls=":")
    ax2.plot([nu0 / 1e14], [0], "o", color=f"C{i}", ms=4)
    ax2.annotate(f"ν0 = {nu0 / 1e14:.1f} × 10^14 Hz", xy=(nu0 / 1e14, 0), xytext=(nu0 / 1e14 + 0.4, -0.5), fontsize=8)
ax2.axhline(0, color="0.5", lw=0.8)
ax2.text(0.5, 2.9, "slope K = h / e = 4.14 × 10^-15 V s", fontsize=8, color="0.4")
ax2.set_xlim(0, 16)
ax2.set_ylim(-1.5, 3.2)
ax2.set_xlabel("frequency  ν / (10^14 Hz)")
ax2.set_ylabel("stopping voltage  U_c / V")
ax2.set_title("Einstein's equation  eU_c = hν - W_0")
ax2.legend(loc="upper left", fontsize=8, frameon=False, bbox_to_anchor=(0.0, 0.88))

fig.tight_layout()
