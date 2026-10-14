import numpy as np
import matplotlib.pyplot as plt

def lyapunov_exponent_logistic(r, x0, n_iter=10000, n_transient=1000):
    """
    Compute the Lyapunov exponent of the logistic map.

    Parameters:
        r: parameter
        x0: initial value
        n_iter: total number of iterations
        n_transient: number of transient iterations discarded

    Returns:
        estimated Lyapunov exponent
    """
    x = x0
    # Discard transient
    for _ in range(n_transient):
        x = r * x * (1 - x)

    # Compute the Lyapunov exponent
    lyap_sum = 0.0
    for _ in range(n_iter):
        # Derivative |f'(x)|
        df_dx = abs(r * (1 - 2*x))
        lyap_sum += np.log(df_dx)
        x = r * x * (1 - x)

    return lyap_sum / n_iter

# Lyapunov exponent for different r values
# Higher resolution for a nicer bifurcation diagram
r_values = np.linspace(2.8, 4.0, 1000)
lyap_values = []
for r in r_values:
    # Fewer iterations to keep computation time reasonable
    lyap = lyapunov_exponent_logistic(r, 0.5, n_iter=2000)
    lyap_values.append(lyap)

# Generate bifurcation diagram data
x_vals_bif = []
r_vals_bif = []
n_transient_bif = 500
n_iter_bif = 100

for r in r_values:
    x = 0.5
    # Discard transient
    for _ in range(n_transient_bif):
        x = r * x * (1 - x)
    # Record subsequent iterations
    for _ in range(n_iter_bif):
        x = r * x * (1 - x)
        x_vals_bif.append(x)
        r_vals_bif.append(r)

# Plot both in a single figure
plt.figure(figsize=(12, 8))

# 1. Bifurcation diagram (black scatter)
# Low alpha so structure stays visible where points are dense
plt.scatter(r_vals_bif, x_vals_bif, s=0.05, c='k', alpha=0.2, label='Bifurcation ($x$)')

# 2. Lyapunov exponent spectrum (blue curve)
plt.plot(r_values, lyap_values, 'b-', linewidth=1.5, alpha=0.9, label='Lyapunov ($\\lambda$)')

# Mark the chaotic region (λ>0)
chaotic_region = np.array(lyap_values) > 0
plt.fill_between(r_values, 0, lyap_values, where=chaotic_region, 
                 color='red', alpha=0.3, label='Chaotic region (λ>0)')

# Zero line
plt.axhline(y=0, color='r', linestyle='--', linewidth=1.0)

plt.xlabel('$r$', fontsize=14)
plt.ylabel('$x$  and  $\\lambda$', fontsize=14)
plt.title('Bifurcation Diagram combined with Lyapunov Exponent', fontsize=16)
plt.grid(True, alpha=0.3)

# Limit the y range, since the Lyapunov exponent tends to -inf at superstable orbits
# and keep the bifurcation diagram (0-1) clearly visible
plt.ylim(-2.5, 1.2)

# Legend (markerscale enlarges the scatter legend marker)
plt.legend(loc='lower left', markerscale=40, fontsize=12)

plt.tight_layout()
