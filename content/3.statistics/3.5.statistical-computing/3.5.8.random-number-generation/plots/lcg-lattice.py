"""Lattice structure of linear congruential generators: successive pairs (R_i, R_(i+1)) for
m = 101 with a = 3 and a = 12, and the triples of RANDU projected on the normal (9, -6, 1)
of its planes, compared with the Mersenne Twister."""

import numpy as np
import matplotlib.pyplot as plt


def lcg(a, c, m, x0, n):
    out = np.empty(n, dtype=np.int64)
    x = x0
    for i in range(n):
        x = (a * x + c) % m
        out[i] = x
    return out / m


fig, axes = plt.subplots(1, 3, figsize=(11, 3.8))
for ax, a in zip(axes[:2], (3, 12)):
    r = lcg(a, 0, 101, 1, 100)
    ax.plot(r[:-1], r[1:], "o", ms=3, color="C0")
    ax.set_title(f"LCG m = 101, a = {a}: pairs", fontsize=10)
    ax.set_xlabel("R_i")
    ax.set_ylabel("R_(i+1)")
    ax.set_aspect("equal")

# RANDU: X_(i+1) = 65539 X_i mod 2^31, so R_(i+2) - 6 R_(i+1) + 9 R_i is an integer
n = 3000
r = lcg(65539, 0, 2 ** 31, 1, n + 2)
proj_randu = 9 * r[:-2] - 6 * r[1:-1] + r[2:]
mt = np.random.RandomState(0).uniform(size=n + 2)  # legacy NumPy generator = Mersenne Twister
proj_mt = 9 * mt[:-2] - 6 * mt[1:-1] + mt[2:]
ax = axes[2]
ax.plot(proj_mt, mt[2:], ".", ms=2, color="C7", alpha=0.6, label="Mersenne Twister")
ax.plot(proj_randu, r[2:], ".", ms=2, color="C3", label="RANDU")
ax.set_title("Triples projected on (9, -6, 1)", fontsize=10)
ax.set_xlabel("9 R_i - 6 R_(i+1) + R_(i+2)")
ax.set_ylabel("R_(i+2)")
ax.legend(fontsize=8, loc="upper left", markerscale=4)
for a in axes:
    a.grid(alpha=0.3)
fig.tight_layout()
