---
type: note
formal: true
subject: differential-geometry
created: 2026-09-03
updated: 2026-09-03
tags: [math, differential-geometry, teaching-pack]
---

# M-02 方法-Gauss方程与Codazzi方程

> 定位：这是本章的**相容性方法**——给出 I、II 必须满足的条件，也是存在性与内蕴性的关键。被 [[04 主题-曲面论基本方程]]、[[05 主题-曲面的存在性定理]]、[[06 主题-Gauss定理]] 共用。

## 方法是什么

**Gauss-Codazzi 方程**是曲面的第一、第二基本形式必须满足的**相容条件**。它们来自"$\pmb{r}_\alpha$ 和 $\pmb{n}$ 的二阶偏导数与求导次序无关"（混合偏导可交换）。

- **Gauss 方程**：$R_{1212}=b_{11}b_{22}-b_{12}^2$（实质 1 个独立方程）。
- **Codazzi 方程**：$\frac{\partial b_{\alpha\beta}}{\partial u^\gamma}-\frac{\partial b_{\alpha\gamma}}{\partial u^\beta}=\Gamma_{\alpha\gamma}^{\delta}b_{\delta\beta}-\Gamma_{\alpha\beta}^{\delta}b_{\delta\gamma}$（实质 2 个独立方程）。

## 为什么需要它（来龙）

- 任意给两个二次微分形式，它们不一定能成为某张曲面的 I、II——因为 I、II 来自同一张曲面，必然满足相容条件。
- 相容条件是存在性定理（[[05 主题-曲面的存在性定理]]）的充分条件，也是 Gauss 绝妙定理（[[06 主题-Gauss定理]]）的出发点。

## 方法主体

### 从运动公式到相容条件

自然标架运动公式（详见 [[M-01 方法-自然标架法]]）：

$$
\frac{\partial\pmb{r}_\alpha}{\partial u^\beta}=\Gamma_{\alpha\beta}^{\gamma}\pmb{r}_\gamma+b_{\alpha\beta}\pmb{n},\quad
\frac{\partial\pmb{n}}{\partial u^\beta}=-b_\beta^{\gamma}\pmb{r}_\gamma.
$$

正则曲面有三次以上连续偏导数，所以混合偏导可交换：

$$
\frac{\partial^2\pmb{r}_\alpha}{\partial u^\beta\partial u^\gamma}=\frac{\partial^2\pmb{r}_\alpha}{\partial u^\gamma\partial u^\beta},\quad
\frac{\partial^2\pmb{n}}{\partial u^\beta\partial u^\gamma}=\frac{\partial^2\pmb{n}}{\partial u^\gamma\partial u^\beta}.
$$

把运动公式代入，展开并利用 $\pmb{r}_1,\pmb{r}_2,\pmb{n}$ 线性无关，得到 Gauss 方程和 Codazzi 方程。

### Riemann 记号

$$
R_{\alpha\beta\gamma}^{\delta}=\frac{\partial\Gamma_{\alpha\beta}^{\delta}}{\partial u^\gamma}-\frac{\partial\Gamma_{\alpha\gamma}^{\delta}}{\partial u^\beta}+\Gamma_{\alpha\beta}^{\eta}\Gamma_{\eta\gamma}^{\delta}-\Gamma_{\alpha\gamma}^{\eta}\Gamma_{\eta\beta}^{\delta}.
$$

它只由第一类基本量 $g_{\alpha\beta}$ 及其不高于二阶的偏导数构成。利用对称性，Gauss 方程实质只有一个独立方程 $R_{1212}=b_{11}b_{22}-b_{12}^2$。

### 正交参数网下的简化

- 正交参数网（$F=0$）：$R_{1212}=-\sqrt{EG}\left(\left(\frac{(\sqrt{E})_v}{\sqrt{G}}\right)_v+\left(\frac{(\sqrt{G})_u}{\sqrt{E}}\right)_u\right)$。
- 正交曲率线网（$F=M=0$）：Codazzi 方程简化为 $\frac{\partial L}{\partial v}=H\frac{\partial E}{\partial v}$，$\frac{\partial N}{\partial u}=H\frac{\partial G}{\partial u}$，其中 $H$ 是平均曲率。

