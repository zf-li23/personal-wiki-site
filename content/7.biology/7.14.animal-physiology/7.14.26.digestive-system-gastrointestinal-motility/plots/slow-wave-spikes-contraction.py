# Slow waves, spikes and contraction in gastrointestinal smooth muscle (illustrative waveform model).
# The ICC-driven slow wave (period 5 s, as in the duodenum) is a fast upstroke, a plateau and slow
# repolarization, amplitude 12 mV on a resting potential of -56 mV. A spike (Ca2+ action potential,
# about 15 ms) fires at 6 /s whenever V exceeds the electrical threshold (-40 mV). Ca2+ entry is
# 0.1 * max(V - V_mech, 0) with mechanical threshold V_mech = -48 mV, plus a pulse per spike; tension
# follows Ca2+ entry with a 1 s time constant. ACh (excitatory motor neurons) depolarizes by 8 mV;
# NO/ATP from inhibitory motor neurons hyperpolarizes by 8 mV. Contraction frequency is set by the
# slow wave, contraction strength by the number of spikes riding on each plateau.
import matplotlib.pyplot as plt
import numpy as np

dt = 0.001
t = np.arange(0, 15, dt)
T = 5.0


def slow_wave(t):
    ph = (t % T) / T
    w = np.where(ph < 0.05, ph / 0.05,
                 np.where(ph < 0.35, 1.0 - 0.15 * (ph - 0.05) / 0.3,
                          np.where(ph < 0.6, 0.85 * (1 - (ph - 0.35) / 0.25), 0.0)))
    return w


def run(shift):
    V = -56.0 + shift + 12.0 * slow_wave(t)
    spikes = np.zeros_like(t)
    last = -1.0
    for i, ti in enumerate(t):
        if V[i] > -40.0 and ti - last > 1 / 6:
            last = ti
            spikes[i] = 1
    Vs = V.copy()
    for i in np.nonzero(spikes)[0]:
        k = np.arange(i, min(i + 15, len(t)))
        Vs[k] += 30 * np.exp(-(t[k] - t[i]) / 0.005)
    drive = 0.1 * np.clip(V + 48.0, 0, None) + spikes / dt * 0.15
    F = np.zeros_like(t)
    for i in range(1, len(t)):
        F[i] = F[i - 1] + dt * (drive[i] - F[i - 1]) / 1.0
    return Vs, F


cases = (("Resting tone", 0.0), ("ACh (excitatory neurons)", 8.0), ("NO / ATP (inhibitory neurons)", -8.0))
fig, axs = plt.subplots(2, 3, figsize=(11, 4.8), sharex=True, sharey="row")
for j, (name, sh) in enumerate(cases):
    Vs, F = run(sh)
    a, b = axs[0, j], axs[1, j]
    a.plot(t, Vs, color="#2f6fb5", lw=1.1)
    a.axhline(-40, color="#c0392b", ls=":", lw=0.9)
    a.axhline(-48, color="#d9822b", ls=":", lw=0.9)
    a.set_title(name, fontsize=10)
    b.plot(t, F, color="#c0392b", lw=1.8)
    b.set_xlabel("Time / s")
    if j == 0:
        a.set_ylabel("V / mV")
        b.set_ylabel("Tension / a.u.")
        a.text(4.0, -39, "electrical threshold", ha="center", va="bottom", fontsize=7.5, color="#c0392b")
        a.text(4.0, -47.5, "mechanical threshold", ha="center", va="bottom", fontsize=7.5, color="#d9822b")
axs[0, 0].set_ylim(-68, 0)
fig.tight_layout()
