---
type: 节
formal: true
subject: 实变函数与泛函分析
created: 2026-09-21
updated: 2026-09-21
tags: [math, 实变函数与泛函分析]
chapter: 5
section: 5.2
---

# Sec5.2 Hilbert 空间理论

> 定位：在距离之上再加一层**内积**，于是"长度、夹角、正交、投影"这些欧氏几何的概念在无穷维全部复活；本节证明这些几何在完备性支撑下完全成立，并给出两个"表示"结论——傅里叶展开与 Riesz 表示定理。
> 教材：郭懋正《实变函数与泛函分析》§5.2（p.223–239）
> 来源：旧讲解包《Ch9 内积空间和希尔伯特空间》§1–§4；郭版教材 §5.2.1–§5.2.3

> [!info] 关联笔记
> - 父级：[[Ch5 Hilbert 空间理论]]
> - 前置：[[Sec5.1 距离空间]] ｜ 后续：[[Sec5.3 Hilbert 空间上的算子]]
> - 概念：[[概念-正交投影]] [[概念-对偶空间]] [[概念-完备性]]

---

## 来龙（为什么需要它）

- **类比已知**：$\mathbb{R}^n$ 的全部几何——长度、夹角、正交、投影、坐标分解——都建立在**内积** $\langle x,y\rangle=\sum_i x_i\bar y_i$ 上。距离只保留"远近"，丢掉了"方向"；要拿回几何，必须把内积加回来。
- **解决新问题**：古典傅里叶级数 $f\sim\sum(a_n\cos nx+b_n\sin nx)$ 一直在问三个问题——系数怎么定？级数收敛到 $f$ 吗？在什么意义下收敛？**光有距离空间答不了**：它没有正交概念，无法谈"把 $f$ 分解成互相垂直的分量"。
- **理论/应用需要**：
  - **最佳逼近**（最小二乘、信号压缩）需要一个"最近点"定理，而这正是投影定理；
  - **连续线性泛函的表示**（本章 §5.2.3）需要内积把抽象泛函变成具体向量；
  - 量子力学的状态空间就是 Hilbert 空间，可观测量 = 自伴算子（§5.3）。

> **本章的位置**：$L^2$ 空间（Ch4 §4.2）是本节最典型的例子，它的内积与正交性归 Ch4；本节只写**一般 Hilbert 空间**的理论，$L^2$ 的具体计算请回 Ch4 §4.2。

---

## 主体（核心内容）

### 5.2.1 定义

**定义（内积空间）**：设 $X$ 是复线性空间，对任意 $x,y\in X$ 对应一个复数 $\langle x,y\rangle$（读作"$x$ 与 $y$ 的内积"），满足：

1. **正定性**：$\langle x,x\rangle\geqslant0$，且 $\langle x,x\rangle=0\iff x=0$；
2. **对第一变元线性**：$\langle\alpha x+\beta y,z\rangle=\alpha\langle x,z\rangle+\beta\langle y,z\rangle$；
3. **共轭对称**：$\langle x,y\rangle=\overline{\langle y,x\rangle}$（$\overline{\ \cdot\ }$ 读作"复共轭"；实空间时即对称性 $\langle x,y\rangle=\langle y,x\rangle$）。

称 $(X,\langle\cdot,\cdot\rangle)$ 为**内积空间**（实空间时也称**欧氏空间**）。

由 2、3 立即推出**对第二变元共轭线性**：
$$\langle x,\alpha y+\beta z\rangle=\bar\alpha\langle x,y\rangle+\bar\beta\langle x,z\rangle.$$
这两条合称**共轭双线性性**。**注意**：把 1 中的"正定"放宽为非负定 $\langle x,x\rangle\geqslant0$，得到的叫**半内积**，对应空间称**半内积空间**——那时 $\langle x,x\rangle=0$ 不再蕴含 $x=0$。

**定义（导出范数）**：$\|x\|=\sqrt{\langle x,x\rangle}$（读作"$x$ 的范数"）。

**定理（Schwarz 不等式，一切估计的起点）**：$|\langle x,y\rangle|\leqslant\|x\|\,\|y\|$，且等号成立 $\iff x,y$ **线性相关**。

**证明**：$y=0$ 时平凡。$y\neq0$ 时，*因为* 内积正定，对任意复数 $\alpha$ 有
$$0\leqslant\langle x-\alpha y,x-\alpha y\rangle=\|x\|^2-\bar\alpha\langle x,y\rangle-\alpha\bigl[\langle y,x\rangle-\bar\alpha\|y\|^2\bigr].$$
取 $\bar\alpha=\dfrac{\langle y,x\rangle}{\|y\|^2}$ 使方括号为 $0$（*因为* $\|y\|\neq0$，这个 $\alpha$ 合法），得
$$0\leqslant\|x\|^2-\frac{|\langle x,y\rangle|^2}{\|y\|^2},$$
移项开方即得。$\square$

