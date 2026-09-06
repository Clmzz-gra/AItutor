---
tags:
  - math
  - 实变函数与泛函分析
  - teaching-pack
created: 2026-08-16
updated: 2026-08-16
status: 重写版（教学模式）
aliases:
  - 第五章 积分论
  - 勒贝格积分学习讲解包
supersedes: []
type: 章
formal: true
subject: 实变函数与泛函分析
---
# Ch5 积分论
> 教材：程其襄、张奠宙、胡善文、薛以锋《实变函数与泛函分析基础》第四版，第五章（§1 黎曼积分的局限性, 勒贝格积分简介、§2 非负简单函数的勒贝格积分、§3 非负可测函数的勒贝格积分、§4 一般可测函数的勒贝格积分、§5 黎曼积分和勒贝格积分、§6 勒贝格积分的几何意义, 富比尼定理）
> 本包是重写版。阅读顺序：从「引言」开始，按"为什么要新积分 → 三步定义 → 极限定理 → 与黎曼积分的关系 → 高维公式"读；每章末尾有「停顿自问」，第九部分自测题答案折叠，点击展开。

> [!info] 关联笔记
> - 上一章（可测函数）：[[Ch4 可测函数]]
> - 测度地基：[[Ch3 测度论]]
> - 学科全景与进度：[[学科概览]]

---

## 引言：为什么需要勒贝格积分？（先读这里）

**一句话**：黎曼积分有两个治不好的病——**极限换序条件太苛刻、微积分基本定理不完整**。勒贝格积分用"横切值域 + 测度称重"重做积分，把这两个病治好了大半。

### 需求一：黎曼积分与极限交换的条件太严

一列 $R$ 可积函数的极限函数（即使有界）可能不是 $R$ 可积的。要在黎曼框架下保证
$$\int_a^b\lim_n f_n(x)\,dx=\lim_n\int_a^b f_n(x)\,dx,$$
通常要求 $\{f_n\}$ **一致收敛**——这个条件既苛刻又难验证。本章§4 的**勒贝格控制收敛定理**将把它放宽为"逐点收敛 + 一个可积的控制函数"，这是勒贝格积分最大的战果。

### 需求二：积分不完全是微分的逆运算

黎曼可积函数 $f$ 的变上限积分 $F(x)=\int_a^x f(t)\,dt$，在 $f$ 的连续点处有 $F'=f$，这没问题；但反过来，一个可微函数 $F$ 的导函数 $f$ 即使有界，也可能不是 $R$ 可积的（Volterra 的例子），于是 Newton-Leibniz 公式 $F(x)-F(a)=\int_a^x f(t)\,dt$ 无法成立。勒贝格积分让导函数"几乎总是"可积回来，微积分基本定理在 a.e. 意义下恢复完整。

### 需求三：测度和可测函数已经造好，只差"组装"

第三章造好了测度 $m$（可数可加、与极限可交换），第四章造好了可测函数（水平集可称重、可用简单函数逼近）。本章要做的就是把它们组装成积分——组装路线就是引言开头见过的公式：
$$\int f\ \approx\ \sum_i y_i\cdot m(A_i).$$
但直接对这个公式取极限会遇到一个麻烦：$f$ 可以无界、可以取 $\pm\infty$，积分值可能出现 $\infty-\infty$ 的不定式。**所以勒贝格的定义分三步走，一步只解决一个麻烦**：

```
第一步（§2）非负简单函数 φ = Σ cᵢ χ_{Eᵢ}：积分 = Σ cᵢ mEᵢ（纯加权和）
        ↓ 第二步（§3）非负可测函数 f：积分 = sup{∫φ : 0 ≤ φ ≤ f}（单调逼近）
        ↓ 第三步（§4）一般可测函数 f = f⁺ - f⁻：积分 = ∫f⁺ - ∫f⁻（正负部分开）
        ↓ 武器（§3-§4）Levi / Fatou / 控制收敛：极限与积分可交换
        ↓ 对话（§5-§6）与黎曼积分的关系；几何意义与 Fubini
```

**先记住两个词**：$(R)\int$ 表示黎曼积分，$(L)\int$ 表示勒贝格积分（$L$ = Lebesgue）。

---

## 一、整体认知：三步定义为什么这样设计

### 1.1 第一步只对非负：避开 $\infty-\infty$

积分值是"有正有负的曲边梯形面积的代数和"。对无界或取 $\infty$ 的函数，正面积和负面积可能都是 $\infty$，相减无意义。**对策**：先只定义非负函数的积分（值允许 $+\infty$），最后一步再用 $f=f^+-f^-$ 拆分，并要求 $\int f^+$ 与 $\int f^-$ 不同时为 $\infty$。

### 1.2 第二步从简单函数出发：先定义"能直接算的"

简单函数 $\varphi=\sum_{i=1}^{k}c_i\chi_{E_i}$（$c_i\geqslant0$，$E_i$ 互不相交可测）的积分没有任何悬念，就是加权和 $\sum c_i mE_i$。*因为*第四章定理 7 保证每个非负可测函数都能被递增简单函数列逼近，所以"简单函数的积分"取上确界就能定义所有非负可测函数的积分——**先定义能直接算的，再用逼近延拓到一切**。

### 1.3 符号约定（首次出现即定义）

