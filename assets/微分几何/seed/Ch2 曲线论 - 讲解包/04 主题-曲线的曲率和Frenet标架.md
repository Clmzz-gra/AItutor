---
type: note
formal: true
subject: differential-geometry
created: 2026-09-03
updated: 2026-09-03
tags: [math, differential-geometry, teaching-pack]
---

# 04 主题-曲线的曲率和 Frenet 标架

> 定位：引入第一个"弯曲不变量"——曲率，并建立随曲线运动的 Frenet 标架。方法详见 [[M-01 方法-活动标架法]]、[[M-02 方法-弧长参数化]]。

## 整体认知

曲率 $\kappa$ 刻画曲线在一点**偏离直线的程度**。为了描述"弯曲方向"，我们在曲线上每一点建立一个随曲线运动的正交标架——**Frenet 标架** $\{\boldsymbol{r}(s);\boldsymbol{\alpha}(s),\boldsymbol{\beta}(s),\boldsymbol{\gamma}(s)\}$，其中 $\boldsymbol{\alpha}$ 是单位切向量，$\boldsymbol{\beta}$ 是主法向量，$\boldsymbol{\gamma}$ 是次法向量。

## 来龙

- **类比已知**：圆有固定半径，半径越小弯曲越厉害；需要把"弯曲程度"推广到一般曲线。
- **解决新问题**：如何用不依赖坐标的量刻画曲线在一点偏离直线的程度？如何描述"朝哪个方向弯"？
- **理论需要**：Frenet 标架是后续挠率、Frenet 公式、基本定理的坐标系基础。

## 主体

### 定义：曲率

设曲线以弧长 $s$ 为参数，命 $\boldsymbol{\alpha}(s)=\boldsymbol{r}'(s)$（单位切向量）。定义

$$
\kappa(s)=\left|\frac{\mathrm{d}\boldsymbol{\alpha}}{\mathrm{d}s}\right|=|\boldsymbol{r}''(s)|,
$$

称 $\kappa(s)$ 为曲线在 $s$ 处的**曲率**（curvature，读作"曲率"），$\frac{\mathrm{d}\boldsymbol{\alpha}}{\mathrm{d}s}$ 称为**曲率向量**。

**几何意义（定理 3.1）**：设 $\Delta\theta$ 是切向量 $\boldsymbol{\alpha}(s+\Delta s)$ 与 $\boldsymbol{\alpha}(s)$ 的夹角，则

$$
\lim_{\Delta s\to 0}\left|\frac{\Delta\theta}{\Delta s}\right|=\left|\frac{\mathrm{d}\boldsymbol{\alpha}}{\mathrm{d}s}\right|=\kappa(s).
$$

即曲率是**单位切向量转动的快慢**。把单位切向量平移到原点，端点描出的曲线叫**切线像**（tangent indicatrix），其弧长元素为 $\mathrm{d}\tilde{s}=\kappa(s)\mathrm{d}s$，故 $\kappa(s)=\frac{\mathrm{d}\tilde{s}}{\mathrm{d}s}$。

### 定理 3.2：直线与曲率

曲线 $C$ 是直线当且仅当 $\kappa(s)\equiv 0$。

**因为**：直线 $\boldsymbol{r}(s)=\boldsymbol{r}_0+\boldsymbol{\alpha}_0 s$ 有 $\boldsymbol{r}''(s)=0$，故 $\kappa\equiv 0$；反之 $\kappa\equiv 0$ 蕴涵 $\boldsymbol{r}''(s)=0$，积分两次得直线。

### 定义：Frenet 标架

因为 $|\boldsymbol{\alpha}(s)|=1$，故 $\boldsymbol{\alpha}(s)\perp\boldsymbol{\alpha}'(s)$，即 $\boldsymbol{\alpha}'(s)$ 是法向量。若 $\kappa(s)\neq 0$，则 $\boldsymbol{\alpha}'(s)$ 有确定方向，其单位向量

$$
\boldsymbol{\beta}(s)=\frac{\boldsymbol{\alpha}'(s)}{|\boldsymbol{\alpha}'(s)|}=\frac{\boldsymbol{r}''(s)}{|\boldsymbol{r}''(s)|}
$$

