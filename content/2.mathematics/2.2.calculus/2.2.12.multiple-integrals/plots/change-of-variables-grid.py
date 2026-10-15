import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(15, 4.8))

# Panel 1: a grid in the (u, v) or (r, theta) parameter plane
ax = axes[0]
for t in np.linspace(0, 1, 9):
    ax.plot([t, t], [0, 1], color="tab:blue", lw=0.8)
    ax.plot([0, 1], [t, t], color="tab:orange", lw=0.8)
ax.add_patch(plt.Rectangle((0.5, 0.5), 0.125, 0.125, color="tab:red", alpha=0.5))
ax.set_aspect("equal")
ax.set_title("Parameter plane: a square grid")
ax.set_xlabel("first coordinate (r or u)")
ax.set_ylabel("second coordinate (theta or v)")

# Panel 2: polar coordinates, r in [0.5, 2], theta in [0, pi/2]
ax = axes[1]
R = np.linspace(0.5, 2, 9)
T = np.linspace(0, np.pi / 2, 9)
tt = np.linspace(0, np.pi / 2, 100)
rr = np.linspace(0.5, 2, 100)
for r in R:
    ax.plot(r * np.cos(tt), r * np.sin(tt), color="tab:blue", lw=0.8)
for t in T:
    ax.plot(rr * np.cos(t), rr * np.sin(t), color="tab:orange", lw=0.8)
r0, r1, t0, t1 = R[4], R[5], T[4], T[5]
a = np.concatenate([np.linspace(t0, t1, 30), np.linspace(t1, t0, 30)])
b = np.concatenate([np.full(30, r0), np.full(30, r1)])
ax.fill(b * np.cos(a), b * np.sin(a), color="tab:red", alpha=0.5)
for r in [R[1], R[7]]:
    a = np.concatenate([np.linspace(T[6], T[7], 30), np.linspace(T[7], T[6], 30)])
    b = np.concatenate([np.full(30, r), np.full(30, r + (R[1] - R[0]))])
    ax.fill(b * np.cos(a), b * np.sin(a), color="tab:green", alpha=0.5)
ax.set_aspect("equal")
ax.set_title("x = r cos(theta), y = r sin(theta)\ncells grow like r: dx dy = r dr dtheta")
ax.set_xlabel("x")
ax.set_ylabel("y")

# Panel 3: x = u^(-2/5) v^(1/5), y = u^(-1/5) v^(3/5), u in [1, 2], v in [1, 2]
ax = axes[2]
s = np.linspace(1, 2, 100)
for c in np.linspace(1, 2, 9):
    ax.plot(c ** (-0.4) * s ** 0.2, c ** (-0.2) * s ** 0.6, color="tab:blue", lw=0.8)
    ax.plot(s ** (-0.4) * c ** 0.2, s ** (-0.2) * c ** 0.6, color="tab:orange", lw=0.8)
u0, u1, v0, v1 = 1.5, 1.625, 1.5, 1.625
uu = np.concatenate([np.linspace(u0, u1, 20), np.full(20, u1), np.linspace(u1, u0, 20), np.full(20, u0)])
vv = np.concatenate([np.full(20, v0), np.linspace(v0, v1, 20), np.full(20, v1), np.linspace(v1, v0, 20)])
ax.fill(uu ** (-0.4) * vv ** 0.2, uu ** (-0.2) * vv ** 0.6, color="tab:red", alpha=0.5)
ax.set_aspect("equal")
ax.set_title("u = y/x^3 (blue: u const), v = y^2/x (orange)")
ax.set_xlabel("x")
ax.set_ylabel("y")
fig.tight_layout()
