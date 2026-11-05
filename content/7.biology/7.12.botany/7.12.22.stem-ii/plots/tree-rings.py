# Tree rings and climate, synthetic data illustrating the steps of dendrochronology.
# Model: growing-season precipitation is an AR(1) process; raw ring width = age trend (negative
# exponential) x (1 + 0.8 x standardized precipitation) x lognormal noise. (A) Raw widths with the fitted
# age trend. (B) Ring-width index (raw / fitted trend) and the precipitation anomaly; the driest years
# are marked. (C) Index against precipitation with the least-squares line and the correlation.
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

rng = np.random.default_rng(12)
n = 200
years = np.arange(1801, 1801 + n)
prec = np.zeros(n)
for t in range(1, n):
    prec[t] = 0.35 * prec[t - 1] + rng.normal(0, 1)
z = (prec - prec.mean()) / prec.std()
age = np.arange(n)
trend_true = 0.4 + 2.6 * np.exp(-age / 45)
width = trend_true * np.clip(1 + 0.25 * z, 0.15, None) * rng.lognormal(0, 0.12, n)


def negexp(x, a, b, c):
    return a + b * np.exp(-x / c)


par, _ = curve_fit(negexp, age, width, p0=(0.4, 2.5, 40))
fit = negexp(age, *par)
index = width / fit
fig, axs = plt.subplots(1, 3, figsize=(13.0, 3.9), gridspec_kw=dict(width_ratios=[1.25, 1.25, 0.8]))
a, b, c = axs
a.plot(years, width, color="#8c6d46", lw=1.0)
a.plot(years, fit, color="0.55", lw=2.0)
a.set_xlabel("Year")
a.set_ylabel("Ring width / mm")
a.set_title("A   Raw ring widths and age trend", loc="left", fontsize=10)
b.plot(years, index, color="#8c6d46", lw=1.1, label="ring-width index")
b.plot(years, 1 + 0.25 * z, color="#3b82c4", lw=0.9, ls="--", label="precipitation (scaled)")
dry = np.argsort(z)[:4]
b.plot(years[dry], index[dry], "v", color="#d9534f", ms=6, label="driest years")
b.axhline(1, color="0.6", lw=0.6)
b.set_xlabel("Year")
b.set_ylabel("Index")
b.set_title("B   Detrended index and climate", loc="left", fontsize=10)
b.legend(fontsize=7, frameon=False, loc="upper right", ncol=3)
b.set_ylim(0.2, 1.95)
c.plot(z, index, "o", ms=3, color="#8c6d46", alpha=0.6)
k, m = np.polyfit(z, index, 1)
xx = np.linspace(z.min(), z.max(), 10)
c.plot(xx, k * xx + m, color="#3b82c4", lw=1.6)
r = np.corrcoef(z, index)[0, 1]
c.text(0.05, 0.92, f"r = {r:.2f}", transform=c.transAxes, fontsize=9)
c.set_xlabel("Precipitation (standardized)")
c.set_ylabel("Index")
c.set_title("C   Calibration", loc="left", fontsize=10)
fig.tight_layout()
