"""Fitting the Michaelis-Menten model v = Vmax S / (Km + S) to simulated
enzyme-kinetics data with scipy.optimize.curve_fit (5% multiplicative noise)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def michaelis_menten(S, Vmax, Km):
    return Vmax * S / (Km + S)


rng = np.random.default_rng(0)
S = np.array([0.5, 1, 2, 4, 8, 16, 32, 64])
v = michaelis_menten(S, 10.0, 4.0) * (1 + 0.05 * rng.standard_normal(S.size))
(Vmax, Km), cov = curve_fit(michaelis_menten, S, v, p0=[5, 1])
se = np.sqrt(np.diag(cov))

SS = np.linspace(0, 70, 400)
fig, ax = plt.subplots(figsize=(7, 4.5))
ax.plot(S, v, "ko", label="data")
ax.plot(SS, michaelis_menten(SS, Vmax, Km), color="C0",
        label=f"fit: Vmax = {Vmax:.2f} ({se[0]:.2f}), Km = {Km:.2f} ({se[1]:.2f})")
ax.plot(SS, michaelis_menten(SS, 10.0, 4.0), color="C7", ls="--", label="true: Vmax = 10, Km = 4")
ax.axhline(Vmax, color="C0", lw=0.8, ls=":")
ax.set_xlabel("substrate concentration S")
ax.set_ylabel("reaction rate v")
ax.set_title("Michaelis-Menten fit (standard errors in parentheses)")
ax.legend(loc="lower right", fontsize=8)
ax.grid(alpha=0.3)
fig.tight_layout()