- $\chi_A$（读作"$A$ 的特征函数"）：$x\in A$ 时取 $1$，否则取 $0$；
- $\int_E f(x)\,dx$（读作"$f$ 在 $E$ 上的积分"）；$E$ 是可测集；
- $f^+(x)=\max\{f(x),0\}$（正部），$f^-(x)=\max\{-f(x),0\}$（负部），恒有 $f=f^+-f^-$，$|f|=f^++f^-$；
- $L(E)$（读作"$E$ 上勒贝格可积函数全体"）：正部、负部积分都有限的函数组成的集合；
- a.e.（几乎处处）：除零测集外处处成立（第四章已定义）。

---

## 二、前置知识补给站（按需读，不打断主线）

- **简单函数与逼近定理（Ch4 §1 定理 7）**：非负可测函数 = 递增简单函数列的逐点极限；有界时可一致。**这是为了**：它是第二步定义与 Levi 定理证明的共同引擎。
- **可测函数对极限封闭（Ch4 §1 定理 6）**：可测函数列的上下极限仍可测。**这是为了**：Fatou 引理里的 $\varliminf f_n$ 仍是可积对象。
- **测度的可数可加性与单调收敛（Ch3 定理 6/8/9）**：**这是为了**：简单函数积分的区域可加性与极限性质（§2 定理 1）完全建立在其上。
- **叶戈罗夫定理与里斯定理（Ch4 §2/§4）**：a.e. 收敛与依测度收敛的桥梁。**这是为了**：控制收敛定理的"依测度版本"证明要调用里斯子列。
- **下确界 $\sup$ 与上确界 $\inf$**：**这是为了**：非负可测函数积分的定义就是一族数的上确界。
- **数学分析的黎曼积分**：达布上下和、可积判据。**这是为了**：§5 要把黎曼可积翻译成"不连续点集零测"。

---

## 三、主体之一：非负简单函数的积分（§2）

### 3.1 定义：唯一没有悬念的积分

**定义（非负简单函数的勒贝格积分）** 设 $E\subset\mathbb{R}^n$ 可测，$\varphi=\sum_{i=1}^{k}c_i\chi_{E_i}$（$c_i\geqslant0$，$\{E_i\}$ 是 $E$ 的有限可测划分），定义
$$\int_E\varphi(x)\,dx=\sum_{i=1}^{k}c_i\,mE_i.$$
对可测子集 $A\subset E$：$\int_A\varphi\,dx=\sum_i c_i\,m(A\cap E_i)$。

**为什么这个定义"良定"**：同一个 $\varphi$ 可以有不同的分块表示（把一块再切细）。*因为*测度可加，$c_i\,m(E_i)=\sum_j c_i\,m(E_{ij})$，两种表示求和相同——加权和不依赖分法。（教材定理 2 的证明里"公共加细 $E_i\cap F_j$"正是这件事的标准写法。）

**例（全章第一算）**：$\mathbb{R}$ 上的狄利克雷函数 $D=\chi_{\mathbb{Q}}$（$\mathbb{Q}$ 读作"有理数集"）：
$$\int_{\mathbb{R}}D(x)\,dx=1\cdot m\mathbb{Q}+0\cdot m(\mathbb{R}\setminus\mathbb{Q})=1\cdot0+0\cdot\infty=0.$$
（用到约定 $0\cdot\infty=0$。注意：**可数但稠密**的 $\mathbb{Q}$ 测度为零——第三章的核心结论在这里第一次变现。）

### 3.2 三条基本性质

**定理 1** 设 $\varphi$ 为非负简单函数：
1. $\int_E c\varphi\,dx=c\int_E\varphi\,dx$（$c\geqslant0$）；
2. $A,B\subset E$ 可测且不相交 $\Rightarrow\int_{A\cup B}\varphi\,dx=\int_A\varphi\,dx+\int_B\varphi\,dx$；
3. 若 $A_1\subset A_2\subset\cdots$ 且 $\bigcup_n A_n=E$，则 $\lim_n\int_{A_n}\varphi\,dx=\int_E\varphi\,dx$。

**证明一句话**：三条都直接展开成有限和 $\sum_i c_i\,m(\cdot\cap E_i)$，然后分别用"数乘分配律""测度有限可加""测度递增连续性（Ch3 定理 8）"。

**定理 2** 非负简单函数 $\varphi,\psi$ 满足线性：
$$\int_E(\alpha\varphi+\beta\psi)\,dx=\alpha\int_E\varphi\,dx+\beta\int_E\psi\,dx\quad(\alpha,\beta\geqslant0).$$
**证明关键**：把 $\varphi,\psi$ 的不同分法做**公共加细**——用 $\{E_i\cap F_j\}$ 同时表示两者，在每块 $E_i\cap F_j$ 上 $\varphi+\psi=c_i+d_j$，于是
$$\int_E(\varphi+\psi)\,dx=\sum_{i,j}(c_i+d_j)\,m(E_i\cap F_j)=\int_E\varphi\,dx+\int_E\psi\,dx.$$

> **停顿自问**：为什么简单函数积分不需要"取极限"？——因为它只有有限块、有限个值，加权和一步到位；所有困难都被推迟到"从简单到一般"的那一步。

---

## 四、主体之二：非负可测函数的积分（§3）

### 4.1 定义：用简单函数从下方逼近

**定义** 设 $f\geqslant0$ 在可测集 $E$ 上可测，定义
$$\int_E f(x)\,dx=\sup\left\{\int_E\varphi(x)\,dx:\ \varphi\ \text{是简单函数},\ 0\leqslant\varphi\leqslant f\ \text{于}\ E\right\}.$$
积分值允许 $+\infty$。若 $\int_E f\,dx<\infty$，称 $f$ 在 $E$ 上**勒贝格可积**（$L$ 可积）。

