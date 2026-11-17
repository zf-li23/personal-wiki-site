"""Stoichiometric models of a consumer.

A, B: threshold elemental ratio (TER) model of a Daphnia-like herbivore. Body C:P (molar) Q_B = 85, carbon assimilation
a_C = 0.8 and net production efficiency of assimilated carbon e_C = 0.3, phosphorus assimilation a_P = 0.8; ingestion
1 unit C per day. Growth (in C units) = min(a_C e_C, Q_B a_P / Q_F); TER = Q_B a_P / (a_C e_C) = 283.
A: gross growth efficiency of C (growth / C ingested). B: release of P (excretion of the P not used for growth),
per unit C ingested.
C: growth rate hypothesis. Dry mass fractions: RNA phi_R rises linearly with specific growth rate mu from 0.04 to
0.30 (mu / mu_max from 0 to 1); protein phi_P = 0.60 - 0.6 phi_R. P content = 0.095 phi_R + 0.004 (RNA ~9.5 % P;
DNA and phospholipid baseline); N content = 0.16 phi_P + 0.155 phi_R + 0.005; C content 0.47.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
QB, aC, eC, aP = 85.0, 0.8, 0.3, 0.8
TER = QB * aP / (aC * eC)
QF = np.logspace(np.log10(30), np.log10(1500), 400)
growth = np.minimum(aC * eC, QB * aP / QF)
p_release = aP / QF - growth / QB

fig, axes = plt.subplots(1, 3, figsize=(14.0, 4.2))
ax = axes[0]
ax.plot(QF, growth, color=P.edge("plant"), lw=2.2)
ax.axvline(TER, color=P.muted(), ls="--", lw=1)
ax.text(TER * 1.06, 0.255, f"TER = {TER:.0f}", fontsize=8, color=P.muted())
ax.text(45, 0.08, "C-limited:\nexcess P\nreleased", fontsize=8, color=P.edge("dna"))
ax.text(500, 0.17, "P-limited:\nexcess C\nrespired or\negested", fontsize=8, color=P.edge("rna"))
ax.set_xscale("log")
ax.set_ylim(0, 0.28)
ax.set_xlabel("food C:P (molar)")
ax.set_ylabel("gross growth efficiency of carbon")
ax.set_title("A  Threshold elemental ratio", loc="left", fontsize=10)

bx = axes[1]
bx.plot(QF, p_release * 1000, color=P.edge("dna"), lw=2.2)
bx.axvline(TER, color=P.muted(), ls="--", lw=1)
bx.set_xscale("log")
bx.set_xlabel("food C:P (molar)")
bx.set_ylabel("P released per unit C eaten ($\\times 10^{-3}$)")
bx.set_title("B  Consumer-driven P recycling", loc="left", fontsize=10)

cx = axes[2]
mu = np.linspace(0, 1, 200)
phiR = 0.04 + 0.26 * mu
phiP = 0.60 - 0.6 * phiR
pc = 0.095 * phiR + 0.004
nc = 0.16 * phiP + 0.155 * phiR + 0.005
np_ratio = (nc / 14.007) / (pc / 30.974)
cx.plot(mu, np_ratio, color=P.edge("rna"), lw=2.2, label="N:P")
cx2 = cx.twinx()
cx2.plot(mu, pc * 100, color=P.edge("plant"), lw=2.2, ls="--", label="P content")
cx.set_xlabel("specific growth rate $\\mu/\\mu_{\\max}$")
cx.set_ylabel("body N:P (molar)", color=P.edge("rna"))
cx2.set_ylabel("P content / % of dry mass", color=P.edge("plant"))
cx.text(0.08, 24, "N:P (left axis)", color=P.edge("rna"), fontsize=9)
cx.text(0.68, 15.5, "P content\n(right axis)", color=P.edge("plant"), fontsize=9)
cx.set_title("C  Growth rate hypothesis", loc="left", fontsize=10)
for a in axes:
    for s in ("top", "right"):
        a.spines[s].set_visible(False)
cx2.spines["top"].set_visible(False)
cx.spines["right"].set_visible(True)
fig.tight_layout()
