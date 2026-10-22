"""Equilateral triangular (Gibbs) coordinates for a ternary system at fixed T and p.
Left: reading the composition of a point O. Right: a partially miscible three-liquid system
A (e.g. water) + C (extracting solvent) + B (solute), computed from a ternary regular
solution model with W_AC/RT = 3.0, W_AB/RT = 0.6, W_BC/RT = -0.4: binodal curve, tie lines
(sloping because B prefers the C-rich phase) and the plait point."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

PA, PB, PC = np.array([0.0, 0.0]), np.array([0.5, np.sqrt(3) / 2]), np.array([1.0, 0.0])


def xy(xa, xb, xc):
    return xa * PA[0] + xb * PB[0] + xc * PC[0], xa * PA[1] + xb * PB[1] + xc * PC[1]


def frame(ax):
    ax.plot([PA[0], PC[0], PB[0], PA[0]], [PA[1], PC[1], PB[1], PA[1]], color="0.2", lw=1.2)
    for f in np.arange(0.1, 1.0, 0.1):
        for a, b in [((f, 1 - f, 0), (f, 0, 1 - f)), ((1 - f, f, 0), (0, f, 1 - f)), ((1 - f, 0, f), (0, 1 - f, f))]:
            p, q = xy(*a), xy(*b)
            ax.plot([p[0], q[0]], [p[1], q[1]], color="0.85", lw=0.6, zorder=0)
    ax.text(-0.04, -0.04, "A", ha="right", fontsize=11)
    ax.text(1.04, -0.04, "C", fontsize=11)
    ax.text(0.5, np.sqrt(3) / 2 + 0.03, "B", ha="center", fontsize=11)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-0.12, 1.12)
    ax.set_ylim(-0.12, 0.98)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.8, 4.2))
frame(ax1)
xa, xb, xc = 0.2, 0.3, 0.5
O = xy(xa, xb, xc)
ax1.plot(*O, "o", color="C3", ms=6, zorder=5)
ax1.text(O[0] + 0.03, O[1] + 0.01, "O", fontsize=10, color="C3")
# lines through O parallel to the three sides, ending on the sides
for a, b, c in [((xa, 1 - xa, 0), (xa, 0, 1 - xa), "C0"), ((1 - xb, xb, 0), (0, xb, 1 - xb), "C2"),
                ((1 - xc, 0, xc), (0, 1 - xc, xc), "C1")]:
    p, q = xy(*a), xy(*b)
    ax1.plot([p[0], q[0]], [p[1], q[1]], color=c, lw=1.2, ls="--")
ax1.text(0.74, -0.08, r"$x_\mathrm{A} = 0.2$", color="C0", fontsize=9)
ax1.text(0.72, 0.30, r"$x_\mathrm{B} = 0.3$", color="C2", fontsize=9)
ax1.text(0.34, -0.08, r"$x_\mathrm{C} = 0.5$", color="C1", fontsize=9)
ax1.set_title("reading a composition", fontsize=10)

# ternary regular solution: tie lines by continuation from the A-C binary
W = {("A", "B"): 0.6, ("B", "C"): -0.4, ("A", "C"): 3.0}
names = "ABC"


def w(i, j):
    return 0.0 if i == j else W.get((i, j), W.get((j, i), 0.0))


def mu(x):
    gE = sum(w(names[i], names[j]) * x[i] * x[j] for i in range(3) for j in range(i + 1, 3))
    lng = np.array([sum(w(names[k], names[j]) * x[j] for j in range(3)) - gE for k in range(3)])
    return np.log(x) + lng


def eqs(v, xb1):
    xa1, xa2, xb2 = v
    return mu(np.array([xa1, xb1, 1 - xa1 - xb1])) - mu(np.array([xa2, xb2, 1 - xa2 - xb2]))


guess, ties = [0.929, 0.0707, 1e-4], []
for xb1 in np.linspace(1e-4, 0.36, 400):
    sol, info, ier, msg = fsolve(eqs, guess, args=(xb1,), full_output=True)
    if ier != 1 or abs(sol[0] - sol[1]) < 2e-3:
        break
    ties.append((sol[0], xb1, sol[1], sol[2]))
    guess = sol
ties = np.array(ties)
left = np.array([xy(a, b, 1 - a - b) for a, b in ties[:, :2]])
right = np.array([xy(a, b, 1 - a - b) for a, b in ties[:, 2:]])
curve = np.vstack([left, right[::-1]])

frame(ax2)
ax2.fill(curve[:, 0], curve[:, 1], color="C0", alpha=0.12, lw=0)
ax2.plot(curve[:, 0], curve[:, 1], color="C0", lw=1.8)
for k in np.linspace(0, len(ties) - 12, 7).astype(int):
    ax2.plot([left[k, 0], right[k, 0]], [left[k, 1], right[k, 1]], color="0.35", lw=0.9)
    ax2.plot([left[k, 0], right[k, 0]], [left[k, 1], right[k, 1]], "o", color="0.35", ms=2.5)
pp = 0.5 * (left[-1] + right[-1])
ax2.plot(*pp, "o", color="C3", ms=5)
ax2.annotate("plait point", pp, xytext=(pp[0] + 0.12, pp[1] + 0.12), fontsize=8,
             arrowprops=dict(arrowstyle="-", color="0.5", lw=0.8))
ax2.text(0.5, 0.55, "one liquid phase", ha="center", fontsize=8)
ax2.text(0.02, 0.1, "raffinate\n(A-rich)", fontsize=7.5)
ax2.text(0.88, 0.12, "extract\n(C-rich)", fontsize=7.5)
ax2.set_title("partially miscible A + C with solute B", fontsize=10)
fig.tight_layout()
