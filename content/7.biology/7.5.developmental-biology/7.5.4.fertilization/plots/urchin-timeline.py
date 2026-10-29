"""The time course of sea urchin fertilization.

A: membrane potential of the egg (schematic of recordings): about -70 mV before fertilization; within 1-3 s of
sperm binding Na+ influx shifts it to about +20 mV (the fast block to polyspermy), where it stays for about a
minute before slowly returning. The cortical granule reaction (slow block) runs from about 15 s to 60 s.
B: events after insemination on a logarithmic time axis (approximate, after Whitaker and Steinhardt 1985 and
Mohri and colleagues 1995, data from several species at 15-24 C): early responses within the first minute
(fertilization potential, membrane fusion, calcium rise from about 10 s, cortical granule exocytosis), late
responses over minutes to an hour (NAD kinase, rise in pH, sperm entry and pronuclear migration, protein
synthesis, DNA synthesis), and the first cleavage at about 85-95 min.
"""

import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(30, 10.6)

bio.panel(ax, "A", (0.2, 10.4))
pa = quant.Plot(ax, (2.2, 1.7, 8.6, 7.4), xlim=(-10, 120), ylim=(-90, 40), xlabel="time after sperm addition / s",
                ylabel="membrane potential / mV", xticks=[0, 30, 60, 90, 120], yticks=[-80, -40, 0, 40])
t = np.linspace(-10, 120, 600)
V = np.where(t < 0, -70, -70 + 90 * (1 - np.exp(-np.maximum(t, 0) / 0.5)))
V = np.where(t > 60, 20 - 60 * (1 - np.exp(-(t - 60) / 25)), V)
pa.line(t, V, "na")
pa.hline(0, dashed=True)
pa.span(15, 60, "vesicle", text="cortical granule exocytosis", strength=0.6, text_y=9.25)
pa.text(4, 28, "fast block: +20 mV", token="na", ha="left")

bio.panel(ax, "B", (12.0, 10.4))
pb = quant.Plot(ax, (13.8, 1.7, 15.4, 7.4), xlim=(0.5, 8000), ylim=(0, 15), xlog=True, xlabel="time after insemination / s",
                xticks=[(1, "1 s"), (10, "10 s"), (60, "1 min"), (600, "10 min"), (3600, "1 h")], frame="l")
events = [(0.7, 1, "fertilization potential, membrane fusion (< 1 s)", "na"), (10, 10, "Ca²⁺ rise first detected (10 s)", "ca"),
          (15, 60, "cortical granule exocytosis", "vesicle"), (60, 60, "NAD kinase, O₂ consumption rise (1 min)", "enzyme"),
          (60, 120, "sperm entry", "dna"), (60, 300, "acid efflux, pH rise", "h"), (120, 720, "sperm nucleus migrates", "dna"),
          (300, 600, "egg nucleus migrates; protein synthesis starts", "protein"), (1200, 2400, "DNA synthesis begins", "dna2"),
          (3600, 4800, "mitosis", "chromatin"), (5100, 5700, "first cleavage", "positive")]
for k, (a, b, txt, tok) in enumerate(events):
    y = float(pb.Y(14.2 - k * 1.3))
    x0, x1 = float(pb.X(a)), float(pb.X(b))
    if x1 - x0 < 0.15:
        x1 = x0 + 0.15
    bio.box(ax, ((x0 + x1) / 2, y), x1 - x0, 0.42, tok, radius=0.05)
    right = x1 < 21
    bio.label(ax, (x1 + 0.15, y) if right else (x0 - 0.15, y), txt, size="tiny", ha="left" if right else "right")
