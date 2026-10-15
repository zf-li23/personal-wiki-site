import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Left: A maps the unit circle to an ellipse whose semi-axes are sigma_i * u_i
A = np.array([[3.0, 0.0], [4.0, 5.0]])
U, s, Vt = np.linalg.svd(A)
theta = np.linspace(0, 2 * np.pi, 400)
circle = np.vstack([np.cos(theta), np.sin(theta)])
ellipse = A @ circle
ax1.plot(circle[0], circle[1], color="tab:blue", label="unit circle")
ax1.plot(ellipse[0], ellipse[1], color="tab:orange", label="image under A")
for i, c in enumerate(["tab:green", "tab:red"]):
    v = Vt[i]
    w = s[i] * U[:, i]
    ax1.annotate("", xy=v, xytext=(0, 0),
                 arrowprops=dict(arrowstyle="->", color=c, lw=2))
    ax1.annotate("", xy=w, xytext=(0, 0),
                 arrowprops=dict(arrowstyle="->", color=c, lw=2, ls="--"))
    ax1.text(*(1.15 * v), f"v{i + 1}", color=c, fontsize=12)
    ax1.text(*(1.08 * w), f"sigma{i + 1} u{i + 1}", color=c, fontsize=12)
ax1.set_aspect("equal")
ax1.grid(True, alpha=0.3)
ax1.set_title("A = [[3, 0], [4, 5]]: circle to ellipse")
ax1.legend(loc="lower right")

# Right: singular values and rank-k approximation errors of a test matrix
rng = np.random.default_rng(0)
m, n = 80, 60
Q1, _ = np.linalg.qr(rng.standard_normal((m, n)))
Q2, _ = np.linalg.qr(rng.standard_normal((n, n)))
sigma = 0.75 ** np.arange(n)          # geometrically decaying spectrum
M = Q1 @ np.diag(sigma) @ Q2.T + 1e-4 * rng.standard_normal((m, n))
sv = np.linalg.svd(M, compute_uv=False)
ks = np.arange(0, 41)
spec_err = sv[ks] / sv[0]             # ||M - M_k||_2 / ||M||_2 = sigma_{k+1} / sigma_1
fro_err = np.sqrt([np.sum(sv[k:] ** 2) for k in ks]) / np.sqrt(np.sum(sv ** 2))
ax2.semilogy(ks, spec_err, "o-", ms=3, label="spectral norm error (relative)")
ax2.semilogy(ks, fro_err, "s-", ms=3, label="Frobenius norm error (relative)")
ax2.set_xlabel("rank k of the truncated SVD")
ax2.set_ylabel("relative error")
ax2.set_title("Best rank-k approximation of an 80 x 60 matrix")
ax2.grid(True, which="both", alpha=0.3)
ax2.legend()
fig.tight_layout()
