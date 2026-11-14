"""The prisoner's dilemma and a cooperative hunting game (after Davies, Krebs and West 2012).

A: prisoner's dilemma payoffs to the row player (T = 5 > R = 3 > P = 1 > S = 0): defection is the better reply to
either move. B: a cooperative hunting game ("prisoner's delight", Binmore 2007): hunting costs 1 unit of energy; a
lone hunter brings back 4 units and two hunters 10, always shared equally between both players, so the payoffs are
4 (both hunt), 1 (hunt alone), 2 (free ride on a lone hunter) and 0 (no hunt); hunting is the better reply to either
move although free riding on a hunter (2) beats being free ridden on (1).
C: replicator dynamics dp/dt = p (1 - p)(W_C - W_D) of the frequency p of cooperators (hunters) in a well-mixed
population, from several starting frequencies: cooperation disappears in the prisoner's dilemma and goes to
fixation in the hunting game.
"""

import numpy as np
import wikibio as bio
from wikibio import behaviour as B
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(33.0, 10.0)

bio.label(ax, (5.6, 9.3), "Prisoner's dilemma", size="small", bold=True)
B.payoff_matrix(ax, (6.3, 5.6), ["C", "D"], [["R = 3", "S = 0"], ["T = 5", "P = 1"]], w=2.4, h=1.3,
                tokens=["positive", "negative"], highlight=(1, 1))
bio.label(ax, (6.3, 2.4), "defect is the best reply\nto both moves", size="tiny", color=P.muted())
bio.panel(ax, "A", (0.3, 9.8))

bio.label(ax, (15.6, 9.3), "Cooperative hunting", size="small", bold=True)
B.payoff_matrix(ax, (16.3, 5.6), ["Hunt", "Free"], [["4", "1"], ["2", "0"]], w=2.4, h=1.3,
                tokens=["positive", "negative"], highlight=(0, 0))
bio.label(ax, (16.3, 2.4), "hunt is the best reply\nto both moves", size="tiny", color=P.muted())
bio.panel(ax, "B", (10.3, 9.8))

pc = Ch.axes_at(ax, (24.0, 1.8, 8.4, 7.2))
t = np.linspace(0, 6, 300)
for M, tok, name in ((np.array([[3.0, 0.0], [5.0, 1.0]]), "negative", "prisoner's dilemma"),
                     (np.array([[4.0, 1.0], [2.0, 0.0]]), "positive", "hunting game")):
    for p0 in (0.1, 0.5, 0.9):
        pc.plot(t, B.replicator(M, p0, t), color=Ch.line(tok), lw=1.4)
pc.text(3.2, 0.12, "prisoner's dilemma", fontsize=FS["tiny"], color=Ch.line("negative"))
pc.text(3.2, 0.86, "hunting game", fontsize=FS["tiny"], color=Ch.line("positive"))
pc.set_xlim(0, 6)
pc.set_ylim(0, 1.02)
Ch.style_axes(pc, "time", "frequency of cooperators")
bio.panel(ax, "C", (21.8, 9.8))