**推论（三角不等式由此推出）**：*因为* $\langle x,y\rangle+\overline{\langle x,y\rangle}=2\operatorname{Re}\langle x,y\rangle\leqslant2|\langle x,y\rangle|$，
$$\|x+y\|^2=\|x\|^2+\langle x,y\rangle+\overline{\langle x,y\rangle}+\|y\|^2\leqslant\|x\|^2+2\|x\|\|y\|+\|y\|^2=(\|x\|+\|y\|)^2.$$
所以内积空间按导出范数自动是距离空间。

**定理（内积的连续性）**：*因为* Schwarz 不等式，$x_n\to x,\ y_n\to y\Rightarrow\langle x_n,y_n\rangle\to\langle x,y\rangle$。

**证明**：把差拆成两项
$$|\langle x_n,y_n\rangle-\langle x,y\rangle|\leqslant|\langle x_n-x,y_n\rangle|+|\langle x,y_n-y\rangle|\leqslant\|x_n-x\|\,\|y_n\|+\|x\|\,\|y_n-y\|.$$
*因为* 收敛列有界，$\|y_n\|\leqslant K$，右端 $\to0$。$\square$

**定义（Hilbert 空间）**：按导出范数**完备**的内积空间称为 **Hilbert 空间**（希尔伯特空间）。

**四个标准例子**：

| 空间 | 内积 | 是不是 Hilbert 空间 | 理由 |
|---|---|---|---|
| $L^2[a,b]$ | $\langle x,y\rangle=\int_a^b x(t)\overline{y(t)}\,\mathrm dt$ | **是** | 导出范数就是 $\|x\|_2$；$L^2$ 完备已在 Ch4 §4.1 证明 |
| $l^2$ | $\langle x,y\rangle=\sum_{i}\xi_i\bar\eta_i$ | **是** | 同上（$l^2$ 就是 $L^2$ 的离散版） |
| $L^p$（$p\neq2$） | —— | **不是内积空间** | 平行四边形公式不成立（见下） |
| $C[a,b]$ 配 $\max$ 范数 | —— | **不是内积空间** | 同上 |

**反例（$L^p$，$p\neq2$，不是内积空间）**：取 $x=(1,1,0,\dots)$、$y=(1,-1,0,\dots)\in l^p$。*因为* $\|x\|=\|y\|=2^{1/p}$，而 $x+y=(2,0,\dots)$、$x-y=(0,2,\dots)$ 给出 $\|x+y\|=\|x-y\|=2$，于是
$$\|x+y\|^2+\|x-y\|^2=8\neq4\cdot2^{2/p}=2(\|x\|^2+\|y\|^2)\quad(p\neq2),$$
**平行四边形公式不成立**。

**反例（$C[a,b]$ 配 $\max$ 范数，不是内积空间）**：取 $x(t)\equiv1$、$y(t)=\dfrac{t-a}{b-a}$，则 $\|x\|=\|y\|=1$、$\|x+y\|=2$、$\|x-y\|=1$，于是
$$\|x+y\|^2+\|x-y\|^2=5\neq4=2(\|x\|^2+\|y\|^2).$$

> **停顿自问**：为什么 $p=2$ 如此特殊？——*因为* $\|x\|_2^2=\sum_i|x_i|^2$ 能展开成交叉项 $\sum_i x_i\bar y_i$（即存在对应的共轭双线性形式），而一般 $p$ 范数没有；平行四边形公式把这一点**检测**了出来。

**定理（平行四边形公式，内积范数的特征）**：对一切 $x,y$，
$$\|x+y\|^2+\|x-y\|^2=2(\|x\|^2+\|y\|^2).$$
**证明**：*因为* 内积对第一变元线性、对第二变元共轭线性，
$$\|x+y\|^2=\|x\|^2+\langle x,y\rangle+\langle y,x\rangle+\|y\|^2,\qquad\|x-y\|^2=\|x\|^2-\langle x,y\rangle-\langle y,x\rangle+\|y\|^2,$$
两式相加即得。几何意义：平行四边形两条对角线长的平方和等于四条边长平方和。$\square$

**定理（极化恒等式，逆命题）**：若赋范线性空间对一切 $x,y$ 满足平行四边形公式，则可用
$$\langle x,y\rangle=\frac14\left(\|x+y\|^2-\|x-y\|^2+\mathrm i\|x+\mathrm iy\|^2-\mathrm i\|x-\mathrm iy\|^2\right)$$
定义内积（**实**空间去掉后两项），且该内积导出的范数就是原来的范数。

> **用途**：判定一个赋范空间是否可能来自内积，**只需检验平行四边形公式**。这是"$L^p$ 只在 $p=2$ 时是 Hilbert 空间"的完整答案。

### 5.2.2 正交性

