# Walter-Lieth climate diagrams for two illustrative climates (rounded monthly values chosen to resemble a
# continental monsoon climate of northern China and a Mediterranean climate; not station records).
# Temperature (red, left axis) and precipitation (blue, right axis) are scaled so that 10 C corresponds to
# 20 mm; where the precipitation curve lies above the temperature curve the month is humid (blue fill),
# where it lies below the month is arid (yellow fill). Precipitation above 100 mm is drawn at 1/10 scale
# (dark blue), as in Walter's convention.
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio

P = bio.P
months = np.arange(1, 13)
climates = [
    ("A  Continental monsoon (illustrative)",
     [-3, 0, 7, 15, 21, 25, 27, 25, 21, 14, 5, -1], [3, 5, 8, 21, 34, 78, 185, 160, 46, 22, 7, 3]),
    ("B  Mediterranean (illustrative)",
     [8, 9, 11, 14, 18, 22, 25, 25, 22, 17, 12, 9], [70, 65, 60, 60, 40, 20, 10, 25, 70, 110, 110, 85]),
]


def scaled(p):
    p = np.asarray(p, float)
    return np.where(p <= 100, p / 2, 50 + (p - 100) / 20)


fig, axs = plt.subplots(1, 2, figsize=(10.6, 4.4))
for ax, (title, T, Pm) in zip(axs, climates):
    T = np.array(T, float)
    x = np.linspace(1, 12, 221)
    Ti = np.interp(x, months, T)
    Pi = np.interp(x, months, scaled(Pm))
    ax.fill_between(x, Ti, np.minimum(Pi, 50), where=np.minimum(Pi, 50) > Ti, color=P.fill("dna"), lw=0,
                    interpolate=True)
    ax.fill_between(x, 50, Pi, where=Pi > 50, color=P.edge("dna"), lw=0, interpolate=True)
    ax.fill_between(x, Pi, Ti, where=Ti > Pi, color=P.fill("highlight"), lw=0, interpolate=True)
    ax.plot(x, Ti, color=P.edge("negative"), lw=2)
    ax.plot(x, Pi, color=P.edge("dna"), lw=2)
    ax.axhline(0, color=P.muted(), lw=0.6)
    ax.set_xlim(1, 12)
    ax.set_xticks(months)
    ax.set_xticklabels(list("JFMAMJJASOND"))
    ax.set_ylim(-10, 70)
    ax.set_ylabel("Temperature / °C", color=P.edge("negative"))
    ax2 = ax.twinx()
    ax2.set_ylim(-20, 140)
    ax2.set_yticks([0, 20, 40, 60, 80, 100, 120, 140])
    ax2.set_yticklabels(["0", "20", "40", "60", "80", "100", "300", "500"])
    ax2.set_ylabel("Precipitation / mm", color=P.edge("dna"))
    ax.text(1.3, 64, "mean %.1f °C, %d mm per year" % (T.mean(), sum(Pm)), fontsize=8, color=P.ink())
    ax.set_title(title, loc="left", fontsize=10, fontweight="bold")
    for s in ("top",):
        ax.spines[s].set_visible(False)
        ax2.spines[s].set_visible(False)
fig.tight_layout()
