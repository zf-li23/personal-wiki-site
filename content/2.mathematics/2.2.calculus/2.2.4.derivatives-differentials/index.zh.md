---
title: 导数与微分
---

从本章起进入微分学。导数描述函数在一点的变化率：几何上是曲线切线的斜率，物理上是瞬时速度；微分描述函数增量的线性主部，即"在局部用直线代替曲线"。本章先由**函数极限**给出导数的定义，讨论单侧导数以及可导与**连续函数**的关系；然后建立四则运算、链式法则与反函数求导法则，求出全部**基本初等函数**的导数，从而**初等函数**都可以机械地求导；再讨论对数求导法、参数方程与隐函数的求导、高阶导数与 Leibniz 公式；最后引入微分及其形式不变性。下一章（[2.2.5](/2.2.5)）用导数研究函数的单调性、极值、凸性与 Taylor 展开；[2.2.6](/2.2.6) 反过来由导数求原函数；多元函数的偏导数与全微分在 [2.2.10](/2.2.10) 中讨论。

## 4.1. 导数的概念

### 4.1.1. 导数

引例 1（瞬时速度）：质点沿 $x$ 轴做直线运动，$t$ 时刻的位置为 $x(t)$。从 $t_0$ 到 $t_0 + \Delta t$ 的位移是 $x(t_0+\Delta t) - x(t_0)$，平均速度为 $\frac{x(t_0+\Delta t)-x(t_0)}{\Delta t}$。$\Delta t$ 越小，平均速度越接近 $t_0$ 时刻的瞬时速度；若极限

$$
\lim_{\Delta t\to 0}\frac{x(t_0+\Delta t)-x(t_0)}{\Delta t}
$$

存在，它就是质点在 $t_0$ 时刻的瞬时速度。

引例 2（切线）：设曲线 $L$ 为 $y = f(x)$ 的图形，$M(x_0, y_0)$ 是 $L$ 上一点。在 $M$ 附近取 $L$ 上的点 $Q(x_0+\Delta x, y_0+\Delta y)$，割线 $MQ$ 的斜率为 $\frac{\Delta y}{\Delta x}$。当 $\Delta x \to 0$ 时 $Q$ 沿曲线趋于 $M$，若割线 $MQ$ 趋于一个极限位置 $MT$，就称直线 $MT$ 为 $L$ 在 $M$ 点的切线，其斜率为

$$
\lim_{\Delta x\to 0}\frac{\Delta y}{\Delta x} = \lim_{\Delta x\to 0}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}.
$$

![Δx 逐渐减小时，割线 MQ 的斜率趋于切线斜率 f′(x₀)](./plots/secant-to-tangent.py)

两个引例归结为同一种极限：函数增量与自变量增量之比在自变量增量趋于零时的极限。下面设函数在 $x_0$ 的某个**邻域**内有定义。

**定义 4.1.1（导数）** 设 $y = f(x)$ 在 $x_0$ 及其附近有定义。若极限

$$
\lim_{\Delta x\to 0}\frac{\Delta y}{\Delta x}=\lim_{\Delta x\to 0}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}
$$
存在，则称 $f$ 在 $x_0$ 点**可导**，并称此极限为 $f$ 在 $x_0$ 点的**导数**，记作 $f'(x_0)$、$\frac{\mathrm{d}f}{\mathrm{d}x}\big|_{x=x_0}$ 或 $\frac{\mathrm{d}f(x_0)}{\mathrm{d}x}$；否则称 $f$ 在 $x_0$ 点不可导。

令 $x = x_0 + \Delta x$，得到导数的等价形式

$$
f'(x_0) = \lim_{x\to x_0}\frac{f(x)-f(x_0)}{x-x_0}.
$$

若 $f$ 在区间 $I$ 的每一点都可导（端点处指单侧导数，见下文），则称 $f$ 在 $I$ 上可导，$x \mapsto f'(x)$ 是 $I$ 上的函数，称为 $f$ 的导函数，简称导数。若 $f'$ 还在 $I$ 上连续，则称 $f$ 在 $I$ 上连续可导，记作 $f \in C^1(I)$。

若上述极限为 $+\infty$ 或 $-\infty$（或 $\infty$），$f$ 在 $x_0$ 不可导，但为书写方便也记 $f'(x_0) = \infty$，此时切线是竖直的。

导数的几何意义：若 $f$ 在 $x_0$ 可导，$f'(x_0)$ 就是曲线 $y = f(x)$ 在 $M(x_0, y_0)$ 处切线的斜率。

**定义 4.1.2** 设曲线 $L\colon y=f(x)$ 过点 $M(x_0,y_0)$。若 $f'(x_0)$ 存在，称直线 $y - y_0 = f'(x_0)(x - x_0)$ 为 $L$ 在 $M$ 点的**切线**；若 $f'(x_0) = \infty$，切线为 $x = x_0$。过 $M$ 且与切线垂直的直线称为 $L$ 在 $M$ 点的**法线**：

$$
y - y_0 = -\frac{1}{f'(x_0)}(x - x_0)\ \ (f'(x_0)\ne 0),\qquad y = y_0\ \ (f'(x_0)=\infty),\qquad x = x_0\ \ (f'(x_0)=0).
$$

**例 4.1.1** 设 $f'(x_0) = A$，求 (1) $\lim\limits_{h\to 0}\frac{f(x_0+3h)-f(x_0)}{h}$；(2) $\lim\limits_{h\to 0}\frac{f(x_0+2h)-f(x_0-h)}{h}$。

解：关键是把分子凑成"同一增量"的差商。(1) $\lim\limits_{h\to0} 3\cdot\frac{f(x_0+3h)-f(x_0)}{3h} = 3A$。(2) 在分子中减去再加上 $f(x_0)$：

$$
\lim_{h\to0}\frac{f(x_0+2h)-f(x_0)}{h} - \lim_{h\to0}\frac{f(x_0-h)-f(x_0)}{h} = 2\lim_{h\to0}\frac{f(x_0+2h)-f(x_0)}{2h} + \lim_{h\to0}\frac{f(x_0-h)-f(x_0)}{-h} = 2A + A = 3A.
$$

注意 (2) 用到了 $f'(x_0)$ 存在；只假设对称差商 $\frac{f(x_0+h)-f(x_0-h)}{2h}$ 有极限并不能推出可导（如 $|x|$ 在 $0$ 点）。