**定义（正交）**：$\langle x,y\rangle=0$ 记作 $x\perp y$（读作"$x$ 正交于 $y$"）；$A\perp B$ 指 $A$ 中每个向量与 $B$ 中每个向量正交。**勾股公式**：$x\perp y\Rightarrow\|x+y\|^2=\|x\|^2+\|y\|^2$。

**定义（正交补）**：$M^\perp=\{x\in X:x\perp M\}$，读作"$M$ 的正交补"。**性质**：$M^\perp$ 是**闭**线性子空间（*因为* 内积连续，正交关系取极限后保持）；$M\cap M^\perp=\{0\}$。

**定义（点到集合的距离、凸集）**：$d(x,M)=\inf_{y\in M}\|x-y\|$；若 $x,y\in M$ 蕴含线段 $[x,y]=\{\alpha x+(1-\alpha)y:0\leqslant\alpha\leqslant1\}\subset M$，称 $M$ 是**凸集**。

**定理（极小化向量定理）**：$X$ 是内积空间，$M$ 是 $X$ 的**非空凸**子集且按导出距离**完备**，则对每个 $x\in X$ 存在**唯一**的 $y\in M$ 使 $\|x-y\|=d(x,M)$。

**证明（平行四边形公式的第一次实战）**：记 $\delta=d(x,M)$，取 $y_n\in M$ 使 $\|x-y_n\|\to\delta$。令 $v_n=y_n-x$，则 $\|v_n\|\to\delta$，且 *因为* $M$ 凸，$\dfrac{y_n+y_m}{2}\in M$，故
$$\|v_n+v_m\|=2\left\|\frac{y_n+y_m}{2}-x\right\|\geqslant2\delta.$$
由平行四边形公式，
$$\|y_n-y_m\|^2=\|v_n-v_m\|^2=-\|v_n+v_m\|^2+2(\|v_n\|^2+\|v_m\|^2)\leqslant-4\delta^2+2(\|v_n\|^2+\|v_m\|^2)\to0.$$
故 $\{y_n\}$ 是 $M$ 中柯西列；*因为* $M$ 完备，存在 $y\in M$ 使 $y_n\to y$，且由范数连续得 $\|x-y\|=\delta$。
**唯一性**：若 $y_0$ 也是最近点，*因为* $\dfrac{y+y_0}{2}\in M$，
$$0\leqslant\|y-y_0\|^2=2\delta^2+2\delta^2-4\left\|\frac{y+y_0}{2}-x\right\|^2\leqslant4\delta^2-4\delta^2=0,$$
故 $y=y_0$。$\square$

**引理（最近点自动垂直）**：若 $y\in M$ 是 $x$ 在子空间 $M$ 上的最近点，则 $x-y\perp M$。

**证明（反证）**：若存在 $y_1\in M$ 使 $\langle x-y,y_1\rangle\neq0$，取 $\bar\alpha=\dfrac{\langle y_1,x-y\rangle}{\|y_1\|^2}$（*因为* $y_1\neq0$，合法），则
$$\|(x-y)-\alpha y_1\|^2=\|x-y\|^2-\frac{|\langle x-y,y_1\rangle|^2}{\|y_1\|^2}<d(x,M)^2.$$
但 $(x-y)-\alpha y_1=x-(y+\alpha y_1)$，且 *因为* $M$ 是子空间，$y+\alpha y_1\in M$——这与 $d(x,M)$ 是下确界矛盾。$\square$

**定理（投影定理，全章几何核心）**：设 $Y$ 是 Hilbert 空间 $X$ 的**闭**子空间，则
$$X=Y\oplus Y^\perp,$$
即每个 $x\in X$ 可**唯一**分解为 $x=y+z$，其中 $y\in Y$、$z\in Y^\perp$。

**证明**：*因为* $Y$ 闭且 $X$ 完备，由子空间完备判据 $Y$ 完备，从而 $Y$ 是非空凸完备集；由极小化向量定理得最近点 $y$，由引理得 $z=x-y\perp Y$。唯一性来自 $Y\cap Y^\perp=\{0\}$。$\square$

**定义（投影算子）**：$Px=y$（$y$ 是 $x$ 在 $Y$ 上的投影）。**性质**：$P$ 有界线性，$\|P\|=1$（$Y\neq\{0\}$）；$PX=Y$，$PY^\perp=\{0\}$；$P^2=P$。更细的性质见 §5.3.3。

**两个重要推论**：

- **$Y=Y^{\perp\perp}$**（$Y$ 闭时）：用投影定理把 $x\in Y^{\perp\perp}$ 分解为 $y+z$，*因为* $x\perp Y^\perp$ 且 $z\in Y^\perp$，得 $\|z\|^2=\langle z,z\rangle=\langle x-y,z\rangle=0$，故 $x=y\in Y$。
- **稠密判据**：$\overline{\operatorname{span}M}=X\iff M^\perp=\{0\}$（$\operatorname{span}M$ 读作"$M$ 张成的线性包"）。它把"张成的线性空间是否稠密"翻译成"是否只有零向量与 $M$ 正交"。

