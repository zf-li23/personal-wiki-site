# Tubular fluid to plasma concentration ratios (TF/P) along the proximal tubule (schematic model).
# Water: the fraction of the filtered water reabsorbed rises along the tubule, f(x) = 0.67 x^0.9, so the
# TF/P of an indicator that is neither reabsorbed nor secreted (inulin) is 1 / (1 - f).
# A solute s reabsorbed with fractional profile r_s(x) has TF/P = (1 - r_s) / (1 - f):
#   Na+: reabsorbed isosmotically, r = f, so TF/P = 1 throughout.
#   glucose and amino acids: r = 1 - exp(-x / 0.12) (taken up in the first quarter by Na+ cotransport).
#   HCO3-: TF/P falls to about 0.3 in the first half (Na+/H+ exchange with carbonic anhydrase).
#   Cl-: anions are conserved, so Cl- rises as HCO3- falls: [Cl-] = 106 + 24 (1 - TF/P_HCO3) mM.
#   urea: about half of the filtered urea is reabsorbed by the end, r = 0.6 f.
#   phosphate: r = 0.77 f / 0.67 (NaPi cotransport; TF/P about 0.7 at the end).
#   PAH: secreted, so its TF/P exceeds that of inulin.
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 300)
f = 0.67 * x ** 0.9
inulin = 1 / (1 - f)
na = np.ones_like(x)
glucose = np.exp(-x / 0.12) / (1 - f)
hco3 = 0.3 + 0.7 * np.exp(-x / 0.22)
cl = (106 + 24 * (1 - hco3)) / 106
urea = (1 - 0.6 * f) / (1 - f)
pi_ = (1 - 0.77 * f / 0.67) / (1 - f)
pah = inulin * (1 + 2.0 * x)

fig, ax = plt.subplots(figsize=(6.6, 4.4))
curves = [
    (pah, "PAH (secreted)", "#7a4fb3", "-"),
    (inulin, "Inulin (water reabsorbed)", "#7a7a7a", "-"),
    (urea, "Urea", "#8c6d31", "-"),
    (cl, "Cl$^-$", "#3c9a5f", "-"),
    (na, "Na$^+$, osmolality", "#2f6fb5", "-"),
    (pi_, "Phosphate", "#e08a3c", "--"),
    (hco3, "HCO$_3^-$", "#c0392b", "--"),
    (glucose, "Glucose, amino acids", "#c0392b", "-"),
]
offset = {"Cl$^-$": 1.1, "Na$^+$, osmolality": 0.92}
for y, lab, c, ls in curves:
    ax.plot(x * 100, y, color=c, lw=2, ls=ls)
    if y[-1] < 0.05:
        ax.text(43, 0.062, lab, color=c, fontsize=8.5, ha="left")
    else:
        ax.text(101, y[-1] * offset.get(lab, 1.0), lab, color=c, fontsize=8.5, va="center")
ax.set_yscale("log")
ax.set_ylim(0.05, 12)
ax.set_yticks([0.1, 0.3, 1, 3, 10])
ax.set_yticklabels(["0.1", "0.3", "1", "3", "10"])
ax.set_xlim(0, 100)
ax.set_xlabel("Proximal tubule length (%)")
ax.set_ylabel("TF/P (log scale)")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
fig.subplots_adjust(left=0.12, right=0.66, bottom=0.13, top=0.95)
