"""Spike timing selects the escape mode of Drosophila (after von Reyn et al. 2014).

A dark disk looms toward the fly with half-size-to-speed ratio l/|v|. A parallel, non-giant-fiber
pathway starts a long-mode takeoff (wings raised before the legs extend; slower but stable) when
the image reaches about 20 deg; the takeoff is completed 15 ms (s.d. 4) later. The giant fiber (GF)
fires a single spike when its input, driven mainly by the angular velocity of expansion, crosses
threshold (with trial-to-trial variability). If the GF spike comes before the long-mode takeoff is
completed, it triggers the fast short-mode jump (wings not raised; the fly often tumbles).
Values are illustrative.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(2)
t = np.linspace(-3.0, -0.0005, 60000)


def trial(r):
    th = 2 * np.degrees(np.arctan(r / np.abs(t)))
    dth = np.gradient(th, t) / 1000.0  # deg per ms
    t_long = t[np.argmax(th > 20)] * 1e3 + rng.normal(15, 4)
    thr = np.exp(rng.normal(np.log(0.1), 0.8))  # GF threshold on angular velocity, deg/ms
    idx = np.argmax(dth > thr)
    t_gf = t[idx] * 1e3 + 1.0 if dth[idx] > thr else np.inf
    return t_gf < t_long, t_gf, t_long


ratios = np.array([10, 20, 40, 80, 160, 320]) / 1000
fig, (a, b) = plt.subplots(1, 2, figsize=(10.5, 3.8))
frac = []
for r in ratios:
    res = [trial(r)[0] for _ in range(300)]
    frac.append(np.mean(res))
a.plot(ratios * 1e3, frac, "o-", color=P.edge("negative"), lw=2)
a.set_xscale("log")
a.set_xticks(ratios * 1e3); a.set_xticklabels([f"{x:.0f}" for x in ratios * 1e3])
a.set_ylim(-0.03, 1.03)
a.set_xlabel("l/|v| of the looming disk / ms  (fast → slow)")
a.set_ylabel("Fraction of short-mode takeoffs")
a.set_title("A", loc="left", fontweight="bold")
for r, col in ((0.02, P.edge("negative")), (0.16, P.edge("dna"))):
    th = 2 * np.degrees(np.arctan(r / np.abs(t)))
    dth = np.gradient(th, t) / 1000.0
    m = t > -6 * r - 0.05
    b.plot(t[m] * 1e3, dth[m], color=col, lw=1.8, label=f"l/|v| = {r * 1e3:.0f} ms")
    tl = t[np.argmax(th > 20)] * 1e3
    b.plot([tl, tl + 15], [0.75 if r < 0.1 else 0.68] * 2, color=col, lw=4, solid_capstyle="butt")
b.axhline(0.1, color=P.muted(), ls="--", lw=0.9)
b.text(-950, 0.115, "median GF threshold", fontsize=7.5, color=P.muted())
b.text(-950, 0.79, "bars: long-mode takeoff from initiation to completion", fontsize=7.5, color=P.muted())
b.set_xlim(-1000, 0)
b.set_ylim(0, 0.85)
b.set_xlabel("Time to collision / ms")
b.set_ylabel("Angular velocity / deg ms$^{-1}$")
b.legend(frameon=False, fontsize=8, loc="upper left", bbox_to_anchor=(0, 0.9))
b.set_title("B", loc="left", fontweight="bold")
for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
