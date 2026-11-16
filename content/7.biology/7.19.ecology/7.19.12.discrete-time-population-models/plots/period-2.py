"""The 2-cycle of the logistic map f(x) = mu x (1 - x) (Section 12.3.1).

A-C: f (thin) and the second iterate f(f(x)) (thick) with the diagonal at mu = 2.8, 3.2 and 3.5;
open circles: fixed points of f; filled: the 2-cycle points p, q (roots of mu^2 x^2 - mu(mu + 1) x
+ (mu + 1) = 0), which exist for mu > 3. The slope of f(f(x)) at p and q is the multiplier
f'(p) f'(q) = -mu^2 + 2 mu + 4.
D: multipliers against mu: of the fixed point x* = 1 - 1/mu, 2 - mu (stable for 1 < mu < 3), and of the
2-cycle (stable for 3 < mu < 1 + sqrt 6); the shaded band is |multiplier| < 1.
"""

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
fig, axes = plt.subplots(1, 4, figsize=(14.0, 3.8))
x = np.linspace(0, 1, 400)
for ax, mu in zip(axes[:3], (2.8, 3.2, 3.5)):
    f = lambda v: mu * v * (1 - v)
    ax.plot(x, f(x), color=C.line("dna"), lw=1, alpha=0.6, label="f(x)")
    ax.plot(x, f(f(x)), color=C.line("dna"), lw=2, label="f(f(x))")
    ax.plot(x, x, color=P.muted(), lw=0.8)
    xs = 1 - 1 / mu
    ax.plot([0, xs], [0, xs], "o", ms=6, mfc=P.surface(), mec=P.ink(), ls="none")
    if mu > 3:
        disc = np.sqrt((mu + 1) * (mu - 3))
        p, q = (mu + 1 - disc) / (2 * mu), (mu + 1 + disc) / (2 * mu)
        ax.plot([p, q], [p, q], "o", ms=6, color=C.line("rna"))
        m = -mu ** 2 + 2 * mu + 4
        ax.text(0.03, 0.9, f"slope at p, q: {m:.2f}\n{'stable' if abs(m) < 1 else 'unstable'} 2-cycle",
                fontsize=FS["tiny"], color=C.line("rna"))
    ax.text(0.03, 0.78 if mu > 3 else 0.9, f"slope at x*: {(2 - mu) ** 2:.2f}", fontsize=FS["tiny"], color=P.ink())
    ax.set_aspect("equal")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    C.style_axes(ax, "x", "f(f(x))" if mu == 2.8 else None)
    C.title(ax, f"{'ABC'[[2.8, 3.2, 3.5].index(mu)]}  μ = {mu:g}")
axes[0].legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower right")
ax = axes[3]
mu = np.linspace(1, 3.7, 400)
ax.axhspan(-1, 1, color=P.fill("positive"), alpha=0.25, lw=0)
ax.plot(mu, 2 - mu, color=P.ink(), lw=1.8, label="fixed point: 2 − μ")
m2 = np.linspace(3, 3.7, 200)
ax.plot(m2, -m2 ** 2 + 2 * m2 + 4, color=C.line("rna"), lw=1.8, label="2-cycle: −μ² + 2μ + 4")
for v, txt in ((3, "3"), (1 + np.sqrt(6), "1 + √6")):
    ax.axvline(v, color=P.muted(), lw=0.6, ls=(0, (3, 2)))
    ax.text(v + 0.02, -2.3, txt, fontsize=FS["tiny"], color=P.muted())
ax.set_ylim(-2.5, 1.5)
C.style_axes(ax, "μ", "multiplier")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left")
C.title(ax, "D  Multipliers")
fig.tight_layout()
