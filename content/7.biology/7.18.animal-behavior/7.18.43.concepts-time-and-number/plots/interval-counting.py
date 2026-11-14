# An interval-counting neuron (model after the auditory midbrain neurons of anurans described by Edwards,
# Alder and Rose 2002). A pulsed advertisement call is a train of sound pulses; the neuron keeps a count of
# consecutive interpulse intervals that fall within its window (here 30-70 ms) and fires one spike for each
# pulse once the count has reached its threshold (here 4 intervals); a single interval outside the window
# resets the count to zero. A: response to a train of 12 pulses at 50-ms intervals: spikes begin only at the
# fifth pulse. B: the same train with one interval lengthened to 120 ms: the count restarts, and spikes
# resume four pulses later. C: response to a train of pulses at 25-ms intervals (too fast): no spikes.
# Such neurons make the response depend on the number of correctly spaced pulses, a basis of female preference
# for longer calls in treefrogs (Gerhardt).
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(22.0, 10.0)
WIN, THRESH = (30, 70), 4


def respond(times):
    count, spikes = 0, []
    for k in range(1, len(times)):
        ipi = times[k] - times[k - 1]
        count = count + 1 if WIN[0] <= ipi <= WIN[1] else 0
        if count >= THRESH:
            spikes.append(times[k] + 6)
    return spikes


trains = [("A: 12 pulses, 50-ms intervals", list(np.arange(12) * 50.0)),
          ("B: one interval of 120 ms", list(np.arange(6) * 50.0) + list(320 + np.arange(7) * 50.0)),
          ("C: pulses too fast (25 ms)", list(np.arange(14) * 25.0))]
p = quant.Plot(ax, (4.2, 1.2, 16.6, 7.8), (-20, 680), (0, 9.4), xlabel="Time / ms", ylabel=None,
               xticks=[0, 200, 400, 600], yticks=[], frame="l")
for i, (name, times) in enumerate(trains):
    y0 = 6.4 - i * 3.0
    bio.label(ax, (0.3, p.Y(y0 + 1.9)), name, size="tiny", ha="left")
    for tt in times:
        x, y = p.xy(tt, y0 + 0.9)
        ax.plot([x, x], [y, y + 0.45], color=quant.line_color("dna"), lw=2.2, solid_capstyle="butt", zorder=8)
    for s in respond(times):
        x, y = p.xy(s, y0)
        ax.plot([x, x], [y, y + 0.55], color=quant.line_color("rna"), lw=1.4, zorder=8)
    bio.label(ax, (3.9, p.Y(y0 + 1.1)), "sound", size="tiny", ha="right", color=quant.line_color("dna"))
    bio.label(ax, (3.9, p.Y(y0 + 0.25)), "spikes", size="tiny", ha="right", color=quant.line_color("rna"))
