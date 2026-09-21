---
type: 节
formal: true
subject: 实变函数与泛函分析
created: 2026-09-21
updated: 2026-09-21
tags: [math, 实变函数与泛函分析]
chapter: 5
section: 5.4
---

# Sec5.4 Hilbert 空间上的紧算子

> 定位：在无穷维算子里挑出"最像有限维矩阵"的一类——紧算子。它们有离散谱、有 Fredholm 二择一、有谱分解，于是无穷维的算子方程可以像线性方程组一样被"解出来"。
> 教材：郭懋正《实变函数与泛函分析》§5.4（p.256–273）
> 来源：郭版教材 §5.4.1–§5.4.3（新写）；旧讲解包《Ch8 有界线性算子和连续线性泛函》§3（有限秩算子，作为前奏）

> [!info] 关联笔记
> - 父级：[[Ch5 Hilbert 空间理论]]
> - 前置：[[Sec5.3 Hilbert 空间上的算子]]
> - 概念：[[概念-紧算子]]

---

## 来龙（为什么需要它）

- **类比已知**：有限维里线性方程组 $Tx=y$ 的求解完全由矩阵决定——**要么对每个 $y$ 有唯一解，要么齐次方程 $Tx=0$ 有非零解**，这两件事必居其一。这个"二择一"是线性代数的基本定理。
- **解决新问题**：无穷维里这个二择一**失效**了。例如 $l^2$ 上的单向移位 $T(\xi_1,\xi_2,\dots)=(0,\xi_1,\xi_2,\dots)$：齐次方程 $Tx=0$ 只有零解，但 $T$ **不是满射**（$y=(1,0,0,\dots)$ 无解）。**"唯一解"和"有非零解"可以都不成立**——这是无穷维独有的病。
- **理论/应用需要**：积分方程
  $$x(t)-\int_a^bk(t,s)x(s)\,\mathrm ds=y(t)$$
  是 Fredholm 在 1900 年代研究的核心问题。它对应的算子是 $I-A$，其中 $A$ 是**积分算子**。**只要 $A$ 是紧算子，二择一就恢复成立**——这就是紧算子存在的根本理由：**它把无穷维问题压回有限维的形状。**
- **本节的边界**：紧算子的谱、Fredholm 二择一、Hilbert–Schmidt 定理在旧讲解包中**没有对应内容**（旧讲解包只讲到 §8.3 有限秩算子），本节主体按郭版教材 §5.4 新写；有限秩算子部分取自旧《Ch8》§3，作为紧算子的前奏。

---

## 主体（核心内容）

### 5.4.1 紧算子定义

**定义（紧算子）**：设 $H,K$ 是 Hilbert 空间，$A$ 是 $H$ 到 $K$ 的线性算子，$B_1=\{x\in H:\|x\|\leqslant1\}$ 是 $H$ 的**单位球**（读作"$B$ 一下标 1"）。若 $\overline{A(B_1)}$（$A(B_1)$ 在 $K$ 中的**闭包**）在 $K$ 中是**紧集**，称 $A$ 是**紧算子**。$\mathcal C(H,K)$ 表示所有紧算子构成的集合；当 $K=H$ 时简记作 $\mathcal C(H)$（$\mathcal C$ 读作"紧算子全体"）。

**等价刻画（三条完全等价）**：
$$A\in\mathcal C(H,K)\iff\text{对 }H\text{ 中任意有界集 }B,\ \overline{A(B)}\text{ 在 }K\text{ 中紧}\iff\text{对 }H\text{ 中任意有界点列 }\{x_n\},\ \{Ax_n\}\text{ 在 }K\text{ 中列紧}.$$

> **读法**：紧算子 = "把**有界**变成**几乎列紧**"的算子。注意两个关键词：**有界集**（不是整个空间）、**闭包紧**（不是像本身紧）。用列紧的语言说就是：**任何有界列在 $A$ 下的像都有收敛子列**——这把"无穷维"压成了"有限维"。

> **注意与 §5.1 的呼应**：这里用"列紧"而不是"紧致"，是因为在距离空间里两者对**闭集**等价（§5.1.2 定理：紧致 $\iff$ 自列紧），而 $\overline{A(B_1)}$ 是闭的，两种说法可以互换。教材采用"$\overline{A(B_1)}$ 紧"的写法，是为了直接对接"有穷 $\varepsilon$ 网"的证明手法。

**命题（紧算子的基本性质）**：

1. $\mathcal C(H,K)$ 是**线性空间**；
2. $\mathcal C(H,K)\subset\mathcal B(H,K)$（**紧 ⟹ 有界**）；
3. $\mathcal C(H,K)$ 是 $\mathcal B(H,K)$ 的**闭子空间**；
4. 若 $A\in\mathcal B(H,K)$、$B\in\mathcal B(K,J)$ 且 $A,B$ 中**有一个是紧算子**，则 $BA\in\mathcal C(H,J)$（**紧算子构成双边理想**）。

**证明**：

- (1) 显然（线性组合的像含于像的和，有限个紧集之和紧）。
- (2) *因为* $\overline{A(B_1)}$ 是紧集故有界，记
  $$M=\sup\{\|Ax\|:x\in B_1\}<\infty,$$
  则对任意 $x\neq0$，*因为* $x/\|x\|\in B_1$，$\|Ax\|=\|x\|\left\|A\dfrac{x}{\|x\|}\right\|\leqslant M\|x\|$，故 $A$ 有界。
- (3) 设 $A_n\in\mathcal C(H,K)$、$A\in\mathcal B(H,K)$、$\|A_n-A\|\to0$。任给 $\varepsilon>0$，*因为* 范数收敛，存在 $n$ 使 $\|A_n-A\|<\varepsilon/2$。*因为* $\overline{A_n(B_1)}$ 紧，它有**有穷 $\varepsilon/2$ 网** $\{y_1,\dots,y_m\}$。则对任意 $x\in B_1$，*因为* $A_nx$ 被某个 $y_i$ 盖住，
  $$\overline{A(B_1)}\subset\bigcup_{i=1}^mB(y_i,\varepsilon),$$
  即 $\overline{A(B_1)}$ 有有穷 $\varepsilon$ 网，故为紧集（*因为* 在距离空间里"完全有界 + 闭 = 紧"）。
- (4) *因为* 连续线性算子把有界集映为有界集、把紧集映为紧集，$\overline{BA(B_1)}$ 是紧集的连续像的闭包，仍紧。$\square$

**反例（恒等算子不紧——有界推不出紧）**：设 $\dim H=\infty$，则恒等算子 $I$ **有界但不紧**。取 $H$ 的标准正交系 $\{e_n\}$，*因为* $\|e_n\|=1$，$\{e_n\}\subset B_1$；但 *因为* $\|Ie_n-Ie_m\|=\|e_n-e_m\|=\sqrt2\ (n\neq m)$，$\{Ie_n\}$ **没有收敛子列**，故 $I$ 不紧。**这是紧算子理论的第一块界碑：无穷维空间上"有界"远远不够。**

