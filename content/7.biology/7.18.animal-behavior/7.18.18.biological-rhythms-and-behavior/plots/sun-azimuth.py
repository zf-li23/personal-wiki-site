"""The sun's azimuth over the day (compass bearing, clockwise from north) at three latitudes on the June solstice,
computed from solar geometry (declination 23.44 deg; local solar time). The average rate is 15 deg per hour, but the
actual rate depends on latitude, season and time of day: slow in the morning and evening and fast around noon,
very fast at low latitudes in summer, when the sun passes nearly overhead. A time-compensated sun compass must
therefore be calibrated by experience to the local course of the sun."""
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P


def azimuth(lat_deg, h, dec_deg=23.44):
    lat, dec = np.radians(lat_deg), np.radians(dec_deg)
    H = np.radians(15 * (h - 12))
    alt = np.arcsin(np.sin(lat) * np.sin(dec) + np.cos(lat) * np.cos(dec) * np.cos(H))
    az = np.degrees(np.arctan2(-np.sin(H) * np.cos(dec), np.cos(lat) * np.sin(dec) - np.sin(lat) * np.cos(dec) * np.cos(H)))
    return np.mod(az, 360), np.degrees(alt)


fig, ax = bio.canvas(22, 9.8)
bio.panel(ax, "A", (0.3, 9.5))
p = quant.Plot(ax, (2.2, 1.7, 8.6, 7.0), xlim=(4, 20), ylim=(0, 360), xlabel="Local solar time / h",
               ylabel="Sun azimuth / deg", xticks=[4, 8, 12, 16, 20], yticks=[0, 90, 180, 270, 360])
bio.panel(ax, "B", (12.3, 9.5))
q = quant.Plot(ax, (14.0, 1.7, 7.6, 7.0), xlim=(4, 20), ylim=(0, 120), xlabel="Local solar time / h",
               ylabel="Rate of azimuth change / deg per h", xticks=[4, 8, 12, 16, 20], yticks=[0, 15, 30, 60, 90, 120])
h = np.linspace(4, 20, 961)
for lat, tok in [(60, "dna"), (40, "positive"), (25, "rna")]:
    az, alt = azimuth(lat, h)
    up = alt > 0
    azu = np.unwrap(np.radians(az)) * 180 / np.pi
    p.line(h[up], az[up], tok, lw=1.6)
    rate = np.gradient(azu, h)
    q.line(h[up], np.abs(rate[up]), tok, lw=1.6)

q.hline(15, text="mean 15°/h", side="right")
p.legend([("60° N", "dna", "-"), ("40° N", "positive", "-"), ("25° N", "rna", "-")], at=p.xy(13.5, 80))
p.hline(180, text="south at noon", side="left")
ax.set_ylim(0.3, 9.8)
