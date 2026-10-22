"""Periodic trends for Z = 1-56: radius, first ionization energy, electron affinity, electronegativity."""

import numpy as np
import matplotlib.pyplot as plt

EV = 96.485  # kJ/mol per eV
SYM = ("H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn "
       "Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba").split()
Z = np.arange(1, 57)
nan = np.nan
# covalent (single-bond) radii / pm, textbook values; noble gases omitted
radius = [37, nan, 123, 89, 82, 77, 70, 66, 64, nan, 154, 136, 118, 117, 110, 104, 99, nan,
          203, 174, 144, 132, 122, 118, 117, 117, 116, 115, 117, 125, 126, 122, 121, 117, 114, nan,
          216, 191, 162, 145, 134, 130, 127, 125, 125, 128, 134, 148, 144, 140, 141, 137, 133, nan,
          235, 198]
# first ionization energies / eV (NIST)
ie = [13.598, 24.587, 5.392, 9.323, 8.298, 11.260, 14.534, 13.618, 17.423, 21.565,
      5.139, 7.646, 5.986, 8.152, 10.487, 10.360, 12.968, 15.760,
      4.341, 6.113, 6.561, 6.828, 6.746, 6.767, 7.434, 7.902, 7.881, 7.640, 7.726, 9.394,
      5.999, 7.900, 9.789, 9.752, 11.814, 14.000,
      4.177, 5.695, 6.217, 6.634, 6.759, 7.092, 7.28, 7.361, 7.459, 8.337, 7.576, 8.994,
      5.786, 7.344, 8.608, 9.010, 10.451, 12.130, 3.894, 5.212]
# electron affinities / eV; None marks an unstable anion
ea = [0.754, None, 0.618, None, 0.280, 1.262, None, 1.461, 3.401, None,
      0.548, None, 0.433, 1.390, 0.746, 2.077, 3.613, None,
      0.501, 0.025, 0.188, 0.079, 0.525, 0.666, None, 0.151, 0.662, 1.156, 1.235, None,
      0.30, 1.233, 0.804, 2.021, 3.364, None,
      0.486, 0.048, 0.307, 0.426, 0.893, 0.748, 0.55, 1.05, 1.137, 0.562, 1.304, None,
      0.38, 1.112, 1.047, 1.971, 3.059, None, 0.472, 0.145]
# Pauling electronegativity (CRC); noble gases without values omitted
chi = [2.20, nan, 0.98, 1.57, 2.04, 2.55, 3.04, 3.44, 3.98, nan,
       0.93, 1.31, 1.61, 1.90, 2.19, 2.58, 3.16, nan,
       0.82, 1.00, 1.36, 1.54, 1.63, 1.66, 1.55, 1.83, 1.88, 1.91, 1.90, 1.65,
       1.81, 2.01, 2.18, 2.55, 2.96, 3.00,
       0.82, 0.95, 1.22, 1.33, 1.6, 2.16, 1.9, 2.2, 2.28, 2.20, 1.93, 1.69,
       1.78, 1.96, 2.05, 2.1, 2.66, 2.60, 0.79, 0.89]

fig, axes = plt.subplots(4, 1, figsize=(10, 10.5), sharex=True)
data = [
    (np.array(radius, float), r"$r\,/\,\mathrm{pm}$"),
    (np.array(ie) * EV, r"$I_1\,/\,(\mathrm{kJ\,mol^{-1}})$"),
    (None, r"$E_{\mathrm{ea}}\,/\,(\mathrm{kJ\,mol^{-1}})$"),
    (np.array(chi, float), r"$\chi$ (Pauling)"),
]
for ax, (y, label) in zip(axes, data):
    for zn in (2, 10, 18, 36, 54):
        ax.axvline(zn, color="0.75", lw=0.7, ls=":")
    if y is None:
        bound = np.array([v is not None for v in ea])
        vals = np.array([v * EV if v is not None else 0.0 for v in ea])
        ax.plot(Z, vals, color="C2", lw=1.0)
        ax.plot(Z[bound], vals[bound], "o", color="C2", ms=4)
        ax.plot(Z[~bound], vals[~bound], "o", mfc="none", mec="C2", ms=4)
        y = vals
    else:
        ax.plot(Z, y, "o-", color="C0" if ax is axes[0] else ("C3" if ax is axes[1] else "C1"),
                ms=4, lw=1.0)
    ax.set_ylabel(label)
    # annotate selected elements
    for s in ["H", "He", "Li", "N", "O", "F", "Na", "Cl", "K", "Kr", "Cs", "Zn", "Xe", "I", "Be"]:
        k = SYM.index(s)
        if not np.isnan(y[k]):
            ax.annotate(s, (Z[k], y[k]), xytext=(3, 3), textcoords="offset points", fontsize=7)
axes[-1].set_xlabel("atomic number Z")
axes[-1].set_xlim(0, 57)
fig.tight_layout()
