"""A toy binary floating-point system on the real line, and the relative spacing of IEEE double precision numbers."""

import numpy as np
import matplotlib.pyplot as plt

# Toy system: base 2, precision p = 3 (hidden bit + 2 fraction bits), exponents e_min = -1, ..., e_max = 2.
p, e_min, e_max = 3, -1, 2
fracs = np.arange(2 ** (p - 1)) / 2 ** (p - 1)
normal = np.array([(1 + f) * 2.0**e for e in range(e_min, e_max + 1) for f in fracs])
subnormal = fracs[1:] * 2.0**e_min

fig, axes = plt.subplots(2, 1, figsize=(9, 5.6), gridspec_kw={"height_ratios": [1, 1.4]})
ax = axes[0]
ax.axhline(0, color="0.6", lw=0.8)
ax.vlines(normal, -0.6, 0.6, color="C0", lw=1.8, label="normalized numbers 1.d1d2 x 2^e")
ax.vlines(subnormal, -0.35, 0.35, color="C1", lw=1.8, label="subnormal numbers 0.d1d2 x 2^e_min")
ax.vlines([0], -0.6, 0.6, color="C3", lw=1.8, label="zero")
for e in range(e_min, e_max + 2):
    ax.annotate(f"2^{e}", (2.0**e, 0.65), ha="center", fontsize=8)
ax.set_ylim(-1, 1.3)
ax.set_yticks([])
ax.set_xlim(-0.2, 8.2)
ax.set_title("Toy system: base 2, p = 3, e in [-1, 2]; the gap doubles at each power of 2", fontsize=10)
ax.legend(fontsize=8, loc="upper right", ncol=1, framealpha=0.9)

# Relative spacing of doubles: spacing(x) / x oscillates between 2^-53 and 2^-52.
ax = axes[1]
x = np.logspace(-3, 4, 4000, base=2)
ax.semilogx(x, np.spacing(x) / x, color="C0", lw=1.2, label="gap to the next double / x")
ax.axhline(2.0**-52, color="C3", ls="--", lw=1, label="machine epsilon 2^-52")
ax.axhline(2.0**-53, color="C2", ls=":", lw=1.4, label="unit roundoff u = 2^-53")
ax.set_xscale("log", base=2)
ax.set_xlabel("x")
ax.set_ylabel("relative gap")
ax.set_title("IEEE double precision: absolute gaps grow with x, relative gaps stay within a factor of 2", fontsize=10)
ax.legend(fontsize=8, loc="center right")
ax.grid(alpha=0.3)
fig.tight_layout()
