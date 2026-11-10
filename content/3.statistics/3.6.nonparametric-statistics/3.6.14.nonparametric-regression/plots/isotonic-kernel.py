"""Isotonic regression (PAVA) and Nadaraya-Watson kernel regression for a simulated series of
annual mean temperatures, 80 years between 1900 and 2025, with an increasing trend, a slow
oscillation and noise (the model used in the R code of the text)."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
x = np.linspace(1900, 2025, 80)
trend = 14 + 1.2 * (x - 1900) / (40 + (x - 1900))
y = trend + 0.15 * np.sin(x / 2) + rng.normal(0, 0.08, len(x))


def pava(y):
    # Blocks of (sum, count); merge backwards while the block means decrease.
    sums, counts = [], []
    for v in y:
        sums.append(v)
        counts.append(1)
        while len(sums) > 1 and sums[-2] / counts[-2] > sums[-1] / counts[-1]:
            s, c = sums.pop(), counts.pop()
            sums[-1] += s
            counts[-1] += c
    return np.repeat(np.array(sums) / np.array(counts), counts)


def nw(x0, x, y, sd):
    w = np.exp(-((x0[:, None] - x[None, :]) / sd) ** 2 / 2)
    return (w * y).sum(axis=1) / w.sum(axis=1)


sd = 0.25 * 15 / 0.6745          # ksmooth(kernel = "normal", bandwidth = 15)
fig, ax = plt.subplots(figsize=(8.4, 4.4))
ax.plot(x, y, "o", color="0.55", ms=3.5, label="simulated annual means")
ax.step(x, pava(y), where="post", color="C3", lw=1.8, label="isotonic regression (PAVA)")
ax.plot(x, nw(x, x, y, sd), color="C0", lw=1.8, label="Nadaraya-Watson, Gaussian kernel")
ax.plot(x, trend, color="0.2", ls=":", lw=1.2, label="trend without the oscillation")
ax.set_xlabel("year")
ax.set_ylabel("annual mean temperature / °C")
ax.legend(fontsize=8, loc="upper left")
ax.grid(alpha=0.3)
fig.tight_layout()
