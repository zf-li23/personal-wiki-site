"""Information transmission through a noisy input-output relation. The input is x = ln(c/K), the mean
output a Hill function g(x) = 1/(1 + exp(-n x)) with n = 5, and the output is Gaussian with variance
sigma^2(g) = eta^2 (g + 0.02) (Poisson-like noise of the output molecules plus a small floor). A: the
mean response and the band of one standard deviation for two noise levels. B: channel capacity from
the Blahut-Arimoto algorithm (points) and the small-noise formula log2[(2 pi e)^(-1/2) int dg/sigma(g)]
(line) against the noise amplitude eta; the dashed line marks the information of an input distribution
uniform in ln c over the same range. C: the distribution of mean outputs produced by the optimal input
distribution for eta = 0.05 (bars) and the small-noise prediction P*(g) proportional to 1/sigma(g)
(line): the optimal code uses the low end of the response, where the output is least noisy, most."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
n_hill = 5.0
x = np.linspace(-2.0, 2.0, 161)
gbar = 1 / (1 + np.exp(-n_hill * x))
gy = np.linspace(-0.4, 1.4, 721)
dg = gy[1] - gy[0]


def sigma(g, eta):
    return eta * np.sqrt(np.clip(g, 0, None) + 0.02)


def channel(eta):
    s = sigma(gbar, eta)[:, None]
    q = np.exp(-0.5 * ((gy[None, :] - gbar[:, None]) / s) ** 2)
    return q / q.sum(axis=1, keepdims=True)


def info(px, Q):
    py = px @ Q
    with np.errstate(divide="ignore", invalid="ignore"):
        t = np.where(Q > 0, Q * np.log2(Q / py[None, :]), 0.0)
    return float(px @ t.sum(axis=1))


def blahut_arimoto(Q, iters=400):
    px = np.full(Q.shape[0], 1 / Q.shape[0])
    for _ in range(iters):
        py = px @ Q
        with np.errstate(divide="ignore", invalid="ignore"):
            d = np.where(Q > 0, Q * np.log(Q / py[None, :]), 0.0).sum(axis=1)
        px = px * np.exp(d)
        px /= px.sum()
    return px, info(px, Q)


def small_noise(eta):
    g = np.linspace(gbar.min(), gbar.max(), 4000)
    z = np.trapezoid(1 / sigma(g, eta), g)
    return np.log2(z / np.sqrt(2 * np.pi * np.e))


fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.3))
fig.subplots_adjust(wspace=0.4, left=0.06, right=0.98, bottom=0.17, top=0.88)

ax = axs[0]
for eta, tok in ((0.12, "enzyme"), (0.03, "receptor")):
    s = sigma(gbar, eta)
    ax.fill_between(x, gbar - s, gbar + s, color=P.light(tok), lw=0, label=rf"$\eta = {eta}$")
ax.plot(x, gbar, color=P.ink(), lw=1.3)
ax.legend(frameon=False, fontsize=7, loc="upper left")
charts.style_axes(ax, r"input $x = \ln(c/K)$", "output g")
charts.title(ax, "A  noisy response")

ax = axs[1]
etas = np.array([0.015, 0.025, 0.04, 0.06, 0.1, 0.16, 0.25, 0.4])
caps, unif = [], []
for eta in etas:
    Q = channel(eta)
    caps.append(blahut_arimoto(Q)[1])
    unif.append(info(np.full(x.size, 1 / x.size), Q))
ef = np.logspace(np.log10(0.012), np.log10(0.45), 100)
ax.semilogx(ef, [small_noise(e) for e in ef], color=charts.line("receptor"), lw=1.2, label="small-noise formula")
ax.semilogx(etas, caps, "o", color=charts.line("receptor"), ms=4, label="Blahut-Arimoto")
ax.semilogx(etas, unif, "--", color=P.muted(), lw=1.0, label="uniform in ln c")
ax.set_ylim(0, None)
ax.legend(frameon=False, fontsize=7, loc="upper right")
charts.style_axes(ax, r"noise amplitude $\eta$", "information / bits")
charts.title(ax, "B  channel capacity")

ax = axs[2]
eta = 0.05
px, cap = blahut_arimoto(channel(eta), iters=800)
edges = np.linspace(0, 1, 26)
h, _ = np.histogram(gbar, bins=edges, weights=px)
ax.bar(0.5 * (edges[1:] + edges[:-1]), h / np.diff(edges), width=np.diff(edges), color=P.fill("receptor"), lw=0)
gg = np.linspace(0, 1, 400)
pred = 1 / sigma(gg, eta)
pred /= np.trapezoid(pred, gg)
ax.plot(gg, pred, color=P.ink(), lw=1.2)
ax.text(0.5, 0.95, f"C = {cap:.2f} bits", transform=ax.transAxes, fontsize=7, color=P.ink(), va="top")
charts.style_axes(ax, r"mean output $\bar g$", "probability density")
charts.title(ax, rf"C  optimal outputs, $\eta = {eta}$")
