# Turnover of the plasma free fatty acid (FFA) pool: a one-compartment model.
#   dF/dt = Ra - k F,  k = ln 2 / t_half,  t_half = 2.5 min
# F is the FFA mass in 3 L of plasma (0.15 g/L at rest, so F = 0.45 g); Ra is the rate of appearance
# from adipose lipolysis. At rest Ra = k F = 0.125 g/min, about 180 g/day of fatty acid, enough to cover
# resting energy needs. A: washout of a tracer bolus (half-life 2.5 min). B: lipolysis rises 6-fold at t = 10 min
# (catecholamines in exercise; insulin falls in fasting): plasma FFA follows within about five
# half-lives; with a 60-min half-life (hypothetical slow pool) the response would take hours.
import matplotlib.pyplot as plt
import numpy as np

th = 2.5
k = np.log(2) / th
F0 = 0.45
Ra0 = k * F0
t = np.linspace(0, 20, 400)
fig, (axa, axb) = plt.subplots(1, 2, figsize=(11, 4.2))
axa.plot(t, 100 * np.exp(-k * t), color="#c0392b", lw=2, label="plasma FFA tracer, $t_{1/2}$ = 2.5 min")
axa.axhline(50, color="0.6", lw=0.8, ls=":")
axa.axvline(th, color="0.6", lw=0.8, ls=":")
axa.set_xlabel("Time after tracer injection / min")
axa.set_ylabel("Tracer remaining / %")
axa.set_title("A  Washout of the FFA pool", loc="left", fontsize=11, fontweight="bold")
axa.text(19.5, 60, f"flux = k F = {Ra0:.3f} g/min\n= {Ra0 * 1440:.0f} g/day", ha="right", fontsize=9)
axa.legend(frameon=False, fontsize=8.5)

T = np.linspace(0, 60, 1200)
for thx, col, lab in ((2.5, "#c0392b", "$t_{1/2}$ = 2.5 min (real)"), (60.0, "0.5", "$t_{1/2}$ = 60 min (hypothetical)")):
    kk = np.log(2) / thx
    F = np.empty_like(T)
    F[0] = F0
    Ra_rest = kk * F0
    for i in range(1, len(T)):
        dt = T[i] - T[i - 1]
        Ra = Ra_rest * (6.0 if T[i] >= 10 else 1.0)
        F[i] = F[i - 1] + dt * (Ra - kk * F[i - 1])
    axb.plot(T, F / 3.0, color=col, lw=2, label=lab)
axb.axvline(10, color="0.6", lw=0.8, ls=":")
axb.text(11, 0.86, "lipolysis x6", fontsize=8.5, color="0.4")
axb.set_xlabel("Time / min")
axb.set_ylabel("Plasma FFA / (g/L)")
axb.set_ylim(0, 1.0)
axb.set_title("B  Fast turnover gives fast control", loc="left", fontsize=11, fontweight="bold")
axb.legend(frameon=False, fontsize=8.5, loc="lower right")
fig.tight_layout()
