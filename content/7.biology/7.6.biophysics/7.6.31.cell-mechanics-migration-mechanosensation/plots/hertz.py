"""Atomic force microscopy indentation analyzed with the Hertz model. A: force against indentation
depth for a spherical probe of radius R = 2.5 um pressed into incompressible cells (Poisson ratio 0.5)
with Young's moduli 0.5, 2 and 10 kPa, F = (4/3) E/(1 - nu^2) R^(1/2) delta^(3/2). B: a synthetic
force curve (E = 2 kPa, contact point 0.2 um into the approach, force noise 30 pN rms) and the
least-squares fit of the Hertz model with E and the contact point as free parameters. C: the same data
on logarithmic axes after subtracting the fitted contact point: slope 3/2 for the sphere, compared with
the slope 2 of a conical tip (Sneddon, half-angle 35 degrees) of the same modulus."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.2))
fig.subplots_adjust(wspace=0.38, left=0.07, right=0.98, bottom=0.17, top=0.87)
R, nu = 2.5e-6, 0.5
d = np.linspace(0, 1.0e-6, 200)


def hertz(delta, E):
    return 4 / 3 * E / (1 - nu ** 2) * np.sqrt(R) * np.clip(delta, 0, None) ** 1.5


ax = axs[0]
for E, tok in [(500, "dna"), (2000, "bacterium"), (10000, "blood")]:
    ax.plot(d * 1e6, hertz(d, E) * 1e9, color=charts.line(tok), lw=1.7, label=f"E = {E / 1000:g} kPa")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"indentation $\delta$ / $\mu$m", "force / nN")
charts.title(ax, "A  Hertz model, sphere")

rng = np.random.default_rng(0)
z = np.linspace(0, 1.2e-6, 120)  # piezo travel after the start of approach
z0_true = 0.2e-6
Fdat = hertz(z - z0_true, 2000) + 30e-12 * rng.standard_normal(len(z))
model = lambda z, E, z0: hertz(z - z0, E)
(Efit, z0fit), cov = curve_fit(model, z, Fdat, p0=(1000, 0.1e-6))
ax = axs[1]
ax.plot(z * 1e6, Fdat * 1e9, "o", ms=2.5, color=charts.line("protein"), label="synthetic data")
ax.plot(z * 1e6, model(z, Efit, z0fit) * 1e9, color=charts.line("blood"), lw=1.5,
        label=f"fit: E = {Efit / 1000:.2f} kPa,\ncontact at {z0fit * 1e6:.2f} " + r"$\mu$m")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"probe travel / $\mu$m", "force / nN")
charts.title(ax, "B  Fitting a force curve")

ax = axs[2]
dd = z - z0fit
sel = (dd > 0.03e-6) & (Fdat > 0)
ax.loglog(dd[sel] * 1e6, Fdat[sel] * 1e9, "o", ms=2.5, color=charts.line("protein"))
dl = np.logspace(-1.5, 0, 50) * 1e-6
ax.loglog(dl * 1e6, hertz(dl, Efit) * 1e9, color=charts.line("blood"), lw=1.4, label=r"sphere, $\propto\delta^{3/2}$")
cone = 2 / np.pi * 2000 / (1 - nu ** 2) * np.tan(np.deg2rad(35)) * dl ** 2
ax.loglog(dl * 1e6, cone * 1e9, "--", color=charts.line("dna"), lw=1.4, label=r"cone, $\propto\delta^{2}$")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"indentation / $\mu$m", "force / nN")
charts.title(ax, "C  Power laws")
