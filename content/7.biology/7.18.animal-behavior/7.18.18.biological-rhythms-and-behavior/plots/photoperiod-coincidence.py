"""Model: external coincidence in avian photoperiodism (Buenning's hypothesis as tested by Farner 1964 and Follett
et al. 1974 in white-crowned sparrows). A circadian rhythm of photosensitivity, entrained by dawn, is low for about
12 h and peaks about 16-20 h after dawn. Light that falls in this phase triggers LH release and gonadal growth.
A: four light schedules (yellow) and the sensitivity cycle phased to each 'dawn': only 16L:8D, the 36-h schedule 8L:28D
(whose second light period falls at circadian hours 12-20) and a 1-h night interruption at hour 18 put light into
the sensitive phase. B: day length over the year at 48 deg N and the critical day
length (about 12.5-13 h); gonads (schematic) grow when days exceed it in spring and regress in summer although
days are still long, because the birds become photorefractory."""
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(25, 11.4)
bio.panel(ax, "A", (0.3, 11.1))


def sens(h):
    """Photosensitivity at h hours after dawn (circadian, period 24 h)."""
    x = np.mod(h, 24.0)
    return np.exp(-0.5 * ((x - 18.0) / 2.2) ** 2)


rows = [("8L:16D", 8, 24, False), ("16L:8D", 16, 24, True), ("8L:28D", 8, 36, True), ("8L:16D + 1 h at 18 h", 8, 24, True)]
x0, w = 4.4, 8.4
H = 72.0
for k, (name, L, T, grows) in enumerate(rows):
    y = 9.0 - k * 2.1
    bio.label(ax, (x0 - 0.2, y + 0.45), name, size="tiny", ha="right", bold=True)
    bio.label(ax, (x0 - 0.2, y + 0.05), "testes grow" if grows else "no growth", size="tiny", ha="right",
              color=P.edge("positive" if grows else "negative"))
    ax.add_patch(__import__("matplotlib").patches.Rectangle((x0, y + 0.55), w, 0.35, facecolor=P.ink(), lw=0, zorder=4))
    t = 0.0
    while t < H:
        a, b = t, min(t + L, H)
        ax.add_patch(__import__("matplotlib").patches.Rectangle((x0 + a / H * w, y + 0.55), (b - a) / H * w, 0.35,
                                                               facecolor=P.fill("highlight"), lw=0, zorder=5))
        if k == 3:
            c = t + 18
            if c < H:
                ax.add_patch(__import__("matplotlib").patches.Rectangle((x0 + c / H * w, y + 0.55), 1 / H * w, 0.35,
                                                                       facecolor=P.fill("highlight"), lw=0, zorder=5))
        t += T
    hh = np.linspace(0, H, 400)
    s = sens(hh)  # the circadian sensitivity rhythm keeps its own ~24 h period
    ax.plot(x0 + hh / H * w, y - 0.45 + 0.85 * s, color=P.edge("dna"), lw=1.2, zorder=6)
for hr in (0, 24, 48, 72):
    bio.label(ax, (x0 + hr / H * w, 0.95), f"{hr} h", size="tiny", color=P.muted())
bio.label(ax, (x0 + w / 2, 0.45), "Hours after the first dawn", size="tiny")
bio.label(ax, (x0, 10.5), "yellow: light   black: dark   blue: circadian photosensitivity", size="tiny", ha="left")
bio.panel(ax, "B", (14.0, 11.1))
d = np.arange(365)
lat = np.radians(48)
dec = np.radians(-23.44) * np.cos(2 * np.pi * (d + 10) / 365)
DL = 24 / np.pi * np.arccos(np.clip(-np.tan(lat) * np.tan(dec), -1, 1))
q = quant.Plot(ax, (15.6, 6.3, 8.8, 4.2), xlim=(0, 365), ylim=(7, 18), ylabel="Day length / h",
               xticks=[(0, "Jan"), (90, "Apr"), (181, "Jul"), (273, "Oct"), (365, "")], yticks=[8, 12, 16])
q.line(d, DL, "highlight", lw=1.8)
q.hline(12.8, token="negative", text="critical day length", side="right")
g = np.zeros_like(d, float)
for i in range(1, 365):
    on = DL[i] > 12.8 and d[i] < 175
    g[i] = g[i - 1] + (0.06 * (1 - g[i - 1]) if on else -0.05 * g[i - 1])
r = quant.Plot(ax, (15.6, 1.7, 8.8, 3.6), xlim=(0, 365), ylim=(0, 1.1), ylabel="Gonad size",
               xticks=[(0, "Jan"), (90, "Apr"), (181, "Jul"), (273, "Oct"), (365, "")], yticks=None)
r.line(d, g, "dna", lw=1.8)
r.span(175, 300, "neutral", text="photorefractory", text_y=0.95)
ax.set_ylim(0.2, 11.4)
