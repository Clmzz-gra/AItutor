---
type: 节
formal: true
subject: 实变函数与泛函分析
created: 2026-09-21
updated: 2026-09-21
tags: [math, 实变函数与泛函分析]
chapter: 4
section: 4.2
---

# Sec4.2 L^2 空间

> 定位：$p=2$ 时 $L^p$ 上多出一个内积，于是欧氏空间的"角度、垂直、投影、坐标展开"全部可用——$L^2$ 因此成为 Hilbert 空间理论的具体模型。
> 教材：郭懋正《实变函数与泛函分析》§4.2（p.169–184）
> 来源：旧讲解包《Ch9 内积空间和希尔伯特空间》§1.1–§1.4（内积公理、Schwarz、平行四边形、Hilbert 空间例子）；郭版教材 §4.2.1–§4.2.2

> [!info] 关联笔记
> - 父级：[[Ch4 L^p 空间]]
> - 前置：[[Sec4.1 L^p 空间]] ｜ 后续：[[Sec4.3 卷积与 Fourier 变换]]
> - 概念：[[概念-Lp空间]] ｜ [[概念-完备性]]

---

## 来龙（为什么需要它）

- **类比已知**：在 $\mathbb{R}^n$ 中，模长公式是 $\|x\|=\sqrt{\sum_{i=1}^n x_i^2}$。把求和换成积分，$L^p$ 范数就是 $\left(\int|f|^p\right)^{1/p}$——**只有 $p=2$ 时它才是 $\mathbb{R}^n$ 模长公式的直接推广**（$\sqrt{\sum x_i^2}$ 与 $\left(\int|f|^2\right)^{1/2}$ 形状一致）。$\mathbb{R}^n$ 中角度、垂直性、平行性都来自内积 $(x,y)=\sum_i x_iy_i$，而 $\sum_i x_iy_i$ 换成积分就是 $\int fg$。所以 $L^2$ 天然继承 $\mathbb{R}^n$ 的全部几何。
- **解决新问题**：$L^p$ 只给了"长度"，没有给"角度"。没有角度就无法回答"哪个函数与哪个函数垂直""用一组基函数逼近 $f$，系数取多少误差最小"。傅里叶级数需要一个几何解释：$\{1,\cos nx,\sin nx\}$ 两两"垂直"——这里的垂直不是画图，而是 $\int_{-\pi}^{\pi}\cos nx\sin mx\,\mathrm{d}x=0$。**把积分看成内积，傅里叶级数就变成"函数在正交坐标系下的展开"，系数就是投影。**
- **理论/应用需要**：$p=2$ 的共轭指数 $q$ 恰好也是 $2$，于是 $f,g\in L^2(E)$ 时 $fg\in L^1(E)$——内积 $\int fg$ 才有意义。这一"自共轭"的特殊性使 $L^2$ 在 $L^p$ 理论中占据枢纽地位：它是量子力学的态空间（概率幅的平方可积），是信号的能量空间，也是唯一能从范数反推出内积的 $L^p$ 空间。

## 主体（核心内容）

### 4.2.1 $L^2$ 空间的内积

**定义**（郭版定义 4.2.1）：对于 $f,g\in L^2(E)$，记
$$(f,g)=\int_E f(x)g(x)\,\mathrm{d}x,$$
称 $(f,g)$ 为 $f$ 与 $g$ 的**内积**（读作"$f$ 与 $g$ 的内积"）。在抽象测度空间 $(X,\mathcal{F},\mu)$ 上，$L^2(X,\mathcal{F},\mu)$ 的内积定义为
$$(f,g)=\int_X f(x)g(x)\,\mu(\mathrm{d}x).$$

> **复值情形的写法**：当 $f,g$ 取复值时，上面这个式子必须改成 $(f,g)=\displaystyle\int_E f(x)\overline{g(x)}\,\mathrm{d}x$（$\overline{g}$ 读作"$g$ 的共轭"），否则正定性会失效——见本节反例 1。郭版 §4.2 讨论的是实值情形，两种写法在实值函数上完全一致。

**由内积导出范数**：$\|f\|_2=\sqrt{(f,f)}$。本节以下把 $\|f\|_2$ 简记作 $\|f\|$。

**Schwarz 不等式**：Schwarz 不等式 (4.1.9) 现在可以写成内积形式
$$|(f,g)|\le\|f\|\,\|g\|.$$

**定理**（内积公理，郭版定理 4.2.2）：内积具有以下性质：
1. **双线性性**：$(f,g)$ 分别关于 $f$ 与 $g$ 是线性的；
2. **对称性**：$(f,g)=(g,f)$（复值情形改为**共轭对称** $(f,g)=\overline{(g,f)}$）；
3. **正定性**：$(f,f)\ge 0$，且 $(f,f)=0$ 当且仅当 $f=0$，$\mathrm{a.e.}[E]$。

这三条由定义式直接推得。**关键观察**：本节许多结果只依赖这三条公理，而不必用到内积的具体表达式——**因为** 推导过程中只出现"线性""对称""正定"三种操作。这就允许我们从公理出发抽象地展开一个**内积空间**理论，$L^2$ 只是其中的一个具体模型（一般理论见 Ch5 §5.2）。

