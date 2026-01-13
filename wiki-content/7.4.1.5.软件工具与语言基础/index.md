**内容**：Python科学计算栈（NumPy, SciPy）及绘图库（Matplotlib, Seaborn）的极简入门；matlab简介；markdown文档与数学公式撰写规范。

在明确了建模的思想、价值与审美之后，我们将从形而上降至形而下，开始接触实现这些想法的具体工具。工欲善其事，必先利其器。本节将介绍本书，也是现代计算生物学界，最核心、最通用的一套软件工具与语言基础。我们的原则是：**最小化、可移植、聚焦生物建模**。你将不会看到一个庞杂的软件列表，而是一个精心挑选的、能贯穿本书所有章节的核心工具栈。

### 核心哲学：为什么是Python？

在众多编程语言和商业软件中，我们选择**Python**作为本书的唯一核心编程语言，基于以下考量：
*   **生态系统**：Python拥有极其丰富且成熟的科学计算库（NumPy, SciPy），数据可视化库（Matplotlib, Seaborn），以及蓬勃发展的生物信息学/计算生物学专用库（如Biopython）。其生态宛如一个巨大的“零件市场”，几乎所有建模需求都能找到现成的、高质量的“零件”。
*   **可读性与易学性**：Python语法接近自然英语和数学表达式，对初学者友好，能让研究者将精力集中于问题本身，而非语言细节。
*   **通用性与免费开源**：Python是跨平台的（Windows, macOS, Linux），且完全免费。这消除了软件许可的成本和障碍，保证了本书所有代码在任何读者的电脑上都能以相同的方式运行。
*   **社区与未来**：Python拥有全球最大、最活跃的开发者与科学计算社区。这意味着遇到问题时更容易找到解决方案，也意味着相关工具库将持续维护和发展，是面向未来的选择。

**我们的核心工具栈**：`Python` + `NumPy` + `SciPy` + `Matplotlib` (+ `Seaborn`)。掌握这四（五）个库，你就能完成本书90%以上的建模与可视化任务。

### 环境配置：你的数字实验室

在开始编写第一行代码前，你需要建立一个统一的、可复现的计算环境。我们强烈推荐使用**Anaconda**发行版和**Jupyter Lab**（或Jupyter Notebook）作为起点。
*   **Anaconda**：它是一个集成了Python、核心科学计算库和包管理工具`conda`的发行版。一次性安装，免去手动配置各种依赖的烦恼。
*   **Jupyter Lab**：它是一个基于网页的交互式计算环境。你可以将代码、方程、可视化结果和叙述性文字（Markdown）整合在一个文档中，非常适合进行探索性数据分析、建模和生成可重复的研究报告。

**行动建议**：访问Anaconda官网，下载并安装适用于你操作系统的Anaconda发行版。启动后，打开Jupyter Lab，新建一个Python笔记本（Notebook），这就是你的第一个“数字生物建模实验室”。

### Python科学计算基础（极简精华）

我们不会展开完整的Python语法教程，而是聚焦于生物建模中最常用、最必须的部分。

1.  **数据结构：数据的容器**
    *   **列表 (List)**：有序、可变的元素集合。用于存储时间序列数据、一组参数等。
        ```python
        time_points = [0, 1, 2, 3, 4, 5]  # 时间点
        protein_concentration = []          # 一个待填充的空列表，用于存储蛋白质浓度
        ```
    *   **字典 (Dictionary)**：键值对的集合。用于存储模型参数，键（参数名）和值（参数值）的映射非常清晰。
        ```python
        params = {
            'k_transcription': 0.5,   # 转录速率，min^-1
            'd_mRNA': 0.1,            # mRNA降解率，min^-1
            'k_translation': 2.0,     # 翻译速率，min^-1
            'd_protein': 0.05         # 蛋白质降解率，min^-1
        }
        print(params['k_transcription'])  # 访问参数值
        ```

2.  **NumPy：数值计算的基石**
    `NumPy`提供了高性能的多维数组对象`ndarray`和相关的数学函数。它是所有科学计算的核心。
    *   **数组**：比列表更高效，支持向量化操作（无需显式循环）。
        ```python
        import numpy as np
        t = np.linspace(0, 10, 100)  # 创建从0到10的100个等间隔点（时间向量）
        y = np.exp(-0.1 * t)          # 对整个数组进行指数运算（向量化），模拟指数衰减
        ```
    *   **基本操作**：数组加减乘除、矩阵乘法(`@`或`np.dot`)、切片、索引。

