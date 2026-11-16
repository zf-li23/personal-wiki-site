# Descriptive versus mechanistic models (simulated data, not a real population).
# Counts of a population growing logistically (r = 0.5 per day, K = 100, N0 = 4) are observed on days 0-11
# with lognormal noise (CV about 8%). A cubic polynomial (descriptive) and the logistic equation
# (mechanistic) are both fitted to the observations by least squares; inside the data range they agree,
# but extrapolated to day 24 the polynomial runs away while the logistic levels off at its fitted K.
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import wikibio as bio

P = bio.P
rng = np.random.default_rng(7)


def logistic(t, r, K, N0):
    return K / (1 + (K / N0 - 1) * np.exp(-r * t))


t_obs = np.arange(0, 12)
true = logistic(t_obs, 0.5, 100, 4)
y_obs = true * np.exp(rng.normal(0, 0.08, t_obs.size))

coef = np.polyfit(t_obs, y_obs, 3)
(r_hat, K_hat, N0_hat), _ = curve_fit(logistic, t_obs, y_obs, p0=[0.3, 80, 5])

t = np.linspace(0, 24, 400)
fig, ax = plt.subplots(figsize=(7.4, 4.4))
ax.axvspan(0, 11, color=P.light("neutral"), alpha=0.6, lw=0)
ax.text(5.5, 182, "observed range", ha="center", fontsize=8, color=P.muted())
ax.text(17.5, 182, "extrapolation", ha="center", fontsize=8, color=P.muted())
ax.plot(t, logistic(t, 0.5, 100, 4), color=P.muted(), lw=1.0, ls=":", label="process that generated the data")
ax.plot(t, np.polyval(coef, t), color=P.edge("negative"), lw=2, label="cubic polynomial (descriptive)")
ax.plot(t, logistic(t, r_hat, K_hat, N0_hat), color=P.edge("dna"), lw=2,
        label="logistic, r = %.2f, K = %.0f (mechanistic)" % (r_hat, K_hat))
ax.plot(t_obs, y_obs, "o", ms=5, color=P.ink(), label="observations")
ax.set_xlim(0, 24)
ax.set_ylim(0, 200)
ax.set_xlabel("Time / d")
ax.set_ylabel("Population size")
ax.legend(frameon=False, fontsize=8, loc="upper left", bbox_to_anchor=(0.0, 0.92))
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.tight_layout()
