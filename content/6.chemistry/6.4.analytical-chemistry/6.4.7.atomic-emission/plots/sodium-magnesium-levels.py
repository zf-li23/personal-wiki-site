"""Simplified Grotrian diagrams of Na I and Mg I (energies in eV above the ground state,
NIST Atomic Spectra Database) with the main emission lines (air wavelengths in nm).
Fine structure of the Na 3p and Mg 3s3p 3P levels is exaggerated for visibility."""

import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(11, 5.6))


def level(ax, x, E, label, w=0.32):
    ax.plot([x - w, x + w], [E, E], color="k", lw=1.4)
    ax.text(x + w + 0.05, E, label, va="center", fontsize=8.5)


def line(ax, x1, E1, x2, E2, txt, col, dx=0.0, ls="-", at=0.5, off=(0.05, 0.0), ha="left"):
    ax.annotate("", xy=(x2 + dx, E2), xytext=(x1 + dx, E1),
                arrowprops=dict(arrowstyle="->", color=col, lw=1.3, ls=ls))
    xt = x1 + (x2 - x1) * at + dx + off[0]
    yt = E1 + (E2 - E1) * at + off[1]
    ax.text(xt, yt, txt, color=col, fontsize=8, ha=ha, va="center")


# sodium: columns S, P, D
ax = axes[0]
xs, xp, xd = 0, 1.6, 3.2
level(ax, xs, 0.0, r"$3\,^2\mathrm{S}_{1/2}$")
level(ax, xs, 3.191, "4s")
level(ax, xs, 4.116, "5s")
level(ax, xp, 2.102, r"$3\,^2\mathrm{P}_{1/2}$")
level(ax, xp, 2.30, r"$3\,^2\mathrm{P}_{3/2}$")
level(ax, xp, 3.753, "4p")
level(ax, xd, 3.617, "3d")
level(ax, xd, 4.284, "4d")
ax.axhline(5.139, color="0.5", lw=0.8, ls="--")
ax.text(3.6, 5.2, "ionization 5.14 eV", fontsize=8.5, color="0.4")
line(ax, xp - 0.25, 2.102, xs + 0.05, 0.0, "589.59 (D1)", "C1", at=0.5, off=(0.55, -0.3))
line(ax, xp + 0.1, 2.30, xs + 0.3, 0.0, "588.99 (D2)", "C3", at=0.45, off=(0.08, 0))
line(ax, xp - 0.3, 3.753, xs - 0.2, 0.0, "330.2", "C4", at=0.35, off=(-0.06, 0), ha="right")
line(ax, xd - 0.2, 3.617, xp + 0.2, 2.25, "818.3 / 819.5", "C0")
line(ax, xs + 0.2, 3.191, xp - 0.25, 2.2, "1138 / 1140", "C2")
ax.set_xlim(-0.8, 4.6)
ax.set_ylim(-0.3, 5.6)
ax.set_xticks([xs, xp, xd], ["S", "P", "D"])
ax.set_ylabel("energy / eV")
ax.set_title("Na I", fontsize=11)

# magnesium: singlets on the left, triplets on the right
ax = axes[1]
x1s, x1p, x1d, x3s, x3p, x3d = 0, 1.1, 2.2, 3.5, 4.6, 5.7
level(ax, x1s, 0.0, r"$3\,^1\mathrm{S}_0$", w=0.28)
level(ax, x1s, 5.394, r"4s $^1\mathrm{S}_0$", w=0.28)
level(ax, x1p, 4.346, r"3p $^1\mathrm{P}_1$", w=0.28)
level(ax, x1d, 5.753, r"3d $^1\mathrm{D}_2$", w=0.28)
level(ax, x3s, 5.108, r"4s $^3\mathrm{S}_1$", w=0.28)
for E in (2.62, 2.71, 2.80):
    level(ax, x3p, E, "", w=0.28)
ax.text(x3p + 0.33, 2.45, r"3p $^3\mathrm{P}_{0,1,2}$", fontsize=8.5, va="center")
level(ax, x3d, 5.946, r"3d $^3\mathrm{D}$", w=0.28)
ax.axhline(7.646, color="0.5", lw=0.8, ls="--")
ax.text(4.2, 7.75, "ionization 7.65 eV", fontsize=8.5, color="0.4")
line(ax, x1p, 4.346, x1s + 0.1, 0.0, "285.21 (resonance)", "C3")
line(ax, x3p - 0.2, 2.71, x1s + 0.25, 0.05, "457.1 (intercombination)", "C7", ls="--")
line(ax, x3s + 0.1, 5.108, x3p - 0.1, 2.85, "516.7 / 517.3 / 518.4", "C2")
line(ax, x3d - 0.1, 5.946, x3p + 0.15, 2.85, "383.8", "C4")
ax.set_xlim(-0.6, 6.8)
ax.set_ylim(-0.3, 8.1)
ax.set_xticks([x1s, x1p, x1d, x3s, x3p, x3d], ["S", "P", "D", "S", "P", "D"])
ax.text(1.1, -1.0, "singlets", ha="center", fontsize=9)
ax.text(4.6, -1.0, "triplets", ha="center", fontsize=9)
ax.set_title("Mg I", fontsize=11)
fig.tight_layout()
