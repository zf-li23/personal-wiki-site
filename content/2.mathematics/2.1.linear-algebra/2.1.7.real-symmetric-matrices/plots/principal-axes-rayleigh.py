import numpy as np
import matplotlib.pyplot as plt

# Quadratic form q(x) = 5 x1^2 + 4 x1 x2 + 5 x2^2 with matrix A = [[5, 2], [2, 5]]
A = np.array([[5.0, 2.0], [2.0, 5.0]])
lam, Q = np.linalg.eigh(A)          # ascending: 3, 7
lam, Q = lam[::-1], Q[:, ::-1]      # descending: 7, 3
if Q[0, 0] < 0:
    Q[:, 0] *= -1
if Q[1, 1] < 0:
    Q[:, 1] *= -1

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Left: level curves q(x) = c are ellipses whose axes are the eigenvectors
t = np.linspace(-0.75, 0.75, 401)
X1, X2 = np.meshgrid(t, t)
Z = 5 * X1**2 + 4 * X1 * X2 + 5 * X2**2
cs = ax1.contour(X1, X2, Z, levels=[0.25, 0.5, 1.0, 1.5, 2.0], cmap="viridis")
ax1.clabel(cs, fmt="%.2g", fontsize=8)
colors = ["tab:red", "tab:blue"]
for i in range(2):
    q = Q[:, i]
    half = 1 / np.sqrt(lam[i])      # semi-axis of q(x) = 1 along q_i
    ax1.plot([-0.75 * q[0], 0.75 * q[0]], [-0.75 * q[1], 0.75 * q[1]],
             ls="--", color=colors[i], lw=1)
    ax1.annotate("", xy=half * q, xytext=(0, 0),
                 arrowprops=dict(arrowstyle="->", color=colors[i], lw=2))
    offset = np.array([0.04, -0.06]) if i == 0 else np.array([-0.33, 0.04])
    ax1.text(*(half * q + offset), f"q{i + 1}/sqrt({lam[i]:.0f})", color=colors[i], fontsize=11)
ax1.axhline(0, color="gray", lw=0.6)
ax1.axvline(0, color="gray", lw=0.6)
ax1.set_aspect("equal")
ax1.set_xlabel("x1")
ax1.set_ylabel("x2")
ax1.set_title("Level curves of 5x1^2 + 4x1x2 + 5x2^2 and principal axes")

# Right: Rayleigh quotient along the unit circle x = (cos t, sin t)
theta = np.linspace(0, np.pi, 721)
R = 5 + 4 * np.cos(theta) * np.sin(theta)
ax2.plot(np.degrees(theta), R, color="tab:purple", lw=2, label="R(x) = x^T A x / x^T x")
ax2.axhline(lam[0], color="tab:red", ls="--", lw=1, label="lambda1 = 7 (max, at q1)")
ax2.axhline(lam[1], color="tab:blue", ls="--", lw=1, label="lambda2 = 3 (min, at q2)")
ax2.plot([45], [7], "o", color="tab:red", ms=8)
ax2.plot([135], [3], "o", color="tab:blue", ms=8)
ax2.set_xticks([0, 45, 90, 135, 180])
ax2.set_xlabel("direction angle of x (degrees)")
ax2.set_ylabel("Rayleigh quotient")
ax2.set_ylim(2, 8)
ax2.grid(True, alpha=0.3)
ax2.legend(loc="lower left")
ax2.set_title("Rayleigh quotient: extreme values are eigenvalues")
fig.tight_layout()
