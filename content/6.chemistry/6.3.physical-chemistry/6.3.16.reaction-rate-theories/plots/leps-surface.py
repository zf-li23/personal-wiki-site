"""LEPS potential energy surface of the collinear reaction H + H2 -> H2 + H (Sato form).
Morse parameters of H2: De = 4.7466 eV, a = 1.942 1/Angstrom, re = 0.7416 Angstrom; the Sato
parameter 0.135 puts the saddle point near the accurate ab initio barrier (about 40 kJ/mol).
The minimum energy path is the steepest-descent path in mass-weighted coordinates.
Lengths are computed in Angstrom and plotted in nm (1 Angstrom = 0.1 nm)."""

import numpy as np
import matplotlib.pyplot as plt

De, a, re, S = 4.7466, 1.942, 0.7416, 0.135
eV = 96.485  # kJ/mol
nm = 0.1     # Angstrom -> nm for plotting


def QJ(r):
    x = np.exp(-a * (r - re))
    Q = De / 4 * ((3 + S) * x**2 - (2 + 6 * S) * x)
    J = De / 4 * ((1 + 3 * S) * x**2 - (6 + 2 * S) * x)
    return Q, J


def V(r1, r2):
    Q1, J1 = QJ(r1)
    Q2, J2 = QJ(r2)
    Q3, J3 = QJ(r1 + r2)
    return (Q1 + Q2 + Q3 - np.sqrt(0.5 * ((J1 - J2) ** 2 + (J2 - J3) ** 2 + (J3 - J1) ** 2))) / (1 + S)


V0 = V(re, 30.0)  # reactants: H2 at equilibrium plus a distant H


def grad(r1, r2, h=1e-6):
    return np.array([(V(r1 + h, r2) - V(r1 - h, r2)) / (2 * h), (V(r1, r2 + h) - V(r1, r2 - h)) / (2 * h)])


# saddle point on the symmetric line r1 = r2
rs = np.linspace(0.8, 1.1, 30001)
rsad = rs[np.argmin(V(rs, rs))]
Eb = (V(rsad, rsad) - V0) * eV

# inverse kinetic metric for bond-length coordinates of collinear ABC with equal masses m = 1
G = np.array([[2.0, -1.0], [-1.0, 2.0]])


def descend(start, n=6000, ds=2e-3):
    path = [np.array(start)]
    for _ in range(n):
        g = G @ grad(*path[-1])
        norm = np.sqrt(g @ np.linalg.solve(G, g))
        if norm < 1e-6:
            break
        path.append(path[-1] - ds * g / norm)
        if path[-1][1] > 3.0 or path[-1][0] > 3.0:
            break
    return np.array(path)


eps = 1e-3
branch1 = descend([rsad - eps, rsad + eps])
branch2 = descend([rsad + eps, rsad - eps])
mep = np.vstack([branch1[::-1], branch2])

r = np.linspace(0.4, 3.0, 300)
R1, R2 = np.meshgrid(r, r)
E = (V(R1, R2) - V0) * eV

fig, axs = plt.subplots(1, 2, figsize=(11, 4.6))
levels = np.arange(-20, 300, 20)
cs = axs[0].contour(R1 * nm, R2 * nm, E, levels=levels, cmap="viridis", linewidths=0.8)
axs[0].clabel(cs, levels[::2], fontsize=6, fmt="%d")
axs[0].plot(mep[:, 0] * nm, mep[:, 1] * nm, color="C3", lw=1.6, label="minimum energy path")
axs[0].plot([rsad * nm], [rsad * nm], "o", color="C3", ms=5)
axs[0].annotate("saddle point", (rsad * nm, rsad * nm), (0.15, 0.135), fontsize=8, arrowprops=dict(arrowstyle="-", lw=0.6))
axs[0].text(0.08, 0.26, r"H + H$_2$", fontsize=9)
axs[0].text(0.24, 0.08, r"H$_2$ + H", fontsize=9)
axs[0].set_xlabel(r"$r_{\mathrm{AB}}$ / nm")
axs[0].set_ylabel(r"$r_{\mathrm{BC}}$ / nm")
axs[0].set_aspect("equal")
axs[0].set_title("collinear H-H-H, contours in kJ/mol", fontsize=10)
axs[0].legend(frameon=False, fontsize=8, loc="upper right")

seg = np.sqrt(np.sum(np.diff(mep, axis=0) ** 2, axis=1))
s = np.concatenate([[0], np.cumsum(seg)])
s -= s[len(branch1) - 1]
Emep = (V(mep[:, 0], mep[:, 1]) - V0) * eV
axs[1].plot(s * nm, Emep, color="C3")
axs[1].axhline(0, color="0.6", ls=":", lw=1)
axs[1].annotate("", (0, Eb), (0, 0), arrowprops=dict(arrowstyle="<->", lw=0.8))
axs[1].text(0.008, Eb / 2, rf"$E_{{\mathrm{{b}}}}$ = {Eb:.0f} kJ/mol", fontsize=9, va="center")
axs[1].set_xlim(-0.2, 0.2)
axs[1].set_xlabel(r"reaction coordinate $s$ / nm (along the path)")
axs[1].set_ylabel(r"$E_{\mathrm{p}}$ / (kJ mol$^{-1}$)")
axs[1].set_title(rf"profile along the path, saddle at $r$ = {rsad * nm:.4f} nm", fontsize=10)
fig.tight_layout()
