import numpy as np
import matplotlib.pyplot as plt

def bifurcation_diagram(r_min=2.5, r_max=4.0, n_r=1000, n_transient=500, n_iter=100, x0=0.3):
    """
    Draw the bifurcation diagram of the logistic map.

    Parameters:
        r_min, r_max: range of r
        n_r: number of r samples
        n_transient: number of transient iterations discarded
        n_iter: number of iterations to record
        x0: initial value (every r starts from x0)
    """
    r_vals = np.linspace(r_min, r_max, n_r)
    # Initialize storage arrays
    x_vals = []
    r_plot = []

    for r in r_vals:
        x = x0
        # Discard transient
        for _ in range(n_transient):
            x = r * x * (1 - x)
        # Record subsequent iterations
        for _ in range(n_iter):
            x = r * x * (1 - x)
            x_vals.append(x)
            r_plot.append(r)

    # Scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(r_plot, x_vals, s=0.01, c='k', alpha=0.5)
    plt.xlabel('$r$', fontsize=14)
    plt.ylabel('$x$', fontsize=14)
    plt.title('Logistic bifurcation diagram', fontsize=16)
    plt.grid(True, alpha=0.3)

bifurcation_diagram()