**旧讲解包给出的抽象内积公理**（复线性空间 $X$ 上，$\langle x,y\rangle$ 读作"$x$ 与 $y$ 的内积"）：
1. $\langle x,x\rangle\ge 0$，且 $\langle x,x\rangle=0\iff x=0$；
2. 对第一个变元线性：$\langle\alpha x+\beta y,z\rangle=\alpha\langle x,z\rangle+\beta\langle y,z\rangle$；
3. **共轭对称**：$\langle x,y\rangle=\overline{\langle y,x\rangle}$（实空间时即 $\langle x,y\rangle=\langle y,x\rangle$）。

由 2、3 立刻推出**对第二个变元共轭线性**：$\langle x,\alpha y+\beta z\rangle=\bar\alpha\langle x,y\rangle+\bar\beta\langle x,z\rangle$。**导出范数**定义为 $\|x\|=\sqrt{\langle x,x\rangle}$。

**Schwarz 不等式的证明**（内积公理版，每一步有"因为"）：$y=0$ 时平凡。$y\ne 0$ 时，对任意复数 $\alpha$，
$$0\le\langle x-\alpha y,x-\alpha y\rangle=\|x\|^2-\bar\alpha\langle x,y\rangle-\alpha\big[\langle y,x\rangle-\bar\alpha\|y\|^2\big],$$
**因为** 左端是自身的内积，由正定性非负。取 $\bar\alpha=\dfrac{\langle y,x\rangle}{\|y\|^2}$ 使方括号为 $0$（**因为** $y\ne 0$ 时 $\|y\|^2>0$ 可作除数），得
$$0\le\|x\|^2-\frac{|\langle x,y\rangle|^2}{\|y\|^2},$$
移项开方即得 $|\langle x,y\rangle|\le\|x\|\,\|y\|$。$\square$

**三角不等式由此推出**（不必再用 Hölder）：
$$\|x+y\|^2=\|x\|^2+\langle x,y\rangle+\overline{\langle x,y\rangle}+\|y\|^2\le\|x\|^2+2\|x\|\,\|y\|+\|y\|^2=(\|x\|+\|y\|)^2.$$
**这一步说明**：$L^2$ 的三角不等式（Minkowski 不等式在 $p=2$ 的情形）可以由内积推出，**不必**再走 §4.1 中"$|f+g|^{p-1}$ 配 Hölder"那条路——两条路殊途同归，这正是 $p=2$ 特殊性的一个体现。

**平行四边形公式与极化恒等式**（内积范数的特征）：
$$\|x+y\|^2+\|x-y\|^2=2\big(\|x\|^2+\|y\|^2\big).$$
**逆命题**：赋范空间若对一切 $x,y$ 满足平行四边形公式，则可用**极化恒等式**定义内积
$$\langle x,y\rangle=\frac14\Big(\|x+y\|^2-\|x-y\|^2+\mathrm{i}\|x+\mathrm{i}y\|^2-\mathrm{i}\|x-\mathrm{i}y\|^2\Big)$$
（实空间去掉后两项），且该内积导出原来的范数。**用途**：判定一个赋范空间是否可能来自内积，只需检验平行四边形公式——这是区分"$L^2$ 型"与"一般 $L^p$ 型"的判别法。

**内积的连续性**：由 Schwarz 不等式，$x_n\to x$、$y_n\to y$ $\Rightarrow$ $\langle x_n,y_n\rangle\to\langle x,y\rangle$。**因为** 把差拆成 $\langle x-x_n,y_n\rangle$ 与 $\langle x,y-y_n\rangle$ 两项分别估计，并用到收敛列有界。这条性质在 §4.2.2 讨论弱收敛时是关键工具。

**反例 1（复值情形必须共轭）**：设 $E$ 有正测度，取复值函数 $f=\mathrm{i}\,\chi_E$。若沿用 $(f,g)=\int fg$ 的定义，则
$$(f,f)=\int_E \mathrm{i}^2\chi_E^2\,\mathrm{d}x=-\int_E\mathrm{d}x=-m(E)<0,$$
**因为** $\mathrm{i}^2=-1$。正定性当场失效。改用 $(f,g)=\int f\bar g$ 后，$(f,f)=\int_E|\mathrm{i}|^2\chi_E\,\mathrm{d}x=m(E)>0$，正定性恢复。**结论**：复 $L^2$ 的内积定义中"取共轭"不是记号的装饰，而是正定性所必需的。

**反例 2（Schwarz 取等号的边界）**：Schwarz 不等式的等号成立 $\iff$ $f,g$ 线性相关（a.e.）。取 $E=[0,1]$，$f=\chi_{[0,1/2]}$，$g=\chi_{[1/2,1]}$。则 $(f,g)=\int fg=0$，而 $\|f\|=\|g\|=1/\sqrt2$，于是 $|(f,g)|=0<1/2=\|f\|\|g\|$，**严格**不等。**因为** $f,g$ 不线性相关（不存在常数 $c$ 使 $f=cg$，$\mathrm{a.e.}$），等号条件不满足。特别地，**正交的非零元素必使 Schwarz 严格不等**。

**例题**：在 $L^2[0,1]$ 中求 $f(t)=t$ 在子空间 $M=\operatorname{span}\{1\}$（常值函数全体）中的最佳逼近，并验证正交性。

