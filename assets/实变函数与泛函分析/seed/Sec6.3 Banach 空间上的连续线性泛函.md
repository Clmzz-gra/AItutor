---
type: 节
formal: true
subject: 实变函数与泛函分析
created: 2026-09-21
updated: 2026-09-21
tags: [math, 实变函数与泛函分析]
chapter: 6
section: 6.3
---

# Sec6.3 Banach 空间上的连续线性泛函

> 定位：没有内积，怎么"表示"泛函——Hahn–Banach 定理保证泛函够多，共轭空间把抽象泛函变成具体对象。
> 教材：郭懋正《实变函数与泛函分析》§6.3（p.301–312）
> 来源：旧讲解包《Ch10 巴拿赫空间中的基本定理》§10.1–§10.3；旧《Ch8 有界线性算子和连续线性泛函》§8.1（泛函部分）、§8.2；郭版教材 §6.3

> [!info] 关联笔记
> - 父级：[[Ch6 Banach 空间]]
> - 前置：[[Sec6.2 Banach 空间上的有界线性算子]] ｜ 后续：[[Sec6.4 Banach 空间的收敛性和紧致性]]
> - 概念：[[概念-对偶空间]]

---

## 来龙（为什么需要它）

- **类比已知**：Ch5 的 Hilbert 空间里，每个连续线性泛函都能用 **Riesz 表示定理**写成内积 $f(x)=\langle x,y\rangle$——"泛函"和"向量"是同一批东西，所以泛函当然够多。
- **解决新问题**：Banach 空间里没有内积，泛函长什么样完全没有先验信息。于是先要问一个更基本的问题：**一个非零的赋范空间上，到底存不存在非零的连续线性泛函？** 如果答案是否定的，那么"用泛函分离点""用对偶刻画收敛"这些手法全部失效，整个泛函分析会塌掉一半。
- **理论/应用需要**：① 分离点：要证明 $x\neq y$，只需找一个泛函把它们分开；② 弱收敛的定义本身就要用到"所有 $f\in X^*$"（§6.4）；③ 变分法与凸分析里的分离定理（用超平面把一个点和一个凸集分开）是 Hahn–Banach 的几何形式；④ 偏微分方程的弱解、分布理论都建立在"对偶空间足够大"这一事实上。

**一句话概括本节**：**Hahn–Banach 保证泛函够多（存在性），共轭空间给出泛函的具体形状（表示），共轭算子把算子的对偶版本造出来（结构）。**

## 主体（核心内容）

### 6.3.1 连续线性泛函的存在性：Hahn–Banach 定理

**定义（次线性泛函）**：$X$ 是实线性空间，$p:X\to\mathbb{R}$ 若满足

1. **正齐次性**：$p(\lambda x)=\lambda p(x)$，$\forall\lambda>0$；
2. **次可加性**：$p(x+y)\leqslant p(x)+p(y)$，

则称 $p$ 是 $X$ 上的**次线性泛函**（读作"次线性"，即"比线性小一点"）。例：赋范空间中 $p(x)=c\|x\|$（$c>0$）是次线性泛函。它扮演的角色是**控制延拓泛函的"上界函数"**。

**引理（Zorn 引理，附录 A，只记结论）**：若偏序集中每个全序子集都有上界，则该偏序集有极大元。

**作用**：Hahn–Banach 中"一维一维地延拓"可能要做不可数多次，普通归纳法失效；*因为* Zorn 引理一次处理完所有链，所以延拓一次完成。

**定理 6.3.1（Hahn–Banach 定理，实空间版本）**：设 $X$ 是实线性赋范空间，$X_0$ 是 $X$ 的线性子空间。若 $f_0$ 是定义在 $X_0$ 上的实的有界线性泛函，则 $f_0$ 可以延拓到整个 $X$ 上且**保持范数不变**：存在 $X$ 上的有界线性实泛函 $f$ 满足

$$(1)\ f(x)=f_0(x),\ \forall x\in X_0\ (\text{延拓条件});\qquad (2)\ \|f\|=\|f_0\|_0\ (\text{保范条件}),$$

其中 $\|f_0\|_0$ 表示 $f_0$ 在 $X_0$ 上的范数。

*证明分两步（推导全程）*：

**第 1 步：一维延拓。** 任取 $y_0\in X\setminus X_0$，记 $X_1=\{x+\alpha y_0:x\in X_0,\ \alpha\in\mathbb{R}\}$。$X_1$ 中元素唯一写成 $x+\alpha y_0$。要让延拓 $f_1$ 满足

$$f_1(x+\alpha y_0)=f_0(x)+\alpha f_1(y_0),\qquad\forall x\in X_0,\ \alpha\in\mathbb{R}, \tag{6.3.1}$$

**可见只要确定 $f_1(y_0)$ 这一个数**。由保范条件，对一切 $x\in X_0$、$\alpha\in\mathbb{R}$，

$$|f_1(x+\alpha y_0)|\leqslant\|f_1\|\,\|x+\alpha y_0\|=\|f_0\|_0\|x+\alpha y_0\| . \tag{6.3.2}$$

取 $\alpha=1$、$\forall y\in X_0$，得 $-\|f_0\|_0\|y_0+y\|\leqslant f_1(y_0+y)\leqslant\|f_0\|_0\|y+y_0\|$；取 $\alpha=-1$、$\forall z\in X_0$，得 $-\|f_0\|_0\|y_0-z\|\leqslant f_1(-y_0+z)\leqslant\|f_0\|_0\|y_0-z\|$。*因为* $f_1$ 在 $X_0$ 上与 $f_0$ 一致且线性，这两组不等式等价于

$$f_0(z)-\|f_0\|_0\|y_0-z\|\leqslant f_1(y_0)\leqslant-f_0(y)+\|f_0\|_0\|y_0+y\|,\qquad\forall y,z\in X_0 . \tag{6.3.5}$$

于是**能取到适合 (6.3.5) 的 $f_1(y_0)$ 必须且仅须**

$$\sup_{z\in X_0}\big\{f_0(z)-\|f_0\|_0\|y_0-z\|\big\}\leqslant\inf_{y\in X_0}\big\{-f_0(y)+\|f_0\|_0\|y_0+y\|\big\} . \tag{6.3.6}$$

*而这个不等式一定成立*：因为对 $\forall y,z\in X_0$，

$$f_0(y)+f_0(z)=f_0(y+z)\leqslant\|f_0\|_0\|y+z\|\leqslant\|f_0\|_0\|y+y_0\|+\|f_0\|_0\|y_0-z\|,$$

（第一个不等号用 $f_0$ 被 $\|f_0\|_0\|\cdot\|$ 控制；第二个用三角不等式 $y+z=(y+y_0)+(z-y_0)$）。整理即得 (6.3.7)，它蕴含 (6.3.6)。

**取 (6.3.6) 两端的任意中间值作为 $f_1(y_0)$**，由 (6.3.1) 就定义了 $X_1$ 上的线性泛函 $f_1$，它是 $f_0$ 的延拓。再证保范：$\|f_1\|\geqslant\|f_0\|_0$ 显然；反向当 $\alpha>0$ 时由 (6.3.3) 与 $x/\alpha\in X_0$ 得

$$|f_1(x+\alpha y_0)|=\alpha\Big|f_1\Big(\frac x\alpha+y_0\Big)\Big|\leqslant\alpha\|f_0\|_0\Big\|\frac x\alpha+y_0\Big\|=\|f_0\|_0\|x+\alpha y_0\|,$$

$\alpha<0$ 时同理。故 $\|f_1\|=\|f_0\|_0$。一维延拓完成。

**第 2 步：全空间延拓（Zorn 引理）。** 令

