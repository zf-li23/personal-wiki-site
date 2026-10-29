"""The double-negative gate that specifies the skeletogenic micromere lineage of the sea urchin. A: the core
network (SBGN activity flow). Nuclear β-catenin with maternal Otx activates pmar1 in the micromeres only;
Pmar1 represses hesC, which is expressed everywhere else and represses the skeletogenic regulators alx1,
ets1, tbr and the signal Delta. Delta from the micromeres activates Notch in the overlying veg2 cells and
specifies non-skeletogenic (secondary) mesoderm through gcm. B: a Boolean version of the gate. Each column is
a gene, each row a cell type or experiment; filled squares are genes on at steady state. Two repressions in
series act as an activation that is confined to cells expressing the first repressor: misexpressing pmar1
everywhere, or knocking down hesC, turns every cell skeletogenic."""
import wikibio as bio
from wikibio import network

P = bio.P
fig, ax = bio.canvas(23, 10.5)
bio.label(ax, (0.4, 10.1), "A  Core network", size="small", bold=True, ha="left")
d = network.Diagram(ax)
nodes = {"bc": ((2.2, 8.6), "β-catenin, Otx", "neutral", False), "pm": ((2.2, 6.6), "pmar1", "protein", True),
         "hc": ((2.2, 4.6), "hesC", "receptor", True), "alx": ((5.6, 2.6), "alx1, ets1, tbr", "enzyme", True),
         "dl": ((9.2, 4.6), "delta", "antibody", True), "sk": ((5.6, 0.8), "skeletogenic genes", "positive", True),
         "gcm": ((9.2, 1.6), "gcm (veg2: SMC)", "channel", True)}
for k, ((x, y), t, tk, it) in nodes.items():
    d.activity(k, (x, y), t, token=tk, italic=it, size="small")
d.connect("bc", "pm", kind="positive")
d.connect("pm", "hc", kind="negative")
d.connect("hc", "alx", kind="negative")
d.connect("hc", "dl", kind="negative")
d.connect("alx", "sk", kind="positive")
d.connect("dl", "gcm", kind="positive")
bio.label(ax, (10.0, 3.2), "Notch in\nneighbours", size="tiny", color=P.muted(), ha="left")

bio.label(ax, (12.4, 10.1), "B  Boolean gate at steady state", size="small", bold=True, ha="left")
genes = ["pmar1", "hesC", "alx1", "delta", "skel."]
cases = [("micromere", True, False), ("macromere, mesomere", False, False), ("pmar1 everywhere", True, False),
         ("hesC knockdown", False, True)]


def state(pmar, kd):
    hes = (not pmar) and (not kd)
    alx = not hes
    return [pmar, hes, alx, not hes, alx]


x0, y0, w, h = 17.2, 8.6, 1.05, 0.9
for j, g in enumerate(genes):
    bio.label(ax, (x0 + j * w, y0 + 0.75), g, size="tiny", italic=j < 4)
for i, (name, pmar, kd) in enumerate(cases):
    y = y0 - i * (h + 0.35)
    bio.label(ax, (x0 - 0.75, y), name, size="tiny", ha="right")
    for j, on in enumerate(state(pmar, kd)):
        tk = "positive" if on else "neutral"
        bio.box(ax, (x0 + j * w, y), w * 0.85, h * 0.85, tk, None, radius=0.08)
        if not on:
            ax.plot([x0 + j * w - 0.25, x0 + j * w + 0.25], [y, y], color=P.muted(), lw=0.8, zorder=12)
bio.label(ax, (17.2, 3.1), "rules:  hesC = NOT pmar1 AND NOT knockdown\n            alx1 = delta = skeletogenic = NOT hesC",
          size="tiny", ha="left", color=P.muted())
