# Phytochrome B as a thermosensor: light-driven photoconversion competes with thermal (dark) reversion
# of Pfr to Pr, whose rate constant k_r rises with temperature.
# Steady state under light: [Pfr]/[P_tot] = k1 / (k1 + k2 + k_r), with k1, k2 the photoconversion rate
# constants (Pr->Pfr, Pfr->Pr) for a daylight-shaped spectrum, computed from the Pr/Pfr model spectra of
# phytochrome-spectra.py with sigma_r(660 nm) = 4.1e-3 m2/umol; light is given as PAR photon flux.
# Darkness: [Pfr](t) = [Pfr](0) exp(-k_r t).
# Illustrative k_r: 2e-4 s-1 at 22 C (one effective rate for the mixture of dimer states), Q10 = 3.
import matplotlib.pyplot as plt
import numpy as np

wl = np.arange(300, 801, 1.0)


def band(c, a, sl, sr):
    s = np.where(wl < c, sl, sr)
    return a * np.exp(-0.5 * ((wl - c) / s) ** 2)


BASE_R = 0.012 * (wl < 720) * np.exp(-np.clip(wl - 650, 0, None) / 25)
PR = band(666, 1.0, 28, 17) + band(612, 0.22, 22, 22) + band(380, 0.28, 35, 35) + band(700, 0.0253, 25, 25) + BASE_R
PFR = band(730, 1.07, 32, 20) + band(672, 0.2125, 25, 25) + band(400, 0.541, 40, 40) + band(610, 0.10, 30, 30) + 0.012
PHI_R, PHI_FR = 0.15, 0.07
SIG660 = 4.1e-3  # m2 per umol, Pr->Pfr at 660 nm
sig_r = SIG660 * PR / PR[wl == 660][0]
sig_f = SIG660 * (PFR * PHI_FR) / (PR[wl == 660][0] * PHI_R)

h, c, kB = 6.626e-34, 2.998e8, 1.381e-23
lam = wl * 1e-9
sun = lam**-4 / (np.exp(h * c / (lam * kB * 5800)) - 1)
sun = sun * (1 + 0.00146 * (660 - wl))
sun = sun / sun[(wl >= 400) & (wl <= 700)].sum()  # 1 umol m-2 s-1 of PAR in total
k1_per = (sun * sig_r).sum()
k2_per = (sun * sig_f).sum()


def kr(T):
    return 2e-4 * 3.0 ** ((T - 22) / 10)


I = np.logspace(-3, 3.3, 300)
fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.0))
temps = ((12, "#3b6fd8"), (22, "#2f7d4f"), (28, "#d9463b"))
for T, col in temps:
    k1, k2 = k1_per * I, k2_per * I
    a.semilogx(I, k1 / (k1 + k2 + kr(T)), color=col, lw=2.2, label=f"{T} °C")
a.axvspan(2e-2, 2, color="0.5", alpha=0.12, lw=0)
a.text(0.2, 0.05, "twilight", ha="center", fontsize=9)
a.axvline(2000, color="#e0a030", lw=1.0, ls=":")
a.text(1300, 0.05, "full sun", ha="right", fontsize=9, color="#b07818")
a.set_xlabel(r"PAR photon flux / $\mu$mol m$^{-2}$ s$^{-1}$")
a.set_ylabel(r"Steady-state Pfr / P$_{\rm tot}$")
a.set_ylim(0, 0.7)
a.legend(frameon=False, fontsize=9, loc="upper left")
a.set_title("A   Light versus thermal reversion", loc="left", fontsize=10)

t = np.linspace(0, 12, 300)
for T, col in temps:
    b.plot(t, 0.6 * np.exp(-kr(T) * t * 3600), color=col, lw=2.2, label=f"{T} °C")
b.set_xlabel("Time after dusk / h")
b.set_ylabel(r"Pfr / P$_{\rm tot}$")
b.set_xlim(0, 12)
b.set_ylim(0, 0.65)
b.legend(frameon=False, fontsize=9, loc="upper right")
b.set_title("B   Dark reversion during the night", loc="left", fontsize=10)
for ax in (a, b):
    ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
