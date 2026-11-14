# Schedules of reinforcement and the matching law (simulated, illustrative parameters; seed 0).
# A: an operant chamber for a rat (side view). B: cumulative records, the total number of lever presses
# plotted against time, for four schedules; ticks mark reinforcers. Fixed ratio 30 (FR 30): a pause after
# each reinforcer, then a high steady run of 30 presses. Variable ratio 30 (VR 30): high, steady responding,
# each press reinforced with probability 1/30. Fixed interval 60 s (FI 60): the first press after 60 s is
# reinforced, and the rate accelerates through the interval (the "scallop"). Variable interval 60 s (VI 60):
# reinforcers are set up at random times (mean 60 s) and collected by the next press; moderate steady rate.
# C: the generalized matching law on two concurrent VI schedules, log(B1/B2) = s log(R1/R2) + log b, with
# sensitivity s = 0.8 (undermatching) and no bias; points are noisy simulated sessions, the dashed line is
# strict matching (s = 1).
import numpy as np

import wikibio as bio
import wikibehav as wb
from wikibio import quant

P = bio.P
rng = np.random.default_rng(0)
DT, TMAX = 0.25, 600.0
fig, ax = bio.canvas(30.0, 10.4)

bio.panel(ax, "A", (0.2, 10.2))
box = wb.operant_box(ax, (4.6, 5.0), w=7.0, h=5.0)
bio.icon(ax, "phylopic/rat", at=box["inside"], height=1.3, anchor="bottom", color="animal")
bio.callout(ax, box["light"], (6.6, 8.4), "cue light", size="tiny")
bio.callout(ax, box["lever"], (4.7, 6.6), "lever", size="tiny")
bio.callout(ax, box["magazine"], (6.4, 1.3), "food magazine", size="tiny")
bio.callout(ax, box["dispenser"], (8.4, 8.9), "pellet dispenser", size="tiny")


def simulate(kind):
    t, n, last, out, rf = 0.0, 0, 0.0, [(0.0, 0)], []
    since, pause = 0, rng.normal(12, 3)
    armed, next_setup = False, rng.exponential(60)
    while t < TMAX:
        t += DT
        el = t - last
        if kind == "FR":
            rate = 0.0 if el < pause else 3.0
        elif kind == "VR":
            rate = 2.3
        elif kind == "FI":
            rate = 2.6 * min(el / 60.0, 1.2) ** 3
        else:
            rate = 0.85
            if not armed and t >= next_setup:
                armed = True
        if rng.random() < rate * DT:
            n += 1
            since += 1
            win = ((kind == "FR" and since >= 30) or (kind == "VR" and rng.random() < 1 / 30)
                   or (kind == "FI" and el >= 60) or (kind == "VI" and armed))
            if win:
                rf.append((t, n))
                last, since, pause = t, 0, max(rng.normal(12, 3), 4)
                if kind == "VI":
                    armed, next_setup = False, t + rng.exponential(60)
        out.append((t, n))
    return np.array(out), rf


pb = quant.Plot(ax, (12.0, 1.8, 7.6, 7.2), (0, TMAX), (0, 1450), xlabel="Time / s", ylabel="Cumulative responses",
                xticks=[0, 200, 400, 600], yticks=[0, 500, 1000], ylabel_offset=1.1)
bio.panel(ax, "B", (10.3, 10.2))
for kind, tok in (("VR", "dna"), ("FR", "rna"), ("VI", "protein"), ("FI", "positive")):
    rec, rf = simulate(kind)
    pb.line(rec[:, 0], rec[:, 1], tok, lw=1.5)
    for (tt, nn) in rf:
        x, y = pb.xy(tt, nn)
        ax.plot([x - 0.08, x + 0.08], [y - 0.14, y + 0.02], color=quant.line_color(tok), lw=1.1, zorder=9)
    label = {"VR": "VR 30", "FR": "FR 30", "VI": "VI 60 s", "FI": "FI 60 s"}[kind]
    pb.text(min(rec[-1, 0], 590), min(rec[-1, 1], 1400) + 40, label, ha="right", va="bottom", token=tok)

pc = quant.Plot(ax, (22.6, 1.8, 6.6, 7.2), (-1.3, 1.3), (-1.3, 1.3), xlabel="log(R1 / R2), reinforcers",
                ylabel="log(B1 / B2), responses", xticks=[-1, 0, 1], yticks=[-1, 0, 1])
bio.panel(ax, "C", (21.0, 10.2))
x = np.linspace(-1.2, 1.2, 2)
pc.line(x, x, "muted", lw=1.0, dashed=True)
pc.line(x, 0.8 * x, "dna", lw=2.0)
pc.text(-1.2, 1.15, "strict matching, s = 1 (dashed)", ha="left", color=P.muted())
pc.text(1.25, 0.6, "s = 0.8", ha="right", token="dna")
lr = np.repeat(np.log10([1 / 8, 1 / 4, 1 / 2, 1, 2, 4, 8]), 3)
pc.points(lr, 0.8 * lr + rng.normal(0, 0.08, lr.size), "dna", r=0.09, hollow=True)
