# How diffusion caps the size of a respiring cell. A spherical cell of radius R consumes O2 uniformly at a
# volumetric rate q (mol m^-3 s^-1); O2 enters only by diffusion (coefficient D) from a surface concentration
# c0. The steady-state reaction-diffusion equation D * Laplacian(c) = q gives
#     c(r) = c0 - q (R^2 - r^2) / (6 D),
# so the centre runs out of O2 when R exceeds R_max = sqrt(6 D c0 / q).
# Parameters: D = 2e-9 m^2 s^-1 (O2 in water; lower in cytoplasm), c0 = 0.2 mM (air-saturated water, 37 C).
# Respiration rates: E. coli in fast aerobic growth ~1.7 mol m^-3 s^-1 (about 1e6 O2 per cell per second);
# a cultured mammalian cell ~0.027 mol m^-3 s^-1 (about 80 amol per cell per second in 3000 um^3).
# A: O2 profiles inside cells of R = 0.5, 0.8 and 1.0 R_max. B: R_max against q, with both cell types.
# C: surface-to-volume ratio 3/R, which falls as cells grow.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
D, c0 = 2e-9, 0.2

fig, axs = plt.subplots(1, 3, figsize=(12.5, 3.8), gridspec_kw={"width_ratios": [1, 1.1, 1]})

ax = axs[0]
x = np.linspace(-1, 1, 201)
for f, tok in ((0.5, "positive"), (0.8, "highlight"), (1.0, "negative")):
    c = 1 - f**2 * (1 - x**2)
    ax.plot(x, c, color=charts.line(tok), lw=1.8, label=f"R = {f:g} R_max")
ax.axhline(0, color=P.muted(), lw=0.6, ls=":")
ax.set_xlim(-1, 1)
ax.set_ylim(-0.05, 1.35)
ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
ax.set_xticks([-1, 0, 1])
ax.set_xticklabels(["−R", "centre", "R"])
ax.legend(fontsize=7, frameon=False, loc="upper center", ncol=1)
charts.style_axes(ax, "position across the cell", "c / c₀")
ax.set_title("A   O₂ inside a respiring sphere", loc="left", fontsize=9, color=P.ink())

ax = axs[1]
q = np.logspace(-3, 1, 100)
rmax = np.sqrt(6 * D * c0 / q) * 1e6
ax.loglog(q, rmax, color=charts.line("mitochondrion"), lw=1.8)
for qq, size, txt, tok in ((1.7, 1.0, "E. coli", "bacterium"), (0.027, 10.0, "mammalian cell", "cytoplasm")):
    r = np.sqrt(6 * D * c0 / qq) * 1e6
    ax.plot([qq], [r], "o", color=charts.line(tok), ms=6)
    ax.plot([qq], [size], "s", color=charts.line(tok), ms=6, mfc="none")
    ax.plot([qq, qq], [size, r], color=charts.line(tok), lw=0.8, ls=":")
    ax.text(qq * 1.25, np.sqrt(size * r), f"{txt}\nlimit {r:.0f} µm", fontsize=7, color=P.ink(), va="center",
            style="italic" if txt == "E. coli" else "normal")
ax.text(1.2e-3, 0.6, "squares: actual radius", fontsize=7, color=P.muted())
ax.set_xlim(1e-3, 10)
ax.set_ylim(0.3, 3000)
charts.style_axes(ax, "O₂ consumption q / (mol m⁻³ s⁻¹)", "R_max / µm")
ax.set_title("B   R_max = (6Dc₀/q)^½", loc="left", fontsize=9, color=P.ink())

ax = axs[2]
R = np.logspace(-1, 3, 100)
ax.loglog(R, 3 / R, color=charts.line("membrane"), lw=1.8)
for r, txt, tok in ((0.15, "Mycoplasma", "bacterium"), (0.5, "E. coli", "bacterium"), (7.5, "HeLa", "cytoplasm"),
                    (60, "oocyte", "animal"), (375, "Thiomargarita", "bacterium")):
    ax.plot([r], [3 / r], "o", color=charts.line(tok), ms=5)
    ax.text(r * 1.3, 3 / r * 1.25, txt, fontsize=7, color=P.ink(),
            style="italic" if txt in ("Mycoplasma", "E. coli", "Thiomargarita") else "normal")
ax.set_xlim(0.1, 1000)
ax.set_ylim(2e-3, 40)
charts.style_axes(ax, "radius R / µm", "S/V / µm⁻¹")
ax.set_title("C   Surface per volume, 3/R", loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
