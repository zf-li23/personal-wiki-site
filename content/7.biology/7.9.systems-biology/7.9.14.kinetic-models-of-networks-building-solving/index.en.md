---
title: "Kinetic Models of Networks: Building, Solving and Fitting"
description: "The craft of dynamical models of biological networks: forward and inverse models; from diagrams to rate equations (mass action, the stoichiometric matrix and conserved moieties, quasi-steady states and their validity, phenomenological rate laws, the ambiguity of diagrams, Lotka–Volterra); numerical solution (Euler and Runge–Kutta methods, order and stability, adaptive steps, stiffness); steady states, linear stability, the Bier model of glycolytic oscillations and its Hopf bifurcation; sensitivity analysis and metabolic control analysis of networks (control-coefficient matrices, summation and connectivity theorems, branched pathways, the combined response theorem); parameter estimation (least squares and likelihood, progress curves, gradients, local minima and multistart); identifiability, Fisher information, profile likelihood, bootstrap, model selection and validation, with a complete Python workflow."
---

The chapters so far treated networks as graphs: which molecules interact, which genes regulate which. A graph does not say what happens in time. To predict how a pathway responds to a stimulus, whether a circuit oscillates or how much a drug that halves an enzyme's activity changes a flux, the edges must be given rates, and the network becomes a system of **ordinary differential equations**. This chapter is about the craft of such kinetic models: how to write the equations from a diagram (14.2), how to solve them numerically (14.3), how to find their steady states and the changes of behavior as parameters vary (14.4), how sensitive their behavior is to each parameter (14.5), and the inverse problem, how to estimate the parameters from data (14.6) and how to know what the data have actually determined (14.7). Section 14.8 puts the steps together in Python.

