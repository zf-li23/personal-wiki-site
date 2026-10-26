# The two numerical constraints on an RNA world: the error threshold and the need for compartments.
# A: Eigen's error threshold L < ln(sigma)/mu (Eq. 23.1) for sigma = 2, 10, 100, with the fidelity regimes of
#    non-enzymatic copying, polymerase ribozymes and modern DNA replication, and the length a replicase must
#    reach (about 200 nt) shown as a target.
# B: the cross-catalytic ligase pair E / E'. Mass action with a shared substrate pool:
#    dE/dt = k E' S, dE'/dt = k E S, dS/dt = -(dE/dt + dE'/dt), k scaled so that the doubling time is 1 h
#    while substrate is abundant. Right: two such pairs with different k competing for one pool.
# C: stochastic simulation of selection on a better replicase, without and with compartments. Without
#    compartments a copy is made by a randomly chosen catalyst from a randomly chosen template, so the type
#    frequency drifts and the improvement is shared by everyone; with the same molecules binned into protocells
#    that reproduce in proportion to the mean activity of their contents and divide by random partition, the
#    improved replicase sweeps.
import numpy as np
import wikibio as bio
from wikibio import quant as Q

P = bio.P
fig, ax = bio.canvas(25.5, 8.4)


def pw(v):
    k = int(round(np.log10(v)))
    return (v, "1" if k == 0 else f"$10^{{{k}}}$")


# ----------------------------------------------------------------- A: error threshold
bio.panel(ax, "A", (0.1, 8.2))
bio.label(ax, (4.0, 8.2), "Eigen's error threshold", size="small", bold=True)
mu = np.logspace(-11, -0.7, 300)
pl = Q.Plot(ax, (1.9, 1.5, 5.0, 5.6), xlim=(1e-11, 0.2), ylim=(1, 1e12), xlog=True, ylog=True,
            xlabel="error rate per nucleotide $\\mu$", ylabel="maximum genome length $L$ / nt",
            xticks=[pw(v) for v in (1e-10, 1e-7, 1e-4, 1e-1)],
            yticks=[pw(v) for v in (1, 1e3, 1e6, 1e9, 1e12)], ylabel_offset=1.3)
for sigma, tok, at in ((2, "neutral", 0.80), (10, "rna", 0.62), (100, "positive", 0.44)):
    pl.line(mu, np.log(sigma) / mu, tok, text=f"σ = {sigma}", at=at, dy=0.45)
pl.hline(200, token="highlight", text="a replicase ribozyme needs $\\approx 200$ nt", side="left")
for x, yt, text in ((1e-2, 3e7, "non-enzymatic"), (1e-4, 2e9, "polymerase\nribozymes"),
                    (1e-10, 2e9, "DNA replication\n(7.2.7)")):
    pl.vline(x, token="muted", top=False)
    pl.text(x, yt, text, size="tiny", color=P.muted())
bio.label(ax, (4.4, 0.5), "a longer genome needs a fidelity that only a longer genome provides", size="tiny",
          color=P.muted())

# ----------------------------------------------------------------- B: cross-catalytic replication
bio.panel(ax, "B", (8.4, 8.2))
bio.label(ax, (12.1, 8.2), "A self-sustaining ligase pair", size="small", bold=True)


def run(k_list, s0=100.0, e0=0.05, t_end=14.0, n=4000):
    """Mass action for pairs of cross-catalytic ligases sharing one substrate pool."""
    dt = t_end / n
    e = np.array([[e0, e0] for _ in k_list], float)
    s = s0
    t = np.zeros(n + 1)
    out = np.zeros((len(k_list), n + 1))
    out[:, 0] = e.sum(axis=1)
    for i in range(n):
        rate = np.array([k * s * np.array([ee[1], ee[0]]) for k, ee in zip(k_list, e)])
        de = rate * dt
        tot = de.sum()
        if tot > s:                       # substrate runs out
            de *= s / tot
            tot = s
        e += de
        s -= tot
        t[i + 1] = (i + 1) * dt
        out[:, i + 1] = e.sum(axis=1)
    return t, out