**直觉**：所有"不超过 $f$ 的阶梯块"的积分，取上确界——这就是"横柱求和"的严格化。$\int_E f$ 是"从下方逼近 $f$ 的最优代价"。

### 4.2 四条基础性质（定理 1）

**定理 1** $f\geqslant0$ 可测，则：
1. $mE=0\Rightarrow\int_E f\,dx=0$；
2. $\int_E f\,dx=0\Rightarrow f=0$ a.e. 于 $E$；
3. $\int_E f\,dx<\infty\Rightarrow f<\infty$ a.e. 于 $E$；
4. $A,B$ 不相交可测 $\Rightarrow\int_{A\cup B}f\,dx=\int_A f\,dx+\int_B f\,dx$。

**证明 (2)（本章第一次"用测试函数压出零测"）**：令 $A_n=E[f\geqslant1/n]$，作简单函数 $\varphi_n=(1/n)\chi_{A_n}$。*因为* $\varphi_n\leqslant f$ 且 $\int_E f=0$，
$$0=\int_E f\,dx\geqslant\int_E\varphi_n\,dx=\frac1n\,mA_n\geqslant0\ \Rightarrow\ mA_n=0.$$
再 *因为* $E[f>0]=\bigcup_n A_n$（可数并），$mE[f>0]=0$。$\square$

**证明 (3)**：令 $E_\infty=E[f=+\infty]$，$\varphi_n=n\chi_{E_\infty}\leqslant f$，于是 $n\,mE_\infty\leqslant\int_E f\,dx<\infty$ 对一切 $n$ 成立 $\Rightarrow mE_\infty=0$。

**证明 (4)**：对 $A\cup B$ 上任一 $0\leqslant\varphi\leqslant f$，用 §3 定理 1 的有限可加性拆 $\int_{A\cup B}\varphi$，两侧取上确界夹逼即得。

**定理 2（单调性与 a.e. 相等）**：$f\leqslant g$ a.e. $\Rightarrow\int_E f\leqslant\int_E g$；$f=g$ a.e. $\Rightarrow$ 积分相等。
**证明**：把例外集 $E[f>g]$ 挖掉（零测），在剩下的 $E_1=E[f\leqslant g]$ 上每个不超过 $f$ 的简单函数也不超过 $g$，取上确界即得。

> **核心事实**：**积分不看零测集**——在零测集上随便改函数值，积分不变。这是勒贝格积分区别于黎曼积分的第一个"宽容"。

### 4.3 Levi 单调收敛定理（本章第一定理，推导全程）

**Levi 定理** 设 $0\leqslant f_1\leqslant f_2\leqslant\cdots$ 是非负可测函数列，$f=\lim_n f_n$，则
$$\lim_{n\to\infty}\int_E f_n(x)\,dx=\int_E f(x)\,dx.$$

**证明（一正一反两个方向）**

- **方向 $\leqslant$（容易）**：*因为* $f_n\leqslant f_{n+1}\leqslant f$，由单调性 $\int_E f_n\leqslant\int_E f_{n+1}\leqslant\int_E f$，故 $\lim_n\int_E f_n\leqslant\int_E f$。
- **方向 $\geqslant$（用简单函数"卡"）**：任取简单函数 $\varphi$，$0\leqslant\varphi\leqslant f$，任取 $0<c<1$。令
  $$E_n=E[f_n\geqslant c\varphi].$$
  *因为* $f_n\uparrow f$ 且 $c<1$，有 $E_n\uparrow E$（哪点会漏掉？对 $x\in E$，只要 $f_n(x)\to f(x)$，终有 $f_n(x)\geqslant c\varphi(x)$，因为 $\varphi(x)\leqslant f(x)$ 且 $c<1$）。
  于是
  $$\int_E f_n\,dx\geqslant\int_{E_n}f_n\,dx\geqslant\int_{E_n}c\varphi\,dx=c\int_{E_n}\varphi\,dx.$$
  由 §3 定理 1(3)（简单函数积分对递增区域列的连续性），$\int_{E_n}\varphi\,dx\to\int_E\varphi\,dx$。故
  $$\lim_n\int_E f_n\,dx\geqslant c\int_E\varphi\,dx.$$
  *因为* $c$ 是任意小于 $1$ 的数，令 $c\to1$；再由 $\varphi$ 任意，取上确界得 $\lim_n\int_E f_n\geqslant\int_E f$。双向夹逼。$\square$

> **为什么引入 $c<1$？** 这是"留一点余量"的标准技术：$f_n$ 未必逐点 $\geqslant\varphi$（$\varphi$ 可能在某个单点上等于 $f$），但乘上 $c<1$ 后终将超过。$c$ 的角色是给"严格超过"留出缝隙。

### 4.4 线性与逐项积分

**定理 4（线性）** $\int_E(\alpha f+\beta g)\,dx=\alpha\int_E f\,dx+\beta\int_E g\,dx$（$\alpha,\beta\geqslant0$）。
**证明**：用 Ch4 定理 7 取递增简单函数列 $\varphi_n\uparrow f$、$\psi_n\uparrow g$，则 $\alpha\varphi_n+\beta\psi_n\uparrow\alpha f+\beta g$；*因为* 简单函数积分线性，对两边用 Levi 定理即得。

