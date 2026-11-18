"""The insurance hypothesis in a model community (after Yachi and Loreau 1999).

Environment: E_t is an autoregressive process E_t = 0.9 E_{t-1} + 0.436 xi_t (xi standard normal; stationary
sd 1), one step per year, 600 years (the first 100 discarded). Species: S species drawn from a pool whose
environmental optima u_i are uniform on [-2.5, 2.5]; each has the same maximal growth rate, and per-capita
growth depends on how close the current environment is to its optimum:
    N_i,t+1 = N_i,t exp(1.2 exp(-(E_t - u_i)^2 / (2 x 0.7^2)) - 0.4 - 0.8 B_t) + 0.01,
with B_t = sum_j N_i,t the total biomass (diffuse competition) and a small immigration term from the regional
pool. Ecosystem function is total biomass B_t.
A: total biomass over 200 years for one community of 1 species and one of 8 species, with the environment.
B: temporal mean of B (temporal means of 60 random communities for each S, bands: central 80 %).
C: coefficient of variation of B over time. More species raise the mean (performance-enhancing effect:
some species suit each environment) and lower the variability (buffering effect: species replace one
another as conditions change), the two components of the insurance effect.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(13)
T, burn = 600, 100


def environment():
    E = np.zeros(T)
    for t in range(1, T):
        E[t] = 0.9 * E[t - 1] + 0.436 * rng.standard_normal()
    return E


def community(u, E):
    N = np.full(u.size, 0.1)
    B = np.zeros(T)
    for t in range(T):
        B[t] = N.sum()
        g = 1.2 * np.exp(-(E[t] - u) ** 2 / (2 * 0.7 ** 2)) - 0.4 - 0.8 * B[t]
        N = N * np.exp(g) + 0.01
    return B[burn:]


Ss = [1, 2, 4, 8, 16]
stats = {S: [] for S in Ss}
for S in Ss:
    for _ in range(60):
        E = environment()
        B = community(rng.uniform(-2.5, 2.5, S), E)
        stats[S].append((B.mean(), B.std() / B.mean()))
    stats[S] = np.array(stats[S])

fig, ax = bio.canvas(32.0, 11.0)
E = environment()
pa = C.axes_at(ax, (2.2, 1.6, 12.6, 7.4))
tt = np.arange(T - burn)
for S, tok in ((1, "negative"), (8, "dna")):
    u = np.linspace(-2.0, 2.0, S) if S > 1 else np.array([0.0])
    B = community(u, E)
    pa.plot(tt[:200], B[:200], color=Q.line_color(tok), lw=1.3, label=f"{S} species")
pa2 = pa.twinx()
pa2.plot(tt[:200], E[burn:burn + 200], color=P.muted(), lw=0.8, alpha=0.7)
pa2.set_ylim(-6, 3)
C.style_axes(pa2, None, "environment E (grey)")
pa2.spines["right"].set_visible(True)
pa.set_ylim(0, 1.6)
C.style_axes(pa, "year", "total biomass B")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "A", (0.5, 10.6))
bio.label(ax, (2.2, 10.2), "Species replace one another as conditions change", size="small", bold=True, ha="left")

for k, (x0, lab, title, panel) in enumerate(((19.2, "mean total biomass", "Higher mean", "B"), (26.4, "CV of total biomass", "Lower variability", "C"))):
    pb = C.axes_at(ax, (x0, 1.6, 5.4, 7.4))
    m = np.array([np.median(stats[S][:, k]) for S in Ss])
    lo = np.array([np.quantile(stats[S][:, k], 0.1) for S in Ss])
    hi = np.array([np.quantile(stats[S][:, k], 0.9) for S in Ss])
    tok = "plant" if k == 0 else "enzyme"
    pb.fill_between(Ss, lo, hi, color=P.light(tok), lw=0, alpha=0.7)
    pb.plot(Ss, m, "o-", color=Q.line_color(tok), lw=1.5, ms=4)
    pb.set_xscale("log", base=2)
    pb.set_xticks(Ss)
    pb.set_xticklabels([str(S) for S in Ss])
    pb.set_ylim(bottom=0)
    C.style_axes(pb, "species richness S", lab)
    bio.panel(ax, panel, (x0 - 1.7, 10.6))
    bio.label(ax, (x0, 10.2), title, size="small", bold=True, ha="left")
