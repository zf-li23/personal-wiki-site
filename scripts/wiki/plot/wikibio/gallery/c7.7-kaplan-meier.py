# Survival analysis of a simulated two-arm mouse study (seed 7). Survival times are Weibull (shape k = 1.5,
# control median 24 d) with proportional hazards (true HR = 0.45 for the drug); censoring comes from random
# loss to follow-up (exponential, mean 150 d) and from the end of the study at day 60. A: the design and a
# swimmer plot of the first eight mice per arm (event = filled dot, censored = open circle). B: Kaplan-Meier
# estimates with 95 % log(-log) Greenwood bands, censoring ticks, medians, the number-at-risk table, the
# log-rank test and the Cox hazard ratio, all computed from the simulated data.
import numpy as np

import wikibio as bio
from wikibio import quant, stats

P = bio.P
fig, ax = bio.canvas(25.0, 12.4)

# ---- simulated data -------------------------------------------------------------------------------
rng = np.random.default_rng(7)
n, k, med_c, hr_true, t_max = 40, 1.5, 24.0, 0.45, 60.0
lam_c = med_c / np.log(2) ** (1 / k)
lam_t = lam_c * hr_true ** (-1 / k)  # PH for a Weibull: the scale changes by HR^(-1/k)
arms = []
for g, lam in enumerate((lam_c, lam_t)):
    T = lam * rng.weibull(k, n)
    C = np.minimum(rng.exponential(150.0, n), t_max)
    arms.append((np.minimum(T, C).round(1), (T <= C).astype(int), np.full(n, g)))
time = np.r_[arms[0][0], arms[1][0]]
event = np.r_[arms[0][1], arms[1][1]]
group = np.r_[arms[0][2], arms[1][2]]
km = [stats.kaplan_meier(time[group == g], event[group == g]) for g in (0, 1)]
lr = stats.logrank(time, event, group)
cox = stats.cox_ph(time, event, group)
tok = ("neutral", "drug")
names = ("Vehicle", "Drug")

# ---- A: design -------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 12.25))
bio.label(ax, (0.9, 11.75), "Randomized mouse study", size="normal", bold=True, ha="left")
bio.icon(ax, "phylopic/mouse", at=(1.55, 9.9), height=0.95, color="animal")
bio.label(ax, (1.55, 9.15), f"{2 * n} mice", size="small")
for g, yy in enumerate((10.75, 9.05)):
    bio.arrow(ax, (2.45, 9.9), (3.55, yy), kind="process", head=0.18, shrink=0.05)
    bio.box(ax, (5.15, yy), 3.0, 1.1, tok[g])
    bio.icon(ax, "phylopic/mouse", at=(4.35, yy), height=0.6, color="animal")
    bio.label(ax, (5.15, yy + 0.2), names[g], size="small", ha="left", color=P.on_fill(), bold=True)
    bio.label(ax, (5.15, yy - 0.22), f"n = {n}", size="tiny", ha="left", color=P.on_fill())
bio.label(ax, (7.0, 9.9), "follow up\n60 days", size="tiny", ha="left", color=P.muted())

# swimmer plot: one line per mouse, from enrolment to death or censoring
m = 8
sw = quant.Plot(ax, (1.7, 1.3, 6.3, 6.0), (0, t_max), (0, 2 * m + 1.5), xlabel="$t$ / days",
                xticks=[0, 20, 40, 60], frame="l")
bio.label(ax, (0.9, 7.9), "Follow-up of individual mice", size="small", bold=True, ha="left")
for g in (0, 1):
    T, E, _ = arms[g]
    for i in range(m):
        yv = 2 * m + 0.5 - (g * (m + 1) + i)
        sw.line([0, T[i]], [yv, yv], tok[g], lw=2.2)
        sw.points([T[i]], [yv], tok[g], r=0.11, hollow=not E[i])
    bio.label(ax, (1.55, float(sw.Y(2 * m + 0.5 - g * (m + 1) - (m - 1) / 2))), names[g], size="tiny", ha="right",
              color=quant.line_color(tok[g]), bold=True)
sw.vline(t_max, text="end of study", top=True)
# legend for the markers
lx, ly = 4.3, 0.15
sw.ax.add_patch(bio.core.Circle((lx, ly), 0.1, color=P.ink()))
bio.label(ax, (lx + 0.22, ly), "death", size="tiny", ha="left")
sw.ax.add_patch(bio.core.Circle((lx + 1.5, ly), 0.1, facecolor=P.surface(), edgecolor=P.ink(), lw=0.9))
bio.label(ax, (lx + 1.72, ly), "censored", size="tiny", ha="left")

# ---- B: Kaplan-Meier --------------------------------------------------------------------------------
X0 = 12.0
bio.panel(ax, "B", (X0 - 2.0, 12.25))
kp = quant.Plot(ax, (X0, 3.4, 11.6, 7.9), (0, t_max), (0, 1.0), ylabel="Survival probability $\\hat S(t)$",
                xlabel="$t$ / days", xticks=[0, 10, 20, 30, 40, 50, 60], yticks=[0, 0.25, 0.5, 0.75, 1], grid=True)
kp.hline(0.5, "muted")
for g in (0, 1):
    stats.draw_km(kp, km[g], tok[g], ci=True, ci_alpha=0.18)
    if km[g].median is not None:
        x, y = kp.xy(km[g].median, 0.5)
        ax.plot([x, x], [kp.Y(0), y], color=quant.line_color(tok[g]), lw=0.8, ls=(0, (2, 1.6)), zorder=kp.z)
med = [km[g].median for g in (0, 1)]
kp.text(med[0] - 0.6, 0.06, f"median {med[0]:.0f} d", color=quant.line_color(tok[0]), ha="right")
if med[1] is not None:
    kp.text(med[1] + 0.6, 0.06, f"median {med[1]:.0f} d", color=quant.line_color(tok[1]), ha="left")
# curve labels at the right end
for g in (0, 1):
    T, _, _ = arms[g]
    kp.text(T.max() + 1.0, km[g].at(T.max()), names[g], color=quant.line_color(tok[g]), size="small", ha="left", bold=True)

# test results
bx, by = X0 + 0.45, 6.35
ci = cox["hr_ci"]
lines = [("Log-rank test", True),
         (f"$\\chi^2_{{{lr['df']}}} = {lr['chi2']:.2f}$,  {stats.fmt_p(lr['p'])}", False),
         (f"deaths {int(lr['O'][0])} / {int(lr['O'][1])} (exp. {lr['E'][0]:.1f} / {lr['E'][1]:.1f})", False),
         ("Cox model, drug vs vehicle", True),
         (f"HR = {cox['hr']:.2f}  (95% CI {ci[0]:.2f}–{ci[1]:.2f})", False)]
for i, (s, b) in enumerate(lines):
    bio.label(ax, (bx, by - i * 0.43 - (0.12 if i > 2 else 0)), s, size="tiny" if not b else "small", ha="left", bold=b,
              color=P.ink() if b else P.muted())
# censor tick legend
cx, cy = X0 + 0.15, 11.75
ax.plot([cx, cx], [cy - 0.07, cy + 0.13], color=P.muted(), lw=1.1)
bio.label(ax, (cx + 0.18, cy + 0.02), "censored    shaded: 95% CI", size="tiny", ha="left", color=P.muted())

stats.risk_table(ax, kp, [(km[0], names[0], tok[0]), (km[1], names[1], tok[1])], times=[0, 10, 20, 30, 40, 50, 60],
                 y=1.55, step=0.45, label_x=X0 - 2.1)
