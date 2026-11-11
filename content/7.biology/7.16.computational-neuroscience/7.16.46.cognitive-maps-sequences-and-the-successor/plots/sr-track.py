"""The successor representation (SR) on a linear track and predictive place fields.

Track of 40 states. Policy: the animal moves one state to the right with probability p and to
the left with probability 1 - p (reflecting ends). T is the one-step transition matrix, the SR is
M = (I - gamma T)^(-1) with gamma = 0.9 (Definition 46.2.1). The "place field" of an SR cell that
predicts state j is the column M(., j), a function of the current state.
A: M for a rightward-biased policy (p = 0.9); color scale clipped at 2 (the right end, where the
   animal accumulates, reaches about 9).
B: SR place fields of the cell for state 20 under an unbiased random walk (p = 0.5, symmetric)
   and the rightward policy (p = 0.9): the field skews backward, toward the states from which the
   animal arrives, and its center of mass shifts against the direction of travel.
C: TD learning of the SR from experience (laps running rightward from state 0 to 39 with
   p = 0.9; learning rate 0.1): M(s, .) <- M(s, .) + alpha [e_s + gamma M(s', .) - M(s, .)].
   The field of the cell for state 20 after 1, 5, 20 and 80 laps: it expands backward with
   experience, as place fields do on a familiar track (Mehta, Barnes and McNaughton, 1997).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
n, gamma = 40, 0.9


def transition(p):
    T = np.zeros((n, n))
    for s in range(n):
        r, l = min(s + 1, n - 1), max(s - 1, 0)
        T[s, r] += p
        T[s, l] += 1 - p
    return T


def sr(p):
    return np.linalg.inv(np.eye(n) - gamma * transition(p))


fig, axs = plt.subplots(1, 3, figsize=(13, 3.9))
M9 = sr(0.9)
im = axs[0].imshow(M9, cmap="viridis", origin="upper", vmax=2.0)
axs[0].set_xlabel("Future state $s'$")
axs[0].set_ylabel("Current state $s$")
axs[0].set_title("A  SR matrix, rightward policy", loc="left", fontsize=10)
fig.colorbar(im, ax=axs[0], fraction=0.046, pad=0.04)

j = 20
xs = np.arange(n)
for p, c, lab in ((0.5, P.edge("neutral"), "random walk"), (0.9, P.edge("dna"), "rightward policy")):
    f = sr(p)[:, j]
    f = f / f.max()
    com = (xs * f).sum() / f.sum()
    axs[1].plot(xs, f, lw=2, color=c, label=f"{lab} (center {com:.1f})")
axs[1].axvline(j, color=P.muted(), ls=":", lw=1)
axs[1].annotate("", xy=(24, 0.5), xytext=(30, 0.5), arrowprops=dict(arrowstyle="<-", color=P.ink()))
axs[1].text(25, 0.55, "travel", fontsize=8)
axs[1].set_xlim(5, 35)
axs[1].set_xlabel("Current position (state)")
axs[1].set_ylabel("Normalized field $M(s, 20)$")
axs[1].set_title("B  Predictive fields skew backward", loc="left", fontsize=10)
axs[1].legend(frameon=False, fontsize=8, loc="upper left")

M = np.eye(n)
alpha = 0.1
snap = {1: None, 5: None, 20: None, 80: None}
for lap in range(1, 81):
    s = 0
    while s < n - 1:
        s2 = s + 1 if rng.random() < 0.9 else max(s - 1, 0)
        e = np.zeros(n)
        e[s] = 1
        M[s] += alpha * (e + gamma * M[s2] - M[s])
        s = s2
    if lap in snap:
        snap[lap] = M[:, j].copy()
cols = [P.edge("neutral"), P.edge("positive"), P.edge("dna"), P.edge("negative")]
for (lap, f), c in zip(snap.items(), cols):
    axs[2].plot(xs, f, lw=1.8, color=c, label=f"lap {lap}")
axs[2].axvline(j, color=P.muted(), ls=":", lw=1)
axs[2].set_xlim(5, 35)
axs[2].set_xlabel("Current position (state)")
axs[2].set_ylabel("Learned $M(s, 20)$")
axs[2].set_title("C  Backward expansion with experience", loc="left", fontsize=10)
axs[2].legend(frameon=False, fontsize=8, loc="upper left")
for a in axs[1:]:
    a.grid(True, alpha=0.3)
fig.tight_layout()
