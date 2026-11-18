# A three-compartment model of nitrogen in a forest: plants (x1), soil organic matter (x2) and
# available inorganic nitrogen (x3); input to x3 by deposition and fixation, loss from x3 by leaching.
# A: fate of a tracer pulse added to the inorganic pool. B: mean time spent per visit and in total
# (columns of the fundamental matrix (-A)^-1) in each compartment.
# C: mean transit time and number of cycles against the leaching rate constant.
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm
import wikibio as bio

P = bio.P
u, l, mz = 4.0, 0.16, 0.02       # uptake, litterfall, mineralization (1/yr)

def matrix(lam):
    return np.array([[-l, 0.0, u],
                     [l, -mz, 0.0],
                     [0.0, mz, -u - lam]])

lam = 0.5
A = matrix(lam)
t = np.logspace(-2, np.log10(5000), 400)
X = np.array([expm(A * s) @ np.array([0, 0, 1.0]) for s in t])
mean_t = np.linalg.solve(-A, np.array([0, 0, 1.0])).sum()

fig, (a, b, c) = plt.subplots(1, 3, figsize=(12.6, 4.0))
cols = [("plants", "plant"), ("soil organic matter", "animal"), ("inorganic N", "dna")]
for i, (lab, tok) in enumerate(cols):
    a.plot(t, X[:, i], color=P.fill(tok), lw=1.8, label=lab)
a.plot(t, X.sum(axis=1), color=P.ink(), lw=2, label="whole system")
a.set_xscale("log")
a.set_xlim(1e-2, 5000)
a.set_ylim(0, 1.03)
a.set_xlabel("Years after the pulse")
a.set_ylabel("Fraction of the tracer")
a.legend(frameon=False, fontsize=7.5, loc="center left")
a.set_title("A  Fate of a tracer pulse", loc="left", fontweight="bold")

# B: expected total time in each compartment for an atom entering the inorganic pool, (-A)^-1 e3,
# and the mean time per visit (turnover time of the compartment)
N = np.linalg.inv(-A)[:, 2]
per = np.array([1 / l, 1 / mz, 1 / (u + lam)])
xs = np.arange(3)
b.bar(xs - 0.2, per, 0.38, color=[P.light(tok) for _, tok in cols], edgecolor=[P.edge(tok) for _, tok in cols],
      label="per visit")
b.bar(xs + 0.2, N, 0.38, color=[P.fill(tok) for _, tok in cols], edgecolor=[P.edge(tok) for _, tok in cols],
      label="in total")
for x, v, w in zip(xs, per, N):
    b.text(x - 0.2, v * 1.15, f"{v:.2g}", ha="center", fontsize=7.5, color=P.ink())
    b.text(x + 0.2, w * 1.15, f"{w:.3g}", ha="center", fontsize=7.5, color=P.ink())
b.set_yscale("log")
b.set_ylim(0.1, 2000)
b.set_xticks(xs, ["plants", "soil organic", "inorganic N"])
b.set_ylabel("Mean time / yr")
b.legend(frameon=False, fontsize=7.5, loc="center right")
b.text(-0.45, 900, f"sum of totals = mean transit time {mean_t:.0f} yr", fontsize=7.5, ha="left", color=P.muted())
b.set_title("B  Time spent in each compartment", loc="left", fontweight="bold")

lams = np.logspace(-2, 1, 200)
means = [np.linalg.solve(-matrix(x), np.array([0, 0, 1.0])).sum() for x in lams]
cycles = u / lams
c.plot(lams, means, color=P.ink(), lw=2, label="mean transit time / yr")
c.plot(lams, cycles, color=P.fill("plant"), lw=1.8, ls="--", label="mean number of cycles")
c.axvline(lam, color=P.muted(), lw=0.8, ls=":")
c.set_xscale("log")
c.set_yscale("log")
c.set_xlabel("Leaching rate constant $\\lambda$ / yr$^{-1}$")
c.legend(frameon=False, fontsize=7.5, loc="upper right")
c.set_title("C  Leakiness and retention", loc="left", fontweight="bold")
for ax in (a, b, c):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
