"""Two faces of the curse of dimensionality for points uniform in the unit cube.
Left: the edge length of a sub-cube that contains a fraction r of the data,
e = r**(1/d). Right: the relative contrast (d_max - d_min) / d_min between the
farthest and the nearest of 1000 points seen from a random query."""

import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

r = np.linspace(0.001, 1, 300)
for d in [1, 2, 3, 10, 100]:
    ax1.plot(r, r ** (1 / d), label=f"d = {d}")
ax1.set(xlabel="fraction of data r", ylabel="edge length of the sub-cube",
        title="Neighborhoods stop being local", xlim=(0, 1), ylim=(0, 1.02))
ax1.legend(loc="lower right")

rng = np.random.default_rng(0)
dims = np.array([1, 2, 5, 10, 20, 50, 100, 200, 500, 1000])
contrast = []
for d in dims:
    vals = []
    for _ in range(20):
        P = rng.random((1000, d))
        q = rng.random(d)
        dist = np.sqrt(((P - q) ** 2).sum(axis=1))
        vals.append((dist.max() - dist.min()) / dist.min())
    contrast.append(np.median(vals))
ax2.loglog(dims, contrast, marker="o")
ax2.set(xlabel="dimension d", ylabel="(d_max - d_min) / d_min",
        title="Distances concentrate (n = 1000)")
ax2.grid(True, which="both", alpha=0.3)
fig.tight_layout()