- **原始信息**：$M$ 是一维子空间，元素形如 $\alpha\cdot 1$；要找一个 $\alpha$ 使 $\|t-\alpha\|$ 最小。
- **代入**：$\|t-\alpha\|^2=\displaystyle\int_0^1(t-\alpha)^2\,\mathrm{d}t=\frac13-\alpha+\alpha^2$。
- **计算**：这是 $\alpha$ 的二次函数，**因为** 二次项系数 $1>0$，在 $\alpha=\dfrac12$ 处取最小值 $\dfrac13-\dfrac14=\dfrac1{12}$。
- **验证正交**：$\langle t-\tfrac12,\,1\rangle=\displaystyle\int_0^1\left(t-\tfrac12\right)\mathrm{d}t=\frac12-\frac12=0$，**因为** $t-\tfrac12$ 在 $[0,1]$ 上关于中点反对称，积分为零。
- **结论**：最佳逼近是 $\alpha=\dfrac12$，误差 $\|t-\tfrac12\|=\dfrac{1}{\sqrt{12}}$。**这不是巧合**：最佳逼近误差向量必与逼近子空间正交，这条"正交性原理"是 Ch5 §5.2 投影定理在 $L^2$ 中的具体形态。

### 4.2.2 $L^2$ 空间的性质

**定义**（弱收敛，郭版定义 4.2.3）：设 $f,f_m\in L^2(E)$。若对**任意** $g\in L^2(E)$ 都有
$$\lim_{m\to\infty}(f_m,g)=(f,g),$$
就称函数列 $\{f_m\}$ **弱收敛**到 $f$，记作 $w\text{-}\lim_{m\to\infty}f_m=f$，也可简记 $f_m\rightharpoonup f$ 或 $f_m\xrightarrow{w}f$。**读法**：$w$ 是 weak（弱）的首字母；$\rightharpoonup$ 读作"弱收敛到"。

易见弱收敛极限唯一（**因为** 若 $f_m\rightharpoonup f$ 且 $f_m\rightharpoonup h$，则对一切 $g$ 有 $(f-h,g)=0$，取 $g=f-h$ 得 $\|f-h\|^2=0$）。

**定理**（强收敛的弱刻画，郭版定理 4.2.4）：设 $f\in L^2(E)$，$\{f_m\}\subset L^2(E)$，则 $f_m\xrightarrow{L^2}f$ 的**充分必要条件**是：
1. $f_m\xrightarrow{w}f$；
2. $\lim_{m\to\infty}\|f_m\|=\|f\|$。

**证明**：
- **必要性**：已知 $\|f_m-f\|\to 0$。由 $\big|\|f_m\|-\|f\|\big|\le\|f_m-f\|$（范数连续性）得 (2)；对任意 $g$，由 $|(f_m,g)-(f,g)|\le\|f_m-f\|\cdot\|g\|$（Schwarz）得 (1)。
- **充分性**：**因为** 范数可由内积展开，
$$\|f_m-f\|^2=(f_m-f,f_m-f)=(f_m,f_m)-2(f_m,f)+(f,f)\to\|f\|^2-2\|f\|^2+\|f\|^2=0,$$
其中 $(f_m,f)\to(f,f)=\|f\|^2$ 由 (1) 取 $g=f$ 得到，$(f_m,f_m)=\|f_m\|^2\to\|f\|^2$ 由 (2) 得到。$\square$

**这条定理的读法**：$L^2$ 收敛 = "所有方向上的投影都收敛" + "长度也收敛"。**缺一不可**——只去掉长度条件就只剩弱收敛（见反例 3），只去掉投影条件则连方向都不对。

**定理**（弱收敛的稠集判据，郭版定理 4.2.5）：设 $\{f_m\}\subset L^2(E)$，$f\in L^2(E)$。若
1. $\|f_m\|\le M$（**一致有界**）；
2. 存在**稠集** $\Gamma\subset L^2(E)$ 使 $\lim_m(f_m,g)=(f,g)$ 对一切 $g\in\Gamma$ 成立，

则 $w\text{-}\lim_m f_m=f$。

**证明概要**：不妨设 $\|f\|<M$。对任意 $h\in L^2(E)$ 与 $\varepsilon>0$，**因为** $\Gamma$ 稠密，存在 $g\in\Gamma$ 使 $\|g-h\|<\dfrac{\varepsilon}{2M}$。于是
$$|(f_m,h)-(f,h)|\le|(f_m-f,g)|+\|f_m-f\|\,\|g-h\|\le|(f_m-f,g)|+2M\cdot\frac{\varepsilon}{2M},$$
第一个不等号**因为** 插入 $g$ 并拆项、对第二项用 Schwarz，第二个**因为** $\|f_m-f\|\le\|f_m\|+\|f\|\le 2M$。令 $m\to\infty$，由条件 (2) 第一项趋于 $0$，得 $\varlimsup_m|(f_m,h)-(f,h)|\le\varepsilon$，由 $\varepsilon$ 任意得结论。$\square$

> 事实上条件 (1)(2) 也是弱收敛的必要条件（可用 Ch6 §6.2 的共鸣定理证明）。**实用价值**：验证弱收敛只需在一组"好函数"（如三角函数、连续函数）上检验，不必对每个 $g\in L^2$ 验证——这是傅里叶分析中"弱收敛"判定的标准套路。

**定义**（正交与标准正交系，郭版定义 4.2.6）：设 $f,g\in L^2(E)$。若 $(f,g)=0$，称 $f$ 与 $g$ **正交**（或垂直），记作 $f\perp g$（读作"$f$ 正交于 $g$"）。若函数列 $\{\varphi_a\}_{a\in A}\subset L^2(E)$ 中任意两个元素都正交，称它是**正交系**；若进一步对一切 $a$ 有 $\|\varphi_a\|=1$，称它是**标准正交系**（也称归一正交系）。

