import matplotlib.pyplot as plt

LEVEL = "#2563eb"
LINK = "#94a3b8"
W = 0.16  # width of one orbital line
GAP = 0.04

# (x centre, energy in Dq, number of degenerate orbitals, label)
columns = {
    "tetrahedral": (0.0, [(1.78, 3, r"$t_2$" "\n" r"$d_{xy}, d_{yz}, d_{xz}$"), (-2.67, 2, r"$e$" "\n" r"$d_{z^2}, d_{x^2-y^2}$")]),
    "spherical": (2.3, [(0.0, 5, "")]),
    "octahedral": (4.0, [(6.0, 2, r"$e_g$" "\n" r"$d_{z^2}, d_{x^2-y^2}$"), (-4.0, 3, r"$t_{2g}$" "\n" r"$d_{xy}, d_{yz}, d_{xz}$")]),
    "square planar": (
        6.0,
        [
            (12.28, 1, r"$d_{x^2-y^2}$"),
            (2.28, 1, r"$d_{xy}$"),
            (-4.28, 1, r"$d_{z^2}$"),
            (-5.14, 2, r"$d_{xz}, d_{yz}$"),
        ],
    ),
}


def level(ax, x, e, n):
    total = n * W + (n - 1) * GAP
    left = x - total / 2
    for i in range(n):
        x0 = left + i * (W + GAP)
        ax.plot([x0, x0 + W], [e, e], color=LEVEL, lw=2.5)
    return x - total / 2, x + total / 2


fig, ax = plt.subplots(figsize=(11, 6.2))
ends = {}
for name, (x, levels) in columns.items():
    ends[name] = []
    for e, n, label in levels:
        l, r = level(ax, x, e, n)
        ends[name].append((l, r, e))
        if label:
            ax.text(r + 0.08, e, label, va="center", fontsize=10)
        ax.text(l - 0.05, e, f"{e:+.2f}" if e else "0", va="center", ha="right", fontsize=8.5)
    ax.text(x, -8.0, name, ha="center", fontsize=11)

sph_l, sph_r, _ = ends["spherical"][0]
for l, r, e in ends["tetrahedral"]:
    ax.plot([r + 1.0, sph_l], [e, 0], color=LINK, lw=0.8, ls="--")
for l, r, e in ends["octahedral"]:
    ax.plot([sph_r, l], [0, e], color=LINK, lw=0.8, ls="--")


def gap(x, lo, hi, text):
    ax.annotate("", xy=(x, hi), xytext=(x, lo), arrowprops=dict(arrowstyle="<->", color=LINK, lw=1))
    ax.text(x + 0.06, (lo + hi) / 2, text, va="center", fontsize=10)


gap(-0.75, -2.67, 1.78, r"$\Delta_t = 4.45\,Dq$")
gap(3.25, -4.0, 6.0, r"$\Delta_o = 10\,Dq$")
gap(5.2, -5.14, 12.28, r"$17.42\,Dq$")

ax.set_xlim(-1.4, 7.5)
ax.set_ylim(-8.6, 13.5)
ax.set_ylabel("orbital energy / Dq")
ax.set_xticks([])
for side in ("top", "right", "bottom"):
    ax.spines[side].set_visible(False)
fig.tight_layout()
