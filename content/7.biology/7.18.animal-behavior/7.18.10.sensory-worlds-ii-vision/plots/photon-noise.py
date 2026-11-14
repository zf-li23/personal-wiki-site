# Photon noise limits vision in dim light (Rose-de Vries law; illustrative parameters).
# A channel that catches N photons in one integration time can detect a contrast C only if the signal
# C*N exceeds about k standard deviations of the Poisson noise sqrt(N): C_min = k / sqrt(N), k = 3.
# N = S * 4.1e3 * L * dt * n, with S from Land's formula S = (pi/4)^2 (A/f)^2 d^2 (1 - exp(-k l))
# (um^2 sr), 4.1e3 photons um^-2 sr^-1 s^-1 per cd m^-2 (555 nm), luminance L, integration time dt and
# n receptors pooled. Designs: human cone in daylight (pupil 3 mm, f 17 mm, d 2 um, l 30 um, dt 20 ms,
# no pooling); human rod channel (pupil 8 mm, d 2 um, l 25 um, dt 100 ms, 100 rods); owl rod channel
# (f-number 1.3, d 1.5 um, l 40 um, dt 100 ms, 100 rods).
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
kabs = 0.035  # um^-1


def S(a_over_f, d, l):
    return (np.pi / 4) ** 2 * a_over_f ** 2 * d ** 2 * (1 - np.exp(-kabs * l))


DESIGNS = [("cone, day pupil, no pooling", S(3 / 17, 2.0, 30), 0.02, 1, "receptor", "-"),
           ("human rods: wide pupil, 100 pooled, 0.1 s", S(8 / 17, 2.0, 25), 0.1, 100, "channel", "-"),
           ("owl rods: f/1.3, 100 pooled, 0.1 s", S(1 / 1.3, 1.5, 40), 0.1, 100, "protein", "--")]
L = np.logspace(-5, 4, 300)
fig, ax = bio.canvas(20, 9.6)
p = quant.Plot(ax, (2.2, 1.8, 16.4, 6.6), xlim=(1e-5, 1e4), ylim=(1e-3, 1.5), xlog=True, ylog=True,
               xlabel="Luminance L / (cd m⁻²)", ylabel="Smallest detectable contrast",
               xticks=[(1e-5, "10⁻⁵"), (1e-3, "10⁻³"), (1e-1, "0.1"), (10, "10"), (1e3, "1000")], yticks=[(1e-3, "0.001"), (1e-2, "0.01"), (0.1, "0.1"), (1, "1")])
for lo, hi, txt in ((1e-5, 1e-3, "starlight"), (1e-2, 1e-1, "moonlight"), (1, 10, "twilight"),
                    (1e2, 1e4, "daylight")):
    p.span(lo, hi, "neutral", strength=0.3)
    p.text(np.sqrt(lo * hi), 1.35, txt, color=P.muted())
for name, s, dt, n, tok, ls in DESIGNS:
    N = s * 4.1e3 * L * dt * n
    c = np.clip(3 / np.sqrt(N), 1e-3, 1.0)
    m = L <= (1e4 if n == 1 else 30)        # rods saturate above about 100 cd m^-2
    p.line(L[m], c[m], tok, dashed=(ls == "--"))
p.legend([(d[0], d[4], d[5]) for d in DESIGNS], at=(2.8, 3.4), step=0.42)
bio.label(ax, (10.4, 0.35), "rod curves end where rods saturate; a contrast of 1 is the largest possible (plateau: nothing detectable)",
          size="tiny", color=P.muted())
