import numpy as np
import matplotlib.pyplot as plt

def universal_function_search():
    """Numerical attempt to find the universal function"""

    # Feigenbaum constant
    alpha = -2.5029

    # Logistic family
    def f(r, x):
        return r * x * (1 - x)

    # Renormalization-group operation
    def renormalize(g, x):
        """Apply one renormalization transformation to g"""
        return alpha * g(g(x / alpha))

    # Choose r near the onset of chaos
    r_inf = 3.5699456  # Accumulation point of bifurcations
    n_iter = 10

    # Initial guess: the logistic map at r_inf
    x_domain = np.linspace(-0.5, 0.5, 1000)
    g_current = lambda x: f(r_inf, x + 0.5) - 0.5  # Centered

    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the iterations
    colors = plt.cm.viridis(np.linspace(0, 1, n_iter))

    for i in range(n_iter):
        # Evaluate the current function
        y_current = g_current(x_domain)

        # Plot (skip the first few, which may be unstable)
        if i >= 5:
            ax.plot(x_domain, y_current, color=colors[i], 
                   alpha=0.7, linewidth=2, 
                   label=f'Iteration {i}' if i % 2 == 0 else '')

        # Apply renormalization
        # Key fix: bind the current function via the default argument g=g_current
        # otherwise the lambda refers to the loop variable and recurses forever
        g_new = lambda x, g=g_current: renormalize(g, x)
        g_current = g_new

    ax.plot(x_domain, x_domain, 'k--', linewidth=1, label='y=x')
    ax.set_xlabel('x (rescaled)', fontsize=14)
    ax.set_ylabel('g(x)', fontsize=14)
    ax.set_title('Renormalization Group Flow to Universal Function', fontsize=16)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-0.5, 0.5)
    ax.set_ylim(-0.5, 0.5)

    # Show the alpha value in the figure instead of printing it
    ax.text(0.05, 0.95, f'Scaling factor $\\alpha \\approx {alpha}$', 
            transform=ax.transAxes, fontsize=12, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    plt.tight_layout()

universal_function_search()
