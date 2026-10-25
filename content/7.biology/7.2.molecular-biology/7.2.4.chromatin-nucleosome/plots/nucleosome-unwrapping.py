# Two-state models of nucleosome opening. A: pulling a nucleosome with force F tilts the free energy of the open
# state by -F dz, so P_open(F) = 1 / (1 + exp[(dG - F dz)/kBT]). Simulated optical-trap measurements (points,
# dG = 30 kBT, dz = 40 nm, kBT = 4.1 pN nm, binomial noise from 60 observations per force) are fitted by least
# squares; the fit returns F1/2 = dG/dz and dz, hence dG = F1/2 dz. B: site exposure (Polach and Widom). A factor
# can bind its site only while the DNA there is transiently unwrapped (equilibrium constant K_conf), so its
# apparent dissociation constant rises from K_D to K_D (1 + K_conf)/K_conf: sites near the entry of the core
# particle (K_conf ~ 1e-2) are occupied at 100-fold higher concentration, sites near the dyad (~1e-4) at 1e4-fold.
import numpy as np
from scipy.optimize import curve_fit
import wikibio as bio
from wikibio import charts as C

P = bio.P
kT = 4.1  # pN nm at 298 K
dG, dz = 30 * kT, 40.0


def p_open(F, F12, dz):
    return 1 / (1 + np.exp(dz * (F12 - F) / kT))


fig, ax = bio.canvas(19.0, 7.8)
rng = np.random.default_rng(0)
F = np.r_[np.linspace(1.6, 2.4, 3), np.linspace(2.6, 3.6, 11), np.linspace(3.9, 4.6, 3)]
n_obs = 60
data = rng.binomial(n_obs, p_open(F, dG / dz, dz)) / n_obs
(F12_fit, dz_fit), _ = curve_fit(p_open, F, data, p0=(3.0, 30.0))
Ff = np.linspace(0, 6, 400)

a = C.axes_at(ax, (1.4, 1.3, 7.2, 5.3))
a.plot(Ff, p_open(Ff, dG / dz, dz), color=P.muted(), lw=1.0, ls=(0, (4, 3)), label="model (true)")
a.plot(Ff, p_open(Ff, F12_fit, dz_fit), color=C.line("chromatin"), lw=2.0, label="fit")
a.plot(F, data, "o", ms=4.5, mfc=P.fill("chromatin"), mec=C.line("chromatin"), mew=0.9, label="simulated data")
a.axvline(F12_fit, color=P.muted(), lw=0.8, ls=(0, (2, 2)))
a.axhline(0.5, color=P.muted(), lw=0.8, ls=(0, (2, 2)))
a.text(F12_fit + 0.12, 0.08, f"$F_{{1/2}}$ = {F12_fit:.2f} pN\n$\\Delta z$ = {dz_fit:.0f} nm\n"
       f"$\\Delta G = F_{{1/2}}\\Delta z$ ≈ {F12_fit * dz_fit / kT:.0f} $k_\\mathrm{{B}}T$",
       fontsize=bio.core.FONT["tiny"], color=P.ink(), va="bottom")
a.set_xlim(0, 6)
a.set_ylim(-0.03, 1.05)
C.style_axes(a, "force F / pN", "$P_\\mathrm{open}$")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "A", (0.1, 7.7))
bio.label(ax, (0.6, 7.35), "Unwrapping under force", size="normal", bold=True, ha="left")

b = C.axes_at(ax, (11.2, 1.3, 7.2, 5.3))
c = np.logspace(-11, -3, 400)
KD = 1e-9
for Kc, tok, name in [(None, "dna", "naked DNA"), (1e-2, "positive", "$K_\\mathrm{conf}=10^{-2}$ (near entry)"),
                      (1e-4, "negative", "$K_\\mathrm{conf}=10^{-4}$ (near dyad)")]:
    Kapp = KD if Kc is None else KD * (1 + Kc) / Kc
    b.plot(c, c / (c + Kapp), color=C.line(tok), lw=2.0, label=name)
b.set_xscale("log")
b.set_xlim(1e-11, 1e-3)
b.set_ylim(0, 1.03)
b.set_xticks([1e-11, 1e-9, 1e-7, 1e-5, 1e-3], ["10 pM", "1 nM", "100 nM", "10 µM", "1 mM"])
C.style_axes(b, "[factor]", "site occupancy")
b.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper left")
b.text(1.3e-11, 0.42, "$K_D = 1$ nM\non naked DNA", fontsize=bio.core.FONT["tiny"], color=P.muted())
bio.panel(ax, "B", (9.9, 7.7))
bio.label(ax, (10.4, 7.35), "Site exposure: binding needs transient unwrapping", size="normal", bold=True, ha="left")
