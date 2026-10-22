"""Molar heat capacity C_V,m / R of ideal diatomic gases in the rigid-rotor, harmonic-oscillator
model: translation 3/2, rotation from the exact sum over J (heteronuclear, sigma = 1), and
vibration from the Einstein function. Left: HCl with its three contributions; right: the
vibrational contribution for I2, N2 and HCl."""

import numpy as np
import matplotlib.pyplot as plt

J = np.arange(0, 600)


def c_rot(theta, t):
    w = (2 * J + 1) * np.exp(-J * (J + 1) * theta / t)
    e = J * (J + 1) * theta / t                      # level energy / kT
    m1 = np.sum(w * e) / np.sum(w)
    m2 = np.sum(w * e**2) / np.sum(w)
    return m2 - m1**2                                # C_rot / R


def c_vib(theta, t):
    x = theta / t
    return x**2 * np.exp(-x) / np.expm1(-x) ** 2     # Einstein function


T = np.logspace(0.3, 4, 400)
th_r, th_v = 15.02, 4152.0                            # HCl
cr = np.array([c_rot(th_r, t) for t in T])
cv = c_vib(th_v, T)
fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4))
a1.semilogx(T, 1.5 + 0 * T, color="C0", lw=1.4, ls="--", label="translation")
a1.semilogx(T, 1.5 + cr, color="C1", lw=1.4, ls="--", label="+ rotation")
a1.semilogx(T, 1.5 + cr + cv, color="C3", lw=1.8, label="+ vibration (total)")
for y in (1.5, 2.5, 3.5):
    a1.axhline(y, color="0.6", lw=0.6, ls=":")
a1.axvline(th_r, color="C1", lw=0.8, ls=":")
a1.axvline(th_v, color="C3", lw=0.8, ls=":")
a1.annotate(r"$\Theta_\mathrm{r}$", (th_r * 1.1, 0.6), color="C1", fontsize=9)
a1.annotate(r"$\Theta_\mathrm{v}$", (th_v * 0.6, 0.6), color="C3", fontsize=9)
a1.set_ylim(0, 4)
a1.set_xlabel(r"$T$ / K")
a1.set_ylabel(r"$C_{V,\mathrm{m}}/R$")
a1.set_title("HCl (ideal gas)", fontsize=10)
a1.legend(frameon=False, fontsize=9, loc="upper left")

T2 = np.linspace(20, 3000, 400)
for name, th, c in [("I2", 308.0, "C4"), ("N2", 3352.0, "C2"), ("HCl", 4152.0, "C3")]:
    a2.plot(T2, c_vib(th, T2), color=c, lw=1.6, label=rf"{name}, $\Theta_\mathrm{{v}}$ = {th:.0f} K")
a2.axvline(298.15, color="0.5", lw=0.8, ls=":")
a2.set_xlabel(r"$T$ / K")
a2.set_ylabel(r"$C_{V,\mathrm{m}}^{\mathrm{vib}}/R$")
a2.set_ylim(0, 1.05)
a2.legend(frameon=False, fontsize=9, loc="lower right")
fig.tight_layout()
