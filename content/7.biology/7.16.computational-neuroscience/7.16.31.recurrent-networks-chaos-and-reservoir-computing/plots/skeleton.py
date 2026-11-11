"""Dynamical skeletons: fixed points of a 3-bit memory network, and a stable heteroclinic channel.

A, B: a 3-bit flip-flop built from three self-exciting units, dx_k/dt = -x_k + w tanh(x_k) + u_k(t),
w = 2 (each unit is bistable), observed through a random rotation into 10 dimensions so that the
structure is not visible in the coordinates. Pulses on input k set bit k to +1 or -1 (A, outputs
sign of the bits). Fixed points are then found as in Sussillo and Barak (2013): minimize
q(x) = |F(x)|^2 / 2 from 400 random starts (scipy L-BFGS), keep minima with q < 1e-10 and classify
them by the number of unstable eigenvalues of the Jacobian (B, projection onto three of the
rotated coordinates' principal axes): 8 stable points (memories), 12 saddles with one unstable
direction (between memories that differ in one bit), 6 with two and 1 with three.
C: winnerless competition in a generalized Lotka-Volterra network (May and Leonard, 1975):
da_i/dt = a_i (1 - sum_j rho_ij a_j) + noise 1e-7, rho cyclic with 0.8 and 1.5: activity visits the
three saddle states in a fixed order (a stable heteroclinic channel); with this noise level the
dwell times are regular.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
w = 2.0
D = 10
Q, _ = np.linalg.qr(rng.normal(0, 1, (D, D)))
E = Q[:, :3]  # embedding: x_full = E y + (other 7 coordinates decay)


def F(z):
    y = E.T @ z
    rest = z - E @ y
    return E @ (-y + w * np.tanh(y)) - rest


def Jac(z):
    y = E.T @ z
    Dy = np.diag(-1 + w * (1 - np.tanh(y) ** 2))
    return E @ Dy @ E.T - (np.eye(D) - E @ E.T)


fig = plt.figure(figsize=(13, 4.2))
ax = fig.add_subplot(1, 3, 1)
dt = 0.05
T = 60.0
n = int(T / dt)
y = np.array([-1.9, -1.9, -1.9])
pulses = [(5, 0, +1), (12, 1, +1), (20, 0, -1), (27, 2, +1), (35, 1, +1), (42, 1, -1), (50, 2, -1)]
out = np.empty((n, 3))
inp = np.zeros((n, 3))
for t0, k, s in pulses:
    inp[int(t0 / dt):int((t0 + 1) / dt), k] = 4 * s
for i in range(n):
    out[i] = np.tanh(y)
    y = y + dt * (-y + w * np.tanh(y) + inp[i])
tt = np.arange(n) * dt
cols = [P.edge("dna"), P.edge("negative"), P.edge("positive")]
for k in range(3):
    ax.plot(tt, inp[:, k] / 4 * 0.6 + 3 * (2 - k), color=P.muted(), lw=0.8)
    ax.plot(tt, out[:, k] + 3 * (2 - k), color=cols[k], lw=1.8)
    ax.text(-1, 3 * (2 - k) + 1.1, f"bit {k + 1}", fontsize=8, color=cols[k])
ax.set_yticks([])
ax.set_xlabel("Time / $\\tau$")
ax.set_title("A  3-bit memory: input pulses (gray), outputs", loc="left", fontsize=10)

found = []
for s in range(400):
    z0 = rng.normal(0, 1.5, D)
    res = minimize(lambda z: 0.5 * np.sum(F(z) ** 2), z0, jac=lambda z: Jac(z).T @ F(z),
                   method="L-BFGS-B", options={"gtol": 1e-12, "ftol": 1e-16, "maxiter": 2000})
    if res.fun < 1e-10 and not any(np.linalg.norm(res.x - f) < 1e-3 for f, _ in found):
        nu = int(np.sum(np.linalg.eigvals(Jac(res.x)).real > 0))
        found.append((res.x, nu))
ax = fig.add_subplot(1, 3, 2, projection="3d")
mk = {0: ("o", P.edge("dna"), "stable (memory)"), 1: ("x", P.edge("positive"), "1 unstable direction"),
      2: ("^", P.edge("rna"), "2 unstable"), 3: ("s", P.edge("negative"), "3 unstable")}
pts = np.array([f for f, _ in found])
proj = pts @ E  # coordinates in the hidden 3D space recovered by the fixed points
for nu in range(4):
    sel = [i for i, (_, v) in enumerate(found) if v == nu]
    if sel:
        m, c, lab = mk[nu]
        ax.scatter(proj[sel, 0], proj[sel, 1], proj[sel, 2], marker=m, color=c, s=30, label=f"{lab}: {len(sel)}")
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.set_title("B  Fixed points found by minimizing $q$", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=7, loc="upper left", bbox_to_anchor=(-0.05, 1.0))

ax = fig.add_subplot(1, 3, 3)
al, be = 0.8, 1.5
R = np.array([[1, al, be], [be, 1, al], [al, be, 1]])
a = np.array([0.6, 0.3, 0.1])
dt = 0.01
n = int(400 / dt)
A = np.empty((n, 3))
for i in range(n):
    A[i] = a
    a = a + dt * a * (1 - R @ a) + np.sqrt(dt) * 1e-7 * rng.normal(0, 1, 3)
    a = np.maximum(a, 1e-12)
tt = np.arange(n) * dt
for k in range(3):
    ax.plot(tt, A[:, k], color=cols[k], lw=1.5, label=f"unit {k + 1}")
ax.set_xlabel("Time / $\\tau$")
ax.set_ylabel("Activity $a_i$")
ax.set_title("C  Stable heteroclinic channel", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="upper right", ncol=3)
ax.set_ylim(0, 1.25)
for a_ in (fig.axes[0], fig.axes[2]):
    a_.grid(True, alpha=0.3)
fig.tight_layout()
