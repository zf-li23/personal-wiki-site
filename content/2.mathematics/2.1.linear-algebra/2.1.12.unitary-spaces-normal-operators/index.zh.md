---
title: 酉空间与正规变换
---

[第 4 章](/2.1.4)在 $\mathbb{R}^n$ 上用**内积**定义了长度、角度与正交，并由此得到 Gram–Schmidt 正交化、**QR 分解**、**正交投影**与最小二乘。那里的结论只用到内积的三条性质：对称、双线性、正定。本章把这三条性质作为公理，做两件推广：一是把内积放到任意线性空间上，使函数空间、矩阵空间也有长度和角度；二是把实数换成复数，对称性相应地改为共轭对称。凡是证明与 $\mathbb{R}^n$ 情形相同的地方，这里只简述。

本章的核心问题是：**线性变换**在什么条件下存在一组标准正交基，使它的矩阵为对角阵？在 $\mathbb{R}^n$ 上，[第 7 章](/2.1.7)证明了实对称矩阵可以正交对角化（定理 7.1.1）。在复数域上，答案是谱定理：恰好是正规变换（$TT^* = T^*T$）。实对称矩阵的**谱分解**将作为谱定理的推论重新得到。证明的路线是一条标准化的拆解：[第 10 章](/2.1.10)的 Schur 三角化加上 QR 分解得到酉三角化，再由正规性推出三角阵其实是对角阵；计算上，酉对角化就是求特征值，再在每个**特征子空间**中做 Gram–Schmidt 正交化。

## 12.1. 内积空间

先回顾 $\mathbb{R}^3$ 的点积 $\boldsymbol{u} \cdot \boldsymbol{v} = \boldsymbol{u}^{\mathsf T}\boldsymbol{v}$。设 $\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_2, \boldsymbol{\alpha}_3$ 是 $\mathbb{R}^3$ 的一组基，$\boldsymbol{\alpha} = \sum x_i\boldsymbol{\alpha}_i$，$\boldsymbol{\beta} = \sum y_j\boldsymbol{\alpha}_j$，则

$$
\boldsymbol{\alpha} \cdot \boldsymbol{\beta} = \sum_{i,j}x_iy_j(\boldsymbol{\alpha}_i \cdot \boldsymbol{\alpha}_j) = \boldsymbol{x}^{\mathsf T}G\boldsymbol{y}, \qquad G = (\boldsymbol{\alpha}_i \cdot \boldsymbol{\alpha}_j)_{3 \times 3},
$$

$G$ 称为点积在这组基下的**度量矩阵**，它是实对称正定矩阵；基为标准正交基时 $G = I$。反过来，任取一个实对称正定矩阵 $G$，$\boldsymbol{x}^{\mathsf T}G\boldsymbol{y}$ 都给出 $\mathbb{R}^3$ 上一种"度量"。这启发我们只保留点积的代数性质。

**定义 12.1.1（内积空间）** 设 $\mathbb{F} = \mathbb{R}$ 或 $\mathbb{C}$，$V$ 是 $\mathbb{F}$ 上的线性空间。若映射 $\langle \cdot, \cdot \rangle\colon V \times V \to \mathbb{F}$ 对任意 $\alpha, \beta, \gamma \in V$、$c_1, c_2 \in \mathbb{F}$ 满足下列三条，则称它是 $V$ 上的一个内积，称 $(V, \langle \cdot, \cdot \rangle)$ 为**内积空间**；$\mathbb{F} = \mathbb{R}$ 且 $\dim V < \infty$ 时称为**欧氏空间**，$\mathbb{F} = \mathbb{C}$ 且 $\dim V < \infty$ 时称为**酉空间**：

1. 共轭对称性：$\langle \alpha, \beta \rangle = \overline{\langle \beta, \alpha \rangle}$；
2. 对第一个变量线性：$\langle c_1\alpha + c_2\beta, \gamma \rangle = c_1\langle \alpha, \gamma \rangle + c_2\langle \beta, \gamma \rangle$；
3. 正定性：$\langle \alpha, \alpha \rangle \ge 0$，且 $\langle \alpha, \alpha \rangle = 0 \Leftrightarrow \alpha = 0$。

$\mathbb{F} = \mathbb{R}$ 时共轭对称就是对称，内积是双线性的。$\mathbb{F} = \mathbb{C}$ 时由 1、2 推出内积对第二个变量共轭线性：$\langle \alpha, c\beta \rangle = \bar c\langle \alpha, \beta \rangle$。本课程（与课件、教材一致）约定对第一个变量线性；物理文献（如量子力学的 Dirac 记号）通常约定对第二个变量线性，公式中的共轭位置相应改变。

**例 12.1.1** $\mathbb{R}^n$ 上 $\langle \boldsymbol{\alpha}, \boldsymbol{\beta} \rangle = \boldsymbol{\alpha}^{\mathsf T}\boldsymbol{\beta}$ 与 $\mathbb{C}^n$ 上

$$
\langle \boldsymbol{\alpha}, \boldsymbol{\beta} \rangle = \boldsymbol{\alpha}^{\mathsf T}\bar{\boldsymbol{\beta}} = \boldsymbol{\beta}^{\mathsf H}\boldsymbol{\alpha} = x_1\bar y_1 + \cdots + x_n\bar y_n
$$

都称为标准内积。复情形必须取共轭：若在 $\mathbb{C}$ 上用 $\langle \alpha, \beta \rangle = \alpha\beta$，则 $\langle \mathrm{i}, \mathrm{i} \rangle = -1 < 0$，正定性失败；而 $\mathrm{i} \cdot \bar{\mathrm{i}} = 1$。例如 $\boldsymbol{\alpha} = (1, \mathrm{i})^{\mathsf T}$，$\boldsymbol{\beta} = (1 + \mathrm{i}, 2\mathrm{i})^{\mathsf T}$ 时，

$$
\langle \boldsymbol{\alpha}, \boldsymbol{\beta} \rangle = 1 \cdot (1 - \mathrm{i}) + \mathrm{i} \cdot (-2\mathrm{i}) = 3 - \mathrm{i}, \qquad \langle \boldsymbol{\alpha}, \boldsymbol{\alpha} \rangle = 2, \qquad \langle \boldsymbol{\beta}, \boldsymbol{\beta} \rangle = 6.
$$

**例 12.1.2** 设 $A \in \mathbb{R}^{n\times n}$，$\langle \boldsymbol{\alpha}, \boldsymbol{\beta} \rangle = \boldsymbol{\alpha}^{\mathsf T}A\boldsymbol{\beta}$ 是 $\mathbb{R}^n$ 上的内积 $\Leftrightarrow$ $A$ 是实对称的**正定矩阵**：对称性 $\Leftrightarrow$ $\boldsymbol{\alpha}^{\mathsf T}A\boldsymbol{\beta} = \boldsymbol{\beta}^{\mathsf T}A\boldsymbol{\alpha}$ 对一切 $\boldsymbol{\alpha}, \boldsymbol{\beta}$ 成立 $\Leftrightarrow$ $A = A^{\mathsf T}$；线性性自动成立；正定性 $\Leftrightarrow$ $\boldsymbol{\alpha}^{\mathsf T}A\boldsymbol{\alpha} > 0$（$\boldsymbol{\alpha} \ne \boldsymbol{0}$）。复情形的对应结论（正定 Hermite 矩阵）见 [第 13 章](/2.1.13)。

**例 12.1.3** $C[a, b]$（$[a, b]$ 上的实连续函数）上，$\langle f, g \rangle = \int_a^b f(t)g(t)\,\mathrm{d}t$ 是内积。它是 $\mathbb{R}^n$ 点积的连续版本：$\int_a^b fg\,\mathrm{d}t = \lim_{n \to \infty}\frac{b - a}{n}\sum_i f(t_i)g(t_i)$。正定性来自：非负连续函数的积分为零当且仅当它恒为零。$C[a, b]$ 是无穷维的，所以它是内积空间，但不是欧氏空间。

