"""Why alveoli need surfactant (Formula 30.7.1). A: the Laplace pressure 2 gamma / r needed to keep an alveolus
open against its surface tension, for a water-air interface (gamma = 70 mN/m, constant) and with pulmonary
surfactant, whose film lowers gamma as the surface shrinks (here gamma rises from about 1 mN/m at small radius
towards 25 mN/m as the alveolus expands). Without surfactant the pressure is highest in the smallest alveolus;
with it the pressure rises with radius. B: two alveoli of radii 90 and 110 micrometres connected through a
common airway, total volume fixed; air flows from the alveolus at higher pressure to the other. Without
surfactant the small one empties into the large one (collapse, atelectasis, as in the respiratory distress
syndrome of premature infants); with surfactant both converge to the same size."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
r0 = 100.0  # micrometres


def gamma(r, surf):
    if not surf:
        return 70.0 + 0 * r
    A = (r / r0) ** 2
    return np.minimum(1.0 + 24.0 * A**3, 70.0)


def pressure(r, surf):
    return 2 * gamma(r, surf) * 1e-3 / (r * 1e-6)  # Pa


fig, (a, b) = plt.subplots(1, 2, figsize=(10.2, 3.9))
fig.subplots_adjust(left=0.08, right=0.97, bottom=0.15, top=0.88, wspace=0.28)
r = np.linspace(30, 160, 300)
a.plot(r, pressure(r, False) / 1000, color=charts.line("negative"), lw=1.8, label="no surfactant, 70 mN/m")
a.plot(r, pressure(r, True) / 1000, color=charts.line("enzyme"), lw=1.8, label="with surfactant")
a.set_ylim(0, 3)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="upper right")
charts.style_axes(a, r"alveolar radius / $\mu$m", "Laplace pressure / kPa")
charts.title(a, "A  Pressure to keep an alveolus open")
for surf, tk, txt in ((False, "negative", "no surfactant"), (True, "enzyme", "with surfactant")):
    r1, r2 = 90.0, 110.0
    Vt = r1**3 + r2**3
    ts, R1, R2 = [], [], []
    dt = 0.002
    for k in range(6000):
        dp = pressure(r1, surf) - pressure(r2, surf)
        r1c = r1**3 - 1500.0 * dt * dp
        if r1c <= 15.0**3:
            r1c = 15.0**3
        r1 = r1c ** (1 / 3)
        r2 = (Vt - r1**3) ** (1 / 3)
        ts.append(k * dt)
        R1.append(r1)
        R2.append(r2)
    b.plot(ts, R1, color=charts.line(tk), lw=1.8, label=f"{txt}: small alveolus")
    b.plot(ts, R2, color=charts.line(tk), lw=1.8, ls="--", label=f"{txt}: large alveolus")
b.set_xlim(0, 4)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="center right")
charts.style_axes(b, "time (arbitrary units)", r"radius / $\mu$m")
charts.title(b, "B  Two connected alveoli")
