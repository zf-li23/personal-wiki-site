# Quantal analysis at the neuromuscular junction (illustrative parameters close to classic frog and cat data).
# (A) del Castillo-Katz experiment: in low Ca2+ / high Mg2+ the evoked end-plate potential (EPP) of 400 trials
#     is simulated as k quanta, k ~ Poisson(m) with m = 1.9, each quantum of size q ~ N(0.40, 0.08) mV, plus
#     recording noise of 0.012 mV. Curve: the Poisson prediction (sum of Gaussians k q, sd sqrt(k) sigma_q);
#     bar at zero: the failures. Two estimates of m: direct (mean EPP / mean quantum) and failures (ln(N/N0)).
# (B) Dodge-Rahamimoff cooperativity: m = K ([Ca]/(1 + [Ca]/K1 + [Mg]/K2))^4, K1 = 1.5 mM, K2 = 1.0 mM;
#     on log-log axes the slope approaches 4 at low [Ca]: four Ca2+ ions act together to release a vesicle.
# (C) Safety factor in a 3 Hz train (EPP normalized to the depolarization needed to fire the muscle action
#     potential): quantal content runs down to 60 % of its first value; normal junction (safety factor 3),
#     myasthenia gravis (quantal size reduced to 35 % by loss of receptors) and the same after an
#     acetylcholinesterase inhibitor (quantal size x 1.6). Bars below 1 are transmission failures.
import matplotlib.pyplot as plt
import numpy as np
from math import factorial

rng = np.random.default_rng(0)
fig, (a, b, c) = plt.subplots(1, 3, figsize=(13.5, 4.2))

# ---- A: quantal histogram
m, q, sq, noise, N = 1.9, 0.40, 0.08, 0.012, 400
k = rng.poisson(m, N)
amp = np.array([rng.normal(q, sq, kk).sum() if kk else 0.0 for kk in k]) + rng.normal(0, noise, N)
bins = np.arange(-0.125, 2.6, 0.05)
a.hist(amp, bins=bins, color="#8fb3d9", edgecolor="#2f6fb5", lw=0.6, label="simulated trials")
x = np.linspace(0.05, 2.6, 600)
dens = np.zeros_like(x)
for kk in range(1, 9):
    s = np.sqrt(kk * sq**2 + noise**2)
    pk = np.exp(-m) * m**kk / factorial(kk)
    dens += N * pk * 0.05 * np.exp(-(x - kk * q) ** 2 / (2 * s**2)) / (s * np.sqrt(2 * np.pi))
a.plot(x, dens, color="#c0504d", lw=2.0, label="Poisson prediction")
n0 = np.sum(k == 0)
a.bar([0], [N * np.exp(-m)], width=0.05, fill=False, edgecolor="#c0504d", lw=1.6, ls="--")
m_dir = amp.mean() / q
m_fail = np.log(N / n0)
a.text(0.98, 0.97, f"failures: {n0} of {N}\nm (failures) = ln(N/N0) = {m_fail:.2f}\nm (direct) = mean EPP / q = {m_dir:.2f}",
       transform=a.transAxes, ha="right", va="top", fontsize=8.5)
for kk in range(1, 5):
    a.text(kk * q, -2.2, f"{kk}q", ha="center", va="top", fontsize=8, color="0.4")
a.set_xlabel("EPP amplitude / mV")
a.set_ylabel("Number of trials")
a.set_ylim(-4.5, None)
a.legend(frameon=False, fontsize=8.5, loc="center right")
a.set_title("A   Quantal EPPs (low Ca²⁺, high Mg²⁺)", loc="left", fontsize=10)

# ---- B: fourth-power dependence on Ca2+
ca = np.logspace(-1, np.log10(4), 200)
K1, K2 = 1.5, 1.0
for mg, col in ((0.0, "#2f6fb5"), (1.0, "#7a5fb0"), (4.0, "#c0504d")):
    mm = 2000 * (ca / (1 + ca / K1 + mg / K2)) ** 4
    b.loglog(ca, mm, color=col, lw=2.0, label=f"[Mg²⁺] = {mg:g} mM")
ref = 2000 * (0.12) ** 4 * (ca / 0.12) ** 4
b.loglog(ca[ca < 0.5], ref[ca < 0.5] * 0.25, color="0.45", lw=1.0, ls="--")
b.text(0.21, 0.35, "slope 4", fontsize=8.5, color="0.5")
b.axhspan(100, 300, color="0.6", alpha=0.25, lw=0)
b.text(0.11, 170, "normal junction", fontsize=8, color="0.5", va="center")
b.set_xlabel("[Ca²⁺]ₒ / mM")
b.set_ylabel("Quantal content m")
b.set_ylim(1e-2, 2e3)
b.legend(frameon=False, fontsize=8.5, loc="lower right")
b.set_title("B   Cooperative action of Ca²⁺", loc="left", fontsize=10)

# ---- C: safety factor in a train
n = np.arange(1, 11)
rundown = 0.6 + 0.4 * np.exp(-(n - 1) / 1.5)
cases = [("normal", 3.0, "#2f6fb5", -0.27), ("myasthenia gravis", 3.0 * 0.35, "#c0504d", 0.0),
         ("myasthenia + AChE inhibitor", 3.0 * 0.35 * 1.6, "#d9a03f", 0.27)]
for name, sf, col, off in cases:
    e = sf * rundown
    c.bar(n + off, e, width=0.26, color=col, edgecolor=col, label=name, alpha=0.9)
    fails = e < 1
    c.plot(n[fails] + off, e[fails] + 0.12, "x", color=col, ms=5)
c.axhline(1.0, color="0.5", lw=1.0, ls="--", label="threshold")
c.set_xticks(n)
c.set_xlabel("Stimulus number (3 Hz)")
c.set_ylabel("EPP / depolarization needed to fire")
c.set_ylim(0, 3.4)
c.legend(frameon=False, fontsize=8.5, loc="upper right")
c.set_title("C   Safety factor and its loss", loc="left", fontsize=10)
for ax in (a, b, c):
    ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