**例 12.1.4** $\mathbb{R}^{n\times n}$ 上 $\langle A, B \rangle = \operatorname{tr}(AB^{\mathsf T}) = \sum_{i,j}a_{ij}b_{ij}$，$\mathbb{C}^{n\times n}$ 上 $\langle A, B \rangle = \operatorname{tr}(AB^{\mathsf H})$，称为 Frobenius 内积（Frobenius inner product）。它就是把矩阵看作 $n^2$ 维向量后的标准内积；**迹**的性质 $\operatorname{tr}(AB^{\mathsf T}) = \operatorname{tr}(BA^{\mathsf T})$ 给出对称性，$\operatorname{tr}(AA^{\mathsf T}) = \sum a_{ij}^2$ 给出正定性。

一般地，设 $\alpha_1, \dots, \alpha_n$ 是内积空间 $V$ 的基，称 $G = (\langle \alpha_i, \alpha_j \rangle)_{n \times n}$ 为内积在这组基下的度量矩阵，也就是这组向量的 **Gram 矩阵**（[第 11 章](/2.1.11)定义 11.2.2 是函数空间中积分内积的特例）。若 $\alpha = \sum x_i\alpha_i$，$\beta = \sum y_j\alpha_j$，则

$$
\langle \alpha, \beta \rangle = \sum_{i,j}x_i\bar y_j\langle \alpha_i, \alpha_j \rangle = \boldsymbol{x}^{\mathsf T}G\bar{\boldsymbol{y}}.
$$

由共轭对称性 $G^{\mathsf H} = G$；由正定性，$G$ 是正定的。所以取定基以后，$n$ 维欧氏空间（酉空间）上的内积与 $n$ 阶正定实对称（Hermite）矩阵一一对应；基是标准正交基当且仅当 $G = I$。

## 12.2. 长度、夹角与正交

**定义 12.2.1** 设 $V$ 是内积空间，$\alpha, \beta \in V$。$\|\alpha\| = \sqrt{\langle \alpha, \alpha \rangle}$ 称为 $\alpha$ 的长度；$\|\alpha\| = 1$ 时称为单位向量，$\alpha \ne 0$ 时 $\alpha / \|\alpha\|$ 是单位向量（单位化）。若 $\langle \alpha, \beta \rangle = 0$，则称 $\alpha$ 与 $\beta$ 正交，记作 $\alpha \perp \beta$。对非零的 $\alpha, \beta$，定义夹角 $\theta$：

- 实内积空间：$\cos\theta = \dfrac{\langle \alpha, \beta \rangle}{\|\alpha\|\,\|\beta\|}$，$0 \le \theta \le \pi$；
- 复内积空间：$\cos\theta = \dfrac{|\langle \alpha, \beta \rangle|}{\|\alpha\|\,\|\beta\|}$，$0 \le \theta \le \dfrac{\pi}{2}$。

复情形的 $\langle \alpha, \beta \rangle$ 是复数，只能取模，夹角因此落在 $[0, \pi/2]$，$\alpha \perp \beta$ 时恰为 $\pi/2$（课件写成 $0 \le \theta < \pi/2$，漏掉了正交的情形）。夹角的定义要求 $|\cos\theta| \le 1$，这正是 Cauchy–Schwarz 不等式。

**性质 12.2.1** 设 $V$ 是内积空间，$\alpha, \beta \in V$，$c \in \mathbb{F}$。

1. $\|\alpha\| = 0 \Leftrightarrow \alpha = 0$；$\|c\alpha\| = |c|\,\|\alpha\|$。
2. （勾股定理）若 $\alpha \perp \beta$，则 $\|\alpha \pm \beta\|^2 = \|\alpha\|^2 + \|\beta\|^2$。
3. （**Cauchy–Schwarz 不等式**）$|\langle \alpha, \beta \rangle| \le \|\alpha\|\,\|\beta\|$，等号成立当且仅当 $\alpha, \beta$ 线性相关。
4. （**三角不等式**）$\|\alpha + \beta\| \le \|\alpha\| + \|\beta\|$。

**证明** 2：$\|\alpha - \beta\|^2 = \langle \alpha, \alpha \rangle - \langle \alpha, \beta \rangle - \langle \beta, \alpha \rangle + \langle \beta, \beta \rangle$，中间两项为零。

3：$\beta = 0$ 时显然。设 $\beta \ne 0$，令 $\alpha_p = t\beta$ 是 $\alpha$ 在 $\beta$ 上的投影，即要求 $\langle \alpha - t\beta, \beta \rangle = 0$，得 $t = \dfrac{\langle \alpha, \beta \rangle}{\langle \beta, \beta \rangle}$。由勾股定理，$\|\alpha\|^2 = \|\alpha - \alpha_p\|^2 + \|\alpha_p\|^2 \ge \|\alpha_p\|^2 = \dfrac{|\langle \alpha, \beta \rangle|^2}{\|\beta\|^2}$。等号成立 $\Leftrightarrow$ $\alpha = \alpha_p$ $\Leftrightarrow$ $\alpha, \beta$ 线性相关。

4：$\|\alpha + \beta\|^2 = \|\alpha\|^2 + 2\operatorname{Re}\langle \alpha, \beta \rangle + \|\beta\|^2 \le \|\alpha\|^2 + 2\|\alpha\|\,\|\beta\| + \|\beta\|^2$，用到 $\operatorname{Re}\langle \alpha, \beta \rangle \le |\langle \alpha, \beta \rangle|$ 与 3。 $\square$

复情形勾股定理的逆命题不成立：$\|\alpha + \beta\|^2 = \|\alpha\|^2 + \|\beta\|^2$ 只说明 $\operatorname{Re}\langle \alpha, \beta \rangle = 0$。例如在 $\mathbb{C}$ 中 $\|1 + \mathrm{i}\|^2 = 2 = \|1\|^2 + \|\mathrm{i}\|^2$，但 $\langle 1, \mathrm{i} \rangle = \bar{\mathrm{i}} = -\mathrm{i} \ne 0$。

## 12.3. 标准正交基与酉矩阵

**定义 12.3.1** 若内积空间 $V$ 中的向量 $u_1, \dots, u_k$ 满足 $\langle u_i, u_j \rangle = \delta_{ij}$，则称它们是标准正交向量组；若 $V$ 是有限维的且 $k = \dim V$，则称 $u_1, \dots, u_k$ 是 $V$ 的一组标准正交基。

**性质 12.3.1** 设 $u_1, \dots, u_k$ 是标准正交向量组。

1. $u_1, \dots, u_k$ 线性无关：若 $\sum c_ju_j = 0$，与 $u_i$ 作内积得 $c_i = 0$；
2. 若 $v = x_1u_1 + \cdots + x_ku_k$，则 $x_i = \langle v, u_i \rangle$；
3. 若 $v = \sum x_iu_i$，$w = \sum y_iu_i$，则 $\langle v, w \rangle = \sum_i x_i\bar y_i = \boldsymbol{x}^{\mathsf T}\bar{\boldsymbol{y}}$，$\|v\|^2 = \sum|x_i|^2$。

所以在**标准正交基**下，坐标只需作内积，内积只需对坐标作标准内积：抽象的酉空间与 $\mathbb{C}^n$ 在计算上没有区别。

**例 12.3.1** 设 $\omega = \mathrm{e}^{2\pi \mathrm{i}/3}$，$\mathbb{C}^3$ 取标准内积。向量

$$
\boldsymbol{v}_1 = \tfrac{1}{\sqrt3}(1, 1, 1)^{\mathsf T}, \qquad \boldsymbol{v}_2 = \tfrac{1}{\sqrt3}(1, \omega, \omega^2)^{\mathsf T}, \qquad \boldsymbol{v}_3 = \tfrac{1}{\sqrt3}(1, \omega^2, \omega^4)^{\mathsf T}
$$

