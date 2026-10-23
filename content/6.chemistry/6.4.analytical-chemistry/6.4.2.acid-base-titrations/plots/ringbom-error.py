"""End-point error of a weak-acid titration from the Ringbom formula
E_t = (10^dpH - 10^-dpH) / sqrt(c_sp K_t), K_t = Ka / Kw, for several values of c_sp K_t.
The dashed lines mark |E_t| = 0.1 % and the usual visual uncertainty |dpH| = 0.2."""

import numpy as np
import matplotlib.pyplot as plt

d = np.linspace(-2, 2, 401)
fig, ax = plt.subplots(figsize=(7, 4.4))
for lg, col in zip([4, 5, 6, 7, 8, 10], ["C0", "C1", "C2", "C3", "C4", "C5"]):
    et = (10.0 ** d - 10.0 ** -d) / np.sqrt(10.0 ** lg) * 100
    ax.plot(d, np.abs(et), color=col, lw=1.6, label=rf"$c_{{sp}}K_t = 10^{{{lg}}}$")
ax.axhline(0.1, color="0.4", ls="--", lw=1)
ax.text(-1.95, 0.12, "|E$_t$| = 0.1 %", fontsize=8.5, color="0.4")
for x in (-0.2, 0.2):
    ax.axvline(x, color="0.4", ls=":", lw=1)
ax.set_yscale("log")
ax.set_ylim(1e-3, 1e2)
ax.set_xlim(-2, 2)
ax.set_xlabel(r"$\Delta$pH = pH$_{ep}$ $-$ pH$_{sp}$")
ax.set_ylabel(r"|end-point error| / %")
ax.legend(frameon=False, fontsize=8, loc="lower right", ncol=2)
fig.tight_layout()
