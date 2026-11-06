# 14C pulse labelling of phloem translocation, simulated with a 1-D advection-dispersion model.
# A short pulse of label enters the stem at x = 0; it moves with the bulk-flow velocity u, spreads with an
# effective longitudinal dispersion coefficient Dl and is lost to surrounding tissues at rate k:
# c(x, t) = M / sqrt(4 pi Dl t) * exp(-(x - u t)^2 / (4 Dl t)) * exp(-k t).
# Counts at detectors 0.10 m and 0.30 m from the source; the velocity is estimated from the peak times.
import matplotlib.pyplot as plt
import numpy as np

u = 0.8 / 3600      # m s^-1
Dl = 2e-6           # m^2 s^-1
k = 0.3 / 3600      # s^-1
t = np.linspace(1, 3 * 3600, 4000)


def conc(x):
    return 1 / np.sqrt(4 * np.pi * Dl * t) * np.exp(-(x - u * t) ** 2 / (4 * Dl * t)) * np.exp(-k * t)


fig, ax = plt.subplots(figsize=(8.2, 4.2))
peaks = []
for x, col in ((0.10, "#2f6fb5"), (0.30, "#c0504d")):
    c = conc(x)
    c = c / conc(0.10).max()
    ax.plot(t / 60, c, color=col, lw=2.2, label=f"detector at {x * 100:.0f} cm")
    i = np.argmax(c)
    peaks.append(t[i])
    ax.plot(t[i] / 60, c[i], "o", color=col, ms=5)
    ax.axvline(t[i] / 60, color=col, lw=0.7, ls=":")
dt = (peaks[1] - peaks[0]) / 3600
ax.annotate("", xy=(peaks[1] / 60, 0.55), xytext=(peaks[0] / 60, 0.55),
            arrowprops=dict(arrowstyle="<->", color="0.4", lw=1))
ax.text(peaks[1] / 60 + 1.5, 0.72, f"Δt = {dt * 60:.0f} min  →  u ≈ 0.20 m / {dt:.2f} h = {0.2 / dt:.2f} m/h",
        ha="left", fontsize=9)
ax.set_xlabel("Time after pulse / min")
ax.set_ylabel("Counts (relative)")
ax.set_xlim(0, 50)
ax.set_ylim(0, 1.15)
ax.legend(frameon=False, fontsize=9)
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