是标准正交基。例如 $\langle \boldsymbol{v}_2, \boldsymbol{v}_1 \rangle = \frac13(1 + \omega + \omega^2) = 0$，$\langle \boldsymbol{v}_3, \boldsymbol{v}_2 \rangle = \frac13(1 + \omega^2\bar\omega + \omega^4\bar\omega^2) = \frac13(1 + \omega + \omega^2) = 0$（$\bar\omega = \omega^2$，$\omega^3 = 1$），$\langle \boldsymbol{v}_2, \boldsymbol{v}_2 \rangle = \frac13(1 + 1 + 1) = 1$。

**例 12.3.2** 在 $C[-\pi, \pi]$ 上取积分内积，函数组

$$
\frac{1}{\sqrt{2\pi}}, \quad \frac{\cos x}{\sqrt\pi}, \quad \frac{\sin x}{\sqrt\pi}, \quad \frac{\cos 2x}{\sqrt\pi}, \quad \frac{\sin 2x}{\sqrt\pi}, \quad \dots
$$

是标准正交向量组（例如 $\int_{-\pi}^\pi \sin x\cos x\,\mathrm{d}x = \frac12\int_{-\pi}^\pi \sin 2x\,\mathrm{d}x = 0$）。性质 12.3.1 的第 2 条给出的坐标就是 Fourier 系数。

在 $\mathbb{C}^n$ 中，设 $A = (\boldsymbol{u}_1, \dots, \boldsymbol{u}_n)$。$\boldsymbol{u}_1, \dots, \boldsymbol{u}_n$ 是标准正交基 $\Leftrightarrow$ $\boldsymbol{u}_j^{\mathsf H}\boldsymbol{u}_i = \delta_{ij}$ $\Leftrightarrow$ $A^{\mathsf H}A = I_n$。实情形就是**正交矩阵**。

**定义 12.3.2（酉矩阵）** 满足 $A^{\mathsf H}A = AA^{\mathsf H} = I_n$（即 $A^{-1} = A^{\mathsf H}$）的复方阵 $A$ 称为**酉矩阵**。

**性质 12.3.2** 设 $A, B$ 是 $n$ 阶酉矩阵。

1. $A$ 的列向量（行向量）构成 $\mathbb{C}^n$ 的标准正交基；
2. $AB$、$A^{-1} = A^{\mathsf H}$ 也是酉矩阵，$n$ 阶酉矩阵全体构成群 $U(n)$（[1.3.5](/1.3.5)）；
3. $\langle A\boldsymbol{x}, A\boldsymbol{y} \rangle = \langle \boldsymbol{x}, \boldsymbol{y} \rangle$，$\|A\boldsymbol{x}\| = \|\boldsymbol{x}\|$；
4. $A$ 的特征值的模为 $1$，$|\det A| = 1$。

**证明** 3：$\langle A\boldsymbol{x}, A\boldsymbol{y} \rangle = \boldsymbol{y}^{\mathsf H}A^{\mathsf H}A\boldsymbol{x} = \boldsymbol{y}^{\mathsf H}\boldsymbol{x}$。4：设 $A\boldsymbol{x} = \lambda \boldsymbol{x}$，$\boldsymbol{x} \ne \boldsymbol{0}$，由 3，$\|\boldsymbol{x}\| = \|A\boldsymbol{x}\| = |\lambda|\,\|\boldsymbol{x}\|$，故 $|\lambda| = 1$；$|\det A|$ 是特征值之模的乘积。 $\square$

**例 12.3.3**

1. 若 $Q$ 是实正交矩阵，$|z| = 1$，则 $zQ$ 是酉矩阵：$(zQ)^{\mathsf H}(zQ) = \bar zzQ^{\mathsf T}Q = I$。
2. 若 $A^{\mathsf H} = A$，则 $\mathrm{e}^{\mathrm{i}A}$ 是酉矩阵：由幂级数定义 $(\mathrm{e}^{\mathrm{i}A})^{\mathsf H} = \mathrm{e}^{(\mathrm{i}A)^{\mathsf H}} = \mathrm{e}^{-\mathrm{i}A}$，而 $\mathrm{i}A$ 与 $-\mathrm{i}A$ 可交换，$\mathrm{e}^{-\mathrm{i}A}\mathrm{e}^{\mathrm{i}A} = \mathrm{e}^O = I$（[第 11 章](/2.1.11)定理 11.8.1）。这是 $|\mathrm{e}^{\mathrm{i}\theta}| = 1$（$\theta$ 实）的矩阵版本。
3. 例 12.3.1 的三个向量作为列，得到酉矩阵 $F_3 = \frac{1}{\sqrt3}(\omega^{jk})_{j,k=0,1,2}$。一般地 $F_n = \frac{1}{\sqrt n}(\omega_n^{jk})$（$\omega_n = \mathrm{e}^{2\pi \mathrm{i}/n}$）是离散 Fourier 变换的矩阵。直接计算 $F_n\boldsymbol{x}$ 需要 $n^2$ 次乘法，快速 Fourier 变换利用 $F_n$ 的分块结构把代价降到 $O(n\log n)$。

## 12.4. Gram–Schmidt 正交化

**算法 12.4.1（Gram–Schmidt 正交化）** 输入内积空间 $V$ 中线性无关的 $v_1, \dots, v_k$。

1. $w_1 = v_1$，$q_1 = w_1 / \|w_1\|$；
2. 对 $j = 2, \dots, k$：$w_j = v_j - \sum_{i=1}^{j-1}\langle v_j, q_i \rangle q_i$（减去 $v_j$ 在 $\operatorname{span}\{q_1, \dots, q_{j-1}\}$ 上的投影），$q_j = w_j / \|w_j\|$。

输出标准正交向量组 $q_1, \dots, q_k$，且对每个 $l \le k$，$\operatorname{span}\{q_1, \dots, q_l\} = \operatorname{span}\{v_1, \dots, v_l\}$。

正确性的证明与 [第 4 章](/2.1.4)相同：$\langle w_j, q_l \rangle = \langle v_j, q_l \rangle - \langle v_j, q_l \rangle = 0$（$l < j$），$w_j \ne 0$ 是因为 $v_j \notin \operatorname{span}\{v_1, \dots, v_{j-1}\}$。复情形要注意系数是 $\langle v_j, q_i \rangle$ 而不是 $\langle q_i, v_j \rangle$，二者互为共轭。由此得到：

**定理 12.4.1** 有限维内积空间都有标准正交基，且任一标准正交向量组都可以扩充为标准正交基。在矩阵语言下，列满秩的 $A = (\boldsymbol{v}_1, \dots, \boldsymbol{v}_k) \in \mathbb{C}^{n \times k}$ 可以分解为 $A = QR$，$Q^{\mathsf H}Q = I_k$，$R$ 是对角元为正数的上三角阵，$r_{ij} = \langle \boldsymbol{v}_j, \boldsymbol{q}_i \rangle = \boldsymbol{q}_i^{\mathsf H}\boldsymbol{v}_j$（$i < j$），$r_{jj} = \|w_j\|$。

**例 12.4.1** $\mathbb{C}^3$ 取标准内积，$\boldsymbol{v}_1 = (1, 0, \mathrm{i})^{\mathsf T}$，$\boldsymbol{v}_2 = (-1, \mathrm{i}, 1)^{\mathsf T}$，$\boldsymbol{v}_3 = (1, -1, 1)^{\mathsf T}$。