$$\mathcal{F}=\big\{(X_\triangle,f)\ \big|\ X_\triangle\ \text{是实线性子空间},\ X_0\subset X_\triangle\subset X,\ \|f\|_{X_\triangle}=\|f_0\|_0,\ f|_{X_0}=f_0\big\}, \tag{6.3.8}$$

在 $\mathcal{F}$ 中规定序：$(X_1,f_1)\prec(X_2,f_2)$ 指 $X_1\subset X_2$ 且 $f_2|_{X_1}=f_1$。任取全序子集 $S$，令 $X_S=\bigcup\{X_\triangle:(X_\triangle,f)\in S\}$，并当 $x\in X_\triangle$、$(X_\triangle,f)\in S$ 时令 $f_S(x)=f(x)$。*因为* $S$ 全序，各定义域相互包含，$f_S$ 在 $X_S$ 上**唯一确定**且满足 $\|f_S\|=\|f_0\|_0$，故 $(X_S,f_S)\in\mathcal{F}$ 且是 $S$ 的上界。由 Zorn 引理，$\mathcal{F}$ 有极大元 $(X_\wedge,f_\wedge)$。

兹证 $X_\wedge=X$：倘若不然，由第 1 步可构造 $(\widetilde{X_\wedge},\widetilde{f_\wedge})\in\mathcal{F}$ 使 $X_\wedge\subsetneqq\widetilde{X_\wedge}$，与极大性矛盾。故所求泛函即 $f=f_\wedge$。$\square$

**定理 6.3.2（Hahn–Banach 定理，复空间版本）**：设 $X$ 是复线性赋范空间，$X_0$ 是线性子空间，$f_0$ 是 $X_0$ 上的有界线性泛函，则 $f_0$ 可保范延拓到整个 $X$。

*证明（关键构造）*：把 $X$ 看成实线性空间、$X_0$ 看成实线性子空间，令 $g_0(x)=\operatorname{Re}f_0(x)$。*因为* $|\operatorname{Re}f_0(x)|\leqslant|f_0(x)|$，有 $\|g_0\|_0\leqslant\|f_0\|_0$；又 *因为* $f_0$ 复线性，$f_0(\mathrm{i}x)=\mathrm{i}f_0(x)$，比较虚部得 $g_0(\mathrm{i}x)=\operatorname{Re}f_0(\mathrm{i}x)=-\operatorname{Im}f_0(x)$。由定理 6.3.1，存在 $X$ 上的**实**线性泛函 $g$ 使

$$g(x)=g_0(x)\ (\forall x\in X_0),\qquad \|g\|=\|\operatorname{Re}f_0\|_0 . \tag{6.3.9},\ (6.3.10)$$

现在令

$$f(x)=g(x)-\mathrm{i}g(\mathrm{i}x),\qquad\forall x\in X .$$

- **是延拓**：*因为* $g_0(\mathrm{i}x)=-\operatorname{Im}f_0(x)$，对 $x\in X_0$ 有 $f(x)=g_0(x)-\mathrm{i}g_0(\mathrm{i}x)=\operatorname{Re}f_0(x)+\mathrm{i}\operatorname{Im}f_0(x)=f_0(x)$。
- **复齐次**：$f(\mathrm{i}x)=g(\mathrm{i}x)-\mathrm{i}g(-x)=\mathrm{i}\big(g(x)-\mathrm{i}g(\mathrm{i}x)\big)=\mathrm{i}f(x)$，*因为* $g$ 是实线性的；结合实线性即得复线性。
- **保范（旋转技巧）**：$\|f\|\geqslant\|f_0\|_0$ 显然。反向当 $f(x)\neq0$ 时记 $\theta=\arg f(x)$，*因为* $f(\mathrm{e}^{-\mathrm{i}\theta}x)$ 是正数 $|f(x)|$、虚部为零，

$$|f(x)|=\mathrm{e}^{-\mathrm{i}\theta}f(x)=f(\mathrm{e}^{-\mathrm{i}\theta}x)=g(\mathrm{e}^{-\mathrm{i}\theta}x)\leqslant\|g\|\,\|\mathrm{e}^{-\mathrm{i}\theta}x\|\leqslant\|f_0\|_0\|x\| . \qquad\square$$

**推论 6.3.3（分离点的泛函）**：设 $X$ 是线性赋范空间，对任意非零 $x_0\in X$，必存在 $f\in X^*$ 满足

$$\|f\|=1,\qquad f(x_0)=\|x_0\| . \tag{6.3.11}$$

*证明*：在一维子空间 $X_0=\{\lambda x_0:\lambda\in\mathbb{K}\}$ 上定义 $f_0(\lambda x_0)=\lambda\|x_0\|$，则 $f_0(x_0)=\|x_0\|$ 且 $\|f_0\|_0=1$；由定理 6.3.2 保范延拓即得。$\square$

**推论 6.3.4**：线性赋范空间 $X$ 上有**足够多**的连续线性泛函。

*证明*：设 $x_1\neq x_2$，记 $x_0=x_1-x_2\neq0$。由推论 6.3.3 存在 $\|f\|=1$ 且 $f(x_0)=\|x_0\|\neq0$，故 $f(x_1)\neq f(x_2)$——**$f$ 能分辨任意两个不同的点**。$\square$

**推论 6.3.5（范数的对偶表示）**：对 $x\in X$，

$$\|x\|=\sup\big\{|f(x)|:f\in X^*,\ \|f\|\leqslant1\big\}, \tag{6.3.12}$$

**且上确界能达到**。

*证明*：记 $\alpha$ 为右端。*因为* $|f(x)|\leqslant\|f\|\|x\|\leqslant\|x\|$，有 $\alpha\leqslant\|x\|$；由推论 6.3.3 存在 $\|f\|=1$、$f(x)=\|x\|$，故 $\|x\|\leqslant\alpha$。故 $\|x\|=\alpha=f(x)$（$x\neq0$ 时）。$\square$

> **读法**：**范数可以完全由对偶空间"测"出来**——这正是"$X^*$ 足够大"的定量版本，也是后面"自然嵌入 $X\hookrightarrow X^{**}$ 是等距的"的依据。

**推论 6.3.6**：设 $x_0\in X$，则 $x_0=0$ $\iff$ 对一切 $f\in X^*$ 有 $f(x_0)=0$。

*证明*：$\Rightarrow$ 显然；$\Leftarrow$ 若 $x_0\neq0$，由推论 6.3.3 存在 $f$ 使 $f(x_0)=\|x_0\|\neq0$，矛盾。$\square$

**定理 6.3.7（分离定理：点与闭子空间）**：设 $X$ 是线性赋范空间，$M$ 是 $X$ 的线性子空间，$x_0\notin M$ 且

$$d\stackrel{\text{def}}{=}\rho(x_0,M)>0, \tag{6.3.13}$$

则存在 $f\in X^*$ 满足 (1) $f(x)=0,\ \forall x\in M$；(2) $f(x_0)=d$；(3) $\|f\|=1$。

*证明*：考虑 $X_0=\{x=y+\lambda x_0:y\in M,\ \lambda\in\mathbb{K}\}$（它是 $X$ 的子空间，*因为* $x_0\notin M$ 故 $y+\lambda x_0=0$ 只在 $y=0,\lambda=0$ 时成立，表示唯一）。在 $X_0$ 上定义

$$f_0(y+\lambda x_0)=\lambda d . \tag{6.3.14}$$

显然 $f_0$ 满足条件 (1)(2)。又当 $\lambda\neq0$ 时，*因为* $-\tfrac1\lambda y\in M$ 而 $d$ 是 $x_0$ 到 $M$ 的距离，

$$|f_0(y+\lambda x_0)|=|\lambda|d=|\lambda|\,\rho(x_0,M)\leqslant|\lambda|\Big\|\frac1\lambda y+x_0\Big\|=\|y+\lambda x_0\|,$$

