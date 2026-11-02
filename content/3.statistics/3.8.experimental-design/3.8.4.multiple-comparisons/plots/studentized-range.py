"""Densities of the studentized range distribution with 16 degrees of freedom for k = 2, 3, 4, 6."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

nu = 16
q = np.linspace(0.0, 7, 400)
fig, ax = plt.subplots(figsize=(8, 4.2))
for i, k in enumerate([2, 3, 4, 6]):
    dens = stats.studentized_range.pdf(q, k, nu)
    crit = stats.studentized_range.ppf(0.95, k, nu)
    ax.plot(q, dens, color=f"C{i}", lw=2, label=f"k = {k}, q(0.05) = {crit:.2f}")
    ax.axvline(crit, color=f"C{i}", ls=":", lw=1)
ax.set_xlabel("q")
ax.set_ylabel("density")
ax.set_title("Studentized range distribution, nu = 16")
ax.set_ylim(0, None)
ax.legend(frameon=False)
ax.grid(alpha=0.3)
fig.tight_layout()
