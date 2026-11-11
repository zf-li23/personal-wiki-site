"""The reduced two-variable model of perceptual decisions (Wong and Wang, 2006).

S_1, S_2: NMDA gating variables of two selective populations (Formula 47.4.1).
  x_i = J_s S_i - J_c S_j + I_0 + I_i + I_noise,i,   H(x) = (a x - b) / (1 - exp(-d (a x - b))),
  dS_i/dt = -S_i / tau_S + (1 - S_i) gamma H(x_i),
  tau_AMPA dI_noise/dt = -I_noise + sqrt(tau_AMPA) sigma eta(t)  (white noise eta),
a = 270 Hz/nA, b = 108 Hz, d = 0.154 s, gamma = 0.641, tau_S = 100 ms, tau_AMPA = 2 ms,
J_s = 0.2609 nA, J_c = 0.0497 nA, I_0 = 0.3255 nA, sigma = 0.02 nA;
stimulus I_{1,2} = J_ext mu_0 (1 +- c'/100), J_ext = 5.2e-4 nA/Hz, mu_0 = 30 Hz, on from t = 0;
decision when one rate H(x_i) first exceeds 15 Hz. Euler-Maruyama, dt = 0.5 ms.
A: rates of the two populations in 4 trials at coherence c' = 6.4 %: slow ramping, then
   winner-take-all.
B: phase plane (S_1, S_2) at c' = 0 with the stimulus on: nullclines (dS_1/dt = 0 blue,
   dS_2/dt = 0 red), two stable decision states (filled), the saddle (open square) whose stable
   manifold divides their basins, and five noisy trajectories from the initial state, which are
   deflected toward a decision state before they reach the saddle.
C: psychometric function (fraction choosing population 1) and mean decision time against
   coherence, 250 trials per coherence (vectorized). Rates in A are smoothed with a 20 ms window.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
a, b, d, gam, tauS, tauA = 270.0, 108.0, 0.154, 0.641, 0.1, 0.002
Js, Jc, I0, sig, Jext, mu0 = 0.2609, 0.0497, 0.3255, 0.02, 5.2e-4, 30.0
dt = 0.0005


def H(x):
    y = a * x - b
    return y / (1 - np.exp(-d * y))


def run(coh, n, T=2.0, keep=False):
    S = np.full((n, 2), 0.1)
    In = np.zeros((n, 2))
    I = Jext * mu0 * np.array([1 + coh / 100, 1 - coh / 100])
    choice = np.zeros(n)
    tdec = np.full(n, np.nan)
    hist = []
    for k in range(int(T / dt)):
        x = Js * S - Jc * S[:, ::-1] + I0 + I + In
        r = H(x)
        if keep:
            hist.append(r.copy())
        new = np.isnan(tdec) & (r.max(axis=1) > 15)
        tdec[new] = k * dt
        choice[new] = np.where(r[new, 0] > r[new, 1], 1, 2)
        S += dt * (-S / tauS + (1 - S) * gam * r)
        In += dt / tauA * (-In) + np.sqrt(dt / tauA) * sig * rng.standard_normal((n, 2))
    return choice, tdec, np.array(hist)


fig, axs = plt.subplots(1, 3, figsize=(14, 4.0))
ch, td, hist = run(6.4, 4, T=1.5, keep=True)
t = np.arange(hist.shape[0]) * dt
kern = np.ones(40) / 40  # 20 ms boxcar smoothing for display
for i in range(4):
    for j, col in ((0, P.edge("dna")), (1, P.edge("negative"))):
        sm = np.convolve(hist[:, i, j], kern, mode="valid")
        axs[0].plot(t[: sm.size] + 0.01, sm, color=col, lw=1.4)
axs[0].axhline(15, color=P.muted(), ls="--", lw=1)
axs[0].text(0.02, 16.5, "decision threshold", fontsize=8, color=P.muted())
axs[0].plot([], [], color=P.edge("dna"), label="population 1 (favored)")
axs[0].plot([], [], color=P.edge("negative"), label="population 2")
axs[0].set_xlabel("Time from stimulus onset / s")
axs[0].set_ylabel("Rate / Hz")
axs[0].set_title("A  Ramping and winner-take-all", loc="left", fontsize=10)
axs[0].legend(frameon=False, fontsize=8, loc="upper left")

ax = axs[1]
I = Jext * mu0 * np.array([1.0, 1.0])
g = np.linspace(0, 0.8, 300)
S1, S2 = np.meshgrid(g, g)


def field(s1, s2):
    x1 = Js * s1 - Jc * s2 + I0 + I[0]
    x2 = Js * s2 - Jc * s1 + I0 + I[1]
    return -s1 / tauS + (1 - s1) * gam * H(x1), -s2 / tauS + (1 - s2) * gam * H(x2)


F1, F2 = field(S1, S2)
ax.contour(S1, S2, F1, levels=[0], colors=[P.edge("dna")], linewidths=2)
ax.contour(S1, S2, F2, levels=[0], colors=[P.edge("negative")], linewidths=2)
sk = slice(None, None, 25)
U, V = field(S1[sk, sk], S2[sk, sk])
nrm = np.hypot(U, V) + 1e-9
ax.quiver(S1[sk, sk], S2[sk, sk], U / nrm, V / nrm, color=P.muted(), alpha=0.6, width=0.003)
pts = []
for guess in ((0.7, 0.05), (0.05, 0.7), (0.3, 0.3), (0.1, 0.1), (0.6, 0.6)):
    sol, info, ok, _ = fsolve(lambda s: field(s[0], s[1]), guess, full_output=True)
    if ok == 1 and not any(np.allclose(sol, p, atol=1e-4) for p in pts) and (0 <= sol).all() and (sol <= 1).all():
        pts.append(sol)
for p in pts:
    eps = 1e-6
    Jm = np.array([[(field(p[0] + eps, p[1])[i] - field(p[0] - eps, p[1])[i]) / (2 * eps),
                    (field(p[0], p[1] + eps)[i] - field(p[0], p[1] - eps)[i]) / (2 * eps)] for i in range(2)])
    ev = np.linalg.eigvals(Jm).real
    if (ev < 0).all():
        ax.plot(*p, "o", ms=9, color=P.ink())
    else:
        ax.plot(*p, "s", ms=8, mfc="none", mec=P.ink(), mew=2)
# trajectories in (S1, S2): rerun storing S
for i in range(5):
    S = np.array([0.1, 0.1])
    In = np.zeros(2)
    tr = [S.copy()]
    for k in range(int(1.5 / dt)):
        x = Js * S - Jc * S[::-1] + I0 + I + In
        S = S + dt * (-S / tauS + (1 - S) * gam * H(x))
        In += dt / tauA * (-In) + np.sqrt(dt / tauA) * sig * rng.standard_normal(2)
        tr.append(S.copy())
    tr = np.array(tr)
    ax.plot(tr[:, 0], tr[:, 1], color=P.edge("positive"), lw=1.0)
ax.set_xlim(0, 0.8)
ax.set_ylim(0, 0.8)
ax.set_aspect("equal")
ax.set_xlabel("$S_1$")
ax.set_ylabel("$S_2$")
ax.set_title("B  Phase plane, c' = 0", loc="left", fontsize=10)

cohs = np.array([-25.6, -12.8, -6.4, -3.2, 0.0, 3.2, 6.4, 12.8, 25.6])
pc, mt = [], []
for coh in cohs:
    ch, td, _ = run(coh, 250)
    pc.append(np.mean(ch == 1))
    mt.append(np.nanmean(td))
ax = axs[2]
ax.plot(cohs, pc, "o-", color=P.edge("dna"), lw=1.8, label="P(choose 1)")
ax.set_xlabel("Coherence c' / %")
ax.set_ylabel("Fraction choosing population 1", color=P.edge("dna"))
ax2 = ax.twinx()
ax2.plot(cohs, np.array(mt) * 1000, "s--", color=P.edge("negative"), lw=1.5, label="Decision time")
ax2.set_ylabel("Mean decision time / ms", color=P.edge("negative"))
ax.set_title("C  Choices and decision times", loc="left", fontsize=10)
for a_ in axs:
    a_.grid(True, alpha=0.3)
fig.tight_layout()
