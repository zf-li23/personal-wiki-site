# The zigzag model of plant immunity (Jones and Dangl 2006), drawn as a schematic time course of the
# amplitude of the defence response against two thresholds: the threshold for effective resistance and
# the (higher) threshold for the hypersensitive response (HR). Phase 1: PAMPs -> PTI. Phase 2: effectors
# -> effector-triggered susceptibility (ETS). Phase 3: an NLR recognises an effector -> ETI, often with HR.
# Phase 4: the pathogen loses the recognised effector or gains new effectors -> ETS again; selection then
# favours new NLR alleles -> ETI again.
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(11.5, 4.6))
xs = [0, 1, 2, 3, 4, 5, 6, 7]
ys = [0.0, 0.42, 0.12, 0.82, 0.10, 0.92, 0.20, 0.0]
ax.plot(xs[:7], ys[:7], color="black", lw=2.4, marker="o", ms=5)
ax.axhline(0.30, color="#2e9e5b", lw=1.2, ls="--")
ax.axhline(0.70, color="#d9463b", lw=1.2, ls="--")
ax.text(7.75, 0.315, "threshold for\neffective resistance", va="bottom", ha="right", fontsize=9, color="#2e9e5b")
ax.text(7.75, 0.715, "threshold for HR", ha="right", fontsize=9, color="#d9463b")
lab = [
    (0.5, 0.25, "PAMPs\nrecognised by PRRs", "PTI"),
    (1.5, 0.30, "effector A\nsuppresses PTI", "ETS"),
    (2.5, 0.50, "NLR-1 recognises\neffector A", "ETI"),
    (3.5, 0.50, "pathogen loses A,\ngains effector B", "ETS"),
    (4.5, 0.55, "NLR-2 recognises\neffector B", "ETI"),
    (5.5, 0.60, "effector C\nescapes recognition", "ETS"),
]
for x, y, t, ph in lab:
    ax.text(x, -0.2, t, ha="center", va="top", fontsize=8.5)
for x0, ph, c in [(1, "PTI", "#2e9e5b"), (2, "ETS", "#8a94a3"), (3, "ETI", "#d9463b"), (4, "ETS", "#8a94a3"),
                  (5, "ETI", "#d9463b"), (6, "ETS", "#8a94a3")]:
    dy = 0.05 if ph != "ETS" else -0.09
    ax.text(x0, ys[x0] + dy, ph, ha="center", fontsize=10, color=c, fontweight="bold")
ax.annotate("", xy=(6.9, -0.42), xytext=(0.1, -0.42), arrowprops=dict(arrowstyle="->", color="0.4"),
            annotation_clip=False)
ax.text(3.5, -0.47, "time and evolutionary rounds of the host-pathogen interaction", ha="center", va="top",
        fontsize=8.5, color="0.4")
ax.set_xlim(-0.1, 7.8)
ax.set_ylim(-0.55, 1.05)
ax.set_xticks([])
ax.set_ylabel("Amplitude of defence (arbitrary units)")
ax.spines[["top", "right", "bottom"]].set_visible(False)
ax.set_yticks([0, 0.5, 1.0])
fig.tight_layout()