> **核心事实**：投影定理把有限维的正交分解搬到无穷维，但要两个条件：**$Y$ 闭**、**空间完备**。它同时解决三件事：最近点存在唯一、差向量垂直、空间直和分解。

**定义（正交系 / 规范正交系）**：不含零向量的集合 $M$，若其中向量**两两正交**，称 $M$ 为**正交系**；若每个向量范数都是 $1$，称 $M$ 为**规范正交系**（旧讲解包中称"完全规范正交系"的前半，英文 orthonormal system，有时译作**标准正交系**）。

**两条基本性质**：

1. **勾股公式推广**：对正交系中任意有限个 $x_i$，$\left\|\sum_i x_i\right\|^2=\sum_i\|x_i\|^2$（*因为* 交叉项全为 $0$）。
2. **正交系线性无关**：若 $\sum_i\alpha_i x_i=0$，与 $x_j$ 作内积得 $\alpha_j\|x_j\|^2=0$，*因为* $\|x_j\|\neq0$ 故 $\alpha_j=0$。

**例**：$\mathbb{R}^n$ 的坐标向量 $e_k$；$L^2[0,2\pi]$ 中的三角函数系
$$\frac{1}{\sqrt2},\ \cos x,\ \sin x,\ \cos 2x,\ \sin 2x,\ \dots$$
（内积取 $\dfrac1\pi\int_0^{2\pi}f g\,\mathrm dx$ 时它们范数全为 $1$）。

**定义（傅里叶系数）**：$\langle x,e\rangle$（$e\in M$，$M$ 是规范正交系）称为 $x$ 关于 $M$ 的**傅里叶系数**（读作"$x$ 在 $e$ 方向上的分量"）。对 $L^2[0,2\pi]$ 的三角函数系，它们就是通常的傅里叶系数 $a_n,b_n$。

**引理（最佳逼近：傅里叶系数就是最优系数）**：

1. $\left\|x-\sum_{i=1}^n\langle x,e_i\rangle e_i\right\|^2=\|x\|^2-\sum_{i=1}^n|\langle x,e_i\rangle|^2$；
2. 在所有复数 $\alpha_i$ 中，取 $\alpha_i=\langle x,e_i\rangle$ 使 $\left\|x-\sum_i\alpha_i e_i\right\|$ **最小**，且
   $$\left\|x-\sum_i\alpha_i e_i\right\|^2=\left\|x-\sum_i\langle x,e_i\rangle e_i\right\|^2+\sum_{i=1}^n|\alpha_i-\langle x,e_i\rangle|^2.$$

**证明**：把 $x-\sum\alpha_i e_i$ 拆成 $\left(x-\sum\langle x,e_i\rangle e_i\right)+\sum\left(\langle x,e_i\rangle-\alpha_i\right)e_i$。*因为* 第一项与每个 $e_i$ 正交（直接计算内积），两项正交，由勾股公式得第二式的形式；*因为* 第二项非负，最小值在 $\alpha_i=\langle x,e_i\rangle$ 处取得，此时第二项为 $0$ 即得第一式。$\square$

**读法**：用 $e_1,\dots,e_n$ 的线性组合逼近 $x$，**最佳系数就是傅里叶系数**——"投影 = 傅里叶截断"。这就是**最小二乘法**的几何本质。

**定理（Bessel 不等式）**：$\sum_i|\langle x,e_i\rangle|^2\leqslant\|x\|^2$（对任意规范正交系，含无穷情形）。

**证明**：*因为* 引理中左边 $\geqslant0$，$\sum_{i=1}^n|\langle x,e_i\rangle|^2\leqslant\|x\|^2$ 对一切 $n$ 成立，令 $n\to\infty$ 即得。$\square$

**推论（Riemann–Lebesgue 引理）**：$\langle x,e_n\rangle\to0$——*因为* 收敛级数的通项趋于 $0$。

**引理（级数收敛判据）**：在 Hilbert 空间中，$\sum_i\alpha_i e_i$ 收敛 $\iff\sum_i|\alpha_i|^2<\infty$。

**证明**：*因为* $\|S_n-S_m\|^2=\sum_{i=m+1}^n|\alpha_i|^2$（正交性消去交叉项），部分和是柯西列 $\iff$ 数值级数 $\sum|\alpha_i|^2$ 收敛。$\square$

**定义（完全规范正交系）**：规范正交系 $M$ 若满足 $\overline{\operatorname{span}M}=X$，称 $M$ 是**完全**的（也叫**完全正交系**，旧讲解包作"完全规范正交系"，郭版亦称**标准正交基**）。

**定理（完全的三个等价刻画）**：

