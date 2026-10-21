"""Infinite square well: eigenfunctions at their energy levels, and large-n probability density."""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-0.5, 0.5, 1000)  # in units of the well width a


def phi(n, x):
    # normalized eigenfunctions on |x| < a/2 (a = 1)
    return np.sqrt(2) * (np.cos(n * np.pi * x) if n % 2 else np.sin(n * np.pi * x))


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.6))

scale = 1.6
for n in range(1, 5):
    E = n**2
    ax1.axhline(E, color="0.6", lw=0.6, ls=":")
    ax1.plot(x, E + scale * phi(n, x), color=f"C{n - 1}", lw=1.6)
    ax1.text(0.56, E, f"n = {n}", va="center", fontsize=9)
for xw in [-0.5, 0.5]:
    ax1.plot([xw, xw], [0, 19], color="0.3", lw=2.5)
ax1.plot([-0.5, 0.5], [0, 0], color="0.3", lw=1)
ax1.set_xlim(-0.65, 0.72)
ax1.set_ylim(-0.5, 19)
ax1.set_xlabel("x / a")
ax1.set_ylabel(r"$E\,/\,E_1$")
ax1.set_title(r"Eigenfunctions $\Phi_n$ drawn at $E_n = n^2 E_1$")

for n, c in [(1, "C0"), (2, "C1"), (20, "C2")]:
    ax2.plot(x, phi(n, x) ** 2, color=c, lw=1.3 if n == 20 else 1.8, label=f"n = {n}")
ax2.plot(x, np.ones_like(x), "k--", lw=1.2, label="classical")
ax2.set_xlim(-0.5, 0.5)
ax2.set_ylim(0, 2.2)
ax2.set_xlabel("x / a")
ax2.set_ylabel(r"$a\,|\Phi_n|^2$")
ax2.set_title("Probability density")
ax2.legend(fontsize=8, loc="upper right", ncol=2)

fig.tight_layout()
