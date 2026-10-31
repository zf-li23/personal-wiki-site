# What free-energy dissipation buys: three functions computed exactly as Markov-chain steady states.
# A: accuracy. Minimum error f = [RL'*]/[RL*] of the driven binding cycle R -> RL -> RL* -> R (correct
# ligand L, wrong ligand L' that dissociates 1/theta times faster from both bound states), minimized over
# all rate constants (each bounded within a factor e^5 of 1) at fixed cycle affinity ln(gamma); the error falls from theta at equilibrium towards
# theta^2 (Hopfield's kinetic proofreading limit).
# B: adaptation. A receptor with activity a in {0, 1} and methylation level m = 0..8, activity free
# energy E = (4 - m) + ln[(1 + c/K_I)/(1 + c/K_A)]; methylation only of inactive, demethylation only of
# active receptors, each driven by dmu so that the cycle affinity is 2 dmu. Error of adaptation after a
# step from c = 0 to c = 5 K_I, against the affinity: exponential improvement, then a kinetic floor.
# C: sensitivity. Response S = d ln([Ep]/[E]) / d ln[K] of a single substrate molecule in the
# phosphorylation cycle E -> EK -> Ep -> EpP -> E, for 3000 random rate sets per affinity: never above
# tanh(dmu/4kBT) (Owen, Gingrich and Horowitz 2020), zero at equilibrium.
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)


def ss(W):
    n = W.shape[0]
    L = W - np.diag(W.sum(0))
    return np.linalg.lstsq(np.vstack([L, np.ones(n)]), np.r_[np.zeros(n), 1.0], rcond=None)[0]


def proof_error(lk, lgam, theta):
    k1, km1, k2, km2, k3 = np.exp(5 * np.tanh(np.asarray(lk) / 5))  # rates bounded within e^{+-5}
    km3 = k1 * k2 * k3 / (km1 * km2) / np.exp(lgam)
    W = np.zeros((5, 5))  # 0 R, 1 RL, 2 RL*, 3 RL', 4 RL'*
    for (b, s), kd1, kd3 in (((1, 2), km1, k3), ((3, 4), km1 / theta, k3 / theta)):
        W[b, 0] = k1; W[0, b] = kd1
        W[s, b] = k2; W[b, s] = km2
        W[0, s] = kd3; W[s, 0] = km3
    p = ss(W)
    return p[4] / p[2]


fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.0))
ax = axs[0]
lg = np.linspace(0, 16, 17)
for theta, tok in ((0.1, "dna"), (0.01, "negative")):
    best = []
    for g in lg:
        fmin = np.inf
        for _ in range(3):
            r = minimize(lambda v: np.log(proof_error(v, g, theta)), rng.uniform(-3, 3, 5), method="Nelder-Mead",
                         options=dict(maxiter=500, xatol=1e-4, fatol=1e-6))
            fmin = min(fmin, np.exp(r.fun))
        best.append(fmin)
    ax.plot(lg, np.array(best) / theta, color=charts.line(tok), lw=2.0, label=f"$\\theta$ = {theta}")
    ax.axhline(theta, color=charts.line(tok), lw=0.8, ls=":")
ax.set_yscale("log")
ax.set_ylim(5e-3, 1.5)
ax.legend(fontsize=7.5, frameon=False, title="dotted: $f = \\theta^2$", title_fontsize=7.5)
charts.style_axes(ax, "cycle affinity $\\ln\\gamma = \\Delta\\mu/k_{\\mathrm{B}}T$", "minimum error $f_{\\min}/\\theta$")
charts.title(ax, "A   Proofreading: energy buys accuracy")

M, KI, KA = 8, 18.0, 3000.0


def adapt(c, dmu, kR=0.1, kB=0.1, om=100.0):
    n = 2 * (M + 1)
    W = np.zeros((n, n))
    idx = lambda a, m: a * (M + 1) + m
    for m in range(M + 1):
        E = (M / 2 - m) + np.log((1 + c / KI) / (1 + c / KA))
        W[idx(1, m), idx(0, m)] = om * np.exp(-E / 2)
        W[idx(0, m), idx(1, m)] = om * np.exp(E / 2)
        if m < M:
            W[idx(0, m + 1), idx(0, m)] = kR
            W[idx(0, m), idx(0, m + 1)] = kR * np.exp(-dmu + 0.5)
        if m > 0:
            W[idx(1, m - 1), idx(1, m)] = kB
            W[idx(1, m), idx(1, m - 1)] = kB * np.exp(-dmu + 0.5)
    return ss(W)[M + 1:].sum()


ax = axs[1]
d = np.linspace(0, 8, 41)
err = [abs(adapt(5 * KI, x) - adapt(0.0, x)) / adapt(0.0, x) for x in d]
ax.plot(2 * d, err, color=charts.line("receptor"), lw=2.0)
ax.set_yscale("log")
charts.style_axes(ax, "affinity of the methylation cycle $\\Delta G/k_{\\mathrm{B}}T$", "adaptation error $|\\Delta a|/a$")
charts.title(ax, "B   Adaptation: energy buys precision")


def resp(f, b, K):
    W = np.zeros((4, 4))
    W[1, 0] = f[0] * K; W[0, 1] = b[0]
    W[2, 1] = f[1]; W[1, 2] = b[1] * K
    W[3, 2] = f[2]; W[2, 3] = b[2]
    W[0, 3] = f[3]; W[3, 0] = b[3]
    p = ss(W)
    return np.log(p[2] / p[0])


ax = axs[2]
for dmu in np.linspace(0.5, 14, 28):
    S = []
    for _ in range(300):
        k = np.exp(rng.uniform(-4, 4, 8))
        f, b = k[:4], k[4:]
        b = b * np.exp((np.log(f).sum() - np.log(b).sum() - dmu) / 4)
        h = 1e-4
        S.append((resp(f, b, np.exp(h)) - resp(f, b, np.exp(-h))) / (2 * h))
    ax.scatter(np.full(len(S), dmu), S, s=3, color=charts.line("enzyme"), alpha=0.3, lw=0)
x = np.linspace(0, 14.5, 200)
ax.plot(x, np.tanh(x / 4), color=P.ink(), lw=1.4, ls="--", label="$\\tanh(\\Delta\\mu/4k_{\\mathrm{B}}T)$")
ax.set_ylim(-0.05, 1.05)
ax.legend(fontsize=7.5, frameon=False, loc="lower right")
charts.style_axes(ax, "driving $\\Delta\\mu/k_{\\mathrm{B}}T$", "sensitivity $\\partial\\ln([E_p]/[E])/\\partial\\ln[K]$")
charts.title(ax, "C   Sensing: energy buys response")
fig.tight_layout()
