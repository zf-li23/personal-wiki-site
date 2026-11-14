# Selective association in conditioned taste aversion (schematic). A: the design and the shape of the result
# of Garcia and Koelling (1966). Rats drank water that was at the same time flavored with saccharin (taste)
# and accompanied by a flash and a click at each lick ("bright-noisy" water). One group was then made ill
# (X-rays or lithium chloride), the other received foot shocks. In the test the two cues were offered
# separately; the bars show the aversion, the reduction of drinking relative to baseline (illustrative
# values). Illness conditioned an aversion to the taste but hardly to the audiovisual cue; shock the reverse.
# B: the range of CS-US intervals over which conditioning occurs depends on the system (schematic curves on a
# logarithmic time axis): eyelid conditioning works best at about half a second and fails beyond a few
# seconds, conditioned fear spans seconds to a minute, and taste aversion is acquired with delays of minutes to several hours.
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(22.0, 9.6)

pa = quant.Plot(ax, (2.0, 1.8, 7.4, 6.4), (0, 5.2), (0, 1.0), xlabel=None, ylabel="Aversion in test",
                xticks=[(1.3, "illness"), (3.9, "shock")], yticks=[0, 0.5, 1])
bio.panel(ax, "A", (0.2, 9.4))
vals = {("illness", "taste"): 0.78, ("illness", "av"): 0.08, ("shock", "taste"): 0.1, ("shock", "av"): 0.66}
for i, us in enumerate(("illness", "shock")):
    x0 = 0.5 + 2.6 * i
    pa.bars([x0, x0 + 0.8], [vals[(us, "taste")]], "rna")
    pa.bars([x0 + 0.8, x0 + 1.6], [vals[(us, "av")]], "dna")
pa.legend([("taste (saccharin)", "rna", "-"), ("bright-noisy water", "dna", "-")], at=(6.6, 7.9))
bio.label(ax, (5.7, 0.75), "Consequence during training", size="small")

pb = quant.Plot(ax, (12.6, 1.8, 8.6, 6.4), (-1, 5.2), (0, 1.05), xlabel="CS-US interval", ylabel="Strength of conditioning",
                xticks=[(-1, "0.1 s"), (0, "1 s"), (1, "10 s"), (np.log10(60), "1 min"), (np.log10(3600), "1 h"),
                        (np.log10(86400), "24 h")], yticks=[0, 0.5, 1])
bio.panel(ax, "B", (10.8, 9.4))
lt = np.linspace(-1, 5.2, 400)


def bump(mu, sd_left, sd_right):
    sd = np.where(lt < mu, sd_left, sd_right)
    return np.exp(-0.5 * ((lt - mu) / sd) ** 2)


pb.line(lt, bump(np.log10(0.4), 0.25, 0.35), "dna", lw=2.0, text="eyelid", at=0.07, dy=0.25, dx=0.45)
pb.line(lt, bump(np.log10(5), 0.5, 0.6), "protein", lw=2.0, text="conditioned fear", at=0.31, dy=0.1, dx=0.15)
pb.line(lt, 0.95 * bump(np.log10(300), 1.6, 1.0), "rna", lw=2.0, text="taste aversion", at=0.66, dy=0.1, dx=0.2)
