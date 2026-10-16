"""Error of Taylor partial sums: log10 |S_N(z) - f(z)| for f = 1/(1-z) and f = 1/(1+z^2),
expanded at 0. The partial sums converge exactly in the disk |z| < 1, whose radius is
the distance to the nearest singularity."""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 601)
X, Y = np.meshgrid(x, x)
Z = X + 1j * Y
N = 30

cases = [
    (lambda z: 1 / (1 - z), lambda z: sum(z**n for n in range(N)), [1 + 0j], r"$f(z) = 1/(1-z)$"),
    (lambda z: 1 / (1 + z**2), lambda z: sum((-1)**n * z**(2 * n) for n in range(N // 2)),
     [1j, -1j], r"$f(z) = 1/(1+z^2)$"),
]
fig, axes = plt.subplots(1, 2, figsize=(12, 5.4))
t = np.linspace(0, 2 * np.pi, 400)
for ax, (f, s, poles, title) in zip(axes, cases):
    with np.errstate(all="ignore"):
        err = np.log10(np.abs(s(Z) - f(Z)) + 1e-17)
    im = ax.imshow(np.clip(err, -16, 4), extent=[-2, 2, -2, 2], origin="lower",
                   cmap="viridis", vmin=-16, vmax=4)
    ax.plot(np.cos(t), np.sin(t), color="white", lw=1.5, ls="--")
    for p in poles:
        ax.plot(p.real, p.imag, "rx", ms=10, mew=2.5)
    ax.set_title(f"{title}, N = {N} terms")
    ax.set_xlabel("Re z")
    ax.set_ylabel("Im z")
fig.colorbar(im, ax=axes, label=r"$\log_{10}|S_N(z) - f(z)|$", shrink=0.85)