**定理 5（逐项积分）** 非负可测函数列 $\{f_n\}$：
$$\int_E\sum_{n=1}^{\infty}f_n(x)\,dx=\sum_{n=1}^{\infty}\int_E f_n(x)\,dx.$$
**证明**：令部分和 $g_n=\sum_{k=1}^{n}f_k$，*因为* $g_n\uparrow\sum f_n$ 且积分有有限线性，用 Levi 定理把极限穿过积分号。

### 4.5 Fatou 引理：极限进去只亏不赚

**Fatou 引理** 非负可测函数列 $\{f_n\}$（$\varliminf_n f_n$ 读作"$f_n$ 的下极限"，逐点取）：
$$\int_E\varliminf_{n\to\infty}f_n(x)\,dx\leqslant\varliminf_{n\to\infty}\int_E f_n(x)\,dx.$$

**证明**：令 $g_n(x)=\inf\{f_k(x):k\geqslant n\}$，则 $0\leqslant g_n\uparrow\varliminf f_n$ 且 $g_n\leqslant f_{n+1}$。由 Levi 定理与单调性：
$$\int_E\varliminf f_n\,dx=\int_E\lim_n g_n\,dx=\lim_n\int_E g_n\,dx\leqslant\varliminf_n\int_E f_n\,dx.\ \square$$

**反例（$\leqslant$ 不能改 $=$，必须会默写）**：在 $(0,\infty)$ 上取 $f_n=n\chi_{(0,1/n)}$。*因为* 每点 $x$ 终有 $1/n<x$，故 $f_n(x)\to0$，所以 $\int\lim f_n=0$；但
$$\int_{(0,\infty)}f_n\,dx=n\cdot m(0,1/n)=n\cdot\frac1n=1,$$
故 $\varliminf\int f_n=1>0$。**直观**：积分是"总量"，逐点极限看不住"质量逃到无穷/散开"的过程。

> **核心洞察**：Levi 与 Fatou 是一对——**单调递增时极限与积分完全可交换（Levi）；一般情形只保证"积分不小于极限的积分"（Fatou）**。Fatou 的 $\leqslant$ 方向永远指向"可能亏"，这个方向感在全章都要用到。

---

## 五、主体之三：一般可测函数的积分（§4）

### 5.1 定义：正负部分开，避开 $\infty-\infty$

**定义（一般可测函数的积分）** 设 $f$ 在可测集 $E$ 上可测。若 $\int_E f^+\,dx$ 与 $\int_E f^-\,dx$ 中**至少一个有限**，称 $f$ 在 $E$ 上**积分确定**，定义
$$\int_E f(x)\,dx=\int_E f^+(x)\,dx-\int_E f^-(x)\,dx;$$
若两者**都有限**，称 $f$ 在 $E$ 上**勒贝格可积**（$L$ 可积），全体记为 $L(E)$。

**读法**：积分确定 = 积分值存在（可为 $\pm\infty$ 或有限）；$L$ 可积 = 积分值是有限实数。例如 $\int_0^\infty\sin x\,dx$ 型"正负面积都无穷"的函数**连积分确定都不是**。

### 5.2 七条基本性质（定理 1，逐条配"因为"）

**定理 1** 设 $f$ 在 $E$ 上可测：

1. **零测集上一切函数可积且积分为零**：$mE=0\Rightarrow$ 任何 $f$ 在 $E$ 上 $L$ 可积且 $\int_E f=0$。*因为* $f^+,f^-\leqslant$ 都是 $E$ 上非负可测，而 §4 定理 1(1) 说零测集上非负积分恒为 $0$。
2. **可积函数 a.e. 有限**：$f\in L(E)\Rightarrow|f|<\infty$ a.e.。*因为* 两个非负积分都有限，§4 定理 1(3) 分别给出 $f^+<\infty$、$f^-<\infty$ a.e.。
3. **区域可加**：$E=A\cup B$ 不相交可测 $\Rightarrow\int_E f=\int_A f+\int_B f$。*因为* 对 $f^+,f^-$ 分别用 §4 定理 1(4)，再相减。
4. **a.e. 相等不改积分**：$f=g$ a.e. $\Rightarrow$ 积分同确定、同值。*因为* $f^\pm=g^\pm$ a.e.，用 §4 定理 2。
5. **单调性**：$f\leqslant g$ a.e. $\Rightarrow\int_E f\leqslant\int_E g$；特别地，$mE<\infty$ 且 $b\leqslant f\leqslant B$ a.e. 时 $b\,mE\leqslant\int_E f\leqslant B\,mE$（有界函数在有限测度集上必可积）。
6. **绝对值不等式**：$f\in L(E)\Rightarrow|f|\in L(E)$ 且 $\left|\int_E f\right|\leqslant\int_E|f|$。*因为* $\int|f|=\int f^++\int f^-<\infty$，而 $|\int f|=|\int f^+-\int f^-|\leqslant\int f^++\int f^-$。
7. **控制判据**：$|f|\leqslant g$ a.e. 且 $g$ 非负 $L$ 可积 $\Rightarrow f\in L(E)$ 且 $\left|\int_E f\right|\leqslant\int_E|f|\leqslant\int_E g$。

### 5.3 线性（定理 2）

**定理 2** $f,g\in L(E)$，$\lambda\in\mathbb{R}\Rightarrow\lambda f,\ f+g,\ \alpha f+\beta g$ 都可积，且
$$\int_E\lambda f=\lambda\int_E f,\qquad \int_E(f+g)=\int_E f+\int_E g.$$

