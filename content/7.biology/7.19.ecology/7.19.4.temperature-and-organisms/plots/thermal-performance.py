# Thermal performance curve (simulated data, illustrative parameters).
# Sharpe-Schoolfield model with high-temperature inactivation:
#   r(T) = r_ref exp[E/k (1/T_ref - 1/T)] / (1 + exp[E_h/k (1/T_h - 1/T)]),  T in kelvin,
#   true parameters r_ref = 1 at T_ref = 20 C, E = 0.65 eV, E_h = 3.0 eV, T_h = 32 C.
# A: performance measured at 2 C intervals with 8% noise, and the curve fitted by nonlinear least squares;
#    the fitted optimum and the critical thermal limits (CTmin, CTmax, where performance falls to 10% of the
#    maximum) are marked.
# B: Jensen's inequality: mean performance when temperature fluctuates sinusoidally around a mean with
#    amplitude 0, 3 or 6 C, against the mean temperature. Fluctuations raise performance where the curve is
#    convex (cool side) and lower it where it is concave (near and above the optimum).
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit, brentq
import wikibio as bio

P = bio.P
k = 8.617e-5
Tref = 293.15


def ss(Tc, rref, E, Eh, Th):
    T = Tc + 273.15
    return rref * np.exp(E / k * (1 / Tref - 1 / T)) / (1 + np.exp(Eh / k * (1 / (Th + 273.15) - 1 / T)))


true = (1.0, 0.65, 3.0, 32.0)
rng = np.random.default_rng(1)
Tobs = np.arange(8, 41, 2.0)
yobs = ss(Tobs, *true) * (1 + rng.normal(0, 0.08, Tobs.size))
fit, _ = curve_fit(ss, Tobs, yobs, p0=[1.0, 0.6, 2.5, 30.0], maxfev=20000)

T = np.linspace(0, 45, 901)
r = ss(T, *fit)
i = np.argmax(r)
Topt, rmax = T[i], r[i]
ctmin = brentq(lambda t: ss(t, *fit) - 0.1 * rmax, -10, Topt)
ctmax = brentq(lambda t: ss(t, *fit) - 0.1 * rmax, Topt, 60)

fig, (a, b) = plt.subplots(1, 2, figsize=(10.8, 4.3))
a.plot(T, r, color=P.edge("dna"), lw=2, label="fitted Sharpe–Schoolfield")
a.plot(Tobs, yobs, "o", color=P.ink(), ms=4.5, label="measurements (simulated)")
for t0, name in ((ctmin, "CTmin"), (Topt, "Topt"), (ctmax, "CTmax")):
    a.axvline(t0, color=P.muted(), lw=0.8, ls="--")
    a.text(t0, rmax * 1.12, "%s\n%.1f °C" % (name, t0), ha="center", fontsize=7.5, color=P.muted())
a.annotate("", xy=(ctmin, 0.1 * rmax), xytext=(ctmax, 0.1 * rmax),
           arrowprops=dict(arrowstyle="<->", color=P.edge("rna"), lw=1))
a.text((ctmin + ctmax) / 2, 0.14 * rmax, "thermal tolerance range", ha="center", fontsize=7.5, color=P.edge("rna"))
a.set_xlim(0, 45)
a.set_ylim(0, rmax * 1.3)
a.set_xlabel("Body temperature / °C")
a.set_ylabel("Performance (relative)")
a.legend(frameon=False, fontsize=7.5, loc="center left", bbox_to_anchor=(0.03, 0.62))
a.set_title("A  Thermal performance curve", loc="left", fontweight="bold")

ph = np.linspace(0, 2 * np.pi, 361)[:-1]
means = np.linspace(5, 40, 351)
for amp, tok in ((0, "ink"), (3, "atp"), (6, "negative")):
    m = [np.mean(ss(mu + amp * np.sin(ph), *true)) for mu in means]
    col = P.ink() if tok == "ink" else P.edge(tok)
    b.plot(means, m, color=col, lw=2, label="amplitude %d °C" % amp)
b.set_xlim(5, 40)
b.set_xlabel("Mean temperature / °C")
b.set_ylabel("Mean performance")
b.legend(frameon=False, fontsize=7.5, loc="upper left")
b.set_title("B  Fluctuating temperature", loc="left", fontweight="bold")
for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
