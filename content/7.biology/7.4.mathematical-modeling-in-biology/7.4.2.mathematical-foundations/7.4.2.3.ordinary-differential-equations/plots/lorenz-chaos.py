"""
chaos_bifurcation.py
Demonstration of chaos and bifurcation in ecological models
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def lorenz_system(t, state, sigma=10.0, rho=28.0, beta=8/3):
    """Lorenz system - classic chaotic system"""
    x, y, z = state

    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z

    return [dxdt, dydt, dzdt]

def plot_lorenz_attractor():
    """Plot Lorenz attractor"""
    # Initial conditions
    state0 = [1.0, 1.0, 1.0]

    # Time span
    t_span = (0, 100)
    t_eval = np.linspace(t_span[0], t_span[1], 10000)

    # Solve ODE
    sol = solve_ivp(lorenz_system, t_span, state0, 
                   t_eval=t_eval, method='RK45', rtol=1e-8)

    x, y, z = sol.y

    fig = plt.figure(figsize=(14, 10))

    # 3D plot
    ax1 = fig.add_subplot(221, projection='3d')
    ax1.plot(x, y, z, '-', linewidth=0.5, alpha=0.7)
    ax1.set_xlabel('X', fontsize=10)
    ax1.set_ylabel('Y', fontsize=10)
    ax1.set_zlabel('Z', fontsize=10)
    ax1.set_title('Lorenz Attractor (3D)', fontsize=12)

    # Projections
    ax2 = fig.add_subplot(222)
    ax2.plot(x, y, '-', linewidth=0.5, alpha=0.7)
    ax2.set_xlabel('X', fontsize=10)
    ax2.set_ylabel('Y', fontsize=10)
    ax2.set_title('X-Y Projection', fontsize=12)
    ax2.grid(True, alpha=0.3)

    ax3 = fig.add_subplot(223)
    ax3.plot(x, z, '-', linewidth=0.5, alpha=0.7)
    ax3.set_xlabel('X', fontsize=10)
    ax3.set_ylabel('Z', fontsize=10)
    ax3.set_title('X-Z Projection', fontsize=12)
    ax3.grid(True, alpha=0.3)

    ax4 = fig.add_subplot(224)
    ax4.plot(y, z, '-', linewidth=0.5, alpha=0.7)
    ax4.set_xlabel('Y', fontsize=10)
    ax4.set_ylabel('Z', fontsize=10)
    ax4.set_title('Y-Z Projection', fontsize=12)
    ax4.grid(True, alpha=0.3)

    plt.tight_layout()

    # Demonstrate sensitivity to initial conditions
    fig2, axes = plt.subplots(3, 1, figsize=(12, 10))

    # Slightly different initial conditions
    state1 = [1.0, 1.0, 1.0]
    state2 = [1.001, 1.0, 1.0]  # 0.1% difference

    sol1 = solve_ivp(lorenz_system, (0, 50), state1, 
                    t_eval=np.linspace(0, 50, 5000), method='RK45')
    sol2 = solve_ivp(lorenz_system, (0, 50), state2,
                    t_eval=np.linspace(0, 50, 5000), method='RK45')

    time = sol1.t

    # Plot comparison
    axes[0].plot(time, sol1.y[0], 'b-', linewidth=1.5, alpha=0.7, label='Initial: (1.0, 1.0, 1.0)')
    axes[0].plot(time, sol2.y[0], 'r--', linewidth=1.5, alpha=0.7, label='Initial: (1.001, 1.0, 1.0)')
    axes[0].set_ylabel('X', fontsize=12)
    axes[0].set_title('Sensitivity to Initial Conditions (X component)', fontsize=14)
    axes[0].legend(fontsize=10)
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(time, sol1.y[1], 'b-', linewidth=1.5, alpha=0.7)
    axes[1].plot(time, sol2.y[1], 'r--', linewidth=1.5, alpha=0.7)
    axes[1].set_ylabel('Y', fontsize=12)
    axes[1].grid(True, alpha=0.3)

    axes[2].plot(time, sol1.y[2], 'b-', linewidth=1.5, alpha=0.7)
    axes[2].plot(time, sol2.y[2], 'r--', linewidth=1.5, alpha=0.7)
    axes[2].set_xlabel('Time', fontsize=12)
    axes[2].set_ylabel('Z', fontsize=12)
    axes[2].grid(True, alpha=0.3)

    plt.tight_layout()


plot_lorenz_attractor()
