"""Borbely two-process model of sleep regulation.

Process S (sleep pressure) rises during wakefulness, S <- 1 - (1 - S) exp(-dt / tau_w),
and decays during sleep, S <- S exp(-dt / tau_s), with tau_w = 18.2 h and tau_s = 4.2 h
(Daan, Beersma and Borbely 1984). Process C, the circadian rhythm from the suprachiasmatic
nucleus, modulates an upper threshold H(t) = 0.60 + 0.10 C(t) at which sleep begins and a lower
threshold L(t) = 0.17 + 0.10 C(t) at which waking occurs, C(t) = sin(2 pi (t - 11.5 h) / 24 h)
(clock time t). A: three normal days. B: one night of sleep deprivation (kept awake from 7:00 on day 1 to
23:00 on day 2, 40 h), followed by recovery sleep.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
tw, ts, dt = 18.2, 4.2, 0.01


def C(t):
    return np.sin(2 * np.pi * (t - 11.5) / 24)


def run(T=96, deprive=None):
    n = int(T / dt)
    t = np.arange(n) * dt + 7.0
    S = np.zeros(n)
    asleep = np.zeros(n, bool)
    s, sl = 0.2, False
    for i in range(n):
        H = 0.60 + 0.10 * C(t[i])
        L = 0.17 + 0.10 * C(t[i])
        forced = deprive is not None and deprive[0] <= t[i] < deprive[1]
        if sl:
            s *= np.exp(-dt / ts)
            if s <= L:
                sl = False
        else:
            s = 1 - (1 - s) * np.exp(-dt / tw)
            if s >= H and not forced:
                sl = True
        S[i], asleep[i] = s, sl
    return t, S, asleep


fig, axes = plt.subplots(2, 1, figsize=(11, 5.6), sharex=True)
for ax, dep, title in ((axes[0], None, "A  Normal days: about 16 h awake, 8 h asleep"),
                       (axes[1], (20, 47), "B  A night without sleep, then recovery")):
    t, S, sl = run(deprive=dep)
    ax.plot(t, 0.60 + 0.10 * C(t), color=P.muted(), lw=1, ls="--", label="H(t): sleep onset threshold")
    ax.plot(t, 0.17 + 0.10 * C(t), color=P.muted(), lw=1, ls=":", label="L(t): waking threshold")
    ax.plot(t, S, color=P.edge("rna"), lw=2, label="S")
    ax.fill_between(t, 0, 0.04, where=sl, color=P.edge("dna"), lw=0, step="mid")
    ax.set_ylim(0, 1.0)
    ax.set_ylabel("Sleep pressure S")
    ax.set_title(title, loc="left", fontsize=10)
    ax.grid(True, alpha=0.3)
    if dep:
        ax.axvspan(*dep, color=P.muted(), alpha=0.12, lw=0)
        ax.text((dep[0] + dep[1]) / 2, 0.92, "kept awake", ha="center", fontsize=8,
                color=P.muted())
        i = np.where(sl & (t > dep[1]))[0]
        print("recovery sleep from", t[i[0]], "S", S[i[0]])
    bouts = np.diff(sl.astype(int))
    on = t[1:][bouts == 1]
    off = t[1:][bouts == -1]
    print(title, "sleep on", np.round(on % 24, 1), "off", np.round(off % 24, 1))
axes[0].legend(frameon=False, fontsize=8, loc="upper right", ncol=3)
axes[1].text(98, 0.06, "bars: sleep", fontsize=8, color=P.edge("dna"), ha="right")
axes[1].set_xlabel("Time / h (clock time of day 1 = 7:00 at start)")
axes[1].set_xticks(np.arange(12, 104, 12))
axes[1].set_xticklabels([f"{int(v % 24)}:00\nday {int(v // 24) + 1}" for v in np.arange(12, 104, 12)],
                        fontsize=8)
fig.tight_layout()
