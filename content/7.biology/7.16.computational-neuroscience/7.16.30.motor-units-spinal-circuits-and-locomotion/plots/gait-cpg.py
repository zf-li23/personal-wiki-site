"""Left-right coordination of four half-centers and the effect of deleting V0 commissural neurons.

Four Matsuoka units (left flexor LF, left extensor LE, right flexor RF, right extensor RE):
tau dx_i/dt = -x_i - b v_i - sum_j w_ij y_j + s,  tau_a dv_i/dt = -v_i + y_i,  y_i = max(x_i, 0),
tau = 25 ms, tau_a = 250 ms, b = 2.5, s = 1.
Ipsilateral flexor-extensor inhibition (V1/V2b-like): weight 2.0.
Commissural pathways between homologous units: inhibition through V0 neurons (weight c_inh) and
excitation through V3-like neurons (weight c_exc = 0.5), represented as negative weights.
A: intact (c_inh = 1.0): left and right flexors alternate (walking).
B: V0 deleted (c_inh = 0): crossed excitation synchronizes the two sides (hopping).
C: left-right phase difference of the flexors against c_inh (0 = synchrony, 0.5 = alternation).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
tau, ta, b, s = 25.0, 250.0, 2.5, 1.0
dt = 1.0


def run(cinh, cexc=0.5, T=4000.0):
    # order: LF, LE, RF, RE; W[i, j] > 0 means inhibition from j to i
    W = np.zeros((4, 4))
    W[0, 1] = W[1, 0] = W[2, 3] = W[3, 2] = 2.0
    for i, j in ((0, 2), (2, 0), (1, 3), (3, 1)):
        W[i, j] = cinh - cexc
    rng = np.random.default_rng(1)
    x = rng.uniform(0, 0.3, 4)
    v = np.zeros(4)
    n = int(T / dt)
    Y = np.empty((n, 4))
    for k in range(n):
        y = np.maximum(x, 0)
        Y[k] = y
        x = x + dt / tau * (-x - b * v - W @ y + s)
        v = v + dt / ta * (-v + y)
    return np.arange(n) * dt, Y


def lr_phase(t, Y):
    m = t > 1500
    on = lambda y: t[m][1:][(y[m][1:] > 0.05) & (y[m][:-1] <= 0.05)]
    l, r = on(Y[:, 0]), on(Y[:, 2])
    if len(l) < 3 or len(r) < 2:
        return np.nan
    T = np.mean(np.diff(l))
    ph = [((r[r >= a][0] - a) / T) % 1 for a in l[:-1] if np.any(r >= a)]
    ph = np.array(ph)
    return np.angle(np.mean(np.exp(2j * np.pi * ph))) / (2 * np.pi) % 1


fig, axs = plt.subplots(1, 3, figsize=(13, 3.9))
lab = ("LF", "LE", "RF", "RE")
cols = (P.edge("dna"), P.edge("dna2"), P.edge("negative"), P.edge("rna"))
for ax, ci, ttl in ((axs[0], 1.0, "A  Intact: alternation"), (axs[1], 0.0, "B  V0 deleted: synchrony")):
    t, Y = run(ci)
    for k in range(4):
        ax.plot(t, Y[:, k] + 1.2 * (3 - k), color=cols[k], lw=1.4)
        ax.text(2005, 1.2 * (3 - k) + 0.1, lab[k], fontsize=8, color=cols[k])
    ax.set_xlim(2000, 4000)
    ax.set_yticks([])
    ax.set_xlabel("Time / ms")
    ax.set_title(ttl, loc="left", fontsize=10)
ax = axs[2]
cs = np.linspace(0, 1.2, 13)
ph = np.array([lr_phase(*run(c)) for c in cs])
ph = np.where(ph > 0.5, 1 - ph, ph)
ax.plot(cs, ph, "o-", color=P.edge("dna"), ms=4, lw=1.5)
ax.axvline(0.5, color=P.muted(), lw=0.8, ls=":")
ax.set_xlabel("Crossed V0 inhibition $c_{\\mathrm{inh}}$ (excitation fixed at 0.5)")
ax.set_ylabel("Left-right phase of flexors / cycle")
ax.set_ylim(-0.03, 0.53)
ax.set_title("C  Phase against commissural balance", loc="left", fontsize=10)
for a_ in axs:
    a_.grid(True, alpha=0.3)
fig.tight_layout()
