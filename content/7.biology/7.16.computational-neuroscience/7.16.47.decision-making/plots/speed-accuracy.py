"""Speed-accuracy trade-off and the optimal threshold in the drift-diffusion model.

Analytic results for dx = A dt + c dW with bounds +-theta (c = 1):
  P_c = 1 / (1 + exp(-2 A theta)),  DT = (theta / A) tanh(A theta).
A: fraction correct against mean decision time as the threshold theta varies from 0.05 to 2,
   for drifts A = 0.5, 1 and 2 (dots mark theta = 0.5, 1, 1.5).
B: reward rate RR = P_c / (DT + T_0) for A = 1 and total non-decision time plus inter-trial
   interval T_0 = 0.5, 1 and 3 s, against theta; dots mark the maximum (Bogacz et al., 2006):
   the optimal threshold rises when the cost of time between trials is larger.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
th = np.linspace(0.05, 2.0, 300)
pc = lambda A, t: 1 / (1 + np.exp(-2 * A * t))
dtm = lambda A, t: t / A * np.tanh(A * t)
fig, axs = plt.subplots(1, 2, figsize=(10, 3.8))
for A, c in ((0.5, P.edge("neutral")), (1.0, P.edge("dna")), (2.0, P.edge("negative"))):
    axs[0].plot(dtm(A, th), pc(A, th), lw=2, color=c, label=f"A = {A}")
    for t0 in (0.5, 1.0, 1.5):
        axs[0].plot(dtm(A, t0), pc(A, t0), "o", ms=4, color=c)
axs[0].set_xlabel("Mean decision time / s")
axs[0].set_ylabel("Fraction correct")
axs[0].set_title("A  Speed-accuracy trade-off", loc="left", fontsize=10)
axs[0].legend(frameon=False, fontsize=8, loc="lower right")
for T0, c in ((0.5, P.edge("positive")), (1.0, P.edge("dna")), (3.0, P.edge("negative"))):
    rr = pc(1.0, th) / (dtm(1.0, th) + T0)
    k = np.argmax(rr)
    axs[1].plot(th, rr, lw=2, color=c, label=f"$T_0$ = {T0} s")
    axs[1].plot(th[k], rr[k], "o", ms=6, color=c)
axs[1].set_xlabel("Threshold $\\theta$")
axs[1].set_ylabel("Reward rate / (rewards per s)")
axs[1].set_title("B  Optimal threshold", loc="left", fontsize=10)
axs[1].legend(frameon=False, fontsize=8, loc="upper right")
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
