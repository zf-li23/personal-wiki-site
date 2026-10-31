# Association kinetics of macromolecules.
# A: electrostatic steering. Debye-Hueckel form of the association rate constant of two charged proteins,
#    ln k_on = ln k_on(basal) - (U/kT) / (1 + kappa a), with Debye length 1/kappa = 0.304 nm / sqrt(I/M) and
#    contact distance a = 0.6 nm; basal rate (no electrostatics) 5e5 /M/s, set by diffusion and the small
#    fraction of collisions with the right orientation; U is the interaction energy at contact in pure water.
#    The Smoluchowski limit for two proteins of radius 2 nm (about 7e9 /M/s) is shown for reference.
# B: induced fit or conformational selection? Observed relaxation rate after mixing with excess ligand L.
#    Induced fit: P + L <-> PL (fast, K1 = 50 uM), PL <-> PL* (k2 = 200 /s, k-2 = 10 /s):
#    k_obs = k-2 + k2 L/(K1 + L) rises. Conformational selection: P_inactive <-> P_active (k+ = 10 /s,
#    k- = 200 /s), P_active + L <-> PL (fast, K_D = 50 uM): k_obs = k+ + k- K_D/(K_D + L) falls.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 2, figsize=(12, 4.2))
I = np.logspace(-3, 0, 200)
kappa = np.sqrt(I) / 0.304
a = 0.6
for U, tok, lab in ((-6.0, "dna", "opposite charges, U = −6 kT"), (0.0, "neutral", "no electrostatics"),
                    (3.0, "rna", "like charges, U = +3 kT")):
    axs[0].loglog(I * 1000, 5e5 * np.exp(-U / (1 + kappa * a)), color=charts.line(tok), lw=1.8, label=lab)
axs[0].axhline(7e9, color=P.muted(), lw=0.8, ls=":")
axs[0].text(1.2, 9e9, "Smoluchowski limit", fontsize=7.5, color=P.muted())
axs[0].axvline(150, color=P.muted(), lw=0.6, ls="--")
axs[0].text(160, 2e4, "physiological", fontsize=7.5, color=P.muted())
axs[0].set_ylim(1e4, 3e10)
charts.style_axes(axs[0], "ionic strength / mM", "k_on / (M⁻¹ s⁻¹)")
axs[0].legend(fontsize=7.5, frameon=False, loc="upper right", bbox_to_anchor=(1.0, 0.88))
charts.title(axs[0], "A   Electrostatic steering is screened by salt")

L = np.linspace(0, 500, 300)  # uM
K = 50.0
axs[1].plot(L, 10 + 200 * L / (K + L), color=charts.line("enzyme"), lw=1.8, label="induced fit")
axs[1].plot(L, 10 + 200 * K / (K + L), color=charts.line("rna"), lw=1.8, label="conformational selection")
charts.style_axes(axs[1], "ligand concentration / µM", "k_obs / s⁻¹")
axs[1].legend(fontsize=7.5, frameon=False, loc="center right")
charts.title(axs[1], "B   The concentration dependence of k_obs")
fig.tight_layout()
