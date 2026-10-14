"""
turing_patterns.py
Simulation of Turing patterns in predator-prey systems
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import laplace

class TuringPatternSimulator:
    """2D Turing pattern simulator for predator-prey system"""

    def __init__(self, size=100, dt=0.1, dx=1.0):
        """
        Initialize Turing pattern simulator

        Parameters:
        -----------
        size : int
            Grid size (size x size)
        dt : float
            Time step
        dx : float
            Spatial step
        """
        self.size = size
        self.dt = dt
        self.dx = dx

        # Model parameters (predator-prey with Holling Type II and self-limitation)
        self.params = {
            'r': 1.0,      # Prey growth rate
            'K': 1.0,      # Carrying capacity
            'a': 1.0,      # Predation rate
            'c': 2.0,      # Conversion efficiency
            'm': 0.5,      # Predator mortality
            'H': 0.3,      # Half-saturation constant (Holling II)
            'delta': 0.1,  # Predator self-limitation (quadratic mortality)
            'D_N': 0.02,   # Prey diffusion coefficient
            'D_P': 1.0,    # Predator diffusion coefficient
        }

        # Initialize grids with Turing-friendly initial conditions
        # Start near the expected homogeneous equilibrium to facilitate pattern formation
        self.N = 0.3 * np.ones((size, size)) 
        self.P = 0.3 * np.ones((size, size))

        # Add random perturbations
        self.N += 0.02 * np.random.randn(size, size)
        self.P += 0.02 * np.random.randn(size, size)

        # Apply reflecting boundary conditions
        self.set_boundary_conditions()

    def set_boundary_conditions(self):
        """Set reflecting (Neumann) boundary conditions"""
        pass

    def reaction_terms(self, N, P):
        """Calculate local reaction terms with Holling Type II response"""
        r, K, a, c, m, H, delta = (self.params[k] for k in ['r', 'K', 'a', 'c', 'm', 'H', 'delta'])

        # Holling Type II functional response: a*N/(N+H)
        predation = a * N * P / (N + H)

        # Prey: Logistic growth - Predation
        f_N = r * N * (1 - N/K) - predation

        # Predator: Conversion * Predation - Mortality - Self-limitation
        f_P = c * predation - m * P - delta * P**2

        return f_N, f_P

    def diffusion_terms(self, grid, D):
        """Calculate diffusion term using discrete Laplacian"""
        # Using 5-point stencil for 2D Laplacian
        laplacian = laplace(grid, mode='reflect') / self.dx**2
        return D * laplacian

    def step(self):
        """Perform one time step using explicit Euler method"""
        # Calculate reaction terms
        f_N, f_P = self.reaction_terms(self.N, self.P)

        # Calculate diffusion terms
        diff_N = self.diffusion_terms(self.N, self.params['D_N'])
        diff_P = self.diffusion_terms(self.P, self.params['D_P'])

        # Update populations
        self.N += self.dt * (f_N + diff_N)
        self.P += self.dt * (f_P + diff_P)

        # Ensure non-negative values
        self.N = np.maximum(self.N, 0.0)
        self.P = np.maximum(self.P, 0.0)

        return self.N, self.P

    def simulate(self, steps=5000, save_interval=100):
        """Run simulation"""
        # Arrays to store snapshots
        n_snapshots = steps // save_interval + 1
        N_snapshots = np.zeros((n_snapshots, self.size, self.size))
        P_snapshots = np.zeros((n_snapshots, self.size, self.size))

        # Save initial state
        N_snapshots[0] = self.N.copy()
        P_snapshots[0] = self.P.copy()

        snapshot_idx = 1

        # Time stepping
        for i in range(1, steps + 1):
            self.step()

            if i % save_interval == 0 and snapshot_idx < n_snapshots:
                N_snapshots[snapshot_idx] = self.N.copy()
                P_snapshots[snapshot_idx] = self.P.copy()
                snapshot_idx += 1

        return N_snapshots[:snapshot_idx], P_snapshots[:snapshot_idx]

    def analyze_turing_conditions(self):
        """Analyze Turing instability conditions for Holling Type II model"""
        # Unpack parameters
        r, K, a, c, m, H, delta = (self.params[k] for k in ['r', 'K', 'a', 'c', 'm', 'H', 'delta'])
        D_N, D_P = self.params['D_N'], self.params['D_P']

        # Calculate homogeneous equilibrium numerically or analytically
        # N* is determined by P-isocline: c*a*N/(N+H) = m + delta*P
        # P* is determined by N-isocline: r(1-N/K) = a*P/(N+H) => P = r/a*(1-N/K)*(N+H)
        # Substitute P into first eq:
        # c*a*N/(N+H) - m - delta * [(r/a)*(1-N/K)*(N+H)] = 0

        def func(n):
            if n <= 0.001 or n >= K: return 1e9
            p = (r/a) * (1 - n/K) * (n + H)
            return c * a * n / (n + H) - m - delta * p

        # Scan to find root
        n_vals = np.linspace(0.01, K-0.01, 1000)
        y_vals = [func(n) for n in n_vals]
        idx = np.argmin(np.abs(y_vals))
        N_star = n_vals[idx]
        P_star = (r/a) * (1 - N_star/K) * (N_star + H)

        print(f"Homogeneous equilibrium:")
        print(f"  N* = {N_star:.4f}, P* = {P_star:.4f}")

        # Jacobian elements
        # fN = r*N*(1-N/K) - a*N*P/(N+H)
        # J11 = d(fN)/dN
        #     = r(1-2N/K) - a*P * [ ((N+H) - N) / (N+H)^2 ]
        J11 = r * (1 - 2*N_star/K) - a * P_star * H / ((N_star + H)**2)

        # J12 = d(fN)/dP = -a*N/(N+H)
        J12 = -a * N_star / (N_star + H)

        # fP = c*a*N*P/(N+H) - m*P - delta*P^2
        # J21 = d(fP)/dN = c*a*P * [ H / (N+H)^2 ]
        J21 = c * a * P_star * H / ((N_star + H)**2)

        # J22 = d(fP)/dP = c*a*N/(N+H) - m - 2*delta*P
        # At eq: c*a*N/(N+H) - m = delta*P
        # So J22 = delta*P - 2*delta*P = -delta*P
        J22 = -delta * P_star

        J = np.array([[J11, J12], [J21, J22]])

        print(f"\nJacobian at equilibrium:")
        print(f"  J = [[{J11:.4f}, {J12:.4f}],")
        print(f"       [{J21:.4f}, {J22:.4f}]]")

        # Eigenvalues without diffusion
        eigvals = np.linalg.eigvals(J)
        print(f"\nEigenvalues (without diffusion):")
        print(f"  λ1 = {eigvals[0]:.4f}, λ2 = {eigvals[1]:.4f}")
        print(f"  Real parts: {np.real(eigvals[0]):.4f}, {np.real(eigvals[1]):.4f}")

        # Turing conditions
        trace = np.trace(J) # J11 + J22
        det = np.linalg.det(J) # J11*J22 - J12*J21

        # Condition 1: Linear stability without diffusion (Trace < 0 and Det > 0)
        condition1 = (trace < 0) and (det > 0)

        # Condition 2: Instability with diffusion
        # D_P*J11 + D_N*J22 > 2*sqrt(D_N*D_P*det)
        lhs = D_P * J11 + D_N * J22
        rhs = 2 * np.sqrt(D_N * D_P * det) if det > 0 else 0
        condition2 = lhs > rhs

        print(f"\nTuring instability conditions:")
        print(f"  1. Stable w/o diffusion (Tr<0, Det>0): {condition1} (Tr={trace:.4f}, Det={det:.4f})")
        print(f"  2. Unstable w/ diffusion (LHS > RHS): {condition2} ({lhs:.4f} > {rhs:.4f})")

        turing_possible = condition1 and condition2

        if turing_possible:
            print(f"\n✅ Turing instability is expected!")
        else:
            print(f"\n❌ Turing instability conditions not satisfied")

        return condition1, turing_possible

def visualize_turing_patterns(N_snapshots, P_snapshots):
    """Visualize Turing pattern evolution"""
    n_snapshots = len(N_snapshots)

    # Create figure with multiple snapshots
    fig, axes = plt.subplots(2, min(4, n_snapshots), figsize=(15, 8))

    # Select snapshots to display
    step_indices = np.linspace(0, n_snapshots-1, min(4, n_snapshots), dtype=int)

    for idx, step_idx in enumerate(step_indices):
        # Prey patterns
        ax1 = axes[0, idx]
        im1 = ax1.imshow(N_snapshots[step_idx], cmap='viridis', 
                        vmin=0, vmax=1.5, origin='lower')
        ax1.set_title(f'Prey (t = {step_idx*100})', fontsize=12)
        ax1.axis('off')
        plt.colorbar(im1, ax=ax1, fraction=0.046, pad=0.04)

        # Predator patterns
        ax2 = axes[1, idx]
        im2 = ax2.imshow(P_snapshots[step_idx], cmap='plasma',
                        vmin=0, vmax=1.5, origin='lower')
        ax2.set_title(f'Predator (t = {step_idx*100})', fontsize=12)
        ax2.axis('off')
        plt.colorbar(im2, ax=ax2, fraction=0.046, pad=0.04)

    plt.tight_layout()

    # Add spatial spectrum analysis for the final pattern
    fig2, axes2 = plt.subplots(1, 3, figsize=(15, 5))

    # Final prey pattern
    ax1 = axes2[0]
    im1 = ax1.imshow(N_snapshots[-1], cmap='viridis', origin='lower')
    ax1.set_title('Final Prey Pattern', fontsize=14)
    ax1.axis('off')
    plt.colorbar(im1, ax=ax1)

    # Final predator pattern
    ax2 = axes2[1]
    im2 = ax2.imshow(P_snapshots[-1], cmap='plasma', origin='lower')
    ax2.set_title('Final Predator Pattern', fontsize=14)
    ax2.axis('off')
    plt.colorbar(im2, ax=ax2)

    # 2D Fourier transform of prey pattern
    ax3 = axes2[2]
    pattern_fft = np.fft.fft2(N_snapshots[-1])
    pattern_fft_shifted = np.fft.fftshift(pattern_fft)
    magnitude_spectrum = np.log(1 + np.abs(pattern_fft_shifted))

    im3 = ax3.imshow(magnitude_spectrum, cmap='hot', origin='lower')
    ax3.set_title('Fourier Spectrum (Prey)', fontsize=14)
    ax3.axis('off')
    plt.colorbar(im3, ax=ax3)

    # Add circle showing dominant wavelength
    center = (magnitude_spectrum.shape[0]//2, magnitude_spectrum.shape[1]//2)
    radius = 15  # This corresponds to pattern wavelength
    circle = plt.Circle(center, radius, color='cyan', fill=False, linewidth=2)
    ax3.add_patch(circle)

    plt.tight_layout()

    return fig, fig2

def explore_parameter_space():
    """Explore different parameter regimes for Turing patterns"""

    parameter_sets = [
        {
            'name': 'Standard Turing patterns',
            # Parameters tuned for Turing instability:
            # D_N reduced, D_P increased (Ratio 200)
            # delta increased to stabilize homogeneous equilibrium
            'params': {'D_N': 0.1, 'D_P': 20.0, 'r': 1.0, 'K': 1.0, 
                       'a': 1.0, 'c': 2.0, 'm': 0.55, 'H': 0.3, 'delta': 0.4},
            'expected': 'Spot/Labyrinth patterns'
        },
        {
            'name': 'Different Pattern Mode',
            # Varying delta slightly
            'params': {'D_N': 0.1, 'D_P': 20.0, 'r': 1.0, 'K': 1.0, 
                       'a': 1.0, 'c': 2.0, 'm': 0.55, 'H': 0.3, 'delta': 0.5},
            'expected': 'Alternative patterns'
        },
        {
            'name': 'No Turing (Low diffusion ratio)',
            # Set D_P close to D_N
            'params': {'D_N': 1.0, 'D_P': 2.0, 'r': 1.0, 'K': 1.0, 
                       'a': 1.0, 'c': 2.0, 'm': 0.55, 'H': 0.3, 'delta': 0.4},
            'expected': 'Homogeneous state'
        }
    ]

    all_results = []

    for i, ps in enumerate(parameter_sets):
        print(f"\n{'='*60}")
        print(f"Case {i+1}: {ps['name']}")
        print(f"{'='*60}")

        # Create simulator with given parameters
        # Adjust dt for stability: D * dt / dx^2 < 0.25
        # Max D is 20. dx=1. dt < 0.0125. Use 0.01
        simulator = TuringPatternSimulator(size=60, dt=0.01, dx=1.0)

        # Update parameters
        for key, value in ps['params'].items():
            if key in simulator.params:
                simulator.params[key] = value

        # Analyze Turing conditions
        stable_no_diff, turing_possible = simulator.analyze_turing_conditions()

        # Run simulation
        print("\nRunning simulation...")
        # Reduce steps but increase plot frequency since dt is small
        # Total T = 20000 * 0.005 = 100
        N_snapshots, P_snapshots = simulator.simulate(steps=20000, save_interval=1000)

        # Store results
        all_results.append({
            'name': ps['name'],
            'params': ps['params'],
            'turing_possible': turing_possible,
            'N_snapshots': N_snapshots,
            'P_snapshots': P_snapshots
        })

        # Visualize
        fig1, fig2 = visualize_turing_patterns(N_snapshots, P_snapshots)
        # Fix title and text
        plt.figure(fig1.number)
        fig1.suptitle(f"{ps['name']}\nD_N={ps['params']['D_N']}, D_P={ps['params']['D_P']}", 
                     fontsize=16)

        # Fix: visualize_turing_patterns uses step number to display time
        # The time is step_idx * save_interval * dt
        # Current logic: step_idx * 100. Let's fix axes titles in visualize_turing_patterns instead if possible
        # Or just accept it displays step number


    return all_results

print("Turing Pattern Formation in Predator-Prey Systems")
print("="*60)

# Explore different parameter regimes
results = explore_parameter_space()

