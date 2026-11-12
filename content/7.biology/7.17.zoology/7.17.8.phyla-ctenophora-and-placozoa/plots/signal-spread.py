"""Time for a signal to travel a distance x (order-of-magnitude values, log-log). Diffusion of a small
peptide, t = x^2 / (2D) with D = 3e-10 m^2/s, against conduction at constant speed, t = x / v:
contraction waves of cellular sponges (0.04 cm/s, an upper bound), the syncytial impulse of glass sponges
(0.3 cm/s, Leys & Mackie 1997), a cnidarian nerve net (~10 cm/s) and a giant axon (~10 m/s).
The shaded band marks the size range of placozoans (0.02-3 mm).
"""

import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(16.0, 9.6)
x = np.logspace(-6, 0, 300)  # metres
D = 3e-10
pl = quant.Plot(ax, (2.6, 1.6, 11.0, 6.8), xlim=(1e-6, 1.0), ylim=(1e-4, 1e6), xlog=True, ylog=True,
                xlabel="distance x (log scale)", ylabel="time t / s (log scale)",
                xticks=[(1e-6, "1 µm"), (1e-5, "10 µm"), (1e-4, "100 µm"), (1e-3, "1 mm"), (1e-2, "1 cm"),
                        (1e-1, "10 cm"), (1.0, "1 m")],
                yticks=[(1e-3, "1 ms"), (1, "1 s"), (60, "1 min"), (3600, "1 h"), (86400, "1 d")], grid=True,
                ylabel_offset=1.75)
pl.span(2e-5, 3e-3, "highlight", strength=0.7)
pl.text(2.5e-4, 3e5, "placozoan size", color=P.muted())
pl.line(x, x ** 2 / (2 * D), "negative", lw=2.2, text="diffusion of a peptide", at=0.6, dx=-0.25, dy=0.2, ha="right")
speeds = [(4e-4, "sponge contraction wave", "neutral"), (3e-3, "glass-sponge syncytium", "dna"),
          (0.1, "cnidarian nerve net", "rna"), (10.0, "giant axon", "plant")]
for k, (v, name, tok) in enumerate(speeds):
    pl.line(x, x / v, tok, lw=1.6, dashed=k == 0, text=name, at=0.97, dx=0.0, dy=0.3, ha="right")
bio.label(ax, (8.1, 9.2), "Diffusion against conduction", size="small", bold=True)
