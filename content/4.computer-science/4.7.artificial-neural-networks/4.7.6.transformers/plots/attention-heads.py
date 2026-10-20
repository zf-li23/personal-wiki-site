"""Attention weights of two hand-constructed causal self-attention heads on a
toy sentence: a positional head whose query is the sinusoidal encoding of the
previous position, so that each token attends to its predecessor (left), and a
content head whose queries and keys are the token embeddings, so that each token
attends to earlier occurrences of the same word (right)."""

import numpy as np
import matplotlib.pyplot as plt

tokens = "the cat sat on the mat because the cat was tired".split()
n, d = len(tokens), 64
rng = np.random.default_rng(0)
vocab = sorted(set(tokens))
emb = {w: v / np.linalg.norm(v) for w, v in zip(vocab, rng.standard_normal((len(vocab), d)))}
E = np.array([emb[w] for w in tokens])

freq = 1.0 / 10000 ** (np.arange(0, d, 2) / d)


def pe(p):
    v = np.zeros(d)
    v[0::2], v[1::2] = np.sin(p * freq), np.cos(p * freq)
    return v


P = np.array([pe(p) for p in range(n)])
Q_pos = np.array([pe(p - 1) for p in range(n)])         # a linear map of pe(p) (block rotation)


def causal_softmax(S):
    S = np.where(np.tril(np.ones_like(S, dtype=bool)), S, -np.inf)
    S = S - S.max(axis=1, keepdims=True)
    A = np.exp(S)
    return A / A.sum(axis=1, keepdims=True)


A_pos = causal_softmax(2.0 * Q_pos @ P.T)
A_tok = causal_softmax(6.0 * E @ E.T)
fig, axes = plt.subplots(1, 2, figsize=(11.5, 5.4), layout="constrained")
for ax, A, title in zip(axes, [A_pos, A_tok], ["positional head (previous token)", "content head (same word)"]):
    im = ax.imshow(A, cmap="viridis", vmin=0, vmax=1)
    ax.set_xticks(range(n))
    ax.set_xticklabels(tokens, rotation=60, fontsize=8)
    ax.set_yticks(range(n))
    ax.set_yticklabels(tokens, fontsize=8)
    ax.set_xlabel("key position (attended to)")
    ax.set_ylabel("query position")
    ax.set_title(title, fontsize=10)
fig.colorbar(im, ax=axes, fraction=0.03)
