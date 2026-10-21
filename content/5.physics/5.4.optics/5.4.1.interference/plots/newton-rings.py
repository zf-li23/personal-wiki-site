"""Newton's rings in reflected light: air gap e = r^2 / (2R), path difference 2e + lambda/2."""

import numpy as np
import matplotlib.pyplot as plt

R = 1.0            # radius of curvature, m
lam = 589.3e-9     # sodium light, m

def intensity(r):
    e = r ** 2 / (2 * R)
    delta = 2 * e + lam / 2
    return 0.5 * (1 + np.cos(2 * np.pi * delta / lam))

rmax = 2.5e-3
x = np.linspace(-rmax, rmax, 700)
X, Y = np.meshgrid(x, x)
img = intensity(np.hypot(X, Y))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.0, 4.4),
                               gridspec_kw={"width_ratios": [1, 1.5]})
ax1.imshow(img, extent=[-rmax * 1e3, rmax * 1e3, -rmax * 1e3, rmax * 1e3],
           cmap="gray", origin="lower", vmin=0, vmax=1)
ax1.set_xlabel("x / mm")
ax1.set_ylabel("y / mm")
ax1.set_title("reflected light, R = 1 m, λ = 589.3 nm", fontsize=9)

r = np.linspace(0, rmax, 3000)
ax2.plot(r * 1e3, intensity(r), color="C0", lw=1.0)
for k in range(1, 6):
    rk = np.sqrt(k * R * lam)
    ax2.plot([rk * 1e3], [0.0], "v", color="C3", ms=5)
ax2.text(0.05, 1.12, "dark rings (triangles): r_k = sqrt(kRλ), k = 0, 1, 2, ...", color="C3", fontsize=8)
ax2.set_xlabel("r / mm")
ax2.set_ylabel("I / I_max")
ax2.set_xlim(0, rmax * 1e3)
ax2.set_ylim(-0.03, 1.25)
fig.tight_layout()
