"""Relative concentration error of a spectrophotometric measurement. If the transmittance
reading has a constant absolute uncertainty (here 0.005), dc/c = 0.434 dtau / (tau lg tau),
with a minimum at A = 0.434 (tau = 1/e). If the detector is shot-noise limited,
s_tau is proportional to sqrt(tau^2 + tau) and the optimum moves to A = 0.96."""

import numpy as np
import matplotlib.pyplot as plt

A = np.linspace(0.03, 2.0, 400)
tau = 10 ** (-A)
dtau = 0.005
err_const = dtau / (tau * A * np.log(10)) * 100
k = dtau / np.sqrt(10 ** (-2 * 0.434) + 10 ** (-0.434))   # same error as above at A = 0.434
err_shot = k * np.sqrt(tau ** 2 + tau) / (tau * A * np.log(10)) * 100

fig, ax = plt.subplots(figsize=(6.6, 4.2))
ax.plot(A, err_const, color="C0", lw=1.6, label=r"constant reading error, $\Delta\tau = 0.005$")
ax.plot(A, err_shot, color="C3", lw=1.4, ls="--", label="shot-noise limited detector")
ax.axvspan(0.2, 0.8, color="0.5", alpha=0.15, lw=0)
ax.axvline(0.434, color="C0", lw=0.8, ls=":")
ax.axvline(0.963, color="C3", lw=0.8, ls=":")
ax.text(0.45, 5.4, "A = 0.434", color="C0", fontsize=8)
ax.text(0.98, 5.4, "A = 0.96", color="C3", fontsize=8)
ax.text(0.22, 0.4, "0.2-0.8", fontsize=8)
secx = ax.secondary_xaxis("top", functions=(lambda a: a, lambda a: a))
ticks = [0.1, 0.2, 0.4, 0.8, 1.5]
secx.set_xticks(ticks)
secx.set_xticklabels([f"{10 ** -t:.2f}" for t in ticks])
secx.set_xlabel(r"transmittance $\tau$")
ax.set_xlabel(r"absorbance $A$")
ax.set_ylabel(r"relative error $|\Delta c / c|$ / %")
ax.set_ylim(0, 6)
ax.set_xlim(0, 2)
ax.legend(frameon=False, fontsize=8, loc="upper right", bbox_to_anchor=(1.0, 0.88))
fig.tight_layout()
