"""Fitting the logistic curve to Carlson's (1913) yeast data (Section 10.4).

Data: amount of yeast (Saccharomyces cerevisiae) in a culture, measured hourly for 18 h (Carlson 1913,
as reanalyzed by Pearl 1927 and Gause 1934).
A: nonlinear least squares fit of N(t) = K / (1 + ((K - N0)/N0) exp(-r t)) (scipy curve_fit) and the
linearized fit (K from the three-point formula with t = 0, 9, 18 h, then least squares regression of
ln((K - N)/N) on t). B: residuals of both fits. C: the per capita growth rate estimated from successive
counts, ln(N_{t+1}/N_t), against the mean density sqrt(N_t N_{t+1}), with its regression line
(intercept r, slope -r/K). D: the same nonlinear fit using only the first 6, 8 or 10 hours, with 95%
confidence bands of K from the asymptotic covariance matrix.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
t = np.arange(19.0)
N = np.array([9.6, 18.3, 29.0, 47.2, 71.1, 119.1, 174.6, 257.3, 350.7, 441.0, 513.3, 559.7, 594.8, 629.4,
              640.8, 651.1, 655.9, 659.6, 661.8])


def logistic(t, K, r, N0):
    return K / (1 + (K - N0) / N0 * np.exp(-r * t))


p, cov = curve_fit(logistic, t, N, p0=[660, 0.5, 10])
N0_, N1_, N2_ = N[0], N[9], N[18]
K3 = (N1_ ** 2 * (N0_ + N2_) - 2 * N0_ * N1_ * N2_) / (N1_ ** 2 - N0_ * N2_)
y = np.log((K3 - N) / N)
slope, icpt = np.polyfit(t, y, 1)
rl, N0l = -slope, K3 / (1 + np.exp(icpt))
tt = np.linspace(0, 18, 300)
cn, cl = C.line("dna"), C.line("rna")

fig, axes = plt.subplots(1, 4, figsize=(14.0, 3.7))
ax = axes[0]
ax.plot(t, N, "o", ms=4, color=P.ink(), label="data")
ax.plot(tt, logistic(tt, *p), color=cn, lw=2, label=f"NLS: K = {p[0]:.0f}, r = {p[1]:.3f}")
ax.plot(tt, logistic(tt, K3, rl, N0l), color=cl, lw=1.5, ls=(0, (4, 2)), label=f"linearized: K = {K3:.0f}, r = {rl:.3f}")
C.style_axes(ax, "time (h)", "amount of yeast")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
C.title(ax, "A  Two fits")

ax = axes[1]
ax.axhline(0, color=P.muted(), lw=0.7)
ax.plot(t, N - logistic(t, *p), "o-", ms=3.5, lw=1, color=cn, label="NLS")
ax.plot(t, N - logistic(t, K3, rl, N0l), "s-", ms=3.5, lw=1, color=cl, label="linearized")
sse = [np.sum((N - logistic(t, *p)) ** 2), np.sum((N - logistic(t, K3, rl, N0l)) ** 2)]
ax.text(0.5, -9.5, f"SSE: {sse[0]:.0f} (NLS), {sse[1]:.0f} (linearized)", fontsize=FS["tiny"], color=P.muted())
ax.set_ylim(-11, 11)
C.style_axes(ax, "time (h)", "residual")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
C.title(ax, "B  Residuals")

ax = axes[2]
pc = np.log(N[1:] / N[:-1])
Nm = np.sqrt(N[1:] * N[:-1])
s2, i2 = np.polyfit(Nm, pc, 1)
ax.plot(Nm, pc, "o", ms=4, color=C.line("positive"))
xx = np.linspace(0, 700, 10)
ax.plot(xx, s2 * xx + i2, color=C.line("positive"), lw=1.2, ls=(0, (3, 2)))
ax.text(250, 0.55, f"r = {i2:.3f} h⁻¹\nK = {-i2 / s2:.0f}", fontsize=FS["tiny"], color=P.ink())
ax.axhline(0, color=P.muted(), lw=0.6)
C.style_axes(ax, "mean density", "ln(Nₜ₊₁ / Nₜ) per hour")
C.title(ax, "C  Per capita rate against density")

ax = axes[3]
ax.plot(t, N, "o", ms=3.5, color=P.ink())
for n, col in ((6, C.line("negative")), (8, C.line("rna")), (10, C.line("positive"))):
    pp, cc = curve_fit(logistic, t[: n + 1], N[: n + 1], p0=[660, 0.5, 10], maxfev=20000)
    se = np.sqrt(cc[0, 0])
    ax.plot(tt, logistic(tt, *pp), color=col, lw=1.5,
            label=f"0–{n} h: K = {pp[0]:.0f} ± {1.96 * se:.0f}")
    ax.axvline(n, color=col, lw=0.5, ls=(0, (1, 2)))
ax.set_ylim(0, 1100)
C.style_axes(ax, "time (h)", "amount of yeast")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
C.title(ax, "D  Fitting early data only")
fig.tight_layout()
