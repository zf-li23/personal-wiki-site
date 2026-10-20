"""Cumulative regret of greedy, epsilon-greedy and UCB1 on a 5-armed Bernoulli bandit."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
mu = np.array([0.8, 0.6, 0.5, 0.4, 0.3])
K, T, runs = len(mu), 20000, 100
gap = mu.max() - mu


def simulate(policy):
    counts = np.zeros((runs, K))
    sums = np.zeros((runs, K))
    regret = np.zeros((runs, T))
    rows = np.arange(runs)
    total = np.zeros(runs)
    for t in range(T):
        if t < K:                                   # play every arm once
            arm = np.full(runs, t)
        else:
            means = sums / counts
            if policy == "greedy":
                arm = means.argmax(1)
            elif policy == "eps":
                explore = rng.random(runs) < 0.1
                arm = np.where(explore, rng.integers(0, K, runs), means.argmax(1))
            else:                                   # UCB1
                arm = (means + np.sqrt(2 * np.log(t) / counts)).argmax(1)
        reward = rng.random(runs) < mu[arm]
        counts[rows, arm] += 1
        sums[rows, arm] += reward
        total += gap[arm]
        regret[:, t] = total
    return regret.mean(0)


t = np.arange(1, T + 1)
fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
for policy, label in [("greedy", "greedy"), ("eps", "epsilon-greedy (0.1)"), ("ucb", "UCB1")]:
    r = simulate(policy)
    axes[0].plot(t, r, label=label)
    axes[1].plot(t, r, label=label)
axes[0].set_xlabel("round t")
axes[0].set_ylabel("expected cumulative regret")
axes[0].set_title("linear time axis")
axes[1].set_xscale("log")
axes[1].set_xlabel("round t (log scale)")
axes[1].set_title("log time axis: UCB1 grows like log t")
for ax in axes:
    ax.grid(alpha=0.3)
axes[0].legend()
fig.tight_layout()
