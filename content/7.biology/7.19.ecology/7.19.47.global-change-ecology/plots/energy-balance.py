# Zero-dimensional energy balance models of planetary climate.
# A: effective radiating temperature Te = [(1 - albedo) S / (4 sigma)]^(1/4) and observed mean surface
#    temperature of Venus, Earth and Mars, with the single-layer greenhouse value 2^(1/4) Te.
# B: two-layer model (mixed layer C = 8, deep ocean C_D = 100 W yr m^-2 K^-1, feedback lambda = 1.3,
#    exchange gamma = 0.7 W m^-2 K^-1; forcing 3.93 ln(C/C0)/ln 2 W m^-2): abrupt doubling of CO2 and
#    a 1% per year increase; equilibrium climate sensitivity 3.0 K, transient response about 2 K.
# C: Budyko-Sellers model with temperature-dependent albedo: equilibrium global temperature against
#    the solar constant relative to today, showing the ice-free and snowball branches.
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio

P = bio.P
sig = 5.670e-8
fig, (a, b, c) = plt.subplots(1, 3, figsize=(13.4, 4.2))
planets = [("Venus", 2601, 0.76, 737), ("Earth", 1361, 0.30, 288), ("Mars", 586, 0.25, 210)]
x = np.arange(3)
Te = [((1 - al) * S / (4 * sig)) ** 0.25 for _, S, al, _ in planets]
Ts = [t for *_, t in planets]
a.bar(x - 0.27, Te, 0.26, color=P.fill("dna"), edgecolor=P.edge("dna"), label="effective $T_e$")
a.bar(x, [2 ** 0.25 * t for t in Te], 0.26, color=P.light("highlight"), edgecolor=P.edge("highlight"),
      label="one opaque layer, $2^{1/4}T_e$")
a.bar(x + 0.27, Ts, 0.26, color=P.fill("negative"), edgecolor=P.edge("negative"), label="observed surface")
for i in range(3):
    a.text(x[i] - 0.27, Te[i] + 12, f"{Te[i]:.0f}", ha="center", fontsize=7, color=P.ink())
    a.text(x[i] + 0.27, Ts[i] + 12, f"{Ts[i]:.0f}", ha="center", fontsize=7, color=P.ink())
a.set_xticks(x, [p[0] for p in planets])
a.set_ylabel("Temperature / K")
a.set_ylim(0, 820)
a.legend(frameon=False, fontsize=7.5, loc="upper right")
a.set_title("A  Greenhouse effect of three planets", loc="left", fontweight="bold")

C, CD, lam, gam, F2 = 8.0, 100.0, 1.3, 0.7, 3.93
def run(F):
    T = TD = 0.0
    out = []
    for f in F:
        T, TD = T + (f - lam * T - gam * (T - TD)) / C, TD + gam * (T - TD) / CD
        out.append(T)
    return np.array(out)
yrs = np.arange(0, 300)
Fab = np.full(yrs.size, F2)
F1 = F2 * np.minimum(yrs, 140) * np.log(1.01) / np.log(2)
b.plot(yrs, run(Fab), color=P.fill("negative"), lw=2, label="abrupt doubling of CO$_2$")
b.plot(yrs, run(F1), color=P.fill("dna"), lw=2, label="1% per year to quadrupling")
b.axhline(F2 / lam, color=P.muted(), lw=0.8, ls="--")
b.text(295, F2 / lam + 0.12, f"ECS {F2 / lam:.1f} K", ha="right", fontsize=7.5, color=P.muted())
t70 = run(F1)[70]
b.plot([70], [t70], "o", color=P.ink(), ms=4)
b.annotate(f"TCR {t70:.1f} K at year 70", (70, t70), xytext=(8, -14), textcoords="offset points", fontsize=7.5)
b.set_xlabel("Years")
b.set_ylabel("Warming / K")
b.set_ylim(0, 7)
b.legend(frameon=False, fontsize=7.5, loc="upper left")
b.set_title("B  Two-layer response", loc="left", fontweight="bold")

A0, B0, Q0 = 203.3, 2.09, 1361 / 4
Tg = np.linspace(-60, 40, 800)
alb = 0.46 - 0.16 * np.tanh(Tg / 8.0)
mu = (A0 + B0 * Tg) / (Q0 * (1 - alb))
dmu = np.gradient(mu, Tg)
stable = dmu > 0
for mask, ls in ((stable, "-"), (~stable, "--")):
    y = np.where(mask, Tg, np.nan)
    c.plot(mu, y, color=P.ink(), lw=2, ls=ls)
c.axvline(1, color=P.muted(), lw=0.8, ls=":")
c.text(1.01, -50, "today", fontsize=7.5, color=P.muted())
c.text(0.84, 22, "ice-free branch", fontsize=7.5, color=P.ink())
c.text(1.06, -40, "snowball branch", fontsize=7.5, color=P.ink())
c.set_xlim(0.8, 1.4)
c.set_ylim(-60, 40)
c.set_xlabel("Solar constant / present value")
c.set_ylabel("Equilibrium global temperature / °C")
c.set_title("C  Ice-albedo bistability", loc="left", fontweight="bold")
for ax in (a, b, c):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
