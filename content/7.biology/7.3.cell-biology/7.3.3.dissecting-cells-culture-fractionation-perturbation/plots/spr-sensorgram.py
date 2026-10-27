# A surface plasmon resonance sensorgram for a protein (analyte, concentration C) binding a partner
# immobilized on the chip (1:1 Langmuir model, analyte in excess):
#   association:  dR/dt = k_on C (R_max - R) - k_off R,  R(t) = R_eq (1 - exp(-k_obs t)),
#                 R_eq = R_max C / (C + K_D),  k_obs = k_on C + k_off;
#   dissociation (buffer only, from t = 120 s):  R(t) = R(120) exp(-k_off (t - 120)).
# Illustrative constants: k_on = 1e5 M^-1 s^-1, k_off = 1e-3 s^-1 (K_D = 10 nM), R_max = 100 RU;
# analyte at 3, 10, 30, 100 and 300 nM, with 0.5 RU noise.
# A: the sensorgrams. B: equilibrium response against concentration (binding isotherm), giving K_D
# independently of the rate fits.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(4)
kon, koff, Rmax = 1e5, 1e-3, 100.0
KD = koff / kon
conc = [3e-9, 10e-9, 30e-9, 100e-9, 300e-9]
toks = ["neutral", "dna", "positive", "protein", "negative"]

fig, axs = plt.subplots(1, 2, figsize=(11.0, 3.9), gridspec_kw={"width_ratios": [1.5, 1]})
ax = axs[0]
t1 = np.linspace(0, 120, 241)
t2 = np.linspace(120, 400, 561)
for c, tok in zip(conc, toks):
    kobs = kon * c + koff
    Req = Rmax * c / (c + KD)
    R1 = Req * (1 - np.exp(-kobs * t1))
    R2 = R1[-1] * np.exp(-koff * (t2 - 120))
    tt = np.r_[-30, -0.5, t1, t2]
    RR = np.r_[0, 0, R1, R2] + rng.normal(0, 0.5, tt.size)
    ax.plot(tt, RR, color=charts.line(tok), lw=1.3, label=f"{c * 1e9:g} nM")
ax.axvspan(0, 120, color=P.fill("highlight"), alpha=0.25, lw=0)
ax.text(60, 101, "analyte injected", fontsize=7, color=P.ink(), ha="center", va="bottom")
ax.text(260, 101, "buffer: dissociation at k_off", fontsize=7, color=P.ink(), ha="center", va="bottom")
ax.set_xlim(-30, 400)
ax.set_ylim(-5, 110)
ax.legend(fontsize=7, frameon=False, loc="center right", title="analyte", title_fontsize=7)
charts.style_axes(ax, "t / s", "response / RU")
ax.set_title("A   Sensorgrams (K_D = 10 nM)", loc="left", fontsize=9, color=P.ink())

ax = axs[1]
cc = np.logspace(-10, -6, 200)
ax.semilogx(cc * 1e9, Rmax * cc / (cc + KD), color=charts.line("dna"), lw=1.8)
for c, tok in zip(conc, toks):
    ax.plot([c * 1e9], [Rmax * c / (c + KD)], "o", color=charts.line(tok), ms=5)
ax.axvline(KD * 1e9, color=P.muted(), lw=0.7, ls=":")
ax.axhline(Rmax / 2, color=P.muted(), lw=0.7, ls=":")
ax.text(KD * 1e9 * 1.15, 8, "K_D", fontsize=7, color=P.muted())
ax.set_xlim(0.1, 1000)
ax.set_ylim(0, 105)
charts.style_axes(ax, "analyte concentration / nM", "R_eq / RU")
ax.set_title("B   Equilibrium isotherm", loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