显然 $\{\varphi_a\}$ 是标准正交系 $\iff$
$$(\varphi_a,\varphi_b)=\delta_{ab},$$
其中 $\delta_{ab}$ 是 **Kronecker 记号**：
$$\delta_{ab}=\begin{cases}1,&a=b,\\0,&a\ne b.\end{cases}$$
若正交系中每个 $\|\varphi_a\|\ne 0$，则 $\varphi_a/\|\varphi_a\|$ 就是标准正交系（**因为** 除以自身范数后长度变为 $1$，而正交性在数乘下保持）。

**定理**（郭版定理 4.2.7）：$L^2(E)$ 中任一标准正交系都是**可数**的。

**证明**：设 $\{\varphi_a\}_{a\in A}$ 是标准正交系，则当 $a\ne b$ 时
$$\|\varphi_a-\varphi_b\|^2=(\varphi_a-\varphi_b,\varphi_a-\varphi_b)=(\varphi_a,\varphi_a)+(\varphi_b,\varphi_b)=2,$$
**因为** 交叉项 $(\varphi_a,\varphi_b)$ 与 $(\varphi_b,\varphi_a)$ 都为零。令 $U_a=\{f\in L^2(E)\mid\|f-\varphi_a\|<1\}$（称为 $\varphi_a$ 的**球形邻域**），**因为** 两球心距离 $\sqrt2>1+1$ 不成立但 $1+1=2>\sqrt2$，故 $a\ne b$ 时 $U_a\cap U_b=\varnothing$：$\{U_a\}_{a\in A}$ 是一族互不相交的非空开集。**因为** $L^2(E)$ 可分（定理 4.1.18），每个 $U_a$ 内可取到一个可数稠密子集中的点，互不相交保证这些点两两不同，故 $\{U_a\}$ 只能可数。$\square$

**例**：$L^2[-\pi,\pi]$ 中的三角函数列
$$\frac{1}{\sqrt{2\pi}},\quad \frac{1}{\sqrt{\pi}}\cos x,\quad \frac{1}{\sqrt{\pi}}\sin x,\quad \dots,\quad \frac{1}{\sqrt{\pi}}\cos kx,\quad \frac{1}{\sqrt{\pi}}\sin kx,\quad\dots$$
是标准正交系。**因为** 三角函数系的正交性来自周期函数的积分：$\int_{-\pi}^{\pi}\cos kx\sin lx\,\mathrm{d}x=0$ 对一切 $k,l$；$\int_{-\pi}^{\pi}\cos kx\cos lx\,\mathrm{d}x=0$（$k\ne l$）；而 $\int_{-\pi}^{\pi}\cos^2kx\,\mathrm{d}x=\pi$、$\int_{-\pi}^{\pi}1^2\,\mathrm{d}x=2\pi$，除以范数即得归一化。

**定义**（Fourier 系数与 Fourier 级数，郭版定义 4.2.8）：设 $\{\varphi_k\}$ 是 $L^2(E)$ 中的标准正交系，$f\in L^2(E)$。称
$$c_k=(f,\varphi_k)=\int_E f(x)\varphi_k(x)\,\mathrm{d}x,\quad k=1,2,\dots$$
为 $f$（关于正交系 $\{\varphi_k\}$）的 **Fourier 系数**；称 $\displaystyle\sum_{k=1}^\infty c_k\varphi_k$ 为 $f$ 的 **Fourier 级数**，简记为 $f\sim\displaystyle\sum_{k=1}^\infty c_k\varphi_k$。

**级数收敛的含义**：记 $S_N=\sum_{k=1}^N c_k\varphi_k$，若存在 $f\in L^2(E)$ 使 $\lim_N\|S_N-f\|=0$，就说该级数收敛且和为 $f$，记 $f=\sum_{k=1}^\infty c_k\varphi_k$。此时由定理 4.2.4，
$$(f,\varphi_j)=\lim_{N\to\infty}(S_N,\varphi_j)=\lim_{N\to\infty}\sum_{k=1}^N c_k(\varphi_k,\varphi_j)=c_j,$$
**因为** 内积连续、且标准正交性使求和号中只有 $k=j$ 项存活。这说明"Fourier 系数就是投影"这一几何直觉在无穷维完全成立。

**定理**（Bessel 不等式，郭版定理 4.2.9）：设 $\{\varphi_k\}$ 是 $L^2(E)$ 中的标准正交系，$f\in L^2(E)$，则 $f$ 的 Fourier 系数满足
$$\sum_{k=1}^\infty c_k^2\le\|f\|^2.$$

**证明**：令 $S_N=\sum_{k=1}^N c_k\varphi_k$，则
$$\|f-S_N\|^2=\Big(f-\sum_{k=1}^N c_k\varphi_k,\ f-\sum_{k=1}^N c_k\varphi_k\Big)=\|f\|^2-2\sum_{k=1}^N c_k^2+\sum_{k=1}^N c_k^2=\|f\|^2-\sum_{k=1}^N c_k^2\ge 0,$$
**因为** 展开后交叉项由标准正交性只剩 $k=j$ 的对角项、且 $\|f-S_N\|^2$ 作为范数平方非负。令 $N\to\infty$ 即得。$\square$

