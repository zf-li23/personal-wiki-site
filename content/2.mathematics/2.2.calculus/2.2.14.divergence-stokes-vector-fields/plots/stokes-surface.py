import numpy as np
import matplotlib.pyplot as plt

# The ellipse x^2 + y^2 = R^2, x/a + z/b = 1 bounds a plane patch; upper normal and induced orientation
R, a, b = 1.0, 2.0, 1.2
fig = plt.figure(figsize=(8, 6.8))
ax = fig.add_subplot(projection="3d")

th = np.linspace(0, 2 * np.pi, 80)
h = np.linspace(0, 2.2, 2)
TH, H = np.meshgrid(th, h)
ax.plot_surface(R * np.cos(TH), R * np.sin(TH), H, color="tab:gray", alpha=0.12, linewidth=0)

r = np.linspace(0, R, 20)
RR, TT = np.meshgrid(r, th)
PX, PY = RR * np.cos(TT), RR * np.sin(TT)
ax.plot_surface(PX, PY, b * (1 - PX / a), color="tab:cyan", alpha=0.45, linewidth=0)

cx, cy = R * np.cos(th), R * np.sin(th)
cz = b * (1 - cx / a)
ax.plot(cx, cy, cz, color="tab:red", lw=2.5, label="boundary L (counterclockwise seen from above)")
for t0 in (0.3, 1.9, 3.5, 5.1):
    p = np.array([R * np.cos(t0), R * np.sin(t0), b * (1 - R * np.cos(t0) / a)])
    d = np.array([-np.sin(t0), np.cos(t0), b * np.sin(t0) / a])
    ax.quiver(*p, *(0.45 * d / np.linalg.norm(d)), color="tab:red", linewidth=2, arrow_length_ratio=0.45)

n = np.array([b / a, 0, 1.0])
n = n / np.linalg.norm(n)
for px, py in [(0, 0), (0.5, 0.4), (-0.5, -0.3), (0.3, -0.6), (-0.4, 0.55)]:
    pz = b * (1 - px / a)
    ax.quiver(px, py, pz, *(0.6 * n), color="tab:blue", linewidth=1.5, arrow_length_ratio=0.3)
ax.plot([], [], color="tab:blue", label="upper normal n of the plane patch S")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Stokes: S on the plane x/a + z/b = 1 inside the cylinder x^2 + y^2 = R^2")
ax.legend(loc="upper left", fontsize=9)
ax.view_init(elev=22, azim=-60)
ax.set_box_aspect((1, 1, 1))
fig.tight_layout()
