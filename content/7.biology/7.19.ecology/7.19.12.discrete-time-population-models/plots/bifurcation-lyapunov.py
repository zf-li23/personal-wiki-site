"""Bifurcation diagrams and Lyapunov exponents (Sections 12.3.2, 12.4).

Left: discrete logistic x_{t+1} = x_t [1 + r (1 - x_t)]; right: Ricker x_{t+1} = x_t exp[r (1 - x_t)]
(x = N/K). For each of 2000 values of r, 600 transient iterations from x0 = 0.3 are discarded and the
next 200 plotted (top). Bottom: Lyapunov exponent lambda = mean of ln |F'(x_t)| over 3000 iterations
after the transient; logistic F'(x) = 1 + r - 2 r x, Ricker F'(x) = (1 - r x) exp[r (1 - x)].
"""

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT

models = [
    ("Discrete logistic", np.linspace(1.8, 3.0, 2000), lambda r, x: x * (1 + r * (1 - x)),
     lambda r, x: 1 + r - 2 * r * x, [2.0, 2.449, 2.5441], 2.5699),
    ("Ricker", np.linspace(1.8, 3.4, 2000), lambda r, x: x * np.exp(r * (1 - x)),
     lambda r, x: (1 - r * x) * np.exp(r * (1 - x)), [2.0, 2.5265, 2.6562], 2.6924),
]
fig, axes = plt.subplots(2, 2, figsize=(12.0, 6.4), sharex="col", gridspec_kw=dict(height_ratios=[1.6, 1]))
for k, (name, rr, F, dF, bifs, rinf) in enumerate(models):
    x = np.full_like(rr, 0.3)
    for _ in range(600):
        x = F(rr, x)
    R, X = [], []
    for _ in range(200):
        x = F(rr, x)
        R.append(rr)
        X.append(x)
    ax = axes[0, k]
    ax.plot(np.concatenate(R), np.concatenate(X), ",", color=P.ink(), alpha=0.25, rasterized=True)
    for b in bifs:
        ax.axvline(b, color=C.line("rna"), lw=0.6, ls=(0, (3, 2)))
    ax.axvline(rinf, color=C.line("negative"), lw=0.8)
    ax.text(rinf + 0.01, ax.get_ylim()[1] * 0.97 if k else 1.32, f"r∞ = {rinf}", fontsize=FS["tiny"],
            color=C.line("negative"), va="top")
    C.style_axes(ax, None, "x = N / K (attractor)")
    C.title(ax, f"{'AB'[k]}  {name}")
    x = np.full_like(rr, 0.3)
    for _ in range(600):
        x = F(rr, x)
    s = np.zeros_like(rr)
    for _ in range(3000):
        s += np.log(np.abs(dF(rr, x)) + 1e-300)
        x = F(rr, x)
    lam = s / 3000
    ax = axes[1, k]
    ax.plot(rr, lam, color=C.line("dna"), lw=0.8)
    ax.fill_between(rr, 0, lam, where=lam > 0, color=P.fill("negative"), alpha=0.6, lw=0)
    ax.axhline(0, color=P.muted(), lw=0.7)
    ax.set_ylim(-1.6, 0.8)
    C.style_axes(ax, "r", "Lyapunov exponent λ")
    C.title(ax, f"{'CD'[k]}  Lyapunov exponent, {name} model")
fig.tight_layout()
