import numpy as np
import matplotlib.pyplot as plt

# Region 0 <= y <= 1, y^2/2 <= x <= sqrt(3 - y^2)  (Example 12.2.3)
y = np.linspace(0, 1, 200)
left = y**2 / 2
right = np.sqrt(3 - y**2)

fig, axes = plt.subplots(1, 2, figsize=(12, 4.6), sharey=True)
for ax in axes:
    ax.fill_betweenx(y, left, right, color="tab:blue", alpha=0.18)
    ax.plot(left, y, color="tab:blue", lw=2, label="y^2 = 2x")
    ax.plot(right, y, color="tab:red", lw=2, label="x^2 + y^2 = 3")
    ax.plot([0.5, np.sqrt(2)], [1, 1], color="tab:green", lw=2, label="y = 1")
    ax.plot([0, np.sqrt(3)], [0, 0], color="gray", lw=1)
    ax.set_xlim(-0.1, 1.9)
    ax.set_ylim(-0.1, 1.25)
    ax.set_aspect("equal")
    ax.set_xlabel("x")

ax = axes[0]
for yy in np.linspace(0.05, 0.95, 10):
    ax.plot([yy**2 / 2, np.sqrt(3 - yy**2)], [yy, yy], color="tab:purple", lw=1.2)
ax.set_ylabel("y")
ax.set_title("Horizontal strips: x from y^2/2 to sqrt(3 - y^2)")
ax.legend(loc="upper right", fontsize=8)

ax = axes[1]
xs = np.linspace(0.04, np.sqrt(3) - 0.03, 22)
for xx in xs:
    top = np.sqrt(2 * xx) if xx <= 0.5 else (1.0 if xx <= np.sqrt(2) else np.sqrt(3 - xx**2))
    ax.plot([xx, xx], [0, top], color="tab:purple", lw=1.2)
for xb in [0.5, np.sqrt(2)]:
    ax.axvline(xb, color="k", ls="--", lw=1)
ax.text(0.12, 1.12, "piece 1", fontsize=9)
ax.text(0.8, 1.12, "piece 2", fontsize=9)
ax.text(1.47, 1.12, "piece 3", fontsize=9)
ax.set_title("Vertical strips: the upper boundary changes twice")
fig.tight_layout()
