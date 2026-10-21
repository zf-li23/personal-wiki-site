"""Model initial magnetization curve and hysteresis loops of a soft and a hard ferromagnet."""

import numpy as np
import matplotlib.pyplot as plt

mu0 = 4e-7 * np.pi


def branches(H, Bs, Hc, a):
    """Descending and ascending branches of a tanh loop model (B in tesla, H in A/m)."""
    down = Bs * np.tanh((H + Hc) / a) + mu0 * H
    up = Bs * np.tanh((H - Hc) / a) + mu0 * H
    return down, up


fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))

# soft material: narrow loop
H = np.linspace(-400, 400, 2001)
down, up = branches(H, 1.5, 40.0, 60.0)
ax = axes[0]
ax.plot(H, down, color="C0", lw=1.8, label="hysteresis loop")
ax.plot(H, up, color="C0", lw=1.8)
Hi = np.linspace(0, 400, 801)
di, ui = branches(Hi, 1.5, 40.0, 60.0)
# a demagnetized sample starts at the origin and runs between the two branches
ax.plot(Hi, 0.5 * (di + ui) * np.tanh(Hi / 30.0), color="C1", lw=1.4, ls="--", label="initial curve")
Br = 1.5 * np.tanh(40.0 / 60.0)
ax.plot([0], [Br], "o", color="C3", ms=4)
ax.annotate("B_r", (0, Br), (40, Br + 0.25), fontsize=9)
ax.plot([-40], [0], "o", color="C3", ms=4)
ax.annotate("-H_c", (-40, 0), (-150, 0.2), fontsize=9)
ax.set_title("soft material (e.g. silicon steel): narrow loop", fontsize=10)
ax.set_xlabel("H / (A/m)")
ax.set_ylabel("B / T")
ax.legend(fontsize=8, loc="lower right")

# hard material: wide loop
H = np.linspace(-1.2e6, 1.2e6, 2001)
down, up = branches(H, 1.1, 8e5, 1.5e5)
ax = axes[1]
ax.plot(H / 1e3, down, color="C2", lw=1.8)
ax.plot(H / 1e3, up, color="C2", lw=1.8)
ax.set_title("hard material (permanent magnet): wide loop", fontsize=10)
ax.set_xlabel("H / (kA/m)")
ax.set_ylabel("B / T")

for ax in axes:
    ax.axhline(0, color="0.6", lw=0.7)
    ax.axvline(0, color="0.6", lw=0.7)
fig.tight_layout()
