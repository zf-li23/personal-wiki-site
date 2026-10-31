"""Nonlinear elasticity of soft tissues. A: the stress-strain curve of a tendon from a fiber-recruitment
model: 2000 collagen fibers, each linearly elastic (modulus 1.5 GPa) once straightened, with crimp
(slack strains) distributed normally with mean 2 % and standard deviation 0.6 %, each failing at
5-8 % strain beyond its slack, collagen volume fraction 0.5: a toe region where fibers are progressively recruited, a linear region
when all carry load, and yield and rupture as fibers fail. B: the exponential (Fung) law
sigma = c (exp(b epsilon) - 1) describes arteries and skin, whose stiffness grows in proportion to the
stress, d sigma/d epsilon = b (sigma + c): curves for an artery in the circumferential and axial
directions (illustrative parameters c = 10 and 20 kPa, b = 8 and 5), showing the anisotropy."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 2, figsize=(8.6, 3.3))
fig.subplots_adjust(wspace=0.32, left=0.09, right=0.98, bottom=0.16, top=0.87)
rng = np.random.default_rng(0)
Nf, Ef = 2000, 1.5e9
slack = np.clip(rng.normal(0.02, 0.006, Nf), 0, None)
fail = slack + rng.uniform(0.05, 0.08, Nf)
eps = np.linspace(0, 0.12, 600)
sig = np.array([Ef / Nf * np.sum(np.where((e > slack) & (e < fail), e - slack, 0)) for e in eps]) * 0.5  # collagen volume fraction 0.5
ax = axs[0]
ax.plot(eps * 100, sig / 1e6, color=charts.line("bone"), lw=1.8)
for txt, e0 in [("toe", 1.5), ("linear", 4.5), ("failure", 9.0)]:
    i = np.argmin(np.abs(eps * 100 - e0))
    ax.annotate(txt, (eps[i] * 100, sig[i] / 1e6), xytext=(-28, 6), textcoords="offset points", fontsize=FT["tiny"],
                color=P.ink())
charts.style_axes(ax, r"strain / %", "stress / MPa")
charts.title(ax, "A  Tendon: fiber recruitment")
ax = axs[1]
e = np.linspace(0, 0.6, 300)
for c, b, tok, lab in [(10e3, 8.0, "blood", "circumferential"), (20e3, 5.0, "dna", "axial")]:
    ax.plot(e * 100, c * (np.exp(b * e) - 1) / 1e3, color=charts.line(tok), lw=1.7, label=lab)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
ax.set_ylim(0, 1200)
charts.style_axes(ax, r"strain / %", "stress / kPa")
charts.title(ax, "B  Artery: exponential stiffening")
