"""Michaelis-Menten kinetics: initial rates with constant (additive) noise, sd = 0.03 vmax
(vmax = 1, KM = 2 in arbitrary units). (a) one simulated data set fitted by nonlinear least
squares (scipy curve_fit) and by a straight line through the Lineweaver-Burk plot;
(b) the double-reciprocal plot; (c) estimates of KM from 2000 simulated data sets."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

vmax, KM, sd = 1.0, 2.0, 0.03
S = np.array([0.25, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0, 8.0, 12.0, 20.0])
rng = np.random.default_rng(0)


def mm(s, vm, km):
    return vm * s / (km + s)


def fits(v):
    (vm_nl, km_nl), _ = curve_fit(mm, S, v, p0=[1, 1])
    b, a0 = np.polyfit(1 / S, 1 / v, 1)
    return vm_nl, km_nl, 1 / a0, b / a0


v = mm(S, vmax, KM) + sd * rng.standard_normal(S.size)
vm_nl, km_nl, vm_lb, km_lb = fits(v)

km_n, km_l = [], []
for _ in range(2000):
    vv = mm(S, vmax, KM) + sd * rng.standard_normal(S.size)
    if np.any(vv <= 0):
        continue
    r = fits(vv)
    km_n.append(r[1])
    km_l.append(r[3])
km_n, km_l = np.array(km_n), np.array(km_l)

ss = np.linspace(0, 21, 300)
fig, axs = plt.subplots(1, 3, figsize=(14, 3.9))
axs[0].plot(S, v, "o", color="0.3", ms=4, label="simulated data")
axs[0].plot(ss, mm(ss, vmax, KM), color="0.6", ls=":", label="true curve")
axs[0].plot(ss, mm(ss, vm_nl, km_nl), color="C0", label=rf"nonlinear: $v_{{\max}}$={vm_nl:.2f}, $K_{{\mathrm{{M}}}}$={km_nl:.2f}")
axs[0].plot(ss, mm(ss, vm_lb, km_lb), color="C3", ls="--", label=rf"Lineweaver-Burk: $v_{{\max}}$={vm_lb:.2f}, $K_{{\mathrm{{M}}}}$={km_lb:.2f}")
axs[0].set_xlabel("[S]")
axs[0].set_ylabel(r"$v$")
axs[0].legend(frameon=False, fontsize=7, loc="lower right")
axs[0].set_title(r"$v = v_{\max}[\mathrm{S}]/(K_{\mathrm{M}} + [\mathrm{S}])$", fontsize=10)

x = np.linspace(-0.6, 4.2, 100)
b, a0 = np.polyfit(1 / S, 1 / v, 1)
axs[1].plot(1 / S, 1 / v, "o", color="0.3", ms=4)
axs[1].plot(x, a0 + b * x, color="C3", ls="--", label="least-squares line")
axs[1].plot(x, 1 / vmax + KM / vmax * x, color="0.6", ls=":", label="true line")
axs[1].axhline(0, color="0.7", lw=0.6)
axs[1].axvline(0, color="0.7", lw=0.6)
axs[1].set_xlabel(r"$1/[\mathrm{S}]$")
axs[1].set_ylabel(r"$1/v$")
axs[1].set_title("Lineweaver-Burk plot", fontsize=10)
axs[1].legend(frameon=False, fontsize=8)

bins = np.linspace(0.5, 4.5, 50)
axs[2].hist(km_n, bins=bins, color="C0", alpha=0.6, label=rf"nonlinear (IQR {np.subtract(*np.percentile(km_n, [75, 25])):.2f})")
axs[2].hist(km_l, bins=bins, color="C3", alpha=0.5, label=rf"Lineweaver-Burk (IQR {np.subtract(*np.percentile(km_l, [75, 25])):.2f})")
axs[2].axvline(KM, color="0.3", lw=1)
axs[2].set_xlabel(r"estimated $K_{\mathrm{M}}$")
axs[2].set_ylabel("count")
axs[2].set_title("2000 simulated experiments", fontsize=10)
axs[2].legend(frameon=False, fontsize=8)
fig.tight_layout()