称为**主法向量**（principal normal）。于是 $\boldsymbol{\alpha}'(s)=\kappa(s)\boldsymbol{\beta}(s)$。再定义

$$
\boldsymbol{\gamma}(s)=\boldsymbol{\alpha}(s)\times\boldsymbol{\beta}(s),
$$

称为**次法向量**（binormal）。这样，在 $\kappa(s)\neq 0$ 的点有完全确定的**右手单位正交标架** $\{\boldsymbol{r}(s);\boldsymbol{\alpha}(s),\boldsymbol{\beta}(s),\boldsymbol{\gamma}(s)\}$，称为曲线在该点的 **Frenet 标架**（Frenet frame，读作"弗勒内标架"）。它与坐标系选取无关，也不受保持定向的容许参数变换影响。

**注意**：在 $\kappa(s)=0$ 的点，Frenet 标架没有定义。若在一段区间内 $\kappa\equiv 0$，则曲线段是直线，可人为取两个正交法向量作标架；若 $\kappa$ 有孤立零点，标架能否延拓取决于两侧极限是否相同。

### 三个坐标面

Frenet 标架的三根轴分别称为**切线、主法线、次法线**；三个坐标面为：

- **法平面**（以 $\boldsymbol{\alpha}$ 为法向）：$(\boldsymbol{X}-\boldsymbol{r}(s))\cdot\boldsymbol{\alpha}(s)=0$；
- **从切平面**（以 $\boldsymbol{\beta}$ 为法向）：$(\boldsymbol{X}-\boldsymbol{r}(s))\cdot\boldsymbol{\beta}(s)=0$；
- **密切平面**（以 $\boldsymbol{\gamma}$ 为法向）：$(\boldsymbol{X}-\boldsymbol{r}(s))\cdot\boldsymbol{\gamma}(s)=0$。

### 一般参数 t 下的计算公式

若 $\boldsymbol{r}=\boldsymbol{r}(t)$，$t$ 不是弧长参数，则

$$
\kappa(t)=\frac{|\boldsymbol{r}'(t)\times\boldsymbol{r}''(t)|}{|\boldsymbol{r}'(t)|^3},\quad
\boldsymbol{\gamma}(t)=\frac{\boldsymbol{r}'(t)\times\boldsymbol{r}''(t)}{|\boldsymbol{r}'(t)\times\boldsymbol{r}''(t)|},\quad
\boldsymbol{\beta}(t)=\boldsymbol{\gamma}(t)\times\boldsymbol{\alpha}(t).
$$

**因为**：$\boldsymbol{r}'(t)=|\boldsymbol{r}'(t)|\boldsymbol{\alpha}(t)$，再求导并利用 $\boldsymbol{\alpha}'=\kappa\boldsymbol{\beta}$ 与 $\frac{\mathrm{d}s}{\mathrm{d}t}=|\boldsymbol{r}'|$，可得 $\boldsymbol{r}'\times\boldsymbol{r}''=|\boldsymbol{r}'|^3\kappa\boldsymbol{\gamma}$，从而推出上述公式。

## 正例与反例

- **正例（圆螺旋线）**：$\boldsymbol{r}(t)=(a\cos t,a\sin t,bt)$，$a>0$。计算得 $\kappa(t)=\frac{a}{a^2+b^2}$（常数），Frenet 标架为 $\boldsymbol{\alpha}=(-\frac{a}{\sqrt{a^2+b^2}}\sin t,\frac{a}{\sqrt{a^2+b^2}}\cos t,\frac{b}{\sqrt{a^2+b^2}})$，$\boldsymbol{\gamma}=(\frac{b}{\sqrt{a^2+b^2}}\sin t,-\frac{b}{\sqrt{a^2+b^2}}\cos t,\frac{a}{\sqrt{a^2+b^2}})$，$\boldsymbol{\beta}=(-\cos t,-\sin t,0)$。
- **反例（直线）**：直线 $\kappa\equiv 0$，此时主法向量 $\boldsymbol{\beta}$ 未定义，Frenet 标架不存在（需单独处理退化情形）。

## 可直接引用的结论句示例

