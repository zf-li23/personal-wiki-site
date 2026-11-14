"""Habitat saturation and helping on an island (individual-based simulation, loosely after the Seychelles warbler).

An island has 110 territories, each held by a breeding pair. Every year each breeder dies with probability 0.15 and
each nonbreeder with probability 0.3; vacant breeding positions are filled by randomly chosen surviving nonbreeders;
each pair raises a Poisson number of recruits with mean (0.9 + 0.2 min(h, 1))(1 - N/450), where h is the number of
nonbreeders per territory and N the total number of birds (food limitation), and recruits join the nonbreeders, which stay on their natal territory and help.
The population starts with 13 pairs. In year 30 the breeders of 29 territories (58 birds) are removed to another
island, as in Komdeur's translocation: the vacancies are filled at once by former helpers, and helping becomes rare
until the island is saturated again.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(3)
K = 110
breeders = 26
helpers = 0
years = 60
rec = []
for yr in range(years):
    if yr == 30:
        breeders -= 58
    breeders = rng.binomial(breeders, 0.85)
    helpers = rng.binomial(helpers, 0.7)
    slots = 2 * K - breeders
    move = min(slots, helpers)
    breeders += move
    helpers -= move
    pairs = breeders // 2
    h = helpers / K
    n = breeders + helpers
    mean = (0.9 + 0.2 * min(h, 1.0)) * max(0.0, 1 - n / 450)
    recruits = rng.poisson(mean, pairs).sum() if pairs else 0
    # recruits take free positions first, the rest stay as helpers
    slots = 2 * K - breeders
    new = min(slots, recruits)
    breeders += new
    helpers += recruits - new
    rec.append((yr, breeders, helpers))
rec = np.array(rec)

fig, ax = bio.canvas(20.0, 10.0)
pa = Ch.axes_at(ax, (2.6, 1.8, 15.8, 7.4))
pa.plot(rec[:, 0], rec[:, 1] + rec[:, 2], color=P.ink(), lw=1.6)
pa.plot(rec[:, 0], rec[:, 1], color=Ch.line("dna"), lw=1.6)
pa.plot(rec[:, 0], rec[:, 2], color=Ch.line("positive"), lw=1.6)
pa.axhline(2 * K, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
pa.text(1, 2 * K + 4, "breeding positions (2 per territory)", fontsize=FS["tiny"], color=P.muted())
pa.axvline(30, color=Ch.line("rna"), lw=0.9, ls=(0, (4, 2)))
pa.text(30.5, 300, "translocation of\n58 breeders", fontsize=FS["tiny"], color=Ch.line("rna"), va="top")
pa.text(52, rec[-1, 1] + rec[-1, 2] + 6, "all birds", fontsize=FS["tiny"], color=P.ink())
pa.text(52, rec[-1, 1] + 6, "breeders", fontsize=FS["tiny"], color=Ch.line("dna"))
pa.text(52, 8, "helpers", fontsize=FS["tiny"], color=Ch.line("positive"))
pa.set_xlim(0, years)
pa.set_ylim(0, max(330, (rec[:, 1] + rec[:, 2]).max() * 1.1))
Ch.style_axes(pa, "years", "number of birds")
