"""Occasionally dishonest casino HMM: true hidden die, posterior P(loaded | rolls) from forward-backward, and the Viterbi path."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
A = np.array([[0.98, 0.02], [0.05, 0.95]])          # 0 = fair, 1 = loaded
B = np.array([[1 / 6] * 6, [0.1] * 5 + [0.5]])       # loaded die shows six half of the time
pi = np.array([0.5, 0.5])
T = 300
x = np.zeros(T, dtype=int)
o = np.zeros(T, dtype=int)
for t in range(T):
    x[t] = rng.choice(2, p=pi if t == 0 else A[x[t - 1]])
    o[t] = rng.choice(6, p=B[x[t]])

# scaled forward-backward
alpha, beta, c = np.zeros((T, 2)), np.ones((T, 2)), np.zeros(T)
alpha[0] = pi * B[:, o[0]]
c[0] = alpha[0].sum()
alpha[0] /= c[0]
for t in range(1, T):
    alpha[t] = (alpha[t - 1] @ A) * B[:, o[t]]
    c[t] = alpha[t].sum()
    alpha[t] /= c[t]
for t in range(T - 2, -1, -1):
    beta[t] = A @ (B[:, o[t + 1]] * beta[t + 1]) / c[t + 1]
posterior = alpha * beta

# Viterbi in log space
logA, logB = np.log(A), np.log(B)
delta = np.log(pi) + logB[:, o[0]]
psi = np.zeros((T, 2), dtype=int)
for t in range(1, T):
    s = delta[:, None] + logA
    psi[t] = s.argmax(axis=0)
    delta = s.max(axis=0) + logB[:, o[t]]
path = np.zeros(T, dtype=int)
path[-1] = delta.argmax()
for t in range(T - 1, 0, -1):
    path[t - 1] = psi[t, path[t]]

fig, axes = plt.subplots(2, 1, figsize=(12, 5), sharex=True, gridspec_kw={"height_ratios": [1, 2]})
ax = axes[0]
ax.scatter(np.arange(T), o + 1, s=6, c=np.where(o == 5, "C3", "gray"))
ax.set_ylabel("roll")
ax.set_yticks(range(1, 7))
ax.set_title("observed rolls (sixes in red)")
ax = axes[1]
ax.fill_between(np.arange(T), 0, x, step="mid", color="C1", alpha=0.25, label="true: loaded die")
ax.plot(posterior[:, 1], color="C0", lw=1.2, label="posterior P(loaded | all rolls)")
ax.step(np.arange(T), path * 0.96 + 0.02, where="mid", color="k", lw=1, ls="--", label="Viterbi path")
ax.set_ylim(-0.05, 1.3)
ax.set_xlabel("t")
ax.set_ylabel("probability / state")
ax.legend(fontsize=8, loc="upper right", ncol=3)
fig.tight_layout()
