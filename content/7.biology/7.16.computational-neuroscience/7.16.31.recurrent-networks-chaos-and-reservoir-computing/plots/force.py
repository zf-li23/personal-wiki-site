"""FORCE learning in a chaotic rate network (Sussillo and Abbott, 2009).

tau dx/dt = -x + g J r + w_f z,  r = tanh(x),  z = w^T r,
N = 300, g = 1.5, J_ij ~ N(0, 1/N), w_f uniform in [-1, 1], tau = 10 ms, Euler step 1 ms.
Target f(t): sum of four sines with fundamental period 600 ms.
Recursive least squares every 2 ms: e = z - f, k = P r / (1 + r^T P r), P <- P - k r^T P, w <- w - e k,
P(0) = I / alpha with alpha = 1.
Phases: 1 s spontaneous (chaotic), 20 s training, 3 s testing with the weights fixed.
A: output z (orange) and target (black) before, at the start of and after training.
B: size of the weight update |dw| per step during training.
C: rates of four network units: irregular before training, periodic afterwards.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
N, g, tau, dt = 300, 1.5, 10.0, 1.0
J = rng.normal(0, 1 / np.sqrt(N), (N, N))
wf = rng.uniform(-1, 1, N)
w = np.zeros(N)
Pm = np.eye(N)
x = rng.normal(0, 0.5, N)
T0, T1, T2 = 1000, 21000, 24000
t = np.arange(T2) * dt
per = 600.0
f = (np.sin(2 * np.pi * t / per) + 0.5 * np.sin(4 * np.pi * t / per)
     + (1 / 3) * np.sin(6 * np.pi * t / per) + 0.25 * np.sin(8 * np.pi * t / per)) / 1.5
z_rec = np.zeros(T2)
r_rec = np.zeros((T2, 4))
dw = np.full(T2, np.nan)
for k in range(T2):
    r = np.tanh(x)
    z = w @ r
    z_rec[k] = z
    r_rec[k] = r[:4]
    if T0 <= k < T1 and k % 2 == 0:
        Pr = Pm @ r
        kk = Pr / (1 + r @ Pr)
        Pm -= np.outer(kk, Pr)
        e = z - f[k]
        w -= e * kk
        dw[k] = np.linalg.norm(e * kk)
    x = x + dt / tau * (-x + g * J @ r + wf * z)

fig = plt.figure(figsize=(13, 5.6))
gs = fig.add_gridspec(2, 2, width_ratios=[2.3, 1])
ax = fig.add_subplot(gs[0, 0])
ax.plot(t / 1000, f, color=P.ink(), lw=1.4, label="target $f(t)$")
ax.plot(t / 1000, z_rec, color=P.edge("rna"), lw=1.0, label="output $z(t)$")
for xv in (T0, T1):
    ax.axvline(xv / 1000, color=P.muted(), lw=0.8, ls=":")
ax.text(0.5, 2.1, "spontaneous", ha="center", fontsize=8, color=P.muted())
ax.text(11, 2.1, "training (RLS on)", ha="center", fontsize=8, color=P.muted())
ax.text(22.5, 2.1, "test (weights fixed)", ha="center", fontsize=8, color=P.muted())
ax.set_ylim(-2.5, 2.5)
ax.set_ylabel("Output")
ax.set_title("A  Output and target", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="lower left", ncol=2)
ax = fig.add_subplot(gs[1, 0], sharex=ax)
cols = [P.edge("dna"), P.edge("negative"), P.edge("positive"), P.edge("protein")]
for j in range(4):
    ax.plot(t / 1000, r_rec[:, j] + 2.2 * j, color=cols[j], lw=0.8)
for xv in (T0, T1):
    ax.axvline(xv / 1000, color=P.muted(), lw=0.8, ls=":")
ax.set_yticks([])
ax.set_xlabel("Time / s")
ax.set_ylabel("Unit rates (offset)")
ax.set_title("C  Network units", loc="left", fontsize=10)
ax = fig.add_subplot(gs[:, 1])
m = ~np.isnan(dw)
ax.semilogy(t[m] / 1000, dw[m], color=P.edge("dna"), lw=0.6)
ax.set_xlabel("Time / s")
ax.set_ylabel("$\\|\\Delta \\boldsymbol{w}\\|$ per update")
ax.set_title("B  Weight changes shrink", loc="left", fontsize=10)
for a_ in fig.axes:
    a_.grid(True, alpha=0.3)
fig.tight_layout()
