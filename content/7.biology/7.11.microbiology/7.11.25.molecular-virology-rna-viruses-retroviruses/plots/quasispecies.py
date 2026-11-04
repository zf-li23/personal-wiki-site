# The error threshold and the mutation rate of RNA viruses.
# A: the steady state of a two-class mutation-selection model (master sequence of fitness 1 + s, all mutants
#    fitness 1, no back mutation): the master sequence is lost once the genomic error rate mu*L exceeds
#    ln(1 + s). B: per-base error rate against genome size, compiled from published estimates; the product
#    mu*L is near 1 for every class, and coronaviruses sit apart because nsp14 proofreads.
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(17, 7.4)


def master_fraction(muL, s, steps=4000):
    """Steady-state frequency of the error-free master sequence.

    x' = (1 + s) Q x / wbar,  Q = exp(-muL) the probability of error-free copying;
    mutants have fitness 1 and never revert.
    """
    Q = np.exp(-muL)
    x = 0.9
    for _ in range(steps):
        w = (1 + s) * x + (1 - x)
        x = (1 + s) * Q * x / w
        x = max(x, 0.0)
    return x


# --- A  the threshold -------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 7.2))
bio.label(ax, (4.6, 7.0), "Mutation–selection balance", size="title", bold=True)
pl = quant.Plot(ax, (1.6, 2.1, 6.0, 4.1), xlim=(0, 3), ylim=(0, 1.0),
                xlabel="genomic error rate  $\\mu L$", ylabel="master sequence frequency",
                xticks=[0, 1, 2, 3], yticks=[0, 0.5, 1])
muL = np.linspace(0.001, 3, 400)
for s, tok, at, dy in ((0.2, "neutral", 0.02, 0.6), (1.0, "positive", 0.2, 0.25), (4.0, "virus", 0.45, 0.25)):
    y = np.array([master_fraction(m, s) for m in muL])
    pl.line(muL, y, tok, text=f"$s = {s:g}$", at=at, dy=dy)
    pl.vline(np.log(1 + s), token="muted", dashed=True)
pl.span(0.3, 1.2, "highlight")
pl.text(0.75, 0.93, "RNA viruses", size="tiny")
bio.label(ax, (4.6, 0.95), "the threshold is at $\\mu L = \\ln(1+s)$: beyond it no sequence is maintained",
          size="tiny", color=P.muted())
bio.label(ax, (4.6, 0.45), "raising $\\mu$ with a mutagen (ribavirin, molnupiravir) pushes a virus over it",
          size="tiny", color=P.muted())

# --- B  rate against genome size ---------------------------------------------------------------------------
bio.panel(ax, "B", (8.8, 7.2))
bio.label(ax, (13.2, 7.0), "Error rate and genome size", size="title", bold=True)
pl2 = quant.Plot(ax, (10.3, 2.1, 5.9, 4.1), xlim=(3.2, 7.2), ylim=(-9.2, -2.8),
                 xlabel="$\\log_{10}$ (genome size / nt)", ylabel="$\\log_{10}$ (error rate / base)",
                 xticks=[4, 5, 6, 7], yticks=[-9, -7, -5, -3])
g = np.linspace(3.2, 7.2, 50)
pl2.line(g, -g, "muted", dashed=True, text="$\\mu L = 1$", at=0.82, dy=0.3)
data = [("poliovirus", 3.88, -4.0, "virus"), ("influenza A", 4.13, -4.2, "virus"),
        ("HIV-1", 4.0, -4.5, "virus"), ("SARS-CoV-2", 4.48, -6.0, "positive"),
        ("bacteriophage λ", 4.69, -7.2, "dna"), ("herpes simplex 1", 5.18, -7.9, "dna"),
        ("$E.\\ coli$", 6.66, -8.6, "bacterium")]
offsets = {"poliovirus": (-0.08, 0.45), "influenza A": (0.13, 0.33), "HIV-1": (-0.08, -0.5),
           "SARS-CoV-2": (0.1, 0.1), "bacteriophage λ": (0.1, 0.35), "herpes simplex 1": (0.08, -0.45),
           "$E.\\ coli$": (-0.1, 0.45)}
for name, x, yv, tok in data:
    pl2.points([x], [yv], tok, r=0.1)
    dx, dy = offsets[name]
    pl2.text(x + dx, yv + dy, name, size="tiny", token=tok)
bio.label(ax, (13.2, 0.95), "RNA genomes cluster at one mutation per genome per copy;",
          size="tiny", color=P.muted())
bio.label(ax, (13.2, 0.45), "the proofreading exonuclease of coronaviruses buys them a larger genome",
          size="tiny", color=P.muted())
