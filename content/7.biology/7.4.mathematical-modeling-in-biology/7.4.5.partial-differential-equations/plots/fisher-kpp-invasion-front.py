"""
invasive_species_model.py
Invasive species spread model
"""

import numpy as np
import matplotlib.pyplot as plt

class InvasiveSpeciesModel:
    """Invasive species spread model"""

    def __init__(self, D=10.0, r=0.5, K=1.0, L=500.0, T=50.0):
        """
        Initialise the invasion model

        Parameters:
        D : diffusion coefficient (km²/year)
        r : annual growth rate
        K : carrying capacity
        L : length of the spatial domain (km)
        T : simulation time (years)
        """
        self.D = D
        self.r = r
        self.K = K
        self.L = L
        self.T = T

        # Space and time discretisation
        self.dx = 5.0  # spatial step (km)
        self.dt = 0.1  # time step (years)

        self.Nx = int(L / self.dx) + 1
        self.Nt = int(T / self.dt) + 1

        self.x = np.linspace(0, L, self.Nx)
        self.t = np.linspace(0, T, self.Nt)

    def simulate_invasion(self, initial_location=100.0, initial_radius=10.0):
        """Simulate the invasion process"""
        # Initial condition: local introduction
        u0 = np.zeros(self.Nx)
        center_idx = np.argmin(np.abs(self.x - initial_location))
        radius_idx = int(initial_radius / self.dx)

        start_idx = max(0, center_idx - radius_idx)
        end_idx = min(self.Nx, center_idx + radius_idx)
        u0[start_idx:end_idx] = 0.1 * self.K

        # Numerical solution
        u = u0.copy()
        u_history = [u.copy()]

        alpha = self.D * self.dt / (self.dx ** 2)

        for n in range(1, self.Nt):
            u_new = u.copy()

            # Explicit update
            for i in range(1, self.Nx-1):
                diffusion = alpha * (u[i+1] - 2*u[i] + u[i-1])
                reaction = self.dt * self.r * u[i] * (1 - u[i]/self.K)
                u_new[i] = u[i] + diffusion + reaction

            # Neumann boundary conditions
            u_new[0] = u_new[1]
            u_new[-1] = u_new[-2]

            u = u_new.copy()

            # Save every 10 years
            if n % int(10/self.dt) == 0:
                u_history.append(u.copy())

        return np.array(u_history)

    def plot_invasion_front(self, u_history):
        """Plot the invasion front"""
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))

        # Spatial distribution over time
        years = np.arange(0, self.T+1, 10)
        for i, u in enumerate(u_history):
            axes[0].plot(self.x, u, label=f'Year {years[i]}', alpha=0.7)

        axes[0].set_xlabel('Distance from origin (km)', fontsize=12)
        axes[0].set_ylabel('Population density', fontsize=12)
        axes[0].set_title('Invasion Front Propagation', fontsize=14)
        axes[0].legend(fontsize=10)
        axes[0].grid(True, alpha=0.3)

        # Compute the wave speed
        threshold = 0.1 * self.K
        wave_positions = []
        times = []

        for i, u in enumerate(u_history):
            # Find the farthest position where density exceeds the threshold
            idx = np.where(u >= threshold)[0]
            if len(idx) > 0:
                wave_positions.append(self.x[idx[-1]])
                times.append(years[i])

        if len(wave_positions) > 2:
            # Linear fit (numerical speed)
            times_arr = np.array(times)
            coeffs = np.polyfit(times_arr, wave_positions, 1)
            numerical_speed = coeffs[0]
            intercept = coeffs[1]

            axes[1].plot(times, wave_positions, 'bo-', label='Wave front position')
            axes[1].plot(times, np.polyval(coeffs, times), 'r--', 
                        label=f'Numerical Speed: {numerical_speed:.2f} km/year')

            # Theoretical wave speed
            theoretical_speed = 2 * np.sqrt(self.D * self.r)

            # To compare slopes, draw a line with the theoretical slope
            # passing through the middle data point for easy visual comparison
            mid_time = times_arr[len(times)//2]
            mid_pos = wave_positions[len(times)//2]
            theoretical_line = mid_pos + theoretical_speed * (times_arr - mid_time)

            axes[1].plot(times, theoretical_line, 'g:', linewidth=2,
                        label=f'Theoretical Speed: {theoretical_speed:.2f} km/year')

            # Add explanatory text
            info_text = (
                f"$c_{{min}} = 2\\sqrt{{rD}} = {theoretical_speed:.2f}$\n"
                f"$c_{{num}} \\approx {numerical_speed:.2f}$"
            )
            axes[1].text(0.05, 0.95, info_text, transform=axes[1].transAxes, 
                        fontsize=12, verticalalignment='top',
                        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

        axes[1].set_xlabel('Time (years)', fontsize=12)
        axes[1].set_ylabel('Wave front position (km)', fontsize=12)
        axes[1].set_title('Invasion Speed', fontsize=14)
        axes[1].legend(fontsize=10)
        axes[1].grid(True, alpha=0.3)

        plt.tight_layout()

        return numerical_speed if 'numerical_speed' in locals() else None

# Example: zebra mussel invasion simulation
def zebra_mussel_invasion():
    """Simulate a zebra mussel invasion"""
    # Parameter estimates (based on literature data)
    D = 15.0  # diffusion coefficient (km²/year), accounting for boat transport
    r = 0.8   # annual growth rate
    K = 1.0   # relative carrying capacity

    print("\n" + "="*60)
    print("FISHER-KPP EQUATION: TRAVELING WAVE ANALYSIS")
    print("="*60)
    print(f"Model parameters:")
    print(f"  Diffusion coefficient (D): {D} km²/year")
    print(f"  Growth rate (r): {r} /year")
    print(f"  Carrying capacity (K): {K}")
    print("-" * 60)
    print("Theoretical Background:")
    print("  The Fisher-KPP equation admits traveling wave solutions of the form:")
    print("    u(x,t) = U(z), where z = x - ct")
    print("  For initial conditions with compact support (localized population),")
    print("  the wave front propagates asymptotically at the minimum wave speed:")
    print("    c_min = 2 * sqrt(r * D)")

    c_theoretical = 2 * np.sqrt(D * r)
    print(f"  Calculated c_min: {c_theoretical:.4f} km/year")
    print("-" * 60)

    model = InvasiveSpeciesModel(D=D, r=r, K=K, L=500.0, T=30.0)
    print("Running numerical simulation...")
    u_history = model.simulate_invasion(initial_location=100.0, initial_radius=20.0)

    print("Analyzing wave front propagation...")
    numerical_speed = model.plot_invasion_front(u_history)

    if numerical_speed:
        print(f"Numerical result:")
        print(f"  Estimated wave speed: {numerical_speed:.4f} km/year")
        error = abs(numerical_speed - c_theoretical) / c_theoretical * 100
        print(f"  Relative error: {error:.2f}%")
        print("Note: Numerical speed convergence requires long times and fine grids.")
        print("      Small discrepancies are expected in finite-time simulations.")

zebra_mussel_invasion()