1. $M$ 完全 $\iff M^\perp=\{0\}$（用稠密判据）；
2. $M$ 完全 $\iff$ 对所有 $x\in X$ 成立 **Parseval 等式**（帕塞瓦尔等式）$\displaystyle\sum_{e\in M}|\langle x,e\rangle|^2=\|x\|^2$；
3. $M$ 完全时，每个 $x\in X$ 有**傅里叶展开**
   $$x=\sum_{e\in M}\langle x,e\rangle e,\qquad \|x\|^2=\sum_{e\in M}|\langle x,e\rangle|^2.$$

**展开的证明**：先证级数收敛（*因为* Bessel 不等式给出 $\sum|\langle x,e\rangle|^2\leqslant\|x\|^2<\infty$，由级数收敛判据即得）；再令 $y=\sum_e\langle x,e\rangle e$，*因为* 对每个 $e_0\in M$，
$$\langle x-y,e_0\rangle=\langle x,e_0\rangle-\langle x,e_0\rangle=0,$$
得 $x-y\perp M$；*因为* $M$ 完全即 $M^\perp=\{0\}$，故 $x=y$。$\square$

**例**：三角函数系是 $L^2[0,2\pi]$ 的完全规范正交系，故每个 $f\in L^2[0,2\pi]$ 都可展开成傅里叶级数；但等式必须理解为 **$L^2$ 意义（平方平均）收敛**——**不是**逐点收敛，更不是一致收敛。这是古典傅里叶分析在 Hilbert 空间框架下的完整形式。

**反例（正交系可以不完全）**：在 $L^2[-\pi,\pi]$ 中只取 $\{\cos nx\}_{n\geqslant1}$。*因为* 任何奇函数（如 $\sin x$）与每个 $\cos nx$ 都正交，$M^\perp\neq\{0\}$，故 $M$ 不完全；相应地 Bessel 不等式取严格不等号，Parseval 等式不成立。**"正交"不等于"完全"——完全性要求这个系"撑满"整个空间。**

**Gram–Schmidt 正交化过程**（把线性无关列 $\{x_n\}$ 变成规范正交系）：
$$e_1=\frac{x_1}{\|x_1\|},\qquad v_n=x_n-\sum_{k=1}^{n-1}\langle x_n,e_k\rangle e_k,\qquad e_n=\frac{v_n}{\|v_n\|}.$$
其中 $\sum_{k=1}^{n-1}\langle x_n,e_k\rangle e_k$ 正是 $x_n$ 在 $\operatorname{span}\{x_1,\dots,x_{n-1}\}$ 上的**投影**（*因为* 最佳逼近引理），$v_n$ 是"扣掉已有方向后剩下的新方向"。

**定理（完全正交系的存在性）**：每个非零 Hilbert 空间都有完全规范正交系。（**可分**情形：对可数稠密集作 Gram–Schmidt 即得**可数**完全规范正交系。）

**定理（分类定理：可分 Hilbert 空间同构于 $l^2$）**：两个 Hilbert 空间**同构**（指存在保内积的线性到上映射）$\iff$ 它们的 **Hilbert 维数**（完全规范正交系的基数）相同。**推论**：可分 Hilbert 空间必与某个 $\mathbb{R}^n$（$\mathbb{C}^n$）或 $l^2$ 同构。

**读法**：无穷维可分 Hilbert 空间**只有一个模型**——$l^2$。$L^2[0,2\pi]$ 与 $l^2$ 同构，傅里叶展开就是这个同构的具体写法（函数 $\leftrightarrow$ 它的傅里叶系数列）。

> **核心事实**：规范正交系把"函数"翻译成"坐标"（傅里叶系数），把无穷维几何翻译成可数坐标运算；**Parseval 等式 = 坐标变换保长度**。Hilbert 空间因此是"最像 $\mathbb{R}^n$ 的无穷维空间"。

**例题**：在 $L^2[-1,1]$ 中把 $f(t)=t^2$ 关于规范正交系 $e_0=\dfrac{1}{\sqrt2}$、$e_1=\sqrt{\dfrac32}\,t$ 作最佳逼近，并求最佳逼近的平方误差。

- **原始信息**：内积 $\langle f,g\rangle=\int_{-1}^1 f(t)g(t)\,\mathrm dt$。先验证 $\{e_0,e_1\}$ 确实是规范正交系：$\|e_0\|^2=\int_{-1}^1\frac12\,\mathrm dt=1$；$\|e_1\|^2=\frac32\int_{-1}^1t^2\,\mathrm dt=\frac32\cdot\frac23=1$；$\langle e_0,e_1\rangle=\frac{\sqrt3}{\sqrt2}\int_{-1}^1t\,\mathrm dt=0$（*因为* 被积函数是奇函数）。
- **代入（算傅里叶系数）**：
  $$\langle f,e_0\rangle=\frac{1}{\sqrt2}\int_{-1}^1t^2\,\mathrm dt=\frac{1}{\sqrt2}\cdot\frac23=\frac{2}{3\sqrt2},\qquad \langle f,e_1\rangle=\sqrt{\frac32}\int_{-1}^1t^3\,\mathrm dt=0$$
  （第二个为 $0$，*因为* $t^3$ 是奇函数）。
