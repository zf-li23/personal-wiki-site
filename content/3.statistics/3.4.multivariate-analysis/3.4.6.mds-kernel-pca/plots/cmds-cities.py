"""Classical MDS of road distances (km) between eight cities in eastern China."""

import numpy as np
import matplotlib.pyplot as plt

names = ["Beijing", "Tianjin", "Jinan", "Qingdao", "Zhengzhou", "Shanghai", "Hangzhou", "Nanjing"]
lower = [[0], [118, 0], [439, 363, 0], [668, 571, 362, 0], [714, 729, 443, 772, 0],
         [1259, 1145, 886, 776, 984, 0], [1328, 1191, 872, 828, 962, 203, 0],
         [1065, 936, 626, 617, 710, 322, 305, 0]]
n = len(names)
D = np.zeros((n, n))
for i, row in enumerate(lower):
    for j, v in enumerate(row):
        D[i, j] = D[j, i] = v

H = np.eye(n) - np.ones((n, n)) / n
B = H @ (-0.5 * D**2) @ H
lam, P = np.linalg.eigh(B)
order = np.argsort(lam)[::-1]
lam, P = lam[order], P[:, order]
Z = P[:, :2] * np.sqrt(lam[:2])
# CMDS determines the configuration only up to an orthogonal transformation; choose the one
# (rotation and/or reflection) that best matches approximate map positions (longitude, latitude)
lonlat = np.array([[116.4, 39.9], [117.2, 39.1], [117.0, 36.7], [120.4, 36.1], [113.6, 34.7],
                   [121.5, 31.2], [120.2, 30.3], [118.8, 32.1]])
T = (lonlat - lonlat.mean(0)) * np.array([111 * np.cos(np.radians(35)), 111])
U, _, Vt = np.linalg.svd(Z.T @ T)
Z = Z @ (U @ Vt)

fig, axes = plt.subplots(1, 2, figsize=(12, 4.8), gridspec_kw={"width_ratios": [1, 1.4]})
ax = axes[0]
ax.bar(np.arange(1, n + 1), lam / 1e3, color=["C0" if v > 0 else "C3" for v in lam])
ax.axhline(0, color="gray", lw=0.8)
ax.set_xlabel("index i")
ax.set_ylabel("eigenvalue of B (1000 km^2)")
ax.set_title("eigenvalues of B")
ax.grid(alpha=0.3)

ax = axes[1]
ax.scatter(Z[:, 0], Z[:, 1], color="C0", zorder=3)
for (x, y), name in zip(Z, names):
    offset = (5, -12) if name == "Hangzhou" else (5, 5)
    ax.annotate(name, (x, y), textcoords="offset points", xytext=offset, fontsize=9)
ax.set_aspect("equal")
ax.set_xlabel("coordinate 1 (km)")
ax.set_ylabel("coordinate 2 (km)")
ax.set_title("two-dimensional CMDS configuration (oriented)")
ax.margins(0.15)
ax.grid(alpha=0.3)
fig.tight_layout()
