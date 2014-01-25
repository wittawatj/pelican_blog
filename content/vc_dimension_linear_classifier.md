Title: VC Dimension of Linear Classifiers
Date: 2013-07-10
Slug: vc_dimension_linear_classifier
Tags: vc, linear


Let $d$ be the dimension of the input data and 
$\mathcal{H} = \{f ~|~ f(\boldsymbol{x}) = \text{sign}(\boldsymbol{w}^\top \boldsymbol{x} + b), 
b \in \mathbb{R} \}$ be the set of all linear classifiers.

<lemma>
$d_{VC}(\mathcal{H}) \geq d + 1$.
</lemma>

**Proof** 
We need to prove that $\mathcal{H}$ can shatter at least $d+1$ points. 
That is, it suffices to show that there exists a set of $d+1$ points such that $\mathcal{H}$ can produce
any pre-specified $\{-1, +1\}$ assignment $\boldsymbol{y} = (y_1, \ldots, y_{d+1})$.
Let $\begin{align}
\boldsymbol{X} &= \left[ \begin{array}{c} \boldsymbol{x}_1^\top \\ \vdots \\ \boldsymbol{x}_{d+1}^\top \end{array} \right] \\
 &= \left[ \begin{array}{ccccc} 
  1 & 0 & 0 & \cdots & 0 \\
  1 & 1 & 0 & \cdots & 0 \\
  1 & 0 & 1 & \cdots & 0 \\
    & \vdots & \vdots & \ddots & \vdots \\
  1 & 0 & 0 & \cdots & 1 
\end{array} \right]
\in \mathbb{R}^{d+1 \times d+1}
\end{align}$

The first coordinate of each $\boldsymbol{x}_i$ is 1 to allow the bias term $b$ to be produced. 
Note that $\boldsymbol{X}$ is invertible.
With this definition, for any $\boldsymbol{y}$ we can always have 
$\text{sign}(\boldsymbol{X} \boldsymbol{w}) = \boldsymbol{y}$ by choosing $\boldsymbol{w} = \boldsymbol{X}^{-1} \boldsymbol{y}$
since $\boldsymbol{X}\boldsymbol{w} = \boldsymbol{y}$ implies 
$\text{sign}(\boldsymbol{X} \boldsymbol{w}) = \boldsymbol{y}$.

<lemma>
$d_{VC}(\mathcal{H}) \leq d + 1$.
</lemma>

**Proof**
We need to show that no $d+2$ points can be shattered by $\mathcal{H}$. That is to show that
there exists a certain assignment $\boldsymbol{y} \in \mathbb{R}^{d+2}$ not achievable by $\mathcal{H}$. 
We will construct one such assignment.

Assume we have $d+2$ points
$\boldsymbol{x}_1, \ldots, \boldsymbol{x}_{d+2}$ in $(d+1)$-dimensional space. Then, the set is linearly
dependent. So, there exists $\boldsymbol{x}_j = \sum_{i\neq j} a_i \boldsymbol{x}_i$ such that not all
$a_i$ are 0. Set $y_j = -1$ and $y_i = \text{sign}(a_i) = \text{sign}(\boldsymbol{w}^\top \boldsymbol{x}_i)$
. If $a_i = 0$, $y_i$ can be arbitrary. 

$\text{sign}(\boldsymbol{w}^\top \boldsymbol{x}_j) = \text{sign}(\sum_{i \neq j} a_i \boldsymbol{w}^\top \boldsymbol{x}_i) > 0 \neq y_j$

Since there exists an assignment of $d+2$ points not achievable by $\mathcal{H}$, 
we can say that $d_{VC}(\mathcal{H}) \leq d + 1 $.

<theorem>
$d_{VC}(\mathcal{H}) = d + 1$.
</theorem>

**Proof**
Combining the two lemmas.

**Source**: 

* Lecture 7 on VC dimension by Professor Yaser Abu-Mostafa [here](http://work.caltech.edu/lectures.html). 
* See also the [previous post](/posts/2013-07-10-vc_dimension.html)  on VC dimension.
