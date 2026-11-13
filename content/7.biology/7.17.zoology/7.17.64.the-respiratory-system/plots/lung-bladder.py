# The air organ of bony fishes on their phylogeny (ventral lungs ancestral, dorsal swim bladder derived), and
# schematic transverse sections of a ventral lung and a dorsal swim bladder. Not to scale.
import numpy as np
import wikibio as bio
from wikibio import phylo
import vertskel as vs

P = bio.P
fig, ax = bio.canvas(26.5, 10.5)
bio.panel(ax, "A", (0.3, 10.1))
nwk = ("((Bichirs,(Sturgeons,(Gars_and_bowfin,Teleosts)Neopterygii)Actinopteri)Actinopterygii,"
       "(Coelacanth,(Lungfishes,Tetrapods)Rhipidistia)Sarcopterygii)Osteichthyes;")
text = {"Bichirs": "Bichirs: paired ventral lungs", "Sturgeons": "Sturgeons, paddlefishes: dorsal swim bladder",
        "Gars and bowfin": "Gars, bowfin: dorsal respiratory gas bladder",
        "Teleosts": "Teleosts: swim bladder (physostomous, physoclistous); lost in many",
        "Coelacanth": "Coelacanth: vestigial lung", "Lungfishes": "Lungfishes: ventral lungs",
        "Tetrapods": "Tetrapods: paired ventral lungs"}
t = phylo.tree(ax, nwk, origin=(0.8, 1.2), width=5.2, height=8.0, tip_text=text, label_size="tiny",
               marks=[dict(node="Osteichthyes", kind="trait", at=0.5, text="ventral lung", token="positive"),
                      dict(node="Actinopteri", kind="trait", at=0.5, text="lung dorsal: swim bladder", token="highlight"),
                      dict(node=["Teleosts"], kind="trait", at=0.5, text="duct closes in many", token="neutral")])

# B: sections
bio.panel(ax, "B", (15.6, 10.1))


def section(cx, cy, dorsal, title):
    bio.label(ax, (cx, cy + 3.3), title, size="small")
    body = vs.oval((cx, cy), 2.0, 2.5)
    bio.shape(ax, body, token="animal", zorder=2)
    # vertebra and gut
    bio.shape(ax, vs.oval((cx, cy + 2.0), 0.35, 0.35), token="bone", zorder=4, lw=0.7)
    gut = (cx, cy - 0.1)
    bio.shape(ax, vs.oval(gut, 0.55, 0.5), token="enzyme", zorder=5, lw=0.7)
    if dorsal:
        bio.shape(ax, vs.oval((cx, cy + 1.15), 1.4, 0.5), token="extracellular", zorder=4, lw=0.9)
        ax.plot([cx, cx], [cy + 0.65, cy + 0.38], color=P.edge("extracellular"), lw=2.4, zorder=6)
        bio.callout(ax, (cx + 0.9, cy + 1.3), (cx + 1.4, cy + 2.75), "swim bladder", size="tiny")
        bio.callout(ax, (cx, cy + 0.5), (cx + 1.0, cy - 2.95), "pneumatic duct (dorsal)", size="tiny")
    else:
        for s in (-1, 1):
            bio.shape(ax, vs.oval((cx + s * 1.1, cy - 1.2), 0.65, 0.75), token="er", zorder=4, lw=0.9)
        ax.plot([cx, cx], [cy - 0.6, cy - 0.95], color=P.edge("er"), lw=2.4, zorder=6)
        bio.callout(ax, (cx + 1.3, cy - 1.4), (cx + 1.5, cy - 2.95), "paired lungs", size="tiny")
        bio.callout(ax, (cx, cy - 0.9), (cx - 2.2, cy - 2.9), "glottis (ventral)", size="tiny")
    bio.callout(ax, gut, (cx - 2.4, cy + 0.2), "gut", size="tiny")
    bio.callout(ax, (cx, cy + 2.0), (cx - 1.9, cy + 3.0), "vertebra", size="tiny")


section(17.4, 5.6, False, "Bichir, lungfish, tetrapod")
section(22.6, 5.6, True, "Teleost")
bio.label(ax, (20.4, 1.0), "both supplied from aortic arch VI in the basal state", size="tiny", color=P.muted())
