---
type: note
formal: true
subject: differential-geometry
created: 2026-09-03
updated: 2026-09-03
tags: [math, differential-geometry, teaching-pack]
---

# 04 主题-Weingarten映射和主曲率

> 定位：把"求主曲率"归结为"求一个线性变换的特征值"，这是本章最关键的抽象一步。

## 整体认知

**Weingarten 映射**（记作 $W$，读作"外因加滕映射"）是曲面在一点切空间 $T_pS$ 到自身的线性变换，定义为 $W=-g_*$，其中 $g$ 是 **Gauss 映射**（读作"高斯映射"，把曲面上每点映到单位球面上对应法向量的映射）。它的两个特征值恰好是**主曲率**，特征方向是**主方向**。这样，几何问题（找弯曲最极端的方向）就变成了线性代数问题（求特征值）。

## 来龙

- 类比已知：曲线论用 Frenet 标架的运动刻画弯曲；曲面论用"法向量怎么变"（Gauss 映射）刻画弯曲。
- 解决新问题：法曲率随方向变化，需要统一地找出极值方向——特征值/特征向量正好提供这个框架。
- 理论/应用需要：主曲率、Gauss 曲率、平均曲率都从 Weingarten 映射的特征值读出。

## 主体

### 定义（先定义再使用）

1. **Gauss 映射** $g:S\to\Sigma$：把曲面点 $\pmb{r}(u,v)$ 映到单位球面 $\Sigma$ 上的点 $\pmb{n}(u,v)$（把法向量平移到原点，终点落在单位球面上）。
2. **切映射** $g_*$：Gauss 映射在切空间之间诱导的线性映射，满足 $g_*(\pmb{r}_u)=\pmb{n}_u$、$g_*(\pmb{r}_v)=\pmb{n}_v$（读作"g 星"，即切映射）。
3. **Weingarten 映射** $W=-g_*:T_pS\to T_pS$，即 $W(\mathrm{d}\pmb{r})=-\mathrm{d}\pmb{n}$。

**为什么 $W$ 是切空间到自身的映射**：$\pmb{n}$ 是单位向量，故 $\pmb{n}_u,\pmb{n}_v$ 都与 $\pmb{n}$ 垂直，因而落在切平面内，可等同为曲面切向量。

### 核心定理

- **定理 3.1**：$\mathbb{II}=W(\mathrm{d}\pmb{r})\cdot\mathrm{d}\pmb{r}$。即第二基本形式可用 Weingarten 映射表示。
- **定理 3.2**：$W$ 是**自共轭映射**（读作"自共轭"，即对任意两个切向量 $\mathrm{d}\pmb{r},\delta\pmb{r}$ 有 $W(\mathrm{d}\pmb{r})\cdot\delta\pmb{r}=\mathrm{d}\pmb{r}\cdot W(\delta\pmb{r})$）。自共轭 ⇒ 有两个实特征值、两个正交特征方向。
- **定理 3.3**：$W$ 的两个特征值就是主曲率 $\kappa_1\ge\kappa_2$，特征方向就是主方向。
- **定理 3.4（Euler 公式）**：设 $e_1,e_2$ 是正交主方向单位向量，则沿 $e=\cos\theta\,e_1+\sin\theta\,e_2$ 的法曲率
  $$
  \kappa_n(\theta)=\kappa_1\cos^2\theta+\kappa_2\sin^2\theta.
  $$

### 脐点、平点、圆点

- **脐点**（读作"脐点"）：$\kappa_1=\kappa_2$ 的点，此时任意方向都是主方向，$\frac{L}{E}=\frac{M}{F}=\frac{N}{G}$。
- 若该比值为零 → **平点**（平面上的点）；非零 → **圆点**（球面上的点）。
- 命题：曲面是平面 ⇔ 所有点都是平点；曲面是球面 ⇔ 所有点都是圆点。

### 曲率线

