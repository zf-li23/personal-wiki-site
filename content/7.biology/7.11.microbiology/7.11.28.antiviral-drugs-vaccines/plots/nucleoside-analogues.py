# How a nucleoside analogue works, and where its selectivity comes from.
# A: the activation pathway of acyclovir - only the infected cell makes the monophosphate.
# B: a competition model. If a polymerase incorporates the analogue triphosphate with efficiency
#    (kcat/Km) a relative to the natural nucleotide, the chance that a given incorporation uses the
#    analogue is  p = a r / (1 + a r)  with r the concentration ratio [analogue-TP]/[dNTP]; the chance
#    that a chain of n = 100 nucleotides is terminated is 1 - (1 - p)^n. A polymerase that
#    discriminates strongly (small a) needs a far higher ratio to be stopped: the window between the
#    two curves is the therapeutic window.
# C: the three modes of action of nucleoside analogues.
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(18.0, 7.8)

# --- A  activation --------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 7.6))
bio.label(ax, (3.9, 7.45), "Activation in the infected cell", size="title", bold=True)


def step(center, w, h, token, text, size="tiny"):
    bio.box(ax, center, w, h, token=token, radius=0.16)
    bio.label(ax, center, text, size=size, color=P.on_fill())


step((1.6, 6.2), 2.4, 0.7, "drug", "acyclovir")
bio.arrow(ax, (1.6, 5.8), (1.6, 5.3), kind="process", color=P.edge("negative"))
bio.label(ax, (2.9, 5.55), "cellular kinases:\nvery poor substrate", size="tiny", color=P.edge("negative"), ha="left")
step((1.6, 4.9), 2.4, 0.7, "neutral", "no reaction")
bio.label(ax, (1.6, 4.3), "uninfected cell", size="tiny", color=P.muted())

step((5.3, 6.2), 2.4, 0.7, "drug", "acyclovir")
bio.arrow(ax, (5.3, 5.8), (5.3, 5.3), kind="process", color=P.edge("positive"))
bio.label(ax, (6.6, 5.55), "viral thymidine\nkinase", size="tiny", color=P.edge("positive"), ha="left")
step((5.3, 4.9), 2.4, 0.7, "metabolite", "ACV monophosphate")
bio.arrow(ax, (5.3, 4.5), (5.3, 4.0), kind="process")
bio.label(ax, (6.6, 4.25), "cellular kinases", size="tiny", color=P.muted(), ha="left")
step((5.3, 3.6), 2.4, 0.7, "metabolite", "ACV triphosphate")
bio.arrow(ax, (5.3, 3.2), (5.3, 2.7), kind="process")
bio.label(ax, (6.6, 2.95), "viral DNA polymerase", size="tiny", color=P.muted(), ha="left")
step((5.3, 2.3), 3.4, 0.8, "virus", "incorporated: no 3′-OH,\nthe chain stops")
bio.label(ax, (5.3, 1.6), "infected cell", size="tiny", color=P.muted())
bio.label(ax, (3.4, 0.85), "selectivity twice over: activation, then incorporation.\n"
                          "Resistance is usually loss of the viral kinase — and such\n"
                          "mutants are themselves less virulent", size="tiny", color=P.muted())

# --- B  competition -------------------------------------------------------------------------------
bio.panel(ax, "B", (7.7, 7.6))
bio.label(ax, (10.8, 7.45), "Why it is selective", size="title", bold=True)

r = np.logspace(-3, 3, 400)
N_CHAIN = 100


def terminated(a):
    p = a * r / (1 + a * r)
    return 1 - (1 - p) ** N_CHAIN


pl = quant.Plot(ax, (8.9, 2.0, 3.9, 4.5), xlim=(-3, 3), ylim=(0, 1.05),
                xlabel="$\\log_{10}$ ([analogue-TP] / [dNTP])", ylabel="chains terminated",
                xticks=[-3, -1, 1, 3], yticks=[0, 0.5, 1])
pl.line(np.log10(r), terminated(1.0), "virus", text="viral polymerase\n($a = 1$)", at=0.12, dy=0.42)
pl.line(np.log10(r), terminated(3e-4), "bacterium", dashed=True,
        text="host polymerase\n($a = 0.0003$)", at=0.78, dy=-0.42)
i_lo = np.argmax(terminated(1.0) > 0.95)
i_hi = np.argmax(terminated(3e-4) > 0.05)
pl.span(np.log10(r[i_lo]), np.log10(r[i_hi]), "positive")
pl.text(np.log10(r[i_hi]) + 0.15, 0.42, "therapeutic\nwindow", size="tiny", ha="left")
bio.label(ax, (10.5, 0.85), "a chain of 100 nucleotides; $a$ is the efficiency of\n"
                            "incorporation relative to the natural nucleotide", size="tiny", color=P.muted())

# --- C  modes -------------------------------------------------------------------------------------
bio.panel(ax, "C", (13.1, 7.6))
bio.label(ax, (15.7, 7.45), "Three modes of action", size="title", bold=True)

MODES = [
    (6.2, "Obligate chain termination", "no 3′-OH: synthesis stops at once", "acyclovir, zidovudine, tenofovir"),
    (4.1, "Delayed termination", "a few more nucleotides are added,\nthen the polymerase stalls",
     "sofosbuvir, remdesivir"),
    (2.0, "Lethal mutagenesis", "the analogue pairs ambiguously and\nraises the error rate past the threshold",
     "ribavirin, molnupiravir"),
]
for y, title, how, examples in MODES:
    bio.box(ax, (15.7, y), 4.6, 1.55, token="drug", radius=0.18)
    bio.label(ax, (15.7, y + 0.52), title, size="small", bold=True, color=P.on_fill())
    bio.label(ax, (15.7, y + 0.02), how, size="tiny", color=P.on_fill())
    bio.label(ax, (15.7, y - 0.5), examples, size="tiny", color=P.on_fill())
bio.label(ax, (15.7, 0.85), "the first two are competitive blocks; the third\n"
                            "works only past the error threshold", size="tiny", color=P.muted())
