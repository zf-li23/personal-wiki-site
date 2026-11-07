"""Hydrostatic pressure along the body: P(h) = P_heart - rho g h, with rho g = 0.77 mmHg per cm of blood
(rho = 1050 kg/m^3; 1 mmHg = 133.3 Pa), h measured upward from the heart (tricuspid valve as reference).

A: a standing adult (head top +50 cm, feet -120 cm), mean arterial pressure 100 mmHg at heart level.
Veins: lying flat about 5 mmHg everywhere; standing still the column is unbroken below the heart (feet ~ +90);
above the heart neck veins collapse near 0 while the rigid dural sinuses go negative (sagittal sinus ~ -10);
walking: the muscle pump and valves break the column, keeping foot venous pressure below ~ +20 mmHg.
B: arterial pressure in a giraffe (head about 1.5 m above, hooves about 1.8 m below the heart when standing upright),
mean pressure about 200 mmHg at the heart, compared with the human. Values are approximate.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
k = 0.77  # mmHg per cm of blood

fig, (ax, bx) = plt.subplots(1, 2, figsize=(11, 5.2))
h = np.linspace(-120, 50, 300)
art = 100 - k * h
ven_still = np.where(h < 0, -k * h, 0.0)
ven_walk = np.where(h < 0, np.minimum(-k * h, 6 + 12 * (-h / 120)), 0.0)
ax.plot(art, h, color=P.edge("blood"), lw=2.2, label="arteries, standing")
ax.plot(np.full_like(h, 98), h, color=P.edge("blood"), lw=1.2, ls=":", label="arteries, lying flat")
ax.plot(ven_still, h, color=P.edge("dna"), lw=2.2, label="veins, standing still")
ax.plot(ven_walk, h, color=P.edge("dna"), lw=1.6, ls="--", label="veins, walking")
ax.plot(np.full_like(h, 5), h, color=P.edge("dna"), lw=1.2, ls=":", label="veins, lying flat")
ax.plot([-10], [40], "o", color=P.edge("dna"), ms=6)
ax.annotate("sagittal sinus\n(rigid): -10", xy=(-10, 40), xytext=(15, 30), fontsize=8,
            arrowprops=dict(arrowstyle="->", color=P.muted()), color=P.muted())
ax.annotate("feet: arteries ~190,\nveins ~90 (still), <20 (walking)", xy=(190, -118), xytext=(95, -95), fontsize=8,
            arrowprops=dict(arrowstyle="->", color=P.muted()), color=P.muted())
ax.axhline(0, color=P.muted(), lw=0.8)
ax.text(160, 3, "heart level", fontsize=8, color=P.muted())
ax.set_xlim(-20, 210)
ax.set_xlabel("Pressure / mmHg")
ax.set_ylabel("Height above the heart / cm")
ax.legend(frameon=False, fontsize=7.5, loc="upper right")
ax.set_title("A  Human: gravity adds rho g h", loc="left", fontsize=10)

hg = np.linspace(-180, 150, 300)
bx.plot(200 - k * hg, hg / 100, color=P.edge("blood"), lw=2.2, label="giraffe, MAP 200 at heart")
hh = np.linspace(-1.2, 0.5, 100)
bx.plot(100 - k * hh * 100, hh, color=P.edge("protein"), lw=2.2, label="human, MAP 100 at heart")
bx.axhline(0, color=P.muted(), lw=0.8)
bx.axvspan(60, 110, color=P.fill("positive"), alpha=0.2, lw=0)
bx.text(85, 1.6, "brain\nperfusion\nrange", ha="center", fontsize=8, color=P.muted())
bx.text(250, -1.75, "hooves: ~340", fontsize=8, color=P.muted())
bx.set_xlim(0, 380)
bx.set_ylim(-1.9, 1.9)
bx.set_xlabel("Mean arterial pressure / mmHg")
bx.set_ylabel("Height above the heart / m")
bx.legend(frameon=False, fontsize=8, loc="upper right")
bx.set_title("B  Giraffe: the price of a long neck (approximate)", loc="left", fontsize=10)
for a in (ax, bx):
    a.grid(True, alpha=0.3)
fig.tight_layout()
