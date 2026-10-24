# Growth of a bacterial batch culture (E. coli-like, glucose minimal medium). Data: viable counts from
# triplicate plates every 2 h, simulated (seed 13) from a Monod model with a Baranyi lag and death after
# starvation (true mu_max = 0.9 per h, lag 2 h, yield 1.7e9 cells/mL per g/L, S0 = 2 g/L glucose,
# death rate 0.1 per h, starvation time constant 10 h) with log-normal plate noise (SD 0.12 log10 units).
# The same model is fitted by nonlinear least squares to the log10 counts (Ks fixed at 10 mg/L, since
# counts alone cannot identify it); the fitted curve, its parameters (+- SE from the Jacobian) and the
# phase boundaries derived from it are shown. Dotted: the tangent construction of the lag time. Bottom:
# the model's substrate depletion; right: the Monod rate law mu(S).
import math

import numpy as np
from scipy import optimize

import wikibio as bio
from wikibio import microbio as M
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(25.0, 13.4)
Ks, S0, N0, tau_s = 0.01, 2.0, 1e5, 10.0
true = dict(mu_max=0.9, q0=1 / (math.exp(0.9 * 2.0) - 1), Y=1.7e9, kd=0.1)

# ---- simulated plate counts --------------------------------------------------------------------
rng = np.random.default_rng(13)
t_obs = np.arange(0, 49, 2.0)
_, N_true, _ = M.batch_growth(t_obs, Ks=Ks, S0=S0, N0=N0, tau_s=tau_s, **true)
reps = np.log10(N_true)[:, None] + rng.normal(0, 0.12, (len(t_obs), 3))
y_mean, y_sd = reps.mean(axis=1), reps.std(axis=1, ddof=1)


# ---- fit: theta = (mu_max, log10 q0, log10 Y, kd) ------------------------------------------------
def model(theta, t):
    mu, lq, lY, kd = theta
    return M.batch_growth(t, mu_max=mu, Ks=Ks, Y=10**lY, S0=S0, N0=N0, q0=10**lq, kd=kd, tau_s=tau_s)


def resid(theta):
    return (np.log10(model(theta, t_obs)[1])[:, None] - reps).ravel()


fit = optimize.least_squares(resid, [0.6, -1.0, 9.0, 0.05], bounds=([0.05, -4, 7, 0], [3, 2, 11, 1]), x_scale="jac")
J = fit.jac
dof = J.shape[0] - J.shape[1]
s2 = (fit.fun**2).sum() / dof
se = np.sqrt(np.diag(s2 * np.linalg.inv(J.T @ J)))
mu, lq, lY, kd = fit.x
lam = M.lag_time(mu, 10**lq)
g_min = math.log(2) / mu * 60
tt = np.linspace(0, 48, 600)
_, N_fit, S_fit = model(fit.x, tt)
lnN = np.log(N_fit)
rate = np.gradient(lnN, tt)
t_exp_end = tt[np.flatnonzero((tt > lam) & (rate < 0.1 * mu))[0]]
t_death = tt[np.flatnonzero((tt > t_exp_end) & (rate < -0.5 * kd))[0]]

# ---- A: growth curve --------------------------------------------------------------------------
X0, W = 2.4, 14.6
bio.panel(ax, "A", (0.1, 13.25))
pg = quant.Plot(ax, (X0, 4.75, W, 5.6), (0, 48), (1e4, 1e10), ylog=True, ylabel="viable cells / (CFU mL$^{-1}$)",
                yticks=[(10.0 ** k, f"10$^{{{k}}}$") for k in range(4, 11)], xticks=[(v, "") for v in range(0, 49, 6)],
                grid=True)
phases = [(0, lam, "lag", "neutral"), (lam, t_exp_end, "exponential (log)", "positive"),
          (t_exp_end, t_death, "stationary", "highlight"), (t_death, 48, "death", "negative")]
slot = W / 4
for k, (a, b, name, tok) in enumerate(phases):
    pg.span(a, b, tok, strength=0.78)
    # each phase gets an equal slot above the plot, joined to its span by a thin guide
    sx = X0 + (k + 0.5) * slot
    bio.label(ax, (sx, 11.1), name, size="small", bold=True, color=quant.line_color(tok), va="bottom")
    mx = float((pg.X(a) + pg.X(b)) / 2)
    ax.plot([sx, sx, mx, mx], [11.0, 10.75, 10.55, 10.35], color=quant.line_color(tok), lw=0.8, zorder=5)
for _, b, _, _ in phases[:-1]:
    pg.vline(b, "muted", lw=0.6)
pg.line(tt, N_fit, "receptor", lw=2.2)
for t, m, sd in zip(t_obs, y_mean, y_sd):
    X = float(pg.X(t))
    ax.plot([X, X], [pg.Y(10 ** (m - sd)), pg.Y(10 ** (m + sd))], color=P.ink(), lw=0.8, zorder=pg.z + 3)
pg.points(t_obs, 10**y_mean, "ink", r=0.075, hollow=True)
# tangent construction: line of slope mu through the steepest point meets the inoculum level at t = lag
i = int(np.argmax(rate))
yl = lnN[i] + mu * (tt - tt[i])
m = (np.exp(yl) > N0 * 0.7) & (np.exp(yl) < 3e9)
pg.line(tt[m], np.exp(yl[m]), "ink", lw=0.9, dotted=True)
pg.hline(N0, "muted", lw=0.7)
bio.callout(ax, pg.xy(lam, N0), pg.xy(lam + 3.5, 2.2e4), f"lag  λ = {lam:.1f} h", size="tiny")
pg.text(tt[i] + 1.2, math.exp(lnN[i]) / 3.5, f"slope $\\mu_{{\\max}}$ = {mu:.2f} h$^{{-1}}$", ha="left", size="tiny")
pg.text(36, N_fit[np.searchsorted(tt, 36)] * 2.2, f"$k_{{\\mathrm{{d}}}}$ = {kd:.2f} h$^{{-1}}$", ha="left", size="tiny",
        token="negative")

