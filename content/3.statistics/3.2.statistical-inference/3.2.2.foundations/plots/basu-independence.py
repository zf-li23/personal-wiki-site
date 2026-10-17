"""Sample mean versus sample range: independent for normal samples (Basu), dependent for exponential samples."""

import numpy as np
import matplotlib.pyplot as plt

n, reps = 10, 3000
fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
for ax, (name, data) in zip(axes, [
    ("N(0, 1) samples", np.random.normal(size=(reps, n))),
    ("Exp(1) samples", np.random.exponential(size=(reps, n))),
]):
    m = data.mean(axis=1)
    r = data.max(axis=1) - data.min(axis=1)
    rho = np.corrcoef(m, r)[0, 1]
    ax.scatter(m, r, s=4, alpha=0.35, color="C0")
    ax.set_title(f"{name}, n = {n}: correlation {rho:.2f}")
    ax.set_xlabel("sample mean")
    ax.set_ylabel("sample range")
    ax.grid(alpha=0.3)
fig.tight_layout()