- **结果（最佳逼近）**：由最佳逼近引理，最优系数就是傅里叶系数，故最佳逼近为
  $$p(t)=\frac{2}{3\sqrt2}\cdot\frac{1}{\sqrt2}=\frac13,$$
  平方误差为
  $$\left\|f-p\right\|^2=\|f\|^2-|\langle f,e_0\rangle|^2-|\langle f,e_1\rangle|^2=\int_{-1}^1t^4\,\mathrm dt-\frac{4}{18}=\frac25-\frac29=\frac{8}{45}\approx0.178.$$
- **结论**：$t^2$ 在 $\operatorname{span}\{1,t\}$ 上的最佳逼近是**常数 $\tfrac13$**，残差 $8/45$；*因为* 残差不为 $0$ 且 $t^2\notin\operatorname{span}\{1,t\}$，说明 $\{e_0,e_1\}$ 在这个空间里不构成完全系——若加入 Legendre 多项式 $e_2=\sqrt{\tfrac58}(3t^2-1)$，残差将降为 $0$。

### 5.2.3 Riesz 表示定理

**定理（Riesz 表示定理）**：设 $X$ 是 Hilbert 空间，$f$ 是 $X$ 上的**连续线性泛函**。则存在**唯一**的 $z\in X$，使
$$f(x)=\langle x,z\rangle\quad(\forall x\in X),\qquad \|f\|=\|z\|.$$

**证明（三个关键动作）**：

1. **猜位置**。$f=0$ 时取 $z=0$ 即可。$f\neq0$ 时，若这样的 $z$ 存在，则对 $x\in\mathcal N(f)$（$\mathcal N(f)$ 读作"$f$ 的零空间"）有 $\langle x,z\rangle=f(x)=0$，即 $z\in\mathcal N(f)^\perp$。*因为* $f$ 连续，$\mathcal N(f)=f^{-1}(\{0\})$ 是闭集的**原像**，由连续映射的闭集判据它是闭子空间；又 *因为* $f\neq0$ 即 $\mathcal N(f)\neq X$，由投影定理 $\mathcal N(f)^\perp\neq\{0\}$，取 $z_0\in\mathcal N(f)^\perp$、$z_0\neq0$。
2. **构造 $z$**。对任意 $x\in X$，令 $v=f(x)z_0-f(z_0)x$。*因为* $f$ 线性，$f(v)=f(x)f(z_0)-f(z_0)f(x)=0$，即 $v\in\mathcal N(f)$；于是 *因为* $z_0\perp\mathcal N(f)$，
   $$0=\langle v,z_0\rangle=f(x)\|z_0\|^2-f(z_0)\langle x,z_0\rangle.$$
   解出
   $$f(x)=\left\langle x,\ \frac{\overline{f(z_0)}}{\|z_0\|^2}z_0\right\rangle,$$
   即 $z=\dfrac{\overline{f(z_0)}}{\|z_0\|^2}z_0$。（**注意复共轭的位置**：内积对第二变元是共轭线性的，这里必须取共轭。）
3. **唯一性与范数**。若另有 $z_1$ 也表示 $f$，则 $\langle x,z-z_1\rangle=0$ 对一切 $x$，取 $x=z-z_1$ 得 $\|z-z_1\|^2=0$，故 $z=z_1$。范数：由 $f(z)=\langle z,z\rangle=\|z\|^2\leqslant\|f\|\,\|z\|$ 得 $\|z\|\leqslant\|f\|$；由 Schwarz 得 $|f(x)|=|\langle x,z\rangle|\leqslant\|z\|\,\|x\|$，即 $\|f\|\leqslant\|z\|$。故 $\|f\|=\|z\|$。$\square$

**读法**：在 Hilbert 空间上，**泛函就是内积，内积就是泛函**。映射 $y\mapsto f_y(\cdot)=\langle\cdot,y\rangle$ 是 $X\to X'$ 的**保范共轭线性**到上映射（$X'$ 读作"$X$ 的共轭空间"，即连续线性泛函全体），所以 $X$ 与 $X'$ 可以等同——这叫**自共轭**。**这是"表示"主题的第一次胜利**：抽象对象（泛函）被表示成具体对象（向量）。

**两个常用例子**：

- $L^2[a,b]$ 上 $f(x)=\int_a^b x(t)\overline{g(t)}\,\mathrm dt$ 对应 $z=g$，且 $\|f\|=\|g\|_2$；
- $l^2$ 上 $f(x)=\sum_i\xi_i\bar\eta_i$ 对应 $z=(\eta_i)$。