故 $\|f_0\|\leqslant1$；$\lambda=0$ 时两边都是 $0$。由 Hahn–Banach 定理（定理 6.3.2）把 $f_0$ 保范延拓为 $f\in X^*$，则 $f$ 满足 (1)(2) 且 $\|f\|\leqslant1$。

兹证 $\|f\|\geqslant1$：按**下确界**的定义，存在 $x_n\in M$ 使 $d\leqslant\rho(x_0,x_n)\leqslant d+1/n$。*因为* $f(x_n)=0$，

$$|f(x_0)|=|f(x_0-x_n)|\leqslant\|f\|\,\|x_n-x_0\|\leqslant\|f\|\Big(d+\frac1n\Big),$$

而 $f(x_0)=d$，令 $n\to\infty$ 得 $d\leqslant\|f\|d$，即 $\|f\|\geqslant1$。故 $\|f\|=1$。$\square$

**定理 6.3.7 的一个直接推论**：若 $S$ 是 $X$ 的子集、$x_0\neq0$，则

$$x_0\in\overline{\operatorname{linspace}S}\iff \forall f\in X^*,\ \big(S\subset\ker f\ \Rightarrow\ x_0\in\ker f\big).$$

即：**一个点落在 $S$ 张成的闭线性包中，当且仅当所有"在 $S$ 上为零"的连续泛函也在该点为零**——这是"闭线性包"的对偶刻画。

**边界情况（延拓一般不唯一）**：定理 6.3.1 证明中，(6.3.6) 两端**未必相等**，其中间值 $f_1(y_0)$ 的取法一般不唯一，因此**保范延拓一般也不唯一**。具体例子：

- 取 $X=\mathbb{R}^2$ 配范数 $\|(a,b)\|_1=|a|+|b|$，$X_0=\{(t,0):t\in\mathbb{R}\}$，$f_0(t,0)=t$，则 $\|f_0\|_0=1$；
- $X$ 上形如 $f(a,b)=a+cb$ 的泛函都是 $f_0$ 的延拓，而

$$\|f\|=\sup_{|a|+|b|=1}|a+cb|=\max(1,|c|);$$

- *因为* 保范要求 $\|f\|=1$，只需 $|c|\leqslant1$——**$c\in[-1,1]$ 中每个值都给出一个合法的保范延拓，共不可数多个**。

**所以 Hahn–Banach 是存在性定理，不是唯一性定理**：它保证"至少有一个"，不保证"只有一个"。（对比：闭图像定理、逆算子定理给出的对象是唯一的。）

**例题（距离的对偶公式，教材习题 7）**：设 $X$ 是线性赋范空间，$X_0$ 是 $X$ 的**闭**子空间。证明

$$\rho(x,X_0)=\sup\big\{|f(x)|:f\in X^*,\ \|f\|=1,\ f|_{X_0}=0\big\}.$$

*原始信息*：左边是几何量（点到子集的距离），右边是对偶量（一族泛函在 $x$ 上的取值）。要证两个方向的夹逼。

*第一步，右边 $\leqslant$ 左边*：任取满足条件的 $f$ 与任意 $y\in X_0$，*因为* $f(y)=0$ 且 $\|f\|=1$，

$$|f(x)|=|f(x-y)|\leqslant\|f\|\,\|x-y\|=\|x-y\| .$$

对 $y\in X_0$ 取下确界得 $|f(x)|\leqslant\rho(x,X_0)$；再对 $f$ 取上确界即得。

*第二步，左边 $\leqslant$ 右边*：若 $\rho(x,X_0)=0$，*因为* $X_0$ 闭得 $x\in X_0$，于是对一切这样的 $f$ 有 $f(x)=0$，右边为 $0$，等式成立。若 $d=\rho(x,X_0)>0$，由**定理 6.3.7**（注意 $x\notin X_0$）存在 $f\in X^*$ 使 $\|f\|=1$、$f|_{X_0}=0$、$f(x)=d$，故右边 $\geqslant d$。

*结果*：两个方向夹住，等式成立。*结论*：**"到子空间的距离"完全可以用对偶空间的泛函来测**——这是 Hahn–Banach 最常用的定量形式，也是 §6.4 证明弱收敛性质的必备工具。

### 6.3.2 共轭空间以及它的表示

**定义 6.3.8（共轭空间）**：设 $X$ 是线性赋范空间，$X$ 上所有连续线性泛函全体在范数

$$\|f\|=\sup\big\{|f(x)|:x\in X,\ \|x\|=1\big\} \tag{6.3.15}$$

下构成一个 Banach 空间，称为 $X$ 的**共轭空间**，记作 $X^*$（读作"$X$ 星"或"$X$ 的共轭空间/对偶空间"）。

*为什么 $X^*$ 一定是 Banach 空间*：*因为* $X^*=\mathcal{B}(X,\mathbb{K})$，而数域 $\mathbb{K}$ 完备，由 §6.1.3 定理 6.1.12 即得。**这一点非常关键**：即使 $X$ 本身不完备，$X^*$ 也完备——§6.4 的所有弱收敛论证都建立在"$X^*$ 是 Banach 空间"之上。

**同构的约定**：保持范数的线性双射（$\|Tx\|=\|x\|$ 且到上）称为**同构映射**；同构的两个空间在泛函分析中**视为同一个空间**（写作 $\cong$）。

**例 1：$(l^1)^*=l^\infty$**

**结论**：$l^1$ 上每个连续线性泛函都可唯一写成

$$f(x)=\sum_{k=1}^\infty\xi_k\eta_k,\qquad x=(\xi_1,\xi_2,\dots)\in l^1,\quad(\eta_1,\eta_2,\dots)\in l^\infty,$$

且 $\|f\|=\sup_k|\eta_k|$，故 $(l^1)^*$ 与 $l^\infty$ 保范同构。

*证明两条线*：
- **给定 $f\in(l^1)^*$**：令 $\eta_k=f(e_k)$（$e_k$ 是第 $k$ 个坐标为 $1$、其余为 $0$ 的向量）。*因为* $x=\lim_n\sum_{k=1}^n\xi_ke_k$ 在 $l^1$ 范数下成立，由 $f$ 连续得 $f(x)=\sum_{k=1}^\infty\xi_k\eta_k$。又 $|\eta_k|=|f(e_k)|\leqslant\|f\|\,\|e_k\|_1=\|f\|$，故 $\sup_k|\eta_k|\leqslant\|f\|$，即 $(\eta_k)\in l^\infty$。
- **给定 $b=(\beta_k)\in l^\infty$**：定义 $g(x)=\sum_k\xi_k\beta_k$。由 Hölder 不等式的级数形式（$p=1,q=\infty$），$|g(x)|\leqslant\sup_k|\beta_k|\cdot\|x\|_1$，故 $g\in(l^1)^*$ 且 $\|g\|\leqslant\sup_k|\beta_k|$。

两边合起来：映射 $f\mapsto(f(e_1),f(e_2),\dots)$ 是 $(l^1)^*$ 到 $l^\infty$ 的保范同构。$\square$

**例 2：$(l^p)^*=l^q$（$1<p<\infty$，$\frac1p+\frac1q=1$）**

**结论**：$l^p$ 上连续线性泛函的一般形式是

$$f(x)=\sum_{k=1}^\infty\xi_k\eta_k,\qquad(\eta_k)\in l^q,\qquad\|f\|=\Big(\sum_k|\eta_k|^q\Big)^{1/q}.$$

*证明难点在 $\|(\eta_k)\|_q\leqslant\|f\|$*：设 $\eta_k=f(e_k)$。若 $f\neq0$，对每个 $n$ 构造**试探元**