**证明要领**：数乘按 $\lambda=0,>0,<0$ 分三种情形（$\lambda<0$ 时用 $(-\lambda f)^+=|\lambda|f^-$ 换号）；加法用不等式 $(f+g)^+\leqslant f^++g^+$、$(f+g)^-\leqslant f^-+g^-$ 先证可积，再搬运等式 $(f+g)^++f^-+g^-=(f+g)^-+f^++g^+$ 两边积分整理。细节繁琐但每步都只是"正负部 + §4 定理 4"。

### 5.4 积分的绝对连续性（定理 3）

**定理 3** $f\in L(E)\Rightarrow$ 对任意 $\varepsilon>0$，存在 $\delta>0$，使可测集 $A\subset E$ 且 $mA<\delta$ 时，$\left|\int_A f\,dx\right|\leqslant\int_A|f|\,dx<\varepsilon$。

**证明思路**：*因为* $\int_E|f|<\infty$，由 §4 定义可取简单函数 $\varphi\leqslant|f|$ 使 $\int_E(|f|-\varphi)<\varepsilon/2$；令 $M=1+\max\varphi$、$\delta=\varepsilon/(2M)$。任取 $mA<\delta$，
$$\int_A|f|\,dx=\int_A(|f|-\varphi)\,dx+\int_A\varphi\,dx\leqslant\frac{\varepsilon}{2}+M\,mA<\varepsilon.$$
**直觉**：积分对"小测度集合"连续——把积分看成集合函数，它是绝对连续的。这一条是后面"分布函数的连续性"与概率论里积分性质的源头。

### 5.5 积分的可数可加性（定理 4）

**定理 4** $E=\bigcup_n E_n$（$E_n$ 两两不相交可测），$f$ 在 $E$ 上积分确定，则
$$\int_E f(x)\,dx=\sum_{n=1}^{\infty}\int_{E_n}f(x)\,dx.$$
**证明**：对 $f^+$ 用 §4 定理 5（逐项积分，注意 $f^+=\sum_n f^+\chi_{E_n}$），对 $f^-$ 同理；*因为* 积分确定保证两个正项级数至少一个收敛，可逐项相减。

### 5.6 勒贝格控制收敛定理（本章核心定理，推导全程）

**LDCT（勒贝格控制收敛定理）** 设 $\{f_n\}$ 在 $E$ 上可测，$F$ 是 $E$ 上非负 $L$ 可积函数，满足
$$|f_n(x)|\leqslant F(x)\ \text{a.e.},\qquad f_n(x)\to f(x)\ \text{a.e.},$$
则
$$\lim_{n\to\infty}\int_E|f_n-f|\,dx=0,\qquad \lim_{n\to\infty}\int_E f_n\,dx=\int_E f\,dx.$$

**证明（全部力气花在第一个等式上）**：令 $g_n=|f_n-f|$。*因为* $|f_n|\leqslant F$ 且 $f_n\to f$，极限函数也满足 $|f|\leqslant F$ a.e.，故 $g_n$ 非负可积且 $g_n\leqslant2F$、$g_n\to0$ a.e.。
对非负函数列 $\{2F-g_n\}$ 用 **Fatou 引理**：
$$2\int_E F\,dx=\int_E\lim_n(2F-g_n)\,dx\leqslant\varliminf_n\int_E(2F-g_n)\,dx=2\int_E F\,dx-\varlimsup_n\int_E g_n\,dx.$$
*因为* $2\int_E F<\infty$（$F$ 可积），两边消去它得 $\varlimsup_n\int_E g_n\leqslant0$；又 $\int_E g_n\geqslant0$，故 $\lim_n\int_E g_n=0$。第二个等式由 $|\int f_n-\int f|\leqslant\int|f_n-f|$ 立即得到。$\square$

**为什么这个证明漂亮**：它把"差收敛到 $0$"包装成 Fatou 引理里"不会亏"的对象——**控制函数 $F$ 的作用不是摆设，它让 $2F-g_n\geqslant0$，Fatou 才敢出手**。

**定理 6（依测度收敛版本）**：条件换成 $f_n\Rightarrow f$（其余同），结论不变。
**证明**：若 $\int|f_n-f|\not\to0$，则存在子列使积分极限 $>0$；由里斯定理再取子列 a.e. 收敛，对它用定理 5 得矛盾。（子列论证法，Ch4 三桥的又一应用。）

**推论（有界 + 有限测度，考试高频）**：$mE<\infty$，$|f_n|\leqslant M$ a.e. 且 $f_n\to f$ a.e.（或 $f_n\Rightarrow f$）$\Rightarrow$ 极限与积分可交换。*因为* 常值函数 $F\equiv M$ 在 $mE<\infty$ 上可积。

### 5.7 逐项积分与积分号下求导（定理 7、8，支撑档）

**定理 7** 若正项级数 $\sum_n\int_E|f_n|\,dx<\infty$，则 $\sum_n f_n$ a.e. 收敛，和函数可积，且积分可与求和交换。
**证明**：令 $F=\sum_n|f_n|$，由逐项积分（§4 定理 5）$\int_E F=\sum_n\int_E|f_n|<\infty$，故 $F$ 可积 $\Rightarrow F<\infty$ a.e. $\Rightarrow$ 级数 a.e. 绝对收敛；对部分和用 LDCT（控制函数 $F$）。