3.  **SciPy：科学算法的宝库**
    `SciPy`建立在NumPy之上，提供了大量高级科学计算模块。
    *   **积分与ODE求解 (`scipy.integrate`)**：这是生物动力系统建模的**核心工具**。
        ```python
        from scipy.integrate import odeint
        # 定义ODE系统（例如，简单的基因表达模型）
        def model(y, t, params):
            mRNA, protein = y
            dmRNA_dt = params['k_txn'] - params['d_mRNA'] * mRNA
            dprotein_dt = params['k_tl'] * mRNA - params['d_protein'] * protein
            return [dmRNA_dt, dprotein_dt]
        # 初始条件、时间点、参数
        y0 = [0, 0]
        t = np.linspace(0, 300, 1000)
        sol = odeint(model, y0, t, args=(params,))  # 求解ODE！
        # sol[:, 0] 是mRNA的时间序列，sol[:, 1] 是protein的时间序列
        ```
    *   **优化 (`scipy.optimize`)**：用于参数拟合（如`curve_fit`， `least_squares`）。
    *   **插值、线性代数、统计等**：满足各种其他需求。

### 数据可视化：Matplotlib与科研图表审美

一图胜千言。`Matplotlib`是Python绘图的事实标准，`Seaborn`基于其构建，提供了更美观的统计图形样式。
*   **基本绘图流程**：
    ```python
    import matplotlib.pyplot as plt
    # 1. 创建图形和坐标轴
    fig, ax = plt.subplots(figsize=(8, 5), dpi=150) # figsize控制尺寸，dpi控制分辨率
    # 2. 在坐标轴上绘图
    ax.plot(t, sol[:, 0], label='mRNA', color='blue', linewidth=2)
    ax.plot(t, sol[:, 1], label='Protein', color='red', linewidth=2, linestyle='--')
    # 3. 美化图表（这是科研图表审美的体现！）
    ax.set_xlabel('Time (min)', fontsize=12)
    ax.set_ylabel('Concentration (a.u.)', fontsize=12)
    ax.set_title('Gene Expression Dynamics', fontsize=14, fontweight='bold')
    ax.legend(fontsize=11)
    ax.grid(True, linestyle=':', alpha=0.6) # 添加网格线，更易读
    # 4. 显示或保存
    plt.tight_layout() # 自动调整布局，避免标签重叠
    plt.savefig('gene_expression.png', bbox_inches='tight') # 保存为高清图片，用于报告或论文
    plt.show()
    ```
*   **科研图表原则**：图表应力求**清晰、准确、信息丰富**。始终标注坐标轴（包括单位！）、使用清晰的图例、选择合适的图表类型（线图、散点图、柱状图等）、并确保在黑白印刷时也能区分不同曲线（利用线型和标记点）。

### 补充：MATLAB简介

尽管我们以Python为主，但许多高校和实验室仍在使用**MATLAB**。了解其基本概念有助于阅读相关文献和代码。
*   **定位**：商业数值计算与仿真环境。在控制理论、信号处理、某些领域的计算物理/化学中应用广泛。
*   **与Python对比**：
    *   **语法**：MATLAB语法更专注于矩阵运算（例如，默认的乘法`*`就是矩阵乘法），对于线性代数问题表达非常简洁。
    *   **生态**：拥有丰富的专业工具箱（Toolbox），但商业许可昂贵。社区和开源生态不如Python活跃。
    *   **交互性**：类似，但其“工作区”变量查看非常直观。
*   **一个简单的ODE求解对比**（与上例对应）：
    ```matlab
    % 定义ODE函数（保存在独立的myModel.m文件中）
    function dydt = myModel(t, y, k_txn, d_mRNA, k_tl, d_protein)
        mRNA = y(1);
        protein = y(2);
        dydt = [k_txn - d_mRNA*mRNA;
                k_tl*mRNA - d_protein*protein];
    end
    % 主脚本
    params = [0.5, 0.1, 2.0, 0.05]; % 参数向量
    y0 = [0; 0];
    tspan = [0, 300];
    [t, sol] = ode45(@(t,y) myModel(t,y,params(1),params(2),params(3),params(4)), tspan, y0);
    plot(t, sol(:,1), 'b-', t, sol(:,2), 'r--');
    xlabel('Time (min)'); ylabel('Concentration (a.u.)');
    legend('mRNA', 'Protein'); grid on;
    ```
    理解两者思维模式的差异，能让你更好地在不同的工具间迁移思想。

### 文档与公式：Markdown与LaTeX基础

优秀的建模工作离不开优秀的文档。清晰的文档能让你在数月后依然能理解自己的代码，也是团队协作和成果展示的基础。
*   **Markdown**：Jupyter Notebook的原生标记语言。它用简单的符号（如`#`表示标题，`**`表示加粗）来格式化文本，让你能轻松地混合代码、文字叙述和图片。
    *   **核心用途**：在Jupyter Notebook中撰写实验记录、模型描述、结果分析。它也是GitHub等平台README文件的标准格式。
