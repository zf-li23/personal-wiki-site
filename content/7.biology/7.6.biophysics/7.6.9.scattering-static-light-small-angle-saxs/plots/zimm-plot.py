# Simulated Zimm plot of a large macromolecular assembly measured by multi-angle static light scattering.
# Model (Zimm equation): K c / R_theta = (1 / Mw) (1 + q^2 Rg^2 / 3) + 2 A2 c, with
# Mw = 2.0e6 g/mol, Rg = 40 nm, A2 = 2.0e-4 mol mL g^-2, laser wavelength 658 nm in water (n = 1.33),
# 4 concentrations (0.25 to 1.0 mg/mL) and 11 angles (30 to 150 degrees); 0.4 % Gaussian noise.
# The data are plotted against q^2 + k c (k = 2e-4 nm^-2 mL/mg spreads the concentrations). For each
# angle the points are extrapolated to c = 0 and for each concentration to theta = 0 (dashed lines);
# the two limiting lines (solid) share the intercept 1/Mw. Their slopes give Rg^2/(3 Mw) and 2 A2.
# The numbers recovered by least squares are printed in the figure.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(3)

MW, RG, A2 = 2.0e6, 40.0, 2.0e-4          # g/mol, nm, mol mL g^-2
lam, n0 = 658.0, 1.33
theta = np.radians(np.linspace(30, 150, 11))
q2 = (4 * np.pi * n0 * np.sin(theta / 2) / lam) ** 2   # nm^-2
conc = np.array([0.25, 0.5, 0.75, 1.0])                 # mg/mL
c_g = conc * 1e-3                                       # g/mL
Q2, C = np.meshgrid(q2, c_g)
y = (1 / MW) * (1 + Q2 * RG**2 / 3) + 2 * A2 * C       # mol/g
y *= 1 + 0.004 * rng.normal(size=y.shape)
Y = y * 1e7                                             # plot in 1e-7 mol/g
kspread = 2e-4                                          # nm^-2 per (mg/mL)
X = Q2 + kspread * conc[:, None]

# global least-squares fit of the Zimm equation: y = a + b q^2 + d c
A = np.column_stack([np.ones(y.size), Q2.ravel(), C.ravel()])
a, b, d = np.linalg.lstsq(A, y.ravel(), rcond=None)[0]
mw_fit, rg_fit, a2_fit = 1 / a, np.sqrt(3 * b / a), d / 2

fig, ax = plt.subplots(figsize=(7.6, 4.6))
cols = [charts.line(t) for t in ("dna", "protein", "rna", "negative")]
for i, cc in enumerate(conc):
    ax.plot(X[i] * 1e4, Y[i], "o", color=cols[i], ms=4.5, label=f"c = {cc:g} mg/mL")
    xs = np.array([kspread * cc, X[i, -1]])
    ax.plot(xs * 1e4, (a + d * c_g[i] + b * (xs - kspread * cc)) * 1e7, color=cols[i], lw=0.8, ls=(0, (3, 2)))
for j in range(len(q2)):
    xs = np.array([q2[j], q2[j] + kspread * conc[-1]])
    ax.plot(xs * 1e4, (a + b * q2[j] + d * (xs - q2[j]) / kspread * 1e-3) * 1e7, color=P.muted(), lw=0.6,
            ls=(0, (3, 2)))
x0 = np.array([0, q2[-1]])
ax.plot(x0 * 1e4, (a + b * x0) * 1e7, color=P.ink(), lw=1.6, label="c → 0")
xc = np.array([0, kspread * conc[-1]])
ax.plot(xc * 1e4, (a + d * xc / kspread * 1e-3) * 1e7, color=charts.line("positive"), lw=1.6, label="θ → 0")
ax.plot([0], [a * 1e7], "o", color=P.ink(), ms=6, mfc="none", mew=1.4)
ax.text(0.15, a * 1e7 - 0.22, "intercept 1/Mw", color=P.ink(), fontsize=7.5)
txt = (f"fit: Mw = {mw_fit / 1e6:.2f} × 10⁶ g/mol\n"
       f"Rg = {rg_fit:.1f} nm\nA₂ = {a2_fit * 1e4:.2f} × 10⁻⁴ mol mL g⁻²")
ax.text(0.02, 0.97, txt, transform=ax.transAxes, va="top", fontsize=8, color=P.ink())
ax.set_xlim(-0.1, None)
ax.legend(fontsize=7.5, frameon=False, loc="lower right", ncol=2)
charts.style_axes(ax, "q² + k c  /  (10⁻⁴ nm⁻²)", "K c / R_θ  /  (10⁻⁷ mol g⁻¹)")
