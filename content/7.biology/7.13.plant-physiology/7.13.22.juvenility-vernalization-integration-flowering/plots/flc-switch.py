# FLC silencing by cold as a cell-autonomous digital switch (stochastic simulation, illustrative
# parameters, after the model of Angel et al. 2011). Each of 400 cells has its FLC locus either ON
# (expression about 1, lognormal noise) or OFF (about 0.04). During cold (4 C) an ON locus switches OFF
# with probability k = 0.035 per day (Polycomb nucleation); the OFF state is inherited and stays OFF
# after the return to warm conditions (memory). For comparison an "analog" model lowers expression in
# every cell continuously at the same mean rate.
# A: population mean FLC (both models) and five single cells (digital model) over 60 d of cold and
#    20 d of warm. B: distribution of FLC expression in single cells after 20 d of cold.
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(0)
ncell, k = 400, 0.035
cold_days, warm_days = 60, 20
days = np.arange(cold_days + warm_days + 1)
on = np.ones(ncell, bool)
noise_on = np.exp(rng.normal(0, 0.25, ncell))
noise_off = 0.04 * np.exp(rng.normal(0, 0.4, ncell))
traj = np.zeros((len(days), ncell))
for i, d in enumerate(days):
    traj[i] = np.where(on, noise_on, noise_off)
    if d < cold_days:
        on &= rng.random(ncell) > k
analog = np.where(days <= cold_days, np.exp(-k * np.minimum(days, cold_days)), np.exp(-k * cold_days))
analog = 0.04 + 0.96 * analog

fig, (ax, bx) = plt.subplots(1, 2, figsize=(10.5, 4.0), gridspec_kw={"width_ratios": [1.6, 1]})
ax.axvspan(0, cold_days, color="#6fa8dc", alpha=0.15, lw=0)
ax.text(cold_days / 2, 1.42, "cold (4 °C)", ha="center", fontsize=9, color="#2f6fb5")
ax.text(cold_days + warm_days / 2, 1.42, "warm", ha="center", fontsize=9, color="#b0661c")
for j in range(5):
    ax.step(days, traj[:, j] + 0.002 * j, where="post", color="0.55", lw=0.9, alpha=0.9)
ax.plot(days, traj.mean(axis=1), color="#2f6fb5", lw=2.6, label="population mean (digital cells)")
ax.plot(days, analog, color="#d9822b", lw=1.8, ls="--", label="analog model (every cell declines)")
ax.set_xlim(0, cold_days + warm_days)
ax.set_ylim(0, 1.55)
ax.set_xlabel("Time / d")
ax.set_ylabel("FLC expression (relative)")
ax.legend(frameon=False, fontsize=8, loc="upper right", bbox_to_anchor=(1.0, 0.9))
ax.text(41, 0.62, "single cells (grey)", fontsize=8, color="0.4")

i20 = 20
bins = np.logspace(-2.2, 0.6, 30)
bx.hist(traj[i20], bins=bins, color="#2f6fb5", alpha=0.75, label="digital: 20 d cold")
bx.axvline(analog[i20], color="#d9822b", lw=2, ls="--", label="analog: all cells")
bx.set_xscale("log")
bx.set_xlabel("FLC expression per cell (relative)")
bx.set_ylabel("Number of cells")
bx.legend(frameon=False, fontsize=8, loc="upper left")
for a, letter in zip((ax, bx), "AB"):
    a.spines[["top", "right"]].set_visible(False)
    a.text(-0.12, 1.03, letter, transform=a.transAxes, fontsize=12, weight="bold")
fig.tight_layout()
