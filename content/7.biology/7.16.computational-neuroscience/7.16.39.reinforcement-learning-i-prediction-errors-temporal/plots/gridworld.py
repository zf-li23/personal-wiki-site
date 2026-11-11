"""Value iteration and Q-learning in a gridworld.

6 x 6 grid, walls at three cells, goal at the top right (reward +1 on entering, episode ends), every other
step reward 0, gamma = 0.9, deterministic moves (up, down, left, right; moving into a wall or edge stays).
A-C: state values after 1, 4 and 20 sweeps of value iteration, with the greedy policy after 20 sweeps.
D: Q-learning and SARSA (alpha = 0.5, epsilon-greedy with epsilon = 0.1), steps to the goal per episode
from the bottom-left start, mean of 50 runs.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
H = W = 6
walls = {(2, 1), (2, 2), (2, 3)}
goal = (0, 5)
start = (5, 0)
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
gamma = 0.9
states = [(i, j) for i in range(H) for j in range(W) if (i, j) not in walls]


def step(s, a):
    i, j = s[0] + moves[a][0], s[1] + moves[a][1]
    if not (0 <= i < H and 0 <= j < W) or (i, j) in walls:
        i, j = s
    r = 1.0 if (i, j) == goal else 0.0
    return (i, j), r


def value_iteration(n):
    v = np.zeros((H, W))
    for _ in range(n):
        new = v.copy()
        for s in states:
            if s == goal:
                continue
            new[s] = max(r + gamma * (0 if s2 == goal else v[s2]) for s2, r in (step(s, a) for a in range(4)))
        v = new
    return v


def greedy(v, s):
    vals = [r + gamma * (0 if s2 == goal else v[s2]) for s2, r in (step(s, a) for a in range(4))]
    return int(np.argmax(vals))


rng = np.random.default_rng(0)


def run(method, episodes=80, alpha=0.5, eps=0.1):
    q = np.zeros((H, W, 4))
    lengths = []

    def act(s):
        if rng.random() < eps:
            return int(rng.integers(4))
        qs = q[s]
        return int(rng.choice(np.flatnonzero(qs == qs.max())))

    for _ in range(episodes):
        s, a, n = start, None, 0
        a = act(s)
        while s != goal and n < 500:
            s2, r = step(s, a)
            a2 = act(s2)
            if s2 == goal:
                target = r
            elif method == "q":
                target = r + gamma * q[s2].max()
            else:
                target = r + gamma * q[s2][a2]
            q[s][a] += alpha * (target - q[s][a])
            s, a, n = s2, a2, n + 1
        lengths.append(n)
    return np.array(lengths)


fig = plt.figure(figsize=(11, 3.4))
gs = fig.add_gridspec(1, 4, width_ratios=[1, 1, 1, 1.5])
arrows = {0: (0, 0.3), 1: (0, -0.3), 2: (-0.3, 0), 3: (0.3, 0)}
for k, (n, letter) in enumerate([(1, "A"), (4, "B"), (20, "C")]):
    ax = fig.add_subplot(gs[k])
    v = value_iteration(n)
    m = np.ma.masked_array(v, mask=np.zeros_like(v, bool))
    for c in walls:
        m.mask[c] = True
    ax.imshow(m, cmap="viridis", vmin=0, vmax=1)
    for c in walls:
        ax.add_patch(plt.Rectangle((c[1] - 0.5, c[0] - 0.5), 1, 1, color=P.muted()))
    ax.text(goal[1], goal[0], "G", ha="center", va="center", color="white", fontsize=10, weight="bold")
    if n == 20:
        for s in states:
            if s != goal:
                dx, dy = arrows[greedy(v, s)]
                ax.annotate("", xy=(s[1] + dx, s[0] - dy), xytext=(s[1] - dx, s[0] + dy),
                            arrowprops=dict(arrowstyle="->", color="white", lw=1.1))
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f"{letter}  {n} sweep{'s' if n > 1 else ''}", loc="left", fontsize=10)
ax = fig.add_subplot(gs[3])
for method, lab, tok in [("q", "Q-learning", "dna"), ("sarsa", "SARSA", "negative")]:
    L = np.mean([run(method) for _ in range(50)], axis=0)
    ax.plot(np.arange(1, len(L) + 1), L, color=P.edge(tok), lw=1.8, label=lab)
ax.axhline(10, color=P.muted(), lw=0.8, ls=":")
ax.text(40, 8.8, "shortest path (10 steps)", fontsize=8, color=P.muted(), va="top")
ax.set_ylim(7, 250)
ax.set_yscale("log")
ax.set_xlabel("Episode")
ax.set_ylabel("Steps to goal")
ax.set_title("D  Learning from experience", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8)
ax.grid(True, alpha=0.3, which="both")
fig.tight_layout()
