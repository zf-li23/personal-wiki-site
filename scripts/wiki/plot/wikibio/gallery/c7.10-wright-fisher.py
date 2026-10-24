# Genetic drift and selection in the Wright-Fisher model (diploid, 2N gene copies, genic selection
# p' = p(1 + s)/(1 + sp), then binomial sampling; seeds 11, 5, 6, 7, 2). A: a genealogy of 12 gene
# copies over 10 generations; every copy picks a random parent in the generation before, and the ancestry
# of the last generation (ink) coalesces to few ancestors. B: 20 trajectories each from p0 = 0.5 for
# N = 20 and N = 200 (drift is faster in small populations), and from p0 = 0.05 with s = 0.03 for N = 200
# (dashed: the deterministic logistic sweep). C: the fixation probability of a single new mutant
# (p = 1/2N, N = 50) estimated from 40 000 replicate populations per s, with 95 % Wilson intervals,
# against Kimura's diffusion formula, the neutral value 1/2N and Haldane's approximation 2s.
import numpy as np

import wikibio as bio
from wikibio import evolution as evo
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(25.0, 12.6)
A0, A1 = "dna", "rna"  # allele colours

# ---- A: genealogy -----------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 12.45))
bio.label(ax, (0.9, 11.95), "Wright–Fisher genealogy", size="normal", bold=True, ha="left")
G = evo.genealogy(ax, (1.3, 1.0), 12, 10, width=6.4, height=10.0, p0=0.5, rng=np.random.default_rng(11))
for g, (yy, f) in enumerate(zip(G["rows"], G["freq"])):
    bio.label(ax, (7.95, yy), f"{f:.2f}", size="tiny", ha="left", color=quant.line_color(A1))
    if g in (0, 9):
        bio.label(ax, (1.05, yy), f"$t = {g}$", size="tiny", ha="right", color=P.muted())
for k, (tk, name) in enumerate(((A0, "allele $a$"), (A1, "allele $A$"))):
    ax.add_patch(bio.core.Circle((1.15 + k * 2.2, 11.35), 0.15, facecolor=P.fill(tk), edgecolor=P.edge(tk), lw=0.8))
    bio.label(ax, (1.4 + k * 2.2, 11.35), name, size="tiny", ha="left")
bio.label(ax, (8.2, 10.9), "$p_A$", size="small", ha="center", color=quant.line_color(A1))
bio.arrow(ax, (0.55, 10.2), (0.55, 2.0), kind="process", head=0.2, color=P.muted(), lw=1.0)
bio.label(ax, (0.3, 6.1), "generations", size="tiny", rotation=90, color=P.muted())

# ---- B: allele-frequency trajectories -------------------------------------------------------------------
T = 200
cases = [(20, 0.0, 0.5, 5, "$N = 20$,  $s = 0$"), (200, 0.0, 0.5, 6, "$N = 200$,  $s = 0$"),
         (200, 0.04, 0.05, 7, "$N = 200$,  $s = 0.04$")]
bio.panel(ax, "B", (9.3, 12.45))
xs = [11.0, 15.6, 20.2]
gen = np.arange(T + 1)
for k, ((N, s, p0, seed, title), x0) in enumerate(zip(cases, xs)):
    traj = evo.wright_fisher(N, s, p0, T, reps=20, rng=np.random.default_rng(seed))
    pl = quant.Plot(ax, (x0, 7.6, 3.9, 3.45), (0, T), (0, 1), xlabel="generation",
                    ylabel="allele frequency $p_A$" if k == 0 else None, xticks=[0, 100, 200],
                    yticks=[0, 0.5, 1] if k == 0 else [(0, ""), (0.5, ""), (1, "")])
    for j in range(traj.shape[1]):
        tr = traj[:, j]
        tok = A1 if tr[-1] == 1 else A0 if tr[-1] == 0 else "muted"
        pl.line(gen, tr, tok, lw=0.9, clip=False)
    if s:
        pl.line(gen, evo.deterministic(s, p0, T), "ink", lw=1.6, dashed=True)
        bio.label(ax, (x0 + 1.95, 6.45), "dashed: deterministic sweep", size="tiny", color=P.muted())
    fix = int((traj[-1] == 1).sum())
    lost = int((traj[-1] == 0).sum())
    bio.label(ax, (x0 + 1.95, 11.75), title, size="small")
    bio.label(ax, (x0 + 1.95, 11.4), f"fixed {fix}, lost {lost}, segregating {20 - fix - lost}", size="tiny",
              color=P.muted())

