"""Floating-point operation counts of LU factorization, triangular solves and inversion."""

import numpy as np
import matplotlib.pyplot as plt


def lu_flops(n):
    # Doolittle elimination without pivoting: one division per multiplier,
    # one multiplication and one subtraction per updated entry
    return sum((n - k - 1) * (1 + 2 * (n - k - 1)) for k in range(n))


def triangular_solve_flops(n, unit_diagonal):
    # row i uses i multiplications and i subtractions (plus one division if not unit)
    return sum(2 * i + (0 if unit_diagonal else 1) for i in range(n))


def inverse_flops(n):
    # Gauss-Jordan on [A I]: for pivot k, scale row k and update n - 1 rows,
    # touching only the columns that can still be nonzero
    total = 0
    for k in range(n):
        width = n + k + 1 - k          # columns k..n-1 of A and 0..k of the identity part
        total += width                 # scale the pivot row
        total += (n - 1) * 2 * width   # eliminate in every other row
    return total


ns = np.arange(2, 301)
lu = np.array([lu_flops(n) for n in ns])
solve = np.array([triangular_solve_flops(n, True) + triangular_solve_flops(n, False) for n in ns])
inv = np.array([inverse_flops(n) for n in ns])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2))
ax1.loglog(ns, lu, label="LU factorization")
ax1.loglog(ns, inv, label="Gauss-Jordan inverse")
ax1.loglog(ns, solve, label="Ly = b and Ux = y")
ax1.loglog(ns, 2 * ns**3 / 3, "--", lw=0.9, color="0.5")
ax1.loglog(ns, 2 * ns**3, ":", lw=0.9, color="0.5")
ax1.loglog(ns, 2 * ns**2, "-.", lw=0.9, color="0.5")
ax1.text(150, 2 * 150**3 / 3 * 0.35, "$2n^3/3$", color="0.4")
ax1.text(150, 2 * 150**3 * 1.6, "$2n^3$", color="0.4")
ax1.text(150, 2 * 150**2 * 1.6, "$2n^2$", color="0.4")
ax1.set_xlabel("matrix order n")
ax1.set_ylabel("floating-point operations")
ax1.set_title("Cost of one factorization or solve")
ax1.legend(fontsize=9)

n = 200
ks = np.arange(1, 401)
repeat = ks * (lu_flops(n) + solve[n - 2])
reuse = lu_flops(n) + ks * solve[n - 2]
ax2.plot(ks, repeat / 1e6, label="eliminate again for every b")
ax2.plot(ks, reuse / 1e6, label="factor once, then two triangular solves")
ax2.set_xlabel("number of right-hand sides k")
ax2.set_ylabel("operations (millions)")
ax2.set_title("Solving Ax = b for k vectors b, n = 200")
ax2.legend(fontsize=9)
fig.tight_layout()
