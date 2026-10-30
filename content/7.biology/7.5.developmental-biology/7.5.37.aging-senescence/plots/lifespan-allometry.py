"""Maximum lifespan and body mass in mammals (Formula 37.2.3).

Points: approximate adult body mass and maximum recorded lifespan of 22 mammals, rounded from the AnAge database
of animal aging and longevity (Tacutu and colleagues 2018; naked mole-rat updated to 37 years). The line is a
least-squares fit of log10(lifespan) on log10(mass) for the 18 non-flying, non-burrowing species other than humans
(open circles excluded from the fit): lifespan ~ a M^b with b of about 0.2. Bats, the naked mole-rat and humans
live far longer than their mass predicts; the bowhead whale fits the trend of large mammals.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
data = [  # name, mass / kg, maximum lifespan / years, in fit
    ("mouse", 0.025, 4.0, True), ("rat", 0.35, 3.8, True), ("hamster", 0.12, 3.9, True),
    ("guinea pig", 0.75, 12.0, True), ("rabbit", 1.6, 9.0, True), ("gray squirrel", 0.5, 23.6, True),
    ("cat", 4.0, 30.0, True), ("dog", 20.0, 24.0, True), ("pig", 100.0, 27.0, True), ("sheep", 60.0, 22.8, True),
    ("cattle", 600.0, 20.0, True), ("horse", 400.0, 57.0, True), ("chimpanzee", 45.0, 59.4, True),
    ("rhesus macaque", 8.0, 40.0, True), ("squirrel monkey", 0.8, 30.0, True), ("African elephant", 4000.0, 65.0, True),
    ("giraffe", 800.0, 39.5, True), ("bowhead whale", 80000.0, 211.0, True),
    ("human", 62.0, 122.5, False), ("naked mole-rat", 0.035, 37.0, False), ("little brown bat", 0.008, 34.0, False),
    ("Brandt's bat", 0.007, 41.0, False),
]
m = np.array([d[1] for d in data])
L = np.array([d[2] for d in data])
fit = np.array([d[3] for d in data])
b, la = np.polyfit(np.log10(m[fit]), np.log10(L[fit]), 1)
fig, ax = bio.canvas(22.0, 13.0)
pa = C.axes_at(ax, (2.6, 1.8, 17.5, 10.0))
pa.loglog(m[fit], L[fit], "o", ms=5, color=Q.line_color("protein"))
pa.loglog(m[~fit], L[~fit], "o", ms=5.5, mfc="none", mew=1.4, color=Q.line_color("negative"))
mm = np.logspace(-2.5, 5.2, 50)
pa.loglog(mm, 10 ** la * mm ** b, color=P.muted(), lw=1.0, ls=(0, (4, 2)))
for name, mass, life, _ in data:
    pa.annotate(name, (mass, life), (4, 3), textcoords="offset points", fontsize=FS["tiny"], color=P.ink())
pa.text(0.005, 160, f"fit: lifespan = {10 ** la:.1f} y × (M / kg)^{b:.2f}", fontsize=FS["small"], color=P.ink())
pa.set_xlim(3e-3, 4e5)
pa.set_ylim(2, 400)
C.style_axes(pa, "adult body mass M / kg", "maximum recorded lifespan / years")
