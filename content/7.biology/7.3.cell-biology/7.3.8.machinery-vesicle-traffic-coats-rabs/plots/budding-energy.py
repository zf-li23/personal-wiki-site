# The energy of making a spherical bud of radius R (Helfrich model, energies in kBT; bending rigidity
# kappa = 20 kBT). A: a closed sphere costs 8 pi kappa ~ 500 kBT whatever its radius, while a coat that
# binds with energy w per unit area gains 4 pi R^2 w and membrane tension sigma costs 4 pi R^2 sigma;
# with w > sigma, budding becomes favourable beyond R* = sqrt(2 kappa / (w - sigma)). B: a coat that imposes a
# spontaneous curvature c0 (bending energy 8 pi kappa (1 - c0 R / 2)^2) makes the energy minimal at
# R = 2 / c0: the coat geometry selects the vesicle size (here c0 for R = 30, 45 and 60 nm).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import quant

kappa = 20.0
R = np.linspace(5, 100, 400)  # nm
fig, axs = plt.subplots(1, 2, figsize=(9.5, 3.5))
axs[0].plot(R, np.full_like(R, 8 * np.pi * kappa), color=quant.line_color("muted"), lw=1.6, ls="--",
            label="bending only, 8πκ")
for w, tok in ((0.02, "channel"), (0.05, "positive"), (0.1, "negative")):
    sigma = 0.005
    E = 8 * np.pi * kappa - 4 * np.pi * R ** 2 * (w - sigma)
    axs[0].plot(R, E, color=quant.line_color(tok), lw=1.8, label=f"w = {w} kBT/nm²")
    axs[0].plot([np.sqrt(2 * kappa / (w - sigma))], [0], "o", color=quant.line_color(tok), ms=4)
axs[0].axhline(0, color=bio.P.muted(), lw=0.8)
axs[0].set(xlabel="R / nm", ylabel="E / kBT", title="A  Bending cost vs coat binding", ylim=(-1500, 900))
axs[0].legend(frameon=False, fontsize=7.5, loc="lower left")

for R0, tok in ((30, "channel"), (45, "positive"), (60, "negative")):
    c0 = 2 / R0
    axs[1].plot(R, 8 * np.pi * kappa * (1 - c0 * R / 2) ** 2, color=quant.line_color(tok), lw=1.8, label=f"2/c₀ = {R0} nm")
axs[1].plot(R, np.full_like(R, 8 * np.pi * kappa), color=quant.line_color("muted"), lw=1.6, ls="--", label="c₀ = 0")
axs[1].set(xlabel="R / nm", ylabel="bending energy / kBT", title="B  Spontaneous curvature sets the size", ylim=(0, 900))
axs[1].legend(frameon=False, fontsize=7.5, loc="upper right")
for a in axs:
    a.spines[["top", "right"]].set_visible(False)
    a.title.set_fontsize(10)
fig.tight_layout()