**定义（有穷秩算子）**：设 $A\in\mathcal B(H,K)$。若 $\dim\mathcal R(A)<\infty$（值域是有限维的），称 $A$ 是**有穷秩算子**，一切有穷秩算子构成集合 $F(H,K)$。

**为什么重要**：有穷秩算子是"最接近矩阵"的无穷维算子——它的像落在有限维子空间里，而 *因为* 有限维的有界集是列紧的，立刻有
$$F(H,K)\subset\mathcal C(H,K).$$
（本节的核心结论将说明：这个包含关系的**闭包**恰好填满 $\mathcal C(H,K)$。）

**秩 1 算子**：对 $x\in H$、$y\in K$，用 $x\otimes y$（读作"$x$ 张量 $y$"）表示算子
$$x\otimes y:h\mapsto\langle h,x\rangle y,\quad\forall h\in H.$$
*因为* 它的值域含于 $\operatorname{span}\{y\}$（一维），$x\otimes y\in F(H,K)$。

**定理（有穷秩算子的标准形）**：$A\in F(H,K)\iff$ 存在 $x_i\in H$、$y_i\in K$（$i=1,\dots,m$）使
$$A=\sum_{i=1}^mx_i\otimes y_i.$$

**证明**：

- **充分性**：*因为* $\mathcal R(A)=\operatorname{span}\{y_1,\dots,y_m\}$ 有限维，故 $A\in F(H,K)$。
- **必要性**：*因为* $\dim\mathcal R(A)=m<\infty$，可在 $\mathcal R(A)$ 上取标准正交基 $\{y_1,\dots,y_m\}$，则对任意 $x\in H$ 有
  $$Ax=\sum_{i=1}^m\langle Ax,y_i\rangle y_i.$$
  记 $l_i(x)=\langle Ax,y_i\rangle$，*因为* $A$ 有界、内积连续，每个 $l_i$ 是 $H$ 上的**有界线性泛函**。*因为* $H$ 是 Hilbert 空间，由 **Riesz 表示定理**（§5.2.3）存在唯一的 $x_i\in H$ 使 $l_i(x)=\langle x,x_i\rangle$。于是
  $$Ax=\sum_{i=1}^m\langle x,x_i\rangle y_i=\sum_{i=1}^m(x_i\otimes y_i)x,$$
  即 $A=\sum_{i=1}^mx_i\otimes y_i$。事实上此时 $x_i=A^*y_i$。$\square$

**定理（紧算子的核心刻画）**：设 $A\in\mathcal B(H,K)$，则下列命题等价：

1. $A$ 是**紧算子**；
2. $A\in\overline{F(H,K)}$（即 $A$ 是**有限秩算子的一致极限**）；
3. $A^*$ 是**紧算子**。

**推论**：$\overline{F(H,K)}=\mathcal C(H,K)$——**紧算子全体恰好是有限秩算子的闭包**。

**证明思路**：

- $(2)\Rightarrow(1)$：*因为* 由命题 (3) $\mathcal C(H,K)$ 是闭子空间，而 $F(H,K)\subset\mathcal C(H,K)$，取闭包得 $\overline{F(H,K)}\subset\mathcal C(H,K)$。
- $(1)\Rightarrow(3)$ 与 $(1)\Rightarrow(2)$ 的证明用到 $A$ 的紧性构造一串有限秩逼近（郭版 §5.4.1 定理 5.4.5 的证明），关键手法是：先证 $A^*$ 紧，再对 $A$ 作有限秩截断并估计余项范数。

> **核心事实（本节的中心句）**：**紧算子 = 有限秩算子的极限**。这条等式把"无穷维"翻译成"有限维的极限"，于是所有有限维的结论都可以"取极限"搬过来——这正是 Fredholm 二择一与谱分解能成立的机制。

**例题**：设 $k(t,s)\in L^2([0,1]^2)$，定义
$$(Af)(t)=\int_0^1k(t,s)f(s)\,\mathrm ds,\qquad f\in L^2[0,1].$$
证明 $A\in\mathcal C(L^2[0,1])$（这类算子称为 **Hilbert–Schmidt 型积分算子**）。

- **原始信息**：核 $k$ 只假设平方可积（*因为* $[0,1]^2$ 测度有限，$L^2\subset L^1$，所以积分有意义）。
- **第一步：$A$ 有界**。取 $[0,1]^2$ 的标准正交基 $\{e_i(t)e_j(s)\}_{i,j\geqslant1}$（*因为* $L^2([0,1]^2)=L^2[0,1]\otimes L^2[0,1]$，二重正交系是完备的），把 $k$ 展开：
  $$k=\sum_{i,j}\alpha_{ij}e_i\otimes e_j,\qquad \sum_{i,j}|\alpha_{ij}|^2=\|k\|_{L^2}^2<\infty.$$
  令 $A_{mn}f=\sum_{i=1}^m\sum_{j=1}^n\alpha_{ij}\langle f,e_i\rangle e_j$。*因为* 这是有限秩算子，$A_{mn}\in F$。
- **第二步：$A_{mn}\to A$**。*因为*
  $$\left\|(A-A_{mn})f\right\|_2\leqslant\|k-k_{mn}\|_{L^2}\cdot\|f\|_2,$$
  得 $\|A-A_{mn}\|\leqslant\|k-k_{mn}\|_{L^2}$；又 *因为* 展开式在 $L^2$ 中收敛，右端 $\to0$。
- **结果与结论**：$A$ 是有限秩算子的一致极限，由定理 5.4.5 得 $A\in\mathcal C(L^2[0,1])$。**这说明 Fredholm 积分方程里的算子天然是紧算子**——这正是紧算子理论的应用主场。

**前奏：有限秩算子扰动不破坏值域闭性（商空间方法）**

紧算子理论要证的第一件事是"$I-A$ 的值域是闭的"（下一小节定理 5.4.10 (2) 用到）。对**有限秩**算子 $T$，这件事有一个漂亮的证明，用到本节唯一的新工具——**商空间**。

**定义（商空间）**：$V$ 是赋范空间 $X$ 的**闭**子空间。规定等价关系 $x_1\sim x_2\iff x_1-x_2\in V$；等价类 $[x]=\{x+v:v\in V\}$；全体等价类记 $X/V$（读作"$X$ 模 $V$ 的商空间"）。加法与数乘按 $[x]+[y]=[x+y]$、$\alpha[x]=[\alpha x]$ 定义，范数取
$$\|[x]\|=\inf\{\|x+v\|:v\in V\}.$$

> **读法**：商空间把 $V$"压成一个点"，$\|[x]\|$ 恰好是 $x$ 到子空间 $V$ 的**距离**。

