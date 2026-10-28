"""The Sevenless pathway as an activity-flow diagram, with the positions of dominant enhancers and
suppressors recovered in a modifier screen in a sensitized (hypomorphic sev) background."""
import wikibio as bio
from wikibio import network as N

P = bio.P
fig, ax = bio.canvas(16.4, 9.4)
d = N.Diagram(ax)

d.activity("boss", (2.8, 7.9), "Boss", token="receptor")
d.activity("sev", (2.8, 6.2), "Sevenless", token="channel")
d.activity("drk", (2.8, 4.7), "Drk", token="protein")
d.activity("sos", (2.8, 3.3), "Sos", token="positive")
d.activity("ras", (2.8, 1.9), "Ras", token="positive")
d.activity("gap", (6.6, 1.9), "Ras GAP", token="negative")
d.activity("casc", (2.8, 0.6), "Kinase cascade", token="enzyme")

for a, b in (("boss", "sev"), ("sev", "drk"), ("drk", "sos"), ("sos", "ras"), ("ras", "casc")):
    d.connect(a, b, "positive")
d.connect("gap", "ras", "negative")

bio.label(ax, (0.6, 8.6), "R8 cell", size="small", color=P.muted(), ha="left")
bio.label(ax, (0.6, 7.0), "R7 precursor", size="small", color=P.muted(), ha="left")
bio.label(ax, (5.9, 7.9), "ligand on the neighbouring cell", size="tiny", color=P.muted())
bio.label(ax, (2.8, -0.25), "transcription factors, R7 fate", size="small")

bio.label(ax, (8.9, 8.9), "In a hypomorphic $sev$ background", size="title", ha="left", bold=True)
bio.label(ax, (8.9, 8.2), "R7 is recruited in only some ommatidia", size="small", ha="left", color=P.muted())
rows = [("Half dose of a positive component", "all ommatidia lack R7", "dominant enhancer", "positive"),
        ("Half dose of a negative component", "every ommatidium has R7", "dominant suppressor", "negative")]
for k, (cause, effect, name, tok) in enumerate(rows):
    y = 6.4 - k * 3.1
    bio.box(ax, (11.6, y), 5.0, 0.8, token=tok, text=cause, size="small")
    bio.arrow(ax, (11.6, y - 0.45), (11.6, y - 1.05), kind="process")
    bio.label(ax, (11.6, y - 1.35), effect, size="small")
    bio.label(ax, (11.6, y - 1.8), name, size="small", bold=True, color=P.edge(tok))
bio.label(ax, (11.6, 0.8), "In a wild-type background these\nheterozygotes have no phenotype", size="small",
          color=P.muted())
