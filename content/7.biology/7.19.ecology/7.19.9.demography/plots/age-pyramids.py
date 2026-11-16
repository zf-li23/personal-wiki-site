"""Age pyramids of model human populations (Section 9.6).

Mortality: Siler-type hazard mu(x) = 0.02 exp(-1.2 x) + 0.0008 + 4e-5 exp(0.095 x) for females,
the senescent term multiplied by 1.4 for males. Births are split 1.05 : 1 (male : female).
A-C: stable age distributions c(x) proportional to exp(-r x) l(x) for r = +0.025, 0 and -0.012 per year
(expanding, stationary and contracting populations).
D: a population that was stable with r = +0.025 and whose fertility then fell, within 10 years, to
a total fertility rate of 1.1 children per woman; projected for 45 years with a female Leslie matrix
(1-year classes, fertility schedule Gaussian with mean 29 and SD 5.5 years). All numbers are
model values, not data for any country.
"""

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
ages = np.arange(0, 100)


def hazard(x, male=False):
    sen = 4e-5 * np.exp(0.095 * x) * (1.4 if male else 1.0)
    return 0.02 * np.exp(-1.2 * x) + 0.0008 + sen


def survival(male=False):
    H = np.concatenate([[0.0], np.cumsum(hazard(ages + 0.5, male))[:-1]])
    return np.exp(-H)


lf, lm = survival(False), survival(True)
pf = 1.05 / 2.05


def to5(v):
    return v.reshape(20, 5).sum(axis=1)


def pyramid(ax, male, female, title):
    tot = male.sum() + female.sum()
    m5, f5 = 100 * to5(male) / tot, 100 * to5(female) / tot
    y = np.arange(20)
    ax.barh(y, -m5, height=0.85, color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.5)
    ax.barh(y, f5, height=0.85, color=P.fill("rna"), edgecolor=P.edge("rna"), lw=0.5)
    ax.set_yticks(y[::2], [f"{5 * i}" for i in y[::2]])
    lim = 7.5
    ax.set_xlim(-lim, lim)
    ax.set_xticks([-6, -3, 0, 3, 6], ["6", "3", "0", "3", "6"])
    ax.axvline(0, color=P.muted(), lw=0.6)
    C.style_axes(ax, "% of population", "age")
    ax.text(-lim * 0.95, 18.6, "male", fontsize=FS["tiny"], color=P.edge("dna"))
    ax.text(lim * 0.95, 18.6, "female", fontsize=FS["tiny"], color=P.edge("rna"), ha="right")
    old = 100 * (male[65:].sum() + female[65:].sum()) / tot
    ax.text(lim * 0.95, 15.6, f"65+: {old:.0f}%", fontsize=FS["tiny"], color=P.ink(), ha="right")
    C.title(ax, title)


fig, axes = plt.subplots(1, 4, figsize=(13.0, 3.9), sharey=True)
for ax, (r, title) in zip(axes[:3], ((0.025, "A  Expanding, r = +0.025"), (0.0, "B  Stationary, r = 0"),
                                      (-0.012, "C  Contracting, r = −0.012"))):
    w = np.exp(-r * ages)
    pyramid(ax, (1 - pf) * w * lm, pf * w * lf, title)

# D: fertility decline, female-only Leslie projection with 1-year classes
fert_shape = np.exp(-0.5 * ((ages - 29) / 5.5) ** 2)
fert_shape /= fert_shape.sum()
s_f = lf[1:] / lf[:-1]
s_m = lm[1:] / lm[:-1]


def daughters_per_year(tfr):
    return tfr * fert_shape * pf  # daughters per woman per year of age


# fertility level giving r = 0.025 initially: solve sum exp(-r x) l(x) m(x) = 1 for TFR
tfr0 = 1.0 / (np.exp(-0.025 * ages) * lf * daughters_per_year(1.0)).sum()
nf = np.exp(-0.025 * ages) * lf
nm = np.exp(-0.025 * ages) * lm * (1 - pf) / pf
for year in range(45):
    tfr = tfr0 + (1.1 - tfr0) * min(year / 10, 1.0)
    births = (nf * tfr * fert_shape).sum()
    nf = np.concatenate([[births * pf], nf[:-1] * s_f])
    nm = np.concatenate([[births * (1 - pf)], nm[:-1] * s_m])
pyramid(axes[3], nm, nf, "D  45 years after fertility fell")
axes[3].text(7.5 * 0.95, 13.6, f"TFR {tfr0:.1f} → 1.1", fontsize=FS["tiny"], color=P.muted(), ha="right")
for ax in axes[1:]:
    ax.set_ylabel("")
fig.tight_layout()
