"""Mathematical models of cancer as a multistep process.

(A) Knudson's two-hit model of retinoblastoma. About N = 1.5e5 retinoblasts are at risk during early childhood;
each suffers inactivating hits of RB1 at rate mu = 4e-6 per allele per year. A child who inherits one mutant
allele needs one more hit in any cell: expected tumors m1(t) = N mu t, probability of disease 1 - exp(-m1).
A child born with two normal alleles needs both alleles of the same cell hit, probability about (mu t)^2 per cell:
m2(t) = N mu^2 t^2. By age 5 this gives about 3 tumors per hereditary child and disease in about 1 in 17 000
sporadic children. On log-log axes the cumulative incidence rises with slope 1 (one hit)
and slope 2 (two hits).
(B) Armitage-Doll multistage model: if a cell must pass through k rare, rate-limiting steps with rates
mu_1..mu_k, the incidence (hazard) at age t is approximately h(t) = N mu_1...mu_k t^(k-1)/(k-1)!, a straight line
of slope k - 1 on log-log axes. Curves are scaled to the same incidence at age 70 (1e-3 per year); the
observed slopes of 4-6 for many carcinomas suggested 5-7 steps.
(C) Two-stage clonal expansion model (Moolgavkar-Knudson): normal stem cells (N = 1e7) produce intermediate
cells at rate nu = 1e-7 per cell per year; intermediate clones grow at net rate g; each intermediate cell
becomes malignant at rate mu = 1e-7 per year: h(t) = N nu mu (exp(g t) - 1)/g (rare-event approximation).
With clonal expansion of the intermediate cells two steps produce steep, apparently high-order age curves:
the local log-log slope rises with age.
"""

import numpy as np
from matplotlib.ticker import NullFormatter
from math import factorial

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, ax = bio.canvas(27.0, 9.0)

# ---------------------------------------------------------------- A Knudson
bio.panel(ax, "A", (0.2, 8.8))
A = charts.axes_at(ax, (1.8, 1.5, 6.4, 6.6))
N, mu = 1.5e5, 4e-6
t = np.geomspace(0.05, 6, 200)
her = 1 - np.exp(-N * mu * t)
spo = 1 - np.exp(-N * mu**2 * t**2)
A.loglog(t, her, color=charts.line("negative"), lw=1.8, label="hereditary (one hit needed)")
A.loglog(t, spo, color=charts.line("dna"), lw=1.8, label="sporadic (two hits needed)")
A.loglog(t, 0.012 * t, color=P.muted(), lw=0.8, ls=":")
A.loglog(t, 2e-6 * t**2, color=P.muted(), lw=0.8, ls=":")
A.text(0.12, 0.0035, "slope 1", fontsize=FT["tiny"], color=P.muted())
A.text(1.6, 1.5e-6, "slope 2", fontsize=FT["tiny"], color=P.muted())
A.set_ylim(1e-8, 2)
A.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(A, "age / years", "probability of retinoblastoma")

# ---------------------------------------------------------------- B Armitage-Doll
bio.panel(ax, "B", (10.0, 8.8))
B = charts.axes_at(ax, (11.6, 1.5, 6.0, 6.6))
age = np.linspace(20, 85, 100)
toks = ["neutral", "dna", "channel", "positive", "drug", "negative"]
for k, tok in zip(range(2, 8), toks):
    h = age ** (k - 1) / factorial(k - 1)
    h = h / (70 ** (k - 1) / factorial(k - 1)) * 1e-3
    B.loglog(age, h, color=charts.line(tok), lw=1.6, label=f"k = {k} steps")
B.set_xticks([20, 30, 50, 70])
B.set_xticklabels(["20", "30", "50", "70"])
B.xaxis.set_minor_formatter(NullFormatter())
B.set_ylim(1e-7, 1e-2)
B.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(B, "age / years", "incidence per year")

# ---------------------------------------------------------------- C clonal expansion
bio.panel(ax, "C", (19.4, 8.8))
C = charts.axes_at(ax, (21.0, 1.5, 5.6, 6.6))
Ns, nu, mu2 = 1e7, 1e-7, 1e-7
for g, tok in ((0.0, "neutral"), (0.05, "channel"), (0.1, "drug"), (0.15, "negative")):
    if g == 0:
        h = Ns * nu * mu2 * age
        lab = "no expansion (g = 0)"
    else:
        h = Ns * nu * mu2 * (np.exp(g * age) - 1) / g
        lab = f"g = {g:g} per year"
    C.loglog(age, h, color=charts.line(tok), lw=1.6, label=lab)
C.set_xticks([20, 30, 50, 70])
C.set_xticklabels(["20", "30", "50", "70"])
C.xaxis.set_minor_formatter(NullFormatter())
C.set_ylim(1e-7, 1e-1)
C.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(C, "age / years", "incidence per year (two stages)")
