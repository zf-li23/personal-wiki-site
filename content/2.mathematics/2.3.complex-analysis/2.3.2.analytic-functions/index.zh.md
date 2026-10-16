---
title: 解析函数
source_hash: 7518d4787793
---

复变函数的导数用与一元微积分相同的差商定义，但增量 $\Delta z$ 现在可以从平面上的任何方向趋于 $0$。要求从所有方向得到同一个极限是一个很强的条件：用实部和虚部 $u,v$ 写出来，就是一对 Cauchy–Riemann 方程。它把 $u$ 与 $v$ 紧紧地联系在一起，使得其中一个在相差常数的意义下决定另一个，而且两者都是调和函数。在开集上处处复可导的函数称为解析函数，它们是整门课程的研究对象。本章给出解析函数的定义和判别解析性的实用方法（Cauchy–Riemann 方程与 Wirtinger 导数 $\partial f/\partial\bar z$），说明怎样由实部重建解析函数，并解释 $f'(z)$ 作为局部旋转与伸缩的几何意义。[2.3.4](/2.3.4) 的积分理论将证明解析函数无穷次可导，[2.3.5](/2.3.5) 将证明它们是幂级数的和。这些判别法所要处理的初等函数 $\mathrm{e}^z$、$\log z$、$\sin z$ 在 [2.3.3](/2.3.3) 中引入，本章的例子只用多项式和有理函数。

## 2.1. 复导数

**定义 2.1.1（复导数）** 设 $f$ 在 $z_0$ 的某个邻域内有定义。若极限

$$
f'(z_0)=\lim_{\Delta z\to0}\frac{f(z_0+\Delta z)-f(z_0)}{\Delta z}
$$
存在（且为有限复数），则称 $f$ 在 $z_0$ 处复可导，$f'(z_0)$ 称为 $f$ 在 $z_0$ 处的**复导数**，也记作 $\frac{\mathrm{d}f}{\mathrm{d}z}(z_0)$。

等价地，$f$ 在 $z_0$ 处复可导且 $f'(z_0)=A$，当且仅当

$$
f(z_0+\Delta z)=f(z_0)+A\,\Delta z+o(|\Delta z|)\qquad(\Delta z\to0). \tag{2.1}
$$

线性部分 $\Delta z\mapsto A\,\Delta z$ 是乘以一个复数。这是与 $\mathbb{R}^2$ 中实可微的本质区别：实可微时线性部分可以是任意 $2\times2$ 实矩阵（§2.2）。与实的情形一样，式 (2.1) 表明复可导蕴含连续，常用的求导法则也成立，证明相同：

$$
(f\pm g)'=f'\pm g',\quad (fg)'=f'g+fg',\quad \Big(\frac fg\Big)'=\frac{f'g-fg'}{g^2}\ (g\ne0),\quad \big(f(g(z))\big)'=f'(g(z))\,g'(z).
$$

若 $f$ 在 $z_0$ 附近复可导、单射、反函数连续，且 $f'(z_0)\ne0$，则在 $w_0=f(z_0)$ 处 $(f^{-1})'(w_0)=1/f'(z_0)$。

**例 2.1.1** 由 $(z+\Delta z)^n-z^n=nz^{n-1}\Delta z+O(|\Delta z|^2)$ 得 $n\ge1$ 时 $(z^n)'=nz^{n-1}$，再由商的求导法则知它对一切 $n\in\mathbb{Z}$ 成立（$n<0$ 时要求 $z\ne0$）。因此多项式处处复可导，有理函数 $P/Q$ 在 $Q\ne0$ 处复可导。

**例 2.1.2** 函数 $f(z)=\bar z$ 连续，但处处不复可导。差商为 $\frac{\overline{\Delta z}}{\Delta z}$：$\Delta z$ 为实数时它等于 $1$，$\Delta z$ 为纯虚数时它等于 $-1$，所以极限不存在。同样的论证表明 $\operatorname{Re}z$、$\operatorname{Im}z$ 和 $|z|$ 处处不复可导。

**例 2.1.3** 函数 $f(z)=|z|^2=z\bar z$ 只在 $0$ 处复可导。在 $z_0$ 处，

$$
\frac{|z_0+\Delta z|^2-|z_0|^2}{\Delta z}=\bar z_0+\overline{\Delta z}+z_0\frac{\overline{\Delta z}}{\Delta z}.
$$

当 $\Delta z\to0$ 时前两项趋于 $\bar z_0$，由例 2.1.2，最后一项只有在 $z_0=0$ 时才有极限。所以 $f'(0)=0$，而 $z_0\ne0$ 时 $f'(z_0)$ 不存在，尽管 $u=x^2+y^2$ 与 $v=0$ 光滑得无可挑剔。

