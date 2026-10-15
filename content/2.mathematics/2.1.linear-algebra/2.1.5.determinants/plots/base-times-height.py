import numpy as np
import matplotlib.pyplot as plt

a1 = np.array([3.0, 1.0])
a2 = np.array([1.0, 2.0])
# Gram-Schmidt: q2t is the part of a2 orthogonal to a1, i.e. the height of the parallelogram
q2t = a2 - (a1 @ a2) / (a1 @ a1) * a1
foot = a2 - q2t
det = a1[0] * a2[1] - a1[1] * a2[0]

para = np.array([[0, 0], a1, a1 + a2, a2, [0, 0]])
rect = np.array([[0, 0], a1, a1 + q2t, q2t, [0, 0]])

fig, ax = plt.subplots(figsize=(7, 4.5))
ax.fill(para[:, 0], para[:, 1], color="C0", alpha=0.25, label="parallelogram spanned by $\\boldsymbol{a}_1, \\boldsymbol{a}_2$")
ax.plot(para[:, 0], para[:, 1], color="C0", lw=1.5)
ax.fill(rect[:, 0], rect[:, 1], color="C1", alpha=0.25, label="rectangle with the same base and height")
ax.plot(rect[:, 0], rect[:, 1], color="C1", lw=1.5, ls="--")
for vec, color, label in [(a1, "C0", r"$\boldsymbol{a}_1$"), (a2, "C0", r"$\boldsymbol{a}_2$")]:
    ax.annotate("", xy=vec, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=color, lw=2, mutation_scale=14))
    ax.text(vec[0] + 0.06, vec[1] + 0.06, label, color=color, fontsize=12)
ax.annotate("", xy=a2, xytext=foot, arrowprops=dict(arrowstyle="-|>", color="C3", lw=2, mutation_scale=14))
ax.text(*((a2 + foot) / 2 + np.array([0.08, -0.15])), r"$\tilde{\boldsymbol{q}}_2$", color="C3", fontsize=12)
u = 0.15 * a1 / np.linalg.norm(a1)
v = 0.15 * q2t / np.linalg.norm(q2t)
corner = np.array([foot + u, foot + u + v, foot + v])
ax.plot(corner[:, 0], corner[:, 1], color="C3", lw=1)
ax.set_title(
    f"$|\\det A| = \\|\\boldsymbol{{a}}_1\\| \\cdot \\|\\tilde{{\\boldsymbol{{q}}}}_2\\|"
    f" = {np.linalg.norm(a1):.3f} \\times {np.linalg.norm(q2t):.3f} = {abs(det):.0f}$"
)
ax.set_aspect("equal")
ax.set_xlim(-0.8, 4.4)
ax.set_ylim(-0.4, 3.4)
ax.grid(True, alpha=0.3)
ax.legend(loc="upper left", fontsize=9)
fig.tight_layout()
