---
title: SciPy
description: The structure of SciPy and its relation to NumPy; scipy.linalg and reusable factorizations; minimization, root finding and curve fitting with scipy.optimize; Gaussian quadrature and initial value problems with solve_ivp, Euler and Runge–Kutta steps, stiffness and the choice of method; interpolation and splines; distribution objects and tests in scipy.stats; sparse arrays, storage formats and sparse solvers; finite differences for the heat equation, sparse assembly, and the stability of explicit time stepping; the fast Fourier transform.
---

NumPy provides arrays and the elementary operations on them; SciPy provides the numerical algorithms built on top: optimization, integration of functions and differential equations, interpolation, statistics, sparse matrices, signal processing and Fourier transforms. Most of these algorithms are decades old and implemented in well-tested Fortran, C and C++ libraries (QUADPACK, ODEPACK, FITPACK, ARPACK, SuperLU, among others) or in carefully written Python, so the task of the user is again to formulate the problem in the form the library expects, to choose the method, and to check the result. This chapter is a guided tour of the most used subpackages. As in [4.4.3](/4.4.3), the theory of the methods is treated elsewhere and linked: optimization and root finding in [3.5.4](/3.5.4) and [3.5.5](/3.5.5), differential equations in 2.4 ([2.4.4](/2.4.4)), interpolation and conditioning in [3.5.1](/3.5.1). The examples use SciPy 1.18 (October 2026) with NumPy 2.5; tables of data are the subject of the next chapter, [4.4.5](/4.4.5).

## 4.1. Overview

SciPy is organized in subpackages, each imported separately (`import scipy` alone does not load them all):

| Subpackage | Contents |
|---|---|
| `scipy.linalg` | dense linear algebra: all of `numpy.linalg` plus LU, Schur, QZ, matrix functions (`expm`, `sqrtm`), structured solvers |
| `scipy.optimize` | minimization, root finding, curve fitting, least squares, linear programming |
| `scipy.integrate` | quadrature of functions and samples, ordinary differential equations |
| `scipy.interpolate` | 1-D and multidimensional interpolation, splines, smoothing |
| `scipy.stats` | probability distributions, descriptive statistics, hypothesis tests, bootstrap |
| `scipy.sparse` | sparse arrays, sparse linear solvers and eigensolvers (`scipy.sparse.linalg`), graph algorithms (`scipy.sparse.csgraph`) |
| `scipy.fft` | fast Fourier transforms and related transforms |
| `scipy.signal` | filtering, convolution, spectral analysis, peak finding |
| `scipy.spatial` | k-d trees, distances, Delaunay triangulations, convex hulls, rotations |
| `scipy.special` | special functions: Gamma, Beta, Bessel, error functions, `logsumexp`, `expit` |
| `scipy.ndimage` | filters and morphology on n-dimensional images |
| `scipy.io`, `scipy.constants` | file formats (MATLAB, Matrix Market, WAV), physical constants |

The convention is to import the subpackage, not the functions: `from scipy import optimize` and then `optimize.minimize`, which keeps the origin of each function visible.

When a subpackage overlaps with NumPy, SciPy's version is usually more complete. `scipy.linalg` always uses LAPACK and offers, for example, a factorization that can be computed once and reused for many right-hand sides, which `numpy.linalg.solve` cannot do:

```python
import numpy as np
from scipy import linalg

rng = np.random.default_rng(0)
A = rng.standard_normal((500, 500))
lu, piv = linalg.lu_factor(A)              # O(n^3), once
for _ in range(10):
    b = rng.standard_normal(500)
    x = linalg.lu_solve((lu, piv), b)      # O(n^2) per right-hand side
print(linalg.expm(np.array([[0.0, 1.0], [-1.0, 0.0]])).round(4))
# [[ 0.5403  0.8415]
#  [-0.8415  0.5403]]   the rotation by 1 radian
```

`scipy.special` deserves a mention because it contains numerically careful versions of functions that are easy to get wrong: `gammaln` for $\log\Gamma(x)$ (where $\Gamma(1000)$ itself overflows), `logsumexp` for $\log\sum_i \mathrm{e}^{a_i}$ without overflow (`logsumexp([1000, 1000])` gives $1000 + \log 2$), `expit` for the logistic function, `comb(n, k, exact=True)` for exact binomial coefficients.