1. $\|\boldsymbol{v}_1\|^2 = 1 + 0 + |\mathrm{i}|^2 = 2$，$\boldsymbol{q}_1 = \frac{1}{\sqrt2}(1, 0, \mathrm{i})^{\mathsf T}$。
2. $\langle \boldsymbol{v}_2, \boldsymbol{q}_1 \rangle = \frac{1}{\sqrt2}(-1 \cdot 1 + 1 \cdot \bar{\mathrm{i}}) = \frac{-1 - \mathrm{i}}{\sqrt2}$，$\boldsymbol{w}_2 = \boldsymbol{v}_2 - \langle \boldsymbol{v}_2, \boldsymbol{q}_1 \rangle \boldsymbol{q}_1 = \left(\frac{-1 + \mathrm{i}}{2}, \mathrm{i}, \frac{1 + \mathrm{i}}{2}\right)^{\mathsf T}$，$\|\boldsymbol{w}_2\|^2 = 2$，$\boldsymbol{q}_2 = \boldsymbol{w}_2 / \sqrt2$。
3. $\boldsymbol{w}_3 = \boldsymbol{v}_3 - \langle \boldsymbol{v}_3, \boldsymbol{q}_1 \rangle \boldsymbol{q}_1 - \langle \boldsymbol{v}_3, \boldsymbol{q}_2 \rangle \boldsymbol{q}_2 = \left(\frac{1 + \mathrm{i}}{2}, -1, \frac{1 - \mathrm{i}}{2}\right)^{\mathsf T}$，$\|\boldsymbol{w}_3\|^2 = 2$，$\boldsymbol{q}_3 = \boldsymbol{w}_3 / \sqrt2$。

可以验证 $\langle \boldsymbol{w}_3, \boldsymbol{q}_1 \rangle = \frac{1}{\sqrt2}\left(\frac{1 + \mathrm{i}}{2} + \frac{1 - \mathrm{i}}{2}\cdot(-\mathrm{i})\right) = 0$。课件此处把 $\boldsymbol{w}_3$ 的第三个分量写成 $\frac{-1 - \mathrm{i}}{2}$，那样 $\langle \boldsymbol{w}_3, \boldsymbol{v}_1 \rangle = \mathrm{i} \ne 0$，应为 $\frac{1 - \mathrm{i}}{2}$。

**例 12.4.2** 在 $\mathcal{P}_2(\mathbb{R}) = \{a_0 + a_1x + a_2x^2\}$ 上取 $\langle f, g \rangle = \int_{-1}^1 f(x)g(x)\,\mathrm{d}x$，对 $1, x, x^2$ 正交化：

1. $\|1\|^2 = 2$，$q_1 = \frac{1}{\sqrt2}$；
2. $\langle x, q_1 \rangle = 0$，$w_2 = x$，$\|x\|^2 = \frac23$，$q_2 = \sqrt{\frac32}\,x$；
3. $\langle x^2, q_1 \rangle = \frac{\sqrt2}{3}$，$\langle x^2, q_2 \rangle = 0$，$w_3 = x^2 - \frac13$，$\|w_3\|^2 = \int_{-1}^1(x^2 - \frac13)^2\,\mathrm{d}x = \frac{8}{45}$，$q_3 = \sqrt{\frac{45}{8}}\left(x^2 - \frac13\right)$。

$q_1, q_2, q_3$ 是归一化的 Legendre 多项式（Legendre polynomials）$1, x, \frac12(3x^2 - 1)$。继续对 $x^3, x^4, \dots$ 正交化就得到全部 Legendre 多项式，它们在逼近论与偏微分方程中反复出现。

数值计算中，经典 Gram–Schmidt 会因舍入误差逐渐失去正交性，实践中用修正的 Gram–Schmidt 或 **Householder 变换**（[第 4 章](/2.1.4)）计算 QR 分解。

## 12.5. 正交补与正交投影

**定义 12.5.1（正交补）** 设 $V$ 是内积空间，$W$ 是子空间。称 $W^\perp = \{v \in V \mid \langle v, w \rangle = 0, \forall w \in W\}$ 为 $W$ 的**正交补**，它是 $V$ 的子空间。

**例 12.5.1** 在 $\mathbb{R}^n$ 中（标准内积），$\mathcal{R}(A)^\perp = \mathcal{N}(A^{\mathsf T})$，$\mathcal{R}(A^{\mathsf T})^\perp = \mathcal{N}(A)$。在 $\mathbb{C}^n$ 中要换成共轭转置：

$$
\boldsymbol{v} \in \mathcal{R}(A)^\perp \Leftrightarrow \langle A\boldsymbol{u}, \boldsymbol{v} \rangle = \boldsymbol{v}^{\mathsf H}A\boldsymbol{u} = (A^{\mathsf H}\boldsymbol{v})^{\mathsf H}\boldsymbol{u} = 0, \ \forall \boldsymbol{u} \Leftrightarrow A^{\mathsf H}\boldsymbol{v} = \boldsymbol{0},
$$

所以 $\mathcal{R}(A)^\perp = \mathcal{N}(A^{\mathsf H})$，$\mathcal{R}(A^{\mathsf H})^\perp = \mathcal{N}(A)$。这解释了[第 10 章](/2.1.10)例 10.1.2 中的现象：复矩阵的 $\mathcal{N}(A^{\mathsf T})$ 未必与 $\mathcal{R}(A)$ 互补。

**定义 12.5.2（正交投影）** 设 $W$ 是内积空间 $V$ 的子空间，$v \in V$。若 $v_p \in W$ 且 $v - v_p \in W^\perp$，则称 $v_p$ 为 $v$ 在 $W$ 上的**正交投影**。

**定理 12.5.1** 设 $V$ 是内积空间，$W$ 是有限维子空间，$e_1, \dots, e_k$ 是 $W$ 的标准正交基。

1. 任意 $v \in V$ 在 $W$ 上的正交投影存在且唯一，$v_p = \langle v, e_1 \rangle e_1 + \cdots + \langle v, e_k \rangle e_k$；
2. （最佳逼近）$\|v - w\| \ge \|v - v_p\|$ 对一切 $w \in W$ 成立，等号仅在 $w = v_p$ 时成立；
3. $W \cap W^\perp = \{0\}$，$V = W \oplus W^\perp$；若 $V$ 有限维，则 $(W^\perp)^\perp = W$。

**证明** 1：$\langle v - v_p, e_i \rangle = \langle v, e_i \rangle - \langle v, e_i \rangle = 0$，所以 $v - v_p \in W^\perp$。唯一性：两个投影之差同时属于 $W$ 与 $W^\perp$，与自身正交，为零。2：$v - w = (v - v_p) + (v_p - w)$，两项分别属于 $W^\perp$ 与 $W$，由勾股定理 $\|v - w\|^2 = \|v - v_p\|^2 + \|v_p - w\|^2$。3：$w \in W \cap W^\perp$ 则 $\langle w, w \rangle = 0$；由 1，$v = v_p + (v - v_p) \in W + W^\perp$。有限维时 $\dim W^\perp = \dim V - \dim W$，于是 $\dim(W^\perp)^\perp = \dim W$，又显然 $W \subseteq (W^\perp)^\perp$，故相等（课件将此留作作业）。 $\square$

**最小二乘法**是正交投影的特例：$\min_x\|\boldsymbol{b} - A\boldsymbol{x}\|$ 在 $A\boldsymbol{x}$ 等于 $\boldsymbol{b}$ 在 $\mathcal{R}(A)$ 上的投影时取到，条件 $\boldsymbol{b} - A\boldsymbol{x} \in \mathcal{R}(A)^\perp = \mathcal{N}(A^{\mathsf H})$ 就是复情形的**正规方程** $A^{\mathsf H}A\boldsymbol{x} = A^{\mathsf H}\boldsymbol{b}$。若已有 $\mathcal{R}(A)$ 的标准正交基（例如 $A = QR$ 中 $Q$ 的列），投影只需作内积：$\boldsymbol{b}_p = QQ^{\mathsf H}\boldsymbol{b}$，不必解方程组。

## 12.6. Riesz 表示定理与伴随变换

[第 8 章](/2.1.8)说明了 $\mathbb{R}^n$ 上的每个**线性函数**都可以写成与一个固定向量作内积。这对任意有限维内积空间成立。

