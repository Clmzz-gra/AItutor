---
type: note
formal: true
subject: differential-geometry
created: 2026-09-03
updated: 2026-09-03
tags: [math, differential-geometry, teaching-pack]
---

# 05 主题-曲线的挠率和 Frenet 公式

> 定位：引入第二个不变量——挠率，并给出 Frenet 标架沿曲线的完整运动方程（Frenet 公式）。方法详见 [[M-01 方法-活动标架法]]、[[M-02 方法-弧长参数化]]。

## 整体认知

曲率刻画"弯不弯"，挠率 $\tau$ 刻画"扭不扭"——即曲线**偏离平面曲线的程度**。Frenet 公式把 Frenet 标架三个向量随弧长的变化写成以 $\kappa,\tau$ 为系数的线性方程组，是曲线论中最基本最重要的公式。

## 来龙

- **类比已知**：平面曲线永远在一个平面内；空间曲线会"扭出"平面。
- **解决新问题**：如何量化"曲线偏离平面的程度"？如何完整描述 Frenet 标架随曲线运动？
- **理论需要**：Frenet 公式是后续基本定理、标准展开、曲线偶研究的核心工具。

## 主体

### 定义：挠率

次法向量 $\boldsymbol{\gamma}(s)$ 关于弧长的导数长度 $|\boldsymbol{\gamma}'(s)|$ 反映密切平面方向转动的快慢，刻画曲线扭曲程度。因为 $\boldsymbol{\gamma}$ 是单位向量，$\boldsymbol{\gamma}'\perp\boldsymbol{\gamma}$；又由 $\boldsymbol{\gamma}=\boldsymbol{\alpha}\times\boldsymbol{\beta}$ 和 $\boldsymbol{\alpha}'\parallel\boldsymbol{\beta}$ 可证 $\boldsymbol{\gamma}'\perp\boldsymbol{\alpha}$，故 $\boldsymbol{\gamma}'$ 与 $\boldsymbol{\beta}$ 共线。设

$$
\boldsymbol{\gamma}'(s)=-\tau(s)\boldsymbol{\beta}(s),
$$

则定义

$$
\tau(s)=-\boldsymbol{\gamma}'(s)\cdot\boldsymbol{\beta}(s),
$$

称为曲线在 $s$ 处的**挠率**（torsion，读作"挠率"），且 $|\tau(s)|=|\boldsymbol{\gamma}'(s)|$。

### 定理 4.1：平面曲线与挠率

设曲线不是直线，则它是**平面曲线当且仅当挠率为零**。

**因为**：若 $\tau\equiv 0$，则 $\boldsymbol{\gamma}'=-\tau\boldsymbol{\beta}\equiv 0$，故 $\boldsymbol{\gamma}=\boldsymbol{\gamma}_0$ 为常向量。又 $0=\boldsymbol{r}'\cdot\boldsymbol{\gamma}=\frac{\mathrm{d}}{\mathrm{d}s}(\boldsymbol{r}\cdot\boldsymbol{\gamma}_0)$，所以 $\boldsymbol{r}(s)\cdot\boldsymbol{\gamma}_0$ 为常数，即曲线落在以 $\boldsymbol{\gamma}_0$ 为法向量的平面内。反之，平面曲线的次法向量是常向量，挠率为零。

### Frenet 公式

由定义已有 $\boldsymbol{r}'=\boldsymbol{\alpha},\ \boldsymbol{\alpha}'=\kappa\boldsymbol{\beta},\ \boldsymbol{\gamma}'=-\tau\boldsymbol{\beta}$。还需求 $\boldsymbol{\beta}'$。设 $\boldsymbol{\beta}'=a\boldsymbol{\alpha}+b\boldsymbol{\beta}+c\boldsymbol{\gamma}$，分别与 $\boldsymbol{\alpha},\boldsymbol{\beta},\boldsymbol{\gamma}$ 点乘，利用单位正交性与 $\boldsymbol{\alpha}'=\kappa\boldsymbol{\beta},\ \boldsymbol{\gamma}'=-\tau\boldsymbol{\beta}$，得 $a=-\kappa,\ b=0,\ c=\tau$。于是

