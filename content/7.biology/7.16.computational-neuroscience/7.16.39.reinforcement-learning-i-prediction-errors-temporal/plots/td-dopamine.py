"""TD(0) model of dopamine responses with a complete serial compound (tapped delay line) stimulus representation.

Trial of 40 time steps (dt = 0.1 s); cue at step 8, reward r = 1 at step 28. The value estimate is
v_hat(t) = sum_k w_k x_k(t), where x_k(t) = 1 if t - t_cue = k (k >= 0), i.e. one feature per time since the cue.
delta_t = r_{t+1} + gamma v_hat(t+1) - v_hat(t); w_k += alpha delta_t x_k(t); gamma = 0.98, alpha = 0.2.
200 training trials; then one omission trial. The pre-cue value is 0 (the cue time is unpredictable).
A: delta over time and trials. B: delta in trial 1, after training, and on omission.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
T, t_cue, t_rew, gamma, alpha = 40, 8, 28, 0.98, 0.2
K = T - t_cue
w = np.zeros(K)


def v(t):
    k = t - t_cue
    return w[k] if 0 <= k < K else 0.0


def trial(reward=True, learn=True):
    d = np.zeros(T)
    for t in range(T - 1):
        r = 1.0 if (reward and t + 1 == t_rew) else 0.0
        d[t + 1] = r + gamma * v(t + 1) - v(t)  # error attributed to the step at which it is observed
        k = t - t_cue
        if learn and 0 <= k < K:
            w[k] += alpha * d[t + 1]
    return d


n = 200
D = np.array([trial() for _ in range(n)])
omit = trial(reward=False, learn=False)
time = (np.arange(T) - t_cue) * 0.1
fig, axs = plt.subplots(1, 2, figsize=(10.5, 3.9), gridspec_kw=dict(width_ratios=[1.3, 1]))
vmax = np.abs(D).max()
im = axs[0].imshow(D, aspect="auto", cmap="RdBu_r", vmin=-vmax, vmax=vmax,
                   extent=[time[0] - 0.05, time[-1] + 0.05, n + 0.5, 0.5])
axs[0].set_xlabel("Time from cue / s")
axs[0].set_ylabel("Trial")
axs[0].set_title("A  TD error during training", loc="left", fontsize=10)
fig.colorbar(im, ax=axs[0], label="$\\delta_t$", shrink=0.85)
for x, lab in [(0, "cue"), ((t_rew - t_cue) * 0.1, "reward")]:
    axs[0].axvline(x, color=P.muted(), lw=0.8, ls=":")
for d, lab, tok, ls in [(D[0], "trial 1", "neutral", "-"), (D[-1], f"trial {n}", "dna", "-"), (omit, "omission after training", "negative", "--")]:
    axs[1].plot(time, d, color=P.edge(tok), lw=2, ls=ls, label=lab)
axs[1].axhline(0, color=P.muted(), lw=0.8)
axs[1].set_xlabel("Time from cue / s")
axs[1].set_ylabel("TD error $\\delta_t$")
axs[1].set_title("B  Single trials", loc="left", fontsize=10)
axs[1].legend(frameon=False, fontsize=8, loc="upper right")
axs[1].grid(True, alpha=0.3)
fig.tight_layout()
