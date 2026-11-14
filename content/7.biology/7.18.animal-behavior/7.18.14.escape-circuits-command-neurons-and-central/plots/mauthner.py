"""Why only one Mauthner cell fires: a two-cell leaky integrate-and-fire model.

Each Mauthner cell (M) receives an abrupt sound-evoked excitation from its own ear; the left
input is 6 % stronger (sound source on the left) and both carry noise. When an M cell fires,
(i) feedback inhibition through interneurons (cranial relay / PHP neurons) clamps both cells near
the chloride reversal potential for ~15 ms, and (ii) the spike crosses the midline to excite the
contralateral motor neurons. Without inhibition both cells may fire, giving a bilateral
contraction and no turn. Time constants and amplitudes are illustrative.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
dt = 0.02  # ms
t = np.arange(0, 20, dt)


def run(inhib, seed):
    rng = np.random.default_rng(seed)
    V = np.zeros((2, len(t)))
    v = np.array([0.0, 0.0])
    tau, thr = 2.0, 1.0
    inh_until = -1
    spikes = [[], []]
    for k, tk in enumerate(t):
        drive = np.zeros(2)
        if tk > 3:
            x = tk - 3
            drive = np.array([1.06, 1.0]) * 3.6 * (1 - np.exp(-x / 0.8)) * np.exp(-x / 4.0)
        noise = rng.normal(0, 0.5, 2) * np.sqrt(dt)
        if inhib and tk < inh_until:
            v = v + dt / 0.3 * (-0.35 - v) + 0.02 * noise
        else:
            v = v + dt / tau * (-v + drive) + 0.08 * noise
        for i in range(2):
            if v[i] >= thr:
                spikes[i].append(tk)
                v[i] = -0.4
                if inhib:
                    inh_until = tk + 15
        V[:, k] = v
    return V, spikes


fig, axs = plt.subplots(2, 2, figsize=(10.5, 4.6), sharex=True, sharey=True)
for row, inhib in enumerate((True, False)):
    for colm, seed in enumerate((3, 8)):
        ax = axs[row, colm]
        V, sp = run(inhib, seed)
        ax.plot(t, V[0] + 1.6, color=P.edge("dna"), lw=1.2)
        ax.plot(t, V[1], color=P.edge("rna"), lw=1.2)
        for i, off in ((0, 1.6), (1, 0.0)):
            for s in sp[i]:
                ax.plot([s, s], [off + 1.0, off + 1.5], color=P.edge("dna") if i == 0 else P.edge("rna"), lw=1.5)
        ax.axvline(3, color=P.muted(), lw=0.6, ls=":")
        ax.set_yticks([0, 1.6]); ax.set_yticklabels(["right M", "left M"])
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
        nl, nr = len(sp[0]), len(sp[1])
        out = ("left M fires: C-bend to the right" if nl and not nr else
               "right M fires: C-bend to the left" if nr and not nl else
               "both fire: no directed turn" if nl and nr else "no response")
        ax.text(19.5, 2.9, out, ha="right", fontsize=8, color=P.ink())
axs[0, 0].set_title("A  With feedback inhibition (two trials)", loc="left", fontweight="bold", fontsize=10)
axs[1, 0].set_title("B  Inhibition blocked (same inputs)", loc="left", fontweight="bold", fontsize=10)
axs[1, 0].set_xlabel("Time / ms"); axs[1, 1].set_xlabel("Time / ms")
axs[0, 0].text(3.2, -0.6, "sound onset", fontsize=7, color=P.muted())
fig.tight_layout()