**定理 8（积分号下求导）**：$f(x,t)$ 对 a.e. $x$ 关于 $t$ 可导，且 $|\partial_t f(x,t)|\leqslant F(x)$（$F$ 可积），则
$$\frac{d}{dt}\int_E f(x,t)\,dx=\int_E\frac{\partial}{\partial t}f(x,t)\,dx.$$
**证明**：对差商序列 $g_n(x)=\frac{1}{h_n}[f(x,t+h_n)-f(x,t)]$ 用中值定理得 $|g_n|\leqslant F$，再套 LDCT。

**例（本章所有机器的一次合奏）**：$f\in L[a,b]$ 可用连续函数按 $L^1$ 距离逼近：先取简单函数 $\varphi$ 逼近 $f$（§4 定义），再用卢津定理把 $\varphi$ 换成连续函数 $g$（只在零测附近改），三角不等式两次 $\varepsilon/2$ 拼起来。**这条链：简单函数逼近 → 卢津 → 连续函数逼近，是全章方法论的缩影。**

---

## 六、主体之四：黎曼积分与勒贝格积分（§5）

### 6.1 黎曼可积的测度论判据

**定理 1** 有界函数 $f$ 在 $[a,b]$ 上 $R$ 可积 $\iff f$ 在 $[a,b]$ 上 **a.e. 连续**（不连续点集是零测集）。

**证明骨架**：取一列分法 $T^{(n)}$ 使最大区间长 $\delta(T^{(n)})\to0$，用达布上、下和构造 $h_n$（各小区间上取 $M_i^{(n)}-m_i^{(n)}$）。*因为* $0\leqslant h_n\leqslant2M$ 且 $h_n\to\omega$（$\omega(x)$ 是 $f$ 在 $x$ 处的**振幅**，$\omega(x)=0\iff f$ 在 $x$ 连续）a.e.，由有界收敛（§5.6 推论）：
$$(L)\int_{[a,b]}\omega\,dx=\lim_n(L)\int_{[a,b]}h_n\,dx=\overline{\int_a^b}f\,dx-\underline{\int_a^b}f\,dx.$$
于是 $R$ 可积（上下积分相等）$\iff(L)\int\omega=0\iff\omega=0$ a.e. $\iff f$ a.e. 连续。$\square$

**读法**：黎曼可积的障碍只有一个——**不连续点太多**；而且"太多"的精确含义是"测度不为零"。狄利克雷函数处处不连续 $\Rightarrow$ 不可积；单调函数不连续点至多可数 $\Rightarrow$ 可积。

### 6.2 两者相等（定理 2）与非负反常积分（定理 3）

**定理 2** $f$ 在 $[a,b]$ 上有界且 $R$ 可积 $\Rightarrow f$ 是 $L$ 可积的，且 $(L)\int_{[a,b]}f=(R)\int_a^b f$。
（证明用达布大和构造 $g_n\to f$ a.e.，再套有界收敛。）

**定理 3** $f\geqslant0$ 在 $[a,\infty)$ 上每段 $[a,A]$ 都 $R$ 可积且 $R$ 反常积分收敛 $\Rightarrow f$ 在 $[a,\infty)$ 上 $L$ 可积，且两者相等。发散时 $L$ 积分同为 $\infty$。

### 6.3 边界：$L$ 积分不是 $R$ **反常**积分的推广

**例（必须记住的边界）**：$f(x)=\dfrac{\sin x}{x}$（$x>0$，$f(0)=1$）。$R$ 反常积分收敛：$(R)\int_0^\infty\frac{\sin x}{x}\,dx=\dfrac{\pi}{2}$。但把正负部分开：
$$\int_{[0,\infty)}f^+\,dx\geqslant\sum_{n=0}^{\infty}\frac{2}{(2n+1)\pi}=\infty,\qquad \int_{[0,\infty)}f^-\,dx=\infty.$$
正部、负部都无穷 $\Rightarrow f$ **连积分确定都不是**，当然不 $L$ 可积。

**原因一句话**：勒贝格积分是**绝对收敛型**积分（$f$ 可积 $\iff|f|$ 可积），而条件收敛的 $R$ 反常积分靠"正负相消"存活，在 $L$ 框架里不允许。

### 6.4 对比总表

| | 黎曼积分 | 勒贝格积分 |
|---|---|---|
| 切法 | 竖切定义域 | 横切值域 |
| 可积函数 | 不连续点集零测（有界） | 可测 + 正负部积分有限 |
| 极限定理 | 一致收敛 | 控制收敛（$F$ 可积） |
| 反常积分 | 可条件收敛（$\sin x/x$） | 只承认绝对收敛 |
| 零测集 | 无对应物 | 积分完全忽略零测集 |
| 完备性 | $R$ 可积空间不完备 | $L^1$ 完备（Ch7 的地基） |

---

## 七、主体之五：几何意义与富比尼定理（§6）

### 7.1 直积与截面（先把新符号定义好）

- **直积** $A\times B=\{(x,y):x\in A,\ y\in B\}$（读作"$A$ 叉乘 $B$"），$A\subset\mathbb{R}^p,\ B\subset\mathbb{R}^q$，它是 $\mathbb{R}^{p+q}$ 中的集合；
- **截面** 对 $E\subset\mathbb{R}^{p+q}$ 与固定 $x_0\in\mathbb{R}^p$，$E_{x_0}=\{y\in\mathbb{R}^q:(x_0,y)\in E\}$（读作"$E$ 在 $x_0$ 处的截面"）——把高维集合沿 $x$ 方向"切片"。

### 7.2 截面定理：高维测度 = 截面测度的积分

