# Disk diffusion as a diffusion problem. A disk releases an amount M of drug into an agar layer of
# depth h; treated as an instantaneous point source in a thin layer, the concentration at distance r
# after time t is C = M / (4 pi D h t) * exp(-r^2 / (4 D t)). The zone edge forms at the critical time
# T0 (when the lawn becomes too dense to be stopped), where C(r, T0) equals the MIC, so the squared
# zone radius falls linearly with ln(MIC).
# Illustrative parameters: M = 30 ug, D = 5e-6 cm^2/s (0.018 cm^2/h), h = 0.4 cm, T0 = 4 h, disk 6 mm.
# A: plate with four disks (zone sizes from the model). B: concentration profiles at T0 and three MICs.
# C: zone diameter against MIC (twofold steps), simulated isolates with scatter and breakpoints.
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

import wikibio as bio
from wikibio import charts

P = bio.P
M, D, h, T0, disk = 30.0, 0.018, 0.4, 4.0, 0.6  # ug, cm^2/h, cm, h, cm (disk diameter)


def conc(r, t=T0):
    return M / (4 * np.pi * D * h * t) * np.exp(-r ** 2 / (4 * D * t))


def zone_d(mic):
    """Zone diameter in mm (the disk diameter if no zone forms)."""
    arg = M / (4 * np.pi * D * h * T0 * mic)
    r2 = 4 * D * T0 * np.log(np.maximum(arg, 1e-12))
    d = 20 * np.sqrt(np.maximum(r2, 0))
    return np.maximum(d, disk * 10)


fig = plt.figure(figsize=(13.5, 4.3))
gs = fig.add_gridspec(1, 3, width_ratios=[1, 1.15, 1.15], wspace=0.35)

# ---- A: plate ----------------------------------------------------------------------------------------------
ax = fig.add_subplot(gs[0, 0])
ax.set_xlim(-4.6, 4.6)
ax.set_ylim(-4.6, 4.6)
ax.set_aspect("equal")
ax.axis("off")
charts.title(ax, "A   Plate after incubation")
lawn = P.mix(P.fill("bacterium"), P.surface(), 0.25)
ax.add_patch(Circle((0, 0), 4.4, facecolor=P.mix(P.fill("neutral"), P.surface(), 0.6), edgecolor=P.muted(), lw=1.2))
ax.add_patch(Circle((0, 0), 4.1, facecolor=lawn, edgecolor="none"))
agar = P.mix(P.fill("metabolite"), P.surface(), 0.75)
for (x, y), mic, lab in [((-1.9, 1.9), 0.25, "0.25"), ((1.9, 1.9), 2, "2"), ((-1.9, -1.9), 16, "16"), ((1.9, -1.9), 128, "128")]:
    d = zone_d(mic) / 10  # cm
    ax.add_patch(Circle((x, y), d / 2, facecolor=agar, edgecolor="none"))
    ax.add_patch(Circle((x, y), disk / 2, facecolor=P.surface(), edgecolor=P.muted(), lw=0.8))
    ax.text(x, y - d / 2 - 0.15, f"MIC {lab}", ha="center", va="top", fontsize=7, color=P.on_fill())
ax.text(0, -4.55, "zone diameter grows as MIC falls", ha="center", va="top", fontsize=7, color=P.muted())

# ---- B: profiles -------------------------------------------------------------------------------------------
ax = fig.add_subplot(gs[0, 1])
r = np.linspace(0.3, 2.0, 300)
for t, ls in ((1.0, ":"), (T0, "-"), (12.0, "--")):
    ax.plot(r * 10, conc(r, t), color=charts.line("drug"), lw=1.8 if t == T0 else 1.1, ls=ls,
            label=f"t = {t:g} h" + (" (T$_0$)" if t == T0 else ""))
for mic, tok in ((0.25, "positive"), (2, "highlight"), (16, "negative")):
    ax.axhline(mic, color=charts.line(tok), lw=0.9)
    rz = zone_d(mic) / 20
    ax.plot([rz * 10], [mic], "o", color=charts.line(tok), ms=5)
    ax.text(19.6, mic * 1.15, f"MIC = {mic:g}", ha="right", va="bottom", fontsize=7, color=charts.line(tok))
ax.set_yscale("log")
ax.set_ylim(0.05, 200)
ax.set_xlim(3, 20)
ax.legend(fontsize=7, frameon=False, loc="lower left", labelcolor=P.ink())
charts.style_axes(ax, "distance from disk center / mm", "drug concentration / ($\\mu$g mL$^{-1}$)")
charts.title(ax, "B   Gradient at the critical time")

# ---- C: zone diameter vs MIC -------------------------------------------------------------------------------
ax = fig.add_subplot(gs[0, 2])
rng = np.random.default_rng(0)
mics = 2.0 ** np.arange(-4, 8)
counts = [6, 14, 22, 18, 9, 4, 3, 5, 9, 12, 8, 4]  # a bimodal population: wild type and resistant isolates
for m, n in zip(mics, counts):
    dd = zone_d(m) + rng.normal(0, 1.3, n)
    dd = np.maximum(dd, 6)
    ax.plot(np.log2(m) + rng.uniform(-0.18, 0.18, n), dd, "o", ms=3.2, color=charts.line("bacterium"), alpha=0.8, mew=0)
mm = 2.0 ** np.linspace(-4.5, 7.5, 200)
ax.plot(np.log2(mm), zone_d(mm), color=P.ink(), lw=1.3, label="model")
S_mic, R_mic = 2, 8
ax.axvspan(-5, np.log2(S_mic) + 0.5, color=P.mix(P.fill("positive"), P.surface(), 0.75), lw=0, zorder=0)
ax.axvspan(np.log2(R_mic) - 0.5, 8, color=P.mix(P.fill("negative"), P.surface(), 0.75), lw=0, zorder=0)
ax.axhline(zone_d(S_mic + 0.5), color=P.muted(), lw=0.7, ls="--")
ax.axhline(zone_d(R_mic - 1), color=P.muted(), lw=0.7, ls="--")
ax.text(-4.3, 7.0, "S", fontsize=9, color=charts.line("positive"), weight="bold")
ax.text(2.0, 7.0, "I", fontsize=9, color=P.muted(), weight="bold")
ax.text(6.8, 31.0, "R", fontsize=9, color=charts.line("negative"), weight="bold")
ax.set_xticks(np.arange(-4, 8))
ax.set_xticklabels([f"{2.0 ** k:g}" for k in range(-4, 8)], rotation=60)
ax.set_xlim(-4.6, 7.6)
ax.set_ylim(5, 34)
charts.style_axes(ax, "MIC / ($\\mu$g mL$^{-1}$), twofold steps", "zone diameter / mm")
charts.title(ax, "C   Zone diameter against MIC")
