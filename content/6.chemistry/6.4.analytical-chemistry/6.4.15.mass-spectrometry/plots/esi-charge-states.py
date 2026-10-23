"""ESI spectrum of a 16951.5 Da protein (horse-heart apomyoglobin) as [M + zH]z+ ions with a
Gaussian charge-state distribution, for a denatured (acidic, organic solvent) and a native
(ammonium acetate) solution; right: the deconvolved (zero-charge) spectrum."""

import numpy as np
import matplotlib.pyplot as plt

M = 16951.5
mp = 1.007276
mz = np.linspace(600, 2600, 20001)


def spectrum(zc, width, zmin, zmax, peak_w=0.6):
    y = np.zeros_like(mz)
    lines = []
    for z in range(zmin, zmax + 1):
        a = np.exp(-((z - zc) ** 2) / (2 * width**2))
        m = (M + z * mp) / z
        y += a * np.exp(-((mz - m) ** 2) / (2 * peak_w**2))
        lines.append((z, m, a))
    return y / y.max(), lines


fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.6, 3.9), gridspec_kw={"width_ratios": [1.8, 1]})
den, den_lines = spectrum(19, 3.0, 11, 27)
nat, nat_lines = spectrum(8.4, 0.8, 7, 10, peak_w=1.5)
ax.plot(mz, den + 1.25, color="C0", lw=1.0)
ax.plot(mz, nat, color="C1", lw=1.0)
for z, m, a in den_lines:
    if a > 0.3:
        ax.text(m, 1.25 + a + 0.04, f"{z}+", ha="center", fontsize=6.5, color="C0")
for z, m, a in nat_lines:
    if a > 0.2:
        ax.text(m, a + 0.07, f"{z}+", ha="center", fontsize=7, color="C1")
ax.text(2580, 2.0, "denatured\n(water/methanol, 1 % acetic acid)", ha="right", fontsize=8, color="C0")
ax.text(1500, 0.75, "native\n(ammonium acetate, pH 7)", ha="right", fontsize=8, color="C1")
ax.set_xlim(600, 2600)
ax.set_ylim(0, 2.55)
ax.set_yticks([])
ax.set_xlabel("$m/z$")
ax.set_title("charge-state envelopes $[\\mathrm{M}+z\\mathrm{H}]^{z+}$", fontsize=10)

# Deconvolution: for each trial mass, add the intensities found at (M' + z mp)/z for all z.
masses = np.linspace(16700, 17200, 2001)
score = np.zeros_like(masses)
for z in range(5, 35):
    score += np.interp((masses + z * mp) / z, mz, den, left=0, right=0)
bx.plot(masses / 1000, score / score.max(), color="C0", lw=1.2)
bx.axvline(M / 1000, color="0.6", lw=0.6, ls=":")
bx.text(M / 1000 + 0.01, 1.0, f"{M:,.1f} Da".replace(",", r" "), fontsize=8, va="top")
bx.set_xlabel("mass $M$ / kDa")
bx.set_yticks([])
bx.set_title("deconvolved", fontsize=10)
fig.tight_layout()
