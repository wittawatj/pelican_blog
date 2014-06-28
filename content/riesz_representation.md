Title: Proof of Riesz Representation
Date: 2014-06-10
Tags: riesz, operator, hilbert
Slug: riesz_representation


Riesz representation is a theorem stating that in a Hilbert space
$\mathcal{F}$, every continuous linear functional $L:\mathcal{F}\rightarrow\mathbb{R}$
can be written as $Lf=\left\langle f,g\right\rangle _{\mathcal{F}}$
for a unique $g\in\mathcal{F}$.

*Proof*. Assume that the linear functional $L$ is continuous. For the
edge case where $Lf=0$ for all $f$, this is trivial because $Lf=\left\langle f,0\right\rangle $,
so $g=0$. If not, we know that the null space of $L$ i.e., $N=\{f\mid Lf=0\}=L^{-1}\left(\{0\}\right)$
is closed because a continuous operator maps a closed set to a closed
set i.e., $\{0\}$. Since $N$ is closed, the orthogonal complement
$N^{\perp}$ (subspace of elements orthogonal to $N$) contains elements
other than $0$ element. Consider $h\in N^{\perp}$ such that $\|h\|_{\mathcal{F}}=1$.
Consider $u_{f}=\left(Lf\right)h-\left(Lh\right)f\in N$ (i.e., $Lu_{f}=0$).
Since $h$ and $u_{f}$ are orthogonal by construction, we have
$$\begin{eqnarray*}
0 & = & \left\langle u_{f},h\right\rangle _{\mathcal{F}}\\
 & = & \left\langle \left(Lf\right)h-\left(Lh\right)f,h\right\rangle _{\mathcal{F}}\\
 & = & \left(Lf\right)\|h\|^{2}-\left(Lh\right)\left\langle f,h\right\rangle \\
 & = & Lf-\left\langle f,(Lh)h\right\rangle _{\mathcal{F}}\\
\Rightarrow Lf & = & \left\langle f,(Lh)h\right\rangle _{\mathcal{F}}.
\end{eqnarray*}$$
Hence, $g=\left(Lh\right)h$ for some $h\in N^{\perp}$. 

The element $g$ is unique. If there were $g_{1}$ and $g_{2}$, then
$0=|Lf-Lf|=|\left\langle f,g_{1}-g_{2}\right\rangle |\leq\|f\|\|g_{1}-g_{2}\|$
by Cauchy-Schwarz inequality. This implies $\|g_{1}-g_{2}\|=0$. Hence
$g_{1}=g_{2}$. Riesz representation is useful in establishing the
existence of a mean embedding in RKHS of a probability distribution.

Reference: [Dino Sejdinovic's teaching slides](http://www.gatsby.ucl.ac.uk/~dino/teaching.html)

