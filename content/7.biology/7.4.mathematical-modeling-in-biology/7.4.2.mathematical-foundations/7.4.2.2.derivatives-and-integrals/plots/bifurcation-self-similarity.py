import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# 1. Bifurcation diagram: the global pattern
def logistic_bifurcation(r_min=2.5, r_max=4.0, n_r=1000):
    """Draw the bifurcation diagram of the logistic map"""
    r_vals = np.linspace(r_min, r_max, n_r)
    n_transient = 500  # Discard transient
    n_record = 100     # Record steady state

    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # Left: full bifurcation diagram
    ax1 = axes[0]
    x_vals = []
    r_plot = []

    for r in r_vals:
        x = 0.5  # Fixed initial value
        # Discard transient
        for _ in range(n_transient):
            x = r * x * (1 - x)
        # Record
        for _ in range(n_record):
            x = r * x * (1 - x)
            x_vals.append(x)
            r_plot.append(r)

    ax1.scatter(r_plot, x_vals, s=0.1, c='k', alpha=0.5)
    ax1.set_xlabel('r', fontsize=14)
    ax1.set_ylabel('x', fontsize=14)
    ax1.set_title('Logistic Bifurcation Diagram', fontsize=16)
    ax1.grid(True, alpha=0.3)

    # Right: zoom-in showing self-similar structure
    ax2 = axes[1]
    # Zoom into the period-4 region
    r_min_zoom, r_max_zoom = 3.45, 3.57
    mask = (np.array(r_plot) >= r_min_zoom) & (np.array(r_plot) <= r_max_zoom)
    ax2.scatter(np.array(r_plot)[mask], np.array(x_vals)[mask], s=0.1, c='k', alpha=0.5)
    ax2.set_xlabel('r', fontsize=14)
    ax2.set_ylabel('x', fontsize=14)
    ax2.set_title('Zoom: Self-Similar Structure', fontsize=16)
    ax2.set_xlim(r_min_zoom, r_max_zoom)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()

logistic_bifurcation()
