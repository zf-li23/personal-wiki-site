# Schematic: Hi-C contact probability decays with distance; the contact map orders contigs.
import numpy as np
import matplotlib.pyplot as plt

fig, (a, b) = plt.subplots(1, 2, figsize=(9.0, 3.6))

s = np.logspace(4, 8, 200)
a.loglog(s, 1e4 / s, color="C0", label="same chromosome, P(s) ~ 1/s")
a.axhline(2e-5, color="C3", linestyle="--", label="different chromosomes")
a.set_xlabel("genomic distance s (bp)")
a.set_ylabel("relative contact frequency")
a.set_title("A  distance decay", fontsize=10, loc="left")
a.legend(fontsize=8, frameon=False)

# Bins of three contigs placed along one chromosome in the true order; the map is drawn
# with the contigs in a wrong order (C, A, B) and in the correct order (A, B, C).
sizes = {"A": 8, "B": 6, "C": 10}
coord = {}
pos = 0
for name in "ABC":
    coord[name] = np.arange(pos, pos + sizes[name])
    pos += sizes[name]

def contact_map(order):
    idx = np.concatenate([coord[n] for n in order])
    d = np.abs(idx[:, None] - idx[None, :]) + 1.0
    return 1.0 / d

m = contact_map("CAB")
b.imshow(np.log10(m), cmap="Reds", interpolation="nearest")
edges = np.cumsum([sizes[n] for n in "CAB"])[:-1] - 0.5
for e in edges:
    b.axhline(e, color="black", linewidth=0.6)
    b.axvline(e, color="black", linewidth=0.6)
ticks = []
start = 0
for n in "CAB":
    ticks.append(start + sizes[n] / 2 - 0.5)
    start += sizes[n]
b.set_xticks(ticks)
b.set_xticklabels(list("CAB"))
b.set_yticks(ticks)
b.set_yticklabels(list("CAB"))
b.set_title("B  contigs in a wrong order", fontsize=10, loc="left")
fig.tight_layout()
