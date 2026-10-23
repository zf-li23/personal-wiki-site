"""Standard addition: equal aliquots of the sample are spiked with increasing amounts of the
analyte and made up to the same volume. The line through the signals is extrapolated to zero
signal; the magnitude of the x-intercept is the analyte concentration in the measured solution."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

xa = np.array([0, 2, 4, 6, 8.0])                 # added concentration, ng/mL
ya = np.array([0.156, 0.230, 0.312, 0.385, 0.463])
fit = stats.linregress(xa, ya)
b, a = fit.slope, fit.intercept
n = len(xa)
s = np.sqrt(np.sum((ya - a - b * xa) ** 2) / (n - 2))
cx = a / b
scx = s / b * np.sqrt(1 / n + ya.mean() ** 2 / (b ** 2 * np.sum((xa - xa.mean()) ** 2)))
t = stats.t.ppf(0.975, n - 2)

fig, ax = plt.subplots(figsize=(6.4, 4.0))
xx = np.linspace(-cx - 0.8, 8.6, 200)
ax.plot(xx, a + b * xx, color="C0", lw=1.5)
ax.plot(xx[xx < 0], a + b * xx[xx < 0], color="C0", lw=1.5, ls="--")
ax.plot(xa, ya, "o", color="C3", ms=6, label="sample + added standard")
ax.axhline(0, color="0.5", lw=0.8)
ax.axvline(0, color="0.5", lw=0.8)
ax.errorbar([-cx], [0], xerr=[[t * scx], [t * scx]], fmt="o", color="C2", capsize=3, ms=5)
ax.annotate(rf"$-c_x$:  $c_x$ = {cx:.2f} $\pm$ {t * scx:.2f} ng mL$^{{-1}}$", (-cx, 0), xytext=(-3.5, 0.33),
            fontsize=9, arrowprops=dict(arrowstyle="-", color="0.5"))
ax.annotate("signal of the unspiked sample", (0, a), xytext=(1.0, 0.07), fontsize=9,
            arrowprops=dict(arrowstyle="-", color="0.5"))
ax.set_xlim(-5.5, 8.8)
ax.set_ylim(-0.04, 0.5)
ax.set_xlabel(r"added concentration / (ng mL$^{-1}$)")
ax.set_ylabel("signal")
ax.legend(frameon=False, fontsize=9, loc="upper left")
fig.tight_layout()
