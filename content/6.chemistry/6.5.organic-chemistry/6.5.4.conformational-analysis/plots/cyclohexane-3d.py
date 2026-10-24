"""Chair and boat cyclohexane in 3D, built from ideal geometry (C-C 154 pm, C-H 109 pm, chair
C-C-C 111.4 degrees). Chair: axial H red, equatorial H blue. Boat: obtained by reflecting C4 of
the chair through the plane of C2, C3, C5, C6; the two flagpole H are about 0.18 nm apart."""

import numpy as np
import matplotlib.pyplot as plt

CC, CH = 1.54, 1.09  # Angstrom inside the script; distances are reported in nm
AX, EQ, FLAG = "#dc2626", "#2563eb", "#d97706"


def chair():
    h = 0.255
    r = np.sqrt(CC**2 - 4 * h**2)
    return np.array([[r * np.cos(np.pi / 3 * k), r * np.sin(np.pi / 3 * k), h if k % 2 == 0 else -h] for k in range(6)])


def hydrogens(C):
    """Two H per carbon, in the plane bisecting the C-C-C angle, H-C-H about 107 degrees."""
    out = []
    for i in range(6):
        u1 = C[i - 1] - C[i]
        u2 = C[(i + 1) % 6] - C[i]
        u1, u2 = u1 / np.linalg.norm(u1), u2 / np.linalg.norm(u2)
        b = -(u1 + u2)
        b /= np.linalg.norm(b)
        p = np.cross(u1, u2)
        p /= np.linalg.norm(p)
        a = np.radians(107.0 / 2)
        out.append([C[i] + CH * (b * np.cos(a) + s * p * np.sin(a)) for s in (1, -1)])
    return np.array(out)


def draw(ax, C, H, colours, title):
    ink = plt.rcParams["text.color"]
    for i in range(6):
        j = (i + 1) % 6
        ax.plot(*zip(C[i], C[j]), color=ink, lw=3)
        for k in range(2):
            ax.plot(*zip(C[i], H[i, k]), color=colours[i][k], lw=1.6)
    ax.scatter(*C.T, s=110, color="0.35", depthshade=False)
    ax.scatter(*H.reshape(-1, 3).T, s=30, c=[c for row in colours for c in row], depthshade=False)
    for i in range(6):
        ax.text(*(C[i] * 1.0 + np.array([0, 0, -0.45])), str(i + 1), fontsize=9, ha="center", color=ink)
    ax.set_box_aspect((1, 1, 0.8))
    lim = 2.2
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(-1.6, 1.6)
    ax.view_init(elev=28, azim=-100)
    ax.set_axis_off()
    ax.set_title(title, fontsize=11)


Cc = chair()
Hc = hydrogens(Cc)
cols_c = []
for i in range(6):
    # the H nearly parallel to the ring axis (z) is axial
    row = [AX if abs(Hc[i, k, 2] - Cc[i, 2]) > 0.9 else EQ for k in range(2)]
    cols_c.append(row)

# boat: reflect C4 (index 3) through the plane of C2, C3, C5, C6 (indices 1, 2, 4, 5)
P = Cc[[1, 2, 4, 5]]
n = np.cross(P[1] - P[0], P[3] - P[0])
n /= np.linalg.norm(n)
Cb = Cc.copy()
Cb[3] = Cc[3] - 2 * np.dot(Cc[3] - P[0], n) * n
# rotate the boat so that its four coplanar carbons are horizontal
z = n if n[2] > 0 else -n
x = P[0] - P[1]
x -= np.dot(x, z) * z
x /= np.linalg.norm(x)
Rm = np.array([x, np.cross(z, x), z])
Cb = (Cb - P.mean(axis=0)) @ Rm.T
Hb = hydrogens(Cb)
d_flag, pair = min(((np.linalg.norm(Hb[0, a] - Hb[3, b]), (a, b)) for a in range(2) for b in range(2)))
cols_b = [["0.6", "0.6"] for _ in range(6)]
cols_b[0][pair[0]] = FLAG
cols_b[3][pair[1]] = FLAG

fig = plt.figure(figsize=(10, 4.4))
draw(fig.add_subplot(1, 2, 1, projection="3d"), Cc, Hc, cols_c, "chair: axial (red) and equatorial (blue) H")
draw(fig.add_subplot(1, 2, 2, projection="3d"), Cb, Hb, cols_b, f"boat: flagpole H (orange) {d_flag / 10:.2f} nm apart")
fig.subplots_adjust(left=0, right=1, bottom=0, top=0.92, wspace=0)
