# Hormonal control of abscission (illustrative models).
# A: Addicott's auxin-gradient hypothesis as a dose-response: the probability that an organ is shed
#    falls with the ratio r of auxin on the distal (organ) side to the proximal (stem) side of the
#    abscission zone, p = 1 / (1 + (r / r50)^h), r50 = 1, h = 3: shedding is likely when r <= 1 and
#    unlikely when r >> 1.
# B: break strength of the abscission zone of leaf explants after an ethylene treatment (10 uL L^-1)
#    given at t = 0. After a lag, cells of the separation layer become competent and secrete
#    cell-wall hydrolases; the force needed to break the zone decays exponentially,
#    F(t) = Fmin + (F0 - Fmin) exp(-k (t - lag)) for t > lag. Auxin applied to the distal side extends
#    the lag and slows the decay; with no ethylene the zone stays strong for longer.
import matplotlib.pyplot as plt
import numpy as np

fig, (ax, bx) = plt.subplots(1, 2, figsize=(11, 4.0))
r = np.logspace(-1.5, 1.5, 400)
p = 1 / (1 + r**3)
ax.plot(r, 100 * p, color="#d9822b", lw=2.2)
ax.axvline(1, color="0.5", lw=0.8, ls=":")
ax.set_xscale("log")
ax.set_xlabel("Auxin ratio, distal / proximal")
ax.set_ylabel("Organs shed / %")
ax.set_ylim(0, 105)
ax.text(0.06, 50, "low auxin from the\nleaf (senescence):\nabscission", fontsize=8, color="0.35")
ax.text(2.2, 50, "young leaf,\nhigh auxin:\nretained", fontsize=8, color="0.35")

t = np.linspace(0, 72, 500)


def force(lag, k, F0=100.0, Fmin=3.0):
    return np.where(t < lag, F0, Fmin + (F0 - Fmin) * np.exp(-k * (t - lag)))


bx.plot(t, force(8, 0.12), color="#d93a2b", lw=2.2, label="ethylene")
bx.plot(t, force(24, 0.06), color="#2f6fb5", lw=2.2, ls="--", label="ethylene + auxin (distal)")
bx.plot(t, force(40, 0.03), color="0.45", lw=1.6, ls=":", label="air (aging only)")
bx.set_xlabel("Time after treatment / h")
bx.set_ylabel("Break strength (% of initial)")
bx.set_xlim(0, 72)
bx.set_ylim(0, 108)
bx.legend(frameon=False, fontsize=8, ncol=3, loc="upper center", bbox_to_anchor=(0.5, 1.14))
for a, letter in zip((ax, bx), "AB"):
    a.spines[["top", "right"]].set_visible(False)
    a.text(-0.13, 1.03, letter, transform=a.transAxes, fontsize=12, weight="bold")
fig.tight_layout()
