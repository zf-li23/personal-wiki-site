"""T-x-y diagrams at 101.325 kPa of two strongly non-ideal mixtures, computed from modified
Raoult's law p_i = x_i gamma_i p_i* with Antoine vapor pressures. Left: ethanol + water with
van Laar activity coefficients (A12 = 1.6798, A21 = 0.9227): minimum-boiling azeotrope.
Right: acetone + chloroform with a one-parameter Margules model (A = -0.70): maximum-boiling
azeotrope."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

MMHG = 0.133322368
P = 101.325


def antoine(A, B, C):
    return lambda T: 10 ** (A - B / (C + T - 273.15)) * MMHG


def txy(p1, p2, gam, x):
    T, y = [], []
    for x1 in x:
        g1, g2 = gam(x1)
        Tb = brentq(lambda T: x1 * g1 * p1(T) + (1 - x1) * g2 * p2(T) - P, 300, 400)
        T.append(Tb)
        y.append(x1 * g1 * p1(Tb) / P)
    return np.array(T) - 273.15, np.array(y)


def van_laar(A12, A21):
    def g(x1):
        x2 = 1 - x1
        d = A12 * x1 + A21 * x2
        return np.exp(A12 * (A21 * x2 / d) ** 2), np.exp(A21 * (A12 * x1 / d) ** 2)
    return g


def margules(A):
    return lambda x1: (np.exp(A * (1 - x1) ** 2), np.exp(A * x1 ** 2))


x = np.linspace(0, 1, 401)
fig, axes = plt.subplots(1, 2, figsize=(8.8, 3.9))
cases = [
    (axes[0], antoine(8.20417, 1642.89, 230.300), antoine(8.07131, 1730.63, 233.426),
     van_laar(1.6798, 0.9227), "ethanol", "water", (76, 101)),
    (axes[1], antoine(7.11714, 1210.595, 229.664), antoine(6.95465, 1170.966, 226.232),
     margules(-0.70), "acetone", "chloroform", (54, 66)),
]
for ax, p1, p2, gam, n1, n2, ylim in cases:
    t, y = txy(p1, p2, gam, x)
    ax.plot(x, t, color="C0", lw=1.8, label="liquid (bubble) line")
    ax.plot(y, t, color="C3", lw=1.8, label="vapor (dew) line")
    i = np.argmin(np.abs(y - x)[5:-5]) + 5
    ax.plot([x[i]], [t[i]], "o", color="C2", ms=5)
    ax.annotate(f"azeotrope\n{x[i]:.2f}, {t[i]:.1f} C".replace(" C", r" $^\circ$C"), (x[i], t[i]),
                xytext=(0.35, ylim[0] + 0.15 * (ylim[1] - ylim[0])) if n1 == "ethanol" else (0.1, 56.0),
                fontsize=8, arrowprops=dict(arrowstyle="-", color="0.5", lw=0.8))
    ax.set_xlim(0, 1)
    ax.set_ylim(*ylim)
    ax.set_xlabel(rf"$x$ or $y$ ({n1}); 0 = pure {n2}")
    ax.set_ylabel(r"$t\,/\,^\circ\mathrm{C}$")
axes[0].set_title("minimum-boiling azeotrope", fontsize=10)
axes[1].set_title("maximum-boiling azeotrope", fontsize=10)
axes[0].legend(frameon=False, fontsize=8, loc="upper right")
fig.tight_layout()
