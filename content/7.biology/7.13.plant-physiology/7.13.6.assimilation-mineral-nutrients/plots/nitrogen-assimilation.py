# Nitrate and ammonium assimilation in a leaf mesophyll cell. Nitrate from the xylem enters by H+ symport (NRT)
# and is reduced to nitrite in the cytosol by nitrate reductase (NR, two electrons from NADH). Nitrite enters the
# chloroplast and is reduced to ammonium by nitrite reductase (NiR, six electrons from reduced ferredoxin of the
# light reactions). Ammonium, together with ammonium released by photorespiration, is fixed by glutamine
# synthetase (GS2, ATP) and glutamate synthase (Fd-GOGAT): glutamate + NH4+ -> glutamine; glutamine +
# 2-oxoglutarate -> 2 glutamate. Glutamate donates amino groups by transamination (aminotransferases, e.g.
# Asp-AT to aspartate) and asparagine synthetase (AS) forms asparagine for transport. Approximate costs in ATP
# equivalents per N for each step (after Bloom, as given in Taiz et al. 2015, Fig. 13.20): NRT 1, NR 3, NiR 7,
# GS/GOGAT 2, AS 2. In roots NR uses NAD(P)H and NiR and GOGAT receive electrons from NADPH of the oxidative
# pentose phosphate pathway via ferredoxin.
from matplotlib.patches import Ellipse

import wikibio as bio
from wikibio import metabolism

P = bio.P
fig, ax = bio.canvas(30.0, 12.0)
ax.add_patch(Ellipse((15.4, 6.0), 29.6, 11.4, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("membrane"), lw=2.0, zorder=1))
ax.add_patch(Ellipse((15.0, 6.6), 13.5, 6.2, facecolor=P.fill("chloroplast"), edgecolor=P.edge("chloroplast"), lw=1.6, zorder=2,
                     alpha=0.55))
bio.label(ax, (15.0, 9.3), "Chloroplast", size="small", bold=True, color=P.edge("chloroplast"))
bio.label(ax, (3.2, 10.2), "Mesophyll cell (cytosol)", size="small", bold=True, color=P.muted())

pw = metabolism.Pathway(ax, size="small")
pw.node("no3o", (0.9, 6.0), "NO₃⁻", token="dna")
pw.node("no3", (4.2, 6.0), "NO₃⁻", token="dna")
pw.node("no2", (7.6, 6.0), "NO₂⁻", token="dna2")
pw.node("no2c", (10.6, 6.0), "NO₂⁻", token="dna2")
pw.node("nh4", (13.8, 6.0), "NH₄⁺", token="rna")
pw.node("gln", (16.6, 7.6), "Glutamine", token="metabolite")
pw.node("glu", (19.6, 6.0), "Glutamate", token="metabolite")
pw.node("oxo", (16.6, 4.3), "2-Oxoglutarate", token="metabolite")
pw.node("glu2", (23.2, 6.0), "Glutamate", token="metabolite")
pw.node("asp", (25.8, 4.0), "Aspartate", token="metabolite")
pw.node("asn", (27.0, 7.6), "Asparagine", token="metabolite")
pw.node("pr", (13.8, 3.3), "NH₄⁺ from\nphotorespiration", token="rna", size="tiny")

pw.step("no3o", "no3", enzyme="NRT", side=("H⁺", None))
pw.step("no3", "no2", enzyme="NR", side=("NADH", "NAD⁺"))
pw.step("no2", "no2c", side=("H⁺", None))
pw.step("no2c", "nh4", enzyme="NiR", side=("6 Fd(red)", "6 Fd(ox)"))
pw.step("nh4", "gln", enzyme="GS", side=("ATP", "ADP"), bend=0.12)
pw.step("gln", "glu", enzyme="GOGAT", side=("2 Fd(red)", "2 Fd(ox)"), bend=0.1, flip=True)
pw.step("oxo", "glu", bend=-0.12)
pw.step("pr", "nh4")
pw.step("glu", "glu2")
pw.step("glu2", "asp", enzyme="Asp-AT", enzyme_flip=True)
pw.step("asp", "asn", enzyme="AS", side=("Gln, ATP", "Glu, AMP"), flip=True)
bio.label(ax, (1.0, 6.9), "from xylem", size="tiny", color=P.muted())
bio.label(ax, (23.2, 3.1), "other amino acids,\nproteins, nucleotides", size="tiny", color=P.muted())
bio.arrow(ax, (23.2, 5.55), (23.2, 3.7), kind="process")

# ATP-equivalent costs
costs = [((2.55, 4.6), "1 ATP"), ((5.9, 4.4), "3 ATP"), ((12.2, 4.4), "7 ATP"), ((18.2, 2.6), "2 ATP (GS/GOGAT)"),
         ((28.6, 4.9), "2 ATP")]
for xy, t in costs:
    bio.box(ax, xy, 1.25 if len(t) < 7 else 3.0, 0.48, token="atp", text=t, size="tiny")
bio.label(ax, (15.4, 0.75), "approximate cost: NO₃⁻ → glutamate ≈ 13 ATP equivalents per N", size="small", bold=True)
