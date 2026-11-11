"""EPSPs from different dendritic locations in a passive soma-plus-cable model.

Model: a spherical soma (diameter 20 um) attached to an unbranched dendrite (diameter 2 um,
length 1500 um, sealed end) divided into 30 compartments of 50 um. R_m = 20 kOhm cm^2,
c_m = 1 uF/cm^2 (tau_m = 20 ms), R_i = 100 Ohm cm, E_L = -65 mV, so the length constant of the
dendrite is lambda = 1 mm and it is 1.5 lambda long. An excitatory conductance with an alpha time
course (peak 0.3 nS at 2 ms, E_syn = 0 mV) is placed at distance X = x / lambda from the soma.
Compartment equations (backward Euler, dt = 0.025 ms):
  C_j dV_j/dt = -g_L,j (V_j - E_L) + sum_k g_jk (V_k - V_j) - g_syn(t) (V_j - E_syn).
A: somatic EPSPs for inputs at X = 0.1, 0.5, 1.0, 1.5.
B: shape-index plot: half-width against 10-90 % rise time of the somatic EPSP for inputs from
   X = 0.05 to 1.5 (distal inputs rise more slowly and are broader; Rall 1967).
C: peak EPSP at the input site (dashed) and at the soma (solid) against X: distal synapses
   produce large local but small somatic depolarizations.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
EL, Es = -65.0, 0.0
cm, gm = 0.01, 5e-4  # pF/um^2, nS/um^2  -> tau = 20 ms
a_d, seg, nseg = 1.0, 50.0, 30  # um
Ri_um = 1e6  # Ohm um
g_ax = np.pi * a_d**2 / (Ri_um * seg) * 1e9  # nS
area = np.r_[4 * np.pi * 10.0**2, np.full(nseg, 2 * np.pi * a_d * seg)]
area[-1] += np.pi * a_d**2
C = cm * area
gL = gm * area
n = nseg + 1
G = np.zeros((n, n))
for j in range(n - 1):
    G[j, j] += g_ax
    G[j + 1, j + 1] += g_ax
    G[j, j + 1] -= g_ax
    G[j + 1, j] -= g_ax
G += np.diag(gL)
lam = 1000.0
dt = 0.025
T = 120.0
t = np.arange(0, T, dt)
alpha = (t / 2.0) * np.exp(1 - t / 2.0)


def run(j, gmax=0.3):
    V = np.full(n, EL)
    A0 = np.diag(C / dt) + G
    vs, vl = np.empty_like(t), np.empty_like(t)
    for k in range(len(t)):
        g = gmax * alpha[k]
        A = A0.copy()
        A[j, j] += g
        rhs = C / dt * V + gL * EL
        rhs[j] += g * Es
        V = np.linalg.solve(A, rhs)
        vs[k], vl[k] = V[0], V[j]
    return vs - EL, vl - EL


def metrics(v):
    pk = v.max()
    i = v.argmax()
    t10 = t[np.argmax(v >= 0.1 * pk)]
    t90 = t[np.argmax(v >= 0.9 * pk)]
    above = np.where(v >= 0.5 * pk)[0]
    return pk, t90 - t10, (above[-1] - above[0]) * dt


fig, axs = plt.subplots(1, 3, figsize=(13, 3.8))
Xs = [0.1, 0.5, 1.0, 1.5]
cols = [P.edge("dna"), P.edge("protein"), P.edge("positive"), P.edge("negative")]
ax = axs[0]
for X, c in zip(Xs, cols):
    j = int(round(X * lam / seg))
    vs, vl = run(j)
    ax.plot(t, vs, color=c, lw=2.0, label=f"$X$ = {X:g}")
ax.set_xlim(0, 100)
ax.set_xlabel("Time / ms")
ax.set_ylabel("Somatic EPSP / mV")
ax.set_title("A  Somatic EPSP by input site", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8)

grid = np.arange(1, 31)  # compartments 1..30 at X = 0.05..1.5
rise, hw, ps, pl = [], [], [], []
for j in grid:
    vs, vl = run(j)
    pk, r10, w = metrics(vs)
    rise.append(r10)
    hw.append(w)
    ps.append(pk)
    pl.append(vl.max())
Xg = grid * seg / lam
ax = axs[1]
sc = ax.scatter(rise, hw, c=Xg, cmap="viridis", s=26)
ax.set_xlabel("10-90% rise time / ms")
ax.set_ylabel("Half-width / ms")
cb = fig.colorbar(sc, ax=ax, pad=0.02)
cb.set_label("$X$")
ax.set_title("B  Shape index", loc="left", fontsize=10)
ax = axs[2]
ax.plot(Xg, ps, color=P.edge("negative"), lw=2.2, label="soma")
ax.plot(Xg, pl, color=P.edge("dna"), lw=2.2, ls="--", label="input site")
ax.set_xlabel("Distance $X = x/\\lambda$")
ax.set_ylabel("Peak EPSP / mV")
ax.set_title("C  Local and somatic amplitude", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8)
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
