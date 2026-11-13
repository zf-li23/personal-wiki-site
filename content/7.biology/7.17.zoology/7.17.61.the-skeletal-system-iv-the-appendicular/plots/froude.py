# Model: dynamic similarity and gait transitions (Alexander 1976, 1989; Alexander & Jayes 1983). A: speed of the
# walk-run transition at Fr = v^2/(g l) = 0.5 and of the trot-gallop transition at Fr = 2.5 against leg (hip)
# length l; the observed human walk-run transition (about 2.0 m/s at l = 0.9 m) is marked. B: maximum walking speed
# at Fr = 1 (inverted-pendulum limit) on the Earth (g = 9.81 m s-2) and on the Moon (g = 1.62 m s-2).
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(24, 9)
l = np.linspace(0.05, 2.0, 200)
p = quant.Plot(ax, (2.0, 1.5, 8.6, 6.4), xlim=(0, 2.0), ylim=(0, 10), xlabel="leg length l / m",
               ylabel="speed / m s-1", xticks=[0, 0.5, 1.0, 1.5, 2.0], yticks=[0, 2, 4, 6, 8, 10])
p.line(l, np.sqrt(0.5 * 9.81 * l), "dna", text="walk-run, Fr = 0.5", at=0.75, dy=-0.6)
p.line(l, np.sqrt(2.5 * 9.81 * l), "mrna", text="trot-gallop, Fr = 2.5", at=0.55, dy=0.6)
p.points([0.9], [2.0], "ink", r=0.1)
p.text(0.95, 1.3, "human, observed", ha="left")
bio.panel(ax, "A", (0.4, 8.6))
q = quant.Plot(ax, (14.0, 1.5, 8.6, 6.4), xlim=(0, 2.0), ylim=(0, 5), xlabel="leg length l / m",
               ylabel="maximum walking speed / m s-1", xticks=[0, 0.5, 1.0, 1.5, 2.0], yticks=[0, 1, 2, 3, 4, 5])
q.line(l, np.sqrt(9.81 * l), "dna", text="Earth, Fr = 1", at=0.7, dy=0.35)
q.line(l, np.sqrt(1.62 * l), "neutral", dashed=True, text="Moon, Fr = 1", at=0.7, dy=0.3)
bio.panel(ax, "B", (12.4, 8.6))
