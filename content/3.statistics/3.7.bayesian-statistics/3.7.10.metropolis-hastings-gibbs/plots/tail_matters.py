"""Tail matters: independence Metropolis-Hastings for the t_1 target with a standard normal proposal:
log(p/g) and the trace of 1000 iterations."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)


def indep_mh(log_target, draw, log_prop, theta0, n):
    theta = np.empty(n)
    theta[0] = theta0
    acc = 0
    for t in range(n - 1):
        cand = draw()
        log_r = (log_target(cand) - log_prop(cand)) - (log_target(theta[t]) - log_prop(theta[t]))
        if np.log(rng.uniform()) < log_r:
            theta[t + 1] = cand
            acc += 1
        else:
            theta[t + 1] = theta[t]
    return theta, acc / (n - 1)


fig, (bx, cx) = plt.subplots(1, 2, figsize=(12, 3.4), gridspec_kw={"width_ratios": [1, 2.2]})
g2 = np.linspace(-6, 6, 400)
bx.plot(g2, stats.t.logpdf(g2, 1) - stats.norm.logpdf(g2))
bx.set_xlabel("θ")
bx.set_ylabel("log p(θ) / g(θ)")
bx.set_title("Target t1, proposal N(0, 1)")
chain2, rate2 = indep_mh(lambda t: stats.t.logpdf(t, 1), lambda: rng.normal(), stats.norm.logpdf, 0.0, 1000)
cx.plot(np.arange(1, 1001), chain2, "o", ms=2)
cx.set_xlabel("iteration")
cx.set_ylabel("θ")
cx.set_title(f"Independence sampler, acceptance {rate2:.2f}")
fig.tight_layout()
