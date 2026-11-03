"""Coalescence time of the two copies of a diploid genome along a chromosome, under the sequentially Markov
coalescent for n = 2. Starting from a coalescence time T (units of 2N0 generations), recombination events
occur along the sequence at rate rho * T per bp, with rho = 4 N0 r = 0.0004 per bp (2 T is the total branch
length, each unit of branch length carrying recombinations at rate rho / 2); at each event a break height u
is uniform on (0, T), and the detached lineage coalesces again above u at rate 1 / nu(t) per unit time, where
nu(t) = N(t) / N0. A: constant size, 5 Mb. B: bottleneck nu = 0.1 between 0.1 and 0.2 time units ago."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rho, Lbp = 0.0004, 5_000_000
grid = np.linspace(0, 30, 300001)
dt = grid[1] - grid[0]


def sim(rel, rng):
    inten = np.concatenate([[0], np.cumsum(1 / rel(grid[:-1]) * dt)])
    inv = lambda w: np.interp(w, inten, grid)
    fwd = lambda t: np.interp(t, grid, inten)
    x, T = 0.0, float(inv(rng.exponential(1.0)))
    xs, Ts = [0.0], [T]
    while x < Lbp:
        x += rng.exponential(1 / (rho * T))
        u = rng.random() * T
        T = float(inv(fwd(u) + rng.exponential(1.0)))
        xs.append(min(x, Lbp))
        Ts.append(T)
    return np.array(xs), np.array(Ts)


fig, axs = plt.subplots(2, 1, figsize=(10.5, 4.6), sharex=True)
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.12, top=0.92, hspace=0.35)
rng = np.random.default_rng(14)
cases = (("A  constant size", lambda t: np.ones_like(t), "dna"),
         ("B  bottleneck between 0.1 and 0.2", lambda t: np.where((t > 0.1) & (t < 0.2), 0.1, 1.0), "rna"))
for ax, (title, rel, tok) in zip(axs, cases):
    xs, Ts = sim(rel, rng)
    ax.step(xs / 1e6, Ts, where="post", color=charts.line(tok), lw=0.8)
    ax.axhline(1, color=P.ink(), lw=0.8, ls="--")
    if "bottleneck" in title:
        ax.axhspan(0.1, 0.2, color=P.mix(P.surface(), P.muted(), 0.25), lw=0)
    ax.set_yscale("log")
    ax.set_ylim(0.01, 8)
    ax.set_xlim(0, Lbp / 1e6)
    charts.style_axes(ax, "position (Mb)" if "B" in title else None, "TMRCA ($2N_0$ gen.)")
    charts.title(ax, title)
