import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return (x - 1) ** 3 / (x + 1) ** 2


fig, ax = plt.subplots(figsize=(7.5, 5.5))
for lo, hi in [(-14, -1.06), (-0.94, 8)]:
    x = np.linspace(lo, hi, 1500)
    ax.plot(x, f(x), color="C0", lw=2, label=r"$y = (x - 1)^3 / (x + 1)^2$" if lo < -2 else None)

x = np.linspace(-14, 8, 10)
ax.plot(x, x - 5, color="C2", lw=1.2, ls="--", label=r"oblique asymptote $y = x - 5$")
ax.axvline(-1, color="C1", lw=1.2, ls="--", label=r"vertical asymptote $x = -1$")
ax.axhline(0, color="gray", lw=0.6)
ax.axvline(0, color="gray", lw=0.6)

ax.plot([-5], [f(-5)], "o", color="C3", ms=7)
ax.annotate(r"local max $(-5, -13.5)$", xy=(-5, f(-5)), xytext=(-12.5, -5),
            arrowprops=dict(arrowstyle="->", lw=0.8))
ax.plot([1], [0], "o", color="C4", ms=7)
ax.annotate("inflection point $(1, 0)$\n" r"$f'(1) = 0$, not an extremum", xy=(1, 0), xytext=(2.0, -9),
            arrowprops=dict(arrowstyle="->", lw=0.8))
ax.text(-11, -21, "concave", fontsize=10)
ax.text(4.2, 1.6, "convex", fontsize=10)

ax.set_xlim(-14, 8)
ax.set_ylim(-26, 8)
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")
ax.set_title(r"Graph of $f(x) = (x - 1)^3 / (x + 1)^2$")
ax.legend(loc="upper left", fontsize=9)
ax.grid(True, alpha=0.3)
fig.tight_layout()