**定理（商空间的赋范与完备性）**：$X$ 赋范 $\Rightarrow X/V$ 赋范；$X$ 完备 $\Rightarrow X/V$ 完备。（完备性证明：把 $X/V$ 中的柯西列用 $2^{-k}$ 余量逐项修到 $X$ 里，再用 $X$ 的完备性求和。）

**例**：$X=C[0,1]$、$V=\{f\in X:f(1)=0\}$。*因为* $[f]=[g]\iff f(1)=g(1)$，映射 $\varphi([f])=f(1)$ 给出 $X/V$ 与 $\mathbb C$ 的等距同构——**商掉"在 $1$ 点为 $0$"的子空间后，剩下的信息恰好是"函数在 $1$ 点的值"。**

**定理（$I+T$ 的值域闭，$T$ 有穷秩）**：设 $X$ 是 Banach 空间，$T\in F(X)$，则 $\mathcal R(I+T)$ 是 $X$ 中的**闭**子空间。

**证明路线**：设 $A=I+T$。先在商空间 $X/\mathcal N(A)$ 上定义 $\hat A[x]=Ax$，*因为* 同一等价类的元素在 $A$ 下像相同，$\hat A$ 良定义且是有界线性算子，且 $\ker\hat A=\{[0]\}$。再证 $\mathcal R(A)$ 闭：若 $y_n\in\mathcal R(A)$、$y_n\to y$，取 $x_n$ 使 $Ax_n=y_n$，适当修代表元（*因为* 商空间范数取的是到 $\mathcal N(A)$ 的距离，可令 $s_n=x_n-z_n$ 使 $\|s_n\|$ 接近 $\|\hat A^{-1}y_n\|$），得 $y_n=s_n+Ts_n$；用反证排除 $\|s_n\|\to\infty$（*因为* $\mathcal R(T)$ 有限维，其中的有界列有收敛子列），于是 $\{s_n\}$ 有界、$\{Ts_n\}$ 有收敛子列，从而 $s_n$ 收敛，得 $y=(I+T)(y-y_0)\in\mathcal R(I+T)$。$\square$

**意义**：这是"**有限维扰动不破坏值域闭性**"。下一小节把它推广到紧扰动（$A=I-$紧算子），值域闭性正是 Fredholm 二择一得以成立的关键——*因为* 只有值域闭时，"$\mathcal R(T)=H$"才等价于"$T$ 满射"。

> **边界说明**：商空间的一般理论属于 Banach 空间范畴，其完整形态（范数等价、商空间与开映射定理的关系）见 Ch6 §6.2；本节只用它证明上面这一条，服务于紧算子理论。

### 5.4.2 Fredholm 理论，紧算子的谱

**定义（预解集、谱、点谱）**：设 $H$ 是 Hilbert 空间，$A\in\mathcal B(H)$。称集合
$$\rho(A)=\{\lambda\in\mathbb C:(\lambda I-A)^{-1}\in\mathcal B(H)\}$$
为 $A$ 的**预解集**（$\rho$ 读作"rho"，$\rho(A)$ 中的 $\lambda$ 称为 $A$ 的**正则值**）；称
$$\sigma(A)=\mathbb C\setminus\rho(A)$$
为 $A$ 的**谱集**（$\sigma$ 读作"sigma"），$\sigma(A)$ 中的 $\lambda$ 称为 $A$ 的**谱**；称
$$\sigma_p(A)=\{\lambda\in\mathbb C:\ker(\lambda I-A)\neq\{0\}\}$$
为 $A$ 的**点谱**，$\sigma_p(A)$ 中的 $\lambda$ 称为 $A$ 的**特征值**。

当 $\lambda\in\sigma_p(A)$ 时存在非零 $x\in H$ 满足 $Ax=\lambda x$，此时 $x$ 称为对应于 $\lambda$ 的**特征元**（特征向量）。*因为* 这时 $\lambda I-A$ 不是单射，故不可逆，所以
$$\sigma_p(A)\subset\sigma(A).$$
**如果 $\dim H<\infty$，则 $\sigma_p(A)=\sigma(A)$**（*因为* 有限维方阵非单射即不可逆）；**当 $\dim H=\infty$ 时，$\sigma_p(A)$ 往往是 $\sigma(A)$ 的真子集**——这个差别正是本节要处理的全部难点。

**引理（无穷维紧算子没有有界逆）**：设 $A\in\mathcal C(H)$、$\dim H=\infty$，则 $A$ **没有有界逆**。

**证明（反证）**：倘若不然，存在 $A^{-1}\in\mathcal B(H)$。由 $\|A^{-1}y\|\leqslant\|A^{-1}\|\,\|y\|$，取 $y=Ax$ 得
$$\|Ax\|\geqslant\|A^{-1}\|^{-1}\|x\|,\quad\forall x\in H.$$
取 $\{x_n\}$ 为标准正交集，则 *因为* $\|x_n-x_m\|=\sqrt2$，
$$\|Ax_n-Ax_m\|\geqslant\|A^{-1}\|^{-1}\|x_n-x_m\|=\sqrt2\,\|A^{-1}\|^{-1}>0,$$
即 $\{Ax_n\}$ 中任意两项都隔开一个固定正距离，**没有收敛子列**，与 $A$ 的紧性矛盾。$\square$

> **重要推论**：在无穷维空间中，$0$ 一定是紧算子的谱（*因为* $A$ 不可逆）。**"除 $0$ 以外"是本节所有谱结论的共同前缀。**

**定理（$T=I-A$ 的四条基本性质）**：设 $A\in\mathcal C(H)$、$T=I-A$，则

1. $\sigma(T^*)=\{\bar\lambda:\lambda\in\sigma(T)\}$；
2. $\mathcal R(T)=(\ker T^*)^\perp$，$\mathcal R(T^*)=(\ker T)^\perp$；
3. $\dim\ker T=\dim\ker T^*<\infty$；
4. $\ker T=\{0\}\iff\mathcal R(T)=H$。

**证明要点**：

