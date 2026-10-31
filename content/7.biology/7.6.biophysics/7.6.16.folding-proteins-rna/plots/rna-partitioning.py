# Kinetic partitioning in RNA folding, and kinetic control of a riboswitch.
# A: scheme. Unfolded RNA (secondary structure formed) folds directly to the native state N with rate
#    k_N = 1 /s or into a long-lived misfolded state M with k_M = 9 /s (partition factor 10 % : 90 %, as for
#    the Tetrahymena group I ribozyme); M reaches N only by partly unfolding, k_MN = 2e-3 /s. A DEAD-box
#    RNA chaperone (CYT-19 type) accelerates the escape from M (here 30-fold).
# B: fraction native against time (logarithmic): a fast phase of 10 % amplitude and a slow phase of 90 %.
# C: a riboswitch that must bind its ligand (k_on = 1e7 /M/s, K_D = 10 nM) before the polymerase reaches the
#    terminator: fraction of transcripts switched = k_on L / (k_on L + k_t) for a decision window 1/k_t.
#    Fast transcription moves the half-switching concentration T50 far above K_D (kinetic control).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig = plt.figure(figsize=(13.5, 4.2))
gs = fig.add_gridspec(1, 3, width_ratios=[1.0, 1.1, 1.1])

ax = fig.add_subplot(gs[0])
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis("off")
bio.box(ax, (1.6, 3.5), 2.0, 1.0, "rna", text="U")
bio.box(ax, (8.2, 5.5), 2.0, 1.0, "positive", text="N")
bio.box(ax, (8.2, 1.5), 2.0, 1.0, "negative", text="M")
bio.arrow(ax, (2.7, 3.8), (7.1, 5.4), kind="process")
bio.arrow(ax, (2.7, 3.2), (7.1, 1.6), kind="process")
bio.arrow(ax, (8.2, 2.1), (8.2, 4.9), kind="process")
bio.label(ax, (4.4, 5.3), "k_N = 1 s⁻¹  (10 %)", size="small")
bio.label(ax, (4.4, 1.7), "k_M = 9 s⁻¹  (90 %)", size="small")
bio.label(ax, (9.0, 3.5), "k_MN", size="small", ha="left")
bio.label(ax, (5.0, 6.7), "A   Kinetic partitioning", size="small", bold=True)
bio.label(ax, (8.2, 0.4), "misfolded, long-lived", size="tiny", color=P.muted())

ax = fig.add_subplot(gs[1])
kN, kM = 1.0, 9.0
t = np.geomspace(1e-2, 1e5, 500)
for kMN, tok, lab in ((2e-3, "rna", "no chaperone, k_MN = 2×10⁻³ s⁻¹"), (6e-2, "dna", "with RNA chaperone (×30)")):
    phi = kN / (kN + kM)
    # exact solution of U -> N, U -> M -> N
    k = kN + kM
    M = kM / (kMN - k) * (np.exp(-k * t) - np.exp(-kMN * t))
    U = np.exp(-k * t)
    ax.semilogx(t, 1 - U - M, color=charts.line(tok), lw=1.8, label=lab)
ax.axhline(0.1, color=P.muted(), lw=0.6, ls=":")
ax.text(0.012, 0.16, "fast phase: partition factor 0.1", fontsize=7.5, color=P.muted())
ax.set_ylim(-0.02, 1.02)
charts.style_axes(ax, "time / s", "fraction native")
ax.legend(fontsize=7.5, frameon=False, loc="upper left")
charts.title(ax, "B   Fast and slow folding populations")

ax = fig.add_subplot(gs[2])
kon, KD = 1e7, 1e-8
L = np.logspace(-10, -4, 300)
ax.semilogx(L * 1e9, L / (L + KD), color=P.muted(), lw=1.2, ls="--", label="equilibrium, K_D = 10 nM")
for kt, tok in ((1.0, "neutral"), (10.0, "dna"), (100.0, "rna")):
    f = kon * L / (kon * L + kt)
    ax.semilogx(L * 1e9, f, color=charts.line(tok), lw=1.8, label=f"window 1/k_t = {1 / kt:g} s:  T50 = {kt / kon * 1e9:.0f} nM")
charts.style_axes(ax, "ligand concentration / nM", "fraction switched")
ax.legend(fontsize=7, frameon=False, loc="upper left")
charts.title(ax, "C   Riboswitch: kinetic control")
fig.tight_layout()
