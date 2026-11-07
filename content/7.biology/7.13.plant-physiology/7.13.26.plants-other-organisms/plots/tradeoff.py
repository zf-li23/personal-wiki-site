# Growth-defence trade-off and the time course of an induced defence (simple models).
# A: a plant allocates a fraction f of its carbon to defence. Relative growth rate g(f) = r0 (1 - f) - h0 exp(-a f):
# growth without defence r0 = 0.20 /d, efficiency of defence a = 5, herbivore pressure h0 (loss rate of an
# undefended plant). The optimum f* = ln(a h0 / r0) / a when a h0 > r0, otherwise 0.
# B: f* against r0 for two herbivore pressures: slow-growing plants (low r0) should invest more in defence
# (the resource availability hypothesis, Coley, Bryant and Chapin 1985).
# C: induced defence after one wounding event at t = 0. A fast wound signal S decays with tau = 10 min;
# dJ/dt = kJ S - J/30 min (jasmonate); dM/dt = kM J^2/(K^2 + J^2) - M/(2 h) (proteinase-inhibitor mRNA);
# dP/dt = kP M - P/(48 h) (proteinase-inhibitor protein). Curves are normalised to their maxima.
import matplotlib.pyplot as plt
import numpy as np

fig, (a, b, c) = plt.subplots(1, 3, figsize=(14.5, 4.3))
f = np.linspace(0, 1, 400)
r0, al = 0.20, 5.0
cols = ["#8a94a3", "#2e9e5b", "#d9a400", "#d9463b"]
for h0, col in zip([0.02, 0.08, 0.20, 0.40], cols):
    g = r0 * (1 - f) - h0 * np.exp(-al * f)
    a.plot(f, g, color=col, lw=2.1, label=f"$h_0$ = {h0:.2f} " + r"$\mathrm{d^{-1}}$")
    fs = max(0.0, np.log(al * h0 / r0) / al)
    a.plot([fs], [r0 * (1 - fs) - h0 * np.exp(-al * fs)], "o", color=col, ms=6)
a.axhline(0, color="0.5", lw=0.7)
a.set_xlabel("Fraction of carbon allocated to defence $f$")
a.set_ylabel(r"Net relative growth rate $g$ / $\mathrm{d^{-1}}$")
a.set_ylim(-0.25, 0.22)
a.legend(frameon=False, fontsize=8, loc="lower left")
a.set_title("A   Optimal allocation (dots: $f^*$)", loc="left", fontsize=10)

r = np.linspace(0.02, 0.45, 300)
for h0, col in [(0.10, "#2e9e5b"), (0.20, "#d9a400")]:
    fs = np.clip(np.log(al * h0 / r) / al, 0, None)
    b.plot(r, fs, color=col, lw=2.2, label=f"$h_0$ = {h0:.2f} " + r"$\mathrm{d^{-1}}$")
b.set_xlabel(r"Maximum relative growth rate $r_0$ / $\mathrm{d^{-1}}$")
b.set_ylabel("Optimal defence allocation $f^*$")
b.set_ylim(0, 0.8)
b.legend(frameon=False, fontsize=8)
b.set_title("B   Slow growers defend more", loc="left", fontsize=10)

t = np.logspace(-1, np.log10(7 * 24 * 60), 3000)  # minutes
dt = np.diff(np.concatenate([[0], t]))
J = M = Pp = 0.0
out = []
for ti, h in zip(t, dt):
    S = np.exp(-ti / 10)
    J += h * (1.0 * S - J / 30)
    M += h * (J**2 / (0.5**2 + J**2) - M / 120)
    Pp += h * (M - Pp / (48 * 60))
    out.append((S, J, M, Pp))
out = np.array(out)
names = ["wound signal", "jasmonate (JA-Ile)", "PI mRNA", "PI protein"]
cc = ["#8a94a3", "#d9463b", "#3e7cb8", "#2e9e5b"]
for k in range(4):
    c.plot(t / 60, out[:, k] / out[:, k].max(), color=cc[k], lw=2.1, label=names[k])
c.set_xscale("log")
c.set_xticks([1 / 60, 10 / 60, 1, 6, 24, 168])
c.set_xticklabels(["1 min", "10 min", "1 h", "6 h", "1 d", "7 d"])
c.set_xlabel("Time after wounding (log scale)")
c.set_ylabel("Relative level")
c.legend(frameon=False, fontsize=7.8, loc="upper left", ncol=2)
c.set_ylim(0, 1.45)
c.set_title("C   Induced defence after one wound", loc="left", fontsize=10)
fig.tight_layout()
