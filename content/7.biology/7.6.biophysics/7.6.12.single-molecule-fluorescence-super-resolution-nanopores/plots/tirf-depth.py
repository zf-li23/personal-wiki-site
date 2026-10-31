# Total internal reflection at a glass (n1 = 1.518) / water (n2 = 1.333) interface.
# A: penetration depth of the evanescent intensity, d = lambda0 / (4 pi sqrt(n1^2 sin^2 theta - n2^2)),
#    against the angle of incidence for 405, 488, 561 and 640 nm; the critical angle is 61.4 deg and the
#    maximal angle reachable through an NA 1.49 objective is 79 deg.
# B: intensity profiles I(z) = I0 exp(-z/d) at 488 nm for three angles, compared with the extent of a
#    confocal (about 600 nm) and a widefield focal region, and with the size of a cell's basal membrane region.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
n1, n2 = 1.518, 1.333
thc = np.degrees(np.arcsin(n2 / n1))
thmax = np.degrees(np.arcsin(1.49 / n1))
fig, axs = plt.subplots(1, 2, figsize=(11.0, 4.0))
ax = axs[0]
th = np.linspace(thc + 0.05, 85, 400)
for lam, tok in ((405, "protein"), (488, "dna"), (561, "positive"), (640, "negative")):
    d = lam / (4 * np.pi * np.sqrt(n1**2 * np.sin(np.radians(th)) ** 2 - n2**2))
    ax.plot(th, d, color=charts.line(tok), lw=1.8, label=f"{lam} nm")
ax.axvline(thc, color=P.muted(), lw=0.8, ls=":")
ax.axvline(thmax, color=P.muted(), lw=0.8, ls="--")
ax.text(66, 440, f"critical angle {thc:.1f}° (dotted)", fontsize=8, color=P.muted())
ax.text(66, 400, f"NA 1.49 limit {thmax:.0f}° (dashed)", fontsize=8, color=P.muted())
ax.set_ylim(0, 500)
ax.legend(fontsize=8, frameon=False, loc="center right")
charts.style_axes(ax, "angle of incidence θ / °", "penetration depth d / nm")
charts.title(ax, "A   Evanescent penetration depth")

ax = axs[1]
z = np.linspace(0, 800, 400)
for thv, tok in ((63, "dna2"), (66, "dna"), (72, "rna")):
    d = 488 / (4 * np.pi * np.sqrt(n1**2 * np.sin(np.radians(thv)) ** 2 - n2**2))
    ax.plot(z, np.exp(-z / d), color=charts.line(tok), lw=1.8, label=f"θ = {thv}°, d = {d:.0f} nm")
ax.axvspan(0, 10, color=P.light("membrane"), alpha=0.9, lw=0)
ax.text(14, 0.9, "membrane", fontsize=8, color=P.ink())
ax.axvline(600, color=P.muted(), lw=0.8, ls=":")
ax.text(610, 0.5, "confocal\nsection ~600 nm", fontsize=8, color=P.muted())
ax.legend(fontsize=8, frameon=False, loc="upper right")
charts.style_axes(ax, "distance from glass z / nm", "excitation intensity I/I0")
charts.title(ax, "B   Only the first ~100 nm are excited")
fig.tight_layout()
