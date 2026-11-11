"""The two-step task (Daw, Gershman, Seymour, Dayan and Dolan 2011): stay probabilities of simulated agents.

Stage 1: choose a1 or a2. a1 leads to state B with p = 0.7 (common) and to C with 0.3 (rare); a2 the reverse.
Stage 2: in B or C choose one of two options; each of the four options pays 1 with a probability that drifts as a
Gaussian random walk (SD 0.025 per trial) reflected into [0.25, 0.75].
Model-free agent: SARSA with lambda = 1, alpha = 0.3: Q2 <- Q2 + alpha (r - Q2), Q1(a) <- Q1(a) + alpha (r - Q1(a)).
Model-based agent: Q1(a) = sum_s P(s | a) max_b Q2(s, b) with the known transition matrix; same Q2 learning.
Hybrid: w * Q_MB + (1 - w) * Q_MF with w = 0.5. Softmax with beta = 5 at both stages.
200 agents x 1000 trials each. Stay probability = P(repeat the previous stage-1 choice) by previous outcome and transition.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
N_AG, T, ALPHA, BETA = 200, 1000, 0.3, 5.0
TRANS = np.array([[0.7, 0.3], [0.3, 0.7]])


def simulate(w):
    q1 = np.zeros((N_AG, 2))
    q2 = np.zeros((N_AG, 2, 2))
    pr = rng.uniform(0.25, 0.75, (N_AG, 2, 2))
    idx = np.arange(N_AG)
    prev = None
    counts = np.zeros((2, 2))
    stays = np.zeros((2, 2))
    for t in range(T):
        qmb = q2.max(axis=2) @ TRANS.T
        q = w * qmb + (1 - w) * q1
        p0 = 1 / (1 + np.exp(-BETA * (q[:, 0] - q[:, 1])))
        a = (rng.random(N_AG) >= p0).astype(int)
        common = rng.random(N_AG) < 0.7
        s = np.where(common, a, 1 - a)
        qs = q2[idx, s]
        pb0 = 1 / (1 + np.exp(-BETA * (qs[:, 0] - qs[:, 1])))
        b = (rng.random(N_AG) >= pb0).astype(int)
        r = (rng.random(N_AG) < pr[idx, s, b]).astype(float)
        if prev is not None:
            pa, pr_, pc = prev
            stay = (a == pa).astype(float)
            for i_r in (0, 1):
                for i_c in (0, 1):
                    m = (pr_ == 1 - i_r) & (pc == (i_c == 0))
                    counts[i_r, i_c] += m.sum()
                    stays[i_r, i_c] += stay[m].sum()
        q2[idx, s, b] += ALPHA * (r - q2[idx, s, b])
        q1[idx, a] += ALPHA * (r - q1[idx, a])
        pr = pr + 0.025 * rng.standard_normal(pr.shape)
        pr = np.where(pr > 0.75, 1.5 - pr, pr)
        pr = np.where(pr < 0.25, 0.5 - pr, pr)
        prev = (a, r, common)
    return stays / counts  # rows: rewarded, unrewarded; cols: common, rare


res = [("A  Model-free", simulate(0.0)), ("B  Model-based", simulate(1.0)), ("C  Hybrid ($w = 0.5$)", simulate(0.5))]
fig, axs = plt.subplots(1, 3, figsize=(10.5, 3.4), sharey=True)
x = np.array([0, 1])
for ax, (title, sp) in zip(axs, res):
    ax.bar(x - 0.18, sp[:, 0], 0.36, color=P.fill("dna"), edgecolor=P.edge("dna"), label="common")
    ax.bar(x + 0.18, sp[:, 1], 0.36, color=P.fill("negative"), edgecolor=P.edge("negative"), label="rare")
    ax.set_xticks(x)
    ax.set_xticklabels(["rewarded", "unrewarded"])
    ax.set_ylim(0.4, 1.0)
    ax.set_title(title, loc="left", fontsize=10)
    ax.grid(True, alpha=0.3, axis="y")
axs[0].set_ylabel("Stay probability")
axs[0].legend(frameon=False, fontsize=8, title="previous transition", title_fontsize=8, loc="upper right")
fig.tight_layout()
