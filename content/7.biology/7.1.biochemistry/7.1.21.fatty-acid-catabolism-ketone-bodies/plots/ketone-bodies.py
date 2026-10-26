"""Ketone bodies: formation in liver mitochondria, transport in the blood, use by extrahepatic tissues.

Liver: thiolase condenses two acetyl-CoA to acetoacetyl-CoA; mitochondrial HMG-CoA synthase adds a third
acetyl-CoA to give HMG-CoA; HMG-CoA lyase releases acetoacetate and acetyl-CoA; D-beta-hydroxybutyrate
dehydrogenase reduces acetoacetate with NADH; some acetoacetate decarboxylates spontaneously to acetone,
which is exhaled. Extrahepatic tissues (heart, skeletal muscle, renal cortex, brain in starvation):
D-beta-hydroxybutyrate is oxidized to acetoacetate, succinyl-CoA:3-ketoacid CoA transferase (absent from
liver) activates it to acetoacetyl-CoA, and thiolase cleaves it to two acetyl-CoA for the citric acid cycle.
"""

from matplotlib.patches import FancyBboxPatch

import wikibio as bio
from wikibio import metabolism as M

P = bio.P
fig, ax = bio.canvas(27.0, 15.0, scale=0.4)
for x0, x1, t in ((0.3, 10.8, "Liver mitochondrion"), (16.2, 26.7, "Extrahepatic mitochondrion")):
    ax.add_patch(FancyBboxPatch((x0, 0.3), x1 - x0, 12.0, boxstyle="round,pad=0,rounding_size=0.8",
                                facecolor=P.fill("matrix"), edgecolor=P.edge("mitochondrion"), lw=1.3, zorder=1))
    bio.label(ax, (x0 + 0.4, 11.8), t, size="small", bold=True, ha="left", color=P.edge("mitochondrion"))
ax.add_patch(FancyBboxPatch((11.6, 0.3), 3.8, 14.4, boxstyle="round,pad=0,rounding_size=0.6",
                            facecolor=P.fill("blood"), edgecolor=P.edge("blood"), lw=1.0, alpha=0.25, zorder=0.5))
bio.label(ax, (13.5, 14.2), "Blood", size="small", bold=True, color=P.edge("blood"))
bio.icon(ax, "servier/liver", at=(2.6, 13.6), height=1.8)
bio.icon(ax, "servier/heart", at=(19.0, 13.6), height=1.8)
bio.icon(ax, "servier/brain", at=(21.6, 13.6), height=1.6)
bio.icon(ax, "servier/muscle", at=(24.4, 13.6), height=1.6)

pw = M.Pathway(ax, size="small")
X = 5.2
pw.node("ac2", (X, 10.6), "2 Acetyl-CoA", token="highlight", bold=True)
pw.node("aac", (X, 8.4), "Acetoacetyl-CoA")
pw.node("hmg", (X, 6.0), "HMG-CoA")
pw.node("aa", (X, 3.6), "Acetoacetate", token="lipid", bold=True)
pw.node("bhb", (X, 1.4), "D-β-Hydroxybutyrate", token="lipid", bold=True)
pw.node("acet", (9.3, 5.6), "Acetone")
pw.step("ac2", "aac", enzyme="Thiolase", side=(None, "CoA"), reversible=True, enzyme_offset=0.2)
pw.step("aac", "hmg", enzyme="HMG-CoA\nsynthase", side=("Acetyl-CoA + H₂O", "CoA"), enzyme_offset=0.2, side_span=0.9)
pw.step("hmg", "aa", enzyme="HMG-CoA\nlyase", side=(None, "Acetyl-CoA"), enzyme_offset=0.2)
pw.step("aa", "bhb", enzyme="β-Hydroxybutyrate\nDH", side=("NADH + H⁺", "NAD⁺"), reversible=True, enzyme_offset=0.2)
pw.step(None, "acet", start=pw.anchor("aa", "r") + (0.1, 0.1), side=(None, "CO₂"), bend=0.15)
bio.label(ax, (9.3, 4.4), "spontaneous;\nexhaled", size="tiny", color=P.muted())

Y = 22.2
pw.node("bhb2", (Y, 1.4), "D-β-Hydroxybutyrate", token="lipid", bold=True)
pw.node("aa2", (Y, 3.9), "Acetoacetate", token="lipid", bold=True)
pw.node("aac2", (Y, 6.6), "Acetoacetyl-CoA")
pw.node("acx", (Y, 9.2), "2 Acetyl-CoA", token="highlight", bold=True)
pw.node("tca", (Y, 10.9), "→ citric acid cycle", token="neutral")
pw.step("bhb2", "aa2", enzyme="β-Hydroxybutyrate\nDH", side=("NAD⁺", "NADH + H⁺"), reversible=True,
        enzyme_offset=0.2)
pw.step("aa2", "aac2", enzyme="SCOT (succinyl-CoA:\n3-ketoacid CoA\ntransferase; not in liver)",
        side=("Succinyl-CoA", "Succinate"), enzyme_offset=0.2, side_span=0.9, flip=True)
pw.step("aac2", "acx", enzyme="Thiolase", side=("CoA", None), reversible=True, enzyme_offset=0.2)
pw.step("acx", "tca")

for y in (1.4, 3.6):
    bio.arrow(ax, (X + 2.1 if y < 2 else X + 1.4, y), (Y - 2.1 if y < 2 else Y - 1.4, y + (0 if y < 2 else 0.3)),
              kind="process", color=P.edge("blood"))
bio.label(ax, (13.5, 2.0), "monocarboxylate\ntransporters", size="tiny", color=P.muted())