## 2.2. Cauchy–Riemann 方程

### 2.2.1. 定理

设 $f=u+\mathrm{i}v$ 在 $z_0=x_0+\mathrm{i}y_0$ 处复可导。在差商中令 $\Delta z=\Delta x$ 为实数，得 $f'(z_0)=u_x+\mathrm{i}v_x$；令 $\Delta z=\mathrm{i}\Delta y$ 为纯虚数，得 $f'(z_0)=\frac{u_y+\mathrm{i}v_y}{\mathrm{i}}=v_y-\mathrm{i}u_y$（偏导数都在 $(x_0,y_0)$ 处取值）。比较两式得到一个必要条件；加上实可微性，它也是充分的。

**定理 2.2.1（Cauchy–Riemann 方程）** 设 $f=u+\mathrm{i}v$ 在 $z_0=x_0+\mathrm{i}y_0$ 的某个邻域内有定义。则 $f$ 在 $z_0$ 处复可导，当且仅当

1. $u$ 与 $v$ 作为二元实函数在 $(x_0,y_0)$ 处可微（在该点有**全微分**），且
2. 它们在 $(x_0,y_0)$ 处满足 Cauchy–Riemann 方程：

$$
\frac{\partial u}{\partial x}=\frac{\partial v}{\partial y},\qquad \frac{\partial u}{\partial y}=-\frac{\partial v}{\partial x}. \tag{2.2}
$$

此时

$$
f'(z_0)=u_x+\mathrm{i}v_x=v_y-\mathrm{i}u_y=u_x-\mathrm{i}u_y=v_y+\mathrm{i}v_x. \tag{2.3}
$$

**证明** 记 $\Delta z=\Delta x+\mathrm{i}\Delta y$，$f'(z_0)=a+\mathrm{i}b$。

必要性。由式 (2.1)，$\Delta f=(a+\mathrm{i}b)(\Delta x+\mathrm{i}\Delta y)+o(|\Delta z|)$。取实部和虚部，

$$
\Delta u=a\,\Delta x-b\,\Delta y+o(|\Delta z|),\qquad \Delta v=b\,\Delta x+a\,\Delta y+o(|\Delta z|).
$$

所以 $u$ 与 $v$ 在 $(x_0,y_0)$ 处可微，且 $u_x=a$，$u_y=-b$，$v_x=b$，$v_y=a$，这就得到式 (2.2) 和式 (2.3)。

充分性。在 $(x_0,y_0)$ 处令 $a=u_x=v_y$，$b=v_x=-u_y$。由 $u$ 与 $v$ 的可微性，

$$
\Delta u+\mathrm{i}\Delta v=(u_x\Delta x+u_y\Delta y)+\mathrm{i}(v_x\Delta x+v_y\Delta y)+o(|\Delta z|)=(a+\mathrm{i}b)(\Delta x+\mathrm{i}\Delta y)+o(|\Delta z|),
$$

这正是 $A=a+\mathrm{i}b$ 时的式 (2.1)。$\square$

由于偏导数连续蕴含可微（[2.2.10](/2.2.10)），得到实际使用的判别法。

**推论 2.2.1** 若 $u$ 与 $v$ 在开集 $D$ 上有连续的一阶**偏导数**，且在 $D$ 上满足 Cauchy–Riemann 方程，则 $f=u+\mathrm{i}v$ 在 $D$ 的每一点处复可导。

只有 Cauchy–Riemann 方程而没有 $u,v$ 的可微性是不够的：$f(z)=\sqrt{|xy|}$ 在 $0$ 处满足式 (2.2)（四个偏导数在该点都为零），但在 $0$ 处不复可导，因为沿 $z=t(1+\mathrm{i})$，差商为 $\frac{|t|}{t(1+\mathrm{i})}$，没有极限。

### 2.2.2. 矩阵形式与极坐标形式

Cauchy–Riemann 方程是说，映射 $(x,y)\mapsto(u,v)$ 的 **Jacobi 矩阵**具有形式

$$
\begin{bmatrix}u_x&u_y\\v_x&v_y\end{bmatrix}=\begin{bmatrix}a&-b\\b&a\end{bmatrix},\qquad a+\mathrm{i}b=f'(z_0),
$$

