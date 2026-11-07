# Extracellular freezing dehydrates cells. A: water potential of ice relative to liquid water at the same
# temperature, Psi_ice = -dG_fus(T) / V_w, with dG_fus(T) = dH0 (1 - T/T0) - dCp [(T0 - T) - T ln(T0/T)],
# dH0 = 6.01 kJ/mol, dCp = 37.6 J/(mol K) (liquid minus ice), V_w = 18.0 cm3/mol, T0 = 273.15 K; dashed: the
# linear approximation -1.22 MPa per K. B: once ice forms in the apoplast, cell water leaves until the cell's
# osmotic potential equals Psi_ice; with turgor zero and the Boyle-van't Hoff relation Psi_s V = Psi_s0 V0, the
# fraction of osmotically active water retained is V/V0 = Psi_s0/Psi_ice (non-acclimated Psi_s0 = -1.0 MPa,
# typical -1.5 MPa, cold-acclimated with sugars -2.5 MPa). Homogeneous nucleation limits deep supercooling to
# about -40 C.
import matplotlib.pyplot as plt
import numpy as np

T0, dH, dCp, Vw = 273.15, 6010.0, 37.6, 18.0e-6
tc = np.linspace(-40, 0, 401)
T = T0 + tc
dG = dH * (1 - T / T0) - dCp * ((T0 - T) - T * np.log(T0 / T))
psi = -dG / Vw / 1e6  # MPa
fig, (a, b) = plt.subplots(1, 2, figsize=(12, 4.3))
a.plot(tc, psi, color="#3e7cb8", lw=2.4, label="$\\Psi_{\\mathrm{ice}}$ (with heat-capacity term)")
a.plot(tc, -1.22 * (-tc), color="0.5", lw=1.0, ls="--", label="linear: −1.22 MPa per °C")
for t in (-5, -10, -20):
    v = np.interp(t, tc, psi)
    a.plot([t], [v], "o", color="#3e7cb8", ms=5)
    a.annotate(f"{v:.1f} MPa", (t, v), xytext=(t + 1.2, v - 2.5), fontsize=8.5)
a.set_xlabel("Temperature / °C")
a.set_ylabel("Water potential of ice / MPa")
a.set_xlim(-40, 0)
a.legend(frameon=False, fontsize=8.5, loc="lower right")
a.set_title("A   Ice has a very low water potential", loc="left", fontsize=10)

for ps0, col, name in [(-1.0, "#d9463b", "$\\Psi_{\\mathrm{s0}}$ = −1.0 MPa"), (-1.5, "#d9a400", "−1.5 MPa"),
                       (-2.5, "#2e9e5b", "−2.5 MPa (acclimated)")]:
    m = psi < ps0
    frac = np.where(m, ps0 / np.where(m, psi, -1), 1.0)
    b.plot(tc, 100 * frac, color=col, lw=2.2, label=name)
b.axvline(-40, color="0.5", lw=0.8)
b.axvline(-10, color="0.6", lw=0.6, ls=":")
b.text(-39.3, 82, "homogeneous\nnucleation\n(≈ −40 °C)", fontsize=8, color="0.4")
b.set_xlabel("Temperature / °C")
b.set_ylabel("Osmotically active water retained / %")
b.set_xlim(-41, 0)
b.set_ylim(0, 105)
b.legend(frameon=False, fontsize=8.5, loc="upper left", bbox_to_anchor=(0.32, 1.0))
b.set_title("B   Cell dehydration at equilibrium", loc="left", fontsize=10)
fig.tight_layout()
