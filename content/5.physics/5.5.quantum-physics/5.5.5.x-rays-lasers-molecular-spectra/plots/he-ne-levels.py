"""Energy levels of helium and neon relevant to the He-Ne laser."""

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8.5, 5.2))


def level(x0, E, label, w=0.8, side="left"):
    ax.plot([x0, x0 + w], [E, E], color="k", lw=2)
    if side == "left":
        ax.text(x0 - 0.06, E, label, ha="right", va="center", fontsize=9)
    else:
        ax.text(x0 + w + 0.06, E, label, ha="left", va="center", fontsize=9)


# Helium (column at x = 0.5) and neon (column at x = 2.4)
level(0.5, 20.62, r"$2\,^1\mathrm{S}_0$  20.62 eV")
level(0.5, 19.82, r"$2\,^3\mathrm{S}_1$  19.82 eV")
level(2.4, 20.66, "5s  20.66 eV", w=1.0, side="right")
level(2.4, 19.78, "4s  19.78 eV", w=1.0, side="right")
level(3.0, 20.30, "4p  20.30 eV", w=1.0, side="right")
level(3.0, 18.70, "3p  18.70 eV", w=1.0, side="right")
level(2.7, 16.70, "3s  16.70 eV", w=1.0, side="right")
# ground states drawn on a broken axis at the bottom
level(0.5, 15.6, r"$1\,^1\mathrm{S}_0$  0 eV")
level(2.4, 15.6, "ground 0 eV", w=1.6, side="right")
ax.text(1.55, 15.95, "(axis broken)", ha="center", fontsize=8, color="0.4")

arrow = dict(arrowstyle="->", lw=1.4)
# electron-impact excitation of He
ax.annotate("", xy=(0.75, 20.55), xytext=(0.75, 15.65), arrowprops=dict(arrowstyle="->", lw=1.2, ls="--", color="0.4"))
ax.annotate("", xy=(1.05, 19.75), xytext=(1.05, 15.65), arrowprops=dict(arrowstyle="->", lw=1.2, ls="--", color="0.4"))
ax.text(0.62, 17.6, "electron\nimpact", fontsize=8, color="0.4", ha="right")
# resonant energy transfer He -> Ne
ax.annotate("", xy=(2.38, 20.66), xytext=(1.32, 20.62), arrowprops=dict(arrowstyle="->", lw=1.2, color="C2"))
ax.annotate("", xy=(2.38, 19.78), xytext=(1.32, 19.82), arrowprops=dict(arrowstyle="->", lw=1.2, color="C2"))
ax.text(1.85, 20.82, "collisional transfer", fontsize=8, color="C2", ha="center")
# laser transitions
ax.annotate("", xy=(3.1, 18.72), xytext=(2.6, 20.64), arrowprops=dict(arrowstyle="->", lw=2, color="C3"))
ax.text(2.58, 19.35, "632.8 nm", color="C3", fontsize=9, ha="right")
ax.annotate("", xy=(3.35, 18.72), xytext=(3.25, 19.76), arrowprops=dict(arrowstyle="->", lw=2, color="C1"))
ax.text(3.42, 19.05, r"1.15 $\mu$m", color="C1", fontsize=9)
ax.annotate("", xy=(3.15, 20.31), xytext=(2.9, 20.64), arrowprops=dict(arrowstyle="->", lw=2, color="C4"))
ax.text(2.9, 20.95, r"3.39 $\mu$m", color="C4", fontsize=9)
# fast decays
ax.annotate("", xy=(3.2, 16.72), xytext=(3.3, 18.68), arrowprops=dict(arrowstyle="->", lw=1.2, color="0.4"))
ax.text(3.0, 17.6, "spontaneous\n(fast)", fontsize=8, color="0.4", ha="right")
ax.annotate("", xy=(3.4, 15.65), xytext=(3.4, 16.66), arrowprops=dict(arrowstyle="->", lw=1.2, ls=":", color="0.4"))
ax.text(3.48, 16.1, "wall collisions", fontsize=8, color="0.4")

ax.text(0.9, 21.4, "He", fontsize=12, ha="center")
ax.text(2.9, 21.4, "Ne", fontsize=12, ha="center")
ax.set_xlim(-0.9, 4.9)
ax.set_ylim(15.2, 21.7)
ax.set_xticks([])
ax.set_ylabel("energy / eV")
ax.set_yticks([16, 17, 18, 19, 20, 21])
for s in ["top", "right", "bottom"]:
    ax.spines[s].set_visible(False)
fig.tight_layout()
