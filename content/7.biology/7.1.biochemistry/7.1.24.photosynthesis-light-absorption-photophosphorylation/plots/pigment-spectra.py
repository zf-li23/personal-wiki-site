"""Light absorption by photosynthetic pigments and the two-photosystem logic of the red drop.
(A) Schematic absorption spectra of chlorophyll a, chlorophyll b and beta-carotene, built from Gaussian bands
at their absorption maxima in organic solvent (Chl a 430 and 662 nm; Chl b 453 and 642 nm; beta-carotene
425, 450 and 478 nm), each normalized to 1; not measured data. The dashed curve is a schematic action spectrum
of a green alga (relative O2 evolution per incident photon), high in the blue and red, low in the green, and
falling sharply beyond 680 nm. Top axis: energy of one mole of photons, E = N_A hc / lambda.
(B) A two-photosystem model of the red drop and the Emerson enhancement. PSII and PSI each absorb a fraction
of the light (PSI pigments extend further into the far red); linear flow needs one photon in each photosystem
per electron, so the quantum yield is 2 min(a1, a2)/(a1 + a2). Far-red light (> 680 nm) excites mainly PSI and
the yield drops; adding 650-nm light (absorbed more by PSII) to 690-nm light raises O2 evolution above the sum: the rate with both beams exceeds the sum
of the rates with each alone."""

import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
lam = np.linspace(380, 740, 721)


def band(c, w, h=1.0):
    return h * np.exp(-0.5 * ((lam - c) / w) ** 2)


chla = band(430, 16) + 0.75 * band(662, 11) + 0.12 * band(615, 14) + 0.08 * band(580, 15)
chlb = band(453, 15) + 0.33 * band(642, 11) + 0.1 * band(595, 15)
car = 0.75 * band(425, 11) + band(450, 13) + 0.85 * band(478, 12)
for s in (chla, chlb, car):
    s /= s.max()

fig, ax = bio.canvas(22.4, 8.6)
a = charts.axes_at(ax, (2.0, 1.4, 8.6, 5.9))
a.plot(lam, chla, color=charts.line("thylakoid"), lw=2.0, label="chlorophyll a")
a.plot(lam, chlb, color=charts.line("plant"), lw=2.0, label="chlorophyll b")
a.plot(lam, car, color=charts.line("antibody"), lw=2.0, label="β-carotene")
red_edge = 1 / (1 + np.exp((lam - 688) / 6))
action = np.clip(0.62 * chla + 0.45 * chlb + 0.3 * car + 0.12, 0, None) * red_edge
action /= action.max()
a.plot(lam, action, color=P.ink(), lw=1.4, ls="--", label="action spectrum (schematic)")
a.set_xlim(380, 740)
a.set_ylim(0, 1.15)
a.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(a, "wavelength λ / nm", "relative absorption")
top = a.secondary_xaxis("top", functions=(lambda x: 119627 / np.maximum(x, 1), lambda e: 119627 / np.maximum(e, 1)))
top.set_xticks([300, 250, 200, 175])
top.tick_params(colors=P.muted(), labelcolor=P.ink(), labelsize=bio.core.FONT["tiny"])
top.set_xlabel("photon energy / (kJ mol⁻¹)", fontsize=bio.core.FONT["small"], color=P.ink())
for sp in top.spines.values():
    sp.set_color(P.muted())

b = charts.axes_at(ax, (12.4, 1.4, 5.6, 5.9))
l2 = np.linspace(600, 720, 241)
ca, cb = np.interp(l2, lam, chla), np.interp(l2, lam, chlb)
a2 = (0.6 * ca + 0.9 * cb + 0.02) / (1 + np.exp((l2 - 680) / 5))  # PSII with LHCII (rich in Chl b), red edge 680 nm
a1 = (0.8 * ca + 0.2 * cb + 0.02) / (1 + np.exp((l2 - 702) / 6)) + 0.18 * np.exp(-0.5 * ((l2 - 700) / 9) ** 2)  # PSI, far-red Chl
phi = 2 * np.minimum(a1, a2) / (a1 + a2)
b.plot(l2, phi, color=charts.line("psi"), lw=2.0, label="quantum yield, one beam")
b.axvline(680, color=P.muted(), lw=0.8, ls=":")
b.text(676, 0.08, "red drop", ha="right", fontsize=bio.core.FONT["tiny"], color=P.muted())
b.set_xlim(600, 720)
b.set_ylim(0, 1.2)
b.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(b, "wavelength λ / nm", "relative quantum yield of O₂")

# Emerson enhancement with equal photon fluxes of a 690-nm and a 650-nm beam
i705, i650 = np.argmin(abs(l2 - 690)), np.argmin(abs(l2 - 650))
r_far = 2 * min(a1[i705], a2[i705])
r_red = 2 * min(a1[i650], a2[i650])
r_both = 2 * min(a1[i705] + a1[i650], a2[i705] + a2[i650])
c = charts.axes_at(ax, (19.4, 1.4, 2.2, 5.9))
c.bar([0, 1, 2, 3], [r_far, r_red, r_far + r_red, r_both], color=[P.fill("negative"), P.fill("enzyme"), P.fill("neutral"),
      P.fill("positive")], edgecolor=P.muted(), width=0.7)
c.set_xticks([0, 1, 2, 3])
c.set_xticklabels(["690", "650", "sum", "both"], fontsize=bio.core.FONT["tiny"])
charts.style_axes(c, "beam / nm", "O₂ evolution (relative)")
charts.title(c, "enhancement")
