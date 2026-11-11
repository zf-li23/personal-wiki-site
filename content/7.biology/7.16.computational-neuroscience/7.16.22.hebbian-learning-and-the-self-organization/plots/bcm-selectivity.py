"""BCM rule with a sliding threshold develops selectivity (Bienenstock, Cooper and Munro 1982).

A linear neuron v = w . u receives K = 4 equally frequent input patterns; the patterns are the columns of
U (random positive vectors with 6 components, normalized), so they are linearly independent. Rule:
  dw/dt = eta v (v - theta) u,   theta = <v^2> / v0  (instantaneous, as in Cooper and Bear 2012; v0 = 1),
here implemented as the running average theta <- theta + (v^2 - theta) dt/tau_theta (tau_theta = 100 presentations).
A: response to each pattern against presentations (starting from similar responses, the neuron becomes selective
for one pattern and silent for the others). B: the phi function and the sliding threshold at three times.
C: final selectivity index for 40 random initial conditions (which pattern wins is random).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(3)
K, N = 4, 6
U = np.abs(rng.normal(size=(N, K))) + 0.3
U /= np.linalg.norm(U, axis=0)
eta, tau_th = 0.004, 100.0


def run(seed, n_steps=60000, record=False):
    r = np.random.default_rng(seed)
    w = 0.2 * (np.abs(r.normal(size=N)) + 0.5)
    th = 0.0
    out, ths = [], []
    for t in range(n_steps):
        k = r.integers(K)
        u = U[:, k]
        v = w @ u
        w = w + eta * v * (v - th) * u
        th += (v * v - th) / tau_th
        if record and t % 200 == 0:
            out.append(U.T @ w)
            ths.append(th)
    return w, np.array(out), np.array(ths)


w, resp, ths = run(5, record=True)
fig, axs = plt.subplots(1, 3, figsize=(13, 4.0))
ax = axs[0]
t = np.arange(len(resp)) * 200
for k in range(K):
    ax.plot(t, resp[:, k], lw=1.8, color=P.edge(P.protein(k)), label=f"pattern {k + 1}")
ax.plot(t, ths, color=P.ink(), lw=1.2, ls="--", label=r"threshold $\theta$")
ax.set_xlabel("Presentations")
ax.set_ylabel("Response $r$")
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.set_title("A  Selectivity emerges", loc="left", fontsize=10)

bx = axs[1]
vv = np.linspace(0, 2.2, 300)
for th_, col in ((0.3, P.edge("dna")), (0.8, P.edge("rna")), (1.4, P.edge("positive"))):
    bx.plot(vv, vv * (vv - th_), color=col, lw=1.8, label=rf"$\theta$ = {th_}")
bx.axhline(0, color=P.muted(), lw=0.8)
bx.set_xlabel("Postsynaptic response $r$")
bx.set_ylabel(r"$\phi(r,\theta) = r\,(r-\theta)$")
bx.set_ylim(-0.4, 2.0)
bx.legend(frameon=False, fontsize=8, loc="upper left")
bx.set_title("B  Potentiation above $\\theta$, depression below", loc="left", fontsize=10)

cx = axs[2]
sels = []
for s in range(40):
    w, _, _ = run(100 + s, n_steps=40000)
    rr = np.sort(U.T @ w)[::-1]
    sels.append((rr[0] - rr[1]) / (rr[0] + rr[1] + 1e-12))
cx.hist(sels, bins=np.linspace(0, 1, 21), color=P.fill("dna"), edgecolor=P.edge("dna"))
cx.set_xlabel("Selectivity (best - second best)/(sum)")
cx.set_ylabel("Number of runs")
cx.set_title("C  40 random initial weights", loc="left", fontsize=10)
fig.tight_layout()
