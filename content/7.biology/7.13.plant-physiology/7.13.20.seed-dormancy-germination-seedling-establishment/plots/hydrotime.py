# Hydrotime model of germination (Gummerson 1986; Bradford 1990): each seed g germinates at time t_g with
# (Psi - Psi_b(g)) t_g = theta_H, and the base water potentials Psi_b are normally distributed in the seed
# population (mean Psi_b(50), s.d. sigma). Fraction germinated at time t and water potential Psi:
# G = Phi((Psi - theta_H / t - Psi_b(50)) / sigma). Parameters of the order of tomato seeds (illustrative):
# theta_H = 30 MPa h, Psi_b(50) = -0.70 MPa, sigma = 0.20 MPa. (A) Germination time courses at several water
# potentials (points: simulated counts of 100 seeds); (B) all curves collapse onto one line when probit(G)
# is plotted against Psi - theta_H / t.
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

thH, pb50, sg = 30.0, -0.70, 0.20
rng = np.random.default_rng(0)
t = np.linspace(1, 120, 600)
psis = [0.0, -0.2, -0.4, -0.6, -0.8]
cols = plt.cm.viridis(np.linspace(0.05, 0.85, len(psis)))
fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.3))
seeds = rng.normal(pb50, sg, 100)
for psi, c in zip(psis, cols):
    G = norm.cdf((psi - thH / t - pb50) / sg)
    a.plot(t, G * 100, color=c, lw=2.2, label=f"Ψ = {psi:.1f} MPa")
    tg = np.where(psi > seeds, thH / np.clip(psi - seeds, 1e-9, None), np.inf)
    ts = np.arange(6, 121, 6)
    frac = np.array([(tg <= x).mean() for x in ts])
    a.plot(ts, frac * 100, "o", color=c, ms=3.5)
    ok = (frac > 0.02) & (frac < 0.98)
    b.plot(psi - thH / ts[ok], norm.ppf(frac[ok]), "o", color=c, ms=5)
xx = np.linspace(-1.4, -0.2, 50)
b.plot(xx, (xx - pb50) / sg, color="0.3", lw=1.5, ls="--", label="probit = (x − Ψb(50))/σ")
a.set_xlabel("Time after sowing t / h")
a.set_ylabel("Germination G / %")
a.set_xlim(0, 120)
a.set_ylim(0, 102)
a.legend(frameon=False, fontsize=8.5, loc="upper left")
a.set_title("A   Germination time courses", loc="left", fontsize=10)
b.set_xlabel("Ψ − θH / t / MPa")
b.set_ylabel("probit(G)")
b.legend(frameon=False, fontsize=8.5, loc="upper left")
b.set_title("B   Normalised: one line", loc="left", fontsize=10)
for x in (a, b):
    x.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