**读法**：$\sum c_k^2$ 是 $f$ 在正交系上"已捕获的能量"，它不能超过 $f$ 的总能量 $\|f\|^2$——**因为** 剩下的部分 $\|f-S_N\|^2$ 是"没捕获到的能量"，恒非负。

**定理**（Riesz–Fischer 定理，郭版定理 4.2.10）：设 $\{\varphi_k\}$ 是 $L^2(E)$ 中的标准正交系。若实数列 $\{c_k\}$ 满足 $\sum_{k=1}^\infty c_k^2<\infty$，则级数 $\sum_{k=1}^\infty c_k\varphi_k$ 在 $L^2(E)$ 中收敛；把它的和记为 $f$，则 $(f,\varphi_k)=c_k$，且
$$\Big\|\sum_{k=1}^\infty c_k\varphi_k\Big\|^2=\sum_{k=1}^\infty c_k^2.$$

**证明**：作部分和 $S_N=\sum_{k=1}^N c_k\varphi_k$，则
$$\|S_{N+p}-S_N\|^2=\sum_{k=N+1}^{N+p}c_k^2,$$
**因为** 标准正交性使展开后无交叉项。**因为** $\sum c_k^2$ 收敛，右端当 $N\to\infty$ 时对一切 $p$ 一致趋于 $0$，故 $\{S_N\}$ 是 $L^2(E)$ 中的**基本列**；**因为** $L^2$ 完备（§4.1.3 的 Riesz–Fischer 完备性定理），它必收敛。再由内积连续得 $\|f\|^2=\lim_N\|S_N\|^2=\sum c_k^2$ 与 $(f,\varphi_k)=c_k$。$\square$

> **两条 Riesz–Fischer 定理要分清**：§4.1.3 的那条说的是"**基本列必收敛**"（空间的完备性）；本条的则是"**系数列平方可和 $\Rightarrow$ 级数收敛**"（展开的存在性）。后者是前者的直接应用，故同名。旧讲解包给出的"选快子列 → Levi → Fatou"三步骨架对应的是**前者**。

**定义**（郭版 (4.2.14)）：记
$$\Gamma=\Big\{\sum_{k=1}^\infty a_k\varphi_k\ \Big|\ \{a_k\}\text{ 是实数列，}\sum_{k=1}^\infty a_k^2<\infty\Big\},$$
即由给定标准正交系"能张成"的全体。

**定理**（最佳逼近，郭版定理 4.2.11）：对任意 $f\in L^2(E)$，令 $\widetilde f=\sum_{k=1}^\infty c_k\varphi_k$（$c_k$ 为 $f$ 的 Fourier 系数），则 $\widetilde f\in\Gamma$，且
$$\|f-\widetilde f\|=\min_{g\in\Gamma}\|f-g\|.$$

**证明概要**：$\widetilde f\in\Gamma$ 由 Bessel 不等式与 Riesz–Fischer 定理得到。对任意 $g=\sum a_k\varphi_k\in\Gamma$，
$$\|f-g\|^2=\lim_{N\to\infty}\Big[\|f\|^2+\sum_{k=1}^N(a_k-c_k)^2-\sum_{k=1}^N c_k^2\Big]\ge\|f\|^2-\sum_{k=1}^\infty c_k^2=\|f-\widetilde f\|^2,$$
**因为** 中间的平方和 $\sum(a_k-c_k)^2\ge 0$，当且仅当 $a_k=c_k$ 对一切 $k$ 成立时取等号。$\square$

**定义**（完全系与标准正交基，郭版定义 4.2.12、4.2.13）：
- 若 $L^2(E)$ 中不再存在非零的 $f$ 能与一切 $\varphi_k$ 正交，称正交系 $\{\varphi_k\}$ 是 $L^2(E)$ 中的**完全系**。等价说法：若 $f\in L^2(E)$ 且 $(f,\varphi_k)=0$（$k=1,2,\dots$），则必有 $f(x)=0$，$\mathrm{a.e.}[E]$。
- 若每个 $f\in L^2(E)$ 都可表成在 $L^2(E)$ 中收敛的级数 $f=\sum_{k=1}^\infty c_k\varphi_k$，称 $\{\varphi_k\}$ 是 $L^2(E)$ 的一个**标准正交基**。

**定理**（五条等价，郭版定理 4.2.14）：设 $\{\varphi_k\}$ 是 $L^2(E)$ 中的标准正交系，则以下条件等价：
1. $\{\varphi_k\}$ 是标准正交基；
2. $\{\varphi_k\}$ 的**有限线性组合之全体**在 $L^2(E)$ 中稠密；
3. **完全性**：$L^2(E)$ 中不再存在非零元素能与一切 $\varphi_k$ 正交；
4. **Parseval 等式**：$\|f\|^2=\sum_{k=1}^\infty|(f,\varphi_k)|^2$ 对一切 $f\in L^2(E)$ 成立；
5. **内积等式**：$(f,g)=\sum_{k=1}^\infty(f,\varphi_k)(\varphi_k,g)$ 对一切 $f,g\in L^2(E)$ 成立。