**定理 12.6.1（Riesz 表示定理）** 设 $V$ 是有限维内积空间（$\mathbb{F} = \mathbb{R}$ 或 $\mathbb{C}$），$f\colon V \to \mathbb{F}$ 是线性函数，则存在唯一的 $u \in V$ 使 $f(v) = \langle v, u \rangle$ 对一切 $v \in V$ 成立。设 $e_1, \dots, e_n$ 是标准正交基，则 $u = \overline{f(e_1)}e_1 + \cdots + \overline{f(e_n)}e_n$。

**证明** 对 $v = \sum_i\langle v, e_i \rangle e_i$，$f(v) = \sum_i\langle v, e_i \rangle f(e_i) = \left\langle v, \sum_i\overline{f(e_i)}e_i \right\rangle$（内积对第二个变量共轭线性）。唯一性：若 $\langle v, u_1 - u_2 \rangle = 0$ 对一切 $v$ 成立，取 $v = u_1 - u_2$。 $\square$

课件把 $u$ 写成 $\sum f(e_i)e_i$，这只在实情形正确；复情形系数要取共轭。也因此，映射 $u \mapsto \langle \cdot, u \rangle$ 从 $V$ 到**对偶空间** $V^*$ 是双射，实情形是线性同构，复情形是共轭线性的（$cu \mapsto \bar c\langle \cdot, u \rangle$）。

**例 12.6.1** 在例 12.4.2 的 $\mathcal{P}_2(\mathbb{R})$ 中，求 $u(x)$ 使 $\langle p, u \rangle = \int_{-1}^1 p(t)\cos(\pi t)\,\mathrm{d}t$ 对一切 $p \in \mathcal{P}_2(\mathbb{R})$ 成立。右边是线性函数 $f$，用例 12.4.2 的标准正交基 $q_1, q_2, q_3$：$f(q_1) = \frac{1}{\sqrt2}\int_{-1}^1\cos\pi t\,\mathrm{d}t = 0$，$f(q_2) = 0$（奇函数），$\int_{-1}^1 t^2\cos\pi t\,\mathrm{d}t = -\frac{4}{\pi^2}$，$f(q_3) = -\sqrt{\frac{45}{8}}\cdot\frac{4}{\pi^2}$。所以

$$
u(x) = f(q_3)q_3 = -\frac{45}{2\pi^2}\left(x^2 - \frac13\right).
$$

几何上，$u$ 就是 $\cos\pi x$（在更大的连续函数空间中）在 $\mathcal{P}_2(\mathbb{R})$ 上的正交投影，即 $\cos\pi x$ 在 $[-1, 1]$ 上的最佳平方逼近二次多项式：对 $p \in \mathcal{P}_2$，$\langle p, \cos\pi x \rangle = \langle p, u \rangle$。

**定义 12.6.1（伴随变换）** 设 $V$ 是内积空间，$T\colon V \to V$ 是线性变换。若线性变换 $T^*\colon V \to V$ 满足 $\langle T\alpha, \beta \rangle = \langle \alpha, T^*\beta \rangle$ 对一切 $\alpha, \beta \in V$ 成立，则称 $T^*$ 为 $T$ 的**伴随变换**（也称伴随算子、共轭变换）。

伴随变换与行列式一章的**伴随矩阵**（$\operatorname{adj}A$）是两回事；它与第 8 章**对偶映射** $T^{\mathsf t}\colon V^* \to V^*$ 的关系见 [第 13 章](/2.1.13)。

**定理 12.6.2** 设 $V$ 是有限维内积空间，$T\colon V \to V$ 是线性变换，则 $T^*$ 存在且唯一。若 $T$ 在标准正交基 $e_1, \dots, e_n$ 下的矩阵为 $A$，则 $T^*$ 在这组基下的矩阵为 $A^{\mathsf H}$（实情形为 $A^{\mathsf T}$）。

**证明** 固定 $\beta$，$\alpha \mapsto \langle T\alpha, \beta \rangle$ 是线性函数，由 Riesz 表示定理存在唯一的向量，记作 $T^*\beta$，使 $\langle T\alpha, \beta \rangle = \langle \alpha, T^*\beta \rangle$。由唯一性可验证 $T^*$ 是线性的。矩阵：$T^*e_j$ 的第 $i$ 个坐标是 $\langle T^*e_j, e_i \rangle = \overline{\langle e_i, T^*e_j \rangle} = \overline{\langle Te_i, e_j \rangle} = \bar a_{ji}$。 $\square$

只有在标准正交基下，伴随的矩阵才是 $A^{\mathsf H}$。在度量矩阵为 $G$ 的一般基下，由 $\langle T\alpha, \beta \rangle = \boldsymbol{x}^{\mathsf T}A^{\mathsf T}G\bar{\boldsymbol{y}}$ 可得 $T^*$ 的矩阵为 $\bar G^{-1}A^{\mathsf H}\bar G$。

**例 12.6.2** $\mathbb{C}^3$ 取标准内积，$T(x_1, x_2, x_3)^{\mathsf T} = (x_1 - \mathrm{i}x_2, x_2 + \mathrm{i}x_3, x_3 + \mathrm{i}x_1)^{\mathsf T}$，矩阵 $A = \begin{bmatrix} 1 & -\mathrm{i} & 0 \\ 0 & 1 & \mathrm{i} \\ \mathrm{i} & 0 & 1 \end{bmatrix}$，则 $T^*\boldsymbol{y} = A^{\mathsf H}\boldsymbol{y} = (y_1 - \mathrm{i}y_3, \mathrm{i}y_1 + y_2, -\mathrm{i}y_2 + y_3)^{\mathsf T}$。

**性质 12.6.1** 设 $V$ 是有限维内积空间，$T, T_1, T_2$ 是 $V$ 上的线性变换，$c \in \mathbb{F}$。

1. $(T^*)^* = T$，$(T_1 + T_2)^* = T_1^* + T_2^*$，$(cT)^* = \bar cT^*$，$(T_1T_2)^* = T_2^*T_1^*$；
2. 若 $T$ 可逆，则 $T^*$ 可逆，$(T^*)^{-1} = (T^{-1})^*$；
3. 若 $W$ 是 $T$-**不变子空间**，则 $W^\perp$ 是 $T^*$-不变子空间；
4. 若 $\lambda$ 是 $T$ 的特征值，则 $\bar\lambda$ 是 $T^*$ 的特征值。

**证明** 1 中第一式：$\langle T^*\alpha, \beta \rangle = \overline{\langle \beta, T^*\alpha \rangle} = \overline{\langle T\beta, \alpha \rangle} = \langle \alpha, T\beta \rangle$。其余由定义直接验证。3：设 $u \in W^\perp$，对任意 $w \in W$，$\langle w, T^*u \rangle = \langle Tw, u \rangle = 0$，因为 $Tw \in W$。4：$\det(\bar\lambda I - A^{\mathsf H}) = \overline{\det(\lambda I - A)} = 0$。 $\square$

**例 12.6.3** 设 $V = W \oplus W^\perp$，$P$ 是到 $W$ 上的正交投影。取 $W$ 的标准正交基 $e_1, \dots, e_k$ 并扩充为 $V$ 的标准正交基，$P$ 的矩阵为 $\operatorname{diag}(I_k, O)$，它的共轭转置是自身，所以 $P^* = P$。

## 12.7. 保积变换

**定义 12.7.1（保积变换）** 设 $V$ 是内积空间。若线性变换 $T\colon V \to V$ 满足 $\langle T\alpha, T\beta \rangle = \langle \alpha, \beta \rangle$ 对一切 $\alpha, \beta$ 成立，则称 $T$ 为**保积变换**。欧氏空间上的保积变换称为**正交变换**，酉空间上的保积变换称为**酉变换**。

保积变换保持长度、角度与正交性。线性的要求其实可以去掉：若映射 $T$ 保持内积，把 $\|T(\alpha + \beta) - T\alpha - T\beta\|^2$ 展开成像之间的内积，再换成原像之间的内积，就得到 $\|(\alpha + \beta) - \alpha - \beta\|^2 = 0$；数乘同理。

