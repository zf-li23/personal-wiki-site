"""SPR sensorgram for 1:1 binding A + B = AB at the sensor surface. Association
(0-300 s) at several analyte concentrations, then buffer (dissociation). True values
ka = 1.0e5 L mol^-1 s^-1, kd = 1.0e-3 s^-1 (K_D = 10 nmol/L), Rmax = 120 RU.
Noisy curves (0.5 RU) are fitted globally with scipy.optimize.curve_fit."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

ka, kd, Rmax = 1.0e5, 1.0e-3, 120.0
concs = np.array([2.5, 5, 10, 20, 40]) * 1e-9
t = np.linspace(0, 700, 351)
t_on = 300.0

def response(tt, c, ka, kd, Rmax):
    kobs = ka * c + kd
    Req = Rmax * ka * c / kobs
    R_on = Req * (1 - np.exp(-kobs * np.minimum(tt, t_on)))
    R_end = Req * (1 - np.exp(-kobs * t_on))
    return np.where(tt <= t_on, R_on, R_end * np.exp(-kd * (tt - t_on)))

rng = np.random.default_rng(0)
data = [response(t, c, ka, kd, Rmax) + 0.5 * rng.standard_normal(t.size) for c in concs]

def glob(_, ka_, kd_, Rm_):
    return np.concatenate([response(t, c, ka_ * 1e5, kd_ * 1e-3, Rm_) for c in concs])
p, cov = curve_fit(glob, None, np.concatenate(data), p0=[0.5, 2.0, 100.0])
ka_f, kd_f = p[0] * 1e5, p[1] * 1e-3

fig, ax = plt.subplots(figsize=(6.8, 4.3))
cmap = plt.get_cmap("viridis")
for i, (c, R) in enumerate(zip(concs, data)):
    col = cmap(i / (len(concs) - 1) * 0.85)
    ax.plot(t, R, ".", ms=1.6, color=col)
    ax.plot(t, response(t, c, ka_f, kd_f, p[2]), color=col, lw=1, label=f"{c * 1e9:g} nmol/L")
ax.axvline(t_on, color="0.5", lw=0.8, ls=":")
ax.text(120, 112, "association", fontsize=8, ha="center")
ax.text(500, 112, "dissociation (buffer)", fontsize=8, ha="center")
ax.set_xlabel(r"$t$ / s")
ax.set_ylabel("response / RU")
ax.set_ylim(-5, 125)
ax.set_title(rf"global fit: $k_a$ = {ka_f:.2e} L/(mol s), $k_d$ = {kd_f:.2e} 1/s, "
             rf"$K_D$ = {kd_f / ka_f * 1e9:.1f} nmol/L", fontsize=9)
ax.legend(frameon=False, fontsize=7, loc="upper left", bbox_to_anchor=(0.0, 0.93), title="analyte", title_fontsize=7)
fig.tight_layout()
