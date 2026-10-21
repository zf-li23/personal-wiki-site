"""Lorentz factor and relativistic versus Newtonian kinetic energy."""

import numpy as np
import matplotlib.pyplot as plt

b = np.linspace(0, 0.995, 800)
g = 1 / np.sqrt(1 - b ** 2)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.0))

ax1.plot(b, g, color="C0", lw=1.8)
ax1.axvline(1, color="0.5", ls="--", lw=1.0)
for bb in [0.6, 0.8, 0.99]:
    gg = 1 / np.sqrt(1 - bb ** 2)
    if gg < 8:
        ax1.plot([bb], [gg], "o", color="C3", ms=4)
        ax1.annotate(f"β = {bb}, γ = {gg:.3g}", (bb, gg), xytext=(-110, 10), textcoords="offset points", fontsize=8)
ax1.set_ylim(0.8, 8)
ax1.set_xlim(0, 1.02)
ax1.set_xlabel("β = v / c")
ax1.set_ylabel("γ")
ax1.set_title("Lorentz factor γ = 1/√(1 - β²)")

ax2.plot(b, g - 1, color="C0", lw=1.8, label="relativistic (γ - 1)mc²")
ax2.plot(b, 0.5 * b ** 2, color="C1", lw=1.8, ls="--", label="Newtonian mv²/2")
ax2.axvline(1, color="0.5", ls="--", lw=1.0)
ax2.set_ylim(0, 4)
ax2.set_xlim(0, 1.02)
ax2.set_xlabel("β = v / c")
ax2.set_ylabel("E_k / (mc²)")
ax2.set_title("Kinetic energy")
ax2.legend(loc="upper left", fontsize=9)

fig.tight_layout()
