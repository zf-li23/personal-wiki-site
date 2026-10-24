"""Frontier orbital energies of simple pi systems, estimated from experiment with Koopmans'
approximation: E(HOMO) ~ -(first vertical ionization energy), E(LUMO) ~ -(vertical electron
affinity), i.e. + the electron-attachment energy measured by electron transmission spectroscopy.
Alkyl groups raise the HOMO (faster electrophilic addition); the alkyne HOMO lies below that of
ethylene; conjugation raises the HOMO and lowers the LUMO."""

import matplotlib.pyplot as plt

# name: (ionization energy / eV, vertical attachment energy / eV or None)
data = {
    "ethyne": (11.40, 2.6),
    "ethene": (10.51, 1.78),
    "propene": (9.73, None),
    "2-methyl-\npropene": (9.22, None),
    "1,3-buta-\ndiene": (9.07, 0.62),
}
fig, ax = plt.subplots(figsize=(6.4, 4.2))
for i, (name, (ie, ae)) in enumerate(data.items()):
    ax.hlines(-ie, i - 0.3, i + 0.3, color="C0", lw=2.5)
    ax.text(i, -ie - 0.55, f"{-ie:.2f}", ha="center", fontsize=8, color="C0")
    if ae is not None:
        ax.hlines(ae, i - 0.3, i + 0.3, color="C3", lw=2.5)
        ax.text(i, ae + 0.25, f"+{ae:.2f}", ha="center", fontsize=8, color="C3")
ax.axhline(0, color="0.6", lw=0.6, ls=":")
ax.set_xticks(range(len(data)), list(data), fontsize=9)
ax.set_ylabel("orbital energy / eV")
ax.set_ylim(-12.5, 4.0)
ax.set_xlim(-0.6, len(data) - 0.4)
ax.text(len(data) - 0.45, 3.3, "LUMO", color="C3", ha="right", fontsize=9)
ax.text(len(data) - 0.45, -11.9, "HOMO", color="C0", ha="right", fontsize=9)
