# Single-molecule biophysics of kinesin-1: an optical-trap bead assay (schematic, not to scale), a simulated
# stepping trace (8.2 nm steps), the dwell-time distribution of a two-step kinetic cycle, and the
# Michaelis-Menten dependence of velocity on ATP.
import numpy as np
from matplotlib.patches import Rectangle

import wikibio as bio
from wikibio import physiology as phys
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(25, 11.6)

# ---- model: each 8.2 nm step needs ATP binding (k_on [ATP]) then an ATP-independent step (k2) -----------
d = 8.2           # nm per step (tubulin dimer spacing)
k_on = 2.0        # 1/(uM s), ATP binding
k2 = 110.0        # 1/s, ATP-independent transitions (hydrolysis, release, neck-linker docking)
atp = 10.0        # uM in the trace and the histogram
k1 = k_on * atp
rng = np.random.default_rng(3)

# ---- A: bead assay -----------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 11.5))
glass_y = 1.15
ax.add_patch(Rectangle((0.4, glass_y - 0.5), 10.9, 0.5, facecolor=P.light("vacuole"), edgecolor=P.edge("vacuole"), lw=0.8, zorder=3))
bio.label(ax, (0.6, glass_y - 0.25), "Coverslip", size="tiny", ha="left", zorder=5)
trap = (6.0, 6.3)
phys.optical_trap(ax, trap, half_height=5.0, spread=2.3, token="h")
mt_y = glass_y + 0.3
bio.microtubule(ax, (0.5, mt_y), (11.2, mt_y), width=0.5)
bio.label(ax, (0.55, mt_y + 0.55), "−", size="title", ha="left", bold=True)
bio.label(ax, (11.15, mt_y + 0.55), "+", size="title", ha="right", bold=True)
bio.label(ax, (9.3, mt_y + 0.55), "Microtubule", size="small")
head_y = mt_y + 0.5
bead_c, bead_r = (trap[0] + 0.75, trap[1]), 1.7
neck = phys.kinesin(ax, (6.2, head_y), (6.95 + 0.25, head_y), (bead_c[0] - 0.1, bead_c[1] - bead_r + 0.05), head=0.62)
phys.bead(ax, bead_c, bead_r)
ax.plot([trap[0] - 0.15, trap[0] + 0.15], [trap[1], trap[1]], color=P.on_fill(), lw=1.0, zorder=14)
ax.plot([trap[0], trap[0]], [trap[1] - 0.15, trap[1] + 0.15], color=P.on_fill(), lw=1.0, zorder=14)
bio.arrow(ax, (bead_c[0] - 0.1, bead_c[1] + 0.25), (bead_c[0] - 1.3, bead_c[1] + 0.25), kind="process", lw=1.6, color=P.on_fill(), zorder=16)
bio.label(ax, (bead_c[0] - 0.75, bead_c[1] + 0.6), "$F$", size="normal", color=P.on_fill(), zorder=16)
quant.bracket(ax, (trap[0], trap[1] + bead_r + 0.45), (bead_c[0], trap[1] + bead_r + 0.45), "$\\Delta x$", side=-1)
bio.callout(ax, (trap[0] + 1.6, trap[1] + 3.6), (8.6, 10.7), "Laser beam (trap stiffness $\\kappa$)")
bio.callout(ax, (bead_c[0] + 1.2, bead_c[1] - 1.1), (9.4, 6.7), "Bead (0.5 µm)")
bio.callout(ax, neck, (4.3, 4.5), "Kinesin-1")
bio.callout(ax, (6.2 - 0.25, head_y - 0.15), (4.3, 3.2), "Motor heads")
bio.label(ax, (10.0, 8.9), "$F = -\\kappa\\,\\Delta x$", size="normal")
bio.arrow(ax, (7.8, mt_y - 0.65 + 0.0), (9.6, mt_y - 0.65), kind="process", color=P.muted(), lw=1.0, head=0.17)
bio.label(ax, (9.75, mt_y - 0.65), "8.2 nm / step", size="tiny", ha="left", zorder=5)

