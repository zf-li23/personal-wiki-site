import numpy as np
import matplotlib.pyplot as plt

def cobweb_plot(r, x0, n_iter, ax=None):
    """
    Draw a cobweb plot of the logistic map.

    Parameters:
        r: growth rate
        x0: initial value
        n_iter: number of iterations
        ax: matplotlib Axes; a new figure is created if None
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 8))

    # Plot the map curve
    x = np.linspace(0, 1, 1000)
    f = r * x * (1 - x)
    ax.plot(x, f, 'b-', lw=2, label=f'$f(x) = r x (1 - x)$')
    ax.plot(x, x, 'k--', lw=1, label='$y = x$')

    # Iterate and draw the cobweb lines
    x_current = x0
    for i in range(n_iter):
        y_current = r * x_current * (1 - x_current)
        # Vertical line
        ax.plot([x_current, x_current], [x_current, y_current], 'r-', lw=0.5)
        # Horizontal line
        ax.plot([x_current, y_current], [y_current, y_current], 'r-', lw=0.5)
        x_current = y_current

    ax.set_xlabel('x', fontsize=14)
    ax.set_ylabel('f(x)', fontsize=14)
    ax.set_title(f'Logistic cobweb plot (r = {r}, x0 = {x0})', fontsize=16)
    ax.legend(fontsize=12)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    return ax

# Example: cobweb plots for different r values
fig, axes = plt.subplots(2, 2, figsize=(12, 12))
r_vals = [0.75, 1.5, 2, 2.5]
x0 = 0.3
n_iter = 50

for i, (r, ax) in enumerate(zip(r_vals, axes.flat)):
    cobweb_plot(r, x0, n_iter, ax)
    # Mark the equilibrium point (if it exists)
    if r > 1:
        x_eq = 1 - 1/r
        ax.plot(x_eq, x_eq, 'go', markersize=8, label='Equilibrium point')
        ax.legend()

plt.tight_layout()
plt.subplots_adjust(hspace=0.3)
