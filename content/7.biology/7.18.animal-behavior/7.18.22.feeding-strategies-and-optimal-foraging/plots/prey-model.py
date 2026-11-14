# The prey model (Charnov 1976; Krebs and coauthors 1977). A: profitability E/h of prey types, here an
# illustrative curve for mussels of increasing size eaten by a shore crab (energy content rises with size,
# handling time rises faster), with a maximum at intermediate sizes as found by Elner and Hughes (1978).
# B: six prey types ranked by profitability (bars); the long-term rate of intake R_k of a diet made of the k
# best types (line, from Eq. 22.2); a type is worth eating only if its profitability exceeds the rate obtainable
# without it, so the optimal diet is the top three types here. C: the zero-one rule for two prey types with
# E1 = 2, E2 = 1 (arbitrary energy units) and h1 = h2 = 5 s, as in the great tit experiment: the less profitable
# type should be taken whenever met if the encounter rate with the better type is below the threshold
# lambda1* = 1 / (E1 h2 / E2 - h1) = 0.2 per s, and never above it (step); real predators show partial
# preferences (illustrative sigmoid, dashed).
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(28.0, 9.6)

# ---- A: profitability by size -------------------------------------------------------------------
pa = quant.Plot(ax, (1.8, 1.7, 6.6, 6.4), (0.5, 4.0), (0, 1.6), xlabel="Mussel length / cm",
                ylabel="Profitability E/h / J s⁻¹", xticks=[1, 2, 3, 4], yticks=[0, 0.5, 1.0, 1.5])
bio.panel(ax, "A", (0.2, 9.4))
L = np.linspace(0.5, 4.0, 300)
E = 30.0 * L ** 3          # energy content (J), proportional to volume
h = 8.0 * np.exp(1.45 * L)  # handling (cracking) time (s), rising steeply with shell strength
prof = E / h
prof = prof / prof.max() * 1.35
pa.line(L, prof, "dna", lw=2.2)
i = int(np.argmax(prof))
pa.points([L[i]], [prof[i]], "dna", r=0.12)
pa.line([L[i], L[i]], [0, prof[i]], "dna", lw=0.8, dotted=True)
pa.text(L[i] + 0.12, prof[i] + 0.1, "most profitable size", ha="left", token="dna")
pa.text(0.7, 0.18, "too little flesh", ha="left", color=P.muted())
pa.text(3.95, 0.48, "too long\nto crack", ha="right", color=P.muted())

# ---- B: ranking and the diet that maximizes the rate ----------------------------------------------
lam = np.array([0.02, 0.03, 0.05, 0.08, 0.10, 0.12])   # encounter rates (per s)
En = np.array([40.0, 30.0, 20.0, 10.0, 6.0, 3.0])       # energy (J)
hn = np.array([10.0, 10.0, 9.0, 8.0, 7.5, 6.0])         # handling times (s)
pr = En / hn
R = np.array([np.sum(lam[:k] * En[:k]) / (1 + np.sum(lam[:k] * hn[:k])) for k in range(1, 7)])
pb = quant.Plot(ax, (11.2, 1.7, 6.8, 6.4), (0.4, 6.6), (0, 4.5), xlabel="Prey type (ranked by E/h)",
                ylabel="Rate / J s⁻¹", xticks=[1, 2, 3, 4, 5, 6], yticks=[0, 1, 2, 3, 4])
bio.panel(ax, "B", (9.6, 9.4))
k_opt = int(np.argmax(R)) + 1
for k in range(6):
    tok = "positive" if k < k_opt else "neutral"
    pb.bars([k + 0.65, k + 1.35], [pr[k]], token=tok)
pb.line(np.arange(1, 7), R, "dna", lw=2.0, zorder=pb.z + 4)
pb.points(np.arange(1, 7), R, "dna", r=0.1, zorder=pb.z + 5)
pb.text(6.5, R[-1] + 0.3, "rate $R_k$ of the\nbest $k$ types", ha="right", va="bottom", token="dna")
pb.text(1.0, 4.35, "profitability $E_i/h_i$", ha="left", va="top", color=P.muted())
pb.text(k_opt + 0.45, R[k_opt - 1] + 0.75, f"optimal diet: types 1–{k_opt}", ha="left", token="positive")
pb.points([k_opt], [R[k_opt - 1]], "ink", r=0.17, hollow=True, zorder=pb.z + 6)

# ---- C: the zero-one rule ----------------------------------------------------------------------------
pc = quant.Plot(ax, (21.0, 1.7, 6.4, 6.4), (0, 0.5), (0, 1.05), xlabel="Encounter rate with large prey $\\lambda_1$ / s⁻¹",
                ylabel="Proportion of small prey taken", xticks=[0, 0.1, 0.2, 0.3, 0.4, 0.5], yticks=[0, 0.5, 1.0])
bio.panel(ax, "C", (19.4, 9.4))
E1, E2, h1, h2 = 2.0, 1.0, 5.0, 5.0
thr = 1.0 / (E1 * h2 / E2 - h1)
pc.line([0, thr, thr, 0.5], [1, 1, 0, 0], "positive", lw=2.2)
x = np.linspace(0, 0.5, 300)
pc.line(x, 1 / (1 + np.exp((x - thr) / 0.035)), "rna", lw=1.6, dashed=True)
pc.vline(thr, text="$\\lambda_1^*$", top=True)
pc.text(0.3, 0.62, "predicted (step)", ha="left", token="positive")
pc.text(0.3, 0.5, "observed: partial\npreferences", ha="left", va="top", token="rna")
pc.text(0.02, 0.08, "generalize", ha="left", color=P.muted())
pc.text(0.48, 0.08, "specialize", ha="right", color=P.muted())
