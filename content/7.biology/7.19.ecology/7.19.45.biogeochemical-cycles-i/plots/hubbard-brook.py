# The Hubbard Brook deforestation experiment.
# A: export of dissolved ions in stream water from the deforested catchment relative to the
#    control catchment (Likens and Bormann; factors as summarized by Begon and Townsend 2021).
# B: a compartment model of the nitrogen cycle of a forested catchment (plants V, soil organic
#    nitrogen O, inorganic nitrogen S) with the trees felled at t = 0, regrowth suppressed by
#    herbicide for three years and then allowed; illustrative parameters.
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import wikibio as bio

P = bio.P
fig, (a, b) = plt.subplots(1, 2, figsize=(10.8, 4.2), gridspec_kw={"width_ratios": [0.8, 1.2]})
ions = ["nitrate", "potassium", "calcium", "magnesium", "sodium"]
fac = [60, 14, 7, 5, 2.5]
toks = ["dna", "metabolite", "bone", "chloroplast", "neutral"]
a.barh(range(5), fac, color=[P.fill(t) for t in toks], edgecolor=[P.edge(t) for t in toks])
for i, f in enumerate(fac):
    a.text(f * 1.1, i, f"{f:g}×", va="center", fontsize=8, color=P.ink())
a.set_xscale("log")
a.set_xlim(1, 150)
a.set_yticks(range(5), ions)
a.invert_yaxis()
a.set_xlabel("Increase in stream export after felling")
a.set_title("A  Hubbard Brook, 1966-1968", loc="left", fontweight="bold")

u, l, mz, lam, inp = 4.0, 0.16, 0.02, 0.2, 4.0   # 1/yr; input kg N/ha/yr
V0, O0 = 500.0, 4000.0
S0 = (inp + mz * O0) / (u + lam)

def rhs(t, x, cut):
    V, O, S = x
    if cut and t >= 0:
        grow = 0.0 if t < 3 else 1.0
        f = 1 + 0.4 * max(0.0, 1 - V / V0)            # more runoff; warmer, wetter soil while open
        lam_t, mz_t = lam * f, mz * f
        uptake = u * S * grow * min(1.0, 0.05 + V / V0)   # regrowth restores uptake
        dV = uptake - l * V
    else:
        lam_t, mz_t, uptake = lam, mz, u * S
        dV = uptake - l * V
    return [dV, l * V - mz_t * O, inp + mz_t * O - uptake - lam_t * S]

t = np.linspace(-2, 20, 2201)
pre = solve_ivp(rhs, (-2, 0), [V0, O0, S0], args=(False,), max_step=0.01)
x0 = pre.y[:, -1]
x0 = [0.0, x0[1] + 0.8 * x0[0], x0[2]]           # felled biomass left as slash
post = solve_ivp(rhs, (0, 20), x0, args=(True,), max_step=0.01, dense_output=True)
tp = t[t >= 0]
Vp, Op, Sp = post.sol(tp)
exp_ctl = lam * S0 * np.ones_like(t)
lam_t = lam * (1 + 0.4 * np.clip(1 - Vp / V0, 0, None))
b.plot(t, exp_ctl, color=P.muted(), lw=1.4, ls="--", label="control catchment")
b.plot(np.r_[t[t < 0], tp], np.r_[lam * S0 * np.ones((t < 0).sum()), lam_t * Sp], color=P.fill("dna"), lw=2,
       label="felled catchment: nitrate export")
b.set_yscale("log")
b.set_ylim(1, 300)
b.set_xlim(-2, 20)
b.axvspan(0, 3, color=P.fill("highlight"), alpha=0.3, lw=0)
b.text(1.5, 220, "felled;\nherbicide", ha="center", va="top", fontsize=7.5, color=P.muted())
b.set_xlabel("Years after felling")
b.set_ylabel("Nitrogen export / kg ha$^{-1}$ yr$^{-1}$")
b2 = b.twinx()
b2.plot(tp, Vp, color=P.fill("plant"), lw=1.6, label="plant nitrogen")
b2.set_ylim(0, 1500)
b2.set_ylabel("Plant nitrogen / kg ha$^{-1}$")
h1, l1 = b.get_legend_handles_labels()
h2, l2 = b2.get_legend_handles_labels()
b.legend(h1 + h2, l1 + l2, frameon=False, fontsize=7.5, loc="upper right")
b.set_title("B  Uncoupling of uptake and mineralization", loc="left", fontweight="bold")
for ax in (a, b, b2):
    ax.spines["top"].set_visible(False)
a.spines["right"].set_visible(False)
fig.tight_layout()
