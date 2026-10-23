"""Curvature of AAS calibration curves. The absorption line has a Gaussian profile; the
measured absorbance is A = -lg( int S(x) 10^(-a(x) c) dx / int S(x) dx ), where S is the
source line profile and a(x) the absorbance profile with unit peak value per unit c.
Curves: ideal (infinitely narrow source), source line half and equal to the absorption width,
1 % stray light, and a non-absorbed line carrying 10 % of the radiation in the band pass."""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 6, 2401)
a = np.exp(-x**2 / 2)  # absorption profile, unit width parameter
c = np.linspace(0, 3.0, 301)  # peak absorbance in the ideal case


def absorbance(ratio):
    s = np.exp(-x**2 / (2 * ratio**2))
    T = np.array([np.trapezoid(s * 10 ** (-a * ci), x) / np.trapezoid(s, x) for ci in c])
    return -np.log10(T)


fig, ax = plt.subplots(figsize=(6.2, 4.4))
ax.plot(c, c, color="k", lw=1.8, label="ideal: $A = Kc$")
ax.plot(c, absorbance(0.5), color="C0", lw=1.6, label="source width = 0.5 x absorption width")
ax.plot(c, absorbance(1.0), color="C1", lw=1.6, label="source width = absorption width")
s = 0.01
ax.plot(c, np.log10((1 + s) / (10 ** (-c) + s)), color="C2", lw=1.6, label="1 % stray light")
f = 0.10
ax.plot(c, -np.log10((1 - f) * 10 ** (-c) + f), color="C3", lw=1.6,
        label="10 % non-absorbed line in band pass")
ax.axhline(1.0, color="C3", lw=0.7, ls=":")
ax.text(0.05, 1.03, r"limit $\lg(1/0.10) = 1$", fontsize=8, color="C3")
ax.set_xlim(0, 3)
ax.set_ylim(0, 3)
ax.set_xlabel("concentration (in units of the ideal peak absorbance)")
ax.set_ylabel("measured absorbance $A$")
ax.legend(fontsize=8, frameon=False, loc="upper left", bbox_to_anchor=(0.0, 0.93))
fig.tight_layout()
