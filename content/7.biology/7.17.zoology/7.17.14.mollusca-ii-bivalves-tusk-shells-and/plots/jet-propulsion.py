# Jet propulsion (model). A: Froude efficiency eta = 2 / (1 + uj/U) (Eq. (14.3)). B: for a required thrust
# F = rho A uj (uj - U), the jet-speed ratio x = uj/U solves x (x - 1) = 1/a with a = rho A U^2 / F, the
# dimensionless jet area; efficiency then follows from Eq. (14.3).
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(24, 9.6)

bio.panel(ax, "A", (0.2, 9.4))
pa = quant.Plot(ax, (2.0, 1.6, 8.8, 6.8), (1, 8), (0, 1.0), xlabel="Jet speed / swimming speed  $u_j/U$",
                ylabel="Froude efficiency  η", xticks=[1, 2, 3, 4, 5, 6, 7, 8], yticks=[0, 0.25, 0.5, 0.75, 1.0])
x = np.linspace(1, 8, 300)
pa.span(2.0, 5.0, "negative")
pa.span(1.05, 1.5, "positive")
pa.text(3.5, 0.94, "squid jets", size="small", color=P.muted())
pa.text(1.27, 0.06, "fish\ntails", size="tiny", color=P.muted())
pa.line(x, 2 / (1 + x), token="dna", lw=2.0)
pa.text(6.2, 0.36, "η = 2 / (1 + u$_j$/U)", size="small", color=quant.line_color("dna"))

bio.panel(ax, "B", (12.4, 9.4))
pb = quant.Plot(ax, (14.4, 1.6, 8.8, 6.8), (0.01, 100), (0, 1.0), xlog=True,
                xlabel="Dimensionless jet area  $a = \\rho A U^2/F$", ylabel="Efficiency  η",
                xticks=[(0.01, "0.01"), (0.1, "0.1"), (1, "1"), (10, "10"), (100, "100")], yticks=[0, 0.25, 0.5, 0.75, 1.0])
a = np.logspace(-2, 2, 300)
xr = (1 + np.sqrt(1 + 4 / a)) / 2
pb.line(a, 2 / (1 + xr), token="dna", lw=2.0)
pb.text(0.012, 0.12, "small funnel:\nfast jet", size="tiny", ha="left", color=P.muted())
pb.text(12, 0.62, "large propulsor:\nslow wake", size="tiny", ha="left", color=P.muted())
# second axis-like annotation: jet speed ratio at a few points
for av in (0.03, 0.3, 3, 30):
    xv = (1 + np.sqrt(1 + 4 / av)) / 2
    e = 2 / (1 + xv)
    pb.points([av], [e], token="dna", r=0.09)
    pb.text(av * 1.25, e - 0.06, f"$u_j/U$ = {xv:.1f}", size="tiny", color=P.muted(), ha="left")
