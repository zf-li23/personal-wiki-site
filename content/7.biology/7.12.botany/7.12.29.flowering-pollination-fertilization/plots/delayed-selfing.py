# Delayed selfing as reproductive assurance. Pollinator visits per flower ~ Poisson(lambda); one visit
# outcrosses all ovules, so the outcrossed fraction is 1 - exp(-lambda). An obligate outcrosser gets only
# these seeds; a delayed selfer also self-fertilizes the remaining exp(-lambda) of ovules at the end of
# anthesis, whose offspring have relative fitness 1 - delta (inbreeding depression delta).
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio

P = bio.P
lam = np.linspace(0, 5, 300)
out = 1 - np.exp(-lam)
fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.0))
ax = axes[0]
ax.plot(lam, out, color=P.ink(), lw=2.0, ls="--", label="Obligate outcrosser")
for d, tok in ((0.2, "positive"), (0.5, "highlight"), (0.8, "negative")):
    ax.plot(lam, out + (1 - d) * np.exp(-lam), color=P.edge(tok), lw=2.0, label=f"Delayed selfer, δ = {d}")
ax.set_xlabel("Mean pollinator visits per flower, λ")
ax.set_ylabel("Fitness-weighted seed set")
ax.set_ylim(0, 1.05)
ax.set_xlim(0, 5)
ax.legend(frameon=False, fontsize=8)
ax.set_title("A  Reproductive assurance", loc="left", fontsize=10)
ax = axes[1]
for d, tok in ((0.2, "positive"), (0.5, "highlight"), (0.8, "negative")):
    gain = (out + (1 - d) * np.exp(-lam)) / np.maximum(out, 1e-9)
    ax.plot(lam[1:], gain[1:], color=P.edge(tok), lw=2.0, label=f"δ = {d}")
ax.axhline(1.0, color=P.muted(), lw=0.8)
ax.set_yscale("log")
ax.set_xlabel("Mean pollinator visits per flower, λ")
ax.set_ylabel("Delayed selfer / outcrosser")
ax.set_xlim(0, 5)
ax.legend(frameon=False, fontsize=8)
ax.set_title("B  Relative advantage of delayed selfing", loc="left", fontsize=10)
for a in axes:
    a.spines["top"].set_visible(False)
    a.spines["right"].set_visible(False)
fig.tight_layout()