$$\xi_k^{(n)}=\begin{cases}|\eta_k|^q/\eta_k,&k\leqslant n,\ \eta_k\neq0,\\[2pt] 0,&\text{其余}.\end{cases}$$

（这是把 $\eta_k$ "旋转到正实轴"的标准构造。）*因为* $|\xi_k^{(n)}|^p=|\eta_k|^{(q-1)p}=|\eta_k|^q$，故 $\|x_n\|_p=\big(\sum_{k=1}^n|\eta_k|^q\big)^{1/p}$；同时 $f(x_n)=\sum_{k=1}^n|\eta_k|^q$。由 $|f(x_n)|\leqslant\|f\|\,\|x_n\|_p$，两边除以 $\|x_n\|_p$ 得

$$\Big(\sum_{k=1}^n|\eta_k|^q\Big)^{1/q}\leqslant\|f\|,$$

令 $n\to\infty$ 即得。反向 $\|f\|\leqslant\|(\eta_k)\|_q$ 由 Hölder 直接给出。$\square$

> **核心事实**：共轭空间是"泛函的仓库"。$(l^1)^*=l^\infty$、$(l^p)^*=l^q$ 说明：**共轭空间的形状和原空间的范数强相关**——同样的集合换范数，共轭空间会变。这是无穷维分析比线性代数复杂的一个来源。

**例 3：$(L^p[0,1])^*=L^q[0,1]$（$1\leqslant p<\infty$）**

设 $q$ 是 $p$ 的**共轭数**：$p>1$ 时 $\frac1p+\frac1q=1$，$p=1$ 时 $q=\infty$。对 $g\in L^q[0,1]$ 令

$$F_g(f)=\int_0^1f(x)g(x)\,\mathrm{d}x,\qquad\forall f\in L^p[0,1] . \tag{6.3.17}$$

由 Hölder 不等式（$p>1$）或本性上确界估计（$p=1$），$|F_g(f)|\leqslant\|f\|_p\|g\|_q$，故 $F_g\in(L^p[0,1])^*$ 且 $\|F_g\|\leqslant\|g\|_q$。*因为* Ch4 的等距性结论（教材 (4.1.11)、(4.1.12) 式）保证 $g\mapsto F_g$ 是**等距**的，上式为等式。进一步可证 $g\mapsto F_g$ 是**满**的：对给定的 $F\in(L^p[0,1])^*$，存在唯一的 $g\in L^q[0,1]$ 使 $F(f)=\int_0^1fg$ 且 $\|g\|_q=\|F\|$（证明见张恭庆、林源渠《泛函分析讲义》上册 p.128）。于是

$$L^p[0,1]^*\cong L^q[0,1] . \tag{6.3.19}$$

更一般地，当 $(X,\Omega,\mu)$ 是 $\sigma$ 有限测度空间时，

$$L^p(X,\Omega,\mu)^*\cong L^q(X,\Omega,\mu),\qquad 1\leqslant p<\infty . \tag{6.3.20}$$

**例 4：$(c_0)^*=l^1$（教材习题 15(2)）**：$c_0$ = 极限为零的实数列全体（配 $\sup$ 范数，是 $l^\infty$ 的闭子空间，因而本身是 Banach 空间），则 $(c_0)^*$ 与 $l^1$ 等距同构。**注意方向**：$(c_0)^*=l^1$，而 $(l^1)^*=l^\infty$——**对偶把"小空间"换成了"大空间"**。

**例 5：$(C[0,1])^*$ = 有界变差函数空间 $BV[0,1]$**

**预备（Ch3 的工具）**：$g$ 是 $[a,b]$ 上的**有界变差函数**，总变差记 $\bigvee_a^b(g)$（读作"$g$ 从 $a$ 到 $b$ 的**全变差**"）；对 $f\in C[a,b]$，Riemann–Stieltjes 积分 $\int_a^bf(t)\,\mathrm{d}g(t)$ 存在。

**定理（Riesz 表示定理，$C[0,1]$ 版）**：$C[0,1]$ 上每个连续线性泛函 $F$ 都可写成

$$F(f)=\int_a^bf(t)\,\mathrm{d}g(t),\qquad\|F\|=\bigvee_a^b(g),$$

其中 $g$ 有界变差。若再要求 $g(a)=0$ 且 $g$ 右连续，则 $g$ 唯一。

*证明骨架（Hahn–Banach 的应用范例，五步）*：

1. **延拓**：*因为* $C[a,b]$ 是有界函数空间 $B[a,b]$（$\sup$ 范数）的子空间，由 Hahn–Banach 把 $F$ 保范延拓为 $\widetilde F\in B[a,b]^*$。
2. **造 $g$**：令 $\chi_t=\mathbf{1}_{[a,t]}$（特征函数，属于 $B[a,b]$ 但不连续），定义 $g(a)=0$、$g(t)=\widetilde F(\chi_t)$。
3. **证 $g$ 有界变差**：对任意分划 $T$，取 $\varepsilon_j=\operatorname{sign}\big(\widetilde F(\chi_{t_j})-\widetilde F(\chi_{t_{j-1}})\big)$，*因为* 括号内的阶梯函数属于 $B[a,b]$ 且范数 $\leqslant1$，

$$\sum_j|g(t_j)-g(t_{j-1})|=\widetilde F\Big(\varepsilon_1\chi_{t_1}+\sum_{j\geqslant2}\varepsilon_j(\chi_{t_j}-\chi_{t_{j-1}})\Big)\leqslant\|\widetilde F\|=\|F\|,$$

故 $\bigvee_a^b(g)\leqslant\|F\|$。
4. **证表示**：对连续 $f$ 作阶梯函数逼近 $h_n$，*因为* $\widetilde F(h_n)$ 是 Stieltjes 和，它趋于 $\int_a^bf\,\mathrm{d}g$；同时 $h_n\to f$（一致），由 $\widetilde F$ 连续得 $\widetilde F(h_n)\to F(f)$。于是 $F(f)=\int_a^bf\,\mathrm{d}g$。
5. **范数**：$|F(f)|\leqslant\|f\|_\infty\bigvee_a^b(g)$ 给出 $\|F\|\leqslant\bigvee_a^b(g)$，与第 3 步反向夹住，得 $\|F\|=\bigvee_a^b(g)$。$\square$

**更一般的形式（教材定理 6.3.9，Riesz 表示定理）**：设 $M$ 是 Hausdorff 紧空间，则对 $C(M)^*$ 中任何元素 $f$，存在**唯一**的复值 Baire 测度与之对应：即存在 $M$ 上完全可加的集函数 $\mu$，$|\mu|<\infty$，满足

$$\langle f,\phi\rangle=\int_M\phi(m)\,\mathrm{d}\mu(m),\quad\forall\phi\in C(M);\qquad \|f\|=|\mu|, \tag{6.3.25},\ (6.3.26)$$

其中 $|\mu|=\sup\big|\sum_{i=1}^n\alpha_i\mu(M_i)\big|$，上确界对所有有限分割 $M=\bigcup_{i=1}^nM_i$（$\{M_i\}$ 互不相交的 Borel 可测子集）与所有 $|\alpha_i|\leqslant1$ 的 $\alpha_i\in\mathbb{K}$ 来取。读法：$|\mu|$ 读作"测度 $\mu$ 的**全变差**"。

> **这是本学科最漂亮的一处呼应**：Ch2 造的 Lebesgue 测度在这里以"泛函"的身份回来了。**$(C[a,b])^*$ 的元素不是别的，正是测度**——连续函数空间的对偶空间，就是测度空间。

**第二共轭空间与自然映射**：定义 $X^{**}=(X^*)^*$ 为 $X$ 的**第二共轭空间**（读作"$X$ 双星"）。当 $f\in X^*$ 时也记 $f(x)=\langle f,x\rangle$，以突出 $f$ 与 $x$ 的对称地位。对每个 $x\in X$ 定义

