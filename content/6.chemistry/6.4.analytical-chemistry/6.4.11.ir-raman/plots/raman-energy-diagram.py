"""Energy-level picture of infrared absorption, Rayleigh scattering, Stokes and anti-Stokes
Raman scattering (via a virtual state), resonance Raman scattering (excitation inside an
electronic absorption band) and fluorescence."""

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(9.6, 4.8))
v0, v1 = 0.0, 0.6  # vibrational levels of the ground electronic state
S1 = 7.0  # electronic excited state
for y in (v0, v1):
    ax.plot([0, 12.8], [y, y], color="k", lw=1.2)
for y in (S1, S1 + 0.6, S1 + 1.2):
    ax.plot([8.4, 12.8], [y, y], color="k", lw=1.0 if y > S1 else 1.4)
ax.text(-0.1, v0, "v = 0", ha="right", va="center", fontsize=8)
ax.text(-0.1, v1, "v = 1", ha="right", va="center", fontsize=8)
ax.text(12.9, S1 + 0.3, "excited\nelectronic\nstate", va="center", fontsize=8)


def up(x, y0, y1, col, ls="-"):
    ax.annotate("", xy=(x, y1), xytext=(x, y0),
                arrowprops=dict(arrowstyle="-|>", color=col, lw=1.6, ls=ls))


virt = 5.2
for x0 in (2.2, 4.2, 6.2):
    ax.plot([x0 - 0.5, x0 + 0.9], [virt + (0.6 if x0 == 6.2 else 0)] * 2,
            color="0.5", lw=1.0, ls="--")
ax.text(3.9, virt + 1.15, "virtual states", ha="center", fontsize=8, color="0.4")

up(0.8, v0, v1, "C3")
ax.text(0.8, -0.55, "IR\nabsorption", ha="center", va="top", fontsize=8)

up(2.0, v0, virt, "C0")
up(2.5, virt, v0, "C0")
ax.text(2.25, -0.55, "Rayleigh", ha="center", va="top", fontsize=8)

up(4.0, v0, virt, "C0")
up(4.5, virt, v1, "C2")
ax.text(4.25, -0.55, "Stokes", ha="center", va="top", fontsize=8)

up(6.0, v1, virt + 0.6, "C0")
up(6.5, virt + 0.6, v0, "C1")
ax.text(6.25, -0.55, "anti-Stokes", ha="center", va="top", fontsize=8)

up(9.0, v0, S1 + 0.6, "C0")
up(9.5, S1 + 0.6, v1, "C2")
ax.text(9.25, -0.55, "resonance\nRaman", ha="center", va="top", fontsize=8)

up(11.2, v0, S1 + 1.2, "C0")
ax.annotate("", xy=(11.6, S1), xytext=(11.6, S1 + 1.2),
            arrowprops=dict(arrowstyle="-|>", color="0.5", lw=1.0, ls=":"))
up(12.0, S1, v1, "C4")
ax.text(11.6, -0.55, "fluorescence", ha="center", va="top", fontsize=8)

ax.set_xlim(-1.0, 14.2)
ax.set_ylim(-1.6, 8.9)
ax.axis("off")
fig.tight_layout()
