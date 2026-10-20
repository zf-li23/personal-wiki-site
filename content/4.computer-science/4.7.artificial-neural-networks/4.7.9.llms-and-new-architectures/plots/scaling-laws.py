"""Compute-optimal scaling from the parametric loss L(N, D) = E + A/N^alpha + B/D^beta
(constants of the Besiroglu et al. 2024 refit of Chinchilla). Left: IsoFLOP curves,
the loss as a function of model size at fixed compute C = 6ND, with their minima.
Right: the compute-optimal parameter count and token count against compute,
compared with Kaplan et al.'s allocation N proportional to C^0.73."""

import numpy as np
import matplotlib.pyplot as plt

E, A, B, alpha, beta = 1.8172, 482.01, 2085.43, 0.3478, 0.3658
a = beta / (alpha + beta)
G = (alpha * A / (beta * B)) ** (1 / (alpha + beta))


def loss(N, C):
    D = C / (6 * N)
    return E + A / N**alpha + B / D**beta


def n_opt(C):
    return G * (C / 6) ** a


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.2))
budgets = [1e19, 1e20, 1e21, 1e22, 1e23, 5.76e23]
colors = plt.cm.viridis(np.linspace(0.1, 0.85, len(budgets)))
for C, c in zip(budgets, colors):
    N = np.logspace(np.log10(n_opt(C)) - 1.2, np.log10(n_opt(C)) + 1.2, 200)
    ax1.plot(N, loss(N, C), color=c, lw=1.6, label=f"C = {C:.2g} FLOPs")
    ax1.plot(n_opt(C), loss(n_opt(C), C), "o", color="C3", ms=5)
ax1.set_xscale("log")
ax1.set_xlabel("parameters N")
ax1.set_ylabel("predicted loss (nats per token)")
ax1.set_title("IsoFLOP curves: fixed compute, varying model size", fontsize=10)
ax1.legend(fontsize=7)
ax1.grid(alpha=0.3)

C = np.logspace(18, 27, 100)
N = n_opt(C)
ax2.plot(C, N, color="C0", lw=2, label=f"optimal parameters, slope {a:.2f}")
ax2.plot(C, C / (6 * N), color="C1", lw=2, label=f"optimal tokens, slope {1 - a:.2f}")
kaplan = 175e9 * (C / 3.14e23) ** 0.73          # through GPT-3, sized in the Kaplan era
ax2.plot(C, kaplan, color="C0", ls="--", lw=1.2, label="Kaplan-style allocation through GPT-3, slope 0.73")
for name, n, c, off in [("GPT-3", 175e9, 3.14e23, (-38, 4)), ("Gopher", 280e9, 5.76e23, (6, 2)),
                        ("Chinchilla", 70e9, 5.76e23, (6, -10)), ("Llama-3-405B", 405e9, 3.8e25, (6, -10))]:
    ax2.plot(c, n, "s", color="C3", ms=5)
    ax2.annotate(name, (c, n), textcoords="offset points", xytext=off, fontsize=8)
ax2.plot([], [], "s", color="C3", ms=5, label="parameters of published models")
ax2.set_xscale("log")
ax2.set_yscale("log")
ax2.set_xlabel("training compute C (FLOPs)")
ax2.set_ylabel("parameters or tokens")
ax2.set_title("compute-optimal allocation", fontsize=10)
ax2.legend(fontsize=7, loc="upper left")
ax2.grid(alpha=0.3)
fig.tight_layout()
