# Counting by the Venus flytrap (Dionaea muscipula): a calcium-threshold model (illustrative; after the
# Ca2+ imaging of Suda et al. 2020 and the action-potential counting of Boehm et al. 2016). Each touch of a
# trigger hair fires an action potential that raises cytosolic Ca2+ by a step c0; Ca2+ decays with time
# constant tau; the trap closes when Ca2+ exceeds the threshold theta (c0 < theta < 2 c0). Two touches
# therefore close the trap only if they are separated by less than dt_max = tau ln(c0 / (theta - c0)).
# (A) Ca2+ traces for touch intervals of 10, 25 and 45 s; (B) closure window as a function of theta / c0.
import matplotlib.pyplot as plt
import numpy as np

c0, tau, theta = 1.0, 30.0, 1.45
t = np.linspace(-5, 90, 2000)
fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.2), gridspec_kw=dict(width_ratios=[1.4, 1]))
for i, (dt, col) in enumerate(((10, "#c0504d"), (25, "#d9822b"), (45, "#2f6fb5"))):
    ca = np.zeros_like(t)
    for tk in (0, dt):
        ca += c0 * np.exp(-(t - tk) / tau) * (t >= tk)
    a.plot(t, ca, color=col, lw=2.2, label=f"second touch at {dt} s")
    above = np.where(ca > theta)[0]
    if above.size:
        a.plot(t[above[0]], ca[above[0]], "v", color=col, ms=8)
a.axhline(theta, color="0.4", lw=1.0, ls="--")
a.text(88, theta + 0.05, "closure threshold θ", ha="right", fontsize=8.5, color="0.35")
a.set_xlabel("Time after first touch t / s")
a.set_ylabel("Cytosolic Ca²⁺ (in units of one step c₀)")
a.set_xlim(-5, 90)
a.set_ylim(0, 2.1)
a.legend(frameon=False, fontsize=8.5, loc="upper right")
a.set_title("A   Two touches: closure only if close in time", loc="left", fontsize=10)
r = np.linspace(1.02, 1.98, 300)
b.plot(r, tau * np.log(1 / (r - 1)), color="0.15", lw=2.4)
b.plot(theta, tau * np.log(1 / (theta - 1)), "o", color="#c0504d", ms=7)
b.annotate(f"θ/c₀ = {theta}: window {tau * np.log(1 / (theta - 1)):.0f} s", xy=(theta, tau * np.log(1 / (theta - 1))),
           xytext=(1.5, 70), fontsize=8.5, arrowprops=dict(arrowstyle="-", color="0.5", lw=0.8))
b.set_xlabel("Threshold relative to one step θ / c₀")
b.set_ylabel("Maximal touch interval Δt_max / s")
b.set_xlim(1, 2)
b.set_ylim(0, 120)
b.set_title("B   Δt_max = τ ln[c₀/(θ − c₀)], τ = 30 s", loc="left", fontsize=10)
for x in (a, b):
    x.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