**定义（共轭双线性形式）**：设 $H,K$ 是 Hilbert 空间，$\mathbb K$ 表示数域（$\mathbb R$ 或 $\mathbb C$）。映射 $u:H\times K\to\mathbb K$ 称为**共轭双线性形式**，是指对任意 $x,y\in H$、$z,w\in K$、$\alpha,\beta\in\mathbb K$ 有
$$u(\alpha x+\beta y,z)=\alpha u(x,z)+\beta u(y,z),\qquad u(x,\alpha z+\beta w)=\bar\alpha u(x,z)+\bar\beta u(x,w).$$
若存在常数 $c$ 使 $|u(x,z)|\leqslant c\|x\|\,\|z\|$ 对一切 $x\in H,z\in K$ 成立，称 $u$ 是**有界**的，$c$ 是 $u$ 的一个**上界**。

> **注意变元的共轭位置**：$u$ 对第一个变元线性、对第二个变元**共轭**线性——这与内积的约定一致（$u(x,z)=\langle Ax,z\rangle$ 时才对得上）。

**共轭双线性形式与算子的对应**：若 $A\in\mathcal B(H,K)$，则 $u(x,z)=\langle Ax,z\rangle$ 是有界共轭双线性形式；相仿地，若 $B\in\mathcal B(K,H)$，则 $u(x,z)=\langle x,Bz\rangle$ 也是有界共轭双线性形式。反过来，**任何有上界 $c$ 的共轭双线性形式都可由算子表示**：存在唯一的一对 $A\in\mathcal B(H,K)$、$B\in\mathcal B(K,H)$ 使
$$u(x,z)=\langle Ax,z\rangle=\langle x,Bz\rangle\quad(\forall x\in H,\ z\in K),$$
且 $\|A\|\leqslant c,\ \|B\|\leqslant c$。（证明用 Riesz 表示定理：固定 $x$，$z\mapsto\overline{u(x,z)}$ 是 $K$ 上的连续线性泛函，由 Riesz 定理得到唯一的 $w$，令 $Bx=w$；$A$ 由 $A=B^{*}$ 得到。这条定理的完整陈述在郭版 §5.3.2，算子的共轭记号见下一节。）

**应用（Lax–Milgram 定理，变分问题的存在唯一性）**：设 $u(x,y)$ 是 Hilbert 空间 $H$ 上的共轭双线性形式，满足

1. **有界**：$|u(x,y)|\leqslant c\|x\|\,\|y\|$；
2. **强制（椭圆）**：$|u(x,x)|\geqslant\delta\|x\|^2$（$\delta>0$），

则对 $H$ 上任意有界线性泛函 $f$，存在唯一 $x_0\in H$ 使 $u(x_0,y)=f(y)$ 对一切 $y\in H$ 成立。（完整证明在郭版 §6.2，用到 Riesz 表示定理。）

**反例（有界性不能去掉）**：在无穷维 Hilbert 空间上取不有界的共轭双线性形式，例如 $H=l^2$ 上取 $H_0=\operatorname{span}\{e_n\}$（有限支集数列），定义 $u(x,z)=\sum_n n\,x_n\bar z_n$。它在 $H_0\times H_0$ 上有定义且正定（$u(x,x)=\sum n|x_n|^2>0$），但 *因为* $u(e_n,e_n)=n\to\infty$，**不存在常数 $c$** 使 $|u(x,z)|\leqslant c\|x\|\|z\|$；相应地它不能由 $l^2$ 上的有界算子 $A$（$u(x,z)=\langle Ax,z\rangle$）表示——$A$ 只能定义在 $H_0$ 上，不是 $\mathcal B(H)$ 的元素。**这就是"无界算子"的来源**：量子力学中的动量算子、位置算子正是这一类。

> **这一节真正要说的是什么**：内积把几何还给了无穷维空间，于是三件事同时成立——**投影定理**（最近点存在唯一 ⟺ 差向量垂直 ⟺ 空间直和分解）、**傅里叶展开**（选好正交基后每个元素变成一列坐标，长度由 Parseval 保持）、**Riesz 表示**（连续线性泛函与向量一一对应）。三者是同一件事的三个侧面：**Hilbert 空间里，"几何"和"对偶"是同一套语言。**

---

## 去脉（学完去哪）

- **当代应用**：
  - **最小二乘与压缩感知**：最佳逼近引理就是最小二乘的法方程来源；稀疏表示则在"字典"（非正交的过完备系）上做同样的投影。
  - **信号处理**：Parseval 等式是能量守恒的频域表述（时域能量 = 频域能量）。
  - **量子力学**：态空间是 Hilbert 空间；可观测量是自伴算子（§5.3），测量结果是谱（§5.4）。
  - **偏微分方程的变分方法**：Lax–Milgram 定理给出弱解的存在唯一性。
  - **再生核 Hilbert 空间（RKHS）**：把 Riesz 表示定理用在"点赋值泛函"上，得到核函数 $k(x,\cdot)$——这是核方法与高斯过程的理论地基。