- (1) *因为* $(\lambda I-T)^{-1}\in\mathcal B(H)\iff(\bar\lambda I-T^*)^{-1}\in\mathcal B(H)$（共轭算子保持可逆性），即 $\rho(T^*)=\{\bar\lambda:\lambda\in\rho(T)\}$，在复平面上取余集即得。
- (2) 用"$T$ 是闭值域算子"这一引理（郭版 §5.4.2 引理 5.4.7：若 $T$ 闭值域则 $\overline{\mathcal R(T)}=\mathcal R(T)$）以及 $\overline{\mathcal R(T)}=(\ker T^*)^\perp$。
- (3) 在 $\ker T$ 上 $T|_{\ker T}=0$，故 $A|_{\ker T}=I|_{\ker T}$，即 $A$ 在 $\ker T$ 上就是恒等算子；*因为* $A$ 紧、而无穷维空间上恒等算子不紧（5.4.1 的反例），必有 $\dim\ker T<\infty$。同法得 $\dim\ker T^*<\infty$。再证两者相等：若 $\dim\ker T<\dim\ker T^*$，*因为* $\dim\ker T<\infty$，可取真子空间 $\widetilde M\subset\ker T^*$ 与等距同构 $\widetilde V:\ker T\to\widetilde M$，则 $\widetilde V+T$ 仍呈"$I-$紧算子"的形状且是单射，由下一条引理（郭版 §5.4.2 引理 5.4.8：$\ker T=\{0\}$ 时 $\mathcal R(T)=H$）应有 $\mathcal R(\widetilde V+T)=H$，但 $\mathcal R(\widetilde V+T)=\widetilde M\oplus\mathcal R(T)$ 是 $H$ 的真子集——矛盾。故 $\dim\ker T\geqslant\dim\ker T^*$；反向用 $T^{**}=T$ 同理。故两者相等。
- (4) 若 $\mathcal R(T)=H$，则 *因为* $\ker T^*=\mathcal R(T)^\perp=\{0\}$，由 (3) 得 $\ker T=\{0\}$；反向由引理 5.4.8 直接给出。$\square$

**定理（Fredholm 二中择一律）**：设 $A\in\mathcal C(H)$，考虑算子方程
$$x=Ax+y,\qquad\text{即}\qquad Tx=y\quad(T=I-A).$$
则**只有两种可能**：

1. **或者** 对每一个 $y\in H$，方程 $Tx=y$ 存在**唯一解**；
2. **或者** $y=0$ 时齐次方程 $Tx=0$ 有**非零解**，且齐次方程的解空间 $\ker T$ 是**有穷维**的。

**证明**：由定理 (4)，$\ker T=\{0\}\iff\mathcal R(T)=H$。

- 若 $\ker T=\{0\}$：*因为* $T$ 单射且满射，$T^{-1}$ 存在；再由定理 (2) 与闭值域引理，$\mathcal R(T)=H$ 是闭的，故 $T^{-1}$ 有界，于是每个 $y$ 有唯一解——这是情形 (1)。
- 若 $\ker T\neq\{0\}$：*因为* 有非零 $x$ 使 $Tx=0$（即 $x=Ax$），齐次方程有非零解；又 *因为* 由定理 (3) $\dim\ker T<\infty$——这是情形 (2)。$\square$

**读法与意义**：*因为* 两种情形**互相排斥且穷尽**，所以"解的存在唯一性"与"齐次方程有非平凡解"必居其一。**当 $\dim H<\infty$、$T$ 是矩阵时，这就是线性代数里"$\det T\neq0$ 或 $T$ 奇异"的二择一**；Fredholm 把它推广到了积分方程 $T=I-A$（$A$ 为积分核算子）。**注意定理对 $A$ 的紧性依赖极重**——单向移位就是反例（见下）。

**反例（紧性不可少：二择一失效）**：$l^2$ 上单向移位 $A(\xi_1,\xi_2,\dots)=(0,\xi_1,\xi_2,\dots)$。*因为* $\|Ae_n\|=1$ 而 $Ae_n\perp Ae_m$，$\{Ae_n\}$ 无收敛子列，$A$ **不紧**。取 $T=I-A$：

- $\ker T=\{0\}$（*因为* $Tx=0$ 即 $\xi_{n+1}=\xi_n$ 且 $\xi_1=0$，推出 $x=0$）；
- 但 $\mathcal R(T)=\{y\in l^2:\sum|y_n|^2<\infty,\ y\ \text{满足某条件}\}$ **不是全空间**——具体地 $y=(1,0,0,\dots)$ 时方程 $Tx=y$ 无解（*因为* 需 $\xi_1=1$、$\xi_2=\xi_1=1$、…… 得 $\xi_n\equiv1\notin l^2$）。

于是**两种情形都不成立**：既非"每个 $y$ 有解"，也非"齐次方程有非零解"。**这正是紧性条件不可去掉的见证。**

**引理（$\lambda\neq0$ 时范数下确界为 $0$ 蕴含特征值）**：设 $A\in\mathcal C(H)$、$\lambda\in\mathbb C$、$\lambda\neq0$。若
$$\inf\{\|(\lambda I-A)x\|:\|x\|=1\}=0,$$
则 $\lambda\in\sigma_p(A)$。

**证明**：要证 $\ker(\lambda I-A)\neq\{0\}$。由已知，存在 $\{x_n\}$、$\|x_n\|=1$ 且 $(\lambda I-A)x_n\to0$。*因为* $A$ 紧，存在子列 $x_{n_k}$ 使 $Ax_{n_k}\to z$。于是 *因为* $\lambda x_{n_k}=(\lambda I-A)x_{n_k}+Ax_{n_k}$，得 $\lambda x_{n_k}\to z$，故
$$\|z\|=\lim_k\|\lambda x_{n_k}\|=|\lambda|\neq0,\quad z\neq0.$$
*因为* $\lambda I-A$ 连续，
$$0=\lim_k(\lambda I-A)x_{n_k}=(\lambda I-A)(\lambda^{-1}z),$$
故 $\lambda^{-1}z\neq0$ 是特征元，即 $\lambda\in\sigma_p(A)$。$\square$

**定理（紧算子的谱结构，本节主定理）**：设 $A\in\mathcal C(H)$，则

1. $0\in\sigma(A)$，**除非** $\dim H<\infty$；
2. $\sigma(A)\setminus\{0\}=\sigma_p(A)\setminus\{0\}$——**除 $0$ 外的谱全是特征值**；
3. $\sigma_p(A)$ **至多以 $0$ 为聚点**。

**证明**：

- (1) 即"无穷维紧算子没有有界逆"引理：*因为* $A$ 不可逆，$0\notin\rho(A)$，故 $0\in\sigma(A)$。
- (2) 只需证：当 $\lambda\notin\sigma_p(A)$、$\lambda\neq0$ 时必有 $\lambda\in\rho(A)$。*因为* $\lambda\notin\sigma_p(A)$，$\ker(\lambda I-A)=\{0\}$；由定理 (4) 得 $\mathcal R(\lambda I-A)=H$，故 $\lambda I-A$ 是单射满射，存在逆算子。剩下只要证 $(\lambda I-A)^{-1}\in\mathcal B(H)$。*因为* $\lambda\notin\sigma_p(A)$，由上一条引理的逆否命题，
  $$\inf\{\|(\lambda I-A)x\|:\|x\|=1\}=c>0,$$
  故 $\|(\lambda I-A)x\|\geqslant c\|x\|$ 对一切 $x$。对任意 $y$，令 $x=(\lambda I-A)^{-1}y$ 代入得
  $$\left\|(\lambda I-A)^{-1}y\right\|\leqslant c^{-1}\|y\|,$$
  即 $\|(\lambda I-A)^{-1}\|\leqslant c^{-1}<\infty$，故 $\lambda\in\rho(A)$。
