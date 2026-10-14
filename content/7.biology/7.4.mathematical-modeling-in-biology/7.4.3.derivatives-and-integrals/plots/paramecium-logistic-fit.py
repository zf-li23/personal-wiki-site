import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import linregress
from sklearn.metrics import r2_score


# Experimental data
t = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
N = np.array([9.6, 18.3, 29.0, 47.2, 71.1, 119.1, 174.6, 257.3, 350.7, 
              441.0, 513.3, 559.7, 594.8, 629.4, 640.9, 651.1, 655.9, 659.6, 661.8])

# ====================== Method 1: nonlinear least squares ======================
def logistic_model(t, K, r, N0):
    return K / (1 + ((K - N0) / N0) * np.exp(-r * t))

# Initial parameter guess (K ≈ 660, r ≈ 0.5, N0 ≈ 10)
initial_guess = [660, 0.5, 10]
params_nonlin, cov_nonlin = curve_fit(logistic_model, t, N, p0=initial_guess, maxfev=5000)
K_nonlin, r_nonlin, N0_nonlin = params_nonlin
# Standard errors of the parameters
params_err_nonlin = np.sqrt(np.diag(cov_nonlin))

# Predictions and goodness of fit
N_pred_nonlin = logistic_model(t, K_nonlin, r_nonlin, N0_nonlin)
SSE_nonlin = np.sum((N - N_pred_nonlin)**2)
R2_nonlin = r2_score(N, N_pred_nonlin)
RMSE_nonlin = np.sqrt(SSE_nonlin / len(N))

# ====================== Method 2: linearized fit (three-point method) ======================
# Pick three equally spaced points: t=0, t=9, t=18
idx0, idx1, idx2 = 0, 9, 18
N0_data, N1_data, N2_data = N[idx0], N[idx1], N[idx2]
Δt = t[idx1] - t[idx0]

# Three-point estimate of K
K_linear = (N1_data**2 * (N0_data + N2_data) - 2 * N0_data * N1_data * N2_data) / (N1_data**2 - N0_data * N2_data)

# Linear regression for r and N0
# Note: (K-N)/N may be zero or negative when N is close to K, so only points with N < K are used
valid_mask = N < K_linear * 0.999  # Avoid non-positive arguments to the log
t_valid = t[valid_mask]
N_valid = N[valid_mask]

# Compute y = ln((K-N)/N)
y = np.log((K_linear - N_valid) / N_valid)

# Linear regression: y = a - r*t
slope, intercept, r_value, p_value, std_err = linregress(t_valid, y)
r_linear = -slope
a = intercept
# Compute N0
N0_linear = K_linear / (1 + np.exp(a))

# Predictions and goodness of fit
N_pred_linear = logistic_model(t, K_linear, r_linear, N0_linear)
SSE_linear = np.sum((N - N_pred_linear)**2)
R2_linear = r2_score(N, N_pred_linear)
RMSE_linear = np.sqrt(SSE_linear / len(N))

# ====================== Visualization ======================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Data and fitted curves
ax1 = axes[0, 0]
ax1.scatter(t, N, color='black', s=50, label='Observed Data', zorder=5)
t_fine = np.linspace(0, 20, 200)
ax1.plot(t_fine, logistic_model(t_fine, K_nonlin, r_nonlin, N0_nonlin), 
         'r-', linewidth=2, label='Non-linear Fit', alpha=0.8)
ax1.plot(t_fine, logistic_model(t_fine, K_linear, r_linear, N0_linear), 
         'b--', linewidth=2, label='Linearized Fit', alpha=0.8)
ax1.set_xlabel('Time t (h)', fontsize=12)
ax1.set_ylabel('Population Density N (ind./mL)', fontsize=12)
ax1.set_title('Logistic Model Fit of Paramecium Population Growth', fontsize=14)
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3)

# 2. Residuals
ax2 = axes[0, 1]
residuals_nonlin = N - N_pred_nonlin
residuals_linear = N - N_pred_linear
ax2.scatter(t, residuals_nonlin, color='red', s=40, alpha=0.7, label='Non-linear Fit Residuals')
ax2.scatter(t, residuals_linear, color='blue', s=40, alpha=0.7, label='Linearized Fit Residuals')
ax2.axhline(y=0, color='black', linestyle='--', alpha=0.5)
ax2.set_xlabel('Time t (h)', fontsize=12)
ax2.set_ylabel('Residuals', fontsize=12)
ax2.set_title('Residual Comparison', fontsize=14)
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3)

# 3. Linearized fit
ax3 = axes[1, 0]
ax3.scatter(t_valid, y, color='blue', s=40, label='Linearized Data')
# Regression line
y_fit = intercept + slope * t_valid
ax3.plot(t_valid, y_fit, 'r-', linewidth=2, label=f'Linear Regression: y = {intercept:.3f} - {r_linear:.3f}t')
ax3.set_xlabel('Time t (h)', fontsize=12)
ax3.set_ylabel('ln((K-N)/N)', fontsize=12)
ax3.set_title(f'Linearization Process (3-point method K = {K_linear:.1f})', fontsize=14)
ax3.legend(fontsize=10)
ax3.grid(True, alpha=0.3)

# 4. Goodness-of-fit statistics
ax4 = axes[1, 1]
methods = ['Non-linear Fit', 'Linearized Fit']
SSE_values = [SSE_nonlin, SSE_linear]
R2_values = [R2_nonlin, R2_linear]
x = np.arange(len(methods))
width = 0.35

# Plot SSE on primary y-axis
bar1 = ax4.bar(x - width/2, SSE_values, width, label='SSE', color='skyblue')
ax4.set_xlabel('Fitting Method', fontsize=12)
ax4.set_ylabel('SSE', fontsize=12, color='steelblue')
ax4.tick_params(axis='y', labelcolor='steelblue')
ax4.set_title('Goodness of Fit Comparison', fontsize=14)
ax4.set_xticks(x)
ax4.set_xticklabels(methods)

# Plot R2 on secondary y-axis
ax4_twin = ax4.twinx()
bar2 = ax4_twin.bar(x + width/2, R2_values, width, label='R²', color='lightcoral')
ax4_twin.set_ylabel('R²', fontsize=12, color='indianred')
ax4_twin.set_ylim(0, 1.1)  # R² is usually <= 1
ax4_twin.tick_params(axis='y', labelcolor='indianred')

# Add legends
lines1, labels1 = [bar1], ['SSE']
lines2, labels2 = [bar2], ['R²']
ax4.legend(lines1 + lines2, labels1 + labels2, loc='upper center', fontsize=10)

ax4.grid(True, alpha=0.3, axis='y')

# Annotate the bars with values
for i, sse in enumerate(SSE_values):
    ax4.text(i - width/2, sse + max(SSE_values)*0.01, f'{sse:.1f}', 
             ha='center', va='bottom', fontsize=9, color='steelblue')

for i, r2 in enumerate(R2_values):
    ax4_twin.text(i + width/2, r2 + 0.01, f'{r2:.4f}', 
             ha='center', va='bottom', fontsize=9, color='indianred')

plt.tight_layout()