$$F_x(f)=\langle f,x\rangle,\qquad\forall f\in X^*, \tag{6.3.27}$$

则 $F_x$ 是 $X^*$ 上的线性泛函；由推论 6.3.5，

$$\|F_x\|=\sup\{|\langle f,x\rangle|:f\in X^*,\|f\|\leqslant1\}=\|x\| . \tag{6.3.28}$$

称映射 $\tau:x\mapsto F_x$ 为**自然映射**；(6.3.28) 表明 $\tau$ 是 $X$ 到 $X^{**}$ 的**连续等距嵌入**。

**定理 6.3.11**：线性赋范空间 $X$ 与它的第二共轭空间 $X^{**}$ 的一个子空间等距同构。今后对 $x$ 与 $F_x$ 不加区别，简单写成 $X\subset X^{**}$。

**定义 6.3.12（自反空间）**：如果 $X$ 到 $X^{**}$ 的自然映射 $\tau$ 是**满射**的，则称 $X$ 是**自反空间**，记作 $X=X^{**}$。显然自反空间必是 Banach 空间，反之则不然（完整讨论见 Sec6.4）。

**反例（对偶表示不是总能"降回原空间"）**：教材明确指出，$1<p<\infty$ 时 $L^p(X,\Omega,\mu)$ 是自反的，但 $p=1$ 或 $\infty$ 时**不是**：$L^1$ 的共轭空间是 $L^\infty$，而 **$L^\infty$ 的共轭空间比 $L^1$ 大得多**。数列版是教材习题 10：$l^\infty=(l^1)^*$，但 $(l^\infty)^*\neq l^1$。*因为* 对偶运算把 $l^1$ 送到 $l^\infty$ 之后"回不来"，所以 $l^1$ 与 $l^\infty$ 都不自反。**"取对偶"是一个不对称的操作**——这正是自反性值得单独讨论的原因。

**例题（$l^p$ 泛函范数的完整计算）**：设 $1<p<\infty$、$\frac1p+\frac1q=1$，$(\eta_k)\in l^q$，在 $l^p$ 上定义 $f(x)=\sum_k\xi_k\eta_k$。求 $\|f\|$。

*原始信息*：要算 $\sup_{\|x\|_p=1}|f(x)|$，直接对一般 $x$ 估计只能得到上界。

*上界方向*：由 Hölder 不等式 $|f(x)|\leqslant\|x\|_p\|(\eta_k)\|_q$，故 $\|f\|\leqslant\|(\eta_k)\|_q$。

*下界方向（构造试探元）*：设 $(\eta_k)\neq0$。对每个 $n$ 令 $\xi_k^{(n)}=|\eta_k|^q/\eta_k$（$k\leqslant n$，$\eta_k\neq0$）、其余取 $0$。*因为* $q-1=q/p$，有 $|\xi_k^{(n)}|^p=|\eta_k|^{(q-1)p}=|\eta_k|^q$，故

$$\|x_n\|_p=\Big(\sum_{k=1}^n|\eta_k|^q\Big)^{1/p},\qquad f(x_n)=\sum_{k=1}^n|\eta_k|^q .$$

*代入* $|f(x_n)|\leqslant\|f\|\,\|x_n\|_p$，两边除以 $\|x_n\|_p=\big(\sum_{k\leqslant n}|\eta_k|^q\big)^{1/p}$ 得

$$\Big(\sum_{k=1}^n|\eta_k|^q\Big)^{1-1/p}=\Big(\sum_{k=1}^n|\eta_k|^q\Big)^{1/q}\leqslant\|f\| .$$

*结果*：令 $n\to\infty$ 得 $\|(\eta_k)\|_q\leqslant\|f\|$。*结论*：$\|f\|=\big(\sum_k|\eta_k|^q\big)^{1/q}$，即 $(l^p)^*=l^q$ 是**保范**的。

### 6.3.3 共轭算子

**动机（有穷维的提示）**：$n\times m$ 矩阵 $A=(a_{ij})$ 可看作 $\mathbb{K}^m\to\mathbb{K}^n$ 的线性算子，它的共轭转置矩阵 $A^*=(\overline{a_{ji}})$ 是 $\mathbb{K}^n\to\mathbb{K}^m$ 的线性算子，二者满足

$$(Ax,y)_{\mathbb{K}^n}=(x,A^*y)_{\mathbb{K}^m},\qquad\forall y\in\mathbb{K}^n,\ x\in\mathbb{K}^m .$$

共轭算子就是把这条关系搬到无穷维。

**定义 6.3.13（共轭算子）**：设 $X,Y$ 是线性赋范空间，$T\in\mathcal{B}(X,Y)$。线性算子 $T^*:Y^*\to X^*$ 称为 $T$ 的**共轭算子**，是指

$$T^*f(x)=f(Tx),\qquad\forall f\in Y^*,\ x\in X . \tag{6.3.29}$$

读法：$T^*$ 读作"$T$ 的共轭算子"；**注意方向是从 $Y^*$ 到 $X^*$，与原算子 $X\to Y$ 相反**。

**存在性与有界性**：对每个 $f\in Y^*$ 令 $g(x)=f(Tx)$，则 *因为* $f,T$ 都线性连续，$g\in X^*$ 且

$$\|g\|\leqslant\|f\|\,\|T\|,\qquad\text{即}\quad\|T^*f\|\leqslant\|T\|\,\|f\| .$$

*因为* $f\mapsto g$ 线性，它就是 $T^*$，于是 $T^*\in\mathcal{B}(Y^*,X^*)$ 且 $\|T^*\|\leqslant\|T\|$。**对每个 $T\in\mathcal{B}(X,Y)$，$T^*$ 是唯一存在的。**

**定理 6.3.14（共轭映射是等距同构）**：映射 $*:T\mapsto T^*$ 是 $\mathcal{B}(X,Y)$ 到 $\mathcal{B}(Y^*,X^*)$ 的**等距同构**。

*证明*：映射 $*$ 显然线性。*因为* $X^*$ 与 $Y^*$ 上的范数由推论 6.3.5 给出，可以交换两重上确界：

$$\begin{aligned}\|T\|&=\sup\{\|Tx\|:\|x\|\leqslant1\}=\sup_{\|x\|\leqslant1}\sup_{\|f\|\leqslant1}|f(Tx)|\\&=\sup_{\|f\|\leqslant1}\sup_{\|x\|\leqslant1}|(T^*f)(x)|=\sup_{\|f\|\leqslant1}\|T^*f\|=\|T^*\| .\end{aligned}$$

（第一个等号用算子范数的定义；第二个等号把"范数"换成"对偶表示"；第三个等号用 $T^*$ 的定义；第四个等号再把对偶表示换回范数。）$\square$

> **这一步用到了什么**：**推论 6.3.5**。*因为* $\|y\|=\sup_{\|f\|\leqslant1}|f(y)|$ 且上确界可达，才能把 $\|Tx\|$ 换成 $|f(Tx)|$ 而不损失信息。**没有 Hahn–Banach，就没有 $\|T^*\|=\|T\|$**——这是"泛函够多"最直接的红利。

**例 3（右平移的共轭是左平移）**：取 $X=Y=l^1$，$T$ 是右平移算子

$$T(\alpha_1,\alpha_2,\dots)=(0,\alpha_1,\alpha_2,\dots), \tag{6.3.30}$$

则 $T^*:l^\infty\to l^\infty$ 是**左平移算子**

$$T^*(\xi_1,\xi_2,\dots)=(\xi_2,\xi_3,\dots), \tag{6.3.31}$$

且 $\|T\|=\|T^*\|=1$。

