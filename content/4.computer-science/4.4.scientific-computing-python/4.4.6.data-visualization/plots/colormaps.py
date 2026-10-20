"""Rainbow versus perceptually uniform colormaps: the same field and the lightness of each map."""

import numpy as np
import matplotlib.pyplot as plt


def srgb_to_lightness(rgb):
    """CIE L* (0-100) of sRGB colors with components in [0, 1]."""
    c = np.where(rgb <= 0.04045, rgb / 12.92, ((rgb + 0.055) / 1.055) ** 2.4)
    y = c @ np.array([0.2126, 0.7152, 0.0722])
    f = np.where(y > (6 / 29) ** 3, np.cbrt(y), y / (3 * (6 / 29) ** 2) + 4 / 29)
    return 116 * f - 16


# A smooth field: one broad peak, a weaker shoulder and a linear trend.
x, y = np.meshgrid(np.linspace(-3, 3, 300), np.linspace(-2, 2, 200))
field = (np.exp(-((x - 0.8) ** 2 + y**2)) + 0.5 * np.exp(-((x + 1.5) ** 2 + (y - 0.6) ** 2) / 0.6)
         + 0.08 * x)

maps = ["jet", "viridis", "cividis"]
fig, axes = plt.subplots(2, 3, figsize=(10, 5), height_ratios=[1.3, 1], layout="constrained")
s = np.linspace(0, 1, 256)
for j, name in enumerate(maps):
    cmap = plt.get_cmap(name)
    ax = axes[0, j]
    ax.imshow(field, cmap=cmap, origin="lower", extent=(-3, 3, -2, 2))
    ax.set_title(name, fontsize=11)
    ax.set_xticks([])
    ax.set_yticks([])

    ax = axes[1, j]
    lightness = srgb_to_lightness(cmap(s)[:, :3])
    ax.scatter(s, lightness, c=s, cmap=cmap, s=8)
    ax.set_ylim(0, 100)
    ax.set_xlabel("Position in colormap")
    if j == 0:
        ax.set_ylabel("Lightness $L^*$")
    ax.spines[["top", "right"]].set_visible(False)
