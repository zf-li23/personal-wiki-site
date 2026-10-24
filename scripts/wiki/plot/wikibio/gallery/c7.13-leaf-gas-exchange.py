# Leaf photosynthesis as supply and demand. (A) CO2 diffuses from the air (Ca) through the stomatal pore
# (conductance gs) into the intercellular air spaces (Ci) and on to Rubisco in the chloroplasts (Cc), while
# water vapour leaves by the same path. (B) The Farquhar-von Caemmerer-Berry model of C3 photosynthesis: net
# assimilation is the minimum of the Rubisco-limited rate Ac and the RuBP-regeneration (electron-transport)
# limited rate Aj (25 C constants of Bernacchi et al. 2001). The supply line A = gc (Ca - Ci) meets the demand
# curve at the operating point. (C) Light-response curves (non-rectangular hyperbola) of a C3 and a C4 leaf
# at 30 C: C4 photosynthesis saturates later and, without photorespiration, has a higher quantum yield.
import numpy as np

import wikibio as bio
from wikibio import photosynthesis as ps
from wikibio import quant
from wikibio.quant import line_color

P = bio.P
fig, ax = bio.canvas(27.2, 10.4)
CO2, H2O = "metabolite", "dna"

# ---- A: the diffusion path ---------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 10.3))
L = ps.leaf_section(ax, (0.6, 4.3, 7.2, 4.9), stoma_x=3.9)
bio.label(ax, (0.6, L["top"] + 0.32), "Upper epidermis", size="tiny", ha="left", color=P.muted())
bio.callout(ax, (7.35, 7.45), (8.45, 7.85), "Palisade", size="tiny")
bio.callout(ax, (7.25, 5.6), (8.45, 5.6), "Spongy\nmesophyll", size="tiny")
pore, cav, air = L["pore"], L["cavity"], L["air"]
cc = line_color(CO2)
bio.arrow(ax, (pore[0] - 0.12, air[1] - 0.25), (cav[0] - 0.12, cav[1] + 0.15), kind="process", color=cc, lw=1.8, head=0.22, zorder=18)
bio.arrow(ax, (cav[0] - 0.05, cav[1] + 0.25), (L["plastid"][0] - 0.18, L["plastid"][1] + 0.02), kind="process", color=cc,
          lw=1.8, head=0.22, bend=-0.25, zorder=18)
wc = line_color(H2O)
bio.arrow(ax, (pore[0] + 0.15, cav[1] - 0.1), (pore[0] + 0.15, air[1] - 0.4), kind="process", color=wc, lw=1.4, dashed=True,
          head=0.2, zorder=18)
bio.label(ax, (pore[0] - 0.3, air[1] - 0.45), "CO₂", size="small", color=cc, ha="right", bold=True)
bio.label(ax, (pore[0] + 0.4, air[1] - 0.45), "H₂O", size="small", color=wc, ha="left", bold=True)
bio.label(ax, (0.6, 3.0), "Air: $C_{\\mathrm{a}}$ ≈ 420 µmol mol⁻¹", size="tiny", ha="left")
bio.callout(ax, (pore[0] - 0.45, pore[1] - 0.1), (2.7, 3.75), "Stoma: $g_{\\mathrm{s}}$", size="tiny")
bio.label(ax, (cav[0] - 0.55, cav[1] + 0.05), "$C_{\\mathrm{i}}$", size="small", ha="right", zorder=21)
bio.label(ax, (L["plastid"][0] + 0.05, L["plastid"][1] + 0.55), "$C_{\\mathrm{c}}$", size="small", ha="center", zorder=21)

bio.box(ax, (4.2, 1.25), 7.6, 1.7, "neutral")
bio.label(ax, (4.2, 1.72), "Demand:  $A = \\min(A_{\\mathrm{c}}, A_{\\mathrm{j}})$", size="small", color=P.on_fill())
bio.label(ax, (4.2, 0.8), "Supply:  $A = g_{\\mathrm{c}}\\,(C_{\\mathrm{a}} - C_{\\mathrm{i}})$,  $g_{\\mathrm{c}} = g_{\\mathrm{s}}/1.6$",
          size="small", color=P.on_fill())

# ---- B: A/Ci curve (Farquhar model) ---------------------------------------------------------------------
X0, Y0, W, H = 11.0, 1.4, 7.0, 7.6
VC, J, RD = 100.0, 180.0, 1.0
pb = quant.Plot(ax, (X0, Y0, W, H), (0, 1200), (-5, 45), xlabel="Intercellular CO₂ $C_{\\mathrm{i}}$ / µmol mol⁻¹",
                ylabel="Net assimilation $A$ / µmol m⁻² s⁻¹", xticks=[0, 400, 800, 1200], yticks=[0, 10, 20, 30, 40])
