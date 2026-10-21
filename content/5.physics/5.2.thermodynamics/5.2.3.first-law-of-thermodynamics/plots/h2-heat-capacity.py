"""Molar heat capacity C_V,m/R of a diatomic gas with H2-like constants: rigid rotor plus harmonic oscillator."""

import numpy as np
import matplotlib.pyplot as plt

theta_rot = 85.0  # K, rotational temperature of H2
theta_vib = 6330.0  # K, vibrational temperature of H2

T = np.logspace(np.log10(10), np.log10(2e4), 600)


def c_rot(T):
    # heat capacity of a rigid rotor from the energy fluctuation of its levels
    J = np.arange(0, 80)[:, None]
    x = J * (J + 1) * theta_rot / T[None, :]
    w = (2 * J + 1) * np.exp(-x)
    Z = w.sum(axis=0)
    m1 = (w * x).sum(axis=0) / Z
    m2 = (w * x**2).sum(axis=0) / Z
    return m2 - m1**2


def c_vib(T):
    y = theta_vib / T
    return y**2 * np.exp(-y) / (-np.expm1(-y)) ** 2


c = 1.5 + c_rot(T) + c_vib(T)

fig, ax = plt.subplots(figsize=(6.8, 4))
ax.semilogx(T, c, color="C0", lw=1.8)
for level, text in [(1.5, "translation only: 3/2"), (2.5, "+ rotation: 5/2"), (3.5, "+ vibration: 7/2")]:
    ax.axhline(level, color="0.5", lw=0.8, ls=":")
    ax.annotate(text, (12, level + 0.06), fontsize=9)
ax.axvline(theta_rot, color="C1", lw=0.9, ls="--")
ax.axvline(theta_vib, color="C2", lw=0.9, ls="--")
ax.annotate(r"$\Theta_{\mathrm{rot}}$", (theta_rot * 1.1, 1.2), color="C1", fontsize=10)
ax.annotate(r"$\Theta_{\mathrm{vib}}$", (theta_vib * 1.1, 1.2), color="C2", fontsize=10)
ax.set_xlim(10, 2e4)
ax.set_ylim(1, 4)
ax.set_xlabel(r"$T$ / K")
ax.set_ylabel(r"$C_{V,\mathrm{m}}/R$")
ax.set_title("Freezing of rotational and vibrational degrees of freedom")
fig.tight_layout()
