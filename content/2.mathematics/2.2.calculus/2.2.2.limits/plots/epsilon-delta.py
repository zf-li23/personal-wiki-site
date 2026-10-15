"""The epsilon-delta definition of a limit at a point; the value f(x0) plays no role."""

import numpy as np
import matplotlib.pyplot as plt

x0, A = 1.0, 1.5
f = lambda x: 0.5 * x ** 2 + 1.0
eps = 0.35
# largest delta that works on both sides: f is increasing near x0
delta = min(x0 - np.sqrt(2 * (A - eps - 1.0)), np.sqrt(2 * (A + eps - 1.0)) - x0)

fig, ax = plt.subplots(figsize=(6.4, 4.6))
x = np.linspace(-0.2, 2.1, 400)
ax.plot(x, f(x), color="C0", lw=2, label="$y = f(x)$")
ax.axhspan(A - eps, A + eps, color="C1", alpha=0.15)
ax.axvspan(x0 - delta, x0 + delta, color="C2", alpha=0.15)
ax.plot([x0], [A], "o", ms=7, mfc="none", mec="C0", mew=1.5)
ax.plot([x0], [2.6], "o", ms=6, color="C0")
ax.annotate("$f(x_0)$ may be anything", (x0, 2.6), xytext=(12, 4), textcoords="offset points", fontsize=10)
for y, label in ((A - eps, "$A - \\varepsilon$"), (A, "$A$"), (A + eps, "$A + \\varepsilon$")):
    ax.axhline(y, color="C1", lw=0.8, ls="--" if y != A else "-")
    ax.text(-0.18, y + 0.03, label, color="C1", fontsize=10)
for xx, label in ((x0 - delta, "$x_0 - \\delta$"), (x0, "$x_0$"), (x0 + delta, "$x_0 + \\delta$")):
    ax.axvline(xx, color="C2", lw=0.8, ls="--" if xx != x0 else "-")
    ax.text(xx, 0.62, label, color="C2", fontsize=10, ha="center")
ax.set_xlim(-0.2, 2.1)
ax.set_ylim(0.55, 3.0)
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("$0 < |x - x_0| < \\delta \\Rightarrow |f(x) - A| < \\varepsilon$", fontsize=11)
ax.legend(loc="upper left", fontsize=9)
fig.tight_layout()
