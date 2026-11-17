# A: decomposition constant k = L / X_ss and 3/k for six biomes (Swift, Heal and Anderson 1979, rounded).
# B: model k = k10 * Q10^((T-10)/10) * g(theta), Q10 = 2, k10 = 0.4 /yr,
#    g(theta) = (4 theta (1 - theta))^1.5 (theta = water-filled fraction of pore volume, optimum 0.5).
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio

P = bio.P
biomes = ["Tundra", "Boreal\nforest", "Temperate\ndeciduous", "Temperate\ngrassland", "Savanna", "Tropical\nrain forest"]
k = [0.03, 0.21, 0.77, 1.5, 3.2, 6.0]
fig, (a, b) = plt.subplots(1, 2, figsize=(11.0, 4.4))
x = np.arange(len(biomes))
a.bar(x, k, color=[P.fill(t) for t in ("neutral", "enzyme", "golgi", "lipid", "rna", "thylakoid")],
      edgecolor=P.muted())
for xi, v in zip(x, k):
    a.text(xi, v * 1.18, (f"3/k ≈ {3/v:.0f} yr" if 3 / v >= 10 else f"3/k ≈ {3/v:.2g} yr"), ha="center", fontsize=7.5, color=P.ink())
a.set_yscale("log")
a.set_ylim(0.01, 30)
a.set_xticks(x, biomes, fontsize=7.5)
a.set_ylabel("k = L / X$_{ss}$ / yr⁻¹ (log scale)")
a.set_title("A  Litter decomposition by biome", loc="left", fontweight="bold")

T = np.linspace(-5, 30, 200)
for th, tok in ((0.15, "antibody"), (0.5, "plant"), (0.7, "dna"), (0.9, "protein")):
    g = (4 * th * (1 - th)) ** 1.5
    b.plot(T, 0.4 * 2 ** ((T - 10) / 10) * g, color=P.edge(tok), lw=2,
           label=f"water-filled pores {th*100:.0f}%" + (" (optimum)" if th == 0.5 else "")
           + (" (nearly saturated)" if th == 0.9 else ""))
b.set_xlabel("Temperature / °C")
b.set_ylabel("k / yr⁻¹")
b.set_xlim(-5, 30)
b.legend(frameon=False, fontsize=8, loc="upper left")
b.set_title("B  Temperature and moisture (model)", loc="left", fontweight="bold")
for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
