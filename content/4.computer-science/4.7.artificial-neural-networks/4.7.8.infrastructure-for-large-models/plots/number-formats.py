"""Range and precision of the floating-point formats used in deep learning:
the interval of positive representable magnitudes (subnormal part lighter) on a
log2 axis, and the relative spacing of numbers (machine epsilon)."""

import numpy as np
import matplotlib.pyplot as plt

# name: (log2 smallest subnormal, log2 smallest normal, largest value, mantissa bits)
formats = {
    "FP32 (E8M23)": (-149, -126, (2 - 2**-23) * 2.0**127, 23),
    "BF16 (E8M7)": (-133, -126, (2 - 2**-7) * 2.0**127, 7),
    "FP16 (E5M10)": (-24, -14, 65504.0, 10),
    "FP8 E5M2": (-16, -14, 57344.0, 2),
    "FP8 E4M3": (-9, -6, 448.0, 3),
    "FP4 E2M1": (-1, 0, 6.0, 1),
}
names = list(formats)
y = np.arange(len(names))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 3.8), gridspec_kw={"width_ratios": [2.2, 1]})
for i, name in enumerate(names):
    sub, norm, big, _ = formats[name]
    top = np.log2(big)
    ax1.barh(i, norm - sub, left=sub, color="C0", alpha=0.35, height=0.6)
    ax1.barh(i, top - norm, left=norm, color="C0", height=0.6)
    ax1.text(top + 2, i, f"max {big:.3g}", va="center", fontsize=8)
ax1.axvspan(-30, 15, color="C3", alpha=0.08)
ax1.text(-29, -0.55, "typical gradients and activations", fontsize=8, color="C3")
ax1.set_yticks(y)
ax1.set_yticklabels(names)
ax1.set_ylim(len(names) - 0.5, -0.8)
ax1.set_xlim(-155, 150)
ax1.set_xlabel("log2 of magnitude (light: subnormal numbers)")
ax1.set_title("range of positive magnitudes", fontsize=10)
ax1.grid(axis="x", alpha=0.3)

eps = [2.0 ** -formats[n][3] for n in names]
ax2.barh(y, eps, color="C1", height=0.6)
for i, e in enumerate(eps):
    ax2.text(e * 1.6, i, f"2^-{formats[names[i]][3]}", va="center", fontsize=8)
ax2.set_xscale("log")
ax2.set_xlim(1e-8, 30)
ax2.set_yticks(y)
ax2.set_yticklabels([])
ax2.invert_yaxis()
ax2.set_xlabel("machine epsilon (gap after 1)")
ax2.set_title("precision", fontsize=10)
ax2.grid(axis="x", alpha=0.3)
fig.tight_layout()