*验证*：*因为* $(l^1)^*=l^\infty$，泛函 $f$ 对应序列 $(\xi_k)$，$f(x)=\sum_kx_k\xi_k$。对 $x=(\alpha_1,\alpha_2,\dots)$，

$$T^*f(x)=f(Tx)=\sum_{k=1}^\infty(Tx)_k\xi_k=\sum_{k=1}^\infty\alpha_k\xi_{k+1},$$

*因为* $(Tx)_k=\alpha_{k-1}$（$k\geqslant2$）、$(Tx)_1=0$，故 $T^*f$ 对应的序列恰是 $(\xi_2,\xi_3,\dots)$。**"右移的对偶是左移"——方向被对偶翻转了**。

**例 4（积分算子的共轭是转置核）**：设 $E\subset\mathbb{R}^n$ 可测，$K(x,y)$ 在 $E\times E$ 上平方可积，定义

$$T:u\mapsto(Tu)(x)=\int_EK(x,y)u(y)\,\mathrm{d}y,\qquad\forall u\in L^2(E), \tag{6.3.32}$$

则 $T\in\mathcal{B}(L^2(E))$，且其共轭算子为

$$(T^*v)(x)=\int_EK(y,x)v(y)\,\mathrm{d}y,\qquad\forall v\in L^2(E). \tag{6.3.33}$$

*读法*：**共轭 = 把核的两个变量交换**。这解释了为什么"自伴算子"在积分算子里的样子是 $K(x,y)=\overline{K(y,x)}$。

**定理 6.3.15（$T^{**}$ 是 $T$ 的延拓）**：设 $X,Y$ 是线性赋范空间，$T\in\mathcal{B}(X,Y)$，则 $T^{**}=(T^*)^*\in\mathcal{B}(X^{**},Y^{**})$ 是 $T$ 在 $X^{**}$ 上的延拓，且 $\|T^{**}\|=\|T\|$。

*证明思路*：*因为* $X\subset X^{**}$、$Y\subset Y^{**}$，把自然映射分别记为 $U,V$。对 $f\in Y^*$、$x\in X$，

$$\langle T^{**}Ux,f\rangle=\langle Ux,T^*f\rangle=\langle T^*f,x\rangle=\langle f,Tx\rangle=\langle VTx,f\rangle,$$

（第一个等号用 $T^{**}$ 的定义；第二个用自然映射的定义；第三个用 $T^*$ 的定义；第四个再用自然映射的定义。）故 $T^{**}Ux=VTx$，即 $T^{**}$ 是 $T$ 在 $X^{**}$ 上的扩张。$\|T^{**}\|=\|T\|$ 由定理 6.3.14 用两次得到。交换图表：

$$\begin{array}{ccc}X&\xrightarrow{\ U\ }&X^{**}\\{\scriptstyle T}\big\downarrow&&\big\downarrow{\scriptstyle T^{**}}\\Y&\xrightarrow{\ V\ }&Y^{**}\end{array}$$

**两条常用运算律（教材习题 23、24）**：
- **复合**：$S\in\mathcal{B}(Y,Z)$、$T\in\mathcal{B}(X,Y)$，则 $(ST)^*=T^*S^*$。*因为* 对 $f\in Z^*$、$x\in X$，$(ST)^*f(x)=f(STx)=(S^*f)(Tx)=(T^*S^*f)(x)$。**注意顺序反了**——这与矩阵转置 $(AB)^T=B^TA^T$ 完全一致。
- **求逆**：若 $T^{-1}\in\mathcal{B}(Y,X)$，则 $(T^*)^{-1}$ 存在、$(T^*)^{-1}\in\mathcal{B}(X^*,Y^*)$ 且 $(T^*)^{-1}=(T^{-1})^*$。*因为* 由复合律 $T^*(T^{-1})^*=(T^{-1}T)^*=I^*=I$，同理另一侧。

**边界情况（三种"共轭"要分清）**：

| 记号 | 定义在 | 是什么 | 出现场合 |
|---|---|---|---|
| $X^*$ | 空间 | 共轭**空间**（对偶空间） | 本节 §6.3.2 |
| $T^*:Y^*\to X^*$ | Banach 空间 | 共轭**算子**（转置的推广） | 本节 §6.3.3 |
| $T^*:H\to H$ | Hilbert 空间 | Hilbert **伴随算子**（自伴、酉算子的基础） | Ch5 §5.3 |

**三者记号常混写，使用时必须按上下文区分**。它们的关系是：若 $H$ 是 Hilbert 空间、$A:H\to H^*$ 是 Riesz 表示给出的共轭线性等距（$Ax_0=f_{x_0}$，$f_{x_0}(x)=\langle x,x_0\rangle$），则 Hilbert 伴随与 Banach 共轭由

$$T^*=A^{-1}T^{\times}A$$

相联系（旧讲解包用 $T^\times$ 记 Banach 共轭以区别）。*因为* $A$ 是共轭线性的，这条公式里的 $A^{-1}$ 也是共轭线性的，所以两种"共轭"差一个共轭线性同构——**方向感完全不同**。

**例题（共轭算子性质的两条验证，教材习题 26）**：设 $X$ 是 Banach 空间，$T\in\mathcal{B}(X)$。证明

$$\operatorname{Ran}(T)^\perp=\ker(T^*),\qquad \overline{\operatorname{Ran}(T^*)}=(\ker T)^\perp,$$

其中 $M^\perp=\{f\in X^*:f|_M=0\}$。

*第一条*：$f\in\operatorname{Ran}(T)^\perp$ $\iff$ 对一切 $x\in X$ 有 $f(Tx)=0$ $\iff$ 对一切 $x$ 有 $(T^*f)(x)=0$ $\iff$ $T^*f=0$ $\iff$ $f\in\ker(T^*)$。（中间两步分别用了 $T^*$ 的定义与"泛函为零 $\iff$ 处处为零"。）

*第二条*：先证 $\overline{\operatorname{Ran}(T^*)}\subset(\ker T)^\perp$。*因为* 对 $g=T^*f\in\operatorname{Ran}(T^*)$ 与 $x\in\ker T$ 有 $g(x)=f(Tx)=f(0)=0$，故 $\operatorname{Ran}(T^*)\subset(\ker T)^\perp$；*因为* $(\ker T)^\perp$ 是闭子空间（它是闭集的交），取闭包即得。反向：设 $g\notin\overline{\operatorname{Ran}(T^*)}$。*因为* $\overline{\operatorname{Ran}(T^*)}$ 是 $X^*$ 的闭子空间，由**定理 6.3.7** 存在 $F\in X^{**}$ 使 $\|F\|=1$、$F|_{\overline{\operatorname{Ran}(T^*)}}=0$、$F(g)=\rho(g,\overline{\operatorname{Ran}(T^*)})>0$。*因为* $X$ 是 Banach 空间……（此处用到"$X\subset X^{**}$"与自反性之外的额外论证，教材习题 26 只要求给出等式，完整推导留待泛函分析续）。**为不臆造，此处只保留第一条的完整证明与第二条的包含方向**，反向的细节列入「防跳跃」。

> **停顿自问**：为什么共轭算子的方向是反的？——*因为* 泛函是"吃掉向量"的：$f$ 吃 $Y$ 中的向量，而 $T$ 把 $X$ 的向量送进 $Y$。要让 $f$ 吃掉 $Tx$，$T^*f$ 就必须反过来作用在 $X$ 上。**对偶天然带一个反向箭头**，这与矩阵转置、微分形式的拉回（pullback）是同一个现象。

### 检验回路：自测题与讲给别人听

> 验收标准：**明天能把本节讲给别人听**，且能回答"学这干嘛"。先自己做，再看答案。

