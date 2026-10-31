# Parameter sensitivity and sloppiness.
# A: steady-state level x* of a protein made at maximal rate beta and degraded at unit rate, without
# regulation (n = 0) or with negative autoregulation, dx/dt = beta / (1 + (x/K)^n) - x, K = 1.
# B: the logarithmic sensitivity S = d ln x* / d ln beta = 1 / (1 + n (x*/K)^n / (1 + (x*/K)^n)): strong
# negative feedback makes the output insensitive (S -> 1/(1 + n)) to the parameter it feeds back on.
# C: "sloppy" parameter spectra (Gutenkunst and colleagues 2007): eigenvalues of the Fisher information
# matrix J^T J (J = derivatives of the model output, sampled at 40 time points, with respect to the
# logarithms of the parameters), normalized to the largest, for a sum of four exponentials (8 parameters)
# and for the adaptation network of Figure 40.2A (12 rate and Michaelis constants), compared with a model
# whose parameters act on orthogonal features (a Fourier series): the eigenvalues of mechanistic models
# spread over many decades, so that most parameter combinations barely affect the behaviour.
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.0))
beta = np.logspace(-1, 3, 200)
for n, tok in ((0, "neutral"), (1, "rna"), (2, "enzyme"), (4, "dna")):
    if n == 0:
        xs = beta.copy()
        S = np.ones_like(beta)
    else:
        xs = np.array([brentq(lambda x: b / (1 + x**n) - x, 0, b) for b in beta])
        u = xs**n
        S = 1 / (1 + n * u / (1 + u))
    lab = "no feedback" if n == 0 else f"$n$ = {n}"
    axs[0].plot(beta, xs, color=charts.line(tok), lw=1.8, label=lab)
    axs[1].plot(beta, S, color=charts.line(tok), lw=1.8, label=lab)
axs[0].set_xscale("log"); axs[0].set_yscale("log")
axs[0].legend(fontsize=7.5, frameon=False)
charts.style_axes(axs[0], "maximal production rate $\\beta$ / $K\\gamma$", "steady state $x^*/K$")
charts.title(axs[0], "A   Negative autoregulation buffers")
axs[1].set_xscale("log")
axs[1].set_ylim(0, 1.05)
for n in (1, 2, 4):
    axs[1].axhline(1 / (1 + n), color=P.muted(), lw=0.6, ls=":")
axs[1].legend(fontsize=7.5, frameon=False, loc="lower left")
charts.style_axes(axs[1], "maximal production rate $\\beta$ / $K\\gamma$", "sensitivity $\\partial\\ln x^*/\\partial\\ln\\beta$")
charts.title(axs[1], "B   Sensitivity falls to $1/(1+n)$")

t = np.linspace(0.1, 10, 40)


def fim(model, lp, h=1e-4):
    y0 = model(lp)
    J = np.empty((y0.size, lp.size))
    for j in range(lp.size):
        d = np.zeros_like(lp); d[j] = h
        J[:, j] = (model(lp + d) - model(lp - d)) / (2 * h)
    ev = np.linalg.eigvalsh(J.T @ J)
    return np.sort(ev)[::-1] / ev.max()


def expsum(lp):
    A, k = np.exp(lp[:4]), np.exp(lp[4:])
    return (A[None, :] * np.exp(-np.outer(t, k))).sum(1)


def fourier(lp):
    c = lp
    return sum(c[j] * np.cos((j + 1) * np.pi * t / 10) for j in range(c.size))


def nfblb(lp):
    k, K = np.exp(lp[:6]), np.exp(lp[6:])

    def rhs(tt, y, I):
        A, B, C = y
        return [k[0] * I * (1 - A) / (1 - A + K[0]) - 0.5 * k[1] * A / (A + K[1]),
                k[2] * C * (1 - B) / (1 - B + K[2]) - 0.5 * k[3] * B / (B + K[3]),
                k[4] * A * (1 - C) / (1 - C + K[4]) - k[5] * B * C / (C + K[5])]
    s0 = solve_ivp(rhs, (0, 300), [0.5, 0.5, 0.5], args=(0.5,), method="LSODA", rtol=1e-10, atol=1e-12)
    s1 = solve_ivp(rhs, (0, 10), s0.y[:, -1], args=(0.6,), t_eval=t, method="LSODA", rtol=1e-10, atol=1e-12)
    return s1.y[2]


ax = axs[2]
spectra = (("sum of 4 exponentials", fim(expsum, np.log([1, 0.8, 0.6, 0.4, 0.2, 0.5, 1.3, 3.0])), "rna"),
           ("adaptation network", fim(nfblb, np.log([1, 1, 0.5, 0.5, 5, 5, 0.1, 0.1, 0.01, 0.01, 0.01, 0.01])), "enzyme"),
           ("orthogonal features", fim(fourier, np.ones(8)), "neutral"))
for x, (lab, ev, tok) in enumerate(spectra):
    ev = np.clip(ev, 1e-16, None)
    ax.hlines(ev, x - 0.3, x + 0.3, color=charts.line(tok), lw=1.6)
ax.set_yscale("log")
ax.set_ylim(1e-16, 3)
ax.set_xticks(range(3), [s[0] for s in spectra], fontsize=7.5)
charts.style_axes(ax, None, "eigenvalue / largest")
charts.title(ax, "C   Sloppy parameter spectra")
fig.tight_layout()