**例 4.1.2** 设 $f(x) = \frac{1-\cos x}{x}$（$x \ne 0$），$f(0) = 0$，求 $f'(0)$。

解：$f'(0) = \lim\limits_{x\to0}\frac{f(x)-f(0)}{x-0} = \lim\limits_{x\to0}\frac{1-\cos x}{x^2} = \frac12$（**等价无穷小** $1-\cos x \sim \frac{x^2}{2}$）。

**定义 4.1.3（单侧导数）** 设 $f$ 在 $x_0$ 及其左侧（右侧）附近有定义。若极限

$$
f'_-(x_0) = \lim_{\Delta x\to 0^-}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}\qquad\Bigl(f'_+(x_0) = \lim_{\Delta x\to 0^+}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}\Bigr)
$$
存在，则称之为 $f$ 在 $x_0$ 点的**左导数**（**右导数**）。

由**单侧极限**与极限的关系立即得到：

**定理 4.1.1** $f$ 在 $x_0$ 点可导 $\iff$ $f$ 在 $x_0$ 点的左导数与右导数都存在且相等。

**例 4.1.3** $y = |x|$ 在 $0$ 点：$\lim\limits_{x\to0^-}\frac{|x|}{x} = -1$，$\lim\limits_{x\to0^+}\frac{|x|}{x} = 1$，左、右导数存在但不相等，故 $|x|$ 在 $0$ 点不可导。图形在 $0$ 点有一个"角"，称为角点。$y=\sqrt{|x|}$ 在 $0$ 点的左、右导数分别为 $-\infty$ 与 $+\infty$，图形在此处形成尖点。

**定理 4.1.2（可导必连续）** 若 $f$ 在 $x_0$ 点可导，则 $f$ 在 $x_0$ 点连续。

**证明** 由 $\lim\limits_{\Delta x\to0}\frac{\Delta y}{\Delta x} = f'(x_0)$ 得 $\lim\limits_{\Delta x\to0}\frac{\Delta y - f'(x_0)\Delta x}{\Delta x} = 0$，即

$$
\Delta y = f'(x_0)\Delta x + o(\Delta x)\qquad(\Delta x\to0). \tag{4.1}
$$

于是 $\Delta x \to 0$ 时 $\Delta y \to 0$，$f$ 在 $x_0$ 点连续。 $\square$

逆命题不成立：$|x|$ 在 $0$ 点连续而不可导（例 4.1.3）。甚至存在处处连续、处处不可导的函数（Weierstrass 构造的 $\sum_n a^n\cos(b^n\pi x)$），所以连续远比可导弱。式 (4.1) 将在 4.5 节中成为微分的定义。

### 4.1.2. 求导举例

**例 4.1.4（部分基本初等函数的导数）** 证明：(1) $c' = 0$（$c$ 为常数）；(2) $(\sin x)' = \cos x$；(3) $(\cos x)' = -\sin x$；(4) $(a^x)' = a^x\ln a$，特别地 $(\mathrm{e}^x)' = \mathrm{e}^x$；(5) $(\log_a x)' = \frac{1}{x\ln a}$，特别地 $(\ln x)' = \frac1x$。

**证明** (1) 显然。(2) 由和差化积，

$$
(\sin x)' = \lim_{\Delta x\to0}\frac{2\cos\bigl(x+\frac{\Delta x}{2}\bigr)\sin\frac{\Delta x}{2}}{\Delta x} = \lim_{\Delta x\to0}\cos\Bigl(x+\frac{\Delta x}{2}\Bigr)\cdot\frac{\sin(\Delta x/2)}{\Delta x/2} = \cos x,
$$

这里用了 $\cos$ 的连续性与 $\lim\limits_{t\to0}\frac{\sin t}{t} = 1$。(3) 同理。(4) 由 $a^{\Delta x} - 1 \sim \Delta x\ln a$，

$$
(a^x)' = \lim_{\Delta x\to0}\frac{a^x(a^{\Delta x}-1)}{\Delta x} = a^x\ln a.
$$

(5) 由 $\ln(1+u)\sim u$，

$$
(\log_a x)' = \lim_{\Delta x\to0}\frac{\log_a\bigl(1+\frac{\Delta x}{x}\bigr)}{\Delta x} = \lim_{\Delta x\to0}\frac{\ln\bigl(1+\frac{\Delta x}{x}\bigr)}{\Delta x\,\ln a} = \frac{1}{x\ln a}. \qquad\square
$$

**例 4.1.5** 求曲线 $y = \sqrt[3]{x}$ 在 $x = 1$ 与 $x = 0$ 对应点处的切线方程。

解：在 $x = 1$ 处，$y'(1) = \lim\limits_{\Delta x\to0}\frac{(1+\Delta x)^{1/3}-1}{\Delta x} = \frac13$（$(1+u)^{1/3}-1\sim\frac u3$），切线为 $y - 1 = \frac13(x-1)$。在 $x = 0$ 处，$\lim\limits_{\Delta x\to0}\frac{(\Delta x)^{1/3}}{\Delta x} = +\infty$，$\sqrt[3]{x}$ 在 $0$ 点不可导，但切线存在，为竖直线 $x = 0$。

**例 4.1.6** 设 $f(x) = x^2\sin\frac1x$（$x\ne0$），$f(0)=0$。则 $f'(0) = \lim\limits_{x\to0}x\sin\frac1x = 0$；$x\ne0$ 时 $f'(x) = 2x\sin\frac1x - \cos\frac1x$，它在 $x\to0$ 时没有极限。所以 $f$ 在 $\mathbb{R}$ 上处处可导，但导函数在 $0$ 点不连续（是**第二类间断点**）：可导函数的导数未必连续，$C^1$ 是比"可导"更强的条件。

![左：x² sin(1/x) 夹在 ±x² 之间，在 0 点的切线是 y = 0；右：它的导函数在 0 附近在 −1 与 1 之间无限振荡，在 0 点没有极限](./plots/x2-sin-inverse-x.py)

## 4.2. 导数的运算法则

### 4.2.1. 导数的四则运算

**定理 4.2.1** 设 $f$ 与 $g$ 都在点 $x$ 可导，则

