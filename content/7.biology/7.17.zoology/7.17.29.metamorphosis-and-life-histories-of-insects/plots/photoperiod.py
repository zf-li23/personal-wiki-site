# Photoperiodic induction of diapause (illustrative parameters).
# A: logistic photoperiodic response curves of a long-day insect from 35, 45 and 55 N (critical photoperiods
#    13.5, 15.5, 17.5 h; slope such that the response goes from 10% to 90% over about 1.5 h).
# B: day length including civil twilight (sun altitude above -6 degrees) through the year at the three
#    latitudes, from the solar declination; dots mark where day length falls below each population's
#    critical photoperiod in late summer.
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(25, 11)
pops = [(35, 13.5, "positive"), (45, 15.5, "enzyme"), (55, 17.5, "negative")]
s = 1.5 / (2 * np.log(9))  # 10-90% width 1.5 h

pA = quant.Plot(ax, (2.2, 1.7, 8.6, 7.6), xlim=(10, 20), ylim=(0, 100), xlabel="Day length / h",
                ylabel="Entering diapause / %", xticks=[10, 12, 14, 16, 18, 20], yticks=[0, 25, 50, 75, 100])
L = np.linspace(10, 20, 400)
pA.hline(50, token="muted", dashed=True, lw=0.6)
for lat, cp, tok in pops:
    y = 100 / (1 + np.exp((L - cp) / s))
    pA.line(L, y, tok, lw=1.6)
    pA.text(cp + 0.15, 55, "%d°N: %.1f h" % (lat, cp), token=tok, ha="left", rotation=0)
pA.text(10.2, 8, "long days: development", ha="left")
pA.text(10.2, 80, "short days: diapause", ha="left")
bio.label(ax, (6.5, 10.3), "A  Photoperiodic response curves", size="small", bold=True)


def daylength(lat, n, alt=-6.0):
    d = np.radians(23.44) * np.sin(2 * np.pi * (284 + n) / 365)
    p = np.radians(lat)
    c = (np.sin(np.radians(alt)) - np.sin(p) * np.sin(d)) / (np.cos(p) * np.cos(d))
    return 24 / np.pi * np.arccos(np.clip(c, -1, 1))


n = np.arange(1, 366)
months = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
pB = quant.Plot(ax, (14.2, 1.7, 9.6, 7.6), xlim=(1, 365), ylim=(8, 20), xlabel="Month",
                ylabel="Day length incl. civil twilight / h",
                xticks=[(m + 15, "JFMAMJJASOND"[k]) for k, m in enumerate(months)], yticks=[8, 10, 12, 14, 16, 18, 20],
                ylabel_offset=0.9)
for lat, cp, tok in pops:
    dl = daylength(lat, n)
    pB.line(n, dl, tok, lw=1.6)
    late = np.where((n > 172) & (dl < cp))[0][0]
    pB.hline(cp, token=tok, dashed=True, lw=0.6)
    pB.points([n[late]], [dl[late]], tok, r=0.13)
    pB.text(n[late] + 6, dl[late] + 0.35, "%d°N" % lat, token=tok, ha="left")
bio.label(ax, (19.0, 10.3), "B  Day length and diapause induction", size="small", bold=True)
