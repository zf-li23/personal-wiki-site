"""Growth of the common complexity classes: on a small scale the slow-growing
functions may even be larger, on a larger scale the order of growth decides."""

import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(1, 60, 600)
curves = [
    (r"$\log n$", np.log2(n)),
    (r"$\sqrt{n}$", np.sqrt(n)),
    (r"$n$", n),
    (r"$n \log n$", n * np.log2(n)),
    (r"$n^2$", n ** 2),
    (r"$n^3$", n ** 3),
    (r"$2^n$", 2.0 ** n),
]

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
for ax, top, title in zip(axes, (30, 2000), ("small scale", "larger scale")):
    for k, (label, y) in enumerate(curves):
        ax.plot(n, y, color=f"C{k}", lw=1.6, label=label)
    ax.set_ylim(0, top)
    ax.set_xlim(1, 60)
    ax.set_xlabel("input size n")
    ax.set_ylabel("cost T(n)")
    ax.set_title(title)
    ax.grid(alpha=0.3)
axes[1].legend(loc="upper left", fontsize=9)
fig.tight_layout()
