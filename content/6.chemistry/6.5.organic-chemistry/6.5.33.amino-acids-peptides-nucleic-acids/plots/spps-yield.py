"""Why every step of solid-phase synthesis must be nearly quantitative: the fraction of chains
that carry the full-length sequence after n coupling cycles, if each cycle (deprotection plus
coupling) succeeds with probability p, is p^(n-1) for a peptide or oligonucleotide of length n
(the first residue is already on the resin). The other chains are deletion sequences that
differ from the product by a single residue and are hard to remove."""

import numpy as np
import matplotlib.pyplot as plt

n = np.arange(1, 201)
fig, ax = plt.subplots(figsize=(7.5, 4.0))
for p, c in ((0.95, "#dc2626"), (0.98, "#d97706"), (0.99, "#16a34a"), (0.995, "#2563eb"), (0.999, "#7c3aed")):
    ax.plot(n, 100 * p ** (n - 1), color=c, lw=2, label=f"{100 * p:g}% per cycle")
ax.set_xlabel("chain length $n$ (residues)")
ax.set_ylabel("full-length chains / %")
ax.set_xlim(1, 200)
ax.set_ylim(0, 100)
ax.legend(frameon=False, fontsize=9)