k1 = np.log(2.0) / 1.0 / 100.0           # doubling time 1 h at S = 100
t, one = run([k1])
pl = Q.Plot(ax, (10.1, 4.9, 4.3, 2.3), xlim=(0, 14), ylim=(0.05, 300), ylog=True,
            xlabel=None, ylabel="[E] + [E′] / nM", xticks=[0, 4, 8, 12],
            yticks=[pw(v) for v in (0.1, 10)], ylabel_offset=1.0, xlabel_offset=0.45)
pl.line(t, one[0], "positive", lw=1.8)
pl.text(7.6, 0.35, "doubling time $\\approx 1$ h,\nthen the substrates run out", size="tiny", color=P.muted())

t, two = run([k1, 0.55 * k1])
pl = Q.Plot(ax, (10.1, 1.5, 4.3, 2.3), xlim=(0, 14), ylim=(0.05, 300), ylog=True,
            xlabel="$t$ / h", ylabel="two pairs, one pool", xticks=[0, 4, 8, 12],
            yticks=[pw(v) for v in (0.1, 10)], ylabel_offset=1.0)
pl.line(t, two[0], "positive", lw=1.8, text="faster pair", at=0.52, dy=0.4)
pl.line(t, two[1], "negative", lw=1.8, text="slower pair", at=0.75, dy=-0.45)
bio.label(ax, (12.2, 0.5), "competition for substrates is already selection", size="tiny", color=P.muted())

# ----------------------------------------------------------------- C: compartments
bio.panel(ax, "C", (15.9, 8.2))
bio.label(ax, (20.6, 8.2), "Why selection on a replicase needs a compartment", size="small", bold=True)

rng = np.random.default_rng(0)
GEN, CELLS, NPER, ADV = 60, 4000, 5, 1.6     # protocells, molecules per protocell, activity of the mutant


def well_mixed(f0=0.02, pop=CELLS * NPER, gens=GEN, seed=1):
    """Copies are made by a random catalyst from a random template: the type frequency only drifts."""
    r = np.random.default_rng(seed)
    f = f0
    traj = [f]
    for _ in range(gens):
        k = r.binomial(pop, f)               # resampling: the improvement helps every template equally
        f = k / pop
        traj.append(f)
    return np.array(traj)


def compartments(f0=0.02, cells=CELLS, n=NPER, gens=GEN, adv=ADV, seed=2):
    """Molecules binned into protocells; a protocell reproduces in proportion to the mean activity of its
    contents and divides by random partition, so a better replicase is rewarded in its own compartment."""
    r = np.random.default_rng(seed)
    counts = r.binomial(n, f0, size=cells)   # mutant molecules per protocell
    traj = [counts.mean() / n]
    for _ in range(gens):
        activity = (counts * adv + (n - counts)) / n
        p = activity / activity.sum()
        parents = r.choice(cells, size=cells, p=p)
        picked = counts[parents]
        # the contents are duplicated (composition kept, with sampling noise) and split at random
        counts = r.hypergeometric(2 * picked, 2 * (n - picked), n)
        traj.append(counts.mean() / n)
    return np.array(traj)


g = np.arange(GEN + 1)
pl = Q.Plot(ax, (17.9, 1.5, 5.2, 5.6), xlim=(0, GEN), ylim=(0, 1.02),
            xlabel="generation", ylabel="frequency of the mutant",
            xticks=[0, 20, 40, 60], yticks=[0, 0.5, 1], ylabel_offset=0.95)
for seed in (1, 2, 3):
    pl.line(g, well_mixed(seed=seed), "neutral", lw=1.1)
pl.line(g, compartments(), "positive", lw=2.0, text="in protocells", at=0.45, dy=0.5)
pl.text(30, 0.14, "in open solution: drift only", size="tiny", color=P.muted())
bio.label(ax, (20.5, 0.5), "$4000$ protocells of $5$ molecules; the mutant replicates $1.6\\times$ faster",
          size="tiny", color=P.muted())