# cells of each phase (drawn natively): few large cells adapting, dividing cells, many small cells, dead ghosts
cy = 12.3
sx = [X0 + (k + 0.5) * slot for k in range(4)]
M.bacillus(ax, (sx[0] - 0.45, cy), 0.85, 0.36, angle=20, gram="-")
M.bacillus(ax, (sx[0] + 0.55, cy + 0.05), 0.85, 0.36, angle=-15, gram="-")
for dx, dy, an in ((-1.1, 0.0, 10), (0.0, 0.12, -15), (1.1, -0.05, 25)):
    M.bacillus(ax, (sx[1] + dx, cy + dy), 0.95, 0.3, angle=an, gram="-", dividing=True)
for k in range(10):
    M.bacillus(ax, (sx[2] - 1.0 + (k % 5) * 0.5, cy + 0.2 - (k // 5) * 0.4), 0.42, 0.2, angle=(k * 37) % 70 - 35, gram="-")
for dx, dy, an, dead in ((-1.1, 0.1, 15, False), (-0.35, -0.12, -30, True), (0.35, 0.15, 40, True), (1.05, -0.05, -10, True)):
    if dead:  # dead or lysed cells: ghost outlines
        o = M.bacillus(ax, (sx[3] + dx, cy + dy), 0.55, 0.24, angle=an, token="neutral")["outline"]
        ax.plot(*np.vstack([o, o[:1]]).T, color=P.muted(), lw=0.8, ls=(0, (2, 1.5)), zorder=9)
    else:
        M.bacillus(ax, (sx[3] + dx, cy + dy), 0.55, 0.24, angle=an, gram="-")

# ---- substrate --------------------------------------------------------------------------------
ps = quant.Plot(ax, (X0, 1.15, W, 2.6), (0, 48), (0, 2.2), xlabel="time $t$ / h", ylabel="glucose $S$ / (g L$^{-1}$)",
                xticks=list(range(0, 49, 6)), yticks=[0, 1, 2], grid=True)
for a, b, name, tok in phases:
    ps.span(a, b, tok, strength=0.86)
ps.line(tt, S_fit, "carbohydrate", lw=2.0)
bio.callout(ax, ps.xy(t_exp_end, 0.02), ps.xy(t_exp_end + 4, 1.1), "glucose exhausted", size="tiny")

def sci(v):
    e = int(math.floor(math.log10(v)))
    return f"{v / 10 ** e:.1f} × 10$^{{{e}}}$"


# ---- right: Monod and parameter table ----------------------------------------------------------
bio.panel(ax, "B", (18.6, 13.25))
pm = quant.Plot(ax, (20.0, 8.0, 4.3, 3.6), (0, 0.1), (0, 1.05), xlabel="$S$ / (g L$^{-1}$)",
                ylabel="$\\mu$ / h$^{-1}$", xticks=[0, 0.05, 0.1], yticks=[0, 0.5, 1])
SS = np.linspace(0, 0.1, 200)
pm.line(SS, M.monod(SS, mu, Ks), "positive", lw=2.0)
pm.hline(mu, "muted", text="$\\mu_{\\max}$", side="left")
pm.line([Ks, Ks], [0, mu / 2], "muted", lw=0.8, dashed=True)
pm.line([0, Ks], [mu / 2, mu / 2], "muted", lw=0.8, dashed=True)
pm.text(Ks + 0.003, 0.08, "$K_{\\mathrm{s}}$", ha="left", color=P.muted())
bio.label(ax, (20.0 - 1.0, 12.5), "Monod: $\\mu = \\mu_{\\max} S / (K_{\\mathrm{s}} + S)$", size="small", ha="left")

ty = 5.95
bio.label(ax, (19.0, ty + 0.75), "Fitted model (±SE)", size="small", bold=True, ha="left")
rows = [("$\\mu_{\\max}$", f"{mu:.2f} ± {se[0]:.2f} h$^{{-1}}$", f"{true['mu_max']:.2f}"),
        ("doubling time", f"{g_min:.0f} min", f"{math.log(2) / true['mu_max'] * 60:.0f}"),
        ("lag λ", f"{lam:.1f} h", f"{M.lag_time(true['mu_max'], true['q0']):.1f}"),
        ("$N_{\\max} = Y S_0$", sci(10 ** lY * S0) + " mL$^{-1}$", sci(true["Y"] * S0)),
        ("$k_{\\mathrm{d}}$", f"{kd:.3f} ± {se[3]:.3f} h$^{{-1}}$", f"{true['kd']:.2f}")]
bio.label(ax, (24.4, ty + 0.3), "true", size="tiny", ha="right", color=P.muted())
for k, (a, b, c) in enumerate(rows):
    yy = ty - k * 0.48
    bio.label(ax, (19.0, yy), a, size="tiny", ha="left")
    bio.label(ax, (20.95, yy), b, size="tiny", ha="left")
    bio.label(ax, (24.4, yy), c, size="tiny", ha="right", color=P.muted())
bio.icon(ax, "servier/erlenmeyer-flask-filled", at=(19.6, 2.2), height=1.8)
bio.label(ax, (20.5, 2.55), "batch culture", size="small", ha="left")
bio.label(ax, (20.5, 2.05), f"$S_0$ = {S0:g} g L$^{{-1}}$ glucose", size="tiny", ha="left", color=P.muted())
bio.label(ax, (20.5, 1.6), "inoculum $N_0$ = 10$^5$ mL$^{-1}$", size="tiny", ha="left", color=P.muted())
