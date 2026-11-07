# Asynchronous flight muscle as a delayed-stretch-activation oscillator (minimal model, illustrative).
# Thorax plus wings: a damped mass-spring system, coordinate x (deformation of the thorax; x > 0 stretches the
# dorsal longitudinal muscles, DLM, and shortens the dorso-ventral muscles, DVM):
#   m x'' + c x' + k x = -K (A_DLM - A_DVM)
# Stretch activation with delay: each muscle's active force A follows its own stretch with a first-order lag,
#   tau A_DLM' = s(x) - A_DLM,   tau A_DVM' = s(-x) - A_DVM,   s(u) = max(0, tanh(u / x0)),
# so force lags length and does net positive work on the thorax (negative damping). K is the activation set by
# the myoplasmic Ca2+ level that sparse motor spikes maintain (no Ca2+ cycling per beat).
# Units: m = 1, k = (2 pi 150 Hz)^2 so that the passive resonance is 150 Hz; c gives Q = 10; tau = 1 ms.
# (A) the wing-beat oscillation at about 150 Hz with motor spikes at only 10 Hz; (B) the beat frequency follows
#     the mechanical resonance sqrt(k/m) as wing mass is added (classic wing-loading experiments), not the
#     spike rate; (C) oscillation amplitude against activation K: a threshold (Hopf bifurcation) where the
#     negative damping of the delayed stretch activation exceeds the passive damping.
import matplotlib.pyplot as plt
import numpy as np

f0 = 150.0
k = (2 * np.pi * f0) ** 2
c = 2 * np.pi * f0 / 10
tau, x0 = 1.0e-3, 1.0


def run(K, m=1.0, T=0.4, dt=2e-6, kick=0.05):
    n = int(T / dt)
    x, v, a1, a2 = kick, 0.0, 0.0, 0.0
    xs = np.empty(n)
    kk = k
    for i in range(n):
        s1 = max(0.0, np.tanh(x / x0))
        s2 = max(0.0, np.tanh(-x / x0))
        acc = (-c * v - kk * x - K * (a1 - a2)) / m
        a1 += dt * (s1 - a1) / tau
        a2 += dt * (s2 - a2) / tau
        v += dt * acc
        x += dt * v
        xs[i] = x
    return np.arange(n) * dt, xs


def freq_amp(t, x):
    h = len(x) // 2
    xx = x[h:]
    tt = t[h:]
    up = np.where((xx[:-1] < 0) & (xx[1:] >= 0))[0]
    f = (len(up) - 1) / (tt[up[-1]] - tt[up[0]]) if len(up) > 2 else np.nan
    return f, (xx.max() - xx.min()) / 2


fig, (a, b, cax) = plt.subplots(1, 3, figsize=(13.5, 4.2))
Kop = 3.0 * k
t, x = run(Kop, T=0.12)
sel = t > 0.06
a.plot((t[sel] - 0.06) * 1000, x[sel] / np.abs(x[sel]).max(), color="#2f6fb5", lw=1.4, label="thorax / wing position")
a.plot([10.0, 10.0], [1.25, 1.55], color="#c0504d", lw=2.0)
a.text(12, 1.62, "one motor spike every 100 ms (10 Hz)", ha="left", fontsize=8.5, color="#c0504d")
a.set_xlim(0, 60)
a.set_ylim(-1.3, 1.85)
a.set_xlabel("Time / ms")
a.set_ylabel("Position (normalized)")
fa, _ = freq_amp(*run(Kop))
a.text(0.98, 0.06, f"wing-beat frequency ≈ {fa:.0f} Hz", transform=a.transAxes, ha="right", fontsize=8.5)
a.set_title("A   Many beats per motor spike", loc="left", fontsize=10)

ms = np.array([0.6, 0.8, 1.0, 1.3, 1.7, 2.2])
fs = [freq_amp(*run(Kop, m=mm))[0] for mm in ms]
mm = np.linspace(0.5, 2.4, 100)
b.plot(mm, f0 / np.sqrt(mm), color="0.5", lw=1.4, ls="--", label="passive resonance √(k/m) / 2π")
b.plot(ms, fs, "o", color="#2f6fb5", ms=6, label="model oscillation")
b.set_xlabel("Effective mass (relative; wings loaded or clipped)")
b.set_ylabel("Wing-beat frequency / Hz")
b.legend(frameon=False, fontsize=8.5)
b.set_title("B   Frequency set by mechanics", loc="left", fontsize=10)

Ks = np.linspace(0.0, 3.0, 16) * k
amps = []
for K in Ks:
    _, A = freq_amp(*run(K, T=0.3))
    amps.append(A)
cax.plot(Ks / k, amps, "o-", color="#c0504d", ms=4, lw=1.6)
cax.set_xlabel("Activation K / k (set by myoplasmic Ca²⁺)")
cax.set_ylabel("Oscillation amplitude (x / x₀)")
cax.set_title("C   Threshold of self-oscillation", loc="left", fontsize=10)
for ax in (a, b, cax):
    ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