The mathematics comes from earlier courses and is not repeated: existence, uniqueness and stability of solutions from [2.4](/2.4) (in particular [2.4.11](/2.4.11)), numerical methods for initial value problems in [4.4.4](/4.4.4#sec-4.3), nonlinear least squares in [3.5.5](/3.5.5#sec-5.1.5) and [7.7.11](/7.7.11), the bootstrap in [3.5.7](/3.5.7). The biological models that use these tools, the toggle switch, the repressilator and the Goodwin oscillator ([7.6.33](/7.6.33)), stochastic kinetics ([7.6.32](/7.6.32)), flux balance analysis ([7.6.34](/7.6.34#sec-34.4)) and robustness ([7.6.40](/7.6.40)), are linked where they are needed. The following chapters apply the tools to network motifs ([7.9.15](/7.9.15)), to feedback and oscillations in signaling ([7.9.16](/7.9.16)) and to noise and robustness ([7.9.17](/7.9.17)).

## 14.1. Forward and Inverse Models

A kinetic model can be used in two directions ([7.9.1](/7.9.1#sec-1.5.3)). A **forward model** computes the behavior of a system from its structure and parameters; an **inverse model** estimates the parameters, or chooses between structures, from observed behavior. The two have different uses and different weaknesses.

| | Forward model | Inverse model |
|---|---|---|
| Question | what would happen if a parameter, an input or the structure changed? | which parameters (or which model) explain the data? |
| Complexity | as detailed as knowledge allows; parameters often taken from the literature | as simple as the data can determine |
| Uses | summarizing knowledge, predicting experiments that are hard to do, testing hypotheses in silico, designing experiments | quantifying rate constants, affinities and feedback strengths; comparing healthy and diseased states |
| Main risk | assumptions and literature values that do not hold together ("garbage in, garbage out") | parameters that the data cannot determine; local optima; overfitting |

The two are combined in forward–inverse studies. Synthetic data are generated from a forward model with known parameters and realistic noise, then fitted with the inverse model; whether the known parameters are recovered shows, before any experiment is done, which parameters a planned experiment can determine and with what precision. Several of the figures of this chapter are such studies. The general rule is that a model must be validated, by its behavior in limiting cases whose outcome is known and by experiments that it did not see, and that the places where it fails are informative: they show what is not understood.

Kinetic models are one of several levels of description ([7.6.33](/7.6.33#sec-33.1.2)). **Boolean networks** need no rate constants and scale to hundreds of genes ([7.6.34](/7.6.34#sec-34.2.3)); ordinary differential equations for concentrations give time scales, thresholds and bifurcations and are the subject of this chapter; the **chemical master equation** and its simulation by the **Gillespie algorithm** describe the fluctuations of small copy numbers ([7.6.32](/7.6.32#sec-32.5)); partial differential equations add space ([2.5](/2.5)); and constraint-based models such as **flux balance analysis** describe the steady states of genome-scale metabolic networks without kinetics ([7.6.34](/7.6.34#sec-34.4)). Models are exchanged in the Systems Biology Markup Language (SBML), an XML format that records species, reactions, rate laws, parameters and initial conditions, drawn in the Systems Biology Graphical Notation (SBGN), and deposited in BioModels, a curated repository of published models that can be downloaded and simulated.

## 14.2. From Diagrams to Equations

### 14.2.1. Mass Action and the Stoichiometric Matrix

The rate of an elementary reaction, one that proceeds through a single transition state, is proportional to the product of the concentrations of its reactants (the **law of mass action**, [7.6.3](/7.6.3#sec-3.2)). A first-order reaction $A \to B$ has rate $k_1[A]$ with $k_1$ in $\mathrm{s^{-1}}$, a second-order reaction $A + B \to C$ has rate $k_2[A][B]$ with $k_2$ in $\mathrm{M^{-1}\,s^{-1}}$: rate constants of different orders have different units, which is a useful check on every equation.

**Definition 14.2.1 (Kinetic Model of a Reaction Network)** Let a network have $m$ species with concentrations $\boldsymbol{x} = (x_1, \dots, x_m)$ and $r$ reactions with rates $\boldsymbol{v}(\boldsymbol{x}, \boldsymbol{p})$, depending on parameters $\boldsymbol{p}$. With the **stoichiometric matrix** $N$ ($m \times r$, entry $N_{ij}$ the net number of molecules of species $i$ produced by reaction $j$), the *kinetic model* of the network is the system
$$
\frac{\mathrm{d}\boldsymbol{x}}{\mathrm{d}t} = N\boldsymbol{v}(\boldsymbol{x}, \boldsymbol{p}), \qquad \boldsymbol{x}(0) = \boldsymbol{x}_0. \tag{14.1}
$$

The structure of the network is in $N$, the kinetics in $\boldsymbol{v}$. Flux balance analysis uses only $N$ and the steady-state condition $N\boldsymbol{v} = \boldsymbol{0}$; a kinetic model needs both.

**Example 14.2.1** For enzyme catalysis $E + S \rightleftharpoons C \to E + P$ with species $(E, S, C, P)$ and reactions $v_1 = k_1[E][S]$ (binding), $v_2 = k_{-1}[C]$ (unbinding) and $v_3 = k_2[C]$ (catalysis),
$$
N = \begin{bmatrix} -1 & 1 & 1 \\ -1 & 1 & 0 \\ 1 & -1 & -1 \\ 0 & 0 & 1 \end{bmatrix}, \qquad
\frac{\mathrm{d}[C]}{\mathrm{d}t} = k_1[E][S] - (k_{-1} + k_2)[C],
$$
and similarly for the other three species: four equations, written mechanically from the scheme.

### 14.2.2. Conservation Laws

Not all the equations are independent. In Example 14.2.1, $\mathrm{d}([E] + [C])/\mathrm{d}t = 0$: the enzyme is neither made nor destroyed, only exchanged between free and bound forms. Such relations are found from $N$ alone.

**Theorem 14.2.1 (Conserved Moieties)** If $\boldsymbol{\ell}$ is a row vector with $\boldsymbol{\ell}N = \boldsymbol{0}$, then $\boldsymbol{\ell}\boldsymbol{x}(t)$ is constant along every solution of Eq. (14.1), whatever the rate laws. If $N$ has rank $\rho$, there are $m - \rho$ linearly independent such relations, and the system can be reduced to $\rho$ independent variables.

**Proof** $\mathrm{d}(\boldsymbol{\ell}\boldsymbol{x})/\mathrm{d}t = \boldsymbol{\ell}N\boldsymbol{v} = 0$. The left null space of an $m \times r$ matrix of rank $\rho$ has dimension $m - \rho$. Choosing a basis $L$ of it, $L\boldsymbol{x} = L\boldsymbol{x}_0$ gives $m - \rho$ linear equations that express $m - \rho$ concentrations in terms of the others. $\square$

**Definition 14.2.2 (Conserved Moiety)** A linear combination $\boldsymbol{\ell}\boldsymbol{x}$ with $\boldsymbol{\ell}N = \boldsymbol{0}$ and nonnegative coefficients is a **conserved moiety**: a chemical group (an enzyme, a phosphate, a coenzyme such as $\mathrm{NAD^+/NADH}$, the adenine nucleotides) that is transferred between species but never created or destroyed in the network.

**Example 14.2.2** The matrix $N$ of Example 14.2.1 has rank $2$, so there are two conservation laws: $\boldsymbol{\ell}_1 = (1, 0, 1, 0)$, total enzyme $E_{\mathrm{T}} = [E] + [C]$, and $\boldsymbol{\ell}_2 = (0, 1, 1, 1)$, total substrate in all forms $S_0 = [S] + [C] + [P]$. Only two equations remain, for $[S]$ and $[C]$:
$$
\frac{\mathrm{d}[S]}{\mathrm{d}t} = -k_1(E_{\mathrm{T}} - [C])[S] + k_{-1}[C], \qquad \frac{\mathrm{d}[C]}{\mathrm{d}t} = k_1(E_{\mathrm{T}} - [C])[S] - (k_{-1} + k_2)[C]. \tag{14.2}
$$

Conservation laws matter numerically as well as conceptually: if all $m$ equations are kept, the Jacobian of the system is singular (14.4), and the steady state is not unique until the conserved totals are fixed.

### 14.2.3. Time-Scale Separation and Quasi-Steady States

Equations (14.2) still contain a fast process, binding, and a slow one, conversion of the substrate. If the complex adjusts to the substrate much faster than the substrate changes, one may set $\mathrm{d}[C]/\mathrm{d}t \approx 0$ in the second equation (the **quasi-steady-state approximation**), solve for $[C]$ and obtain the **Michaelis–Menten equation** $\mathrm{d}[S]/\mathrm{d}t = -V_{\max}[S]/(K_{\mathrm{M}} + [S])$ with $V_{\max} = k_2E_{\mathrm{T}}$ and $K_{\mathrm{M}} = (k_{-1} + k_2)/k_1$; the derivation, and its assumptions, are those of [7.1.9](/7.1.9). The question for modeling is when the reduction is valid.

**Formula 14.2.1 (Validity of the Quasi-Steady State)** For the enzyme scheme started at $[S] = S_0$, $[C] = 0$, the standard quasi-steady-state approximation is accurate when (Segel and Slemrod, 1989)
$$
\frac{E_{\mathrm{T}}}{S_0 + K_{\mathrm{M}}} \ll 1 .
$$
It follows from comparing the time $t_C = 1/[k_1(S_0 + K_{\mathrm{M}})]$ in which the complex approaches its quasi-steady level with the time $t_S = (S_0 + K_{\mathrm{M}})/(k_2E_{\mathrm{T}})$ over which the substrate changes appreciably, and from requiring that little substrate be consumed during the initial transient.

The usual textbook condition $E_{\mathrm{T}} \ll S_0$ is sufficient but not necessary: the approximation also holds at low substrate if $E_{\mathrm{T}} \ll K_{\mathrm{M}}$. When neither holds, a better reduction is the total quasi-steady-state approximation (Borghans, de Boer and Segel, 1996): write the equation for the total substrate $\hat S = [S] + [C]$, $\mathrm{d}\hat S/\mathrm{d}t = -k_2[C]$, and take for $[C]$ the quasi-steady root of $[C]^2 - (E_{\mathrm{T}} + K_{\mathrm{M}} + \hat S)[C] + E_{\mathrm{T}}\hat S = 0$,
$$
[C] = \tfrac12\Bigl(E_{\mathrm{T}} + K_{\mathrm{M}} + \hat S - \sqrt{(E_{\mathrm{T}} + K_{\mathrm{M}} + \hat S)^2 - 4E_{\mathrm{T}}\hat S}\Bigr),
$$
which remains accurate when enzyme and substrate are comparable, as for many signaling proteins whose substrates are other proteins at similar concentrations.

![When the Michaelis–Menten rate law may replace the mass-action scheme (k₁ = 1, k₋₁ = 9, k₂ = 1, so K_M = 10; S₀ = 50; model units). A: with E_T = 0.1, E_T/(S₀ + K_M) = 0.0017; the complex (dashed, right axis) reaches its quasi-steady level within about 0.1 time units, after which the product curves of the full model (solid) and of the Michaelis–Menten equation (dots) coincide (logarithmic time axis). B: with E_T = 20 (ratio 0.33) the standard approximation (dotted) runs ahead of the full model because a third of the substrate is held in the complex; the total quasi-steady-state approximation (dashed) follows the full model](./plots/qssa.py)

**Example 14.2.3** In the figure, with $E_{\mathrm{T}} = 0.1$ the largest difference between the product curves of the full model and of the Michaelis–Menten equation is $0.06\,\%$ of $S_0$, and the half-conversion times are $319.5$ and $319.3$. With $E_{\mathrm{T}} = 20$ the difference reaches $11.7\,\%$ of $S_0$ and the half-conversion times are $1.83$ (full) and $1.60$ (standard approximation); the total approximation gives $1.82$, with a largest error of $0.5\,\%$.

### 14.2.4. Rate Laws for Larger Networks

Above the level of single enzymes, models use phenomenological rate laws whose parameters summarize several elementary steps: Michaelis–Menten terms for modification enzymes, **Hill equations** for cooperative binding and transcriptional regulation ([7.6.4](/7.6.4), [7.6.33](/7.6.33#sec-33.1.2)), and their combination for covalent modification cycles, whose **zero-order ultrasensitivity** arises when both converting enzymes are saturated ([7.1.9](/7.1.9#sec-9.6.1)).

**Example 14.2.4** A generic three-component repressive network (Mogilner, Wollman and Marshall, 2006, a simplified form of an oscillatory circuit in soil bacteria) has proteins $A$, $B$, $C$ that exist in unmodified and phosphorylated forms: $C$ catalyzes the phosphorylation of $A$, $A$ the dephosphorylation of $B$, and $B$ the dephosphorylation of $C$. With Michaelis–Menten rate laws for every conversion, the equations for $A$ and its phosphorylated form $A_{\mathrm{p}}$ are
$$
\frac{\mathrm{d}[A]}{\mathrm{d}t} = \frac{k_{\mathrm{p}1}[A_{\mathrm{p}}]}{[A_{\mathrm{p}}] + K_{\mathrm{p}1}} - \frac{k_{\mathrm{k}1}[A][C]}{[A] + K_{\mathrm{k}1}}, \qquad \frac{\mathrm{d}[A_{\mathrm{p}}]}{\mathrm{d}t} = -\frac{\mathrm{d}[A]}{\mathrm{d}t},
$$
and the conservation law $[A] + [A_{\mathrm{p}}] = A_{\mathrm{T}}$ eliminates $[A_{\mathrm{p}}]$. Doing the same for $B$ and $C$ leaves three equations of the form
$$
\frac{\mathrm{d}[A]}{\mathrm{d}t} = \frac{k_{\mathrm{p}1}(A_{\mathrm{T}} - [A])}{A_{\mathrm{T}} - [A] + K_{\mathrm{p}1}} - \frac{k_{\mathrm{k}1}[A][C]}{[A] + K_{\mathrm{k}1}},
$$
a negative feedback loop of three stages that, like the **repressilator** ([7.6.33](/7.6.33#sec-33.5.3)), oscillates for some parameter values and settles to a steady state for others.

The example shows the general procedure: list the species including every modified form, list the conversions and assign each a rate law, add the conservation laws, and check units. It also shows the main obstacle: diagrams are often ambiguous. An arrow "MEK → ERK" in a signaling diagram stands for two phosphorylations of ERK by MEK, two dephosphorylations by phosphatases, and the same for MEK itself; equations can be written for the detailed scheme, not for the arrow. Some diagrams cannot be converted at all, because they omit the mechanism between a receptor and its effect or skip intermediate kinases. Writing equations is therefore a test of a diagram: every arrow must be said to be a conversion, a catalysis or a regulation, which is exactly the distinction that SBGN process diagrams enforce.

### 14.2.5. The Simplest Oscillating Network

The Lotka–Volterra system is the simplest network with a sustained oscillation: prey $x$ grow and are eaten, predators $y$ grow by eating and die,
$$
\dot x = x(\alpha - \beta y), \qquad \dot y = y(-\gamma + \delta x). \tag{14.3}
$$
In network terms it is a negative feedback loop of two nodes, $x$ activating $y$ and $y$ inhibiting $x$, built from mass-action terms. Its positive solutions are closed orbits around the equilibrium $(\gamma/\delta, \alpha/\beta)$, because $\Phi(x, y) = \delta x - \gamma\ln x + \beta y - \alpha\ln y$ is a **first integral** ([Example 14.1.2](/2.4.14#ex-14.1.2)). Two properties set it apart from biological oscillators. The amplitude is not selected by the system but fixed by the initial condition, and any perturbation moves it to a different orbit. And the structure is fragile: adding a self-limitation of the prey ($-\varepsilon x^2$) turns the closed orbits into spirals toward a stable equilibrium. Robust biological oscillators are **limit cycles** (14.4); the ecological use of Eq. (14.3) is the subject of [7.19](/7.19), and its first integral makes it a good test of numerical methods (14.3).

## 14.3. Numerical Solution

Few kinetic models can be solved in closed form. Numerical methods compute the solution of the **initial value problem** $\dot{\boldsymbol{x}} = \boldsymbol{f}(t, \boldsymbol{x})$, $\boldsymbol{x}(t_0) = \boldsymbol{x}_0$ at discrete times $t_n = t_0 + nh$.

### 14.3.1. The Euler Method

**Algorithm 14.3.1 (Euler Method)** Given $\boldsymbol{x}_0$ and a step size $h$, for $n = 0, 1, 2, \dots$ set
$$
\boldsymbol{x}_{n+1} = \boldsymbol{x}_n + h\,\boldsymbol{f}(t_n, \boldsymbol{x}_n). \tag{14.4}
$$

The Euler method follows the tangent of the solution through the current point for one step: it is the construction of the **Euler polygon** of [2.4.4](/2.4.4) used as an algorithm. For a model it is coded as a loop: define the constants, the step size and the initial state, and at each step compute $\mathrm{d}\boldsymbol{x}/\mathrm{d}t$ and update $\boldsymbol{x}$.

**Example 14.3.1** For $\dot x = a - bx$ with $a = 20$, $b = 2$, $x(0) = 5$ and $h = 0.05$, the first steps are $\dot x(0) = 20 - 10 = 10$, $x_1 = 5 + 0.05 \times 10 = 5.5$; $\dot x = 20 - 11 = 9$, $x_2 = 5.5 + 0.05 \times 9 = 5.95$. The exact solution is $x(t) = a/b - (a/b - c)\mathrm{e}^{-bt}$ with $c = x(0)$, so $x(1) = 10 - 5\mathrm{e}^{-2} = 9.3233$; twenty Euler steps give $9.3921$, an error of $0.069$. With $h = 0.025$ the error is $0.034$: halving the step halves the error.

Two properties of a method determine its use.

**Theorem 14.3.1 (Convergence of the Euler Method)** Let $\boldsymbol{f}$ be continuously differentiable and Lipschitz in $\boldsymbol{x}$ with constant $L$, and let the solution have a bounded second derivative, $\lVert\ddot{\boldsymbol{x}}\rVert \le M$, on $[t_0, T]$. Then the Euler approximations satisfy
$$
\lVert\boldsymbol{x}_n - \boldsymbol{x}(t_n)\rVert \le \frac{hM}{2L}\bigl(\mathrm{e}^{L(t_n - t_0)} - 1\bigr),
$$
so the global error is $O(h)$: the method has order $1$.

**Proof** The local error of one step started on the true solution is, by Taylor's theorem, at most $Mh^2/2$. Let $e_n = \lVert\boldsymbol{x}_n - \boldsymbol{x}(t_n)\rVert$. Subtracting $\boldsymbol{x}(t_{n+1}) = \boldsymbol{x}(t_n) + h\boldsymbol{f}(t_n, \boldsymbol{x}(t_n)) + \boldsymbol{\tau}_n$ from Eq. (14.4) and using the Lipschitz bound gives $e_{n+1} \le (1 + hL)e_n + Mh^2/2$, with $e_0 = 0$. By induction $e_n \le \frac{Mh^2}{2}\sum_{k<n}(1 + hL)^k = \frac{Mh}{2L}\bigl((1 + hL)^n - 1\bigr) \le \frac{Mh}{2L}(\mathrm{e}^{nhL} - 1)$. $\square$

The second property is stability. For the test equation $\dot x = -\lambda x$ with $\lambda > 0$, whose solutions decay, Euler's method gives $x_{n+1} = (1 - h\lambda)x_n$, which decays only if $\lvert 1 - h\lambda\rvert < 1$, that is, if $h < 2/\lambda$. With a larger step the numerical solution oscillates with growing amplitude, takes values such as $10^{78}$, and concentrations that must be nonnegative become negative. In Example 14.3.1, $\lambda = b = 2$ and the limit is $h = 1$ (panel B of the figure): with $h = 0.9$ the iterates oscillate around $10$ and converge slowly, with $h = 1.1$ they diverge.

### 14.3.2. Runge–Kutta Methods and Adaptive Steps

Better methods evaluate $\boldsymbol{f}$ several times per step and combine the slopes so that the low-order error terms cancel.

**Algorithm 14.3.2 (Classical Runge–Kutta Method)** For $n = 0, 1, 2, \dots$ compute
$$
\boldsymbol{k}_1 = \boldsymbol{f}(t_n, \boldsymbol{x}_n), \quad \boldsymbol{k}_2 = \boldsymbol{f}\bigl(t_n + \tfrac h2, \boldsymbol{x}_n + \tfrac h2\boldsymbol{k}_1\bigr), \quad \boldsymbol{k}_3 = \boldsymbol{f}\bigl(t_n + \tfrac h2, \boldsymbol{x}_n + \tfrac h2\boldsymbol{k}_2\bigr), \quad \boldsymbol{k}_4 = \boldsymbol{f}(t_n + h, \boldsymbol{x}_n + h\boldsymbol{k}_3),
$$
$$
\boldsymbol{x}_{n+1} = \boldsymbol{x}_n + \tfrac h6(\boldsymbol{k}_1 + 2\boldsymbol{k}_2 + 2\boldsymbol{k}_3 + \boldsymbol{k}_4).
$$

The Runge–Kutta method of Algorithm 14.3.2 has order $4$: its global error is $O(h^4)$, so halving the step reduces the error sixteenfold, for four evaluations of $\boldsymbol{f}$ per step. Heun's method, $\boldsymbol{x}_{n+1} = \boldsymbol{x}_n + \tfrac h2[\boldsymbol{f}(t_n, \boldsymbol{x}_n) + \boldsymbol{f}(t_{n+1}, \boldsymbol{x}_n + h\boldsymbol{f}(t_n, \boldsymbol{x}_n))]$, is the second-order member of the family.

![Numerical solution of ordinary differential equations. A: error at t = 1 of the Euler method, Heun's method and the classical fourth-order Runge–Kutta method for dx/dt = a − bx (a = 20, b = 2, x(0) = 5) against the step size h, on logarithmic axes; the slopes are the orders 1, 2 and 4. B: Euler solutions with three step sizes; for hb > 2 the iteration diverges although the true solution relaxes to a/b = 10. C: the Lotka–Volterra system x′ = x(1 − 0.1y), y′ = y(−1.5 + 0.075x) from (10, 5) over 50 time units: the exact orbit is closed, the Euler solution with h = 0.01 spirals outward, the Runge–Kutta solution with h = 0.1 stays on the orbit](./plots/ode_methods.py)

**Example 14.3.2** For the equation of Example 14.3.1 the Runge–Kutta error at $t = 1$ is $1.2 \times 10^{-6}$ with $h = 0.05$ and $7.3 \times 10^{-8}$ with $h = 0.025$, a ratio of $16.7$. For the Lotka–Volterra system of panel C ($\alpha = 1$, $\beta = 0.1$, $\gamma = 1.5$, $\delta = 0.075$), the first integral $\Phi$ should stay at its initial value $-3.813$. After $50$ time units (about nine periods of $5.48$) Euler's method has increased it by $0.51$ with $h = 0.01$ ($5000$ steps) and by $0.036$ with $h = 0.001$; the Runge–Kutta method has changed it by $4 \times 10^{-6}$ with $h = 0.1$ ($500$ steps, $2000$ evaluations). A method that does not preserve the first integral turns a conservative system into a dissipative or an explosive one, a qualitative error that can be mistaken for biology.

Fixed steps waste effort where the solution is smooth and are too large where it changes quickly. Modern solvers choose the step adaptively. An embedded pair of Runge–Kutta formulas of orders $p$ and $p + 1$ that share their evaluations (Dormand and Prince, orders $4$ and $5$, the default `RK45` of `solve_ivp`) gives two estimates of $\boldsymbol{x}_{n+1}$; their difference estimates the local error, the step is accepted if the error is below $\mathrm{atol} + \mathrm{rtol}\,\lvert x\rvert$ componentwise and rejected otherwise, and the next step is enlarged or reduced accordingly. In the Lotka–Volterra example, `RK45` with $\mathrm{rtol} = 10^{-3}$ needs $566$ evaluations and changes $\Phi$ by $0.011$, with $\mathrm{rtol} = 10^{-6}$ it needs $1676$ evaluations and changes it by $2 \times 10^{-6}$. The tolerances are part of the model specification: $\mathrm{atol}$ must be small compared with the smallest concentration that matters, or species at low concentration are computed with no accurate digits. The solvers and their options are described in [4.4.4](/4.4.4#sec-4.3.2).

### 14.3.3. Stiffness

Biochemical networks combine fast and slow processes: binding in milliseconds, transcription in minutes, growth in hours. When a system has decaying modes much faster than the solution that is being followed, explicit methods must take steps limited by the fastest mode, $h < 2/\lambda_{\max}$, long after that mode has died away. Such a system is stiff (**stiffness**, [4.4.4](/4.4.4#sec-4.3.3)). The ratio of the largest to the smallest decay rate, the eigenvalues of the Jacobian (14.4), measures it.

**Example 14.3.3** The enzyme system (14.2) with $k_1 = 1$, $k_{-1} = 9$, $k_2 = 1$, $E_{\mathrm{T}} = 0.1$ and $S_0 = 50$ has, after the initial transient, Jacobian eigenvalues $-60.0$ (relaxation of the complex) and $-2.8 \times 10^{-4}$ (conversion of the substrate), a ratio of $2 \times 10^5$. Integrating to $t = 1500$, which converts almost all the substrate, with $\mathrm{rtol} = 10^{-6}$: the explicit `RK45` needs $65\,630$ evaluations of $\boldsymbol{f}$; the implicit `BDF` (backward differentiation formulas) $518$, `Radau` (implicit Runge–Kutta) $1084$, and `LSODA`, which switches automatically between explicit and implicit methods, $463$.

Implicit methods, such as the backward Euler method $\boldsymbol{x}_{n+1} = \boldsymbol{x}_n + h\boldsymbol{f}(t_{n+1}, \boldsymbol{x}_{n+1})$, solve an equation at every step, by Newton's method with the Jacobian, and are stable for all step sizes on decaying modes: for $\dot x = -\lambda x$ the backward Euler iteration $x_{n+1} = x_n/(1 + h\lambda)$ decays for every $h > 0$. Their cost per step is higher, their number of steps is set by accuracy instead of stability. A practical rule for network models: try an explicit solver; if it is slow or needs very small steps, switch to `LSODA` or `BDF` and supply the Jacobian if it can be written down.

## 14.4. Steady States, Stability and Bifurcations

### 14.4.1. Linearization

A steady state $\boldsymbol{x}^*$ of Eq. (14.1) solves $N\boldsymbol{v}(\boldsymbol{x}^*, \boldsymbol{p}) = \boldsymbol{0}$ (after elimination of conserved moieties). Its stability is decided, if no eigenvalue has zero real part, by the **Jacobian matrix** $J = \partial\boldsymbol{f}/\partial\boldsymbol{x}$ at $\boldsymbol{x}^*$: the steady state is asymptotically stable if all **eigenvalues** of $J$ have negative real parts and unstable if one has a positive real part ([2.4.11](/2.4.11#sec-11.3)). For a planar system the eigenvalues are determined by $\tau = \operatorname{tr}J$ and $\Delta = \det J$: $\Delta < 0$ gives a saddle; $\Delta > 0$ and $\tau < 0$ a stable node or focus; $\Delta > 0$ and $\tau > 0$ an unstable one; complex eigenvalues ($\tau^2 < 4\Delta$) give spirals ([2.4.11](/2.4.11#sec-11.5.2)). The **phase plane**, with the **nullclines** on which one derivative vanishes and the **direction field** between them ([7.6.33](/7.6.33#sec-33.3.1)), shows the rest of the dynamics: nullclines divide the plane into regions in which the signs of both derivatives are fixed, and a trajectory changes direction only when it crosses one.

### 14.4.2. The Bier Model of Glycolytic Oscillations

Yeast cells in suspension, starved and then given glucose, show oscillations of NADH and other glycolytic intermediates with periods of about a minute (**glycolytic oscillations**, [7.1.18](/7.1.18), [6.3.18](/6.3.18#sec-18.3.3)). The source of the oscillation is phosphofructokinase, which consumes ATP but is activated by its products, so that ATP made downstream accelerates its own consumption: an autocatalytic loop. Many models exist; one of the simplest keeps two variables (Bier, Bakker and Westerhoff, 2000).

**Definition 14.4.1 (Bier Model)** With $G$ the concentration of glucose inside the cell and $T$ that of ATP, glucose enters at a constant rate $V_{\mathrm{in}}$, is phosphorylated in a step that consumes ATP and whose rate is proportional to both ($k_1GT$), producing net ATP at twice this rate in lower glycolysis, and ATP is consumed by ATPases with Michaelis–Menten kinetics:
$$
\frac{\mathrm{d}G}{\mathrm{d}t} = V_{\mathrm{in}} - k_1GT, \qquad \frac{\mathrm{d}T}{\mathrm{d}t} = 2k_1GT - \frac{k_{\mathrm{p}}T}{T + K_{\mathrm{m}}}. \tag{14.5}
$$

**Example 14.4.1** The nullclines are $G = V_{\mathrm{in}}/(k_1T)$ ($\dot G = 0$) and $G = k_{\mathrm{p}}/[2k_1(T + K_{\mathrm{m}})]$ ($\dot T = 0$, for $T > 0$). Equating them gives the unique steady state
$$
T^* = \frac{2V_{\mathrm{in}}K_{\mathrm{m}}}{k_{\mathrm{p}} - 2V_{\mathrm{in}}}, \qquad G^* = \frac{V_{\mathrm{in}}}{k_1T^*},
$$
which exists if $k_{\mathrm{p}} > 2V_{\mathrm{in}}$ (the ATPases can consume the ATP made from the glucose supply). With $V_{\mathrm{in}} = 0.36$, $k_1 = 0.02$, $k_{\mathrm{p}} = 6$ (model units) and $K_{\mathrm{m}} = 13$: $T^* = 9.36/5.28 = 1.773$ and $G^* = 10.15$. The Jacobian, using $2k_1G^* = k_{\mathrm{p}}/(T^* + K_{\mathrm{m}})$ at the steady state, is
$$
J = \begin{bmatrix} -k_1T^* & -k_1G^* \\ 2k_1T^* & \dfrac{k_{\mathrm{p}}T^*}{(T^* + K_{\mathrm{m}})^2} \end{bmatrix}, \qquad
\operatorname{tr}J = \frac{k_{\mathrm{p}}T^*}{(T^* + K_{\mathrm{m}})^2} - k_1T^*, \qquad \det J = \frac{k_1k_{\mathrm{p}}K_{\mathrm{m}}T^*}{(T^* + K_{\mathrm{m}})^2} > 0 .
$$
For $K_{\mathrm{m}} = 13$, $\operatorname{tr}J = 0.0133 > 0$ and $\det J = 0.0127$: the eigenvalues $0.0066 \pm 0.1124\,\mathrm{i}$ make the steady state an unstable focus. For $K_{\mathrm{m}} = 20$ ($T^* = 2.727$, $G^* = 6.60$), $\operatorname{tr}J = -0.0229$ and the eigenvalues $-0.0114 \pm 0.1120\,\mathrm{i}$ make it a stable focus.

The positive diagonal entry $\partial\dot T/\partial T > 0$ is the autocatalysis: more ATP speeds up the step that makes more ATP. It destabilizes the steady state when it outweighs the damping $k_1T^*$ of glucose consumption. Because the steady state is the only one and trajectories stay in a bounded region, an unstable focus is surrounded by a stable **limit cycle** by the Poincaré–Bendixson theorem ([2.4.11](/2.4.11#sec-11.6.2)).

![The Bier model of yeast glycolytic oscillations, Eq. (14.5) (V_in = 0.36, k₁ = 0.02, k_p = 6; model units). A: phase plane for K_m = 13 with the two nullclines, the direction field and a trajectory started next to the steady state (open circle): the steady state is an unstable focus and the trajectory winds out onto a stable limit cycle. B: for K_m = 20 a trajectory started far away spirals into the stable focus (filled circle). C: bifurcation diagram, the minimum and maximum of G on the attractor against K_m; the oscillation is born at the supercritical Hopf bifurcation K_m = 15.24, where the trace of the Jacobian vanishes; to its left the dashed line is the unstable steady state](./plots/bier_phase.py)

### 14.4.3. The Hopf Bifurcation and Bifurcation Diagrams

A change of qualitative behavior as a parameter passes a critical value is a **bifurcation**. In the Bier model, $\det J$ is positive for all $K_{\mathrm{m}}$ (it equals $0.0127$ whatever $K_{\mathrm{m}}$, because $T^*$ is proportional to $K_{\mathrm{m}}$), while $\operatorname{tr}J$ changes sign: a pair of complex eigenvalues crosses the imaginary axis, the signature of a **Hopf bifurcation** ([2.4.11](/2.4.11#sec-11.6.4), [7.6.33](/7.6.33#sec-33.5.2)).

**Example 14.4.2** Setting $\operatorname{tr}J = 0$ gives $(T^* + K_{\mathrm{m}})^2 = k_{\mathrm{p}}/k_1 = 300$. With $T^* = 0.1364K_{\mathrm{m}}$, the critical value is $K_{\mathrm{m}} = \sqrt{300}/1.1364 = 15.24$, and the eigenvalues there are $\pm 0.1126\,\mathrm{i}$, so the oscillation is born with period $2\pi/0.1126 = 55.8$. Simulation shows a supercritical bifurcation: the amplitude of the cycle grows continuously from zero as $K_{\mathrm{m}}$ decreases below $15.24$, approximately as $4.6\sqrt{15.24 - K_{\mathrm{m}}}$ in $G$ ($0.94$ at $K_{\mathrm{m}} = 15.2$, $2.26$ at $15.0$), and trajectories started near or far from the steady state reach the same cycle. At $K_{\mathrm{m}} = 13$ the cycle has period $68.5$, $G$ oscillates between $3.07$ and $17.6$ and $T$ between $0.05$ and $12.4$: far from the Hopf point the oscillation is a large, nonsinusoidal relaxation with a lengthened period.

A brute-force bifurcation diagram, as in panel C, simulates the model for many parameter values and records the extremes of the variables after transients have died out. Near the bifurcation the transients decay slowly (at $K_{\mathrm{m}} = 15.3$ the real part of the eigenvalues is only $-1.3 \times 10^{-4}$, a decay time of several thousand time units), and a simulation of limited length misplaces the critical point: a sweep that records only the last $500$ time units after a short run places it near $16$ instead of $15.24$. The analytic condition, or numerical continuation, avoids this. Continuation methods follow a branch of steady states as a parameter varies by predicting the next point from the tangent of the branch and correcting it with Newton's method (pseudo-arclength continuation, which also passes around folds where the branch turns back), monitor the eigenvalues of $J$ along the branch to detect saddle-node and Hopf points, and then follow the periodic orbits born at Hopf points; AUTO, MatCont and XPPAUT implement them. The **saddle-node bifurcations** behind switches and hysteresis are treated in [7.6.33](/7.6.33#sec-33.2.2), and the biological uses of such diagrams, in cell-fate switches and in the cell cycle, in [7.9.16](/7.9.16).

## 14.5. Sensitivity and Control

### 14.5.1. Sensitivity Coefficients

How much does a model's behavior depend on each parameter? The question matters in three ways: for robustness (a function that depends on fine-tuned parameters is fragile, [7.6.40](/7.6.40)), for experimental design (parameters to which the observations are insensitive cannot be estimated, 14.7), and for intervention (a drug acts by changing a parameter).

**Definition 14.5.1 (Sensitivity Coefficient)** For a model output $y$ (a concentration at time $t$, a steady-state level, a period) and a parameter $p$, the *sensitivity coefficient* is $\partial y/\partial p$, and the scaled sensitivity coefficient is the **logarithmic sensitivity** $S^y_p = \partial\ln y/\partial\ln p$ ([Definition 40.1.2](/7.6.40#def-40.1.2)), the relative change of the output per relative change of the parameter.

**Formula 14.5.1 (Sensitivity Equations)** Let $\boldsymbol{x}(t; \boldsymbol{p})$ solve $\dot{\boldsymbol{x}} = \boldsymbol{f}(\boldsymbol{x}, \boldsymbol{p})$ and let $S(t) = \partial\boldsymbol{x}/\partial\boldsymbol{p}$ be the $m \times q$ matrix of sensitivities to the $q$ parameters. Then
$$
\dot S = J(t)S + \frac{\partial\boldsymbol{f}}{\partial\boldsymbol{p}}, \qquad S(0) = \frac{\partial\boldsymbol{x}_0}{\partial\boldsymbol{p}}, \tag{14.6}
$$
with $J(t) = \partial\boldsymbol{f}/\partial\boldsymbol{x}$ evaluated along the solution; at a stable steady state ($\dot S = 0$),
$$
\frac{\partial\boldsymbol{x}^*}{\partial\boldsymbol{p}} = -J^{-1}\frac{\partial\boldsymbol{f}}{\partial\boldsymbol{p}}. \tag{14.7}
$$

**Proof** Differentiate $\dot{\boldsymbol{x}} = \boldsymbol{f}(\boldsymbol{x}, \boldsymbol{p})$ with respect to $\boldsymbol{p}$ and exchange the order of differentiation (justified by the differentiable dependence of solutions on parameters, [2.4.7](/2.4.7)). Equation (14.7) is the **implicit function theorem** applied to $\boldsymbol{f}(\boldsymbol{x}^*, \boldsymbol{p}) = \boldsymbol{0}$; $J$ is invertible because no eigenvalue of a stable steady state is zero. $\square$

The sensitivity equations are solved together with the model, which roughly multiplies the cost by $q + 1$; they are more accurate than finite differences, which need a step small enough for the derivative and large enough to exceed the solver's error.

**Example 14.5.1** For the induction of a gene, $\dot x = \beta - \alpha x$ with $x(0) = 0$ and solution $x = (\beta/\alpha)(1 - \mathrm{e}^{-\alpha t})$ ([Example 1.5.1](/7.9.1#ex-1.5.1)), the sensitivities are
$$
\frac{\partial x}{\partial\beta} = \frac{1 - \mathrm{e}^{-\alpha t}}{\alpha}, \qquad \frac{\partial x}{\partial\alpha} = -\frac{\beta}{\alpha^2}\bigl(1 - \mathrm{e}^{-\alpha t}\bigr) + \frac{\beta}{\alpha}t\,\mathrm{e}^{-\alpha t}.
$$
At steady state $S^x_\beta = 1$ and $S^x_\alpha = -1$. At early times, $\partial x/\partial\beta \approx t$ and $\partial x/\partial\alpha \approx -\beta t^2/2$: the sensitivity to the degradation rate is of second order in $t$, which is why early measurements determine $\beta$ and not $\alpha$.

Local sensitivities describe small changes around one parameter set. When parameters are uncertain by orders of magnitude, global methods sample the parameter space, for example on a Latin hypercube in logarithmic coordinates, and decompose the variance of the output into contributions of each parameter and their interactions (Sobol indices); the parameter-robustness study of the segment polarity network ([7.6.40](/7.6.40#sec-40.2.3)) is a global analysis of this kind.

### 14.5.2. Control Coefficients of Networks

**Metabolic control analysis** ([7.1.17](/7.1.17#sec-17.4)) is sensitivity analysis of steady states with respect to enzyme activities, expressed through two kinds of coefficients: the **flux control coefficient** $C^J_i = \partial\ln J/\partial\ln e_i$, a property of the system, and the **elasticity coefficient** $\varepsilon^{v_i}_{S}$, a local property of one rate law. For a linear pathway the summation and connectivity theorems determine the control coefficients from the elasticities. Formula (14.7) extends this to any network.

**Theorem 14.5.1 (Control Coefficients of a Network)** Let $\dot{\boldsymbol{s}} = N\boldsymbol{v}(\boldsymbol{s}, \boldsymbol{e})$ have a stable steady state with metabolite concentrations $\boldsymbol{s}$ and fluxes $\boldsymbol{J} = \boldsymbol{v}$, where each rate $v_i$ is proportional to the activity $e_i$ of its enzyme and $N$ has full row rank (conserved moieties eliminated). Let $\varepsilon$ be the $r \times m$ matrix of scaled elasticities $\varepsilon_{ij} = \partial\ln v_i/\partial\ln s_j$ and $D = \operatorname{diag}(\boldsymbol{J})$. Then the matrices of *concentration control coefficients* $C^S_{ji} = \partial\ln s_j/\partial\ln e_i$ and flux control coefficients $C^J_{ki} = \partial\ln J_k/\partial\ln e_i$ are
$$
C^S = -(ND\varepsilon)^{-1}ND, \qquad C^J = I + \varepsilon C^S, \tag{14.8}
$$
and they satisfy the summation theorems $C^J\boldsymbol{1} = \boldsymbol{1}$, $C^S\boldsymbol{1} = \boldsymbol{0}$ and the connectivity theorems $C^J\varepsilon = O$, $C^S\varepsilon = -I$.

**Proof** At steady state $N\boldsymbol{v}(\boldsymbol{s}(\boldsymbol{e}), \boldsymbol{e}) = \boldsymbol{0}$. Differentiating with respect to $\ln e_i$, with $\partial\boldsymbol{v}/\partial\ln e_i = v_i\boldsymbol{u}_i$ ($\boldsymbol{u}_i$ the $i$th unit vector) and $\partial\boldsymbol{v}/\partial\ln\boldsymbol{s} = D\varepsilon$, gives $ND\varepsilon\,C^S + ND = O$, hence the first formula ($ND\varepsilon$ is the Jacobian in logarithmic coordinates up to a diagonal factor, invertible at a stable steady state). The fluxes depend on $e_i$ directly and through $\boldsymbol{s}$: $\partial\ln\boldsymbol{J}/\partial\ln e_i = \boldsymbol{u}_i + \varepsilon\,\partial\ln\boldsymbol{s}/\partial\ln e_i$, which is the second formula. Summation: $ND\boldsymbol{1} = N\boldsymbol{J} = \boldsymbol{0}$, so $C^S\boldsymbol{1} = \boldsymbol{0}$ and $C^J\boldsymbol{1} = \boldsymbol{1}$. Connectivity: $C^S\varepsilon = -(ND\varepsilon)^{-1}ND\varepsilon = -I$, and $C^J\varepsilon = \varepsilon + \varepsilon C^S\varepsilon = O$. $\square$

For a linear pathway these reduce to Theorems [17.4.1](/7.1.17#thm-17.4.1) and [17.4.2](/7.1.17#thm-17.4.2). The concentration theorems say that increasing all enzymes by the same factor changes no concentration, and that a metabolite's control over itself, through the elasticities of the enzymes around it, is homeostatic ($-1$). In branched networks new effects appear.

![Metabolic control analysis of a branched pathway. A: enzyme 1 converts the fixed source X₀ into S₁ and is inhibited by its product; S₁ is converted by enzymes 2 and 3 through S₂ into P, or diverted by enzyme 4 into Q (irreversible Michaelis–Menten rate laws; V₁ = 10, K₁ = 0.5, K_i = 1, V₂ = 4, K₂ = 1, V₃ = 10, K₃ = 1, V₄ = 6, K₄ = 2, X₀ = 1). B: flux control coefficients from Eq. (14.8); each row sums to one; enzyme 4 has negative control over the flux to P and enzyme 2 over the flux to Q; enzyme 3 has none, because S₂ acts on no other step. C: steady fluxes J_P and J_Q, relative to the reference state, when the amount of enzyme 4 is varied from 0.25 to 4 times its reference value (logarithmic axes); the slopes at the reference point are the control coefficients of enzyme 4](./plots/branched_mca.py)

**Example 14.5.2** For the branched pathway of the figure the steady state is $s_1 = 0.845$, $s_2 = 0.224$ with fluxes $J_1 = 3.61$ into the branch point, $J_P = 1.83$ and $J_Q = 1.78$. The elasticities are $\varepsilon^{v_1}_{S_1} = -0.46$ (product inhibition), $\varepsilon^{v_2}_{S_1} = 0.54$, $\varepsilon^{v_4}_{S_1} = 0.70$ and $\varepsilon^{v_3}_{S_2} = 0.82$. Equation (14.8) gives the control coefficients of panel B (rows: fluxes; columns: enzymes 1 to 4):

| | $e_1$ | $e_2$ | $e_3$ | $e_4$ | sum |
|---|---|---|---|---|---|
| $J_1$ (supply) | 0.58 | 0.22 | 0 | 0.21 | 1 |
| $J_P$ | 0.50 | 0.75 | 0 | −0.25 | 1 |
| $J_Q$ | 0.65 | −0.33 | 0 | 0.68 | 1 |

They agree with finite-difference derivatives to four decimals. Increasing enzyme 4 lowers $s_1$ and therefore the flux to $P$; halving it raises $J_P$ by $15\,\%$ and lowers $J_Q$ by $40\,\%$. Enzyme 3 has no control over any flux, because its substrate $S_2$ affects no other rate; it controls only $s_2$ ($C^{S_2}_3 = -1.22$). In metabolic engineering the negative entries are the opportunity: to increase the flux to a product, one can slow a competing branch, as well as speed up the producing one.

**Theorem 14.5.2 (Combined Response Theorem)** Let an external effector $X$ (an inhibitor, an activator, a hormone) act directly only on the rate $v_i$, with elasticity $\varepsilon^{v_i}_X = \partial\ln v_i/\partial\ln X$. Then the response coefficient of any flux or concentration $Y$ to $X$, $R^Y_X = \mathrm{d}\ln Y/\mathrm{d}\ln X$, is
$$
R^Y_X = C^Y_i\,\varepsilon^{v_i}_X .
$$
If $X$ acts on several steps, $R^Y_X = \sum_iC^Y_i\varepsilon^{v_i}_X$.

**Proof** At fixed metabolite concentrations, a change of $\ln X$ by $\delta$ changes $\ln v_i$ by $\varepsilon^{v_i}_X\delta$, exactly as a change of $\ln e_i$ by $\varepsilon^{v_i}_X\delta$ would, since $v_i$ is proportional to $e_i$. The steady state responds to the change of $v_i$ only, whatever its cause, so $\mathrm{d}\ln Y = C^Y_i\varepsilon^{v_i}_X\delta$. Several effects add to first order. $\square$

**Example 14.5.3** Let a competitive inhibitor of enzyme 4 act as $v_4 \propto 1/(1 + I/K_I)$ with $K_I = 0.5$; at $I = 0.25$ its elasticity is $\varepsilon^{v_4}_I = -I/(K_I + I) = -1/3$. Recomputing the control coefficients at the inhibited steady state gives $C^{J_P}_4 = -0.19$ and $C^{J_Q}_4 = 0.75$, so the theorem predicts $R^{J_P}_I = 0.0625$ and $R^{J_Q}_I = -0.25$; finite differences of the steady-state fluxes give the same values. The theorem divides a drug's effect into a property of the drug (how strongly it inhibits its target) and a property of the network (how much the target controls the output): a potent inhibitor of an enzyme with little control has little effect on the flux ([7.1.17](/7.1.17#sec-17.4.4)).

## 14.6. Parameter Estimation

### 14.6.1. The Figure of Merit

The inverse problem has six steps: choose a model (an empirical trend function or, better, a mechanistic one whose parameters mean something); define a figure of merit that measures the disagreement between model and data; minimize it over the parameters; examine the goodness of fit and the residuals; ask whether a much better fit exists (a lower minimum, or a better model); and determine how precisely the parameters are known. The first four are treated here, the last two in 14.6.4 and 14.7.

**Formula 14.6.1 ($\chi^2$ Figure of Merit)** Let the observations be $y_k$ at times or conditions $t_k$ ($k = 1, \dots, n$), let the model predict $\hat y_k(\boldsymbol{\theta})$ (for a kinetic model, an observable function of the solution of Eq. (14.1) with parameters $\boldsymbol{\theta}$), and let the errors be independent and normal with standard deviations $\sigma_k$. The negative log-likelihood is, up to a constant, $\tfrac12\chi^2(\boldsymbol{\theta})$ with
$$
\chi^2(\boldsymbol{\theta}) = \sum_{k=1}^n\frac{\bigl(y_k - \hat y_k(\boldsymbol{\theta})\bigr)^2}{\sigma_k^2},
$$
so the **maximum likelihood estimation** of $\boldsymbol{\theta}$ is weighted **least squares** with weights $1/\sigma_k^2$ ([Theorem 11.1.1](/7.7.11#thm-11.1.1)); with equal $\sigma_k$ it is ordinary least squares. At the minimum, $\chi^2$ follows approximately a **chi-square distribution** with $n - q$ degrees of freedom if the model is correct and the $\sigma_k$ are right, which tests the goodness of fit ([7.7.11](/7.7.11#sec-11.2.2)).

Other error models give other figures of merit: multiplicative errors, common for concentrations and fluorescence, give least squares on logarithms; counts give Poisson likelihoods; outliers call for robust losses. A high $R^2$ is not evidence of a good fit: a model that deviates systematically from the data can have $R^2 > 0.99$. Residuals plotted against time or condition should scatter around zero without trends; runs of residuals of the same sign show a missing mechanism (Example 14.7.5).

Two features distinguish fitting a kinetic model from ordinary **nonlinear regression**. Every evaluation of $\hat y(\boldsymbol{\theta})$ requires the numerical solution of an initial value problem, whose error must be small compared with the measurement error and whose solver must not fail for the parameter values the optimizer tries (stiffness changes with the parameters). And rate constants are positive and vary over orders of magnitude, so parameters are best estimated as logarithms, $\boldsymbol{\theta} = \ln\boldsymbol{p}$, which enforces positivity and makes relative precisions comparable.

### 14.6.2. Linearization and Progress Curves

Before computers, nonlinear models were linearized: the Michaelis–Menten equation becomes linear in the double-reciprocal **Lineweaver–Burk plot**, $1/v = (K_{\mathrm{M}}/V_{\max})(1/[S]) + 1/V_{\max}$. Linearization distorts the error structure (the reciprocal of a small, noisy rate has a huge error) and gives biased, inefficient estimates; nonlinear least squares on the original scale is the method of choice ([7.7.11](/7.7.11#sec-11.4.2) shows this on the Puromycin data). Kinetic models offer a further step: instead of initial rates, each of which uses only the beginning of a reaction, fit the whole time course.

**Formula 14.6.2 (Integrated Michaelis–Menten Equation)** The solution of $\mathrm{d}[S]/\mathrm{d}t = -V_{\max}[S]/(K_{\mathrm{M}} + [S])$ with $[S](0) = S_0$ satisfies $K_{\mathrm{M}}\ln(S_0/[S]) + S_0 - [S] = V_{\max}t$, and explicitly
$$
[S](t) = K_{\mathrm{M}}\,W\!\left(\frac{S_0}{K_{\mathrm{M}}}\exp\frac{S_0 - V_{\max}t}{K_{\mathrm{M}}}\right),
$$
where $W$ is the Lambert function, the inverse of $w \mapsto w\mathrm{e}^w$ (`scipy.special.lambertw`).

**Proof** Separating variables, $(K_{\mathrm{M}}/[S] + 1)\,\mathrm{d}[S] = -V_{\max}\,\mathrm{d}t$, and integrating from $0$ to $t$ gives the implicit form. Writing $w = [S]/K_{\mathrm{M}}$, it becomes $w\mathrm{e}^w = (S_0/K_{\mathrm{M}})\mathrm{e}^{(S_0 - V_{\max}t)/K_{\mathrm{M}}}$, and $W$ inverts it. $\square$

A single progress curve that runs from saturating substrate to well below $K_{\mathrm{M}}$ contains the whole rate law, $v$ against $[S]$, in one experiment. Whether it determines the parameters depends on the design, as the next section shows.

### 14.6.3. Computing the Fit

The minimization uses the Gauss–Newton idea: linearize the residuals $\boldsymbol{r}(\boldsymbol{\theta}) = (y_k - \hat y_k(\boldsymbol{\theta}))/\sigma_k$ around the current estimate, $\boldsymbol{r}(\boldsymbol{\theta} + \boldsymbol{\delta}) \approx \boldsymbol{r} - J_{\boldsymbol{r}}\boldsymbol{\delta}$, and solve the linear least-squares problem for $\boldsymbol{\delta}$; the **Levenberg–Marquardt method** adds a damping term $\lambda\operatorname{diag}(J_{\boldsymbol{r}}^{\mathsf T}J_{\boldsymbol{r}})$ that turns the step into a short gradient step when the linearization is poor ([3.5.5](/3.5.5#sec-5.1.5), [Algorithm 11.4.1](/7.7.11#alg-11.4.1)). For a kinetic model the Jacobian of the residuals is the matrix of output sensitivities: $J_{\boldsymbol{r}}$ has entries $(\partial\hat y_k/\partial\theta_j)/\sigma_k$, which are obtained from the sensitivity equations (14.6). Three ways to compute them, by increasing efficiency for many parameters:

| Method | Cost per gradient | Accuracy | Use |
|---|---|---|---|
| finite differences | $q + 1$ solutions | limited by the solver tolerance | small models, quick checks |
| forward sensitivities, Eq. (14.6) | one extended system of $m(q + 1)$ equations | as accurate as the solver | the default for tens of parameters |
| adjoint method | one forward and one backward solution of $m$ equations | as accurate as the solver | many parameters, a scalar objective (gradient-based optimizers) |

Automatic differentiation through the solver, as in the Julia and JAX ecosystems, computes either form without deriving the equations by hand.

### 14.6.4. Local Minima and Multistart

Nonlinear least-squares problems can have several local minima, and an iterative method converges to the minimum of the basin in which it starts. The error surface of a model with oscillations, time delays or several modes is often bumpy, and the minimum found depends on the starting values.

![Local minima in fitting an oscillation (simulation: 41 measurements over four periods of y = 2 + sin(2πt + 0.5) plus Gaussian noise of standard deviation 0.2; the model y = c + a sin ωt + b cos ωt is linear in c, a, b and nonlinear in the angular frequency ω). A: the data, the best fit (ω = 6.29) and the fit reached by Levenberg–Marquardt from the start ω = 4, a local minimum that misses the oscillation. B: the residual sum of squares minimized over c, a, b for each ω: one deep minimum near 2π and six shallow ones. Below, the frequencies reached from 200 starting values of ω drawn uniformly between 0.5 and 15: each run ends in the minimum of its own basin (13 drift toward ω = 0 and 10 beyond 15), and 19.5 % reach the best one](./plots/multistart.py)

**Example 14.6.1** In the figure the best fit has residual sum of squares $1.04$ (the expected value for the noise is $41 \times 0.04 = 1.64$, minus the fitted parameters), the local minimum near $\omega = 4.00$ has $19.8$, close to the value $20$ of a constant model: it fits a slow, weak wave and explains almost nothing. Of $200$ Levenberg–Marquardt runs from random starting frequencies, $39$ ($19.5\,\%$) find the best minimum.

Two remedies are standard. Multistart: run a local optimizer from many starting points spread over the plausible region (uniformly on logarithmic scales for rate constants, or on a Latin hypercube) and keep the best result; if the best value is found repeatedly from different starts, it is probably the global minimum, and if the best few minima have nearly equal $\chi^2$ but different parameters, the data do not distinguish them. Global optimizers (differential evolution, scatter search, **simulated annealing**) explore the space more systematically and are usually followed by a local refinement; benchmarks on published models of signaling and metabolic networks have found multistart of a gradient-based local optimizer with sensitivities (Raue and colleagues, 2013) and hybrids of a global search with local refinement (Villaverde and colleagues, 2019) to be the most efficient strategies. Where the model is linear in some parameters, as $c$, $a$, $b$ here, they can be eliminated by linear least squares for each value of the others, which leaves a low-dimensional search (the profile in panel B). Bounds on parameters enforce physical sense, but an estimate that ends on a bound is a warning that the model or the data are inadequate, not a result.

## 14.7. Uncertainty, Identifiability and Model Selection

### 14.7.1. Identifiability

A fit returns numbers; the question is which of them the data determine.

**Definition 14.7.1 (Identifiability)** A parameter $\theta_j$ of a model is *structurally identifiable* from a given experiment if, for noise-free data from that experiment, the observations determine its value uniquely (globally, or locally in a neighborhood); otherwise distinct parameter values produce identical observations. A structurally identifiable parameter is *practically identifiable* from a given data set if its **confidence interval** at the usual levels is finite. **Identifiability** in the first sense is a property of the model and the experimental design, in the second also of the amount and quality of the data.

**Example 14.7.1** A gene is induced at $t = 0$, $\dot x = ku - \gamma x$ with $u = 1$ and $x(0) = 0$, and is measured by fluorescence $y = sx$ with an unknown scale $s$. Then $y(t) = (sk/\gamma)(1 - \mathrm{e}^{-\gamma t})$: the data determine $\gamma$ and the product $sk$, but not $s$ and $k$ separately. Any $(s, k)$ with the same product fits equally well. The remedy is either to fix the scale by calibration or to reparametrize the model in identifiable combinations.

**Example 14.7.2** An enzyme subject to competitive inhibition by its product follows $\mathrm{d}[S]/\mathrm{d}t = -V_{\max}[S]/\bigl(K_{\mathrm{M}}(1 + [P]/K_{\mathrm{p}}) + [S]\bigr)$. In a single progress curve $[P] = S_0 - [S]$, so the denominator is $a + b[S]$ with $a = K_{\mathrm{M}}(1 + S_0/K_{\mathrm{p}})$ and $b = 1 - K_{\mathrm{M}}/K_{\mathrm{p}}$, and the curve is exactly a Michaelis–Menten progress curve with apparent constants $K' = a/b$ and $V' = V_{\max}/b$. Three parameters enter through two combinations: from one progress curve, product inhibition is structurally indistinguishable from a larger $K_{\mathrm{M}}$. With $K_{\mathrm{M}} = 10$, $V_{\max} = 1$, $K_{\mathrm{p}} = 20$ and $S_0 = 50$, $K' = 70$ and $V' = 2$; a simulated curve with noise ($\sigma = 0.5$, $15$ points) is fitted by plain Michaelis–Menten with $K' = 94$, $V' = 2.47$, and by the product-inhibition model with the same $\chi^2$ to eight digits; the third singular value of the Jacobian of the residuals is $7 \times 10^{-7}$ against $147$ and $13.7$ for the first two. Progress curves started at several $S_0$, in which $[P]$ and $[S]$ vary independently, make all three parameters identifiable (Example 14.7.5).

Structural identifiability can be checked symbolically, by differential algebra or by Taylor-series expansion of the outputs (tools such as SIAN or StructuralIdentifiability.jl), or numerically, by the rank of the sensitivity matrix at random parameter values: a zero singular value, as in Example 14.7.2, reveals a combination of parameters that does not change the outputs.

### 14.7.2. Fisher Information and Its Spectrum

Near the optimum, the figure of merit is approximately quadratic, $\chi^2(\hat{\boldsymbol{\theta}} + \boldsymbol{\delta}) \approx \chi^2(\hat{\boldsymbol{\theta}}) + \boldsymbol{\delta}^{\mathsf T}F\boldsymbol{\delta}$, with $F = J_{\boldsymbol{r}}^{\mathsf T}J_{\boldsymbol{r}}$ the **Fisher information matrix** of the experiment for Gaussian errors. Its inverse approximates the covariance of the estimates (the **Cramér–Rao inequality**, [3.2.3](/3.2.3#sec-3.4.5)), and Wald intervals are $\hat\theta_j \pm 1.96\sqrt{(F^{-1})_{jj}}$. The eigenvectors of $F$ are the parameter combinations the data determine independently, and its eigenvalues measure how well; a ratio of extreme eigenvalues (the **condition number** of $F$) of many orders of magnitude means that some combinations are nearly undetermined. Models of biochemical networks typically have eigenvalues spread evenly over many decades, the property called sloppiness ([7.6.40](/7.6.40#sec-40.1.3)): a few stiff combinations are fixed by the data and most are not.

![Identifiability of K_M and V_max from enzyme progress curves (simulation: K_M = 10, V_max = 1; 15 measurements of the product with Gaussian error of standard deviation 2 % of S₀; model: Formula 14.6.2). Low design: S₀ = 2 (0.2 K_M), times 2 to 60; high design: S₀ = 50 (5 K_M), times 6 to 90. A: data and fitted curves. B: profile likelihood of K_M with the 95 % threshold 3.84; the profile of the low design stays below the threshold for all large K_M, so K_M has no upper confidence limit, while the high design gives a closed interval. C: estimates from 300 parametric bootstrap data sets of each design (logarithmic axes); for the low design they spread along the line V_max/K_M = 0.1 (dashed), the combination the data determine; star: true values](./plots/progress_curve.py)

**Example 14.7.3** In the figure both designs are fitted in logarithmic parameters. For the low design ($S_0 = 0.2K_{\mathrm{M}}$) the estimates are $K_{\mathrm{M}} = 15.1$ and $V_{\max} = 1.47$, the correlation of $\ln\hat K_{\mathrm{M}}$ and $\ln\hat V_{\max}$ is $0.9998$, and the eigenvalues of $F$ are $0.30$ and $3211$, a condition number of $1.1 \times 10^4$; the Wald interval for $K_{\mathrm{M}}$ is $1.1$ to $205$. For the high design ($S_0 = 5K_{\mathrm{M}}$): $K_{\mathrm{M}} = 13.3$, $V_{\max} = 1.07$, correlation $0.983$, eigenvalues $20$ and $6555$ (condition number $328$), Wald interval $8.8$ to $20.1$. At low substrate the rate is $v \approx (V_{\max}/K_{\mathrm{M}})[S]$, a first-order decay that determines only the ratio: the eigenvector of the small eigenvalue points along $\ln V_{\max} - \ln K_{\mathrm{M}} = \text{constant}$, and the ratio itself is well determined (bootstrap interval $0.088$ to $0.116$, true $0.1$).

### 14.7.3. Profile Likelihood

The quadratic approximation fails exactly where it matters: for poorly determined parameters the likelihood is far from quadratic, and Wald intervals can be wildly wrong (they are symmetric on the log scale by construction). The **profile likelihood** ([3.5.4](/3.5.4#sec-4.1.3)) avoids the approximation: fix one parameter at each value of a grid, re-optimize all others, and record the best $\chi^2$.

**Formula 14.7.1 (Profile-Likelihood Confidence Interval)** With $\chi^2_{\mathrm{PL}}(\theta_j) = \min_{\boldsymbol{\theta}_{-j}}\chi^2(\theta_j, \boldsymbol{\theta}_{-j})$, the set
$$
\bigl\{\theta_j : \chi^2_{\mathrm{PL}}(\theta_j) - \chi^2(\hat{\boldsymbol{\theta}}) \le \chi^2_{1, 0.05}\bigr\}, \qquad \chi^2_{1, 0.05} = 3.84,
$$
is an approximate $95\,\%$ confidence interval for $\theta_j$, by the asymptotic distribution of the **likelihood ratio test** statistic. A parameter is practically non-identifiable if its profile does not exceed the threshold on one or both sides; it is structurally non-identifiable if the profile is flat.

**Example 14.7.4 (continued)** In panel B of the figure, the profile of $K_{\mathrm{M}}$ for the high design crosses $3.84$ at $8.9$ and $19.8$, a closed interval around the true value $10$, close to the Wald interval. For the low design it crosses at $3.6$ on the left but rises only to $0.55$ as $K_{\mathrm{M}} \to \infty$: no upper limit exists, because for $K_{\mathrm{M}} \gg S_0$ every progress curve is the same exponential decay. The Wald interval, $1.1$ to $205$, misrepresents both sides. The parametric bootstrap (panel C) agrees with the profile: $26\,\%$ of the low-design estimates of $K_{\mathrm{M}}$ exceed $100$, some by many orders of magnitude.

Profiles have a second use: following the other parameters along the profile of a non-identifiable one shows the functional relation between them (here $V_{\max}/K_{\mathrm{M}}$ constant), which suggests a reparametrization or the experiment that would break it. Profiles of predictions, computed in the same way for a model output instead of a parameter, show whether a prediction is determined even if the parameters are not: in a sloppy model, predictions that depend on the stiff combinations are often precise.

### 14.7.4. Monte Carlo and Bootstrap

The true parameters are unknown, the data are one realization of the experiment, and other realizations would have given other estimates. The distribution of those estimates is what an interval should describe.

- *Monte Carlo (parametric bootstrap).* Assume that the fitted parameters are close to the true ones and that the error model is right; simulate many synthetic data sets from the fitted model with the estimated noise, at the same times as the real data; fit each; the spread of the estimates around the fitted values estimates the spread of the original estimate around the truth (the **parametric bootstrap**, [3.5.7](/3.5.7#sec-7.4)). If $\sigma$ is not known, it is estimated by $\chi^2$ with unit weights divided by $n - q$.
- *Nonparametric bootstrap.* If the error distribution is unknown, resample the data themselves. Resampling time points with replacement is the classical recipe; for time courses, in which neighboring points are not exchangeable, resampling the residuals (adding resampled residuals to the fitted curve) or resampling whole replicate experiments respects the design better.

Both cost a full fit per replicate, and both inherit the multistart problem: each replicate must be fitted carefully, or the spread reflects optimizer failures.

### 14.7.5. Model Selection

A model with more parameters fits at least as well; the question is whether it fits significantly better. For nested models fitted to the same data, the extra-sum-of-squares **F-test** ([Formula 11.6.1](/7.7.11#fml-11.6.1)) compares
$$
F = \frac{(\chi^2_{\mathrm{simple}} - \chi^2_{\mathrm{complex}})/(q_{\mathrm{complex}} - q_{\mathrm{simple}})}{\chi^2_{\mathrm{complex}}/(n - q_{\mathrm{complex}})}
$$
with the $F$ distribution; when $\sigma$ is known, the likelihood ratio statistic $\chi^2_{\mathrm{simple}} - \chi^2_{\mathrm{complex}}$ is compared with $\chi^2$ with $q_{\mathrm{complex}} - q_{\mathrm{simple}}$ degrees of freedom. The mean squared error $\chi^2/(n - q)$ also helps: if it increases while $\chi^2$ decreases, the extra parameters are not earning their keep. For non-nested models the **Akaike information criterion** $\mathrm{AIC} = n\ln(\mathrm{RSS}/n) + 2q$ (for estimated $\sigma$) or the **Bayesian information criterion** trade fit against complexity ([7.7.11](/7.7.11#sec-11.8)).

**Example 14.7.5** Three progress curves with $S_0 = 10$, $25$ and $50$ ($15$ points each, $\sigma = 0.5$) are simulated from the product-inhibition model of Example 14.7.2 and fitted by both models. Michaelis–Menten ($K_{\mathrm{M}} = 17.5$, $V_{\max} = 0.96$) gives $\chi^2 = 259.3$; the product-inhibition model ($K_{\mathrm{M}} = 10.2$, $V_{\max} = 1.03$, $K_{\mathrm{p}} = 17.3$) gives $\chi^2 = 33.6$ on $42$ degrees of freedom, an adequate fit. $F = 282$ on $1$ and $42$ degrees of freedom, $p = 3 \times 10^{-20}$; AIC is $20.4$ for Michaelis–Menten and $-69.5$ for product inhibition. The residuals of the Michaelis–Menten fit show the missing mechanism without any test: for $S_0 = 50$ they are negative for the first seven points and positive for the last seven.

### 14.7.6. Validation

A model that fits is a hypothesis; it becomes useful when it predicts what it was not fitted to.

1. Physical sense: rate constants positive, affinities and concentrations in plausible ranges, parameters not stuck on their bounds.
2. Independent measurements: compare fitted values with values measured directly (a $K_{\mathrm{M}}$ from purified enzyme, a degradation rate from a chase experiment) or with limiting behavior known in advance.
3. Perturbation: alter a parameter experimentally (overexpress an enzyme, add an inhibitor, change the input) and check that the model, refitted or not, predicts the new data and that the right parameter changes.
4. Contrast between populations: a model of a disease state should place the difference in the parameters where the pathology is thought to lie (higher airway resistance in asthma, lower insulin sensitivity in diabetes).
5. Cross-validation by condition: fit to some conditions (inputs, doses, mutants) and predict the others; prediction of left-out conditions, not of left-out time points of the same experiment, tests the mechanism (**cross-validation**, [7.7.21](/7.7.21)).

## 14.8. A Complete Fit in Python

The following code carries out the analysis of Examples 14.7.2 and 14.7.5: simulation of the model with `solve_ivp`, a multistart trust-region fit within bounds in logarithmic parameters (unbounded Levenberg–Marquardt from poor starts can wander to absurd rate constants, where every solve becomes slow), Fisher information and Wald intervals, the profile likelihood of $K_{\mathrm{p}}$ and a parametric bootstrap.

```python
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares
from scipy import stats

# Model: Michaelis-Menten enzyme with competitive product inhibition, three progress curves
S0s = [10.0, 25.0, 50.0]
t_obs = np.linspace(6, 90, 15)
sigma = 0.5                                     # known measurement error (same units as P)

def rhs(t, s, KM, Vmax, Kp, S0):
    S = s[0]
    return [-Vmax * S / (KM * (1 + (S0 - S) / Kp) + S)]

def predict(logp, S0, t=t_obs):
    KM, Vmax, Kp = np.exp(logp)                 # log parameters keep rates positive
    sol = solve_ivp(rhs, (0, t[-1]), [S0], t_eval=t, args=(KM, Vmax, Kp, S0),
                    method="LSODA", rtol=1e-6, atol=1e-9)
    return S0 - sol.y[0]                        # product P(t)

def residuals(logp, data):
    return np.concatenate([(predict(logp, S0) - y) / sigma for S0, y in zip(S0s, data)])

rng = np.random.default_rng(1)
true = np.log([10.0, 1.0, 20.0])
data = [predict(true, S0) + rng.normal(0, sigma, t_obs.size) for S0 in S0s]

# 1. multistart trust-region fits within bounds (rate constants between 1e-3 and 1e3)
lo, hi = np.log(1e-3), np.log(1e3)
starts = rng.uniform(np.log(0.1), np.log(100), size=(10, 3))
fits = [least_squares(residuals, x0, args=(data,), bounds=(lo, hi)) for x0 in starts]
best = min(fits, key=lambda f: f.cost)
chi2 = 2 * best.cost
print("estimates", np.exp(best.x), "chi2", chi2, "dof", 3 * t_obs.size - 3)

# 2. Fisher information and Wald intervals (on the log scale)
J = best.jac                                    # sensitivities of the scaled residuals
cov = np.linalg.inv(J.T @ J)
print("FIM eigenvalues", np.linalg.eigvalsh(J.T @ J))
se = np.sqrt(np.diag(cov))
print("Wald 95% CI", np.exp(best.x - 1.96 * se), np.exp(best.x + 1.96 * se))

# 3. profile likelihood of Kp
def profile(logKp):
    f = least_squares(lambda q: residuals([q[0], q[1], logKp], data), best.x[:2], method="lm")
    return 2 * f.cost - chi2
grid = best.x[2] + np.linspace(-1.5, 1.5, 31)
prof = np.array([profile(g) for g in grid])
inside = np.exp(grid[prof <= stats.chi2.ppf(0.95, 1)])
print("profile 95% CI for Kp", inside.min(), inside.max())

# 4. parametric bootstrap
boot = []
for b in range(100):
    yb = [predict(best.x, S0) + rng.normal(0, sigma, t_obs.size) for S0 in S0s]
    boot.append(least_squares(residuals, best.x, args=(yb,), method="lm").x)
print("bootstrap 95% CI", np.exp(np.percentile(boot, [2.5, 97.5], axis=0)))
```

Run as shown, it gives $K_{\mathrm{M}} = 10.16$, $V_{\max} = 1.030$ and $K_{\mathrm{p}} = 17.35$ with $\chi^2 = 33.6$ on $42$ degrees of freedom; Fisher-information eigenvalues $35$, $261$ and $26\,421$ (condition number $755$: all three parameters determined, but not equally well); Wald intervals $8.3$ to $12.5$ for $K_{\mathrm{M}}$, $0.97$ to $1.09$ for $V_{\max}$ and $13.1$ to $23.0$ for $K_{\mathrm{p}}$; a profile-likelihood interval of $14.2$ to $21.2$ for $K_{\mathrm{p}}$ (on a grid of step $0.1$ in $\ln K_{\mathrm{p}}$); and parametric bootstrap intervals of $8.2$ to $12.3$, $0.98$ to $1.10$ and $13.5$ to $22.2$. The true values $10$, $1$ and $20$ lie inside all of them. With three curves at different $S_0$ the parameters that were confounded in a single curve (Example 14.7.2) are separated, and the three kinds of interval nearly agree because the likelihood is close to quadratic; for sloppy parameters they would not (Example 14.7.4).

## Summary

| Step | Key object | Formula or rule | Pitfall | Section |
|---|---|---|---|---|
| Write the model | stoichiometric matrix, rate laws | $\dot{\boldsymbol{x}} = N\boldsymbol{v}(\boldsymbol{x}, \boldsymbol{p})$, Eq. (14.1) | ambiguous diagrams; unit errors | 14.2.1, 14.2.4 |
| Reduce it | conserved moieties, quasi-steady states | $\boldsymbol{\ell}N = \boldsymbol{0}$ (Theorem 14.2.1); $E_{\mathrm{T}}/(S_0 + K_{\mathrm{M}}) \ll 1$ (Formula 14.2.1) | standard QSSA fails when enzyme and substrate are comparable | 14.2.2, 14.2.3 |
| Solve it | Euler, Runge–Kutta, implicit methods | orders 1 and 4 (Theorem 14.3.1); Euler stable for $h < 2/\lambda$ | drifting first integrals; stiffness | 14.3 |
| Analyze it | Jacobian, nullclines, bifurcations | trace and determinant; Hopf at $\operatorname{tr}J = 0$ (Example 14.4.2) | transients near bifurcations | 14.4 |
| Ask what matters | sensitivities, control coefficients | Eq. (14.6), (14.7); $C^S = -(ND\varepsilon)^{-1}ND$, $C^J = I + \varepsilon C^S$ (Theorem 14.5.1); $R^Y_X = C^Y_i\varepsilon^{v_i}_X$ (Theorem 14.5.2) | local versus global sensitivity | 14.5 |
| Fit it | $\chi^2$, likelihood | Formula 14.6.1; Levenberg–Marquardt with sensitivities | local minima (multistart); linearization | 14.6 |
| Trust it? | identifiability, Fisher information, profiles, bootstrap | Definition 14.7.1; Formula 14.7.1 | Wald intervals for sloppy parameters | 14.7.1–14.7.4 |
| Choose and test it | F-test, AIC; validation | Example 14.7.5 | fitting is not validation | 14.7.5, 14.7.6 |

- Writing rate equations is mechanical once the scheme is mechanistic; conservation laws come from the left null space of $N$, and quasi-steady-state reductions need a time-scale separation that must be checked (Formula 14.2.1, Example 14.2.3).
- The Euler method has order $1$ and a stability limit; Runge–Kutta methods with adaptive steps are the default, implicit methods for stiff networks (Example 14.3.3: $65\,630$ against $463$ evaluations).
- The Bier model (Definition 14.4.1) oscillates through a supercritical Hopf bifurcation at $K_{\mathrm{m}} = 15.24$ (Example 14.4.2).
- In networks, control is shared and can be negative across branches (Example 14.5.2); the effect of a drug is its elasticity times the control coefficient of its target (Theorem 14.5.2).
- Fits determine combinations of parameters; whether single parameters are determined depends on the design (Examples 14.7.1–14.7.4), and the profile likelihood, not the curvature, is the reliable test.

## Questions

1. Write the stoichiometric matrix for the reversible phosphorylation cycle $X \to X_{\mathrm{p}}$ (kinase, rate $v_1$) and $X_{\mathrm{p}} \to X$ (phosphatase, rate $v_2$), and for its extension in which the kinase forms a complex $K + X \rightleftharpoons KX \to K + X_{\mathrm{p}}$. Find the conservation laws in each case.

   **Answer** Cycle with species $(X, X_{\mathrm{p}})$: $N = \begin{bmatrix} -1 & 1 \\ 1 & -1\end{bmatrix}$, rank $1$, one conservation law $(1, 1)$: $[X] + [X_{\mathrm{p}}] = X_{\mathrm{T}}$. Extended scheme with species $(K, X, KX, X_{\mathrm{p}})$ and reactions binding, unbinding, catalysis, dephosphorylation: $N = \begin{bmatrix} -1 & 1 & 1 & 0 \\ -1 & 1 & 0 & 1 \\ 1 & -1 & -1 & 0 \\ 0 & 0 & 1 & -1 \end{bmatrix}$, of rank $2$ (the third row is minus the first, and the sum of the second and fourth rows is minus the third). Two conservation laws: $(1, 0, 1, 0)$, total kinase $[K] + [KX]$; and $(0, 1, 1, 1)$, total substrate $[X] + [KX] + [X_{\mathrm{p}}]$. Two independent variables remain.

2. For $\dot x = -\lambda x$, show that the classical Runge–Kutta method multiplies $x$ by $R(z) = 1 + z + z^2/2 + z^3/6 + z^4/24$ per step, with $z = -h\lambda$, and find the largest stable step for $\lambda = 60$, the fast eigenvalue of Example 14.3.3. How many steps would be needed to reach $t = 1500$?

   **Answer** Substituting $f = -\lambda x$: $k_1 = zx/h$, $k_2 = z(1 + z/2)x/h$, $k_3 = z(1 + z/2 + z^2/4)x/h$, $k_4 = z(1 + z + z^2/2 + z^3/4)x/h$, and $x_{n+1} = x_n[1 + \tfrac16(z + 2z(1 + z/2) + 2z(1 + z/2 + z^2/4) + z(1 + z + z^2/2 + z^3/4))] = R(z)x_n$, the Taylor polynomial of $\mathrm{e}^z$. On the negative real axis $R(z)$ stays positive and $\lvert R(z)\rvert < 1$ exactly for $-2.785 < z < 0$ ($R(-2.785) = 1$). So $h < 2.785/60 = 0.046$, and $1500/0.046 \approx 32\,000$ steps, about $130\,000$ evaluations, the order of magnitude found for `RK45` (whose stability region is similar), although accuracy alone would allow steps of tens of time units after the transient.

3. In the Bier model (Eq. 14.5) with $V_{\mathrm{in}} = 0.36$, $k_1 = 0.02$, $k_{\mathrm{p}} = 6$, how does the critical $K_{\mathrm{m}}$ of the Hopf bifurcation change if the glucose supply is raised to $V_{\mathrm{in}} = 0.5$? Interpret.

   **Answer** $T^* = 2V_{\mathrm{in}}K_{\mathrm{m}}/(k_{\mathrm{p}} - 2V_{\mathrm{in}}) = K_{\mathrm{m}}/5$ for $V_{\mathrm{in}} = 0.5$, so $T^* + K_{\mathrm{m}} = 1.2K_{\mathrm{m}}$. The condition $(T^* + K_{\mathrm{m}})^2 = k_{\mathrm{p}}/k_1 = 300$ gives $K_{\mathrm{m}} = 17.32/1.2 = 14.43$, lower than $15.24$. Oscillations require $K_{\mathrm{m}} < 14.43$: with a higher supply, the steady-state ATP level is higher relative to $K_{\mathrm{m}}$, the ATPases are more saturated, and the autocatalytic term $k_{\mathrm{p}}T^*/(T^* + K_{\mathrm{m}})^2$ must overcome a larger damping $k_1T^*$; a smaller $K_{\mathrm{m}}$ is needed. The determinant stays positive, so the bifurcation is again of Hopf type.

4. Show that for a two-step pathway $X_0 \to S \to P$ Theorem 14.5.1 gives $C^J_1 = \varepsilon_2/(\varepsilon_2 - \varepsilon_1)$ and $C^J_2 = -\varepsilon_1/(\varepsilon_2 - \varepsilon_1)$, with $\varepsilon_i = \varepsilon^{v_i}_S$, and $C^S_1 = -C^S_2 = 1/(\varepsilon_2 - \varepsilon_1)$.

   **Answer** $N = \begin{bmatrix} 1 & -1\end{bmatrix}$, $D = J\,I$ (both fluxes equal $J$), $\varepsilon = (\varepsilon_1, \varepsilon_2)^{\mathsf T}$. Then $ND\varepsilon = J(\varepsilon_1 - \varepsilon_2)$ and $ND = J\begin{bmatrix} 1 & -1\end{bmatrix}$, so $C^S = -\begin{bmatrix} 1 & -1\end{bmatrix}/(\varepsilon_1 - \varepsilon_2) = \begin{bmatrix} 1 & -1\end{bmatrix}/(\varepsilon_2 - \varepsilon_1)$. $C^J = I + \varepsilon C^S$: $C^J_{11} = 1 + \varepsilon_1/(\varepsilon_2 - \varepsilon_1) = \varepsilon_2/(\varepsilon_2 - \varepsilon_1)$, $C^J_{12} = -\varepsilon_1/(\varepsilon_2 - \varepsilon_1)$; the second row is the same because the fluxes are equal. These are [Eq. (17.5)](/7.1.17#eq-17.5) of 7.1.17. Increasing enzyme 1 raises $S$ ($C^S_1 > 0$ since $\varepsilon_2 > 0 \ge \varepsilon_1$), increasing enzyme 2 lowers it, and both changes by the same factor leave $S$ unchanged.

5. A drug inhibits enzyme 4 of Example 14.5.2 noncompetitively, $v_4 \propto 1/(1 + I/K_I)$. Using the control coefficients at the reference state ($C^{J_P}_4 = -0.25$, $C^{J_Q}_4 = 0.68$), estimate the relative changes of $J_P$ and $J_Q$ for a small dose $I = 0.05K_I$. Why does the estimate become inaccurate at large doses?

   **Answer** $\varepsilon^{v_4}_I = -I/(K_I + I) = -0.05/1.05 = -0.048$. The dose reduces $v_4$ by the factor $1/1.05$, a change of $\ln v_4$ by $-\ln 1.05 = -0.049$ at fixed metabolites. By Theorem 14.5.2 the fluxes change by $C^{J}_4 \times (-0.049)$: $\ln J_P$ by $+0.012$ and $\ln J_Q$ by $-0.033$, that is, $J_P$ rises by about $1.2\,\%$ and $J_Q$ falls by about $3.3\,\%$. Response coefficients are derivatives; at large doses the control coefficients themselves change with the state (at $I = 0.25$, $C^{J_P}_4 = -0.19$ and $C^{J_Q}_4 = 0.75$, Example 14.5.3), so the response must be computed by solving for the new steady state or by integrating the response coefficient over the dose.

6. In the gene induction model $\dot x = \beta - \alpha x$, $x(0) = 0$, measured at times $t_k$ with constant error $\sigma$, compute the Fisher information matrix for $(\beta, \alpha)$ from a single measurement at time $t$, and show that one time point cannot identify both parameters while two time points can (when $\alpha t$ is not small).

   **Answer** With the sensitivities of Example 14.5.1, $\boldsymbol{g}(t) = (\partial x/\partial\beta, \partial x/\partial\alpha)$, one measurement gives $F = \boldsymbol{g}\boldsymbol{g}^{\mathsf T}/\sigma^2$, a rank-one matrix: one combination of parameters is determined, the other not (a single number cannot fix two parameters). Two times give $F = (\boldsymbol{g}_1\boldsymbol{g}_1^{\mathsf T} + \boldsymbol{g}_2\boldsymbol{g}_2^{\mathsf T})/\sigma^2$, of rank two if $\boldsymbol{g}_1$ and $\boldsymbol{g}_2$ are not parallel. The ratio $(\partial x/\partial\alpha)/(\partial x/\partial\beta) = -\beta/\alpha + \beta t\mathrm{e}^{-\alpha t}/(1 - \mathrm{e}^{-\alpha t})$ varies with $t$ (from $\approx -\beta t/2$ at small $t$ to $-\beta/\alpha$ at large $t$), so two distinct times give independent vectors; but if both times are early, the vectors are nearly parallel ($\boldsymbol{g} \approx (t, -\beta t^2/2)$ differs only in the small second component), $F$ is ill-conditioned, and $\alpha$ is practically non-identifiable, as in [Example 1.5.1](/7.9.1#ex-1.5.1). One measurement on the rise and one on the plateau is the efficient design.

7. Explain why the profile likelihood of $K_{\mathrm{M}}$ in the low design of Example 14.7.4 approaches a finite limit ($0.55$ above the minimum) as $K_{\mathrm{M}} \to \infty$ instead of rising. What experiment would make $K_{\mathrm{M}}$ identifiable with the least extra work?

   **Answer** For $K_{\mathrm{M}} \gg S_0$ the rate law becomes $v = (V_{\max}/K_{\mathrm{M}})[S]$ exactly in the limit, so the family of progress curves converges to the exponential decay $[S] = S_0\mathrm{e}^{-kt}$ with $k = V_{\max}/K_{\mathrm{M}}$; re-optimizing $V_{\max}$ for each $K_{\mathrm{M}}$ keeps $k$ at its best value, and $\chi^2$ tends to the value of the best first-order fit, which is only slightly worse ($0.55$) than the best Michaelis–Menten fit, a difference within noise. The data cannot exclude first-order kinetics. Making $K_{\mathrm{M}}$ identifiable requires substrate concentrations at or above $K_{\mathrm{M}}$, where saturation shows: a single additional progress curve with $S_0$ several times $K_{\mathrm{M}}$ (as in the high design, which gave $8.9$ to $19.8$) suffices.

8. In Example 14.7.5, compute the mean squared errors $\chi^2/(n - q)$ for the two models and interpret them, assuming the stated $\sigma = 0.5$ is correct. Then explain why the F-test would not have been possible with a single progress curve (Example 14.7.2).

   **Answer** Michaelis–Menten: $259.3/43 = 6.03$; product inhibition: $33.6/42 = 0.80$. With correct weights, a good model has a mean squared (weighted) error near $1$: the simple model's value of $6$ shows a lack of fit (its $\chi^2$ of $259$ on $43$ degrees of freedom has $p < 10^{-30}$), the complex model is consistent with the noise. With a single curve the two models give the same $\chi^2$ (to eight digits), because product inhibition and a larger $K_{\mathrm{M}}$ are structurally indistinguishable; $F = 0$ and the test has no power. The F-test can only compare models that make different predictions for the experiment performed; design must come before testing.

9. (Design problem) You want to estimate the rate constants of a three-kinase cascade (MAPKKK, MAPKK, MAPK, each with a kinase and a phosphatase step) from Western blots of the doubly phosphorylated MAPK at eight time points after stimulation. Outline the modeling workflow and the identifiability problems you expect, and propose additional measurements.

   **Answer** (i) Model: write the detailed scheme (single and double phosphorylations at each level, phosphatases, conservation of each kinase's total), with Michaelis–Menten or mass-action rate laws, and a stimulus input; roughly $15$ to $25$ parameters. (ii) Observation model: Western blots measure relative amounts with an unknown scale per blot and multiplicative error, so add scale factors and fit logarithms; this already makes the absolute concentrations and some rate constants structurally non-identifiable (Example 14.7.1). (iii) Fit by multistart Levenberg–Marquardt with sensitivities in log parameters; check the best minimum is found repeatedly. (iv) Identifiability: eight points of one output cannot determine twenty parameters; expect a sloppy Fisher spectrum and flat profiles for most rate constants; compute profiles to see which combinations are determined (time scales of activation and deactivation, overall gain). (v) Additional measurements: phosphorylation of the upstream kinases (each layer becomes observable), several stimulus doses (to expose saturation and ultrasensitivity), inhibitor perturbations and phosphatase inhibition (separating forward and backward rates), absolute quantification of total kinase levels (by targeted mass spectrometry, [7.9.9](/7.9.9)) to remove the scale problem, and denser early time points. (vi) Validate on a held-out condition (a new dose or inhibitor), and report predictions with profile-likelihood intervals rather than single parameter values.

10. A colleague fits a model to a time course and reports $R^2 = 0.995$. List three checks that you would ask for before accepting the fitted parameters.

    **Answer** (i) Residuals: plot them against time; runs of the same sign mean systematic misfit even at high $R^2$, and a $\chi^2$ with the known measurement error should be consistent with $n - q$ degrees of freedom. (ii) Identifiability and uncertainty: profile likelihoods (or a bootstrap with careful refitting) for each parameter; a high $R^2$ says nothing about whether the parameters are determined, and Wald standard errors can be misleading. (iii) Global optimality: multistart from widely spread initial values, showing that the reported minimum is the best found and whether other minima of similar $\chi^2$ with different parameters exist. Further: parameters not on bounds and physically plausible; comparison with a simpler model (F-test or AIC); and prediction of an independent condition.
