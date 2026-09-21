---
type: note
formal: true
subject: differential-geometry
created: 2026-09-03
updated: 2026-09-03
tags: [math, differential-geometry, teaching-pack]
---

# M-01 方法-第二基本形式与Weingarten映射

> 定位：共用方法文件。本方法把"第二基本形式 II"与"Weingarten 映射 W"讲透，被多个主题共用。首次用到它的主题会创建它，后续主题直接引用「详见 M-01」。

## 这个方法是什么

本方法提供两条主线：
1. **第二基本形式 II 的两种等价定义**：$L,M,N$ 定义与 $\mathbb{II}=-\mathrm{d}\pmb{r}\cdot\mathrm{d}\pmb{n}$。
2. **Weingarten 映射 W**：$W=-g_*$，把"法向量怎么变"编码成切空间上的自共轭线性变换，且 $\mathbb{II}=W(\mathrm{d}\pmb{r})\cdot\mathrm{d}\pmb{r}$。

## 为什么需要它

- II 是本章所有曲率的分子来源（法曲率、主曲率、H、K）。
- W 把"求主曲率"变成"求特征值"，是统一框架。
- 多个主题（02/03/04/05/06）都依赖这两个对象，故单独成方法文件。

## 主体

### 第二基本形式 II

设 $S:\pmb{r}=\pmb{r}(u,v)$ 正则参数曲面，$\pmb{n}$ 为单位法向量。定义第二类基本量
$$
L=\pmb{r}_{uu}\cdot\pmb{n},\quad M=\pmb{r}_{uv}\cdot\pmb{n},\quad N=\pmb{r}_{vv}\cdot\pmb{n}.
$$
因为 $\pmb{r}_u\cdot\pmb{n}=0$、$\pmb{r}_v\cdot\pmb{n}=0$（切向量与法向量垂直），求导得
$$
L=-\pmb{r}_u\cdot\pmb{n}_u,\quad M=-\pmb{r}_u\cdot\pmb{n}_v=-\pmb{r}_v\cdot\pmb{n}_u,\quad N=-\pmb{r}_v\cdot\pmb{n}_v.
$$
于是
$$
\mathbb{II}=L(\mathrm{d}u)^2+2M\,\mathrm{d}u\,\mathrm{d}v+N(\mathrm{d}v)^2=-\mathrm{d}\pmb{r}\cdot\mathrm{d}\pmb{n}.
$$

**几何意义**：$\mathbb{II}$ 是邻近点到切平面有向距离 $\delta$ 的二阶主要部分的两倍，即 $\mathbb{II}\approx 2\delta$。

### Weingarten 映射 W

1. **Gauss 映射** $g:S\to\Sigma$：$g(\pmb{r}(u,v))=\pmb{n}(u,v)$（把法向量平移到原点，终点在单位球面上）。
2. **切映射** $g_*$：$g_*(\pmb{r}_u)=\pmb{n}_u$、$g_*(\pmb{r}_v)=\pmb{n}_v$。
3. **Weingarten 映射** $W=-g_*$：$W(\mathrm{d}\pmb{r})=-\mathrm{d}\pmb{n}$。

**为什么 W 是切空间到自身的映射**：$\pmb{n}$ 是单位向量，故 $\pmb{n}_u,\pmb{n}_v$ 都与 $\pmb{n}$ 垂直，落在切平面内。

### 核心性质

- **定理 3.1**：$\mathbb{II}=W(\mathrm{d}\pmb{r})\cdot\mathrm{d}\pmb{r}$。
- **定理 3.2**：$W$ 是自共轭映射：$W(\mathrm{d}\pmb{r})\cdot\delta\pmb{r}=\mathrm{d}\pmb{r}\cdot W(\delta\pmb{r})$。自共轭 ⇒ 两个实特征值、两个正交特征方向。
- **定理 3.3**：$W$ 的特征值就是主曲率，特征方向就是主方向。

### 迷你算例（数字从哪来）

**输入**：圆柱面 $\pmb{r}=(a\cos\frac{u}{a},\,a\sin\frac{u}{a},\,v)$，$a=2$，点 $u=0,v=0$。

