---
title: SymPy：符号计算
description: 用 SymPy 做符号计算：符号与假设，精确数，表达式树，代入与求值；化简与改写；导数、积分、极限、级数与求和；用 solve、solveset 和 nsolve 解代数方程；用 dsolve 解微分方程；精确的矩阵计算；lambdify 与代码生成；表达式膨胀以及符号方法与数值方法的分工。
source_hash: f61fc775516e
---

本课程前面的各章都在用数做计算：NumPy 中的浮点数组，SciPy 中的数值算法。符号计算则操作公式本身。求 $ax^2 + bx + c$ 的根时，数值求解器需要 $a$、$b$、$c$ 的值，返回两个**浮点数**；符号系统则返回公式 $x = (-b \pm \sqrt{b^2 - 4ac})/(2a)$，它对所有系数都成立，是精确的，并且可以继续做进一步的运算。本章介绍科学计算 Python 栈中的符号数学库 SymPy：它怎样表示表达式，怎样化简、求导、积分和求解，以及怎样把结果变回快速的数值代码。各种运算背后的数学（极限与级数见 [2.2](/2.2)，微分方程见 [2.4](/2.4)，线性代数见 [2.1](/2.1)）这里不再重复；SymPy 是可靠地完成并检查这些数学的工具。最后一节讨论两个世界的边界：符号结果增长很快，求值常常很慢，也不自动就是好的数值公式，所以实际中两种计算是分工合作的。示例使用 SymPy 1.14 与 Python 3.14。

## 8.1. 符号计算

