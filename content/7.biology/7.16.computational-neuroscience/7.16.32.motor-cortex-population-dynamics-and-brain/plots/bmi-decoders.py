"""Linear filter versus Kalman filter decoding of cursor velocity from synthetic motor cortex data.

Kinematics: two-dimensional hand velocity v_t, a smooth random process (AR(1) with coefficient 0.98
per 50 ms bin, driven by Gaussian noise), the same in training and test sets of 3000 and 600 bins.
Neurons: rates lambda_i = b_i + c_i . v_t (velocity-tuned, cosine tuning in direction), b_i from
5 to 20 Hz, |c_i| chosen to give modulation depths of 3 to 12 Hz at typical speeds; spike counts in
50 ms bins drawn from a Poisson distribution.
Linear filter: ridge regression of v_t on the counts of the current and two preceding bins.
Kalman filter: state x_t = v_t with x_{t+1} = A x_t + w, counts y_t = H x_t + d + q; A, W fitted to
the training kinematics and H, d, Q to the training counts by least squares (Wu et al., 2006).
A: decoded horizontal velocity on a test segment (N = 40).
B: decoded cursor path, obtained by integrating velocity, against the true path (N = 40).
C: root-mean-square velocity error on the test set against the number of neurons.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
dt, a_true = 0.05, 0.98


def kinematics(n):
    v = np.zeros((n, 2))
    for t in range(1, n):
        v[t] = a_true * v[t - 1] + rng.normal(0, 1.6, 2)
    return v                                           # cm/s


def neurons(n):
    b = rng.uniform(5, 20, n)
    ang = rng.uniform(0, 2 * np.pi, n)
    depth = rng.uniform(0.3, 1.2, n)                   # Hz per cm/s
    C = depth[:, None] * np.c_[np.cos(ang), np.sin(ang)]
    return b, C


def spikes(v, b, C):
    lam = np.maximum(b[None, :] + v @ C.T, 0.1)
    return rng.poisson(lam * dt).astype(float)


def lagged(Y, L=3):
    rows = [np.roll(Y, k, axis=0) for k in range(L)]
    X = np.hstack(rows + [np.ones((len(Y), 1))])
    X[:L] = 0
    return X


def linear_filter(Ytr, vtr, Yte, lam=1.0):
    X = lagged(Ytr)
    D = np.linalg.solve(X.T @ X + lam * np.eye(X.shape[1]), X.T @ vtr)
    return lagged(Yte) @ D


def kalman(Ytr, vtr, Yte):
    X0, X1 = vtr[:-1], vtr[1:]
    A = np.linalg.lstsq(X0, X1, rcond=None)[0].T
    W = np.cov((X1 - X0 @ A.T).T)
    Xh = np.c_[vtr, np.ones(len(vtr))]
    Hd = np.linalg.lstsq(Xh, Ytr, rcond=None)[0].T
    H, d = Hd[:, :2], Hd[:, 2]
    Q = np.cov((Ytr - Xh @ Hd.T).T) + 1e-6 * np.eye(len(d))
    x, S = np.zeros(2), np.eye(2) * 10
    out = []
    G = np.linalg.solve(Q, H).T                        # H^T Q^-1, 2 x N
    GH = G @ H
    for y in Yte:
        x, S = A @ x, A @ S @ A.T + W
        # information form of the update (many neurons, two state dimensions)
        S = np.linalg.inv(np.linalg.inv(S) + GH)
        x = x + S @ (G @ (y - d) - GH @ x)
        out.append(x.copy())
    return np.array(out)


vtr, vte = kinematics(3000), kinematics(600)
b, C = neurons(40)
Ytr, Yte = spikes(vtr, b, C), spikes(vte, b, C)
vl, vk = linear_filter(Ytr, vtr, Yte), kalman(Ytr, vtr, Yte)

fig, axs = plt.subplots(1, 3, figsize=(13, 3.8), gridspec_kw={"width_ratios": [1.5, 1, 1]})
ax = axs[0]
seg = slice(100, 260)
tt = np.arange(600)[seg] * dt
ax.plot(tt, vte[seg, 0], color=P.ink(), lw=2.0, label="true")
ax.plot(tt, vl[seg, 0], color=P.edge("negative"), lw=1.2, label="linear filter")
ax.plot(tt, vk[seg, 0], color=P.edge("dna"), lw=1.4, label="Kalman filter")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Horizontal velocity (cm/s)")
ax.set_title("A  Decoded velocity ($N = 40$)", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, ncol=3, loc="upper left")

ax = axs[1]
seg = slice(100, 400)
for v, col, lw in ((vte, P.ink(), 2.0), (vl, P.edge("negative"), 1.2), (vk, P.edge("dna"), 1.4)):
    p = np.cumsum(v[seg] * dt, axis=0)
    ax.plot(p[:, 0], p[:, 1], color=col, lw=lw)
ax.plot(0, 0, "o", color=P.ink(), ms=4)
ax.set_aspect("equal", adjustable="datalim")
ax.set_xlabel("$x$ (cm)")
ax.set_ylabel("$y$ (cm)")
ax.set_title("B  Cursor path (15 s)", loc="left", fontsize=10)

ax = axs[2]
Ns = [10, 20, 40, 80, 160]
el, ek = [], []
for n in Ns:
    rl, rk = [], []
    for rep in range(4):
        b, C = neurons(n)
        Ytr, Yte = spikes(vtr, b, C), spikes(vte, b, C)
        rl.append(np.sqrt(((linear_filter(Ytr, vtr, Yte) - vte) ** 2).sum(1).mean()))
        rk.append(np.sqrt(((kalman(Ytr, vtr, Yte) - vte) ** 2).sum(1).mean()))
    el.append(np.mean(rl))
    ek.append(np.mean(rk))
ax.plot(Ns, el, "o-", color=P.edge("negative"), lw=1.6, ms=4, label="linear filter")
ax.plot(Ns, ek, "o-", color=P.edge("dna"), lw=1.6, ms=4, label="Kalman filter")
ax.axhline(np.sqrt((vte ** 2).sum(1).mean()), color=P.muted(), lw=0.8, ls=":")
ax.text(Ns[-1], np.sqrt((vte ** 2).sum(1).mean()), "s.d. of velocity", fontsize=7,
        color=P.muted(), ha="right", va="top")
ax.set_xscale("log")
ax.set_xticks(Ns)
ax.set_xticklabels([str(n) for n in Ns])
ax.set_ylim(0, None)
ax.set_xlabel("Number of neurons $N$")
ax.set_ylabel("RMS velocity error (cm/s)")
ax.set_title("C  Accuracy", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8)
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
