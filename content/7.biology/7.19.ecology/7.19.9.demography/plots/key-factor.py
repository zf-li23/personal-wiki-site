"""Key factor analysis of a simulated univoltine insect (Section 9.5).

Each generation: eggs E_t = F * A_t (F = 150 eggs per adult, sex ratio included).
k1 egg and early-larval loss (weather): Normal(0.9, 0.25), density independent and highly variable.
k2 parasitism of larvae: Normal(0.35, 0.04), density independent and nearly constant.
k3 pupal predation: k3 = 0.3 * (log10 N - 1.0) if positive (density dependent, N = pupae entering).
k4 adult mortality before reproduction: Normal(0.15, 0.05).
K = k1 + k2 + k3 + k4; A_{t+1} = E_t * 10^-K. 40 generations after a burn-in of 20.
B: regression coefficients of each k_i on K (Podoler & Rogers 1975); they sum to 1.
C: k3 and k1 against log10 of the numbers entering the stage.
"""

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(4)

F = 150.0
A = 50.0
rows = []
for t in range(60):
    E = F * A
    k1 = max(rng.normal(0.9, 0.25), 0.0)
    n1 = E * 10 ** -k1
    k2 = max(rng.normal(0.35, 0.04), 0.0)
    n2 = n1 * 10 ** -k2
    k3 = max(0.3 * (np.log10(n2) - 1.0), 0.0)
    n3 = n2 * 10 ** -k3
    k4 = max(rng.normal(0.15, 0.05), 0.0)
    A = n3 * 10 ** -k4
    rows.append((np.log10(E), np.log10(n2), k1, k2, k3, k4))
d = np.array(rows[20:])
logE, logN3, k = d[:, 0], d[:, 1], d[:, 2:]
K = k.sum(axis=1)
gen = np.arange(1, len(K) + 1)
cols = [C.line("rna"), C.line("dna"), C.line("positive"), C.line("neutral")]
names = ["k₁ eggs, early larvae", "k₂ parasitism", "k₃ pupal predation", "k₄ adults"]

fig, axes = plt.subplots(1, 3, figsize=(12.5, 3.9), gridspec_kw=dict(width_ratios=[1.6, 0.8, 1.0]))
ax = axes[0]
ax.plot(gen, K + 0.6, color=P.ink(), lw=2, label="K (shifted up 0.6)")
for i in range(4):
    ax.plot(gen, k[:, i], color=cols[i], lw=1.4, label=names[i])
C.style_axes(ax, "generation", "k value")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left", ncol=3)
ax.set_ylim(-0.05, 3.6)
C.title(ax, "A  Varley–Gradwell plot")

ax = axes[1]
b = np.array([np.cov(k[:, i], K)[0, 1] / np.var(K, ddof=1) for i in range(4)])
ax.bar(range(4), b, color=[P.fill(t) for t in ("rna", "dna", "positive", "neutral")],
       edgecolor=cols, lw=0.8)
for i, v in enumerate(b):
    ax.text(i, v + 0.02 if v >= 0 else v - 0.06, f"{v:.2f}", ha="center", fontsize=FS["tiny"], color=P.ink())
ax.axhline(0, color=P.muted(), lw=0.7)
ax.set_xticks(range(4), ["k₁", "k₂", "k₃", "k₄"])
C.style_axes(ax, None, "slope of kᵢ on K")
ax.text(2.5, 0.9 * max(b.max(), 1.0), f"sum = {b.sum():.2f}", ha="center", fontsize=FS["tiny"], color=P.muted())
ax.set_ylim(min(b.min() - 0.15, -0.1), max(b.max() + 0.15, 1.1))
C.title(ax, "B  Podoler–Rogers")

ax = axes[2]
ax.plot(logN3, k[:, 2], "o", ms=4, color=cols[2], label="k₃ vs log N (pupae)")
ax.plot(logE, k[:, 0], "^", ms=4, color=cols[0], label="k₁ vs log N (eggs)")
for xs, ys, col in ((logN3, k[:, 2], cols[2]), (logE, k[:, 0], cols[0])):
    s, c0 = np.polyfit(xs, ys, 1)
    xx = np.linspace(xs.min(), xs.max(), 10)
    ax.plot(xx, s * xx + c0, color=col, lw=1, ls=(0, (3, 2)))
    ax.text(xx[-1], s * xx[-1] + c0 + 0.05, f"slope {s:.2f}", fontsize=FS["tiny"], color=col, ha="right")
C.style_axes(ax, "log₁₀ N entering the stage", "k value")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
C.title(ax, "C  Which factor is density dependent?")

fig.tight_layout()