**例 12.7.1**

1. $\mathbb{R}^2$ 上的旋转 $\boldsymbol{x} \mapsto \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}\boldsymbol{x}$：$\langle A\boldsymbol{x}, A\boldsymbol{y} \rangle = \boldsymbol{x}^{\mathsf T}A^{\mathsf T}A\boldsymbol{y} = \boldsymbol{x}^{\mathsf T}\boldsymbol{y}$。
2. $\mathbb{C}^n$ 上 $\boldsymbol{\alpha} \mapsto U\boldsymbol{\alpha}$，$U$ 是酉矩阵（性质 12.3.2）。
3. $\mathbb{C}^{n\times n}$ 取 Frobenius 内积，$U$ 是固定的酉矩阵，$T(A) = UA$：$\langle UA, UB \rangle = \operatorname{tr}(UAB^{\mathsf H}U^{\mathsf H}) = \operatorname{tr}(AB^{\mathsf H}U^{\mathsf H}U) = \langle A, B \rangle$。

**定理 12.7.1** 有限维内积空间上的保积变换是线性同构。

**证明** 若 $T\alpha = 0$，则 $\langle \alpha, \alpha \rangle = \langle T\alpha, T\alpha \rangle = 0$，$\alpha = 0$，故 $\mathcal{N}(T) = \{0\}$；由**秩–零化度定理**，$T$ 也是满射。 $\square$

**引理 12.7.1** 设 $\alpha_1, \dots, \alpha_n$ 是 $n$ 维内积空间 $V$ 的标准正交基，$(\beta_1, \dots, \beta_n) = (\alpha_1, \dots, \alpha_n)P$。则 $\beta_1, \dots, \beta_n$ 是标准正交基 $\Leftrightarrow$ **过渡矩阵** $P$ 是酉矩阵（实情形为正交矩阵）。

**证明** $\beta_j = \sum_k p_{kj}\alpha_k$，由性质 12.3.1 的第 3 条，$\langle \beta_i, \beta_j \rangle = \sum_k p_{ki}\bar p_{kj}$，它是 $P$ 的第 $i$ 列与第 $j$ 列在 $\mathbb{C}^n$ 中的标准内积。所以 $\langle \beta_i, \beta_j \rangle = \delta_{ij}$ $\Leftrightarrow$ $P$ 的列是标准正交基 $\Leftrightarrow$ $P$ 是酉矩阵。 $\square$

例如在 $\mathbb{C}^n$ 中，若 $A = (\boldsymbol{\alpha}_1, \dots, \boldsymbol{\alpha}_n)$、$B = (\boldsymbol{\beta}_1, \dots, \boldsymbol{\beta}_n)$ 都是酉矩阵，则从 $\{\boldsymbol{\alpha}_i\}$ 到 $\{\boldsymbol{\beta}_i\}$ 的过渡矩阵 $P = A^{-1}B = A^{\mathsf H}B$ 是酉矩阵。

**定理 12.7.2** 设 $V$ 是有限维内积空间，$T\colon V \to V$ 是线性变换。以下条件等价：

1. $T$ 是保积变换；
2. $TT^* = T^*T = \mathrm{id}_V$，即 $T^* = T^{-1}$；
3. $T$ 保持长度：$\|T\alpha\| = \|\alpha\|$ 对一切 $\alpha$ 成立；
4. $T$ 把某一组（从而任意一组）标准正交基映为标准正交基；
5. $T$ 在某一组标准正交基下的矩阵是酉矩阵（实情形为正交矩阵）。

**证明** 1 $\Leftrightarrow$ 2：$\langle T\alpha, T\beta \rangle = \langle \alpha, T^*T\beta \rangle$，它对一切 $\alpha$ 等于 $\langle \alpha, \beta \rangle$ 当且仅当 $T^*T\beta = \beta$；有限维时 $T^*T = \mathrm{id}$ 推出 $TT^* = \mathrm{id}$。1 $\Rightarrow$ 3 显然。3 $\Rightarrow$ 1 用极化恒等式，内积可以由长度表示：

$$
\langle \alpha, \beta \rangle = \frac14\left(\|\alpha + \beta\|^2 - \|\alpha - \beta\|^2\right) \ (\text{实}), \qquad \langle \alpha, \beta \rangle = \frac14\sum_{k=0}^3 \mathrm{i}^k\|\alpha + \mathrm{i}^k\beta\|^2 \ (\text{复}).
$$

1 $\Rightarrow$ 4：$\langle Te_i, Te_j \rangle = \langle e_i, e_j \rangle = \delta_{ij}$。4 $\Rightarrow$ 1：设 $Te_1, \dots, Te_n$ 标准正交，$\alpha = \sum x_ie_i$，$\beta = \sum y_ie_i$，则 $T\alpha, T\beta$ 在基 $Te_i$ 下的坐标仍是 $\boldsymbol{x}, \boldsymbol{y}$，由性质 12.3.1 的第 3 条，$\langle T\alpha, T\beta \rangle = \boldsymbol{x}^{\mathsf T}\bar{\boldsymbol{y}} = \langle \alpha, \beta \rangle$。4 $\Leftrightarrow$ 5：$(Te_1, \dots, Te_n) = (e_1, \dots, e_n)A$，由引理 12.7.1。 $\square$

**例 12.7.2** 设 $V$ 是 $n$ 维欧氏空间，$u \in V$，$\|u\| = 1$，$T\alpha = \alpha - 2\langle \alpha, u \rangle u$。直接验证：

$$
\langle T\alpha, T\beta \rangle = \langle \alpha, \beta \rangle - 2\langle \alpha, u \rangle\langle u, \beta \rangle - 2\langle \beta, u \rangle\langle \alpha, u \rangle + 4\langle \alpha, u \rangle\langle \beta, u \rangle = \langle \alpha, \beta \rangle.
$$

也可以用定理 12.7.2：把 $u$ 扩充为标准正交基 $e_1 = u, e_2, \dots, e_n$，则 $Te_1 = -e_1$，$Te_j = e_j$（$j \ge 2$），矩阵 $\operatorname{diag}(-1, 1, \dots, 1)$ 是正交矩阵。$T$ 是关于超平面 $u^\perp$ 的镜面反射，在 $\mathbb{R}^n$ 中就是 Householder 变换 $I - 2\boldsymbol{u}\boldsymbol{u}^{\mathsf T}$。

