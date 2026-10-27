# Three cell plans side by side (not to scale; the bacterium is drawn about ten times enlarged relative to the
# two eukaryotic cells): a rod-shaped bacterium with nucleoid, ribosomes and flagellum; an animal cell with
# nucleus, ER, Golgi, mitochondria, lysosomes and vesicles; a plant cell with cell wall, central vacuole and
# chloroplasts in addition.
import numpy as np

import wikibio as bio
from wikibio import microbio

P = bio.P
fig, ax = bio.canvas(24, 9.2)

# bacterium
microbio.bacillus(ax, (3.6, 4.6), 4.6, 1.9, gram="-", flagella="monotrichous", flagellum_length=1.8)
rng = np.random.default_rng(2)
t = np.linspace(0, 2 * np.pi, 300)
ax.plot(3.6 + 1.1 * np.cos(t) + 0.12 * np.sin(7 * t), 4.6 + 0.45 * np.sin(t) + 0.1 * np.cos(5 * t),
        color=P.edge("dna"), lw=1.2, zorder=10)
for _ in range(26):
    x, y = rng.uniform(1.8, 5.4), rng.uniform(3.95, 5.25)
    if abs(x - 3.6) < 1.2 and abs(y - 4.6) < 0.5:
        continue
    bio.ribosome(ax, (x, y), size=0.12)
bio.callout(ax, (3.9, 5.0), (4.6, 7.0), "nucleoid (DNA)")
bio.callout(ax, (2.2, 4.4), (1.4, 2.4), "ribosomes")
bio.callout(ax, (5.75, 4.9), (6.4, 6.6), "cell envelope")
bio.label(ax, (3.6, 1.2), "Bacterium (~2 µm)", size="title")

# animal cell
bio.cell(ax, (12, 4.8), 3.6, 3.2, kind="animal", seed=4)
bio.nucleus(ax, (11.4, 5.3), 1.25)
bio.er(ax, (13.2, 6.2), 1.6, 0.9, sheets=3, angle=-20)
bio.golgi(ax, (13.4, 4.2), 1.3, cisternae=4, angle=80)
bio.mitochondrion(ax, (10.0, 3.0), 1.1, 0.45, angle=25)
bio.mitochondrion(ax, (12.4, 2.4), 1.0, 0.42, angle=-15)
bio.lysosome(ax, (14.4, 2.9), 0.28)
bio.vesicle(ax, (9.5, 6.6), 0.18)
bio.callout(ax, (11.0, 6.3), (9.6, 8.7), "nucleus")
bio.callout(ax, (13.5, 6.6), (14.7, 8.6), "endoplasmic reticulum")
bio.callout(ax, (13.4, 3.9), (13.2, 1.15), "Golgi apparatus")
bio.callout(ax, (10.0, 3.0), (8.0, 1.6), "mitochondrion")
bio.callout(ax, (14.4, 2.9), (16.0, 1.9), "lysosome")
bio.callout(ax, (9.45, 7.05), (8.0, 8.1), "plasma membrane")
bio.label(ax, (12, 0.5), "Animal cell (~20 µm)", size="title")

# plant cell
bio.cell(ax, (20.1, 4.8), 3.4, 3.3, kind="plant", seed=3)
bio.nucleus(ax, (18.3, 6.2), 0.75, pores=7)
bio.chloroplast(ax, (21.9, 6.9), 1.1, 0.5, angle=-25)
bio.chloroplast(ax, (17.7, 3.6), 1.0, 0.45, angle=70)
bio.chloroplast(ax, (21.6, 2.4), 1.0, 0.45, angle=20)
bio.mitochondrion(ax, (19.6, 7.4), 0.8, 0.35, angle=5)
bio.callout(ax, (20.3, 4.7), (20.8, 8.9), "central vacuole")
bio.callout(ax, (22.4, 6.7), (23.6, 8.0), "chloroplast")
bio.callout(ax, (23.3, 4.0), (23.6, 1.5), "cell wall")
bio.label(ax, (20.1, 0.5), "Plant cell (~50 µm)", size="title")
