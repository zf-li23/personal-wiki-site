"""A depressing synapse reports relative changes of the presynaptic rate (gain control).

Tsodyks-Markram synapse with U = 0.5, tau_d = 800 ms, tau_f = 20 ms driven by regular trains
whose rate steps up by a factor of 2 at t = 0 (10 -> 20 Hz, 50 -> 100 Hz). The transmitted rate
is r u x: the release per spike times the instantaneous rate 1/ISI, normalized to its value
before the step. After a transient of height close to 2 in both cases it returns to the same
steady value (about 1/tau_d), whatever the absolute rate.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
U, td, tf = 0.5, 800.0, 20.0


def run(r0, r1, t_pre=2500.0, t_post=2500.0):
    times = []
    t = -t_pre
    while t < 0:
        times.append(t)
        t += 1000.0 / r0
    t = 0.0
    while t < t_post:
        times.append(t)
        t += 1000.0 / r1
    u, x, last = 0.0, 1.0, None
    out_t, out_r = [], []
    for k, ts in enumerate(times):
        if last is not None:
            d = ts - last
            u *= np.exp(-d / tf)
            x = 1 + (x - 1) * np.exp(-d / td)
        u = u + U * (1 - u)
        rel = u * x
        x -= rel
        if k + 1 < len(times):
            rate = 1000.0 / (times[k + 1] - ts)
        else:
            rate = 1000.0 / (ts - last)
        out_t.append(ts)
        out_r.append(rate * rel)
        last = ts
    out_t, out_r = np.array(out_t), np.array(out_r)
    pre = out_r[(out_t > -600) & (out_t < 0)].mean()
    return out_t, out_r / pre


fig, axs = plt.subplots(1, 3, figsize=(12.5, 3.7))
for ax, (r0, r1, c) in zip(axs[:2], ((10, 20, P.edge("dna")), (50, 100, P.edge("negative")))):
    t, y = run(r0, r1)
    ax.step(t, y, where="post", color=c, lw=1.6)
    ax.axvline(0, color=P.muted(), lw=0.8, ls=":")
    ax.axhline(1, color=P.muted(), lw=0.6)
    ax.set_xlim(-1000, 2500)
    ax.set_ylim(0.8, 1.15 * y[t > -1000].max())
    ax.set_xlabel("Time from rate step / ms")
    ax.set_ylabel("Transmitted rate / pre-step value")
    ax.set_title(f"{'AB'[(r0 == 50)]}  {r0} to {r1} Hz", loc="left", fontsize=10)
    ax.grid(True, alpha=0.3)
ax = axs[2]
ratios = np.linspace(1.1, 4, 12)
for r0, c in ((10, P.edge("dna")), (50, P.edge("negative"))):
    peaks = []
    for q in ratios:
        t, y = run(r0, r0 * q, t_pre=2500, t_post=1500)
        peaks.append(y[t >= 0].max())
    ax.plot(ratios, peaks, "o-", ms=4, lw=1.4, color=c, label=f"from {r0} Hz")
ax.plot(ratios, ratios, color=P.muted(), lw=0.8, ls="--", label="peak = rate ratio")
ax.set_xlabel("Rate ratio $r_1/r_0$")
ax.set_ylabel("Peak transmitted rate / pre-step value")
ax.set_title("C  Peak depends on the ratio", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8)
ax.grid(True, alpha=0.3)
fig.tight_layout()
