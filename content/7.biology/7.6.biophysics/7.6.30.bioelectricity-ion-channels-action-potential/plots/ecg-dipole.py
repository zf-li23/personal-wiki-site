"""The electrocardiogram as the projection of the heart's electric dipole. A: a synthetic
vectorcardiogram in the frontal plane: the tip of the cardiac dipole moment traces a small P loop
(atrial depolarization), a large QRS loop (ventricular depolarization, mean axis about +60 degrees,
pointing down and to the left) and a T loop (repolarization), with the axes of Einthoven's limb leads
I (0 degrees), II (+60) and III (+120). B: the potential difference recorded by each lead is the
projection of the dipole on its axis; the three traces satisfy Einthoven's law II = I + III at every
instant (dotted: I + III, on top of II). Synthetic dipole, one beat of 0.8 s (75 beats per minute)."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 2, figsize=(9.0, 3.4), gridspec_kw=dict(width_ratios=[0.8, 1.4]))
fig.subplots_adjust(wspace=0.25, left=0.04, right=0.98, bottom=0.17, top=0.87)

t = np.linspace(0, 0.8, 1600)


def wave(t0, w, amp, ang0, ang1):
    s = np.exp(-0.5 * ((t - t0) / w) ** 2) * amp
    ang = np.deg2rad(ang0 + (ang1 - ang0) * (1 / (1 + np.exp(-(t - t0) / (w / 2)))))
    return s * np.cos(ang), s * np.sin(ang)


px, py = np.zeros_like(t), np.zeros_like(t)
for args in [(0.10, 0.025, 0.15, 30, 70), (0.25, 0.012, 0.35, 120, 160), (0.27, 0.013, 1.3, 20, 70),
             (0.29, 0.012, 0.3, -90, -110), (0.52, 0.045, 0.35, 40, 60)]:
    x, y = wave(*args)
    px += x
    py += y

ax = axs[0]
ax.plot(px, py, color=charts.line("blood"), lw=1.4)
for ang, lab in [(0, "I"), (60, "II"), (120, "III")]:
    a = np.deg2rad(ang)
    ax.annotate("", (1.25 * np.cos(a), 1.25 * np.sin(a)), (0, 0),
                arrowprops=dict(arrowstyle="->", color=P.muted(), lw=0.9))
    ax.text(1.38 * np.cos(a), 1.38 * np.sin(a), lab, fontsize=FT["small"], color=P.ink(), ha="center", va="center")
ax.set_xlim(-0.8, 1.6)
ax.set_ylim(1.6, -0.8)  # downward positive, as in the hexaxial reference system
ax.set_aspect("equal")
ax.text(-0.75, -0.65, "subject's left →", fontsize=FT["tiny"], color=P.muted())
ax.text(-0.75, 1.5, "feet ↓", fontsize=FT["tiny"], color=P.muted())
ax.set_xticks([]); ax.set_yticks([])
for sp in ax.spines.values():
    sp.set_visible(False)
charts.title(ax, "A  Frontal-plane dipole loop")

ax = axs[1]
leads = {}
for k, (ang, lab, tok) in enumerate([(0, "I", "dna"), (60, "II", "blood"), (120, "III", "bacterium")]):
    a = np.deg2rad(ang)
    leads[lab] = px * np.cos(a) + py * np.sin(a)
    ax.plot(t, leads[lab] - 1.6 * k, color=charts.line(tok), lw=1.3)
    ax.text(-0.04, -1.6 * k, lab, fontsize=FT["small"], color=P.ink(), ha="right", va="center")
ax.plot(t, leads["I"] + leads["III"] - 1.6, ":", color=P.ink(), lw=1.0)
for lab, tt in [("P", 0.10), ("QRS", 0.27), ("T", 0.52)]:
    ax.text(tt, 1.45, lab, fontsize=FT["tiny"], color=P.ink(), ha="center")
ax.set_ylim(-4.3, 1.7)
ax.set_yticks([])
charts.style_axes(ax, "time / s", None)
ax.spines["left"].set_visible(False)
charts.title(ax, "B  Limb leads (Einthoven's law II = I + III)")
