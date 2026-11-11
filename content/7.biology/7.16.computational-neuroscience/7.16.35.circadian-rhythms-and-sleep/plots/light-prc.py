"""Phase response curve of the Goodwin clock to a light pulse that induces transcription.

Same model as goodwin-clock.py (b = 0.15 / h, h = 12); a 1-h pulse adds L to the transcription rate,
as light induces Per transcription in the SCN. Circadian time CT 0 is set 6 h before the mRNA peak
(the peak of Per mRNA in the SCN is near CT 6). Phase shifts are measured from mRNA peaks 6 cycles later.
All pulse times are integrated in parallel with fixed-step RK4.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
b, h, dt = 0.15, 12.0, 0.05


def f(y, light):
    M, Pc, Pn = y
    return np.array([1.0 / (1.0 + Pn ** h) + light - b * M, b * (M - Pc), b * (Pc - Pn)])


def run(y0, t_on, L, T, record_from):
    """Integrate a batch (one column per pulse time); return times and M after record_from."""
    y = np.repeat(np.asarray(y0, float)[:, None], len(t_on), axis=1)
    n = int(T / dt)
    s = int(record_from / dt)
    Ms = np.empty((n - s, len(t_on)))
    for i in range(n):
        t = i * dt
        lt = np.where((t_on <= t) & (t < t_on + 1.0), L, 0.0)
        lm = np.where((t_on <= t + dt / 2) & (t + dt / 2 < t_on + 1.0), L, 0.0)
        k1 = f(y, lt)
        k2 = f(y + 0.5 * dt * k1, lm)
        k3 = f(y + 0.5 * dt * k2, lm)
        k4 = f(y + dt * k3, lm)
        y = y + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        if i >= s:
            Ms[i - s] = y[0]
    return np.arange(s, n) * dt, Ms


def last_peak(t, m):
    idx = np.where((m[1:-1] > m[:-2]) & (m[1:-1] > m[2:]))[0] + 1
    return t[idx[-1]]


# settle onto the limit cycle and start at an mRNA peak
t, Ms = run([0.5, 0.5, 0.5], np.array([-1e9]), 0.0, 900.0, 600.0)
m = Ms[:, 0]
pk = t[np.where((m[1:-1] > m[:-2]) & (m[1:-1] > m[2:]))[0] + 1]
tau = np.mean(np.diff(pk))
# a state on the limit cycle; its first mRNA peak p0 anchors circadian time
y = np.full(3, 0.5)
for i in range(int(600.0 / dt)):
    y = y + dt * f(y, 0.0)
cts = np.linspace(0, 24, 49)
T = 7 * tau
ct_peak = 6.0
fig, ax = plt.subplots(figsize=(7.5, 3.6))
tr, Mr = run(y, np.array([-1e9]), 0.0, T, T - 1.5 * tau)
ref = last_peak(tr, Mr[:, 0])
first = run(y, np.array([-1e9]), 0.0, 1.5 * tau, 0.0)
p0 = first[0][np.where((first[1][1:-1, 0] > first[1][:-2, 0]) & (first[1][1:-1, 0] > first[1][2:, 0]))[0] + 1][0]
for L, tok in [(0.25, "dna"), (0.5, "negative")]:
    t_on = p0 + (cts - ct_peak) * tau / 24.0 + tau - 0.5
    tt, MM = run(y, t_on, L, T, T - 1.5 * tau)
    shifts = []
    for j in range(len(cts)):
        d = (ref - last_peak(tt, MM[:, j]) + tau / 2) % tau - tau / 2
        shifts.append(d * 24.0 / tau)
    ax.plot(cts, shifts, "o-", color=P.edge(tok), ms=3.5, lw=1.6, label=f"pulse strength $L = {L}$")
ax.axhline(0, color=P.muted(), lw=0.8)
ax.axvspan(12, 24, color=P.light("neutral"), zorder=0)
yl = ax.get_ylim()
ax.text(6, yl[1] - 0.1 * (yl[1] - yl[0]), "subjective day", ha="center", fontsize=8.5, color=P.muted())
ax.text(18, yl[1] - 0.1 * (yl[1] - yl[0]), "subjective night", ha="center", fontsize=8.5, color=P.muted())
ax.set_xticks(np.arange(0, 25, 4))
ax.set_xlim(0, 24)
ax.set_xlabel("Circadian time of the 1-h light pulse / CT h")
ax.set_ylabel("Phase shift / h (advance > 0)")
ax.legend(frameon=False, fontsize=8, loc="lower left")
ax.grid(True, alpha=0.3)
fig.tight_layout()
