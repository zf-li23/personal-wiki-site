# Growth and maintenance respiration (McCree 1970).
# (A) Simulated daily respiration R and gross photosynthesis P of plants under different light levels, both
# per unit dry mass W: R/W = k (P/W) + c with k = 0.25, c = 0.015 d^-1, plus 8 % multiplicative noise
# (seed 0); an ordinary least-squares fit recovers k (slope) and c (intercept).
# (B) A plant growing logistically over 60 days: growth respiration (1 - YG)/YG dW/dt with YG = 0.8 and
# maintenance respiration m W with m = 0.015 d^-1.
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(0)
k, c = 0.25, 0.015
pw = rng.uniform(0.02, 0.32, 40)
rw = (k * pw + c) * (1 + 0.08 * rng.standard_normal(40))
slope, icpt = np.polyfit(pw, rw, 1)

t = np.linspace(0, 60, 400)
Wmax, r0, W0 = 50.0, 0.15, 0.5
W = Wmax / (1 + (Wmax / W0 - 1) * np.exp(-r0 * t))
dW = r0 * W * (1 - W / Wmax)
YG, mm = 0.8, 0.015
Rg = (1 - YG) / YG * dW
Rm = mm * W

fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.2))
a.plot(pw, rw, "o", color="#2f6fb5", ms=5, alpha=0.85, label="simulated plants")
xx = np.linspace(0, 0.34, 10)
a.plot(xx, slope * xx + icpt, color="#c0504d", lw=2, label=f"fit: k = {slope:.3f}, c = {icpt:.4f} d⁻¹")
a.set_xlabel("P / W (gross photosynthesis per dry mass) / d⁻¹")
a.set_ylabel("R / W / d⁻¹")
a.set_xlim(0, 0.34)
a.set_ylim(0, 0.11)
a.legend(frameon=False, fontsize=9, loc="upper left")
a.set_title("A   McCree regression", loc="left", fontsize=10)
b.stackplot(t, Rg, Rm, colors=["#7fb77e", "#e0a35a"], labels=["growth respiration", "maintenance respiration"],
            alpha=0.85)
b.set_xlabel("Time / d")
b.set_ylabel("Respiration / (g dry mass d⁻¹)")
b.set_xlim(0, 60)
b.legend(frameon=False, fontsize=9, loc="upper left")
b.set_title("B   Components during growth", loc="left", fontsize=10)
b2 = b.twinx()
b2.plot(t, W, color="0.35", lw=1.2, ls="--")
b2.set_ylabel("Dry mass W / g", color="0.35")
for ax in (a, b):
    ax.spines["top"].set_visible(False)
a.spines["right"].set_visible(False)
fig.tight_layout()