$$
\left\{\begin{array}{l}
\boldsymbol{r}'(s)=\boldsymbol{\alpha}(s),\
\boldsymbol{\alpha}'(s)=\kappa(s)\boldsymbol{\beta}(s),\
\boldsymbol{\beta}'(s)=-\kappa(s)\boldsymbol{\alpha}(s)+\tau(s)\boldsymbol{\gamma}(s),\
\boldsymbol{\gamma}'(s)=-\tau(s)\boldsymbol{\beta}(s).
\end{array}\right.
$$

这组公式称为 **Frenet 公式**（Frenet formulas，由 Serret 1851 与 Frenet 1852 发表）。后三个方程可写成矩阵形式：

$$
\begin{pmatrix}\boldsymbol{\alpha}'\\boldsymbol{\beta}'\\boldsymbol{\gamma}'\end{pmatrix}
=\begin{pmatrix}0&\kappa&0\-\kappa&0&\tau\0&-\tau&0\end{pmatrix}
\begin{pmatrix}\boldsymbol{\alpha}\\boldsymbol{\beta}\\boldsymbol{\gamma}\end{pmatrix},
$$

系数矩阵是**反对称矩阵**（即 $a_{ij}=-a_{ji}$）。一般地，沿曲线定义的任意单位正交标架场的导数公式系数矩阵都是反对称的。

### 挠率的计算公式

若 $\boldsymbol{r}=\boldsymbol{r}(t)$，$t$ 非弧长参数，则

$$
\tau(t)=\frac{(\boldsymbol{r}'(t),\boldsymbol{r}''(t),\boldsymbol{r}'''(t))}{|\boldsymbol{r}'(t)\times\boldsymbol{r}''(t)|^2},
$$

其中 $(\cdot,\cdot,\cdot)$ 表示**混合积**（三个向量的行列式）。若 $t=s$ 是弧长参数，则

$$
\tau(s)=\frac{(\boldsymbol{r}'(s),\boldsymbol{r}''(s),\boldsymbol{r}'''(s))}{|\boldsymbol{r}''(s)|^2}.
$$

### 定理 4.3：平面曲线的混合积判据

曲线 $\boldsymbol{r}=\boldsymbol{r}(t)$ 是平面曲线的充分必要条件是

$$
(\boldsymbol{r}'(t),\boldsymbol{r}''(t),\boldsymbol{r}'''(t))\equiv 0.
$$

这是定理 4.1 与挠率公式的直接推论，且包含直线段情形。

### 定理 4.2：球面曲线的必要条件

设曲线曲率、挠率都不为零，若它落在球面上，则

$$
\left(\frac{1}{\kappa(s)}\right)^2+\left(\frac{1}{\tau(s)}\frac{\mathrm{d}}{\mathrm{d}s}\left(\frac{1}{\kappa(s)}\right)\right)^2=\text{常数}.
$$

**因为**：设球心 $\boldsymbol{r}_0$、半径 $a$，则 $(\boldsymbol{r}-\boldsymbol{r}_0)^2=a^2$。求导得 $\boldsymbol{\alpha}\cdot(\boldsymbol{r}-\boldsymbol{r}_0)=0$，故 $\boldsymbol{r}-\boldsymbol{r}_0=\lambda\boldsymbol{\beta}+\mu\boldsymbol{\gamma}$。再用 Frenet 公式比较系数得 $\lambda=-\frac{1}{\kappa},\ \mu=-\frac{1}{\tau}\frac{\mathrm{d}}{\mathrm{d}s}(\frac{1}{\kappa})$，代入 $(\boldsymbol{r}-\boldsymbol{r}_0)^2=a^2$ 即得。

## 正例与反例

- **正例（圆螺旋线）**：$\boldsymbol{r}(t)=(a\cos t,a\sin t,bt)$ 的挠率 $\tau=\frac{b}{a^2+b^2}$（常数，非零），所以它不是平面曲线。
- **反例（平面圆）**：圆 $\boldsymbol{r}(t)=(R\cos t,R\sin t,0)$ 的挠率 $\tau=0$，是平面曲线。

## 可直接引用的结论句示例

- "挠率 $\tau(s)=-\boldsymbol{\gamma}'(s)\cdot\boldsymbol{\beta}(s)$ 刻画曲线偏离平面曲线的程度，即'扭曲'的快慢。"
- "非直线的曲线是平面曲线当且仅当挠率恒为零。"
- "Frenet 公式把 Frenet 标架的运动写成以曲率、挠率为系数的反对称线性方程组，是曲线论最基本最重要的公式。"

## 哪些说法是过度承诺、不能写

- ❌ "挠率就是 $|\boldsymbol{\gamma}'|$"——不准确：$|\tau|=|\boldsymbol{\gamma}'|$，但 $\tau$ 本身带符号（$\tau=-\boldsymbol{\gamma}'\cdot\boldsymbol{\beta}$），符号有几何意义。
- ❌ "平面曲线就是挠率为零的曲线"——不准确：需排除直线（定理 4.1 假设曲线不是直线）；直线挠率未定义。
- ❌ "Frenet 公式的系数矩阵总是反对称"——准确说法是"沿曲线定义的任意单位正交标架场的导数公式系数矩阵都是反对称的"，Frenet 公式是特例。

## 迷你算例（数字从哪来）

**输入**：求圆螺旋线 $\boldsymbol{r}(t)=(a\cos t,a\sin t,bt)$ 的挠率。

**处理**：
1. $\boldsymbol{r}'(t)=(-a\sin t,a\cos t,b)$。
2. $\boldsymbol{r}''(t)=(-a\cos t,-a\sin t,0)$。
3. $\boldsymbol{r}'''(t)=(a\sin t,-a\cos t,0)$。
4. 混合积 $(\boldsymbol{r}',\boldsymbol{r}'',\boldsymbol{r}''')=\det\begin{pmatrix}-a\sin t&a\cos t&b\-a\cos t&-a\sin t&0\a\sin t&-a\cos t&0\end{pmatrix}$。计算得 $=a^2b$（可展开验证：第三列只有 $b$ 非零，故 $=b\cdot\det\begin{pmatrix}-a\cos t&-a\sin t\a\sin t&-a\cos t\end{pmatrix}=b(a^2\cos^2 t+a^2\sin^2 t)=a^2b$）。
5. 分母：$|\boldsymbol{r}'\times\boldsymbol{r}''|^2=(a\sqrt{a^2+b^2})^2=a^2(a^2+b^2)$（来自上一主题）。
6. 代入：$\tau=\frac{a^2b}{a^2(a^2+b^2)}=\frac{b}{a^2+b^2}$。

**结果**：$\tau=\frac{b}{a^2+b^2}$（常数）。当 $b=0$ 时 $\tau=0$，退化为平面圆。

## 延伸指引

- 前置：[[04 主题-曲线的曲率和Frenet标架]]（Frenet 标架）、[[Ch1 预备知识 - 讲解包/00 整体认知]]（混合积）。
- 深入：Frenet 公式在曲面论中推广为自然标架的运动公式（见 [[Ch5 曲面论基本定理 - 讲解包/00 整体认知]]）。
- 相关：反对称矩阵、常微分方程组（曲线论基本定理的证明工具）。

## 防跳跃（可能需要展开的概念点）

- 为什么 $\boldsymbol{\gamma}'\perp\boldsymbol{\alpha}$？（由 $\boldsymbol{\gamma}=\boldsymbol{\alpha}\times\boldsymbol{\beta}$ 与 $\boldsymbol{\alpha}'\parallel\boldsymbol{\beta}$ 推出）
- 为什么 $\boldsymbol{\beta}'$ 的系数 $b=0$？（因为 $\boldsymbol{\beta}$ 是单位向量，$\boldsymbol{\beta}'\perp\boldsymbol{\beta}$）
- 挠率的正负号有什么几何意义？（见 [[07 主题-曲线参数方程在一点的标准展开]]：$\tau_0>0$ 时曲线从下而上穿过密切平面）

## 核心洞察收束

> 挠率补全了曲率缺失的"扭转"信息，而 Frenet 公式把标架运动完整地写成由 $\kappa,\tau$ 决定的线性方程组——这正是曲线形状的全部局部信息。

## 自测题

1. （动机复述）挠率刻画什么？为什么用次法向量的变化率来定义？
2. 求圆螺旋线 $\boldsymbol{r}(t)=(a\cos t,a\sin t,bt)$ 的挠率。
3. （应用陷阱）有人说"平面曲线就是挠率为零的曲线"，这个说法哪里不严谨？
4. 为什么 Frenet 公式的系数矩阵是反对称的？
5. 定理 4.3 说平面曲线当且仅当混合积恒为零，这个判据和挠率公式有什么关系？

[[00 整体认知]] · 相邻主题：[[04 主题-曲线的曲率和Frenet标架]]、[[06 主题-曲线论基本定理]] · 方法：[[M-01 方法-活动标架法]]、[[M-02 方法-弧长参数化]]
