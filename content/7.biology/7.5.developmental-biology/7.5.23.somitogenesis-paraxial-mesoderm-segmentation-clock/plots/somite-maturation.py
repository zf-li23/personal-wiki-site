"""Maturation of the somite in transverse section (dorsal up): epithelial somite, early sclerotome EMT, mature
compartments with the signals that pattern them."""
import wikibio as bio
from wikibio import mesoderm as M

fig, ax = bio.canvas(28, 9.4)
P = bio.P
W = 8.0
cy = 7.6
titles = ("A  Epithelial somite", "B  Sclerotome forms", "C  Mature somite")
for k, st in enumerate(("epithelial", "early", "mature")):
    cx = 4.4 + k * 9.4
    a = M.somite_section(ax, (cx, cy), W, st)
    bio.label(ax, (cx - W / 2, 8.9), titles[k], bold=True, ha="left")
    if st == "epithelial":
        bio.callout(ax, a["somitocoel"], (cx + 3.4, 8.3), "Somitocoel")
        bio.callout(ax, a["neural"], (cx + 1.0, 8.5), "Neural tube")
        bio.callout(ax, a["notochord"], (cx - 2.6, 3.5), "Notochord")
        bio.callout(ax, a["aorta"], (cx + 0.6, 2.4), "Dorsal aorta")
        bio.callout(ax, a["intermediate"], (cx + 2.6, 2.4), "Intermediate mesoderm")
        bio.callout(ax, a["coelom"], (cx + 3.9, 3.4), "Coelom")
    elif st == "early":
        bio.callout(ax, a["dermomyotome"], (cx + 3.0, 8.4), "Dermomyotome")
        bio.callout(ax, a["sclerotome"], (cx + 1.4, 3.0), "Sclerotome (EMT)")
    else:
        bio.callout(ax, a["dermomyotome"], (cx + 3.3, 8.5), "Dermomyotome")
        bio.callout(ax, a["myotome"], (cx + 4.2, 7.3), "Myotome")
        bio.callout(ax, a["syndetome"], (cx + 4.2, 6.2), "Syndetome")
        bio.callout(ax, a["sclerotome"], (cx + 4.2, 4.9), "Sclerotome")
        # signals (left side)
        nt, nc = a["neural"], a["notochord"]
        sl = a["somite_l"]
        bio.arrow(ax, (nc[0] - 0.3, nc[1] + 0.05), (sl[0] + 0.2, sl[1] - 1.0), kind="activation", color=P.edge("drug"), lw=1.1, bend=-0.15)
        bio.arrow(ax, (cx - 0.45, cy - 0.5), (sl[0] + 0.55, sl[1] + 0.55), kind="activation", color=P.edge("protein"), lw=1.1)
        bio.arrow(ax, (sl[0] - 0.9, cy - 0.25), (sl[0] - 0.2, sl[1] + 0.85), kind="activation", color=P.edge("ectoderm"), lw=1.1)
        lp = a["somatic_l"]
        bio.arrow(ax, (lp[0] + 0.2, lp[1] + 0.3), (sl[0] - 0.85, sl[1] - 0.2), kind="inhibition", color=P.edge("mesoderm"), lw=1.1)

        for j, (tok, kind, txt) in enumerate((("drug", "activation", "Shh, Noggin (notochord, floor plate): sclerotome"),
                                              ("protein", "activation", "Wnt1/3a, NT-3 (dorsal neural tube): myotome, dermis"),
                                              ("ectoderm", "activation", "Wnt6/7a (surface ectoderm): dermomyotome"),
                                              ("mesoderm", "inhibition", "BMP4 (lateral plate): delays lateral myogenesis"))):
            yl = 2.3 - 0.55 * j
            bio.arrow(ax, (cx - 3.9, yl), (cx - 3.1, yl), kind=kind, color=P.edge(tok), lw=1.1)
            bio.label(ax, (cx - 2.9, yl), txt, size="tiny", ha="left")
