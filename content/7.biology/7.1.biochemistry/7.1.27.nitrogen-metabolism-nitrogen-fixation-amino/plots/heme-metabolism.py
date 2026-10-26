"""Heme synthesis (shuttling between mitochondrion and cytosol) and heme degradation to bile pigments.

Synthesis (top). Mitochondrion: delta-aminolevulinate synthase (ALAS, PLP) condenses glycine and succinyl-CoA to
delta-aminolevulinate (ALA), releasing CO2 and CoA; heme inhibits ALAS1 (feedback). Cytosol: ALA dehydratase
(ALAD, Zn; inhibited by lead) joins two ALA to porphobilinogen (PBG); PBG deaminase (hydroxymethylbilane
synthase) links four PBG into hydroxymethylbilane; uroporphyrinogen III synthase closes the ring with
inversion of the last pyrrole (without it, the symmetric uroporphyrinogen I forms); uroporphyrinogen
decarboxylase gives coproporphyrinogen III. Mitochondrion: coproporphyrinogen oxidase, protoporphyrinogen
oxidase and ferrochelatase (inhibited by lead) give heme. Red labels: the main porphyrias (acute
intermittent porphyria, congenital erythropoietic porphyria, porphyria cutanea tarda, erythropoietic
protoporphyria). Degradation (bottom): heme oxygenase opens the ring to biliverdin, releasing Fe2+ and CO;
biliverdin reductase gives bilirubin, carried by albumin to the liver, conjugated by UGT1A1 to bilirubin
diglucuronide and secreted into bile; gut bacteria convert it to urobilinogen, urobilin (urine) and
stercobilin (feces).
"""

from matplotlib.patches import FancyBboxPatch

import wikibio as bio
from wikibio import metabolism as M
from wikibio import photosynthesis as ps

P = bio.P
fig, ax = bio.canvas(28.0, 16.0, scale=0.4)
for (x0, y0, x1, y1), tok, txt in (((0.3, 8.6, 9.4, 15.7), "mitochondrion", "Mitochondrion"),
                                   ((9.8, 8.6, 27.7, 15.7), "cytoplasm", "Cytosol"),
                                   ((0.3, 0.3, 27.7, 8.0), "extracellular", "Degradation: macrophages (spleen), blood, liver, gut")):
    ax.add_patch(FancyBboxPatch((x0, y0), x1 - x0, y1 - y0, boxstyle="round,pad=0,rounding_size=0.6",
                                facecolor=ps.tint(tok, 0.55, 0.82), edgecolor=P.edge(tok), lw=1.3, zorder=1))
    bio.label(ax, (x0 + 0.3, y1 - 0.35), txt, size="small", bold=True, ha="left", color=P.edge(tok))

pw = M.Pathway(ax, size="small")
pw.node("gly", (2.6, 14.0), "Glycine + succinyl-CoA")
pw.node("ala", (2.6, 11.6), "δ-Aminolevulinate", bold=True)
pw.step("gly", "ala", enzyme="ALAS (PLP)\n− CO₂, CoA", enzyme_offset=0.15, flip=True)
pw.node("ala_c", (12.6, 14.0), "2 δ-Aminolevulinate")
pw.node("pbg", (17.6, 14.0), "Porphobilinogen")
pw.node("hmb", (23.6, 14.0), "Hydroxymethylbilane")
pw.node("uro", (23.6, 11.4), "Uroporphyrinogen III")
pw.node("copro", (17.6, 11.4), "Coproporphyrinogen III")
pw.step("ala", "ala_c", color=P.muted(), start=pw.anchor("ala", "r") + (0.05, 0.3))
pw.step("ala_c", "pbg", enzyme="ALAD", side=(None, "2 H₂O"), enzyme_offset=0.15)
pw.step("pbg", "hmb", enzyme="PBG deaminase (×4)", side=(None, "4 NH₄⁺"), enzyme_offset=0.15)
pw.step("hmb", "uro", enzyme="UROS", enzyme_offset=0.15)
pw.step("uro", "copro", enzyme="UROD", side=(None, "4 CO₂"), enzyme_offset=0.15)
pw.node("copro_m", (6.6, 11.6), "Coproporphyrinogen III")
pw.node("proto", (6.6, 9.6), "Protoporphyrin IX")
pw.node("heme", (2.6, 9.6), "Heme", token="negative", bold=True)
pw.step("copro", "copro_m", color=P.muted())
pw.step("copro_m", "proto", enzyme="CPOX, PPOX", enzyme_offset=0.15, flip=True)
pw.step("proto", "heme", enzyme="ferrochelatase\n(+ Fe²⁺)", enzyme_offset=0.15)
for a, b, k in (((1.85, 9.6), (0.75, 9.6), "link"), ((0.75, 9.6), (0.75, 12.8), "link"), ((0.75, 12.8), (2.45, 12.8), "inhibition")):
    bio.arrow(ax, a, b, kind=k, color=P.edge("negative"), lw=1.4)
bio.label(ax, (1.55, 13.15), "heme ⊣ ALAS1", size="tiny", color=P.edge("negative"))
for xy, t, ha in (((20.6, 15.25), "AIP", "center"), ((24.1, 12.7), "CEP", "left"),
                  ((20.6, 12.1), "PCT", "center"), ((4.6, 9.05), "EPP", "center")):
    bio.label(ax, xy, t, size="tiny", bold=True, color=P.edge("negative"), ha=ha)
bio.label(ax, (15.1, 14.75), "lead", size="tiny", color=P.muted())

pd = M.Pathway(ax, size="small")
pd.node("heme2", (2.4, 5.6), "Heme", token="negative", bold=True)
pd.node("bv", (7.6, 5.6), "Biliverdin (green)")
pd.node("br", (13.2, 5.6), "Bilirubin (yellow)")
pd.node("bralb", (13.2, 2.4), "Bilirubin–albumin (blood)")
pd.node("brg", (19.6, 2.4), "Bilirubin diglucuronide")
pd.node("ubg", (19.6, 5.6), "Urobilinogen (gut)")
pd.node("urob", (25.0, 6.8), "Urobilin (urine)", token="highlight")
pd.node("sterc", (25.0, 4.4), "Stercobilin (feces)", token="lipid")
pd.step("heme2", "bv", enzyme="heme oxygenase", side=("O₂, NADPH", "Fe²⁺ + CO"), enzyme_offset=0.15, side_span=1.0)
pd.step("bv", "br", enzyme="biliverdin reductase", side=("NADPH", None), enzyme_offset=0.15)
pd.step("br", "bralb")
pd.step("bralb", "brg", enzyme="liver: UGT1A1", side=("2 UDP-GlcA", None), enzyme_offset=0.15, flip=True)
pd.step("brg", "ubg", enzyme="bile → gut bacteria", enzyme_offset=0.15, enzyme_flip=True)
pd.step("ubg", "urob")
pd.step("ubg", "sterc")
bio.label(ax, (7.6, 2.3), "jaundice when bilirubin\nexceeds liver capacity", size="tiny", color=P.muted())