- (3) **反证**。若存在 $\lambda_n\in\sigma_p(A)\setminus\{0\}$ 两两不同且 $\lambda_n\to\lambda\neq0$。任取 $x_n\in\ker(\lambda_nI-A)\setminus\{0\}$，则
  **(i)** $\{x_1,x_2,\dots,x_n\}$ 对每个 $n$ 都**线性无关**。事实上用归纳法：若有 $x_{n+1}=\sum_{i=1}^na_ix_i$，两边作用 $A$ 得 $\lambda_{n+1}x_{n+1}=\sum_{i=1}^na_i\lambda_ix_i$；与 $\lambda_{n+1}x_{n+1}=\sum_i a_i\lambda_{n+1}x_i$ 相减得 $\sum_i a_i(\lambda_i-\lambda_{n+1})x_i=0$，*因为* 归纳假设 $\{x_1,\dots,x_n\}$ 线性无关，得 $a_i(\lambda_i-\lambda_{n+1})=0$；*因为* $\lambda_i\neq\lambda_{n+1}$，得 $a_i=0$，于是 $x_{n+1}=0$，与 $x_{n+1}\neq0$ 矛盾。
  **(ii)** 令 $H_n=\operatorname{span}\{x_1,\dots,x_n\}$，*因为* $A$ 把 $H_n$ 映入 $H_n$，可构造单位向量 $y_n\in H_n\cap H_{n-1}^\perp$。对 $m>n$，*因为* $Ay_n-\lambda_my_n\in H_{n+1}$（用 $y_n$ 的展开式与 $A$ 的作用可验证），可得
  $$\|Ay_n-Ay_m\|\geqslant|\lambda_m|\cdot\|y_n\|\geqslant\delta>0,$$
  即 $\{Ay_n\}$ 没有收敛子列，与 $A$ 紧矛盾。$\square$

> **核心事实（紧算子谱的三句话）**：**除 $0$ 外全是特征值；特征值只有可数多个；$0$ 是唯一可能的聚点。** 这就是"离散谱"——与有限维矩阵的谱形状完全一致，只不过多了一个必然出现的 $0$。

**例题**：设 $A\in\mathcal C(H)$ 且 $\|A\|<\tfrac12$。证明方程 $x=Ax+y$ 对每个 $y\in H$ 有唯一解，并估计解的范数。

- **原始信息**：$A$ 紧，$\|A\|<\tfrac12$，$T=I-A$。
- **验证前提**：*因为* $\|A\|<1$，取 $\lambda=1$，则
  $$\inf_{\|x\|=1}\|(\lambda I-A)x\|=\inf_{\|x\|=1}\|x-Ax\|\geqslant1-\|A\|>0,$$
  即 $\lambda=1\notin\sigma_p(A)$。*因为* $A$ 紧且 $\lambda=1\neq0$，由谱结构定理 (2)，$\lambda=1\in\rho(A)$，即 $(I-A)^{-1}\in\mathcal B(H)$。
- **代入**：于是对每个 $y\in H$，$x=(I-A)^{-1}y$ 是唯一解。再由
  $$\|x\|=\|y+Ax\|\leqslant\|y\|+\|A\|\,\|x\|\Longrightarrow\|x\|\leqslant\frac{\|y\|}{1-\|A\|},$$
  得 $\left\|(I-A)^{-1}\right\|\leqslant\dfrac{1}{1-\|A\|}<2$。
- **结果与结论**：解存在唯一且 $\|x\|\leqslant\dfrac{\|y\|}{1-\|A\|}<2\|y\|$。**注意这里用的是"谱结构定理"而非压缩映射原理**：$A$ 不必是压缩映射（$\|A\|$ 可以接近 $1$），紧性已经足够保证 $1$ 是正则值。这是紧算子理论比压缩映射原理更强的表现——**"二择一"取代了"收缩性"。**

### 5.4.3 Hilbert–Schmidt 理论

本节的目标：把**自伴紧算子**像对称矩阵一样对角化。

**引理（正规算子的特征子空间）**：设 $A$ 是**复** Hilbert 空间 $H$ 上的正规算子（$AA^*=A^*A$），$\lambda\in\mathbb C$，则

1. $\ker(\lambda I-A)=\ker(\bar\lambda I-A^*)$；
2. $\ker(\lambda I-A)$ 是 $A$ 的**可约化子空间**，即 $\ker(\lambda I-A)$ 与它的正交补都是 $A$-不变的。

**证明要点**：*因为* $A-\lambda I$ 仍正规，由 5.3.2 的正规算子刻画 $\|T^*x\|=\|Tx\|$，
$$\|(A^*-\bar\lambda I)x\|=\|(A-\lambda I)^*x\|=\|(A-\lambda I)x\|,$$
故两者同时为 $0$，得 (1)。(2) 由 (1)：若 $x\perp\ker(\lambda I-A)$，则对任意 $y\in\ker(\lambda I-A)$，*因为* $A^*y=\bar\lambda y$，
$$\langle Ax,y\rangle=\langle x,A^*y\rangle=\bar\lambda\langle x,y\rangle=0,$$
故 $Ax\perp\ker(\lambda I-A)$，即 $\ker(\lambda I-A)^\perp$ 也是 $A$-不变的。$\square$

**命题（自伴紧算子的最大特征值）**：设 $A$ 是自伴紧算子，则存在实数 $\lambda_1\in\sigma_p(A)$ 使 $|\lambda_1|=\|A\|$。

> **读法**：有限维对称矩阵的最大特征值绝对值等于算子范数（*因为* 对称矩阵可正交对角化）；这条命题说**无穷维自伴紧算子也一样**——而且它正是谱分解能"一步一步剥出来"的引擎。

**定理（Hilbert–Schmidt 谱分解定理）**：设 $A$ 是**复** Hilbert 空间 $H$ 上的**紧自伴**算子（$A^*=A$、$A\in\mathcal C(H)$），记 $\{\lambda_1,\lambda_2,\dots,\lambda_n,\dots\}$ 为 $A$ 的**所有不同的非零特征值**，则

1. 每个 $\lambda_n$ 都是**实数**；
2. 记 $P_n$ 是 $H$ 到 $\ker(\lambda_nI-A)$ 的**正交投影**，则 $P_nP_m=P_mP_n=O\ (n\neq m)$；
3. **谱分解**：
   $$A=\sum_{n=1}^\infty\lambda_nP_n,$$
   且级数在 $\mathcal B(H)$ 的**算子范数**意义下收敛到 $A$。

**证明（"逐个剥出特征值"的归纳构造）**：