1. $(cf)' = cf'$（$c$ 为常数），$(f+g)' = f'+g'$；
2. $(fg)' = f'g + fg'$，更一般地 $(f_1f_2\cdots f_n)' = f_1'f_2\cdots f_n + f_1f_2'\cdots f_n + \cdots + f_1f_2\cdots f_n'$；
3. 若 $g(x)\ne0$，则 $\bigl(\frac1g\bigr)' = -\frac{g'}{g^2}$，$\bigl(\frac fg\bigr)' = \frac{f'g-fg'}{g^2}$。

**证明** 2. 在分子中减去再加上 $f(x)g(x+\Delta x)$：

$$
(fg)' = \lim_{\Delta x\to0}\Bigl[\frac{f(x+\Delta x)-f(x)}{\Delta x}\,g(x+\Delta x) + f(x)\,\frac{g(x+\Delta x)-g(x)}{\Delta x}\Bigr] = f'g+fg',
$$

其中 $g(x+\Delta x)\to g(x)$ 用到了可导必连续（定理 4.1.2）。

3. 
$$
\Bigl(\frac1g\Bigr)' = \lim_{\Delta x\to0}\frac{1}{\Delta x}\Bigl(\frac{1}{g(x+\Delta x)}-\frac1{g(x)}\Bigr) = \lim_{\Delta x\to0}\Bigl(-\frac{g(x+\Delta x)-g(x)}{\Delta x}\Bigr)\frac{1}{g(x+\Delta x)g(x)} = -\frac{g'}{g^2}.
$$