把两种计算放在一起比较，差别最清楚。数值上，$3x^2 + 6x + 1$ 的根用括号法求得（[4.4.4](/4.4.4#sec-4.2.2)），每组系数、每个根都要算一次：

```python
from scipy import optimize

f = lambda x, a, b, c: a * x ** 2 + b * x + c
print(optimize.brentq(f, -1, 10, args=(3, 6, 1)))   # -0.18350341907227513
print(optimize.brentq(f, -5, -1, args=(3, 6, 1)))   # -1.8164965809277258
```

符号上，一般的方程只需解一次：

```python
import sympy as sp

a, b, c, x = sp.symbols("a b c x")
roots = sp.solve(a * x ** 2 + b * x + c, x)
print(roots)
# [(-b - sqrt(-4*a*c + b**2))/(2*a), (-b + sqrt(-4*a*c + b**2))/(2*a)]
print([r.subs({a: 3, b: 6, c: 1}) for r in roots])   # [-1 - sqrt(6)/3, -1 + sqrt(6)/3]
```

结果是含参数的公式，代入之后是精确的数 $-1 + \sqrt 6/3$，而不是保留 16 位数字的近似值。以这种方式精确地、按代数与微积分的规则操作数学表达式的程序，称为计算机代数系统（computer algebra system），简称 CAS。主要的系统有：

| 系统 | 特点 |
|---|---|
| Mathematica（Wolfram 语言） | 最完整的通用系统；商业软件；Wolfram Alpha 是免费的网页前端 |
| Maple | 微积分与微分方程方面很强；商业软件 |
| MATLAB Symbolic Math Toolbox | MATLAB 内部的符号计算；商业软件 |
| Maxima | Macsyma（1968）的后继，用 Lisp 写成；免费 |
| SymPy | Python 库，纯 Python，免费（BSD 许可）；用在普通的 Python 程序里 |
| SageMath | 用 Python 写的免费数学系统，整合了 SymPy、Maxima、PARI、GAP、FLINT 等许多软件 |

对于困难的积分与微分方程，SymPy 不如 Mathematica 或 Maple 强大，但它是库而不是独立的环境：它的表达式是 Python 对象，所以推导可以编成脚本、测试、与 NumPy 和 SciPy 结合，并在同一个程序里转成数值代码。

推荐的导入方式是 `import sympy as sp`。教程里常见 `from sympy import *`，但它会替换同名的标准函数（`sp.sin` 与 `math.sin` 的行为不同），所以在程序里最好避免。输出默认是纯文本。在 Jupyter 中，`sp.init_printing()` 把表达式显示为排版好的公式；`sp.pprint(expr)` 在终端中打印二维的文本形式，`sp.latex(expr)` 返回 LaTeX 源码，可直接用于报告或像本页这样的页面：

```python
print(sp.latex(roots[0]))   # \frac{- b - \sqrt{- 4 a c + b^{2}}}{2 a}
```

## 8.2. 符号、数与表达式

### 8.2.1. 符号与假设

Python 变量与 SymPy 符号是不同的东西。`x = sp.Symbol("x")` 创建名为 `x` 的符号并把它绑定到 Python 变量 `x`；`sp.symbols("x y z")`（或 `"x, y, z"`）一次创建几个，`sp.symbols("x0:5")` 创建符号 `x0`, ..., `x4`。较老的函数 `sp.var` 创建符号并以副作用的方式把它们注入全局命名空间；显式赋值更清楚。

符号带有假设（assumptions）：`real`、`positive`、`integer`、`nonnegative`、`finite` 等关键字参数，告诉 SymPy 这个符号代表什么样的值。没有假设时符号是任意的复数，许多"显然"的化简便不成立：

```python
x = sp.Symbol("x")
r = sp.Symbol("r", real=True)
p = sp.Symbol("p", positive=True)
n = sp.Symbol("n", integer=True)

print(sp.sqrt(x ** 2), sp.sqrt(r ** 2), sp.sqrt(p ** 2))   # sqrt(x**2) Abs(r) p
print(sp.cos(2 * sp.pi * n), sp.sin(sp.pi * n))             # 1 0
print((p + 1).is_positive, (r ** 2).is_nonnegative, (x ** 2).is_nonnegative)   # True True None
```

$\sqrt{x^2} = x$ 对 $x = -1$ 和 $x = \mathrm{i}$ 都不成立，所以除非假设能够证明化简合理，否则 SymPy 不会动它。属性 `is_positive`、`is_real` 等使用三值逻辑：`True`、`False`，以及表示"无法判定"的 `None`。`p.assumptions0` 列出从所声明的假设推出的一切（正的符号同时是实的、非零的、有限的……）。声明问题中成立的假设，是使 `simplify`、`integrate` 和 `solve` 得到更简单结果的最有效的办法。

### 8.2.2. 精确数与浮点数

SymPy 有自己的数的类型：`sp.Integer`（任意大小）、`sp.Rational(3, 7)`、`sp.Float("3.14", 30)`（任意精度，借助 mpmath 库），以及常数 `sp.pi`、`sp.E`、`sp.I`（虚数单位 $\mathrm{i}$）和 `sp.oo`（$\infty$）。整数与有理数是精确的，只要计算不越出它们，结果也是精确的。陷阱在于，Python 在 SymPy 看到之前就先算了自己的算术：

```python
print(1 / 3 * x, sp.Rational(1, 3) * x, sp.S(1) / 3 * x)   # 0.333333333333333*x x/3 x/3
print(sp.Float(0.1, 30), sp.Float("0.1", 30))
# 0.100000000000000005551115123126 0.100000000000000000000000000000
```

`1 / 3` 在遇到 `x` 之前就是 Python 的浮点数 $0.333\dots$，浮点字面量 `0.1` 也早已带有它的二进制舍入误差（[3.5.1](/3.5.1#sec-1.2.4)），30 位的 `Float` 忠实地保留了这一误差。精确的常数应写成 `sp.Rational(1, 3)`、`sp.S(1) / 3`（`sp.S` 把 Python 对象转成 SymPy 对象；`sp.S("1/3")` 解析字符串），或者把符号写在前面，如 `x / 3`。反过来，`sp.nsimplify(0.333333333333)` 猜出精确的数 `1/3`，`int()`、`float()` 与 `complex()` 把 SymPy 的数转回 Python 的数。

### 8.2.3. 作为树的表达式

SymPy 的**表达式**是一棵树：每个节点是一个函数或运算符（`Add`、`Mul`、`Pow`、`sin`……），它的子节点是参数，叶子是符号和数。`expr.func` 是树的头，`expr.args` 是子节点的元组，`sp.srepr` 显示整个结构：

```python
e = x ** 2 + 2 * sp.sin(y)
print(e.func, e.args)    # <class 'sympy.core.add.Add'> (x**2, 2*sin(y))
print(sp.srepr(x ** 2 - 2 * x))
# Add(Pow(Symbol('x'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('x')))
```

没有减法节点：$a - b$ 存为 `Add(a, Mul(-1, b))`，$a/b$ 存为 `Mul(a, Pow(b, -1))`。知道这一点可以解释若干行为。表达式是不可变的：每个运算都返回新的树。`Add` 与 `Mul` 的参数按规范的顺序存放，所以 `x + y` 与 `y + x` 是同一个对象，但除此之外 SymPy 只做代价很小的自动化简。特别地，`==` 检验的是树的*结构*相等，而不是数学上的相等：

```python
print((x + 1) ** 2 == x ** 2 + 2 * x + 1)                        # False
print(sp.expand((x + 1) ** 2) == x ** 2 + 2 * x + 1)             # True
print(sp.simplify((x + 1) ** 2 - (x ** 2 + 2 * x + 1)) == 0)     # True
```

要检验两个表达式在数学上是否相等，化简它们的差（或调用 `a.equals(b)`，它还会在随机点上做数值求值）。方程写成 `sp.Eq(lhs, rhs)`，不用 `==`。

未定义的函数用 `f = sp.Function("f")` 创建；`f(x)` 是一个表达式，可以求导（得到未求值的 `Derivative(f(x), x)`），也可以用作微分方程的未知函数。匿名函数是 `sp.Lambda(x, x ** 3)`，把它作用于 `y + 1` 得到 `(y + 1)**3`。数学函数（`sp.sin`、`sp.exp`、`sp.log`、`sp.gamma`、`sp.besselj`……）产生表达式节点，从不产生浮点结果，除非它们的参数是一个已知精确值的数（`sp.sin(sp.pi / 6)` 是 `1/2`）。

### 8.2.4. 代入与数值求值

`expr.subs(old, new)` 替换一个子表达式，用字典可以一次替换几个。代入数就是对表达式求值，若这些数是精确的，求值也是精确的：

```python
e = x ** 3 + 7 * y + z ** 2 * x
print(e.subs({x: 1.3, y: 0.2, z: 5}))                                     # 36.0970000000000
print(e.subs({x: sp.Rational(13, 10), y: sp.Rational(1, 5), z: 5}))       # 36097/1000
print(sp.pi.evalf(30), sp.N(sp.sqrt(2), 50))
# 3.14159265358979323846264338328 1.4142135623730950488016887242096980785696718753769
```

`expr.evalf(n)`，或等价地 `sp.N(expr, n)`，用任意精度的算术求值到 `n` 位有效数字，内部自动调整工作精度，使返回的数字都是正确的。这使 SymPy 成为检验浮点代码的有用裁判：§8.7.2 给出一个极限，双精度根本无法算出它的值。要在许多点上对表达式求值，`subs` 与 `evalf` 都太慢了；`lambdify`（§8.7.1）把表达式转成 NumPy 函数。

## 8.3. 化简与改写

表达式没有唯一的"最简形式"：$(x+1)^2$ 与 $x^2 + 2x + 1$ 各自在某些用途上更简单。`sp.simplify(expr)` 尝试若干策略，并按某种复杂度度量返回最短的结果，这在交互使用时很方便，但慢、不可预测，有时还令人失望。在程序里，执行某一种特定变换的函数更好：

| 函数 | 变换 | 例 |
|---|---|---|
| `expand` | 展开乘积与幂 | $(x+y)^3 \to x^3 + 3x^2y + 3xy^2 + y^3$ |
| `factor` | 在有理数域上分解多项式 | $x^3 - x^2 - x + 1 \to (x-1)^2(x+1)$ |
| `collect(expr, x)` | 合并 `x` 的各次幂的系数 | $xy + x + 2x^2 - x^2y - 3 \to x^2(2-y) + x(y+1) - 3$ |
| `cancel` | 把有理函数约成最简的 $p/q$ | $\frac{x^2-1}{x^2+2x+1} \to \frac{x-1}{x+1}$ |
| `apart` | **部分分式**分解 | $\frac{4x^2+3}{x(x-1)^2} \to \frac{3}{x} + \frac{1}{x-1} + \frac{7}{(x-1)^2}$ |
| `together` | 通分 | $\frac1x + \frac1{x+1} \to \frac{2x+1}{x(x+1)}$ |
| `trigsimp` | 三角恒等式 | $\sin^4 x - 2\sin^2 x\cos^2 x + \cos^4 x \to \frac{\cos 4x}{2} + \frac12$ |
| `expand_trig` | 加法公式 | $\sin 2x \to 2\sin x\cos x$ |
| `powsimp` | 合并幂 | $x^y x^2 \to x^{y+2}$ |
| `expand_log`、`logcombine` | 拆分或合并对数 | $\log(pq^2) \leftrightarrow \log p + 2\log q$ |
| `gammasimp` | 阶乘、二项式系数、Gamma 函数 | $\frac{(x+1)!}{x!} \to x + 1$ |
| `radsimp` | 分母有理化 | $\frac{1}{1+\sqrt2} \to \sqrt2 - 1$ |
| `expr.rewrite(f)` | 用另一个函数表示 | $\cos x \to \frac{\mathrm{e}^{\mathrm{i}x}}{2} + \frac{\mathrm{e}^{-\mathrm{i}x}}{2}$ |

`sp.fraction(expr)` 分别返回分子与分母。这些变换中有几个只在一定的假设下有效，SymPy 只在假设成立时才应用它们。$\log x + \log y = \log(xy)$ 对 $x = y = -1$ 是错的，$x^a y^a = (xy)^a$ 也因类似的原因失效，所以对普通的符号，`logcombine` 与 `powsimp` 什么也不做，而对正的符号它们就会合并：

```python
p, q = sp.symbols("p q", positive=True)
print(sp.logcombine(sp.log(x) + sp.log(y)), sp.logcombine(sp.log(p) + sp.log(q)))   # log(x) + log(y) log(p*q)
print(sp.powsimp(x ** y * y ** y), sp.powsimp(p ** y * q ** y))                     # x**y*y**y (p*q)**y
```

参数 `force=True` 使这些函数忽略假设，只有用户知道结果对所关心的取值是正确的时，才可以这样做。

## 8.4. 微积分

### 8.4.1. 导数

求导是微积分运算中最容易自动化的：[2.2.4](/2.2.4) 的法则机械地作用于表达式树的每个节点。`expr.diff(x)`（或 `sp.diff(expr, x)`）对 `x` 求导；再给出更多参数就得到高阶导数与混合偏导数：

```python
e = sp.exp(x * y) * sp.sin(x)
print(e.diff(x))          # y*exp(x*y)*sin(x) + exp(x*y)*cos(x)
print(sp.diff(x ** 10, x, 4))   # 5040*x**6, the fourth derivative
print(e.diff(x, 2, y))    # second derivative in x, then one in y
d = sp.Derivative(e, x)   # unevaluated; d.doit() computes it
```

`diff(x, x, y)` 与 `diff(x, 2, y)` 这样的参数是等价的。未求值的 `Derivative`（类似地还有 `Integral`、`Limit`、`Sum`）可以在计算之前先显示公式，`.doit()` 对它求值。对于向量值函数，`sp.Matrix(...).jacobian(vars)` 给出 **Jacobi 矩阵**，`sp.hessian(f, vars)` 给出 Hesse 矩阵：

```python
F = sp.Matrix([x ** 2 * y, 5 * x + sp.sin(y)])
print(F.jacobian([x, y]))             # Matrix([[2*x*y, x**2], [5, cos(y)]])
print(sp.hessian(x ** 3 + x * y ** 2, (x, y)))   # Matrix([[6*x, 2*y], [2*y, 2*x]])
```

公式既然是 Python 对象，一个公式库就是一组接收并返回表达式的普通 Python 函数。例如，直角坐标系中的梯度，既可以作用于未定义的函数，也可以作用于具体的函数：

```python
def gradient(f, coords):
    """Gradient of the scalar expression f in Cartesian coordinates."""
    return sp.Matrix([f.diff(c) for c in coords])


f = sp.Function("f")(x, y, z)
print(gradient(f, (x, y, z)).T)   # Matrix([[Derivative(f(x, y, z), x), ..., Derivative(f(x, y, z), z)]])
print(gradient(x * y * z, (x, y, z)).T)   # Matrix([[y*z, x*z, x*y]])
```

### 8.4.2. 积分

积分更难：大多数初等函数没有初等的**原函数**，而当它存在时找到它是一个真正的算法问题。`sp.integrate(expr, x)` 返回一个原函数（不含积分常数），`sp.integrate(expr, (x, a, b))` 返回定积分，几个元组表示重积分，从第一个元组到最后一个依次积分：

```python
print(sp.integrate(x ** 2 * sp.exp(x), x))                        # (x**2 - 2*x + 2)*exp(x)
print(sp.integrate(1 / (x ** 3 + 1), x))
# log(x + 1)/3 - log(x**2 - x + 1)/6 + sqrt(3)*atan(2*sqrt(3)*x/3 - sqrt(3)/3)/3
print(sp.integrate(sp.exp(-x ** 2), (x, -sp.oo, sp.oo)))          # sqrt(pi)
print(sp.integrate(sp.exp(-x ** 2), x))                           # sqrt(pi)*erf(x)/2
print(sp.integrate(sp.sin(x) / x, (x, 0, sp.oo)))                 # pi/2
print(sp.integrate(x * y, (y, 0, x), (x, 0, 1)))                  # 1/8
```

结果中有 **Gauss 积分** $\int_{-\infty}^{\infty} \mathrm{e}^{-x^2}\,\mathrm{d}x = \sqrt\pi$，以及用**误差函数**表示的 $\mathrm{e}^{-x^2}$ 的原函数，误差函数是 SymPy 认识的一个特殊函数。最后一行中元组的顺序很重要：`(y, 0, x)` 最先积分，所以它计算的是 $\int_0^1 \int_0^x xy\,\mathrm{d}y\,\mathrm{d}x$。SymPy 把查表和启发式方法与 Risch 算法（Risch algorithm）的部分实现结合起来，对定积分还结合了经 Meijer G 函数的积分；Risch 算法是一种判定过程，它要么找到初等原函数，要么证明不存在。

假设对反常积分有影响。$\int_0^\infty \mathrm{e}^{-ax}\,\mathrm{d}x$ 只在 $\operatorname{Re} a > 0$ 时收敛，所以对普通的符号 `a`，SymPy 返回带条件 `Abs(arg(a)) < pi/2` 的 `Piecewise` 结果；对 `a = sp.Symbol("a", positive=True)`，它返回 `1/a`。找不到闭式时，`integrate` 把积分以未求值的 `Integral` 对象返回（当 Risch 算法已证明不存在初等原函数时，则是 `NonElementaryIntegral`）。这样的积分仍然可以数值求值到任意精度，最可靠的办法是直接把它构造成 `Integral`：

```python
print(sp.integrate(x ** x, (x, 0, 1)))                # Integral(x**x, (x, 0, 1))
print(sp.Integral(x ** x, (x, 0, 1)).evalf(20))       # 0.78343051071213440706
```

要做许多次这样的求值时，对 lambdify 之后的被积函数使用 `scipy.integrate.quad` 要快得多。

### 8.4.3. 极限、级数与求和

`sp.limit(expr, x, x0)` 用 Gruntz 算法计算极限，该算法使用渐近展开，而不是 **L'Hôpital 法则**；参数 `dir="+"`（默认）、`"-"` 或 `"+-"` 选择单侧或双侧极限，`x0` 可以是 `sp.oo`：

```python
print(sp.limit(sp.sin(x) / x, x, 0), sp.limit((1 + 1 / x) ** x, x, sp.oo))   # 1 E
print(sp.limit(1 / x, x, 0), sp.limit(1 / x, x, 0, "-"))                     # oo -oo
```

V. I. Arnold 提出过一个著名的检验

$$
\lim_{x \to 0} \frac{\sin \tan x - \tan \sin x}{\arcsin \arctan x - \arctan \arcsin x} = 1,
$$
用 L'Hôpital 法则要求导七次才能解决。SymPy 在不到一秒钟内返回 1，`series` 则说明了原因：

```python
num = sp.sin(sp.tan(x)) - sp.tan(sp.sin(x))
den = sp.asin(sp.atan(x)) - sp.atan(sp.asin(x))
print(sp.limit(num / den, x, 0))      # 1
print(num.series(x, 0, 10))           # -x**7/30 - 29*x**9/756 + O(x**10)
print(den.series(x, 0, 10))           # -x**7/30 + 13*x**9/756 + O(x**10)
```

`expr.series(x, x0, n)` 计算在 `x0` 处的 **Taylor 级数**，直到但不包括 `n` 阶的项（默认 `x0 = 0`，`n = 6`），并带有阶项 `O(...)`；`.removeO()` 去掉阶项，留下 **Taylor 多项式**：

```python
print(sp.exp(x).series(x, 0, 4))       # 1 + x + x**2/2 + x**3/6 + O(x**4)
t = sp.sin(x).series(x, sp.pi / 2, 5).removeO()   # 1 - (x - pi/2)**2/2 + (x - pi/2)**4/24
print(t.subs(x, 89 * sp.pi / 180).evalf())        # 0.999847695156430, sin 89° = 0.999847695156391
```

`sp.Sum(expr, (k, a, b))` 与 `sp.Product(expr, (k, a, b))` 表示和与积，用 `.doit()` 求值；`sp.summation` 直接求值。SymPy 知道许多闭式，包括无穷级数：

```python
k, n = sp.symbols("k n", integer=True, positive=True)
print(sp.Sum(1 / k ** 2, (k, 1, sp.oo)).doit())         # pi**2/6
print(sp.Sum(k ** 3, (k, 1, n)).doit().factor())        # n**2*(n + 1)**2/4
print(sp.Sum(1 / k ** 3, (k, 1, sp.oo)).doit())         # zeta(3)
print(sp.summation(x ** k / sp.factorial(k), (k, 0, sp.oo)))   # exp(x)
```

## 8.5. 方程

### 8.5.1. 代数方程

SymPy 有两个主要的求解器。`sp.solve(f, x)` 解 $f = 0$（或一个 `Eq`），返回解的列表；加上 `dict=True` 则返回字典的列表，这是方程组最稳妥的格式。`sp.solveset(f, x, domain)` 返回一个数学上的集合，能够表达列表表达不了的东西：无穷多个解、在定义域中无解，或者在找不到闭式解时的"这个方程的解"：

```python
print(sp.solve(x ** 2 - 4, x), sp.solve(x ** 2 - 4, x, dict=True))   # [-2, 2] [{x: -2}, {x: 2}]
print(sp.solve(sp.sin(x) - sp.Rational(1, 2), x))                     # [pi/6, 5*pi/6]
print(sp.solveset(sp.sin(x) - sp.Rational(1, 2), x, domain=sp.S.Reals))
# Union(ImageSet(Lambda(_n, 2*_n*pi + pi/6), Integers), ImageSet(Lambda(_n, 2*_n*pi + 5*pi/6), Integers))
print(sp.solveset(x ** 2 + 1, x), sp.solveset(x ** 2 + 1, x, sp.S.Reals))   # {-I, I} EmptySet
print(sp.solveset(sp.cos(x) - x, x, sp.S.Reals))     # ConditionSet(x, Eq(-x + cos(x), 0), Reals)
print(sp.solveset(x ** 2 - 3 * x + 2 < 0, x, sp.S.Reals))   # Interval.open(1, 2)
```

`solve` 只返回了 $\sin x = 1/2$ 在 $[0, 2\pi)$ 中的两个解；`solveset` 返回了全部的解，$\pi/6 + 2k\pi$ 与 $5\pi/6 + 2k\pi$。`solveset` 的默认定义域是复数。对于方程组，`sp.linsolve` 处理线性方程组（包括欠定的，其解集含有自由参数），`sp.nonlinsolve` 处理多项式及其他非线性方程组：

```python
print(sp.solve([x + y - 3, x - y - 1], [x, y]))              # {x: 2, y: 1}
print(sp.linsolve([x + y - 3, 2 * x + 2 * y - 6], [x, y]))  # {(3 - y, y)}
print(sp.nonlinsolve([x ** 2 + y ** 2 - 4, x - y], [x, y]))  # {(-sqrt(2), -sqrt(2)), (sqrt(2), sqrt(2))}
```

许多方程没有闭式解。五次及更高次的多项式方程一般不能用根式求解（Abel–Ruffini 定理）；此时 SymPy 把根精确地表示为 `CRootOf` 对象，它可以求值到任意精度。超越方程有时有用特殊函数表示的解，如 $x\mathrm{e}^x = 1$ 用 Lambert W 函数，但通常没有。对于这些，`sp.nsolve(f, x, x0)` 从一个起点出发，以任意精度数值地求根，方程组也可以：

```python
print(sp.solve(x ** 5 - x + 1, x)[0], sp.CRootOf(x ** 5 - x + 1, 0).evalf())   # CRootOf(x**5 - x + 1, 0) -1.16730397826142
print(sp.solve(x * sp.exp(x) - 1, x))                       # [LambertW(1)]
print(sp.nsolve(sp.cos(x) - x, x, 1, prec=30))              # 0.739085133215160641655312087674
print(sp.nsolve([x ** 2 + y ** 2 - 4, sp.exp(x) + y - 1], [x, y], [1, -1]).T)
# Matrix([[1.00416873847466, -1.72963728702587]]), the root found by optimize.root in 4.4.4
```

### 8.5.2. 微分方程

`sp.dsolve(eq, f(x))` 符号地求解常微分方程。它先对方程分类（`sp.classify_ode(eq)` 列出适用的方法：可分离变量、线性、恰当、Bernoulli、常系数……；方法本身就是 [2.4.3](/2.4.3) 与 [2.4.9](/2.4.9) 的那些），然后返回含通解的 `Eq`，其中的常数是 `C1`、`C2`……参数 `ics` 给定初值条件。Newton 冷却定律，$T' = -k(T - T_{\mathrm{a}})$，$T(0) = T_0$：

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

`checkodesol` 把解代回方程，这对任何解（无论是 SymPy 求出的还是手算的）都是有用的检查。导数的初值条件用 `subs` 写出。**阻尼振动** $q'' + \frac12 q' + q = 0$，以及在固有频率下受迫的无阻尼振子的**共振**：

```python
q = sp.Function("q")
ics = {q(0): 1, q(t).diff(t).subs(t, 0): 0}
print(sp.dsolve(q(t).diff(t, 2) + q(t).diff(t) / 2 + q(t), ics=ics))
# Eq(q(t), (sqrt(15)*sin(sqrt(15)*t/4)/15 + cos(sqrt(15)*t/4))*exp(-t/4))
ics0 = {q(0): 0, q(t).diff(t).subs(t, 0): 0}
print(sp.dsolve(sp.Eq(q(t).diff(t, 2) + q(t), sp.cos(t)), ics=ics0))   # Eq(q(t), t*sin(t)/2)
```

方程组以方程的列表传入，而**逻辑斯谛增长**方程是 Bernoulli 方程，经 `simplify` 之后可以求得闭式解：

```python
y1, y2 = sp.symbols("y1 y2", cls=sp.Function)
print(sp.dsolve([sp.Eq(y1(t).diff(t), y2(t)), sp.Eq(y2(t).diff(t), -y1(t))],
                ics={y1(0): 1, y2(0): 0}))     # [Eq(y1(t), cos(t)), Eq(y2(t), -sin(t))]

r, K, y0 = sp.symbols("r K y_0", positive=True)
P = sp.Function("P")
s = sp.dsolve(sp.Eq(P(t).diff(t), r * P(t) * (1 - P(t) / K)), ics={P(0): y0})
print(sp.simplify(s.rhs))                      # K*y_0*exp(r*t)/(K + y_0*exp(r*t) - y_0)
```

然而大多数微分方程没有闭式解，对它们 `dsolve` 会抛出 `NotImplementedError`（例如对 $y' = \sin y + t$），或者返回隐式解或级数解（`hint="1st_power_series"`）。任何实际规模的非线性模型都用 `solve_ivp`（[4.4.4](/4.4.4#sec-4.3.2)）数值求解，SymPy 仍然可以帮忙推导右端函数或它的 Jacobi 矩阵（§8.7.1）。偏微分方程只在简单的情形可以符号求解（`sp.pdsolve` 处理一阶线性的）；用有限差分的数值解法见 [4.4.4](/4.4.4#sec-4.6.3)。

## 8.6. 矩阵

`sp.Matrix` 是由 SymPy 表达式组成的二维矩阵，可以由嵌套的列表创建，也可以由形状与下标的函数创建（`sp.Matrix(2, 2, lambda i, j: i**2 + j**2)`），或用 `sp.eye`、`sp.zeros`、`sp.ones`、`sp.diag` 创建。乘积写成 `A * B` 或 `A @ B`，幂写成 `A ** k`，转置是 `A.T`。由于元素是精确的，[2.1](/2.1) 的各种方法给出精确的结果，对含符号元素的矩阵也是如此：

```python
a, b = sp.symbols("a b")
A = sp.Matrix([[a, b], [b, a]])
print(A.det(), A.inv())          # a**2 - b**2, Matrix([[a/(a**2 - b**2), -b/(a**2 - b**2)], ...])
print(A.eigenvals())             # {a - b: 1, a + b: 1}, eigenvalue: algebraic multiplicity
print(A.eigenvects())            # [(a - b, 1, [Matrix([[-1], [1]])]), (a + b, 1, [Matrix([[1], [1]])])]
print(A.charpoly().as_expr())    # a**2 - 2*a*lambda - b**2 + lambda**2
```

| 任务 | 方法 |
|---|---|
| **行列式**、**逆矩阵**、**秩** | `A.det()`、`A.inv()`、`A.rank()` |
| 简化行阶梯形、零空间、列空间 | `A.rref()`、`A.nullspace()`、`A.columnspace()` |
| 解 $A\boldsymbol{x} = \boldsymbol{b}$ | `A.solve(b)`、`A.LUsolve(b)`、`sp.linsolve((A, b), vars)` |
| 分解 | `A.LUdecomposition()`、`A.QRdecomposition()`、`A.cholesky()` |
| **特征值**、**特征向量**、**特征多项式** | `A.eigenvals()`、`A.eigenvects()`、`A.charpoly()` |
| 对角化、**Jordan 标准形** | `A.diagonalize()`、`A.jordan_form()`（返回 $P$、$J$，使 $A = PJP^{-1}$） |
| 奇异值、范数 | `A.singular_values()`、`A.norm(ord)` |
| **矩阵指数**、其他矩阵函数 | `A.exp()`、`A.analytic_func(f, x)` |

对于奇异矩阵，精确计算能够判定浮点算术只能近似回答的问题：$\begin{bmatrix} 1&2&3\\4&5&6\\7&8&9 \end{bmatrix}$ 的秩为 2，零空间由 $(1, -2, 1)^{\mathsf T}$ 张成，不涉及任何容差（比较数值秩，它要对奇异值取容差来判定，见 [2.1.3](/2.1.3) 与 [4.4.3](/4.4.3) 中的 `np.linalg.matrix_rank`）。$\begin{bmatrix} 2&1\\-1&4 \end{bmatrix}$ 的 Jordan 标准形是单个块 $\begin{bmatrix} 3&1\\0&3 \end{bmatrix}$，任何浮点特征值程序都无法可靠地算出它，因为任意小的扰动都会使二重特征值分裂。取 $M = \begin{bmatrix} 0&1\\-1&0 \end{bmatrix}$，则 $tM$ 的矩阵指数恰好是旋转矩阵，它解出 §8.5.2 的方程组 $\boldsymbol{y}' = M\boldsymbol{y}$（[2.4.8](/2.4.8)）：

```python
M = sp.Matrix([[0, 1], [-1, 0]])
print(sp.simplify((M * t).exp()))   # Matrix([[cos(t), sin(t)], [-sin(t), cos(t)]])
```

`sp.MatrixSymbol("X", 3, 3)` 是本身就是符号、没有元素的矩阵：`(X * Y).T` 这样的表达式按矩阵代数的规则化简（为 `Y.T*X.T`），这对阶数未指定的矩阵的推导很有用。矩阵是可变的；`sp.ImmutableMatrix` 是可以用作字典键或放进其他表达式的变体。

## 8.7. 从符号计算到数值计算

### 8.7.1. lambdify 与代码生成

符号结果最常需要的形式是快速的数值函数。`sp.lambdify(args, expr, modules)` 把表达式翻译成调用数值库的 Python 源码，并把它编译成函数；用默认的模块时它使用 NumPy（装有 SciPy 时，特殊函数用 SciPy），所以这个函数接受数组：

```python
import numpy as np

expr = sp.sin(x) * sp.exp(-y ** 2)
f = sp.lambdify((x, y), expr)
print(f(1.0, 0.5), f(np.array([0.0, 1.0]), 0.5))   # 0.655338261900256 [0.         0.65533826]
g = sp.lambdify([(x, y)], expr)                    # one argument: a pair
print(g((1.0, 0.5)))                               # 0.655338261900256
```

生成的函数是普通的 NumPy 代码（`inspect.getsource(f)` 显示 `return exp(-y**2)*sin(x)`），而且很快：在本课程所用的机器上，用 `subs` 与 `evalf` 在 1000 个点上对表达式求值用了 0.73 s，而 lambdify 之后的函数在 10000 个点上求值只用 85 µs，每个点的比值约为 $10^5$。用 `modules` 选择其他目标：标量用 `"math"`，还有 `"scipy"`、任意精度的 `"mpmath"`，以及 [4.4.7](/4.4.7#sec-7.4.5) 中数组库的 `"jax"` 与 `"cupy"`。

一种典型的用法是推导手算起来繁琐而易错的东西。隐式的常微分方程求解器需要右端函数的 **Jacobi 矩阵**（[4.4.4](/4.4.4#sec-4.3.3)）；对 van der Pol 方程组 $u' = v$，$v' = \mu(1 - u^2)v - u$：

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

对二维的方程组，有限差分的 Jacobi 矩阵同样够用，但对大型方程组，精确的 Jacobi 矩阵既便宜又可靠，而用符号方法推导它去除了一个经典的出错来源。对于 Python 之外的代码，打印器 `sp.pycode`、`sp.ccode`、`sp.fcode`（Fortran）、`sp.octave_code`、`sp.julia_code` 与 `sp.rust_code` 生成源码，`sp.cse`（公共子表达式消除）把重复出现的子表达式提出来，使它们只计算一次：

```python
print(sp.ccode(expr))                  # exp(-pow(y, 2))*sin(x)
print(sp.cse((sp.sin(x) + sp.cos(y)) ** 2 + sp.exp(sp.sin(x) + sp.cos(y))))
# ([(x0, sin(x) + cos(y))], [x0**2 + exp(x0)])
```

### 8.7.2. 表达式膨胀与分工

精确的结果是有代价的。符号计算的中间结果和最终结果比输入大得多的现象称为表达式膨胀（expression swell）。含符号元素的 $n \times n$ 矩阵的行列式有 $n!$ 项：

| $n$ | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|
| 展开后行列式的项数 | 6 | 24 | 120 | 720 | 5040 |
| 时间（Berkowitz 方法，然后 `expand`） | 1 ms | 23 ms | 0.11 s | 1.1 s | 25 s |

而用 **LU 分解**数值地计算 $1000 \times 1000$ 矩阵的行列式只需几毫秒。类似地，一般三次方程的根各有约 100 次运算（Cardano 公式），一般四次方程的根有一千多次，而一般五次方程的根用根式根本不存在。精确的有理数算术同样会膨胀：整数矩阵的逆矩阵的元素，分子与分母的位数可能比矩阵本身多得多。

第二个代价是，正确的公式不一定是好的数值公式。对 $a = c = 1$、$b = 10^8$，在双精度下计算符号求出的根 $(-b + \sqrt{b^2 - 4ac})/(2a)$，得到 $-7.45 \times 10^{-9}$ 而不是 $-1.0 \times 10^{-8}$，这是**灾难性抵消**（[3.5.1](/3.5.1#sec-1.3.3)）；代数上等价的形式 $-2c/(b + \sqrt{b^2 - 4ac})$ 给出正确的 $-1 \times 10^{-8}$。§8.4.3 中 Arnold 的极限是一个极端的情形：分子与分母都是几乎相等的量之差，二者一直到 $x^7$ 阶都相同，所以 lambdify 之后的表达式在 $x = 0.1$ 处返回 $1.0167$，在 $x = 0.01$ 处返回 $0.9896$，在 $x = 0.001$ 处返回 $0.0$，此时两个差都小于各项的舍入误差；`expr.subs(x, sp.Rational(1, 1000)).evalf(30)` 则给出正确的 $1.0000016667$。

所以两种计算要分工：

| 符号计算用于 | 数值计算用于 |
|---|---|
| 推导公式：导数、Jacobi 矩阵、级数展开、小问题的闭式解 | 在许多点上对公式求值，大型矩阵，大型方程组 |
| 精确的答案：秩、零空间、小矩阵的精确特征值，检验恒等式 | 没有闭式解的问题：大多数积分，非线性常微分方程，偏微分方程 |
| 含参数的问题，当对参数的依赖关系有兴趣时 | 数据，它们本来就是带误差的浮点数 |
| 检验数值代码：高精度的参考值，对推导出的公式做测试 | 问题的规模增长的一切情形 |

有成效的模式是把二者结合：符号地推导、化简，用 `lambdify` 或代码打印器转换，再数值地计算。大型数值程序中的导数，如神经网络的梯度，是一种特殊情形：对很长的程序做符号求导会膨胀，用有限差分做数值求导又不精确，所以它们用**自动微分**计算，它把链式法则作用于流过程序的数，而不是公式（[4.7.2](/4.7.2)）。

## 小结

- 计算机代数系统精确地操作表达式；SymPy 是纯 Python 库，结果是 Python 对象，所以推导可以编成脚本、测试并转成数值代码。
- 符号带有假设（`positive=True`、`integer=True`……）；许多化简、积分与解只在适当的假设下才成立，也才会被执行。
- 保持数的精确：用 `sp.Rational(1, 3)` 或 `sp.S(1) / 3`，不要写 `1 / 3`。`evalf(n)` 与 `N` 求值到任意精度。
- 表达式是不可变的树（`func`、`args`）；`==` 比较结构，`simplify(a - b) == 0` 或 `a.equals(b)` 比较数学上的相等；方程用 `sp.Eq`。
- 在程序里，用具体的变换（`expand`、`factor`、`cancel`、`apart`、`collect`、`trigsimp`……）而不是 `simplify`。
- 微积分：`diff`、`integrate`（找不到闭式时是未求值的 `Integral`；用 `evalf` 数值求值）、`limit`、`series`、`Sum` 与 `Product`。
- 方程：`solve` 给出解的列表，`solveset` 给出定义域中完整的解集，`linsolve` 与 `nonlinsolve` 解方程组，`nsolve` 求数值根；常微分方程用带 `ics` 的 `dsolve`，并用 `checkodesol` 检验。
- `sp.Matrix` 精确地计算：小矩阵的行列式、逆矩阵、秩、零空间、特征向量与 Jordan 标准形，含符号元素时也可以。
- `lambdify` 把表达式变成快速的 NumPy 函数；代码打印器与 `cse` 为其他语言生成代码。
- 精确公式中的表达式膨胀与抵消限制了符号计算；符号地推导，数值地计算。

## 思考题

1. 为什么对 `x = sp.Symbol("x")`，`sp.simplify(sp.sqrt(x**2))` 返回 `sqrt(x**2)`？怎样才能得到 `x` 或 `Abs(x)`？

   **答** 对复数 $x$，$\sqrt{x^2} = x$ 不成立（$x = -1$ 时左边是 $1$），$\sqrt{x^2} = \lvert x\rvert$ 也不成立（$x = \mathrm{i}$ 时左边是 $\mathrm{i}$，右边是 $1$）；不存在对所有复数 $x$ 都有效的更简单的形式。声明 `x = sp.Symbol("x", real=True)` 得到 `Abs(x)`，`positive=True`（或 `nonnegative=True`）得到 `x`。

2. 某学生对 `a = sp.Symbol("a")` 计算 `sp.integrate(sp.exp(-a*x**2), (x, -sp.oo, sp.oo))`，得到一个 `Piecewise` 表达式。解释这一结果，并说明怎样直接得到 $\sqrt{\pi/a}$。

   **答** 该积分在 $\operatorname{Re} a > 0$ 时绝对收敛，在虚轴 $a \ne 0$ 上条件收敛（Fresnel 积分），其余情形发散。所以对任意的复符号，SymPy 在条件 `Abs(arg(a)) <= pi/2` 下返回 $\sqrt{\pi}/\sqrt{a}$，其他情形返回未求值的积分。取 `a = sp.Symbol("a", positive=True)` 时条件已知成立，结果是 `sqrt(pi)/sqrt(a)`。

3. 用 SymPy 求 $f(x, y) = x^3 - 3x + y^2$ 的驻点，并用 Hesse 矩阵分类。然后说明对一个类似的 50 元函数，你会怎样找它的极小点。

   **答** 取 `f = x**3 - 3*x + y**2`，`sp.solve([f.diff(x), f.diff(y)], [x, y], dict=True)` 给出 $(x, y) = (-1, 0)$ 与 $(1, 0)$。`H = sp.hessian(f, (x, y))` 是 $\begin{bmatrix} 6x & 0\\ 0 & 2 \end{bmatrix}$：在 $(1, 0)$ 处它正定，是局部极小点，$f = -2$；在 $(-1, 0)$ 处它的特征值为 $-6$ 与 $2$，是鞍点。对 50 个变量，符号地解梯度方程是没有希望的（这个多项式方程组有极多的复数解，求解器会膨胀）。应当符号地推导梯度（或用自动微分），用 `lambdify` 转换，再把函数与梯度交给 `scipy.optimize.minimize`，用 BFGS 或 L-BFGS-B 从几个起点出发（[4.4.4](/4.4.4#sec-4.2.1)）。

4. 为什么数值程序不应当在循环里用 `expr.subs(...).evalf()` 对 SymPy 表达式求值？它应当怎么做？

   **答** 每次 `subs` 调用都要在 Python 中遍历并重建表达式树，`evalf` 则做带精度控制的任意精度算术；二者都比浮点算术慢几个数量级（§8.7.1 中每个点约慢 $10^5$ 倍）。程序应当在循环之外调用一次 `f = sp.lambdify(args, expr)`，然后对整个 NumPy 数组求 `f`。若表达式很大，在 lambdify 之前用 `sp.cse` 或 `sp.simplify` 可以减少每次求值的工作量；对其他语言的代码，则由代码打印器直接生成公式。
