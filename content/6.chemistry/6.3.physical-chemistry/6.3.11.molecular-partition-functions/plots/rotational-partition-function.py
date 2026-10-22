"""Rotational partition function of a heteronuclear diatomic (rigid rotor, sigma = 1).
Left: the exact sum over J compared with the classical integral T/Theta_r and with the
Mulholland expansion, as a ratio to the exact sum (HCl, Theta_r = 15.02 K).
Right: populations of rotational levels at 298.15 K for HCl and CO."""

import numpy as np
import matplotlib.pyplot as plt

J = np.arange(0, 400)


def q_sum(theta, t):
    return np.sum((2 * J + 1) * np.exp(-J * (J + 1) * theta / t))


def q_mulholland(theta, t):
    y = theta / t
    return (1 / y) * (1 + y / 3 + y**2 / 15 + 4 * y**3 / 315)


th_hcl, th_co = 15.02, 2.77
T = np.linspace(4, 120, 300)
exact = np.array([q_sum(th_hcl, t) for t in T])
fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4))
a1.plot(T / th_hcl, (T / th_hcl) / exact, color="C0", lw=1.6, label=r"integral $T/\Theta_\mathrm{r}$")
a1.plot(T / th_hcl, q_mulholland(th_hcl, T) / exact, color="C1", lw=1.6, label="Mulholland, 4 terms")
a1.axhline(1, color="0.4", ls="--", lw=1)
a1.set_xlabel(r"$T/\Theta_\mathrm{r}$")
a1.set_ylabel(r"approximation / exact sum")
a1.set_ylim(0.7, 1.1)
a1.legend(frameon=False, fontsize=9, loc="lower right")

t = 298.15
for th, name, c, off in [(th_hcl, "HCl", "C0", -0.2), (th_co, "CO", "C2", 0.2)]:
    j = np.arange(0, 41)
    p = (2 * j + 1) * np.exp(-j * (j + 1) * th / t) / q_sum(th, t)
    a2.bar(j + off, p, width=0.4, color=c, label=rf"{name} ($q_\mathrm{{r}}$ = {q_sum(th, t):.1f})")
a2.set_xlabel(r"$J$")
a2.set_ylabel(r"$N_J/N$ at 298.15 K")
a2.set_xlim(-1, 30)
a2.legend(frameon=False, fontsize=9)
fig.tight_layout()
