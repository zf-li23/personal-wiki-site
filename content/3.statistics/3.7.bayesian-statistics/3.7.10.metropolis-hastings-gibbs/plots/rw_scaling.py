"""Random walk Metropolis for a N(0, 1) target with normal proposals of scale l: exact acceptance rate
(2/pi) arctan(2/l) and the simulated effective sample size per iteration."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)


def ess_per_draw(x):
    # initial positive sequence estimator (Geyer) of n_eff / n
    n = len(x)
    x = x - x.mean()
    f = np.fft.rfft(x, 2 * n)
    acf = np.fft.irfft(f * np.conj(f))[:n] / (np.arange(n, 0, -1) * x.var())
    s = 0.0
    for k in range(1, n - 1, 2):
        pair = acf[k] + acf[k + 1]
        if pair < 0:
            break
        s += pair
    return 1.0 / (1.0 + 2.0 * s)


ls = np.geomspace(0.2, 12, 30)
n = 40000
x = rng.normal(size=ls.size)
chains = np.empty((n, ls.size))
for t in range(n):
    cand = x + ls * rng.normal(size=ls.size)
    acc = np.log(rng.uniform(size=ls.size)) < 0.5 * (x ** 2 - cand ** 2)
    x = np.where(acc, cand, x)
    chains[t] = x
eff = np.array([ess_per_draw(chains[:, k]) for k in range(ls.size)])
fine = np.geomspace(0.2, 12, 300)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 3.6))
ax1.plot(fine, 2 / np.pi * np.arctan(2 / fine))
ax1.axvline(2.4, color="gray", ls=":")
ax1.axhline(0.44, color="gray", ls=":")
ax1.set_xscale("log")
ax1.set_xlabel("proposal scale l (target sd = 1)")
ax1.set_ylabel("acceptance rate")
ax1.set_title("Acceptance rate (2/π) arctan(2/l)")
ax2.plot(ls, eff, "o-", ms=3)
ax2.axvline(2.4, color="gray", ls=":")
ax2.set_xscale("log")
ax2.set_xlabel("proposal scale l (target sd = 1)")
ax2.set_ylabel("effective sample size per iteration")
ax2.set_title("Efficiency of random-walk Metropolis")
fig.tight_layout()
