Title: Learning the parameters of determinantal point process kernels
Date: 2015-06-29
Tags: dpp, kernel, learning
Slug: learn_params_dpp_kernels


This post summarizes this
[paper](http://stat.wharton.upenn.edu/~rajara/LearningParametricDPP.pdf):

    Learning the Parameters of Determinantal Point Process Kernels 
    R. H. Affandi, E. B. Fox, R. P. Adams and B. Taskar. 
    ICML 2014.

A determinantal point process (DPP) is a probability measure on the
$2^{N}$ possible subsets $A$ of a discrete set
$\Omega=\{x_{1},\ldots,x_{N}\}$:
$$P_{L}(A)=\frac{\det(L_{A})}{\det(L+I)}$$ where $L_{A}$ is a submatrix
of the $N\times N$ matrix $L$ indexed by the members in the set $A$.
Given a set of $T$ samples $S=\{A^{1},\ldots,A^{T}\}$, the parameters
$\theta$ of the kernel $L$ can be learned by performing a gradient
ascent on the log likelihood $\mathcal{L}(\theta)$:
$$\mathcal{L}(\theta)=\sum_{t=1}^{T}\log\det(L_{A^{t}})-T\log\det(L(\theta)+I).$$
When $N$ is large, however, computing the likelihood or the derivative
is inefficient. A Bayesian learning of DPPs relies on sampling techniqes
such as Metropolis-Hastings (MG) and slice sampling. In MH, we use a
proposal distribution $f(\hat{\theta}|\theta_{i})$ to generate a
candidate $\hat{\theta}$ given the current parameters $\theta_{i}$ which
are then accepted or rejected with probability $\min(1,r)$ where
$$r=\left(\frac{p\left(\hat{\theta}|S\right)f(\theta_{i}|\hat{\theta})}{p(\theta_{i}|S)f(\hat{\theta}|\theta_{i})}\right).$$
Notice that the normalizer $\det(L+I)$ depends on $\theta$ and does not
cancel out in the ratio in $r$. In fact, evaluation of the
normalizer[^1]
$\det(L(\theta)+I)=\prod_{n=1}^{\infty}(\lambda_{n}(\theta)+1)$ is
difficult. The main idea of @Affandi2014 is to use lower and upper
bounds of $p(\hat{\theta}|S)$ in place of $p(\hat{\theta}|S)$ in the MH
acceptance ratio.

$$\begin{aligned}
\text{lower bound: }\prod_{n=1}^{M}(1+\lambda_{n}) & \leq\prod_{n=1}^{\infty}(1+\lambda_{n}),\\
\text{upper bound: }\prod_{n=1}^{\infty}(1+\lambda_{n}) & \leq\exp\left\{ \mathrm{trace}(L)-\sum_{n=1}^{M}\lambda_{n}\right\} \left[\prod_{n=1}^{M}(1+\lambda_{n})\right],\end{aligned}$$

where $\mathop{\mathrm{tr}}(L)$ can be computed as either
$\sum_{i=1}^{N}L_{ii}$ in the discrete case or
$\int_{\Omega}L(x,x)\,\mathrm{d}x$ in the continuous case. In each MH
step, two quantities $r^{+}$ and $r^{-}$ are computed:
$$r^{+}=\left(\frac{p^{+}\left(\hat{\theta}|S\right)f(\theta_{i}|\hat{\theta})}{p^{-}(\theta_{i}|S)f(\hat{\theta}|\theta_{i})}\right),\thinspace\thinspace\thinspace\thinspace\thinspace\thinspace\thinspace\thinspace r^{-}=\left(\frac{p^{-}\left(\hat{\theta}|S\right)f(\theta_{i}|\hat{\theta})}{p^{+}(\theta_{i}|S)f(\hat{\theta}|\theta_{i})}\right).$$
If $u<\min(1,r^{-1})$ where $u\sim\text{Uniform}[0,1]$, the immediately
reject because it follows that $u<\min(1,r)$ as well. Similarly, if
$u>\min(1,r^{+})$, immediately accept the proposal. If
$u\in(r^{-},r^{+})$, then tighten the bounds until a decision can be
made. This idea is also applicable to the slice sampling.

[^1]: Here we consider $\Omega$ to be an uncountable set; hence, the
    operator $L$ has infinitely many eigenvalues.
