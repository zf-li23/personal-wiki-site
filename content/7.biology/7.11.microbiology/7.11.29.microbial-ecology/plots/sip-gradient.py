"""Stable isotope probing (DNA-SIP): workflow and why a 12C control is needed (illustrative calculation).

A: a sample is incubated with a 13C-labelled substrate; organisms that assimilate it build 13C into their
DNA. Total DNA is centrifuged to equilibrium in a CsCl gradient (isopycnic ultracentrifugation, about
2 days); "heavy" 13C-DNA bands below "light" 12C-DNA. The gradient is fractionated, the buoyant density
of each fraction measured, and the DNA of each fraction analysed (16S rRNA amplicons, metagenomes).
B: buoyant density of double-stranded DNA in CsCl rises with G + C content, rho = 1.660 + 0.098 GC g/mL,
and full 13C labelling adds about 0.036 g/mL. Curves: distribution of the DNA of three taxa across the
gradient (Gaussian, SD 0.004 g/mL) in the 13C incubation (solid); dashed, the substrate user in a parallel 12C control.
A labelled low-GC taxon (35% GC) moves to the position of an unlabelled high-GC taxon (70% GC); only the
shift relative to the 12C control identifies it as the substrate user.
"""
import numpy as np
from matplotlib.patches import FancyBboxPatch

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(26.0, 11.0)

# A: workflow --------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.3, 10.8))
y = 7.6
steps = [(1.8, "sample +\n¹³C substrate", "metabolite"), (5.0, "incubation:\nactive cells\nmake ¹³C-DNA", "bacterium"),
         (8.2, "extract\ntotal DNA", "dna")]
for x, t, tok in steps:
    bio.box(ax, (x, y), 2.6, 1.9, token=tok, text=t, size="small")
for a, b in [(3.1, 3.7), (6.3, 6.9)]:
    bio.arrow(ax, (a, y), (b, y), kind="process")
bio.arrow(ax, (8.2, y - 1.0), (8.2, y - 2.0), kind="process")
bio.label(ax, (8.5, y - 1.5), "CsCl gradient,\nultracentrifuge", size="tiny", ha="left")
# tube
tx, ty0, ty1, tw = 8.2, 0.9, 5.2, 1.2
ax.add_patch(FancyBboxPatch((tx - tw / 2, ty0), tw, ty1 - ty0,
                                     boxstyle="round,pad=0,rounding_size=0.5", facecolor=P.fill("extracellular"),
                                     edgecolor=P.ink(), lw=1.2, zorder=5))
for yy, tok, txt in [(3.8, "dna", "light ¹²C-DNA"), (2.6, "atp", "heavy ¹³C-DNA")]:
    ax.add_patch(FancyBboxPatch((tx - tw / 2 + 0.08, yy - 0.12), tw - 0.16, 0.24,
                                         boxstyle="round,pad=0,rounding_size=0.1", facecolor=P.fill(tok),
                                         edgecolor=P.edge(tok), lw=0.8, zorder=6))
    bio.callout(ax, (tx - tw / 2 + 0.1, yy), (tx - 2.3, yy), txt, size="tiny")
bio.label(ax, (tx + 0.9, 4.9), "low\ndensity", size="tiny", ha="left", color=P.muted())
bio.label(ax, (tx + 0.9, 1.3), "high\ndensity", size="tiny", ha="left", color=P.muted())
bio.arrow(ax, (tx + 0.8, 2.8), (10.6, 2.8), kind="process")
bio.label(ax, (11.0, 3.4), "fractionate; measure density;\nsequence each fraction", size="tiny", ha="left")

# B: density distributions ------------------------------------------------------------------------
bio.panel(ax, "B", (14.4, 10.8))
rho = np.linspace(1.68, 1.75, 400)


def g(mu, sd=0.004):
    return np.exp(-0.5 * ((rho - mu) / sd) ** 2)


def dens(gc, label13=0.0):
    return 1.660 + 0.098 * gc + 0.036 * label13


pb = quant.Plot(ax, (16.0, 1.5, 9.4, 7.6), xlim=(1.68, 1.75), ylim=(0, 1.25),
                xlabel="buoyant density / (g mL⁻¹)", ylabel="relative amount of DNA",
                xticks=[1.68, 1.70, 1.72, 1.74], yticks=[0, 0.5, 1.0], grid=True)
taxa = [("unlabelled taxon, 35% GC", 0.35, 0.0, "dna", 1.0), ("unlabelled taxon, 70% GC", 0.70, 0.0, "neutral", 0.7),
        ("¹³C substrate user, 35% GC", 0.35, 1.0, "atp", 0.45)]
for name, gc, lab, tok, amp in taxa:
    pb.line(rho, amp * g(dens(gc, lab)), tok, lw=1.9)
pb.line(rho, 0.45 * g(dens(0.35, 0.0)), "atp", lw=1.4, dashed=True)
pb.text(dens(0.35), 1.07, "35% GC", ha="center", va="bottom", token="dna")
pb.text(dens(0.70), 0.77, "70% GC", ha="center", va="bottom", token="neutral")
bio.arrow(ax, pb.xy(dens(0.35) + 0.005, 0.3), pb.xy(dens(0.35, 1.0) - 0.006, 0.3), kind="process",
          color=P.edge("atp"))
pb.text(dens(0.35) + 0.018, 0.34, "+0.036 by ¹³C", ha="center", va="bottom", token="atp")
pb.legend([(n, t, "-") for n, _, _, t, _ in taxa] + [("substrate user in the ¹²C control", "atp", "--")], at=(16.3, 10.2))
