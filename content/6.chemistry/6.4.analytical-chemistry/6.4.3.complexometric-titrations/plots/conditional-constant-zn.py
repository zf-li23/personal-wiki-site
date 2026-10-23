"""Conditional stability constant lg K'(ZnY) versus pH: acid effect of EDTA only; plus hydrolysis of Zn2+;
plus an NH3-NH4+ buffer with 0.10 mol/L total ammonia (pKa(NH4+) = 9.25).
Constants: lg K(ZnY) = 16.50; Zn-NH3 lg beta1..4 = 2.37, 4.81, 7.31, 9.46; Zn-OH lg beta1..4 = 4.4, 10.1, 14.2, 15.5."""

import numpy as np
import matplotlib.pyplot as plt

pKa = [0.0, 1.5, 2.00, 2.69, 6.13, 10.37]
pH = np.linspace(1, 13, 600)
h = 10.0 ** -pH


def lg_alpha_Y(h):
    s, term = 1.0, 1.0
    for p in pKa[::-1]:
        term = term * h / 10.0 ** -p
        s = s + term
    return np.log10(s)


def alpha_complex(lgb, L):
    return 1 + sum(10.0 ** b * L ** (i + 1) for i, b in enumerate(lgb))


OH = 1e-14 / h
a_OH = alpha_complex([4.4, 10.1, 14.2, 15.5], OH)
NH3 = 0.10 * 10 ** -9.25 / (10 ** -9.25 + h)
a_NH3 = alpha_complex([2.37, 4.81, 7.31, 9.46], NH3)

lgK = 16.50
fig, ax = plt.subplots(figsize=(6.4, 4))
ax.plot(pH, lgK - lg_alpha_Y(h), color="C0", lw=1.8, label="acid effect of EDTA only")
ax.plot(pH, lgK - lg_alpha_Y(h) - np.log10(a_OH), color="C1", lw=1.8, label="+ hydrolysis of Zn$^{2+}$")
ax.plot(pH, lgK - lg_alpha_Y(h) - np.log10(a_OH + a_NH3 - 1), color="C2", lw=1.8,
        label="+ NH$_3$ (0.10 mol L$^{-1}$ total)")
ax.axhline(8, color="0.5", lw=0.8, ls="--")
ax.text(1.2, 8.3, r"lg $K'$ = 8 (lg $cK'$ = 6 at $c$ = 0.01 mol L$^{-1}$)", fontsize=8)
ax.set_xlabel("pH")
ax.set_ylabel(r"lg $K'_{\mathrm{ZnY}}$")
ax.set_xlim(1, 13)
ax.set_ylim(0, 17)
ax.legend(frameon=False, fontsize=8, loc="lower center")
fig.tight_layout()