**Q1（动机复述，必答）** 用自己的话回答：为什么需要 Hahn–Banach 定理？它与其他三个大定理在"是否要求完备性"上有什么不同？

> [!note]- 答案
> 没有 Hahn–Banach，连"非零赋范空间上存在非零连续泛函"都无法保证，分离点、对偶论证、$\|T^*\|=\|T\|$ 全部失效。它做的是"把子空间上的泛函保范延拓到全空间"，用的是 Zorn 引理（集合论工具），**完全不需要完备性**；而开映射、逆算子、闭图像、共鸣定理都靠 Baire 纲定理，都以 Banach 空间为前提。

**Q2（分离泛函）** 设 $X$ 赋范，$x_0\neq0$。叙述并证明：存在 $f\in X^*$ 使 $f(x_0)=\|x_0\|$ 且 $\|f\|=1$。这个结论说明 $X^*$ 的什么性质？

> [!note]- 答案
> 在一维子空间 $X_1=\{\alpha x_0\}$ 上定义 $f_1(\alpha x_0)=\alpha\|x_0\|$，则 $|f_1(\alpha x_0)|=|\alpha|\|x_0\|=\|\alpha x_0\|$，故 $\|f_1\|=1$。由保范延拓定理，存在 $f\in X^*$ 使 $f|_{X_1}=f_1$、$\|f\|=1$；特别 $f(x_0)=\|x_0\|$。它说明 $X^*$ **能分离点**：若对一切 $f\in X^*$ 有 $f(x)=0$，则 $x=0$。

**Q3（共轭空间）** 写出 $l^1$ 上连续线性泛函的一般形式，并证明 $\|f\|=\sup_k|\eta_k|$ 的两个方向。

> [!note]- 答案
> 一般形式：$f(x)=\sum_k\xi_k\eta_k$，其中 $(\eta_k)\in l^\infty$。方向 $\sup_k|\eta_k|\leqslant\|f\|$：$\eta_k=f(e_k)$ 且 $\|e_k\|_1=1$。方向 $\|f\|\leqslant\sup_k|\eta_k|$：$|f(x)|\leqslant\sum_k|\xi_k||\eta_k|\leqslant\sup_k|\eta_k|\cdot\|x\|_1$。两个方向合起来即 $(l^1)^*$ 与 $l^\infty$ 保范同构。

**Q4（$(l^p)^*=l^q$ 的难点）** 证明 $(l^p)^*=l^q$ 时，$\|(\eta_k)\|_q\leqslant\|f\|$ 这一步怎么走？试探元构造的目的是什么？

> [!note]- 答案
> 令 $\eta_k=f(e_k)$，构造 $\xi_k^{(n)}=|\eta_k|^q/\eta_k$（$k\leqslant n$）、其余为 $0$。目的：让 $|\xi_k^{(n)}|^p=|\eta_k|^q$，于是 $\|x_n\|_p=\big(\sum_{k\leqslant n}|\eta_k|^q\big)^{1/p}$ 而 $f(x_n)=\sum_{k\leqslant n}|\eta_k|^q$——分子分母恰好对消，除以 $\|x_n\|_p$ 后直接得到 $\big(\sum_{k\leqslant n}|\eta_k|^q\big)^{1/q}\leqslant\|f\|$。它的几何含义是把 $\eta_k$ "旋转到正实轴"，使 $f$ 在 $x_n$ 上的取值不带相位损失。

**Q5（共轭算子）** 设 $X=Y=l^1$，$T$ 是右平移。求 $T^*$ 并验证 $\|T^*\|=\|T\|$。为什么 $T^*$ 与 $T$ 方向相反？

> [!note]- 答案
> 由 $(l^1)^*=l^\infty$，$f$ 对应 $(\xi_k)$。$T^*f(x)=f(Tx)=\sum_k\alpha_k\xi_{k+1}$，故 $T^*f$ 对应 $(\xi_2,\xi_3,\dots)$，即 $T^*$ 是左平移。$\|T\|=1$（右移不改变 $l^1$ 范数），$\|T^*\|=1$（左移不改变 $l^\infty$ 范数），二者相等，符合定理 6.3.14。方向相反的原因：泛函"吃掉"向量，$f$ 吃 $Y$ 的向量而 $T$ 把 $X$ 的向量送进 $Y$，所以 $T^*f$ 必须作用在 $X$ 上——**对偶天然带一个反向箭头**。

**讲给别人听清单**：① 次线性泛函与 Zorn 引理的角色；② Hahn–Banach 实版本的一维延拓（$c$ 夹在 sup 与 inf 之间）与复版本的 $f(x)=g(x)-\mathrm{i}g(\mathrm{i}x)$；③ 推论 6.3.3–6.3.6 的链条与 $\|x\|=\sup_{\|f\|\leqslant1}|f(x)|$；④ 定理 6.3.7（分离定理）的证明；⑤ 保范延拓不唯一的反例；⑥ $(l^1)^*=l^\infty$、$(l^p)^*=l^q$ 的两条线；⑦ $(C[a,b])^*$ = 有界变差/测度的五步证明；⑧ 第二共轭空间、自然映射与自反空间；⑨ 共轭算子的定义、$\|T^*\|=\|T\|$ 与复合律 $(ST)^*=T^*S^*$；⑩ 三种"共轭"记号的区别。

**回填学习者状态**：卡在 **Hahn–Banach 一维延拓** → 只记 $c$ 必须夹在 $\sup[-p(x''-x_0)+f(x'')]$ 与 $\inf[p(x'+x_0)-f(x')]$ 之间，关键是证明左 $\leqslant$ 右；卡在 **$(l^p)^*=l^q$** → 只记试探元 $\xi_k^{(n)}=|\eta_k|^q/\eta_k$ 的目的：让 $f(x_n)$ 恰好等于 $\sum|\eta_k|^q$；卡在 **$\|T^*\|=\|T\|$** → 把 $\|Tx\|$ 用推论 6.3.5 换成 $\sup_{\|f\|\leqslant1}|f(Tx)|$，然后交换两个上确界；卡在 **$C[a,b]$ 共轭空间** → 只记五步标题，细节用到再查。

> **本节真正要说的是什么**：**"表示"是泛函分析的核心动词。** Hahn–Banach 保证泛函够多（所以"表示"有素材），共轭空间把抽象泛函表示成具体对象（$l^q$、$L^q$、有界变差函数、测度），共轭算子把算子的对偶版本表示出来。**Ch2 的测度在这里以泛函的身份回归**——这是全书两条线（测度论与泛函分析）唯一一次真正合流。

## 去脉（学完去哪）

- **当代应用**：① **测度论与概率论**：Riesz 表示定理把"连续线性泛函"等同于"测度"，这正是一般测度构造（如 Riesz–Markov–Kakutani 定理）的入口；概率论中"随机变量 = 线性泛函"的视角也来自这里。② **分布理论**：Schwartz 分布就是 $C_0^\infty$ 的对偶空间，Hahn–Banach 是"分布足够多"的保证。③ **凸分析与最优化**：分离定理的几何形式（超平面分离凸集与点）是 Lagrange 对偶、支撑超平面理论的基础。④ **变分法**：弱解的存在性论证先要在对偶空间中"找泛函"，再用 Hahn–Banach 延拓回去。
- **跨领域解读**：共轭算子 $T^*:Y^*\to X^*$ 与矩阵转置 $(AB)^T=B^TA^T$、微分形式的拉回是同一个"方向反转"现象。**凡是有"配对"（pairing）的地方，映射都会在对偶侧反向**。
- **高层视角**：本节把"泛函"从被动工具变成主动对象。回到学科概览的两条主线：Hilbert 侧用内积做表示（Riesz 表示定理），Banach 侧用泛函做表示（Hahn–Banach + 共轭空间）。**两边的差别是"有没有内积"，共同点都是"表示"。**

