# How an integron captures and expresses gene cassettes (SBOL Visual glyphs; a class 1 integron).
# Row 1: the integron platform: the integrase gene intI, the promoter Pc and the recombination site attI,
#   followed by an array of promoterless cassettes (each a coding sequence with its own attC site) and, in
#   class 1 integrons, a 3' conserved segment (qacE-delta1, sul1).
# Row 2: a free circular cassette (dfrA, trimethoprim resistance) is opened and inserted at attI by the
#   integrase, which recombines attI with the cassette's attC site.
# Row 3: the new cassette lies next to Pc and is transcribed most strongly; expression falls along the array
#   (bars). Transcription of intI is repressed by LexA, so the SOS response induced by DNA-damaging
#   antibiotics stimulates capture and reshuffling of cassettes.
import numpy as np
from matplotlib.patches import Rectangle

import wikibio as bio
from wikibio import genetics as G

P = bio.P
fig, ax = bio.canvas(23.0, 11.5)
U = 0.6


def platform(y, cassettes, bars=False):
    parts = [{"kind": "cds", "text": "intI", "token": "enzyme", "reverse": True, "width": 2.2},
             {"kind": "promoter", "text": "Pc"},
             {"kind": "recombination", "text": "attI", "token": "highlight"}]
    for name in cassettes:
        parts += [{"kind": "cds", "text": name, "token": "receptor", "width": 1.9},
                  {"kind": "recombination", "text": "attC", "token": "highlight"}]
    parts += [{"kind": "cds", "text": "qacEΔ1", "token": "neutral", "width": 1.9},
              {"kind": "cds", "text": "sul1", "token": "receptor", "width": 1.5}]
    g = G.construct(ax, 1.0, y, parts, unit=U, gap=0.12)
    if bars:
        ks = [k for k, p in enumerate(parts) if p["kind"] == "cds" and p["text"] in cassettes]
        for rank, k in enumerate(ks):
            h = 0.85 * 0.5 ** rank
            ax.add_patch(Rectangle((g[k]["centre"] - 0.32, y + 0.7), 0.64, h, facecolor=P.fill("positive"),
                                   edgecolor=P.edge("positive"), lw=0.8, zorder=11))
        bio.label(ax, (g[ks[-1]]["x1"] + 1.2, y + 1.15), "transcription from Pc\nweakens along the array",
                  size="tiny", ha="left", color=P.muted())
    return g


bio.label(ax, (1.0, 10.9), "1   Integron platform with two captured cassettes", size="small", bold=True, ha="left")
g1 = platform(9.3, ["aadA", "catB"])

bio.label(ax, (1.0, 7.6), "2   Integrase inserts a free circular cassette at attI", size="small", bold=True, ha="left")
c = (4.2, 5.9)
t = np.linspace(0, 2 * np.pi, 200)
ax.plot(c[0] + 1.0 * np.cos(t), c[1] + 0.75 * np.sin(t), color=P.edge("receptor"), lw=2.4, zorder=10)
bio.label(ax, (c[0], c[1]), "dfrA", size="small", italic=True)
ax.add_patch(bio.core.Circle((c[0], c[1] - 0.75), 0.16, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"),
                             lw=0.9, zorder=12))
bio.label(ax, (c[0], c[1] - 1.15), "attC", size="tiny")
bio.label(ax, (c[0], c[1] + 1.15), "free cassette (no promoter)", size="tiny", color=P.muted())
bio.protein(ax, (8.4, 5.9), 1.5, 0.9, token="enzyme", text="IntI", zorder=12)
bio.label(ax, (8.4, 5.9), "IntI", size="small", color=P.on_fill(), zorder=13)
bio.arrow(ax, (5.5, 5.9), (7.5, 5.9), kind="process")
bio.arrow(ax, (9.4, 5.9), (11.6, 5.9), kind="process")
bio.label(ax, (12.0, 5.9), "attI × attC site-specific recombination", size="small", ha="left")
bio.label(ax, (8.4, 4.9), "intI is repressed by LexA:\nthe SOS response turns capture on", size="tiny", color=P.muted())

bio.label(ax, (1.0, 3.3), "3   The new cassette is first in line", size="small", bold=True, ha="left")
platform(1.6, ["dfrA", "aadA", "catB"], bars=True)
