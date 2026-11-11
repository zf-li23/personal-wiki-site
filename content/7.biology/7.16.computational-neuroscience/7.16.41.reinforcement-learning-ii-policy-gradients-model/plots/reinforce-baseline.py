"""REINFORCE on a two-armed bandit, with and without a baseline.

Arm 1 pays N(6, 1), arm 2 pays N(5, 1). Softmax policy with one parameter theta: pi(arm 1) = 1 / (1 + exp(-theta)).
Score: d/dtheta ln pi(a) = 1 - pi for arm 1, -pi for arm 2. Single-sample gradient estimate g = (R - b) * score.
A: standard deviation of g against pi(arm 1), exact, for b = 0 and for b = v_pi (expected reward of the policy);
   the mean gradient pi (1 - pi) (mu1 - mu2) is shown for comparison.
B: learning curves, alpha = 0.05, 300 trials, mean over 400 runs; baseline = running average of reward (rate 0.1).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
mu = np.array([6.0, 5.0])
sd = 1.0
pi = np.linspace(0.01, 0.99, 300)


def grad_stats(pi, b):
    s1, s2 = 1 - pi, -pi
    m1 = pi * s1 * (mu[0] - b) + (1 - pi) * s2 * (mu[1] - b)
    e2 = pi * s1**2 * (sd**2 + (mu[0] - b) ** 2) + (1 - pi) * s2**2 * (sd**2 + (mu[1] - b) ** 2)
    return m1, np.sqrt(e2 - m1**2)


mean0, sd0 = grad_stats(pi, 0.0)
v = pi * mu[0] + (1 - pi) * mu[1]
meanb, sdb = grad_stats(pi, v)

rng = np.random.default_rng(0)
R_RUNS, T, ALPHA = 400, 300, 0.05


def learn(use_baseline):
    theta = np.zeros(R_RUNS)
    b = np.zeros(R_RUNS)
    if use_baseline:
        b[:] = 5.5
    out = np.empty((T, R_RUNS))
    for t in range(T):
        p1 = 1 / (1 + np.exp(-theta))
        out[t] = p1
        arm1 = rng.random(R_RUNS) < p1
        r = np.where(arm1, mu[0], mu[1]) + sd * rng.standard_normal(R_RUNS)
        score = np.where(arm1, 1 - p1, -p1)
        theta += ALPHA * (r - (b if use_baseline else 0.0)) * score
        if use_baseline:
            b += 0.1 * (r - b)
    return out


no_b = learn(False)
with_b = learn(True)

fig, axs = plt.subplots(1, 2, figsize=(10, 3.7))
ax = axs[0]
ax.plot(pi, sd0, color=P.edge("negative"), lw=2.2, label="SD of estimate, no baseline")
ax.plot(pi, sdb, color=P.edge("dna"), lw=2.2, label="SD of estimate, baseline $b = v_\\pi$")
ax.plot(pi, mean0, color=P.ink(), lw=1.4, ls="--", label="true gradient (both)")
ax.set_xlabel("$\\pi(\\mathrm{arm\\ 1})$")
ax.set_ylabel("Single-sample gradient")
ax.set_title("A  Unbiased, but very different variance", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="upper right")
ax.set_ylim(0, 3.4)
ax = axs[1]
t = np.arange(T)
for out, tok, lab in [(no_b, "negative", "no baseline"), (with_b, "dna", "running-average baseline")]:
    m = out.mean(axis=1)
    lo, hi = np.percentile(out, [25, 75], axis=1)
    ax.fill_between(t, lo, hi, color=P.fill(tok), alpha=0.35, lw=0)
    ax.plot(t, m, color=P.edge(tok), lw=2.2, label=lab)
ax.axhline(0.5, color=P.muted(), lw=0.8, ls=":")
ax.set_xlabel("Trial")
ax.set_ylabel("$\\pi(\\mathrm{arm\\ 1})$")
ax.set_ylim(0, 1.02)
ax.set_title("B  Learning (mean and interquartile range)", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="lower right")
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
