"""A-, B- and Z-DNA drawn to scale from their helix parameters (24 base pairs each, side view).
Each backbone is a helix of the given diameter, pitch and handedness projected onto the page; segments
on the near side are drawn solid, those behind lighter. The two strands are offset in phase so that
the grooves between them are unequal (major and minor groove; the offset is schematic). Lines between
the strands are base pairs, tilted by the base-pair tilt of each form. Parameters (fibre and crystal
structures): A: right-handed, 11 bp per turn, rise 0.26 nm, diameter 2.6 nm, tilt 20 deg;
B: right-handed, 10.5 bp per turn, rise 0.34 nm, diameter 2.0 nm, tilt 6 deg; Z: left-handed,
12 bp per turn (6 dinucleotide repeats), rise 0.37 nm, diameter 1.8 nm, tilt 7 deg."""

import numpy as np
import wikibio as bio

P = bio.P
FORMS = [("A-DNA", 11.0, 0.26, 2.6, 20, 1, 0.42), ("B-DNA", 10.5, 0.34, 2.0, 6, 1, 0.38),
         ("Z-DNA", 12.0, 0.37, 1.8, 7, -1, 0.45)]
NBP = 24
S = 1.2  # canvas units per nm

fig, ax = bio.canvas(15.0, 14.0)
for k, (name, bpt, rise, dia, tilt, hand, offset) in enumerate(FORMS):
    x0, y0 = 2.6 + k * 4.9, 2.0
    r = dia / 2 * S
    L = NBP * rise
    z = np.linspace(0, L, 800)
    phase = 2 * np.pi * z / (bpt * rise) * hand
    for strand, tok in ((0, "dna"), (1, "dna2")):
        th = phase + strand * 2 * np.pi * offset
        x, d = x0 + r * np.cos(th), np.sin(th)
        y = y0 + z * S
        for i in range(len(z) - 1):
            front = d[i] < 0  # the viewer looks along +y: points with negative depth are in front
            ax.plot(x[i:i + 2], y[i:i + 2], color=P.edge(tok) if front else P.mix(P.edge(tok), P.surface(), 0.55),
                    lw=3.2 if front else 2.0, zorder=6 if front else 2, solid_capstyle="round")
    for j in range(NBP):
        zz = (j + 0.5) * rise
        ph = 2 * np.pi * zz / (bpt * rise) * hand
        xa, xb = x0 + r * np.cos(ph), x0 + r * np.cos(ph + 2 * np.pi * offset)
        dy = np.tan(np.radians(tilt)) * (xb - xa) / 2
        yc = y0 + zz * S
        ax.plot([xa, xb], [yc - dy, yc + dy], color=P.mix(P.ink(), P.surface(), 0.45), lw=1.0, zorder=4)
    bio.label(ax, (x0, y0 - 0.55), name, size="normal", bold=True)
    bio.label(ax, (x0, y0 + L * S + 0.55), f"{bpt:g} bp/turn, {rise:.2f} nm/bp", size="tiny")
    bio.label(ax, (x0, y0 + L * S + 0.95), "right-handed" if hand > 0 else "left-handed", size="small")
# scale bar: 2 nm
bio.scale_bar(ax, (0.4, 0.75), 2 * S, "2 nm")