bio.panel(ax, "B", (X0 - 1.7, 10.3))
ci = np.linspace(1, 1200, 600)
A, Ac, Aj = ps.farquhar(ci, VC, J, RD)
i_t = int(np.argmin(np.where(ci > 100, np.abs(Ac - Aj), np.inf)))  # Ac = Aj (not at Gamma*)
ct = ci[i_t]
pb.span(0, ct, "enzyme", strength=0.82)
pb.span(ct, 1200, "highlight", strength=0.82)
pb.text(ct / 2, 43.5, "Rubisco-limited", va="top", ha="center", token="enzyme")
pb.text((ct + 1200) / 2, 43.5, "RuBP-limited", va="top", ha="center", token="atp")
pb.hline(0, dashed=False, lw=0.6)
pb.line(ci, Ac, "enzyme", lw=1.3, dashed=True)
pb.line(ci, Aj, "atp", lw=1.3, dashed=True)
pb.line(ci, A, "ink", lw=2.4)
pb.text(540, float(ps.farquhar(540, VC, J, RD)[1]) + 0.5, "$A_{\\mathrm{c}}$", token="enzyme", size="small", ha="right", va="bottom")
pb.text(150, float(ps.farquhar(150, VC, J, RD)[2]) + 1.8, "$A_{\\mathrm{j}}$", token="atp", size="small", ha="right", va="bottom")
# supply line and operating point (Ci / Ca = 0.7)
CA = 420.0
ci_op = 0.7 * CA
a_op = float(ps.farquhar(ci_op, VC, J, RD)[0])
gc = a_op / (CA - ci_op)
xs = np.linspace(CA - 45 / gc, CA, 50)
pb.line(xs, gc * (CA - xs), CO2, lw=1.6)
pb.points([CA], [0], CO2, r=0.1)
pb.text(CA + 25, 1.2, "$C_{\\mathrm{a}}$", token=CO2, size="small", ha="left", va="bottom")
pb.text(CA + 25, 9.0, f"supply\nslope −$g_{{\\mathrm{{c}}}}$\n= −{gc:.2f}", token=CO2, ha="left", va="center")
pb.points([ci_op], [a_op], "ink", r=0.14, zorder=14)
pb.text(ci_op + 45, a_op - 1.0, f"operating point\n$C_{{\\mathrm{{i}}}}$ = {ci_op:.0f}, $A$ = {a_op:.1f}", ha="left", va="top")
g_comp = ci[np.argmin(np.abs(A))]
pb.points([g_comp], [0], "ink", r=0.08, hollow=True)
pb.text(g_comp + 25, -1.0, f"Γ ≈ {g_comp:.0f}", ha="left", va="top", color=P.muted())
pb.text(1180, 16, f"$V_{{\\mathrm{{cmax}}}}$ = {VC:.0f},  $J$ = {J:.0f},  $R_{{\\mathrm{{d}}}}$ = {RD:.0f}", ha="right", color=P.muted())
pb.text(1180, 13.5, f"Γ* = {ps.GAMMA_STAR:g}, 25 °C", ha="right", color=P.muted())

# ---- C: light response, C3 vs C4 -------------------------------------------------------------------------------
X1 = 20.2
pc = quant.Plot(ax, (X1, Y0, W - 0.6, H), (0, 2000), (-5, 45), xlabel="PPFD / µmol photons m⁻² s⁻¹",
                ylabel="Net assimilation $A$ / µmol m⁻² s⁻¹", xticks=[0, 500, 1000, 1500, 2000], yticks=[0, 10, 20, 30, 40])
bio.panel(ax, "C", (X1 - 1.7, 10.3))
I = np.linspace(0, 2000, 500)
c3 = dict(phi=0.045, amax=24.0, theta=0.7, rd=1.2)
c4 = dict(phi=0.055, amax=44.0, theta=0.8, rd=1.5)
pc.hline(0, dashed=False, lw=0.6)
for name, prm, tok, at in (("C₃", c3, "plant", 0.95), ("C₄", c4, "rna", 0.95)):
    a = ps.light_response(I, **prm)
    pc.line(I, a, tok, lw=2.4)
    pc.text(I[-1], a[-1] + 1.0, name, token=tok, size="normal", ha="right", va="bottom", bold=True)
    pc.line([0, 380], [-prm["rd"], -prm["rd"] + prm["phi"] * 380], tok, lw=0.9, dotted=True)
for k, (name, prm, tok) in enumerate((("C₄", c4, "rna"), ("C₃", c3, "plant"))):
    pc.text(1950, 15.5 - 2.4 * k, f"{name}:  φ = {prm['phi']:.3f},  $A_{{\\max}}$ = {prm['amax']:.0f}", token=tok, ha="right")
pc.text(1950, 9.0, "30 °C, ambient CO₂", ha="right", color=P.muted())
pc.text(1950, 6.5, "dotted: initial slope (quantum yield φ)", ha="right", color=P.muted())
