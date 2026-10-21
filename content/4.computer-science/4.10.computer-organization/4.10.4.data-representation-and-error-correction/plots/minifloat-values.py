import numpy as np
import matplotlib.pyplot as plt

# A toy IEEE-style format: 1 sign bit, 3 exponent bits (bias 3), 2 fraction bits.
EXP_BITS, FRAC_BITS = 3, 2
BIAS = 2 ** (EXP_BITS - 1) - 1

normal, subnormal = [], []
for e in range(0, 2 ** EXP_BITS - 1):          # the all-ones exponent is reserved for inf/NaN
    for f in range(2 ** FRAC_BITS):
        frac = f / 2 ** FRAC_BITS
        if e == 0:
            subnormal.append(frac * 2.0 ** (1 - BIAS))
        else:
            normal.append((1 + frac) * 2.0 ** (e - BIAS))

normal = np.array(normal)
subnormal = np.array(subnormal)

fig, axes = plt.subplots(2, 1, figsize=(8.4, 3.4), gridspec_kw={"height_ratios": [1, 1]})

for ax, xmax, title in [(axes[0], normal.max() * 1.05, "all non-negative finite values"),
                        (axes[1], 1.1, "zoom near zero")]:
    ax.axhline(0, color="0.6", lw=0.8)
    ax.vlines(normal, -0.4, 0.4, color="C0", lw=1.6, label="normalized")
    ax.vlines(subnormal, -0.4, 0.4, color="C1", lw=1.6, label="subnormal (and zero)")
    for k in range(1 - BIAS, 2 ** EXP_BITS - 1 - BIAS):
        if 2.0 ** k <= xmax:
            ax.axvline(2.0 ** k, color="0.75", ls=":", lw=0.8)
    ax.set_xlim(-0.02 * xmax, xmax)
    ax.set_ylim(-1, 1)
    ax.set_yticks([])
    ax.set_title(title, fontsize=10)

axes[1].set_xticks([0, 0.25, 0.5, 0.75, 1.0])
axes[0].set_ylim(-0.6, 1.5)
axes[0].legend(loc="upper left", fontsize=9, ncol=2, frameon=False)
axes[1].set_xlabel("value (1 sign, 3 exponent, 2 fraction bits; bias 3; dotted lines at powers of two)")
fig.tight_layout()
