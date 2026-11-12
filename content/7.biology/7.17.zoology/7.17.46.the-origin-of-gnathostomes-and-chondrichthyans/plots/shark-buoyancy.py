# Model: buoyancy of a shark from an oil-rich liver. A body of tissue density rho_b with a liver occupying
# volume fraction phi (density rho_L) has mean density rho = phi*rho_L + (1-phi)*rho_b; its weight in
# seawater (rho_w) as a fraction of its weight in air is (rho - rho_w)/rho. The lift that fins and body must
# provide equals this net weight; at speed U it is 0.5*rho_w*U^2*S*C_L, so the minimum speed to stay level
# is U = sqrt(2*W_net/(rho_w*S*C_L)). Parameter values are round illustrative numbers, not measurements:
# rho_b = 1.075 g/mL (lean shark tissue), rho_w = 1.026 g/mL, rho_L = 0.90 (squalene-rich liver) or 0.95
# (triglyceride-rich liver); a 10 kg shark with lifting area S = 0.06 m^2 and C_L = 0.4.
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
rho_b, rho_w = 1.075, 1.026
phi = np.linspace(0, 0.35, 200)
fig, ax = bio.canvas(22, 8.5)


def net(rho_L):
    rho = phi * rho_L + (1 - phi) * rho_b
    return (rho - rho_w) / rho


p = quant.Plot(ax, (1.6, 1.4, 8.6, 6.0), xlim=(0, 0.35), ylim=(-0.03, 0.05), xlabel="liver volume fraction",
               ylabel="net weight in water / weight in air", xticks=[0, 0.1, 0.2, 0.3],
               yticks=[-0.02, 0, 0.02, 0.04])
p.hline(0, text="neutral buoyancy", size="tiny")
for rho_L, tok, txt in ((0.90, "lipid", "liver density 0.90 (squalene)"), (0.95, "metabolite",
                                                                            "liver density 0.95 (triglycerides)")):
    p.line(phi, net(rho_L), tok, text=txt, at=0.55)
    phi0 = (rho_b - rho_w) / (rho_b - rho_L)
    if phi0 <= 0.35:
        p.points([phi0], [0], tok)
bio.panel(ax, "A", (0.4, 8.1))

S, CL, M, g = 0.06, 0.4, 10.0, 9.81
q = quant.Plot(ax, (13.0, 1.4, 8.4, 6.0), xlim=(0, 0.35), ylim=(0, 1.6), xlabel="liver volume fraction",
               ylabel="minimum speed / m s⁻¹", xticks=[0, 0.1, 0.2, 0.3], yticks=[0, 0.5, 1.0, 1.5])
for rho_L, tok in ((0.90, "lipid"), (0.95, "metabolite")):
    w = np.clip(net(rho_L), 0, None) * M * g
    u = np.sqrt(2 * w / (rho_w * 1000 * S * CL))
    q.line(phi, u, tok)
q.text(0.02, 1.45, "10 kg shark, S = 0.06 m², C_L = 0.4 (model)", size="tiny", ha="left")
bio.panel(ax, "B", (11.8, 8.1))