**处理**：
1. $\pmb{r}_u=(0,1,0)$，$\pmb{r}_v=(0,0,1)$，$\pmb{n}=(1,0,0)$。
2. $\pmb{r}_{uu}=(-\frac{1}{2},0,0)$，$\pmb{r}_{uv}=\pmb{r}_{vv}=\pmb{0}$。
3. $L=\pmb{r}_{uu}\cdot\pmb{n}=-\frac{1}{2}$，$M=N=0$。
4. $W(\pmb{r}_u)=-\pmb{n}_u$。由 $L=-\pmb{r}_u\cdot\pmb{n}_u$ 且 $\pmb{n}_u$ 在切平面内，可解出 $\pmb{n}_u=\frac{1}{2}\pmb{r}_u$（因为 $-\pmb{r}_u\cdot\pmb{n}_u=-\frac{1}{2}$），故 $W(\pmb{r}_u)=-\frac{1}{2}\pmb{r}_u$；同理 $W(\pmb{r}_v)=0$。

**结果**：$W$ 在基底 $(\pmb{r}_u,\pmb{r}_v)$ 下的矩阵是 $\begin{pmatrix}-\frac{1}{2}&0\0&0\end{pmatrix}$，特征值 $-\frac{1}{2}$ 和 $0$。数字来源：$L=-\frac{1}{2}$ 直接成为特征值，$N=0$ 给出另一个特征值 0。

## 使用它的主题

- [[02 主题-第二基本形式]]（II 的定义与几何意义）
- [[03 主题-法曲率]]（$\kappa_n=\mathbb{II}/\mathrm{I}$）
- [[04 主题-Weingarten映射和主曲率]]（W 与主曲率）
- [[05 主题-主方向和主曲率的计算]]（H、K、特征方程）
- [[06 主题-Dupin标形和曲面参数方程在一点的标准展开]]（Euler 公式、标准展开）

## 可直接引用的结论句

- "第二基本形式 $\mathbb{II}=-\mathrm{d}\pmb{r}\cdot\mathrm{d}\pmb{n}$ 是曲面偏离切平面的二阶度量。"
- "Weingarten 映射 $W=-g_*$ 满足 $\mathbb{II}=W(\mathrm{d}\pmb{r})\cdot\mathrm{d}\pmb{r}$，且是自共轭的。"
- "W 的特征值就是主曲率，特征方向就是主方向。"

**过度承诺（不能写）**：
- ❌ "W 的矩阵就是 $\begin{pmatrix}L&M\M&N\end{pmatrix}$"——那是 II 的系数矩阵；W 的矩阵是 $\begin{pmatrix}L&M\M&N\end{pmatrix}\begin{pmatrix}E&F\F&G\end{pmatrix}^{-1}$。
- ❌ "II 是内蕴量"——II 依赖法向量在空间中的取法，翻转定向会改变符号，是外蕴量。

## 延伸指引

- 前置：[[Ch3 曲面的第一基本形式 - 讲解包/00 整体认知]]（I、切平面、法向量）、线性代数自共轭变换。
- 深入：[[04 主题-Weingarten映射和主曲率]]、[[05 主题-主方向和主曲率的计算]]。
- 更远：第五章自然标架运动公式、第七章活动标架与外微分。

## 自测题

1. （动机复述）为什么把 II 与 W 放在同一个方法文件里？它们之间有什么等式联系？
2. （概念）$L=-\pmb{r}_u\cdot\pmb{n}_u$ 是怎么从 $L=\pmb{r}_{uu}\cdot\pmb{n}$ 推出来的？用了哪条性质？
3. （应用陷阱）"W 的矩阵就是 $\begin{pmatrix}L&M\M&N\end{pmatrix}$"——为什么错？正确的矩阵是什么？
4. （计算）对圆柱面 $a=2$，$W$ 的特征值是多少？分别对应什么方向？
5. （概念）为什么 W 是自共轭的？自共轭保证了什么？

[[00 整体认知]] · [[02 主题-第二基本形式]] · [[03 主题-法曲率]] · [[04 主题-Weingarten映射和主曲率]] · [[05 主题-主方向和主曲率的计算]] · [[06 主题-Dupin标形和曲面参数方程在一点的标准展开]]
