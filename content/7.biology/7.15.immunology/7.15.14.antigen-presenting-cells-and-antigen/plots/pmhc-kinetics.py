# Supply and lifetime set the number of a given peptide-MHC complex on an antigen-presenting cell.
# One-compartment model: dP/dt = sigma(t) - (ln 2 / t_half) P, with sigma the rate at which complexes of one
# peptide reach the surface (complexes per hour) and t_half the surface half-life of that complex.
# Steady state P* = sigma * t_half / ln 2. Illustrative values: sigma = 20 h^-1 during a 24 h antigen pulse;
# half-lives of 2 h (weakly bound peptide) to 48 h (stable peptide on a mature dendritic cell). A T cell is
# assumed to detect about 10 complexes per cell (order of magnitude from single-molecule studies).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
LN2 = np.log(2)
t = np.linspace(0, 120, 2401)
dt = t[1] - t[0]
sigma = np.where(t < 24, 20.0, 0.0)

fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.4))
for th, tok in ((2, "neutral"), (8, "dna"), (24, "enzyme"), (48, "negative")):
    p = np.zeros_like(t)
    for i in range(1, len(t)):
        p[i] = p[i - 1] + dt * (sigma[i - 1] - LN2 / th * p[i - 1])
    axs[0].plot(t, p, color=charts.line(tok), lw=1.4, label=f"t½ = {th} h")
axs[0].axvspan(0, 24, color=P.fill("highlight"), alpha=0.25, lw=0)
axs[0].text(12, 1500, "antigen\nsupply", fontsize=7, color=P.ink(), ha="center", va="top")
axs[0].axhline(10, color=P.muted(), lw=0.8, ls="--")
axs[0].text(118, 12, "detection ~10 per cell", fontsize=7, color=P.muted(), ha="right", va="bottom")
axs[0].set_yscale("log")
axs[0].set_ylim(1, 2000)
axs[0].legend(frameon=False, fontsize=7, labelcolor=P.ink(), loc="upper right")
charts.style_axes(axs[0], "time / h", "complexes of one peptide per cell")
charts.title(axs[0], "A")

s = np.logspace(-1, 3, 200)
for th, tok in ((2, "neutral"), (8, "dna"), (24, "enzyme"), (48, "negative")):
    axs[1].plot(s, s * th / LN2, color=charts.line(tok), lw=1.4, label=f"t½ = {th} h")
axs[1].axhline(10, color=P.muted(), lw=0.8, ls="--")
axs[1].axhline(1e5, color=P.muted(), lw=0.8, ls=":")
axs[1].text(0.12, 1.3e5, "total MHC I ~10⁵ per cell", fontsize=7, color=P.muted(), va="bottom")
axs[1].set_xscale("log")
axs[1].set_yscale("log")
axs[1].set_ylim(0.1, 1e6)
charts.style_axes(axs[1], "supply σ / (complexes h⁻¹)", "steady state P* = σ t½ / ln 2")
charts.title(axs[1], "B")
fig.tight_layout()