## 迷你算例：球面验证 Gauss 方程

**输入**：半径 $a$ 的球面，正交参数网。

**处理**：

1. 度量：$E=a^2$，$G=a^2\sin^2 u$，$F=0$。
2. 第二基本量：$L=a$，$N=a\sin^2 u$，$M=0$，所以 $b_{11}b_{22}-b_{12}^2=a^2\sin^2 u$。
3. 用公式算 $R_{1212}$：$\sqrt{E}=a$（对 $v$ 导数为 0），$\sqrt{G}=a\sin u$，$(\sqrt{G})_u=a\cos u$，$\frac{(\sqrt{G})_u}{\sqrt{E}}=\cos u$，再对 $u$ 求导得 $-\sin u$。所以 $R_{1212}=-\sqrt{a^2\cdot a^2\sin^2 u}\cdot(-\sin u)=a^2\sin^2 u$。

**结果**：$R_{1212}=a^2\sin^2 u=b_{11}b_{22}-b_{12}^2$，Gauss 方程成立。**数字从哪来**：左边由度量及其导数算出，右边由第二基本量相乘。

## 反例（方法边界）

- **不满足 Gauss 方程 ⇒ 不能成为曲面**：$\varphi=du^2+dv^2$，$\psi=du^2-dv^2$。$R_{1212}=0$ 但 $b_{11}b_{22}-b_{12}^2=-1\neq0$，Gauss 方程不成立。
- **只满足 Gauss 不满足 Codazzi 也不行**：相容条件必须同时满足两个方程。

## 去脉

- Gauss-Codazzi 方程是 [[05 主题-曲面的存在性定理]] 的充分条件（运动公式可积）。
- Gauss 方程本身推出 [[06 主题-Gauss定理]]：$K=R_{1212}/(g_{11}g_{22}-g_{12}^2)$ 只依赖 I，是保长不变量。

## 可直接引用的结论句（示例）

- "Gauss-Codazzi 方程是 I、II 必须满足的相容条件，来自混合偏导可交换。"
- "Gauss 方程实质 1 个、Codazzi 方程实质 2 个，共 3 个独立条件。"
- "满足 Gauss-Codazzi 方程是 I、II 能成为曲面的充要条件（配合存在性定理）。"

## 哪些说法是过度承诺（不能写）

- ❌ "Gauss-Codazzi 方程是三个完全独立的方程"——**错**，Gauss 实质 1 个、Codazzi 实质 2 个。
- ❌ "Riemann 记号依赖第二基本量"——**错**，只依赖第一类基本量。
- ❌ "满足 Gauss 方程就足够"——**错**，必须同时满足 Gauss 和 Codazzi。

## 延伸指引

- **深入方向**：Riemann 曲率张量的对称性与 Bianchi 恒等式；高维 Riemann 几何。
- **前置知识**：[[02 主题-自然标架的运动公式]]（Christoffel 记号）、[[04 主题-曲面论基本方程]]（推导细节）。
- **相关材料**：[[05 主题-曲面的存在性定理]]、[[06 主题-Gauss定理]]。

## 防跳跃（可能需要展开的概念点）

- Riemann 记号 $R_{\alpha\delta\beta\gamma}$ 的对称性（(3.17) 式）如何推出"Gauss 方程实质只有一个"。
- 为什么从 $\pmb{n}$ 的混合偏导得不到新的相容条件（等价于 Codazzi 方程）。
- 正交曲率线网下 Codazzi 方程的简化推导。

## 自测题

1. （动机复述）Gauss-Codazzi 方程解决什么问题？它从哪里来？
2. 对平面，验证 Gauss 方程成立（$R_{1212}=0$）。
3. （伪装成应用陷阱）有人说"只要 Gauss 方程成立，I、II 就能成为曲面"，对吗？为什么？
4. 为什么 Gauss 方程实质只有一个独立方程？利用 Riemann 记号对称性说明。
5. 球面 $R_{1212}=a^2\sin^2 u$ 是怎么算出来的？写出关键步骤。

[[00 整体认知]] · 被 [[04 主题-曲面论基本方程]]、[[05 主题-曲面的存在性定理]]、[[06 主题-Gauss定理]] 使用
