"""Forward and reverse genetics as two chains of steps that meet in a gene of known sequence and phenotype.

Forward: phenotype -> mutagenesis / natural variants -> screen -> complementation groups -> mapping ->
gene and causal change, confirmed by rescue. Reverse: gene (sequence, expression, homology) -> targeted
alteration (knockout, CRISPR, RNAi) -> mutant -> phenotype -> inferred function.
"""
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24.0, 8.4)

w, h = 3.25, 1.35
xs = [2.1 + i * 3.95 for i in range(6)]
yf, yr = 6.3, 2.0

fwd = ["Phenotype\nof interest", "Mutagenesis or\nnatural variants", "Screen for\nmutants",
       "Complementation\ngroups = genes", "Map by\nrecombination", "Gene and\ncausal DNA change"]
rev = ["Function of the\nnormal product", "Phenotype", "Mutant\n(loss or gain)", "Targeted change:\nknockout, CRISPR, RNAi",
       "Design a\nperturbation", "Gene known from\nsequence, homology"]
toks_f = ["highlight", "neutral", "neutral", "neutral", "neutral", "dna"]
toks_r = ["highlight", "neutral", "neutral", "neutral", "neutral", "dna"]

bio.label(ax, (0.3, 7.95), "Forward genetics: phenotype → gene", size="title", bold=True, ha="left")
bio.label(ax, (0.3, 0.45), "Reverse genetics: gene → phenotype", size="title", bold=True, ha="left")
for i, (t, k) in enumerate(zip(fwd, toks_f)):
    bio.box(ax, (xs[i], yf), w, h, token=k, text=t, size="small")
    if i:
        bio.arrow(ax, (xs[i - 1] + w / 2 + 0.08, yf), (xs[i] - w / 2 - 0.08, yf), kind="process")
for i, (t, k) in enumerate(zip(rev, toks_r)):
    bio.box(ax, (xs[i], yr), w, h, token=k, text=t, size="small")
    if i:
        bio.arrow(ax, (xs[i] - w / 2 - 0.08, yr), (xs[i - 1] + w / 2 + 0.08, yr), kind="process")

# meeting point: the same gene, and rescue
bio.arrow(ax, (xs[5], yf - h / 2 - 0.1), (xs[5], yr + h / 2 + 0.1), kind="link", dashed=True)
bio.label(ax, (xs[5] + 0.25, (yf + yr) / 2), "same gene:\nsequence and\nmutant phenotype", size="small", ha="left",
          color=P.muted())
bio.arrow(ax, (xs[5] - 0.6, yf + h / 2 + 0.1), (xs[0] + 0.6, yf + h / 2 + 0.1), kind="activation", bend=-0.06,
          dashed=True, color=P.edge("positive"))
bio.label(ax, ((xs[0] + xs[5]) / 2, 8.05), "rescue: a wild-type copy restores the phenotype", size="small",
          color=P.edge("positive"))
bio.label(ax, (xs[2], 3.55), "loss of function: necessary;  gain of function: sufficient", size="small",
          color=P.muted())