**定理 1（截面定理）** 设 $E\subset\mathbb{R}^{p+q}$ 可测，则
1. 对 a.e. 的 $x\in\mathbb{R}^p$，截面 $E_x$ 是 $\mathbb{R}^q$ 中可测集；
2. $mE_x$ 作为 $x$ 的函数在 $\mathbb{R}^p$ 上 a.e. 有定义且可测；
3. $mE=\int_{\mathbb{R}^p}mE_x\,dx$。

**证明按"特殊到一般"分五步推进**（这与卢津定理的三步证明是同一方法）：区间（直接算）→ 开集（可数不交区间之并 + 逐项积分）→ $G_\delta$ 集（递减交 + Ch3 定理 9/控制收敛）→ 零集（用 $G_\delta$ 包住）→ 一般可测集（Ch3 结构定理 $E=G\setminus M$）。每一步都只调用上一步 + 一个已证定理。

### 7.3 积分的几何意义：积分 = 下方图形的测度

**定义（下方图形）** $f\geqslant0$ 在 $E\subset\mathbb{R}^n$ 上，$\mathbb{R}^{n+1}$ 中集合
$$G(E,f)=\{(x,z):x\in E,\ 0\leqslant z<f(x)\}$$
（读作"$f$ 在 $E$ 上的下方图形"）。

**定理 3** $f\geqslant0$ 可测 $\iff G(E,f)$ 可测；且此时
$$\int_E f(x)\,dx=mG(E,f).$$

**直觉**：积分终于回到最原始的"面积"——曲边梯形面积就是它的下方图形测度。勒贝格绕了一大圈（测度 → 可测函数 → 简单函数 → 积分），最后证明这条圆闭合上了：**积分与测度互为表里**。推论：$f$ 可积 $\iff mG(E,f^+)$ 与 $mG(E,f^-)$ 都有限。

### 7.4 富比尼定理：高维积分 = 累次积分

**富比尼定理** 设 $A\subset\mathbb{R}^p$、$B\subset\mathbb{R}^q$ 可测，$f$ 定义在 $A\times B$ 上：

1. **非负版本**：$f\geqslant0$ 可测 $\Rightarrow$ 对 a.e. 的 $x\in A$，$f(x,y)$ 作为 $y$ 的函数在 $B$ 上可测，且
   $$\int_{A\times B}f\,dP=\int_A dx\int_B f(x,y)\,dy;$$
2. **可积版本**：$f$ 在 $A\times B$ 上 $L$ 可积 $\Rightarrow$ 对 a.e. 的 $x\in A$，$f(x,y)$ 作为 $y$ 的函数在 $B$ 上可积，且上式成立（内层积分作为 $x$ 的函数也可积）。

**证明路线**：把 $A\times B$ 上的积分写成下方图形测度 $mG(A\times B,f)$（定理 3），对下方图形用**截面定理**沿 $x$ 切片，截面恰好是 $G(B,f_{(x\text{固定})})$，其测度再由几何意义等于 $\int_B f(x,y)\,dy$——三个定理首尾相接，Fubini 是它们的直接推论。

**最小实例**：$f(x,y)=x$ 在 $[0,1]\times[0,1]$ 上：
$$\int_{[0,1]^2}x\,dP=\int_0^1dx\int_0^1 x\,dy=\int_0^1 x\,dx=\frac12;$$
另一顺序 $\int_0^1dy\int_0^1 x\,dx$ 同样得 $1/2$。两个顺序都合法（非负可测）。

---

## 八、去脉：本章通向哪里

- **$L^p$ 空间（Ch7 的原料）**：$L^p$ = $\{|f|^p$ 可积$\}$ 按 a.e. 相等分等价类；本章的线性、可数可加、控制收敛保证 $L^p$ 是**完备**的赋范空间——泛函分析就此开场。$L^2$ 是 Hilbert 空间，傅里叶级数在 $L^2$ 中最自然。
- **概率论**：期望 $E[X]=\int_\Omega X\,dP$ 就是勒贝格积分；控制收敛 = 期望与极限交换的标准工具；Fubini = 联合分布化边缘分布。
- **PDE 与变分法**：$L^p$ 完备性让变分问题的最小化序列有极限；积分号下求导（定理 8）是研究解关于参数光滑性的日常工具。
- **Ch6 微分与不定积分**：本章的绝对连续积分（§5.4 定理 3）与 Ch6 的绝对连续函数是同一件事的两面——"$F(x)=\int_a^x f\,dt$ 的 $F$ 绝对连续，且 $F'=f$ a.e."。

> **核心洞察**：勒贝格积分的定义是"**先简单、再单调、后分解**"的三级跳；它的威力浓缩在 LDCT 里——用一个可积控制函数，换掉黎曼时代苛刻的一致收敛。**一句话：测度负责称重，简单函数负责逼近，控制收敛负责换序。**

---

## 九、检验回路

> 验收标准：**明天能把本章讲给别人听**，且能回答"学这干嘛"。

### 9.1 自测题（5 题，含陷阱，先做再看答案）

**Q1（动机复述，必答）** 用自己的话回答：黎曼积分有哪两个治不好的病？勒贝格积分的三步定义各解决什么问题？

> [!note]- 答案
> 两个病：(1) 极限与积分交换需要一致收敛，条件太苛刻；(2) 微积分基本定理不完整——可微函数的导函数（Volterra 例）可以不是 $R$ 可积。三步定义：第一步定义非负简单函数积分（加权和 $\sum c_i mE_i$，唯一能直接算的）；第二步用简单函数从下方逼近，取上确界定义非负可测函数积分（避免直接面对无界/无穷值）；第三步用 $f=f^+-f^-$ 定义一般函数，要求正负部不同时无穷（避开 $\infty-\infty$）。