# ---- C: fixation probability ---------------------------------------------------------------------
N = 50
p_new = 1 / (2 * N)
s_grid = np.array([-0.02, -0.01, -0.005, 0.0, 0.005, 0.01, 0.02, 0.04, 0.06])
rng = np.random.default_rng(2)
sim = np.array([evo.fixation_probability(N, s, p_new, reps=40000, rng=rng) for s in s_grid])
bio.panel(ax, "C", (9.3, 6.1))
pc = quant.Plot(ax, (11.0, 1.1, 6.6, 4.5), (-0.022, 0.065), (1e-4, 0.3), ylog=True, xlabel="selection coefficient $s$",
                ylabel="fixation probability $u$", xticks=[-0.02, 0, 0.02, 0.04, 0.06],
                yticks=[(1e-4, "10⁻⁴"), (1e-3, "10⁻³"), (1e-2, "10⁻²"), (1e-1, "10⁻¹")], grid=True)
ss = np.linspace(-0.022, 0.065, 300)
pc.line(ss, evo.kimura_u(p_new, N, ss), "rna", lw=1.8)
pc.hline(p_new, "muted", text=None)
pc.text(-0.021, p_new * 1.25, "neutral $1/2N$", ha="left", va="bottom", color=P.muted())
s_pos = ss[ss > 0.004]
pc.line(s_pos, 2 * s_pos, "dna", lw=1.2, dashed=True)
pc.text(0.047, 0.125, "$2s$", token="dna", ha="left", size="small")
for (u, lo, hi), s in zip(sim, s_grid):
    if u > 0:
        X = float(pc.X(s))
        ax.plot([X, X], [pc.Y(max(lo, 1.01e-4)), pc.Y(hi)], color=P.ink(), lw=0.9, zorder=pc.z + 2)
        pc.points([s], [u], "ink", r=0.075)
pc.vline(0, "muted")

# explanation beside C
tx = 18.4
bio.label(ax, (tx, 5.25), "Kimura (1962), diffusion limit", size="small", bold=True, ha="left")
bio.label(ax, (tx, 4.45), "$u(p) = \\dfrac{1 - \\mathrm{e}^{-4Nsp}}{1 - \\mathrm{e}^{-4Ns}}$", size="normal", ha="left")
bio.label(ax, (tx, 3.45), f"new mutant: $p = 1/2N$,  $N = {N}$", size="tiny", ha="left", color=P.muted())
bio.label(ax, (tx, 3.00), "dots: 40 000 simulated populations", size="tiny", ha="left", color=P.muted())
bio.label(ax, (tx, 2.55), "bars: 95% Wilson interval", size="tiny", ha="left", color=P.muted())
bio.label(ax, (tx, 1.95), "$|4Ns| \\lesssim 1$: drift dominates", size="tiny", ha="left")
bio.label(ax, (tx, 1.50), "$4Ns \\gg 1$: $u \\approx 2s$ (Haldane)", size="tiny", ha="left")

# colour key of the trajectories (final state)
lx = 11.0
for tk, name in ((A1, "$A$ fixed"), (A0, "$A$ lost"), ("muted", "still segregating")):
    ax.plot([lx, lx + 0.5], [6.45, 6.45], color=quant.line_color(tk), lw=1.6)
    bio.label(ax, (lx + 0.62, 6.45), name, size="tiny", ha="left")
    lx += 0.62 + {"$A$ fixed": 1.35, "$A$ lost": 1.25}.get(name, 2.6)
