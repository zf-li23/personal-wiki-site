"""Population vector versus optimal linear estimator for cosine-tuned neurons.

Neurons: r_i = b + k cos(theta - theta_i), b = 20 Hz, k = 15 Hz; spike counts in a 0.5 s window
drawn from a Poisson distribution. Preferred directions theta_i either uniform on the circle or
bimodal (von Mises mixture around 45 and 225 degrees, concentration 2), as reported for proximal arm
neurons. Population vector (PV): sum of unit vectors along theta_i weighted by (r_i - b)/k.
Optimal linear estimator (OLE): linear map from (r - b) to (cos theta, sin theta) fitted by least
squares (small ridge penalty) on 400 training trials with random directions; tested on new trials.
A: distribution of preferred directions (bimodal case).
B: decoded minus true direction against the true direction (N = 200, bimodal): the PV is biased
toward the clusters of preferred directions, the OLE is not.
C: mean absolute direction error against N (log-log): the PV error saturates at its bias for
bimodal preferred directions; the OLE error falls as N^(-1/2).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
b, k, T = 20.0, 15.0, 0.5


def prefs(n, kind):
    if kind == "uniform":
        return rng.uniform(0, 2 * np.pi, n)
    centers = np.where(rng.random(n) < 0.5, np.pi / 4, 5 * np.pi / 4)
    return centers + rng.vonmises(0, 2.0, n)


def counts(theta, th_i):
    lam = (b + k * np.cos(theta[:, None] - th_i[None, :])) * T
    return rng.poisson(lam) / T


def pv(r, th_i):
    w = (r - b) / k
    return np.arctan2(w @ np.sin(th_i), w @ np.cos(th_i))


def ole(r_train, th_train, r_test):
    X = r_train - b
    Y = np.c_[np.cos(th_train), np.sin(th_train)]
    D = X.T @ np.linalg.solve(X @ X.T + 1.0 * np.eye(len(X)), Y)     # ridge, dual form
    Z = (r_test - b) @ D
    return np.arctan2(Z[:, 1], Z[:, 0])


def wrap(a):
    return (a + np.pi) % (2 * np.pi) - np.pi


fig = plt.figure(figsize=(12, 3.8))
ax0 = fig.add_subplot(1, 3, 1, projection="polar")
th_b = prefs(200, "bimodal")
ax0.hist(th_b, bins=24, color=P.fill("neuron"), edgecolor=P.edge("neuron"), lw=0.6)
ax0.set_yticklabels([])
ax0.set_title("A  Preferred directions (bimodal)", loc="left", fontsize=10)

ax1 = fig.add_subplot(1, 3, 2)
test = np.linspace(-np.pi, np.pi, 73)[:-1]
tr = rng.uniform(-np.pi, np.pi, 400)
rt = counts(np.repeat(test, 20), th_b)
e_pv = np.degrees(wrap(pv(rt, th_b) - np.repeat(test, 20))).reshape(-1, 20).mean(1)
e_ole = np.degrees(wrap(ole(counts(tr, th_b), tr, rt) - np.repeat(test, 20))).reshape(-1, 20).mean(1)
ax1.axhline(0, color=P.muted(), lw=0.8)
ax1.plot(np.degrees(test), e_pv, color=P.edge("negative"), lw=1.8, label="population vector")
ax1.plot(np.degrees(test), e_ole, color=P.edge("dna"), lw=1.8, label="optimal linear estimator")
for c in (45, -135):
    ax1.axvline(c, color=P.muted(), lw=0.8, ls=":")
ax1.set_xlabel("True direction (deg)")
ax1.set_ylabel("Mean decoding error (deg)")
ax1.set_xticks([-180, -90, 0, 90, 180])
ax1.set_title("B  Bias ($N = 200$)", loc="left", fontsize=10)
ax1.set_ylim(-22, 30)
ax1.legend(frameon=False, fontsize=8, ncol=2, loc="upper center")

ax2 = fig.add_subplot(1, 3, 3)
Ns = np.array([10, 20, 40, 80, 160, 320, 640])
res = {"pv_u": [], "pv_b": [], "ole_b": []}
for n in Ns:
    acc = {key: [] for key in res}
    for rep in range(6):
        thu, thb = prefs(n, "uniform"), prefs(n, "bimodal")
        th = rng.uniform(-np.pi, np.pi, 300)
        acc["pv_u"].append(np.abs(wrap(pv(counts(th, thu), thu) - th)).mean())
        rb = counts(th, thb)
        acc["pv_b"].append(np.abs(wrap(pv(rb, thb) - th)).mean())
        tr = rng.uniform(-np.pi, np.pi, 400)
        acc["ole_b"].append(np.abs(wrap(ole(counts(tr, thb), tr, rb) - th)).mean())
    for key in res:
        res[key].append(np.degrees(np.mean(acc[key])))
ax2.loglog(Ns, res["pv_u"], "o-", color=P.muted(), lw=1.6, ms=4, label="PV, uniform")
ax2.loglog(Ns, res["pv_b"], "o-", color=P.edge("negative"), lw=1.6, ms=4, label="PV, bimodal")
ax2.loglog(Ns, res["ole_b"], "o-", color=P.edge("dna"), lw=1.6, ms=4, label="OLE, bimodal")
ax2.loglog(Ns, res["ole_b"][0] * np.sqrt(Ns[0] / Ns), ls="--", color=P.ink(), lw=0.8,
           label="$\\propto N^{-1/2}$")
ax2.set_xlabel("Number of neurons $N$")
ax2.set_ylabel("Mean absolute error (deg)")
ax2.set_title("C  Error and population size", loc="left", fontsize=10)
ax2.legend(frameon=False, fontsize=8)
for a in (ax1, ax2):
    a.grid(True, alpha=0.3)
fig.tight_layout()
