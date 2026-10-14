"""
Exercise 3: fitting the Lotka-Volterra model to the Hudson's Bay lynx-hare data
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import minimize

# Data
years = np.arange(1900, 1921)
hares_data = np.array([30, 47.2, 70.2, 77.4, 36.3, 20.6, 18.1, 21.4, 22.0, 25.4, 27.1, 40.3, 57, 76.6, 52.3, 19.5, 11.2, 7.6, 14.6, 16.2, 24.7])
lynx_data = np.array([4, 6.1, 9.8, 35.2, 59.4, 41.7, 19, 13, 8.3, 9.1, 7.4, 8, 12.3, 19.5, 45.7, 51.1, 29.7, 15.8, 9.7, 10.1, 8.6])

# Classic Lotka-Volterra model
# H' = a*H - b*H*L
# L' = -c*L + d*H*L
def lotka_volterra(t, z, a, b, c, d):
    H, L = z
    dHdt = a*H - b*H*L
    dLdt = -c*L + d*H*L
    return [dHdt, dLdt]

# Loss function: mean squared error (MSE) between model and data
def objective(params):
    a, b, c, d = params
    # Parameters must be positive
    if any(p <= 0 for p in params):
        return 1e9

    # Use the first data point as the initial condition
    initial_state = [hares_data[0], lynx_data[0]]

    # Solve the ODE
    try:
        sol = solve_ivp(lotka_volterra,
                        (years[0], years[-1]),
                        initial_state,
                        t_eval=years,
                        args=(a, b, c, d),
                        method='RK45')
    except:
        return 1e9

    if sol.status != 0 or len(sol.t) != len(years):
        return 1e9

    # Error (species could be weighted; here we simply sum)
    mse_h = np.mean((sol.y[0] - hares_data)**2)
    mse_l = np.mean((sol.y[1] - lynx_data)**2)

    return mse_h + mse_l

# Initial parameter guess
# Rough estimate from the period: T ≈ 10 years (1900-1910, 1910-1920)
# Period formula T ≈ 2π / sqrt(a*c) -> a*c ≈ (2π/10)^2 ≈ 0.4
# Means H_bar = c/d ≈ 30, L_bar = a/b ≈ 20 (rough estimate)
initial_guess = [0.5, 0.02, 0.8, 0.02]

print("Optimizing parameters...")
res = minimize(objective, initial_guess, method='Nelder-Mead', tol=1e-4)

best_params = res.x
print(f"Best-fit parameters: a={best_params[0]:.4f}, b={best_params[1]:.4f}, c={best_params[2]:.4f}, d={best_params[3]:.4f}")
print(f"Fit error (MSE): {res.fun:.2f}")

# Simulate with the best-fit parameters
t_fine = np.linspace(years[0], years[-1], 200)
sol_best = solve_ivp(lotka_volterra,
                     (years[0], years[-1]),
                     [hares_data[0], lynx_data[0]],
                     t_eval=t_fine,
                     args=tuple(best_params))

# Plotting

plt.figure(figsize=(12, 6))

# Raw data points
plt.scatter(years, hares_data, color='green', label='Data: Hares (Prey)')
plt.scatter(years, lynx_data, color='red', label='Data: Lynx (Predator)')

# Fitted curves
plt.plot(sol_best.t, sol_best.y[0], 'g--', label='Fit: Hares')
plt.plot(sol_best.t, sol_best.y[1], 'r--', label='Fit: Lynx')

plt.xlabel('Year')
plt.ylabel('Population (x1000)')
plt.title('Lynx-Hare Cycle: Data vs. Lotka-Volterra Fit')
plt.legend()
plt.grid(True, alpha=0.3)

# Phase-plane plot
plt.figure(figsize=(8, 6))
plt.plot(hares_data, lynx_data, 'ko-', alpha=0.3, label='Data Trajectory')
plt.plot(sol_best.y[0], sol_best.y[1], 'b-', linewidth=2, label='Model Cycle')
plt.xlabel('Hares (x1000)')
plt.ylabel('Lynx (x1000)')
plt.title('Phase Portrait: Limit Cycle Analysis')
plt.legend()
plt.grid(True)
