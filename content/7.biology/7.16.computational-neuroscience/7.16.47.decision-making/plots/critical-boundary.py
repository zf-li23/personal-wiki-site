"""Speed and accuracy of the Wong-Wang network near the critical boundary.

Same reduced model and parameters as wong-wang.py, except that the recurrent self-excitation J_s
is varied (J_c = 0.0497 nA, I_0 = 0.3255 nA, mu_0 = 30 Hz, sigma = 0.02 nA, threshold 15 Hz).
A: eigenvalues of the symmetric fixed point with the stimulus on (c' = 0), computed from the
   Jacobian: the difference mode (S_1 - S_2) and the sum mode (S_1 + S_2). The difference-mode
   eigenvalue crosses zero near J_s = 0.222 nA (pitchfork: below it the symmetric state is
   stable and the network does not decide); its inverse is the time over which the network
   integrates the difference of its inputs. Above J_s = 0.277 nA it becomes negative again: the
   symmetric state is then a stable state with both populations at high rates.
B: fraction correct at coherence c' = 3.2 % and mean decision time (250 trials per point,
   trials lasting 3 s; undecided trials excluded) against J_s: close to the boundary the network
   integrates slowly and decides accurately, far from it quickly and less accurately.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
a, b, d, gam, tauS, tauA = 270.0, 108.0, 0.154, 0.641, 0.1, 0.002
Jc, I0, sig, Jext, mu0 = 0.0497, 0.3255, 0.02, 5.2e-4, 30.0
dt = 0.0005


def H(x):
    y = a * x - b
    return y / (1 - np.exp(-d * y))


def dH(x, e=1e-7):
    return (H(x + e) - H(x - e)) / (2 * e)


def modes(Js):
    """Eigenvalues (difference, sum) of the symmetric fixed point with the stimulus on."""
    I = Jext * mu0
    f = lambda s: -s / tauS + (1 - s) * gam * H((Js - Jc) * s + I0 + I)
    ss = np.linspace(1e-4, 0.99, 2000)
    v = f(ss)
    i = np.nonzero(v[:-1] * v[1:] < 0)[0][0]
    s = brentq(f, ss[i], ss[i + 1])
    x = (Js - Jc) * s + I0 + I
    A = -1 / tauS - gam * H(x) + (1 - s) * gam * dH(x) * Js
    B = -(1 - s) * gam * dH(x) * Jc
    return A - B, A + B


def run(Js, coh, n, T=3.0):
    S = np.full((n, 2), 0.1)
    In = np.zeros((n, 2))
    I = Jext * mu0 * np.array([1 + coh / 100, 1 - coh / 100])
    choice = np.zeros(n)
    tdec = np.full(n, np.nan)
    for k in range(int(T / dt)):
        r = H(Js * S - Jc * S[:, ::-1] + I0 + I + In)
        new = np.isnan(tdec) & (r.max(axis=1) > 15)
        tdec[new] = k * dt
        choice[new] = np.where(r[new, 0] > r[new, 1], 1, 2)
        S += dt * (-S / tauS + (1 - S) * gam * r)
        In += dt / tauA * (-In) + np.sqrt(dt / tauA) * sig * rng.standard_normal((n, 2))
    return choice, tdec


fig, axs = plt.subplots(1, 2, figsize=(10.5, 3.9))
jj = np.linspace(0.20, 0.30, 81)
lam = np.array([modes(j) for j in jj])
ax = axs[0]
ax.plot(jj, lam[:, 0], color=P.edge("dna"), lw=2, label="difference mode")
ax.plot(jj, lam[:, 1], color=P.edge("neutral"), lw=1.6, ls="--", label="sum mode")
ax.axhline(0, color=P.ink(), lw=0.8)
ax.axvline(0.2609, color=P.muted(), lw=1, ls=":")
ax.text(0.2615, -12.5, "standard\nparameters", fontsize=8, color=P.muted())
ax.text(0.201, -9.5, "symmetric state\nstable: no\ndecision", fontsize=8, color=P.muted())
ax.text(0.281, 1.0, "both high:\nno decision", fontsize=8, color=P.muted())
ax.set_xlabel("Self-excitation $J_s$ / nA")
ax.set_ylabel("Eigenvalue / s$^{-1}$")
ax.set_title("A  Modes of the symmetric state", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="upper left")

js = np.array([0.225, 0.23, 0.24, 0.25, 0.26, 0.27])
acc, mdt = [], []
for j in js:
    ch, td = run(j, 3.2, 250)
    acc.append(np.mean(ch[ch > 0] == 1))
    mdt.append(np.nanmean(td))
ax = axs[1]
ax.plot(js, acc, "o-", color=P.edge("dna"), lw=1.8)
ax.set_xlabel("Self-excitation $J_s$ / nA")
ax.set_ylabel("Fraction correct (c' = 3.2 %)", color=P.edge("dna"))
ax2 = ax.twinx()
ax2.plot(js, np.array(mdt) * 1000, "s--", color=P.edge("negative"), lw=1.5)
ax2.set_ylabel("Mean decision time / ms", color=P.edge("negative"))
ax.set_title("B  Accuracy and speed", loc="left", fontsize=10)
for a_ in axs:
    a_.grid(True, alpha=0.3)
fig.tight_layout()
