import numpy as np
import matplotlib.pyplot as plt

METAL = "#d97706"
DONOR = "#2563eb"
BOND = "#94a3b8"
EDGE = "#64748b"
CHELATE = "#dc2626"

X, Y, Z = np.eye(3)
# Three chelate edges related by the C3 axis along (1, 1, 1); this set is the right-handed (Delta) isomer.
DELTA = [(X, -Y), (Y, -Z), (Z, -X)]
MIRROR = np.diag([-1.0, 1.0, 1.0])  # reflection through the yz plane


def draw(ax, chelates, title, azim):
    donors = [p for pair in chelates for p in pair]
    for i, p in enumerate(donors):
        for q in donors[i + 1:]:
            if abs(np.linalg.norm(p - q) - np.sqrt(2)) < 1e-6:
                ax.plot(*zip(p, q), color=EDGE, lw=0.8, ls=":")
    for p in donors:
        ax.plot([0, p[0]], [0, p[1]], [0, p[2]], color=BOND, lw=2.5)
    t = np.linspace(0, 1, 40)[:, None]
    for p, q in chelates:
        bulge = 1.45 * (p + q) / 2  # control point pushed outwards: the ethylenediamine bridge
        curve = (1 - t) ** 2 * p + 2 * t * (1 - t) * bulge + t**2 * q
        ax.plot(*curve.T, color=CHELATE, lw=4, solid_capstyle="round")
    d = np.array(donors)
    ax.scatter(*d.T, s=200, color=DONOR, depthshade=False, edgecolors="none")
    ax.scatter([0], [0], [0], s=340, color=METAL, depthshade=False, edgecolors="none")
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_zlim(-1.1, 1.1)
    ax.set_box_aspect((1, 1, 1))
    ax.view_init(elev=30, azim=azim)
    ax.set_axis_off()
    ax.set_title(title, fontsize=14)


fig = plt.figure(figsize=(10, 5.2))
ax1 = fig.add_subplot(1, 2, 1, projection="3d")
draw(ax1, DELTA, r"$\Delta$-[Co(en)$_3$]$^{3+}$", azim=40)
ax2 = fig.add_subplot(1, 2, 2, projection="3d")
draw(ax2, [(MIRROR @ p, MIRROR @ q) for p, q in DELTA], r"$\Lambda$-[Co(en)$_3$]$^{3+}$", azim=140)
fig.add_artist(plt.Line2D([0.5, 0.5], [0.1, 0.88], color=EDGE, lw=1.5, ls="--"))
fig.text(0.5, 0.05, "mirror", ha="center", fontsize=11)
fig.legend(
    handles=[
        plt.Line2D([], [], marker="o", ls="", color=METAL, markersize=11, label="Co"),
        plt.Line2D([], [], marker="o", ls="", color=DONOR, markersize=9, label="N"),
        plt.Line2D([], [], color=CHELATE, lw=4, label="en bridge"),
    ],
    loc="upper center",
    ncol=3,
    frameon=False,
)
fig.subplots_adjust(left=0, right=1, top=0.86, bottom=0.08, wspace=0.05)
