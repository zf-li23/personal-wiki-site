# Kinetic proofreading (Hopfield 1974, Ninio 1975).
# A: the scheme with one proofreading stage. Substrate X (correct C or wrong D, equal concentrations) binds the
#    enzyme reversibly (k_on, k_off,X); an energy-consuming, irreversible step (rate m, e.g. GTP hydrolysis by
#    EF-Tu) converts the complex into a second state from which X can still leave (l_X) or be used (W).
#    Both dissociation constants differ by the same factor exp(ddG/kT) between C and D.
# B: error ratio f against the discrimination energy ddG for 0, 1 and 2 proofreading stages, with
#    m/k_off,C = 0.05 and W/l_C = 0.05 (curves, Eq. 19.2) and the ideal limits exp(-(n+1) ddG/kT) (dashed);
#    points: stochastic simulation of single binding events for n = 1 (embedded Markov chain, 10^5 products).
# C: the price of accuracy for one stage at ddG = 4.6 kT (single-step error 0.01): as the commitment rate W is
#    lowered relative to the rejection rate l_C, the error falls towards 1e-4, but the number of irreversible
#    steps (GTP) spent per correct product and the time per product rise.
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P


def error(dg, n, a=0.05, b=0.05):
    """Error ratio with n proofreading stages; a = m/k_off,C, b = W/l_C, dg in units of kT."""
    q = np.exp(dg)
    f = (1 + a) / (q + a)  # initial selection (k_off,D = q k_off,C)
    for _ in range(n):
        f = f * (b + 1) / (b + q)
    return f


def simulate(dg, n_products=20000, a=0.05, b=0.05, seed=1):
    """Follow single binding events: each passes the m step with probability a/(1+a) (correct) or a/(q+a)
    (wrong), and is then committed with probability b/(1+b) or b/(b+q); returns wrong/correct products."""
    rng = np.random.default_rng(seed)
    q = np.exp(dg)
    p = np.array([a / (1 + a) * b / (1 + b), a / (q + a) * b / (b + q)])
    made = np.zeros(2)
    while made[0] < n_products:
        wrong = rng.random(2_000_000) < 0.5
        u1, u2 = rng.random(wrong.size), rng.random(wrong.size)
        q1 = np.where(wrong, a / (q + a), a / (1 + a))
        q2 = np.where(wrong, b / (b + q), b / (1 + b))
        hit = (u1 < q1) & (u2 < q2)
        made += [np.sum(hit & ~wrong), np.sum(hit & wrong)]
    return made[1] / made[0]


fig = plt.figure(figsize=(12.6, 4.2))
gs = fig.add_gridspec(1, 3, width_ratios=[1.25, 1, 1])

# --- A: scheme ---
ax = fig.add_subplot(gs[0])
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis("off")
ax.set_title("A   One proofreading stage", loc="left", fontsize=9, color=P.ink())
bio.box(ax, (1.2, 3.0), 1.7, 0.9, token="neutral", text="E + X", size="small")
bio.box(ax, (4.4, 3.0), 1.5, 0.9, token="enzyme", text="EX", size="small")
bio.box(ax, (7.6, 3.0), 1.5, 0.9, token="highlight", text="EX*", size="small")
bio.box(ax, (7.6, 0.8), 1.9, 0.8, token="protein", text="product", size="small")
bio.arrow(ax, (2.1, 3.2), (3.6, 3.2), kind="process")
bio.arrow(ax, (3.6, 2.8), (2.1, 2.8), kind="process")
bio.label(ax, (2.85, 3.6), "k_on [X]", size="tiny")
bio.label(ax, (2.85, 2.4), "k_off,X", size="tiny")
bio.arrow(ax, (5.2, 3.0), (6.8, 3.0), kind="process")
bio.label(ax, (6.0, 3.45), "m", size="tiny")
bio.label(ax, (6.0, 2.35), "GTP hydrolysis", size="tiny", color=P.muted())
bio.arrow(ax, (7.6, 3.5), (1.4, 3.55), kind="process", bend=-0.35)
bio.label(ax, (4.6, 4.75), "l_X  (rejection)", size="tiny")
bio.arrow(ax, (7.6, 2.5), (7.6, 1.25), kind="process")
bio.label(ax, (8.05, 1.9), "W", size="tiny", ha="left")
bio.label(ax, (5.0, 0.15), "k_off,D / k_off,C = l_D / l_C = exp(ΔΔG / kT)", size="tiny", color=P.muted())

# --- B: error vs discrimination energy ---
ax = fig.add_subplot(gs[1])
dg = np.linspace(0, 8, 200)
toks = ["neutral", "rna", "dna"]
for n, tok in enumerate(toks):
    ax.semilogy(dg, error(dg, n), color=charts.line(tok), lw=1.6, label=f"n = {n}")
    ax.semilogy(dg, np.exp(-(n + 1) * dg), color=charts.line(tok), lw=0.9, ls="--")
pts = np.array([1.0, 2.0, 3.0])
sim = [simulate(d) for d in pts]
ax.semilogy(pts, sim, "o", ms=4.5, mfc=P.fill("rna"), mec=P.edge("rna"), label="simulation, n = 1")
ax.set_ylim(1e-8, 1.5)
ax.set_xlim(0, 8)
ax.legend(fontsize=7, frameon=False, loc="lower left")
charts.style_axes(ax, "ΔΔG / kT", "error ratio f")
ax.set_title("B   Error ratio", loc="left", fontsize=9, color=P.ink())

# --- C: speed-accuracy-cost trade-off ---
ax = fig.add_subplot(gs[2])
b = np.logspace(-3, 1.5, 200)
f1 = error(4.6, 1, a=0.05, b=b)
cost = 1 + 1 / b  # irreversible steps per correct product (one stage): 1/(fraction of EX*_C committed)
ax.loglog(cost, f1, color=charts.line("rna"), lw=1.8)
for bb in (10, 1, 0.1, 0.01):
    i = np.argmin(abs(b - bb))
    ax.plot(cost[i], f1[i], "o", ms=4, mfc=P.fill("highlight"), mec=P.edge("highlight"))
    ax.text(cost[i] * 1.25, f1[i] * 1.15, f"W/l_C = {bb:g}", fontsize=7, color=P.ink())
ax.axhline(0.01, color=P.muted(), lw=0.8, ls=":")
ax.axhline(1e-4, color=P.muted(), lw=0.8, ls=":")
ax.text(1.05, 0.0125, "no proofreading", fontsize=7, color=P.muted())
ax.text(1.05, 1.25e-4, "ideal limit f₀²", fontsize=7, color=P.muted())
ax.set_ylim(5e-5, 3e-2)
charts.style_axes(ax, "GTP spent per correct product", "error ratio f")
ax.set_title("C   Price of accuracy (ΔΔG = 4.6 kT)", loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