- "曲率 $\kappa(s)=|\boldsymbol{r}''(s)|$ 是单位切向量随弧长转动的快慢，刻画曲线偏离直线的程度。"
- "曲线是直线当且仅当曲率恒为零；半径为 $R$ 的圆曲率为 $1/R$。"
- "Frenet 标架 $\{\boldsymbol{r};\boldsymbol{\alpha},\boldsymbol{\beta},\boldsymbol{\gamma}\}$ 是随曲线运动的右手单位正交标架，在 $\kappa\neq 0$ 处完全确定。"

## 哪些说法是过度承诺、不能写

- ❌ "Frenet 标架在曲线上处处有定义"——不准确：在 $\kappa=0$ 处未定义，需单独处理。
- ❌ "曲率越大曲线越弯"——基本对，但严格说曲率是"单位切向量转动的快慢"，对直线为 0、对圆为 $1/R$。
- ❌ "曲率与参数选择无关"——不准确：曲率作为几何量确实与参数无关，但**计算公式**依赖参数；用弧长参数最简洁。

## 迷你算例（数字从哪来）

**输入**：求圆螺旋线 $\boldsymbol{r}(t)=(a\cos t,a\sin t,bt)$ 的曲率。

**处理**：
1. $\boldsymbol{r}'(t)=(-a\sin t,a\cos t,b)$，$|\boldsymbol{r}'|=\sqrt{a^2+b^2}$。
2. $\boldsymbol{r}''(t)=(-a\cos t,-a\sin t,0)$。
3. 叉乘：$\boldsymbol{r}'\times\boldsymbol{r}''=(ab\sin t,-ab\cos t,a^2)$，其长度 $=\sqrt{a^2b^2(\sin^2+\cos^2)+a^4}=\sqrt{a^2b^2+a^4}=a\sqrt{a^2+b^2}$。
4. 代入公式：$\kappa=\frac{|\boldsymbol{r}'\times\boldsymbol{r}''|}{|\boldsymbol{r}'|^3}=\frac{a\sqrt{a^2+b^2}}{(a^2+b^2)^{3/2}}=\frac{a}{a^2+b^2}$。

**结果**：$\kappa=\frac{a}{a^2+b^2}$（常数）。当 $b=0$ 时退化为圆，$\kappa=\frac{1}{a}$，符合"半径为 $a$ 的圆曲率为 $1/a$"。

## 延伸指引

- 前置：[[03 主题-曲线的弧长]]（弧长参数）、[[Ch1 预备知识 - 讲解包/00 整体认知]]（叉乘、标架）。
- 深入：曲率在曲面论中推广为法曲率、Gauss 曲率；在黎曼几何中推广为截面曲率。
- 相关：Schmidt 正交化（Frenet 标架可由 $\{\boldsymbol{r}',\boldsymbol{r}'',\boldsymbol{r}'''\}$ 正交化得到）。

## 防跳跃（可能需要展开的概念点）

- 为什么 $|\boldsymbol{\alpha}|=1$ 推出 $\boldsymbol{\alpha}\perp\boldsymbol{\alpha}'$？（对 $\boldsymbol{\alpha}\cdot\boldsymbol{\alpha}=1$ 求导）
- 为什么 $\kappa=0$ 时主法向量未定义？
- 什么是"切线像"？为什么它的弧长元素是 $\kappa\,\mathrm{d}s$？

## 核心洞察收束

> 曲率把"弯曲的快慢"翻译成单位切向量的变化率，而 Frenet 标架把"朝哪个方向弯"翻译成一个随曲线运动的正交坐标系。

## 自测题

1. （动机复述）曲率刻画什么？为什么用单位切向量的变化率来定义？
2. 求圆 $\boldsymbol{r}(t)=(R\cos t,R\sin t)$ 的曲率。
3. （应用陷阱）有人说"Frenet 标架在曲线上处处有定义"，这个说法哪里不对？
4. 为什么直线是 $\kappa\equiv 0$ 的曲线？反过来成立吗？
5. 圆螺旋线 $\boldsymbol{r}(t)=(a\cos t,a\sin t,bt)$ 的曲率是多少？当 $b=0$ 时退化成什么？

[[00 整体认知]] · 相邻主题：[[03 主题-曲线的弧长]]、[[05 主题-曲线的挠率和Frenet公式]] · 方法：[[M-01 方法-活动标架法]]、[[M-02 方法-弧长参数化]]
