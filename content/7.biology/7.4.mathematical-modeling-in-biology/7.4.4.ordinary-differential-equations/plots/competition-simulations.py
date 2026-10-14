"""
lotka_volterra_competition.py
Complete analysis of Lotka-Volterra competition model
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

class CompetitionModel:
    """Lotka-Volterra competition model with dimensionless variables"""

    def __init__(self, a=0.4, b=0.6, rho=1.0):
        """
        Initialize competition model

        Parameters:
        -----------
        a : float
            Effect of species 2 on species 1 (normalized)
        b : float
            Effect of species 1 on species 2 (normalized)
        rho : float
            Relative growth rate (r2/r1)
        """
        self.a = a
        self.b = b
        self.rho = rho

        # Calculate equilibria
        self.equilibria = self.calculate_equilibria()

    def equations(self, t, state):
        """Define the ODE system"""
        x, y = state
        dxdt = x * (1 - x - self.a * y)
        dydt = self.rho * y * (1 - y - self.b * x)
        return [dxdt, dydt]

    def jacobian(self, x, y):
        """Calculate Jacobian matrix at point (x, y)"""
        J11 = 1 - 2*x - self.a*y
        J12 = -self.a * x
        J21 = -self.rho * self.b * y
        J22 = self.rho * (1 - 2*y - self.b * x)
        return np.array([[J11, J12], [J21, J22]])

    def calculate_equilibria(self):
        """Calculate all equilibrium points"""
        eq_points = []

        # (0, 0)
        eq_points.append((0.0, 0.0))

        # (1, 0)
        eq_points.append((1.0, 0.0))

        # (0, 1)
        eq_points.append((0.0, 1.0))

        # Coexistence point
        denominator = 1 - self.a * self.b
        if abs(denominator) > 1e-10:
            x_star = (1 - self.a) / denominator
            y_star = (1 - self.b) / denominator
            if 0 <= x_star <= 1 and 0 <= y_star <= 1:
                eq_points.append((x_star, y_star))

        return eq_points

    def analyze_equilibrium(self, eq_point):
        """Analyze stability of an equilibrium point"""
        x, y = eq_point
        J = self.jacobian(x, y)
        eigvals, eigvecs = np.linalg.eig(J)

        # Classify stability
        real_parts = np.real(eigvals)

        if all(real_parts < 0):
            stability = "stable"
        elif any(real_parts > 0):
            stability = "unstable"
        else:
            # All real parts <= 0, some may be zero
            stability = "marginally stable"

        # Classify type
        if np.all(np.isreal(eigvals)):
            if stability == "stable":
                eq_type = "stable node"
            elif stability == "unstable":
                if eigvals[0] * eigvals[1] < 0:
                    eq_type = "saddle"
                else:
                    eq_type = "unstable node"
            else:
                eq_type = "degenerate"
        else:
            if stability == "stable":
                eq_type = "stable focus"
            elif stability == "unstable":
                eq_type = "unstable focus"
            else:
                eq_type = "center"

        return {
            'point': eq_point,
            'jacobian': J,
            'eigenvalues': eigvals,
            'eigenvectors': eigvecs,
            'stability': stability,
            'type': eq_type
        }

    def plot_nullclines(self, ax, x_max=2, y_max=2):
        """Plot nullclines on the given axes"""
        # x-nullcline: x=0 or y=(1-x)/a
        x_vals = np.linspace(0, x_max, 100)
        y_xnull = (1 - x_vals) / self.a
        valid_idx = (y_xnull >= 0) & (y_xnull <= y_max)
        ax.plot(x_vals[valid_idx], y_xnull[valid_idx], 
                'r-', linewidth=2.5, alpha=0.8, label='dx/dt=0')

        # y-nullcline: y=0 or y=1-bx
        y_ynull = 1 - self.b * x_vals
        valid_idx = (y_ynull >= 0) & (y_ynull <= y_max)
        ax.plot(x_vals[valid_idx], y_ynull[valid_idx], 
                'b-', linewidth=2.5, alpha=0.8, label='dy/dt=0')

        # Plot axes (x=0 and y=0)
        ax.axhline(0, color='r', linestyle='-', alpha=0.5, linewidth=1)
        ax.axvline(0, color='b', linestyle='-', alpha=0.5, linewidth=1)

    def plot_vector_field(self, ax, x_max=2, y_max=2, density=20):
        """Plot vector field on the given axes"""
        # Create grid
        x = np.linspace(0.05, x_max, density)
        y = np.linspace(0.05, y_max, density)
        X, Y = np.meshgrid(x, y)

        # Calculate derivatives
        DX, DY = np.zeros_like(X), np.zeros_like(Y)
        for i in range(len(x)):
            for j in range(len(y)):
                dstate = self.equations(0, [X[j,i], Y[j,i]])
                DX[j,i] = dstate[0]
                DY[j,i] = dstate[1]

        # Normalize for better visualization
        norm = np.sqrt(DX**2 + DY**2)
        mask = norm > 0
        DX[mask] = DX[mask] / norm[mask] * 0.1  # Scale arrows
        DY[mask] = DY[mask] / norm[mask] * 0.1

        # Plot vector field
        ax.quiver(X, Y, DX, DY, color='gray', alpha=0.6, 
                  angles='xy', scale_units='xy', scale=1, width=0.003)

    def plot_equilibria(self, ax):
        """Plot equilibrium points with stability information"""
        for eq in self.equilibria:
            x, y = eq
            if 0 <= x <= 2 and 0 <= y <= 2:
                analysis = self.analyze_equilibrium(eq)

                if analysis['type'] == 'stable node' or analysis['type'] == 'stable focus':
                    marker = 'o'
                    color = 'green'
                    size = 100
                    label = 'Stable'
                elif analysis['type'] == 'saddle':
                    marker = 's'
                    color = 'orange'
                    size = 100
                    label = 'Saddle'
                elif analysis['type'] == 'unstable node' or analysis['type'] == 'unstable focus':
                    marker = '^'
                    color = 'red'
                    size = 100
                    label = 'Unstable'
                else:
                    marker = 'x'
                    color = 'black'
                    size = 100
                    label = 'Degenerate'

                ax.scatter(x, y, s=size, c=color, marker=marker, 
                          edgecolors='black', linewidth=1, zorder=5,
                          label=label if 'label_added' not in locals() else "")
                locals()['label_added'] = True

    def simulate_trajectory(self, initial_state, t_span=(0, 50), n_points=1000):
        """Simulate a trajectory from given initial state"""
        t_eval = np.linspace(t_span[0], t_span[1], n_points)
        sol = solve_ivp(self.equations, t_span, initial_state, 
                       t_eval=t_eval, method='RK45', rtol=1e-8)
        return sol

    def plot_trajectory(self, ax, initial_state, t_span=(0, 50), color='purple'):
        """Plot a trajectory on the phase plane"""
        sol = self.simulate_trajectory(initial_state, t_span)
        ax.plot(sol.y[0], sol.y[1], '-', color=color, linewidth=2, alpha=0.8)
        ax.plot(initial_state[0], initial_state[1], 'o', 
                color=color, markersize=8, markeredgecolor='black', markeredgewidth=1)

def create_competition_figure(a, b, rho=1.0, case_name=""):
    """Create a complete figure for competition model analysis"""
    model = CompetitionModel(a, b, rho)

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Phase portrait
    ax1 = axes[0]
    model.plot_vector_field(ax1, x_max=1.2, y_max=1.2, density=15)
    model.plot_nullclines(ax1, x_max=1.2, y_max=1.2)
    model.plot_equilibria(ax1)

    # Add threshold lines
    ax1.axvline(1, color='gray', linestyle='--', alpha=0.5)
    ax1.axhline(1, color='gray', linestyle='--', alpha=0.5)

    ax1.set_xlabel('Species 1 (x)', fontsize=12)
    ax1.set_ylabel('Species 2 (y)', fontsize=12)
    ax1.set_title(f'Phase Portrait: {case_name}\na={a}, b={b}, ρ={rho}', fontsize=14)
    ax1.set_xlim([-0.05, 1.2])
    ax1.set_ylim([-0.05, 1.2])
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc='upper right', fontsize=10)

    # Time series for multiple trajectories
    ax2 = axes[1]

    # Different initial conditions
    initial_conditions = [
        [0.1, 0.4],
        [0.3, 0.7],
        [0.8, 0.2],
        [0.9, 0.6]
    ]

    colors = plt.cm.viridis(np.linspace(0, 1, len(initial_conditions)))

    for i, init_state in enumerate(initial_conditions):
        sol = model.simulate_trajectory(init_state, t_span=(0, 50))

        # Plot time series
        time = sol.t
        species1 = sol.y[0]
        species2 = sol.y[1]

        ax2.plot(time, species1, '-', color=colors[i], linewidth=1.5, 
                alpha=0.7, label=f'x(t), init={init_state}')
        ax2.plot(time, species2, '--', color=colors[i], linewidth=1.5, 
                alpha=0.7, label=f'y(t), init={init_state}')

    ax2.set_xlabel('Time (τ)', fontsize=12)
    ax2.set_ylabel('Population', fontsize=12)
    ax2.set_title('Time Series', fontsize=14)
    ax2.grid(True, alpha=0.3)
    ax2.legend(loc='upper right', fontsize=9, ncol=2)

    plt.tight_layout()
    return fig, model

# Case 1: Species 1 wins (a < 1, b > 1)
print("Case 1: Species 1 wins")
fig1, model1 = create_competition_figure(a=0.5, b=1.5, case_name="Species 1 wins")

# Case 2: Species 2 wins (a > 1, b < 1)
print("\nCase 2: Species 2 wins")
fig2, model2 = create_competition_figure(a=1.5, b=0.5, case_name="Species 2 wins")

# Case 3: Stable coexistence (a < 1, b < 1)
print("\nCase 3: Stable coexistence")
fig3, model3 = create_competition_figure(a=0.4, b=0.6, case_name="Stable coexistence")

# Case 4: Unstable coexistence (a > 1, b > 1)
print("\nCase 4: Unstable coexistence (competitive exclusion)")
fig4, model4 = create_competition_figure(a=1.4, b=1.6, case_name="Unstable coexistence")

