# Grand period of growth: logistic and Gompertz curves fitted by least squares to simulated plant-height
# data (a maize-like crop, 0-90 days after sowing; values illustrative). (A) cumulative height with the two
# fits; (B) growth rate dh/dt (finite differences of the data and the derivatives of the fits): slow, fast,
# slow. The logistic rate peaks at K/2, the Gompertz rate at K/e.
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

rng = np.random.default_rng(0)


def logistic(t, K, r, tm):
    return K / (1 + np.exp(-r * (t - tm)))


def gompertz(t, K, r, ti):
    return K * np.exp(-np.exp(-r * (t - ti)))


t = np.arange(4, 91, 4.0)
h_true = gompertz(t, 165, 0.075, 42)
h = np.clip(h_true * (1 + rng.normal(0, 0.015, t.size)) + rng.normal(0, 0.5, t.size), 0.5, None)
pl, _ = curve_fit(logistic, t, h, p0=(160, 0.1, 45))
pg, _ = curve_fit(gompertz, t, h, p0=(160, 0.08, 40))
tt = np.linspace(0, 95, 400)
fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.2))
a.plot(t, h, "o", color="0.3", ms=5, label="measured (simulated)")
a.plot(tt, logistic(tt, *pl), color="#c0504d", lw=2.2, label=f"logistic: K = {pl[0]:.0f} cm, r = {pl[1]:.3f} d⁻¹")
a.plot(tt, gompertz(tt, *pg), color="#2f6fb5", lw=2.2, ls="--", label=f"Gompertz: K = {pg[0]:.0f} cm, r = {pg[1]:.3f} d⁻¹")
a.set_xlabel("Days after sowing t / d")
a.set_ylabel("Plant height h / cm")
a.set_xlim(0, 95)
a.set_ylim(0, 190)
a.legend(frameon=False, fontsize=8.5, loc="upper left")
a.set_title("A   Cumulative growth (S curve)", loc="left", fontsize=10)
mid = (t[1:] + t[:-1]) / 2
b.plot(mid, np.diff(h) / np.diff(t), "o", color="0.3", ms=5, label="data (differences)")
rl = pl[1] * logistic(tt, *pl) * (1 - logistic(tt, *pl) / pl[0])
rg = pg[1] * gompertz(tt, *pg) * np.log(pg[0] / gompertz(tt, *pg))
b.plot(tt, rl, color="#c0504d", lw=2.2, label="logistic")
b.plot(tt, rg, color="#2f6fb5", lw=2.2, ls="--", label="Gompertz")
for x, y, c in ((pl[2], pl[0] * pl[1] / 4, "#c0504d"), (pg[2], pg[0] * pg[1] / np.e, "#2f6fb5")):
    b.plot(x, y, "D", color=c, ms=6)
for x0, x1, name in ((0, 25, "slow"), (25, 62, "fast"), (62, 95, "slow")):
    b.text((x0 + x1) / 2, 0.3, name, ha="center", fontsize=9, color="0.4")
b.set_xlabel("Days after sowing t / d")
b.set_ylabel("Growth rate dh/dt / cm d⁻¹")
b.set_xlim(0, 95)
b.set_ylim(0, 6.5)
b.legend(frameon=False, fontsize=8.5, loc="upper right")
b.set_title("B   Growth rate", loc="left", fontsize=10)
for x in (a, b):
    x.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
