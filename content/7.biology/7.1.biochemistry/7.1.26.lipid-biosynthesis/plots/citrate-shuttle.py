"""The citrate shuttle: acetyl groups leave the mitochondrion as citrate, and the shuttle makes NADPH.

Matrix: pyruvate dehydrogenase makes acetyl-CoA and pyruvate carboxylase oxaloacetate; citrate synthase
joins them. Citrate leaves on the citrate transporter of the inner membrane. Cytosol: ATP-citrate lyase
regenerates acetyl-CoA (for acetyl-CoA carboxylase and fatty acid synthase) and oxaloacetate; malate
dehydrogenase reduces oxaloacetate to malate with NADH, and malic enzyme oxidatively decarboxylates malate
to pyruvate, producing NADPH; pyruvate returns on the mitochondrial pyruvate carrier. Per acetyl group the
cycle costs 2 ATP (lyase and pyruvate carboxylase) and converts one cytosolic NADH into NADPH; the pentose
phosphate pathway supplies the rest of the NADPH.
"""

from matplotlib.patches import FancyBboxPatch

import wikibio as bio
from wikibio import metabolism as M
from wikibio import photosynthesis as ps

P = bio.P
fig, ax = bio.canvas(27.0, 14.2, scale=0.42)
ax.add_patch(FancyBboxPatch((0.3, 0.3), 10.2, 13.6, boxstyle="round,pad=0,rounding_size=0.7",
                            facecolor=ps.tint("mitochondrion", 0.5, 0.82), edgecolor=P.edge("mitochondrion"), lw=1.6,
                            zorder=1))
bio.label(ax, (0.7, 13.45), "Mitochondrial matrix", size="small", bold=True, ha="left", color=P.edge("mitochondrion"))
bio.label(ax, (11.5, 13.45), "Cytosol", size="small", bold=True, ha="left", color=P.muted())
for y, t in ((10.6, "citrate\ntransporter"), (3.0, "pyruvate\ncarrier")):
    bio.box(ax, (10.5, y), 0.8, 1.4, "channel")
    bio.label(ax, (10.5, y - 1.05), t, size="tiny", color=P.muted(), va="top")

pw = M.Pathway(ax, size="small")
pw.node("pyr_m", (5.2, 3.0), "Pyruvate")
pw.node("acoa_m", (2.6, 7.2), "Acetyl-CoA", token="highlight")
pw.node("oaa_m", (7.8, 7.2), "Oxaloacetate")
pw.node("cit_m", (5.2, 10.6), "Citrate", bold=True)
pw.step("pyr_m", "acoa_m", enzyme="PDH\n(NAD⁺ → NADH;\n− CO₂)", enzyme_offset=0.2, enzyme_flip=True)
pw.step("pyr_m", "oaa_m", enzyme="pyruvate\ncarboxylase\n(ATP, HCO₃⁻)", enzyme_offset=0.2)
pw.step("acoa_m", "cit_m", side=(None, "CoA"))
pw.step("oaa_m", "cit_m")
bio.label(ax, (5.2, 8.6), "citrate\nsynthase", size="tiny", bold=True, color=P.edge("enzyme"))

pw.node("cit_c", (14.2, 10.6), "Citrate", bold=True)
pw.node("acoa_c", (18.4, 12.4), "Acetyl-CoA", token="highlight", bold=True)
pw.node("oaa_c", (18.4, 8.4), "Oxaloacetate")
pw.node("mal_c", (18.4, 5.4), "Malate")
pw.node("pyr_c", (14.2, 3.0), "Pyruvate")
pw.node("malcoa", (23.6, 12.4), "Malonyl-CoA")
pw.node("fas", (23.6, 9.6), "Fatty acid synthase\n→ palmitate", token="lipid", bold=True, h=1.1)
pw.step("cit_m", "cit_c", color=P.muted())
pw.step("cit_c", "acoa_c", side=("ATP + CoA", "ADP + Pᵢ"), enzyme_offset=0.2)
pw.step("cit_c", "oaa_c")
bio.label(ax, (17.4, 10.75), "ATP-citrate\nlyase", size="tiny", bold=True, color=P.edge("enzyme"), ha="left")
pw.step("acoa_c", "malcoa", enzyme="ACC", side=("ATP + HCO₃⁻", "ADP + Pᵢ"), enzyme_offset=0.2, flip=True)
pw.step("malcoa", "fas", side=("NADPH", "NADP⁺"), enzyme_offset=0.2)
pw.step("oaa_c", "mal_c", enzyme="malate DH", side=("NADH", "NAD⁺"), enzyme_offset=0.2, flip=True)
pw.step("mal_c", "pyr_c", enzyme="malic enzyme", side=("NADP⁺", "NADPH + CO₂"), enzyme_offset=0.2)
pw.step("pyr_c", "pyr_m", color=P.muted())
pw.node("glc", (14.2, 0.95), "from glycolysis", token="neutral")
pw.step("glc", "pyr_c")
bio.box(ax, (23.6, 5.4), 4.4, 1.6, "carbohydrate", text="pentose phosphate\npathway → NADPH", size="tiny")
bio.arrow(ax, (23.6, 6.25), (23.6, 8.95), kind="process", color=P.muted(), dashed=True)
bio.label(ax, (23.6, 2.6), "per acetyl group: 2 ATP;\nNADH (cytosol) → NADPH", size="tiny", color=P.muted())
