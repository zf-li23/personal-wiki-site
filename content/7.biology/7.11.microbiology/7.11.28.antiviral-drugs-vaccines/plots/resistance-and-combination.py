# Why monotherapy fails and combination therapy works.
# A: expected number of genomes already carrying all k resistance substitutions, N * mu^k, for a
#    population of N = 1e10 replicating genomes per day and per-site mutation frequencies 1e-4 to 1e-5.
# B: a deterministic two-population model of viral load under treatment. The wild type is suppressed
#    by a factor (1 - eps) per drug; a resistant variant, present at frequency f0 and with a fitness
#    cost, is suppressed less. Monotherapy leaves the resistant variant growing; three drugs leave
#    nothing growing unless adherence lapses, modelled here as a 7-day interruption.
# C: the residual replication left by a regimen against the time until resistance dominates.
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(17.6, 7.4)

# --- A  pre-existing mutants ------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 7.2))
bio.label(ax, (3.4, 7.05), "Do the mutants pre-exist?", size="title", bold=True)

N_GENOMES = 1e10
k = np.arange(1, 6)
pl = quant.Plot(ax, (1.5, 1.9, 4.2, 4.4), xlim=(0.5, 5.5), ylim=(-16, 11),
                xlabel="substitutions needed for resistance", ylabel="$\\log_{10}$ (such genomes)",
                xticks=[1, 2, 3, 4, 5], yticks=[-15, -10, -5, 0, 5, 10])
for mu, tok, name in ((1e-4, "virus", "$\\mu = 10^{-4}$"), (1e-5, "bacterium", "$\\mu = 10^{-5}$")):
    y = np.log10(N_GENOMES * mu ** k)
    pl.line(k, y, tok, text=name, at=0.55, dy=0.30)
    pl.points(k, y, tok, r=0.07)
pl.hline(0.0, token="negative", dashed=True, text="one genome")
pl.span(0.5, 2.5, "negative", strength=0.35)
pl.span(3.5, 5.5, "positive", strength=0.35)
pl.text(1.5, 9.0, "present before therapy", size="tiny")
pl.text(4.5, 9.0, "absent", size="tiny")
bio.label(ax, (3.4, 0.8), "$10^{10}$ genomes replicated per day (untreated HIV-1)",
          size="tiny", color=P.muted())

# --- B  viral load under therapy --------------------------------------------------------------------
bio.panel(ax, "B", (6.3, 7.2))
bio.label(ax, (9.7, 7.05), "Load under treatment", size="title", bold=True)

T = np.linspace(0, 365, 1500)
R_WT, COST = 0.80, 0.25          # net growth rate per day of wild type; fitness cost of resistance
EPS = 0.85                       # suppression by one drug
V_SET, F0 = 1e5, 1e-4            # set-point load, frequency of the resistant variant


def load(n_drugs, interruption=None):
    """Two subpopulations; each drug suppresses the wild type by (1 - EPS) and the resistant
    variant by (1 - EPS) for every drug except the one it is resistant to."""
    v_wt = np.empty_like(T)
    v_r = np.empty_like(T)
    wt, res = V_SET * (1 - F0), V_SET * F0
    dt = T[1] - T[0]
    for i, t in enumerate(T):
        on = True if interruption is None else not (interruption[0] <= t <= interruption[1])
        e_wt = (1 - EPS) ** n_drugs if on else 1.0
        e_r = (1 - EPS) ** (n_drugs - 1) if on else 1.0          # resistant to one of the drugs
        g_wt = R_WT * e_wt - 0.4
        g_r = R_WT * (1 - COST) * e_r - 0.4
        wt = min(max(wt * np.exp(g_wt * dt), 1.0), 1e6)
        res = min(max(res * np.exp(g_r * dt), 1.0), 1e6)
        v_wt[i], v_r[i] = wt, res
    return v_wt + v_r, v_r


pl2 = quant.Plot(ax, (7.6, 1.9, 4.3, 4.4), xlim=(0, 365), ylim=(-0.3, 6.3),
                 xlabel="days of treatment", ylabel="$\\log_{10}$ (plasma virus ml$^{-1}$)",
                 xticks=[0, 120, 240, 365], yticks=[0, 2, 4, 6])
mono, mono_r = load(1)
triple, _ = load(3)
lapse, _ = load(3, interruption=(150, 157))
pl2.line(T, np.log10(mono), "negative", text="one drug", at=0.30, dy=0.34)
pl2.line(T, np.log10(mono_r), "negative", dotted=True, text="its resistant variant", at=0.52, dy=-0.45)
pl2.line(T, np.log10(triple), "virus", text="three drugs", at=0.84, dy=0.32)
pl2.line(T, np.log10(lapse), "highlight", dashed=True, text="three drugs,\n7 days missed", at=0.40, dy=0.95)
pl2.hline(1.6, token="muted", dashed=True, text="limit of detection")
bio.label(ax, (9.7, 0.8), "a lapse restores replication, and replication makes mutants",
          size="tiny", color=P.muted())

# --- C  residual replication -------------------------------------------------------------------------
bio.panel(ax, "C", (12.4, 7.2))
bio.label(ax, (15.3, 7.05), "Residual replication", size="title", bold=True)

eps = np.linspace(0.0, 0.999, 400)
mutants_per_day = N_GENOMES * (1 - eps) * 3e-5
pl3 = quant.Plot(ax, (13.6, 1.9, 3.4, 4.4), xlim=(0, 1), ylim=(0, 7),
                 xlabel="fraction of replication blocked", ylabel="$\\log_{10}$ (new mutants per day)",
                 xticks=[0, 0.5, 1], yticks=[0, 2, 4, 6])
pl3.line(eps, np.log10(np.maximum(mutants_per_day, 1e-3)), "virus")
pl3.hline(0.0, token="negative", dashed=True, text="one per day", side="left")
pl3.span(0.999, 1.0, "positive")
bio.label(ax, (15.3, 0.8), "each mutation arises only when a genome is copied:\n"
                           "complete suppression creates no resistance at all",
          size="tiny", color=P.muted())
