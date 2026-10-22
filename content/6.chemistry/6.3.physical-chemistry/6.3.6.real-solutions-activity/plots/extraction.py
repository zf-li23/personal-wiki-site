"""Fraction of solute left in the aqueous phase after extracting V = 100 mL of solution with a total
of V_e = 30 mL of organic solvent split into n equal portions. Distribution coefficient
K = c(organic)/c(water) = 4 (hypothetical). Remaining fraction (1 + K V_e/(n V))^(-n) -> exp(-K V_e/V)."""

import numpy as np
import matplotlib.pyplot as plt

K, V, Ve = 4.0, 100.0, 30.0
n = np.arange(1, 13)
frac = (1 + K * Ve / (n * V)) ** (-n)
lim = np.exp(-K * Ve / V)

fig, ax = plt.subplots(figsize=(6.2, 3.8))
ax.plot(n, frac * 100, "o-", color="C0", lw=1.5, ms=5, label=r"$n$ portions of $V_\mathrm{e}/n$")
ax.axhline(lim * 100, color="C3", lw=1.0, ls="--", label=rf"limit $n\to\infty$: {lim * 100:.1f} %")
ax.set_xlabel("number of extractions $n$")
ax.set_ylabel("solute left in water / %")
ax.set_xticks(n)
ax.set_ylim(25, 50)
ax.legend(frameon=False, fontsize=9)
fig.tight_layout()
