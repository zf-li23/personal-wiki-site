# ABA and strigolactone biosynthesis from carotenoids (simplified).
# Plastid: beta-carotene -> zeaxanthin -> (ZEP) antheraxanthin -> violaxanthin -> 9'-cis-neoxanthin
# -> (NCED, rate-limiting) xanthoxin; cytosol: ABA2 -> abscisic aldehyde -> AAO3 -> ABA.
# Inactivation: CYP707A (8'-OH-ABA -> PA -> DPA); UGT -> ABA-GE, released again by BG1/BG2.
# Strigolactone branch: D27, CCD7, CCD8 -> carlactone -> MAX1 -> strigolactones.
import wikibio as bio
from matplotlib.patches import FancyBboxPatch
from wikibio import metabolism as M

fig, ax = bio.canvas(22, 12.5)
P = bio.P
for (x, w, tok, name) in ((0.3, 21.4, "chloroplast", "Plastid"),):
    fc = P.mix(P.edge(tok), P.surface(), 0.8) if P.is_dark() else P.light(tok)
    ax.add_patch(FancyBboxPatch((0.3, 6.3), 21.4, 6.0, boxstyle="round,pad=0,rounding_size=0.4", facecolor=fc,
                                edgecolor=P.edge(tok), lw=1.1, zorder=1))
bio.label(ax, (0.7, 11.9), "Plastid", size="small", bold=True, ha="left")
bio.label(ax, (0.7, 5.8), "Cytosol", size="small", bold=True, ha="left", color=P.muted())

pw = M.Pathway(ax, size="small")
pw.node("bc", (4.0, 10.9), "all-trans-β-Carotene (C40)", bold=True)
pw.node("zea", (11.0, 10.9), "Zeaxanthin")
pw.node("vio", (16.5, 10.9), "all-trans-Violaxanthin")
pw.node("neo", (16.5, 8.6), "9′-cis-Neoxanthin")
pw.node("xan", (16.5, 6.9), "Xanthoxin (C15)")
pw.node("ald", (16.5, 4.7), "Abscisic aldehyde")
pw.node("aba", (16.5, 2.6), "ABA", bold=True, token="positive")
pw.node("pa", (12.0, 2.6), "8′-OH-ABA → PA → DPA", token="neutral")
pw.node("ge", (20.3, 0.9), "ABA-GE", token="neutral")
pw.node("bc9", (4.0, 8.9), "9-cis-β-Carotene")
pw.node("cl", (4.0, 6.9), "Carlactone")
pw.node("sl", (4.0, 3.6), "Strigolactones", bold=True, token="positive")

pw.step("bc", "zea", enzyme="β-carotene hydroxylase", enzyme_size="tiny")
pw.step("zea", "vio", enzyme="ZEP (via antheraxanthin)", enzyme_size="tiny")
pw.step("vio", "neo", enzyme="NSY / isomerase", enzyme_size="tiny", enzyme_flip=True)
pw.step("neo", "xan", enzyme="NCED (rate-limiting)", enzyme_size="tiny", enzyme_flip=True)
pw.step("xan", "ald", enzyme="ABA2 (SDR)", enzyme_size="tiny", enzyme_flip=True)
pw.step("ald", "aba", enzyme="AAO3 (MoCo)", enzyme_size="tiny", enzyme_flip=True)
pw.step("aba", "pa", enzyme="CYP707A", enzyme_size="tiny")
pw.step("aba", "ge", reversible=True, enzyme="UGT / BG1, BG2", enzyme_size="tiny", enzyme_flip=True)
pw.step("bc", "bc9", enzyme="D27", enzyme_size="tiny")
pw.step("bc9", "cl", enzyme="CCD7, CCD8", enzyme_size="tiny")
pw.step("cl", "sl", enzyme="MAX1 (P450) and others", enzyme_size="tiny", enzyme_flip=True)
bio.label(ax, (19.6, 8.0), "induced by drought", size="tiny", color=P.edge("negative"))
bio.label(ax, (12.0, 1.9), "inactive", size="tiny", color=P.muted())
