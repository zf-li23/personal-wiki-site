"""Preparation in the output-null space and execution by rotational dynamics.

Latent state z in R^4 with two planes, (z1, z2) and (z3, z4). Muscle output m = (z2, z4) (the
output-potent directions); z1 and z3 are output-null. During the delay (t < 0) an input drives z
toward a condition-specific preparatory state z_prep = (cos phi, 0, sin phi, 0) with a time
constant of 60 ms; this state lies in the null space, so the muscles stay silent. At the go cue
(t = 0) the input is removed and z evolves as z' = A z with rotations at 2.5 and 3.5 Hz and decay
time 0.25 s, which carries the state from the null into the potent directions. 30 neurons read the
latent state through a random orthonormal embedding plus a baseline (rates in Hz, rectified).
Eight conditions (reach directions phi). Output-null and output-potent subspaces are recovered from
the simulated neurons by regressing the muscles on the rates (as in Kaufman et al., 2014).
A: rates of four neurons for two conditions: preparatory activity without output.
B: across-condition variance of the neural activity in the output-null and output-potent subspaces.
C: muscle output 1 for the eight conditions.
D: population trajectories projected on one null and one potent direction: preparation moves the
state along the null axis, execution rotates it into the potent axis.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import expm

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
dt = 0.002
t = np.arange(-0.4, 0.6, dt)
w1, w2, tau_d, tau_in = 2 * np.pi * 2.5, 2 * np.pi * 3.5, 0.25, 0.06
A = np.zeros((4, 4))
A[0, 1], A[1, 0] = -w1, w1
A[2, 3], A[3, 2] = -w2, w2
A -= np.eye(4) / tau_d
E = expm(A * dt)
nc, N = 8, 30
phis = np.arange(nc) * 2 * np.pi / nc
Z = np.zeros((nc, len(t), 4))
for c, ph in enumerate(phis):
    zp = np.array([np.cos(ph), 0.0, np.sin(ph), 0.0])
    z = np.zeros(4)
    for i, ti in enumerate(t):
        Z[c, i] = z
        if ti < -0.3:
            continue
        if ti < 0:
            z = z + dt / tau_in * (zp - z)
        else:
            z = E @ z
# the transient of z toward z_prep is confined to the null plane, so the output stays at zero
Q, _ = np.linalg.qr(rng.normal(size=(N, 4)))
base = rng.uniform(15, 30, N)
R = np.maximum(base + 18 * Z @ Q.T, 0)            # (nc, T, N)
M = Z[:, :, [1, 3]]                                # muscles

# recover potent / null subspaces from data: regress M on mean-subtracted rates
X = (R - R.mean(axis=(0, 1))).reshape(-1, N)
Wm, *_ = np.linalg.lstsq(X, M.reshape(-1, 2), rcond=None)    # N x 2
U, s, Vt = np.linalg.svd(Wm.T, full_matrices=True)
potent = Vt[:2].T
null = Vt[2:].T
Xc = R - R.mean(axis=0, keepdims=True)
var_pot = (np.einsum("ctn,nk->ctk", Xc, potent) ** 2).sum(-1).mean(0)
var_null = (np.einsum("ctn,nk->ctk", Xc, null) ** 2).sum(-1).mean(0)

fig, axs = plt.subplots(1, 4, figsize=(14.5, 3.6))
ax = axs[0]
cols = [P.edge("dna"), P.edge("negative")]
for j, cc in enumerate([0, 3]):
    for n in range(4):
        ax.plot(t * 1e3, R[cc, :, n] + 40 * n, color=cols[j], lw=1.3)
ax.axvline(-300, color=P.muted(), lw=0.8, ls=":")
ax.axvline(0, color=P.muted(), lw=0.8, ls="--")
ax.set_yticks([])
ax.set_xlabel("Time from go cue (ms)")
ax.set_ylabel("Rate (four neurons, offset)")
ax.set_title("A  Single neurons", loc="left", fontsize=10)
ax.text(-300, ax.get_ylim()[1], "target", fontsize=7, color=P.muted(), va="top", ha="left")
ax.text(0, ax.get_ylim()[1], "go", fontsize=7, color=P.muted(), va="top", ha="left")

ax = axs[1]
ax.plot(t * 1e3, var_null, color=P.edge("dna"), lw=1.8, label="output-null")
ax.plot(t * 1e3, var_pot, color=P.edge("negative"), lw=1.8, label="output-potent")
ax.axvline(0, color=P.muted(), lw=0.8, ls="--")
ax.set_xlabel("Time from go cue (ms)")
ax.set_ylabel("Across-condition variance")
ax.set_title("B  Null and potent subspaces", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8)

ax = axs[2]
ctoks = ["dna", "negative", "positive", "neuron", "highlight", "rna", "enzyme", "receptor"]


def ccol(c):
    return P.edge(ctoks[c])


for c in range(nc):
    ax.plot(t * 1e3, M[c, :, 0], color=ccol(c), lw=1.4)
ax.axvline(0, color=P.muted(), lw=0.8, ls="--")
ax.set_xlabel("Time from go cue (ms)")
ax.set_ylabel("Muscle 1 (a.u.)")
ax.set_title("C  Output", loc="left", fontsize=10)

ax = axs[3]
for c in range(nc):
    prep = t < 0
    ax.plot(Z[c, prep, 0], Z[c, prep, 1], color=P.muted(), lw=1.2)
    ax.plot(Z[c, ~prep, 0], Z[c, ~prep, 1], color=ccol(c), lw=1.4)
    ax.plot(Z[c, np.searchsorted(t, 0), 0], Z[c, np.searchsorted(t, 0), 1], "o",
            color=ccol(c), ms=4)
ax.axhline(0, color=P.muted(), lw=0.6)
ax.axvline(0, color=P.muted(), lw=0.6)
ax.set_xlabel("Null direction $z_1$")
ax.set_ylabel("Potent direction $z_2$")
ax.set_aspect("equal")
ax.set_title("D  State space", loc="left", fontsize=10)
for a in axs[1:3]:
    a.grid(True, alpha=0.3)
fig.tight_layout()
