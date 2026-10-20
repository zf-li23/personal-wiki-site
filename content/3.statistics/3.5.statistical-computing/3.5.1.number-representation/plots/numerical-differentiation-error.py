"""Total error of forward and central difference approximations to f'(1) for f = exp, as a function of the step h."""

import numpy as np
import matplotlib.pyplot as plt

x0 = 1.0
exact = np.exp(x0)
h = np.logspace(-16, 0, 161)
forward = (np.exp(x0 + h) - np.exp(x0)) / h
central = (np.exp(x0 + h) - np.exp(x0 - h)) / (2 * h)
err_f = np.maximum(np.abs(forward - exact), 1e-17)
err_c = np.maximum(np.abs(central - exact), 1e-17)

u = 2.0**-53
fig, ax = plt.subplots(figsize=(7.5, 4.8))
ax.loglog(h, err_f, "o", ms=3, color="C0", label="forward difference")
ax.loglog(h, err_c, "s", ms=3, color="C1", label="central difference")
ax.loglog(h, exact * h / 2, color="C0", lw=1, ls="--", label="truncation h f''/2")
ax.loglog(h, exact * h**2 / 6, color="C1", lw=1, ls="--", label="truncation h^2 f'''/6")
ax.loglog(h, 2 * u * exact / h, color="0.5", lw=1, ls=":", label="rounding 2u f/h")
for hs, c in [(np.sqrt(4 * u), "C0"), ((3 * u) ** (1 / 3), "C1")]:
    ax.axvline(hs, color=c, lw=0.8, alpha=0.6)
ax.set_ylim(1e-12, 10)
ax.set_xlabel("step h")
ax.set_ylabel("absolute error")
ax.set_title("f(x) = exp(x) at x0 = 1: optimal h near 1e-8 (forward) and 1e-5 (central)", fontsize=10)
ax.legend(fontsize=8, loc="upper center", ncol=2)
ax.grid(alpha=0.3, which="both")
fig.tight_layout()
