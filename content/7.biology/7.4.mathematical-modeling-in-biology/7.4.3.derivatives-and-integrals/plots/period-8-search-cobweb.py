import numpy as np
import matplotlib.pyplot as plt

def find_attractor_period(r, x0=0.5, n_transient=500, n_iterations=100, tol=1e-20):
    """
    Find the attractor period of the logistic map for a given r

    Parameters:
        r: parameter value
        x0: initial value
        n_transient: number of transient steps to reach the steady state
        n_iterations: number of recorded iterations used for period detection
        tol: tolerance

    Returns:
        period of the attractor
    """
    # Transient iterations: let the system reach the steady state
    x = x0
    for _ in range(n_transient):
        x = r * x * (1 - x)

    # Record subsequent iterations
    attractor = np.zeros(n_iterations)
    for i in range(n_iterations):
        x = r * x * (1 - x)
        attractor[i] = x

    # Find the period by checking for repeating patterns
    period = 1
    for k in range(2, n_iterations+1):
        # Check whether period k exists
        if n_iterations - k + 1 > 0:
            # Compare the first n-k+1 elements with the last n-k+1 (offset by k)
            if np.all(np.abs(attractor[:n_iterations-k] - attractor[k:n_iterations]) < tol):
                period = k
                break

    return period

def cobweb_plot(r, x0=0.5, n_iter=50, ax=None):
    """
    Draw a cobweb plot of the logistic map

    Parameters:
        r: parameter value
        x0: initial value
        n_iter: number of iterations
        ax: matplotlib Axes (optional)

    Returns:
        ax: matplotlib Axes
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 8))

    # Plot the map curve
    x = np.linspace(0, 1, 1000)
    f = r * x * (1 - x)
    ax.plot(x, f, 'b-', linewidth=2, label=f'$f(x) = {r}x(1-x)$')
    ax.plot(x, x, 'r--', linewidth=1.5, label='$y=x$')

    # Build the cobweb lines
    x_vals = [x0]
    y_vals = [0]

    # Iterate
    for _ in range(n_iter):
        # Vertical line: from (x_t, x_t) to (x_t, f(x_t))
        x_vals.append(x_vals[-1])
        y_vals.append(r * x_vals[-1] * (1 - x_vals[-1]))

        # Horizontal line: from (x_t, f(x_t)) to (f(x_t), f(x_t))
        x_vals.append(y_vals[-1])
        y_vals.append(y_vals[-1])

    # Draw the cobweb lines
    ax.plot(x_vals, y_vals, 'g-', linewidth=1, alpha=0.7, label='Cobweb')

    # Mark the starting point
    ax.plot(x0, 0, 'go', markersize=8, label=f'Start $x_0={x0}$')

    ax.set_xlabel('$x$', fontsize=12)
    ax.set_ylabel('$f(x)$', fontsize=12)
    ax.set_title(f'Cobweb diagram for $r={r:.4f}$', fontsize=14)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    return ax

# Parameters
r_min = 3.6  # Start of r search
r_max = 3.7  # End of r search (narrow range for efficiency)
delta_r = 0.000001  # Step in r
n_transient = 500  # Transient steps
n_iterations = 100  # Recorded iterations
target_period = 8  # Target period

# Search the r range for a period-8 attractor
found = False
optimal_r = None
optimal_period = None

# Scan r values
for r in np.arange(r_min, r_max + delta_r, delta_r):
    period = find_attractor_period(r, 0.5, n_transient, n_iterations)

    # Check whether the target period was found
    if period == target_period:
        optimal_r = r
        optimal_period = period
        found = True
        break

# Report the result
if found:
    print(f"Found r = {optimal_r:.6f} with period-{optimal_period} attractor.")

    # Draw the cobweb plot
    fig, ax = plt.subplots(figsize=(8, 8))
    cobweb_plot(optimal_r, 0.5, 50, ax)

    # Add the period to the title
    ax.set_title(f'Cobweb diagram for $r={optimal_r:.6f}$ (period-{optimal_period})', 
                 fontsize=14)

    plt.tight_layout()
else:
    print(f"No r found with period-{target_period} attractor in the range [{r_min:.2f}, {r_max:.2f}].")

    # Optional: plot period vs r to aid understanding
    print("\nTrying to understand the period structure...")

    # Test a set of r values and check their periods
    test_r_vals = np.linspace(3.6, 3.7, 100)
    periods = []

    for r in test_r_vals:
        period = find_attractor_period(r, 0.5, n_transient, n_iterations)
        periods.append(period)

    # Plot the periods
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(test_r_vals, periods, 'b-', linewidth=2, alpha=0.7)
    ax.set_xlabel('$r$', fontsize=14)
    ax.set_ylabel('Period', fontsize=14)
    ax.set_title(f'Period vs $r$ in range [{r_min:.2f}, {r_max:.2f}]', fontsize=16)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, max(periods) + 2)

    # Mark the target period
    ax.axhline(y=target_period, color='r', linestyle='--', linewidth=1.5, 
               label=f'Target period = {target_period}')
    ax.legend(fontsize=12)

    plt.tight_layout()
