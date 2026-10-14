"""
complex_ecological_model_enhanced.py
Enhanced analysis of complex ecological models with diverse dynamics
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from mpl_toolkits.mplot3d import Axes3D

class ComplexEcologicalModel:
    """Model combining competition and predation with enhanced analysis"""

    def __init__(self, a=0.5, b=0.5, rho=1.0, c1=0.5, c2=0.5, d=0.5, e1=1.0, e2=1.0):
        """
        Initialize complex ecological model

        Parameters:
        -----------
        a, b : float
            Competition coefficients
        rho : float
            Relative growth rate of species 2
        c1, c2 : float
            Predation rates on species 1 and 2
        d : float
            Predator mortality rate
        e1, e2 : float
            Conversion efficiencies
        """
        self.a = a
        self.b = b
        self.rho = rho
        self.c1 = c1
        self.c2 = c2
        self.d = d
        self.e1 = e1
        self.e2 = e2

    def equations(self, t, state):
        """Define the 3D ODE system"""
        u1, u2, v = state

        du1dt = u1 * (1 - u1 - self.a * u2 - v)
        du2dt = self.rho * u2 * (1 - u2 - self.b * u1 - (self.c2/self.c1) * v)
        dvdt = -self.d * v + self.e1 * u1 * v + self.e2 * u2 * v

        return [du1dt, du2dt, dvdt]

    def jacobian(self, u1, u2, v):
        """Calculate Jacobian matrix at point (u1, u2, v)"""
        J11 = 1 - 2*u1 - self.a*u2 - v
        J12 = -self.a * u1
        J13 = -u1

        J21 = -self.rho * self.b * u2
        J22 = self.rho * (1 - 2*u2 - self.b * u1 - (self.c2/self.c1) * v)
        J23 = -self.rho * (self.c2/self.c1) * u2

        J31 = self.e1 * v
        J32 = self.e2 * v
        J33 = -self.d + self.e1 * u1 + self.e2 * u2

        return np.array([[J11, J12, J13],
                         [J21, J22, J23],
                         [J31, J32, J33]])

    def analyze_equilibria(self):
        """Analyze all possible equilibria of the system"""
        equilibria = []

        # Extinction: (0, 0, 0)
        equilibria.append((0.0, 0.0, 0.0))

        # Prey 1 only: (1, 0, 0)
        equilibria.append((1.0, 0.0, 0.0))

        # Prey 2 only: (0, 1, 0)
        equilibria.append((0.0, 1.0, 0.0))

        # Both preys, no predator: coexistence without predation
        # Solve: 1 - u1 - a*u2 = 0 and 1 - u2 - b*u1 = 0
        denominator = 1 - self.a * self.b
        if abs(denominator) > 1e-10:
            u1_star = (1 - self.a) / denominator
            u2_star = (1 - self.b) / denominator
            if u1_star > 0 and u2_star > 0:
                equilibria.append((u1_star, u2_star, 0.0))

        # Predator with prey 1 only: (d/e1, 0, 1 - d/e1)
        if self.e1 > 0:
            u1_star = self.d / self.e1
            v_star = 1 - u1_star
            if u1_star > 0 and v_star > 0:
                equilibria.append((u1_star, 0.0, v_star))

        # Predator with prey 2 only: (0, d/e2, 1 - d/e2)
        if self.e2 > 0:
            u2_star = self.d / self.e2
            v_star = 1 - u2_star
            if u2_star > 0 and v_star > 0:
                equilibria.append((0.0, u2_star, v_star))

        # Coexistence of all three species
        # Solve the full system numerically
        from scipy.optimize import fsolve

        def full_system(vars):
            u1, u2, v = vars
            eq1 = u1 * (1 - u1 - self.a * u2 - v)
            eq2 = self.rho * u2 * (1 - u2 - self.b * u1 - (self.c2/self.c1) * v)
            eq3 = v * (-self.d + self.e1 * u1 + self.e2 * u2)
            return [eq1, eq2, eq3]

        # Try multiple starting points
        initial_guesses = [
            [0.3, 0.3, 0.3],
            [0.5, 0.2, 0.4],
            [0.2, 0.5, 0.4],
            [0.4, 0.4, 0.2]
        ]

        for guess in initial_guesses:
            try:
                solution = fsolve(full_system, guess, full_output=True)
                if solution[2] == 1:  # ier == 1 means solution found
                    u1_sol, u2_sol, v_sol = solution[0]
                    if (u1_sol > 0 and u2_sol > 0 and v_sol > 0 and 
                        u1_sol <= 1.5 and u2_sol <= 1.5 and v_sol <= 1.5):
                        # Check if this solution is significantly different from existing ones
                        is_new = True
                        for existing in equilibria:
                            dist = np.sqrt((u1_sol-existing[0])**2 + 
                                          (u2_sol-existing[1])**2 + 
                                          (v_sol-existing[2])**2)
                            if dist < 1e-3:
                                is_new = False
                                break
                        if is_new:
                            equilibria.append((u1_sol, u2_sol, v_sol))
            except:
                continue

        return equilibria

    def analyze_stability(self, equilibrium):
        """Analyze stability of an equilibrium point"""
        u1, u2, v = equilibrium
        J = self.jacobian(u1, u2, v)
        eigvals = np.linalg.eigvals(J)

        # Classify stability
        real_parts = np.real(eigvals)

        if all(real_parts < 0):
            stability = "asymptotically stable"
        elif any(real_parts > 0):
            stability = "unstable"
        else:
            stability = "marginally stable"

        # Classify type
        if np.all(np.isreal(eigvals)):
            if stability == "asymptotically stable":
                eq_type = "stable node"
            elif stability == "unstable":
                if np.sum(real_parts > 0) == 1:
                    eq_type = "saddle point (1D unstable)"
                elif np.sum(real_parts > 0) == 2:
                    eq_type = "saddle point (2D unstable)"
                else:
                    eq_type = "unstable node"
            else:
                eq_type = "degenerate"
        else:
            complex_eigs = eigvals[np.iscomplex(eigvals)]
            if stability == "asymptotically stable":
                eq_type = "stable focus"
            elif stability == "unstable":
                eq_type = "unstable focus"
            elif np.all(np.abs(real_parts) < 1e-10):
                eq_type = "center"
            else:
                eq_type = "unknown"

        return {
            'point': equilibrium,
            'jacobian': J,
            'eigenvalues': eigvals,
            'stability': stability,
            'type': eq_type
        }

    def simulate(self, initial_state, t_span=(0, 500), n_points=10000, method='RK45'):
        """Simulate the system"""
        t_eval = np.linspace(t_span[0], t_span[1], n_points)
        sol = solve_ivp(self.equations, t_span, initial_state,
                       t_eval=t_eval, method=method, rtol=1e-10, atol=1e-12)
        return sol

    def calculate_lyapunov_exponents(self, initial_state, t_span=(0, 1000), 
                                   perturbation=1e-8, n_trajectories=2):
        """Estimate Lyapunov exponents using nearby trajectories"""
        # This is a simplified method for demonstration
        # For accurate calculation, use specialized algorithms

        results = []

        # Reference trajectory
        sol_ref = self.simulate(initial_state, t_span, n_points=2000)
        t_ref = sol_ref.t
        u1_ref, u2_ref, v_ref = sol_ref.y

        # Perturbed trajectories
        perturbations = [
            [perturbation, 0, 0],
            [0, perturbation, 0],
            [0, 0, perturbation]
        ]

        exponents = []

        for i, pert in enumerate(perturbations):
            initial_pert = [initial_state[j] + pert[j] for j in range(3)]
            sol_pert = self.simulate(initial_pert, t_span, n_points=2000)

            # Calculate separation over time
            separation = []
            for j in range(min(len(t_ref), len(sol_pert.t))):
                idx_ref = j
                # Find closest time in perturbed solution
                idx_pert = np.argmin(np.abs(sol_pert.t - t_ref[idx_ref]))

                dist = np.sqrt(
                    (u1_ref[idx_ref] - sol_pert.y[0][idx_pert])**2 +
                    (u2_ref[idx_ref] - sol_pert.y[1][idx_pert])**2 +
                    (v_ref[idx_ref] - sol_pert.y[2][idx_pert])**2
                )
                separation.append(dist)

            separation = np.array(separation)
            # Filter out zero and very small separations
            valid = separation > 1e-12
            if np.any(valid):
                # Fit exponential to separation growth
                from scipy.stats import linregress
                slope, intercept, r_value, p_value, std_err = linregress(
                    t_ref[valid], np.log(separation[valid])
                )
                exponents.append(slope)
            else:
                exponents.append(0.0)

        return exponents

    def plot_3d_trajectory(self, initial_state, t_span=(0, 500), 
                          show_equilibria=True, show_vector_field=False):
        """Plot 3D trajectory with enhanced visualization"""
        sol = self.simulate(initial_state, t_span, n_points=10000)
        u1, u2, v = sol.y

        fig = plt.figure(figsize=(16, 12))

        # 3D trajectory
        ax1 = fig.add_subplot(231, projection='3d')

        # Color trajectory by time
        colors = plt.cm.viridis(np.linspace(0, 1, len(u1)))
        for i in range(len(u1)-1):
            ax1.plot(u1[i:i+2], u2[i:i+2], v[i:i+2], 
                    color=colors[i], linewidth=0.5, alpha=0.8)

        ax1.scatter(u1[0], u2[0], v[0], s=100, c='red', 
                   marker='o', label='Start', zorder=5)
        ax1.scatter(u1[-1], u2[-1], v[-1], s=100, c='green', 
                   marker='s', label='End', zorder=5)

        if show_equilibria:
            equilibria = self.analyze_equilibria()
            for eq in equilibria:
                u1_eq, u2_eq, v_eq = eq
                analysis = self.analyze_stability(eq)

                if analysis['stability'] == 'asymptotically stable':
                    color = 'green'
                    marker = 'o'
                    size = 80
                    label = 'Stable'
                elif analysis['stability'] == 'unstable':
                    if analysis['type'].startswith('saddle'):
                        color = 'orange'
                        marker = 's'
                        size = 80
                        label = 'Saddle'
                    else:
                        color = 'red'
                        marker = '^'
                        size = 80
                        label = 'Unstable'
                else:
                    color = 'blue'
                    marker = 'D'
                    size = 60
                    label = 'Center'

                ax1.scatter(u1_eq, u2_eq, v_eq, s=size, c=color, 
                           marker=marker, edgecolors='black', 
                           linewidth=1, zorder=10, label=label)

        ax1.set_xlabel('Species 1 (u1)', fontsize=12)
        ax1.set_ylabel('Species 2 (u2)', fontsize=12)
        ax1.set_zlabel('Predator (v)', fontsize=12)
        ax1.set_title('3D State Space Trajectory', fontsize=14)
        ax1.legend(fontsize=10)
        ax1.grid(True, alpha=0.3)

        # Projections with phase portraits
        projections = [
            (232, u1, u2, 'Species 1 (u1)', 'Species 2 (u2)', 'Prey Competition Plane'),
            (233, u1, v, 'Species 1 (u1)', 'Predator (v)', 'Species 1 vs Predator'),
            (234, u2, v, 'Species 2 (u2)', 'Predator (v)', 'Species 2 vs Predator'),
        ]

        for subplot_idx, x_data, y_data, xlabel, ylabel, title in projections:
            ax = fig.add_subplot(subplot_idx)

            # Color by density (2D histogram)
            hb = ax.hexbin(x_data, y_data, gridsize=30, cmap='viridis', 
                          alpha=0.7, bins='log')
            plt.colorbar(hb, ax=ax, label='Density')

            # Overlay trajectory
            ax.plot(x_data, y_data, 'k-', linewidth=0.5, alpha=0.5)

            ax.set_xlabel(xlabel, fontsize=11)
            ax.set_ylabel(ylabel, fontsize=11)
            ax.set_title(title, fontsize=13)
            ax.grid(True, alpha=0.3)

        # Time series
        ax5 = fig.add_subplot(235)
        t = sol.t
        ax5.plot(t, u1, 'b-', linewidth=1.5, alpha=0.8, label='Species 1')
        ax5.plot(t, u2, 'g-', linewidth=1.5, alpha=0.8, label='Species 2')
        ax5.plot(t, v, 'r-', linewidth=1.5, alpha=0.8, label='Predator')
        ax5.set_xlabel('Time (τ)', fontsize=12)
        ax5.set_ylabel('Population', fontsize=12)
        ax5.set_title('Time Series', fontsize=14)
        ax5.legend(fontsize=11)
        ax5.grid(True, alpha=0.3)

        # Frequency analysis (for oscillatory behavior)
        ax6 = fig.add_subplot(236)

        # Calculate power spectral density
        from scipy.signal import periodogram
        f1, P1 = periodogram(u1, fs=1/(t[1]-t[0]))
        f2, P2 = periodogram(u2, fs=1/(t[1]-t[0]))
        f3, P3 = periodogram(v, fs=1/(t[1]-t[0]))

        ax6.loglog(f1[f1>0], P1[f1>0], 'b-', alpha=0.7, label='Species 1')
        ax6.loglog(f2[f2>0], P2[f2>0], 'g-', alpha=0.7, label='Species 2')
        ax6.loglog(f3[f3>0], P3[f3>0], 'r-', alpha=0.7, label='Predator')

        ax6.set_xlabel('Frequency', fontsize=12)
        ax6.set_ylabel('Power', fontsize=12)
        ax6.set_title('Power Spectral Density', fontsize=14)
        ax6.legend(fontsize=11)
        ax6.grid(True, alpha=0.3, which='both')

        plt.tight_layout()
        return fig, sol

def explore_diverse_dynamics():
    """Explore different dynamical regimes with parameters tuned for diverse behaviors"""

    # Enhanced parameter sets for diverse behaviors
    parameter_sets = [
        {
            'name': 'Predator-mediated coexistence (stable equilibrium)',
            'params': {'a': 1.2, 'b': 1.2, 'rho': 1.0, 'c1': 0.3, 
                      'c2': 0.3, 'd': 0.3, 'e1': 0.8, 'e2': 0.8},
            'initial': [0.3, 0.4, 0.2],
            't_span': (0, 300)
        },
        {
            'name': 'Competitive exclusion (boundary equilibrium)',
            'params': {'a': 0.8, 'b': 1.5, 'rho': 1.0, 'c1': 0.8,
                      'c2': 0.2, 'd': 0.4, 'e1': 1.2, 'e2': 0.5},
            'initial': [0.4, 0.4, 0.3],
            't_span': (0, 300)
        },
        {
            'name': 'Stable limit cycle (periodic oscillations)',
            'params': {'a': 1.0, 'b': 1.0, 'rho': 1.0, 'c1': 0.5,
                      'c2': 0.5, 'd': 0.2, 'e1': 2.0, 'e2': 2.0},
            'initial': [0.5, 0.3, 0.4],
            't_span': (0, 500)
        },
        {
            'name': 'Complex oscillations (quasi-periodic or chaotic)',
            'params': {'a': 1.2, 'b': 1.2, 'rho': 1.2, 'c1': 0.6,
                      'c2': 0.6, 'd': 0.1, 'e1': 2.5, 'e2': 2.5},
            'initial': [0.6, 0.4, 0.5],
            't_span': (0, 1000)
        },
        {
            'name': 'Bistability (multiple attractors)',
            'params': {'a': 1.1, 'b': 1.1, 'rho': 1.0, 'c1': 0.4,
                      'c2': 0.4, 'd': 0.3, 'e1': 1.5, 'e2': 1.5},
            'initial': [0.7, 0.2, 0.4],
            't_span': (0, 400)
        },
        {
            'name': 'Stable coexistence (weak competition)',
            'params': {'a': 0.3, 'b': 0.3, 'rho': 1.0, 'c1': 0.2,
                      'c2': 0.2, 'd': 0.6, 'e1': 0.8, 'e2': 0.8},
            'initial': [0.5, 0.5, 0.3],
            't_span': (0, 300)
        }
    ]

    all_results = []

    for i, ps in enumerate(parameter_sets):
        print(f"\n{'='*80}")
        print(f"Case {i+1}: {ps['name']}")
        print(f"{'='*80}")

        model = ComplexEcologicalModel(**ps['params'])

        # Analyze equilibria
        print("\nEquilibrium Analysis:")
        equilibria = model.analyze_equilibria()
        for j, eq in enumerate(equilibria):
            analysis = model.analyze_stability(eq)
            print(f"  Equilibrium {j}: {eq}")
            print(f"    Type: {analysis['type']}")
            print(f"    Stability: {analysis['stability']}")
            print(f"    Eigenvalues: {analysis['eigenvalues']}")

        # Create figures
        fig, sol = model.plot_3d_trajectory(ps['initial'], t_span=ps['t_span'])
        fig.suptitle(f"{ps['name']}\nParameters: a={ps['params']['a']}, b={ps['params']['b']}, "
                    f"d={ps['params']['d']}, e1={ps['params']['e1']}, e2={ps['params']['e2']}", 
                    fontsize=16, y=1.05)

        # Calculate statistics
        u1, u2, v = sol.y
        t = sol.t

        # Remove transient (first 20%)
        n_transient = len(t) // 5
        u1_steady = u1[n_transient:]
        u2_steady = u2[n_transient:]
        v_steady = v[n_transient:]

        # Calculate mean and std
        mean_u1 = np.mean(u1_steady)
        mean_u2 = np.mean(u2_steady)
        mean_v = np.mean(v_steady)

        std_u1 = np.std(u1_steady)
        std_u2 = np.std(u2_steady)
        std_v = np.std(v_steady)

        print(f"\nSteady-state Statistics (after transient):")
        print(f"  Species 1: mean = {mean_u1:.4f}, std = {std_u1:.4f}")
        print(f"  Species 2: mean = {mean_u2:.4f}, std = {std_u2:.4f}")
        print(f"  Predator:  mean = {mean_v:.4f}, std = {std_v:.4f}")

        # Classify behavior based on statistics
        if std_u1 < 0.001 and std_u2 < 0.001 and std_v < 0.001:
            behavior = "Stable equilibrium"
        elif std_u1 > 0.01 or std_u2 > 0.01 or std_v > 0.01:
            # Check for periodicity
            from scipy.signal import find_peaks
            peaks_u1, _ = find_peaks(u1_steady, height=np.mean(u1_steady))
            peaks_u2, _ = find_peaks(u2_steady, height=np.mean(u2_steady))
            peaks_v, _ = find_peaks(v_steady, height=np.mean(v_steady))

            if len(peaks_u1) > 3 and len(peaks_u2) > 3 and len(peaks_v) > 3:
                # Calculate period consistency
                periods_u1 = np.diff(t[n_transient:][peaks_u1])
                period_std_u1 = np.std(periods_u1) / np.mean(periods_u1) if len(periods_u1) > 0 else np.inf

                if period_std_u1 < 0.1:  # Consistent periods
                    behavior = f"Periodic oscillations (period ≈ {np.mean(periods_u1):.1f})"
                else:
                    behavior = "Complex/chaotic oscillations"
            else:
                behavior = "Irregular oscillations"
        else:
            behavior = "Damped oscillations approaching equilibrium"

        print(f"\nSystem Behavior: {behavior}")

        # Estimate Lyapunov exponents for chaotic cases
        if "chaotic" in behavior.lower() or i == 3:  # Case 4 is tuned for chaos
            try:
                exponents = model.calculate_lyapunov_exponents(
                    ps['initial'], t_span=(0, min(ps['t_span'][1], 200))
                )
                print(f"Estimated Lyapunov exponents: {exponents}")
                max_exponent = max(exponents)
                if max_exponent > 0.01:
                    print(f"  Largest Lyapunov exponent: {max_exponent:.4f} > 0 → Chaotic behavior")
            except Exception as e:
                print(f"  Lyapunov exponent calculation failed: {e}")

        all_results.append({
            'name': ps['name'],
            'params': ps['params'],
            'means': (mean_u1, mean_u2, mean_v),
            'stds': (std_u1, std_u2, std_v),
            'behavior': behavior,
            'fig': fig
        })

        # Save figures

    # Create summary table
    print(f"\n{'='*80}")
    print("SUMMARY OF ALL CASES")
    print(f"{'='*80}")

    print("\nCase | Behavior | Species 1 (mean±std) | Species 2 (mean±std) | Predator (mean±std)")
    print("-" * 100)

    for i, result in enumerate(all_results):
        print(f"{i+1:2d} | {result['behavior'][:30]:30} | "
              f"{result['means'][0]:.3f}±{result['stds'][0]:.3f} | "
              f"{result['means'][1]:.3f}±{result['stds'][1]:.3f} | "
              f"{result['means'][2]:.3f}±{result['stds'][2]:.3f}")

    # Create behavior classification plot
    fig_summary, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.flatten()

    for i, result in enumerate(all_results):
        ax = axes[i]

        # Create a simple visualization of the behavior
        if "Stable equilibrium" in result['behavior']:
            # Show a point at the mean
            ax.scatter(result['means'][0], result['means'][1], 
                      s=100, c='green', marker='o')
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
        elif "Periodic" in result['behavior']:
            # Show a circle representing oscillations
            circle = plt.Circle((0.5, 0.5), 0.3, color='blue', 
                               fill=False, linewidth=2)
            ax.add_patch(circle)
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
        elif "Chaotic" in result['behavior']:
            # Show a fractal-like pattern
            x = np.random.rand(100) * result['stds'][0] + result['means'][0]
            y = np.random.rand(100) * result['stds'][1] + result['means'][1]
            ax.scatter(x, y, s=10, c='red', alpha=0.5)
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
        elif "Damped" in result['behavior']:
            # Show a spiral
            t_spiral = np.linspace(0, 4*np.pi, 100)
            x_spiral = 0.5 + 0.3*np.exp(-0.5*t_spiral)*np.cos(t_spiral)
            y_spiral = 0.5 + 0.3*np.exp(-0.5*t_spiral)*np.sin(t_spiral)
            ax.plot(x_spiral, y_spiral, 'orange', linewidth=2)
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)

        ax.set_title(f"Case {i+1}: {result['name'][:20]}...", fontsize=10)
        ax.set_xlabel('Species 1', fontsize=9)
        ax.set_ylabel('Species 2', fontsize=9)
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    fig_summary.suptitle('Behavior Classification of Different Cases', fontsize=16, y=1.05)


    return all_results

def parameter_sensitivity_analysis():
    """Perform sensitivity analysis on key parameters"""

    base_params = {'a': 1.0, 'b': 1.0, 'rho': 1.0, 'c1': 0.5, 
                   'c2': 0.5, 'd': 0.3, 'e1': 1.5, 'e2': 1.5}

    # Vary key parameters
    parameters_to_vary = ['d', 'e1', 'a']
    ranges = {
        'd': np.linspace(0.1, 0.8, 20),  # Predator mortality
        'e1': np.linspace(0.5, 3.0, 20),  # Conversion efficiency
        'a': np.linspace(0.1, 2.0, 20),   # Competition coefficient
    }

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    for idx, param_name in enumerate(parameters_to_vary):
        ax = axes[idx]
        param_values = ranges[param_name]
        final_u1 = []
        final_u2 = []
        final_v = []
        behaviors = []

        for param_value in param_values:
            params = base_params.copy()
            params[param_name] = param_value

            model = ComplexEcologicalModel(**params)
            sol = model.simulate([0.5, 0.3, 0.4], t_span=(0, 500))

            u1, u2, v = sol.y
            t = sol.t

            # Remove transient
            n_transient = len(t) // 5
            u1_steady = u1[n_transient:]
            u2_steady = u2[n_transient:]
            v_steady = v[n_transient:]

            # Calculate statistics
            std_u1 = np.std(u1_steady)
            std_u2 = np.std(u2_steady)
            std_v = np.std(v_steady)

            # Classify behavior
            if std_u1 < 0.001 and std_u2 < 0.001 and std_v < 0.001:
                behavior = 0  # Stable
            elif std_u1 > 0.01 or std_u2 > 0.01 or std_v > 0.01:
                behavior = 1  # Oscillatory
            else:
                behavior = 0.5  # Intermediate

            final_u1.append(np.mean(u1_steady))
            final_u2.append(np.mean(u2_steady))
            final_v.append(np.mean(v_steady))
            behaviors.append(behavior)

        # Plot results
        ax.plot(param_values, final_u1, 'b-', linewidth=2, label='Species 1')
        ax.plot(param_values, final_u2, 'g-', linewidth=2, label='Species 2')
        ax.plot(param_values, final_v, 'r-', linewidth=2, label='Predator')

        # Add background color for behavior regions
        for i in range(len(param_values)-1):
            if behaviors[i] == 0 and behaviors[i+1] == 0:
                ax.axvspan(param_values[i], param_values[i+1], 
                          alpha=0.2, color='green')
            elif behaviors[i] == 1 and behaviors[i+1] == 1:
                ax.axvspan(param_values[i], param_values[i+1], 
                          alpha=0.2, color='red')

        ax.set_xlabel(param_name, fontsize=12)
        ax.set_ylabel('Steady-state population', fontsize=12)
        ax.set_title(f'Sensitivity to {param_name}', fontsize=14)
        ax.legend(fontsize=10)
        ax.grid(True, alpha=0.3)

    plt.tight_layout()

print("Complex Ecological Model Analysis")
print("Exploring diverse dynamical behaviors in competition-predation systems\n")

# Explore diverse dynamics
results = explore_diverse_dynamics()

# Perform parameter sensitivity analysis
print("\n" + "="*80)
print("PARAMETER SENSITIVITY ANALYSIS")
print("="*80)
parameter_sensitivity_analysis()
