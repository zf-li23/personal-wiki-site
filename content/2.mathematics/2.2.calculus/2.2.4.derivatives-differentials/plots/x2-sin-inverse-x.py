import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-0.25, 0.25, 20001)
x = x[x != 0]
f = x**2 * np.sin(1 / x)
fp = 2 * x * np.sin(1 / x) - np.cos(1 / x)

fig, axes = plt.subplots(1, 2, figsize=(11, 4.3))

ax = axes[0]
ax.plot(x, f, color="C0", lw=1)
ax.plot(x, x**2, color="gray", lw=0.8, ls="--", label=r"$\pm x^2$")
ax.plot(x, -x**2, color="gray", lw=0.8, ls="--")
ax.axhline(0, color="C3", lw=1.2, label=r"tangent at $0$: $y = 0$")
ax.set_title(r"$f(x) = x^2 \sin(1/x)$, $f(0) = 0$: differentiable, $f'(0) = 0$")
ax.set_xlabel(r"$x$")
ax.legend(loc="upper center", fontsize=9)
ax.grid(True, alpha=0.3)

ax = axes[1]
ax.plot(x, fp, color="C1", lw=0.6)
ax.plot([0], [0], "o", color="C3", ms=6, label=r"$f'(0) = 0$")
ax.set_title(r"$f'(x) = 2x\sin(1/x) - \cos(1/x)$ has no limit at $0$")
ax.set_xlabel(r"$x$")
ax.set_ylim(-1.6, 1.6)
ax.legend(loc="upper right", fontsize=9)
ax.grid(True, alpha=0.3)
fig.tight_layout()
