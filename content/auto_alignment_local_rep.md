Title: Automatic Alignment of Local Representations
Date: 2015-04-10
Slug: auto_alignment_local_rep
Tags: manifold, dimensionality reduction, eigenvalue


This post summarizes 

    Automatic Alignment of Local Representations (2003)
    Yee Whye Teh , Sam Roweis
    NIPS 2003. 

The [paper](http://www.stats.ox.ac.uk/~teh/research/llc/nips2002.pdf) proposes
a generic method to combine coordinates obtained from many dimensionality
reduction algorithms into one global coordinate, essentially “aligning” local
coordinates into a global one. The motivation of such a proposal starts from
the inability of linear methods (e.g., PCA) to capture the structure of curved
manifolds. A common way to deal with a curved manifold is to consider a mixture
of local dimensionality reducers. The idea is analogous to approximating a
curve with a piecewise linear function. The problem with this approach is that
there is no globally coherent coordinate because each local region has its own.

Proposal
--------

Assume that we are given a set of points
$\mathcal{X}=\left[x_{1},\ldots,x_{N}\right]^{\top}$ from
$D$-dimensional space sampled from a $d\ll D$ dimensional manifold. Let
$\mathcal{Y}=\left[y_{1},\ldots,y_{N}\right]^{\top}$ be the reduced
images of $\mathcal{X}$ in $d$ dimensional embedding space. Suppose that
we have already trained $K$ local dimensionality reducers, each
producing a representation $z_{nk}\in\mathbb{R}^{d_{k}}$ of point
$x_{n}$. Associated with each output $z_{nk}$ is a responsibity
$r_{nk}\geq0$ describing the reliability of the representation of
$x_{n}$ from the $k^{th}$ reducer. The algorithm aligns
$\{z_{nk}\}_{n,k}$ and $\{r_{nk}\}_{n,k}$ to produce $\mathcal{Y}$.

Assume that the global coordinate is a linear function of $z_{nk}$. The
paper proposes to obtain $\mathcal{Y}$ from

$$\begin{aligned}
y_{n} & =\sum_{k}r_{nk}(L_{k}z_{nk}+l_{k}^{0})=\sum_{k}\sum_{i=0}^{d_{k}}r_{nk}z_{nk}^{i}l_{k}^{i}=\sum_{j}u_{nj}l_{j},\end{aligned}$$

where $L_{k}=\left(l_{k}^{0}|\cdots|l_{k}^{d_{k}}\right)$ is a linear
projection associated with the $k^{th}$ reducer, and $l_{k}^{0}$ is an
offset. If we let $u_{nj}=r_{nk}z_{nk}^{i}$, $z_{nk}^{0}:=1$ and
vectorizing the indeces $(i,k)$ into $j$, we have $$\mathcal{Y}=UL,$$
which is a linear system with fixed $U$ and unknown $L$. To determine
$L$, the authors proposed to use a cost function $\mathcal{E}$ based on
the locally linear embedding
([LLE](https://www.cs.nyu.edu/~roweis/lle/)) algorithm:
$$\mathcal{E}(\mathcal{Y},W)=\sum_{n}\|x_{n}-\sum_{m\in\mathcal{N}_{n}}w_{nm}x_{m}\|^{2}=\mathrm{tr}(\mathcal{Y}^{\top}(I-W^{\top})(I-W)\mathcal{Y}),$$
where $\mathcal{N}_{n}$ is the set of nearest neighbours of $x_{n}$ and
$\sum_{m\in\mathcal{N}_{n}}w_{nm}=1$. The local linear reconstruction
weights $W$ are constructed by solving
$\min_{W}\mathcal{E}(\mathcal{X},W)$ subject to the normalization
constraint. With $W$ determined, $\mathcal{E}(\mathcal{Y},W)$ can be
solved by minimizing
$$\mathcal{E}(\mathcal{Y},W)=\mathrm{tr}\left[L^{\top}U^{\top}(I-W^{\top})(I-W)UL\right],$$
subject to two constraints,
$\frac{1}{N}\boldsymbol{1}^{\top}\mathcal{Y}=0$ and
$\frac{1}{N}\mathcal{Y}^{\top}\mathcal{Y}=I_{d}$ to break degeneracies.
Solving for $\mathcal{Y}$ now amounts to solving for $L$. The objective
together with the two constraints form a generalized eigenvalue problem
whose solution is given by the $2^{nd}$ to $(d+1)^{st}$ smallest
eigenvectors. The alignment problem has no local optima.
