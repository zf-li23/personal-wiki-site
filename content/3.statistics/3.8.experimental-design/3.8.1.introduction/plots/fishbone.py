"""Cause-and-effect diagram for a CNC turbine blade experiment, by role in the design."""

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(9.5, 5.2))
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.axis("off")

# Spine and head
ax.annotate("", xy=(10.0, 4.0), xytext=(0.5, 4.0),
            arrowprops=dict(arrowstyle="-|>", lw=2.2, color="black", mutation_scale=20))
ax.text(10.1, 4.0, "Blade profile,\nsurface finish,\ndefects", va="center", ha="left", fontsize=10)

branches = [
    # (x on spine, top?, title, causes)
    (4.5, True, "Uncontrollable\nfactors", ["Spindle differences", "Ambient temperature", "Titanium properties"]),
    (8.2, True, "Controllable design\nfactors", ["x-axis shift", "y-axis shift", "z-axis shift",
                                                "Spindle speed", "Fixture height", "Feed rate"]),
    (4.5, False, "Nuisance (blocking)\nfactors", ["Operators", "Tool vendor"]),
    (8.2, False, "Held-constant\nfactors", ["Viscosity of cutting fluid", "Temperature of cutting fluid"]),
]
colors = ["C3", "C0", "C1", "C2"]
for (x, top, title, causes), c in zip(branches, colors):
    sign = 1 if top else -1
    x_end, y_end = x - 1.9, 4.0 + sign * 3.4
    ax.plot([x, x_end], [4.0, y_end], color=c, lw=2)
    ax.text(x_end, y_end + sign * 0.15, title, ha="center", va="bottom" if top else "top",
            fontsize=10, color=c, fontweight="bold")
    k = len(causes)
    for i, cause in enumerate(causes):
        t = (i + 1) / (k + 1)
        xb = x + t * (x_end - x)
        yb = 4.0 + t * (y_end - 4.0)
        ax.plot([xb, xb + 0.35], [yb, yb], color=c, lw=1)
        ax.text(xb + 0.4, yb, cause, va="center", ha="left", fontsize=8.5)
fig.tight_layout()