再由 2 得 $\bigl(\frac fg\bigr)' = f'\cdot\frac1g + f\cdot\bigl(-\frac{g'}{g^2}\bigr) = \frac{f'g-fg'}{g^2}$。 $\square$

1 说明求导是线性运算：可导函数全体构成**向量空间**，求导是其上的**线性映射**。

**例 4.2.1** 由商的法则，

$$
(\tan x)' = \frac{\cos^2x+\sin^2x}{\cos^2x} = \sec^2x,\quad (\cot x)' = -\csc^2x,\quad (\sec x)' = \frac{\sin x}{\cos^2x} = \sec x\tan x,\quad (\csc x)' = -\csc x\cot x.
$$

### 4.2.2. 复合函数的求导法则

**定理 4.2.2（链式法则）** 设 $u = u(x)$ 在 $x_0$ 点可导，$y = y(u)$ 在 $u_0 = u(x_0)$ 点可导，则**复合函数** $y = y(u(x))$ 在 $x_0$ 点可导，并且

$$
(y\circ u)'(x_0) = y'(u_0)\,u'(x_0),\qquad\text{即}\quad \frac{\mathrm{d}y}{\mathrm{d}x}\Big|_{x=x_0} = \frac{\mathrm{d}y}{\mathrm{d}u}\Big|_{u=u_0}\cdot\frac{\mathrm{d}u}{\mathrm{d}x}\Big|_{x=x_0}.
$$

**证明** 由 $y$ 在 $u_0$ 可导，令 $\alpha(\Delta u) = \frac{y(u_0+\Delta u)-y(u_0)}{\Delta u} - y'(u_0)$（$\Delta u\ne0$），$\alpha(0) = 0$，则 $\alpha$ 在 $0$ 点连续，并且对一切 $\Delta u$（包括 $\Delta u = 0$）有

$$
\Delta y = y(u_0+\Delta u)-y(u_0) = \bigl(y'(u_0)+\alpha(\Delta u)\bigr)\Delta u.
$$

给 $x$ 增量 $\Delta x\ne0$，令 $\Delta u = u(x_0+\Delta x)-u(x_0)$，则 $\frac{\Delta y}{\Delta x} = \bigl(y'(u_0)+\alpha(\Delta u)\bigr)\frac{\Delta u}{\Delta x}$。$\Delta x\to0$ 时，由 $u$ 的连续性 $\Delta u\to0$，故 $\alpha(\Delta u)\to0$，而 $\frac{\Delta u}{\Delta x}\to u'(x_0)$，所以 $\frac{\Delta y}{\Delta x}\to y'(u_0)u'(x_0)$。 $\square$

（直接写 $\Delta y = y'(u_0)\Delta u + o(\Delta u)$ 再除以 $\Delta x$ 也可以，但要说明 $\Delta u$ 可能为零时 $o(\Delta u)/\Delta x \to 0$ 仍成立；引入 $\alpha$ 正是为了处理这一点。）

链式法则可以记成 $y\to u\to x$：沿着复合的链条逐层求导再相乘。

**例 4.2.2** 求导数：(1) $y = x^\alpha$（$x>0$，$\alpha\in\mathbb{R}$）；(2) $y = \cos(5x^2+2x+3)$；(3) $y = \bigl(\frac{x+1}{x-1}\bigr)^{3/2}$；(4) $y = \ln\bigl(x+\sqrt{x^2+a^2}\bigr)$。

解：(1) $y = \mathrm{e}^{\alpha\ln x}$，$y' = \mathrm{e}^{\alpha\ln x}\cdot\frac{\alpha}{x} = \alpha x^{\alpha-1}$。

(2) 令 $u = 5x^2+2x+3$，$y' = -\sin u\cdot(10x+2) = -(10x+2)\sin(5x^2+2x+3)$。

(3) 令 $u = \frac{x+1}{x-1}$，$y' = \frac32u^{1/2}\cdot\frac{-2}{(x-1)^2} = -\frac{3(x+1)^{1/2}}{(x-1)^{5/2}}$。

(4) 
$$
y' = \frac{1}{x+\sqrt{x^2+a^2}}\Bigl(1+\frac{x}{\sqrt{x^2+a^2}}\Bigr) = \frac{1}{\sqrt{x^2+a^2}}.
$$

**例 4.2.3** 证明 $(\ln|x|)' = \frac1x$（$x\ne0$）。

**证明** $x>0$ 时即 $(\ln x)' = \frac1x$。$x<0$ 时 $(\ln|x|)' = (\ln(-x))' = \frac{-1}{-x} = \frac1x$。 $\square$

### 4.2.3. 反函数求导法则

**定理 4.2.3** 设 $y = f(x)$ 在 $[a,b]$ 上严格单调且连续，$x_0\in(a,b)$，$f'(x_0)$ 存在且不等于 $0$，则**反函数** $x = f^{-1}(y)$ 在 $y_0 = f(x_0)$ 点可导，并且

$$
(f^{-1})'(y_0) = \frac{1}{f'(x_0)},\qquad\text{即}\quad\frac{\mathrm{d}x}{\mathrm{d}y} = 1\Big/\frac{\mathrm{d}y}{\mathrm{d}x}.
$$

**证明** 严格单调连续函数的反函数也严格单调连续，所以 $y\to y_0 \iff x = f^{-1}(y)\to x_0$，且 $y\ne y_0\iff x\ne x_0$。于是

$$
\lim_{y\to y_0}\frac{f^{-1}(y)-f^{-1}(y_0)}{y-y_0} = \lim_{x\to x_0}\frac{x-x_0}{f(x)-f(x_0)} = \frac1{f'(x_0)}. \qquad\square
$$

几何上，$y=f(x)$ 与 $x = f^{-1}(y)$ 是同一条曲线，切线斜率分别对 $x$ 轴与 $y$ 轴计量，所以互为倒数。若把反函数也写成以 $x$ 为自变量的 $y = f^{-1}(x)$，则 $(f^{-1})'(x) = \frac{1}{f'(y)}$，其中 $y = f^{-1}(x)$。

**例 4.2.4（反三角函数的导数）** $y = \arcsin x$（$-1<x<1$）与 $x = \sin y$（$-\frac\pi2<y<\frac\pi2$）互为反函数，$\cos y>0$，故

$$
(\arcsin x)' = \frac{1}{\cos y} = \frac{1}{\sqrt{1-\sin^2y}} = \frac{1}{\sqrt{1-x^2}}.
$$

同理 $(\arccos x)' = -\frac{1}{\sin y} = -\frac{1}{\sqrt{1-x^2}}$（$0<y<\pi$）；$y=\arctan x$ 与 $x = \tan y$ 互为反函数，$(\arctan x)' = \cos^2y = \frac{1}{1+\tan^2y} = \frac1{1+x^2}$；由 $\arctan x+\operatorname{arccot}x = \frac\pi2$ 得 $(\operatorname{arccot}x)' = -\frac{1}{1+x^2}$。

**例 4.2.5** 设 $y = \arctan\frac{\sin x}{\mathrm{e}^x-1}$，求 $y'$。

解：令 $u = \frac{\sin x}{\mathrm{e}^x-1}$，

$$
y' = \frac{1}{1+u^2}\cdot\frac{\cos x\,(\mathrm{e}^x-1)-\mathrm{e}^x\sin x}{(\mathrm{e}^x-1)^2} = \frac{(\cos x-\sin x)\mathrm{e}^x-\cos x}{(\mathrm{e}^x-1)^2+\sin^2x}.
$$

**例 4.2.6** 设 $y = \arcsin(\arctan x)+\log_a\arccos x$，则

$$
y' = \frac{1}{\sqrt{1-\arctan^2x}}\cdot\frac1{1+x^2}+\frac{1}{\arccos x\,\ln a}\cdot\Bigl(-\frac{1}{\sqrt{1-x^2}}\Bigr).
$$

至此，六类基本初等函数的导数都已求出。由四则运算法则与链式法则，任何初等函数在其定义区间内（除个别点外）都可以按公式求导，其导数仍是初等函数。

| 函数 | 导数 | 函数 | 导数 |
|---|---|---|---|
| $c$ | $0$ | $x^\alpha$（$x>0$，$\alpha\in\mathbb{R}$） | $\alpha x^{\alpha-1}$ |
| $a^x$（$a>0$） | $a^x\ln a$ | $\mathrm{e}^x$ | $\mathrm{e}^x$ |
| $\log_a x$ | $\frac{1}{x\ln a}$ | $\ln\lvert x\rvert$ | $\frac1x$ |
| $\sin x$ | $\cos x$ | $\cos x$ | $-\sin x$ |
| $\tan x$ | $\sec^2x$ | $\cot x$ | $-\csc^2x$ |
| $\sec x$ | $\sec x\tan x$ | $\csc x$ | $-\csc x\cot x$ |
| $\arcsin x$ | $\frac{1}{\sqrt{1-x^2}}$ | $\arccos x$ | $-\frac{1}{\sqrt{1-x^2}}$ |
| $\arctan x$ | $\frac{1}{1+x^2}$ | $\operatorname{arccot} x$ | $-\frac{1}{1+x^2}$ |
| $\sinh x$ | $\cosh x$ | $\cosh x$ | $\sinh x$ |
| $\ln\bigl(x+\sqrt{x^2+a^2}\bigr)$ | $\frac{1}{\sqrt{x^2+a^2}}$ | $\ln\lvert x+\sqrt{x^2-a^2}\rvert$ | $\frac{1}{\sqrt{x^2-a^2}}$ |

最后一行的两个函数在不定积分中经常出现（[2.2.6](/2.2.6)）；**双曲函数**的导数由 $\sinh x = \frac{\mathrm{e}^x-\mathrm{e}^{-x}}2$、$\cosh x = \frac{\mathrm{e}^x+\mathrm{e}^{-x}}2$ 直接求出。

## 4.3. 特殊的求导法则

### 4.3.1. 对数求导法

对乘积、商、幂次很多的函数，或幂指函数 $u(x)^{v(x)}$（$u>0$），先取对数再求导往往更简单，这称为对数求导法（logarithmic differentiation）。对 $y = u(x)^{v(x)}$，

$$
\ln y = v\ln u\ \Longrightarrow\ \frac{y'}{y} = v'\ln u+v\frac{u'}{u}\ \Longrightarrow\ y' = u^{v}\Bigl(v'\ln u+\frac{vu'}{u}\Bigr).
$$

也可以直接写 $y = \mathrm{e}^{v\ln u}$ 再用链式法则，结果相同。

**例 4.3.1** 求导数：(1) $y = x^{\sin x}$；(2) $y = (x^2+1)^{\tan x}$；(3) $y = (\arccos x)^{\arctan x}$。

解：(1) $y' = \bigl(\mathrm{e}^{\sin x\ln x}\bigr)' = x^{\sin x}\bigl(\cos x\ln x+\frac{\sin x}{x}\bigr)$。

(2) $y' = (x^2+1)^{\tan x}\Bigl[\sec^2x\,\ln(x^2+1)+\frac{2x\tan x}{x^2+1}\Bigr]$。

(3) 
$$
y' = (\arccos x)^{\arctan x}\Bigl[\frac{\ln\arccos x}{1+x^2}-\frac{\arctan x}{\arccos x\,\sqrt{1-x^2}}\Bigr].
$$

对多个因子的乘积 $y = f_1f_2\cdots f_n$，$\frac{y'}{y} = (\ln|y|)' = \frac{f_1'}{f_1}+\cdots+\frac{f_n'}{f_n}$（在各因子不为零处），这正是乘积法则的另一种写法。

**例 4.3.2** 设 $y = \frac{\mathrm{e}^{-x+1}}{\sqrt[3]{2x-1}\,(4x^2+1)}$（$x\ne\frac12$），求 $y'$。

解：$\ln|y| = (-x+1)-\frac13\ln|2x-1|-\ln(4x^2+1)$，两边求导：

$$
\frac{y'}{y} = -1-\frac{2}{3(2x-1)}-\frac{8x}{4x^2+1},\qquad y' = -\frac{\mathrm{e}^{-x+1}}{\sqrt[3]{2x-1}\,(4x^2+1)}\Bigl(1+\frac{2}{3(2x-1)}+\frac{8x}{4x^2+1}\Bigr).
$$

### 4.3.2. 参数方程确定的函数的导数

设 $y$ 是 $x$ 的函数，由参数方程 $x = \varphi(t)$、$y = \psi(t)$ 确定。若 $\varphi,\psi$ 可导，$\varphi'(t)\ne0$（于是 $x=\varphi(t)$ 在局部有可导的反函数 $t = \varphi^{-1}(x)$，$y = \psi(\varphi^{-1}(x))$），则由链式法则与反函数求导法则

$$
\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{\mathrm{d}y}{\mathrm{d}t}\cdot\frac{\mathrm{d}t}{\mathrm{d}x} = \frac{\psi'(t)}{\varphi'(t)}.
$$

以后对参数方程求导，都默认 $\frac{\mathrm{d}x}{\mathrm{d}t}\ne0$；在 $\varphi'(t)=0$、$\psi'(t)\ne0$ 的点，切线是竖直的。

**例 4.3.3** 求椭圆 $x = a\cos\theta$，$y = b\sin\theta$（$0\le\theta<2\pi$）上任意点的切线方程。

解：$\theta\ne0,\pi$ 时 $\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{b\cos\theta}{-a\sin\theta} = -\frac ba\cot\theta$，切线为 $y - b\sin\theta = -\frac ba\cot\theta\,(x-a\cos\theta)$，整理得 $\frac{x\cos\theta}{a}+\frac{y\sin\theta}{b} = 1$。$\theta = 0,\pi$ 时 $\frac{\mathrm{d}y}{\mathrm{d}x} = \infty$，切线分别为 $x = a$ 与 $x = -a$，也符合上式。

### 4.3.3. 隐函数求导

形如 $y = f(x)$ 的函数称为显函数。若 $x, y$ 的关系由方程 $F(x,y) = 0$ 确定，称 $y = y(x)$ 为该方程确定的**隐函数**。隐函数的存在性与可导性要用多元微分学（**隐函数定理**，[2.2.10](/2.2.10)），这里假定隐函数存在且可导，只讨论怎样求导：在方程两边对 $x$ 求导，把 $y$ 看成 $x$ 的函数（对含 $y$ 的项用链式法则），再解出 $y'$。这称为隐函数求导（implicit differentiation）。

**例 4.3.4** 设 $y = y(x)$ 由方程 $\mathrm{e}^{xy}+\sin(x+y) = 0$ 确定，求 $\frac{\mathrm{d}y}{\mathrm{d}x}$。

解：两边对 $x$ 求导：$\mathrm{e}^{xy}(y+xy')+\cos(x+y)(1+y') = 0$，所以

$$
y' = -\frac{y\,\mathrm{e}^{xy}+\cos(x+y)}{x\,\mathrm{e}^{xy}+\cos(x+y)}.
$$

**例 4.3.5** 曲线 $L\colon y^3+y^2 = 2x^2$，求 $L$ 在点 $(1,1)$ 处的切线方程。

解：两边对 $x$ 求导：$3y^2y'+2yy' = 4x$，$y' = \frac{4x}{3y^2+2y}$。在 $(1,1)$ 处 $y' = \frac45$，切线为 $y - 1 = \frac45(x-1)$。

## 4.4. 高阶导数

**定义 4.4.1（高阶导数）** 设 $f$ 在区间 $I$ 上可导。若导函数 $f'$ 在 $I$ 上仍可导，称 $(f')'$ 为 $f$ 的**二阶导数**，记作 $f''(x)$ 或 $\frac{\mathrm{d}^2f}{\mathrm{d}x^2}$。依次可定义三阶导数 $f'''$ 以及 $n$ 阶导数 $f^{(n)}(x) = \frac{\mathrm{d}^nf}{\mathrm{d}x^n}$，约定 $f^{(0)} = f$。二阶及二阶以上的导数统称**高阶导数**。

记号：$f\in C^n(I)$ 表示 $f$ 在 $I$ 上有 $n$ 阶连续导数，也称 $f$ 在 $I$ 上 $n$ 阶连续可导；$f\in C^\infty(I)$ 表示 $f$ 有任意阶导数，也称 $f$ 光滑。物理上，位置对时间的二阶导数就是加速度。

**例 4.4.1** 设 $f(x) = x^4\cos\frac1x$（$x\ne0$），$f(0) = 0$，求 $f''(0)$。

解：$f'(0) = \lim\limits_{x\to0}x^3\cos\frac1x = 0$，$x\ne0$ 时 $f'(x) = 4x^3\cos\frac1x+x^2\sin\frac1x$。于是

$$
f''(0) = \lim_{x\to0}\frac{f'(x)-f'(0)}{x} = \lim_{x\to0}\Bigl(4x^2\cos\frac1x+x\sin\frac1x\Bigr) = 0.
$$

在分段点处的高阶导数必须按定义逐阶计算，不能对分段表达式求导后取极限。

**例 4.4.2** $y = \sin x$：$y' = \cos x = \sin\bigl(x+\frac\pi2\bigr)$，$y'' = \sin(x+\pi)$，……，归纳得

$$
(\sin x)^{(n)} = \sin\Bigl(x+\frac{n\pi}{2}\Bigr),\qquad (\cos x)^{(n)} = \cos\Bigl(x+\frac{n\pi}{2}\Bigr),\qquad n\in\mathbb{N}.
$$

**例 4.4.3** $y = \ln x$：$y' = \frac1x$，$y'' = -\frac1{x^2}$，$y''' = \frac{2}{x^3}$，$y^{(4)} = -\frac{2\cdot3}{x^4}$，……，

$$
(\ln x)^{(n)} = (-1)^{n-1}\frac{(n-1)!}{x^n},\qquad \bigl(\ln(ax+b)\bigr)^{(n)} = (-1)^{n-1}\frac{(n-1)!\,a^n}{(ax+b)^n},\qquad \Bigl(\frac1{ax+b}\Bigr)^{(n)} = (-1)^n\frac{n!\,a^n}{(ax+b)^{n+1}}.
$$

第三式由 $\frac1{ax+b} = \frac1a\bigl(\ln(ax+b)\bigr)'$ 得到。

**定理 4.4.1** 设 $f, g$ 有 $n$ 阶导数，$a, b$ 为常数，则 $(af+bg)^{(n)} = af^{(n)}+bg^{(n)}$。

**定理 4.4.2（Leibniz 公式）** 设 $f, g$ 有 $n$ 阶导数，则

$$
(fg)^{(n)} = \sum_{k=0}^{n}\binom nk f^{(k)}g^{(n-k)}.
$$

**证明** 对 $n$ 归纳。$n = 1$ 即乘积法则。设 $n = m$ 时成立，两边求导：

$$
(fg)^{(m+1)} = \sum_{k=0}^m\binom mk\bigl(f^{(k+1)}g^{(m-k)}+f^{(k)}g^{(m-k+1)}\bigr) = \sum_{k=0}^{m+1}\Bigl[\binom m{k-1}+\binom mk\Bigr]f^{(k)}g^{(m+1-k)},
$$

其中约定 $\binom m{-1} = \binom m{m+1} = 0$。由 $\binom m{k-1}+\binom mk = \binom{m+1}k$，$n = m+1$ 时成立。 $\square$

公式的形式与二项式定理 $(a+b)^n = \sum\binom nka^kb^{n-k}$ 完全相同。当一个因子是低次多项式时，求和中只有前几项不为零，最为实用。

**例 4.4.4** 设 $y = \frac{x^2-2}{x^2-x-2}$，求 $y^{(n)}$。

解：先做带余除法并分解成**部分分式**（见定理 6.4.1）：

$$
y = 1+\frac{x}{(x-2)(x+1)} = 1+\frac23\cdot\frac{1}{x-2}+\frac13\cdot\frac1{x+1}.
$$

由例 4.4.3，

$$
y^{(n)} = (-1)^n n!\Bigl[\frac{2}{3(x-2)^{n+1}}+\frac{1}{3(x+1)^{n+1}}\Bigr],\qquad n\ge1.
$$

**例 4.4.5** 设 $y = x^2\sin x$，求 $y^{(20)}$。

解：$(x^2)^{(k)} = 0$（$k\ge3$），由 Leibniz 公式与例 4.4.2，

$$
y^{(20)} = x^2\sin(x+10\pi)+\binom{20}{1}2x\sin\Bigl(x+\frac{19\pi}2\Bigr)+\binom{20}22\sin(x+9\pi) = x^2\sin x-40x\cos x-380\sin x.
$$

**例 4.4.6** 设 $y = \frac{\ln x}{x}$，求 $y^{(n)}$。

解：由 Leibniz 公式，取 $f = \ln x$，$g = \frac1x$：

$$
y^{(n)} = \ln x\cdot\Bigl(\frac1x\Bigr)^{(n)}+\sum_{k=1}^n\binom nk(\ln x)^{(k)}\Bigl(\frac1x\Bigr)^{(n-k)} = \frac{(-1)^nn!}{x^{n+1}}\ln x+\sum_{k=1}^n\binom nk\frac{(-1)^{k-1}(k-1)!}{x^k}\cdot\frac{(-1)^{n-k}(n-k)!}{x^{n-k+1}}.
$$

由 $\binom nk(k-1)!(n-k)! = \frac{n!}{k}$，后一和式为 $\frac{(-1)^{n-1}n!}{x^{n+1}}\sum_{k=1}^n\frac1k$，故

$$
\Bigl(\frac{\ln x}{x}\Bigr)^{(n)} = \frac{(-1)^nn!}{x^{n+1}}\Bigl(\ln x-\sum_{k=1}^n\frac1k\Bigr).
$$

参数方程的二阶导数。设 $x = \varphi(t)$，$y = \psi(t)$ 二阶可导，$\varphi'\ne0$。$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{\psi'(t)}{\varphi'(t)}$ 仍是 $t$ 的函数，再对 $x$ 求导时要乘以 $\frac{\mathrm{d}t}{\mathrm{d}x} = \frac1{\varphi'(t)}$：

$$
\frac{\mathrm{d}^2y}{\mathrm{d}x^2} = \frac{\mathrm{d}}{\mathrm{d}t}\Bigl(\frac{\psi'}{\varphi'}\Bigr)\cdot\frac{1}{\varphi'} = \frac{\varphi'\psi''-\psi'\varphi''}{\varphi'^3}.
$$

**例 4.4.7** 设 $x = a\cos^3t$，$y = a\sin^3t$（星形线），求 $\frac{\mathrm{d}y}{\mathrm{d}x}$ 与 $\frac{\mathrm{d}^2y}{\mathrm{d}x^2}$。

解：$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{3a\sin^2t\cos t}{-3a\cos^2t\sin t} = -\tan t$，

$$
\frac{\mathrm{d}^2y}{\mathrm{d}x^2} = \frac{\mathrm{d}(-\tan t)}{\mathrm{d}t}\cdot\frac{\mathrm{d}t}{\mathrm{d}x} = -\sec^2t\cdot\frac{1}{-3a\cos^2t\sin t} = \frac{1}{3a\cos^4t\sin t}.
$$

**例 4.4.8** 设 $y = y(x)$ 由方程 $\mathrm{e}^y-xy = 0$ 确定，求 $\frac{\mathrm{d}^2y}{\mathrm{d}x^2}$。

解：两边对 $x$ 求导：$\mathrm{e}^yy'-y-xy' = 0$，$y' = \frac{y}{\mathrm{e}^y-x}$。再求导（$y'$ 中的 $y$ 仍是 $x$ 的函数）：

$$
y'' = \frac{y'(\mathrm{e}^y-x)-y(\mathrm{e}^yy'-1)}{(\mathrm{e}^y-x)^2} = \frac{2y(\mathrm{e}^y-x)-y^2\mathrm{e}^y}{(\mathrm{e}^y-x)^3},
$$

最后一步代入了 $y' = \frac{y}{\mathrm{e}^y-x}$。

反函数的二阶导数。设 $y = f(x)$ 二阶可导，$f'\ne0$，$x = g(y)$ 为其反函数。对恒等式 $f(g(y)) = y$ 求导两次：$f'(g(y))g'(y) = 1$，$f''(g(y))g'(y)^2+f'(g(y))g''(y) = 0$，所以

$$
g'(y) = \frac{1}{f'(x)},\qquad g''(y) = -\frac{f''(x)}{f'(x)^3},\qquad x = g(y).
$$

**例 4.4.9** 设 $y = \mathrm{e}^x+x+1$，$x = g(y)$ 为其反函数，求 $g'(2)$ 与 $g''(2)$。

解：$y = 2$ 时 $x = 0$。$g'(y) = \frac{1}{\mathrm{e}^x+1}$，$g'(2) = \frac12$；$g''(y) = -\frac{\mathrm{e}^x}{(\mathrm{e}^x+1)^3}$，$g''(2) = -\frac18$。

## 4.5. 微分

### 4.5.1. 微分的概念

给定函数 $y = f(x)$，自变量在 $x_0$ 处的改变量 $\Delta x$ 引起函数的改变量 $\Delta y = f(x_0+\Delta x)-f(x_0)$。一般而言 $\Delta y$ 与 $\Delta x$ 的关系很复杂；最简单的关系是线性关系，或者近似的线性关系。

**定义 4.5.1（微分）** 若存在与 $\Delta x$ 无关的常数 $a$，使得 $\Delta x\to0$ 时

$$
\Delta y = f(x_0+\Delta x)-f(x_0) = a\,\Delta x+o(\Delta x),
$$
则称 $f$ 在 $x_0$ 点**可微**，称线性主部 $a\,\Delta x$ 为 $f$ 在 $x_0$ 点的**微分**，记作 $\mathrm{d}f(x_0) = a\,\Delta x$。

**定理 4.5.1** $f$ 在 $x_0$ 点可微 $\iff$ $f$ 在 $x_0$ 点可导，并且 $\mathrm{d}f(x_0) = f'(x_0)\Delta x$。

**证明** 若 $f$ 在 $x_0$ 可微，$\Delta y = a\Delta x+o(\Delta x)$，则 $\frac{\Delta y}{\Delta x} = a+\frac{o(\Delta x)}{\Delta x}\to a$，即 $f'(x_0) = a$。反之，若 $f$ 在 $x_0$ 可导，由式 (4.1)，$\Delta y = f'(x_0)\Delta x+o(\Delta x)$，故可微且 $\mathrm{d}f(x_0) = f'(x_0)\Delta x$。 $\square$

对自变量 $y = x$ 本身，$\mathrm{d}x = 1\cdot\Delta x$，即自变量的微分就是它的增量。所以微分常写成 $\mathrm{d}y = f'(x)\,\mathrm{d}x$，导数就是两个微分之商 $f'(x) = \frac{\mathrm{d}y}{\mathrm{d}x}$，因此导数也称微商。习惯上，表示一个具体的小数值（如 $0.01$）时用 $\Delta x$，表示形式上的线性主部时用 $\mathrm{d}x$。

一元函数的可导与可微是等价的，但两者是不同的概念：可微讨论增量 $\Delta y$ 与 $\Delta x$ 之间是否近似为线性关系；可导讨论增量之比的极限。到多元函数时两者不再等价（[2.2.10](/2.2.10)），可微才是"好"的概念。

**例 4.5.1** $\mathrm{d}\cos x = -\sin x\,\mathrm{d}x$，$\mathrm{d}\ln x = \frac{\mathrm{d}x}{x}$，$\mathrm{d}a^x = a^x\ln a\,\mathrm{d}x$。

微分的几何解释。设曲线 $y = f(x)$ 在 $x_0$ 可微。自变量有增量 $\Delta x$ 时，$\Delta y$ 是曲线上纵坐标的增量，而 $\mathrm{d}y = f'(x_0)\Delta x$ 恰好是切线 $y = y_0+f'(x_0)(x-x_0)$ 上纵坐标的增量，两者之差是 $\Delta x$ 的高阶无穷小。用微分代替增量，就是在 $x_0$ 的局部用切线代替曲线（局部线性化）。

![Δy 是曲线上纵坐标的增量，dy = f'(x₀)Δx 是切线上纵坐标的增量，两者相差 o(Δx)](./plots/differential-vs-increment.py)

### 4.5.2. 用微分做近似计算

由 $\Delta y = f'(x_0)\Delta x+o(\Delta x)$，当 $|x-x_0|$ 很小时

$$
f(x)\approx f(x_0)+f'(x_0)(x-x_0).
$$

**例 4.5.2** 用微分求 $\sqrt{1.02}$ 的近似值。

解：取 $f(x) = \sqrt x$，$x_0 = 1$，$f'(x) = \frac{1}{2\sqrt x}$，$\sqrt{1.02}\approx1+\frac12\times0.02 = 1.01$（准确值 $1.00995\cdots$）。

选取 $x_0$ 时要兼顾两点：$x_0$ 离 $x$ 足够近，且 $f(x_0)$、$f'(x_0)$ 容易计算。这种近似有两个不足：(1) 合适的 $x_0$ 不一定好找；(2) 精度不高，而且没有给出误差估计。用高阶导数改进它，就得到下一章的 Taylor 公式（[2.2.5](/2.2.5)）。

### 4.5.3. 微分的运算法则

由 $\mathrm{d}f = f'\,\mathrm{d}x$ 与导数的运算法则，立即得到微分的四则运算法则：设 $u, v$ 可微，$c$ 为常数，则

$$
\mathrm{d}(cu) = c\,\mathrm{d}u,\quad \mathrm{d}(u\pm v) = \mathrm{d}u\pm\mathrm{d}v,\quad \mathrm{d}(uv) = v\,\mathrm{d}u+u\,\mathrm{d}v,\quad \mathrm{d}\Bigl(\frac uv\Bigr) = \frac{v\,\mathrm{d}u-u\,\mathrm{d}v}{v^2}\ (v\ne0).
$$

例如 $\mathrm{d}(uv) = (uv)'\,\mathrm{d}x = (u'v+uv')\,\mathrm{d}x = v\,\mathrm{d}u+u\,\mathrm{d}v$。

复合函数的微分。若 $y = y(u)$，$u = u(x)$ 都可导，则 $\mathrm{d}y = \frac{\mathrm{d}y}{\mathrm{d}x}\mathrm{d}x = \frac{\mathrm{d}y}{\mathrm{d}u}\frac{\mathrm{d}u}{\mathrm{d}x}\mathrm{d}x = \frac{\mathrm{d}y}{\mathrm{d}u}\mathrm{d}u$。也就是说，无论 $u$ 是自变量还是中间变量，都有

$$
\mathrm{d}y = y'(u)\,\mathrm{d}u.
$$

这称为一阶微分形式不变性（invariance of the first differential）。它使得求微分时可以把中间变量当作自变量处理，例如 $\mathrm{d}\,\mathrm{e}^{\sin x} = \mathrm{e}^{\sin x}\,\mathrm{d}\sin x = \mathrm{e}^{\sin x}\cos x\,\mathrm{d}x$；它也是 [2.2.6](/2.2.6) 中"凑微分"（第一换元法）的依据。对隐函数，也可以直接对方程两边取微分：由 $y^3+y^2 = 2x^2$ 得 $(3y^2+2y)\,\mathrm{d}y = 4x\,\mathrm{d}x$，与例 4.3.5 的结果一致。高阶微分没有这种不变性：$x$ 是自变量时 $\mathrm{d}^2y = y''\,\mathrm{d}x^2$，$x$ 是中间变量时还多出一项 $y'\,\mathrm{d}^2x$。

**例 4.5.3** 设 $f$ 在 $x_0$ 点可导，数列 $\{x_n\}$、$\{y_n\}$ 满足 $x_n<x_0<y_n$，$x_n\to x_0$，$y_n\to x_0$，求 $\lim\limits_{n\to\infty}\frac{f(y_n)-f(x_n)}{y_n-x_n}$。

解：由可微性，$f(y_n) = f(x_0)+f'(x_0)(y_n-x_0)+o(y_n-x_0)$，$f(x_n) = f(x_0)+f'(x_0)(x_n-x_0)+o(x_n-x_0)$，相减得

$$
\frac{f(y_n)-f(x_n)}{y_n-x_n} = f'(x_0)+\frac{o(y_n-x_0)}{y_n-x_0}\cdot\frac{y_n-x_0}{y_n-x_n}-\frac{o(x_n-x_0)}{x_n-x_0}\cdot\frac{x_n-x_0}{y_n-x_n}.
$$

由于 $0<\frac{y_n-x_0}{y_n-x_n}<1$，$0<\frac{x_0-x_n}{y_n-x_n}<1$ 有界，后两项都趋于 $0$，所以极限为 $f'(x_0)$。条件 $x_n<x_0<y_n$ 不能去掉：例如 $f = x^2\sin\frac1x$（例 4.1.6）在 $0$ 点可导，但取 $x_n,y_n$ 同在 $0$ 的一侧时，割线斜率可以不趋于 $f'(0) = 0$。

## 小结

| 概念或法则 | 内容 |
|---|---|
| 导数 | $f'(x_0) = \lim\limits_{\Delta x\to0}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}$；可导 $\iff$ $f'_-(x_0) = f'_+(x_0)$ |
| 切线与法线 | $y-y_0 = f'(x_0)(x-x_0)$；$y-y_0 = -\frac{1}{f'(x_0)}(x-x_0)$ |
| 可导、可微、连续 | 可微 $\iff$ 可导 $\implies$ 连续，反之不成立（$\lvert x\rvert$）；可导不保证导数连续（$x^2\sin\frac1x$） |
| 四则运算 | $(fg)' = f'g+fg'$，$\bigl(\frac fg\bigr)' = \frac{f'g-fg'}{g^2}$ |
| 链式法则 | $\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{\mathrm{d}y}{\mathrm{d}u}\cdot\frac{\mathrm{d}u}{\mathrm{d}x}$ |
| 反函数 | $\frac{\mathrm{d}x}{\mathrm{d}y} = 1\big/\frac{\mathrm{d}y}{\mathrm{d}x}$，$g'' = -\frac{f''}{f'^3}$ |
| 对数求导 | $(u^v)' = u^v\bigl(v'\ln u+\frac{vu'}{u}\bigr)$ |
| 参数方程 | $\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{\psi'}{\varphi'}$，$\frac{\mathrm{d}^2y}{\mathrm{d}x^2} = \frac{\varphi'\psi''-\psi'\varphi''}{\varphi'^3}$ |
| 隐函数 | 方程两边对 $x$ 求导，$y$ 视为 $x$ 的函数，解出 $y'$ |
| 高阶导数 | $(\sin x)^{(n)} = \sin\bigl(x+\frac{n\pi}2\bigr)$，$\bigl(\frac1{ax+b}\bigr)^{(n)} = \frac{(-1)^nn!\,a^n}{(ax+b)^{n+1}}$，$(fg)^{(n)} = \sum\binom nkf^{(k)}g^{(n-k)}$ |
| 微分 | $\mathrm{d}y = f'(x)\,\mathrm{d}x$，$\Delta y = \mathrm{d}y+o(\Delta x)$；一阶微分形式不变：$\mathrm{d}y = y'(u)\,\mathrm{d}u$ |
| 近似计算 | $f(x)\approx f(x_0)+f'(x_0)(x-x_0)$ |
