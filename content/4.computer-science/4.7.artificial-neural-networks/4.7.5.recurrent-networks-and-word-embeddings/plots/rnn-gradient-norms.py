"""Norm of the Jacobian dh_T/dh_t of a tanh RNN with random recurrent weights
W = g * N(0, 1/n), as a function of the distance T - t, for several gains g
(left); the same for the cell state of an LSTM, dc_T/dc_t = prod diag(f_k),
for forget gates f_k = sigmoid(b + noise) with several biases b (right)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import expit

rng = np.random.default_rng(0)
n, T, burn = 64, 100, 50
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.2))
for g, ls in zip([0.5, 0.9, 1.5, 3.0], ["-", "--", "-.", ":"]):
    curves = []
    for trial in range(3):
        W = g * rng.standard_normal((n, n)) / np.sqrt(n)
        U = rng.standard_normal((n, 8)) / np.sqrt(8)
        h = np.zeros(n)
        hs = []
        for t in range(burn + T):
            h = np.tanh(W @ h + U @ rng.standard_normal(8))
            hs.append(h)
        J = np.eye(n)
        norms = [1.0]
        for t in range(burn + T - 1, burn, -1):      # backward through time from the last step
            J = J @ ((1 - hs[t] ** 2)[:, None] * W)
            norms.append(np.linalg.norm(J, 2))
        curves.append(norms)
    ax1.semilogy(np.exp(np.mean(np.log(np.array(curves) + 1e-300), axis=0)), ls, lw=1.6, label=f"gain g = {g}")
ax1.set_xlabel("distance T - t (time steps)")
ax1.set_ylabel("spectral norm of dh_T / dh_t")
ax1.set_title("simple tanh RNN", fontsize=10)
ax1.set_ylim(1e-30, 1e12)
ax1.legend(fontsize=8)
ax1.grid(alpha=0.3)

k = np.arange(T)
for bias, ls in zip([0.0, 2.0, 4.0, 6.0], ["-", "--", "-.", ":"]):
    f = expit(bias + 0.5 * rng.standard_normal((200, T)))
    prod = np.cumprod(f, axis=1).mean(axis=0)
    ax2.semilogy(k + 1, prod, ls, lw=1.6, label=f"forget-gate bias b = {bias:g}")
ax2.set_xlabel("distance T - t (time steps)")
ax2.set_ylabel("mean of prod f_k")
ax2.set_title("LSTM cell state path", fontsize=10)
ax2.set_ylim(1e-30, 1e12)
ax2.legend(fontsize=8)
ax2.grid(alpha=0.3)
fig.tight_layout()
