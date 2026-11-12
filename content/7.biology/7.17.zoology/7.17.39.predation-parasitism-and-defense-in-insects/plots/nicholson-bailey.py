# Host-parasitoid dynamics. A: Nicholson-Bailey model (Eq. 39.2), lambda = 2, a = 0.05, c = 1, started 5%
# above equilibrium: diverging oscillations. B: May's negative binomial model (Eq. 39.4), same parameters,
# k = 0.5, started far from equilibrium: damped oscillations to a stable equilibrium. C: stability boundary k < 1 for all lambda.
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(24, 9)
lam, a, c = 2.0, 0.05, 1.0


def run(k, T):
    Ps = np.log(lam) / a if k is None else k * (lam ** (1 / k) - 1) / a
    Hs = lam * Ps / ((lam - 1) * c)
    H, Pp = ([Hs * 1.05], [Ps]) if k is None else ([Hs * 2.0], [Ps * 0.5])
    for _ in range(T):
        esc = np.exp(-a * Pp[-1]) if k is None else (1 + a * Pp[-1] / k) ** -k
        H.append(lam * H[-1] * esc)
        Pp.append(c * H[-2] * (1 - esc))
        if H[-1] < 1e-3:
            break
    return np.array(H), np.array(Pp), Hs, Ps


for i, (k, T, title) in enumerate([(None, 40, "A  Nicholson-Bailey (random search)"),
                                   (0.5, 40, "B  Aggregated attacks (k = 0.5)")]):
    A = charts.axes_at(ax, (1.6 + i * 8.0, 1.4, 6.4, 6.6))
    H, Pp, Hs, Ps = run(k, T)
    t = np.arange(len(H))
    A.semilogy(t, H, "-o", ms=2.5, color=P.edge("positive"), lw=1.3, label="hosts")
    A.semilogy(t, Pp, "--s", ms=2.5, color=P.edge("negative"), lw=1.3, label="parasitoids")
    A.set_xlabel("Generation")
    A.set_ylabel("Number (log scale)")
    A.set_title(title, fontsize=8, loc="left")
    A.set_ylim(1e-2, 1e3)
    A.legend(fontsize=7, frameon=False, loc="lower left")
C = charts.axes_at(ax, (18.0, 1.4, 5.4, 6.6))
C.axhspan(0, 1, color=P.light("positive"))
C.axhline(1, color=P.edge("positive"), lw=1.4)
C.text(6, 0.5, "stable", ha="center", fontsize=8, color=P.edge("positive"))
C.text(6, 2.0, "unstable", ha="center", fontsize=8, color=P.edge("negative"))
C.set_xlim(1, 11)
C.set_ylim(0, 3)
C.set_xlabel("Host rate of increase, lambda")
C.set_ylabel("Clumping parameter k")
C.set_title("C  Stability (May 1978)", fontsize=8, loc="left")