这恰好是乘以复数 $a+\mathrm{i}b$ 所对应的实矩阵（[命题 9.1.1](/2.1.9#prop-9.1.1)）。一个实可微映射复可导，当且仅当它的线性近似是旋转再伸缩。特别地，**Jacobi 行列式**为 $u_xv_y-u_yv_x=a^2+b^2=|f'(z_0)|^2\ge0$，所以解析映射保持定向。

在极坐标 $z=r\mathrm{e}^{\mathrm{i}\theta}$（$r>0$）下，由链式法则 $u_r=u_x\cos\theta+u_y\sin\theta$，$u_\theta=-u_xr\sin\theta+u_yr\cos\theta$（$v$ 同理），式 (2.2) 化为

$$
\frac{\partial u}{\partial r}=\frac1r\frac{\partial v}{\partial\theta},\qquad \frac{\partial v}{\partial r}=-\frac1r\frac{\partial u}{\partial\theta},\qquad f'(z)=\mathrm{e}^{-\mathrm{i}\theta}\Big(\frac{\partial u}{\partial r}+\mathrm{i}\frac{\partial v}{\partial r}\Big). \tag{2.4}
$$

最后一式成立，是因为沿射线求导有 $\frac{\partial f}{\partial r}=f'(z)\frac{\partial z}{\partial r}=f'(z)\mathrm{e}^{\mathrm{i}\theta}$。对于用模和辐角定义的函数，如 [2.3.3](/2.3.3) 中的 $\log z$ 与 $z^\alpha$，极坐标形式用起来更方便。

**例 2.2.1** $f(z)=x^2+\mathrm{i}y^2$ 在哪里复可导？这里 $u_x=2x$，$v_y=2y$，$u_y=0$，$v_x=0$，都连续。第二个方程总成立，第一个方程当且仅当 $x=y$ 时成立。所以 $f$ 恰在直线 $y=x$ 上复可导，且 $f'(x+\mathrm{i}x)=u_x+\mathrm{i}v_x=2x$。

**例 2.2.2** 对 $f(z)=z^3$，$u=x^3-3xy^2$，$v=3x^2y-y^3$，确实有 $u_x=3x^2-3y^2=v_y$，$u_y=-6xy=-v_x$；由式 (2.3)，$f'(z)=u_x+\mathrm{i}v_x=3(x^2-y^2)+6xy\,\mathrm{i}=3z^2$。对 $f(z)=\frac1z$ 用极坐标形式：$u=\frac{\cos\theta}{r}$，$v=-\frac{\sin\theta}{r}$；于是 $u_r=-\frac{\cos\theta}{r^2}=\frac1rv_\theta$，$v_r=\frac{\sin\theta}{r^2}=-\frac1ru_\theta$，且 $f'(z)=\mathrm{e}^{-\mathrm{i}\theta}\cdot\frac{-\cos\theta+\mathrm{i}\sin\theta}{r^2}=-\frac{\mathrm{e}^{-2\mathrm{i}\theta}}{r^2}=-\frac1{z^2}$。

## 2.3. 解析函数

只在一点处复可导，或像例 2.2.1 那样只在一条直线上复可导，提供的信息很少。有用的概念要求在开集上可导。

**定义 2.3.1（解析函数）** 若函数 $f$ 在 $z_0$ 的某个邻域内处处复可导，则称 $f$ 在 $z_0$ 处解析。若 $f$ 在开集 $D$ 的每一点处解析，即在 $D$ 上处处复可导，则称 $f$ 在 $D$ 上解析，并称它为 $D$ 上的**解析函数**（或**全纯函数**）。在整个 $\mathbb{C}$ 上解析的函数称为**整函数**。若 $f$ 在包含闭集 $E$ 的某个开集上解析，则称 $f$ 在 $E$ 上解析。

**定义 2.3.2（奇点）** 若 $f$ 在 $z_0$ 处不解析，但 $z_0$ 的每个邻域内都有 $f$ 的解析点，则称 $z_0$ 为 $f$ 的**奇点**。

例如，多项式是整函数；既约的有理函数 $P/Q$ 在 $\mathbb{C}$ 上除 $Q$ 的零点外处处解析，$Q$ 的零点就是它的奇点；$\frac1z$ 在 $\mathbb{C}\setminus\{0\}$ 上解析，奇点为 $0$。函数 $x^2+\mathrm{i}y^2$（例 2.2.1）与 $|z|^2$（例 2.1.3）虽然在某些点处复可导，却处处不解析，按上述定义它们也没有奇点。若 $f$ 在奇点周围的整个去心圆盘内解析，则称这个奇点是孤立的；把孤立奇点分为可去奇点、极点和本性奇点，是 [2.3.6](/2.3.6) 的内容。

**定理 2.3.1** 解析函数的和、差、积与复合仍解析；商 $f/g$ 在 $g\ne0$ 处解析。

这由 §2.1 的求导法则立即得到。下面是 Cauchy–Riemann 方程的两个推论，它们显示了解析函数的刚性。

**定理 2.3.2** 设 $f=u+\mathrm{i}v$ 在**区域** $D$ 上解析。若在 $D$ 上 $f'\equiv0$，则 $f$ 在 $D$ 上为常数。

**证明** 由式 (2.3)，在 $D$ 上 $u_x=u_y=v_x=v_y=0$。沿平行于坐标轴的线段应用 **Lagrange 中值定理**，$u$ 与 $v$ 在 $D$ 所含的每个圆盘上为常数，因而局部为常数。连通开集上局部为常数的函数是常数：集合 $\{u=u(z_0)\}$ 是开集，它在 $D$ 中的余集也是开集，而 $D$ 不能分成两个不相交的非空开集。$\square$

**推论 2.3.1** 设 $f=u+\mathrm{i}v$ 在区域 $D$ 上解析。下列任一条件都推出 $f$ 在 $D$ 上为常数：

1. $u$ 为常数（或 $v$ 为常数）；
2. $|f|$ 为常数；
3. $\bar f$ 在 $D$ 上也解析。

**证明** 1. 若 $u$ 为常数，则 $u_x=u_y=0$，于是 $f'=u_x-\mathrm{i}u_y=0$，由定理 2.3.2 即得；$v$ 的情形相同，用 $f'=v_y+\mathrm{i}v_x$。

2. 设 $u^2+v^2=c$。若 $c=0$，则 $f\equiv0$。否则求导得 $uu_x+vv_x=0$，$uu_y+vv_y=0$；代入 $v_x=-u_y$，$v_y=u_x$，得线性方程组 $uu_x-vu_y=0$，$vu_x+uu_y=0$，其系数行列式为 $u^2+v^2=c\ne0$。所以 $u_x=u_y=0$，由 1 知 $f$ 为常数。

3. 此时 $f+\bar f=2u$ 解析且取实值，其虚部为常数，由 1 它是常数；于是 $u$ 为常数，$f$ 也是常数。$\square$

## 2.4. Wirtinger 导数

### 2.4.1. 定义与解析性判别

实变量 $x,y$ 的函数 $f(x,y)$ 可以通过 $x=\frac{z+\bar z}{2}$、$y=\frac{z-\bar z}{2\mathrm{i}}$ 看作 $z$ 与 $\bar z$ 的函数。假装 $z$ 与 $\bar z$ 是独立变量，形式地应用链式法则，得 $\frac{\partial}{\partial z}=\frac{\partial x}{\partial z}\frac{\partial}{\partial x}+\frac{\partial y}{\partial z}\frac{\partial}{\partial y}=\frac12\frac{\partial}{\partial x}+\frac1{2\mathrm{i}}\frac{\partial}{\partial y}$，对 $\bar z$ 也类似。我们把所得结果作为定义。

**定义 2.4.1（Wirtinger 导数）** 设函数 $f=u+\mathrm{i}v$ 的实部与虚部有一阶偏导数，称

$$
\frac{\partial f}{\partial z}=\frac12\Big(\frac{\partial f}{\partial x}-\mathrm{i}\frac{\partial f}{\partial y}\Big),\qquad \frac{\partial f}{\partial\bar z}=\frac12\Big(\frac{\partial f}{\partial x}+\mathrm{i}\frac{\partial f}{\partial y}\Big)
$$

为 $f$ 的 **Wirtinger 导数**，其中 $\frac{\partial f}{\partial x}=u_x+\mathrm{i}v_x$，$\frac{\partial f}{\partial y}=u_y+\mathrm{i}v_y$。也记作 $f_z$ 与 $f_{\bar z}$。

展开得

$$
\frac{\partial f}{\partial\bar z}=\frac12\big[(u_x-v_y)+\mathrm{i}(v_x+u_y)\big],\qquad \frac{\partial f}{\partial z}=\frac12\big[(u_x+v_y)+\mathrm{i}(v_x-u_y)\big]. \tag{2.5}
$$

所以 $\frac{\partial f}{\partial\bar z}=0$ 就是写成一个复方程的 Cauchy–Riemann 方程组；它成立时 $\frac{\partial f}{\partial z}=u_x+\mathrm{i}v_x=f'$。于是定理 2.2.1 可以写成：

**定理 2.4.1** 设 $u,v$ 在 $z_0$ 处可微。则 $f=u+\mathrm{i}v$ 在 $z_0$ 处复可导当且仅当 $\dfrac{\partial f}{\partial\bar z}(z_0)=0$，此时 $f'(z_0)=\dfrac{\partial f}{\partial z}(z_0)$。在开集 $D$ 上有连续一阶偏导数的函数在 $D$ 上解析，当且仅当在 $D$ 上 $\dfrac{\partial f}{\partial\bar z}\equiv0$。

一句话概括：解析函数就是只依赖于 $z$、不依赖于 $\bar z$ 的函数。用实变量写，全微分为

$$
\mathrm{d}f=f_x\,\mathrm{d}x+f_y\,\mathrm{d}y=\frac{\partial f}{\partial z}\,\mathrm{d}z+\frac{\partial f}{\partial\bar z}\,\mathrm{d}\bar z,
$$

代入 $\mathrm{d}x=\frac{\mathrm{d}z+\mathrm{d}\bar z}{2}$、$\mathrm{d}y=\frac{\mathrm{d}z-\mathrm{d}\bar z}{2\mathrm{i}}$ 即可验证。导数 $f'$ 是 $\mathrm{d}z$ 的系数，$\mathrm{d}\bar z$ 的系数则度量了 $f$ 偏离解析的程度。

### 2.4.2. 用 Wirtinger 导数计算

算子 $\partial/\partial z$ 与 $\partial/\partial\bar z$ 是 $\partial/\partial x$ 与 $\partial/\partial y$ 的线性组合，所以它们是线性的，并满足乘积与商的求导法则。此外

$$
\frac{\partial z}{\partial z}=1,\quad \frac{\partial\bar z}{\partial z}=0,\quad \frac{\partial z}{\partial\bar z}=0,\quad \frac{\partial\bar z}{\partial\bar z}=1,\qquad \overline{\Big(\frac{\partial f}{\partial z}\Big)}=\frac{\partial\bar f}{\partial\bar z}, \tag{2.6}
$$

且对解析函数 $g$，链式法则取如下形式：

$$
\frac{\partial}{\partial z}g(h)=g'(h)\frac{\partial h}{\partial z},\qquad \frac{\partial}{\partial\bar z}g(h)=g'(h)\frac{\partial h}{\partial\bar z},
$$

其中 $h$ 是任意有连续偏导数的函数。（两式都由 $\mathrm{d}\,g(h)=g'(h)\,\mathrm{d}h$ 及上面 $\mathrm{d}h$ 的表达式得到。）因此实际计算时：利用 $|z|^2=z\bar z$、$\operatorname{Re}z=\frac{z+\bar z}2$、$\operatorname{Im}z=\frac{z-\bar z}{2\mathrm{i}}$ 把 $f$ 写成 $z$ 与 $\bar z$ 的表达式，再把 $z$ 与 $\bar z$ 当作独立变量求导。最后，**Laplace 算子**可以分解为

$$
\Delta=\frac{\partial^2}{\partial x^2}+\frac{\partial^2}{\partial y^2}=4\frac{\partial^2}{\partial z\,\partial\bar z}, \tag{2.7}
$$

这是因为对有连续二阶偏导数的函数，$\big(\partial_x-\mathrm{i}\partial_y\big)\big(\partial_x+\mathrm{i}\partial_y\big)=\partial_x^2+\partial_y^2$。

**例 2.4.1** 设 $f(z)=z^2+3z\bar z^2$。则 $\frac{\partial f}{\partial\bar z}=6z\bar z=6|z|^2$，只在 $z=0$ 处为零。所以 $f$ 只在 $0$ 处复可导，$f'(0)=\frac{\partial f}{\partial z}(0)=(2z+3\bar z^2)\big|_{z=0}=0$，且 $f$ 处处不解析。对例 2.2.1 中的 $f=x^2+\mathrm{i}y^2$，由式 (2.5) 得 $\frac{\partial f}{\partial\bar z}=\frac12(2x+\mathrm{i}\cdot\mathrm{i}\,2y)=x-y$，又得到了直线 $y=x$。

**例 2.4.2** 设 $f(z)=\sin(z)\,\mathrm{e}^{|z|^2}$，其中 $\sin z$ 是 [2.3.3](/2.3.3) 中的整函数（其导数为 $\cos z$，且 $\sin(\mathrm{i}t)=\mathrm{i}\sinh t$）。求 $\frac{\partial f}{\partial\bar z}$ 与 $\frac{\partial f}{\partial z}$ 在 $z=\mathrm{i}\pi$ 处的值。把 $\mathrm{e}^{|z|^2}$ 写成 $\mathrm{e}^{z\bar z}$，由乘积法则与链式法则得

$$
\frac{\partial f}{\partial\bar z}=\sin z\cdot z\,\mathrm{e}^{z\bar z},\qquad \frac{\partial f}{\partial z}=\cos z\cdot\mathrm{e}^{z\bar z}+\sin z\cdot\bar z\,\mathrm{e}^{z\bar z}.
$$

在 $z=\mathrm{i}\pi$ 处，$z\bar z=\pi^2$，$\sin(\mathrm{i}\pi)=\mathrm{i}\sinh\pi$，$\cos(\mathrm{i}\pi)=\cosh\pi$，所以

$$
\frac{\partial f}{\partial\bar z}(\mathrm{i}\pi)=\mathrm{i}\sinh\pi\cdot\mathrm{i}\pi\,\mathrm{e}^{\pi^2}=-\pi\sinh\pi\,\mathrm{e}^{\pi^2},\qquad \frac{\partial f}{\partial z}(\mathrm{i}\pi)=\big(\cosh\pi+\pi\sinh\pi\big)\mathrm{e}^{\pi^2}.
$$

若用 $x,y$ 和式 (2.5) 计算，过程要长得多。

## 2.5. 调和函数与共轭调和函数

### 2.5.1. 实部与虚部是调和函数

**定理 2.5.1** 若 $f=u+\mathrm{i}v$ 在开集 $D$ 上解析，则 $u$ 与 $v$ 是 $D$ 上的**调和函数**：$\Delta u=\Delta v=0$。

**证明** 我们用到 [2.3.4](/2.3.4)（定理 4.4.2）中证明的事实：解析函数的导数仍解析；特别地，$u$ 与 $v$ 有各阶连续偏导数。把 $u_x=v_y$ 对 $x$ 求导、$u_y=-v_x$ 对 $y$ 求导，相加，由混合偏导数相等得 $u_{xx}+u_{yy}=v_{yx}-v_{xy}=0$。同理 $\Delta v=-u_{yx}+u_{xy}=0$。用式 (2.7) 的记号：$\Delta f=4\frac{\partial}{\partial z}\frac{\partial f}{\partial\bar z}=0$，取实部与虚部即得结论。$\square$

调和函数描述稳态温度、无电荷区域中的静电势以及理想流体的速度势（[2.2.14](/2.2.14)）；这个定理使解析函数成为 Laplace 方程显式解的来源，[2.3.8](/2.3.8) 与 [2.5.8](/2.5.8) 将结合共形映射系统地利用这一点。

**定义 2.5.1（共轭调和函数）** 设 $u$ 是开集 $D$ 上的调和函数。若 $D$ 上的调和函数 $v$ 使 $u+\mathrm{i}v$ 在 $D$ 上解析，则称 $v$ 为 $u$ 的**共轭调和函数**。

这个关系不是对称的：若 $v$ 是 $u$ 的共轭调和函数，则 $v$ 的共轭调和函数是 $-u$（而不是 $u$），因为 $v-\mathrm{i}u=-\mathrm{i}(u+\mathrm{i}v)$ 解析。由推论 2.3.1，区域上的共轭调和函数在相差一个实常数的意义下唯一。

### 2.5.2. 单连通区域上的存在性

**定理 2.5.2** 设 $u$ 是单连通区域 $D$ 上的调和函数，$z_0=(x_0,y_0)\in D$。则

$$
v(x,y)=\int_{(x_0,y_0)}^{(x,y)}-u_y\,\mathrm{d}x+u_x\,\mathrm{d}y+C \tag{2.8}
$$

是良定义的（与 $D$ 内的路径无关），且对每个实常数 $C$，它都是 $u$ 的共轭调和函数；$u$ 的每个共轭调和函数都具有这种形式。

**证明** Cauchy–Riemann 方程要求 $v_x=-u_y$，$v_y=u_x$，即 $-u_y\,\mathrm{d}x+u_x\,\mathrm{d}y$ 是 $v$ 的全微分。可积条件 $\frac{\partial(-u_y)}{\partial y}=\frac{\partial u_x}{\partial x}$ 恰好就是 $\Delta u=0$。在单连通区域上，分量连续可微且满足这一条件的**第二型曲线积分**与路径无关，并定义了一个具有给定偏导数的势函数（由 **Green 公式**，[2.2.13](/2.2.13)）。所以 $v$ 是良定义的，且 $v_x=-u_y$，$v_y=u_x$；它们连续，故由推论 2.2.1，$u+\mathrm{i}v$ 解析，再由定理 2.5.1，$v$ 调和。相差常数意义下的唯一性上面已经说明。$\square$

单连通的条件不能去掉。函数 $u=\ln|z|=\frac12\ln(x^2+y^2)$ 在 $\mathbb{C}\setminus\{0\}$ 上调和，式 (2.8) 给出 $v=\arg z$，它绕原点一周改变 $2\pi$：$u$ 在每个单连通子区域上都有共轭调和函数（例如在割去负实轴的平面上，$v=\operatorname{Arg}z$），但在整个去心平面上没有。这就是 [2.3.3](/2.3.3) 中多值对数 $\ln|z|+\mathrm{i}\arg z$ 的来源。

### 2.5.3. 由实部求解析函数

一个典型问题：已知调和函数 $u$（或 $v$），求解析函数 $f$ 使 $\operatorname{Re}f=u$，可能还附带某种规范化条件，如给定 $f(z_0)$ 的值。常用三种方法。

1. 偏积分法。由 $v_y=u_x$ 对 $y$ 积分：$v=\int u_x\,\mathrm{d}y+\varphi(x)$；再由 $v_x=-u_y$ 确定 $\varphi$。（这就是沿平行于坐标轴的折线计算式 (2.8)。）
2. 曲线积分法：沿任意方便的路径计算式 (2.8)。
3. 导数法。由式 (2.3)，$f'(z)=u_x-\mathrm{i}u_y$（已知 $v$ 时用 $f'=v_y+\mathrm{i}v_x$）。若 $u$ 由多项式和初等函数构成，在右端令 $x=z$，$y=0$：$f'(z)=u_x(z,0)-\mathrm{i}u_y(z,0)$，再对 $z$ 积分。这一代换是合理的，因为两端都解析且在实轴上相等，而在一条线段上相等的两个解析函数在整个区域上相等（唯一性定理，[2.3.5](/2.3.5)）。

**例 2.5.1** 求 $a\in\mathbb{R}$ 使 $u=x^3+axy^2+x^2-y^2$ 为调和函数，并求解析函数 $f$，使 $\operatorname{Re}f=u$ 且 $f(0)=0$。

由 $\Delta u=6x+2ax+2-2=(6+2a)x$，需 $a=-3$。用方法 1：$u_x=3x^2-3y^2+2x$，故 $v=\int(3x^2-3y^2+2x)\,\mathrm{d}y=3x^2y-y^3+2xy+\varphi(x)$。于是 $v_x=6xy+2y+\varphi'(x)$ 应等于 $-u_y=6xy+2y$，所以 $\varphi$ 是常数 $c$。因此

$$
f=u+\mathrm{i}v=(x^3-3xy^2+x^2-y^2)+\mathrm{i}(3x^2y-y^3+2xy)+\mathrm{i}c=z^3+z^2+\mathrm{i}c,
$$

由 $f(0)=0$ 得 $c=0$，故 $f(z)=z^3+z^2$。

**例 2.5.2** 求 $\mathbb{C}\setminus\{0\}$ 上的解析函数 $f$，使 $\operatorname{Im}f=v=2xy-\dfrac{y}{x^2+y^2}$ 且 $f(1)=3$。

用方法 3，$f'=v_y+\mathrm{i}v_x$：算得 $v_y=2x-\frac{x^2-y^2}{(x^2+y^2)^2}$，$v_x=2y+\frac{2xy}{(x^2+y^2)^2}$，于是 $v_y(z,0)=2z-\frac1{z^2}$，$v_x(z,0)=0$。所以 $f'(z)=2z-\frac1{z^2}$，$f(z)=z^2+\frac1z+c$，其中 $c$ 为实数（因为 $\operatorname{Im}f$ 已给定）。由 $f(1)=2+c=3$ 得 $f(z)=z^2+\frac1z+1$。验证：$\operatorname{Im}z^2=2xy$，$\operatorname{Im}\frac1z=-\frac{y}{x^2+y^2}$。

$u$ 中含指数函数或三角函数的问题，在有了 $\mathrm{e}^z$ 与 $\sin z$ 之后用同样的方法求解，见 [2.3.3](/2.3.3) 的例 3.1.2。

## 2.6. 导数的几何意义

设 $f$ 在 $z_0$ 处解析，$f'(z_0)=\rho\,\mathrm{e}^{\mathrm{i}\alpha}\ne0$，$\gamma$ 是满足 $\gamma(t_0)=z_0$ 的光滑曲线。由链式法则，像曲线 $\Gamma=f\circ\gamma$ 满足

$$
\Gamma'(t_0)=f'(z_0)\,\gamma'(t_0).
$$

所以 $\Gamma$ 在 $f(z_0)$ 处的切线方向是 $\gamma$ 的切线方向旋转 $\alpha=\operatorname{Arg}f'(z_0)$，而 $z_0$ 附近的微小长度近似地乘以 $\rho=|f'(z_0)|$，在各个方向上倍数相同。由此有两个推论：

- 旋转角与伸缩率与曲线无关，所以过 $z_0$ 的任意两条曲线的夹角（切线的夹角）的大小和方向都保持不变；
- 无穷小的圆映为无穷小的圆，面积乘以 Jacobi 行列式 $|f'(z_0)|^2$。

具有这些性质的映射称为在 $z_0$ 处共形的；共形映射在 [2.3.8](/2.3.8) 中研究。在 $f'(z_0)=0$ 处情况不同：若 $f(z)-f(z_0)$ 的性态像 $c(z-z_0)^k$（$k\ge2$），则 $z_0$ 处的角度乘以 $k$。

![映射 w = z^2 作用于第一象限中的网格。竖直线 x = c 与水平线 y = c 变成两族仍然直角相交的抛物线，小正方形变成小曲边正方形；在导数为零的 z = 0 处，正实轴与正虚轴之间的直角加倍成平角。](./plots/square-map.py)

**例 2.6.1** 对 $w=z^2$，竖直线 $x=c$ 映为 $u=c^2-y^2$，$v=2cy$，即开口向左的抛物线 $u=c^2-\frac{v^2}{4c^2}$；水平线 $y=c$ 映为 $u=x^2-c^2$，$v=2cx$，即开口向右的抛物线 $u=\frac{v^2}{4c^2}-c^2$。在交点 $z_0=c_1+\mathrm{i}c_2\ne0$ 处，两条直线正交且 $f'(z_0)=2z_0\ne0$，所以两条抛物线也正交。在 $z_0=0$ 处 $f'(0)=0$，正实轴与正虚轴之间的角 $\frac\pi2$ 变成正、负实轴之间的角 $\pi$。

把同样的计算反过来读，就解释了关于等值线的一个经典事实。

**定理 2.6.1** 设 $f=u+\mathrm{i}v$ 解析且 $f'(z_0)\ne0$。则等值线 $u=u(z_0)$ 与 $v=v(z_0)$ 在 $z_0$ 处正交。

**证明** 由 Cauchy–Riemann 方程，梯度 $\nabla u=(u_x,u_y)$ 与 $\nabla v=(v_x,v_y)=(-u_y,u_x)$ 满足 $\nabla u\cdot\nabla v=0$。由于 $|\nabla u|=|\nabla v|=|f'(z_0)|$，两者都不为零，而它们分别是相应**等值线**的法向量。$\square$

![u = Re(1/z) 的等值线（在 0 处与虚轴相切的圆）与 v = Im(1/z) 的等值线（在 0 处与实轴相切的圆）。每个蓝色圆都与每个红色圆直角相交；它们都经过奇点 z = 0。](./plots/level-curves.py)

在二维理想流动中，若 $u$ 是速度势，则其共轭调和函数 $v$ 的等值线就是流线；定理 2.6.1 说明流线与等势线直角相交。函数 $f=u+\mathrm{i}v$ 是该流动的复势（[2.3.8](/2.3.8)）。

## 小结

| 概念 | 判别法或公式 |
|---|---|
| 在 $z_0$ 处复可导 | $u,v$ 可微且 $u_x=v_y$，$u_y=-v_x$；等价地 $\partial f/\partial\bar z=0$ |
| 导数 | $f'=u_x+\mathrm{i}v_x=v_y-\mathrm{i}u_y=\partial f/\partial z$；极坐标：$f'=\mathrm{e}^{-\mathrm{i}\theta}(u_r+\mathrm{i}v_r)$ |
| 在 $D$ 上解析 | 在开集 $D$ 的每一点处复可导 |
| 刚性 | 在区域上：$f'=0$，或 $\operatorname{Re}f$ 为常数，或 $\lvert f\rvert$ 为常数，或 $\bar f$ 解析 $\Rightarrow$ $f$ 为常数 |
| 调和性 | $\operatorname{Re}f$、$\operatorname{Im}f$ 调和；$\Delta=4\,\partial^2/\partial z\,\partial\bar z$ |
| 重建 | $f'(z)=u_x(z,0)-\mathrm{i}u_y(z,0)$，或式 (2.8)；在相差一个纯虚常数的意义下唯一 |
| 几何 | $f'(z_0)\ne0$：旋转 $\operatorname{Arg}f'(z_0)$，伸缩 $\lvert f'(z_0)\rvert$，保持角度 |
