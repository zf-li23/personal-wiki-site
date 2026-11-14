# Serial position effects in list memory and their change with the retention interval (illustrative model of
# the pattern found by Wright, Santiago, Sands, Kendrick and Cook 1985 in pigeons, rhesus monkeys and humans).
# A list of four pictures is followed, after a delay, by a probe; the subject reports whether the probe was in
# the list. Accuracy at position i is 0.5 + 0.45 max(R, F), with a recency component
# R = exp(-0.7 (4 - i) - d / tau_R) that decays with the delay d and a primacy component
# F = 0.85 (1 - exp(-d / tau_F)) exp(-0.9 (i - 1)) that grows with it (tau_R = 3 s, tau_F = 2 s, pigeon time
# scale). At short delays only the last items are remembered well (recency); at long delays the first items
# are (primacy); in between the curve is U-shaped. In monkeys and humans the same sequence occurs over longer
# delays.
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(12.0, 9.0)
p = quant.Plot(ax, (2.0, 1.8, 8.2, 6.4), (0.6, 4.6), (0.4, 1.0), xlabel="Serial position in the list",
               ylabel="Proportion correct", xticks=[1, 2, 3, 4], yticks=[0.5, 0.75, 1.0])
p.hline(0.5, text="chance", side="left")
i = np.arange(1, 5)
for d, tok, lab in ((0.0, "rna", "delay 0 s"), (1.5, "protein", "delay 1.5 s"), (10.0, "dna", "delay 10 s")):
    R = np.exp(-0.7 * (4 - i) - d / 3.0)
    F = 0.85 * (1 - np.exp(-d / 2.0)) * np.exp(-0.9 * (i - 1))
    acc = 0.5 + 0.45 * np.maximum(R, F)
    p.line(i, acc, tok, lw=2.0)
    p.points(i, acc, tok, r=0.1)
    p.text(4.55 if d < 5 else 1.1, acc[-1] + 0.02 if d < 5 else acc[0] + 0.03, lab, ha="right" if d < 5 else "left",
           va="bottom", token=tok)
