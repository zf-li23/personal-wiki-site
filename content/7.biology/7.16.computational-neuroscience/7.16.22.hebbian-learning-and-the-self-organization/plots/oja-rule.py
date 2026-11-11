"""Hebbian learning on a correlated two-dimensional input: instability and the Oja rule (Oja 1982).

Inputs u are drawn from a zero-mean Gaussian with covariance Q whose principal eigenvector e1 lies at 30 degrees
(eigenvalues 1.0 and 0.2); the output is v = w . u. Three rules, all started from the same weight vector:
  basic Hebb:  dw/dt = v u                    (norm grows without bound, direction approaches e1)
  Oja:         dw/dt = v (u - v w)            (w converges to e1 with |w| = 1)
  subtractive normalization: dw/dt = v u - n n.(v u)/N with n = (1, 1) projects out the mean component
A: scatter of inputs, principal axis, and the weight trajectories of the Hebb and Oja rules.
B: |w| against the number of presentations (log axis). C: angle between w and e1.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
th = np.deg2rad(30)
e1 = np.array([np.cos(th), np.sin(th)])
e2 = np.array([-np.sin(th), np.cos(th)])
Q = 1.0 * np.outer(e1, e1) + 0.2 * np.outer(e2, e2)
Lc = np.linalg.cholesky(Q)
n_steps, eta = 3000, 0.01
U = (Lc @ rng.normal(size=(2, n_steps))).T

w0 = np.array([0.15, -0.3])
traj = {}
for name in ("hebb", "oja"):
    w = w0.copy()
    tr = [w.copy()]
    for u in U:
        v = w @ u
        w = w + eta * (v * u if name == "hebb" else v * (u - v * w))
        tr.append(w.copy())
    traj[name] = np.array(tr)

fig, axs = plt.subplots(1, 3, figsize=(13, 4.0))
ax = axs[0]
ax.scatter(U[:600, 0], U[:600, 1], s=4, color=P.fill("neutral"), alpha=0.7)
ax.plot([-3 * e1[0], 3 * e1[0]], [-3 * e1[1], 3 * e1[1]], color=P.muted(), lw=1, ls=":")
ax.text(2.0 * e1[0] + 0.1, 2.0 * e1[1] - 0.2, "principal axis", fontsize=8, color=P.muted())
for name, col, lab in (("hebb", P.edge("rna"), "Hebb"), ("oja", P.edge("dna"), "Oja")):
    tr = traj[name]
    tr = tr[:: 20]
    s = 1.0 if name == "oja" else 1 / max(np.abs(traj["hebb"]).max(), 1) * 3
    ax.plot(tr[:, 0] * s, tr[:, 1] * s, color=col, lw=1.8, label=lab + (" (rescaled)" if name == "hebb" else ""))
    ax.plot(*(tr[-1] * s), "o", color=col, ms=5)
ax.plot(*w0, "s", color=P.ink(), ms=5)
ax.set_aspect("equal")
ax.set_xlim(-3.2, 3.2)
ax.set_ylim(-3.2, 3.2)
ax.set_xlabel("$u_1$, $w_1$")
ax.set_ylabel("$u_2$, $w_2$")
ax.legend(frameon=False, fontsize=8, loc="lower left")
ax.set_title("A  Inputs and weight trajectories", loc="left", fontsize=10)

t = np.arange(n_steps + 1)
bx = axs[1]
for name, col, lab in (("hebb", P.edge("rna"), "Hebb"), ("oja", P.edge("dna"), "Oja")):
    bx.plot(t, np.linalg.norm(traj[name], axis=1), color=col, lw=1.8, label=lab)
bx.set_yscale("log")
bx.set_xlabel("Presentations")
bx.set_ylabel("|w|")
bx.legend(frameon=False, fontsize=8)
bx.set_title("B  Hebb diverges, Oja stabilizes", loc="left", fontsize=10)

cx = axs[2]
for name, col, lab in (("hebb", P.edge("rna"), "Hebb"), ("oja", P.edge("dna"), "Oja")):
    tr = traj[name]
    ang = np.degrees(np.arccos(np.clip(np.abs(tr @ e1) / np.linalg.norm(tr, axis=1), 0, 1)))
    cx.plot(t, ang, color=col, lw=1.8, label=lab)
cx.set_xlabel("Presentations")
cx.set_ylabel("Angle between w and $e_1$ (degrees)")
cx.legend(frameon=False, fontsize=8)
cx.set_title("C  Both align with the principal axis", loc="left", fontsize=10)
fig.tight_layout()