*   **LaTeX**：专业的学术排版系统，尤其在处理复杂数学公式时无可替代。
    *   **在Markdown/Notebook中使用**：Jupyter Notebook支持使用`$$ ... $$`（行间公式）或`$ ... $`（行内公式）来嵌入LaTeX数学公式。
        ```markdown
        我们的一维扩散方程可以写为：
        $$ \frac{\partial c(x, t)}{\partial t} = D \frac{\partial^2 c(x, t)}{\partial x^2} $$
        其中 $c$ 是浓度，$D$ 是扩散系数。
        ```
    *   **重要性**：掌握基本的LaTeX公式语法，是清晰、专业地表达你模型中数学思想的必备技能。

### 从这里出发

现在，你的数字实验室已经就绪，拥有了理解生物数学建模思想所需的语言和工具。从下一章开始，我们将运用Python和这些工具，去具体学习构建生物模型的数理基础。请记住，工具的价值在于使用。在学习过程中，请务必在Jupyter Notebook中亲手运行、修改、甚至“玩坏”每一个代码示例。这是将抽象知识转化为肌肉记忆的唯一途径。

欢迎来到生物数学建模的计算世界。让我们开始构建。

# 生物数学建模公式书写规范

## 1. 基础数学规范

### 1.1 公式格式
- **行间公式**：使用双美元号包裹，如 `$$公式$$`
- **行内公式**：使用单美元号包裹，如 `$公式$`
- **字体规范**：
  - 正体粗体：`$\mathbf{}$`，如 $\mathbf{A}$（表示矩阵）
  - 斜体粗体：`$\boldsymbol{}$`，如 $\boldsymbol{x}$（表示向量）
  - 特殊集合：`$\mathbb{}$`，如 $\mathbb{R}$（实数集）、$\mathbb{Z}$（整数集）

### 1.2 符号与运算符
- **分数表示**：
  - 行内公式：使用 `$\dfrac{}{}$`，如 $\dfrac{\partial f}{\partial t}$
  - 行间公式：可使用 `$\frac{}{}$`，如 $\frac{dx}{dt} = kx$
- **括号使用**：分式等内容使用自适应高度括号
  - 正确：$\left( \dfrac{a}{b} + \dfrac{c}{d} \right)$
  - 避免：$(\dfrac{a}{b} + \dfrac{c}{d})$
- **省略号**：使用 `$\cdots$` 表示居中省略号
  - 正确：$a_1, a_2, \cdots, a_n$
  - 避免：$a_1, a_2, ..., a_n$
- **相等性**：使用单等号 `$=$` 表示相等
  - 正确：$f(x) = g(x)$
  - 避免：$f(x) == g(x)$

### 1.3 变量命名
- **变量名**：使用斜体，如 $x, y, t$
- **常量**：通常使用正体，如 $\pi, e$
- **函数**：使用正体，如 $\sin, \log, \exp$
- **数字与公式间隔**：数字、字母、公式与前后的汉字之间各留一个空格
  - 正确：在第 $k$ 个时间点
  - 避免：在第$k$个时间点

## 2. 生物学特定规范

### 2.1 基因与蛋白质表示
- **基因名称**：使用斜体小写或首字母大写，根据物种惯例
  - 原核生物：$lacZ, \textit{lacZ}$
  - 真核生物：$p53, \textit{p53}$
- **蛋白质名称**：使用正体首字母大写或全大写
  - 正确：LacZ, $\text{LacZ}$, GFP
  - 避免：$LacZ$（除非作为数学变量）
- **基因座**：使用斜体，如 $lacZ::GFP$

### 2.2 浓度表示
- **标准表示**：使用方括号或直接变量名
  - 方括号：$[A]$, $[\text{mRNA}]$
  - 变量名：$c_A$, $m_A$（mRNA浓度），$p_A$（蛋白浓度）
- **下标表示**：细胞类型或状态作为下标
  - $[\text{IPTG}]_\text{in}$（细胞内IPTG浓度）
  - $[\text{GFP}]_\text{total}$（总GFP浓度）

### 2.3 反应与速率常数
- **速率常数**：$k$ 加描述性下标
  - 转录速率：$k_\text{txn}$ 或 $k_t$
  - 翻译速率：$k_\text{tl}$ 或 $k_p$
  - 降解速率：$d_m$（mRNA降解），$d_p$（蛋白降解）
  - 结合常数：$K_d$（解离常数），$K_a$（结合常数）
