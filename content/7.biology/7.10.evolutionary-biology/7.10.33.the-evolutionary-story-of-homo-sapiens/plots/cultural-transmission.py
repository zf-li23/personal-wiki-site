"""Genetic and cultural transmission compared (Section 33.7). A: frequency of a variant over 60 years. A
gene with a selective advantage of 5 % per generation (generation time 25 years) spreads by vertical
transmission only; a cultural variant with the same 5 % advantage per transmission event, but copied
horizontally, with every individual re-sampling a model 4 times a year, spreads within years. B:
conformist transmission, in which individuals adopt the more common variant disproportionately often,
dp/dt = c p (1 - p)(2p - 1) (c = 0.5 per year): the rare variant is lost and the common one fixed from
any start above or below 1/2, which keeps groups culturally homogeneous and different from each other."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
years = np.linspace(0, 60, 601)
s, gen = 0.05, 25.0
p0 = 0.01


def logistic(r, t):
    return p0 * np.exp(r * t) / (1 - p0 + p0 * np.exp(r * t))


fig, (a, b) = plt.subplots(1, 2, figsize=(9.8, 3.4))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.87, wspace=0.28)
a.plot(years, logistic(np.log(1 + s) / gen, years), color=charts.line("dna"), lw=2, label="gene (vertical)")
a.plot(years, logistic(4 * np.log(1 + s), years), color=charts.line("rna"), lw=2, label="cultural variant (horizontal)")
charts.style_axes(a, "years", "frequency")
charts.title(a, "A  Speed of spread")
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
c, dt = 0.5, 0.05
tt = np.arange(0, 40, dt)
for start in (0.2, 0.35, 0.45, 0.55, 0.65, 0.8):
    p = start
    traj = []
    for _ in tt:
        traj.append(p)
        p += c * p * (1 - p) * (2 * p - 1) * dt
    b.plot(tt, traj, color=charts.line("plant" if start > 0.5 else "neutral"), lw=1.6)
b.axhline(0.5, color=P.muted(), lw=0.7, ls=":")
charts.style_axes(b, "years", "frequency")
charts.title(b, "B  Conformist transmission")
