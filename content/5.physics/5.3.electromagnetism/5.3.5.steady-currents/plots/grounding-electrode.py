"""Spherical grounding electrode of radius a deep in soil of conductivity sigma.
The potential falls as phi(r) = phi_a * a / r, so 90 % of the voltage drop happens within r = 10 a."""

import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(1, 30, 600)  # in units of a
phi = 1 / r                  # in units of phi_a

fig, ax = plt.subplots(figsize=(6.8, 3.8))
ax.plot(r, phi, lw=2, label=r"$\varphi(r) / \varphi_a = a / r$")
ax.fill_between(r[r <= 10], phi[r <= 10], 0.1, color="C0", alpha=0.18, lw=0)
ax.axhline(0.1, color="0.5", lw=0.8, ls=":")
ax.axvline(10, color="0.5", lw=0.8, ls=":")
ax.annotate("90 % of the drop\nwithin r = 10 a", xy=(4, 0.3), xytext=(12, 0.55), fontsize=9,
            arrowprops=dict(arrowstyle="->", color="0.4"))
ax.set_xlabel(r"$r / a$")
ax.set_ylabel(r"$\varphi / \varphi_a$")
ax.set_xlim(0, 30)
ax.set_ylim(0, 1.05)
ax.legend(fontsize=9)
fig.tight_layout()
