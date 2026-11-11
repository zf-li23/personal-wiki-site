"""Generation by reversing diffusion, for a bimodal one-dimensional distribution.

Data: p0 = 0.5 N(-2, 0.3^2) + 0.5 N(2, 0.3^2). Forward (variance-preserving) process
dx = -0.5 b x dt + sqrt(b) dW with constant b = 6 on t in [0, 1]: x_t = a_t x_0 + sqrt(1 - a_t^2) eps,
a_t = exp(-b t / 2), so p_t is again a Gaussian mixture and its score d/dx log p_t is exact.
Reverse-time SDE (Anderson 1982): dx = [-0.5 b x - b d/dx log p_t(x)] dt + sqrt(b) dW_bar,
integrated from t = 1 back to 0 with Euler-Maruyama (1000 steps, 4000 particles started from N(0, 1)).
A: the density p_t (shading) and 25 reverse trajectories.
B: histogram of the generated samples against p0.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
mus = np.array([-2.0, 2.0])
sd0 = 0.3
b = 6.0


def mix_params(t):
    a = np.exp(-0.5 * b * t)
    return a * mus, np.sqrt(a ** 2 * sd0 ** 2 + 1 - a ** 2)


def density(x, t):
    m, s = mix_params(t)
    return 0.5 * np.sum(np.exp(-(x[..., None] - m) ** 2 / (2 * s ** 2)) / np.sqrt(2 * np.pi * s ** 2), axis=-1)


def score(x, t):
    m, s = mix_params(t)
    lw = -(x[:, None] - m) ** 2 / (2 * s ** 2)
    lw -= lw.max(axis=1, keepdims=True)
    wgt = np.exp(lw)
    wgt /= wgt.sum(axis=1, keepdims=True)
    return np.sum(wgt * (m - x[:, None]), axis=1) / s ** 2


n, N = 1000, 4000
dt = 1.0 / n
x = rng.normal(size=N)
traj = np.empty((n + 1, 25))
traj[0] = x[:25]
for k in range(n):
    t = 1.0 - k * dt
    drift = -0.5 * b * x - b * score(x, t)
    x = x - drift * dt + np.sqrt(b * dt) * rng.normal(size=N)
    traj[k + 1] = x[:25]

fig, axs = plt.subplots(1, 2, figsize=(10.5, 3.9), gridspec_kw={"width_ratios": [1.6, 1]})
ax = axs[0]
ts = np.linspace(0, 1, 200)
xs = np.linspace(-4, 4, 300)
Dn = np.array([density(xs, t) for t in ts]).T
ax.imshow(Dn, extent=[0, 1, -4, 4], origin="lower", aspect="auto", cmap="Blues", alpha=0.8)
tt = 1.0 - np.arange(n + 1) * dt
for j in range(25):
    ax.plot(tt, traj[:, j], color=P.edge("negative"), lw=0.6, alpha=0.8)
ax.set_xlim(1, 0)
ax.set_xlabel("Diffusion time $t$ (generation runs from left to right)")
ax.set_ylabel("$x$")
ax.set_title("A  Reverse diffusion trajectories over $p_t(x)$", loc="left", fontsize=10)

ax = axs[1]
ax.hist(x, bins=80, range=(-4, 4), density=True, color=P.fill("negative"), edgecolor=P.edge("negative"), lw=0.3, label="generated")
ax.plot(xs, density(xs, 0.0), color=P.edge("dna"), lw=1.8, label="data $p_0$")
ax.plot(xs, np.exp(-xs ** 2 / 2) / np.sqrt(2 * np.pi), color=P.muted(), lw=1.2, ls="--", label="start $\\mathcal{N}(0, 1)$")
ax.set_xlabel("$x$")
ax.set_ylabel("Density")
ax.legend(frameon=False, fontsize=7.5)
ax.set_title("B  Generated samples", loc="left", fontsize=10)
fig.tight_layout()
