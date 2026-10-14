"""
lotka_volterra_predator_prey.py
Complete analysis of Lotka-Volterra predator-prey models
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

class PredatorPreyModel:
    """Generalized predator-prey model with density dependence"""

    def __init__(self, alpha=1.0, beta=0.5, gamma=0.0, delta=0.0):
        """
        Initialize predator-prey model

        Parameters:
        -----------
        alpha : float
            Predator mortality relative to prey growth
        beta : float
            Predator half-saturation constant (or threshold prey density)
        gamma : float
            Prey density dependence (0 for classic model)
        delta : float
            Prey saturation constant (Holling Type II denominator coefficient)
            If 0, functional response is Type I (linear)
        """
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.delta = delta

        # Calculate equilibria
        self.equilibria = self.calculate_equilibria()

    def equations(self, t, state):
        """Define the ODE system"""
        x, y = state  # x: prey, y: predator

        # Interaction term with functional response
        # Type I: xy (when delta=0)
        # Type II: xy / (1 + delta*x) (when delta>0)
        interaction = (x * y) / (1 + self.delta * x)

        # dxdt = x(1 - gamma*x) - interaction
        dxdt = x * (1 - self.gamma * x) - interaction

        # dydt = alpha * y * (predator_growth - beta)
        # Note: beta represents death/conversion ratio threshold
        if self.delta > 0:
            # For Holling II, typical form: dy/dt = alpha * (x/(1+delta*x)) * y - mu * y
            # Here we keep structure: alpha * y * (x/(1+delta*x) - beta)
            dydt = self.alpha * y * (x/(1 + self.delta * x) - self.beta)
        else:
            dydt = self.alpha * y * (x - self.beta)

        return [dxdt, dydt]

    def jacobian(self, x, y):
        """Calculate Jacobian matrix at point (x, y)"""
        if self.delta == 0:
            J11 = 1 - 2*self.gamma*x - y
            J12 = -x
            J21 = self.alpha * y
            J22 = self.alpha * (x - self.beta)
        else:
            denom = 1 + self.delta * x
            denom_sq = denom * denom

            # dxdt = x - gamma*x^2 - x*y/denom
            # dx/dx = 1 - 2*gamma*x - (y(1) - 0)/denom ... wait d(x/denom)/dx
            # d(x/(1+dx))/dx = (1+dx - xd)/(1+dx)^2 = 1/(1+dx)^2
            J11 = 1 - 2*self.gamma*x - y / denom_sq

            # dx/dy = -x/denom
            J12 = -x / denom

            # dydt = alpha*y*(x/denom - beta)
            # dy/dx = alpha*y * (1/denom_sq)
            J21 = self.alpha * y / denom_sq

            # dy/dy = alpha * (x/denom - beta)
            J22 = self.alpha * (x/denom - self.beta)

        return np.array([[J11, J12], [J21, J22]])

    def calculate_equilibria(self):
        """Calculate all equilibrium points"""
        eq_points = []

        # (0, 0) - extinction
        eq_points.append((0.0, 0.0))

        # Prey only (y=0) -> x(1 - gamma*x) = 0
        if self.gamma > 0:
            eq_points.append((1/self.gamma, 0.0))

        # Coexistence
        # From dy/dt=0 -> x/(1+delta*x) = beta  => x = beta(1+delta*x) => x(1 - beta*delta) = beta
        if self.delta > 0:
            if 1 - self.beta * self.delta > 0:
                x_star = self.beta / (1 - self.beta * self.delta)
                # From dx/dt=0 -> 1 - gamma*x - y/(1+delta*x) = 0 => y = (1-gamma*x)(1+delta*x)
                if self.gamma == 0 or x_star < 1/self.gamma:
                    y_star = (1 - self.gamma * x_star) * (1 + self.delta * x_star)
                    if y_star > 0:
                        eq_points.append((x_star, y_star))
        else:
            # Classic model: x = beta
            x_star = self.beta
            if self.gamma == 0:
                eq_points.append((x_star, 1.0))
            else:
                y_star = 1 - self.gamma * x_star
                if y_star > 0:
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
            elif real_parts[0] == 0 and real_parts[1] == 0:
                eq_type = "center"
            else:
                eq_type = "unknown"

        return {
            'point': eq_point,
            'jacobian': J,
            'eigenvalues': eigvals,
            'eigenvectors': eigvecs,
            'stability': stability,
            'type': eq_type
        }

    def plot_nullclines(self, ax, x_max=3.0, y_max=3.0):
        """Plot nullclines on the given axes"""
        # Prey nullcline: dx/dt = 0 => y = (1 - gamma*x)(1 + delta*x) (if delta>0)
        x_vals = np.linspace(0, x_max, 200)

        if self.delta > 0:
            y_prey_null = (1 - self.gamma * x_vals) * (1 + self.delta * x_vals)
        else:
            y_prey_null = 1 - self.gamma * x_vals

        # Clip purely for visualization convenience if needed, but plotting logic handles bounds
        valid_idx = (y_prey_null >= -0.5) & (y_prey_null <= y_max + 1)
        ax.plot(x_vals[valid_idx], y_prey_null[valid_idx], 
                'r-', linewidth=2.5, alpha=0.8, label='Prey nullcline (dx/dt=0)')

        # Predator nullcline: dy/dt = 0
        if self.delta > 0:
            if 1 - self.beta * self.delta > 0:
                threshold_x = self.beta / (1 - self.beta * self.delta)
            else:
                threshold_x = np.inf
        else:
            threshold_x = self.beta

        if 0 <= threshold_x <= x_max:
            ax.axvline(threshold_x, 0, y_max, 
                      color='b', linewidth=2.5, alpha=0.8, 
                      label='Predator nullcline (dy/dt=0)')

        # Plot axes (x=0 and y=0)
        ax.axhline(0, color='r', linestyle='-', alpha=0.5, linewidth=1)
        ax.axvline(0, color='b', linestyle='-', alpha=0.5, linewidth=1)

    def plot_vector_field(self, ax, x_max=3.0, y_max=3.0, density=20):
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
        DX[mask] = DX[mask] / norm[mask] * 0.15  # Scale arrows
        DY[mask] = DY[mask] / norm[mask] * 0.15

        # Plot vector field
        ax.quiver(X, Y, DX, DY, color='gray', alpha=0.6, 
                  angles='xy', scale_units='xy', scale=1, width=0.003)

    def plot_equilibria(self, ax):
        """Plot equilibrium points with stability information"""
        for eq in self.equilibria:
            x, y = eq
            if 0 <= x <= 3.0 and 0 <= y <= 3.0:
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
                elif analysis['type'] == 'center':
                    marker = 'D'
                    color = 'blue'
                    size = 80
                    label = 'Center'
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

    def simulate_trajectory(self, initial_state, t_span=(0, 100), n_points=2000):
        """Simulate a trajectory from given initial state"""
        t_eval = np.linspace(t_span[0], t_span[1], n_points)
        sol = solve_ivp(self.equations, t_span, initial_state, 
                       t_eval=t_eval, method='RK45', rtol=1e-8)
        return sol

    def plot_trajectory(self, ax, initial_state, t_span=(0, 100), color='purple'):
        """Plot a trajectory on the phase plane"""
        sol = self.simulate_trajectory(initial_state, t_span)
        ax.plot(sol.y[0], sol.y[1], '-', color=color, linewidth=2, alpha=0.8)
        ax.plot(initial_state[0], initial_state[1], 'o', 
                color=color, markersize=8, markeredgecolor='black', markeredgewidth=1)

def create_predator_prey_figure(alpha=1.0, beta=0.5, gamma=0.0, delta=0.0, case_name=""):
    """Create a complete figure for predator-prey model analysis"""
    model = PredatorPreyModel(alpha, beta, gamma, delta)

    fig, axes = plt.subplots(2, 2, figsize=(14, 12))

    # Phase portrait
    ax1 = axes[0, 0]
    model.plot_vector_field(ax1, x_max=3.0, y_max=2.0, density=20)
    model.plot_nullclines(ax1, x_max=3.0, y_max=2.0)
    model.plot_equilibria(ax1)

    # Add trajectories
    initial_conditions = [
        [0.5, 0.5],
        [1.5, 0.3],
        [0.8, 1.2],
        [2.0, 0.8]
    ]

    colors = plt.cm.viridis(np.linspace(0, 1, len(initial_conditions)))

    for i, init_state in enumerate(initial_conditions):
        model.plot_trajectory(ax1, init_state, t_span=(0, 100), color=colors[i])

    ax1.set_xlabel('Prey population (x)', fontsize=12)
    ax1.set_ylabel('Predator population (y)', fontsize=12)
    ax1.set_title(f'Phase Portrait: {case_name}\nα={alpha}, β={beta}, γ={gamma}, δ={delta}', fontsize=14)
    ax1.set_xlim([-0.1, 3.0])
    ax1.set_ylim([-0.1, 2.0])
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc='upper right', fontsize=10)

    # Time series for first trajectory
    ax2 = axes[0, 1]
    sol = model.simulate_trajectory(initial_conditions[0], t_span=(0, 100))

    time = sol.t
    prey = sol.y[0]
    predator = sol.y[1]

    ax2.plot(time, prey, 'b-', linewidth=2, label='Prey (x)')
    ax2.plot(time, predator, 'r-', linewidth=2, label='Predator (y)')

    ax2.set_xlabel('Time (τ)', fontsize=12)
    ax2.set_ylabel('Population', fontsize=12)
    ax2.set_title('Time Series (single trajectory)', fontsize=14)
    ax2.grid(True, alpha=0.3)
    ax2.legend(loc='upper right', fontsize=11)

    # State-space plot with time color coding
    ax3 = axes[1, 0]
    scatter = ax3.scatter(prey, predator, c=time, cmap='viridis', 
                         s=20, alpha=0.6, edgecolors='none')

    # Add nullclines for reference
    model.plot_nullclines(ax3, x_max=3.0, y_max=2.0)

    ax3.set_xlabel('Prey population (x)', fontsize=12)
    ax3.set_ylabel('Predator population (y)', fontsize=12)
    ax3.set_title('State Space with Time Color Coding', fontsize=14)
    ax3.set_xlim([0, 3.0])
    ax3.set_ylim([0, 2.0])
    ax3.grid(True, alpha=0.3)

    plt.colorbar(scatter, ax=ax3, label='Time (τ)')

    # Population ratio and conserved quantity (for classic model)
    ax4 = axes[1, 1]

    if gamma == 0 and delta == 0:
        # For classic model, plot conserved quantity
        V = alpha * (prey - np.log(prey + 1e-10)) + (predator - np.log(predator + 1e-10))
        ax4.plot(time, V, 'g-', linewidth=2, label='Conserved quantity V')
        ax4.set_ylabel('V(x,y)', fontsize=12)
        ax4.set_title('Conserved Quantity (Classic Model)', fontsize=14)
    else:
        # For other models
        ratio = prey / (predator + 1e-10)
        ax4.plot(time, ratio, 'm-', linewidth=2, label='Prey/Predator ratio')
        ax4.set_ylabel('Prey/Predator ratio', fontsize=12)
        ax4.set_title('Population Ratio', fontsize=14)

    ax4.set_xlabel('Time (τ)', fontsize=12)
    ax4.grid(True, alpha=0.3)
    ax4.legend(loc='upper right', fontsize=11)

    plt.tight_layout()
    return fig, model

# Analyze different predator-prey scenarios
# Case 1: Classic Lotka-Volterra (γ=0, center)
print("Case 1: Classic Lotka-Volterra model")
fig1, model1 = create_predator_prey_figure(
    alpha=1.0, beta=0.5, gamma=0.0, delta=0.0,
    case_name="Classic Lotka-Volterra (neutral cycles)"
)

# Case 2: With density dependence (damped oscillations)
print("\nCase 2: Model with prey density dependence")
fig2, model2 = create_predator_prey_figure(
    alpha=1.0, beta=0.5, gamma=0.2, delta=0.0,
    case_name="With density dependence (damped oscillations)"
)

# Case 3: Limit cycle (Hopf bifurcation) using Rosenzweig-MacArthur
# Parameters adjusted to ensure the interior equilibrium is unstable (left of hump)
# Peak of prey nullcline y=(1-0.3x)(1+x) is at x approx 1.16
# Predator nullcline is at x* = beta/(1-beta) (if delta=1)
# 0.35 / 0.65 = 0.53, which is < 1.16, creating instability.
print("\nCase 3: Model exhibiting limit cycle")
fig3, model3 = create_predator_prey_figure(
    alpha=1.0, beta=0.35, gamma=0.3, delta=1.0,
    case_name="Limit Cycle (Rosenzweig-MacArthur)"
)

