# A, B: single exponential (k = 0.5), two-pool (f = 0.3, k1 = 4, k2 = 0.25) and gamma continuum
#       (alpha = 0.8, beta = 0.6 yr; Proposition 44.5.2): mass remaining and apparent k = -d ln X/dt.
# C: three parallel soil pools (input 300 g C m^-2 yr^-1 split 0.6/0.35/0.05; turnover 2, 30, 800 yr),
#    at steady state, then all k multiplied by q = 2^(2/10) = 1.149 at year 0 (2 C warming, Q10 = 2).
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio

P = bio.P
fig, (a, b, c) = plt.subplots(1, 3, figsize=(12.8, 4.2))
t = np.linspace(0, 20, 2001)
single = np.exp(-0.5 * t)
two = 0.3 * np.exp(-4 * t) + 0.7 * np.exp(-0.25 * t)
al, be = 0.8, 0.6
cont = (1 + t / be) ** (-al)
for y, lab, tok in ((single, "single exponential", "neutral"), (two, "two pools", "dna"),
                    (cont, "gamma continuum", "rna")):
    a.plot(t, y * 100, color=P.edge(tok), lw=2, label=lab)
    kapp = -np.gradient(np.log(y), t)
    b.plot(t, kapp, color=P.edge(tok), lw=2, label=lab)
a.set_yscale("log")
a.set_ylim(0.5, 100)
a.set_xlim(0, 20)
a.set_xlabel("Time / years")
a.set_ylabel("Mass remaining / % (log scale)")
a.legend(frameon=False, fontsize=8)
a.set_title("A  Mass remaining", loc="left", fontweight="bold")
b.set_ylim(0, 1.6)
b.set_xlim(0, 10)
b.set_xlabel("Time / years")
b.set_ylabel("Apparent k = −d ln X / dt  / yr⁻¹")
b.legend(frameon=False, fontsize=8)
b.set_title("B  Apparent decomposition constant", loc="left", fontweight="bold")

L = 300.0
frac = np.array([0.6, 0.35, 0.05])
tau = np.array([2.0, 30.0, 800.0])
k0 = 1 / tau
q = 2 ** 0.2
ss0 = L * frac / k0
yrs = np.linspace(0, 600, 1201)
pools = np.array([L * f / (q * k) + (s - L * f / (q * k)) * np.exp(-q * k * yrs) for f, k, s in zip(frac, k0, ss0)])
tot = pools.sum(axis=0)
for p_, lab, tok in zip(pools, ("active (2 yr)", "slow (30 yr)", "passive (800 yr)"), ("plant", "antibody", "animal")):
    c.plot(yrs, (p_ - p_[0]) / 1000, color=P.edge(tok), lw=1.6, label=lab)
c.plot(yrs, (tot - tot[0]) / 1000, color=P.ink(), lw=2.2, label="total")
c.axhline((tot[0] / q - tot[0]) / 1000, color=P.muted(), lw=0.8, ls=":")
c.text(590, (tot[0] / q - tot[0]) / 1000 + 0.05, f"eventual loss {100*(1-1/q):.0f}% of {tot[0]/1000:.1f} kg C m⁻²",
       fontsize=7.5, ha="right", va="bottom", color=P.muted())
c.set_xlabel("Years after warming")
c.set_ylabel("Change in soil carbon / kg C m⁻²")
c.set_xlim(0, 600)
c.legend(frameon=False, fontsize=7.5, loc="center right")
c.set_title("C  Soil carbon after warming", loc="left", fontweight="bold")
for ax in (a, b, c):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