- **第 1 步**。由命题，存在实数 $\lambda_1\in\sigma_p(A)$ 使 $|\lambda_1|=\|A\|$。令 $E_1=\ker(\lambda_1I-A)$、$P_1=P_{E_1}$、$H_2=E_1^\perp$。*因为* 由引理 $E_1$ 是 $A$ 的可约化子空间，$H_2$ 也是 $A$-不变的；令 $A_2=A|_{H_2}$，则 $A_2$ 是 $H_2$ 上的紧自伴算子。
- **第 2 步（归纳）**。对 $A_2$ 重复第 1 步，得实数 $\lambda_2\in\sigma_p(A_2)$ 使 $|\lambda_2|=\|A_2\|$；*因为* $H_2$ 的定义，$\lambda_2\neq\lambda_1$ 且 $E_2=\ker(\lambda_2I-A_2)=\ker(\lambda_2I-A)$。继续得
  $$|\lambda_1|\geqslant|\lambda_2|\geqslant\cdots,\qquad|\lambda_{n+1}|=\left\|A\big|_{(E_1\oplus\cdots\oplus E_n)^\perp}\right\|.$$
- **第 3 步：证 $\lambda_n\to0$**。*因为* 单调下降有下界，$|\lambda_n|\to\alpha\geqslant0$。取 $e_n\in E_n$、$\|e_n\|=1$，*因为* 不同特征子空间互相正交，$e_n\perp e_m\ (n\neq m)$；*因为* $A$ 紧，存在子列使 $Ae_{n_j}\to y$。但 *因为* $Ae_{n_j}=\lambda_{n_j}e_{n_j}$ 且 $e_{n_j}\perp e_{n_k}$，
  $$\left\|Ae_{n_j}-Ae_{n_k}\right\|^2=\lambda_{n_j}^2+\lambda_{n_k}^2\geqslant2\alpha^2,$$
  *因为* $\{Ae_{n_j}\}$ 是收敛列（柯西列），必须 $\alpha=0$。**这就是"非零特征值只能以 $0$ 为聚点"的来源。**
- **第 4 步：证级数收敛到 $A$**。考虑 $A-\sum_{j=1}^n\lambda_jP_j$。*因为* 当 $x\in E_k\ (1\leqslant k\leqslant n)$ 时
  $$\left(A-\sum_{j=1}^n\lambda_jP_j\right)x=Ax-\lambda_kx=0,$$
  故 $E_1\oplus\cdots\oplus E_n\subset\ker\left(A-\sum_{j=1}^n\lambda_jP_j\right)$；而当 $x\in(E_1\oplus\cdots\oplus E_n)^\perp$ 时 $P_jx=0\ (1\leqslant j\leqslant n)$，故
  $$\left(A-\sum_{j=1}^n\lambda_jP_j\right)x=Ax,$$
  于是由第 2 步的范数等式得
  $$\left\|A-\sum_{j=1}^n\lambda_jP_j\right\|=|\lambda_{n+1}|\xrightarrow[n\to\infty]{}0.$$
  $\square$

> **读法（与线性代数的对应）**：$A=\sum_n\lambda_nP_n$ 就是**对称矩阵的正交对角化** $A=Q\Lambda Q^{\mathsf T}$ 的无穷维版本——$P_n$ 扮演"投影到第 $n$ 个特征子空间"的角色，$\lambda_n$ 是特征值。区别只有一处：**这里有无穷多项，而且它们必须按 $|\lambda_n|\to0$ 的次序排列。**

**定理（特征值的极小极大刻画）**：设 $A$ 是紧自伴算子，特征值如上，则
$$\lambda_n^+=\inf_{V_{n-1}}\sup_{\substack{x\in V_{n-1}^\perp\\ x\neq0}}\frac{\langle Ax,x\rangle}{\langle x,x\rangle},\qquad\lambda_n^-=\sup_{V_{n-1}}\inf_{\substack{x\in V_{n-1}^\perp\\ x\neq0}}\frac{\langle Ax,x\rangle}{\langle x,x\rangle},$$
其中 $V_{n-1}$ 取遍 $H$ 的**任意 $n-1$ 维闭线性子空间**。

**证明要点**：*因为* 用 $-A$ 代替 $A$ 可把第二个等式化为第一个，只需证第一个。对任意 $x=\sum_ja_j^+e_j^++\sum_ja_j^-e_j^-$（按特征元展开），
$$\frac{\langle Ax,x\rangle}{\langle x,x\rangle}=\frac{\sum_j\lambda_j^+|a_j^+|^2+\sum_j\lambda_j^-|a_j^-|^2}{\sum_j|a_j^+|^2+\sum_j|a_j^-|^2},$$
即二次型是特征值以 $|a_j^\pm|^2$ 为权的**加权平均**。记右端为 $\mu_n$：

- **$\lambda_n^+\leqslant\mu_n$**：*因为* 任意 $V_{n-1}$ 与 $n$ 维空间 $\operatorname{span}\{e_1^+,\dots,e_n^+\}$ 必有非零交向量 $x_n\perp V_{n-1}$（*因为* 维数之和 $n-1+n>2n-1$ 超过 $\dim$ 限制，两者在 $n$ 维子空间内必相交），此时加权平均 $\geqslant\lambda_n^+$，取上确界得 $\mu_n\geqslant\lambda_n^+$。
- **$\lambda_n^+\geqslant\mu_n$**：取 $V_{n-1}=\operatorname{span}\{e_1^+,\dots,e_{n-1}^+\}$，则 $x\perp V_{n-1}$ 时加权平均 $\leqslant\lambda_n^+$，故 $\lambda_n^+\geqslant\mu_n$。$\square$

> **用途**：这是有限元方法与数值谱计算的理论依据——**不必求特征向量就能给出特征值的上下界**（Rayleigh 商逼近）。

**应用：积分方程求解（Fredholm 积分方程）**

考虑第二类 Fredholm 积分方程
$$x(t)-\int_a^bk(t,s)x(s)\,\mathrm ds=y(t),$$
其中核 $k$ 满足 $k(t,s)=\overline{k(s,t)}$（**对称核**）且 $k\in L^2([a,b]^2)$。由 5.4.1 的例题，积分算子
$$(Ax)(t)=\int_a^bk(t,s)x(s)\,\mathrm ds$$
是 $L^2[a,b]$ 上的紧算子；*因为* 核对称，$A$ 还是**自伴**的（直接交换积分次序即得 $\langle Ax,y\rangle=\langle x,Ay\rangle$）。于是：

