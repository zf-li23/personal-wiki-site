---
title: "SymPy: Symbolic Computation"
description: "Symbolic computation with SymPy: symbols and assumptions, exact numbers, expression trees, substitution and evaluation; simplification and rewriting; derivatives, integrals, limits, series and sums; algebraic equations with solve, solveset and nsolve; differential equations with dsolve; exact matrix computations; lambdify and code generation; expression swell and the division of labor between symbolic and numerical methods."
---

All previous chapters of this course computed with numbers: floating-point arrays in NumPy, numerical algorithms in SciPy. Symbolic computation manipulates the formulas themselves. Asked for the roots of $ax^2 + bx + c$, a numerical solver needs values of $a$, $b$, $c$ and returns two **floating-point numbers**; a symbolic system returns the formula $x = (-b \pm \sqrt{b^2 - 4ac})/(2a)$, valid for all coefficients, exact, and ready for further manipulation. This chapter introduces SymPy, the symbolic mathematics library of the scientific Python stack: how it represents expressions, how it simplifies, differentiates, integrates and solves them, and how its results are turned back into fast numerical code. The mathematics behind each operation (limits and series in [2.2](/2.2), differential equations in [2.4](/2.4), linear algebra in [2.1](/2.1)) is not repeated here; SymPy is a tool for doing that mathematics reliably, and for checking it. The last section is about the boundary between the two worlds: symbolic results grow quickly, are often slow to evaluate and are not automatically good numerical formulas, so in practice the two kinds of computation divide the work. The examples use SymPy 1.14 with Python 3.14.

## 8.1. Symbolic Computation

