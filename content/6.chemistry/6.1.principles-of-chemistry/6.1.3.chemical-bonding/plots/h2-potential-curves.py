"""Potential energy of two H atoms versus internuclear distance: bound ground state, Heitler-London estimate, repulsive state."""

import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(45, 400, 800)  # internuclear distance / pm

def morse(r, De, re, a):
    x = np.exp(-a * (r - re))
    return De * (x * x - 2 * x)

# Ground state: experimental De = 458 kJ/mol, re = 74.1 pm (Morse fit, a = 0.0194 / pm).
ground = morse(r, 458, 74.1, 0.0194)
# Heitler-London (1927): De about 303 kJ/mol at re about 87 pm.
hl = morse(r, 303, 87, 0.0175)
# Repulsive state (parallel spins), Sato-type anti-Morse curve.
x = np.exp(-0.0194 * (r - 74.1))
repulsive = 0.5 * 458 * (x * x + 2 * x)

fig, ax = plt.subplots(figsize=(7, 4.4))
ax.plot(r, ground, color="C0", lw=1.8, label="ground state (antiparallel spins), experiment")
ax.plot(r, hl, color="C0", lw=1.3, ls="--", label="ground state, Heitler-London calculation")
ax.plot(r, repulsive, color="C3", lw=1.8, label="repulsive state (parallel spins)")
ax.axhline(0, color="0.5", lw=0.8)
ax.axvline(74.1, color="0.5", lw=0.8, ls=":")
ax.annotate("", xy=(74.1, -458), xytext=(74.1, 0), arrowprops=dict(arrowstyle="<->", color="0.4", lw=1))
ax.text(80, -250, r"$D_{\mathrm{e}} = 458\ \mathrm{kJ\,mol^{-1}}$", fontsize=10)
ax.text(76, 260, r"$r_{\mathrm{e}} = 74\ \mathrm{pm}$", fontsize=10)
ax.set_xlim(40, 400)
ax.set_ylim(-520, 450)
ax.set_xlabel(r"internuclear distance $r$ / pm")
ax.set_ylabel(r"$E$ / (kJ mol$^{-1}$)")
ax.set_title("Two hydrogen atoms approaching each other")
ax.legend(fontsize=9, loc="upper right")
fig.tight_layout()
