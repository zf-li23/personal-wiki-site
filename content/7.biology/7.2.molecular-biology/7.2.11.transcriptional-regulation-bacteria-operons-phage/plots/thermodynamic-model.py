# The thermodynamic model of lac regulation (weak-promoter limit).
# A: simple repression, fold change = 1 / (1 + R/N_NS exp(-beta d_eps)), N_NS = 4.6e6, for operators with
#    binding energies -17.0 (Oid), -15.3 (O1), -13.9 (O2), -9.7 kBT (O3) (Garcia and Phillips 2011).
# B: induction with an MWC repressor: active fraction
#    p_act = (1 + c/KA)^2 / ((1 + c/KA)^2 + exp(-beta d_eps_AI) (1 + c/KI)^2),
#    KA = 140 uM, KI = 0.5 uM, d_eps_AI = 4.5 kBT (Razo-Mejia et al. 2018), O1 with R = 10, 100, 1000.
# C: activation, fold change = (1 + a exp(-beta eps_ap)) / (1 + a) with eps_ap = -3.9 kBT (max ~50-fold) and
#    a proportional to the cAMP-liganded fraction of CAP (half-saturation 50 uM, Hill coefficient 2; a_max = 50),
#    compared with a CAP-deficient strain (a = 0).
# D: repression (1 / fold change) by O1 plus an auxiliary operator O2 at distance L (bp), Eq. (11.5):
#    FC = (1 + r_aux) / (1 + r1 + r_aux + r1 r_aux + r1 K_loop(L)), K_loop = exp(-beta dF(L)),
#    beta dF = F0 + 1.5 ln L + a lp / L + 2 pi^2 (C_eff / L) delta^2, delta = L/10.5 - round(L/10.5),
#    lp = 150 bp, a = 0.75, C_eff = 35 bp; F0 is chosen so that the best loop gives ~1000-fold repression with
#    R = 10. An illustrative minimal model, not a fit.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
NNS = 4.6e6
fig, ax = bio.canvas(20.0, 15.0)
fs = bio.core.FONT["tiny"]

# --- A ---
a = C.axes_at(ax, (2.0, 8.8, 6.6, 5.2))
R = np.logspace(0, 3.5, 300)
for de, name, tok in [(-17.0, "Oid", "negative"), (-15.3, "O1", "enzyme"), (-13.9, "O2", "dna"), (-9.7, "O3", "neutral")]:
    fc = 1 / (1 + R / NNS * np.exp(-de))
    a.loglog(R, fc, color=C.line(tok), lw=1.8, label=f"{name} ({de:g} " .replace("-", "−") + r"$k_{\mathrm{B}}T$)")
a.axvline(10, color=P.muted(), lw=0.8, ls=(0, (1.5, 2)))
a.set_xlim(1, 10 ** 3.5)
a.set_ylim(1e-4, 1.5)
C.style_axes(a, "repressors per cell R", "fold change")
a.legend(fontsize=fs, frameon=False, labelcolor=P.ink(), loc="lower left")
bio.panel(ax, "A", (0.1, 14.8))

# --- B ---
b = C.axes_at(ax, (12.4, 8.8, 6.6, 5.2))
c = np.logspace(-2, 4, 400)  # IPTG / uM
KA, KI, dAI = 140.0, 0.5, 4.5
pact = (1 + c / KA) ** 2 / ((1 + c / KA) ** 2 + np.exp(-dAI) * (1 + c / KI) ** 2)
for Rn, tok in [(10, "dna"), (100, "enzyme"), (1000, "negative")]:
    fc = 1 / (1 + pact * Rn / NNS * np.exp(15.3))
    b.loglog(c, fc, color=C.line(tok), lw=1.8, label=f"O1, R = {Rn}")
b.set_xlim(1e-2, 1e4)
b.set_ylim(1e-3, 1.5)
C.style_axes(b, "[IPTG] / µM", "fold change")
b.legend(fontsize=fs, frameon=False, labelcolor=P.ink(), loc="lower right")
bio.panel(ax, "B", (10.5, 14.8))

# --- C ---
cc = C.axes_at(ax, (2.0, 1.4, 6.6, 5.2))
camp = np.logspace(-1, 4, 400)  # uM
occ = camp ** 2 / (camp ** 2 + 50.0 ** 2)
amax, eap = 50.0, -3.9
act = amax * occ
fc_wt = (1 + act * np.exp(-eap)) / (1 + act)
cc.semilogx(camp, fc_wt, color=C.line("positive"), lw=1.8, label="wild type")
cc.semilogx(camp, np.ones_like(camp), color=C.line("negative"), lw=1.8, ls=(0, (4, 2)), label="CAP-deficient")
cc.set_xlim(0.1, 1e4)
cc.set_ylim(0, 50)
C.style_axes(cc, "[cAMP] / µM", "expression relative to basal")
cc.legend(fontsize=fs, frameon=False, labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "C", (0.1, 7.4))

# --- D ---
d = C.axes_at(ax, (12.4, 1.4, 6.6, 5.2))
L = np.arange(40, 401)
r1 = 10 / NNS * np.exp(15.3)
raux = 10 / NNS * np.exp(13.9)
lp, aa, Ceff = 150.0, 0.75, 35.0
delta = L / 10.5 - np.round(L / 10.5)
g = 1.5 * np.log(L) + aa * lp / L + 2 * np.pi ** 2 * Ceff / L * delta ** 2
# calibrate F0: best loop -> 1000-fold repression
target = 1000.0
Kbest = (target * (1 + raux) - (1 + r1 + raux + r1 * raux)) / r1
F0 = -np.log(Kbest) - g.min()
Kloop = np.exp(-(F0 + g))
fc = (1 + raux) / (1 + r1 + raux + r1 * raux + r1 * Kloop)
d.plot(L, 1 / fc, color=C.line("enzyme"), lw=1.4)
d.axhline(1 + r1, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
d.text(300, (1 + r1) * 1.6, "O1 alone", fontsize=fs, color=P.muted())
d.set_yscale("log")
d.set_xlim(40, 400)
d.set_ylim(5, 2000)
C.style_axes(d, "distance between operators L / bp", "repression")
bio.panel(ax, "D", (10.5, 7.4))
