"""Learning-rate schedules over a run of T = 10000 steps with peak rate 1:
step decay, exponential decay, linear warmup followed by cosine decay,
warmup-stable-decay (WSD), and the inverse square root schedule of the
original Transformer."""

import numpy as np
import matplotlib.pyplot as plt

T, warm = 10000, 500
t = np.arange(T + 1)
step = 0.1 ** np.floor(t / 4000)
expo = 0.9997 ** t
warmup = np.minimum(1.0, t / warm)
cosine = np.where(t < warm, t / warm,
                  0.1 + 0.9 * 0.5 * (1 + np.cos(np.pi * (t - warm) / (T - warm))))
decay_start = int(0.8 * T)
wsd = np.where(t < warm, t / warm,
               np.where(t < decay_start, 1.0, 1 - 0.99 * (t - decay_start) / (T - decay_start)))
inv_sqrt = np.minimum(np.maximum(t, 1) / warm, np.sqrt(warm / np.maximum(t, 1)))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.0))
ax1.plot(t, step, lw=1.6, label="step decay (x0.1 every 4000 steps)")
ax1.plot(t, expo, "--", lw=1.6, label="exponential decay")
ax1.plot(t, cosine, lw=1.6, label="warmup + cosine (to 10%)")
ax1.plot(t, wsd, "-.", lw=1.6, label="warmup-stable-decay (last 20%)")
ax1.plot(t, inv_sqrt, ":", lw=1.8, label="warmup + inverse square root")
ax1.set_xlabel("step")
ax1.set_ylabel("learning rate / peak")
ax1.set_title("schedules", fontsize=10)
ax1.legend(fontsize=8)
ax1.grid(alpha=0.3)
ax2.plot(t[:1500], cosine[:1500], lw=1.6, color="C2", label="linear warmup, 500 steps")
ax2.plot(t[:1500], inv_sqrt[:1500], ":", lw=1.8, color="C4", label="inverse square root")
ax2.set_xlabel("step")
ax2.set_title("the first 1500 steps", fontsize=10)
ax2.legend(fontsize=8)
ax2.grid(alpha=0.3)
fig.tight_layout()
