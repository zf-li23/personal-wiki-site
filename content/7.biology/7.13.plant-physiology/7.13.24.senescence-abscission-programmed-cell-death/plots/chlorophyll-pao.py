# Chlorophyll breakdown during leaf senescence: the PAO/phyllobilin pathway (simplified).
# In the chloroplast, chlorophyll b is reduced to chlorophyll a (NYC1/NOL, then HCAR); STAY-GREEN (SGR,
# a Mg-dechelatase) removes Mg2+ to give pheophytin a; pheophytinase (PPH) removes phytol to give
# pheophorbide a; pheophorbide a oxygenase (PAO) opens the porphyrin ring (the step that removes the
# green colour and the phototoxicity) to the red chlorophyll catabolite (RCC), which RCC reductase
# (RCCR) reduces to a primary fluorescent chlorophyll catabolite (pFCC). FCCs are exported, modified in
# the cytosol and imported into the vacuole by ABC transporters, where the acidic pH converts them
# non-enzymatically to nonfluorescent catabolites (NCCs). Liberated apoproteins are recycled.
from matplotlib.patches import FancyBboxPatch

import wikibio as bio
from wikibio import metabolism

fig, ax = bio.canvas(20, 8.6)
P = bio.P

for (x0, w, tok, name) in ((0.3, 12.6, "chloroplast", "Chloroplast (gerontoplast)"),
                           (13.2, 3.3, "cytoplasm", "Cytosol"),
                           (16.8, 2.9, "vacuole", "Vacuole")):
    ax.add_patch(FancyBboxPatch((x0, 0.4), w, 7.6, boxstyle="round,pad=0,rounding_size=0.5",
                                facecolor=P.light(tok), edgecolor=P.edge(tok), lw=1.2, zorder=1))
    bio.label(ax, (x0 + 0.3, 7.6), name, size="small", ha="left", color=P.edge(tok))

pw = metabolism.Pathway(ax, size="small")
pw.node("chlb", (2.0, 6.2), "Chlorophyll b")
pw.node("chla", (2.0, 3.9), "Chlorophyll a")
pw.node("phein", (6.2, 3.9), "Pheophytin a")
pw.node("pheide", (10.4, 3.9), "Pheophorbide a")
pw.node("rcc", (7.0, 1.6), "RCC (red)")
pw.node("pfcc", (11.4, 1.6), "pFCC")
pw.node("mfcc", (14.85, 3.9), "modified FCC")
pw.node("ncc", (18.25, 3.9), "NCC")
pw.step("chlb", "chla", enzyme="NYC1/NOL, HCAR", enzyme_flip=True)
pw.step("chla", "phein", enzyme="SGR (Mg-dechelatase)", side=(None, "Mg²⁺"))
pw.step("phein", "pheide", enzyme="PPH", side=(None, "phytol"))
pw.step("pheide", "rcc", enzyme="PAO", side=("O₂", None))
pw.step("rcc", "pfcc", enzyme="RCCR")
pw.step("pfcc", "mfcc", enzyme="export")
pw.step("mfcc", "ncc", enzyme="ABC transporter")
bio.label(ax, (7.6, 6.2), "SGR destabilizes chlorophyll-protein complexes;\napoproteins are released for recycling", size="tiny", color=P.muted())
bio.label(ax, (18.25, 2.9), "acidic pH,\nnonenzymatic", size="tiny", color=P.muted())
bio.label(ax, (9.2, 0.85), "PAO opens the ring: colourless, not phototoxic", size="tiny", color=P.muted())
