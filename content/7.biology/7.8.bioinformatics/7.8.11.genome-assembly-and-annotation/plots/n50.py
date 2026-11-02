# Definition of N50 and L50 on an abstract set of contig lengths (arbitrary units).
import numpy as np
import matplotlib.pyplot as plt

lengths = np.array([30, 22, 15, 11, 8, 6, 4, 2, 1, 1])
total = lengths.sum()
cum = np.cumsum(lengths) / total
i50 = int(np.argmax(cum >= 0.5))

fig, (a, b) = plt.subplots(1, 2, figsize=(9.0, 3.4))
starts = np.concatenate([[0], np.cumsum(lengths)[:-1]]) / total
for k, (s, w) in enumerate(zip(starts, lengths / total)):
    a.barh(0, w, left=s, height=0.5, color="C0" if k <= i50 else "C7", edgecolor="black", linewidth=0.6)
a.axvline(0.5, color="C3", linestyle="--")
a.text(0.5, 0.42, "50 % of total length", color="C3", ha="center", fontsize=9)
a.set_xlim(0, 1)
a.set_ylim(-0.5, 0.6)
a.set_yticks([])
a.set_xlabel("cumulative fraction of assembly length")
a.set_title("A  contigs sorted by length", fontsize=10, loc="left")
a.text(starts[i50] + lengths[i50] / total / 2, -0.38, f"N50 = {lengths[i50]}, L50 = {i50 + 1}",
       ha="center", fontsize=9)

x = np.concatenate([[0], cum])
y = np.concatenate([[lengths[0]], lengths])
b.step(100 * x, y, where="pre", color="C0")
b.axvline(50, color="C3", linestyle="--")
b.set_xlabel("x (%)")
b.set_ylabel("Nx (length units)")
b.set_xlim(0, 100)
b.set_ylim(0, 33)
b.set_title("B  the Nx curve", fontsize=10, loc="left")
fig.tight_layout()
