"""Calibration of a photometric Fe determination (absorbance versus concentration).
Left: standards, least-squares line, 95 % confidence band for the mean response and 95 %
prediction band for a single new signal; the mean of three replicate signals of an unknown is
read back through the line (inverse prediction). Right: the low-concentration end with the
blank mean, the decision level y_b + 3 s_b and the limits of detection and quantification."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

x = np.array([0, 0.5, 1, 2, 3, 4, 5.0])                  # standards, ug/mL
y = np.array([0.003, 0.104, 0.201, 0.402, 0.596, 0.801, 0.994])
blank = np.array([0.002, 0.004, 0.001, 0.003, 0.000, 0.003, 0.002, 0.005, 0.001, 0.003])
y0 = np.array([0.512, 0.508, 0.515])                     # unknown, three replicates

fit = stats.linregress(x, y)
b, a = fit.slope, fit.intercept
n = len(x)
s = np.sqrt(np.sum((y - a - b * x) ** 2) / (n - 2))
sxx = np.sum((x - x.mean()) ** 2)
t = stats.t.ppf(0.975, n - 2)
xx = np.linspace(-0.2, 5.4, 300)
yy = a + b * xx
conf = t * s * np.sqrt(1 / n + (xx - x.mean()) ** 2 / sxx)
pred = t * s * np.sqrt(1 + 1 / n + (xx - x.mean()) ** 2 / sxx)
x0 = (y0.mean() - a) / b
sx0 = s / b * np.sqrt(1 / len(y0) + 1 / n + (y0.mean() - y.mean()) ** 2 / (b ** 2 * sxx))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.2))
ax1.fill_between(xx, yy - pred, yy + pred, color="C0", alpha=0.12, lw=0, label="95 % prediction band")
ax1.fill_between(xx, yy - conf, yy + conf, color="C0", alpha=0.30, lw=0, label="95 % confidence band")
ax1.plot(xx, yy, color="C0", lw=1.5, label=f"fit: A = {a:.4f} + {b:.4f} c")
ax1.plot(x, y, "o", color="C3", ms=5, label="standards")
ax1.plot([-0.2, x0], [y0.mean()] * 2, color="C2", lw=1, ls="--")
ax1.plot([x0, x0], [0, y0.mean()], color="C2", lw=1, ls="--")
ax1.errorbar([x0], [0.02], xerr=[[t * sx0], [t * sx0]], fmt="v", color="C2", capsize=3, ms=5)
ax1.annotate(rf"unknown: $\hat c$ = {x0:.3f} $\pm$ {t * sx0:.3f}", (x0, y0.mean()), xytext=(0.3, 0.62),
             fontsize=9, arrowprops=dict(arrowstyle="-", color="0.5"))
ins = ax1.inset_axes([0.60, 0.08, 0.37, 0.40])
for axx in (ins,):
    axx.fill_between(xx, yy - pred, yy + pred, color="C0", alpha=0.12, lw=0)
    axx.fill_between(xx, yy - conf, yy + conf, color="C0", alpha=0.30, lw=0)
    axx.plot(xx, yy, color="C0", lw=1.2)
    axx.plot(y0 * 0 + x0, y0, "_", color="C2", ms=8)
    axx.axhline(y0.mean(), color="C2", lw=0.8, ls="--")
    axx.errorbar([x0], [y0.mean() - 0.012], xerr=[[t * sx0], [t * sx0]], fmt="v", color="C2", capsize=3, ms=4)
ins.set_xlim(2.45, 2.67)
ins.set_ylim(0.49, 0.53)
ins.tick_params(labelsize=7)
ins.set_title("zoom near the unknown", fontsize=8)
ax1.set_xlim(-0.2, 5.4)
ax1.set_ylim(-0.03, 1.08)
ax1.set_xlabel(r"$c$(Fe) / ($\mu$g mL$^{-1}$)")
ax1.set_ylabel("absorbance $A$")
ax1.legend(frameon=False, fontsize=8, loc="upper left")

yb, sb = blank.mean(), blank.std(ddof=1)
yl = yb + 3 * sb
lod, loq = 3 * sb / b, 10 * sb / b
xs = np.linspace(0, 0.12, 100)
ax2.plot(xs, yb + b * xs, color="C0", lw=1.5, label="calibration line (through blank mean)")
ax2.axhspan(yb - sb, yb + sb, color="0.6", alpha=0.25, lw=0, label=r"blank mean $\pm s_b$")
ax2.axhline(yb, color="0.4", lw=1)
ax2.axhline(yl, color="C3", lw=1, ls="--")
ax2.text(0.105, yl + 0.0004, r"$y_b + 3s_b$", va="bottom", fontsize=9, color="C3")
ax2.axhline(yb + 10 * sb, color="C1", lw=1, ls="--")
ax2.text(0.105, yb + 10 * sb + 0.0004, r"$y_b + 10s_b$", va="bottom", fontsize=9, color="C1")
ax2.axvline(lod, color="C3", lw=1, ls=":")
ax2.axvline(loq, color="C1", lw=1, ls=":")
ax2.text(lod, 0.0005 - 0.004, f" LOD\n {lod:.3f}", fontsize=8.5, color="C3", va="top")
ax2.text(loq, 0.0005 - 0.004, f" LOQ\n {loq:.3f}", fontsize=8.5, color="C1", va="top")
ax2.plot(np.zeros_like(blank) + 0.004, blank, "_", color="0.3", ms=8)
ax2.set_xlim(0, 0.14)
ax2.set_ylim(-0.012, 0.025)
ax2.set_xlabel(r"$c$(Fe) / ($\mu$g mL$^{-1}$)")
ax2.set_ylabel("absorbance $A$")
ax2.legend(frameon=False, fontsize=8, loc="upper left")
fig.tight_layout()