- **曲率线**（读作"曲率线"）：每点切方向都是主方向的曲线，即主方向场的积分曲线。
- **定理 3.5（Rodrigues 定理）**：曲线 $C$ 是曲率线 ⇔ 沿 $C$ 的法向量导数与切向量平行，即 $\frac{\mathrm{d}\pmb{n}}{\mathrm{d}t}\parallel\frac{\mathrm{d}\pmb{r}}{\mathrm{d}t}$。
- **定理 3.6**：$C$ 是曲率线 ⇔ 沿 $C$ 的法线构成可展曲面。

### 迷你算例（数字从哪来）

**输入**：圆柱面 $\pmb{r}=(a\cos\frac{u}{a},\,a\sin\frac{u}{a},\,v)$，$a=2$。已知 $L=-\frac{1}{2},M=0,N=0$，$E=1,F=0,G=1$。

**处理**：Weingarten 映射在自然基底下的矩阵（详见 [[M-02 方法-主曲率计算]]）为
$$
A=\frac{1}{EG-F^2}\begin{pmatrix}LG-MF & -LF+ME\ MG-NF & -MF+NE\end{pmatrix}
=\begin{pmatrix}-\frac{1}{2} & 0\ 0 & 0\end{pmatrix}.
$$
特征方程 $\det(A-\lambda I)=(-\frac{1}{2}-\lambda)(-\lambda)=0$，得 $\lambda_1=0,\lambda_2=-\frac{1}{2}$。

**结果**：主曲率 $\kappa_1=0$（沿 v 方向，直母线方向）、$\kappa_2=-\frac{1}{2}$（沿 u 方向，圆周方向）。数字来源：$L=-\frac{1}{2}$ 直接成为矩阵的 $(1,1)$ 元，特征值就是 $L/E$ 和 $N/G$。

## 去脉

主曲率是后续 H、K（[[05 主题-主方向和主曲率的计算]]）、Dupin 标形（[[06 主题-Dupin标形和曲面参数方程在一点的标准展开]]）的基础。方法细节见 [[M-01 方法-第二基本形式与Weingarten映射]] 与 [[M-02 方法-主曲率计算]]。

## 可直接引用的结论句

- "Weingarten 映射的特征值就是主曲率，特征方向就是主方向。"
- "Euler 公式：$\kappa_n(\theta)=\kappa_1\cos^2\theta+\kappa_2\sin^2\theta$。"
- "曲率线是主方向场的积分曲线，等价于沿它法向量导数与切向量平行（Rodrigues 定理）。"

**过度承诺（不能写）**：
- ❌ "Weingarten 映射的矩阵就是 $\begin{pmatrix}L&M\M&N\end{pmatrix}$"——那是 II 的系数矩阵；$W$ 的矩阵是 $\begin{pmatrix}L&M\M&N\end{pmatrix}\begin{pmatrix}E&F\F&G\end{pmatrix}^{-1}$。
- ❌ "脐点处主方向不存在"——脐点处主方向不确定（任意方向都是主方向），不是不存在。

## 延伸指引

- 前置：[[03 主题-法曲率]]（法曲率、Euler 公式的初等推导）、[[M-01 方法-第二基本形式与Weingarten映射]]。
- 深入：[[05 主题-主方向和主曲率的计算]]（具体怎么算）、[[M-02 方法-主曲率计算]]。
- 更远：第五章自然标架运动公式、第七章活动标架与外微分。

## 自测题

1. （动机复述）为什么把"求主曲率"转化为"求 Weingarten 映射的特征值"是有价值的？它把几何问题变成了什么问题？
2. （概念）Weingarten 映射 $W$ 与第二基本形式 II 的关系是什么？写出 $\mathbb{II}=W(\mathrm{d}\pmb{r})\cdot\mathrm{d}\pmb{r}$。
3. （应用陷阱）"Weingarten 映射的矩阵就是 $\begin{pmatrix}L&M\M&N\end{pmatrix}$"——这个说法对吗？正确的矩阵是什么？
4. （概念）脐点处主方向是什么情况？平点与圆点分别对应什么曲面？
5. （计算）对圆柱面 $a=2$，两个主曲率分别是多少？分别对应哪个方向？

[[00 整体认知]] · [[03 主题-法曲率]] · [[05 主题-主方向和主曲率的计算]] · [[M-01 方法-第二基本形式与Weingarten映射]] · [[M-02 方法-主曲率计算]]