The difference between the two kinds of computation is best seen side by side. Numerically, a root of $3x^2 + 6x + 1$ is found by a bracketing method ([4.4.4](/4.4.4#sec-4.2.2)), once for each set of coefficients and each root:

```python
from scipy import optimize

f = lambda x, a, b, c: a * x ** 2 + b * x + c
print(optimize.brentq(f, -1, 10, args=(3, 6, 1)))   # -0.18350341907227513
print(optimize.brentq(f, -5, -1, args=(3, 6, 1)))   # -1.8164965809277258
```

Symbolically, the general equation is solved once:

```python
import sympy as sp

a, b, c, x = sp.symbols("a b c x")
roots = sp.solve(a * x ** 2 + b * x + c, x)
print(roots)
# [(-b - sqrt(-4*a*c + b**2))/(2*a), (-b + sqrt(-4*a*c + b**2))/(2*a)]
print([r.subs({a: 3, b: 6, c: 1}) for r in roots])   # [-1 - sqrt(6)/3, -1 + sqrt(6)/3]
```

The result is a formula in the parameters, and after substitution an exact number, $-1 + \sqrt 6/3$, not an approximation to 16 digits. A program that manipulates mathematical expressions in this way, exactly and following the rules of algebra and calculus, is a *computer algebra system* (CAS). The main systems are:

| System | Character |
|---|---|
| Mathematica (Wolfram Language) | the most complete general system; commercial; Wolfram Alpha is a free web front end |
| Maple | strong in calculus and differential equations; commercial |
| MATLAB Symbolic Math Toolbox | symbolic computation inside MATLAB; commercial |
| Maxima | descendant of Macsyma (1968), written in Lisp; free |
| SymPy | a Python library, pure Python, free (BSD license); used inside ordinary Python programs |
| SageMath | a free mathematics system in Python that combines SymPy, Maxima, PARI, GAP, FLINT and many others |

SymPy is less powerful than Mathematica or Maple for hard integrals and differential equations, but it is a library rather than a separate environment: its expressions are Python objects, so a derivation can be scripted, tested, combined with NumPy and SciPy, and converted to numerical code in the same program.

The recommended import is `import sympy as sp`. The form `from sympy import *` is common in tutorials but replaces the standard functions of the same name (`sp.sin` and `math.sin` behave differently), so in programs it is better avoided. Output is plain text by default. In Jupyter, `sp.init_printing()` displays expressions as typeset formulas; `sp.pprint(expr)` prints a two-dimensional text form in a terminal, and `sp.latex(expr)` returns the LaTeX source, ready for a report or a page like this one:

```python
print(sp.latex(roots[0]))   # \frac{- b - \sqrt{- 4 a c + b^{2}}}{2 a}
```

## 8.2. Symbols, Numbers and Expressions

### 8.2.1. Symbols and Assumptions

A Python variable and a SymPy symbol are different things. `x = sp.Symbol("x")` creates a symbol named `x` and binds it to the Python variable `x`; `sp.symbols("x y z")` (or `"x, y, z"`) creates several at once, and `sp.symbols("x0:5")` the symbols `x0`, ..., `x4`. The older function `sp.var` creates symbols and injects them into the global namespace as a side effect; explicit assignment is clearer.

Symbols carry *assumptions*: keyword arguments such as `real`, `positive`, `integer`, `nonnegative` or `finite` that tell SymPy what values the symbol stands for. Without assumptions a symbol is an arbitrary complex number, and many "obvious" simplifications are then false:

```python
x = sp.Symbol("x")
r = sp.Symbol("r", real=True)
p = sp.Symbol("p", positive=True)
n = sp.Symbol("n", integer=True)

print(sp.sqrt(x ** 2), sp.sqrt(r ** 2), sp.sqrt(p ** 2))   # sqrt(x**2) Abs(r) p
print(sp.cos(2 * sp.pi * n), sp.sin(sp.pi * n))             # 1 0
print((p + 1).is_positive, (r ** 2).is_nonnegative, (x ** 2).is_nonnegative)   # True True None
```

$\sqrt{x^2} = x$ fails for $x = -1$ and for $x = \mathrm{i}$, so SymPy leaves it alone unless the assumptions justify the simplification. The attributes `is_positive`, `is_real` and so on use three-valued logic: `True`, `False`, or `None` for "cannot be decided". `p.assumptions0` lists everything that follows from the declared assumptions (a positive symbol is also real, nonzero, finite, ...). Declaring the assumptions that hold in the problem is the single most effective way to obtain simpler results from `simplify`, `integrate` and `solve`.

### 8.2.2. Exact and Floating-Point Numbers

SymPy has its own number types: `sp.Integer` (arbitrary size), `sp.Rational(3, 7)`, `sp.Float("3.14", 30)` (arbitrary precision, via the library mpmath), and the constants `sp.pi`, `sp.E`, `sp.I` (the imaginary unit $\mathrm{i}$) and `sp.oo` ($\infty$). Integers and rationals are exact, and as long as a computation stays within them, so is the result. The trap is that Python evaluates its own arithmetic before SymPy sees it:

```python
print(1 / 3 * x, sp.Rational(1, 3) * x, sp.S(1) / 3 * x)   # 0.333333333333333*x x/3 x/3
print(sp.Float(0.1, 30), sp.Float("0.1", 30))
# 0.100000000000000005551115123126 0.100000000000000000000000000000
```

`1 / 3` is the Python float $0.333\dots$ before it meets `x`, and the float literal `0.1` already carries its binary rounding error ([3.5.1](/3.5.1#sec-1.2.4)), which a 30-digit `Float` faithfully preserves. Exact constants are written as `sp.Rational(1, 3)`, `sp.S(1) / 3` (`sp.S` converts a Python object to a SymPy one; `sp.S("1/3")` parses a string), or by putting a symbol first, as in `x / 3`. Conversely, `sp.nsimplify(0.333333333333)` guesses the exact number `1/3`, and `int()`, `float()` and `complex()` convert SymPy numbers back to Python numbers.

### 8.2.3. Expressions as Trees

A SymPy **expression** is a tree: each node is a function or operator (`Add`, `Mul`, `Pow`, `sin`, ...), its children are its arguments, and the leaves are symbols and numbers. `expr.func` is the head of the tree, `expr.args` the tuple of children, and `sp.srepr` shows the whole structure:

```python
e = x ** 2 + 2 * sp.sin(y)
print(e.func, e.args)    # <class 'sympy.core.add.Add'> (x**2, 2*sin(y))
print(sp.srepr(x ** 2 - 2 * x))
# Add(Pow(Symbol('x'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x')))
```

There is no subtraction node: $a - b$ is stored as `Add(a, Mul(-1, b))`, and $a/b$ as `Mul(a, Pow(b, -1))`. Knowing this explains several behaviors. Expressions are immutable: every operation returns a new tree. Arguments of `Add` and `Mul` are stored in a canonical order, so `x + y` and `y + x` are the same object, but otherwise SymPy performs only cheap automatic simplifications. In particular, `==` tests *structural* equality of trees, not mathematical equality:

```python
print((x + 1) ** 2 == x ** 2 + 2 * x + 1)                        # False
print(sp.expand((x + 1) ** 2) == x ** 2 + 2 * x + 1)             # True
print(sp.simplify((x + 1) ** 2 - (x ** 2 + 2 * x + 1)) == 0)     # True
```

To test whether two expressions are mathematically equal, simplify their difference (or call `a.equals(b)`, which also tries numerical evaluation at random points). An equation is written `sp.Eq(lhs, rhs)`, not with `==`.

Undefined functions are created with `f = sp.Function("f")`; `f(x)` is then an expression that can be differentiated (giving an unevaluated `Derivative(f(x), x)`) and used as the unknown of a differential equation. Anonymous functions are `sp.Lambda(x, x ** 3)`, which applied to `y + 1` gives `(y + 1)**3`. The mathematical functions (`sp.sin`, `sp.exp`, `sp.log`, `sp.gamma`, `sp.besselj`, ...) produce expression nodes, never floating-point results, unless their argument is a number for which an exact value is known (`sp.sin(sp.pi / 6)` is `1/2`).

### 8.2.4. Substitution and Numerical Evaluation

`expr.subs(old, new)` replaces a subexpression, and with a dictionary several at once. Substituting numbers evaluates the expression, exactly if the numbers are exact:

```python
e = x ** 3 + 7 * y + z ** 2 * x
print(e.subs({x: 1.3, y: 0.2, z: 5}))                                     # 36.0970000000000
print(e.subs({x: sp.Rational(13, 10), y: sp.Rational(1, 5), z: 5}))       # 36097/1000
print(sp.pi.evalf(30), sp.N(sp.sqrt(2), 50))
# 3.14159265358979323846264338328 1.4142135623730950488016887242096980785696718753769
```

`expr.evalf(n)`, or equivalently `sp.N(expr, n)`, evaluates to `n` significant digits with arbitrary-precision arithmetic, adapting the working precision internally so that the digits returned are correct. This makes SymPy a useful referee for floating-point code: §8.7.2 shows a limit whose value double precision cannot compute at all. For evaluating an expression at many points, `subs` and `evalf` are far too slow; `lambdify` (§8.7.1) converts the expression to a NumPy function.

## 8.3. Simplification and Rewriting

There is no single "simplest form" of an expression: $(x+1)^2$ and $x^2 + 2x + 1$ are each simpler for some purposes. `sp.simplify(expr)` tries a number of strategies and returns the shortest result by a complexity measure, which is convenient interactively but slow, unpredictable and sometimes disappointing. In programs, the functions that perform one specific transformation are better:

| Function | Transformation | Example |
|---|---|---|
| `expand` | multiply out products and powers | $(x+y)^3 \to x^3 + 3x^2y + 3xy^2 + y^3$ |
| `factor` | factor polynomials over the rationals | $x^3 - x^2 - x + 1 \to (x-1)^2(x+1)$ |
| `collect(expr, x)` | collect coefficients of powers of `x` | $xy + x + 2x^2 - x^2y - 3 \to x^2(2-y) + x(y+1) - 3$ |
| `cancel` | rational function in lowest terms $p/q$ | $\frac{x^2-1}{x^2+2x+1} \to \frac{x-1}{x+1}$ |
| `apart` | **partial fraction decomposition** | $\frac{4x^2+3}{x(x-1)^2} \to \frac{3}{x} + \frac{1}{x-1} + \frac{7}{(x-1)^2}$ |
| `together` | combine over a common denominator | $\frac1x + \frac1{x+1} \to \frac{2x+1}{x(x+1)}$ |
| `trigsimp` | trigonometric identities | $\sin^4 x - 2\sin^2 x\cos^2 x + \cos^4 x \to \frac{\cos 4x}{2} + \frac12$ |
| `expand_trig` | addition formulas | $\sin 2x \to 2\sin x\cos x$ |
| `powsimp` | combine powers | $x^y x^2 \to x^{y+2}$ |
| `expand_log`, `logcombine` | split or combine logarithms | $\log(pq^2) \leftrightarrow \log p + 2\log q$ |
| `gammasimp` | factorials, binomials, Gamma functions | $\frac{(x+1)!}{x!} \to x + 1$ |
| `radsimp` | rationalize denominators | $\frac{1}{1+\sqrt2} \to \sqrt2 - 1$ |
| `expr.rewrite(f)` | express in terms of another function | $\cos x \to \frac{\mathrm{e}^{\mathrm{i}x}}{2} + \frac{\mathrm{e}^{-\mathrm{i}x}}{2}$ |

`sp.fraction(expr)` returns numerator and denominator separately. Several of these transformations are valid only under assumptions, and SymPy applies them only when the assumptions hold. $\log x + \log y = \log(xy)$ is false for $x = y = -1$, and $x^a y^a = (xy)^a$ fails for similar reasons, so with plain symbols `logcombine` and `powsimp` do nothing, while with positive symbols they combine:

```python
p, q = sp.symbols("p q", positive=True)
print(sp.logcombine(sp.log(x) + sp.log(y)), sp.logcombine(sp.log(p) + sp.log(q)))   # log(x) + log(y) log(p*q)
print(sp.powsimp(x ** y * y ** y), sp.powsimp(p ** y * q ** y))                     # x**y*y**y (p*q)**y
```

The argument `force=True` makes these functions ignore the assumptions, which is acceptable only when the user knows that the result is correct for the values of interest.

## 8.4. Calculus

### 8.4.1. Derivatives

Differentiation is the easiest operation of calculus to automate: the rules of [2.2.4](/2.2.4) apply mechanically to every node of the expression tree. `expr.diff(x)` (or `sp.diff(expr, x)`) differentiates with respect to `x`; further arguments give higher and mixed derivatives:

```python
e = sp.exp(x * y) * sp.sin(x)
print(e.diff(x))          # y*exp(x*y)*sin(x) + exp(x*y)*cos(x)
print(sp.diff(x ** 10, x, 4))   # 5040*x**6, the fourth derivative
print(e.diff(x, 2, y))    # second derivative in x, then one in y
d = sp.Derivative(e, x)   # unevaluated; d.doit() computes it
```

Arguments such as `diff(x, x, y)` or `diff(x, 2, y)` are equivalent. The unevaluated `Derivative` (and similarly `Integral`, `Limit`, `Sum`) is useful for displaying a formula before computing it, and `.doit()` evaluates it. For vector-valued functions, `sp.Matrix(...).jacobian(vars)` gives the **Jacobian matrix** and `sp.hessian(f, vars)` the Hessian:

```python
F = sp.Matrix([x ** 2 * y, 5 * x + sp.sin(y)])
print(F.jacobian([x, y]))             # Matrix([[2*x*y, x**2], [5, cos(y)]])
print(sp.hessian(x ** 3 + x * y ** 2, (x, y)))   # Matrix([[6*x, 2*y], [2*y, 2*x]])
```

Since formulas are Python objects, a library of formulas is a set of ordinary Python functions that take and return expressions. A gradient in Cartesian coordinates, for instance, applies to an undefined function as well as to a concrete one:

```python
def gradient(f, coords):
    """Gradient of the scalar expression f in Cartesian coordinates."""
    return sp.Matrix([f.diff(c) for c in coords])


f = sp.Function("f")(x, y, z)
print(gradient(f, (x, y, z)).T)   # Matrix([[Derivative(f(x, y, z), x), ..., Derivative(f(x, y, z), z)]])
print(gradient(x * y * z, (x, y, z)).T)   # Matrix([[y*z, x*z, x*y]])
```

### 8.4.2. Integrals

Integration is harder: most elementary functions have no elementary **antiderivative**, and finding one when it exists is a real algorithmic problem. `sp.integrate(expr, x)` returns an antiderivative (without the constant of integration), `sp.integrate(expr, (x, a, b))` a definite integral, and several tuples a multiple integral, integrated from the first tuple to the last:

```python
print(sp.integrate(x ** 2 * sp.exp(x), x))                        # (x**2 - 2*x + 2)*exp(x)
print(sp.integrate(1 / (x ** 3 + 1), x))
# log(x + 1)/3 - log(x**2 - x + 1)/6 + sqrt(3)*atan(2*sqrt(3)*x/3 - sqrt(3)/3)/3
print(sp.integrate(sp.exp(-x ** 2), (x, -sp.oo, sp.oo)))          # sqrt(pi)
print(sp.integrate(sp.exp(-x ** 2), x))                           # sqrt(pi)*erf(x)/2
print(sp.integrate(sp.sin(x) / x, (x, 0, sp.oo)))                 # pi/2
print(sp.integrate(x * y, (y, 0, x), (x, 0, 1)))                  # 1/8
```

The results include the **Gaussian integral** $\int_{-\infty}^{\infty} \mathrm{e}^{-x^2}\,\mathrm{d}x = \sqrt\pi$, and an antiderivative of $\mathrm{e}^{-x^2}$ in terms of the **error function**, a special function that SymPy knows. The order of the tuples matters in the last line: `(y, 0, x)` is integrated first, so it computes $\int_0^1 \int_0^x xy\,\mathrm{d}y\,\mathrm{d}x$. SymPy combines table lookup and heuristics with a partial implementation of the *Risch algorithm*, a decision procedure that either finds an elementary antiderivative or proves that none exists, and with integration via Meijer G-functions for definite integrals.

Assumptions matter for improper integrals. $\int_0^\infty \mathrm{e}^{-ax}\,\mathrm{d}x$ converges only for $\operatorname{Re} a > 0$, so for a plain symbol `a` SymPy returns a `Piecewise` result with the condition `Abs(arg(a)) < pi/2`; for `a = sp.Symbol("a", positive=True)` it returns `1/a`. When no closed form is found, `integrate` returns the integral unevaluated, as an `Integral` object (or a `NonElementaryIntegral`, when the Risch algorithm has proved that no elementary antiderivative exists). Such an integral can still be evaluated numerically to any precision, most reliably by constructing it directly as an `Integral`:

```python
print(sp.integrate(x ** x, (x, 0, 1)))                # Integral(x**x, (x, 0, 1))
print(sp.Integral(x ** x, (x, 0, 1)).evalf(20))       # 0.78343051071213440706
```

For many such evaluations, `scipy.integrate.quad` applied to a lambdified integrand is much faster.

### 8.4.3. Limits, Series and Sums

`sp.limit(expr, x, x0)` computes limits with the Gruntz algorithm, which works with asymptotic expansions rather than with **L'Hôpital's rule**; the argument `dir="+"` (the default), `"-"` or `"+-"` selects one-sided or two-sided limits, and `x0` may be `sp.oo`:

```python
print(sp.limit(sp.sin(x) / x, x, 0), sp.limit((1 + 1 / x) ** x, x, sp.oo))   # 1 E
print(sp.limit(1 / x, x, 0), sp.limit(1 / x, x, 0, "-"))                     # oo -oo
```

A famous test, posed by V. I. Arnold, is

$$
\lim_{x \to 0} \frac{\sin \tan x - \tan \sin x}{\arcsin \arctan x - \arctan \arcsin x} = 1,
$$
which L'Hôpital's rule settles only after differentiating seven times. SymPy returns 1 in a fraction of a second, and `series` shows why:

```python
num = sp.sin(sp.tan(x)) - sp.tan(sp.sin(x))
den = sp.asin(sp.atan(x)) - sp.atan(sp.asin(x))
print(sp.limit(num / den, x, 0))      # 1
print(num.series(x, 0, 10))           # -x**7/30 - 29*x**9/756 + O(x**10)
print(den.series(x, 0, 10))           # -x**7/30 + 13*x**9/756 + O(x**10)
```

`expr.series(x, x0, n)` computes the **Taylor series** about `x0` up to, but not including, the term of order `n` (default `x0 = 0`, `n = 6`), with an order term `O(...)`; `.removeO()` drops it and leaves a **Taylor polynomial**:

```python
print(sp.exp(x).series(x, 0, 4))       # 1 + x + x**2/2 + x**3/6 + O(x**4)
t = sp.sin(x).series(x, sp.pi / 2, 5).removeO()   # 1 - (x - pi/2)**2/2 + (x - pi/2)**4/24
print(t.subs(x, 89 * sp.pi / 180).evalf())        # 0.999847695156430, sin 89° = 0.999847695156391
```

`sp.Sum(expr, (k, a, b))` and `sp.Product(expr, (k, a, b))` represent sums and products, evaluated by `.doit()`; `sp.summation` evaluates directly. SymPy knows many closed forms, including infinite series:

```python
k, n = sp.symbols("k n", integer=True, positive=True)
print(sp.Sum(1 / k ** 2, (k, 1, sp.oo)).doit())         # pi**2/6
print(sp.Sum(k ** 3, (k, 1, n)).doit().factor())        # n**2*(n + 1)**2/4
print(sp.Sum(1 / k ** 3, (k, 1, sp.oo)).doit())         # zeta(3)
print(sp.summation(x ** k / sp.factorial(k), (k, 0, sp.oo)))   # exp(x)
```

## 8.5. Equations

### 8.5.1. Algebraic Equations

SymPy has two main solvers. `sp.solve(f, x)` solves $f = 0$ (or an `Eq`) and returns a list of solutions; with `dict=True` it returns a list of dictionaries, the most robust format for systems. `sp.solveset(f, x, domain)` returns a mathematical set, which can express what a list cannot: infinitely many solutions, no solution in the domain, or "the solutions of this equation" when they are not found in closed form:

```python
print(sp.solve(x ** 2 - 4, x), sp.solve(x ** 2 - 4, x, dict=True))   # [-2, 2] [{x: -2}, {x: 2}]
print(sp.solve(sp.sin(x) - sp.Rational(1, 2), x))                     # [pi/6, 5*pi/6]
print(sp.solveset(sp.sin(x) - sp.Rational(1, 2), x, domain=sp.S.Reals))
# Union(ImageSet(Lambda(_n, 2*_n*pi + pi/6), Integers), ImageSet(Lambda(_n, 2*_n*pi + 5*pi/6), Integers))
print(sp.solveset(x ** 2 + 1, x), sp.solveset(x ** 2 + 1, x, sp.S.Reals))   # {-I, I} EmptySet
print(sp.solveset(sp.cos(x) - x, x, sp.S.Reals))     # ConditionSet(x, Eq(-x + cos(x), 0), Reals)
print(sp.solveset(x ** 2 - 3 * x + 2 < 0, x, sp.S.Reals))   # Interval.open(1, 2)
```

`solve` returned only the two solutions in $[0, 2\pi)$ of $\sin x = 1/2$; `solveset` returned all of them, $\pi/6 + 2k\pi$ and $5\pi/6 + 2k\pi$. The default domain of `solveset` is the complex numbers. For systems, `sp.linsolve` handles linear systems (including underdetermined ones, whose solution sets have free parameters) and `sp.nonlinsolve` polynomial and other nonlinear systems:

```python
print(sp.solve([x + y - 3, x - y - 1], [x, y]))              # {x: 2, y: 1}
print(sp.linsolve([x + y - 3, 2 * x + 2 * y - 6], [x, y]))  # {(3 - y, y)}
print(sp.nonlinsolve([x ** 2 + y ** 2 - 4, x - y], [x, y]))  # {(-sqrt(2), -sqrt(2)), (sqrt(2), sqrt(2))}
```

Many equations have no solution in closed form. Polynomial equations of degree five and higher are in general not solvable by radicals (the Abel–Ruffini theorem); SymPy then represents the roots exactly as `CRootOf` objects, which can be evaluated to any precision. Transcendental equations sometimes have solutions in terms of special functions, such as $x\mathrm{e}^x = 1$ with the Lambert W function, and usually have none. For these, `sp.nsolve(f, x, x0)` finds a root numerically from a starting point, in arbitrary precision, also for systems:

```python
print(sp.solve(x ** 5 - x + 1, x)[0], sp.CRootOf(x ** 5 - x + 1, 0).evalf())   # CRootOf(x**5 - x + 1, 0) -1.16730397826142
print(sp.solve(x * sp.exp(x) - 1, x))                       # [LambertW(1)]
print(sp.nsolve(sp.cos(x) - x, x, 1, prec=30))              # 0.739085133215160641655312087674
print(sp.nsolve([x ** 2 + y ** 2 - 4, sp.exp(x) + y - 1], [x, y], [1, -1]).T)
# Matrix([[1.00416873847466, -1.72963728702587]]), the root found by optimize.root in 4.4.4
```

### 8.5.2. Differential Equations

`sp.dsolve(eq, f(x))` solves ordinary differential equations symbolically. It classifies the equation (`sp.classify_ode(eq)` lists the methods that apply: separable, linear, exact, Bernoulli, constant coefficients, ...; the methods themselves are those of [2.4.3](/2.4.3) and [2.4.9](/2.4.9)) and returns an `Eq` with the general solution, with constants `C1`, `C2`, ... The argument `ics` imposes initial conditions. Newton's law of cooling, $T' = -k(T - T_{\mathrm{a}})$, $T(0) = T_0$:

```python
t = sp.symbols("t")
k, T0, Ta = sp.symbols("k T_0 T_a", positive=True)
T = sp.Function("T")
ode = sp.Eq(T(t).diff(t), -k * (T(t) - Ta))
print(sp.dsolve(ode))                          # Eq(T(t), C1*exp(-k*t) + T_a)
sol = sp.dsolve(ode, T(t), ics={T(0): T0})
print(sol)                                     # Eq(T(t), T_a + (T_0 - T_a)*exp(-k*t))
print(sp.checkodesol(ode, sol))                # (True, 0)
```

`checkodesol` substitutes the solution back into the equation, a useful check for any solution, whether found by SymPy or by hand. Initial conditions on derivatives are written with `subs`. A **damped oscillation** $q'' + \frac12 q' + q = 0$ and the **resonance** of an undamped oscillator driven at its natural frequency:

```python
q = sp.Function("q")
ics = {q(0): 1, q(t).diff(t).subs(t, 0): 0}
print(sp.dsolve(q(t).diff(t, 2) + q(t).diff(t) / 2 + q(t), ics=ics))
# Eq(q(t), (sqrt(15)*sin(sqrt(15)*t/4)/15 + cos(sqrt(15)*t/4))*exp(-t/4))
ics0 = {q(0): 0, q(t).diff(t).subs(t, 0): 0}
print(sp.dsolve(sp.Eq(q(t).diff(t, 2) + q(t), sp.cos(t)), ics=ics0))   # Eq(q(t), t*sin(t)/2)
```

Systems are passed as a list of equations, and the **logistic growth** equation, being a Bernoulli equation, is solved in closed form after a `simplify`:

```python
y1, y2 = sp.symbols("y1 y2", cls=sp.Function)
print(sp.dsolve([sp.Eq(y1(t).diff(t), y2(t)), sp.Eq(y2(t).diff(t), -y1(t))],
                ics={y1(0): 1, y2(0): 0}))     # [Eq(y1(t), cos(t)), Eq(y2(t), -sin(t))]

r, K, y0 = sp.symbols("r K y_0", positive=True)
P = sp.Function("P")
s = sp.dsolve(sp.Eq(P(t).diff(t), r * P(t) * (1 - P(t) / K)), ics={P(0): y0})
print(sp.simplify(s.rhs))                      # K*y_0*exp(r*t)/(K + y_0*exp(r*t) - y_0)
```

Most differential equations, however, have no closed-form solution, and for those `dsolve` raises `NotImplementedError` (for example for $y' = \sin y + t$) or returns an implicit or series solution (`hint="1st_power_series"`). Nonlinear models of any realistic size are solved numerically with `solve_ivp` ([4.4.4](/4.4.4#sec-4.3.2)), and SymPy can still help by deriving the right-hand side or its Jacobian (§8.7.1). Partial differential equations are solved symbolically only in simple cases (`sp.pdsolve` handles first-order linear ones); their numerical solution by finite differences is shown in [4.4.4](/4.4.4#sec-4.6.3).

## 8.6. Matrices

`sp.Matrix` is a two-dimensional matrix of SymPy expressions, created from nested lists, or from a shape and a function of the indices (`sp.Matrix(2, 2, lambda i, j: i**2 + j**2)`), or with `sp.eye`, `sp.zeros`, `sp.ones`, `sp.diag`. Products are written `A * B` or `A @ B`, powers `A ** k`, the transpose `A.T`. Since the entries are exact, the methods of [2.1](/2.1) give exact results, also for matrices with symbolic entries:

```python
a, b = sp.symbols("a b")
A = sp.Matrix([[a, b], [b, a]])
print(A.det(), A.inv())          # a**2 - b**2, Matrix([[a/(a**2 - b**2), -b/(a**2 - b**2)], ...])
print(A.eigenvals())             # {a - b: 1, a + b: 1}, eigenvalue: algebraic multiplicity
print(A.eigenvects())            # [(a - b, 1, [Matrix([[-1], [1]])]), (a + b, 1, [Matrix([[1], [1]])])]
print(A.charpoly().as_expr())    # a**2 - 2*a*lambda - b**2 + lambda**2
```

| Task | Method |
|---|---|
| **determinant**, **inverse matrix**, **rank** | `A.det()`, `A.inv()`, `A.rank()` |
| reduced row echelon form, null space, column space | `A.rref()`, `A.nullspace()`, `A.columnspace()` |
| solve $A\boldsymbol{x} = \boldsymbol{b}$ | `A.solve(b)`, `A.LUsolve(b)`, `sp.linsolve((A, b), vars)` |
| factorizations | `A.LUdecomposition()`, `A.QRdecomposition()`, `A.cholesky()` |
| **eigenvalues**, **eigenvectors**, **characteristic polynomial** | `A.eigenvals()`, `A.eigenvects()`, `A.charpoly()` |
| diagonalization, **Jordan canonical form** | `A.diagonalize()`, `A.jordan_form()` (returns $P$, $J$ with $A = PJP^{-1}$) |
| singular values, norms | `A.singular_values()`, `A.norm(ord)` |
| **matrix exponential**, other matrix functions | `A.exp()`, `A.analytic_func(f, x)` |

For a singular matrix the exact computation decides questions that floating-point arithmetic can only approximate: $\begin{bmatrix} 1&2&3\\4&5&6\\7&8&9 \end{bmatrix}$ has rank 2 and null space spanned by $(1, -2, 1)^{\mathsf T}$, with no tolerance involved (compare the numerical rank, decided with a tolerance on the singular values, in [2.1.3](/2.1.3) and `np.linalg.matrix_rank` in [4.4.3](/4.4.3)). The Jordan form of $\begin{bmatrix} 2&1\\-1&4 \end{bmatrix}$ is the single block $\begin{bmatrix} 3&1\\0&3 \end{bmatrix}$, which no floating-point eigenvalue routine can compute reliably, since an arbitrarily small perturbation splits the double eigenvalue. The matrix exponential of $tM$ with $M = \begin{bmatrix} 0&1\\-1&0 \end{bmatrix}$ comes out as the rotation matrix, which solves the system $\boldsymbol{y}' = M\boldsymbol{y}$ of §8.5.2 ([2.4.8](/2.4.8)):

```python
M = sp.Matrix([[0, 1], [-1, 0]])
print(sp.simplify((M * t).exp()))   # Matrix([[cos(t), sin(t)], [-sin(t), cos(t)]])
```

`sp.MatrixSymbol("X", 3, 3)` is a matrix that is itself a symbol, without entries: expressions such as `(X * Y).T` simplify by the rules of matrix algebra (to `Y.T*X.T`), which is useful for derivations with matrices of unspecified size. Matrices are mutable; `sp.ImmutableMatrix` is the variant that can be used as a dictionary key or inside other expressions.

## 8.7. From Symbolic to Numerical Computation

### 8.7.1. lambdify and Code Generation

A symbolic result is most often needed as a fast numerical function. `sp.lambdify(args, expr, modules)` translates an expression into Python source code that calls a numerical library and compiles it into a function; with the default modules it uses NumPy (and SciPy for special functions, when installed), so the function accepts arrays:

```python
import numpy as np

expr = sp.sin(x) * sp.exp(-y ** 2)
f = sp.lambdify((x, y), expr)
print(f(1.0, 0.5), f(np.array([0.0, 1.0]), 0.5))   # 0.655338261900256 [0.         0.65533826]
g = sp.lambdify([(x, y)], expr)                    # one argument: a pair
print(g((1.0, 0.5)))                               # 0.655338261900256
```

The generated function is ordinary NumPy code (`inspect.getsource(f)` shows `return exp(-y**2)*sin(x)`), and it is fast: evaluating the expression at 1000 points with `subs` and `evalf` took 0.73 s on the machine used for this course, while the lambdified function evaluated it at 10000 points in 85 µs, a ratio of about $10^5$ per point. Other targets are selected with `modules`: `"math"` for scalars, `"scipy"`, `"mpmath"` for arbitrary precision, and `"jax"` or `"cupy"` for the array libraries of [4.4.7](/4.4.7#sec-7.4.5).

A typical use is to derive what is tedious and error-prone by hand. Implicit ODE solvers need the **Jacobian matrix** of the right-hand side ([4.4.4](/4.4.4#sec-4.3.3)); for the van der Pol system $u' = v$, $v' = \mu(1 - u^2)v - u$:

```python
from scipy import integrate

u, v, mu = sp.symbols("u v mu")
rhs = sp.Matrix([v, mu * (1 - u ** 2) * v - u])
jac = rhs.jacobian([u, v])             # Matrix([[0, 1], [-2*mu*u*v - 1, mu*(1 - u**2)]])
f_rhs = sp.lambdify((u, v, mu), list(rhs))
f_jac = sp.lambdify((u, v, mu), jac)
sol = integrate.solve_ivp(lambda t, z, m: f_rhs(*z, m), (0, 3000), [2.0, 0.0],
                          method="Radau", jac=lambda t, z, m: f_jac(*z, m), args=(1000.0,))
print(sol.success, sol.t.size)         # True 287
```

For a two-dimensional system the finite-difference Jacobian would serve as well, but for large systems an exact Jacobian is both cheaper and more reliable, and deriving it symbolically removes a classic source of bugs. For code outside Python, the printers `sp.pycode`, `sp.ccode`, `sp.fcode` (Fortran), `sp.octave_code`, `sp.julia_code` and `sp.rust_code` produce source code, and `sp.cse` (common subexpression elimination) factors out repeated subexpressions so that they are computed once:

```python
print(sp.ccode(expr))                  # exp(-pow(y, 2))*sin(x)
print(sp.cse((sp.sin(x) + sp.cos(y)) ** 2 + sp.exp(sp.sin(x) + sp.cos(y))))
# ([(x0, sin(x) + cos(y))], [x0**2 + exp(x0)])
```

### 8.7.2. Expression Swell and the Division of Labor

Exact results have a price. The phenomenon that intermediate and final results of symbolic computations grow far larger than the input is called *expression swell*. The determinant of an $n \times n$ matrix with symbolic entries has $n!$ terms:

| $n$ | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|
| terms of the expanded determinant | 6 | 24 | 120 | 720 | 5040 |
| time (Berkowitz method, then `expand`) | 1 ms | 23 ms | 0.11 s | 1.1 s | 25 s |

while the numerical determinant of a $1000 \times 1000$ matrix by **LU decomposition** takes milliseconds. Similarly, the general cubic equation has roots with about 100 operations each (Cardano's formulas), the general quartic with over 1000, and the roots of the general quintic do not exist in radicals at all. Exact rational arithmetic swells too: the entries of the inverse of an integer matrix can have numerators and denominators with many more digits than the matrix itself.

A second price is that a correct formula is not necessarily a good numerical formula. Evaluating the symbolic root $(-b + \sqrt{b^2 - 4ac})/(2a)$ in double precision for $a = c = 1$, $b = 10^8$ gives $-7.45 \times 10^{-9}$ instead of $-1.0 \times 10^{-8}$, a **catastrophic cancellation** ([3.5.1](/3.5.1#sec-1.3.3)); the algebraically equivalent form $-2c/(b + \sqrt{b^2 - 4ac})$ gives the correct $-1 \times 10^{-8}$. Arnold's limit of §8.4.3 is an extreme case: numerator and denominator are differences of nearly equal quantities that agree to order $x^7$, so the lambdified expression returns $1.0167$ at $x = 0.1$, $0.9896$ at $x = 0.01$ and $0.0$ at $x = 0.001$, where both differences are below the rounding error of the terms; `expr.subs(x, sp.Rational(1, 1000)).evalf(30)` gives the correct $1.0000016667$.

The two kinds of computation therefore divide the work:

| Use symbolic computation for | Use numerical computation for |
|---|---|
| deriving formulas: derivatives, Jacobians, series expansions, closed-form solutions of small problems | evaluating formulas at many points, large matrices, large systems of equations |
| exact answers: rank, null spaces, exact eigenvalues of small matrices, checking identities | problems without closed-form solutions: most integrals, nonlinear ODEs, PDEs |
| problems with parameters, when the dependence on a parameter is of interest | data, which are floating-point numbers with errors anyway |
| checking numerical code: reference values in high precision, tests of derived formulas | anything where the size of the problem grows |

The productive pattern combines them: derive symbolically, simplify, convert with `lambdify` or a code printer, and compute numerically. Derivatives in large numerical programs, such as the gradients of a neural network, are a special case: symbolic differentiation of a long program would swell, and numerical differentiation by finite differences is inaccurate, so they are computed by **automatic differentiation**, which applies the chain rule to the numbers flowing through the program rather than to formulas ([4.7.2](/4.7.2)).

## Summary

- A computer algebra system manipulates expressions exactly; SymPy is a pure-Python library whose results are Python objects, so derivations can be scripted, tested and converted to numerical code.
- Symbols carry assumptions (`positive=True`, `integer=True`, ...); many simplifications, integrals and solutions are valid, and are performed, only under appropriate assumptions.
- Keep numbers exact: `sp.Rational(1, 3)` or `sp.S(1) / 3`, not `1 / 3`. `evalf(n)` and `N` evaluate to any precision.
- Expressions are immutable trees (`func`, `args`); `==` compares structure, `simplify(a - b) == 0` or `a.equals(b)` mathematics; equations are `sp.Eq`.
- Prefer specific transformations (`expand`, `factor`, `cancel`, `apart`, `collect`, `trigsimp`, ...) to `simplify` in programs.
- Calculus: `diff`, `integrate` (unevaluated `Integral` when no closed form is found; evaluate it numerically with `evalf`), `limit`, `series`, `Sum` and `Product`.
- Equations: `solve` for lists of solutions, `solveset` for complete solution sets in a domain, `linsolve` and `nonlinsolve` for systems, `nsolve` for numerical roots; `dsolve` with `ics` for ODEs, checked with `checkodesol`.
- `sp.Matrix` computes exactly: determinants, inverses, rank, null spaces, eigenvectors and Jordan forms of small matrices, also with symbolic entries.
- `lambdify` turns expressions into fast NumPy functions; code printers and `cse` generate code for other languages.
- Expression swell and cancellation in exact formulas limit symbolic computation; derive symbolically, compute numerically.

## Questions

1. Why does `sp.simplify(sp.sqrt(x**2))` return `sqrt(x**2)` for `x = sp.Symbol("x")`, and how do you obtain `x` or `Abs(x)`?

   **Answer** For a complex $x$, $\sqrt{x^2} = x$ is false (for $x = -1$ the left side is $1$), and so is $\sqrt{x^2} = \lvert x\rvert$ (for $x = \mathrm{i}$ the left side is $\mathrm{i}$, the right side $1$); there is no simpler form valid for all complex $x$. Declaring `x = sp.Symbol("x", real=True)` gives `Abs(x)`, and `positive=True` (or `nonnegative=True`) gives `x`.

2. A student computes `sp.integrate(sp.exp(-a*x**2), (x, -sp.oo, sp.oo))` with `a = sp.Symbol("a")` and gets a `Piecewise` expression. Explain the result and how to obtain $\sqrt{\pi/a}$ directly.

   **Answer** The integral converges absolutely for $\operatorname{Re} a > 0$, conditionally on the imaginary axis $a \ne 0$ (a Fresnel integral), and diverges otherwise. For an arbitrary complex symbol SymPy therefore returns $\sqrt{\pi}/\sqrt{a}$ under the condition `Abs(arg(a)) <= pi/2`, and the unevaluated integral otherwise. With `a = sp.Symbol("a", positive=True)` the condition is known to hold and the result is `sqrt(pi)/sqrt(a)`.

3. Use SymPy to find the stationary points of $f(x, y) = x^3 - 3x + y^2$ and classify them with the Hessian. Then explain how you would locate the minima of a similar function with 50 variables.

   **Answer** With `f = x**3 - 3*x + y**2`, `sp.solve([f.diff(x), f.diff(y)], [x, y], dict=True)` gives $(x, y) = (-1, 0)$ and $(1, 0)$. `H = sp.hessian(f, (x, y))` is $\begin{bmatrix} 6x & 0\\ 0 & 2 \end{bmatrix}$: at $(1, 0)$ it is positive definite, a local minimum with $f = -2$; at $(-1, 0)$ it has eigenvalues $-6$ and $2$, a saddle point. For 50 variables, solving the gradient equations symbolically is hopeless (the polynomial system has a huge number of complex solutions and the solvers swell). Instead, derive the gradient symbolically (or by automatic differentiation), convert it with `lambdify`, and pass function and gradient to `scipy.optimize.minimize` with BFGS or L-BFGS-B from several starting points ([4.4.4](/4.4.4#sec-4.2.1)).

4. Why should a numerical program not evaluate a SymPy expression with `expr.subs(...).evalf()` inside a loop, and what should it do instead?

   **Answer** Each `subs` call walks and rebuilds the expression tree in Python, and `evalf` performs arbitrary-precision arithmetic with precision control; both are orders of magnitude slower than floating-point arithmetic (about $10^5$ times per point in §8.7.1). The program should call `f = sp.lambdify(args, expr)` once, outside the loop, and then evaluate `f` on whole NumPy arrays. If the expression is large, `sp.cse` or `sp.simplify` before lambdifying reduces the work per evaluation, and for code in other languages the code printers generate the formula directly.
