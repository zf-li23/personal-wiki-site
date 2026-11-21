"""Canceling the expected: an adaptive negative image in the mormyrid electrosensory lobe.

A principal cell receives (i) the electrosensory input caused by the fish's own discharge
(reafference), which has a fixed time course after each EOD command, and (ii) a corollary
discharge signal time-locked to the command, carried by many parallel fibers with different
delays. Anti-Hebbian plasticity at the parallel-fiber synapses (weight change opposite to the
correlation between parallel-fiber activity and the cell's response) builds a negative image of
the predictable input. A: response after the command on trials 1, 10 and 100: the predictable
part is canceled. B: response on the last trials with a small novel signal (a prey, dashed) added:
the novel signal stands out. C: after the reafferent input is removed (e.g. EOD silenced but
commands continue) the learned negative image appears as an inverted response and fades.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
t = np.linspace(0, 60, 301)  # ms after the command
reaff = 1.2 * np.exp(-((t - 8) / 4) ** 2) - 0.5 * np.exp(-((t - 20) / 7) ** 2) + 0.2 * np.exp(-((t - 35) / 10) ** 2)
novel = 0.35 * np.exp(-((t - 28) / 3) ** 2)
basis = np.array([np.exp(-((t - c) / 2.5) ** 2) for c in np.linspace(0, 60, 40)])
w = np.zeros(len(basis))
eta = 0.04
resp = {}
for trial in range(1, 301):
    inp = reaff if trial <= 200 else np.zeros_like(t)
    if trial > 197 and trial <= 200:
        inp = reaff + novel
    r = inp - w @ basis
    w += eta * (basis @ r) / basis.sum(1).mean()
    resp[trial] = r
fig, axs = plt.subplots(1, 3, figsize=(11.5, 3.5), sharey=True)
for k, col in ((1, P.edge("negative")), (10, P.edge("rna")), (100, P.edge("dna"))):
    axs[0].plot(t, resp[k], color=col, lw=1.8, label=f"trial {k}")
axs[0].set_title("A  Predictable input is canceled", loc="left", fontweight="bold", fontsize=9.5)
axs[0].legend(frameon=False, fontsize=7.5)
axs[1].plot(t, resp[200], color=P.edge("dna"), lw=1.8, label="response, trial 200")
axs[1].plot(t, novel, color=P.muted(), lw=1, ls="--", label="novel signal alone")
axs[1].set_title("B  A novel signal stands out", loc="left", fontweight="bold", fontsize=9.5)
axs[1].legend(frameon=False, fontsize=7.5)
for k, col in ((201, P.edge("negative")), (215, P.edge("rna")), (260, P.edge("dna"))):
    axs[2].plot(t, resp[k], color=col, lw=1.8, label=f"{k - 200} trials after removal")
axs[2].set_title("C  Negative afterimage", loc="left", fontweight="bold", fontsize=9.5)
axs[2].legend(frameon=False, fontsize=7.5)
for ax in axs:
    ax.axhline(0, color=P.muted(), lw=0.5)
    ax.set_xlabel("Time after EOD command / ms")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
axs[0].set_ylabel("Response (rel.)")
fig.tight_layout()