**证明脉络**：
- (1)$\iff$(4)：由 $\|f-S_N\|^2=\|f\|^2-\|S_N\|^2=\|f\|^2-\sum_{k=1}^N c_k^2$（**因为** 标准正交性消去交叉项），故 $\lim_N\|f-S_N\|=0$ $\iff$ Parseval 成立。
- (1)$\Rightarrow$(2)：**因为** 级数的部分和本身就是有限线性组合，收敛即稠密。
- (2)$\Rightarrow$(3)：设 $f\perp\varphi_k$ 对一切 $k$。任给 $\varepsilon>0$，由 (2) 存在有限线性组合 $g=\sum_{i=1}^n c_i\varphi_i$ 使 $\|f-g\|<\varepsilon$。**因为** $f\perp g$，故
$$\|f\|^2=(f,f-g)+(f,g)=(f,f-g)\le\|f\|\,\|f-g\|\le\varepsilon\|f\|,$$
由此 $\|f\|=0$，即 $f=0$，$\mathrm{a.e.}[E]$。
- (3)$\Rightarrow$(1)：令 $\widetilde f=\sum_{k=1}^\infty c_k\varphi_k$（由 Bessel + Riesz–Fischer 合法），则 $(\widetilde f,\varphi_k)=c_k=(f,\varphi_k)$，**因为** 内积连续；于是 $(f-\widetilde f)\perp\varphi_k$ 对一切 $k$，由 (3) 得 $\widetilde f=f$。
- (4)$\Rightarrow$(5)：**因为** 实内积可由范数用极化恒等式恢复，$(f,g)=\dfrac14\big(\|f+g\|^2-\|f-g\|^2\big)$，把 (4) 分别用于 $f+g$ 与 $f-g$ 再相减即得 (5)；(5)$\Rightarrow$(4) 取 $g=f$ 显然。$\square$

**例**（郭版 §4.2 例 1）：$L^2[-\pi,\pi]$ 中的三角函数系 (4.2.17) 是标准正交系，**且是标准正交基**——**因为** 三角多项式的全体在 $C[-\pi,\pi]$ 中稠密（Weierstrass 三角逼近定理），从而在 $L^2[-\pi,\pi]$ 中稠密（由 §4.1.4 的 $C_c$ 逼近台阶），于是由定理 4.2.14 的 (2)$\Rightarrow$(1) 得结论。因此每个 $f\in L^2[-\pi,\pi]$ 都可展开成 $L^2$ 收敛的 Fourier 级数
$$f(x)=\frac12a_0+\sum_{n=1}^\infty a_n\cos nx+b_n\sin nx.$$
由定理 4.2.14 的 (4)(5) 还得到
$$\|f\|=\Big(\sum_{k=1}^\infty|c_k|^2\Big)^{1/2},\qquad (f,g)=\sum_{k=1}^\infty c_kd_k,$$
**这两式正是欧氏空间中模长与内积公式的推广**，充分显示出标准正交基与直角坐标系的类似性。

**反例 3（弱收敛推不出强收敛）**：设 $\{e_k\}$ 是 $L^2(E)$ 中的标准正交列。对任意 $g\in L^2(E)$，由 Bessel 不等式 $\sum_k(e_k,g)^2\le\|g\|^2<\infty$，**因为** 收敛级数的通项趋于零，得 $(e_k,g)\to 0=(0,g)$，故 $e_k\xrightarrow{w}0$。但 $\|e_k\|=1\not\to 0=\|0\|$，所以 $e_k$ **不**依 $L^2$ 收敛到 $0$。**结论**：定理 4.2.4 中的条件 (2)"长度也收敛"不可少——弱收敛只保证"所有方向上的投影趋于零"，不保证"长度趋于零"。物理上这就是"能量不流失但方向乱转"。

**反例 4（正交系不完全时，Fourier 级数不等于 $f$）**：取 $L^2[-\pi,\pi]$ 中的标准正交系 $\{\varphi_k\}$ 为三角函数系中去掉 $\cos x/\sqrt\pi$ 后剩下的子系。**因为** 剩下的系仍标准正交，但不完全（**因为** $\cos x/\sqrt\pi$ 与子系中每个元素都正交且非零），由定理 4.2.14 的条件 (3) 失败知它不是标准正交基。取 $f(x)=\cos x$，则 $f$ 关于子系的 Fourier 系数**全为零**，故 $\widetilde f=0\ne f$，Bessel 不等式取**严格**不等号：$0<\|\cos x\|^2=\pi$。**结论**：Bessel 不等式是"不超过"，等号成立需要完全性（Parseval 等式）——这正是定理 4.2.14 中 (1)$\iff$(4) 的内容。

**例题**：利用三角函数系是 $L^2[-\pi,\pi]$ 的标准正交基，用 Parseval 等式求 $\displaystyle\sum_{n=1}^\infty\frac{1}{n^2}$。

