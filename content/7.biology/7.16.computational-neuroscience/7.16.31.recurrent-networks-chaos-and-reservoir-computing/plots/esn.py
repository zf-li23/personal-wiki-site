"""Echo state networks: the echo state property, memory capacity and prediction of the Lorenz system.

Reservoir: x(n+1) = tanh(W x(n) + W_in u(n+1)), W random Gaussian rescaled to spectral radius rho,
W_in uniform in [-0.5, 0.5]; readout y = W_out x trained by ridge regression (lambda = 1e-6).
A: echo state property: the same input sequence (uniform noise) drives two copies of a 200-unit
   reservoir from different initial states; their distance decays for rho = 0.9, decays slowly for
   rho = 1.0 and does not decay for rho = 1.5 (input scale 0.1).
B: short-term memory capacity MC = sum_k r^2(u(n - k), y_k(n)) (Jaeger, 2002) for a 100-unit
   reservoir and i.i.d. input, against rho: maximal just below 1 (upper bound N).
C: a 400-unit sparse reservoir (rho = 0.9, input scale 0.1, readout from the rates and the squares of
   half of them) trained to predict the next step of the Lorenz system
   (sigma = 10, rho_L = 28, beta = 8/3, sampling 0.02) is run autonomously by feeding its output
   back as input: it follows the true x(t) for several Lyapunov times and then diverges, while
   staying on a Lorenz-like attractor.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)


def reservoir(N, rho, nin, scale=0.5, density=1.0):
    W = rng.normal(0, 1, (N, N)) * (rng.random((N, N)) < density)
    W *= rho / np.max(np.abs(np.linalg.eigvals(W)))
    Win = rng.uniform(-scale, scale, (N, nin))
    return W, Win


def ridge(X, Y, lam=1e-6):
    return Y.T @ X @ np.linalg.inv(X.T @ X + lam * np.eye(X.shape[1]))


fig, axs = plt.subplots(1, 3, figsize=(13, 3.9), gridspec_kw={"width_ratios": [1, 1, 1.4]})
ax = axs[0]
u = rng.uniform(-1, 1, 300)
for rho, col in ((0.9, P.edge("dna")), (1.0, P.edge("positive")), (1.5, P.edge("negative"))):
    W, Win = reservoir(200, rho, 1, scale=0.1)
    a = rng.normal(0, 1, 200)
    b = rng.normal(0, 1, 200)
    d = []
    for n in range(300):
        a = np.tanh(W @ a + Win[:, 0] * u[n])
        b = np.tanh(W @ b + Win[:, 0] * u[n])
        d.append(np.linalg.norm(a - b))
    ax.semilogy(d, color=col, lw=1.6, label=f"$\\rho$ = {rho}")
ax.set_xlabel("Time step $n$")
ax.set_ylabel("$\\|\\boldsymbol{x}(n) - \\boldsymbol{x}'(n)\\|$")
ax.set_title("A  Echo state property", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="lower left")

ax = axs[1]
rhos = np.array([0.1, 0.3, 0.5, 0.7, 0.8, 0.9, 0.95, 1.0, 1.1, 1.3])
mcs = []
T = 3000
u = rng.uniform(-1, 1, T)
for rho in rhos:
    W, Win = reservoir(100, rho, 1, scale=0.1)
    x = np.zeros(100)
    X = np.empty((T, 100))
    for n in range(T):
        x = np.tanh(W @ x + Win[:, 0] * u[n])
        X[n] = x
    mc = 0.0
    tr = slice(200, 2000)
    te = slice(2000, T)
    for k in range(1, 101):
        Y = np.roll(u, k)
        w = ridge(X[tr], Y[tr, None], 1e-8)
        yh = X[te] @ w.ravel()
        mc += np.corrcoef(yh, Y[te])[0, 1] ** 2
    mcs.append(mc)
ax.plot(rhos, mcs, "o-", color=P.edge("dna"), lw=1.6, ms=4)
ax.set_xlabel("Spectral radius $\\rho$")
ax.set_ylabel("Memory capacity (steps)")
ax.set_title("B  Short-term memory", loc="left", fontsize=10)

ax = axs[2]
lor = lambda t, s: [10 * (s[1] - s[0]), s[0] * (28 - s[2]) - s[1], s[0] * s[1] - 8 / 3 * s[2]]
dt = 0.02
tt = np.arange(0, 140, dt)
sol = solve_ivp(lor, (0, tt[-1]), [1.0, 1.0, 1.0], t_eval=tt, rtol=1e-9, atol=1e-9).y.T[1000:]
data = (sol - sol.mean(0)) / sol.std(0)
N = 400
rc = np.random.default_rng(0)
W = rc.normal(0, 1, (N, N)) * (rc.random((N, N)) < 0.02)
W *= 0.9 / np.max(np.abs(np.linalg.eigvals(W)))
Win = rc.uniform(-0.1, 0.1, (N, 3))
feat = lambda x: np.r_[x, x[:N // 2] ** 2]  # squares of half the units (Pathak et al., 2018)
ntr = 4000
x = np.zeros(N)
X = np.empty((ntr, N + N // 2))
for n in range(ntr):
    x = np.tanh(W @ x + Win @ data[n])
    X[n] = feat(x)
Wout = ridge(X[200:], data[201:ntr + 1], 1e-6)
npred = 600
pred = np.empty((npred, 3))
y = Wout @ feat(x)
for n in range(npred):
    pred[n] = y
    x = np.tanh(W @ x + Win @ y)
    y = Wout @ feat(x)
truth = data[ntr + 1:ntr + 1 + npred]
lt = np.arange(npred) * dt * 0.906  # in Lyapunov times (lambda_max = 0.906)
ax.plot(lt, truth[:, 0], color=P.ink(), lw=1.8, label="Lorenz $x(t)$")
ax.plot(lt, pred[:, 0], color=P.edge("rna"), lw=1.4, ls="--", label="autonomous reservoir")
ax.set_xlabel("Time / Lyapunov times")
ax.set_ylabel("$x$ (standardized)")
ax.set_title("C  Predicting a chaotic system", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="upper right")
for a_ in axs:
    a_.grid(True, alpha=0.3)
fig.tight_layout()
