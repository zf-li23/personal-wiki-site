"""False-positive rate of a Bloom filter versus bits per key, with a simulation check."""

import matplotlib.pyplot as plt
import numpy as np

bits_per_key = np.linspace(1, 20, 200)


def fpr(c, k):
    """Approximate false-positive rate with c = m/n bits per key and k hash functions."""
    return (1 - np.exp(-k / c)) ** k


fig, ax = plt.subplots(figsize=(7, 4))
for k, color in [(1, "C0"), (3, "C1"), (7, "C2")]:
    ax.semilogy(bits_per_key, fpr(bits_per_key, k), color=color, lw=1.6, label=f"k = {k}")
k_opt = np.maximum(1, np.round(bits_per_key * np.log(2)))
ax.semilogy(bits_per_key, fpr(bits_per_key, k_opt), color="black", lw=1.2, ls="--",
            label="optimal integer k")

# simulation: n keys inserted into m bits, then probe with keys not in the set
rng = np.random.default_rng(0)
n = 2000
sim_c, sim_rate = [], []
for c in [2, 4, 6, 8, 10, 12, 14, 16]:
    m = c * n
    k = max(1, round(c * np.log(2)))
    bits = np.zeros(m, dtype=bool)
    bits[rng.integers(0, m, size=(n, k))] = True        # positions of the inserted keys
    probes = rng.integers(0, m, size=(200_000, k))        # positions of absent keys
    sim_c.append(c)
    sim_rate.append(bits[probes].all(axis=1).mean())
ax.semilogy(sim_c, sim_rate, "o", color="C3", ms=5, label="simulation (optimal k)")

ax.set_xlabel("bits per key  m / n")
ax.set_ylabel("false-positive rate")
ax.set_xlim(1, 20)
ax.set_ylim(1e-5, 1)
ax.grid(True, which="both", alpha=0.3)
ax.legend()
fig.tight_layout()