- **原始信息**：取 $f(x)=x$ 于 $[-\pi,\pi]$，它在 $L^2[-\pi,\pi]$ 中（**因为** $\int_{-\pi}^\pi x^2\,\mathrm{d}x=\dfrac{2\pi^3}{3}<\infty$）；三角函数系 (4.2.17) 是标准正交基，故 Parseval 等式成立。
- **代入**：逐个算 Fourier 系数。
  - $c_0=\Big(x,\dfrac{1}{\sqrt{2\pi}}\Big)=\dfrac{1}{\sqrt{2\pi}}\displaystyle\int_{-\pi}^{\pi}x\,\mathrm{d}x=0$，**因为** $x$ 是奇函数。
  - $\Big(x,\dfrac{\cos nx}{\sqrt\pi}\Big)=\dfrac{1}{\sqrt\pi}\displaystyle\int_{-\pi}^{\pi}x\cos nx\,\mathrm{d}x=0$，**因为** $x\cos nx$ 也是奇函数。
  - $\Big(x,\dfrac{\sin nx}{\sqrt\pi}\Big)=\dfrac{1}{\sqrt\pi}\displaystyle\int_{-\pi}^{\pi}x\sin nx\,\mathrm{d}x=\dfrac{2}{\sqrt\pi}\displaystyle\int_0^{\pi}x\sin nx\,\mathrm{d}x$，**因为** 被积函数为偶函数。分部积分（取 $u=x$、$\mathrm{d}v=\sin nx\,\mathrm{d}x$）得
  $$\int_0^\pi x\sin nx\,\mathrm{d}x=\Big[-\frac{x\cos nx}{n}\Big]_0^\pi+\frac1n\int_0^\pi\cos nx\,\mathrm{d}x=-\frac{\pi\cos n\pi}{n}+\frac{\sin n\pi}{n^2}=\frac{(-1)^{n+1}\pi}{n},$$
  **因为** $\cos n\pi=(-1)^n$、$\sin n\pi=0$。故 $c_n=\dfrac{2(-1)^{n+1}\sqrt\pi}{n}$。
- **计算**：$\|f\|^2=\displaystyle\int_{-\pi}^{\pi}x^2\,\mathrm{d}x=\frac{2\pi^3}{3}$；而 $\sum_{n=1}^\infty c_n^2=\sum_{n=1}^\infty\dfrac{4\pi}{n^2}$。Parseval 等式给出
  $$\frac{2\pi^3}{3}=\sum_{n=1}^\infty\frac{4\pi}{n^2}\quad\Longrightarrow\quad \sum_{n=1}^\infty\frac{1}{n^2}=\frac{2\pi^3}{3}\cdot\frac{1}{4\pi}=\frac{\pi^2}{6}.$$
- **结论**：$\displaystyle\sum_{n=1}^\infty\frac{1}{n^2}=\frac{\pi^2}{6}$（Euler 1735 年得到的经典结果）。**这个例题的意义**：Parseval 等式把一个"函数空间中的能量守恒"翻译成了一个数论恒等式——这说明 $L^2$ 的几何语言确实能反过来解决经典分析问题。

**本节收束**：$L^2(E)$ 是一个**可分的 Hilbert 空间**——可分性来自 §4.1.4（$1\le p<\infty$ 时 $L^p$ 可分），完备性来自 §4.1.3（Riesz–Fischer），内积来自本节 §4.2.1。三条合起来，$L^2$ 就成了"无穷维欧氏空间"的具体模型：有长度、有角度、有正交基、有坐标展开。

## 去脉（学完去哪）

- **当代应用**：$L^2$ 是量子力学的态空间（波函数 $\psi$ 满足 $\int|\psi|^2=1$，概率解释正是归一化）；信号处理中 $\|f\|^2$ 是能量，Parseval 等式就是"时域能量 = 频域能量"；统计与机器学习中条件期望是 $L^2$ 意义下的正交投影，核方法（RKHS）中的再生核 Hilbert 空间直接建立在 Riesz 表示定理上。
- **跨领域解读**：**"最佳逼近 = 正交投影"** 是本节最有迁移价值的一条原理：它把"求最小值"的优化问题转成"解正交方程"的线性问题。§4.2.1 例题中"$\alpha=\tfrac12$ 使 $\|t-\alpha\|$ 最小"与"$\int_0^1(t-\alpha)\,\mathrm{d}t=0$"是同一件事，这个等价在最小二乘、有限元、谱方法中反复出现。
- **高层视角**：$L^2$ 的几何来自三条内积公理，而**公理本身不依赖 $\int fg$ 这个具体形式**——于是可以抽象出"内积空间"，再补上完备性得到"Hilbert 空间"。**$L^2$ 只是 Hilbert 空间的一个具体模型**，一般理论（投影定理、规范正交系、Riesz 表示定理、自伴/酉/正规算子）见 Ch5 §5.2、§5.3。另一条伏笔是：由 $p=2$ 的"自共轭"性质（$q=2$），本节的正交展开将在 [[Sec4.3 卷积与 Fourier 变换]] 中升级为 $L^2(\mathbb{R}^n)$ 上的 Plancherel 定理——那里 Fourier 变换被证明是 $L^2$ 到自身的**等距同构**，是本节"正交基展开"在连续群上的形态。

## 防跳跃

- [ ] **$L^2$ 可分性的来源**：定理 4.2.7（标准正交系可数）依赖 $L^2$ 可分（§4.1.4）。若测度空间不可分（例如 $[0,1]$ 上每个点配测度 $1$ 的计数测度），$L^2$ 不可分，标准正交系可以不可数——郭版未讨论，需要时另找材料。
- [ ] **平行四边形公式的逆命题证明**：本节只给结论（旧讲解包列为习题 5）。完整证明需验证极化恒等式定义的 $\langle\cdot,\cdot\rangle$ 满足内积三公理，其中"对第一变元线性"的验证较繁。
- [ ] **弱收敛的完整刻画**：定理 4.2.5 的充分性本节已证，必要性郭版指出"可用 Ch6 定理 6.2.8 或其证明方法"——即共鸣定理（一致有界原理），需先学 Ch6 §6.2。
- [ ] **$\Gamma$ 是 $L^2(E)$ 的闭子空间**：当 $\{\varphi_k\}$ 不完全时 $\Gamma\ne L^2(E)$，$\Gamma$ 是 $L^2$ 的真闭子空间，最佳逼近定理 4.2.11 说的正是"$\widetilde f$ 是 $f$ 在 $\Gamma$ 上的投影"。投影定理的一般形态见 Ch5 §5.2。
- [ ] **三角多项式在 $C[-\pi,\pi]$ 中稠密**（Weierstrass 三角逼近定理）：这是判定三角函数系为**标准正交基**的关键一步，郭版只引用未证。证明思路（Fejér 核或卷积平滑）在 [[Sec4.3 卷积与 Fourier 变换]] 的逼近恒等元处会有呼应。
- [ ] **复 $L^2$ 的共轭约定**：郭版 §4.2 取实值情形，本节补注了复值写法 $(f,g)=\int f\bar g$。复 $L^2$ 中 Parseval 等式要写成 $\|f\|^2=\sum|(f,\varphi_k)|^2$（带模），定理 4.2.14 已按此写。

