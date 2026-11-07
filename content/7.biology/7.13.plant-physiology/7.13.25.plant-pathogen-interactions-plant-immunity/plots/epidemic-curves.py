# van der Plank's logistic model of a polycyclic epidemic, dx/dt = r x (1 - x).
# x: disease proportion (severity), r: apparent infection rate per day, x0: initial disease.
# Panel A: susceptible cultivar (r = 0.40 /d, x0 = 1e-4), vertical (race-specific) resistance that removes
# 99 % of the effective initial inoculum (x0 = 1e-6, same r), and horizontal (race-nonspecific) resistance that
# lowers r to 0.20 /d (same x0). Panel B: the logit transform ln[x/(1-x)] is linear in t with slope r.
# Parameter values are illustrative, of the order reported for potato late blight on susceptible cultivars.
import matplotlib.pyplot as plt
import numpy as np


def logistic(t, x0, r):
    e = x0 * np.exp(r * t)
    return e / (1 - x0 + e)


t = np.linspace(0, 70, 400)
cases = [
    ("susceptible", 1e-4, 0.40, "#d9463b", "-"),
    ("vertical resistance ($x_0$/100)", 1e-6, 0.40, "#3e7cb8", "--"),
    ("horizontal resistance ($r$/2)", 1e-4, 0.20, "#2e9e5b", "-"),
]
fig, (a, b) = plt.subplots(1, 2, figsize=(12.5, 4.3))
for name, x0, r, c, ls in cases:
    x = logistic(t, x0, r)
    a.plot(t, 100 * x, color=c, ls=ls, lw=2.2, label=name)
    b.plot(t, np.log(x / (1 - x)), color=c, ls=ls, lw=2.2)
    t50 = np.log((1 - x0) / x0) / r
    a.plot([t50], [50], "o", color=c, ms=6)
a.axhline(5, color="0.5", lw=0.8, ls=":")
a.text(48, 7, "5 % (damage becomes visible)", fontsize=8.5, color="0.4")
a.set_xlabel("Time / d")
a.set_ylabel("Disease severity $x$ / %")
a.set_xlim(0, 70)
a.set_ylim(0, 102)
a.legend(frameon=False, fontsize=8.3, loc="lower right", bbox_to_anchor=(1.0, 0.08))
a.set_title("A   Logistic epidemics (dots: $t_{50}$)", loc="left", fontsize=10)

# synthetic field data for panel B
rng = np.random.default_rng(0)
td = np.arange(8, 33, 4.0)
xd = logistic(td, 1e-4, 0.40) * np.exp(rng.normal(0, 0.15, td.size))
xd = np.clip(xd, 1e-4, 0.99)
y = np.log(xd / (1 - xd))
slope, icpt = np.polyfit(td, y, 1)
b.plot(td, y, "s", color="black", ms=5, zorder=5, label="field survey (simulated)")
b.plot(t, icpt + slope * t, color="black", lw=0.9, ls=":", label=f"least-squares line, slope $r$ = {slope:.2f} " + "$\\mathrm{d^{-1}}$")
b.set_xlabel("Time / d")
b.set_ylabel("logit $x$ = ln[$x$/(1 − $x$)]")
b.set_xlim(0, 70)
b.set_ylim(-15, 8)
b.legend(frameon=False, fontsize=8.3, loc="lower right")
b.set_title("B   Logit transform: straight lines of slope $r$", loc="left", fontsize=10)
fig.tight_layout()
