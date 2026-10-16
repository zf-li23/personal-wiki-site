"""Left: entries of exp(tJ) for a 3x3 Jordan block with eigenvalue -0.5.
Right: transient growth of the spectral norm of exp(tA) for non-normal A."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.4))

t = np.linspace(0, 16, 800)
lam = -0.5
ax1.plot(t, np.exp(lam * t), label=r"$\mathrm{e}^{-t/2}$")
ax1.plot(t, t * np.exp(lam * t), label=r"$t\,\mathrm{e}^{-t/2}$")
ax1.plot(t, t**2 / 2 * np.exp(lam * t), label=r"$\frac{t^2}{2}\mathrm{e}^{-t/2}$")
ax1.set_xlabel("t")
ax1.set_title(r"first row of $\mathrm{e}^{tJ}$, $J = J_{-0.5,3}$")
ax1.legend()
ax1.grid(alpha=0.3)

t = np.linspace(0, 6, 400)
for a in [0.0, 3.0, 10.0, 30.0]:
    A = np.array([[-1.0, a], [0.0, -2.0]])
    norms = [np.linalg.norm(expm(s * A), 2) for s in t]
    ax2.plot(t, norms, label=f"a = {a:g}")
ax2.plot(t, np.exp(-t), "k--", lw=1, label=r"$\mathrm{e}^{-t}$")
ax2.set_xlabel("t")
ax2.set_title(r"$\|\mathrm{e}^{tA}\|_2$ for $A = [[-1, a], [0, -2]]$")
ax2.legend()
ax2.grid(alpha=0.3)
fig.tight_layout()
