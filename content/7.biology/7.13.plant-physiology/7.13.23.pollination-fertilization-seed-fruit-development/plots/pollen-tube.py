# Tip growth of the pollen tube.
# A: tip-focused gradient of cytosolic Ca2+ (about 3 uM at the extreme tip, falling to a basal 0.2 uM
#    within about 20 um; exponential profile with a decay length of 5 um) and the pH profile (slightly
#    acidic tip, alkaline band at the base of the clear zone), after the values quoted by Taiz et al.
# B: oscillatory growth from a minimal delayed negative-feedback model (illustrative parameters):
#    active ROP GTPase R promotes growth, v = v0 + g R; growth opens Ca2+ channels with a delay tau,
#    and tip Ca2+ C inhibits ROP activity:
#      dR/dt = 1 / (1 + (C/K)^8) - b R,   dC/dt = s v(t - tau) - d C
#    with tau = 4 s, b = 0.2 /s, d = 0.5 /s. Growth rate and tip Ca2+ oscillate with the same period
#    (about 18 s here), and the Ca2+ peak lags behind the growth peak by several seconds.
import matplotlib.pyplot as plt
import numpy as np

fig, (ax, bx) = plt.subplots(1, 2, figsize=(11, 4.0), gridspec_kw={"width_ratios": [1, 1.5]})
x = np.linspace(0, 40, 400)
ca = 0.2 + 2.8 * np.exp(-x / 5.0)
ph = 6.8 + 0.55 * np.exp(-((x - 12) / 5) ** 2) + 0.25 * (1 - np.exp(-x / 8))
ax.plot(x, ca, color="#d93a2b", lw=2.2, label="cytosolic Ca²⁺")
ax.set_xlabel("Distance from the tip / μm")
ax.set_ylabel("[Ca²⁺] / μM", color="#b0302a")
ax.set_xlim(0, 40)
ax.set_ylim(0, 3.3)
ax.axvspan(0, 15, color="0.6", alpha=0.12, lw=0)
ax.text(7.5, 3.1, "clear zone", ha="center", fontsize=8, color="0.35")
ax2 = ax.twinx()
ax2.plot(x, ph, color="#2f6fb5", lw=1.8, ls="--")
ax2.set_ylabel("Cytosolic pH", color="#2f6fb5")
ax2.set_ylim(6.6, 7.8)
ax.spines["top"].set_visible(False)
ax2.spines["top"].set_visible(False)

dt, T = 0.01, 400.0
n, lag = int(T / dt), int(4.0 / dt)
v0, g, s, b, d, K = 0.1, 0.12, 0.6, 0.2, 0.5, 1.0
R, C, v = np.zeros(n), np.zeros(n), np.zeros(n)
R[0], C[0] = 1.0, 0.2
for i in range(n - 1):
    v[i] = v0 + g * R[i]
    vd = v[i - lag] if i >= lag else v0
    R[i + 1] = R[i] + dt * (1.0 / (1 + (C[i] / K) ** 8) - b * R[i])
    C[i + 1] = C[i] + dt * (s * vd / 0.2 - d * C[i])
v[-1] = v[-2]
t = np.arange(n) * dt
sel = (t > 300) & (t < 380)
tt = t[sel] - 300
bx.plot(tt, v[sel], color="#3a9a5b", lw=2.2, label="growth rate")
bx.set_xlabel("Time / s")
bx.set_ylabel("Growth rate / (μm s⁻¹)", color="#2e7d4a")
bx.set_xlim(0, 80)
bx3 = bx.twinx()
bx3.plot(tt, C[sel], color="#d93a2b", lw=1.8, ls="--", label="tip Ca²⁺")
bx3.set_ylabel("Tip [Ca²⁺] (relative)", color="#b0302a")
vs, cs = v[sel], C[sel]
i1 = np.argmax(vs[: int(25 / dt)])
j1 = i1 + np.argmax(cs[i1: i1 + int(15 / dt)])
bx.axvline(tt[i1], color="#3a9a5b", lw=0.8, ls=":")
bx3.axvline(tt[j1], color="#d93a2b", lw=0.8, ls=":")
bx3.annotate("", (tt[j1], cs.max() * 1.06), (tt[i1], cs.max() * 1.06),
             arrowprops=dict(arrowstyle="->", color="0.3", lw=0.9))
bx3.text((tt[i1] + tt[j1]) / 2, cs.max() * 1.09, f"lag {tt[j1] - tt[i1]:.0f} s", ha="center", fontsize=8)
bx3.set_ylim(cs.min() * 0.8, cs.max() * 1.18)
h1, l1 = bx.get_legend_handles_labels()
h2, l2 = bx3.get_legend_handles_labels()
bx.legend(h1 + h2, l1 + l2, frameon=False, fontsize=8, ncol=2, loc="upper right", bbox_to_anchor=(1.0, 1.13))
bx.spines["top"].set_visible(False)
bx3.spines["top"].set_visible(False)
for a, letter in zip((ax, bx), "AB"):
    a.text(-0.16 if a is ax else -0.1, 1.03, letter, transform=a.transAxes, fontsize=12, weight="bold")
fig.tight_layout()
