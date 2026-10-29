"""Linear stability of the reduced mechanochemical model of dermal condensation (Percus and Childress, after
Oster, Murray and Harris; Formula 22.5.2), with mu = D1 = 1 and substrate stiffness s = 0.1, so that the critical
traction is tau_c = 1/2 + sqrt(mu s D1) = 0.82 and the critical wavenumber k_c = (s / mu D1)^(1/4) = 0.56. (A) The
coefficient b(k^2) = mu D1 k^4 + (1 - 2 tau) k^2 + s for traction tau below, at and above tau_c: instability sets in
where b becomes negative. (B) Largest real part of the growth rate lambda as a function of wavenumber: above
tau_c a band of wavenumbers around k_c grows, setting the spacing of the condensations (feather buds, scales,
hair follicles). (C) Imaginary part of the most unstable root: in this reduced model the instability first appears
as an oscillatory one (b passes through zero while c > 0); with stronger traction (tau > 1 + s / k^2) a real
root becomes positive at short wavelengths."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
mu, D1, s = 1.0, 1.0, 0.1
tc = 0.5 + np.sqrt(mu * s * D1)
kc = (s / (mu * D1)) ** 0.25
k = np.linspace(0.01, 1.6, 500)
K = k ** 2
fig, axs = plt.subplots(1, 3, figsize=(11.6, 3.7))
fig.subplots_adjust(left=0.06, right=0.985, bottom=0.17, top=0.86, wspace=0.33)
for tau, tok in ((0.7, "neutral"), (tc, "antibody"), (0.95, "negative")):
    b = mu * D1 * K ** 2 + (1 - 2 * tau) * K + s
    c = K * D1 * (K * (1 - tau) + s)
    disc = b * b - 4 * mu * K * c + 0j
    lam = (-b + np.sqrt(disc)) / (2 * mu * K)
    lab = rf"$\tau$ = {tau:.2f}" + (" (critical)" if abs(tau - tc) < 1e-9 else "")
    axs[0].plot(k, b, color=charts.line(tok), lw=1.6, label=lab)
    axs[1].plot(k, lam.real, color=charts.line(tok), lw=1.6, label=lab)
    axs[2].plot(k, np.abs(lam.imag), color=charts.line(tok), lw=1.6, label=lab)
for a in axs:
    a.axvline(kc, color=P_.muted(), lw=0.7, ls=":")
axs[0].axhline(0, color=P_.muted(), lw=0.7)
axs[1].axhline(0, color=P_.muted(), lw=0.7)
axs[0].text(kc + 0.03, 0.8, r"$k_c$", fontsize=FT["tiny"], color=P_.muted())
axs[0].legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="upper left")
axs[0].set_ylim(-0.25, 1.0)
charts.style_axes(axs[0], "wavenumber k", r"$b(k^2)$")
charts.title(axs[0], "A  The coefficient b")
axs[1].set_ylim(-0.3, 0.15)
charts.style_axes(axs[1], "wavenumber k", r"largest Re $\lambda$")
charts.title(axs[1], "B  Growth rate")
charts.style_axes(axs[2], "wavenumber k", r"$|\mathrm{Im}\,\lambda|$")
charts.title(axs[2], "C  Oscillation frequency")
