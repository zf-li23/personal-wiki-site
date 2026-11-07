# Astronomical day length (sunrise to sunset, sun's upper limb with refraction: h0 = -0.833 deg)
# at three latitudes in China, from cos H0 = (sin h0 - sin(phi) sin(delta)) / (cos(phi) cos(delta)),
# N = 2 H0 / 15 h, with the solar declination delta = -23.44 cos(360 (d + 10) / 365) deg.
# Left: annual course; the dashed line is a critical day length of 13.5 h (an SDP such as soybean);
# dots mark the date after the summer solstice when the day becomes shorter than it.
# Right: longest and shortest day as a function of latitude.
import matplotlib.pyplot as plt
import numpy as np


def declination(d):
    return -23.44 * np.cos(np.radians(360.0 / 365.0 * (d + 10)))


def day_length(phi, d, h0=-0.833):
    p, de = np.radians(phi), np.radians(declination(d))
    c = (np.sin(np.radians(h0)) - np.sin(p) * np.sin(de)) / (np.cos(p) * np.cos(de))
    return 2 * np.degrees(np.arccos(np.clip(c, -1, 1))) / 15.0


days = np.arange(1, 366)
sites = [("Harbin 45.8° N", 45.8, "#2f6fb5"), ("Beijing 39.9° N", 39.9, "#d9822b"),
         ("Haikou 20.0° N", 20.0, "#3a9a5b")]
crit = 13.5

fig, (ax, bx) = plt.subplots(1, 2, figsize=(10.5, 4.3), gridspec_kw={"width_ratios": [1.7, 1]})
for name, phi, col in sites:
    n = day_length(phi, days)
    ax.plot(days, n, color=col, lw=2, label=name)
    after = np.where((days > 172) & (n < crit))[0]
    if len(after) and n.max() > crit:
        k = after[0]
        ax.plot(days[k], n[k], "o", color=col, ms=6, zorder=5)
ax.axhline(crit, color="0.35", lw=1, ls="--")
ax.text(4, crit + 0.15, "critical day length 13.5 h", fontsize=8, color="0.3")
for d, lab in [(80, "Mar\nequinox"), (172, "Jun\nsolstice"), (266, "Sep\nequinox"), (355, "Dec\nsolstice")]:
    ax.axvline(d, color="0.75", lw=0.7, zorder=0)
    ax.text(d, 8.05, lab, fontsize=7, ha="center", va="bottom", color="0.4")
ax.set_xlim(1, 365)
ax.set_ylim(8, 16.5)
ax.set_xticks([1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335])
ax.set_xticklabels(list("JFMAMJJASOND"))
ax.set_xlabel("Month")
ax.set_ylabel("Day length / h")
ax.legend(frameon=False, fontsize=8, loc="upper left", bbox_to_anchor=(0.0, 0.93))
ax.spines[["top", "right"]].set_visible(False)

lat = np.linspace(0, 66, 200)
bx.plot(lat, day_length(lat, 172), color="#d9822b", lw=2, label="June solstice")
bx.plot(lat, day_length(lat, 355), color="#2f6fb5", lw=2, label="December solstice")
bx.plot(lat, day_length(lat, 80), color="0.4", lw=1.2, ls=":", label="equinox")
for _, phi, col in sites:
    bx.axvline(phi, color="0.8", lw=0.7, zorder=0)
bx.set_xlabel("Latitude / ° N")
bx.set_ylabel("Day length / h")
bx.set_xlim(0, 66)
bx.set_ylim(0, 24)
bx.set_yticks([0, 6, 12, 18, 24])
bx.legend(frameon=False, fontsize=8, loc="upper left")
bx.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