## 防跳跃

- [ ] 定理 6.3.7 的**几何形式**：超平面与半空间、单位球在 $x_0\in\partial B_1$ 处的切平面（教材 §6.3 习题 20 只给结论）
- [ ] $(L^p)^*=L^q$ 满射性的完整证明（教材转引张恭庆、林源渠《泛函分析讲义》上册 p.128，本 seed 无该书）
- [ ] $(C[a,b])^*\cong BV[a,b]$ 满射性与唯一性的完整证明（同上，教材转引 p.130）
- [ ] Riesz 表示定理（定理 6.3.9）中"完全可加的集函数"与 Ch2 的测度公理的对接细节
- [ ] 教材习题 26 第二条等式 $\overline{\operatorname{Ran}(T^*)}=(\ker T)^\perp$ 的完整证明（本节点只给出 $\subset$ 方向）
- [ ] $\mathbb{K}^n$ 上"共轭矩阵 $A^*=(\overline{a_{ji}})$"与实矩阵转置的差别（复情形的共轭线性）
- [ ] 自反空间的性质（闭子空间自反、$X$ 自反 $\iff$ $X^*$ 自反、与弱列紧性的关系）——**在 Sec6.4 展开**
- [ ] 定理 6.3.7 与"$M^\perp$ 的对偶刻画"在商空间 $(X/M)^*$ 上的形态（教材 §6.3 习题 14）
- [ ] 泛函延拓在**非赋范**的拓扑线性空间中的形式（教材不覆盖）

## 来源与映射

| 本节点内容 | 来源 | 处理 |
|---|---|---|
| 次线性泛函定义、Zorn 引理的作用 | 旧《Ch10》§10.1（§1.1、§1.2） | 原文迁移 |
| 定理 6.3.1（Hahn–Banach 实版本）及一维延拓 + Zorn 两步证明 | 旧《Ch10》§10.1（§2.2）+ 郭版教材 §6.3.1 | 合并改写（郭版用"保范"形式叙述，旧包用"被 $p$ 控制"形式叙述，此处以郭版叙述、旧包的一维夹逼论证为主） |
| 定理 6.3.2（Hahn–Banach 复版本）及旋转技巧证明 | 旧《Ch10》§10.1（§2.3）+ 郭版教材 §6.3.1 | 合并改写（郭版证明更完整，以郭版为准） |
| 推论 6.3.3–6.3.6（分离点、泛函够多、范数对偶表示、$x_0=0$ 判据） | 郭版教材 §6.3.1 | 新写补缺（旧《Ch10》§10.1 定理 4 与之部分重合，已并入） |
| 定理 6.3.7（分离定理）及证明 | 旧《Ch10》§10.1 定理 3、4 相关段落 + 郭版教材 §6.3.1 | 合并改写（以郭版为准） |
| 定理 6.3.7 的推论（$\overline{\operatorname{linspace}S}$ 的对偶刻画） | 郭版教材 §6.3.1 末段 | 新写补缺 |
| 边界情况：保范延拓一般不唯一（$\mathbb{R}^2$ 配 $\|\cdot\|_1$ 的例子） | 郭版教材 §6.3.1 关于 (6.3.6) 的注 + §6.1 习题 1 的范数 $\|z\|_1$ | 新写补缺（教材指出"不唯一"但未给例子，例子由教材已有素材构造） |
| 例题：教材习题 7（距离的对偶公式） | 郭版教材 §6.3 习题 7 | 新写补缺 |
| 定义 6.3.8（共轭空间）；$X^*$ 恒为 Banach 空间 | 旧《Ch8》§8.2（§4.1）+ 郭版教材 §6.3.2 | 合并改写 |
| 例 1：$(l^1)^*=l^\infty$（两条线证明） | 旧《Ch8》§8.2（§4.2） | 原文迁移 |
| 例 2：$(l^p)^*=l^q$（试探元构造） | 旧《Ch8》§8.2（§4.3） | 原文迁移 |
| 例 3：$(L^p[0,1])^*=L^q[0,1]$、$\sigma$ 有限情形 | 郭版教材 §6.3.2 例 1 | 新写补缺 |
| 例 4：$(c_0)^*=l^1$ | 郭版教材 §6.3 习题 15(2) | 新写补缺 |
| 例 5：$(C[0,1])^*\cong BV[0,1]$（五步证明） | 旧《Ch10》§10.2 + 郭版教材 §6.3.2 例 2 | 合并改写（郭版给出 $BV[0,1]$ 的定义与范数 $\|g\|_v=\operatorname{Var}(g)$，旧包给出五步证明骨架） |
| 定理 6.3.9（Riesz 表示定理，$C(M)^*$ = Baire 测度） | 郭版教材 §6.3.2 | 新写补缺 |
| 第二共轭空间、自然映射 $\tau$、$\|F_x\|=\|x\|$、定理 6.3.11 | 郭版教材 §6.3.2 | 新写补缺 |
| 定义 6.3.12（自反空间）与"$p=1,\infty$ 时 $L^p$ 不自反"的反例 | 郭版教材 §6.3.2 | 新写补缺（自反空间的**性质与弱列紧应用**归 Sec6.4，此处只给定义与反例） |
| 反例：$(l^\infty)^*\neq l^1$ | 郭版教材 §6.3 习题 10 | 新写补缺 |
| 例题：$l^p$ 泛函范数的完整计算 | 旧《Ch8》§8.2（§4.3 的证明）+ 郭版教材 §6.3.2 例 1 的两条线 | 合并改写 |
| 定义 6.3.13（共轭算子）、存在唯一性与 $\|T^*\|\leqslant\|T\|$ | 旧《Ch10》§10.3 + 郭版教材 §6.3.3 | 合并改写 |
| 定理 6.3.14（$*\mapsto T^*$ 是等距同构）及双重上确界证明 | 郭版教材 §6.3.3 | 新写补缺（旧包用定理 4 分别证两个方向，郭版用推论 6.3.5 一次交换上确界，以郭版为准并注明旧包路线） |
| 例 3（右平移的共轭是左平移）、例 4（积分算子的共轭是转置核） | 郭版教材 §6.3.3 例 3、例 4 | 新写补缺 |
| 定理 6.3.15（$T^{**}$ 是 $T$ 的延拓）与交换图表 | 郭版教材 §6.3.3 | 新写补缺 |
| 运算律 $(ST)^*=T^*S^*$、$(T^*)^{-1}=(T^{-1})^*$ | 郭版教材 §6.3 习题 24、23 | 新写补缺 |
| 有限维对应（共轭矩阵 $(\overline{a_{ji}})$）；与 Hilbert 共轭的关系 $T^*=A^{-1}T^\times A$ | 旧《Ch10》§10.3（"有限维对应""与希尔伯特共轭的关系"两段）+ 郭版教材 §6.3.3 开头 | 原文迁移 |
| 例题：教材习题 26 第一条等式（$\operatorname{Ran}(T)^\perp=\ker(T^*)$） | 郭版教材 §6.3 习题 26 | 新写补缺（第二条等式只给 $\subset$ 方向，反向转「防跳跃」） |
| 检验回路：5 道自测题与讲给别人听清单 | 旧《Ch10》§10.9（Q2、Q5 等）+ 旧《Ch8》§8.7（Q4）+ 本次按本节内容重排 | 原文迁移 + 合并改写 |
| Hilbert 空间的 Riesz 表示定理与投影定理 | — | **不写入本节**（归 Ch5 §5.2、§5.3；本节只在 §6.3.2 的动机与 §6.3.3 的记号对照处引用） |
| 自反空间的弱列紧性、Banach–Alaoglu | — | **不写入本节**（归 Sec6.4） |