**Q2（计算）** 用定义计算 $\int_{[0,1]}D(x)\,dx$（$D$ 为狄利克雷函数），并说明为什么黎曼框架算不出这个数而勒贝格框架能。

> [!note]- 答案
> $D=\chi_{\mathbb{Q}\cap[0,1]}$ 是非负简单函数，$[0,1]=(\mathbb{Q}\cap[0,1])\cup([0,1]\setminus\mathbb{Q})$ 是两块可测划分，故 $\int_{[0,1]}D=1\cdot m(\mathbb{Q}\cap[0,1])+0\cdot m([0,1]\setminus\mathbb{Q})=0$。黎曼框架算不出的原因：$D$ 处处不连续，不连续点集测度为 $1\neq0$，不满足"$R$ 可积 $\iff$ a.e. 连续"。

**Q3（Fatou 的严格不等号）** 在 $(0,\infty)$ 上取 $f_n=n\chi_{(0,1/n)}$。分别算出 $\int\varliminf f_n\,dx$ 与 $\varliminf\int f_n\,dx$，并解释"亏"在哪里。

> [!note]- 答案
> 对每个 $x$，当 $n>1/x$ 时 $f_n(x)=0$，故 $f_n\to0$，$\int\lim f_n=0$。而 $\int f_n=n\cdot m(0,1/n)=1$，故 $\varliminf\int f_n=1$。所以 $0<1$。亏在：每点的极限是 $0$，但"质量"（积分 $=1$）随 $n$ 不断向右逃逸，逐点极限看不见总质量的去向；Fatou 只保证 $\leqslant$。

**Q4（控制条件的必要性——陷阱）** 判断："$f_n\to f$ a.e. 且每个 $f_n$ 都 $L$ 可积，则 $\int f_n\to\int f$。" 用 Q3 的序列检验这个论断，并指出 LDCT 缺了哪个条件。

> [!note]- 答案
> **错误**。Q3 的 $f_n=n\chi_{(0,1/n)}$ 满足 $f_n\to0$ a.e. 且 $\int f_n=1<\infty$，但 $\int f_n=1\nrightarrow0=\int f$。缺的条件是**可积控制函数**：这里不存在 $F\in L(0,\infty)$ 使 $|f_n|\leqslant F$ a.e.（否则由 LDCT 必有 $\int f_n\to0$）。"逐点收敛 + 各元可积"不足以换序——这是本章最高频的错误直觉。

**Q5（$L$ 与 $R$ 反常积分的边界）** $f(x)=\sin x/x$ 的 $R$ 反常积分收敛，但它不是 $L$ 可积。为什么？并用一句话说出 $L$ 积分与 $R$ 反常积分的本质差别。

> [!note]- 答案
> 因为正部积分 $\int_{[0,\infty)}f^+=\infty$、负部积分 $\int f^-=\infty$，两者都无穷，$f$ 连"积分确定"都不是。$R$ 反常积分靠正负相消条件收敛；勒贝格积分要求 $\int|f|<\infty$（绝对收敛型），所以 $\sin x/x$ 在 $(R)$ 意义下可积而在 $(L)$ 意义下不可积。

### 9.2 讲给别人听清单（明天验收）

1. **动机复述（必答）**：黎曼积分的两个缺陷 + 三步定义各解决什么；
2. 非负简单函数积分的定义、良定性（公共加细）与三条性质；
3. 非负可测函数积分的定义（上确界），为什么这样定义；
4. 定理 1(2)：$\int f=0\Rightarrow f=0$ a.e. 的 $n^{-1}\chi_{A_n}$ 证明；
5. Levi 定理的完整证明，特别是 $c<1$ 的余量技巧；
6. Fatou 引理与 $n\chi_{(0,1/n)}$ 反例；
7. 一般函数的积分确定与 $L$ 可积的区别；
8. LDCT 的完整证明（Fatou 作用于 $2F-g_n$）与"控制函数不可少"的反例；
9. 黎曼可积 $\iff$ a.e. 连续；$\sin x/x$ 的边界；
10. 几何意义与 Fubini 定理的证明路线（下方图形 → 截面 → 累次）。

### 9.3 回填学习者状态与下一步建议

- 卡在 **Levi 的 $c<1$** → 把 $E_n=E[f_n\geqslant c\varphi]$ 画出来，验证 $E_n\uparrow E$ 需要 $c<1$ 与逐点收敛两件事；
- 卡在 **LDCT 证明** → 先复述 Fatou，再写下 $2F-g_n\geqslant0$ 与 $\int(2F-g_n)\to\int2F$ 的目标，证明只是这两句的展开；
- 卡在 **$\sin x/x$** → 只记结论链：$L$ 可积 $\iff|f|$ 可积；条件收敛的正负面积都无穷；
- **主动建议**：读完本章后把 Ch4 的叶戈罗夫 + Ch5 的 LDCT 连起来看——它们是同一句话"有限测度/可积控制把几乎换成真正"的两种实现；
- **下一步**：Ch6 微分与不定积分按"走马观花"处理（绝对连续函数 ↔ 变上限积分）；然后进入 Ch7 度量空间（泛函分析开场）。

---

## 全包一句话

> **勒贝格积分 = 简单函数称重求和，再用单调逼近与正负分解延拓到所有可测函数；它的全部力量浓缩为一句话：只要有一个可积的控制函数，极限就可以穿过积分号。**