设 $T$ 是欧氏空间上的正交变换，在标准正交基下的矩阵 $A$ 是正交矩阵，$\det A = \pm 1$。$\det A = 1$ 时称 $T$ 为第一类正交变换（旋转），$\det A = -1$ 时称为第二类正交变换。例如 $\mathbb{R}^2$ 上 $\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$ 是第一类的，$\begin{bmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{bmatrix}$（关于倾角为 $\theta/2$ 的直线的反射）是第二类的。所有正交变换构成群，第一类正交变换构成它的子群，对应 [1.3.5](/1.3.5) 中的 $O(n)$ 与 $\operatorname{SO}(n)$；[第 13 章](/2.1.13)将从双线性型的角度重新认识这些群。

## 12.8. 正交相似与酉相似

线性变换 $T$ 在不同的标准正交基下的矩阵有什么关系？设 $v_1, \dots, v_n$ 与 $w_1, \dots, w_n$ 是两组标准正交基，$(w_1, \dots, w_n) = (v_1, \dots, v_n)P$，$T$ 在两组基下的矩阵分别为 $A$、$B$。由引理 12.7.1，$P$ 是酉矩阵，于是

$$
B = P^{-1}AP = P^{\mathsf H}AP.
$$

**定义 12.8.1** 设 $A, B \in \mathbb{C}^{n\times n}$。若存在酉矩阵 $P$ 使 $P^{\mathsf H}AP = B$，则称 $A$ 与 $B$ **酉相似**。实方阵之间的**正交相似**（$P$ 为正交矩阵，$P^{\mathsf T}AP = B$）是它的实版本（[第 7 章](/2.1.7)）。

**定理 12.8.1** 有限维内积空间上的线性变换在不同标准正交基下的矩阵是正交相似（欧氏空间）或酉相似（酉空间）的。反之，与 $A$ 酉相似的每个矩阵都是 $T$ 在某组标准正交基下的矩阵。

于是本章的核心问题有了矩阵形式：$\{P^{\mathsf H}AP \mid P \text{ 是酉矩阵}\}$ 中什么时候有对角阵？酉相似比一般的**相似**更严格，但它有两个优点：$P^{-1} = P^{\mathsf H}$ 不用求逆；酉矩阵保持长度，数值计算中误差不会被放大。

## 12.9. 正规变换

若 $T$ 在标准正交基下的矩阵是对角阵 $\Lambda$，则 $T^*$ 的矩阵是 $\bar\Lambda$，两个对角阵可交换，所以 $TT^* = T^*T$。这个必要条件其实也是充分的。

**定义 12.9.1** 设 $V$ 是酉空间。满足 $TT^* = T^*T$ 的线性变换 $T$ 称为**正规变换**；满足 $AA^{\mathsf H} = A^{\mathsf H}A$ 的复方阵 $A$ 称为**正规矩阵**。

$T$ 是正规变换当且仅当它在标准正交基下的矩阵是正规矩阵。酉矩阵（$A^{\mathsf H}A = I = AA^{\mathsf H}$）、Hermite 矩阵（$A^{\mathsf H} = A$）、反 Hermite 矩阵（$A^{\mathsf H} = -A$）与对角阵都是正规的，所以酉变换是正规变换的特例，而且是真子类。$\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$ 不是正规的。

**性质 12.9.1** 设 $T$ 是正规变换。

1. 若 $T\alpha = \lambda\alpha$，则 $T^*\alpha = \bar\lambda\alpha$：$T$ 与 $T^*$ 有相同的特征向量，特征值互为共轭；
2. 属于不同特征值的特征向量正交。

**证明** 1：$S = T - \lambda\,\mathrm{id}$ 也是正规的（$S^* = T^* - \bar\lambda\,\mathrm{id}$），对正规变换 $\|S\alpha\|^2 = \langle \alpha, S^*S\alpha \rangle = \langle \alpha, SS^*\alpha \rangle = \|S^*\alpha\|^2$。所以 $S\alpha = 0 \Leftrightarrow S^*\alpha = 0$。2：设 $T\alpha = \lambda\alpha$，$T\beta = \mu\beta$，$\lambda \ne \mu$。由 1，$\lambda\langle \alpha, \beta \rangle = \langle T\alpha, \beta \rangle = \langle \alpha, T^*\beta \rangle = \langle \alpha, \bar\mu\beta \rangle = \mu\langle \alpha, \beta \rangle$，故 $\langle \alpha, \beta \rangle = 0$。 $\square$

为了证明正规变换可以酉对角化，先把 Schur 定理加强为酉三角化。

**定理 12.9.1（推广的 Schur 定理）** 设 $T$ 是 $n$ 维酉空间上的线性变换，则存在标准正交基使 $T$ 的矩阵为上三角阵。矩阵形式：任意 $A \in \mathbb{C}^{n\times n}$ 都酉相似于上三角阵，$U^{\mathsf H}AU = R'$，对角元是 $A$ 的特征值。

**证明** 由 Schur 定理（定理 10.3.1），存在可逆阵 $M$ 使 $N = M^{-1}AM$ 是上三角阵。对 $M$ 作 QR 分解（定理 12.4.1）：$M = UR$，$U$ 是酉矩阵，$R$ 是可逆上三角阵。于是

$$
U^{\mathsf H}AU = U^{-1}AU = R\left(M^{-1}AM\right)R^{-1} = RNR^{-1},
$$

上三角阵的乘积与逆仍是上三角阵。 $\square$

这个证明是"Schur 定理 + QR 分解"的组合：Schur 定理给出一组基 $\boldsymbol{m}_1, \dots, \boldsymbol{m}_n$ 使 $A$ 成为上三角，这等价于子空间 $\operatorname{span}\{\boldsymbol{m}_1\} \subseteq \operatorname{span}\{\boldsymbol{m}_1, \boldsymbol{m}_2\} \subseteq \cdots \subseteq \mathbb{C}^n$ 都是 $A$-不变的；Gram–Schmidt 正交化不改变这串子空间，所以正交化以后的基仍使矩阵为上三角。数值线性代数中计算特征值的 QR 算法，正是以这种酉三角化为目标。

## 12.10. 谱定理

**定理 12.10.1（谱定理）** 设 $T$ 是酉空间 $V$ 上的线性变换。以下条件等价：

1. $T$ 是正规变换；
2. 存在 $V$ 的标准正交基，使 $T$ 的矩阵为对角阵；
3. （矩阵形式）$T$ 在标准正交基下的矩阵 $A$ 酉相似于对角阵：存在酉矩阵 $U$ 使 $U^{\mathsf H}AU = \Lambda = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$。

**证明** 2 $\Leftrightarrow$ 3 是定理 12.8.1。3 $\Rightarrow$ 1：$A = U\Lambda U^{\mathsf H}$，$AA^{\mathsf H} = U\Lambda\bar\Lambda U^{\mathsf H} = U\bar\Lambda\Lambda U^{\mathsf H} = A^{\mathsf H}A$。

1 $\Rightarrow$ 3：由定理 12.9.1，$U^{\mathsf H}AU = B$ 是上三角阵，且 $BB^{\mathsf H} = U^{\mathsf H}AA^{\mathsf H}U = U^{\mathsf H}A^{\mathsf H}AU = B^{\mathsf H}B$，即 $B$ 也是正规的。比较 $BB^{\mathsf H}$ 与 $B^{\mathsf H}B$ 的 $(1, 1)$ 元：

$$
|b_{11}|^2 + |b_{12}|^2 + \cdots + |b_{1n}|^2 = |b_{11}|^2,
$$

所以 $b_{12} = \cdots = b_{1n} = 0$。再比较 $(2, 2)$ 元：$|b_{22}|^2 + \cdots + |b_{2n}|^2 = |b_{12}|^2 + |b_{22}|^2 = |b_{22}|^2$，得 $b_{23} = \cdots = b_{2n} = 0$。依次进行，$B$ 是对角阵。 $\square$

写成外积的形式，$A = \sum_i\lambda_i\boldsymbol{u}_i\boldsymbol{u}_i^{\mathsf H}$，$\boldsymbol{u}_i$ 是 $U$ 的列；把同一特征值的项合并，$A = \sum_j\mu_jP_j$，$P_j$ 是到特征子空间 $V_{\mu_j}$ 上的正交投影（例 12.6.3），$\sum_j P_j = I$，$P_jP_k = O$（$j \ne k$）。这就是正规矩阵的谱分解。

**推论 12.10.1** 酉矩阵可以酉对角化，对角元的模为 $1$；Hermite 矩阵可以酉对角化，对角元为实数；反 Hermite 矩阵可以酉对角化，对角元为纯虚数。

**证明** 它们都是正规矩阵。由性质 12.9.1 的第 1 条，特征值满足：酉矩阵 $\bar\lambda = \lambda^{-1}$；Hermite 矩阵 $\bar\lambda = \lambda$；反 Hermite 矩阵 $\bar\lambda = -\lambda$。 $\square$

**推论 12.10.2** 实对称矩阵 $A$ 正交相似于实对角阵：存在实正交矩阵 $Q$ 使 $Q^{\mathsf T}AQ$ 是实对角阵。

**证明** $A$ 是 Hermite 矩阵，由推论 12.10.1，它的特征值都是实数。对每个实特征值 $\mu$，$A - \mu I$ 是实矩阵，$\mathcal{N}(A - \mu I)$ 有一组实的基，在 $\mathbb{R}^n$ 中作 Gram–Schmidt 正交化得到实的标准正交基；不同特征子空间互相正交（性质 12.9.1 的第 2 条），维数之和为 $n$（$A$ 可以酉对角化，所以几何重数等于代数重数）。合起来就是 $\mathbb{R}^n$ 的标准正交基，它们作为列构成 $Q$。 $\square$

这就是 [第 7 章](/2.1.7)定理 7.1.1 的实对称矩阵谱分解，这里从复的谱定理推出，证明中的"特征值为实数"一步正是复数域带来的方便。

**推论 12.10.3** 既正规又幂零的矩阵是零矩阵：它酉相似于对角阵，而对角元（特征值）全为零。

**例 12.10.1** 2 阶实正规矩阵。设 $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix} \in \mathbb{R}^{2\times 2}$，比较 $AA^{\mathsf T}$ 与 $A^{\mathsf T}A$ 得 $b^2 = c^2$ 与 $(c - b)(a - d) = 0$，所以 $A$ 正规当且仅当 $A$ 对称（$b = c$），或 $A = \begin{bmatrix} a & b \\ -b & a \end{bmatrix}$（$b \ne 0$）。后者是复数 $a - b\mathrm{i}$ 的矩阵表示（[第 9 章](/2.1.9)），特征值 $a \pm b\mathrm{i}$，对应的特征向量 $\frac{1}{\sqrt2}(1, \pm \mathrm{i})^{\mathsf T}$ 正交，$U = \frac{1}{\sqrt2}\begin{bmatrix} 1 & 1 \\ \mathrm{i} & -\mathrm{i} \end{bmatrix}$ 是酉矩阵，$U^{\mathsf H}AU = \operatorname{diag}(a + b\mathrm{i}, a - b\mathrm{i})$。它在 $\mathbb{R}^2$ 中没有实特征向量，不能正交对角化，但可以酉对角化。

