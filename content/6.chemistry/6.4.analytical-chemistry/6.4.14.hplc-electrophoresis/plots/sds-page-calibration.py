"""SDS-PAGE calibration (12 % gel, illustrative data): lg M of the marker proteins against
their relative mobility R_f (migration distance / distance of the dye front). The relation
is linear in the middle of the range and bends at both ends, where the gel no longer
sieves effectively. The line is the least-squares fit to the 15-150 kDa markers; an unknown
band at R_f = 0.47 is read back from it."""

import numpy as np
import matplotlib.pyplot as plt

M = np.array([250, 150, 100, 75, 50, 37, 25, 20, 15, 10.0])        # kDa
lg = np.log10(M)
rng = np.random.default_rng(0)
Rf = np.clip(0.5 - (lg - 1.6) / 1.45 + 0.09 * (lg - 1.6) ** 3 - 0.12 * np.maximum(1.25 - lg, 0) ** 0.5
             + rng.normal(0, 0.006, len(M)), 0.02, 0.98)
Rf[-1] = 0.93
sel = (M <= 150) & (M >= 15)
b, a = np.polyfit(Rf[sel], lg[sel], 1)
Rx = 0.47
Mx = 10 ** (a + b * Rx)

fig, ax = plt.subplots(figsize=(6.4, 4.2))
ax.plot(Rf, lg, "o", color="C0", ms=5, label="marker proteins")
for m, r, l in zip(M, Rf, lg):
    ax.text(r + 0.015, l + 0.02, f"{m:g}", fontsize=7)
rr = np.linspace(0.12, 0.85, 50)
ax.plot(rr, a + b * rr, color="C0", lw=1.4, label=rf"fit (15-150 kDa): $\lg M$ = {a:.2f} $-$ {-b:.2f} $R_f$")
ax.plot([Rx], [np.log10(Mx)], "s", color="C3", ms=6)
ax.annotate(rf"unknown band: {Mx:.0f} kDa", (Rx, np.log10(Mx)), xytext=(Rx + 0.08, np.log10(Mx) + 0.3),
            fontsize=8, arrowprops=dict(arrowstyle="-", color="0.5"))
ax.set_xlim(0, 1)
ax.set_xlabel(r"relative mobility $R_f$")
ax.set_ylabel(r"$\lg (M$ / kDa)")
ax.legend(frameon=False, fontsize=8, loc="lower left")
fig.tight_layout()
