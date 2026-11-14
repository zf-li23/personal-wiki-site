"""Spite by bacteriocins: why it pays most at intermediate frequencies.

Within a patch with a fraction f of producer cells, producers pay a fecundity cost c (they make the toxin, and some
lyse to release it) and are immune; the toxin kills a fraction k f of the sensitive cells, and the resources freed
are shared locally among the survivors. The relative fitnesses are W_P = (1 - c)/W and W_S = (1 - k f)/W with
W = f (1 - c) + (1 - f)(1 - k f), so that the frequency of producers changes by
Delta f = f (1 - f)(k f - c) / W (an illustrative version of Gardner, West and Buckling 2004).
A: Delta f against f for k = 0.5 and two costs: producers decline when rare (too few toxin molecules to kill enough
competitors), spread above f = c/k, and the advantage vanishes when almost everyone is a producer (there is no one
left to harm).
B: trajectories over growth cycles in patches started at different producer frequencies, c = 0.1.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
k = 0.5
fig, ax = bio.canvas(30.0, 10.0)

pa = Ch.axes_at(ax, (2.6, 1.8, 11.0, 7.2))
f = np.linspace(0, 1, 300)
for c, tok in ((0.05, "dna"), (0.1, "rna")):
    W = f * (1 - c) + (1 - f) * (1 - k * f)
    df = f * (1 - f) * (k * f - c) / W
    pa.plot(f, df, color=Ch.line(tok), lw=1.6)
    pa.plot([c / k], [0], "o", ms=4.5, color=Ch.line(tok), mfc=P.surface())
    j = np.argmax(df)
    pa.text(f[j], df[j] + 0.004, f"c = {c:g}", fontsize=FS["tiny"], color=Ch.line(tok), ha="center")
pa.axhline(0, color=P.muted(), lw=0.8)
pa.set_xlim(0, 1)
Ch.style_axes(pa, "frequency of producers in the patch f", "change per cycle, Δf")
bio.panel(ax, "A", (0.3, 9.8))

pb = Ch.axes_at(ax, (18.2, 1.8, 10.8, 7.2))
c = 0.1
for f0, tok in ((0.15, "neutral"), (0.25, "dna"), (0.4, "protein"), (0.6, "rna")):
    fs = [f0]
    for _ in range(40):
        x = fs[-1]
        W = x * (1 - c) + (1 - x) * (1 - k * x)
        fs.append(x + x * (1 - x) * (k * x - c) / W)
    pb.plot(range(41), fs, color=Ch.line(tok), lw=1.5)
    pb.text(0.6, f0 + 0.035, f"f0 = {f0:g}", fontsize=FS["tiny"], color=Ch.line(tok), va="center")
pb.axhline(c / k, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
pb.text(33, c / k + 0.02, "f = c/k", fontsize=FS["tiny"], color=P.muted())
pb.set_xlim(0, 40)
pb.set_ylim(0, 1.02)
Ch.style_axes(pb, "growth cycles", "producer frequency")
bio.panel(ax, "B", (15.8, 9.8))
