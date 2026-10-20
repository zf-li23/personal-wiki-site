"""Sinusoidal positional encodings: the matrix PE(pos, i) for 128 positions and
d = 128 (left); the dot product PE(m) . PE(n) as a function of the offset n - m,
which depends only on the offset (middle); and, for rotary position embedding,
the bound on the relative score used by Su et al., which decays with distance (right)."""

import numpy as np
import matplotlib.pyplot as plt

d, L = 128, 128
pos = np.arange(L)[:, None]
freq = 1.0 / 10000 ** (np.arange(0, d, 2) / d)          # theta_i = 10000^(-2i/d)
PE = np.zeros((L, d))
PE[:, 0::2] = np.sin(pos * freq)
PE[:, 1::2] = np.cos(pos * freq)

fig, axes = plt.subplots(1, 3, figsize=(13, 4.0))
im = axes[0].imshow(PE, aspect="auto", cmap="RdBu_r", vmin=-1, vmax=1, origin="lower")
axes[0].set_xlabel("dimension i")
axes[0].set_ylabel("position")
axes[0].set_title("sinusoidal encoding, d = 128", fontsize=10)
fig.colorbar(im, ax=axes[0], fraction=0.046)

offsets = np.arange(-100, 101)
for m, ls in zip([0, 30, 60], ["-", "--", ":"]):
    valid = (m + offsets >= 0) & (m + offsets < L)
    dots = PE[m] @ PE[m + offsets[valid]].T
    axes[1].plot(offsets[valid], dots, ls, lw=1.4, label=f"m = {m}")
axes[1].set_xlabel("offset n - m")
axes[1].set_ylabel("PE(m) . PE(n)")
axes[1].set_title("dot products depend only on n - m", fontsize=10)
axes[1].legend(fontsize=8)
axes[1].grid(alpha=0.3)

rel = np.arange(0, 2001)
S = np.cumsum(np.exp(1j * rel[:, None] * freq[None, :]), axis=1)   # partial sums S_j
bound = np.abs(S).mean(axis=1)
axes[2].plot(rel, bound, lw=1.2, color="C3")
axes[2].set_xlabel("relative distance m - n")
axes[2].set_ylabel("mean |S_j|")
axes[2].set_title("RoPE: long-range decay of the bound", fontsize=10)
axes[2].grid(alpha=0.3)
fig.tight_layout()