SciPy is gradually adopting the array API standard ([4.4.2](/4.4.2#sec-2.8)): with the environment variable `SCIPY_ARRAY_API=1`, a growing set of functions accepts PyTorch, CuPy or JAX arrays and computes on their devices. This support is still experimental in SciPy 1.18.

## 4.2. Optimization

### 4.2.1. Minimization

`optimize.minimize(fun, x0, method=..., jac=..., bounds=..., constraints=...)` minimizes a scalar function of a vector $\boldsymbol{x}$ starting from `x0` and returns an `OptimizeResult`, an object whose attributes include the solution `x`, the minimum `fun`, a flag `success`, a `message`, and the numbers of iterations `nit` and function evaluations `nfev`. The method should be chosen according to what we know about the problem:

| Method | Uses | Constraints | Notes |
|---|---|---|---|
| `Nelder-Mead` | function values only | bounds | **Nelder–Mead method** ([3.5.4](/3.5.4#sec-4.2.3)); robust, slow, small dimensions |
| `Powell` | function values only | bounds | conjugate directions without derivatives |
| `BFGS` | gradient | none | quasi-Newton (**BFGS** update, [3.5.5](/3.5.5#sec-5.1.4.4)); the default without constraints |
| `L-BFGS-B` | gradient | bounds | limited-memory BFGS; large problems; the default with bounds |
| `CG` | gradient | none | nonlinear **conjugate gradient method** ([3.5.5](/3.5.5#sec-5.3.2)) |
| `Newton-CG`, `trust-exact`, `trust-krylov` | gradient and Hessian | none | Newton-type and **trust-region methods** ([3.5.5](/3.5.5#sec-5.1.5.1)) |
| `SLSQP`, `trust-constr`, `COBYQA` | gradient (or none for COBYQA) | general | nonlinear equality and inequality constraints |

Supplying the gradient through `jac` makes gradient-based methods faster and more accurate; without it, SciPy approximates the gradient by finite differences, at the cost of $p + 1$ function evaluations per gradient in dimension $p$. The Rosenbrock function $f(x, y) = (1 - x)^2 + 100(y - x^2)^2$, with its narrow curved valley and minimum at $(1, 1)$, is the standard test:

```python
from scipy import optimize


def rosen(x):
    return (1 - x[0]) ** 2 + 100 * (x[1] - x[0] ** 2) ** 2


def rosen_grad(x):
    return np.array([-2 * (1 - x[0]) - 400 * x[0] * (x[1] - x[0] ** 2),
                     200 * (x[1] - x[0] ** 2)])


x0 = np.array([-1.2, 1.0])
res = optimize.minimize(rosen, x0, method="BFGS", jac=rosen_grad)
print(res.x, res.nit, res.nfev, res.success)   # [1. 1.] 32 39 True
```

| Method | Gradient | Solution | Iterations | Function evaluations |
|---|---|---|---|---|
| Nelder–Mead | no | $(1.000022, 1.000042)$ | 85 | 159 |
| BFGS | finite differences | $(0.999996, 0.999991)$ | 32 | 117 |
| BFGS | exact | $(1, 1)$ to 6 digits | 32 | 39 |
| L-BFGS-B | exact | $(0.999999, 0.999998)$ | 36 | 44 |

With finite differences, BFGS needs three function evaluations per iteration (one value, two for the gradient in two dimensions) and is less accurate. Bounds are passed as a list of `(low, high)` pairs; for example, with `bounds=[(-2, 0.5), (-2, 2)]`, L-BFGS-B returns the constrained minimum $(0.5, 0.25)$ on the boundary. Constraints are passed as dictionaries such as `{"type": "ineq", "fun": lambda x: 1 - x[0]**2 - x[1]**2}`, meaning $1 - x^2 - y^2 \ge 0$; with it, SLSQP finds the minimum $(0.7864, 0.6177)$ on the unit circle.

All these methods find *local* minima. For functions with many local minima, `optimize.differential_evolution`, `dual_annealing` and `basinhopping` search globally, at a much higher cost, and restarting a local method from many starting points is a simple alternative. A one-dimensional function is minimized with `optimize.minimize_scalar`, which uses **Brent's method** combining **golden-section search** and parabolic interpolation ([3.5.4](/3.5.4#sec-4.2.1)).

### 4.2.2. Root Finding

For a scalar equation $f(x) = 0$, `optimize.root_scalar` offers bracketing methods, which need an interval $[a, b]$ with a sign change and always converge, and open methods, which need a starting point and converge faster when they converge:

```python
f = lambda x: x ** 3 - 2 * x - 5          # Newton's historical example
s = optimize.root_scalar(f, bracket=[2, 3], method="brentq")
print(s.root, s.iterations)               # 2.094551481542327 7
s = optimize.root_scalar(f, x0=2.0, fprime=lambda x: 3 * x ** 2 - 2, method="newton")
print(s.root, s.iterations)               # 2.0945514815423265 4
```

`brentq` (**Brent's method**, [3.5.4](/3.5.4#sec-4.3.6)) combines the **bisection method** with the **secant method** and **inverse quadratic interpolation**; it is the method of choice whenever a bracket is known. **Newton's method** ([3.5.5](/3.5.5#sec-5.1.1)) converges quadratically from a good starting point but may diverge from a bad one. For systems of equations $\boldsymbol{F}(\boldsymbol{x}) = \boldsymbol{0}$, `optimize.root` uses a modified Powell hybrid method by default:

```python
def F(v):
    x, y = v
    return [x ** 2 + y ** 2 - 4, np.exp(x) + y - 1]

sol = optimize.root(F, [1.0, -1.0])
print(sol.x, sol.success)                 # [ 1.00416874 -1.72963729] True
```

### 4.2.3. Curve Fitting

Fitting a nonlinear model $y \approx f(x; \boldsymbol{\theta})$ to data by **least squares** is the most common optimization task in experimental science. `optimize.curve_fit(f, xdata, ydata, p0)` minimizes $\sum_i (y_i - f(x_i; \boldsymbol{\theta}))^2$ with the **Levenberg–Marquardt method** ([3.5.5](/3.5.5#sec-5.1.5.3)) and returns the estimate together with an estimated **covariance matrix**, from which approximate **standard errors** follow. For the Michaelis–Menten model of enzyme kinetics, $v = V_{\max} S / (K_{\mathrm{m}} + S)$:

```python
def michaelis_menten(S, Vmax, Km):
    return Vmax * S / (Km + S)


rng = np.random.default_rng(0)
S = np.array([0.5, 1, 2, 4, 8, 16, 32, 64])
v = michaelis_menten(S, 10.0, 4.0) * (1 + 0.05 * rng.standard_normal(S.size))   # 5% noise
p, cov = optimize.curve_fit(michaelis_menten, S, v, p0=[5, 1])
print(p.round(3), np.sqrt(np.diag(cov)).round(3))   # [10.554  4.468] [0.154 0.234]
```

![Simulated Michaelis-Menten data with the curve fitted by curve_fit and the true curve; estimated parameters with standard errors in the legend](./plots/michaelis-menten.py)

The model function takes the independent variable first and the parameters as separate arguments. A reasonable starting point `p0` matters for nonlinear problems; here it is read off the data ($V_{\max}$ near the largest rate, $K_{\mathrm{m}}$ near the concentration at half of it). The standard errors assume that the model is correct and the errors independent with constant variance; with known measurement errors, pass them as `sigma` (with `absolute_sigma=True`). The underlying, more general function is `optimize.least_squares(residuals, x0)`, which also supports bounds and robust loss functions that reduce the influence of outliers. Linearizing the model instead (the Lineweaver–Burk plot of $1/v$ against $1/S$) distorts the error structure and gives biased estimates; with a computer, the nonlinear fit is the right method.

## 4.3. Integration

### 4.3.1. Quadrature

`integrate.quad(f, a, b)` computes $\int_a^b f(x)\,\mathrm{d}x$ by adaptive Gauss–Kronrod quadrature (from the Fortran library QUADPACK) and returns the value together with an estimate of the absolute error. Infinite limits are allowed, and extra parameters of `f` are passed with `args`:

```python
from scipy import integrate

val, err = integrate.quad(lambda x: np.exp(-x ** 2), -np.inf, np.inf)
print(val, err, np.sqrt(np.pi))            # 1.7724538509055159 1.42e-08 1.7724538509055159
val, err = integrate.quad(lambda x, a: x ** a, 0, 1, args=(2,))
print(val)                                 # 0.33333333333333337
```

The error estimate is reliable for smooth integrands; for integrands with singularities, discontinuities or sharp peaks, the location should be given with `points=[...]`, or the interval split. **Multiple integrals** are computed by `dblquad`, `tplquad` and `nquad`, and `quad_vec` integrates vector-valued functions. Gauss–Kronrod quadrature builds on *Gaussian quadrature*: an $n$-point Gauss–Legendre rule places its nodes at the roots of the Legendre polynomial of degree $n$ and chooses the weights so that it integrates polynomials of degree up to $2n - 1$ exactly, the highest possible degree for $n$ nodes. Its weights are positive, which makes it numerically stable, unlike Newton–Cotes rules of high order on equispaced nodes. `integrate.fixed_quad(f, a, b, n=5)` applies such a rule without an error estimate ($\int_0^\pi \sin x\,\mathrm{d}x$ with five nodes gives $2.0000001$); the Kronrod extension adds nodes to a Gauss rule so that the difference of the two results estimates the error. The older functions `quadrature` and `romberg` were removed in SciPy 1.15.

When the integrand is known only at sample points, for example a measured time series, we use the composite rules: `integrate.trapezoid(y, x=x)` and `integrate.simpson(y, x=x)` give the integral, and `integrate.cumulative_trapezoid(y, x=x, initial=0)` the running integral. For $\int_0^\pi \sin x\,\mathrm{d}x = 2$ with 11 points, the trapezoidal rule gives $1.9835$ and Simpson's rule $2.0001$, reflecting their errors of order $h^2$ and $h^4$.

### 4.3.2. Initial Value Problems

An **initial value problem** $\boldsymbol{y}' = \boldsymbol{f}(t, \boldsymbol{y})$, $\boldsymbol{y}(t_0) = \boldsymbol{y}_0$, is solved numerically by `integrate.solve_ivp(fun, t_span, y0, method=..., t_eval=..., ...)`. Existence and uniqueness of the solution are the subject of [2.4.4](/2.4.4); numerical methods construct approximations step by step, the simplest being the **Euler polygon** of [2.4.4](/2.4.4#sec-4.4.1). Production solvers use higher-order methods and choose the step size adaptively so that the estimated local error stays below $\mathrm{atol} + \mathrm{rtol}\,\lvert y\rvert$ in each component.

The interface follows a few conventions:

- `fun(t, y)` takes the time first and the state vector second, and returns $\boldsymbol{y}'$ as a sequence of the same length. Parameters are passed through `args`.
- `t_span = (t0, tf)` is the interval; the solver chooses its own steps. To obtain the solution at specified times, pass `t_eval`, or pass `dense_output=True` and evaluate the continuous interpolant `sol.sol(t)`.
- The result has the times `sol.t`, the solution `sol.y` of shape `(n_components, n_times)` (one row per component), a flag `sol.success` and the number of evaluations of `fun`, `sol.nfev`.
- The default tolerances `rtol=1e-3`, `atol=1e-6` are loose. They are adequate for plotting but not for quantitative results.

The Lotka–Volterra equations describe a prey population $x$ and a predator population $y$:

$$
x' = ax - bxy, \qquad y' = -cy + dxy.
$$
They have a conserved quantity $H(x, y) = dx - c\log x + by - a\log y$, so the exact orbits are closed curves, which gives a test of accuracy.

```python
def lotka_volterra(t, z, a, b, c, d):
    x, y = z
    return [a * x - b * x * y, -c * y + d * x * y]


params = (1.0, 0.1, 1.5, 0.075)
sol = integrate.solve_ivp(lotka_volterra, (0, 30), [10, 5], args=params,
                          rtol=1e-8, atol=1e-10, dense_output=True)
print(sol.t.size, sol.nfev)            # 345 2174
print(sol.sol(10.0).round(4))          # [ 8.0066 11.4162]
```

With these tolerances $H$ varies by $3 \times 10^{-8}$ along the computed solution; with the default tolerances, the solver takes only 44 steps (350 evaluations) and $H$ varies by $0.04$, which is visible as a slow drift of the orbit.

![Lotka-Volterra model solved with solve_ivp: prey and predator populations against time (left), and closed orbits in the phase plane for three initial conditions around the equilibrium (c/d, a/b) (right)](./plots/lotka-volterra.py)

*Events* locate times at which a function of the solution crosses zero, such as a population exceeding a threshold. An event function `g(t, y)` has optional attributes `terminal` (stop the integration) and `direction` (only upward or downward crossings):

```python
def predator_peak(t, z, *args):
    return z[1] - 20          # predator population crosses 20
predator_peak.direction = 1   # upward crossings only

s = integrate.solve_ivp(lotka_volterra, (0, 30), [10, 5], args=params,
                        events=predator_peak, rtol=1e-8)
print(s.t_events[0].round(4))  # [ 3.0172  8.4969 13.9766 19.4563 24.936 ]
```

### 4.3.3. Stiff Problems and the Choice of Method

`solve_ivp` offers explicit and implicit methods:

| Method | Type | Order | Use |
|---|---|---|---|
| `RK45` (default) | explicit Runge–Kutta (Dormand–Prince) | 5(4) | non-stiff problems, moderate accuracy |
| `DOP853` | explicit Runge–Kutta | 8 | non-stiff problems, high accuracy |
| `RK23` | explicit Runge–Kutta (Bogacki–Shampine) | 3(2) | non-stiff, loose tolerances |
| `Radau` | implicit Runge–Kutta | 5 | stiff problems |
| `BDF` | implicit multistep (backward differentiation) | 1–5 | stiff problems |
| `LSODA` | switches between Adams and BDF | variable | unknown stiffness |

This difficulty is called *stiffness*: a problem is stiff when it contains processes on very different time scales, such as fast chemical reactions together with slow transport, so that an explicit method must take tiny steps for stability even where the solution itself changes slowly. The van der Pol oscillator $u'' - \mu(1 - u^2)u' + u = 0$ ([2.4.11](/2.4.11#sec-11.6.3)) with $\mu = 1000$ is a classic example: its solution alternates between slow drifts and sudden jumps. Integrating it over $[0, 3000]$, written as a first-order system, gave on the test machine:

| Method | Steps | Evaluations of `fun` | Time |
|---|---|---|---|
| `RK45` | 1 687 436 | 11 859 590 | 101 s |
| `Radau` | 285 | 2 824 | 0.18 s |
| `BDF` | 539 | 1 902 | 0.14 s |
| `LSODA` | 728 | 1 803 | 0.01 s |

All four succeed, but the explicit method needs 3000 times more steps. Implicit methods solve a nonlinear system with the **Jacobian matrix** $\partial\boldsymbol{f}/\partial\boldsymbol{y}$ at each step; supplying it through `jac=` saves the finite-difference approximation, and `jac_sparsity=` helps for large sparse systems such as discretized **partial differential equations**. The practical rule: start with `RK45`; if it is unexpectedly slow or takes very many steps, try `BDF`, `Radau` or `LSODA`.

### 4.3.4. What the Solvers Do: Euler and Runge–Kutta Steps

The methods in the table are refinements of a few simple ideas, which are worth seeing in their simplest form. For $\boldsymbol{y}' = \boldsymbol{f}(t, \boldsymbol{y})$ and a step $h$, the explicit **Euler method**

$$
\boldsymbol{y}_{k+1} = \boldsymbol{y}_k + h\,\boldsymbol{f}(t_k, \boldsymbol{y}_k)
$$
follows the tangent for one step, which produces the Euler polygon; its global error is of order $h$. The implicit (backward) Euler method $\boldsymbol{y}_{k+1} = \boldsymbol{y}_k + h\,\boldsymbol{f}(t_{k+1}, \boldsymbol{y}_{k+1})$ evaluates $\boldsymbol{f}$ at the unknown new point, so each step requires solving an equation, but it remains stable for large steps on stiff problems; it is the simplest member of the BDF family. The classical fourth-order **Runge–Kutta method** (RK4) combines four evaluations of $\boldsymbol{f}$ per step,

$$
\begin{aligned}
\boldsymbol{k}_1 &= \boldsymbol{f}(t_k, \boldsymbol{y}_k), &
\boldsymbol{k}_2 &= \boldsymbol{f}\bigl(t_k + \tfrac h2, \boldsymbol{y}_k + \tfrac h2 \boldsymbol{k}_1\bigr),\\
\boldsymbol{k}_3 &= \boldsymbol{f}\bigl(t_k + \tfrac h2, \boldsymbol{y}_k + \tfrac h2 \boldsymbol{k}_2\bigr), &
\boldsymbol{k}_4 &= \boldsymbol{f}(t_k + h, \boldsymbol{y}_k + h\boldsymbol{k}_3),
\end{aligned}
\qquad
\boldsymbol{y}_{k+1} = \boldsymbol{y}_k + \frac h6(\boldsymbol{k}_1 + 2\boldsymbol{k}_2 + 2\boldsymbol{k}_3 + \boldsymbol{k}_4),
$$
and has global error of order $h^4$. Multistep methods such as the Adams methods (used by `LSODA`) reuse values from several previous steps instead. Both one-step methods fit in a few lines:

```python
def euler(f, t_span, y0, h):
    t, y = t_span[0], np.asarray(y0, dtype=float)
    for _ in range(round((t_span[1] - t_span[0]) / h)):
        y = y + h * f(t, y)
        t += h
    return y


def rk4(f, t_span, y0, h):
    t, y = t_span[0], np.asarray(y0, dtype=float)
    for _ in range(round((t_span[1] - t_span[0]) / h)):
        k1 = f(t, y)
        k2 = f(t + h / 2, y + h / 2 * k1)
        k3 = f(t + h / 2, y + h / 2 * k2)
        k4 = f(t + h, y + h * k3)
        y = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        t += h
    return y


oscillator = lambda t, y: np.array([y[1], -y[0]])     # x'' = -x, exact x = cos t
exact = np.array([np.cos(10.0), -np.sin(10.0)])
for h in [0.1, 0.05, 0.025]:
    print(h, np.abs(euler(oscillator, (0, 10), [1, 0], h) - exact).max(),
          np.abs(rk4(oscillator, (0, 10), [1, 0], h) - exact).max())
```

| Step $h$ | Euler: error at $t = 10$ | RK4: error at $t = 10$ | evaluations of $\boldsymbol{f}$ (Euler / RK4) |
|---|---|---|---|
| 0.1 | $5.7 \times 10^{-1}$ | $7.3 \times 10^{-6}$ | 100 / 400 |
| 0.05 | $2.4 \times 10^{-1}$ | $4.5 \times 10^{-7}$ | 200 / 800 |
| 0.025 | $1.1 \times 10^{-1}$ | $2.8 \times 10^{-8}$ | 400 / 1600 |

Halving the step roughly halves the Euler error and divides the RK4 error by 16, as the orders predict; for the same number of evaluations, RK4 is better by many orders of magnitude. The two Euler methods also err qualitatively. For the harmonic oscillator each explicit step multiplies the amplitude by $\sqrt{1 + h^2}$, so with $h = 0.1$ the amplitude has grown from 1 to $1.645$ at $t = 10$, an orbit spiraling outward; each implicit step divides it by the same factor, giving $0.608$, a spurious damping. `solve_ivp` adds what a fixed-step loop lacks: an error estimate in every step (RK45 compares embedded solutions of orders 4 and 5) and an adaptive step size. With the default tolerances it reaches an error of $2 \times 10^{-3}$ here with 86 evaluations, and with `rtol=1e-8, atol=1e-10` an error of $1.1 \times 10^{-8}$ with 812 evaluations, without the user choosing a step.

Older code uses `integrate.odeint`, a wrapper of LSODA whose right-hand side takes the arguments in the order `f(y, t)`, and the object-oriented class `integrate.ode`; both still work, but `solve_ivp` is the interface for new code.

## 4.4. Interpolation

Interpolation constructs a function that passes through given points $(x_i, y_i)$; unlike fitting (§4.2.3), which determines a few parameters from many noisy points, it reproduces the data exactly. One global polynomial through many equispaced points oscillates near the ends, the **Runge phenomenon** of **polynomial interpolation**, so practical interpolation uses piecewise polynomials. `scipy.interpolate` offers several, which differ in smoothness and shape preservation:

| Class or function | Method | Properties |
|---|---|---|
| `np.interp(x, xp, fp)` | piecewise linear | continuous, shape preserving, not smooth |
| `CubicSpline(x, y)` | cubic spline | twice continuously differentiable; may overshoot |
| `PchipInterpolator(x, y)` | monotone piecewise cubic Hermite | once differentiable; monotone where the data are |
| `Akima1DInterpolator(x, y, method="makima")` | modified Akima | once differentiable; little overshoot |
| `make_interp_spline(x, y, k)` | B-spline of degree `k` | general spline interpolation |
| `make_smoothing_spline(x, y, lam)` | smoothing spline | does not interpolate noisy data exactly |
| `RegularGridInterpolator`, `griddata` | multidimensional | regular grids, scattered data |

A *cubic spline* is a function that is a cubic polynomial on each interval $[x_i, x_{i+1}]$ and twice continuously differentiable at the nodes; two boundary conditions (by default the "not-a-knot" condition) make it unique. Its smoothness is ideal for smooth data, but on data with steps it overshoots, which is unacceptable for quantities that must stay in a range, such as concentrations or probabilities. PCHIP and modified Akima interpolants preserve monotonicity at the price of a discontinuous second derivative:

```python
from scipy import interpolate

x = np.array([0, 1, 2, 3, 4, 5.0])
y = np.array([0, 0, 0, 1, 1, 1.0])
cs = interpolate.CubicSpline(x, y)
pc = interpolate.PchipInterpolator(x, y)
print(cs([2.5, 3.5]), pc([2.5, 3.5]))   # [0.5   1.125] [0.5 1. ]: the spline overshoots to 1.125
print(cs.derivative()(2.5), cs.integrate(0, 5))   # 1.1666666666666665 2.5
```

![Left: step-like data interpolated by np.interp, CubicSpline, PchipInterpolator and modified Akima; the cubic spline overshoots. Right: Runge's function with 11 equispaced nodes; the degree-10 interpolating polynomial oscillates near the ends, the cubic spline does not](./plots/interpolation.py)

The interpolant objects are callable and have methods for derivatives, antiderivatives, integrals and roots. The older class `interp1d` is now marked as legacy; the classes above replace it. `interp2d` was removed in SciPy 1.14: gridded data in two or more dimensions are interpolated with `RegularGridInterpolator` (or `RectBivariateSpline` for smooth splines), scattered data with `griddata` or `RBFInterpolator`.

## 4.5. Statistics

### 4.5.1. Distribution Objects

`scipy.stats` contains about 110 continuous and 20 discrete distributions. Each is an object with methods for the density (`pdf`, or `pmf` for discrete distributions), the **cumulative distribution function** (`cdf`), the **survival function** (`sf`, $1 - F$, accurate in the far tail), the **quantile** function (`ppf`, the inverse of the CDF), **moments**, random variates (`rvs`) and fitting (`fit`). All continuous distributions are parameterized by shape parameters together with `loc` and `scale`, so that $X = \mathrm{loc} + \mathrm{scale}\cdot Z$ for a standard variable $Z$. As with NumPy's `Generator` ([4.4.3](/4.4.3#sec-3.4.2)), this means that `scale` is the standard deviation for the **normal distribution** and the mean $1/\lambda$ for the **exponential distribution**:

```python
from scipy import stats

X = stats.norm(loc=1.0, scale=2.0)           # N(1, 4), a "frozen" distribution
print(X.mean(), X.var(), X.cdf(1.0))         # 1.0 4.0 0.5
print(stats.norm.ppf(0.975))                 # 1.959963984540054, the quantile z_{0.025}
print(stats.expon(scale=1 / 2.0).mean())     # 0.5 for Exp(2)
print(stats.gamma(a=3.0, scale=1 / 2.0).var())   # 0.75 for Gamma(3, 2)
rng = np.random.default_rng(0)
print(X.rvs(size=3, random_state=rng))       # draws use a NumPy Generator
```

SciPy 1.15 introduced a new interface for distributions, in which distributions are classes with named parameters (`stats.Normal(mu=1.0, sigma=2.0)`, with methods `pdf`, `cdf`, `icdf`, `sample`), and **random variables** can be transformed arithmetically: `2 * stats.Normal(mu=1.0, sigma=2.0) + 1` is again a distribution object with mean 3 and standard deviation 4. `stats.make_distribution` turns other distributions into this form. The classical interface remains fully supported, and most code and documentation still use it.

### 4.5.2. Estimation and Tests

Parameters are estimated by **maximum likelihood estimation** with `fit`; parameters that should not be estimated are fixed with arguments such as `floc=0`:

```python
data = stats.gamma(a=3.0, scale=0.5).rvs(size=500, random_state=rng)
print(stats.gamma.fit(data, floc=0))   # (3.213..., 0, 0.455...): shape, loc, scale
```

The hypothesis tests return result objects with the statistic, the **p-value** and, for many tests, further information such as **degrees of freedom** or a **confidence interval**:

```python
a = rng.normal(0.0, 1.0, 30)
b = rng.normal(0.8, 1.0, 30)
t = stats.ttest_ind(a, b, equal_var=False)      # Welch's t-test
print(t.statistic, t.pvalue, t.df)              # -3.533 0.00085 53.58 (rounded)
print(t.confidence_interval(0.95))              # interval for the difference of the means
print(stats.mannwhitneyu(a, b).pvalue)          # 0.00289, the rank-based alternative
```

Other frequently used functions are `pearsonr`, `spearmanr`, `linregress`, `chi2_contingency`, `fisher_exact`, `shapiro`, `kstest`, `wilcoxon`, `kruskal`, `f_oneway`, and the resampling methods `bootstrap` and `permutation_test`. Newer functions take a NumPy `Generator` through an argument named `rng`, older ones through `random_state`. What the tests mean, and when they are valid, is the subject of the statistics courses; for regression models with formulas, standard errors and diagnostics, the package statsmodels is more convenient than `scipy.stats`.

## 4.6. Sparse Matrices

### 4.6.1. Storage Formats

Many large matrices in science have mostly zero entries: the discretization of a differential equation couples only neighboring grid points, the **adjacency matrix** of a network has one entry per edge, and a gene-by-cell count matrix in single-cell sequencing is typically over 90% zeros. A *sparse matrix* is a matrix stored in a format that records only the nonzero entries, so that memory and computation scale with the number of nonzeros instead of with $mn$. `scipy.sparse` provides several formats, each efficient for different operations:

| Format | Stores | Good for |
|---|---|---|
| COO (coordinate) | three arrays: row indices, column indices, values | construction; duplicate entries are summed |
| CSR (compressed sparse row) | values and column indices row by row, plus row pointers `indptr` | row slicing, matrix–vector products, arithmetic |
| CSC (compressed sparse column) | the same by columns | column slicing, direct solvers |
| LIL, DOK | lists per row, dictionary of keys | changing the sparsity pattern element by element |
| DIA | diagonals | banded matrices |

In CSR format, the column indices and values of row $i$ are `indices[indptr[i]:indptr[i+1]]` and `data[indptr[i]:indptr[i+1]]`. The typical workflow is to assemble the matrix in COO (or with `diags_array`, `block_array`, `kron`), convert it once to CSR or CSC, and then compute.

SciPy has two sets of classes: the older *sparse matrices* (`csr_matrix`, ...), which imitate `np.matrix`, and the newer *sparse arrays* (`csr_array`, ...), which behave like NumPy arrays. New code should use sparse arrays. The difference matters for `*`, which is matrix multiplication for sparse matrices but elementwise multiplication for sparse arrays, exactly as for dense arrays; `@` is matrix multiplication for both.

```python
from scipy import sparse

n = 6
off, main = -np.ones(n - 1), 2 * np.ones(n)
L = sparse.diags_array([off, main, off], offsets=[-1, 0, 1], format="csr")
print(type(L).__name__, L.shape, L.nnz)    # csr_array (6, 6) 16
print(L.indptr)                            # [ 0  2  5  8 11 14 16]
print((L * L)[0, 0], (L @ L)[0, 0])        # 4.0 5.0: elementwise versus matrix product
coo = sparse.coo_array(([1.0, 2.0, 3.0], ([0, 1, 1], [2, 0, 0])), shape=(2, 3))
print(coo.toarray())                       # [[0. 0. 1.]  [5. 0. 0.]]: entry (1, 0) summed
```

### 4.6.2. Sparse Linear Algebra

`scipy.sparse.linalg` contains solvers that exploit sparsity. The tridiagonal matrix above, scaled by $1/h^2$, is the discretization of $-u''$ on a grid with spacing $h$, so solving $L\boldsymbol{u} = \boldsymbol{f}$ approximates the **boundary value problem** $-u'' = f$, $u(0) = u(1) = 0$, a one-dimensional **Poisson equation**. For $f = 1$ the exact solution is $u(x) = x(1 - x)/2$, which the discretization reproduces exactly up to rounding:

```python
from scipy.sparse import linalg as spla


def laplacian_1d(n):
    h = 1 / (n + 1)
    main, off = 2 * np.ones(n), -np.ones(n - 1)
    return sparse.diags_array([off, main, off], offsets=[-1, 0, 1], format="csr") / h ** 2


n = 100_000
A = laplacian_1d(n)
x = np.linspace(0, 1, n + 2)[1:-1]
u = spla.spsolve(A.tocsc(), np.ones(n))
print(np.abs(u - x * (1 - x) / 2).max())    # 2.3e-11
```

The sparse matrix with $n = 10^5$ occupies 4 MB and is solved in 0.1 s; the same matrix stored densely would need 80 GB. The main tools are:

| Task | Function | Method |
|---|---|---|
| direct solve | `spsolve(A, b)`, `splu(A)`, `factorized(A)` | sparse LU (SuperLU) |
| iterative solve, symmetric positive definite | `cg(A, b, rtol=...)` | **conjugate gradient method** ([3.5.5](/3.5.5#sec-5.3.2)) |
| iterative solve, general | `gmres`, `bicgstab`, `minres` | Krylov subspace methods |
| a few eigenvalues | `eigsh(A, k, sigma=...)`, `eigs` | Lanczos and Arnoldi (ARPACK) |
| a few singular values | `svds(A, k)` | |
| matrix-free operators | `LinearOperator(shape, matvec=...)` | iterative methods only need products $A\boldsymbol{v}$ |

Iterative methods converge at a rate determined by the **condition number**. For $n = 1000$, $\kappa(A) \approx 4 \times 10^5$, and conjugate gradients needs 500 iterations to reach a relative residual of $10^{-10}$, while the direct solver takes 2 ms; for this one-dimensional problem the direct method is clearly better. For large two- and three-dimensional problems, direct solvers suffer from fill-in, and iterative methods with a preconditioner become the method of choice. The smallest eigenvalues of $A$ for $n = 1000$, computed by `spla.eigsh(A, k=3, sigma=0)` with the shift-invert mode, agree with the exact values $\frac{4}{h^2}\sin^2\frac{k\pi h}{2} \approx (k\pi)^2$, $k = 1, 2, 3$, to all printed digits. Graph algorithms on sparse adjacency matrices (shortest paths, **connected components**, **minimum spanning trees**, as in [4.3.11](/4.3.11)) are in `scipy.sparse.csgraph`.

### 4.6.3. Example: Finite Differences for the Heat Equation

Sparse matrices arise above all from the discretization of **partial differential equations**, and a complete example shows how the pieces of this section fit together. Consider a square plate $[0, 1]^2$ with thermal conductivity $\alpha$ and a uniformly distributed heat source of density $q$, insulated on its edges except for a cold segment $0.3 < x < 0.7$ of the top edge held at temperature $0$. The stationary temperature satisfies $\alpha\,\Delta T + q = 0$, a **Poisson equation** ([2.5.1](/2.5.1#sec-1.2.3)), with a **Dirichlet boundary condition** $T = 0$ on the cold segment and a **Neumann boundary condition** $\partial T/\partial\boldsymbol{n} = 0$ (no heat flux) on the rest of the boundary ([2.5.1](/2.5.1#sec-1.3.2)). The time-dependent problem is the **heat equation** $T_t = \alpha\,\Delta T + q$.

The *finite difference method* replaces derivatives by difference quotients on a grid. The **central difference** for the second derivative,

$$
u''(x) = \frac{u(x + h) - 2u(x) + u(x - h)}{h^2} + O(h^2),
$$
follows from **Taylor's formula** ([3.5.1](/3.5.1#sec-1.5.2) discusses the competing rounding error). We divide the plate into $n \times n$ square cells of side $h = 1/n$ and take as unknowns the temperatures $T_{i,j}$ at the cell centers $\bigl((i + \frac12)h, (j + \frac12)h\bigr)$, $0 \le i, j < n$. Applying the central difference in both directions gives, for an interior cell, the *five-point stencil*

$$
4T_{i,j} - T_{i+1,j} - T_{i-1,j} - T_{i,j+1} - T_{i,j-1} = \frac{q h^2}{\alpha}.
$$
At the boundary, the missing neighbor is replaced by a *ghost value* outside the plate, chosen so that the boundary condition holds on the cell face between the two:

- insulated face: ghost value $= T_{i,j}$, so that the difference across the face, and with it the heat flux, is zero. The neighbor term disappears and the diagonal coefficient drops by one (to 3 on an edge, 2 in a corner);
- face held at $T_{\mathrm{w}}$, half a cell from the center: ghost value $= 2T_{\mathrm{w}} - T_{i,j}$, so that the linear interpolation between the two equals $T_{\mathrm{w}}$ on the face. Compared with the insulated face, the diagonal coefficient grows by two and the right-hand side by $2T_{\mathrm{w}}$; for a top-edge cell below the cold segment the equation reads $5T_{i,n-1} - T_{i+1,n-1} - T_{i-1,n-1} - T_{i,n-2} = qh^2/\alpha$.

Numbering the unknowns row by row, $k = jn + i$, turns the $n^2$ equations into a linear system $A\boldsymbol{T} = \boldsymbol{b}$ whose matrix has at most five nonzeros per row. The numbering matches NumPy's row-major `reshape(n, n)`, with $j$ (the $y$ direction) as the row index. The matrix need not be assembled entry by entry: with $D$ the $n \times n$ second-difference matrix of one dimension (with insulated ends) and $I$ the identity, the two-dimensional operator is $I \otimes D + D \otimes I$, where $\otimes$ is the Kronecker product, `sparse.kron`. The Dirichlet segment then only adds a diagonal correction:

```python
def second_difference(n):
    """1D matrix of -u'' times h^2 on n cells with insulated (zero-flux) ends."""
    main = 2.0 * np.ones(n)
    main[[0, -1]] = 1.0                      # ghost value equals the boundary cell
    off = -np.ones(n - 1)
    return sparse.diags_array([off, main, off], offsets=[-1, 0, 1])


n = 100                                      # n x n cells on the unit square
h = 1.0 / n
alpha, q = 1.0, 1.0                          # conductivity and heat source density
I = sparse.eye_array(n)
D = second_difference(n)
A = sparse.kron(I, D) + sparse.kron(D, I)    # unknown T[j, i] has index k = j * n + i

xc = (np.arange(n) + 0.5) * h                # cell centers
cold = np.flatnonzero(np.abs(xc - 0.5) < 0.2)    # T = 0 on the middle of the top edge
d = np.zeros(n * n)
d[(n - 1) * n + cold] = 2.0                  # ghost value -T: two more on the diagonal
A = (A + sparse.diags_array(d)).tocsc()
b = np.full(n * n, q * h ** 2 / alpha)

T = spla.spsolve(A, b).reshape(n, n)
print(A.shape, A.nnz, T.max())               # (10000, 10000) 49600 0.6748...
print(2 * alpha * T[-1, cold].sum())         # 0.9999999999998: heat out = q * area
```

The system with $10^4$ unknowns is solved in 0.03 s. The last line checks a conservation law: the heat flux density through a cold face is $\alpha \cdot T_{i,n-1}/(h/2)$ and the face has length $h$, so the total outflow is $2\alpha\sum_i T_{i,n-1}$, and it equals the heat $q \cdot 1$ produced in the plate to rounding error. This holds exactly because the scheme is also a balance of fluxes between neighboring cells, a simple *finite volume* discretization; such checks catch most errors in the treatment of boundaries.

![Steady temperature in a square plate with a uniform heat source, insulated edges and a cold segment on the top edge, computed on 100 x 100 cells: temperature field with isotherms (left) and temperature along the vertical center line and along a horizontal line just below the cold segment (right)](./plots/heat-conduction.py)

The matrix is symmetric and, thanks to the Dirichlet segment, positive definite (with insulated edges only, it would be singular, since adding a constant to $T$ changes nothing). Conjugate gradients therefore also applies: `spla.cg(A, b, rtol=1e-10)` needs 458 iterations and 0.06 s here. The classical iterations that update one cell at a time from its neighbors, the **Jacobi method** $T_{i,j} \leftarrow \frac14\bigl(\sum \text{neighbors} + qh^2/\alpha\bigr)$ and the **Gauss–Seidel method** ([3.5.4](/3.5.4#sec-4.3.4)), need no matrix at all but converge much more slowly, with a number of iterations proportional to $n^2$; multigrid methods (the package PyAMG), which correct the error on a hierarchy of coarser grids, solve such problems in a time proportional to the number of unknowns. For problems in three dimensions, preconditioned iterative methods are usually the only option.

For the time-dependent equation, discretizing only in space (the *method of lines*) gives the linear ODE system $\boldsymbol{T}' = -\frac{\alpha}{h^2}A\boldsymbol{T} + q\boldsymbol{1}$. Its stepping with the explicit Euler method of §4.3.4 is

$$
\boldsymbol{T}^{m+1} = \boldsymbol{T}^m - r A\boldsymbol{T}^m + \Delta t\,q\boldsymbol{1}, \qquad r = \frac{\alpha\,\Delta t}{h^2}.
$$
A grid oscillation $\mathrm{e}^{\mathrm{i}(\theta_1 i + \theta_2 j)}$ is multiplied in each step of the interior scheme by $g = 1 - 4r\bigl(\sin^2\frac{\theta_1}{2} + \sin^2\frac{\theta_2}{2}\bigr)$, which ranges down to $1 - 8r$. The scheme is stable, $\lvert g\rvert \le 1$ for all modes, if and only if $r \le 1/4$ in two dimensions (and $r \le 1/2$ in one, where $g = 1 - 4r\sin^2\frac\theta2$); this is von Neumann stability analysis. Under this condition the new value of each cell is a weighted average, with nonnegative weights, of the old values of its neighbors and itself, so the scheme also inherits the **maximum principle** of the heat equation ([2.5.7](/2.5.7#sec-7.2)). Beyond it, the highest-frequency mode grows by the factor $\lvert 1 - 8r\rvert$ (or $\lvert 1 - 4r\rvert$ in one dimension) in every step and destroys the solution within a few dozen steps:

![Explicit time stepping of the one-dimensional heat equation from a step-shaped initial profile: with r = 0.48 the profile smooths out as expected (left); with r = 0.52 a sawtooth oscillation on the grid grows in every step (right)](./plots/diffusion-stability.py)

The condition $\Delta t \le h^2/(4\alpha)$ is severe: halving the grid spacing quarters the time step. The semi-discrete system is a stiff problem in the sense of §4.3.3: the eigenvalues of $A$ range from $1.8 \times 10^{-4}$ to almost 8, a ratio of $4.5 \times 10^4$ for $n = 100$, growing like $n^2$. Implicit time stepping avoids the restriction. The implicit Euler step $(I + rA)\boldsymbol{T}^{m+1} = \boldsymbol{T}^m + \Delta t\,q\boldsymbol{1}$ is stable for every $\Delta t$, and since the matrix does not change, it is factorized once:

```python
dt = 0.01                                    # r = 100, far beyond the explicit limit
step = spla.factorized((sparse.eye_array(n * n) + alpha * dt / h ** 2 * A).tocsc())
Tt = np.zeros(n * n)                         # start from a cold plate
for m in range(300):                         # up to t = 3
    Tt = step(Tt + dt * q)
print(np.abs(Tt.reshape(n, n) - T).max())    # 0.0034: close to the steady state
```

Alternatively, `solve_ivp(..., method="BDF", jac=-alpha / h**2 * A)` integrates the semi-discrete system with adaptive steps, using the sparse Jacobian directly. The Crank–Nicolson method, the average of the explicit and implicit steps, is also unconditionally stable and second-order accurate in time.

Finite differences on rectangular grids are the simplest discretization. Complex geometries are handled by the finite element method (structural mechanics, electromagnetics; in Python FEniCSx, Firedrake, scikit-fem), and conservation laws, as in fluid dynamics, by finite volume methods (FiPy); problems with periodic or very smooth solutions by spectral methods built on the FFT (§4.7); physics-informed neural networks, which fit a network to the equation and the data, are a newer and still less reliable alternative.

## 4.7. The Fast Fourier Transform

The *discrete Fourier transform* (DFT) of a sequence $x_0, \dots, x_{N-1}$ is

$$
X_k = \sum_{n=0}^{N-1} x_n\,\mathrm{e}^{-2\pi\mathrm{i}kn/N}, \qquad k = 0, 1, \dots, N - 1,
$$
the discrete analogue of the **Fourier transform**; it decomposes the sequence into oscillations with frequencies $k/N$ cycles per sample. Evaluated directly, it costs $O(N^2)$ operations; the *fast Fourier transform* (FFT) computes it in $O(N \log N)$ operations by recursively splitting it into transforms of smaller sizes, a **divide and conquer** algorithm ([4.1.11](/4.1.11)). The FFT is one of the most important algorithms in scientific computing: it underlies spectral analysis, fast **convolution**, image processing and the numerical solution of **partial differential equations**.

`scipy.fft` (and the similar but smaller `numpy.fft`) provides:

| Function | Purpose |
|---|---|
| `fft`, `ifft` | complex transform and its inverse |
| `rfft`, `irfft` | for real input: only the $N/2 + 1$ nonnegative frequencies, about twice as fast |
| `fftfreq(N, d)`, `rfftfreq(N, d)` | the frequencies of the outputs, for sample spacing `d` |
| `fft2`, `fftn`, `rfftn` | multidimensional transforms |
| `fftshift` | reorder so that the zero frequency is in the middle |
| `dct`, `dst` | discrete cosine and sine transforms |
| `next_fast_len(N)` | a size $\ge N$ with small prime factors, for zero padding |

The convention for normalization is that the forward transform carries no factor and the inverse transform the factor $1/N$, as in the formula above; `norm="ortho"` uses $1/\sqrt{N}$ for both, and `norm="forward"` puts $1/N$ on the forward transform. Conventions differ between libraries and textbooks, so it is worth checking with a small example. The speed depends on the prime factorization of $N$: sizes with only small prime factors are fastest, which is why `next_fast_len(1009)` (1009 is prime) suggests 1024.

To estimate the frequency content of a sampled signal, we transform it and convert the outputs to amplitudes. For a signal sampled at rate $f_s$ for a duration $T$, the frequency resolution is $1/T$ and the largest representable frequency, the Nyquist frequency, is $f_s/2$:

```python
from scipy import fft

fs = 100.0                                        # samples per second
t = np.arange(0, 4, 1 / fs)                       # 4 seconds, N = 400
rng = np.random.default_rng(1)
signal = (np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 12 * t)
          + 0.8 * rng.standard_normal(t.size))
amplitude = 2 * np.abs(fft.rfft(signal)) / t.size  # one-sided amplitude spectrum
freq = fft.rfftfreq(t.size, d=1 / fs)              # 0, 0.25, ..., 50 Hz
```

![A noisy signal composed of 5 Hz and 12 Hz sine waves (left) and its one-sided amplitude spectrum computed with rfft, with peaks near amplitudes 1 and 0.5 at 5 Hz and 12 Hz (right)](./plots/spectrum.py)

The two components, invisible by eye in the noisy signal, stand out as peaks of height about 1 and 0.5. Since the frequencies 5 Hz and 12 Hz are multiples of the resolution $0.25$ Hz, each falls exactly on one output; in general the energy of a frequency between two outputs leaks into neighboring ones, which is reduced by multiplying the signal by a window function (`scipy.signal.windows`) before the transform. `scipy.signal.welch` averages spectra of overlapping segments and gives a smoother estimate of the power spectral density. Convolution, which costs $O(N^2)$ directly, becomes a pointwise product in the frequency domain; `scipy.signal.fftconvolve` uses this and is much faster than `np.convolve` for long inputs.

## Summary

- SciPy is a collection of subpackages built on NumPy and on established compiled libraries; import subpackages (`from scipy import optimize`) and prefer `scipy.linalg` over `numpy.linalg`.
- `optimize.minimize` finds local minima; choose the method by what is available (values, gradients, Hessians) and by the constraints, and supply gradients when possible. Use `root_scalar` with a bracket (`brentq`) for scalar equations, `curve_fit` or `least_squares` for **nonlinear regression**.
- `quad` integrates functions adaptively with an error estimate; `trapezoid` and `simpson` integrate samples.
- `solve_ivp(fun(t, y), t_span, y0)` solves initial value problems with adaptive steps; set tolerances explicitly, use `dense_output` or `t_eval` for output, `events` to locate crossings, and an implicit method (`BDF`, `Radau`, `LSODA`) for stiff problems. Behind it are one-step formulas such as the Euler method (order 1) and RK4 (order 4), with error estimates and adaptive steps added.
- Cubic splines are smooth but may overshoot; PCHIP and modified Akima preserve monotonicity. `interp1d` is legacy.
- `scipy.stats` distributions use `loc` and `scale`; tests return result objects with statistics, **p-values** and often **confidence intervals**.
- Use sparse arrays (`csr_array`) rather than sparse matrices; assemble in COO, compute in CSR or CSC; `spsolve` for direct and `cg` or `gmres` for iterative solution.
- Finite differences turn a PDE such as $\alpha\,\Delta T + q = 0$ into a sparse system: five-point stencil, ghost values for Dirichlet and Neumann boundaries, assembly with `sparse.kron`; explicit time stepping of the heat equation is stable only for $\alpha\,\Delta t/h^2 \le 1/4$ (two dimensions), implicit stepping for every step size.
- The FFT computes the discrete Fourier transform in $O(N \log N)$; use `rfft` and `rfftfreq` for real signals and check normalization conventions.