正规矩阵酉对角化的计算是两个标准问题的组合：

**算法 12.10.1（正规矩阵的酉对角化）** 输入正规矩阵 $A \in \mathbb{C}^{n\times n}$。

1. 求特征值 $\mu_1, \dots, \mu_s$ 及代数重数。
2. 对每个 $\mu_j$，解 $(A - \mu_jI)\boldsymbol{x} = \boldsymbol{0}$ 得特征子空间的一组基，对它作 Gram–Schmidt 正交化，得到标准正交基。
3. 把所有这些向量排成 $U$。不同特征子空间自动正交（性质 12.9.1），所以 $U$ 是酉矩阵，$U^{\mathsf H}AU = \Lambda$。

**例 12.10.2** $A = \begin{bmatrix} 0 & 1 & 0 \\ -1 & 0 & 0 \\ 0 & 0 & \mathrm{i} \end{bmatrix}$。$A^{\mathsf H} = \begin{bmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & -\mathrm{i} \end{bmatrix}$，$A^{\mathsf H}A = I = AA^{\mathsf H}$，$A$ 是酉矩阵，从而正规。$\det(\lambda I - A) = (\lambda^2 + 1)(\lambda - \mathrm{i})$，特征值 $\mathrm{i}$（二重）与 $-\mathrm{i}$。

1. $\lambda = \mathrm{i}$：$(A - \mathrm{i}I)\boldsymbol{x} = \boldsymbol{0}$ 的基为 $(-\mathrm{i}, 1, 0)^{\mathsf T}$、$(0, 0, 1)^{\mathsf T}$，它们已经正交，单位化得 $\boldsymbol{u}_1 = \frac{1}{\sqrt2}(-\mathrm{i}, 1, 0)^{\mathsf T}$，$\boldsymbol{u}_2 = (0, 0, 1)^{\mathsf T}$。若取的基不正交（例如 $(-\mathrm{i}, 1, 1)^{\mathsf T}$ 与 $(0, 0, 1)^{\mathsf T}$），就需要先作 Gram–Schmidt。
2. $\lambda = -\mathrm{i}$：基为 $(\mathrm{i}, 1, 0)^{\mathsf T}$，$\boldsymbol{u}_3 = \frac{1}{\sqrt2}(\mathrm{i}, 1, 0)^{\mathsf T}$，它与 $\boldsymbol{u}_1, \boldsymbol{u}_2$ 自动正交。
3. $U = (\boldsymbol{u}_1, \boldsymbol{u}_2, \boldsymbol{u}_3)$，$U^{\mathsf H}AU = \operatorname{diag}(\mathrm{i}, \mathrm{i}, -\mathrm{i})$。

数值软件不按算法 12.10.1 计算（重特征值的特征子空间在浮点运算中难以准确求出），而是直接计算推广的 Schur 定理中的酉三角化；对正规矩阵，得到的三角阵就是对角阵。

```python
import numpy as np
from scipy.linalg import schur

A = np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1j]])
print(np.allclose(A @ A.conj().T, A.conj().T @ A))   # True: A is normal
T, U = schur(A, output='complex')                    # A = U T U^H, U unitary
print(np.round(T, 12))                               # T is diagonal
print(np.allclose(U @ T @ U.conj().T, A))            # True
```

## 小结

| | $\mathbb{R}^n$（第 4、7 章） | 欧氏空间 | 酉空间 |
|---|---|---|---|
| 内积 | $\boldsymbol{\alpha}^{\mathsf T}\boldsymbol{\beta}$ | 对称、双线性、正定 | 共轭对称、对第一变量线性、正定 |
| 基下的表示 | — | $\boldsymbol{x}^{\mathsf T}G\boldsymbol{y}$，$G$ 实对称正定 | $\boldsymbol{x}^{\mathsf T}G\bar{\boldsymbol{y}}$，$G$ 正定 Hermite |
| 保持内积的矩阵 | 正交矩阵 | 正交矩阵（标准正交基下） | 酉矩阵 $A^{\mathsf H}A = I$ |
| 伴随的矩阵 | $A^{\mathsf T}$ | $A^{\mathsf T}$ | $A^{\mathsf H}$ |
| 可正交（酉）对角化 | 实对称矩阵 | 对称变换 | 正规变换 |

| 结论 | 内容 |
|---|---|
| Cauchy–Schwarz、三角不等式 | 性质 12.2.1，投影证明 |
| Gram–Schmidt | 算法 12.4.1；有限维内积空间有标准正交基；$A = QR$（定理 12.4.1） |
| 正交补与投影 | $V = W \oplus W^\perp$，$v_p = \sum\langle v, e_i \rangle e_i$，最佳逼近（定理 12.5.1）；$\mathcal{R}(A)^\perp = \mathcal{N}(A^{\mathsf H})$ |
| Riesz 表示 | $f = \langle \cdot, u \rangle$，$u = \sum\overline{f(e_i)}e_i$（定理 12.6.1） |
| 伴随 | 存在唯一，标准正交基下矩阵为 $A^{\mathsf H}$（定理 12.6.2） |
| 保积变换 | 五个等价条件（定理 12.7.2）；标准正交基之间的过渡矩阵是酉矩阵 |
| 推广的 Schur 定理 | 任意复方阵酉相似于上三角阵 = Schur 定理 + QR（定理 12.9.1） |
| 谱定理 | 可酉对角化 $\Leftrightarrow$ 正规（定理 12.10.1）；实对称矩阵的谱分解是推论 |
| 酉对角化 | 算法 12.10.1：求特征值，在每个特征子空间中 Gram–Schmidt |

有了标准正交基，坐标、投影、伴随都只需要作内积或共轭转置，不需要解方程组或求逆；这正是正交（酉）方法在数值计算中受欢迎的原因。[下一章](/2.1.13)研究正规变换中特征值为实数的一类（Hermite 变换），并在复数域上重新讨论二次型与奇异值分解。