# ---- B: stepping trace ------------------------------------------------------------------------------
T = 1.0
dwell = rng.exponential(1 / k1, 400) + rng.exponential(1 / k2, 400)
times = np.cumsum(dwell)
times = times[times < T]
fs = 2000.0  # Hz sampling
t = np.arange(0, T, 1 / fs)
x = d * np.searchsorted(times, t)
# bead position noise: Ornstein-Uhlenbeck with a 300 Hz corner frequency and 3 nm s.d.
fc, sd = 300.0, 3.0
a = np.exp(-2 * np.pi * fc / fs)
noise = np.empty_like(t)
noise[0] = 0
e = rng.standard_normal(len(t)) * sd * np.sqrt(1 - a * a)
for i in range(1, len(t)):
    noise[i] = a * noise[i - 1] + e[i]
raw = x + noise
smooth = np.convolve(raw, np.ones(20) / 20, mode="same")
X0, W = 14.0, 10.3
pb = quant.Plot(ax, (X0, 6.6, W, 4.3), (0, 1), (-10, 170), xlabel="$t$ / s", ylabel="Position / nm",
                xticks=[0, 0.25, 0.5, 0.75, 1], yticks=[0, 40, 80, 120, 160], grid=True)
bio.panel(ax, "B", (X0 - 1.6, 11.5))
pb.line(t, raw, "neutral", lw=0.6)
pb.line(t[10:-10], smooth[10:-10], "dna", lw=1.3)
pb.steps(np.r_[0, times], d * np.arange(len(times) + 1), "negative", lw=1.0, dashed=True)
pb.legend([("bead (2 kHz)", "neutral", "-"), ("10 ms average", "dna", "-"), ("fitted steps", "negative", "--")],
          (X0 + 0.3, 10.6))
pb.text(1.0, 172, f"[ATP] = {atp:g} µM", ha="right", va="bottom", size="small")

# ---- C: dwell-time histogram ------------------------------------------------------------------------
dw = rng.exponential(1 / k1, 1500) + rng.exponential(1 / k2, 1500)
edges = np.linspace(0, 0.25, 26)
hist, _ = np.histogram(dw, edges, density=True)
tc = np.linspace(0, 0.25, 300)
pdf2 = k1 * k2 / (k2 - k1) * (np.exp(-k1 * tc) - np.exp(-k2 * tc))
mean = 1 / k1 + 1 / k2
pdf1 = np.exp(-tc / mean) / mean
pc = quant.Plot(ax, (X0, 0.95, 4.3, 3.6), (0, 0.25), (0, 18), xlabel="Dwell time / s", ylabel="Density / s$^{-1}$",
                xticks=[0, 0.1, 0.2], yticks=[0, 5, 10, 15])
bio.panel(ax, "C", (X0 - 1.6, 5.2))
pc.bars(edges, hist, "dna2", lw=0.4)
pc.line(tc, pdf1, "muted", lw=1.2, dashed=True)
pc.line(tc, pdf2, "negative", lw=1.8)
pc.text(0.1, 15.5, "two steps\n$k_1 = k_{\\mathrm{on}}[\\mathrm{ATP}]$, $k_2$", ha="left", va="center", token="negative")
pc.text(0.13, 7.0, "one step", ha="left", va="center", color=P.muted())

# ---- D: velocity against ATP (Michaelis-Menten) ----------------------------------------------------------
A = np.logspace(0, 4, 200)
v = d * k_on * A * k2 / (k_on * A + k2)
KM = k2 / k_on
pd = quant.Plot(ax, (X0 + 6.0, 0.95, 4.3, 3.6), (1, 1e4), (0, 1000), xlog=True, xlabel="[ATP] / µM",
                ylabel="$v$ / (nm s$^{-1}$)", xticks=[(1, "1"), (10, "10"), (100, "100"), (1000, "10³"), (10000, "10⁴")],
                yticks=[0, 500, 1000])
bio.panel(ax, "D", (X0 + 4.7, 5.2))
pd.line(A, v, "dna", lw=2.0)
pd.hline(d * k2, "muted", x=1.2, text="$v_{\\max} = d\\,k_2$")
pd.points([KM], [d * k2 / 2], "dna", r=0.08)
pd.text(KM * 1.35, d * k2 / 2 - 30, f"$K_{{\\mathrm{{M}}}}$ = {KM:.0f} µM", ha="left", va="top", size="tiny")
pd.points([atp], [d * k1 * k2 / (k1 + k2)], "negative", r=0.08)
pd.text(atp * 1.3, d * k1 * k2 / (k1 + k2) - 20, "trace", ha="left", va="top", token="negative")