1. **Fredholm 二择一**：方程 $x-Ax=y$ 对每个 $y$ 有唯一解 $\iff$ 齐次方程 $x=Ax$ 只有零解；
2. **若齐次方程有非零解**，则由谱结构定理，非零解集是**有限维**的（$\dim\ker(I-A)<\infty$），且其特征值 $\lambda_n$ 满足 $\lambda_n\to0$；
3. **谱分解给出解的显式形式**：把 $y$ 按 $A$ 的特征元 $\{e_n\}$ 展开 $y=\sum_n\langle y,e_n\rangle e_n$，则（当 $1$ 不是特征值时）
   $$x=y+\sum_{n=1}^\infty\frac{\lambda_n}{1-\lambda_n}\langle y,e_n\rangle e_n$$
   是方程的解。**验证**：*因为* $Ae_n=\lambda_ne_n$，
   $$(I-A)x=y+\sum_n\frac{\lambda_n}{1-\lambda_n}\langle y,e_n\rangle e_n-\sum_n\frac{\lambda_n^2}{1-\lambda_n}\langle y,e_n\rangle e_n=y+\sum_n\lambda_n\langle y,e_n\rangle e_n=y+Ay,$$
   即 $x-Ax=y$，且 *因为* $\lambda_n\to0$，$\dfrac{\lambda_n}{1-\lambda_n}\to0$，级数收敛。
4. **核的 Hilbert–Schmidt 展开**：*因为* 对称核的积分算子自伴紧，可写成
   $$k(t,s)=\sum_{n=1}^\infty\lambda_n e_n(t)\overline{e_n(s)},$$
   且 $\sum_n|\lambda_n|^2=\|k\|_{L^2}^2$（**这就是"Hilbert–Schmidt 定理"名字的来源**：它给出了核的谱展开与平方可和性）。

**例题**：设 $[a,b]=[0,1]$，核 $k(t,s)=\min(t,s)$。求积分算子 $(Ax)(t)=\int_0^1\min(t,s)x(s)\,\mathrm ds$ 的谱与算子范数，并写出核的 Hilbert–Schmidt 展开。

- **原始信息**：$k(t,s)=\min(t,s)$ 在 $[0,1]^2$ 上连续，故 $k\in L^2$；*因为* $k(t,s)=k(s,t)$，核对称，$A$ 自伴紧（由 5.4.1 例题）。
- **代入特征方程**：设 $Ax=\lambda x$，即
  $$(Ax)(t)=\int_0^ts\,x(s)\,\mathrm ds+t\int_t^1x(s)\,\mathrm ds=\lambda x(t).$$
  两边求导：*因为* 第一项求导给出 $t\,x(t)$，第二项求导给出 $\int_t^1x(s)\,\mathrm ds-t\,x(t)$，两项相加 $t x(t)$ 相消，得
  $$(Ax)'(t)=\int_t^1x(s)\,\mathrm ds.$$
  再求导得 $(Ax)''(t)=-x(t)$。
- **化为边值问题**：由 $Ax=\lambda x$ 得 $\lambda x''(t)=-x(t)$，即
  $$x''+\frac1\lambda x=0.$$
  边界条件：*因为* $(Ax)(0)=0$ 得 $x(0)=0$；*因为* $(Ax)'(1)=0$ 得 $x'(1)=0$。
- **解边值问题**：$x(t)=\sin\dfrac{t}{\sqrt\lambda}$（*因为* 通解为 $A\sin(t/\sqrt\lambda)+B\cos(t/\sqrt\lambda)$，$x(0)=0$ 迫使 $B=0$），由 $x'(1)=0$ 得
  $$\frac{1}{\sqrt\lambda}\cos\frac{1}{\sqrt\lambda}=0\Longrightarrow\frac{1}{\sqrt\lambda}=\left(n-\frac12\right)\pi,\qquad n=1,2,\dots$$
- **结果（谱与范数）**：
  $$\lambda_n=\frac{1}{\left(n-\frac12\right)^2\pi^2},\qquad e_n(t)=\sqrt2\,\sin\!\left(\left(n-\frac12\right)\pi t\right)\ (n\geqslant1),$$
  且 *因为* $\lambda_n>0$ 单调递减到 $0$，由命题（最大特征值）与谱分解，
  $$\|A\|=\lambda_1=\frac{4}{\pi^2}\approx0.4053.$$
- **核的展开**：由 Hilbert–Schmidt 展开，
  $$\min(t,s)=\sum_{n=1}^\infty\frac{2\sin\!\left(\left(n-\frac12\right)\pi t\right)\sin\!\left(\left(n-\frac12\right)\pi s\right)}{\left(n-\frac12\right)^2\pi^2},$$
  且
  $$\sum_{n=1}^\infty\lambda_n^2=\frac{1}{\pi^4}\sum_{n=1}^\infty\frac{1}{\left(n-\frac12\right)^4}=\frac{1}{\pi^4}\cdot\frac{\pi^4}{6}=\frac16,$$
  这与直接计算核的 $L^2$ 范数一致：*因为* 按 $t<s$ 与 $s<t$ 两块积分，
  $$\|k\|_{L^2}^2=\int_0^1\!\!\int_0^1\min(t,s)^2\,\mathrm ds\,\mathrm dt=\int_0^1t^2(1-t)\,\mathrm dt+\int_0^1\frac{t^3}{3}\,\mathrm dt=\frac1{12}+\frac1{12}=\frac16,$$
  **两边相等正是"$\sum_n\lambda_n^2=\|k\|_{L^2}^2$"这条 Hilbert–Schmidt 等式的具体验证**。
- **结论**：一个看起来平凡的核 $\min(t,s)$ 给出**恰好可数、单调趋于 $0$、全为正实数**的谱——这正是紧自伴算子谱的典型形状。它在微分方程中扮演"Green 函数"角色（对应 $-x''=\mu x$、$x(0)=x'(1)=0$ 的边值问题），**微分方程的特征值问题因此可以翻译成积分算子的谱问题**——这是 Fredholm 理论的原始动机。

> **这一节真正要说的是什么**：紧算子是**无穷维里唯一还"听话"的一类算子**——它把有界集压成列紧集，因此有限维的结论可以"取极限"搬过来：**紧算子 = 有限秩算子的极限**（5.4.1）、**Fredholm 二择一恢复成立**（5.4.2）、**自伴紧算子可以像对称矩阵一样对角化**（5.4.3）。代价只有一个：**$0$ 必然落在谱里，而且是唯一的聚点。**

---

## 去脉（学完去哪）

- **当代应用**：
  - **积分方程与边值问题**：第二类 Fredholm 方程的可解性完全由紧算子理论给出；Green 函数把微分方程边值问题化成积分方程，从而纳入同一框架。
  - **反问题与正则化**：紧算子的逆（若存在）必然无界，这是**反问题不适定**的根源；Tikhonov 正则化正是对 $\lambda_n$ 的小特征值方向做阻尼。
  - **数值方法**：有限元离散把无穷维紧算子截断为有限秩算子（矩阵），Rayleigh 商（极小极大刻画）给出特征值的上下界。
  - **统计与机器学习**：核矩阵的特征分解、主成分分析（PCA）、核主成分分析（KPCA）都是自伴紧算子谱分解的离散版本；**Mercer 定理**就是 Hilbert–Schmidt 展开在正定核上的形态。
  - **量子力学**：紧自伴算子 = 有离散能级的可观测量（束缚态）；$\lambda_n\to0$ 对应能级向连续谱堆积。
