import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def logistic_growth(t, N0, r, K):
    """Logistic growth function"""
    return K / (1 + (K - N0) / N0 * np.exp(-r * t))

# Generate synthetic data (with noise)
np.random.seed(42)
t_data = np.linspace(0, 20, 21)
N0_true, r_true, K_true = 10, 0.5, 500
N_data = logistic_growth(t_data, N0_true, r_true, K_true) + np.random.normal(0, 20, len(t_data))

# Fit parameters
p0 = [5, 0.3, 300]  # Initial guess
params, params_cov = curve_fit(logistic_growth, t_data, N_data, p0=p0)
N0_fit, r_fit, K_fit = params

# Plot the fitted curve
t_fine = np.linspace(0, 20, 200)
N_fit = logistic_growth(t_fine, N0_fit, r_fit, K_fit)

plt.figure(figsize=(8, 6))
plt.scatter(t_data, N_data, label='Data Points', c='k')
plt.plot(t_fine, N_fit, 'r-', label='Fitted Curve')
plt.xlabel('Time', fontsize=14)
plt.ylabel('Population Size', fontsize=14)
plt.title('Logistic Growth Curve Fitting', fontsize=16)

# Show the fitted parameters in the figure
param_text = f'$N_0 = {N0_fit:.2f}$\n$r = {r_fit:.4f}$\n$K = {K_fit:.2f}$'
plt.text(0.95, 0.15, param_text, transform=plt.gca().transAxes, 
         fontsize=12, verticalalignment='bottom', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))

plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
