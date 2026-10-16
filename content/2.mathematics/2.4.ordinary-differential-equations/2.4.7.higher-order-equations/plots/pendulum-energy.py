"""Energy level curves of the pendulum theta'' + sin(theta) = 0 in the phase plane."""

import numpy as np
import matplotlib.pyplot as plt

th = np.linspace(-2 * np.pi, 2 * np.pi, 600)
om = np.linspace(-3, 3, 400)
TH, OM = np.meshgrid(th, om)
E = OM ** 2 / 2 - np.cos(TH)

fig, ax = plt.subplots(figsize=(7.5, 4.6))
ax.contour(TH, OM, E, levels=[-0.9, -0.6, -0.2, 0.3, 0.7], colors="C0", linewidths=1.2)
ax.contour(TH, OM, E, levels=[1.4, 2.0, 3.0], colors="C2", linewidths=1.2)
ax.contour(TH, OM, E, levels=[1.0], colors="C3", linewidths=2.2)
ax.plot([-np.pi, np.pi], [0, 0], "o", color="C3", ms=5)
ax.plot([-2 * np.pi, 0, 2 * np.pi], [0, 0, 0], "o", color="C0", ms=5)
ax.plot([], [], color="C0", label="oscillation (E < 1)")
ax.plot([], [], color="C3", lw=2.2, label="separatrix (E = 1)")
ax.plot([], [], color="C2", label="rotation (E > 1)")
ax.set_xticks(np.pi * np.arange(-2, 3))
ax.set_xticklabels(["-2 pi", "-pi", "0", "pi", "2 pi"])
ax.set_xlabel("theta")
ax.set_ylabel("theta'")
ax.set_title("Pendulum: level curves of (theta')^2/2 - cos(theta)")
ax.legend(loc="upper right", fontsize=8)
fig.tight_layout()
