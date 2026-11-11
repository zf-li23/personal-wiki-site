"""Minimum-variance control with signal-dependent noise (Harris and Wolpert, 1998).

Plant: point mass (1 kg) driven by a muscle force f filtered from the command u:
tau1 tau2-type second-order muscle, here two first-order stages with tau1 = 40 ms, tau2 = 30 ms.
State s = (x, v, f1, f2); dt = 5 ms. The command is corrupted by noise whose s.d. is proportional
to its size: u_t (1 + kappa eps_t). The mean state must reach (A, 0, 0, 0) at time T; afterwards u = 0
for a hold period of 200 ms. The command minimizes the summed positional variance during the hold.
Because the variance is sum_t w_t u_t^2 and the constraints are linear, the optimum is
u = W^-1 G^T (G W^-1 G^T)^-1 s*.
A: optimal velocity profiles for A = 10 cm and T = 300, 450, 600 ms (bell-shaped).
B: endpoint s.d. against movement duration (s.d. proportional to A).
C: 20 simulated executions of the optimal command for T = 450 ms (kappa = 0.2): the scatter of
   the endpoints is the minimized variance.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import expm

import wikibio as bio

P = bio.P
dt = 0.005
t1, t2 = 0.04, 0.03
Ac = np.array([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, -1 / t1, 1 / t1], [0, 0, 0, -1 / t2]])
Bc = np.array([0, 0, 0, 1 / t2])
M = expm(np.block([[Ac, Bc[:, None]], [np.zeros((1, 5))]]) * dt)
Ad, Bd = M[:4, :4], M[:4, 4]
hold = int(0.2 / dt)
Ah = [np.linalg.matrix_power(Ad, h) for h in range(hold)]
kappa = 0.2


def solve(T, amp):
    N = int(round(T / dt))
    pw = [np.linalg.matrix_power(Ad, N - 1 - j) @ Bd for j in range(N)]
    G = np.array(pw).T  # 4 x N
    w = np.zeros(N)
    for h in range(hold):
        g = Ah[h][0] @ G  # position at hold step h per unit command
        w += g**2
    w *= kappa**2
    target = np.array([amp, 0, 0, 0])
    Wi = 1 / w
    lam = np.linalg.solve(G @ (Wi[:, None] * G.T), target)
    u = Wi * (G.T @ lam)
    var = np.sum(w * u**2) / hold
    s = np.zeros(4)
    vel = []
    for j in range(N):
        vel.append(s[1])
        s = Ad @ s + Bd * u[j]
    return np.array(vel), np.sqrt(var)


fig, axs = plt.subplots(1, 3, figsize=(13, 3.9))
ax = axs[0]
for T, col in zip((0.3, 0.45, 0.6), (P.edge("negative"), P.edge("positive"), P.edge("dna"))):
    v, sd = solve(T, 10.0)
    tt = np.arange(len(v)) * dt
    ax.plot(tt * 1000, v, color=col, lw=2.0, label=f"$T$ = {int(T * 1000)} ms")
ax.set_xlabel("Time / ms")
ax.set_ylabel("Velocity / cm s$^{-1}$")
ax.set_title("A  Optimal velocity profiles", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8)

Ts = np.arange(0.2, 0.81, 0.025)
sds = np.array([solve(T, 1.0)[1] for T in Ts])  # s.d. per cm of amplitude
ax = axs[1]
ax.plot(Ts * 1000, 10 * sds, color=P.edge("dna"), lw=2.0)
ax.set_yscale("log")
ax.set_xlabel("Movement duration $T$ / ms")
ax.set_ylabel("Endpoint s.d. / cm  ($A$ = 10 cm)")
ax.set_title("B  Speed-accuracy trade-off", loc="left", fontsize=10)

ax = axs[2]
rng = np.random.default_rng(0)
T = 0.45
N = int(round(T / dt))
pw = [np.linalg.matrix_power(Ad, N - 1 - j) @ Bd for j in range(N)]
G = np.array(pw).T
w = np.zeros(N)
for h in range(hold):
    w += (Ah[h][0] @ G) ** 2
lam = np.linalg.solve(G @ ((1 / w)[:, None] * G.T), np.array([10.0, 0, 0, 0]))
u = (1 / w) * (G.T @ lam)
ends = []
for k in range(200):
    s = np.zeros(4)
    xs = []
    un = u * (1 + kappa * rng.standard_normal(N))
    for j in range(N + hold):
        xs.append(s[0])
        s = Ad @ s + Bd * (un[j] if j < N else 0.0)
    ends.append(xs[-1])
    if k < 20:
        ax.plot(np.arange(N + hold) * dt * 1000, xs, color=P.edge("dna"), lw=0.8, alpha=0.6)
ax.axvline(T * 1000, color=P.muted(), lw=0.8, ls=":")
ax.text(T * 1000 + 8, 2, "end of movement", fontsize=8, color=P.muted())
ax.set_xlabel("Time / ms")
ax.set_ylabel("Position / cm")
ax.set_title(f"C  Noisy executions ($T$ = 450 ms, s.d. {np.std(ends):.2f} cm)", loc="left", fontsize=10)
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
