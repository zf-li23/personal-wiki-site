"""EDTA titration curves pM' versus fraction titrated (exact mass balances with dilution):
left, 20.00 mL of 0.020 mol/L M titrated with 0.020 mol/L EDTA for lg K' = 4 ... 12;
right, lg K' = 10 at different concentrations (titrant and analyte equal)."""

import numpy as np
import matplotlib.pyplot as plt


def pM(f, c, lgK):
    K = 10.0 ** lgK
    cM = c / (1 + f)          # total metal after dilution (equal concentrations)
    cY = c * f / (1 + f)      # total EDTA after dilution
    # free metal m: K m (cY - cM + m) = cM - m
    a, b, cc = K, 1 + K * (cY - cM), -cM
    m = (-b + np.sqrt(b * b - 4 * a * cc)) / (2 * a)
    return -np.log10(m)


f = np.linspace(0, 2, 2001)
fig, axes = plt.subplots(1, 2, figsize=(11, 4), sharey=True)
for i, lgK in enumerate([4, 6, 8, 10, 12]):
    axes[0].plot(f * 100, pM(f, 0.020, lgK), color=f"C{i}", lw=1.6, label=f"lg $K'$ = {lgK}")
axes[0].set_title("c = 0.020 mol L$^{-1}$", fontsize=10)
for i, c in enumerate([1e-1, 1e-2, 1e-3, 1e-4]):
    axes[1].plot(f * 100, pM(f, c, 10), color=f"C{i}", lw=1.6, label=f"c = 10$^{{{int(np.log10(c))}}}$ mol L$^{{-1}}$")
axes[1].set_title("lg $K'$ = 10", fontsize=10)
for ax in axes:
    ax.set_xlabel("fraction titrated / %")
    ax.axvline(100, color="0.6", lw=0.8, ls=":")
    ax.legend(frameon=False, fontsize=8, loc="upper left")
    ax.set_xlim(0, 200)
axes[0].set_ylabel("pM$'$")
fig.tight_layout()
