"""Credit assignment without weight transport: backpropagation, feedback alignment and evolution strategies.

Task: regression from a fixed random teacher, y* = T2 tanh(T1 x), x in R^30, y in R^10, 20 hidden teacher units.
Student: y = W2 tanh(W1 x) with 40 hidden units, squared error, minibatches of 50, learning rate 0.1.
- Backpropagation (BP): hidden error delta_h = (W2^T e) * tanh'(a).
- Feedback alignment (FA, Lillicrap et al. 2016): delta_h = (B e) * tanh'(a) with B a fixed random
  matrix of the shape of W2^T.
- Evolution strategies (ES): no backward pass; 20 antithetic pairs (40 samples) of Gaussian perturbations
  (std 0.02) of all weights per update, fitness rank-transformed to [-0.5, 0.5] (centred rank),
  step 0.003 / (1 + k / 200) at update k.
- Shallow baseline: only the output layer W2 is trained (hidden weights fixed).
A: test error against the number of updates. B: angle between the FA hidden-error signal (B e) and the
true backpropagated signal (W2^T e), averaged over a test batch: the forward weights come to align with B.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
nx, nh, ny, nt = 30, 40, 10, 20
T1 = rng.normal(size=(nt, nx)) / np.sqrt(nx)
T2 = rng.normal(size=(ny, nt)) / np.sqrt(nt)
Xte = rng.normal(size=(nx, 500))
Yte = T2 @ np.tanh(T1 @ Xte)
steps, bs, lr = 1500, 50, 0.1
n_pop, sd, alpha = 20, 0.02, 0.003
W1_0 = rng.normal(size=(nh, nx)) / np.sqrt(nx)
W2_0 = rng.normal(size=(ny, nh)) / np.sqrt(nh) * 0.1
B = rng.normal(size=(nh, ny)) / np.sqrt(ny)


def test_err(W1, W2):
    return np.mean((W2 @ np.tanh(W1 @ Xte) - Yte) ** 2)


def train(mode, seed=1):
    r = np.random.default_rng(seed)
    W1, W2 = W1_0.copy(), W2_0.copy()
    errs, angs = [], []
    for k in range(steps):
        X = r.normal(size=(nx, bs))
        Y = T2 @ np.tanh(T1 @ X)
        if mode == "es":
            e1 = r.normal(size=(n_pop, nh, nx))
            e2 = r.normal(size=(n_pop, ny, nh))
            e1 = np.concatenate([e1, -e1])
            e2 = np.concatenate([e2, -e2])
            H = np.tanh(np.einsum("pij,jb->pib", W1 + sd * e1, X))
            O = np.einsum("pij,pjb->pib", W2 + sd * e2, H)
            f = -np.mean((O - Y) ** 2, axis=(1, 2))
            rank = np.empty_like(f)
            rank[np.argsort(f)] = np.arange(len(f))
            u = rank / (len(f) - 1) - 0.5
            step = alpha / (1 + k / 200)
            W1 += step * np.tensordot(u, e1, axes=1) / (len(f) * sd)
            W2 += step * np.tensordot(u, e2, axes=1) / (len(f) * sd)
        else:
            H = np.tanh(W1 @ X)
            E = W2 @ H - Y
            if mode in ("bp", "fa"):
                back = W2.T @ E if mode == "bp" else B @ E
                W1 -= lr * (back * (1 - H ** 2)) @ X.T / bs
            W2 -= lr * E @ H.T / bs
        if k % 30 == 0:
            errs.append(test_err(W1, W2))
            if mode == "fa":
                Ht = np.tanh(W1 @ Xte)
                Et = W2 @ Ht - Yte
                a, b = (B @ Et).ravel(), (W2.T @ Et).ravel()
                angs.append(np.degrees(np.arccos(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))))
    return np.array(errs), np.array(angs)


ks = np.arange(0, steps, 30)
res = {m: train(m) for m in ("bp", "fa", "shallow", "es")}
fig, axs = plt.subplots(1, 2, figsize=(10.5, 3.9))
ax = axs[0]
labels = {"bp": "backpropagation", "fa": "feedback alignment", "shallow": "output layer only", "es": "evolution strategies (40 samples per update)"}
cols = {"bp": P.edge("dna"), "fa": P.edge("negative"), "shallow": P.muted(), "es": P.edge("enzyme")}
for m in ("bp", "fa", "es", "shallow"):
    ax.semilogy(ks, res[m][0], color=cols[m], lw=1.8, label=labels[m], ls="--" if m == "shallow" else "-")
ax.set_xlabel("Updates")
ax.set_ylabel("Test error (mean squared)")
ax.legend(frameon=False, fontsize=7.5)
ax.set_title("A  Learning curves", loc="left", fontsize=10)
ax = axs[1]
ax.plot(ks, res["fa"][1], color=P.edge("negative"), lw=1.8)
ax.axhline(90, color=P.muted(), lw=0.8, ls=":")
ax.text(steps * 0.98, 86, "orthogonal (no information)", ha="right", va="top", fontsize=8, color=P.muted())
ax.set_ylim(0, 100)
ax.set_xlabel("Updates")
ax.set_ylabel("Angle between FA and BP signals / degrees")
ax.set_title("B  Alignment of the feedback signal", loc="left", fontsize=10)
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
