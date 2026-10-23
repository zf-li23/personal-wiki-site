"""Size-exclusion calibration of a gel-filtration column (illustrative: void volume
V0 = 8.0 mL, pore volume Vi = 16.0 mL, total volume Vt = 24 mL) with globular protein
standards. V_R = V0 + K_SEC Vi; between total exclusion (K = 0) and total permeation (K = 1)
lg M falls almost linearly with V_R. The straight line is the least-squares fit to the
standards in the fractionation range; the unknown eluting at 14.6 mL is read back from it."""

import numpy as np
import matplotlib.pyplot as plt

V0, Vi = 8.0, 16.0
std = [("thyroglobulin", 669), ("ferritin", 440), ("aldolase", 158), ("conalbumin", 75),
       ("ovalbumin", 44), ("carbonic anhydrase", 29), ("ribonuclease A", 13.7),
       ("aprotinin", 6.5)]
rng = np.random.default_rng(0)


def K_of(lgM):
    return 0.5 * (1 - np.tanh((lgM - 4.85) / 0.95))


lgM = np.log10([m * 1e3 for _, m in std])
VR = V0 + K_of(lgM) * Vi + rng.normal(0, 0.08, len(std))
sel = (VR > V0 + 1.5) & (VR < V0 + Vi - 1.5)
b, a = np.polyfit(VR[sel], lgM[sel], 1)
Vx = 14.6
Mx = 10 ** (a + b * Vx)

fig, ax = plt.subplots(figsize=(6.6, 4.3))
grid = np.linspace(3.2, 6.6, 300)
ax.plot(V0 + K_of(grid) * Vi, grid, color="0.6", lw=1.0, ls=":")
vv = np.linspace(9.0, 21.5, 50)
ax.plot(vv, a + b * vv, color="C0", lw=1.5, label=rf"fit: $\lg M$ = {a:.2f} $-$ {-b:.3f} $V_\mathrm{{R}}$/mL")
ax.plot(VR, lgM, "o", color="C0", ms=5)
for (name, m), v, l in zip(std, VR, lgM):
    ax.text(v + 0.25, l + 0.04, name, fontsize=7)
ax.plot([Vx], [np.log10(Mx)], "s", color="C3", ms=6)
ax.annotate(rf"unknown: {Mx / 1e3:.0f} kDa", (Vx, np.log10(Mx)), xytext=(Vx - 5.2, np.log10(Mx) - 0.55),
            fontsize=8, arrowprops=dict(arrowstyle="-", color="0.5"))
for v, lab in [(V0, r"$V_0$ (exclusion)"), (V0 + Vi, r"$V_\mathrm{t}$ (total permeation)")]:
    ax.axvline(v, color="0.5", lw=0.8, ls="--")
    ax.text(v + 0.2, 3.3, lab, fontsize=8)
ax.set_xlim(6, 26)
ax.set_ylim(3.2, 6.4)
ax.set_xlabel(r"elution volume $V_\mathrm{R}$ / mL")
ax.set_ylabel(r"$\lg (M / \mathrm{g\,mol^{-1}})$")
ax.legend(frameon=False, fontsize=8, loc="upper right")
fig.tight_layout()
