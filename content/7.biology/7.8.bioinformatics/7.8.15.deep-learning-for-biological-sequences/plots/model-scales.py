# Input length and output resolution of published sequence-to-function models of regulatory DNA (values
# from the original publications). The input is the sequence the model reads for one prediction; the
# output resolution is the length of sequence summarized by one predicted value (for models that predict
# one value per sequence, the full window they label). The dashed diagonal is one prediction per input;
# models far below it predict a profile along their input.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FT = bio.core.FONT
# name, year, input (bp), output resolution (bp)
M = [("DeepBind", 2015, 101, 101), ("DeepSEA", 2015, 1000, 200), ("Basset", 2016, 600, 600),
     ("Basenji", 2018, 131072, 128), ("BPNet", 2021, 1000, 1), ("Enformer", 2021, 196608, 128),
     ("Borzoi", 2025, 524288, 32), ("SpliceAI", 2019, 10001, 1)]
fig, ax = bio.canvas(16.0, 9.5)
a = C.axes_at(ax, (2.0, 1.4, 12.0, 7.4))
xx = np.logspace(1.5, 6.2, 10)
a.plot(xx, xx, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
for name, yr, inp, res in M:
    a.scatter(inp, res, s=28, color=C.line("dna"), zorder=5)
    below = name == "Basenji"
    a.text(inp * (0.85 if below else 1.18), res * (0.55 if below else 1.15), f"{name} ({yr})", fontsize=FT["tiny"],
           color=P.ink(), ha="right" if below else "left")
a.set_xscale("log")
a.set_yscale("log")
a.set_xlim(40, 3e6)
a.set_ylim(0.5, 3000)
C.style_axes(a, "input sequence length (bp)", "output resolution (bp per value)")
