"""Hormonal control of molting and metamorphosis in Manduca sexta (schematic titres after the classical
measurements; days of the last larval instar and the pupa).

A: the pathways: brain neurosecretory cells release PTTH, which acts on the prothoracic gland (through the receptor
tyrosine kinase Torso) to make ecdysone; peripheral tissues convert it to 20-hydroxyecdysone (20E), which acts through
the EcR/Usp receptor; the corpora allata make juvenile hormone (JH), which acts through Met and Kr-h1 and decides the
character of the molt. B: titres: JH falls early in the last instar once the larva passes the critical weight; a
small pulse of 20E without JH commits the epidermis to pupal development (commitment peak), a large pulse then
starts the pupal molt; JH reappears briefly before pupation and is absent during adult development.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
fig, ax = bio.canvas(30.0, 10.0)
bio.panel(ax, "A", (0.2, 9.8))
N = {"brain": (2.6, 8.4, "Brain: PTTH", "neuron"), "pg": (2.6, 5.8, "Prothoracic gland", "highlight"),
     "e": (7.4, 5.8, "Ecdysone", "highlight"), "20e": (12.0, 5.8, "20E → EcR/Usp", "drug"),
     "ca": (7.4, 3.0, "Corpora allata: JH", "positive"), "jh": (12.0, 3.0, "JH → Met, Kr-h1", "positive")}
for k, (x, y, t, tk) in N.items():
    bio.box(ax, (x, y), 3.8, 1.0, tk, t, size="small")
bio.arrow(ax, (2.6, 7.85), (2.6, 6.35), kind="activation", lw=1.0)
bio.label(ax, (2.8, 7.1), "Torso (RTK)", size="tiny", color=P.muted(), ha="left")
bio.arrow(ax, (4.55, 5.8), (5.45, 5.8), kind="process", lw=1.0)
bio.arrow(ax, (9.35, 5.8), (10.05, 5.8), kind="process", lw=1.0)
bio.arrow(ax, (9.35, 3.0), (10.05, 3.0), kind="process", lw=1.0)
bio.arrow(ax, (1.0, 7.9), (5.45, 2.7), kind="inhibition", lw=0.9, dashed=True, bend=0.35)
bio.label(ax, (1.0, 2.2), "last instar:\nallatostatic signals", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (12.0, 1.6), "JH present: larval molt\nJH absent: pupal / adult molt", size="tiny", color=P.ink())

bio.panel(ax, "B", (15.6, 9.8))
pa = C.axes_at(ax, (17.2, 1.6, 11.8, 7.0))
t = np.linspace(0, 12, 600)
jh = 1.0 * np.exp(-np.clip(t - 1.5, 0, None) / 0.6) * (t < 6) + 0.45 * np.exp(-((t - 6.6) / 0.35) ** 2)
e20 = 0.22 * np.exp(-((t - 4.2) / 0.35) ** 2) + 1.0 * np.exp(-((t - 7.4) / 0.6) ** 2) + 0.7 * np.exp(-((t - 10.5) / 0.9) ** 2)
pa.plot(t, jh, color=Q.line_color("positive"), lw=1.8, label="juvenile hormone")
pa.plot(t, e20, color=Q.line_color("drug"), lw=1.8, label="ecdysteroids (20E)")
pa.axvline(1.5, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pa.text(1.6, 1.05, "critical weight", fontsize=bio.core.FONT["tiny"], color=P.muted())
pa.text(4.2, 0.3, "commitment\npeak", fontsize=bio.core.FONT["tiny"], color=P.ink(), ha="center")
pa.text(7.4, 1.04, "pupal molt", fontsize=bio.core.FONT["tiny"], color=P.ink(), ha="center")
pa.text(10.5, 0.75, "adult development", fontsize=bio.core.FONT["tiny"], color=P.ink(), ha="center")
pa.axvline(8.3, color=P.muted(), lw=0.8)
pa.text(8.4, 1.12, "pupa →", fontsize=bio.core.FONT["tiny"], color=P.muted())
pa.set_xlim(0, 12)
pa.set_ylim(0, 1.25)
pa.set_yticks([])
C.style_axes(pa, "time (days, last larval instar → pupa)", "titre (relative)")
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left", bbox_to_anchor=(0.16, 0.72))
