# Surface plasmon resonance with mass-transport limitation (simulation and fitting).
# 1:1 binding of an analyte (concentration C, injected for 300 s, then buffer) to an immobilized ligand,
# k_on = 1e6 /M/s, k_off = 1e-3 /s (K_D = 1 nM), R_max = 100 RU. Transport to the surface is described by the
# two-compartment model in its quasi-steady form (Myszka et al. 1998):
#   dR/dt = [k_on C (R_max - R) - k_off R] / [1 + k_on (R_max - R) / k_t],
# with transport coefficient k_t = 1e10 RU/(M s) (reaction-limited) or 1e8 RU/(M s) (transport-limited).
# A: sensorgrams at 3, 10 and 30 nM in the two regimes. B: the transport-limited data (with 0.3 RU noise)
#    fitted globally with the simple 1:1 model: the fit underestimates both rate constants, although their
#    ratio (K_D) is nearly right, and leaves systematic residuals (inset numbers).
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
kon, koff, Rmax, tinj, tend = 1e6, 1e-3, 100.0, 300.0, 900.0
t = np.linspace(0, tend, 451)
concs = (3e-9, 10e-9, 30e-9)


def sensorgram(C, kt):
    def rhs(tt, R):
        c = C if tt < tinj else 0.0
        return [(kon * c * (Rmax - R[0]) - koff * R[0]) / (1 + kon * (Rmax - R[0]) / kt)]
    s = solve_ivp(rhs, (0, tend), [0.0], t_eval=t, max_step=1.0, rtol=1e-8)
    return s.y[0]


def simple(p, C):
    ka, kd, Rm = p
    kobs = ka * C + kd
    Req = Rm * ka * C / kobs
    Rt = Req * (1 - np.exp(-kobs * np.minimum(t, tinj)))
    return np.where(t < tinj, Rt, Rt[t <= tinj][-1] * np.exp(-kd * (t - tinj)))


fig, axs = plt.subplots(1, 2, figsize=(12.5, 4.2))
toks = ("dna", "neutral", "rna")
data = []
for C, tok in zip(concs, toks):
    axs[0].plot(t, sensorgram(C, 1e10), color=charts.line(tok), lw=1.6, label=f"{C * 1e9:g} nM, reaction-limited")
    R = sensorgram(C, 1e8)
    axs[0].plot(t, R, color=charts.line(tok), lw=1.4, ls="--")
    data.append(R + rng.normal(0, 0.3, t.size))
axs[0].plot([], [], color=P.muted(), ls="--", label="dashed: transport-limited")
axs[0].axvline(tinj, color=P.muted(), lw=0.6, ls=":")
charts.style_axes(axs[0], "time / s", "response / RU")
axs[0].legend(fontsize=7.5, frameon=False, loc="upper right")
charts.title(axs[0], "A   Mass transport slows binding and rebinding")


def res(p):
    return np.concatenate([simple(p, C) - d for C, d in zip(concs, data)])


fit = least_squares(res, (5e5, 2e-3, 90.0), x_scale=(1e5, 1e-3, 10.0))
ka, kd, Rm = fit.x
for C, d, tok in zip(concs, data, toks):
    axs[1].plot(t, d, ".", ms=1.5, color=charts.line(tok))
    axs[1].plot(t, simple(fit.x, C), color=P.ink(), lw=0.9)
rms = np.sqrt(np.mean(fit.fun**2))
axs[1].text(380, 1, f"1:1 fit: k_on = {ka:.2e} M⁻¹ s⁻¹ (true 1e6)\nk_off = {kd:.2e} s⁻¹ (true 1e-3)\n"
            f"K_D = {kd / ka * 1e9:.2f} nM (true 1.00)\nrms residual {rms:.2f} RU (noise 0.30)", fontsize=7.5, color=P.ink(), va="bottom")
charts.style_axes(axs[1], "time / s", "response / RU")
charts.title(axs[1], "B   A 1:1 fit to transport-limited data")
fig.tight_layout()
