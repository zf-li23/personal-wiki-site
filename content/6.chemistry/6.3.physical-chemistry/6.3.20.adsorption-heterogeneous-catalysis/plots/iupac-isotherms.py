"""Schematic of the six types of physisorption isotherms in the IUPAC 2015 classification
(Thommes et al., Pure Appl. Chem. 87, 1051): amount adsorbed against relative pressure p/p*.
Type I(a)/I(b): micropores; II: nonporous or macroporous, unrestricted multilayer (point B marks
monolayer completion); III: weak adsorbent-adsorbate interaction; IV(a) with hysteresis and IV(b)
reversible: mesopores with capillary condensation; V: weak interaction plus pores; VI: layer-by-layer
adsorption on a uniform nonporous surface."""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.0005, 0.995, 600)


def bet(x, c, n=None):
    if n is None:
        return c * x / ((1 - x) * (1 + (c - 1) * x))
    num = c * x * (1 - (n + 1) * x**n + n * x ** (n + 1))
    den = (1 - x) * (1 + (c - 1) * x - c * x ** (n + 1))
    return num / den


def step(x, x0, w):
    return 0.5 * (1 + np.tanh((x - x0) / w))


fig, axes = plt.subplots(2, 3, figsize=(8.6, 5.4))
ax = axes[0, 0]
ax.plot(x, 1 - np.exp(-x / 0.01), color="C0", lw=1.8, label="I(a)")
ax.plot(x, 0.95 * (1 - np.exp(-x / 0.06)), color="C1", lw=1.8, label="I(b)")
ax.legend(frameon=False, fontsize=8, loc="lower right")
ax.set_title("Type I", fontsize=9)

ax = axes[0, 1]
y = bet(x, 100)
ax.plot(x, y, color="C0", lw=1.8)
xb = 1 / (1 + np.sqrt(100))
ax.plot(xb, bet(xb, 100), "o", color="C3", ms=4)
ax.text(xb + 0.04, bet(xb, 100), "B", fontsize=9, va="center")
ax.set_ylim(0, 6)
ax.set_title("Type II", fontsize=9)

ax = axes[0, 2]
ax.plot(x, bet(x, 0.3), color="C0", lw=1.8)
ax.set_ylim(0, 6)
ax.set_title("Type III", fontsize=9)

ax = axes[1, 0]
base = bet(np.minimum(x, 0.9), 100, n=3)
ads = base + 3.0 * step(x, 0.72, 0.025)
des = base + 3.0 * step(x, 0.58, 0.02)
ax.plot(x, ads, color="C0", lw=1.8, label="IV(a)")
ax.plot(x, des, color="C0", lw=1.2, ls="--")
ax.plot(x, bet(np.minimum(x, 0.9), 100, n=2) + 1.5 * step(x, 0.35, 0.03) - 0.8, color="C1", lw=1.8, label="IV(b)")
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.set_title("Type IV", fontsize=9)

ax = axes[1, 1]
b5 = bet(np.minimum(x, 0.9), 0.3, n=3)
ax.plot(x, b5 + 3.0 * step(x, 0.70, 0.03), color="C0", lw=1.8)
ax.plot(x, b5 + 3.0 * step(x, 0.56, 0.02), color="C0", lw=1.2, ls="--")
ax.set_title("Type V", fontsize=9)

ax = axes[1, 2]
y6 = sum(step(x, x0, 0.012) for x0 in [0.15, 0.35, 0.55, 0.75])
ax.plot(x, y6, color="C0", lw=1.8)
ax.set_title("Type VI", fontsize=9)

for a in axes.flat:
    a.set_xlim(0, 1)
    a.set_xticks([0, 0.5, 1])
    a.set_yticks([])
for a in axes[1]:
    a.set_xlabel(r"$p/p^*$")
for a in axes[:, 0]:
    a.set_ylabel("amount adsorbed")
fig.tight_layout()