- **跨领域解读**：Riesz 表示定理在机器学习里就是"核技巧"的合法性证明：只要泛函（"在点 $x$ 处取值"）连续，就一定存在一个向量（核函数在该点的截面）来代表它。
- **高层视角**：Ch4 已把 $L^2$ 造好，本节证明它（以及一切可分无穷维 Hilbert 空间）**都只是 $l^2$ 的换装**。这正是"抽象"的收益：定理只证一次，例子无穷多。

## 防跳跃

- [ ] 极化恒等式逆命题的完整验证：用该式定义出的 $\langle\cdot,\cdot\rangle$ 确实满足三条内积公理、且导出原范数（郭版 §5.2.1 习题）
- [ ] 分类定理的证明：保内积同构的构造（把 $x$ 映为它的傅里叶系数列），以及"任意两个完全规范正交系基数相同"的论证
- [ ] 完全正交系存在性的证明（Zorn 引理路径 vs 可分情形的 Gram–Schmidt 路径）
- [ ] 引理"最近点自动垂直"中 $M$ 必须是**子空间**（而非仅凸集）的原因：$\alpha$ 是复数时 $y+\alpha y_1$ 未必落在凸集里
- [ ] 共轭双线性形式表示定理（郭版 §5.3.2 定理 5.3.9）的完整证明与 Lax–Milgram 定理（郭版 §6.2）
- [ ] $L^2[0,2\pi]$ 三角函数系**完全性**的证明（古典傅里叶级数收敛定理的 Hilbert 空间版本）
- [ ] 可分 Hilbert 空间中"完全规范正交系可数"的证明

## 来源与映射

| 本节点内容 | 来源 | 处理 |
|---|---|---|
| 内积三公理、共轭双线性性、半内积 | 旧《Ch9》§1.1；郭版教材 §5.2.1 | 原文迁移 + 补半内积 |
| Schwarz 不等式与证明 | 旧《Ch9》§1.2 | 原文迁移 |
| 导出范数、三角不等式、内积连续性 | 旧《Ch9》§1.2、§1.4 | 原文迁移 |
| Hilbert 空间定义与四个例子 | 旧《Ch9》§1.4 | 原文迁移（表格化） |
| 平行四边形公式与极化恒等式 | 旧《Ch9》§1.3 | 原文迁移 |
| 正交、正交补、勾股公式 | 旧《Ch9》§2.2 | 原文迁移 |
| 极小化向量定理（含唯一性证明） | 旧《Ch9》§2.1 | 原文迁移 |
| 投影定理与投影算子 | 旧《Ch9》§2.2 | 原文迁移（投影算子的进一步性质归 §5.3.3） |
| $Y=Y^{\perp\perp}$ 与稠密判据 | 旧《Ch9》§2.2 推论 | 原文迁移 |
| 规范正交系、傅里叶系数、最佳逼近引理 | 旧《Ch9》§3.1–§3.2 | 原文迁移（补"标准正交系"别名） |
| Bessel 不等式、Parseval 等式、级数收敛判据 | 旧《Ch9》§3.3 | 原文迁移 |
| 完全规范正交系三个等价刻画与傅里叶展开 | 旧《Ch9》§3.4 | 原文迁移 |
| Gram–Schmidt 正交化 | 旧《Ch9》§3.5 | 原文迁移 |
| 分类定理（可分 Hilbert 空间同构于 $l^2$） | 旧《Ch9》§3.5 定理 4、定理 5 | 原文迁移 |
| Riesz 表示定理与三步证明 | 旧《Ch9》§4.1 | 原文迁移 |
| 共轭双线性形式的定义、有界性、与算子的对应 | 郭版教材 §5.3.2 定义 5.3.8、定理 5.3.9；§5.2.3 习题 1（极化恒等式） | 新写补缺（旧讲解包无） |
| Lax–Milgram 定理 | 郭版教材 §6.2 定理 6.2.12 | 新写补缺（仅陈述与出处，证明归 Ch6） |
| 反例：$L^p\ (p\neq2)$ 与 $C[a,b]$ 不是内积空间 | 旧《Ch9》§1.4 例 3、例 4 | 原文迁移 |
| 反例：$\{\cos nx\}$ 不完全 | 旧《Ch9》§3.4 | 新写（据完全性定义构造） |
| 反例：无界共轭双线性形式 | 郭版教材 §5.3.2、§5.4 无界算子思想 | 新写 |
| 例题：$t^2$ 在 $L^2[-1,1]$ 中的最佳逼近 | 旧《Ch9》§3.2 最佳逼近引理 | 新写（据引理自编计算例） |