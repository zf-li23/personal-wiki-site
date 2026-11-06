# Triphasic water uptake and respiration of a germinating seed (a phenomenological model with illustrative
# parameters, after Bewley et al. and Taiz et al. 6e, Fig. 18.8). Water content (g water per g dry
# weight): phase I, imbibition driven by the matric potential, approaches a plateau exponentially; phase II,
# little uptake while metabolism restarts; phase III, after radicle emergence (t_r = 30 h), growth-driven
# uptake. A dead seed imbibes (phase I) but never enters phase III. Respiration (O2 uptake, relative):
# a rise in phase I as hydrated mitochondria resume, a lag in phase II, and a second rise in phase III as
# new mitochondria form and the radicle pierces the coat.
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 60, 601)
tr = 30.0
w1 = 0.08 + 0.72 * (1 - np.exp(-t / 3.5))
w2 = 0.06 * np.clip(t - 6, 0, None) / 24
w3 = 1.6 / (1 + np.exp(-(t - tr - 9) / 4.0)) * (t > tr) * (1 - np.exp(-np.clip(t - tr, 0, None) / 3))
water = w1 + np.minimum(w2, 0.06) + w3
dead = w1
resp = 0.9 * (1 - np.exp(-t / 3)) + 0.15 * np.clip(t - 6, 0, 20) / 20 + 2.2 / (1 + np.exp(-(t - tr - 6) / 3.5))
fig, (a, b) = plt.subplots(2, 1, figsize=(8.5, 6.4), sharex=True)
for x in (a, b):
    for x0, x1, name in ((0, 7, "I"), (7, tr, "II"), (tr, 60, "III")):
        x.axvspan(x0, x1, color=("#e8eef7", "#f7f1e1", "#e7f3e9")["I II III".split().index(name)], lw=0, alpha=0.7)
a.plot(t, water, color="#2f6fb5", lw=2.4, label="viable seed")
a.plot(t, dead, color="0.5", lw=1.8, ls="--", label="dead seed (imbibes only)")
a.axvline(tr, color="#c0504d", lw=1, ls=":")
a.text(tr + 0.5, 2.45, "radicle emergence\n(end of germination)", fontsize=8.5, color="#c0504d", va="top")
for x0, x1, name in ((0, 7, "Phase I\nimbibition"), (7, tr, "Phase II\nlag: metabolism restarts"), (tr, 60, "Phase III\ngrowth")):
    a.text((x0 + x1) / 2, 2.0 if name.startswith("Phase I\n") else 1.55, name, ha="center", fontsize=8.5, color="0.3")
a.set_ylabel("Water content / g g⁻¹ dry mass")
a.set_ylim(0, 2.6)
a.legend(frameon=False, fontsize=8.5, loc="center right")
a.set_title("A   Water uptake", loc="left", fontsize=10)
b.plot(t, resp, color="#c0504d", lw=2.4)
b.axvline(tr, color="#c0504d", lw=1, ls=":")
b.set_xlabel("Time after the start of imbibition t / h")
b.set_ylabel("O₂ uptake (relative)")
b.set_ylim(0, 3.6)
b.set_xlim(0, 60)
b.set_title("B   Respiration", loc="left", fontsize=10)
for x in (a, b):
    x.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