- **Hill函数参数**：
  - 半最大浓度：$K$
  - Hill系数：$n$
  - 基础表达水平：$\alpha_0$
  - 最大表达水平：$\alpha_\text{max}$

### 2.4 缩写规范
- **长名称缩写**：首次出现时定义，后续使用缩写
  - 首次：mRNA（信使RNA）
  - 后续：mRNA
- **常见缩写**：
  - ODE：常微分方程
  - PDE：偏微分方程
  - RBS：核糖体结合位点
  - TF：转录因子
  - PTM：翻译后修饰
  - FBA：通量平衡分析

### 2.5 特殊符号
- **化学计量系数**：使用希腊字母 $\nu$，如 $\nu_i$
- **通量**：使用 $J$ 或 $v$，如 $J_\text{glc}$（葡萄糖通量）
- **生长速率**：$\mu$
- **产率系数**：$Y_{X/S}$（基质S到生物量X的产率）

## 3. 数学建模特定规范

### 3.1 方程格式
- **微分方程**：使用 Leibniz 或 Newton 记号
  - Leibniz：$\dfrac{d[A]}{dt} = k[B]$
  - Newton：$\dot{x} = f(x, t)$
- **偏微分方程**：明确自变量
  - $\dfrac{\partial c}{\partial t} = D \dfrac{\partial^2 c}{\partial x^2}$
- **反应方程式**：化学式或数学式
  - 化学式：$A + B \xrightarrow{k} C$
  - 数学式：$v = k[A][B]$

### 3.2 参数与变量
- **参数**：通常使用希腊字母或带下标的拉丁字母
  - $\alpha, \beta, \gamma$
  - $k_1, k_2, k_{-1}$
- **状态变量**：通常使用拉丁字母
  - $x, y, z$ 或带生物学含义：$m, p, s$
- **时间与空间**：
  - 时间：$t$，空间：$x, y, z$
  - 离散时间：$t_n$ 或 $t[n]$
  - 空间网格：$x_i, y_j$

### 3.3 集合与索引
- **物种集合**：$\mathcal{S} = \{S_1, S_2, \cdots, S_n\}$
- **反应集合**：$\mathcal{R} = \{R_1, R_2, \cdots, R_m\}$
- **索引表示**：
  - 物种 $i$ 的浓度：$[S_i]$ 或 $x_i$
  - 反应 $j$ 的速率：$v_j$

### 3.4 矩阵与向量
- **代谢网络**：化学计量矩阵 $\mathbf{N}$
- **通量向量**：$\mathbf{v} = (v_1, v_2, \cdots, v_m)^\top$
- **浓度向量**：$\mathbf{x} = (x_1, x_2, \cdots, x_n)^\top$

## 4. 代码与数学区分

### 4.1 变量表示
- **数学变量**：斜体，如 $x[i]$
- **代码变量**：等宽字体，如 `x[i]`
- **避免混淆**：不在公式中使用代码语法
  - 正确：$a_{i,j}$ 或 $a(i, j)$
  - 避免：$a[i][j]$

### 4.2 函数调用
- **数学函数**：$\sin(x)$, $\log(x)$
- **自定义函数**：$f(x, y)$, $g(t; \theta)$
- **参数分隔**：使用逗号或分号
  - 变量：$f(x, y)$
  - 参数：$f(x; \alpha, \beta)$

### 4.3 条件与约束
- **约束条件**：使用大括号或文本
  - $\max f(x) \quad \text{subject to} \quad g(x) = 0$
  - $\{ x \in \mathbb{R}^n \mid Ax = b \}$
- **条件概率**：$P(A \mid B)$

## 5. 示例整合

### 示例1：基因表达模型
$$
\begin{aligned}
\dfrac{dm}{dt} &= k_\text{txn} - d_m m \\
\dfrac{dp}{dt} &= k_\text{tl} m - d_p p
\end{aligned}
$$
其中 $m$ 为 mRNA 浓度，$p$ 为蛋白质浓度。

### 示例2：酶促反应
$$
v = \dfrac{V_\text{max} [S]}{K_m + [S]}
$$
其中 $v$ 为反应速率，$[S]$ 为底物浓度。

### 示例3：逻辑回归（分类模型）
$$
P(y=1 \mid \boldsymbol{x}) = \dfrac{1}{1 + \exp(-\boldsymbol{\beta}^\top \boldsymbol{x})}
$$
其中 $\boldsymbol{x}$ 为特征向量，$\boldsymbol{\beta}$ 为参数向量。

---

**遵循本规范可确保公式的清晰性、一致性和专业性，便于读者理解和复现建模工作。**