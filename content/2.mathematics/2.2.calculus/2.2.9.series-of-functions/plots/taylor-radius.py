"""Taylor partial sums of 1/(1+x^2): good inside |x| < 1, divergent outside,
although the function is smooth on the whole real line (poles at x = +-i)."""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1.6, 1.6, 800)
fig, ax = plt.subplots(figsize=(7.5, 4.4))
ax.axvspan(-1, 1, color="gray", alpha=0.12, label=r"$|x| < R = 1$")
ax.plot(x, 1 / (1 + x**2), color="black", linewidth=2.2, label=r"$1/(1+x^2)$")
for k, n in enumerate([2, 3, 10, 11]):
    s = sum((-1) ** j * x ** (2 * j) for j in range(n + 1))
    ax.plot(x, s, color=f"C{k}", linewidth=1.2, label=rf"$\sum_{{k=0}}^{{{n}}} (-1)^k x^{{2k}}$")
ax.set_ylim(-2.0, 2.5)
ax.set_xlabel(r"$x$")
ax.set_title(r"Taylor partial sums of $1/(1+x^2)$ diverge for $|x| > 1$", fontsize=10)
ax.legend(fontsize=8, loc="lower center", ncol=3)
ax.grid(True, alpha=0.3)
fig.tight_layout()