## 来源与映射

| 本节点内容 | 来源 | 处理 |
|---|---|---|
| 内积定义 $(f,g)=\int_E fg$、$\|f\|_2=\sqrt{(f,f)}$ | 郭版教材 §4.2.1 定义 4.2.1 | 原文迁移 |
| 抽象测度空间上的内积 | 郭版教材 §4.2.1 注 | 原文迁移 |
| 复值情形取共轭的必要性 | 本节推演 | 新写（补反例 1，郭版只讨论实值情形） |
| 内积三公理（双线性/对称/正定） | 郭版教材 §4.2.1 定理 4.2.2 | 原文迁移 |
| 复内积公理（共轭对称）、导出范数 | 旧《Ch9》§1.1 | 原文迁移（与郭版公理并列，标注差异） |
| Schwarz 不等式及证明 | 旧《Ch9》§1.2；郭版教材 §4.2.1 (4.2.3) | 合并：郭版只引用 (4.1.9)，旧讲解包给内积公理版证明 |
| 由内积推出三角不等式 | 旧《Ch9》§1.2 | 原文迁移 |
| 平行四边形公式与极化恒等式 | 旧《Ch9》§1.3 | 原文迁移 |
| 内积的连续性 | 旧《Ch9》§1.4 | 原文迁移 |
| Schwarz 等号条件的边界反例 | 本节推演 | 新写（补反例 2） |
| 最佳逼近例题（$f=t$ 在 $\operatorname{span}\{1\}$ 上投影） | 旧《Ch9》§7.1 自测题 Q2 | 原文迁移并展开为完整例题 |
| 弱收敛定义 | 郭版教材 §4.2.2 定义 4.2.3 | 原文迁移 |
| $L^2$ 收敛 $\iff$ 弱收敛 + 范数收敛 | 郭版教材 §4.2.2 定理 4.2.4 | 原文迁移 |
| 弱收敛的稠集判据 | 郭版教材 §4.2.2 定理 4.2.5 | 原文迁移 |
| 弱收敛推不出强收敛（反例 3） | 本节推演 | 新写（由 Bessel 不等式构造） |
| 正交、正交系、标准正交系、Kronecker 记号 | 郭版教材 §4.2.2 定义 4.2.6 | 原文迁移 |
| 标准正交系必可数 | 郭版教材 §4.2.2 定理 4.2.7 | 原文迁移 |
| 三角函数系是标准正交系 | 郭版教材 §4.2.2 (4.2.7)、例 1 | 原文迁移 + 补正交性来源说明 |
| Fourier 系数、Fourier 级数 | 郭版教材 §4.2.2 定义 4.2.8 | 原文迁移 |
| Bessel 不等式 | 郭版教材 §4.2.2 定理 4.2.9；旧《Ch9》§3.3 | 合并 |
| Riesz–Fischer 定理（系数列版本） | 郭版教材 §4.2.2 定理 4.2.10 | 原文迁移 + 补与 §4.1.3 同名定理的区分说明 |
| 最佳逼近定理 | 郭版教材 §4.2.2 定理 4.2.11 | 原文迁移 |
| 完全系、标准正交基 | 郭版教材 §4.2.2 定义 4.2.12、4.2.13 | 原文迁移 |
| 五条等价（标准正交基 $\iff$ 稠密 $\iff$ 完全 $\iff$ Parseval $\iff$ 内积等式） | 郭版教材 §4.2.2 定理 4.2.14 | 原文迁移（证明脉络完整保留） |
| 正交系不完全时 Bessel 取严格不等（反例 4） | 本节推演 | 新写 |
| 三角函数系是标准正交基、Fourier 展开式 | 郭版教材 §4.2.2 例 1 | 原文迁移 |
| $\|f\|=\big(\sum|c_k|^2\big)^{1/2}$、$(f,g)=\sum c_kd_k$ | 郭版教材 §4.2.2 (4.2.18)(4.2.19) | 原文迁移 |
| $\sum 1/n^2=\pi^2/6$ 例题 | 本节推演 | 新写（Parseval 等式的应用） |
| $L^2$ 是 Hilbert 空间、$l^2$ 是 Hilbert 空间 | 旧《Ch9》§1.4 例 1、例 2 | 迁入「去脉」，一般理论归 Ch5 |
| $l^p(p\ne 2)$、$C[a,b]$ 不是内积空间（平行四边形反例） | 旧《Ch9》§1.4 例 3、例 4 | 迁入 §4.2.1「平行四边形公式」处作为判别法的说明，完整推演归 Ch5 §5.2 |