- **跨领域解读**：Hilbert–Schmidt 展开 $\sum_n\lambda_ne_n(t)\overline{e_n(s)}$ 在信号处理里就是"把核按正交基分解"，其系数 $\lambda_n$ 的衰减速率决定该核能否被低秩逼近——**这正是低秩近似与压缩感知的数学地基**。
- **高层视角**：本章到这里完成了 Hilbert 空间理论的完整闭环——**几何**（§5.2 投影与正交展开）、**算子**（§5.3 有界/共轭/投影）、**谱**（§5.4 紧算子的离散谱）。下一章（Ch6）回到只有范数的 Banach 空间：几何消失了（没有正交），必须靠 Hahn–Banach 定理、开映射定理、共鸣定理等"补丁"来替代——**这正好从反面说明内积带来了多少东西。**

## 防跳跃

- [ ] 定理 5.4.5 中 $(1)\Rightarrow(2)$、$(1)\Rightarrow(3)$ 的完整证明（构造有限秩逼近与 $A^*$ 紧性的论证）
- [ ] 引理 5.4.7（$T$ 闭值域 $\Rightarrow\overline{\mathcal R(T)}=\mathcal R(T)$）与引理 5.4.8（$\ker T=\{0\}\Rightarrow\mathcal R(T)=H$）的证明
- [ ] 定理 5.4.10 (2) 中"$\overline{\mathcal R(T)}=(\ker T^*)^\perp$"的推导
- [ ] 定理 5.4.10 (3) 中 $\dim\ker T=\dim\ker T^*$ 的构造细节（等距同构 $\widetilde V$ 与 $\widetilde V+T$ 的满射性）
- [ ] 命题 5.4.15（自伴紧算子存在 $|\lambda_1|=\|A\|$ 的特征值）的证明
- [ ] 一般（非自伴）紧算子的谱理论：Schauder 型定理、Riesz–Schauder 理论、指标（index）与 Fredholm 算子
- [ ] 核的 Hilbert–Schmidt 展开的收敛性（按 $L^2$ 收敛 vs 逐点收敛的条件差异，Mercer 定理需要核连续且正定）
- [ ] 例题中 $\sum_n\lambda_n^2=\|k\|_{L^2}^2$ 的精确数值（本例仅验证了收敛性，未算出和）
- [ ] 紧算子的谱半径与算子范数的关系：一般（非自伴）紧算子只有 $\lim_n\|\lambda_n\|^{1/n}$ 的估计，不保证 $\|A\|$ 是特征值

## 来源与映射

| 本节点内容 | 来源 | 处理 |
|---|---|---|
| 紧算子定义与三条等价刻画 | 郭版教材 §5.4.1 定义 5.4.1 | 新写补缺 |
| 紧算子基本性质（线性空间、$\subset\mathcal B$、闭子空间、理想性） | 郭版教材 §5.4.1 命题 5.4.2 | 新写补缺（含完整证明） |
| 反例：无穷维恒等算子有界不紧 | 郭版教材 §5.4.1（引理 5.4.9 的思想） | 新写补缺 |
| 有穷秩算子、秩 1 算子 $x\otimes y$、$F\subset\mathcal C$ | 旧《Ch8》§3 有限秩算子；郭版教材 §5.4.1 定义 5.4.3 | 迁移 + 新写（补 $x\otimes y$ 记号） |
| 有穷秩算子标准形定理与证明 | 郭版教材 §5.4.1 定理 5.4.4；旧《Ch8》§5.1 | 新写补缺（旧版只有陈述，无 Riesz 定理证明路径） |
| 定理：$A$ 紧 $\iff A\in\overline{F(H,K)}\iff A^*$ 紧 | 郭版教材 §5.4.1 定理 5.4.5 | 新写补缺 |
| 例题：Hilbert–Schmidt 型积分算子是紧算子 | 郭版教材 §5.4.1、§5.3.2 例（积分核算子） | 新写补缺 |
| 商空间定义、赋范与完备性、例子 | 旧《Ch8》§3 商空间（§5.2） | 原文迁移（限定于紧算子前奏的用途，一般理论指向 Ch6 §6.2） |
| 定理：$I+T$ 的值域闭（$T$ 有穷秩，商空间方法） | 旧《Ch8》§3 定理 3（§5.3） | 原文迁移 |
| 预解集、谱、点谱的定义与 $\sigma_p\subset\sigma$ | 郭版教材 §5.4.2 定义 5.4.6 | 新写补缺 |
| 引理：无穷维紧算子无有界逆 | 郭版教材 §5.4.2 引理 5.4.9 | 新写补缺（含完整证明） |
| 定理：$T=I-A$ 的四条基本性质 | 郭版教材 §5.4.2 定理 5.4.10 | 新写补缺 |
| **Fredholm 二中择一律** | 郭版教材 §5.4.2（式 5.4.10–5.4.11 后） | 新写补缺 |
| 反例：单向移位使二择一失效（紧性不可少） | 旧《Ch9》§5.4 单向移位；郭版教材 §5.4.2 注 | 新写（据旧反例改造为二择一失效的见证） |
| 引理：$\lambda\neq0$ 时下确界为 $0$ 蕴含特征值 | 郭版教材 §5.4.2 引理 5.4.11 | 新写补缺 |
| **紧算子的谱**（除 $0$ 外全是特征值、至多以 $0$ 为聚点） | 郭版教材 §5.4.2 定理 5.4.12 | 新写补缺（含 (3) 的线性无关性与反证构造） |
| 例题：$\|A\|<\tfrac12$ 时 $x=Ax+y$ 有唯一解 | 郭版教材 §5.4.2 定理 5.4.12 | 新写（据定理自编计算例） |
| 引理：正规算子特征子空间与可约化性 | 郭版教材 §5.4.3 引理 5.4.13 | 新写补缺 |
| 命题：自伴紧算子存在 $|\lambda_1|=\|A\|$ 的特征值 | 郭版教材 §5.4.3 命题 5.4.15 | 新写补缺 |
| **Hilbert–Schmidt 谱分解定理**（$A=\sum\lambda_nP_n$） | 郭版教材 §5.4.3 定理 5.4.16 | 新写补缺（含四步证明骨架） |
| 特征值的极小极大刻画 | 郭版教材 §5.4.3 定理 5.4.17 | 新写补缺 |
| 积分方程求解与核的 Hilbert–Schmidt 展开 | 郭版教材 §5.4.2–§5.4.3（Fredholm 积分方程） | 新写补缺 |
| 例题：核 $\min(t,s)$ 的谱与范数 | 郭版教材 §5.4.3 谱分解定理 | 新写（据定理自编计算例，与 Green 函数对应） |