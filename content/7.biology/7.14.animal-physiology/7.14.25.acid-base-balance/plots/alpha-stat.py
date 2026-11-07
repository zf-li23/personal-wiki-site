# Blood pH and temperature: the alpha-stat hypothesis.
# A: neutral pH of water, pN = pKw / 2, from pKw(T) = 4470.99 / T - 6.0875 + 0.01706 T (T in K); the blood pH of
# ectotherms follows a line about 0.6 units above pN with slope about -0.017 per degree C (Reeves; Rahn), so
# the ratio [OH-]/[H+] stays near 16. Mammalian and avian blood is held at 7.40 at 37-41 degrees C, on the
# same line. B: fractional dissociation alpha of histidine imidazole groups (pK 6.8 at 37 degrees C,
# enthalpy of ionization 30 kJ/mol, van 't Hoff) when blood pH follows the ectotherm line (alpha-stat) or is
# held at 7.40 at every temperature (pH-stat): only the first keeps protein charge constant.
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 40, 200)
T = t + 273.15
pkw = 4470.99 / T - 6.0875 + 0.01706 * T
pn = pkw / 2
offset = 7.40 - np.interp(37, t, pn)
blood = pn + offset

fig, (axa, axb) = plt.subplots(1, 2, figsize=(10.5, 4.2))
axa.plot(t, pn, color="#7a7a7a", lw=2, label="neutral water, pN")
axa.plot(t, blood, color="#c0392b", lw=2, label="ectotherm blood (pN + 0.6)")
axa.plot([37], [7.40], "o", color="#2f6fb5", ms=7, label="mammal, 37 °C")
slope = np.polyfit(t, blood, 1)[0]
axa.text(10, 7.5, f"slope {slope:.3f} pH units per °C", fontsize=8.5)
axa.set_xlabel("Body temperature (°C)")
axa.set_ylabel("pH")
axa.set_ylim(6.6, 8.2)
axa.set_title("A  Blood pH follows neutrality", loc="left", fontsize=11, fontweight="bold")
axa.legend(frameon=False, fontsize=8.5, loc="upper right")

R, dH = 8.314, 30e3
pk = 6.8 + dH / (np.log(10) * R) * (1 / T - 1 / 310.15)
alpha_stat = 1 / (1 + 10 ** (pk - blood))
ph_stat = 1 / (1 + 10 ** (pk - 7.40))
axb.plot(t, alpha_stat, color="#c0392b", lw=2, label="alpha-stat (pH follows the line)")
axb.plot(t, ph_stat, color="#2f6fb5", lw=2, ls="--", label="pH-stat (pH 7.40 at all T)")
axb.set_ylim(0.5, 1.0)
axb.set_xlabel("Body temperature (°C)")
axb.set_ylabel("Imidazole fraction unprotonated, alpha")
axb.set_title("B  Protein charge state", loc="left", fontsize=11, fontweight="bold")
axb.legend(frameon=False, fontsize=8.5, loc="lower left")
for ax in (axa, axb):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
fig.tight_layout()
