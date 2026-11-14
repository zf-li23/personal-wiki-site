"""Delayed-response task: trial structure with schematic prefrontal delay activity (A), and accuracy
versus delay for intact and DLPFC-lesioned animals (B): exponential decay of memory toward chance,
p(delay) = 0.5 + 0.45 exp(-delay / tau), tau = 30 s (intact) and 3 s (lesion)."""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
fig, (a, b) = plt.subplots(1, 2, figsize=(10, 3.6), gridspec_kw={"width_ratios": [1.5, 1]})
t = np.linspace(-1, 6.5, 600)
cue, delay_end = (0.0, 0.5), 4.5
pref = 4 + 26 * ((t > 0.1) & (t < 0.6)) + 14 * ((t >= 0.6) & (t < delay_end)) + 8 * ((t >= delay_end) & (t < 5.0))
nonp = 4 + 3 * ((t > 0.1) & (t < 0.6)) + 0 * t
err = 4 + 26 * ((t > 0.1) & (t < 0.6)) + 14 * np.exp(-np.clip(t - 0.6, 0, None) / 0.9) * ((t >= 0.6) & (t < delay_end))
smooth = lambda y: np.convolve(y, np.ones(15) / 15, mode="same")
for spn, lab in [((-1, 0), "fixation"), (cue, "cue"), ((0.5, delay_end), "delay"), ((delay_end, 5.2), "saccade")]:
    if lab in ("cue", "delay"):
        a.axvspan(*spn, color=P.fill("highlight" if lab == "cue" else "neutral"), alpha=0.35 if lab == "cue" else 0.25, lw=0, zorder=0)
    a.text((spn[0] + spn[1]) / 2, 33, lab, ha="center", fontsize=8, color=P.muted())
a.plot(t, smooth(pref), color=P.edge("rna"), lw=2, label="cue in memory field")
a.plot(t, smooth(nonp), color=P.muted(), lw=1.6, label="cue elsewhere")
a.plot(t, smooth(err), color=P.edge("rna"), lw=1.4, ls="--", label="error trial")
a.set_xlim(-1, 6.5); a.set_ylim(0, 36)
a.set_xlabel("Time from cue onset / s"); a.set_ylabel("Firing rate / Hz")
a.set_title("A", loc="left", fontweight="bold")
a.legend(frameon=False, fontsize=8, loc="center right")
d = np.linspace(0, 40, 200)
b.plot(d, 50 + 45 * np.exp(-d / 30), color=P.edge("positive"), lw=2, label="intact")
b.plot(d, 50 + 45 * np.exp(-d / 3), color=P.edge("negative"), lw=2, label="DLPFC lesion")
b.plot([0, 40], [93, 93], color=P.edge("negative"), lw=1.4, ls=":", label="lesion, discrimination\nwithout delay")
b.axhline(50, color=P.muted(), lw=0.8, ls="--"); b.text(1, 51.5, "chance", ha="left", fontsize=8, color=P.muted())
b.set_ylim(30, 100); b.set_xlabel("Delay / s"); b.set_ylabel("Correct choices / %")
b.set_title("B", loc="left", fontweight="bold")
b.legend(frameon=False, fontsize=7.5, loc="lower right", bbox_to_anchor=(1.0, 0.0))
for ax in (a, b):
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
fig.tight_layout()
