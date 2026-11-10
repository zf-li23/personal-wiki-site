# Reaction-diffusion model of a chemokine gradient (Example 4.3.1): steady state c(x) = c0 exp(-x/l),
# l = sqrt(D/k), for three clearance rates; and the difference in receptor occupancy across a 10 um cell,
# d(theta) = theta (1 - theta) L / l, which peaks where c = Kd. Illustrative parameters.
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(20.0, 7.6)
D, KD, L = 100.0, 0.1, 10.0  # um^2/s, Kd in units of c0, cell length um
x = np.linspace(0, 1500, 1501)
cases = ((1e-2, "drug"), (1e-3, "dna"), (3e-4, "protein"))

bio.panel(ax, "A", (0.1, 7.5))
pa = quant.Plot(ax, (1.8, 1.4, 7.0, 5.4), xlim=(0, 1500), ylim=(1e-4, 1.2), ylog=True,
                xlabel="distance from source x / µm", ylabel="c(x) / c₀",
                xticks=[0, 500, 1000, 1500], yticks=[(1e-4, "10⁻⁴"), (1e-3, "10⁻³"), (1e-2, "10⁻²"), (0.1, "0.1"), (1, "1")])
pa.hline(KD, "muted", text="$K_d$", side="right")
for k, tok in cases:
    ell = np.sqrt(D / k)
    pa.line(x, np.exp(-x / ell), tok, lw=2.0)
pa.legend([(f"k = {k:g} s⁻¹, ℓ = {np.sqrt(D / k):.0f} µm", tok, "-") for k, tok in cases], at=(4.6, 7.25))

bio.panel(ax, "B", (10.3, 7.5))
pb = quant.Plot(ax, (12.0, 1.4, 7.4, 5.4), xlim=(0, 1500), ylim=(0, 0.03), xlabel="distance from source x / µm",
                ylabel="Δθ across a 10 µm cell", xticks=[0, 500, 1000, 1500], yticks=[0, 0.01, 0.02, 0.03])
for k, tok in cases:
    ell = np.sqrt(D / k)
    c = np.exp(-x / ell)
    th = c / (c + KD)
    pb.line(x, th * (1 - th) * L / ell, tok, lw=2.0)
    xp = ell * np.log(1 / KD)
    pb.vline(xp, tok, dashed=True)
pb.text(260, 0.0262, "peak L/(4ℓ) where c = K$_d$", size="tiny", ha="left")
