"""
Exercise 2: analysis of a predator-prey model with prey density dependence
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def density_dependent_model(t, state, r, K, epsilon, mu, theta):
    N, P = state
    # dN/dt = rN(1 - N/K) - εNP
    dNdt = r * N * (1 - N/K) - epsilon * N * P
    # dP/dt = -μP + θNP
    dPdt = -mu * P + theta * N * P
    return [dNdt, dPdt]

# Parameters
r = 1.0       # prey growth rate
K = 100.0     # prey carrying capacity
epsilon = 0.1 # predation efficiency
mu = 0.5      # predator mortality
theta = 0.02  # conversion efficiency

# Equilibria
# 1. Extinction (0,0)
# 2. Prey only (K, 0)
# 3. Coexistence (N*, P*):
#    -μ + θN* = 0  => N* = μ/θ
#    r(1 - N*/K) - εP* = 0 => P* = (r/ε)(1 - N*/K)
N_star = mu / theta
P_star = (r / epsilon) * (1 - N_star / K)

print(f"Parameters: r={r}, K={K}, ε={epsilon}, μ={mu}, θ={theta}")
print(f"Coexistence equilibrium: N*={N_star:.2f}, P*={P_star:.2f}")

# Jacobian analysis
def analyze_stability(N, P):
    J11 = r - 2*r*N/K - epsilon*P
    J12 = -epsilon * N
    J21 = theta * P
    J22 = -mu + theta * N
    J = np.array([[J11, J12], [J21, J22]])
    evals = np.linalg.eigvals(J)
    return evals

print("\n(0,0) stability:", analyze_stability(0, 0))
print(f"({K},0) stability:", analyze_stability(K, 0))
if P_star > 0:
    evals = analyze_stability(N_star, P_star)
    print(f"({N_star:.2f},{P_star:.2f}) eigenvalues:", evals)
    if np.all(np.real(evals) < 0):
        print(" -> Stable")
        if np.iscomplex(evals[0]):
            print(" -> Stable focus (damped oscillations)")
    else:
        print(" -> Unstable")

# Numerical simulation
t_span = (0, 100)
t_eval = np.linspace(0, 100, 1000)
init_state = [10, 5] # initial populations
sol = solve_ivp(density_dependent_model, t_span, init_state, t_eval=t_eval,
                args=(r, K, epsilon, mu, theta))

# Plotting

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Time series
ax1.plot(sol.t, sol.y[0], 'g-', label='Prey (N)')
ax1.plot(sol.t, sol.y[1], 'r-', label='Predator (P)')
ax1.set_xlabel('Time')
ax1.set_ylabel('Population')
ax1.set_title('Time Series: Damped Oscillations')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Phase portrait
ax2.plot(sol.y[0], sol.y[1], 'b-', linewidth=1.5)
ax2.plot(sol.y[0][0], sol.y[1][0], 'go', label='Start') # start point
ax2.plot(N_star, P_star, 'r*', markersize=12, label='Equilibrium') # equilibrium
# Draw nullclines
n_vals = np.linspace(0, K*1.1, 100)
p_null_prey = (r/epsilon)*(1 - n_vals/K) # dN/dt=0 => P = r/ε(1-N/K)
ax2.plot(n_vals, p_null_prey, 'g--', alpha=0.5, label='dN/dt=0')
ax2.axvline(N_star, color='r', linestyle='--', alpha=0.5, label='dP/dt=0')

ax2.set_xlabel('Prey (N)')
ax2.set_ylabel('Predator (P)')
ax2.set_title('Phase Portrait: Spiral Sink')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()

# Classic Lotka-Volterra model (dimensionless: dx/dt = x(1 - y), dy/dt = α y(x - 1))
def classic_lv(t, state, alpha):
    x, y = state
    dxdt = x * (1 - y)
    dydt = alpha * y * (x - 1)
    return [dxdt, dydt]

# Model with density dependence (dimensionless: dx/dt = x(1 - x - y), dy/dt = α y(β x - 1))
def logistic_lv(t, state, alpha, beta):
    x, y = state
    dxdt = x * (1 - x - y)
    dydt = alpha * y * (beta * x - 1)
    return [dxdt, dydt]

# Parameters
alpha = 1.0          # α = μ/r
beta = 2.0           # β = θK/r (>1 guarantees a coexistence equilibrium)
t_span = (0, 50)
t_eval = np.linspace(0, 50, 2000)

# Initial conditions (slightly off equilibrium)
x0, y0 = 0.4, 0.5    # Classic equilibrium is (1,1); scalings differ, for illustration only
# The classic equilibrium (1,1) corresponds to (μ/θ, r/ε) in original variables; would the classic model need other parameters?
# For a fair comparison we use the same dimensionless form; the classic model has no β, so with α=1 its equilibrium is (1,1)
# while the density-dependent equilibrium is (1/β, 1-1/β) = (0.5, 0.5)
# Hence we start both from (0.6, 0.4) to compare their behaviour from the same initial point.

# Simulate the classic model
sol_classic = solve_ivp(classic_lv, t_span, [0.6, 0.4], args=(alpha,), t_eval=t_eval, method='RK45')

# Simulate the density-dependent model
sol_logistic = solve_ivp(logistic_lv, t_span, [0.6, 0.4], args=(alpha, beta), t_eval=t_eval, method='RK45')

# Plotting
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Classic model: phase plane
ax = axes[0,0]
ax.plot(sol_classic.y[0], sol_classic.y[1], 'b-', lw=1.5)
ax.plot(sol_classic.y[0,0], sol_classic.y[1,0], 'ro', label='start')
ax.plot(1, 1, 'g*', markersize=10, label='center (1,1)')
ax.set_xlabel('Prey x')
ax.set_ylabel('Predator y')
ax.set_title('Classic LV: phase plane')
ax.grid(True, alpha=0.3)
ax.legend()

# Classic model: time series
ax = axes[1,0]
ax.plot(sol_classic.t, sol_classic.y[0], 'b-', label='prey')
ax.plot(sol_classic.t, sol_classic.y[1], 'r-', label='predator')
ax.set_xlabel('Time τ')
ax.set_ylabel('Population')
ax.set_title('Classic LV: time series')
ax.grid(True, alpha=0.3)
ax.legend()

# Density-dependent model: phase plane
ax = axes[0,1]
ax.plot(sol_logistic.y[0], sol_logistic.y[1], 'b-', lw=1.5)
ax.plot(sol_logistic.y[0,0], sol_logistic.y[1,0], 'ro', label='start')
x_star = 1/beta
y_star = 1 - x_star
ax.plot(x_star, y_star, 'g*', markersize=10, label=f'stable node ({x_star:.2f},{y_star:.2f})')
ax.set_xlabel('Prey x')
ax.set_ylabel('Predator y')
ax.set_title('Logistic LV: phase plane')
ax.grid(True, alpha=0.3)
ax.legend()

# Density-dependent model: time series
ax = axes[1,1]
ax.plot(sol_logistic.t, sol_logistic.y[0], 'b-', label='prey')
ax.plot(sol_logistic.t, sol_logistic.y[1], 'r-', label='predator')
ax.set_xlabel('Time τ')
ax.set_ylabel('Population')
ax.set_title('Logistic LV: time series')
ax.grid(True, alpha=0.3)
ax.legend()

plt.tight_layout()
